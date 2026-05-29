import lrModel from '../../models/logistic_regression.json';
import rfModel from '../../models/random_forest.json';
import scaler from '../../models/scaler.json';
import featureOrder from '../../models/feature_names.json';
import mlWinRates from '../../models/champion_ml_win_rates.json';
import { score as xgbScore } from '../../models/xgboost_code.js';

// 챔피언 한국어 이름 맵핑
export const CHAMPION_NAMES_KR = {
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
};

// 챔피언 기본 태그
export const CHAMPION_TAGS = {
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
};

// 인기 챔피언 기본 승률
export const CHAMPION_BASE_WIN_RATES = {
    "Aatrox": 0.502, "Fiora": 0.512, "Jax": 0.508, "Malphite": 0.515, "Ornn": 0.505,
    "Renekton": 0.485, "Riven": 0.501, "Camille": 0.510, "Darius": 0.503, "Gnar": 0.482,
    "Kled": 0.514, "Mordekaiser": 0.504, "Sion": 0.490, "Teemo": 0.480, "Nasus": 0.495,
    "Jayce": 0.475, "Rumble": 0.506, "Ksante": 0.468, "Yorick": 0.511, "Garen": 0.518,
    "LeeSin": 0.486, "Graves": 0.492, "Viego": 0.498, "KhaZix": 0.507, "Kayn": 0.501,
    "Elise": 0.504, "Nidalee": 0.472, "Nocturne": 0.521, "JarvanIV": 0.506, "Hecarim": 0.495,
    "Sejuani": 0.497, "Maokai": 0.512, "Zac": 0.518, "Rammus": 0.519, "Evelynn": 0.508,
    "Shaco": 0.499, "XinZhao": 0.510, "Belveth": 0.515, "Briar": 0.510, "Amumu": 0.513,
    "Ahri": 0.514, "Yasuo": 0.488, "Yone": 0.486, "Zed": 0.491, "Sylas": 0.495,
    "Orianna": 0.493, "Syndra": 0.497, "Azir": 0.465, "Talon": 0.511, "Katarina": 0.496,
    "Kassadin": 0.509, "Veigar": 0.502, "Viktor": 0.499, "LeBlanc": 0.484, "Ryze": 0.472,
    "Akali": 0.487, "Taliyah": 0.512, "Hwei": 0.480, "Anivia": 0.523, "Zoe": 0.494,
    "Ezreal": 0.482, "KaiSa": 0.495, "Jinx": 0.516, "Caitlyn": 0.491, "Jhin": 0.512,
    "Vayne": 0.508, "Ashe": 0.520, "Lucian": 0.484, "Samira": 0.503, "Xayah": 0.492,
    "Twitch": 0.513, "Aphelios": 0.468, "Tristana": 0.496, "Zeri": 0.481, "MissFortune": 0.518,
    "Draven": 0.497, "Varus": 0.489, "KogMaw": 0.522, "Kalista": 0.478, "Sivir": 0.501,
    "Thresh": 0.498, "Lulu": 0.494, "Nami": 0.502, "Nautilus": 0.491, "Blitzcrank": 0.513,
    "Leona": 0.516, "Karma": 0.489, "Yuumi": 0.462, "Milio": 0.505, "Rakan": 0.508,
    "Braum": 0.511, "Janna": 0.524, "Soraka": 0.509, "Senna": 0.501, "Morgana": 0.495,
    "Pyke": 0.499, "Alistar": 0.502, "Bard": 0.514, "Renata": 0.497, "Lux": 0.496
};

// 챔피언 한글 이름 가져오기
export function getChampionNameKr(champId) {
    return CHAMPION_NAMES_KR[champId] || champId;
}

// 챔피언 태그 가져오기
export function getChampionTags(championsList) {
    return championsList.map(c => {
        if (!c) return "Unknown";
        return CHAMPION_TAGS[c] || "Unknown";
    });
}

// 챔피언 조합 명칭 판별
export function determineComposition(tags) {
    const tankCount = tags.filter(t => t === 'Tank').length;
    const bruiserCount = tags.filter(t => t === 'Fighter').length;
    const assassinCount = tags.filter(t => t === 'Assassin').length;
    const carryCount = tags.filter(t => t === 'Marksman').length;
    
    if (bruiserCount >= 3) return '브루저조합';
    if (assassinCount >= 2) return '암살자조합';
    if (tankCount >= 3) return '전체탱커';
    if (carryCount >= 2 && tags.filter(t => t === 'Support').length >= 1) return '하이퍼캐리';
    return '혼합조합';
}

