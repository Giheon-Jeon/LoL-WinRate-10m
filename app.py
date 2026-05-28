# -*- coding: utf-8 -*-
import os
import json
import numpy as np
import io
import sys
import importlib
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

# ==============================================================================
# [INLINED] 챔피언 데이터베이스 및 드래프트 시너지/조합 계산 엔진
# ==============================================================================

# 인기 챔피언 기본 승률 (없는 경우 기본값 0.50)
CHAMPION_BASE_WIN_RATES = {
    # Top
    "Aatrox": 0.502, "Fiora": 0.512, "Jax": 0.508, "Malphite": 0.515, "Ornn": 0.505,
    "Renekton": 0.485, "Riven": 0.501, "Camille": 0.510, "Darius": 0.503, "Gnar": 0.482,
    "Kled": 0.514, "Mordekaiser": 0.504, "Sion": 0.490, "Teemo": 0.480, "Nasus": 0.495,
    "Jayce": 0.475, "Rumble": 0.506, "Ksante": 0.468, "Yorick": 0.511, "Garen": 0.518,
    
    # Jungle
    "LeeSin": 0.486, "Graves": 0.492, "Viego": 0.498, "KhaZix": 0.507, "Kayn": 0.501,
    "Elise": 0.504, "Nidalee": 0.472, "Nocturne": 0.521, "JarvanIV": 0.506, "Hecarim": 0.495,
    "Sejuani": 0.497, "Maokai": 0.512, "Zac": 0.518, "Rammus": 0.519, "Evelynn": 0.508,
    "Shaco": 0.499, "XinZhao": 0.510, "Belveth": 0.515, "Briar": 0.510, "Amumu": 0.513,
    
    # Mid
    "Ahri": 0.514, "Yasuo": 0.488, "Yone": 0.486, "Zed": 0.491, "Sylas": 0.495,
    "Orianna": 0.493, "Syndra": 0.497, "Azir": 0.465, "Talon": 0.511, "Katarina": 0.496,
    "Kassadin": 0.509, "Veigar": 0.502, "Viktor": 0.499, "LeBlanc": 0.484, "Ryze": 0.472,
    "Akali": 0.487, "Taliyah": 0.512, "Hwei": 0.480, "Anivia": 0.523, "Zoe": 0.494,
    
    # ADC (Bot)
    "Ezreal": 0.482, "KaiSa": 0.495, "Jinx": 0.516, "Caitlyn": 0.491, "Jhin": 0.512,
    "Vayne": 0.508, "Ashe": 0.520, "Lucian": 0.484, "Samira": 0.503, "Xayah": 0.492,
    "Twitch": 0.513, "Aphelios": 0.468, "Tristana": 0.496, "Zeri": 0.481, "MissFortune": 0.518,
    "Draven": 0.497, "Varus": 0.489, "KogMaw": 0.522, "Kalista": 0.478, "Sivir": 0.501,
    
    # Support
    "Thresh": 0.498, "Lulu": 0.494, "Nami": 0.502, "Nautilus": 0.491, "Blitzcrank": 0.513,
    "Leona": 0.516, "Karma": 0.489, "Yuumi": 0.462, "Milio": 0.505, "Rakan": 0.508,
    "Braum": 0.511, "Janna": 0.524, "Soraka": 0.509, "Senna": 0.501, "Morgana": 0.495,
    "Pyke": 0.499, "Alistar": 0.502, "Bard": 0.514, "Renata": 0.497, "Lux": 0.496
}

# 특수 시너지 보너스 (두 챔피언 조합)
CHAMPION_SYNERGIES = {
    frozenset(["Lulu", "KogMaw"]): 0.040,       # 코그모-룰루 조합
    frozenset(["Yasuo", "Gragas"]): 0.035,      # 야스오-그라가스 조합
    frozenset(["Yasuo", "Malphite"]): 0.030,   # 야스오-말파이트 조합
    frozenset(["Lucian", "Nami"]): 0.030,       # 루시안-나미 조합
    frozenset(["Rakan", "Xayah"]): 0.025,       # 자야-라칸 연인 조합
    frozenset(["Nautilus", "Samira"]): 0.025,   # 사미라-노틸러스 조합
    frozenset(["Amumu", "MissFortune"]): 0.020,  # 아무무-미포 조합
    frozenset(["JarvanIV", "Orianna"]): 0.025,  # 자르반-오리아나 조합
    frozenset(["Milio", "Jinx"]): 0.020,        # 밀리오-징크스 조합
    frozenset(["Braum", "Lucian"]): 0.020       # 루시안-브라움 조합
}

