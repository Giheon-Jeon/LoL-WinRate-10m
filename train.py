import os
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import joblib

# XGBoost 로드 시도
try:
    from xgboost import XGBClassifier
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

def train_and_evaluate():
    print("머신러닝 모델 학습을 시작합니다...")
    
    # 1. 데이터 로드 (새로운 데이터셋 적용)
    data_path = os.path.join(os.path.dirname(__file__), "lol_clean_final.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"데이터셋을 찾을 수 없습니다: {data_path}")
            
    df = pd.read_csv(data_path)
    
    # [1단계] 데이터 전처리
    # 불필요 컬럼 제거 (매치 ID)
    if 'match_id' in df.columns:
        df = df.drop(columns=['match_id'])
    
    # 챔피언 이름 컬럼을 기반으로 블루/레드 팀별 챔피언 멀티핫 피처 생성
    blue_champion_cols = ['blue_top_champion', 'blue_jungle_champion', 'blue_middle_champion', 'blue_bottom_champion', 'blue_utility_champion']
    red_champion_cols = ['red_top_champion', 'red_jungle_champion', 'red_middle_champion', 'red_bottom_champion', 'red_utility_champion']
    
    all_champions = set()
    for col in blue_champion_cols + red_champion_cols:
        if col in df.columns:
            all_champions.update(df[col].dropna().unique())
    all_champions = sorted(list(all_champions))
    
    # 성능 최적화를 위해 각 행의 챔피언들을 set으로 사전 변환
    blue_champs_sets = df[blue_champion_cols].apply(lambda row: set(row.dropna().values), axis=1)
    red_champs_sets = df[red_champion_cols].apply(lambda row: set(row.dropna().values), axis=1)
    
    # DataFrame 파편화 방지를 위해 딕셔너리로 취합 후 일괄 concat
    champ_features = {}
    for champ in all_champions:
        champ_features[f'blue_champion_{champ}'] = blue_champs_sets.apply(lambda s: 1.0 if champ in s else 0.0)
        champ_features[f'red_champion_{champ}'] = red_champs_sets.apply(lambda s: 1.0 if champ in s else 0.0)
        
    champ_df = pd.DataFrame(champ_features, index=df.index)
    df = pd.concat([df, champ_df], axis=1)
    
    # 원본 챔피언명 컬럼들 제거
    existing_champion_cols = [c for c in blue_champion_cols + red_champion_cols if c in df.columns]
    df = df.drop(columns=existing_champion_cols)
    
    # 문자열 컬럼 (태그, 조합 등) 원핫 인코딩
    categorical_cols = [c for c in df.columns if 'tag' in c or 'comp' in c]
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    # 타겟 변수 분리
    if 'win' not in df.columns:
        raise ValueError("데이터셋에 'win' 컬럼이 없습니다.")
        
    X = df.drop(columns=['win'])
    y = df['win']
    
    # 부울(Boolean) 및 정수 타입을 실수(float)형으로 변환
    X = X.astype(float)
    
    # 피처 이름 저장 (추후 백엔드 API에서 입력 맵핑 시 사용)
    feature_names = list(X.columns)
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, "feature_names.json"), "w", encoding="utf-8") as f:
        json.dump(feature_names, f, indent=4, ensure_ascii=False)
    print(f"총 {len(feature_names)}개의 피처 이름이 저장되었습니다.")

    # 학습/테스트 데이터 분할 (80:20 비율, 클래스 비율 유지)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # 피처 스케일링 (로지스틱 회귀에 사용)
    scaler = StandardScaler()
    X_tr_scaled = scaler.fit_transform(X_tr)
    X_te_scaled = scaler.transform(X_te)
    joblib.dump(scaler, os.path.join(models_dir, "scaler.joblib"))
    print("StandardScaler 학습 및 저장 완료.")

    metrics_report = {}
    
    # --- 2단계. 베이스라인 모델: Logistic Regression ---
    print("Logistic Regression 모델 학습 중...")
    lr_model = LogisticRegression(max_iter=2000, random_state=42)
    lr_model.fit(X_tr_scaled, y_tr)
    
    y_pred_lr = lr_model.predict(X_te_scaled)
    y_pred_proba_lr = lr_model.predict_proba(X_te_scaled)[:, 1]
    
    # 계수(Coefficient) 및 해석 준비
    lr_coefs = lr_model.coef_[0]
    coefficients_dict = dict(zip(feature_names, lr_coefs.tolist()))
    
    # 비표준화(Unscaled) 계수 계산: w_i = beta_i / sigma_i
    unscaled_coeffs = {}
    for col, beta, sigma in zip(feature_names, lr_coefs, scaler.scale_):
        unscaled_coeffs[col] = float(beta / sigma) if sigma != 0 else 0.0
        
    # 드래곤 골드 가치는 백엔드에서 편미분으로 계산하므로 여기서는 기본값 처리
    dragon_gold_value = 1500.0
    
    tn_lr, fp_lr, fn_lr, tp_lr = confusion_matrix(y_te, y_pred_lr).ravel()
    
    metrics_report["Logistic Regression"] = {
        "Accuracy": float(accuracy_score(y_te, y_pred_lr)),
        "Precision": float(precision_score(y_te, y_pred_lr)),
        "Recall": float(recall_score(y_te, y_pred_lr)),
        "F1-Score": float(f1_score(y_te, y_pred_lr)),
        "ROC-AUC": float(roc_auc_score(y_te, y_pred_proba_lr)),
        "Confusion_Matrix": {
            "TN": int(tn_lr), "FP": int(fp_lr), "FN": int(fn_lr), "TP": int(tp_lr)
        },
        "Coefficients": coefficients_dict,
        "Unscaled_Coefficients": unscaled_coeffs,
        "Dragon_Gold_Value": dragon_gold_value
    }
    joblib.dump(lr_model, os.path.join(models_dir, "logistic_regression.joblib"))
    print(f"[Logistic Regression] 정확도: {metrics_report['Logistic Regression']['Accuracy']:.4f}")

    # --- 3단계. 비교 모델: Random Forest ---
    print("Random Forest 모델 학습 중...")
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    rf_model.fit(X_tr, y_tr)
    
    y_pred_rf = rf_model.predict(X_te)
    y_pred_proba_rf = rf_model.predict_proba(X_te)[:, 1]
    
    rf_importances = rf_model.feature_importances_
    rf_importances_dict = dict(zip(feature_names, rf_importances.tolist()))
    
    tn_rf, fp_rf, fn_rf, tp_rf = confusion_matrix(y_te, y_pred_rf).ravel()
    
    metrics_report["Random Forest"] = {
        "Accuracy": float(accuracy_score(y_te, y_pred_rf)),
        "Precision": float(precision_score(y_te, y_pred_rf)),
        "Recall": float(recall_score(y_te, y_pred_rf)),
        "F1-Score": float(f1_score(y_te, y_pred_rf)),
        "ROC-AUC": float(roc_auc_score(y_te, y_pred_proba_rf)),
        "Confusion_Matrix": {
            "TN": int(tn_rf), "FP": int(fp_rf), "FN": int(fn_rf), "TP": int(tp_rf)
        },
        "Feature_Importances": rf_importances_dict
    }
    joblib.dump(rf_model, os.path.join(models_dir, "random_forest.joblib"))
    print(f"[Random Forest] 정확도: {metrics_report['Random Forest']['Accuracy']:.4f}")

    # --- 4단계. 최적화 모델: XGBoost ---
    xgb_model = None
    if HAS_XGBOOST:
        print("XGBoost 모델 학습 및 튜닝 중...")
        xgb_base = XGBClassifier(random_state=42, eval_metric="logloss")
        xgb_param_grid = {
            'n_estimators': [50, 100],
            'max_depth': [3, 5],
            'learning_rate': [0.05, 0.1]
        }
        xgb_grid = GridSearchCV(xgb_base, xgb_param_grid, cv=3, scoring='accuracy', n_jobs=-1)
        xgb_grid.fit(X_tr, y_tr)
        
        xgb_model = xgb_grid.best_estimator_
        best_params = xgb_grid.best_params_
        print(f"XGBoost 최적 파라미터: {best_params}")
        
        y_pred_xgb = xgb_model.predict(X_te)
        y_pred_proba_xgb = xgb_model.predict_proba(X_te)[:, 1]
        
        xgb_importances = xgb_model.feature_importances_
        xgb_importances_dict = dict(zip(feature_names, xgb_importances.tolist()))
        
        tn_xgb, fp_xgb, fn_xgb, tp_xgb = confusion_matrix(y_te, y_pred_xgb).ravel()
        
        metrics_report["XGBoost"] = {
            "Accuracy": float(accuracy_score(y_te, y_pred_xgb)),
            "Precision": float(precision_score(y_te, y_pred_xgb)),
            "Recall": float(recall_score(y_te, y_pred_xgb)),
            "F1-Score": float(f1_score(y_te, y_pred_xgb)),
            "ROC-AUC": float(roc_auc_score(y_te, y_pred_proba_xgb)),
            "Confusion_Matrix": {
                "TN": int(tn_xgb), "FP": int(fp_xgb), "FN": int(fn_xgb), "TP": int(tp_xgb)
            },
            "Feature_Importances": xgb_importances_dict,
            "Best_Params": best_params
        }
        joblib.dump(xgb_model, os.path.join(models_dir, "xgboost.joblib"))
        print(f"[XGBoost] 정확도: {metrics_report['XGBoost']['Accuracy']:.4f}")
    else:
        print("XGBoost가 설치되어 있지 않아 건너뜁니다.")
        
    # [경량화 최적화]
    # 1. Logistic Regression JSON 저장
    lr_data = {
        "intercept": float(lr_model.intercept_[0]),
        "coefficients": lr_model.coef_[0].tolist()
    }
    with open(os.path.join(models_dir, "logistic_regression.json"), "w", encoding="utf-8") as f:
        json.dump(lr_data, f, indent=4)
        
    # 2. Random Forest JSON 저장 (트리 구조 컴팩트화)
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
        json.dump(rf_trees, f) # No indent to save size
        
    # 3. XGBoost는 m2cgen 컴파일 유지 (코드 크기 64KB 수준으로 경량)
    try:
        import m2cgen as m2c
        if HAS_XGBOOST and xgb_model is not None:
            print("m2cgen으로 XGBoost 모델 코드 컴파일 중...")
            xgb_model.base_score = 0.5
            xgb_code = m2c.export_to_python(xgb_model)
            with open(os.path.join(models_dir, "xgboost_code.py"), "w", encoding="utf-8") as f:
                f.write(xgb_code)
            print("XGBoost m2cgen 모델 컴파일 성공!")
    except Exception as e:
        print(f"XGBoost m2cgen 컴파일 에러: {str(e)}")
            
    # 4. 스케일러 파라미터 저장
    scaler_data = {
        "mean": scaler.mean_.tolist(),
        "scale": scaler.scale_.tolist()
    }
    with open(os.path.join(models_dir, "scaler.json"), "w", encoding="utf-8") as f:
        json.dump(scaler_data, f, indent=4)
        
    # 5. 챔피언 기여도 기반 동적 승률 계산
    calculate_champ_ml_win_rates(lr_model, rf_model, xgb_model, scaler, feature_names, all_champions, models_dir)

    # 지표 저장
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
    print(f"모델 지표가 저장되었습니다: {metrics_path}")
        
    return metrics_report

