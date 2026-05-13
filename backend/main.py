import os
import json
import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib

from train import train_and_evaluate

app = FastAPI(
    title="League of Legends Match Predictor (10m)",
    description="Predicts match outcome based on early 10 minutes game data using ML.",
    version="1.0.0"
)

# CORS configuration to allow Next.js frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify frontend domain e.g., ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")

class PredictionInput(BaseModel):
    # Blue team features (default values represent typical 10m diamond game averages)
    blueWardsPlaced: int = Field(15, description="Blue team wards placed")
    blueWardsDestroyed: int = Field(2, description="Blue team wards destroyed")
    blueFirstBlood: int = Field(0, description="Blue team got first blood (1: Yes, 0: No)")
    blueKills: int = Field(5, description="Blue team total kills")
    blueDeaths: int = Field(5, description="Blue team total deaths")
    blueAssists: int = Field(5, description="Blue team total assists")
    blueEliteMonsters: int = Field(0, description="Blue team elite monsters killed (Dragons + Heralds)")
    blueDragons: int = Field(0, description="Blue team dragons killed")
    blueHeralds: int = Field(0, description="Blue team heralds killed")
    blueTowersDestroyed: int = Field(0, description="Blue team towers destroyed")
    blueTotalGold: int = Field(16500, description="Blue team total gold")
    blueAvgLevel: float = Field(6.8, description="Blue team average champion level")
    blueTotalExperience: int = Field(18000, description="Blue team total experience")
    blueTotalMinionsKilled: int = Field(210, description="Blue team total minions killed (CS)")
    blueTotalJungleMinionsKilled: int = Field(50, description="Blue team total jungle monsters killed")
    blueGoldDiff: int = Field(0, description="Blue team gold difference (Blue Gold - Red Gold)")
    blueExperienceDiff: int = Field(0, description="Blue team experience difference (Blue Exp - Red Exp)")
    blueCSPerMin: float = Field(21.0, description="Blue team CS per minute")
    blueGoldPerMin: float = Field(1650.0, description="Blue team gold per minute")
    
    # Red team features
    redWardsPlaced: int = Field(15, description="Red team wards placed")
    redWardsDestroyed: int = Field(2, description="Red team wards destroyed")
    redFirstBlood: int = Field(0, description="Red team got first blood (1: Yes, 0: No)")
    redKills: int = Field(5, description="Red team total kills")
    redDeaths: int = Field(5, description="Red team total deaths")
    redAssists: int = Field(5, description="Red team total assists")
    redEliteMonsters: int = Field(0, description="Red team elite monsters killed (Dragons + Heralds)")
    redDragons: int = Field(0, description="Red team dragons killed")
    redHeralds: int = Field(0, description="Red team heralds killed")
    redTowersDestroyed: int = Field(0, description="Red team towers destroyed")
    redTotalGold: int = Field(16500, description="Red team total gold")
    redAvgLevel: float = Field(6.8, description="Red team average champion level")
    redTotalExperience: int = Field(18000, description="Red team total experience")
    redTotalMinionsKilled: int = Field(210, description="Red team total minions killed (CS)")
    redTotalJungleMinionsKilled: int = Field(50, description="Red team total jungle monsters killed")
    redGoldDiff: int = Field(0, description="Red team gold difference (Red Gold - Blue Gold)")
    redExperienceDiff: int = Field(0, description="Red team experience difference (Red Exp - Blue Exp)")
    redCSPerMin: float = Field(21.0, description="Red team CS per minute")
    redGoldPerMin: float = Field(1650.0, description="Red team gold per minute")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "League of Legends Win Rate Predictor API is running.",
        "api_endpoints": {
            "get_metrics": "/api/metrics",
            "predict": "/api/predict",
            "train": "/api/train"
        }
    }

@app.get("/api/metrics")
def get_metrics():
    metrics_path = os.path.join(MODELS_DIR, "metrics.json")
    if not os.path.exists(metrics_path):
        # If metrics doesn't exist, trigger training first
        try:
            print("Metrics file not found. Auto-training models...")
            metrics = train_and_evaluate()
            return metrics
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to auto-train models: {str(e)}")
            
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)
    return metrics

@app.post("/api/predict")
def predict_match(input_data: PredictionInput, model_name: str = "XGBoost"):
    # Determine the model file based on input query
    model_key = model_name.lower().replace(" ", "_")
    model_file = os.path.join(MODELS_DIR, f"{model_key}.joblib")
    scaler_file = os.path.join(MODELS_DIR, "scaler.joblib")
    
    # Fallback to Logistic Regression if XGBoost not present
    if not os.path.exists(model_file):
        if model_key == "xgboost":
            model_key = "logistic_regression"
            model_file = os.path.join(MODELS_DIR, "logistic_regression.joblib")
            model_name = "Logistic Regression"
            
    if not os.path.exists(model_file) or not os.path.exists(scaler_file):
        # Auto-train if models directory is empty
        try:
            print("Model weights not found. Auto-training models...")
            train_and_evaluate()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to auto-train models: {str(e)}")
            
    # Load model & scaler
    try:
        model = joblib.load(model_file)
        scaler = joblib.load(scaler_file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading models: {str(e)}")
        
    # Convert input to DataFrame
    input_dict = input_data.model_dump()
    
    # Make sure we maintain identical feature order as the training dataset columns
    # Excluding 'blueWins' and 'gameId'
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
    
    # Check goldDiff and experienceDiff auto-alignment (dynamic user assistance)
    # Typically, blueGoldDiff is blueTotalGold - redTotalGold, etc.
    # We will automatically calculate these to ensure user doesn't have to manually calculate them.
    input_dict['blueGoldDiff'] = input_dict['blueTotalGold'] - input_dict['redTotalGold']
    input_dict['redGoldDiff'] = input_dict['redTotalGold'] - input_dict['blueTotalGold']
    input_dict['blueExperienceDiff'] = input_dict['blueTotalExperience'] - input_dict['redTotalExperience']
    input_dict['redExperienceDiff'] = input_dict['redTotalExperience'] - input_dict['blueTotalExperience']
    
    # Auto-adjust CS/Gold Per Min
    input_dict['blueCSPerMin'] = input_dict['blueTotalMinionsKilled'] / 10.0
    input_dict['redCSPerMin'] = input_dict['redTotalMinionsKilled'] / 10.0
    input_dict['blueGoldPerMin'] = input_dict['blueTotalGold'] / 10.0
    input_dict['redGoldPerMin'] = input_dict['redTotalGold'] / 10.0
    
    # Auto-adjust elite monsters
    input_dict['blueEliteMonsters'] = input_dict['blueDragons'] + input_dict['blueHeralds']
    input_dict['redEliteMonsters'] = input_dict['redDragons'] + input_dict['redHeralds']
    
    try:
        df_input = pd.DataFrame([input_dict])[feature_order]
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing feature: {str(e)}")
        
    # Scale input features
    df_input_scaled = scaler.transform(df_input)
    
    # Predict probability of blue win
    try:
        blue_win_probability = model.predict_proba(df_input_scaled)[0][1]
        prediction = int(model.predict(df_input_scaled)[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
        
    return {
        "model_used": model_name,
        "prediction": prediction,  # 1 if Blue wins, 0 if Red wins
        "winner": "Blue" if prediction == 1 else "Red",
        "blue_win_probability": float(blue_win_probability),
        "red_win_probability": float(1.0 - blue_win_probability)
    }

@app.post("/api/train")
def train_models():
    try:
        metrics = train_and_evaluate()
        return {
            "status": "success",
            "message": "Models trained successfully.",
            "metrics": metrics
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to train models: {str(e)}")
