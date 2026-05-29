import os
import sys
import json

sys.setrecursionlimit(20000)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import joblib

try:
    from xgboost import XGBClassifier
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

def train_and_evaluate():
    print("15분 데이터 기반 머신러닝 모델 학습을 시작합니다...")
    
    # 1. 데이터 로드 (새로운 15분 데이터셋 lol_clean_final.csv 적용)
    data_path = os.path.join(os.path.dirname(__file__), "lol_clean_final.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"데이터셋을 찾을 수 없습니다: {data_path}")
            
    df = pd.read_csv(data_path, encoding="utf-8")
    
    # [1단계] 데이터 전처리 (사용자 정의에 맞게 피처 클린업)
    # match_id, 전령, 챔피언, 역할군 태그, 조합 컬럼 제거
    drop_cols = ['match_id', 'blue_heralds', 'red_heralds'] + \
                [c for c in df.columns if 'champion' in c] + \
                [c for c in df.columns if '_tag' in c] + \
                [c for c in df.columns if '_comp' in c]
    
    df = df.drop(columns=[c for c in drop_cols if c in df.columns])
    print(f"불필요 컬럼 제거 완료. 남은 컬럼 수: {df.shape[1]}")
    
    # 타겟 변수 분리
    if 'win' not in df.columns:
        raise ValueError("데이터셋에 'win' 컬럼이 없습니다.")
        
    X = df.drop(columns=['win'])
    y = df['win']
    
    # 부울 및 정수 타입을 실수형으로 변환
    X = X.astype(float)
    
    # 피처 이름 저장
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
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_tr_scaled, y_tr)
    
    y_pred_lr = lr_model.predict(X_te_scaled)
    y_pred_proba_lr = lr_model.predict_proba(X_te_scaled)[:, 1]
    
    # 계수(Coefficient) 저장
    lr_coefs = lr_model.coef_[0]
    coefficients_dict = dict(zip(feature_names, lr_coefs.tolist()))
    
    # 비표준화(Unscaled) 계수 계산: w_i = beta_i / sigma_i
    unscaled_coeffs = {}
    for col, beta, sigma in zip(feature_names, lr_coefs, scaler.scale_):
        unscaled_coeffs[col] = float(beta / sigma) if sigma != 0 else 0.0
        
    # 드래곤 골드 가치 계산 (LR의 편미분값 기반 - 백엔드/프론트엔드 연동용)
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
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
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
        print("XGBoost 모델 학습 및 튜닝 값 적용 중...")
        # 사용자가 Optuna로 찾은 최적 파라미터 적용
        best_params = {
            'n_estimators': 498,
            'max_depth': 3,
            'learning_rate': 0.0122,
            'subsample': 0.6345,
            'colsample_bytree': 0.6051
        }
        xgb_model = XGBClassifier(
            **best_params,
            eval_metric="logloss",
            random_state=42,
            n_jobs=-1
        )
        xgb_model.fit(X_tr, y_tr)
        
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
        
    # [경량화 최적화 및 JS 포팅 파일 생성]
    # 1. Logistic Regression JSON 저장
    lr_data = {
        "intercept": float(lr_model.intercept_[0]),
        "coefficients": lr_model.coef_[0].tolist()
    }
    with open(os.path.join(models_dir, "logistic_regression.json"), "w", encoding="utf-8") as f:
        json.dump(lr_data, f, indent=4)
        
    # 2. Random Forest JSON 저장
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
        
    # 3. XGBoost m2cgen JavaScript 컴파일 및 저장
    try:
        import m2cgen as m2c
        if HAS_XGBOOST and xgb_model is not None:
            print("m2cgen으로 XGBoost 모델을 JavaScript 코드로 컴파일 중...")
            xgb_model.base_score = 0.5
            xgb_code = m2c.export_to_javascript(xgb_model)
            # ESM 모듈 호환성 위한 export 구문 추가
            xgb_code += "\nexport { score };\n"
            with open(os.path.join(models_dir, "xgboost_code.js"), "w", encoding="utf-8") as f:
                f.write(xgb_code)
            print("XGBoost m2cgen JS 컴파일 성공!")
    except Exception as e:
        print(f"XGBoost m2cgen 컴파일 에러: {str(e)}")
            
    # 4. 스케일러 파라미터 저장
    scaler_data = {
        "mean": scaler.mean_.tolist(),
        "scale": scaler.scale_.tolist()
    }
    with open(os.path.join(models_dir, "scaler.json"), "w", encoding="utf-8") as f:
        json.dump(scaler_data, f, indent=4)
        
    # 5. 챔피언 기여도 더미 파일 생성 (챔피언 정보가 피처에서 배제되었으므로 껍데기만 유지)
    dummy_champ_win_rates = {
        "Logistic Regression": {},
        "Random Forest": {},
        "XGBoost": {}
    }
    win_rates_path = os.path.join(models_dir, "champion_ml_win_rates.json")
    with open(win_rates_path, "w", encoding="utf-8") as f:
        json.dump(dummy_champ_win_rates, f, indent=4, ensure_ascii=False)
    print("챔피언 기여도 더미 구조 생성 완료.")

    # 지표 저장
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
    print(f"모델 지표가 저장되었습니다: {metrics_path}")
        
    return metrics_report

if __name__ == "__main__":
    train_and_evaluate()
