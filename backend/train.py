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
    
    # 1. Load Dataset
    # Data path relative to this backend script
    data_path = os.path.join(os.path.dirname(__file__), "..", "public", "high_diamond_ranked_10min.csv")
    if not os.path.exists(data_path):
        # Fallback to absolute path or backup file if exists
        data_path = os.path.join(os.path.dirname(__file__), "..", "high_diamond_ranked_10min.csv.bak")
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Dataset not found at: {data_path}")
            
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    
    # 2. Preprocess Data
    # Drop identifier
    if 'gameId' in df.columns:
        df = df.drop(columns=['gameId'])
        
    # Split features and target
    X = df.drop(columns=['blueWins'])
    y = df['blueWins']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save the scaler
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    joblib.dump(scaler, os.path.join(models_dir, "scaler.joblib"))
    print("Scaler saved successfully.")
    
    # Define models to train
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
    else:
        print("XGBoost library not found, skipping XGBoost training. (Will use fallbacks)")
        
    metrics_report = {}
    
    # Train & Evaluate each model
    for model_name, model in models.items():
        print(f"Training {model_name}...")
        model.fit(X_train_scaled, y_train)
        
        # Predictions
        y_pred = model.predict(X_test_scaled)
        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
        
        # Calculate metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        # Save metrics
        metrics_report[model_name] = {
            "Accuracy": float(acc),
            "Precision": float(prec),
            "Recall": float(rec),
            "F1-Score": float(f1),
            "ROC-AUC": float(roc_auc)
        }
        
        # Save model weights
        model_filename = model_name.lower().replace(" ", "_") + ".joblib"
        joblib.dump(model, os.path.join(models_dir, model_filename))
        print(f"{model_name} trained. Accuracy: {acc:.4f}, F1-Score: {f1:.4f}")
        
    # Save metrics JSON
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
        
    print(f"All model metrics saved to {metrics_path}.")
    return metrics_report

if __name__ == "__main__":
    train_and_evaluate()
