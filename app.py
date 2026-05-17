import os
import json
import numpy as np
import joblib
import io
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import google.generativeai as genai
from train import train_and_evaluate

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")

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
        return jsonify({"error": "Metrics file not found. Please run training locally first."}), 404
            
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)
    return jsonify(metrics)

@app.route("/api/predict", methods=["POST"])
def predict_match():
    input_data = request.json
    model_name = request.args.get("model_name", "XGBoost")
    
    model_key = model_name.lower().replace(" ", "_")
    model_file = os.path.join(MODELS_DIR, f"{model_key}.joblib")
    scaler_file = os.path.join(MODELS_DIR, "scaler.joblib")
    
    if not os.path.exists(model_file):
        return jsonify({"error": f"Model not found: {model_name}. Ensure models are trained."}), 500
            
    try:
        model = joblib.load(model_file)
        scaler = None
        if model_name == "Logistic Regression":
            if os.path.exists(scaler_file):
                scaler = joblib.load(scaler_file)
            else:
                return jsonify({"error": "Scaler file not found for Logistic Regression."}), 500
    except Exception as e:
        return jsonify({"error": f"Error loading models: {str(e)}"}), 500
        
    # Feature engineering (Auto-alignment)
    input_dict = input_data.copy()
    
    # Matching deaths to kills
    input_dict['blueDeaths'] = input_data.get('redKills', 0)
    input_dict['redDeaths'] = input_data.get('blueKills', 0)
    
    # Gold/Exp Diffs (Note: redGoldDiff and redExperienceDiff are dropped from model features but kept for tracking)
    input_dict['blueGoldDiff'] = input_dict.get('blueTotalGold', 16500) - input_dict.get('redTotalGold', 16500)
    input_dict['redGoldDiff'] = input_dict.get('redTotalGold', 16500) - input_dict.get('blueTotalGold', 16500)
    input_dict['blueExperienceDiff'] = input_dict.get('blueTotalExperience', 18000) - input_dict.get('redTotalExperience', 18000)
    input_dict['redExperienceDiff'] = input_dict.get('redTotalExperience', 18000) - input_dict.get('blueTotalExperience', 18000)
    
    # CS/Gold rates
    input_dict['blueCSPerMin'] = input_dict.get('blueTotalMinionsKilled', 210) / 10.0
    input_dict['redCSPerMin'] = input_dict.get('redTotalMinionsKilled', 210) / 10.0
    input_dict['blueGoldPerMin'] = input_dict.get('blueTotalGold', 16500) / 10.0
    input_dict['redGoldPerMin'] = input_dict.get('redTotalGold', 16500) / 10.0
    
    # Objectives
    input_dict['blueEliteMonsters'] = input_dict.get('blueDragons', 0) + input_dict.get('blueHeralds', 0)
    input_dict['redEliteMonsters'] = input_dict.get('redDragons', 0) + input_dict.get('redHeralds', 0)
    
    # First Blood exclusive
    input_dict['redFirstBlood'] = 1 if input_dict.get('blueFirstBlood') == 0 else 0

    # Ensure all required features are present with default values
    feature_defaults = {
        'blueWardsPlaced': 15, 'blueWardsDestroyed': 2, 'blueFirstBlood': 1, 'blueKills': 5, 'blueDeaths': 5, 'blueAssists': 5,
        'blueEliteMonsters': 0, 'blueDragons': 0, 'blueHeralds': 0, 'blueTowersDestroyed': 0, 'blueTotalGold': 16500, 'blueAvgLevel': 6.8,
        'blueTotalExperience': 18000, 'blueTotalMinionsKilled': 210, 'blueTotalJungleMinionsKilled': 50, 'blueGoldDiff': 0,
        'blueExperienceDiff': 0, 'blueCSPerMin': 21.0, 'blueGoldPerMin': 1650.0,
        'redWardsPlaced': 15, 'redWardsDestroyed': 2, 'redFirstBlood': 0, 'redKills': 5, 'redDeaths': 5, 'redAssists': 5,
        'redEliteMonsters': 0, 'redDragons': 0, 'redHeralds': 0, 'redTowersDestroyed': 0, 'redTotalGold': 16500, 'redAvgLevel': 6.8,
        'redTotalExperience': 18000, 'redTotalMinionsKilled': 210, 'redTotalJungleMinionsKilled': 50, 'redCSPerMin': 21.0, 'redGoldPerMin': 1650.0
    }
    
    full_input = feature_defaults.copy()
    full_input.update(input_dict)
    
    # Dynamically load the exact feature order used in training (omits redGoldDiff and redExperienceDiff)
    feature_order = []
    feature_names_file = os.path.join(MODELS_DIR, "feature_names.json")
    if os.path.exists(feature_names_file):
        try:
            with open(feature_names_file, "r", encoding="utf-8") as f:
                feature_order = json.load(f)
        except Exception:
            pass
            
    if not feature_order:
        # Fallback to feature order without redGoldDiff and redExperienceDiff
        feature_order = [
            'blueWardsPlaced', 'blueWardsDestroyed', 'blueFirstBlood', 'blueKills', 'blueDeaths', 'blueAssists',
            'blueEliteMonsters', 'blueDragons', 'blueHeralds', 'blueTowersDestroyed', 'blueTotalGold', 'blueAvgLevel',
            'blueTotalExperience', 'blueTotalMinionsKilled', 'blueTotalJungleMinionsKilled', 'blueGoldDiff',
            'blueExperienceDiff', 'blueCSPerMin', 'blueGoldPerMin',
            'redWardsPlaced', 'redWardsDestroyed', 'redFirstBlood', 'redKills', 'redDeaths', 'redAssists',
            'redEliteMonsters', 'redDragons', 'redHeralds', 'redTowersDestroyed', 'redTotalGold', 'redAvgLevel',
            'redTotalExperience', 'redTotalMinionsKilled', 'redTotalJungleMinionsKilled', 'redCSPerMin', 'redGoldPerMin'
        ]
    
    try:
        # Create numpy array in exact feature order
        input_values = [full_input.get(f, feature_defaults.get(f, 0)) for f in feature_order]
        X = np.array(input_values).reshape(1, -1)
        
        # Scaling is applied ONLY to Logistic Regression
        if model_name == "Logistic Regression":
            X_input = scaler.transform(X)
        else:
            X_input = X
            
        proba = model.predict_proba(X_input)[0]
        blue_win_probability = proba[1]
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
    try:
        metrics = train_and_evaluate()
        return jsonify({
            "status": "success",
            "message": "Models trained successfully.",
            "metrics": metrics
        })
    except Exception as e:
        return jsonify({"error": f"Failed to train models: {str(e)}"}), 500

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
        # Demo data fallback
        return jsonify({
            "is_mocked": True,
            "blueKills": 9, "blueDeaths": 4, "blueAssists": 6,
            "blueTotalMinionsKilled": 106, "blueAvgLevel": 5.6,
            "blueTotalGold": 16800, "blueTotalExperience": 18200,
            "blueWardsPlaced": 15, "blueWardsDestroyed": 2,
            "blueDragons": 1, "blueHeralds": 0, "blueTowersDestroyed": 0,
            "blueTotalJungleMinionsKilled": 50, "blueFirstBlood": 1,
            "redKills": 0, "redDeaths": 9, "redAssists": 1,
            "redTotalMinionsKilled": 89, "redAvgLevel": 5.6,
            "redTotalGold": 15400, "redTotalExperience": 17200,
            "redWardsPlaced": 14, "redWardsDestroyed": 3,
            "redDragons": 0, "redHeralds": 1, "redTowersDestroyed": 0,
            "redTotalJungleMinionsKilled": 48, "redFirstBlood": 0
        })
    
    try:
        prompt = "Analyze this LoL scoreboard at 10m and extract stats (KDA, CS, Level, Gold, Exp, Wards, Monsters) for Blue and Red teams. Return valid JSON."
        model = genai.GenerativeModel("gemini-2.0-flash") # Use latest flash
        response = model.generate_content([image, prompt], generation_config={"response_mime_type": "application/json"})
        parsed_data = json.loads(response.text.strip())
        parsed_data["is_mocked"] = False
        return jsonify(parsed_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
