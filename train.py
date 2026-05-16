import os
import json
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

# Mixture of Experts (MoE) Model Definition
class MoEModel:
    def __init__(self, experts, gating_network):
        self.experts = experts
        self.gating_network = gating_network
        self.expert_names = list(experts.keys())

    def fit(self, X, y):
        for name in self.expert_names:
            self.experts[name].fit(X, y)
        self.gating_network.fit(X, y)

    def predict_proba(self, X):
        expert_probas = np.array([self.experts[name].predict_proba(X)[:, 1] for name in self.expert_names]).T
        gater_probs = self.gating_network.predict_proba(X)
        
        # Dynamic weighting based on gater
        weights = np.zeros((X.shape[0], len(self.expert_names)))
        for i in range(len(self.expert_names)):
            # Distribute weights across experts
            weights[:, i] = gater_probs[:, 1] if i == len(self.expert_names)-1 else (gater_probs[:, 0] / (len(self.expert_names)-1))
            
        final_proba = np.sum(expert_probas * weights, axis=1)
        return np.vstack([1 - final_proba, final_proba]).T

    def predict(self, X):
        probas = self.predict_proba(X)
        return (probas[:, 1] >= 0.5).astype(int)

def train_and_evaluate():
    print("Starting ML Model training process...")
    
    # 1. 데이터 로드 (Using numpy instead of pandas to reduce bundle size)
    data_path = os.path.join(os.path.dirname(__file__), "high_diamond_ranked_10min.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at: {data_path}")
            
    # Load data skipping header, assuming standard structure
    # Column indices: blueWins is index 1, gameId is index 0
    # We use genfromtxt with delimiter=',' and skip_header=1
    raw_data = np.genfromtxt(data_path, delimiter=',', skip_header=1)
    
    # Column mapping (based on header check):
    # gameId(0), blueWins(1), ...others(2-39)
    y = raw_data[:, 1]
    X = raw_data[:, 2:] # Drop gameId and blueWins
    
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_tr_scaled = scaler.fit_transform(X_tr)
    X_te_scaled = scaler.transform(X_te)
    
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    joblib.dump(scaler, os.path.join(models_dir, "scaler.joblib"))

    # Experts 준비
    expert_list = {
        "LR_Expert": LogisticRegression(max_iter=1000, random_state=42),
        "RF_Expert": RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    }
    if HAS_XGBOOST:
        expert_list["XGB_Expert"] = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42, eval_metric="logloss")

    # 2. 모델 리스트 구성 (MoE 포함)
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
        "MoE Ensemble": MoEModel(experts=expert_list, gating_network=RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42))
    }
    
    if HAS_XGBOOST:
        models["XGBoost"] = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42, eval_metric="logloss")
        
    metrics_report = {}
    
    for model_name, model in models.items():
        print(f"Training {model_name}...")
        model.fit(X_tr_scaled, y_tr)
        
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
        
        model_filename = model_name.lower().replace(" ", "_") + ".joblib"
        joblib.dump(model, os.path.join(models_dir, model_filename))
        print(f"[{model_name}] Accuracy: {acc:.4f}, F1-Score: {f1:.4f}")
        
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
        
    return metrics_report

if __name__ == "__main__":
    train_and_evaluate()
