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
import { HelpCircle, RefreshCw, X, Shield, Sword, Award, Eye, Coins, Trophy, Flame } from 'lucide-react';
import { getChampionNameKr, calculateCompositionScores, buildLaneFeatures, CHAMPION_NAMES_KR } from './utils/lolEngine';
import { predictMatch, calculateMLCompositionScore } from './utils/predictEngine';
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
  { value: "XGBoost", label: "최적화 모델: XGBoost" },
  { value: "Random Forest", label: "비교 모델: Random Forest" },
  { value: "Logistic Regression", label: "베이스라인: Logistic Regression" }
];

export default function App() {
  // 상태 변수 정의
  const [modelName, setModelName] = useState("XGBoost");
  const [features, setFeatures] = useState({
    blueWardsPlaced: 15, blueWardsDestroyed: 2, blueFirstBlood: 1, blueKills: 5, blueDeaths: 5, blueAssists: 5,
    blueEliteMonsters: 0, blueDragons: 0, blueHeralds: 0, blueTowersDestroyed: 0, blueTotalGold: 16500, blueAvgLevel: 6.8,
    blueTotalExperience: 18000, blueTotalMinionsKilled: 210, blueTotalJungleMinionsKilled: 50,
    blueGoldDiff: 0, blueExperienceDiff: 0, blueCSPerMin: 21.0, blueGoldPerMin: 1650.0,
    redWardsPlaced: 15, redWardsDestroyed: 2, redFirstBlood: 0, redKills: 5, redDeaths: 5, redAssists: 5,
    redEliteMonsters: 0, redDragons: 0, redHeralds: 0, redTowersDestroyed: 0, redTotalGold: 16500, redAvgLevel: 6.8,
    redTotalExperience: 18000, redTotalMinionsKilled: 210, redTotalJungleMinionsKilled: 50,
    redGoldDiff: 0, redExperienceDiff: 0, redCSPerMin: 21.0, redGoldPerMin: 1650.0
  });

  const [selectedBlueChampions, setSelectedBlueChampions] = useState(["", "", "", "", ""]);
  const [selectedRedChampions, setSelectedRedChampions] = useState(["", "", "", "", ""]);
  const [championsList, setChampionsList] = useState([]);
  
  // 모달 상태
  const [modalOpen, setModalOpen] = useState(false);
  const [activeSlot, setActiveSlot] = useState({ team: 'blue', index: 0 });
  const [searchTerm, setSearchTerm] = useState('');
  
  // 분석 탭
  const [activeTab, setActiveTab] = useState('xgb');
  
  // 예측 결과
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
    counters: []
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
        // Fallback
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

  // 실시간 예측 수행
  useEffect(() => {
    const predResult = predictMatch(modelName, features, selectedBlueChampions, selectedRedChampions);
    const compDetails = calculateCompositionScores(selectedBlueChampions, selectedRedChampions);
    
    // ML 기반 조합 점수 매핑
    const mlBlueScore = calculateMLCompositionScore(modelName, selectedBlueChampions, []);
    const mlRedScore = calculateMLCompositionScore(modelName, [], selectedRedChampions);
    
    setPrediction({
      ...predResult,
      blue_comp_score: mlBlueScore,
      red_comp_score: mlRedScore,
      blue_synergies: compDetails.blue_synergies,
      red_synergies: compDetails.red_synergies,
      counters: compDetails.counters
    });
  }, [modelName, features, selectedBlueChampions, selectedRedChampions]);

  // 수치 업데이트 핸들러 (격차 계산 싱크)
  const handleValChange = (id, value) => {
    const val = parseFloat(value);
    setFeatures(prev => {
      const next = { ...prev, [id]: val };
      
      // 킬/데스 대칭 매핑
      if (id === 'blueKills') next.redDeaths = val;
      if (id === 'redDeaths') next.blueKills = val;
      if (id === 'redKills') next.blueDeaths = val;
      if (id === 'blueDeaths') next.redKills = val;
      
      // 골드 격차 및 분당 연산
      if (id === 'blueTotalGold' || id === 'redTotalGold') {
        const diff = next.blueTotalGold - next.redTotalGold;
        next.blueGoldDiff = diff;
        next.redGoldDiff = -diff;
        next.blueGoldPerMin = next.blueTotalGold / 10.0;
        next.redGoldPerMin = next.redTotalGold / 10.0;
      }
      
      // 경험치 격차
      if (id === 'blueTotalExperience' || id === 'redTotalExperience') {
        const diff = next.blueTotalExperience - next.redTotalExperience;
        next.blueExperienceDiff = diff;
        next.redExperienceDiff = -diff;
      }
      
      // CS 격차 분당 cs
      if (id === 'blueTotalMinionsKilled') next.blueCSPerMin = val / 10.0;
      if (id === 'redTotalMinionsKilled') next.redCSPerMin = val / 10.0;

      return next;
    });
  };

  // 퍼스트 블러드 설정
  const handleFBChange = (team) => {
    setFeatures(prev => ({
      ...prev,
      blueFirstBlood: team === 'blue' ? 1 : 0,
      redFirstBlood: team === 'red' ? 1 : 0
    }));
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
    
    // 완성형 체크 (모든 슬롯이 채워졌는지 검사)
    const allSelected = list.every(c => c !== "");
    
    if (allSelected) {
      // 5개 완성 시 모달 닫기
      setModalOpen(false);
    } else if (activeSlot.index < 4) {
      // 다음 슬롯으로 자동 포커스
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

  return (
    <div className="container mx-auto max-w-6xl px-4 py-8 relative">
      <header className="text-center mb-8">
        <h1 className="text-5xl font-extrabold tracking-tight bg-gradient-to-r from-gold-bright to-gold-main bg-clip-text text-transparent filter drop-shadow-[0_0_10px_rgba(200,170,110,0.3)] mb-2">
          HEXTECH EARLY PREDICTOR
        </h1>
        <p className="text-gold-main text-xs font-semibold tracking-[0.25em] uppercase">
          리그 오브 레전드 10분 지표 머신러닝 정밀 분석
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
      </div>

      <div className="flex gap-4 mb-8">
        <button
          onClick={() => handleFBChange('blue')}
          className={`flex-1 py-3 border border-gold-dark/40 rounded-xl text-sm font-semibold transition ${features.blueFirstBlood === 1 ? 'bg-gold-main text-bg-deep shadow-glow-gold font-bold' : 'text-text-secondary hover:bg-white/5'}`}
        >
          🔵 블루팀 퍼스트 블러드 획득
        </button>
        <button
          onClick={() => handleFBChange('red')}
          className={`flex-1 py-3 border border-gold-dark/40 rounded-xl text-sm font-semibold transition ${features.redFirstBlood === 1 ? 'bg-gold-main text-bg-deep shadow-glow-gold font-bold' : 'text-text-secondary hover:bg-white/5'}`}
        >
          🔴 레드팀 퍼스트 블러드 획득
        </button>
      </div>

      {/* 2. 🗺️ 소환사의 협곡 대시보드 맵 (핵심 시각화) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-8">
        {/* 소환사의 협곡 맵 영역 (7/12) */}
        <div className="lg:col-span-7 bg-bg-card border border-border-glass rounded-3xl p-4 shadow-glow flex flex-col justify-center items-center relative overflow-hidden">
          <h3 className="text-gold-bright mb-4 text-sm font-bold border-l-4 border-gold-main pl-3 self-start">
            🗺️ 소환사의 협곡 인게임 라인 지표 설정
          </h3>
          
          <div className="w-full aspect-square max-w-[550px] relative rounded-2xl overflow-hidden border border-border-glass shadow-[0_0_20px_rgba(0,0,0,0.8)]"
               style={{
                 backgroundImage: 'url("https://ddragon.leagueoflegends.com/cdn/6.8.1/img/map/map11.png")',
                 backgroundSize: 'cover',
                 backgroundPosition: 'center'
               }}>
            
            {/* 1. TOP 패널 */}
            <div className="absolute top-[8%] left-[8%] bg-bg-card/95 border border-border-glass rounded-xl p-2.5 w-[200px] backdrop-blur-md shadow-glow hover:border-gold-main transition-all group">
              <div className="flex justify-between items-center text-[10px] text-gold-main font-bold border-b border-border-glass pb-1 mb-1">
                <span>📍 TOP LANE</span>
                <span className="text-text-secondary group-hover:text-gold-bright transition">골드 / KDA</span>
              </div>
              <div className="flex flex-col gap-1.5">
                <div className="flex items-center justify-between text-xs">
                  <span className="text-blue-team font-semibold">🔵 KDA</span>
                  <div className="flex gap-1 items-center">
                    <input type="number" value={features.blueKills} onChange={(e) => handleValChange('blueKills', e.target.value)} className="w-8 bg-black/60 border border-border-glass rounded text-center text-xs p-0.5 outline-none" />
                    <span>/</span>
                    <input type="number" value={features.blueDeaths} onChange={(e) => handleValChange('blueDeaths', e.target.value)} className="w-8 bg-black/60 border border-border-glass rounded text-center text-xs p-0.5 outline-none" />
                  </div>
                </div>
                <div className="flex flex-col gap-0.5">
                  <div className="flex justify-between text-[10px] text-text-secondary">
                    <span>골드</span>
                    <span className="text-gold-bright font-bold">{features.blueTotalGold.toLocaleString()} G</span>
                  </div>
                  <input type="range" min="5000" max="30000" step="100" value={features.blueTotalGold} onChange={(e) => handleValChange('blueTotalGold', e.target.value)} className="h-1" />
                </div>
              </div>
            </div>

            {/* 2. JUNGLE 패널 */}
            <div className="absolute top-[35%] left-[22%] bg-bg-card/95 border border-border-glass rounded-xl p-2.5 w-[200px] backdrop-blur-md shadow-glow hover:border-gold-main transition-all group">
              <div className="flex justify-between items-center text-[10px] text-gold-main font-bold border-b border-border-glass pb-1 mb-1">
                <span>📍 JUNGLE</span>
                <span className="text-text-secondary">오브젝트 / 골드</span>
              </div>
              <div className="flex flex-col gap-2">
                <div className="flex justify-between items-center text-xs gap-1">
                  <span className="text-gold-bright text-[10px]">🐉 용</span>
                  <div className="flex gap-1">
                    <button onClick={() => handleValChange('blueDragons', 0)} className={`px-1.5 py-0.5 rounded text-[9px] ${features.blueDragons === 0 ? 'bg-gold-main text-bg-deep font-bold' : 'bg-black/40 border border-border-glass'}`}>0</button>
                    <button onClick={() => handleValChange('blueDragons', 1)} className={`px-1.5 py-0.5 rounded text-[9px] ${features.blueDragons === 1 ? 'bg-gold-main text-bg-deep font-bold' : 'bg-black/40 border border-border-glass'}`}>1</button>
                    <button onClick={() => handleValChange('blueDragons', 2)} className={`px-1.5 py-0.5 rounded text-[9px] ${features.blueDragons === 2 ? 'bg-gold-main text-bg-deep font-bold' : 'bg-black/40 border border-border-glass'}`}>2</button>
                  </div>
                </div>
                <div className="flex justify-between items-center text-xs gap-1">
                  <span className="text-gold-bright text-[10px]">👾 유충</span>
                  <input type="number" min="0" max="6" value={features.blueEliteMonsters} onChange={(e) => handleValChange('blueEliteMonsters', e.target.value)} className="w-8 bg-black/60 border border-border-glass rounded text-center text-[10px] p-0.5 outline-none" />
                </div>
                <div className="flex flex-col gap-0.5">
                  <div className="flex justify-between text-[10px] text-text-secondary">
                    <span>CS (정글)</span>
                    <span className="text-gold-bright">{features.blueTotalJungleMinionsKilled}</span>
                  </div>
                  <input type="range" min="0" max="100" value={features.blueTotalJungleMinionsKilled} onChange={(e) => handleValChange('blueTotalJungleMinionsKilled', e.target.value)} className="h-1" />
                </div>
              </div>
            </div>

            {/* 3. MID 패널 */}
            <div className="absolute top-[48%] right-[8%] bg-bg-card/95 border border-border-glass rounded-xl p-2.5 w-[200px] backdrop-blur-md shadow-glow hover:border-gold-main transition-all group">
              <div className="flex justify-between items-center text-[10px] text-gold-main font-bold border-b border-border-glass pb-1 mb-1">
                <span>📍 MID LANE</span>
                <span className="text-text-secondary">골드 / CS</span>
              </div>
              <div className="flex flex-col gap-1.5">
                <div className="flex justify-between text-xs">
                  <span className="text-gold-bright text-[10px]">미니언 CS</span>
                  <div className="flex items-center gap-1">
                    <input type="number" min="0" max="300" value={features.blueTotalMinionsKilled} onChange={(e) => handleValChange('blueTotalMinionsKilled', e.target.value)} className="w-12 bg-black/60 border border-border-glass rounded text-center text-xs p-0.5 outline-none" />
                  </div>
                </div>
                <div className="flex flex-col gap-0.5">
                  <div className="flex justify-between text-[10px] text-text-secondary">
                    <span>레드팀 골드</span>
                    <span className="text-gold-bright font-bold">{features.redTotalGold.toLocaleString()} G</span>
                  </div>
                  <input type="range" min="5000" max="30000" step="100" value={features.redTotalGold} onChange={(e) => handleValChange('redTotalGold', e.target.value)} className="h-1" />
                </div>
              </div>
            </div>

            {/* 4. BOT 패널 */}
            <div className="absolute bottom-[8%] right-[8%] bg-bg-card/95 border border-border-glass rounded-xl p-2.5 w-[200px] backdrop-blur-md shadow-glow hover:border-gold-main transition-all group">
              <div className="flex justify-between items-center text-[10px] text-gold-main font-bold border-b border-border-glass pb-1 mb-1">
                <span>📍 BOT LANE</span>
                <span className="text-text-secondary">바텀 포탑 / 시야</span>
              </div>
              <div className="flex flex-col gap-2">
                <div className="flex justify-between items-center text-xs gap-1">
                  <span className="text-gold-bright text-[10px]">🏰 포탑 파괴</span>
                  <div className="flex gap-1">
                    <button onClick={() => handleValChange('blueTowersDestroyed', 0)} className={`px-1.5 py-0.5 rounded text-[9px] ${features.blueTowersDestroyed === 0 ? 'bg-gold-main text-bg-deep font-bold' : 'bg-black/40 border border-border-glass'}`}>0</button>
                    <button onClick={() => handleValChange('blueTowersDestroyed', 1)} className={`px-1.5 py-0.5 rounded text-[9px] ${features.blueTowersDestroyed === 1 ? 'bg-gold-main text-bg-deep font-bold' : 'bg-black/40 border border-border-glass'}`}>1</button>
                    <button onClick={() => handleValChange('blueTowersDestroyed', 2)} className={`px-1.5 py-0.5 rounded text-[9px] ${features.blueTowersDestroyed === 2 ? 'bg-gold-main text-bg-deep font-bold' : 'bg-black/40 border border-border-glass'}`}>2</button>
                  </div>
                </div>
                <div className="flex justify-between items-center text-xs gap-1">
                  <span className="text-gold-bright text-[10px]">👁️ 와드 설치</span>
                  <input type="number" min="0" max="100" value={features.blueWardsPlaced} onChange={(e) => handleValChange('blueWardsPlaced', e.target.value)} className="w-12 bg-black/60 border border-border-glass rounded text-center text-xs p-0.5 outline-none" />
                </div>
              </div>
            </div>

          </div>
        </div>

        {/* 밴픽 조합 설정 영역 (5/12) */}
        <div className="lg:col-span-5 flex flex-col gap-6">
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
                    className={`aspect-square border border-border-glass rounded-xl overflow-hidden flex flex-col justify-center items-center bg-black/40 hover:border-blue-team hover:shadow-glow-blue transition group relative`}
                  >
                    {c ? (
                      <>
                        <img src={`https://ddragon.leagueoflegends.com/cdn/14.22.1/img/champion/${c}.png`} alt={c} className="w-full h-full object-cover" />
                        <div className="absolute bottom-0 left-0 right-0 bg-black/80 text-white text-[8px] py-0.5 truncate text-center font-semibold">{getChampionNameKr(c)}</div>
                      </>
                    ) : (
                      <>
                        <span className="text-text-secondary text-sm group-hover:scale-110 transition duration-300">🛡️</span>
                        <span className="text-[8px] text-text-secondary mt-1">포지션 {i + 1}</span>
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
                    className={`aspect-square border border-border-glass rounded-xl overflow-hidden flex flex-col justify-center items-center bg-black/40 hover:border-red-team hover:shadow-glow-red transition group relative`}
                  >
                    {c ? (
                      <>
                        <img src={`https://ddragon.leagueoflegends.com/cdn/14.22.1/img/champion/${c}.png`} alt={c} className="w-full h-full object-cover" />
                        <div className="absolute bottom-0 left-0 right-0 bg-black/80 text-white text-[8px] py-0.5 truncate text-center font-semibold">{getChampionNameKr(c)}</div>
                      </>
                    ) : (
                      <>
                        <span className="text-text-secondary text-sm group-hover:scale-110 transition duration-300">⚔️</span>
                        <span className="text-[8px] text-text-secondary mt-1">포지션 {i + 1}</span>
                      </>
                    )}
                  </button>
                ))}
              </div>
            </div>

            {/* 시너지 효과 & 상성 리포트 패널 */}
            {(prediction.blue_synergies.length > 0 || prediction.red_synergies.length > 0 || prediction.counters.length > 0) ? (
              <div className="border-t border-border-glass pt-4 mt-4 grid grid-cols-2 gap-4 text-[10px]">
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

      {/* 3. 드래곤 가치 환산 정보 배너 */}
      {features.blueDragons !== features.redDragons && (
        <div className="bg-gradient-to-r from-gold-dark/10 via-bg-card to-gold-dark/10 border border-border-glass rounded-2xl p-5 mb-8 shadow-glow flex items-center gap-4 animate-fade-in">
          <span className="text-4xl filter drop-shadow-[0_0_8px_rgba(200,170,110,0.5)]">🐉</span>
          <div>
            <h4 className="font-outfit font-bold text-sm text-gold-bright mb-1 uppercase tracking-wider">
              {features.blueDragons > features.redDragons ? '블루팀' : '레드팀'} 드래곤 가치 환산
            </h4>
            <p className="text-xs text-text-secondary leading-relaxed">
              {modelName} 분석 결과, {features.blueDragons > features.redDragons ? '블루팀' : '레드팀'}이 획득한 드래곤은 게임 승률 관점에서 약 <strong className="text-gold-main font-extrabold text-shadow-glow">{(prediction.dragon_gold_value * Math.max(features.blueDragons, features.redDragons)).toLocaleString()} 골드</strong>(1마리당 약 {Math.round(prediction.dragon_gold_value).toLocaleString()} 골드)의 격차를 벌린 것과 동일한 Odds 상승 효과를 가집니다.
            </p>
          </div>
        </div>
      )}

      {/* 4. 모델 정밀 분석 대시보드 */}
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

      {/* 5. 🏆 챔피언 선택 모달 */}
      {modalOpen && (
        <div className="fixed inset-0 bg-black/90 backdrop-blur-md z-[2000] flex justify-center items-center p-4">
          <div className="bg-bg-card border-2 border-gold-main rounded-3xl w-full max-w-lg max-h-[80vh] flex flex-col shadow-[0_0_35px_rgba(200,170,110,0.3)] overflow-hidden">
            
            {/* 헤더 */}
            <div className="flex justify-between items-center px-6 py-4 border-b border-border-glass bg-gold-main/5">
              <h3 className="font-outfit font-bold text-gold-bright">
                {activeSlot.team === 'blue' ? '블루팀' : '레드팀'} 포지션 {activeSlot.index + 1} 챔피언 선택
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