# 카운터 픽 보너스 ((챔피언A, 챔피언B) -> A가 B 상대로 갖는 보너스)
CHAMPION_COUNTERS = {
    ("Caitlyn", "Vayne"): 0.025,        # 케이틀린의 베인 카운터
    ("Morgana", "Blitzcrank"): 0.025,   # 모르가나의 블리츠 카운터
    ("Morgana", "Nautilus"): 0.020,     # 모르가나의 노틸 카운터
    ("Kassadin", "Veigar"): 0.030,      # 카사딘의 베이가 카운터
    ("Sylas", "Malphite"): 0.030,       # 사일러스의 말파이트 카운터
    ("Fiora", "Aatrox"): 0.020,         # 피오라의 아트록스 카운터
    ("Poppy", "LeeSin"): 0.025,         # 뽀삐의 리신 카운터
    ("Jax", "MasterYi"): 0.030,         # 잭스의 마이 카운터
    ("Vayne", "DrMundo"): 0.025,        # 베인의 문도 카운터
    ("Teemo", "Nasus"): 0.020,          # 티모의 나서스 카운터
    ("Zed", "Veigar"): 0.020,           # 제드의 베이가 카운터
    ("Cassiopeia", "Ryze"): 0.020,      # 카시오페아의 라이즈 카운터
    ("Olaf", "Sejuani"): 0.025          # 올라프의 세주아니 카운터
}

