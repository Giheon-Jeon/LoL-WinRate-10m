import os
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
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
    
    # 전처리: ID 컬럼 제거 및 특성/타겟 분리
    if 'gameId' in df.columns:
        df = df.drop(columns=['gameId'])
        
    X = df.drop(columns=['blueWins'])
    y = df['blueWins']
    
    # 테스트 데이터셋 비율을 20%로 하여 split
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # 특성 스케일링 (선형 모델인 로지스틱 회귀를 위해 권장)
    scaler = StandardScaler()
    X_tr_scaled = scaler.fit_transform(X_tr)
    X_te_scaled = scaler.transform(X_te)
    
    # 스케일러 저장 (예측 시 사용)
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    joblib.dump(scaler, os.path.join(models_dir, "scaler.joblib"))

    # 2. 모델 학습 (다중 모델 지원)
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    }
    
    if HAS_XGBOOST:
        models["XGBoost"] = XGBClassifier(
            n_estimators=100, 
            max_depth=5, 
            learning_rate=0.1, 
            random_state=42, 
            eval_metric="logloss"
        )
        
    metrics_report = {}
    
    for model_name, model in models.items():
        print(f"Training {model_name}...")
        model.fit(X_tr_scaled, y_tr)
        
        # 3. 예측 & 평가
        y_pred = model.predict(X_te_scaled)
        y_pred_proba = model.predict_proba(X_te_scaled)[:, 1]
        
        acc = accuracy_score(y_te, y_pred)
        prec = precision_score(y_te, y_pred)
        rec = recall_score(y_te, y_pred)
        f1 = f1_score(y_te, y_pred)
        roc_auc = roc_auc_score(y_te, y_pred_proba)
        
        metrics_report[model_name] = {
            "Accuracy": float(acc),
            "Precision": float(prec),
            "Recall": float(rec),
            "F1-Score": float(f1),
            "ROC-AUC": float(roc_auc)
        }
        
        # 모델 저장
        model_filename = model_name.lower().replace(" ", "_") + ".joblib"
        joblib.dump(model, os.path.join(models_dir, model_filename))
        
        print(f"[{model_name}] Accuracy: {acc:.4f}, F1-Score: {f1:.4f}")
        
    # 결과 요약 저장
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
        
    return metrics_report

if __name__ == "__main__":
    train_and_evaluate()