// 특수 시너지 보너스
export const CHAMPION_SYNERGIES = [
    { champs: ["Lulu", "KogMaw"], bonus: 0.040 },
    { champs: ["Yasuo", "Gragas"], bonus: 0.035 },
    { champs: ["Yasuo", "Malphite"], bonus: 0.030 },
    { champs: ["Lucian", "Nami"], bonus: 0.030 },
    { champs: ["Rakan", "Xayah"], bonus: 0.025 },
    { champs: ["Nautilus", "Samira"], bonus: 0.025 },
    { champs: ["Amumu", "MissFortune"], bonus: 0.020 },
    { champs: ["JarvanIV", "Orianna"], bonus: 0.025 },
    { champs: ["Milio", "Jinx"], bonus: 0.020 },
    { champs: ["Braum", "Lucian"], bonus: 0.020 }
];

// 카운터 관계
export const CHAMPION_COUNTERS = [
    { counter: "Caitlyn", victim: "Vayne", bonus: 0.025 },
    { counter: "Morgana", victim: "Blitzcrank", bonus: 0.025 },
    { counter: "Morgana", victim: "Nautilus", bonus: 0.020 },
    { counter: "Kassadin", victim: "Veigar", bonus: 0.030 },
    { counter: "Sylas", victim: "Malphite", bonus: 0.030 },
    { counter: "Fiora", victim: "Aatrox", bonus: 0.020 },
    { counter: "Poppy", victim: "LeeSin", bonus: 0.025 },
    { counter: "Jax", victim: "MasterYi", bonus: 0.030 },
    { counter: "Vayne", victim: "DrMundo", bonus: 0.025 },
    { counter: "Teemo", victim: "Nasus", bonus: 0.020 },
    { counter: "Zed", victim: "Veigar", bonus: 0.020 },
    { counter: "Cassiopeia", victim: "Ryze", bonus: 0.020 },
    { counter: "Olaf", victim: "Sejuani", bonus: 0.025 }
];

// 밴픽 조합 시너지 & 카운터 스코어 연산
export function calculateCompositionScores(blueChampions, redChampions, mlWinRates = null) {
    const winRatesTable = mlWinRates || CHAMPION_BASE_WIN_RATES;
    
    const blueBases = blueChampions.filter(c => c).map(c => winRatesTable[c] || 0.50);
    const redBases = redChampions.filter(c => c).map(c => winRatesTable[c] || 0.50);
    
    let blueScore = blueBases.length > 0 ? blueBases.reduce((a, b) => a + b, 0) / blueBases.length : 0.50;
    let redScore = redBases.length > 0 ? redBases.reduce((a, b) => a + b, 0) / redBases.length : 0.50;
    
    const blueSynergiesDetected = [];
    const redSynergiesDetected = [];
    const countersDetected = [];
    
    // 블루팀 시너지
    for (let i = 0; i < blueChampions.length; i++) {
        for (let j = i + 1; j < blueChampions.length; j++) {
            const c1 = blueChampions[i];
            const c2 = blueChampions[j];
            if (!c1 || !c2) continue;
            
            const synergy = CHAMPION_SYNERGIES.find(s => 
                (s.champs[0] === c1 && s.champs[1] === c2) || 
                (s.champs[0] === c2 && s.champs[1] === c1)
            );
            if (synergy) {
                blueScore += synergy.bonus;
                blueSynergiesDetected.push({
                    champions: [c1, c2],
                    names_kr: [getChampionNameKr(c1), getChampionNameKr(c2)],
                    bonus: synergy.bonus
                });
            }
        }
    }
    
    // 레드팀 시너지
    for (let i = 0; i < redChampions.length; i++) {
        for (let j = i + 1; j < redChampions.length; j++) {
            const c1 = redChampions[i];
            const c2 = redChampions[j];
            if (!c1 || !c2) continue;
            
            const synergy = CHAMPION_SYNERGIES.find(s => 
                (s.champs[0] === c1 && s.champs[1] === c2) || 
                (s.champs[0] === c2 && s.champs[1] === c1)
            );
            if (synergy) {
                redScore += synergy.bonus;
                redSynergiesDetected.push({
                    champions: [c1, c2],
                    names_kr: [getChampionNameKr(c1), getChampionNameKr(c2)],
                    bonus: synergy.bonus
                });
            }
        }
    }
    
    // 카운터 픽 연산
    for (const bChamp of blueChampions) {
        for (const rChamp of redChampions) {
            if (!bChamp || !rChamp) continue;
            
            // 블루가 레드를 카운터치는 경우
            const bCounter = CHAMPION_COUNTERS.find(c => c.counter === bChamp && c.victim === rChamp);
            if (bCounter) {
                blueScore += bCounter.bonus;
                redScore -= bCounter.bonus;
                countersDetected.push({
                    winner_team: "blue",
                    counter: bChamp,
                    counter_kr: getChampionNameKr(bChamp),
                    victim: rChamp,
                    victim_kr: getChampionNameKr(rChamp),
                    bonus: bCounter.bonus
                });
            }
            
            // 레드가 블루를 카운터치는 경우
            const rCounter = CHAMPION_COUNTERS.find(c => c.counter === rChamp && c.victim === bChamp);
            if (rCounter) {
                redScore += rCounter.bonus;
                blueScore -= rCounter.bonus;
                countersDetected.push({
                    winner_team: "red",
                    counter: rChamp,
                    counter_kr: getChampionNameKr(rChamp),
                    victim: bChamp,
                    victim_kr: getChampionNameKr(bChamp),
                    bonus: rCounter.bonus
                });
            }
        }
    }
    
    blueScore = Math.max(0.40, Math.min(0.60, blueScore));
    redScore = Math.max(0.40, Math.min(0.60, redScore));
    
    return {
        blue_score: parseFloat(blueScore.toFixed(4)),
        red_score: parseFloat(redScore.toFixed(4)),
        blue_synergies: blueSynergiesDetected,
        red_synergies: redSynergiesDetected,
        counters: countersDetected
    };
}

