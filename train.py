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
    
    # 챔피언 이름 컬럼은 피처 공간이 너무 커지므로 모델 피처에서는 제거 (대신 태그와 조합 데이터 사용)
    champion_cols = [c for c in df.columns if 'champion' in c]
    df = df.drop(columns=champion_cols)
    
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
        
    # [Vercel 최적화] m2cgen을 사용하여 무의존성 순수 파이썬 모델 코드 컴파일
    try:
        import m2cgen as m2c
        print("m2cgen으로 순수 파이썬 모델 코드 컴파일 중...")
        
        # 1. Logistic Regression 컴파일
        lr_code = m2c.export_to_python(lr_model)
        with open(os.path.join(models_dir, "logistic_regression_code.py"), "w", encoding="utf-8") as f:
            f.write(lr_code)
            
        # 2. Random Forest 컴파일
        rf_code = m2c.export_to_python(rf_model)
        with open(os.path.join(models_dir, "random_forest_code.py"), "w", encoding="utf-8") as f:
            f.write(rf_code)
            
        # 3. XGBoost 컴파일
        if HAS_XGBOOST:
            xgb_model.base_score = 0.5
            xgb_code = m2c.export_to_python(xgb_model)
            with open(os.path.join(models_dir, "xgboost_code.py"), "w", encoding="utf-8") as f:
                f.write(xgb_code)
                
        # 4. 스케일러 파라미터 저장
        scaler_data = {
            "mean": scaler.mean_.tolist(),
            "scale": scaler.scale_.tolist()
        }
        with open(os.path.join(models_dir, "scaler.json"), "w", encoding="utf-8") as f:
            json.dump(scaler_data, f, indent=4)
            
        print("m2cgen 모델 컴파일 성공!")
    except Exception as e:
        print(f"m2cgen 컴파일 에러: {str(e)}")

    # 지표 저장
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
    print(f"모델 지표가 저장되었습니다: {metrics_path}")
        
    return metrics_report

if __name__ == "__main__":
    train_and_evaluate()

