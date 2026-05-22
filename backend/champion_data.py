# -*- coding: utf-8 -*-
"""
Champion database and draft composition evaluation engine.
"""

# Base win rates for popular champions (defaults to 0.50 if not specified)
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

# Special synergies: frozenset of two champions -> win rate bonus
CHAMPION_SYNERGIES = {
    frozenset(["Lulu", "KogMaw"]): 0.040,       # Legendary Kog-Lulu hypercarry combo
    frozenset(["Yasuo", "Gragas"]): 0.035,      # Gragas explosive cask setup for Yasuo ult
    frozenset(["Yasuo", "Malphite"]): 0.030,   # Malphite unstoppable force setup for Yasuo ult
    frozenset(["Lucian", "Nami"]): 0.030,       # Lucian double shot procs Nami E
    frozenset(["Rakan", "Xayah"]): 0.025,       # Lover's duo specialized synergy
    frozenset(["Nautilus", "Samira"]): 0.025,   # Heavy CC triggers Samira passive
    frozenset(["Amumu", "MissFortune"]): 0.020,  # Double AoE ultimate combo
    frozenset(["JarvanIV", "Orianna"]): 0.025,  # Shockwave inside Cataclysm
    frozenset(["Milio", "Jinx"]): 0.020,        # Milio range extension for Jinx rockets
    frozenset(["Braum", "Lucian"]): 0.020       # Lucian passive triggers Braum stun quickly
}

# Counter-picks: (champion_A, champion_B) -> win rate bonus for A against B
# e.g., ("Caitlyn", "Vayne") means Caitlyn counters Vayne (+2.5% win rate for Caitlyn's team)
CHAMPION_COUNTERS = {
    ("Caitlyn", "Vayne"): 0.025,        # Caitlyn range harass in lane
    ("Morgana", "Blitzcrank"): 0.025,   # Black Shield blocks hook
    ("Morgana", "Nautilus"): 0.020,     # Black Shield blocks cc
    ("Kassadin", "Veigar"): 0.030,      # Kassadin magic shield + riftwalk out of cage
    ("Sylas", "Malphite"): 0.030,       # Sylas steals a high-value tank ultimate
    ("Fiora", "Aatrox"): 0.020,         # Fiora out-duels and parries Aatrox Q3
    ("Poppy", "LeeSin"): 0.025,         # Poppy W blocks Lee Sin's Q2 dash
    ("Jax", "MasterYi"): 0.030,         # Jax E blocks Master Yi's basic attacks
    ("Vayne", "DrMundo"): 0.025,        # Vayne silver bolts shred Mundo's max HP tanking
    ("Teemo", "Nasus"): 0.020,          # Teemo blind disables Nasus Q farming
    ("Zed", "Veigar"): 0.020,           # Zed shadows bypass Veigar's stun cage
    ("Cassiopeia", "Ryze"): 0.020,      # Grounding prevents Ryze from kiting
    ("Olaf", "Sejuani"): 0.025          # Olaf ult makes him immune to Sejuani's stuns
}

# Champion names dictionary for pretty display
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

def calculate_composition_scores(blue_champions, red_champions):
    """
    Evaluates 5v5 team draft composition.
    
    Returns:
        dict: {
            "blue_score": float,
            "red_score": float,
            "blue_synergies": list of dict,
            "red_synergies": list of dict,
            "counters": list of dict
        }
    """
    # 1. Base Win Rates (if champion is empty or not in database, default to 0.50)
    blue_bases = [CHAMPION_BASE_WIN_RATES.get(c, 0.50) for c in blue_champions if c]
    red_bases = [CHAMPION_BASE_WIN_RATES.get(c, 0.50) for c in red_champions if c]
    
    # Calculate average base win rates
    blue_base_avg = sum(blue_bases) / len(blue_bases) if blue_bases else 0.50
    red_base_avg = sum(red_bases) / len(red_bases) if red_bases else 0.50
    
    # Start accumulation
    blue_score = blue_base_avg
    red_score = red_base_avg
    
    blue_synergies_detected = []
    red_synergies_detected = []
    counters_detected = []
    
    # 2. Synergy Bonuses
    # Check Blue Team Synergies
    for i in range(len(blue_champions)):
        for j in range(i + 1, len(blue_champions)):
            c1, c2 = blue_champions[i], blue_champions[j]
            if not c1 or not c2:
                continue
            pair = frozenset([c1, c2])
            if pair in CHAMPION_SYNERGIES:
                bonus = CHAMPION_SYNERGIES[pair]
                blue_score += bonus
                blue_synergies_detected.append({
                    "champions": [c1, c2],
                    "names_kr": [get_champion_name_kr(c1), get_champion_name_kr(c2)],
                    "bonus": bonus
                })
                
    # Check Red Team Synergies
    for i in range(len(red_champions)):
        for j in range(i + 1, len(red_champions)):
            c1, c2 = red_champions[i], red_champions[j]
            if not c1 or not c2:
                continue
            pair = frozenset([c1, c2])
            if pair in CHAMPION_SYNERGIES:
                bonus = CHAMPION_SYNERGIES[pair]
                red_score += bonus
                red_synergies_detected.append({
                    "champions": [c1, c2],
                    "names_kr": [get_champion_name_kr(c1), get_champion_name_kr(c2)],
                    "bonus": bonus
                })
                
    # 3. Counter-pick Matchups
    for b_champ in blue_champions:
        for r_champ in red_champions:
            if not b_champ or not r_champ:
                continue
            
            # If Blue counters Red
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
                
            # If Red counters Blue
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
                
    # Clamp final scores between 0.40 and 0.60 to prevent extreme skewing
    blue_score = max(0.40, min(0.60, blue_score))
    red_score = max(0.40, min(0.60, red_score))
    
    return {
        "blue_score": round(blue_score, 4),
        "red_score": round(red_score, 4),
        "blue_synergies": blue_synergies_detected,
        "red_synergies": red_synergies_detected,
        "counters": counters_detected
    }
