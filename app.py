import os
import json
import numpy as np
import io
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import google.generativeai as genai

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")

# Gemini API 설정 (환경변수)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/metrics")
def get_metrics():
    """학습된 모델의 평가 지표(Metrics)를 반환합니다."""
    metrics_path = os.path.join(MODELS_DIR, "metrics.json")
    if not os.path.exists(metrics_path):
        return jsonify({"error": "모델 지표 파일을 찾을 수 없습니다. 먼저 모델을 학습시켜주세요."}), 404
            
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)
    return jsonify(metrics)

@app.route("/api/champions")
def get_champions():
    """Riot API에서 챔피언 데이터를 가져옵니다."""
    import urllib.request
    url = "https://ddragon.leagueoflegends.com/cdn/14.22.1/data/ko_KR/champion.json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as response:
            data = json.loads(response.read().decode('utf-8'))
            champions_dict = data.get("data", {})
            champions_list = []
            for c_id, c_data in champions_dict.items():
                champions_list.append({
                    "id": c_id,
                    "name": c_data.get("name"),
                    "title": c_data.get("title"),
                    "image": f"https://ddragon.leagueoflegends.com/cdn/14.22.1/img/champion/{c_id}.png"
                })
            champions_list.sort(key=lambda x: x["name"])
            return jsonify(champions_list)
    except Exception as e:
        from backend.champion_data import CHAMPION_NAMES_KR
        champions_list = []
        for c_id, name_kr in CHAMPION_NAMES_KR.items():
            champions_list.append({
                "id": c_id,
                "name": name_kr,
                "title": "",
                "image": f"https://ddragon.leagueoflegends.com/cdn/14.22.1/img/champion/{c_id}.png"
            })
        champions_list.sort(key=lambda x: x["name"])
        return jsonify(champions_list)

def calculate_dragon_gold_value(model_name, full_input, feature_order):
    """
    편미분을 이용해 드래곤 1마리가 승률에 미치는 영향을 골드 가치로 환산합니다.
    """
    def get_prob(inp_dict):
        # 피처 정렬
        input_vals = [inp_dict.get(f, 0.0) for f in feature_order]
        
        if model_name == "Logistic Regression":
            from models.logistic_regression_code import score as lr_score
            scaler_file = os.path.join(MODELS_DIR, "scaler.json")
            if not os.path.exists(scaler_file):
                return 0.5
            with open(scaler_file, "r") as f:
                scaler_data = json.load(f)
                scaler_mean = scaler_data["mean"]
                scaler_scale = scaler_data["scale"]
            X_scaled = [(x_i - mean_i) / (scale_i if scale_i != 0 else 1) for x_i, mean_i, scale_i in zip(input_vals, scaler_mean, scaler_scale)]
            margin = lr_score(X_scaled)
            return 1.0 / (1.0 + np.exp(-margin))
            
        elif model_name == "Random Forest":
            from models.random_forest_code import score as rf_score
            proba = rf_score(input_vals)
            return proba[1]
            
        elif model_name == "XGBoost":
            from models.xgboost_code import score as xgb_score
            proba = xgb_score(input_vals)
            return proba[1]
        return 0.5

    # 1. 현재 승률
    p_current = get_prob(full_input)
    
    # 2. 드래곤 1마리 추가 시 승률
    current_dragons = full_input.get('blue_dragons', 0)
    dragons_changed = current_dragons + 1 if current_dragons < 2 else current_dragons - 1
    direction = 1 if current_dragons < 2 else -1
    
    inp_dragon_changed = full_input.copy()
    inp_dragon_changed['blue_dragons'] = dragons_changed
    p_dragon_changed = get_prob(inp_dragon_changed)
    
    # 3. 골드 격차 100당 승률 변화량 계산 (Top/Mid/Bot 등 라인별 골드 증감 적용)
    # 단순화를 위해 전체 라인에 균등하게 분배
    inp_gold_plus = full_input.copy()
    gold_increment = 100.0 / 5.0
    for role in ['top', 'jungle', 'middle', 'bottom', 'utility']:
        inp_gold_plus[f'blue_{role}_gold'] += gold_increment
        inp_gold_plus[f'{role}_gold_diff'] += gold_increment
        
    p_gold_plus = get_prob(inp_gold_plus)
    
    inp_gold_minus = full_input.copy()
    for role in ['top', 'jungle', 'middle', 'bottom', 'utility']:
        inp_gold_minus[f'blue_{role}_gold'] -= gold_increment
        inp_gold_minus[f'{role}_gold_diff'] -= gold_increment
        
    p_gold_minus = get_prob(inp_gold_minus)
    
    dp_dgold = (p_gold_plus - p_gold_minus) / 200.0
    
    if abs(dp_dgold) < 1e-7:
        return 1500.0
            
    dragon_gold_value = ((p_dragon_changed - p_current) / direction) / dp_dgold
    
    if dragon_gold_value < 0 or dragon_gold_value > 5000 or np.isnan(dragon_gold_value):
        return 1500.0
            
    return float(dragon_gold_value)