# 한국어 챔피언 이름 맵핑
CHAMPION_NAMES_KR = {
    "Aatrox": "아트록스", "Ahri": "아리", "Akali": "아칼리", "Alistar": "알리스타", 
    "Amumu": "아무무", "Anivia": "애니비아", "Annie": "애니", "Aphelios": "아펠리오스", 
    "Ashe": "애쉬", "AurelionSol": "아우렐리온 솔", "Azir": "아지르", "Bard": "바드", 
    "Belveth": "벨베스", "Blitzcrank": "블리츠크랭크", "Brand": "브랜드", "Braum": "브라움", 
    "Briar": "브라이어", "Caitlyn": "케이틀린", "Camille": "카밀", "Cassiopeia": "카시오페아", 
    "Chogath": "초가스", "Corki": "코르키", "Darius": "다리우스", "Diana": "다이아나", 
    "DrMundo": "문도 박사", "Draven": "드레이븐", "Ekko": "에코", "Elise": "엘리스", 
    "Evelynn": "이브린", "Ezreal": "이즈리얼", "Fiddlesticks": "피들스틱", "Fiora": "피오라", 
    "Fizz": "피즈", "Galio": "갈리오", "Gangplank": "갱플랭크", "Garen": "가렌", 
    "Gnar": "나르", "Gragas": "그라가스", "Graves": "그레이브즈", "Gwen": "그웬", 
    "Hecarim": "헤카림", "Heimerdinger": "하이머딩거", "Hwei": "흐웨이", "Illaoi": "일라오이", 
    "Irelia": "이렐리아", "Ivern": "아이번", "Janna": "잔나", "JarvanIV": "자르반 4세", 
    "Jax": "잭스", "Jayce": "제이스", "Jhin": "진", "Jinx": "징크스", 
    "Ksante": "크산테", "Kaisa": "카이사", "Kalista": "칼리스타", "Karma": "카르마", 
    "Karthus": "카서스", "Kassadin": "카사딘", "Katarina": "카타리나", "Kayle": "케일", 
    "Kayn": "케인", "Kennen": "케넨", "Khazix": "카직스", "Kindred": "킨드레드", 
    "Kled": "클레드", "KogMaw": "코그모", "Leblanc": "르블랑", "LeeSin": "리신", 
    "Leona": "레오나", "Lillia": "릴리아", "Lissandra": "리스안드라", "Lucian": "루시안", 
    "Lulu": "룰루", "Lux": "럭스", "Malphite": "말파이트", "Malzahar": "말자하", 
    "Maokai": "마오카이", "MasterYi": "마스터 이", "Milio": "밀리오", "MissFortune": "미스 포츈", 
    "Mordekaiser": "모데카이저", "Morgana": "모르가나", "Naafiri": "나아피리", "Nami": "나미", 
    "Nasus": "나서스", "Nautilus": "노틸러스", "Neeko": "니코", "Nidalee": "니달리", 
    "Nilah": "닐라", "Nocturne": "녹턴", "Nunu": "누누와 윌럼프", "Olaf": "올라프", 
    "Orianna": "오리아나", "Ornn": "오른", "Pantheon": "판테온", "Poppy": "뽀삐", 
    "Pyke": "파이크", "Qiyana": "키아나", "Quinn": "퀸", "Rakan": "라칸", 
    "Rammus": "람머스", "RekSai": "렉사이", "Rell": "렐", "Renata": "레나타 글라스크", 
    "Renekton": "레넥톤", "Rengar": "렝가", "Riven": "리븐", "Rumble": "럼블", 
    "Ryze": "라이즈", "Samira": "사미라", "Sejuani": "세주아니", "Senna": "세나", 
    "Seraphine": "세라핀", "Sett": "세트", "Shaco": "샤코", "Shen": "쉔", 
    "Shyvana": "쉬바나", "Singed": "신지드", "Sion": "사이온", "Sivir": "시비르", 
    "Skarner": "스카너", "Sona": "소나", "Soraka": "소라카", "Swain": "스웨인", 
    "Sylas": "사일러스", "Syndra": "신드라", "TahmKench": "탐 켄치", "Taliyah": "탈리야", 
    "Talon": "탈론", "Taric": "타릭", "Teemo": "티모", "Thresh": "쓰레쉬", 
    "Tristana": "트리스타나", "Trundle": "트런들", "Tryndamere": "트린다미어", 
    "TwistedFate": "트위스티드 페이트", "Twitch": "트위치", "Udyr": "우디르", 
    "Urgot": "우르곳", "Varus": "바루스", "Vayne": "베인", "Veigar": "베이가", 
    "Velkoz": "벨코즈", "Vex": "벡스", "Vi": "바이", "Viego": "비에고", 
    "Viktor": "빅토르", "Vladimir": "블라디미르", "Volibear": "볼리베어", "Warwick": "워윅", 
    "Wukong": "오공", "Xayah": "자야", "Xerath": "제라스", "XinZhao": "신 짜오", 
    "Yasuo": "야스오", "Yone": "요네", "Yorick": "요릭", "Yuumi": "유미", 
    "Zac": "자크", "Zed": "제드", "Zeri": "제리", "Ziggs": "직스", 
    "Zilean": "질리언", "Zoe": "조이", "Zyra": "자이라"
}

def get_champion_name_kr(champ_id):
    return CHAMPION_NAMES_KR.get(champ_id, champ_id)