// 라인별 지표 분배 로직
export function buildLaneFeatures(inputData) {
    const roles = ['top', 'jungle', 'middle', 'bottom', 'utility'];
    const ratios = {
        'gold': [0.22, 0.19, 0.23, 0.24, 0.12],
        'cs': [0.25, 0.15, 0.27, 0.28, 0.05],
        'kills': [0.20, 0.25, 0.25, 0.25, 0.05],
        'deaths': [0.22, 0.18, 0.22, 0.20, 0.18]
    };
    
    const out = {};
    
    out['blue_dragons'] = parseFloat(inputData.blueDragons || 0);
    out['blue_heralds'] = parseFloat(inputData.blueHeralds || 0);
    out['blue_towers'] = parseFloat(inputData.blueTowersDestroyed || 0);
    out['blue_kills'] = parseFloat(inputData.blueKills || 0);
    out['blue_firstBlood'] = parseFloat(inputData.blueFirstBlood || 0);
    out['blue_voidgrubs'] = parseFloat(inputData.blueEliteMonsters || 0);
    
    out['red_dragons'] = parseFloat(inputData.redDragons || 0);
    out['red_heralds'] = parseFloat(inputData.redHeralds || 0);
    out['red_towers'] = parseFloat(inputData.redTowersDestroyed || 0);
    out['red_kills'] = parseFloat(inputData.redKills || 0);
    out['red_voidgrubs'] = parseFloat(inputData.redEliteMonsters || 0);
    
    const blue_gold = parseFloat(inputData.blueTotalGold || 16500);
    const red_gold = parseFloat(inputData.redTotalGold || 16500);
    const blue_cs = parseFloat(inputData.blueTotalMinionsKilled || 210);
    const red_cs = parseFloat(inputData.redTotalMinionsKilled || 210);
    const blue_k = parseFloat(inputData.blueKills || 5);
    const red_k = parseFloat(inputData.redKills || 5);
    const blue_d = parseFloat(inputData.blueDeaths || 5);
    const red_d = parseFloat(inputData.redDeaths || 5);
    
    for (let i = 0; i < roles.length; i++) {
        const role = roles[i];
        out[`blue_${role}_gold`] = blue_gold * ratios['gold'][i];
        out[`blue_${role}_cs`] = blue_cs * ratios['cs'][i];
        out[`blue_${role}_kills`] = blue_k * ratios['kills'][i];
        out[`blue_${role}_deaths`] = blue_d * ratios['deaths'][i];
        
        out[`red_${role}_gold`] = red_gold * ratios['gold'][i];
        out[`red_${role}_cs`] = red_cs * ratios['cs'][i];
        out[`red_${role}_kills`] = red_k * ratios['kills'][i];
        out[`red_${role}_deaths`] = red_d * ratios['deaths'][i];
        
        out[`${role}_gold_diff`] = out[`blue_${role}_gold`] - out[`red_${role}_gold`];
    }
    
    return out;
}

