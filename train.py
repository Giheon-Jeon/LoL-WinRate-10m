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

# Optional model imports with safe fallback
try:
    from xgboost import XGBClassifier
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

def train_and_evaluate():
    print("Starting ML Model training process...")
    
    # 1. 데이터 로드
    data_path = os.path.join(os.path.dirname(__file__), "high_diamond_ranked_10min.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at: {data_path}")
            
    df = pd.read_csv(data_path)
    
    # [1단계] 데이터 전처리
    # 불필요 컬럼 제거 (gameId)
    if 'gameId' in df.columns:
        df = df.drop(columns=['gameId'])
    
    # 중복 피처 정리 (레드팀의 Gold Diff, Exp Diff 컬럼 제거하여 다중공선성 방지)
    cols_to_drop = ['redGoldDiff', 'redExperienceDiff']
    for col in cols_to_drop:
        if col in df.columns:
            df = df.drop(columns=[col])
            print(f"Dropped collinear column: {col}")
            
    X = df.drop(columns=['blueWins'])
    y = df['blueWins']
    
    # feature names 저장
    feature_names = list(X.columns)
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, "feature_names.json"), "w", encoding="utf-8") as f:
        json.dump(feature_names, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(feature_names)} feature names.")

    # 학습/테스트 데이터 분할 (80:20 비율, stratify 적용)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # 피처 스케일링 (로지스틱 회귀에만 적용)
    scaler = StandardScaler()
    X_tr_scaled = scaler.fit_transform(X_tr)
    X_te_scaled = scaler.transform(X_te)
    joblib.dump(scaler, os.path.join(models_dir, "scaler.joblib"))
    print("StandardScaler trained and saved.")

    metrics_report = {}
    
    # --- 2단계. 베이스라인 모델: Logistic Regression ---
    print("Training Logistic Regression...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_tr_scaled, y_tr)
    
    y_pred_lr = lr_model.predict(X_te_scaled)
    y_pred_proba_lr = lr_model.predict_proba(X_te_scaled)[:, 1]
    
    # 계수(Coefficient) 및 해석 준비
    lr_coefs = lr_model.coef_[0]
    coefficients_dict = dict(zip(feature_names, lr_coefs.tolist()))
    
    # 비표준화(Unscaled) 계수 계산: w_i = beta_i / sigma_i
    unscaled_coeffs = {}
    for col, beta, sigma in zip(feature_names, lr_coefs, scaler.scale_):
        unscaled_coeffs[col] = float(beta / sigma)
        
    # 드래곤 1마리의 골드 가치 환산 (blueDragons vs blueGoldDiff)
    # 1 Dragon = w_dragon / w_gold_diff gold units
    w_dragon = unscaled_coeffs.get('blueDragons', 0)
    w_gold_diff = unscaled_coeffs.get('blueGoldDiff', 1)
    dragon_gold_value = float(w_dragon / w_gold_diff) if w_gold_diff != 0 else 0.0
    
    tn_lr, fp_lr, fn_lr, tp_lr = confusion_matrix(y_te, y_pred_lr).ravel()
    
    metrics_report["Logistic Regression"] = {
        "Accuracy": float(accuracy_score(y_te, y_pred_lr)),
        "Precision": float(precision_score(y_te, y_pred_lr)),
        "Recall": float(recall_score(y_te, y_pred_lr)),
        "F1-Score": float(f1_score(y_te, y_pred_lr)),
        "ROC-AUC": float(roc_auc_score(y_te, y_pred_proba_lr)),
        "Confusion_Matrix": {
            "TN": int(tn_lr),
            "FP": int(fp_lr),
            "FN": int(fn_lr),
            "TP": int(tp_lr)
        },
        "Coefficients": coefficients_dict,
        "Unscaled_Coefficients": unscaled_coeffs,
        "Dragon_Gold_Value": dragon_gold_value
    }
    joblib.dump(lr_model, os.path.join(models_dir, "logistic_regression.joblib"))
    print(f"[Logistic Regression] Accuracy: {metrics_report['Logistic Regression']['Accuracy']:.4f}, Dragon Gold Value: {dragon_gold_value:.1f} Gold")

    # --- 3단계. 비교 모델: Random Forest ---
    print("Training Random Forest...")
    # 트리 기반 모델은 스케일링 없이 원본(X_tr, X_te) 데이터를 사용
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
            "TN": int(tn_rf),
            "FP": int(fp_rf),
            "FN": int(fn_rf),
            "TP": int(tp_rf)
        },
        "Feature_Importances": rf_importances_dict
    }
    joblib.dump(rf_model, os.path.join(models_dir, "random_forest.joblib"))
    print(f"[Random Forest] Accuracy: {metrics_report['Random Forest']['Accuracy']:.4f}")

    # --- 4단계. 최적화 모델: XGBoost ---
    if HAS_XGBOOST:
        print("Tuning and Training XGBoost...")
        # 하이퍼파라미터 튜닝 로직 포함 (스케일링 없는 원본 데이터 사용)
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
        print(f"XGBoost Best Params: {best_params}")
        
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
                "TN": int(tn_xgb),
                "FP": int(fp_xgb),
                "FN": int(fn_xgb),
                "TP": int(tp_xgb)
            },
            "Feature_Importances": xgb_importances_dict,
            "Best_Params": best_params
        }
        joblib.dump(xgb_model, os.path.join(models_dir, "xgboost.joblib"))
        print(f"[XGBoost] Accuracy: {metrics_report['XGBoost']['Accuracy']:.4f}")
    else:
        print("XGBoost is not installed. Skipping XGBoost model training.")
        
    # [Vercel 최적화] m2cgen을 사용하여 무의존성 순수 파이썬 모델 코드 컴파일
    try:
        import m2cgen as m2c
        print("Compiling models to pure Python code using m2cgen...")
        
        # 1. Logistic Regression 컴파일
        lr_code = m2c.export_to_python(lr_model)
        with open(os.path.join(models_dir, "logistic_regression_code.py"), "w", encoding="utf-8") as f:
            f.write(lr_code)
            
        # 2. Random Forest 컴파일 (용량이 크므로 Vercel 최적화를 위해 무의존성으로 컴파일)
        rf_code = m2c.export_to_python(rf_model)
        with open(os.path.join(models_dir, "random_forest_code.py"), "w", encoding="utf-8") as f:
            f.write(rf_code)
            
        # 3. XGBoost 컴파일
        if HAS_XGBOOST:
            xgb_model.base_score = 0.5
            xgb_code = m2c.export_to_python(xgb_model)
            with open(os.path.join(models_dir, "xgboost_code.py"), "w", encoding="utf-8") as f:
                f.write(xgb_code)
                
        # 4. 스케일러 파라미터 JSON으로 별도 저장 (무의존성 전처리용)
        scaler_data = {
            "mean": scaler.mean_.tolist(),
            "scale": scaler.scale_.tolist()
        }
        with open(os.path.join(models_dir, "scaler.json"), "w", encoding="utf-8") as f:
            json.dump(scaler_data, f, indent=4)
            
        print("m2cgen model compilation completed successfully!")
    except Exception as e:
        print(f"Error compiling models with m2cgen: {str(e)}")

    # JSON 파일로 종합 지표 및 성능 저장
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
    print(f"Metrics saved to {metrics_path}")
        
    return metrics_report

if __name__ == "__main__":
    train_and_evaluate()