def calculate_composition_scores(blue_champions, red_champions, model_name="XGBoost"):
    """5v5 밴픽 조합 기반 지표 평가"""
    # 머신러닝 모델 기반 동적 승률 로드
    ml_rates = {}
    ml_rates_path = os.path.join(MODELS_DIR, "champion_ml_win_rates.json")
    if os.path.exists(ml_rates_path):
        try:
            with open(ml_rates_path, "r", encoding="utf-8") as f:
                ml_rates = json.load(f)
        except Exception:
            pass
            
    # 선택된 모델 전용 승률 테이블 사용 (로딩 실패 또는 키 부재 시 하드코딩 폴백)
    win_rates_table = ml_rates.get(model_name, CHAMPION_BASE_WIN_RATES)
    if not win_rates_table:
        win_rates_table = CHAMPION_BASE_WIN_RATES

    blue_bases = [win_rates_table.get(c, 0.50) for c in blue_champions if c]
    red_bases = [win_rates_table.get(c, 0.50) for c in red_champions if c]
    
    blue_base_avg = sum(blue_bases) / len(blue_bases) if blue_bases else 0.50
    red_base_avg = sum(red_bases) / len(red_bases) if red_bases else 0.50
    
    blue_score = blue_base_avg
    red_score = red_base_avg
    
    blue_synergies_detected = []
    red_synergies_detected = []
    counters_detected = []
    
    # 시너지 평가
    for i in range(len(blue_champions)):
        for j in range(i + 1, len(blue_champions)):
            c1, c2 = blue_champions[i], blue_champions[j]
            if not c1 or not c2: continue
            pair = frozenset([c1, c2])
            if pair in CHAMPION_SYNERGIES:
                bonus = CHAMPION_SYNERGIES[pair]
                blue_score += bonus
                blue_synergies_detected.append({
                    "champions": [c1, c2],
                    "names_kr": [get_champion_name_kr(c1), get_champion_name_kr(c2)],
                    "bonus": bonus
                })
                
    for i in range(len(red_champions)):
        for j in range(i + 1, len(red_champions)):
            c1, c2 = red_champions[i], red_champions[j]
            if not c1 or not c2: continue
            pair = frozenset([c1, c2])
            if pair in CHAMPION_SYNERGIES:
                bonus = CHAMPION_SYNERGIES[pair]
                red_score += bonus
                red_synergies_detected.append({
                    "champions": [c1, c2],
                    "names_kr": [get_champion_name_kr(c1), get_champion_name_kr(c2)],
                    "bonus": bonus
                })
                
    # 카운터픽 평가
    for b_champ in blue_champions:
        for r_champ in red_champions:
            if not b_champ or not r_champ: continue
            
            if (b_champ, r_champ) in CHAMPION_COUNTERS:
                bonus = CHAMPION_COUNTERS[(b_champ, r_champ)]
                blue_score += bonus
                red_score -= bonus
                counters_detected.append({
                    "winner_team": "blue",
                    "counter": b_champ,
                    "counter_kr": get_champion_name_kr(b_champ),
                    "victim": r_champ,
                    "victim_kr": get_champion_name_kr(r_champ),
                    "bonus": bonus
                })
                
            if (r_champ, b_champ) in CHAMPION_COUNTERS:
                bonus = CHAMPION_COUNTERS[(r_champ, b_champ)]
                red_score += bonus
                blue_score -= bonus
                counters_detected.append({
                    "winner_team": "red",
                    "counter": r_champ,
                    "counter_kr": get_champion_name_kr(r_champ),
                    "victim": b_champ,
                    "victim_kr": get_champion_name_kr(b_champ),
                    "bonus": bonus
                })
                
    blue_score = max(0.40, min(0.60, blue_score))
    red_score = max(0.40, min(0.60, red_score))
    
    return {
        "blue_score": round(blue_score, 4),
        "red_score": round(red_score, 4),
        "blue_synergies": blue_synergies_detected,
        "red_synergies": red_synergies_detected,
        "counters": counters_detected
    }

CHAMPION_TAGS = {}

