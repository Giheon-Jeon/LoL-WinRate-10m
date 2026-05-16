import os
import json
import numpy as np
import io
import sys
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import google.generativeai as genai

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")
sys.path.append(MODELS_DIR)

# Import generated model codes
try:
    import logistic_regression_code as lr_model
    import random_forest_code as rf_model
    import moe_expert_lr_code as moe_lr
    import moe_expert_rf_code as moe_rf
    import moe_gater_code as moe_gater
except ImportError as e:
    print(f"Warning: Some models could not be imported: {e}")

# Load Scaler from JSON
SCALER_DATA = None
scaler_path = os.path.join(MODELS_DIR, "scaler.json")
if os.path.exists(scaler_path):
    with open(scaler_path, "r") as f:
        SCALER_DATA = json.load(f)

# Try to configure Gemini from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/metrics")
def get_metrics():
    metrics_path = os.path.join(MODELS_DIR, "metrics.json")
    if not os.path.exists(metrics_path):
        return jsonify({"error": "Metrics file not found."}), 404
            
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)
    return jsonify(metrics)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def get_prediction_proba(model_module, X_scaled):
    # m2cgen generated 'score' function returns a list or float
    score = model_module.score(X_scaled[0].tolist())
    if isinstance(score, list):
        return score # [prob_0, prob_1]
    else:
        # Logistic Regression returns raw logit, apply sigmoid
        prob = float(sigmoid(score))
        return [1.0 - prob, prob]

@app.route("/api/predict", methods=["POST"])
def predict_match():
    input_data = request.json
    model_name = request.args.get("model_name", "MoE Ensemble")
    
    if SCALER_DATA is None:
        return jsonify({"error": "Scaler data not found."}), 500
        
    # Feature engineering (Auto-alignment)
    input_dict = input_data.copy()
    input_dict['blueDeaths'] = input_data.get('redKills', 0)
    input_dict['redDeaths'] = input_data.get('blueKills', 0)
    
    input_dict['blueGoldDiff'] = input_dict.get('blueTotalGold', 16500) - input_dict.get('redTotalGold', 16500)
    input_dict['redGoldDiff'] = input_dict.get('redTotalGold', 16500) - input_dict.get('blueTotalGold', 16500)
    input_dict['blueExperienceDiff'] = input_dict.get('blueTotalExperience', 18000) - input_dict.get('redTotalExperience', 18000)
    input_dict['redExperienceDiff'] = input_dict.get('redTotalExperience', 18000) - input_dict.get('blueTotalExperience', 18000)
    
    input_dict['blueCSPerMin'] = input_dict.get('blueTotalMinionsKilled', 210) / 10.0
    input_dict['redCSPerMin'] = input_dict.get('redTotalMinionsKilled', 210) / 10.0
    input_dict['blueGoldPerMin'] = input_dict.get('blueTotalGold', 16500) / 10.0
    input_dict['redGoldPerMin'] = input_dict.get('redTotalGold', 16500) / 10.0
    
    input_dict['blueEliteMonsters'] = input_dict.get('blueDragons', 0) + input_dict.get('blueHeralds', 0)
    input_dict['redEliteMonsters'] = input_dict.get('redDragons', 0) + input_dict.get('redHeralds', 0)
    input_dict['redFirstBlood'] = 1 if input_dict.get('blueFirstBlood') == 0 else 0

    feature_order = [
        'blueWardsPlaced', 'blueWardsDestroyed', 'blueFirstBlood', 'blueKills', 'blueDeaths', 'blueAssists',
        'blueEliteMonsters', 'blueDragons', 'blueHeralds', 'blueTowersDestroyed', 'blueTotalGold', 'blueAvgLevel',
        'blueTotalExperience', 'blueTotalMinionsKilled', 'blueTotalJungleMinionsKilled', 'blueGoldDiff',
        'blueExperienceDiff', 'blueCSPerMin', 'blueGoldPerMin',
        'redWardsPlaced', 'redWardsDestroyed', 'redFirstBlood', 'redKills', 'redDeaths', 'redAssists',
        'redEliteMonsters', 'redDragons', 'redHeralds', 'redTowersDestroyed', 'redTotalGold', 'redAvgLevel',
        'redTotalExperience', 'redTotalMinionsKilled', 'redTotalJungleMinionsKilled', 'redGoldDiff',
        'redExperienceDiff', 'redCSPerMin', 'redGoldPerMin'
    ]
    
    try:
        input_values = [input_dict.get(f, 0) for f in feature_order]
        X = np.array(input_values).reshape(1, -1)
        
        # Manual Scaling
        X_scaled = (X - np.array(SCALER_DATA["mean"])) / np.array(SCALER_DATA["scale"])
        
        blue_win_probability = 0.5
        
        if model_name == "Logistic Regression":
            probs = get_prediction_proba(lr_model, X_scaled)
            blue_win_probability = probs[1]
        elif model_name == "Random Forest":
            probs = get_prediction_proba(rf_model, X_scaled)
            blue_win_probability = probs[1]
        else: # MoE Ensemble
            p_lr = get_prediction_proba(moe_lr, X_scaled)[1]
            p_rf = get_prediction_proba(moe_rf, X_scaled)[1]
            # Gater weights
            w_gater = get_prediction_proba(moe_gater, X_scaled)
            # Logic: weights[0] for LR, weights[1] for RF
            blue_win_probability = p_lr * w_gater[0] + p_rf * w_gater[1]
        
        prediction = 1 if blue_win_probability >= 0.5 else 0
        return jsonify({
            "model_used": model_name,
            "prediction": prediction,
            "winner": "Blue" if prediction == 1 else "Red",
            "blue_win_probability": float(blue_win_probability),
            "red_win_probability": float(1.0 - blue_win_probability)
        })
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

@app.route("/api/train", methods=["POST"])
def train_models():
    return jsonify({"error": "Training is disabled on Vercel. Please run locally."}), 403

@app.route("/api/parse-scoreboard", methods=["POST"])
def parse_scoreboard():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    try:
        image = Image.open(file.stream)
    except Exception as e:
        return jsonify({"error": f"Invalid image: {str(e)}"}), 400
        
    if not GEMINI_API_KEY:
        return jsonify({"error": "Gemini API Key not configured."}), 500
    
    try:
        prompt = "Analyze this LoL scoreboard at 10m and extract stats (KDA, CS, Level, Gold, Exp, Wards, Monsters) for Blue and Red teams. Return valid JSON."
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content([image, prompt], generation_config={"response_mime_type": "application/json"})
        parsed_data = json.loads(response.text.strip())
        parsed_data["is_mocked"] = False
        return jsonify(parsed_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