// Sigmoid 함수
function sigmoid(x) {
    if (x < 0.0) {
        const z = Math.exp(x);
        return z / (1.0 + z);
    }
    return 1.0 / (1.0 + Math.exp(-x));
}

// Random Forest 트리 탐색 함수
function predictRfTree(nodes, inputValues) {
    let nodeId = 0;
    while (true) {
        const node = nodes[nodeId];
        if (typeof node === 'number') {
            return node;
        }
        const [featIdx, threshold, left, right] = node;
        if (inputValues[featIdx] <= threshold) {
            nodeId = left;
        } else {
            nodeId = right;
        }
    }
}

// 개별 모델 추론
export function runModelInference(modelName, featureDict) {
    const inputValues = featureOrder.map(f => featureDict[f] || 0.0);
    
    if (modelName === "Logistic Regression") {
        const { mean, scale } = scaler;
        const { intercept, coefficients } = lrModel;
        
        // StandardScaler 변환
        const X_scaled = inputValues.map((x, i) => {
            const m = mean[i];
            const s = scale[i];
            return s !== 0 ? (x - m) / s : 0.0;
        });
        
        // 선형 결합
        let margin = intercept;
        for (let i = 0; i < X_scaled.length; i++) {
            margin += X_scaled[i] * coefficients[i];
        }
        return sigmoid(margin);
        
    } else if (modelName === "Random Forest") {
        // rfModel: Array of trees
        let totalProb = 0.0;
        for (let i = 0; i < rfModel.length; i++) {
            totalProb += predictRfTree(rfModel[i], inputValues);
        }
        return totalProb / rfModel.length;
        
    } else if (modelName === "XGBoost") {
        // m2cgen 컴파일된 함수 활용
        // xgbScore는 [1.0 - prob, prob] 형태로 반환됨
        const proba = xgbScore(inputValues);
        return proba[1];
    } else {
        throw new Error(`Invalid model name: ${modelName}`);
    }
}

// 챔피언 조합 점수 (모델 가중치 포함)
export function calculateMLCompositionScore(modelName, blueChamps, redChamps) {
    if (!blueChamps.some(c => c) && !redChamps.some(c => c)) {
        return 0.50;
    }
    
    // 1. 중립 기본 피처 구축
    const featureDict = buildLaneFeatures({});
    
    // 5개 완성
    const blueChampsFull = [...blueChamps];
    const redChampsFull = [...redChamps];
    while (blueChampsFull.length < 5) blueChampsFull.push("");
    while (redChampsFull.length < 5) redChampsFull.push("");
    
    const blueTags = getChampionTags(blueChampsFull);
    const redTags = getChampionTags(redChampsFull);
    const blueCompName = determineComposition(blueTags);
    const redCompName = determineComposition(redTags);
    
    const roles = ['top', 'jungle', 'middle', 'bottom', 'utility'];
    for (let i = 0; i < roles.length; i++) {
        const role = roles[i];
        featureDict[`blue_${role}_tag_${blueTags[i]}`] = 1.0;
        featureDict[`red_${role}_tag_${redTags[i]}`] = 1.0;
    }
    
    featureDict[`blue_comp_${blueCompName}`] = 1.0;
    featureDict[`red_comp_${redCompName}`] = 1.0;
    
    // 챔피언 멀티핫 피처 탑재
    blueChampsFull.forEach(c => {
        if (c) featureDict[`blue_champion_${c}`] = 1.0;
    });
    redChampsFull.forEach(c => {
        if (c) featureDict[`red_champion_${c}`] = 1.0;
    });
    
    try {
        return runModelInference(modelName, featureDict);
    } catch (e) {
        return 0.50;
    }
}

