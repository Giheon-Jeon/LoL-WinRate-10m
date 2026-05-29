import os
import sys
import json
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

sys.setrecursionlimit(20000)

try:
    from xgboost import XGBClassifier
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

try:
    import optuna
    HAS_OPTUNA = True
except ImportError:
    HAS_OPTUNA = False

def train_and_evaluate():
    print("15분 데이터 기반 고도화 머신러닝 모델 학습을 시작합니다...")
    
    # 1. 데이터 로드
    data_path = os.path.join(os.path.dirname(__file__), "lol_clean_final.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"데이터셋을 찾을 수 없습니다: {data_path}")
            
    df = pd.read_csv(data_path, encoding="utf-8")
    print(f"원천 데이터 로드 완료. 행 수: {df.shape[0]}, 열 수: {df.shape[1]}")
    
    # [공통 피처 엔지니어링: 상호작용 피처 생성]
    blue_gold_cols = [f'blue_{r}_gold' for r in ['top', 'jungle', 'middle', 'bottom', 'utility']]
    red_gold_cols = [f'red_{r}_gold' for r in ['top', 'jungle', 'middle', 'bottom', 'utility']]
    blue_total_gold = df[blue_gold_cols].sum(axis=1)
    red_total_gold = df[red_gold_cols].sum(axis=1)
    df['gold_ratio'] = blue_total_gold / (blue_total_gold + red_total_gold + 1e-5)
    df['gold_diff_total'] = blue_total_gold - red_total_gold

    blue_cs_cols = [f'blue_{r}_cs' for r in ['top', 'jungle', 'middle', 'bottom', 'utility']]
    red_cs_cols = [f'red_{r}_cs' for r in ['top', 'jungle', 'middle', 'bottom', 'utility']]
    blue_total_cs = df[blue_cs_cols].sum(axis=1)
    red_total_cs = df[red_cs_cols].sum(axis=1)
    df['cs_ratio'] = blue_total_cs / (blue_total_cs + red_total_cs + 1e-5)

    df['kills_ratio'] = df['blue_kills'] / (df['blue_kills'] + df['red_kills'] + 1e-5)
    df['dragons_diff'] = df['blue_dragons'] - df['red_dragons']
    df['towers_diff'] = df['blue_towers'] - df['red_towers']
    df['voidgrubs_diff'] = df['blue_voidgrubs'] - df['red_voidgrubs']
    
    # ----------------------------------------------------
    # [피처셋 1. 로지스틱 회귀용 피처셋 생성 (챔피언 멀티핫 + 태그/조합 원핫)]
    # ----------------------------------------------------
    print("로지스틱 회귀용 피처 인코딩 중...")
    df_lr = df.copy()
    
    # 유니크 챔피언 리스트 추출
    champions = set()
    for role in ['top', 'jungle', 'middle', 'bottom', 'utility']:
        champions.update(df_lr[f'blue_{role}_champion'].dropna().unique())
        champions.update(df_lr[f'red_{role}_champion'].dropna().unique())
    champions = sorted(list(champions))
    
    # 멀티핫 피처 데이터프레임 고속 생성
    blue_champ_data = {}
    red_champ_data = {}
    
    # 각 라인 챔피언 컬럼 모음
    blue_roles_champs = [df_lr[f'blue_{r}_champion'].values for r in ['top', 'jungle', 'middle', 'bottom', 'utility']]
    red_roles_champs = [df_lr[f'red_{r}_champion'].values for r in ['top', 'jungle', 'middle', 'bottom', 'utility']]
    
    for champ in champions:
        # 5개 라인 중 하나라도 매칭되면 1.0, 아니면 0.0
        blue_champ_data[f'blue_champion_{champ}'] = np.any([rc == champ for rc in blue_roles_champs], axis=0).astype(float)
        red_champ_data[f'red_champion_{champ}'] = np.any([rc == champ for rc in red_roles_champs], axis=0).astype(float)
        
    df_lr = pd.concat([df_lr, pd.DataFrame(blue_champ_data, index=df_lr.index), pd.DataFrame(red_champ_data, index=df_lr.index)], axis=1)

    # 태그 및 조합 원핫 인코딩
    tag_cols = [f'blue_{role}_tag' for role in ['top', 'jungle', 'middle', 'bottom', 'utility']] + \
               [f'red_{role}_tag' for role in ['top', 'jungle', 'middle', 'bottom', 'utility']]
    comp_cols = ['blue_comp', 'red_comp']
    df_lr = pd.get_dummies(df_lr, columns=tag_cols + comp_cols, dtype=float)

    # 텍스트 및 불필요 원천 컬럼 제거
    drop_cols_lr = ['match_id', 'blue_heralds', 'red_heralds'] + \
                   [f'blue_{role}_champion' for role in ['top', 'jungle', 'middle', 'bottom', 'utility']] + \
                   [f'red_{role}_champion' for role in ['top', 'jungle', 'middle', 'bottom', 'utility']]
    df_lr = df_lr.drop(columns=[c for c in drop_cols_lr if c in df_lr.columns], errors='ignore')
    
    X_lr = df_lr.drop(columns=['win'])
    y_lr = df_lr['win'].astype(int)
    
    # ----------------------------------------------------
    # [피처셋 2. 트리 모델용 피처셋 생성 (수치형 + 상호작용 피처만 활용, 챔피언 배제)]
    # ----------------------------------------------------
    print("트리 모델용 피처 인코딩 중...")
    df_tree = df.copy()
    drop_cols_tree = ['match_id', 'blue_heralds', 'red_heralds'] + \
                      [c for c in df_tree.columns if 'champion' in c] + \
                      [c for c in df_tree.columns if '_tag' in c] + \
                      [c for c in df_tree.columns if '_comp' in c]
    df_tree = df_tree.drop(columns=[c for c in drop_cols_tree if c in df_tree.columns], errors='ignore')
    
    X_tree = df_tree.drop(columns=['win'])
    y_tree = df_tree['win'].astype(int)

    # ----------------------------------------------------
    # 3. 모델 파일 저장 경로 및 피처 이름 저장
    # ----------------------------------------------------
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    
    feature_names_lr = list(X_lr.columns)
    feature_names_tree = list(X_tree.columns)
    
    with open(os.path.join(models_dir, "feature_names.json"), "w", encoding="utf-8") as f:
        json.dump(feature_names_lr, f, indent=4, ensure_ascii=False)
        
    with open(os.path.join(models_dir, "feature_names_tree.json"), "w", encoding="utf-8") as f:
        json.dump(feature_names_tree, f, indent=4, ensure_ascii=False)
        
    print(f"로지스틱 피처 수: {len(feature_names_lr)}, 트리 피처 수: {len(feature_names_tree)}")

    # ----------------------------------------------------
    # 4. 데이터셋 분할 및 학습 시작
    # ----------------------------------------------------
    # 동일한 random_state와 stratify로 분할하여 동일 인덱스 보장
    X_tr_lr, X_te_lr, y_tr_lr, y_te_lr = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42, stratify=y_lr)
    X_tr_tree, X_te_tree, y_tr_tree, y_te_tree = train_test_split(X_tree, y_tree, test_size=0.2, random_state=42, stratify=y_tree)
    
    # StandardScaler (로지스틱 회귀에만 적용)
    scaler = StandardScaler()
    X_tr_scaled_lr = scaler.fit_transform(X_tr_lr)
    X_te_scaled_lr = scaler.transform(X_te_lr)
    
    metrics_report = {}
    
    # --- [모델 1] Logistic Regression ---
    print("Logistic Regression 모델 학습 중...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_tr_scaled_lr, y_tr_lr)
    
    y_pred_lr = lr_model.predict(X_te_scaled_lr)
    y_pred_proba_lr = lr_model.predict_proba(X_te_scaled_lr)[:, 1]
    
    coefficients_dict = dict(zip(feature_names_lr, lr_model.coef_[0].tolist()))
    
    # 비표준화 계수 계산
    unscaled_coeffs = {}
    for col, beta, sigma in zip(feature_names_lr, lr_model.coef_[0], scaler.scale_):
        unscaled_coeffs[col] = float(beta / sigma) if sigma != 0 else 0.0
        
    tn_lr, fp_lr, fn_lr, tp_lr = confusion_matrix(y_te_lr, y_pred_lr).ravel()
    
    metrics_report["Logistic Regression"] = {
        "Accuracy": float(accuracy_score(y_te_lr, y_pred_lr)),
        "Precision": float(precision_score(y_te_lr, y_pred_lr)),
        "Recall": float(recall_score(y_te_lr, y_pred_lr)),
        "F1-Score": float(f1_score(y_te_lr, y_pred_lr)),
        "ROC-AUC": float(roc_auc_score(y_te_lr, y_pred_proba_lr)),
        "Confusion_Matrix": {
            "TN": int(tn_lr), "FP": int(fp_lr), "FN": int(fn_lr), "TP": int(tp_lr)
        },
        "Coefficients": coefficients_dict,
        "Unscaled_Coefficients": unscaled_coeffs,
        "Dragon_Gold_Value": 1500.0
    }
    print(f"[Logistic Regression] 정확도: {metrics_report['Logistic Regression']['Accuracy']:.4f}")

    # --- [모델 2] Random Forest ---
    print("Random Forest 모델 학습 중...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1, max_depth=10)
    rf_model.fit(X_tr_tree, y_tr_tree)
    
    y_pred_rf = rf_model.predict(X_te_tree)
    y_pred_proba_rf = rf_model.predict_proba(X_te_tree)[:, 1]
    
    rf_importances = rf_model.feature_importances_
    rf_importances_dict = dict(zip(feature_names_tree, rf_importances.tolist()))
    
    tn_rf, fp_rf, fn_rf, tp_rf = confusion_matrix(y_te_tree, y_pred_rf).ravel()
    
    metrics_report["Random Forest"] = {
        "Accuracy": float(accuracy_score(y_te_tree, y_pred_rf)),
        "Precision": float(precision_score(y_te_tree, y_pred_rf)),
        "Recall": float(recall_score(y_te_tree, y_pred_rf)),
        "F1-Score": float(f1_score(y_te_tree, y_pred_rf)),
        "ROC-AUC": float(roc_auc_score(y_te_tree, y_pred_proba_rf)),
        "Confusion_Matrix": {
            "TN": int(tn_rf), "FP": int(fp_rf), "FN": int(fn_rf), "TP": int(tp_rf)
        },
        "Feature_Importances": rf_importances_dict
    }
    print(f"[Random Forest] 정확도: {metrics_report['Random Forest']['Accuracy']:.4f}")

    # --- [모델 3] XGBoost (Optuna 자동 튜닝 적용) ---
    xgb_model = None
    best_params = {
        'n_estimators': 150,
        'max_depth': 3,
        'learning_rate': 0.05,
        'subsample': 0.7,
        'colsample_bytree': 0.7
    }
    
    if HAS_XGBOOST:
        if HAS_OPTUNA:
            print("Optuna로 XGBoost 하이퍼파라미터 최적값 탐색을 시작합니다...")
            def objective(trial):
                params = {
                    'n_estimators': trial.suggest_int('n_estimators', 50, 150),
                    'max_depth': trial.suggest_int('max_depth', 2, 4),
                    'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.1, log=True),
                    'subsample': trial.suggest_float('subsample', 0.6, 0.8),
                    'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 0.8),
                    'eval_metric': 'logloss',
                    'random_state': 42,
                    'n_jobs': -1
                }
                
                clf = XGBClassifier(**params)
                cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
                scores = cross_val_score(clf, X_tr_tree, y_tr_tree, cv=cv, scoring='accuracy', n_jobs=-1)
                return float(np.mean(scores))
                
            optuna.logging.set_verbosity(optuna.logging.WARNING)
            study = optuna.create_study(direction='maximize')
            study.optimize(objective, n_trials=20)
            best_params = study.best_params
            print(f"Optuna 최적 파라미터 도출 완료: {best_params}")
        else:
            print("Optuna가 존재하지 않아 기본 파라미터로 XGBoost를 학습합니다.")
            
        print("최종 XGBoost 모델 학습 중...")
        xgb_model = XGBClassifier(
            **best_params,
            eval_metric="logloss",
            random_state=42,
            n_jobs=-1
        )
        xgb_model.fit(X_tr_tree, y_tr_tree)
        
        y_pred_xgb = xgb_model.predict(X_te_tree)
        y_pred_proba_xgb = xgb_model.predict_proba(X_te_tree)[:, 1]
        
        xgb_importances = xgb_model.feature_importances_
        xgb_importances_dict = dict(zip(feature_names_tree, xgb_importances.tolist()))
        
        tn_xgb, fp_xgb, fn_xgb, tp_xgb = confusion_matrix(y_te_tree, y_pred_xgb).ravel()
        
        metrics_report["XGBoost"] = {
            "Accuracy": float(accuracy_score(y_te_tree, y_pred_xgb)),
            "Precision": float(precision_score(y_te_tree, y_pred_xgb)),
            "Recall": float(recall_score(y_te_tree, y_pred_xgb)),
            "F1-Score": float(f1_score(y_te_tree, y_pred_xgb)),
            "ROC-AUC": float(roc_auc_score(y_te_tree, y_pred_proba_xgb)),
            "Confusion_Matrix": {
                "TN": int(tn_xgb), "FP": int(fp_xgb), "FN": int(fn_xgb), "TP": int(tp_xgb)
            },
            "Feature_Importances": xgb_importances_dict,
            "Best_Params": best_params
        }
        print(f"[XGBoost] 정확도: {metrics_report['XGBoost']['Accuracy']:.4f}")
    else:
        print("XGBoost가 설치되어 있지 않아 건너뜁니다.")

    # ----------------------------------------------------
    # 5. 경량화 최적화 및 JS/JSON 포팅 파일 생성
    # ----------------------------------------------------
    # 1) Logistic Regression JSON 저장
    lr_data = {
        "intercept": float(lr_model.intercept_[0]),
        "coefficients": lr_model.coef_[0].tolist()
    }
    with open(os.path.join(models_dir, "logistic_regression.json"), "w", encoding="utf-8") as f:
        json.dump(lr_data, f, indent=4)
        
    # 2) Random Forest JSON 저장
    rf_trees = []
    for dt in rf_model.estimators_:
        tree = dt.tree_
        nodes = []
        for i in range(tree.node_count):
            if tree.children_left[i] == -1: # Leaf node
                val = tree.value[i][0]
                prob_1 = val[1] / (val[0] + val[1]) if (val[0] + val[1]) > 0 else 0.0
                nodes.append(float(prob_1))
            else: # Split node
                nodes.append([
                    int(tree.feature[i]),
                    float(tree.threshold[i]),
                    int(tree.children_left[i]),
                    int(tree.children_right[i])
                ])
        rf_trees.append(nodes)
    with open(os.path.join(models_dir, "random_forest.json"), "w", encoding="utf-8") as f:
        json.dump(rf_trees, f)
        
    # 3) XGBoost m2cgen JavaScript 컴파일 및 저장
    try:
        import m2cgen as m2c
        if HAS_XGBOOST and xgb_model is not None:
            print("m2cgen으로 XGBoost 모델을 JavaScript 코드로 컴파일 중...")
            xgb_model.base_score = 0.5
            xgb_code = m2c.export_to_javascript(xgb_model)
            xgb_code += "\nexport { score };\n"
            with open(os.path.join(models_dir, "xgboost_code.js"), "w", encoding="utf-8") as f:
                f.write(xgb_code)
            print("XGBoost m2cgen JS 컴파일 성공!")
    except Exception as e:
        print(f"XGBoost m2cgen 컴파일 에러: {str(e)}")
            
    # 4) 스케일러 파라미터 저장
    scaler_data = {
        "mean": scaler.mean_.tolist(),
        "scale": scaler.scale_.tolist()
    }
    with open(os.path.join(models_dir, "scaler.json"), "w", encoding="utf-8") as f:
        json.dump(scaler_data, f, indent=4)
        
    # 5) 챔피언 기여도 데이터 생성 (더미 탈피, 실제 Coefficient 기반 역산)
    champion_win_rates = {}
    for col, coef in zip(X_lr.columns, lr_model.coef_[0]):
        if col.startswith("blue_champion_"):
            champ_name = col.replace("blue_champion_", "")
            champion_win_rates[champ_name] = float(coef)
            
    champ_ml_win_rates = {
        "Logistic Regression": champion_win_rates,
        "Random Forest": {},
        "XGBoost": {}
    }
    with open(os.path.join(models_dir, "champion_ml_win_rates.json"), "w", encoding="utf-8") as f:
        json.dump(champ_ml_win_rates, f, indent=4, ensure_ascii=False)
    print("챔피언 기여도 분석 데이터 생성 완료.")

    # 6) 지표 저장
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
    print(f"모델 지표가 저장되었습니다: {metrics_path}")
        
    return metrics_report

if __name__ == "__main__":
    train_and_evaluate()