def initialize_champion_tags():
    global CHAMPION_TAGS
    fallback_tags = {
        "Aatrox": "Fighter", "Ahri": "Mage", "Akali": "Assassin", "Akshan": "Marksman",
        "Alistar": "Tank", "Amumu": "Tank", "Anivia": "Mage", "Annie": "Mage",
        "Aphelios": "Marksman", "Ashe": "Marksman", "AurelionSol": "Mage", "Azir": "Mage",
        "Bard": "Support", "Belveth": "Fighter", "Blitzcrank": "Tank", "Brand": "Mage",
        "Braum": "Support", "Briar": "Fighter", "Caitlyn": "Marksman", "Camille": "Fighter",
        "Cassiopeia": "Mage", "Chogath": "Tank", "Corki": "Marksman", "Darius": "Fighter",
        "Diana": "Fighter", "DrMundo": "Fighter", "Draven": "Marksman",
        "Ekko": "Assassin", "Elise": "Mage", "Evelynn": "Assassin", "Ezreal": "Marksman",
        "FiddleSticks": "Mage", "Fiora": "Fighter", "Fizz": "Assassin", "Galio": "Tank",
        "Gangplank": "Fighter", "Garen": "Fighter", "Gnar": "Fighter", "Gragas": "Fighter",
        "Graves": "Marksman", "Gwen": "Fighter", "Hecarim": "Fighter", "Heimerdinger": "Mage",
        "Hwei": "Mage", "Illaoi": "Fighter", "Irelia": "Fighter", "Ivern": "Support",
        "Janna": "Support", "JarvanIV": "Fighter", "Jax": "Fighter", "Jayce": "Fighter",
        "Jhin": "Marksman", "Jinx": "Marksman", "KSante": "Tank", "Kaisa": "Marksman",
        "Kalista": "Marksman", "Karma": "Mage", "Karthus": "Mage", "Kassadin": "Assassin",
        "Katarina": "Assassin", "Kayle": "Fighter", "Kayn": "Fighter", "Kennen": "Mage",
        "Khazix": "Assassin", "Kindred": "Marksman", "Kled": "Fighter", "KogMaw": "Marksman",
        "Leblanc": "Assassin", "LeeSin": "Fighter", "Leona": "Tank", "Lillia": "Fighter",
        "Lissandra": "Mage", "Lucian": "Marksman", "Lulu": "Support", "Lux": "Mage",
        "Malphite": "Tank", "Malzahar": "Mage", "Maokai": "Tank", "MasterYi": "Assassin",
        "Milio": "Support", "MissFortune": "Marksman", "MonkeyKing": "Fighter", "Mordekaiser": "Fighter",
        "Morgana": "Mage", "Naafiri": "Assassin", "Nami": "Support", "Nasus": "Fighter",
        "Nautilus": "Tank", "Neeko": "Mage", "Nidalee": "Assassin", "Nilah": "Fighter",
        "Nocturne": "Assassin", "Nunu": "Tank", "Olaf": "Fighter", "Orianna": "Mage",
        "Ornn": "Tank", "Pantheon": "Fighter", "Poppy": "Tank", "Pyke": "Assassin",
        "Qiyana": "Assassin", "Quinn": "Marksman", "Rakan": "Support", "Rammus": "Tank",
        "RekSai": "Fighter", "Rell": "Tank", "Renata": "Support", "Renekton": "Fighter",
        "Rengar": "Assassin", "Riven": "Fighter", "Rumble": "Fighter", "Ryze": "Mage",
        "Samira": "Marksman", "Sejuani": "Tank", "Senna": "Marksman", "Seraphine": "Mage",
        "Sett": "Fighter", "Shaco": "Assassin", "Shen": "Tank", "Shyvana": "Fighter",
        "Singed": "Tank", "Sion": "Tank", "Sivir": "Marksman", "Skarner": "Fighter",
        "Smolder": "Marksman", "Sona": "Support", "Soraka": "Support", "Swain": "Mage",
        "Sylas": "Mage", "Syndra": "Mage", "TahmKench": "Support", "Taliyah": "Mage",
        "Talon": "Assassin", "Taric": "Support", "Teemo": "Marksman", "Thresh": "Support",
        "Tristana": "Marksman", "Trundle": "Fighter", "Tryndamere": "Fighter", "TwistedFate": "Mage",
        "Twitch": "Marksman", "Udyr": "Fighter", "Urgot": "Fighter", "Varus": "Marksman",
        "Vayne": "Marksman", "Veigar": "Mage", "Velkoz": "Mage", "Vex": "Mage",
        "Vi": "Fighter", "Viego": "Fighter", "Viktor": "Mage", "Vladimir": "Mage",
        "Volibear": "Fighter", "Warwick": "Fighter", "Xayah": "Marksman", "Xerath": "Mage",
        "XinZhao": "Fighter", "Yasuo": "Fighter", "Yone": "Assassin", "Yorick": "Fighter",
        "Yuumi": "Support", "Zac": "Tank", "Zed": "Assassin", "Zeri": "Marksman",
        "Ziggs": "Mage", "Zilean": "Support", "Zoe": "Mage", "Zyra": "Mage"
    }
    CHAMPION_TAGS.update(fallback_tags)
    
    # Riot Data Dragon에서 동적 가져오기
    import urllib.request
    url = "https://ddragon.leagueoflegends.com/cdn/14.22.1/data/ko_KR/champion.json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as response:
            data = json.loads(response.read().decode('utf-8'))
            champions_dict = data.get("data", {})
            for c_id, c_data in champions_dict.items():
                c_tags = c_data.get("tags", [])
                if c_tags:
                    CHAMPION_TAGS[c_id] = c_tags[0]
            print(f"Data Dragon에서 {len(champions_dict)}개 챔피언 태그 로드 성공.")
    except Exception as e:
        print(f"Data Dragon 태그 로드 실패 (폴백 사용): {str(e)}")

