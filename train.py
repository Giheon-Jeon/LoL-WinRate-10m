import os
import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix
import m2cgen as m2c

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
        weights = gater_probs
        final_proba = np.sum(expert_probas * weights, axis=1)
        return np.vstack([1 - final_proba, final_proba]).T

    def predict(self, X):
        probas = self.predict_proba(X)
        return (probas[:, 1] >= 0.5).astype(int)

def train_and_evaluate():
    print("Starting ML Model training process with m2cgen export...")
    
    data_path = os.path.join(os.path.dirname(__file__), "high_diamond_ranked_10min.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at: {data_path}")
            
    raw_data = np.genfromtxt(data_path, delimiter=',', skip_header=1)
    y = raw_data[:, 1]
    X = raw_data[:, 2:]
    
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_tr_scaled = scaler.fit_transform(X_tr)
    X_te_scaled = scaler.transform(X_te)
    
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    
    # Export Scaler to JSON
    scaler_data = {"mean": scaler.mean_.tolist(), "scale": scaler.scale_.tolist()}
    with open(os.path.join(models_dir, "scaler.json"), "w") as f: json.dump(scaler_data, f)

    # Models preparation
    base_models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)
    }
    
    metrics_report = {}

    # 1. Train and Export Base Models
    for name, model in base_models.items():
        print(f"Training and exporting {name}...")
        model.fit(X_tr_scaled, y_tr)
        
        y_pred = model.predict(X_te_scaled)
        y_proba = model.predict_proba(X_te_scaled)[:, 1]
        
        metrics_report[name] = {
            "Accuracy": round(float(accuracy_score(y_te, y_pred)), 4),
            "F1-Score": round(float(f1_score(y_te, y_pred)), 4),
            "ROC-AUC": round(float(roc_auc_score(y_te, y_proba)), 4),
            "ConfusionMatrix": confusion_matrix(y_te, y_pred).tolist()
        }
        
        code = m2c.export_to_python(model)
        with open(os.path.join(models_dir, f"{name.lower().replace(' ', '_')}_code.py"), "w") as f:
            f.write(code)
            
    # 2. Train and Export MoE Components
    print("Training and exporting MoE components...")
    moe_lr = LogisticRegression(max_iter=1000, random_state=42)
    moe_rf = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)
    moe_gater = RandomForestClassifier(n_estimators=30, max_depth=5, random_state=42)
    
    moe_lr.fit(X_tr_scaled, y_tr)
    moe_rf.fit(X_tr_scaled, y_tr)
    moe_gater.fit(X_tr_scaled, y_tr)
    
    # Calculate MoE metrics
    p_lr = moe_lr.predict_proba(X_te_scaled)[:, 1]
    p_rf = moe_rf.predict_proba(X_te_scaled)[:, 1]
    w_gater = moe_gater.predict_proba(X_te_scaled)
    moe_proba = p_lr * w_gater[:, 0] + p_rf * w_gater[:, 1]
    moe_pred = (moe_proba >= 0.5).astype(int)
    
    metrics_report["MoE Ensemble"] = {
        "Accuracy": round(float(accuracy_score(y_te, moe_pred)), 4),
        "F1-Score": round(float(f1_score(y_te, moe_pred)), 4),
        "ROC-AUC": round(float(roc_auc_score(y_te, moe_proba)), 4),
        "ConfusionMatrix": confusion_matrix(y_te, moe_pred).tolist()
    }
    
    with open(os.path.join(models_dir, "moe_expert_lr_code.py"), "w") as f: f.write(m2c.export_to_python(moe_lr))
    with open(os.path.join(models_dir, "moe_expert_rf_code.py"), "w") as f: f.write(m2c.export_to_python(moe_rf))
    with open(os.path.join(models_dir, "moe_gater_code.py"), "w") as f: f.write(m2c.export_to_python(moe_gater))

    with open(os.path.join(models_dir, "metrics.json"), "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
        
    print("All models exported as pure Python code.")
    return metrics_report
        
    print("All models exported as pure Python code.")
    return metrics_report

if __name__ == "__main__":
    train_and_evaluate()

if __name__ == "__main__":
    train_and_evaluate()