// 드래곤 편미분 골드 가치 환산
export function calculateDragonGoldValue(modelName, featureDict) {
    const getProb = (fDict) => {
        try {
            return runModelInference(modelName, fDict);
        } catch (e) {
            return 0.50;
        }
    };
    
    // 1. 현재 확률
    const pCurrent = getProb(featureDict);
    
    // 2. 드래곤 1마리 추가 시 승률 변동
    const currentDragons = featureDict['blue_dragons'] || 0;
    const dragonsChanged = currentDragons < 2 ? currentDragons + 1 : currentDragons - 1;
    const direction = currentDragons < 2 ? 1 : -1;
    
    const fDragonChanged = { ...featureDict, blue_dragons: dragonsChanged };
    const pDragonChanged = getProb(fDragonChanged);
    
    // 3. 골드 격차 100 증가 시 승률 변동
    const fGoldPlus = { ...featureDict };
    const goldIncrement = 100.0 / 5.0; // 5개 역할군 분배
    const roles = ['top', 'jungle', 'middle', 'bottom', 'utility'];
    roles.forEach(role => {
        fGoldPlus[`blue_${role}_gold`] = (fGoldPlus[`blue_${role}_gold`] || 0.0) + goldIncrement;
        fGoldPlus[`${role}_gold_diff`] = (fGoldPlus[`${role}_gold_diff`] || 0.0) + goldIncrement;
    });
    const pGoldPlus = getProb(fGoldPlus);
    
    const fGoldMinus = { ...featureDict };
    roles.forEach(role => {
        fGoldMinus[`blue_${role}_gold`] = (fGoldMinus[`blue_${role}_gold`] || 0.0) - goldIncrement;
        fGoldMinus[`${role}_gold_diff`] = (fGoldMinus[`${role}_gold_diff`] || 0.0) - goldIncrement;
    });
    const pGoldMinus = getProb(fGoldMinus);
    
    const dpDgold = (pGoldPlus - pGoldMinus) / 200.0;
    
    if (Math.abs(dpDgold) < 1e-7) {
        return 1500.0;
    }
    
    const dragonGoldValue = ((pDragonChanged - pCurrent) / direction) / dpDgold;
    
    if (dragonGoldValue < 0 || dragonGoldValue > 5000 || isNaN(dragonGoldValue)) {
        return 1500.0;
    }
    return dragonGoldValue;
}

// 메인 예측 통합 컨트롤러
export function predictMatch(modelName, rawInput, blueChamps, redChamps) {
    // 1. 챔피언 태그 및 밴픽 조합 판별
    const blueChampsFull = [...blueChamps];
    const redChampsFull = [...redChamps];
    while (blueChampsFull.length < 5) blueChampsFull.push("");
    while (redChampsFull.length < 5) redChampsFull.push("");
    
    const blueTags = getChampionTags(blueChampsFull);
    const redTags = getChampionTags(redChampsFull);
    const blueCompName = determineComposition(blueTags);
    const redCompName = determineComposition(redTags);
    
    // 2. 수치 지표 분배
    const featureDict = buildLaneFeatures(rawInput);
    
    // 3. 원핫 인코딩 피처 추가
    const roles = ['top', 'jungle', 'middle', 'bottom', 'utility'];
    for (let i = 0; i < roles.length; i++) {
        const role = roles[i];
        featureDict[`blue_${role}_tag_${blueTags[i]}`] = 1.0;
        featureDict[`red_${role}_tag_${redTags[i]}`] = 1.0;
    }
    featureDict[`blue_comp_${blueCompName}`] = 1.0;
    featureDict[`red_comp_${redCompName}`] = 1.0;
    
    // 챔피언 멀티핫 피처 추가
    blueChampsFull.forEach(c => {
        if (c) featureDict[`blue_champion_${c}`] = 1.0;
    });
    redChampsFull.forEach(c => {
        if (c) featureDict[`red_champion_${c}`] = 1.0;
    });
    
    // 4. 모델 추론
    const blueWinProb = runModelInference(modelName, featureDict);
    const redWinProb = 1.0 - blueWinProb;
    const prediction = blueWinProb >= 0.5 ? 1 : 0;
    
    // 5. 드래곤 가치 계산
    const dragonGoldVal = calculateDragonGoldValue(modelName, featureDict);
    
    return {
        model_used: modelName,
        prediction: prediction,
        winner: prediction === 1 ? "Blue" : "Red",
        blue_win_probability: blueWinProb,
        red_win_probability: redWinProb,
        dragon_gold_value: dragonGoldVal,
        mlWinRates: mlWinRates
    };
}