# 태그 데이터 기동 시 사전 로드
initialize_champion_tags()

def get_champion_tags(champions_list):
    tags = []
    for c in champions_list:
        if not c:
            tags.append("Unknown")
            continue
        tag = CHAMPION_TAGS.get(c, "Unknown")
        tags.append(tag)
    return tags

def determine_composition(tags):
    tank_count = tags.count('Tank')
    bruiser_count = tags.count('Fighter')
    assassin_count = tags.count('Assassin')
    carry_count = tags.count('Marksman')
    
    if bruiser_count >= 3:
        return '브루저조합'
    elif assassin_count >= 2:
        return '암살자조합'
    elif tank_count >= 3:
        return '전체탱커'
    elif carry_count >= 2 and tags.count('Support') >= 1:
        return '하이퍼캐리'
    else:
        return '혼합조합'

# ==============================================================================

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

def run_model_inference(model_name, feature_dict, feature_order):
    """
    주어진 feature_dict와 feature_order를 바탕으로 특정 모델의 승률(블루팀 승리 확률)을 계산합니다.
    """
    input_values = [feature_dict.get(f, 0.0) for f in feature_order]
    
    if model_name == "Logistic Regression":
        # JSON 기반 무의존성 추론
        scaler_file = os.path.join(MODELS_DIR, "scaler.json")
        lr_file = os.path.join(MODELS_DIR, "logistic_regression.json")
        
        with open(scaler_file, "r") as f:
            scaler_data = json.load(f)
            scaler_mean = scaler_data["mean"]
            scaler_scale = scaler_data["scale"]
            
        with open(lr_file, "r") as f:
            lr_data = json.load(f)
            intercept = lr_data["intercept"]
            coefficients = lr_data["coefficients"]
        
        X_scaled = [(x_i - mean_i) / (scale_i if scale_i != 0 else 1.0) for x_i, mean_i, scale_i in zip(input_values, scaler_mean, scaler_scale)]
        margin = intercept + sum(x_i * coef_i for x_i, coef_i in zip(X_scaled, coefficients))
        return 1.0 / (1.0 + np.exp(-margin))
        
    elif model_name == "Random Forest":
        # JSON 기반 트리 순회 무의존성 추론
        rf_file = os.path.join(MODELS_DIR, "random_forest.json")
        with open(rf_file, "r") as f:
            rf_trees = json.load(f)
            
        total_prob = 0.0
        for nodes in rf_trees:
            node_id = 0
            while True:
                node = nodes[node_id]
                if isinstance(node, (int, float)): # Leaf
                    total_prob += node
                    break
                # Split node: [feature_idx, threshold, left, right]
                feat_idx, thresh, left, right = node
                if input_values[feat_idx] <= thresh:
                    node_id = left
                else:
                    node_id = right
        return total_prob / len(rf_trees)
        
    elif model_name == "XGBoost":
        # 모듈 캐싱 문제 방지를 위해 sys.modules에서 제거 후 로드
        if 'models.xgboost_code' in sys.modules:
            importlib.reload(sys.modules['models.xgboost_code'])
        from models.xgboost_code import score as xgb_score
        proba = xgb_score(input_values)
        return proba[1]
    else:
        raise ValueError(f"Invalid model name: {model_name}")