def build_lane_features(input_data):
    """
    팀 합산 지표를 라인별 지표로 분배하고 원핫 인코딩 피처를 생성합니다.
    """
    roles = ['top', 'jungle', 'middle', 'bottom', 'utility']
    
    # 역할별 골드/CS/킬 분배 비율 (경험적 추정치)
    ratios = {
        'gold': [0.22, 0.19, 0.23, 0.24, 0.12],
        'cs': [0.25, 0.15, 0.27, 0.28, 0.05],
        'kills': [0.20, 0.25, 0.25, 0.25, 0.05],
        'deaths': [0.22, 0.18, 0.22, 0.20, 0.18]
    }
    
    out = {}
    
    # 1. 오브젝트 지표 직접 매핑
    out['blue_dragons'] = float(input_data.get('blueDragons', 0))
    out['blue_heralds'] = float(input_data.get('blueHeralds', 0))
    out['blue_towers'] = float(input_data.get('blueTowersDestroyed', 0))
    out['blue_kills'] = float(input_data.get('blueKills', 0))
    out['blue_firstBlood'] = float(input_data.get('blueFirstBlood', 0))
    out['blue_voidgrubs'] = float(input_data.get('blueEliteMonsters', 0)) # 유충은 대략적으로 매핑
    
    out['red_dragons'] = float(input_data.get('redDragons', 0))
    out['red_heralds'] = float(input_data.get('redHeralds', 0))
    out['red_towers'] = float(input_data.get('redTowersDestroyed', 0))
    out['red_kills'] = float(input_data.get('redKills', 0))
    out['red_voidgrubs'] = float(input_data.get('redEliteMonsters', 0))
    
    # 2. 라인별 수치 지표 분배
    blue_gold = float(input_data.get('blueTotalGold', 16500))
    red_gold = float(input_data.get('redTotalGold', 16500))
    
    blue_cs = float(input_data.get('blueTotalMinionsKilled', 210))
    red_cs = float(input_data.get('redTotalMinionsKilled', 210))
    
    blue_k = float(input_data.get('blueKills', 5))
    red_k = float(input_data.get('redKills', 5))
    
    blue_d = float(input_data.get('blueDeaths', 5))
    red_d = float(input_data.get('redDeaths', 5))
    
    for i, role in enumerate(roles):
        # 블루팀
        out[f'blue_{role}_gold'] = blue_gold * ratios['gold'][i]
        out[f'blue_{role}_cs'] = blue_cs * ratios['cs'][i]
        out[f'blue_{role}_kills'] = blue_k * ratios['kills'][i]
        out[f'blue_{role}_deaths'] = blue_d * ratios['deaths'][i]
        
        # 레드팀
        out[f'red_{role}_gold'] = red_gold * ratios['gold'][i]
        out[f'red_{role}_cs'] = red_cs * ratios['cs'][i]
        out[f'red_{role}_kills'] = red_k * ratios['kills'][i]
        out[f'red_{role}_deaths'] = red_d * ratios['deaths'][i]
        
        # 격차 (Diff)
        out[f'{role}_gold_diff'] = out[f'blue_{role}_gold'] - out[f'red_{role}_gold']
        
    return out