def calculate_champ_ml_win_rates(lr_model, rf_model, xgb_model, scaler, feature_names, all_champions, models_dir):
    """
    모든 피처가 0인 가상 중립 상태에서 특정 챔피언 기여도(멀티핫=1.0)를 주었을 때의 블루팀 승률을 추출하여 저장
    """
    print("3대 알고리즘별 챔피언 기본 승률 예측 및 추출 중...")
    champ_win_rates = {
        "Logistic Regression": {},
        "Random Forest": {},
        "XGBoost": {}
    }
    
    # 모든 피처가 0.0인 1행짜리 기본 DataFrame 생성
    neutral_row = pd.DataFrame(0.0, index=[0], columns=feature_names)
    
    for champ in all_champions:
        # 블루팀에 해당 챔피언 투입
        champ_row = neutral_row.copy()
        blue_champ_col = f'blue_champion_{champ}'
        if blue_champ_col in champ_row.columns:
            champ_row[blue_champ_col] = 1.0
            
        # 1. Logistic Regression 예측
        champ_row_scaled = scaler.transform(champ_row)
        lr_prob = lr_model.predict_proba(champ_row_scaled)[0][1]
        champ_win_rates["Logistic Regression"][champ] = float(lr_prob)
        
        # 2. Random Forest 예측
        rf_prob = rf_model.predict_proba(champ_row)[0][1]
        champ_win_rates["Random Forest"][champ] = float(rf_prob)
        
        # 3. XGBoost 예측
        if HAS_XGBOOST and xgb_model is not None:
            xgb_prob = xgb_model.predict_proba(champ_row)[0][1]
            champ_win_rates["XGBoost"][champ] = float(xgb_prob)
        else:
            champ_win_rates["XGBoost"][champ] = float(rf_prob)
            
    # 결과를 JSON 파일로 저장
    win_rates_path = os.path.join(models_dir, "champion_ml_win_rates.json")
    with open(win_rates_path, "w", encoding="utf-8") as f:
        json.dump(champ_win_rates, f, indent=4, ensure_ascii=False)
    print(f"머신러닝 기반 챔피언 동적 승률이 저장되었습니다: {win_rates_path}")

if __name__ == "__main__":
    train_and_evaluate()