def calculate_ml_composition_score(model_name, blue_champs, red_champs, feature_order):
    """
    모든 경제적 지표를 동등(격차 0)하게 맞춘 상태에서 챔피언 조합만으로 얻어지는 모델 예측 승률을
    해당 알고리즘의 조합 점수(Composition Score)로 계산합니다.
    """
    # 양 팀 챔피언이 한 명도 선택되지 않은 경우 조합 점수는 대칭인 0.50 (50%) 반환
    if not any(blue_champs) and not any(red_champs):
        return 0.50
        
    # 1. 중립 경제 피처 구축 (input_data={} 전달 시 기본값 탑재)
    feature_dict = build_lane_features({})
    
    # 빈 슬롯 채우기 (최대 5명)
    blue_champs_full = list(blue_champs)
    red_champs_full = list(red_champs)
    while len(blue_champs_full) < 5: blue_champs_full.append("")
    while len(red_champs_full) < 5: red_champs_full.append("")
    
    blue_tags = get_champion_tags(blue_champs_full)
    red_tags = get_champion_tags(red_champs_full)
    blue_comp_name = determine_composition(blue_tags)
    red_comp_name = determine_composition(red_tags)
    
    roles = ['top', 'jungle', 'middle', 'bottom', 'utility']
    for i, role in enumerate(roles):
        feature_dict[f'blue_{role}_tag_{blue_tags[i]}'] = 1.0
        feature_dict[f'red_{role}_tag_{red_tags[i]}'] = 1.0
        
    feature_dict[f'blue_comp_{blue_comp_name}'] = 1.0
    feature_dict[f'red_comp_{red_comp_name}'] = 1.0
    
    # 3. 챔피언 멀티핫 피처 탑재
    for champ in blue_champs_full:
        if champ:
            feature_dict[f'blue_champion_{champ}'] = 1.0
    for champ in red_champs_full:
        if champ:
            feature_dict[f'red_champion_{champ}'] = 1.0
            
    # 4. 모델 추론
    try:
        blue_prob = run_model_inference(model_name, feature_dict, feature_order)
        return float(blue_prob)
    except Exception:
        return 0.5

def calculate_dragon_gold_value(model_name, full_input, feature_order):
    """
    편미분을 이용해 드래곤 1마리가 승률에 미치는 영향을 골드 가치로 환산합니다.
    """
    def get_prob(inp_dict):
        try:
            return run_model_inference(model_name, inp_dict, feature_order)
        except Exception:
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
    out['blue_voidgrubs'] = float(input_data.get('blueEliteMonsters', 0))
    
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

    # 챔피언 멀티핫 피처 추가 (기본 0, 일치하면 1)
    for champ in blue_champs:
        if champ:
            feature_dict[f'blue_champion_{champ}'] = 1.0
    for champ in red_champs:
        if champ:
            feature_dict[f'red_champion_{champ}'] = 1.0

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
        
    try:
        # 모델 추론 수행
        try:
            blue_win_prob = run_model_inference(model_name, feature_dict, feature_order)
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
            
        prediction = 1 if blue_win_prob >= 0.5 else 0
        
        # 드래곤 가치 편미분 계산
        dragon_val = calculate_dragon_gold_value(model_name, feature_dict, feature_order)
        
        # 챔피언 조합 점수 연산 (선택한 머신러닝 모델 기반)
        blue_comp_score = calculate_ml_composition_score(model_name, blue_champs, red_champs, feature_order)
        red_comp_score = 1.0 - blue_comp_score
        
        # UI 시너지/카운터 텍스트 바인딩 연산 (선택한 모델의 동적 승률 적용)
        comp_details = calculate_composition_scores(blue_champs, red_champs, model_name=model_name)
        
        return jsonify({
            "model_used": model_name,
            "prediction": prediction,
            "winner": "Blue" if prediction == 1 else "Red",
            "blue_win_probability": float(blue_win_prob),
            "red_win_probability": float(1.0 - blue_win_prob),
            "dragon_gold_value": float(dragon_val),
            "blue_comp_score": float(blue_comp_score),
            "red_comp_score": float(red_comp_score),
            "blue_synergies": comp_details["blue_synergies"],
            "red_synergies": comp_details["red_synergies"],
            "counters": comp_details["counters"]
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
        return jsonify({"error": f"학습 중 오류 발생: {str(e)}"}), 500

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
