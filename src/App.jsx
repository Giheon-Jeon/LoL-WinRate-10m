import React, { useState, useEffect, useRef } from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title as ChartTitle,
  Tooltip,
  Legend
} from 'chart.js';
import { X, Shield, Sword, Award, Eye, Coins, Trophy, Flame } from 'lucide-react';
import { getChampionNameKr, calculateCompositionScores, determineComposition, CHAMPION_NAMES_KR, runModelInference, calculateDragonGoldValue, calculateMLCompositionScore, ensembleSoftVoting } from './utils/lolEngine';
import metricsData from '../models/metrics.json';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ChartTitle,
  Tooltip,
  Legend
);

const MODEL_OPTIONS = [
  { value: "Ensemble", label: "🏆 앙상블: Soft Voting (추천)" },
  { value: "XGBoost", label: "최적화 모델: XGBoost" },
  { value: "Random Forest", label: "비교 모델: Random Forest" },
  { value: "Logistic Regression", label: "베이스라인: Logistic Regression" }
];

// 맵 마커 위치 좌표
const LANE_POSITIONS = {
  blue: {
    top: { top: '32%', left: '12%', label: '블루 탑', champIdx: 0 },
    jungle: { top: '70%', left: '30%', label: '블루 정글', champIdx: 1 },
    middle: { top: '58%', left: '42%', label: '블루 미드', champIdx: 2 },
    bottom: { top: '88%', left: '68%', label: '블루 바텀', champIdx: 3 }
  },
  red: {
    top: { top: '12%', left: '32%', label: '레드 탑', champIdx: 0 },
    jungle: { top: '30%', left: '70%', label: '레드 정글', champIdx: 1 },
    middle: { top: '42%', left: '58%', label: '레드 미드', champIdx: 2 },
    bottom: { top: '68%', left: '88%', label: '레드 바텀', champIdx: 3 }
  }
};

// 포지션별 라벨 및 기본 이모지 아이콘 정의
const LANE_LABELS = ["탑", "정글", "미드", "바텀(원딜)", "서폿"];
const LANE_ICONS = ["🛡️", "⚔️", "🔮", "🏹", "💚"];

// 초기 라인 데이터 템플릿
const INITIAL_LINE_STATS = {
  top: { gold: 3600, kills: 1, deaths: 1, assists: 0, cs: 50 },
  jungle: { gold: 3100, kills: 1, deaths: 1, assists: 1, cs: 45 },
  middle: { gold: 3800, kills: 1, deaths: 1, assists: 1, cs: 55 },
  bottom: { gold: 6000, kills: 2, deaths: 2, assists: 2, cs: 60 } // 바텀(원딜) + 유틸(서폿) 합산 듀오
};