@app.route("/api/predict", methods=["POST"])
def predict_match():
    """선택된 모델과 입력 데이터를 바탕으로 승률 예측을 수행합니다."""
    input_data = request.json
    model_name = request.args.get("model_name", "XGBoost")
    
    # 1. 챔피언 데이터 파싱 및 조합 계산
    blue_champs = input_data.get('blue_champions', ["", "", "", "", ""])
    red_champs = input_data.get('red_champions', ["", "", "", "", ""])
    
    # 빈 슬롯 채우기 (최대 5명)
    while len(blue_champs) < 5: blue_champs.append("")
    while len(red_champs) < 5: red_champs.append("")
    
    # 챔피언 태그 및 조합 분석
    from backend.champion_data import get_champion_tags, determine_composition
    
    # 각 라인별 태그 추출
    blue_tags = get_champion_tags(blue_champs)
    red_tags = get_champion_tags(red_champs)
    
    # 조합 이름 판별
    blue_comp_name = determine_composition(blue_tags)
    red_comp_name = determine_composition(red_tags)
    
    # 2. 숫자형 지표 구축 (합산 지표를 라인별로 분배)
    feature_dict = build_lane_features(input_data)
    
    # 3. 원핫 인코딩 피처 추가 (기본 0, 일치하면 1)
    roles = ['top', 'jungle', 'middle', 'bottom', 'utility']
    for i, role in enumerate(roles):
        b_tag = blue_tags[i]
        r_tag = red_tags[i]
        feature_dict[f'blue_{role}_tag_{b_tag}'] = 1.0
        feature_dict[f'red_{role}_tag_{r_tag}'] = 1.0
        
    feature_dict[f'blue_comp_{blue_comp_name}'] = 1.0
    feature_dict[f'red_comp_{red_comp_name}'] = 1.0

    # 4. 저장된 Feature 순서에 맞게 입력 배열 생성
    feature_order = []
    feature_names_file = os.path.join(MODELS_DIR, "feature_names.json")
    if os.path.exists(feature_names_file):
        try:
            with open(feature_names_file, "r", encoding="utf-8") as f:
                feature_order = json.load(f)
        except Exception:
            pass
            
    if not feature_order:
        return jsonify({"error": "모델 학습 후 feature_names.json 파일이 필요합니다."}), 500
        
    # 입력 배열 (Order 기반으로 매핑, 없는 피처는 0으로 처리)
    input_values = [feature_dict.get(f, 0.0) for f in feature_order]
    
    try:
        # 모델 추론 수행
        if model_name == "Logistic Regression":
            from models.logistic_regression_code import score as lr_score
            scaler_file = os.path.join(MODELS_DIR, "scaler.json")
            with open(scaler_file, "r") as f:
                scaler_data = json.load(f)
                scaler_mean = scaler_data["mean"]
                scaler_scale = scaler_data["scale"]
            
            X_scaled = [(x_i - mean_i) / (scale_i if scale_i != 0 else 1) for x_i, mean_i, scale_i in zip(input_values, scaler_mean, scaler_scale)]
            margin = lr_score(X_scaled)
            blue_win_prob = 1.0 / (1.0 + np.exp(-margin))
            
        elif model_name == "Random Forest":
            from models.random_forest_code import score as rf_score
            proba = rf_score(input_values)
            blue_win_prob = proba[1]
            
        elif model_name == "XGBoost":
            from models.xgboost_code import score as xgb_score
            proba = xgb_score(input_values)
            blue_win_prob = proba[1]
            
        else:
            return jsonify({"error": f"Invalid model: {model_name}"}), 400
            
        prediction = 1 if blue_win_prob >= 0.5 else 0
        
        # 드래곤 가치 편미분 계산
        dragon_val = calculate_dragon_gold_value(model_name, feature_dict, feature_order)
        
        # 기존 로직과 호환성 유지용 임시 시너지 데이터
        synergies = {"blue_synergies": [], "red_synergies": [], "counters": []}
        
        return jsonify({
            "model_used": model_name,
            "prediction": prediction,
            "winner": "Blue" if prediction == 1 else "Red",
            "blue_win_probability": float(blue_win_prob),
            "red_win_probability": float(1.0 - blue_win_prob),
            "dragon_gold_value": float(dragon_val),
            "blue_comp_score": 0.5, # 새로운 데이터에선 미사용
            "red_comp_score": 0.5,
            "blue_synergies": synergies['blue_synergies'],
            "red_synergies": synergies['red_synergies'],
            "counters": synergies['counters']
        })
    except Exception as e:
        return jsonify({"error": f"예측 중 오류 발생: {str(e)}"}), 500

@app.route("/api/train", methods=["POST"])
def train_models():
    """모델 재학습 요청 API"""
    try:
        from train import train_and_evaluate
        metrics = train_and_evaluate()
        return jsonify({
            "status": "success",
            "message": "모델 학습 완료",
            "metrics": metrics
        })
    except Exception as e:
        return jsonify({"error": f"로컬 환경에서만 지원됩니다: {str(e)}"}), 500

@app.route("/api/parse-scoreboard", methods=["POST"])
def parse_scoreboard():
    """Gemini Vision 기반 스코어보드 이미지 분석 API"""
    if 'file' not in request.files:
        return jsonify({"error": "파일이 업로드되지 않았습니다."}), 400
    
    file = request.files['file']
    try:
        image = Image.open(file.stream)
    except Exception as e:
        return jsonify({"error": f"이미지 인식 실패: {str(e)}"}), 400
        
    if not GEMINI_API_KEY:
        # 데모 응답 (키가 없을 경우)
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
        prompt = "이 리그 오브 레전드 스코어보드를 분석하여 블루팀과 레드팀의 총 킬, 데스, 골드, CS, 와드, 드래곤, 전령 정보를 JSON 형태로 추출해주세요."
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content([image, prompt], generation_config={"response_mime_type": "application/json"})
        parsed_data = json.loads(response.text.strip())
        parsed_data["is_mocked"] = False
        return jsonify(parsed_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