export default function App() {
  const [modelName, setModelName] = useState("Ensemble");
  
  // 블루팀/레드팀 라인별 개별 데이터 (8개 그리드)
  const [blueLines, setBlueLines] = useState(JSON.parse(JSON.stringify(INITIAL_LINE_STATS)));
  const [redLines, setRedLines] = useState(JSON.parse(JSON.stringify(INITIAL_LINE_STATS)));
  
  // 현재 활성화된 라인 팝오버 (null 또는 { team: 'blue'|'red', lane: 'top'|'jungle'|'middle'|'bottom' })
  const [activePopover, setActivePopover] = useState(null);
  
  // 마우스 호버 상태 제어를 위한 타이머 Ref
  const hoverTimeoutRef = useRef(null);

  const handleMarkerMouseEnter = (team, lane) => {
    if (hoverTimeoutRef.current) {
      clearTimeout(hoverTimeoutRef.current);
      hoverTimeoutRef.current = null;
    }
    setActivePopover({ team, lane });
  };

  const handleMarkerMouseLeave = () => {
    if (hoverTimeoutRef.current) {
      clearTimeout(hoverTimeoutRef.current);
    }
    hoverTimeoutRef.current = setTimeout(() => {
      setActivePopover(null);
    }, 250); // 250ms의 넉넉한 틈을 제공하여 부드러운 호버 전환 지원
  };

  // 공통 오브젝트 및 시야 지표
  const [commonStats, setCommonStats] = useState({
    blueDragons: 0, redDragons: 0,
    blueHeralds: 0, redHeralds: 0,
    blueEliteMonsters: 0, redEliteMonsters: 0, // Voidgrubs (유충)
    blueTowersDestroyed: 0, redTowersDestroyed: 0,
    blueWardsPlaced: 15, redWardsPlaced: 15,
    blueWardsDestroyed: 2, redWardsDestroyed: 2,
    blueFirstBlood: 1, redFirstBlood: 0
  });

  const [selectedBlueChampions, setSelectedBlueChampions] = useState(["", "", "", "", ""]);
  const [selectedRedChampions, setSelectedRedChampions] = useState(["", "", "", "", ""]);
  const [championsList, setChampionsList] = useState([]);
  
  const [modalOpen, setModalOpen] = useState(false);
  const [activeSlot, setActiveSlot] = useState({ team: 'blue', index: 0 });
  const [searchTerm, setSearchTerm] = useState('');
  const [activeTab, setActiveTab] = useState('xgb');
  
  const [prediction, setPrediction] = useState({
    prediction: 1,
    winner: "Blue",
    blue_win_probability: 0.50,
    red_win_probability: 0.50,
    dragon_gold_value: 1500.0,
    blue_comp_score: 0.50,
    red_comp_score: 0.50,
    blue_synergies: [],
    red_synergies: [],
    counters: [],
    individualProbs: null
  });

  // 챔피언 목록 로드
  useEffect(() => {
    const fetchChampions = async () => {
      try {
        const res = await fetch("https://ddragon.leagueoflegends.com/cdn/14.22.1/data/ko_KR/champion.json");
        const data = await res.json();
        const champs = Object.keys(data.data).map(key => ({
          id: key,
          name: data.data[key].name,
          title: data.data[key].title,
          image: `https://ddragon.leagueoflegends.com/cdn/14.22.1/img/champion/${key}.png`
        }));
        champs.sort((a, b) => a.name.localeCompare(b.name, 'ko'));
        setChampionsList(champs);
      } catch (e) {
        const fallback = Object.keys(CHAMPION_NAMES_KR).map(key => ({
          id: key,
          name: CHAMPION_NAMES_KR[key],
          title: "",
          image: `https://ddragon.leagueoflegends.com/cdn/14.22.1/img/champion/${key}.png`
        }));
        fallback.sort((a, b) => a.name.localeCompare(b.name, 'ko'));
        setChampionsList(fallback);
      }
    };
    fetchChampions();
  }, []);

  // 8개 라인 변경 시 모델 인풋 피처 매핑 & 실시간 예측 실행
  useEffect(() => {
    // 1. 피처 객체 빌드 (사용자 라인별 값 100% 매핑)
    const featureDict = {};
    
    // 블루팀 매핑
    featureDict['blue_top_gold'] = blueLines.top.gold;
    featureDict['blue_top_cs'] = blueLines.top.cs;
    featureDict['blue_top_kills'] = blueLines.top.kills;
    featureDict['blue_top_deaths'] = blueLines.top.deaths;
    
    featureDict['blue_jungle_gold'] = blueLines.jungle.gold;
    featureDict['blue_jungle_cs'] = blueLines.jungle.cs;
    featureDict['blue_jungle_kills'] = blueLines.jungle.kills;
    featureDict['blue_jungle_deaths'] = blueLines.jungle.deaths;
    
    featureDict['blue_middle_gold'] = blueLines.middle.gold;
    featureDict['blue_middle_cs'] = blueLines.middle.cs;
    featureDict['blue_middle_kills'] = blueLines.middle.kills;
    featureDict['blue_middle_deaths'] = blueLines.middle.deaths;
    
    // 바텀 듀오 분배 (원딜 65%, 서폿 35% 골드 분배 / CS 원딜 95%, 서폿 5% 분배 / KDA 킬데스 분배)
    featureDict['blue_bottom_gold'] = blueLines.bottom.gold * 0.65;
    featureDict['blue_utility_gold'] = blueLines.bottom.gold * 0.35;
    featureDict['blue_bottom_cs'] = blueLines.bottom.cs * 0.95;
    featureDict['blue_utility_cs'] = blueLines.bottom.cs * 0.05;
    featureDict['blue_bottom_kills'] = blueLines.bottom.kills * 0.8;
    featureDict['blue_utility_kills'] = blueLines.bottom.kills * 0.2;
    featureDict['blue_bottom_deaths'] = blueLines.bottom.deaths * 0.5;
    featureDict['blue_utility_deaths'] = blueLines.bottom.deaths * 0.5;
    
    // 레드팀 매핑
    featureDict['red_top_gold'] = redLines.top.gold;
    featureDict['red_top_cs'] = redLines.top.cs;
    featureDict['red_top_kills'] = redLines.top.kills;
    featureDict['red_top_deaths'] = redLines.top.deaths;
    
    featureDict['red_jungle_gold'] = redLines.jungle.gold;
    featureDict['red_jungle_cs'] = redLines.jungle.cs;
    featureDict['red_jungle_kills'] = redLines.jungle.kills;
    featureDict['red_jungle_deaths'] = redLines.jungle.deaths;
    
    featureDict['red_middle_gold'] = redLines.middle.gold;
    featureDict['red_middle_cs'] = redLines.middle.cs;
    featureDict['red_middle_kills'] = redLines.middle.kills;
    featureDict['red_middle_deaths'] = redLines.middle.deaths;
    
    featureDict['red_bottom_gold'] = redLines.bottom.gold * 0.65;
    featureDict['red_utility_gold'] = redLines.bottom.gold * 0.35;
    featureDict['red_bottom_cs'] = redLines.bottom.cs * 0.95;
    featureDict['red_utility_cs'] = redLines.bottom.cs * 0.05;
    featureDict['red_bottom_kills'] = redLines.bottom.kills * 0.8;
    featureDict['red_utility_kills'] = redLines.bottom.kills * 0.2;
    featureDict['red_bottom_deaths'] = redLines.bottom.deaths * 0.5;
    featureDict['red_utility_deaths'] = redLines.bottom.deaths * 0.5;
    
    // 격차(Diff) 매핑
    const roles = ['top', 'jungle', 'middle', 'bottom', 'utility'];
    roles.forEach(role => {
      featureDict[`${role}_gold_diff`] = featureDict[`blue_${role}_gold`] - featureDict[`red_${role}_gold`];
    });
    
    // 공통 오브젝트 매핑
    featureDict['blue_dragons'] = commonStats.blueDragons;
    featureDict['blue_heralds'] = commonStats.blueHeralds;
    featureDict['blue_towers'] = commonStats.blueTowersDestroyed;
    featureDict['blue_kills'] = blueLines.top.kills + blueLines.jungle.kills + blueLines.middle.kills + blueLines.bottom.kills;
    featureDict['blue_firstBlood'] = commonStats.blueFirstBlood;
    featureDict['blue_voidgrubs'] = commonStats.blueEliteMonsters;
    
    featureDict['red_dragons'] = commonStats.redDragons;
    featureDict['red_heralds'] = commonStats.redHeralds;
    featureDict['red_towers'] = commonStats.redTowersDestroyed;
    featureDict['red_kills'] = redLines.top.kills + redLines.jungle.kills + redLines.middle.kills + redLines.bottom.kills;
    featureDict['red_voidgrubs'] = commonStats.redEliteMonsters;

    // 상호작용 피처 (Interaction Features) 계산
    const blueGoldTotal = featureDict['blue_top_gold'] + featureDict['blue_jungle_gold'] + featureDict['blue_middle_gold'] + featureDict['blue_bottom_gold'] + featureDict['blue_utility_gold'];
    const redGoldTotal = featureDict['red_top_gold'] + featureDict['red_jungle_gold'] + featureDict['red_middle_gold'] + featureDict['red_bottom_gold'] + featureDict['red_utility_gold'];
    featureDict['gold_ratio'] = blueGoldTotal / (blueGoldTotal + redGoldTotal + 1e-5);
    featureDict['gold_diff_total'] = blueGoldTotal - redGoldTotal;

    const blueCsTotal = featureDict['blue_top_cs'] + featureDict['blue_jungle_cs'] + featureDict['blue_middle_cs'] + featureDict['blue_bottom_cs'] + featureDict['blue_utility_cs'];
    const redCsTotal = featureDict['red_top_cs'] + featureDict['red_jungle_cs'] + featureDict['red_middle_cs'] + featureDict['red_bottom_cs'] + featureDict['red_utility_cs'];
    featureDict['cs_ratio'] = blueCsTotal / (blueCsTotal + redCsTotal + 1e-5);

    featureDict['kills_ratio'] = featureDict['blue_kills'] / (featureDict['blue_kills'] + featureDict['red_kills'] + 1e-5);
    featureDict['dragons_diff'] = featureDict['blue_dragons'] - featureDict['red_dragons'];
    featureDict['towers_diff'] = featureDict['blue_towers'] - featureDict['red_towers'];
    featureDict['voidgrubs_diff'] = featureDict['blue_voidgrubs'] - featureDict['red_voidgrubs'];

    // 2. 원핫 인코딩 피처 추가
    const blueChampsFull = [...selectedBlueChampions];
    const redChampsFull = [...selectedRedChampions];
    while (blueChampsFull.length < 5) blueChampsFull.push("");
    while (redChampsFull.length < 5) redChampsFull.push("");
    
    const blueTags = blueChampsFull.map(c => c ? (CHAMPION_TAGS[c] || "Unknown") : "Unknown");
    const redTags = redChampsFull.map(c => c ? (CHAMPION_TAGS[c] || "Unknown") : "Unknown");
    const blueCompName = determineComposition(blueTags);
    const redCompName = determineComposition(redTags);
    
    roles.forEach((role, i) => {
      featureDict[`blue_${role}_tag_${blueTags[i]}`] = 1.0;
      featureDict[`red_${role}_tag_${redTags[i]}`] = 1.0;
    });
    featureDict[`blue_comp_${blueCompName}`] = 1.0;
    featureDict[`red_comp_${redCompName}`] = 1.0;
    
    blueChampsFull.forEach(c => {
      if (c) featureDict[`blue_champion_${c}`] = 1.0;
    });
    redChampsFull.forEach(c => {
      if (c) featureDict[`red_champion_${c}`] = 1.0;
    });

    // 3. 머신러닝 예측 수행
    let blueWinProb = 0.50;
    let individualProbs = null;
    try {
      if (modelName === "Ensemble") {
        const ensembleResult = ensembleSoftVoting(featureDict);
        blueWinProb = ensembleResult.ensemble_probability;
        individualProbs = ensembleResult.individual;
      } else {
        blueWinProb = runModelInference(modelName, featureDict);
      }
    } catch (e) {}
    
    const redWinProb = 1.0 - blueWinProb;
    const predictionVal = blueWinProb >= 0.5 ? 1 : 0;
    
    // 드래곤 가치 편미분 연산 (앙상블 시 XGBoost 기준)
    const dragonModelName = modelName === "Ensemble" ? "XGBoost" : modelName;
    const dragonGoldVal = calculateDragonGoldValue(dragonModelName, featureDict);
    
    // 시너지 & 카운터픽 연산
    const compDetails = calculateCompositionScores(selectedBlueChampions, selectedRedChampions);
    const compModelName = modelName === "Ensemble" ? "XGBoost" : modelName;
    const mlBlueScore = calculateMLCompositionScore(compModelName, selectedBlueChampions, []);
    const mlRedScore = calculateMLCompositionScore(compModelName, [], selectedRedChampions);
    
    setPrediction({
      prediction: predictionVal,
      winner: predictionVal === 1 ? "Blue" : "Red",
      blue_win_probability: blueWinProb,
      red_win_probability: redWinProb,
      dragon_gold_value: dragonGoldVal,
      blue_comp_score: mlBlueScore,
      red_comp_score: mlRedScore,
      blue_synergies: compDetails.blue_synergies,
      red_synergies: compDetails.red_synergies,
      counters: compDetails.counters,
      individualProbs: individualProbs
    });
  }, [modelName, blueLines, redLines, commonStats, selectedBlueChampions, selectedRedChampions]);

  // 개별 라인 데이터 수정 핸들러
  const handleLineStatChange = (team, lane, statKey, value) => {
    const val = parseFloat(value) || 0;
    if (team === 'blue') {
      setBlueLines(prev => ({
        ...prev,
        [lane]: { ...prev[lane], [statKey]: val }
      }));
    } else {
      setRedLines(prev => ({
        ...prev,
        [lane]: { ...prev[lane], [statKey]: val }
      }));
    }
  };

  // 공통 오브젝트 지표 변경 핸들러
  const handleCommonStatChange = (statKey, value) => {
    const val = parseInt(value) || 0;
    setCommonStats(prev => {
      const next = { ...prev, [statKey]: val };
      if (statKey === 'blueFirstBlood') next.redFirstBlood = val === 1 ? 0 : 1;
      if (statKey === 'redFirstBlood') next.blueFirstBlood = val === 1 ? 0 : 1;
      return next;
    });
  };

  // 챔피언 선택 모달 제어
  const openModal = (team, index) => {
    setActiveSlot({ team, index });
    setSearchTerm('');
    setModalOpen(true);
  };

  const handleSelectChampion = (champId) => {
    const isBlue = activeSlot.team === 'blue';
    const list = isBlue ? [...selectedBlueChampions] : [...selectedRedChampions];
    list[activeSlot.index] = champId;
    
    if (isBlue) {
      setSelectedBlueChampions(list);
    } else {
      setSelectedRedChampions(list);
    }
    
    const allSelected = list.every(c => c !== "");
    if (allSelected) {
      setModalOpen(false);
    } else if (activeSlot.index < 4) {
      setActiveSlot(prev => ({ ...prev, index: prev.index + 1 }));
      setSearchTerm('');
    } else {
      setModalOpen(false);
    }
  };

  const handleClearSlot = () => {
    const isBlue = activeSlot.team === 'blue';
    const list = isBlue ? [...selectedBlueChampions] : [...selectedRedChampions];
    list[activeSlot.index] = "";
    if (isBlue) {
      setSelectedBlueChampions(list);
    } else {
      setSelectedRedChampions(list);
    }
    setModalOpen(false);
  };

  const handleClearTeam = (team) => {
    if (team === 'blue') {
      setSelectedBlueChampions(["", "", "", "", ""]);
    } else {
      setSelectedRedChampions(["", "", "", "", ""]);
    }
  };

  // 챔피언 태그 데이터 맵핑
  const CHAMPION_TAGS = {
    "Aatrox": "Fighter", "Ahri": "Mage", "Akali": "Assassin", "Alistar": "Tank", "Amumu": "Tank",
    "Anivia": "Mage", "Annie": "Mage", "Aphelios": "Marksman", "Ashe": "Marksman", "Azir": "Mage",
    "Bard": "Support", "Belveth": "Fighter", "Blitzcrank": "Tank", "Brand": "Mage", "Braum": "Support",
    "Caitlyn": "Marksman", "Camille": "Fighter", "Cassiopeia": "Mage", "Chogath": "Tank", "Darius": "Fighter",
    "Diana": "Fighter", "DrMundo": "Fighter", "Draven": "Marksman", "Ekko": "Assassin", "Elise": "Mage",
    "Evelynn": "Assassin", "Ezreal": "Marksman", "Fiora": "Fighter", "Fizz": "Assassin", "Galio": "Tank",
    "Garen": "Fighter", "Gnar": "Fighter", "Gragas": "Fighter", "Graves": "Marksman", "Gwen": "Fighter",
    "Hecarim": "Fighter", "Hwei": "Mage", "Irelia": "Fighter", "Janna": "Support", "JarvanIV": "Fighter",
    "Jax": "Fighter", "Jayce": "Fighter", "Jhin": "Marksman", "Jinx": "Marksman", "Kaisa": "Marksman",
    "Kalista": "Marksman", "Karma": "Mage", "Karthus": "Mage", "Kassadin": "Assassin", "Katarina": "Assassin",
    "Kayn": "Fighter", "Khazix": "Assassin", "Kled": "Fighter", "KogMaw": "Marksman", "Leblanc": "Assassin",
    "LeeSin": "Fighter", "Leona": "Tank", "Lillia": "Fighter", "Lucian": "Marksman", "Lulu": "Support",
    "Lux": "Mage", "Malphite": "Tank", "Maokai": "Tank", "MasterYi": "Assassin", "Milio": "Support",
    "MissFortune": "Marksman", "Mordekaiser": "Fighter", "Morgana": "Mage", "Nami": "Support", "Nasus": "Fighter",
    "Nautilus": "Tank", "Nidalee": "Assassin", "Nocturne": "Assassin", "Olaf": "Fighter", "Orianna": "Mage",
    "Ornn": "Tank", "Poppy": "Tank", "Pyke": "Assassin", "Rakan": "Support", "Rammus": "Tank",
    "Renata": "Support", "Renekton": "Fighter", "Riven": "Fighter", "Rumble": "Fighter", "Ryze": "Mage",
    "Samira": "Marksman", "Sejuani": "Tank", "Senna": "Marksman", "Sett": "Fighter", "Shaco": "Assassin",
    "Shen": "Tank", "Sion": "Tank", "Sivir": "Marksman", "Sona": "Support", "Soraka": "Support",
    "Sylas": "Mage", "Syndra": "Mage", "Taliyah": "Mage", "Talon": "Assassin", "Teemo": "Marksman",
    "Thresh": "Support", "Tristana": "Marksman", "Trundle": "Fighter", "Twitch": "Marksman", "Varus": "Marksman",
    "Vayne": "Marksman", "Veigar": "Mage", "Viego": "Fighter", "Viktor": "Mage", "Vladimir": "Mage",
    "Volibear": "Fighter", "Warwick": "Fighter", "Xayah": "Marksman", "XinZhao": "Fighter", "Yasuo": "Fighter",
    "Yone": "Assassin", "Yorick": "Fighter", "Yuumi": "Support", "Zac": "Tank", "Zed": "Assassin",
    "Zeri": "Marksman", "Zoe": "Mage", "Zyra": "Mage"
  };

  // Chart Rendering Helper
  const getChartData = (modelKey) => {
    const model = metricsData[modelKey];
    if (!model) return { labels: [], datasets: [] };
    
    const coefficients = model.Coefficients || model.Feature_Importances;
    const sorted = Object.entries(coefficients)
      .sort((a, b) => Math.abs(b[1]) - Math.abs(a[1]))
      .slice(0, 10);
      
    const translateLabel = (name) => {
      const mapping = {
        'blueWardsPlaced': '와드 설치 (블루)', 'blueWardsDestroyed': '와드 파괴 (블루)',
        'blueFirstBlood': '선취점 (블루)', 'blueKills': '총 킬 (블루)', 'blueDeaths': '총 데스 (블루)',
        'blueAssists': '어시스트 (블루)', 'blueEliteMonsters': '엘리트 몹 (블루)',
        'blueDragons': '드래곤 (블루)', 'blueHeralds': '전령 (블루)', 'blueTowersDestroyed': '포탑 파괴 (블루)',
        'blueTotalGold': '총 골드 (블루)', 'blueAvgLevel': '평균 레벨 (블루)',
        'blueTotalExperience': '총 경험치 (블루)', 'blueTotalMinionsKilled': '미니언 CS (블루)',
        'blueTotalJungleMinionsKilled': '정글 CS (블루)', 'blueGoldDiff': '골드 격차 (블루)',
        'blueExperienceDiff': '경험치 격차 (블루)', 'blueCSPerMin': '분당 CS (블루)',
        'blueGoldPerMin': '분당 골드 (블루)', 'redWardsPlaced': '와드 설치 (레드)',
        'redWardsDestroyed': '와드 파괴 (레드)', 'redFirstBlood': '선취점 (레드)',
        'redKills': '총 킬 (레드)', 'redDeaths': '총 데스 (레드)', 'redAssists': '어시스트 (레드)',
        'redEliteMonsters': '엘리트 몹 (레드)', 'redDragons': '드래곤 (레드)', 'redHeralds': '전령 (레드)',
        'redTowersDestroyed': '포탑 파괴 (레드)', 'redTotalGold': '총 골드 (레드)',
        'redAvgLevel': '평균 레벨 (레드)', 'redTotalExperience': '총 경험치 (레드)',
        'redTotalMinionsKilled': '미니언 CS (레드)', 'redTotalJungleMinionsKilled': '정글 CS (레드)',
        'redGoldDiff': '골드 격차 (레드)', 'redExperienceDiff': '경험치 격차 (레드)',
        'redCSPerMin': '분당 CS (레드)', 'redGoldPerMin': '분당 골드 (레드)'
      };
      return mapping[name] || name;
    };
    
    return {
      labels: sorted.map(item => translateLabel(item[0])),
      datasets: [{
        data: sorted.map(item => item[1]),
        backgroundColor: sorted.map(item => item[1] >= 0 ? 'rgba(31, 142, 206, 0.65)' : 'rgba(232, 64, 87, 0.65)'),
        borderColor: sorted.map(item => item[1] >= 0 ? '#1f8ece' : '#e84057'),
        borderWidth: 1.5,
        borderRadius: 4
      }]
    };
  };

  const chartOptions = {
    indexAxis: 'y',
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: (context) => ` 가중치: ${context.raw.toFixed(4)}`
        }
      }
    },
    scales: {
      x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#a0a0a0' } },
      y: { grid: { display: false }, ticks: { color: '#f0f0f0', font: { family: 'Inter', size: 10 } } }
    }
  };

  // 라인별 맵 마커 컴포넌트
  const MapMarker = ({ team, lane }) => {
    const isBlue = team === 'blue';
    const pos = LANE_POSITIONS[team][lane];
    const lines = isBlue ? blueLines : redLines;
    const stats = lines[lane];
    const champList = isBlue ? selectedBlueChampions : selectedRedChampions;
    const champId = champList[pos.champIdx];
    
    // 포지션별 기본 이니셜
    const getLaneInitial = (l) => {
      switch (l) {
        case 'top': return 'T';
        case 'jungle': return 'J';
        case 'middle': return 'M';
        case 'bottom': return 'B';
        default: return '';
      }
    };

    // 골드 1,000단위 축약 (ex: 3600 -> 3.6k)
    const formatGoldShort = (g) => {
      return (g / 1000).toFixed(1) + 'k';
    };

    const teamColorClass = isBlue 
      ? 'border-blue-team/70 text-blue-team shadow-[0_0_8px_rgba(31,142,206,0.2)] hover:border-blue-team hover:shadow-glow-blue' 
      : 'border-red-team/70 text-red-team shadow-[0_0_8px_rgba(232,64,87,0.2)] hover:border-red-team hover:shadow-glow-red';
      
    const isSelected = activePopover && activePopover.team === team && activePopover.lane === lane;
    const titleColor = isBlue ? 'text-blue-team' : 'text-red-team';
    const cardBorderColor = isBlue ? 'border-blue-team/40 shadow-glow-blue' : 'border-red-team/40 shadow-glow-red';

    // 좌우 배치 판단 (left%가 50 미만이면 팝오버를 마커 우측에, 50 이상이면 좌측에 배치)
    const isLeftHalf = parseFloat(pos.left) < 50;
    
    // 상하 배치 판단 (top%가 30 미만이면 아래로 내리고, 70 초과면 위로 올리고, 그 외엔 중앙정렬)
    const topPercent = parseFloat(pos.top);
    let verticalOffsetClass = 'top-[-85px]';
    if (topPercent < 30) {
      verticalOffsetClass = 'top-[-10px]';
    } else if (topPercent > 70) {
      verticalOffsetClass = 'top-[-185px]';
    }

    const popoverPositionClass = isLeftHalf 
      ? `left-[46px] ${verticalOffsetClass} origin-left` 
      : `right-[46px] ${verticalOffsetClass} origin-right`;

    return (
      <div
        className={`absolute -translate-x-1/2 -translate-y-1/2 flex flex-col items-center cursor-pointer group select-none transition-all duration-200 hover:scale-105 ${
          isSelected ? 'z-40' : 'z-10'
        }`}
        style={{ top: pos.top, left: pos.left }}
        onMouseEnter={() => handleMarkerMouseEnter(team, lane)}
        onMouseLeave={handleMarkerMouseLeave}
      >
        {/* 활성화 상태 핑 애니메이션 */}
        {isSelected && (
          <span className={`absolute top-0 w-[42px] h-[42px] rounded-full animate-ping opacity-40 ${isBlue ? 'bg-blue-team' : 'bg-red-team'}`} />
        )}

        {/* 핀 원형 버튼 */}
        <div className={`w-[42px] h-[42px] rounded-full border-2 bg-bg-deep flex items-center justify-center overflow-hidden transition-all duration-300 ${
          isSelected 
            ? 'border-gold-main scale-105 shadow-glow-gold ring-2 ring-gold-main/30' 
            : teamColorClass
        }`}>
          {champId ? (
            <img
              src={`https://ddragon.leagueoflegends.com/cdn/14.22.1/img/champion/${champId}.png`}
              alt={champId}
              className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
            />
          ) : (
            <span className="font-outfit font-black text-sm tracking-tighter">
              {getLaneInitial(lane)}
            </span>
          )}
        </div>

        {/* 정보 요약 캡슐 뱃지 */}
        <div className={`mt-1 px-1.5 py-0.5 rounded-full text-[8px] font-bold border backdrop-blur-md transition-all duration-300 ${
          isSelected 
            ? 'bg-gold-main/20 text-gold-bright border-gold-main/40 shadow-glow-gold' 
            : 'bg-black/80 text-text-primary border-white/10 group-hover:border-white/20'
        }`}>
          {stats.kills}/{stats.deaths}/{stats.assists} • {formatGoldShort(stats.gold)}
        </div>

        {/* 상세 조작 팝오버 카드 (마커 호버 시 미려하게 오픈) */}
        {isSelected && (
          <div 
            className={`absolute z-30 bg-bg-deep/95 border-2 rounded-2xl p-4 w-[250px] shadow-2xl backdrop-blur-xl transition-all duration-300 scale-100 ${popoverPositionClass} ${cardBorderColor}`}
            onClick={(e) => e.stopPropagation()}
            onMouseEnter={() => handleMarkerMouseEnter(team, lane)}
            onMouseLeave={handleMarkerMouseLeave}
          >
            {/* 타이틀 */}
            <div className="flex items-center gap-2 border-b border-white/10 pb-2 mb-3">
              <span className={`w-2 h-2 rounded-full ${isBlue ? 'bg-blue-team shadow-[0_0_8px_#1f8ece]' : 'bg-red-team shadow-[0_0_8px_#e84057]'}`} />
              <h4 className={`font-bold text-[11px] ${titleColor} flex items-center gap-1.5`}>
                {pos.label} 지표 설정
              </h4>
              {champId && (
                <span className="text-[9px] text-text-secondary">({getChampionNameKr(champId)})</span>
              )}
            </div>

            <div className="flex flex-col gap-3 text-[10px]">
              {/* K/D/A */}
              <div className="flex justify-between items-center bg-white/[0.02] border border-white/5 rounded-xl p-2">
                <span className="text-text-secondary font-semibold">K / D / A</span>
                <div className="flex gap-1 items-center">
                  <input
                    type="number"
                    min="0"
                    value={stats.kills}
                    onChange={(e) => handleLineStatChange(team, lane, 'kills', e.target.value)}
                    className="w-7 bg-black/60 border border-border-glass rounded text-center text-xs p-0.5 outline-none font-bold text-text-primary"
                  />
                  <span className="text-text-secondary/30">/</span>
                  <input
                    type="number"
                    min="0"
                    value={stats.deaths}
                    onChange={(e) => handleLineStatChange(team, lane, 'deaths', e.target.value)}
                    className="w-7 bg-black/60 border border-border-glass rounded text-center text-xs p-0.5 outline-none font-bold text-text-primary"
                  />
                  <span className="text-text-secondary/30">/</span>
                  <input
                    type="number"
                    min="0"
                    value={stats.assists}
                    onChange={(e) => handleLineStatChange(team, lane, 'assists', e.target.value)}
                    className="w-7 bg-black/60 border border-border-glass rounded text-center text-xs p-0.5 outline-none font-bold text-text-primary"
                  />
                </div>
              </div>

              {/* CS */}
              <div className="flex justify-between items-center bg-white/[0.02] border border-white/5 rounded-xl p-2">
                <span className="text-text-secondary font-semibold">
                  {lane === 'jungle' ? '정글 CS' : '라인 CS'}
                </span>
                <input
                  type="number"
                  min="0"
                  value={stats.cs}
                  onChange={(e) => handleLineStatChange(team, lane, 'cs', e.target.value)}
                  className="w-10 bg-black/60 border border-border-glass rounded text-center text-xs p-0.5 outline-none font-bold text-text-primary"
                />
              </div>

              {/* Gold */}
              <div className="bg-white/[0.02] border border-white/5 rounded-xl p-2 flex flex-col gap-1.5">
                <div className="flex justify-between items-center">
                  <span className="text-text-secondary font-semibold">골드 획득량</span>
                  <span className="text-gold-bright font-black text-[10px]">{stats.gold.toLocaleString()} G</span>
                </div>
                <input
                  type="range"
                  min="1000"
                  max="20000"
                  step="100"
                  value={stats.gold}
                  onChange={(e) => handleLineStatChange(team, lane, 'gold', e.target.value)}
                  className="w-full h-1 bg-black/60 rounded-lg appearance-none cursor-pointer accent-gold-main"
                />
                <div className="flex justify-between text-[7px] text-text-secondary/30">
                  <span>1k G</span>
                  <span>20k G</span>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    );
  };

  // 라인 상세 지표 설정 팝오버 (호버 인터랙션으로 전환되어 미사용)
  const LinePopoverOverlay = () => null;


  return (
    <div className="container mx-auto max-w-6xl px-4 py-8 relative">
      <header className="text-center mb-8">
        <h1 className="text-5xl font-extrabold tracking-tight bg-gradient-to-r from-gold-bright to-gold-main bg-clip-text text-transparent filter drop-shadow-[0_0_10px_rgba(200,170,110,0.3)] mb-2">
          HEXTECH EARLY PREDICTOR
        </h1>
        <p className="text-gold-main text-xs font-semibold tracking-[0.25em] uppercase">
          리그 오브 레전드 15분 지표 머신러닝 정밀 분석
        </p>
      </header>

      {/* 1. 실시간 예측 요약 바 */}
      <div className="bg-bg-card border border-border-glass rounded-3xl p-6 mb-8 shadow-glow relative overflow-hidden">
        <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-team via-gold-main to-red-team"></div>
        <div className="flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="text-center md:text-left">
            <span className="text-xs text-text-secondary uppercase tracking-widest block mb-1">실시간 승률 예측 엔진</span>
            <h2 className={`text-3xl font-black ${prediction.winner === 'Blue' ? 'text-blue-team drop-shadow-[0_0_10px_rgba(31,142,206,0.3)]' : 'text-red-team drop-shadow-[0_0_10px_rgba(232,64,87,0.3)]'}`}>
              {prediction.winner === 'Blue' ? '블루팀 승리 유력' : '레드팀 승리 유력'}
            </h2>
          </div>

          <div className="flex-1 w-full max-w-md">
            <div className="flex justify-between font-bold text-sm mb-1 px-1">
              <span className="text-blue-team">블루팀 {(prediction.blue_win_probability * 100).toFixed(1)}%</span>
              <span className="text-red-team">레드팀 {(prediction.red_win_probability * 100).toFixed(1)}%</span>
            </div>
            <div className="h-3 bg-white/5 rounded-full overflow-hidden flex shadow-[inset_0_2px_4px_rgba(0,0,0,0.5)]">
              <div className="bg-blue-team shadow-[0_0_10px_#1f8ece] transition-all duration-700 ease-out" style={{ width: `${prediction.blue_win_probability * 100}%` }}></div>
              <div className="bg-red-team shadow-[0_0_10px_#e84057] transition-all duration-700 ease-out flex-1"></div>
            </div>
          </div>

          <div>
            <select
              value={modelName}
              onChange={(e) => setModelName(e.target.value)}
              className="bg-bg-deep text-gold-bright border border-border-glass rounded-xl px-4 py-2 text-sm font-semibold cursor-pointer outline-none transition hover:border-gold-main"
            >
              {MODEL_OPTIONS.map(opt => (
                <option key={opt.value} value={opt.value}>{opt.label}</option>
              ))}
            </select>
          </div>
        </div>

        {/* 앙상블 개별 모델 기여도 표시 */}
        {modelName === "Ensemble" && prediction.individualProbs && (
          <div className="mt-5 pt-4 border-t border-white/5">
            <div className="text-[10px] text-text-secondary uppercase tracking-widest mb-3 font-semibold">개별 모델 예측 기여도 (Soft Voting Breakdown)</div>
            <div className="grid grid-cols-3 gap-3">
              {Object.entries(prediction.individualProbs).map(([name, prob]) => {
                const shortName = name === "Logistic Regression" ? "LR" : name === "Random Forest" ? "RF" : "XGB";
                const weight = name === "Logistic Regression" ? "40%" : name === "Random Forest" ? "20%" : "40%";
                const colorClass = name === "Logistic Regression" ? "border-gold-main/30" : name === "Random Forest" ? "border-blue-team/30" : "border-red-team/30";
                const labelColor = name === "Logistic Regression" ? "text-gold-main" : name === "Random Forest" ? "text-blue-team" : "text-red-team";
                return (
                  <div key={name} className={`bg-white/[0.03] border ${colorClass} rounded-xl p-3 text-center transition hover:bg-white/[0.05]`}>
                    <div className={`text-[11px] font-bold mb-1 ${labelColor}`}>{shortName} <span className="text-text-secondary/40 font-normal">({weight})</span></div>
                    <div className={`text-xl font-black ${prob >= 0.5 ? 'text-blue-team' : 'text-red-team'}`}>
                      {(prob * 100).toFixed(1)}%
                    </div>
                    <div className="h-1.5 bg-white/5 rounded-full overflow-hidden mt-2 flex">
                      <div className="bg-blue-team/70 transition-all duration-500" style={{ width: `${prob * 100}%` }}></div>
                      <div className="bg-red-team/70 flex-1"></div>
                    </div>
                    <div className="text-[8px] text-text-secondary/40 mt-1.5">{name}</div>
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </div>

      {/* 2. 🗺️ 소환사의 협곡 맵 내 지표 조작 (8개 라인 그리드 절대 좌표화) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-8">
        {/* 맵 컨테이너 (8/12) */}
        <div className="lg:col-span-8 bg-bg-card border border-border-glass rounded-3xl p-4 shadow-glow flex flex-col justify-center items-center relative overflow-hidden">
          <h3 className="text-gold-bright mb-4 text-sm font-bold border-l-4 border-gold-main pl-3 self-start">
            🗺️ 소환사의 협곡 인게임 라인 지표 설정
          </h3>
          
          <div className="w-full aspect-square max-w-[650px] relative rounded-2xl overflow-hidden border border-border-glass shadow-[0_0_20px_rgba(0,0,0,0.8)]"
               style={{
                 backgroundImage: 'url("https://ddragon.leagueoflegends.com/cdn/6.8.1/img/map/map11.png")',
                 backgroundSize: 'cover',
                 backgroundPosition: 'center'
               }}>
            
            {/* 블루팀 4개 마커 핀 */}
            <MapMarker team="blue" lane="top" />
            <MapMarker team="blue" lane="jungle" />
            <MapMarker team="blue" lane="middle" />
            <MapMarker team="blue" lane="bottom" />

            {/* 레드팀 4개 마커 핀 */}
            <MapMarker team="red" lane="top" />
            <MapMarker team="red" lane="jungle" />
            <MapMarker team="red" lane="middle" />
            <MapMarker team="red" lane="bottom" />

            {/* 라인 지표 상세 설정 팝오버 */}
            <LinePopoverOverlay />

          </div>
        </div>

        {/* 밴픽 조합 설정 영역 (4/12) */}
        <div className="lg:col-span-4 flex flex-col gap-6">
          <div className="bg-bg-card border border-border-glass rounded-3xl p-6 shadow-glow flex-1">
            <h3 className="text-gold-bright mb-4 text-sm font-bold border-l-4 border-gold-main pl-3">
              🛡️ 챔피언 밴픽 조합 설정
            </h3>

            {/* 블루팀 챔피언 */}
            <div className="mb-6">
              <div className="flex justify-between items-center border-b border-white/5 pb-2 mb-3">
                <div className="flex items-center gap-2">
                  <span className="text-sm font-bold text-blue-team">🔵 블루팀 챔피언</span>
                  <button onClick={() => handleClearTeam('blue')} className="text-[10px] bg-red-team/10 border border-red-team/30 text-red-team rounded px-1.5 py-0.5 font-bold hover:bg-red-team/20 transition">초기화</button>
                </div>
                <span className="text-xs font-bold text-gold-main">조합 점수: {(prediction.blue_comp_score * 100).toFixed(1)}%</span>
              </div>
              <div className="grid grid-cols-5 gap-2">
                {selectedBlueChampions.map((c, i) => (
                  <button
                    key={`blue-slot-${i}`}
                    onClick={() => openModal('blue', i)}
                    className="aspect-square border border-border-glass rounded-xl overflow-hidden flex flex-col justify-center items-center bg-black/40 hover:border-blue-team hover:shadow-glow-blue transition group relative"
                  >
                    {c ? (
                      <>
                        <img src={`https://ddragon.leagueoflegends.com/cdn/14.22.1/img/champion/${c}.png`} alt={c} className="w-full h-full object-cover" />
                        <div className="absolute bottom-0 left-0 right-0 bg-black/80 text-white text-[8px] py-0.5 truncate text-center font-semibold">{getChampionNameKr(c)}</div>
                      </>
                    ) : (
                      <>
                        <span className="text-text-secondary text-sm group-hover:scale-110 transition duration-300">{LANE_ICONS[i]}</span>
                        <span className="text-[9px] font-bold text-text-secondary mt-1">{LANE_LABELS[i]}</span>
                      </>
                    )}
                  </button>
                ))}
              </div>
            </div>

            {/* 레드팀 챔피언 */}
            <div className="mb-6">
              <div className="flex justify-between items-center border-b border-white/5 pb-2 mb-3">
                <div className="flex items-center gap-2">
                  <span className="text-sm font-bold text-red-team">🔴 레드팀 챔피언</span>
                  <button onClick={() => handleClearTeam('red')} className="text-[10px] bg-red-team/10 border border-red-team/30 text-red-team rounded px-1.5 py-0.5 font-bold hover:bg-red-team/20 transition">초기화</button>
                </div>
                <span className="text-xs font-bold text-gold-main">조합 점수: {(prediction.red_comp_score * 100).toFixed(1)}%</span>
              </div>
              <div className="grid grid-cols-5 gap-2">
                {selectedRedChampions.map((c, i) => (
                  <button
                    key={`red-slot-${i}`}
                    onClick={() => openModal('red', i)}
                    className="aspect-square border border-border-glass rounded-xl overflow-hidden flex flex-col justify-center items-center bg-black/40 hover:border-red-team hover:shadow-glow-red transition group relative"
                  >
                    {c ? (
                      <>
                        <img src={`https://ddragon.leagueoflegends.com/cdn/14.22.1/img/champion/${c}.png`} alt={c} className="w-full h-full object-cover" />
                        <div className="absolute bottom-0 left-0 right-0 bg-black/80 text-white text-[8px] py-0.5 truncate text-center font-semibold">{getChampionNameKr(c)}</div>
                      </>
                    ) : (
                      <>
                        <span className="text-text-secondary text-sm group-hover:scale-110 transition duration-300">{LANE_ICONS[i]}</span>
                        <span className="text-[9px] font-bold text-text-secondary mt-1">{LANE_LABELS[i]}</span>
                      </>
                    )}
                  </button>
                ))}
              </div>
            </div>

            {/* 시너지 효과 & 상성 리포트 패널 */}
            {(prediction.blue_synergies.length > 0 || prediction.red_synergies.length > 0 || prediction.counters.length > 0) ? (
              <div className="border-t border-border-glass pt-4 mt-4 grid grid-cols-1 gap-3.5 text-[10px]">
                <div className="bg-blue-team/5 border border-blue-team/10 rounded-xl p-3 flex flex-col gap-2">
                  <h5 className="text-blue-team font-bold text-xs">🔵 블루 시너지 / 상성</h5>
                  <ul className="list-none flex flex-col gap-1.5 text-text-secondary">
                    {prediction.blue_synergies.map((syn, idx) => (
                      <li key={`b-syn-${idx}`}><span className="text-blue-team font-bold">[시너지]</span> {syn.names_kr.join(' + ')} (+{(syn.bonus * 100).toFixed(1)}%)</li>
                    ))}
                    {prediction.counters.filter(c => c.winner_team === 'blue').map((cnt, idx) => (
                      <li key={`b-cnt-${idx}`}><span className="text-green-500 font-bold">[상성우위]</span> {cnt.counter_kr} ➔ {cnt.victim_kr} (+{(cnt.bonus * 100).toFixed(1)}%)</li>
                    ))}
                    {prediction.blue_synergies.length === 0 && prediction.counters.filter(c => c.winner_team === 'blue').length === 0 && (
                      <li className="opacity-40">활성화된 보정이 없습니다.</li>
                    )}
                  </ul>
                </div>
                <div className="bg-red-team/5 border border-red-team/10 rounded-xl p-3 flex flex-col gap-2">
                  <h5 className="text-red-team font-bold text-xs">🔴 레드 시너지 / 상성</h5>
                  <ul className="list-none flex flex-col gap-1.5 text-text-secondary">
                    {prediction.red_synergies.map((syn, idx) => (
                      <li key={`r-syn-${idx}`}><span className="text-red-team font-bold">[시너지]</span> {syn.names_kr.join(' + ')} (+{(syn.bonus * 100).toFixed(1)}%)</li>
                    ))}
                    {prediction.counters.filter(c => c.winner_team === 'red').map((cnt, idx) => (
                      <li key={`r-cnt-${idx}`}><span className="text-green-500 font-bold">[상성우위]</span> {cnt.counter_kr} ➔ {cnt.victim_kr} (+{(cnt.bonus * 100).toFixed(1)}%)</li>
                    ))}
                    {prediction.red_synergies.length === 0 && prediction.counters.filter(c => c.winner_team === 'red').length === 0 && (
                      <li className="opacity-40">활성화된 보정이 없습니다.</li>
                    )}
                  </ul>
                </div>
              </div>
            ) : (
              <div className="border-t border-border-glass pt-4 mt-4 text-center text-xs text-text-secondary opacity-60">
                활성화된 조합 시너지나 라인 카운터가 없습니다.
              </div>
            )}
          </div>
        </div>
      </div>

      {/* 3. 🔮 공통 경기 오브젝트 및 시야 지표 설정 패널 (추가 요구사항) */}
      <div className="bg-bg-card border border-border-glass rounded-3xl p-6 mb-8 shadow-glow">
        <h3 className="text-gold-bright mb-6 text-sm font-bold border-l-4 border-gold-main pl-3">
          🔮 공통 경기 오브젝트 및 시야 지표 설정
        </h3>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 text-xs">
          {/* 오브젝트 설정 (용 / 전령 / 유충) */}
          <div className="bg-white/[0.02] border border-white/5 rounded-2xl p-4 flex flex-col gap-4">
            <h4 className="text-gold-main font-bold border-b border-white/5 pb-1 flex items-center gap-1.5"><Trophy size={14} /> 에픽 몬스터 오브젝트</h4>
            
            <div className="flex flex-col gap-3">
              <div className="flex justify-between items-center">
                <span>🐉 블루팀 드래곤</span>
                <div className="flex gap-1.5">
                  {[0, 1, 2].map(n => (
                    <button key={`b-drag-${n}`} onClick={() => handleCommonStatChange('blueDragons', n)} className={`px-2.5 py-1 rounded-lg font-bold transition ${commonStats.blueDragons === n ? 'bg-blue-team text-white shadow-glow-blue' : 'bg-black/40 border border-border-glass text-text-secondary'}`}>{n}</button>
                  ))}
                </div>
              </div>

              <div className="flex justify-between items-center">
                <span>🐉 레드팀 드래곤</span>
                <div className="flex gap-1.5">
                  {[0, 1, 2].map(n => (
                    <button key={`r-drag-${n}`} onClick={() => handleCommonStatChange('redDragons', n)} className={`px-2.5 py-1 rounded-lg font-bold transition ${commonStats.redDragons === n ? 'bg-red-team text-white shadow-glow-red' : 'bg-black/40 border border-border-glass text-text-secondary'}`}>{n}</button>
                  ))}
                </div>
              </div>

              <div className="flex justify-between items-center border-t border-white/5 pt-3">
                <span>👾 공통 공허 유충 처치 (0~6)</span>
                <input
                  type="number"
                  min="0"
                  max="6"
                  value={commonStats.blueEliteMonsters}
                  onChange={(e) => handleCommonStatChange('blueEliteMonsters', e.target.value)}
                  className="w-12 bg-black/60 border border-border-glass rounded text-center text-xs p-1 outline-none font-bold text-text-primary"
                />
              </div>

              <div className="flex justify-between items-center">
                <span>👾 협곡의 전령 처치 (0~1)</span>
                <div className="flex gap-1.5">
                  <span>블루:</span>
                  <button onClick={() => handleCommonStatChange('blueHeralds', commonStats.blueHeralds === 1 ? 0 : 1)} className={`px-2 py-0.5 rounded text-[10px] ${commonStats.blueHeralds === 1 ? 'bg-blue-team text-white' : 'bg-black/40 border'}`}>획득</button>
                  <span>레드:</span>
                  <button onClick={() => handleCommonStatChange('redHeralds', commonStats.redHeralds === 1 ? 0 : 1)} className={`px-2 py-0.5 rounded text-[10px] ${commonStats.redHeralds === 1 ? 'bg-red-team text-white' : 'bg-black/40 border'}`}>획득</button>
                </div>
              </div>
            </div>
          </div>

          {/* 포탑 파괴 및 선취점 */}
          <div className="bg-white/[0.02] border border-white/5 rounded-2xl p-4 flex flex-col gap-4">
            <h4 className="text-gold-main font-bold border-b border-white/5 pb-1 flex items-center gap-1.5"><Shield size={14} /> 구조물 및 퍼스트 블러드</h4>
            
            <div className="flex flex-col gap-4">
              <div className="flex flex-col gap-1.5">
                <div className="flex justify-between">
                  <span>블루팀 포탑 파괴 수</span>
                  <span className="text-gold-bright font-bold">{commonStats.blueTowersDestroyed} 개</span>
                </div>
                <input type="range" min="0" max="5" value={commonStats.blueTowersDestroyed} onChange={(e) => handleCommonStatChange('blueTowersDestroyed', e.target.value)} className="h-1 cursor-pointer" />
              </div>

              <div className="flex flex-col gap-1.5">
                <div className="flex justify-between">
                  <span>레드팀 포탑 파괴 수</span>
                  <span className="text-gold-bright font-bold">{commonStats.redTowersDestroyed} 개</span>
                </div>
                <input type="range" min="0" max="5" value={commonStats.redTowersDestroyed} onChange={(e) => handleCommonStatChange('redTowersDestroyed', e.target.value)} className="h-1 cursor-pointer" />
              </div>

              <div className="flex justify-between items-center border-t border-white/5 pt-3">
                <span>💥 선취점 (First Blood)</span>
                <div className="flex gap-1.5">
                  <button onClick={() => handleCommonStatChange('blueFirstBlood', 1)} className={`px-3 py-1 rounded-lg transition font-bold ${commonStats.blueFirstBlood === 1 ? 'bg-blue-team text-white shadow-glow-blue' : 'bg-black/40 border border-border-glass text-text-secondary'}`}>블루</button>
                  <button onClick={() => handleCommonStatChange('redFirstBlood', 1)} className={`px-3 py-1 rounded-lg transition font-bold ${commonStats.redFirstBlood === 1 ? 'bg-red-team text-white shadow-glow-red' : 'bg-black/40 border border-border-glass text-text-secondary'}`}>레드</button>
                </div>
              </div>
            </div>
          </div>

          {/* 시야 및 와드 지표 */}
          <div className="bg-white/[0.02] border border-white/5 rounded-2xl p-4 flex flex-col gap-4">
            <h4 className="text-gold-main font-bold border-b border-white/5 pb-1 flex items-center gap-1.5"><Eye size={14} /> 시야 및 와드 수치</h4>
            
            <div className="grid grid-cols-2 gap-4">
              <div className="flex flex-col gap-1.5">
                <span>👁️ 블루 와드 설치</span>
                <input
                  type="number"
                  min="0"
                  value={commonStats.blueWardsPlaced}
                  onChange={(e) => handleCommonStatChange('blueWardsPlaced', e.target.value)}
                  className="w-full bg-black/60 border border-border-glass rounded px-2.5 py-1 outline-none font-bold text-text-primary text-center"
                />
              </div>

              <div className="flex flex-col gap-1.5">
                <span>👁️ 레드 와드 설치</span>
                <input
                  type="number"
                  min="0"
                  value={commonStats.redWardsPlaced}
                  onChange={(e) => handleCommonStatChange('redWardsPlaced', e.target.value)}
                  className="w-full bg-black/60 border border-border-glass rounded px-2.5 py-1 outline-none font-bold text-text-primary text-center"
                />
              </div>

              <div className="flex flex-col gap-1.5 border-t border-white/5 pt-2">
                <span>❌ 블루 와드 제거</span>
                <input
                  type="number"
                  min="0"
                  value={commonStats.blueWardsDestroyed}
                  onChange={(e) => handleCommonStatChange('blueWardsDestroyed', e.target.value)}
                  className="w-full bg-black/60 border border-border-glass rounded px-2.5 py-1 outline-none font-bold text-text-primary text-center"
                />
              </div>

              <div className="flex flex-col gap-1.5 border-t border-white/5 pt-2">
                <span>❌ 레드 와드 제거</span>
                <input
                  type="number"
                  min="0"
                  value={commonStats.redWardsDestroyed}
                  onChange={(e) => handleCommonStatChange('redWardsDestroyed', e.target.value)}
                  className="w-full bg-black/60 border border-border-glass rounded px-2.5 py-1 outline-none font-bold text-text-primary text-center"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* 4. 드래곤 가치 환산 정보 배너 */}
      {commonStats.blueDragons !== commonStats.redDragons && (
        <div className="bg-gradient-to-r from-gold-dark/10 via-bg-card to-gold-dark/10 border border-border-glass rounded-2xl p-5 mb-8 shadow-glow flex items-center gap-4">
          <span className="text-4xl filter drop-shadow-[0_0_8px_rgba(200,170,110,0.5)]">🐉</span>
          <div>
            <h4 className="font-outfit font-bold text-sm text-gold-bright mb-1 uppercase tracking-wider">
              {commonStats.blueDragons > commonStats.redDragons ? '블루팀' : '레드팀'} 드래곤 가치 환산
            </h4>
            <p className="text-xs text-text-secondary leading-relaxed">
              {modelName} 분석 결과, {commonStats.blueDragons > commonStats.redDragons ? '블루팀' : '레드팀'}이 획득한 드래곤은 게임 승률 관점에서 약 <strong className="text-gold-main font-extrabold text-shadow-glow">{(prediction.dragon_gold_value * Math.max(commonStats.blueDragons, commonStats.redDragons)).toLocaleString()} 골드</strong>(1마리당 약 {Math.round(prediction.dragon_gold_value).toLocaleString()} 골드)의 격차를 벌린 것과 동일한 Odds 상승 효과를 가집니다.
            </p>
          </div>
        </div>
      )}

      {/* 5. 모델 정밀 분석 대시보드 */}
      <div className="bg-bg-card border border-border-glass rounded-3xl p-6 shadow-glow">
        <h3 className="text-gold-bright mb-4 text-sm font-bold border-l-4 border-gold-main pl-3">
          🔎 모델 정밀 분석 대시보드
        </h3>
        <div className="flex border-b border-border-glass mb-6 gap-2 overflow-x-auto pb-1">
          <button onClick={() => setActiveTab('lr')} className={`text-xs uppercase tracking-wider px-4 py-2 font-bold transition outline-none ${activeTab === 'lr' ? 'text-gold-main border-b-2 border-gold-main' : 'text-text-secondary hover:text-gold-bright'}`}>로지스틱 회귀 (베이스라인)</button>
          <button onClick={() => setActiveTab('rf')} className={`text-xs uppercase tracking-wider px-4 py-2 font-bold transition outline-none ${activeTab === 'rf' ? 'text-gold-main border-b-2 border-gold-main' : 'text-text-secondary hover:text-gold-bright'}`}>랜덤 포레스트 (비교 모델)</button>
          <button onClick={() => setActiveTab('xgb')} className={`text-xs uppercase tracking-wider px-4 py-2 font-bold transition outline-none ${activeTab === 'xgb' ? 'text-gold-main border-b-2 border-gold-main' : 'text-text-secondary hover:text-gold-bright'}`}>XGBoost (최적화 모델)</button>
        </div>

        {/* 탭 내부 카드 레이아웃 */}
        <div className="grid grid-cols-1 md:grid-cols-12 gap-6">
          <div className="md:col-span-5 flex flex-col gap-4">
            <div className="bg-white/[0.02] border border-white/5 rounded-2xl p-4">
              <h5 className="text-gold-main text-xs font-semibold mb-3 border-b border-white/5 pb-1">평가 지표 (Test Metrics)</h5>
              <div className="grid grid-cols-2 gap-2 text-center">
                <div className="bg-black/20 border border-white/5 rounded-lg p-2.5">
                  <div className="text-xl font-black text-gold-bright">{(metricsData[activeTab === 'lr' ? 'Logistic Regression' : activeTab === 'rf' ? 'Random Forest' : 'XGBoost'].Accuracy * 100).toFixed(1)}%</div>
                  <div className="text-[9px] text-text-secondary uppercase">Accuracy</div>
                </div>
                <div className="bg-black/20 border border-white/5 rounded-lg p-2.5">
                  <div className="text-xl font-black text-gold-bright">{(metricsData[activeTab === 'lr' ? 'Logistic Regression' : activeTab === 'rf' ? 'Random Forest' : 'XGBoost']['F1-Score'] * 100).toFixed(1)}%</div>
                  <div className="text-[9px] text-text-secondary uppercase">F1-Score</div>
                </div>
                <div className="bg-black/20 border border-white/5 rounded-lg p-2.5">
                  <div className="text-xl font-black text-gold-bright">{metricsData[activeTab === 'lr' ? 'Logistic Regression' : activeTab === 'rf' ? 'Random Forest' : 'XGBoost']['ROC-AUC'].toFixed(3)}</div>
                  <div className="text-[9px] text-text-secondary uppercase">ROC-AUC</div>
                </div>
                <div className="bg-black/20 border border-white/5 rounded-lg p-2.5">
                  <div className="text-xl font-black text-gold-bright">{(metricsData[activeTab === 'lr' ? 'Logistic Regression' : activeTab === 'rf' ? 'Random Forest' : 'XGBoost'].Precision * 100).toFixed(1)}%</div>
                  <div className="text-[9px] text-text-secondary uppercase">Precision</div>
                </div>
              </div>
            </div>

            <div className="bg-white/[0.02] border border-white/5 rounded-2xl p-4">
              <h5 className="text-gold-main text-xs font-semibold mb-3 border-b border-white/5 pb-1">혼동 행렬 (Confusion Matrix)</h5>
              <div className="grid grid-cols-2 gap-2 text-[10px] text-center font-bold">
                <div className="bg-blue-team/5 border-l-4 border-blue-team rounded p-2 text-blue-team">
                  <div>True Positive (TP)</div>
                  <div className="text-lg font-black">{metricsData[activeTab === 'lr' ? 'Logistic Regression' : activeTab === 'rf' ? 'Random Forest' : 'XGBoost'].Confusion_Matrix.TP}</div>
                </div>
                <div className="bg-red-team/5 border-l-4 border-red-team rounded p-2 text-red-team">
                  <div>False Positive (FP)</div>
                  <div className="text-lg font-black">{metricsData[activeTab === 'lr' ? 'Logistic Regression' : activeTab === 'rf' ? 'Random Forest' : 'XGBoost'].Confusion_Matrix.FP}</div>
                </div>
                <div className="bg-red-team/5 border-l-4 border-red-team rounded p-2 text-red-team">
                  <div>False Negative (FN)</div>
                  <div className="text-lg font-black">{metricsData[activeTab === 'lr' ? 'Logistic Regression' : activeTab === 'rf' ? 'Random Forest' : 'XGBoost'].Confusion_Matrix.FN}</div>
                </div>
                <div className="bg-gold-main/5 border-l-4 border-gold-main rounded p-2 text-gold-bright">
                  <div>True Negative (TN)</div>
                  <div className="text-lg font-black">{metricsData[activeTab === 'lr' ? 'Logistic Regression' : activeTab === 'rf' ? 'Random Forest' : 'XGBoost'].Confusion_Matrix.TN}</div>
                </div>
              </div>
            </div>
          </div>

          {/* 차트 시각화 영역 (7/12) */}
          <div className="md:col-span-7 bg-white/[0.02] border border-white/5 rounded-2xl p-4 h-[350px]">
            <h5 className="text-gold-main text-xs font-semibold mb-3 border-b border-white/5 pb-1">
              {activeTab === 'lr' ? '가중치 계수 분석 (Coefficients)' : '피처 중요도 분석 (Feature Importance)'}
            </h5>
            <div className="h-[280px]">
              <Bar
                data={getChartData(activeTab === 'lr' ? 'Logistic Regression' : activeTab === 'rf' ? 'Random Forest' : 'XGBoost')}
                options={chartOptions}
              />
            </div>
          </div>
        </div>

        {/* 하위 요약 표 */}
        <div className="border-t border-border-glass mt-6 pt-6">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="text-gold-main border-b border-border-glass">
                <th className="pb-2">구분</th>
                <th className="pb-2">모델명</th>
                <th className="pb-2">정확도 (ACC)</th>
                <th className="pb-2">F1-Score</th>
                <th className="pb-2">ROC-AUC</th>
              </tr>
            </thead>
            <tbody className="text-text-secondary">
              {Object.keys(metricsData).map(mKey => (
                <tr key={mKey} className="border-b border-white/5 last:border-b-0">
                  <td className="py-2.5"><span className={`px-2 py-0.5 rounded text-[10px] font-bold ${mKey === 'Logistic Regression' ? 'bg-gold-main/20 text-gold-bright border border-gold-main/40' : mKey === 'Random Forest' ? 'bg-blue-team/20 text-blue-team border border-blue-team/40' : 'bg-red-team/20 text-red-team border border-red-team/40'}`}>{mKey === 'Logistic Regression' ? '베이스라인' : mKey === 'Random Forest' ? '비교' : '최적화'}</span></td>
                  <td className="py-2.5 font-bold text-text-primary">{mKey}</td>
                  <td className="py-2.5">{(metricsData[mKey].Accuracy * 100).toFixed(1)}%</td>
                  <td className="py-2.5">{(metricsData[mKey]['F1-Score'] * 100).toFixed(1)}%</td>
                  <td className="py-2.5">{metricsData[mKey]['ROC-AUC'].toFixed(3)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* 6. 🏆 챔피언 선택 모달 */}
      {modalOpen && (
        <div className="fixed inset-0 bg-black/90 backdrop-blur-md z-[2000] flex justify-center items-center p-4">
          <div className="bg-bg-card border-2 border-gold-main rounded-3xl w-full max-w-lg max-h-[80vh] flex flex-col shadow-[0_0_35px_rgba(200,170,110,0.3)] overflow-hidden">
            
            {/* 헤더 */}
            <div className="flex justify-between items-center px-6 py-4 border-b border-border-glass bg-gold-main/5">
              <h3 className="font-outfit font-bold text-gold-bright">
                {activeSlot.team === 'blue' ? '블루팀' : '레드팀'} {LANE_LABELS[activeSlot.index]} 챔피언 선택
              </h3>
              <button onClick={() => setModalOpen(false)} className="text-text-secondary hover:text-white transition outline-none">
                <X size={20} />
              </button>
            </div>

            {/* 검색바 */}
            <div className="px-6 py-3 border-b border-white/5">
              <input
                type="text"
                placeholder="챔피언 이름 검색 (예: 아리, 아트로, Ahri)..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full bg-black/40 border border-border-glass rounded-xl px-4 py-2.5 text-sm text-text-primary placeholder:text-text-secondary/50 outline-none focus:border-gold-main transition"
                autoFocus
              />
            </div>

            {/* 그리드 */}
            <div className="flex-1 overflow-y-auto p-6 bg-black/20 grid grid-cols-4 sm:grid-cols-5 gap-3.5">
              {championsList
                .filter(champ => 
                  champ.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                  champ.id.toLowerCase().includes(searchTerm.toLowerCase())
                )
                .map(champ => (
                  <button
                    key={champ.id}
                    onClick={() => handleSelectChampion(champ.id)}
                    className="flex flex-col items-center gap-1.5 p-2 bg-white/[0.02] border border-white/5 rounded-xl hover:border-gold-main hover:bg-gold-main/5 hover:scale-105 transition-all outline-none"
                  >
                    <img src={champ.image} alt={champ.name} className="w-12 h-12 rounded-lg border border-border-glass" />
                    <span className="text-[10px] font-semibold text-text-primary text-center truncate w-full">{champ.name}</span>
                  </button>
                ))}
            </div>

            {/* 푸터 */}
            <div className="px-6 py-4 border-t border-border-glass bg-gold-main/5 text-right">
              <button
                onClick={handleClearSlot}
                className="bg-red-team/10 border border-red-team/40 text-red-team px-4 py-2 text-xs font-bold rounded-xl hover:bg-red-team/20 transition outline-none"
              >
                비우기 (Clear)
              </button>
            </div>

          </div>
        </div>
      )}
    </div>
  );
}
