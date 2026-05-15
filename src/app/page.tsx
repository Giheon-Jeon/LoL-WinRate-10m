"use client";

import { useState, useEffect, useCallback } from "react";

// Types for ML Model Metrics
interface ModelMetrics {
  Accuracy: number;
  Precision: number;
  Recall: number;
  "F1-Score": number;
  "ROC-AUC": number;
}

interface MetricsMap {
  [modelName: string]: ModelMetrics;
}

interface PredictionResponse {
  model_used: string;
  prediction: number;
  winner: string;
  blue_win_probability: number;
  red_win_probability: number;
}

export default function Home() {
  // Backend URL (FastAPI)
  const API_URL = "http://localhost:8000";

  // State Management
  const [selectedModel, setSelectedModel] = useState<string>("XGBoost");
  const [metrics, setMetrics] = useState<MetricsMap | null>(null);
  const [loadingMetrics, setLoadingMetrics] = useState<boolean>(true);
  const [metricsError, setMetricsError] = useState<string | null>(null);
  const [isTraining, setIsTraining] = useState<boolean>(false);

  // Early 10 mins game features state
  const [features, setFeatures] = useState({
    // Blue Team
    blueWardsPlaced: 15,
    blueWardsDestroyed: 2,
    blueFirstBlood: 1, // 1: Blue, 0: Red
    blueKills: 6,
    blueDeaths: 4,
    blueAssists: 6,
    blueDragons: 1,
    blueHeralds: 0,
    blueTowersDestroyed: 0,
    blueTotalGold: 16800,
    blueTotalExperience: 18200,
    blueTotalMinionsKilled: 215,
    blueTotalJungleMinionsKilled: 50,
    blueAvgLevel: 6.8,
    
    // Red Team
    redWardsPlaced: 14,
    redWardsDestroyed: 3,
    redKills: 4,
    redDeaths: 6,
    redAssists: 4,
    redDragons: 0,
    redHeralds: 1,
    redTowersDestroyed: 0,
    redTotalGold: 15400,
    redTotalExperience: 17200,
    redTotalMinionsKilled: 205,
    redTotalJungleMinionsKilled: 48,
    redAvgLevel: 6.8,
  });

  // Prediction Result State
  const [prediction, setPrediction] = useState<PredictionResponse | null>(null);
  const [isPredicting, setIsPredicting] = useState<boolean>(false);
  const [predictionError, setPredictionError] = useState<string | null>(null);

  // Scoreboard Vision Scanning States
  const [isScanning, setIsScanning] = useState<boolean>(false);
  const [scanError, setScanError] = useState<string | null>(null);
  const [scanSuccessMsg, setScanSuccessMsg] = useState<string | null>(null);
  const [highlightedFields, setHighlightedFields] = useState<string[]>([]);

  // Fetch metrics from backend
  const fetchMetrics = useCallback(async () => {
    setLoadingMetrics(true);
    setMetricsError(null);
    try {
      const res = await fetch(`${API_URL}/api/metrics`);
      if (!res.ok) {
        throw new Error("서버에서 메트릭 정보를 불러오는데 실패했습니다.");
      }
      const data = await res.json();
      setMetrics(data);
    } catch (err: unknown) {
      console.error(err);
      const msg = err instanceof Error ? err.message : String(err);
      setMetricsError(msg || "백엔드 연결 실패. 서버가 구동 중인지 확인해 주세요.");
    } finally {
      setLoadingMetrics(false);
    }
  }, [API_URL]);

  // Request Prediction from ML Server
  const getPrediction = useCallback(async (currentFeatures = features, currentModel = selectedModel) => {
    setIsPredicting(true);
    setPredictionError(null);
    
    // Auto align matching opposing features before sending
    const alignedFeatures = {
      ...currentFeatures,
      // Deaths of Blue is always Kills of Red
      redDeaths: currentFeatures.blueKills,
      blueDeaths: currentFeatures.redKills,
      // First blood is exclusive
      redFirstBlood: currentFeatures.blueFirstBlood === 1 ? 0 : 1,
    };

    try {
      const res = await fetch(`${API_URL}/api/predict?model_name=${encodeURIComponent(currentModel)}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(alignedFeatures),
      });

      if (!res.ok) {
        throw new Error("서버에서 예측값을 반환하는 데 실패했습니다.");
      }

      const data = await res.json();
      setPrediction(data);
      setPredictionError(null);
    } catch (err: unknown) {
      console.error(err);
      const msg = err instanceof Error ? err.message : String(err);
      setPredictionError(msg || "예측 오류가 발생했습니다. 백엔드 연결을 확인하세요.");
      // Don't clear prediction here to keep old data visible, 
      // but the error will show if we handle it in UI
    } finally {
      setIsPredicting(false);
    }
  }, [features, selectedModel, API_URL]);

  // Handle Scoreboard Image Scanning via FastAPI Vision API
  const handleImageUpload = useCallback(async (file: File) => {
    setIsScanning(true);
    setScanError(null);
    setScanSuccessMsg(null);
    setHighlightedFields([]);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch(`${API_URL}/api/parse-scoreboard`, {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        throw new Error("스코어보드 이미지 분석에 실패했습니다.");
      }

      const data = await res.json();
      
      if (data.is_mocked) {
        setScanSuccessMsg("데모 모드: 예시 이미지를 기준으로 분석된 데이터가 주입되었습니다. (.env에 GEMINI_API_KEY를 설정하시면 실제 이미지가 분석됩니다)");
      } else {
        setScanSuccessMsg("성공: 스코어보드 이미지의 수치가 정확하게 감지 및 주입되었습니다!");
      }

      const newFeatures = {
        blueWardsPlaced: typeof data.blueWardsPlaced === "number" ? data.blueWardsPlaced : features.blueWardsPlaced,
        blueWardsDestroyed: typeof data.blueWardsDestroyed === "number" ? data.blueWardsDestroyed : features.blueWardsDestroyed,
        blueFirstBlood: typeof data.blueFirstBlood === "number" ? data.blueFirstBlood : features.blueFirstBlood,
        blueKills: typeof data.blueKills === "number" ? data.blueKills : features.blueKills,
        blueDeaths: typeof data.blueDeaths === "number" ? data.blueDeaths : features.blueDeaths,
        blueAssists: typeof data.blueAssists === "number" ? data.blueAssists : features.blueAssists,
        blueDragons: typeof data.blueDragons === "number" ? data.blueDragons : features.blueDragons,
        blueHeralds: typeof data.blueHeralds === "number" ? data.blueHeralds : features.blueHeralds,
        blueTowersDestroyed: typeof data.blueTowersDestroyed === "number" ? data.blueTowersDestroyed : features.blueTowersDestroyed,
        blueTotalGold: typeof data.blueTotalGold === "number" ? data.blueTotalGold : features.blueTotalGold,
        blueTotalExperience: typeof data.blueTotalExperience === "number" ? data.blueTotalExperience : features.blueTotalExperience,
        blueTotalMinionsKilled: typeof data.blueTotalMinionsKilled === "number" ? data.blueTotalMinionsKilled : features.blueTotalMinionsKilled,
        blueTotalJungleMinionsKilled: typeof data.blueTotalJungleMinionsKilled === "number" ? data.blueTotalJungleMinionsKilled : features.blueTotalJungleMinionsKilled,
        
        redWardsPlaced: typeof data.redWardsPlaced === "number" ? data.redWardsPlaced : features.redWardsPlaced,
        redWardsDestroyed: typeof data.redWardsDestroyed === "number" ? data.redWardsDestroyed : features.redWardsDestroyed,
        redKills: typeof data.redKills === "number" ? data.redKills : features.redKills,
        redDeaths: typeof data.redDeaths === "number" ? data.redDeaths : features.redDeaths,
        redAssists: typeof data.redAssists === "number" ? data.redAssists : features.redAssists,
        redDragons: typeof data.redDragons === "number" ? data.redDragons : features.redDragons,
        redHeralds: typeof data.redHeralds === "number" ? data.redHeralds : features.redHeralds,
        redTowersDestroyed: typeof data.redTowersDestroyed === "number" ? data.redTowersDestroyed : features.redTowersDestroyed,
        redTotalGold: typeof data.redTotalGold === "number" ? data.redTotalGold : features.redTotalGold,
        redTotalExperience: typeof data.redTotalExperience === "number" ? data.redTotalExperience : features.redTotalExperience,
        redTotalMinionsKilled: typeof data.redTotalMinionsKilled === "number" ? data.redTotalMinionsKilled : features.redTotalMinionsKilled,
        redTotalJungleMinionsKilled: typeof data.redTotalJungleMinionsKilled === "number" ? data.redTotalJungleMinionsKilled : features.redTotalJungleMinionsKilled,
        blueAvgLevel: typeof data.blueAvgLevel === "number" ? data.blueAvgLevel : features.blueAvgLevel,
        redAvgLevel: typeof data.redAvgLevel === "number" ? data.redAvgLevel : features.redAvgLevel,
      };

      setFeatures(newFeatures);

      // Trigger highlighters for changed fields
      const changed: string[] = [];
      Object.keys(newFeatures).forEach((key) => {
        if (newFeatures[key as keyof typeof newFeatures] !== features[key as keyof typeof features]) {
          changed.push(key);
        }
      });
      setHighlightedFields(changed);

      // Clear highlights after 4 seconds
      setTimeout(() => {
        setHighlightedFields([]);
      }, 4000);

      // Request new prediction immediately
      getPrediction(newFeatures, selectedModel);

    } catch (err: unknown) {
      console.error(err);
      const msg = err instanceof Error ? err.message : String(err);
      setScanError(msg || "이미지 분석 오류가 발생했습니다.");
    } finally {
      setIsScanning(false);
    }
  }, [features, selectedModel, getPrediction, API_URL]);

  // Support pasting image from clipboard directly
  useEffect(() => {
    const handlePaste = (e: ClipboardEvent) => {
      if (e.clipboardData && e.clipboardData.files && e.clipboardData.files[0]) {
        const file = e.clipboardData.files[0];
        if (file.type.startsWith("image/")) {
          handleImageUpload(file);
        }
      }
    };
    window.addEventListener("paste", handlePaste);
    return () => window.removeEventListener("paste", handlePaste);
  }, [handleImageUpload]);

  // Trigger Model Re-training
  const handleRetrain = async () => {
    setIsTraining(true);
    try {
      const res = await fetch(`${API_URL}/api/train`, { method: "POST" });
      if (!res.ok) throw new Error("모델 재학습에 실패했습니다.");
      const data = await res.json();
      setMetrics(data.metrics);
      alert("머신러닝 모델 재학습이 완료되었습니다!");
      // Re-trigger prediction with the newly trained model
      getPrediction();
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : String(err);
      alert(msg);
    } finally {
      setIsTraining(false);
    }
  };

  // Initial Fetch & Predict
  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    fetchMetrics();
  }, [fetchMetrics]);

  useEffect(() => {
    // Debounce predictions to avoid spamming the backend during slider changes
    const timer = setTimeout(() => {
      getPrediction();
    }, 400);
    return () => clearTimeout(timer);
  }, [features, selectedModel, getPrediction]);

  // Feature change handler with interactive balancing
  const handleFeatureChange = (name: string, value: number) => {
    setFeatures(prev => {
      const updated = { ...prev, [name]: value };
      
      // Smart Auto-balancing for competitive fairness
      if (name === "blueKills") {
        updated.redDeaths = value;
        // Adjust Gold & EXP dynamically on kills
        updated.blueTotalGold = prev.blueTotalGold + (value - prev.blueKills) * 300;
        updated.blueTotalExperience = prev.blueTotalExperience + (value - prev.blueKills) * 150;
      } else if (name === "redKills") {
        updated.blueDeaths = value;
        // Adjust Gold & EXP dynamically on kills
        updated.redTotalGold = prev.redTotalGold + (value - prev.redKills) * 300;
        updated.redTotalExperience = prev.redTotalExperience + (value - prev.redKills) * 150;
      } else if (name === "blueTotalMinionsKilled") {
        // 1 CS is around 20 gold
        updated.blueTotalGold = prev.blueTotalGold + (value - prev.blueTotalMinionsKilled) * 20;
      } else if (name === "redTotalMinionsKilled") {
        updated.redTotalGold = prev.redTotalGold + (value - prev.redTotalMinionsKilled) * 20;
      } else if (name === "blueDragons") {
        // Dragon objective grants gold & buffs
        updated.blueTotalGold = prev.blueTotalGold + (value - prev.blueDragons) * 100;
      } else if (name === "redDragons") {
        updated.redTotalGold = prev.redTotalGold + (value - prev.redDragons) * 100;
      } else if (name === "blueTowersDestroyed") {
        // Tower objective grants massive gold
        updated.blueTotalGold = prev.blueTotalGold + (value - prev.blueTowersDestroyed) * 250;
      } else if (name === "redTowersDestroyed") {
        updated.redTotalGold = prev.redTotalGold + (value - prev.redTowersDestroyed) * 250;
      } else if (name === "blueTotalExperience") {
        // Levels are tied to Experience
        updated.blueAvgLevel = Number((value / 2650).toFixed(1));
      } else if (name === "redTotalExperience") {
        updated.redAvgLevel = Number((value / 2650).toFixed(1));
      }
      
      return updated;
    });
    
    // Provide instant feedback for manual changes too
    setHighlightedFields([name]);
    const timer = setTimeout(() => setHighlightedFields([]), 800);
    return () => clearTimeout(timer);
  };

  // Helper to format float to percentage
  const toPercent = (val: number) => `${(val * 100).toFixed(1)}%`;

  return (
    <div className="container">
      {/* HEADER SECTION */}
      <header style={{ textAlign: "center", marginBottom: "3rem", position: "relative" }}>
        <h1 style={{ fontSize: "2.8rem", color: "var(--gold-bright)", textShadow: "0 0 20px rgba(200, 170, 110, 0.4)", marginBottom: "0.5rem" }}>
          HEXTECH Early Predictor
        </h1>
        <p style={{ color: "var(--gold-main)", fontSize: "1.1rem", textTransform: "uppercase", letterSpacing: "0.15em" }}>
          early 10-minute lol match winrate ml engine
        </p>
        <div style={{ width: "120px", height: "1px", background: "var(--gold-main)", margin: "1rem auto" }}></div>
      </header>

      {/* CORE WORKSPACE GRID */}
      <main style={{ display: "grid", gridTemplateColumns: "1.1fr 0.9fr", gap: "2.5rem" }} className="grid-cols-2">
        
        {/* LEFT COLUMN: INTERACTIVE CONTROLLER (SANDBOX) */}
        <section style={{ display: "flex", flexDirection: "column", gap: "2rem" }}>
          
          {/* HEXTECH SCOREBOARD VISION SCANNER */}
          <div className="card-hextech scanner-container" style={{ padding: "2rem" }}>
            {isScanning && <div className="scanner-laser"></div>}
            
            <h2 style={{ fontSize: "1.4rem", marginBottom: "1rem", borderBottom: "1px solid var(--border-gold)", paddingBottom: "0.5rem", display: "flex", alignItems: "center", gap: "0.5rem" }}>
              <span>👁️ HEXTECH VISION SCOREBOARD SCANNER</span>
              <span style={{ fontSize: "0.75rem", background: "rgba(200, 170, 110, 0.1)", padding: "0.2rem 0.5rem", borderRadius: "3px", color: "var(--gold-main)" }}>BETA</span>
            </h2>
            
            <p style={{ fontSize: "0.9rem", color: "var(--text-secondary)", marginBottom: "1.2rem" }}>
              인게임 스코어보드(Tab키 화면) 캡처본을 업로드해 보세요! AI가 인게임 데이터(KDA, CS, 레벨 등)를 감지하여 예측 모델에 맞게 자동으로 채워줍니다.
            </p>

            {/* Upload Area */}
            <div 
              className="upload-zone"
              onClick={() => document.getElementById("scoreboard-file-input")?.click()}
              onDragOver={(e) => {
                e.preventDefault();
                e.stopPropagation();
              }}
              onDrop={(e) => {
                e.preventDefault();
                e.stopPropagation();
                if (e.dataTransfer.files && e.dataTransfer.files[0]) {
                  handleImageUpload(e.dataTransfer.files[0]);
                }
              }}
            >
              <input 
                id="scoreboard-file-input"
                type="file" 
                accept="image/*" 
                style={{ display: "none" }} 
                onChange={(e) => {
                  if (e.target.files && e.target.files[0]) {
                    handleImageUpload(e.target.files[0]);
                  }
                }}
              />
              
              {isScanning ? (
                <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "1rem" }}>
                  <div style={{ width: "40px", height: "40px", border: "3px solid var(--gold-dark)", borderTop: "3px solid var(--gold-bright)", borderRadius: "50%", animation: "spin 1s linear infinite" }}></div>
                  <p style={{ color: "var(--gold-bright)", fontWeight: "bold", fontFamily: "var(--font-display)" }}>헥스테크 마법 공학 렌즈 분석 중...</p>
                </div>
              ) : (
                <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "0.5rem" }}>
                  <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" style={{ color: "var(--gold-main)" }}>
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                    <polyline points="17 8 12 3 7 8" />
                    <line x1="12" y1="3" x2="12" y2="15" />
                  </svg>
                  <p style={{ fontWeight: "bold", color: "var(--text-primary)" }}>이미지를 드래그 앤 드롭하거나 클릭하여 업로드</p>
                  <p style={{ fontSize: "0.8rem", color: "var(--text-muted)" }}>PNG, JPG, WebP 지원 (클립보드 스크린샷 붙여넣기 가능)</p>
                </div>
              )}
            </div>

            {/* Feedback messages */}
            {scanSuccessMsg && (
              <div style={{ marginTop: "1rem", color: "var(--gold-bright)", padding: "0.75rem 1rem", background: "rgba(200, 170, 110, 0.08)", borderRadius: "6px", border: "1px solid rgba(200, 170, 110, 0.2)", fontSize: "0.85rem", display: "flex", gap: "0.5rem", alignItems: "center" }}>
                <span>✨</span>
                <span>{scanSuccessMsg}</span>
              </div>
            )}

            {scanError && (
              <div style={{ marginTop: "1rem", color: "var(--red-team)", padding: "0.75rem 1rem", background: "rgba(232, 64, 87, 0.08)", borderRadius: "6px", border: "1px solid rgba(232, 64, 87, 0.2)", fontSize: "0.85rem", display: "flex", gap: "0.5rem", alignItems: "center" }}>
                <span>⚠️</span>
                <span>{scanError}</span>
              </div>
            )}
          </div>

          <div className="card-hextech" style={{ padding: "2rem" }}>
            <h2 style={{ fontSize: "1.4rem", marginBottom: "1.5rem", borderBottom: "1px solid var(--border-gold)", paddingBottom: "0.5rem", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <span>🎮 EARLY GAME SANDBOX (10 MINS)</span>
              <button 
                onClick={() => setFeatures({
                  blueWardsPlaced: 15, blueWardsDestroyed: 2, blueFirstBlood: 1, blueKills: 6, blueDeaths: 4, blueAssists: 6, blueDragons: 1, blueHeralds: 0, blueTowersDestroyed: 0, blueTotalGold: 16800, blueTotalExperience: 18200, blueTotalMinionsKilled: 215, blueTotalJungleMinionsKilled: 50,
                  redWardsPlaced: 14, redWardsDestroyed: 3, redKills: 4, redDeaths: 6, redAssists: 4, redDragons: 0, redHeralds: 1, redTowersDestroyed: 0, redTotalGold: 15400, redTotalExperience: 17200, redTotalMinionsKilled: 205, redTotalJungleMinionsKilled: 48,
                })}
                style={{ fontSize: "0.8rem", background: "transparent", border: "1px solid var(--gold-main)", color: "var(--gold-main)", padding: "0.25rem 0.5rem", borderRadius: "3px", cursor: "pointer" }}
              >
                초기화
              </button>
            </h2>

            {/* TEAM GRID VS ROW */}
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "2rem" }} className="grid-cols-2">
              
              {/* BLUE TEAM (LEFT SIDE) */}
              <div style={{ borderRight: "1px solid rgba(255,255,255,0.05)", paddingRight: "1rem" }}>
                <h3 className="text-blue" style={{ fontSize: "1.2rem", marginBottom: "1.5rem", display: "flex", alignItems: "center", gap: "0.5rem" }}>
                  <span style={{ display: "inline-block", width: "10px", height: "10px", borderRadius: "50%", backgroundColor: "var(--blue-team)", boxShadow: "var(--shadow-blue)" }}></span>
                  블루 진영 (Blue Team)
                </h3>

                {/* Blue Kills Slider */}
                <div className={highlightedFields.includes("blueKills") ? "highlight-pulse" : ""} style={{ marginBottom: "1.2rem", padding: highlightedFields.includes("blueKills") ? "0.5rem" : "0", transition: "all 0.3s ease" }}>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.9rem" }}>
                    <span>총 킬수 (Kills)</span>
                    <strong className="text-blue">{features.blueKills}</strong>
                  </div>
                  <input 
                    type="range" min="0" max="25" className="range-slider blue-slider"
                    value={features.blueKills} 
                    onChange={(e) => handleFeatureChange("blueKills", parseInt(e.target.value))}
                  />
                </div>

                {/* Blue Total Gold Slider */}
                <div className={highlightedFields.includes("blueTotalGold") ? "highlight-pulse" : ""} style={{ marginBottom: "1.2rem", padding: highlightedFields.includes("blueTotalGold") ? "0.5rem" : "0", transition: "all 0.3s ease" }}>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.9rem" }}>
                    <span>총 획득 골드 (Gold)</span>
                    <strong className="text-blue">{features.blueTotalGold.toLocaleString()}G</strong>
                  </div>
                  <input 
                    type="range" min="10000" max="25000" step="100" className="range-slider blue-slider"
                    value={features.blueTotalGold} 
                    onChange={(e) => handleFeatureChange("blueTotalGold", parseInt(e.target.value))}
                  />
                </div>

                {/* Blue CS Slider */}
                <div className={highlightedFields.includes("blueTotalMinionsKilled") ? "highlight-pulse" : ""} style={{ marginBottom: "1.2rem", padding: highlightedFields.includes("blueTotalMinionsKilled") ? "0.5rem" : "0", transition: "all 0.3s ease" }}>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.9rem" }}>
                    <span>미니언 처치수 (CS)</span>
                    <strong className="text-blue">{features.blueTotalMinionsKilled}</strong>
                  </div>
                  <input 
                    type="range" min="100" max="300" className="range-slider blue-slider"
                    value={features.blueTotalMinionsKilled} 
                    onChange={(e) => handleFeatureChange("blueTotalMinionsKilled", parseInt(e.target.value))}
                  />
                </div>

                {/* Blue Objective Counters */}
                <div className={`grid-cols-3 ${["blueDragons", "blueHeralds", "blueTowersDestroyed"].some(f => highlightedFields.includes(f)) ? "highlight-pulse" : ""}`} style={{ display: "flex", gap: "1rem", marginTop: "1rem", padding: ["blueDragons", "blueHeralds", "blueTowersDestroyed"].some(f => highlightedFields.includes(f)) ? "0.5rem" : "0", transition: "all 0.3s ease" }}>
                  <div style={{ background: "rgba(255,255,255,0.02)", padding: "0.5rem", borderRadius: "4px", textAlign: "center" }}>
                    <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textTransform: "uppercase" }}>드래곤</div>
                    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: "0.5rem", marginTop: "0.25rem" }}>
                      <button style={{ background: "transparent", border: "none", color: "var(--blue-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("blueDragons", Math.max(0, features.blueDragons - 1))}>-</button>
                      <span style={{ fontSize: "1rem", color: "var(--text-primary)" }}>{features.blueDragons}</span>
                      <button style={{ background: "transparent", border: "none", color: "var(--blue-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("blueDragons", Math.min(2, features.blueDragons + 1))}>+</button>
                    </div>
                  </div>
                  
                  <div style={{ background: "rgba(255,255,255,0.02)", padding: "0.5rem", borderRadius: "4px", textAlign: "center" }}>
                    <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textTransform: "uppercase" }}>전령</div>
                    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: "0.5rem", marginTop: "0.25rem" }}>
                      <button style={{ background: "transparent", border: "none", color: "var(--blue-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("blueHeralds", Math.max(0, features.blueHeralds - 1))}>-</button>
                      <span style={{ fontSize: "1rem", color: "var(--text-primary)" }}>{features.blueHeralds}</span>
                      <button style={{ background: "transparent", border: "none", color: "var(--blue-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("blueHeralds", Math.min(1, features.blueHeralds + 1))}>+</button>
                    </div>
                  </div>

                  <div style={{ background: "rgba(255,255,255,0.02)", padding: "0.5rem", borderRadius: "4px", textAlign: "center" }}>
                    <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textTransform: "uppercase" }}>포탑 파괴</div>
                    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: "0.5rem", marginTop: "0.25rem" }}>
                      <button style={{ background: "transparent", border: "none", color: "var(--blue-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("blueTowersDestroyed", Math.max(0, features.blueTowersDestroyed - 1))}>-</button>
                      <span style={{ fontSize: "1rem", color: "var(--text-primary)" }}>{features.blueTowersDestroyed}</span>
                      <button style={{ background: "transparent", border: "none", color: "var(--blue-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("blueTowersDestroyed", Math.min(4, features.blueTowersDestroyed + 1))}>+</button>
                    </div>
                  </div>
                </div>

                {/* Blue Utility features */}
                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.5rem", marginTop: "1rem" }}>
                  <div className={highlightedFields.includes("blueWardsPlaced") ? "highlight-pulse" : ""}>
                    <label style={{ fontSize: "0.75rem", color: "var(--text-muted)" }}>와드 설치</label>
                    <input type="number" className="range-slider blue-slider" style={{ background: "rgba(255,255,255,0.05)", border: "1px solid var(--border-glass)", color: "white", padding: "0.25rem 0.5rem", borderRadius: "4px", width: "100%" }} value={features.blueWardsPlaced} onChange={(e) => handleFeatureChange("blueWardsPlaced", parseInt(e.target.value) || 0)} />
                  </div>
                  <div className={highlightedFields.includes("blueAvgLevel") ? "highlight-pulse" : ""}>
                    <label style={{ fontSize: "0.75rem", color: "var(--text-muted)" }}>평균 레벨</label>
                    <input type="number" step="0.1" className="range-slider blue-slider" style={{ background: "rgba(255,255,255,0.05)", border: "1px solid var(--border-glass)", color: "white", padding: "0.25rem 0.5rem", borderRadius: "4px", width: "100%" }} value={features.blueAvgLevel} onChange={(e) => handleFeatureChange("blueAvgLevel", parseFloat(e.target.value) || 0)} />
                  </div>
                </div>

              </div>

              {/* RED TEAM (RIGHT SIDE) */}
              <div>
                <h3 className="text-red" style={{ fontSize: "1.2rem", marginBottom: "1.5rem", display: "flex", alignItems: "center", gap: "0.5rem" }}>
                  <span style={{ display: "inline-block", width: "10px", height: "10px", borderRadius: "50%", backgroundColor: "var(--red-team)", boxShadow: "var(--shadow-red)" }}></span>
                  레드 진영 (Red Team)
                </h3>

                {/* Red Kills Slider */}
                <div className={highlightedFields.includes("redKills") ? "highlight-pulse" : ""} style={{ marginBottom: "1.2rem", padding: highlightedFields.includes("redKills") ? "0.5rem" : "0", transition: "all 0.3s ease" }}>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.9rem" }}>
                    <span>총 킬수 (Kills)</span>
                    <strong className="text-red">{features.redKills}</strong>
                  </div>
                  <input 
                    type="range" min="0" max="25" className="range-slider red-slider"
                    value={features.redKills} 
                    onChange={(e) => handleFeatureChange("redKills", parseInt(e.target.value))}
                  />
                </div>

                {/* Red Total Gold Slider */}
                <div className={highlightedFields.includes("redTotalGold") ? "highlight-pulse" : ""} style={{ marginBottom: "1.2rem", padding: highlightedFields.includes("redTotalGold") ? "0.5rem" : "0", transition: "all 0.3s ease" }}>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.9rem" }}>
                    <span>총 획득 골드 (Gold)</span>
                    <strong className="text-red">{features.redTotalGold.toLocaleString()}G</strong>
                  </div>
                  <input 
                    type="range" min="10000" max="25000" step="100" className="range-slider red-slider"
                    value={features.redTotalGold} 
                    onChange={(e) => handleFeatureChange("redTotalGold", parseInt(e.target.value))}
                  />
                </div>

                {/* Red CS Slider */}
                <div className={highlightedFields.includes("redTotalMinionsKilled") ? "highlight-pulse" : ""} style={{ marginBottom: "1.2rem", padding: highlightedFields.includes("redTotalMinionsKilled") ? "0.5rem" : "0", transition: "all 0.3s ease" }}>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.9rem" }}>
                    <span>미니언 처치수 (CS)</span>
                    <strong className="text-red">{features.redTotalMinionsKilled}</strong>
                  </div>
                  <input 
                    type="range" min="100" max="300" className="range-slider red-slider"
                    value={features.redTotalMinionsKilled} 
                    onChange={(e) => handleFeatureChange("redTotalMinionsKilled", parseInt(e.target.value))}
                  />
                </div>

                {/* Red Objective Counters */}
                <div className={`grid-cols-3 ${["redDragons", "redHeralds", "redTowersDestroyed"].some(f => highlightedFields.includes(f)) ? "highlight-pulse" : ""}`} style={{ display: "flex", gap: "1rem", marginTop: "1rem", padding: ["redDragons", "redHeralds", "redTowersDestroyed"].some(f => highlightedFields.includes(f)) ? "0.5rem" : "0", transition: "all 0.3s ease" }}>
                  <div style={{ background: "rgba(255,255,255,0.02)", padding: "0.5rem", borderRadius: "4px", textAlign: "center" }}>
                    <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textTransform: "uppercase" }}>드래곤</div>
                    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: "0.5rem", marginTop: "0.25rem" }}>
                      <button style={{ background: "transparent", border: "none", color: "var(--red-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("redDragons", Math.max(0, features.redDragons - 1))}>-</button>
                      <span style={{ fontSize: "1rem", color: "var(--text-primary)" }}>{features.redDragons}</span>
                      <button style={{ background: "transparent", border: "none", color: "var(--red-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("redDragons", Math.min(2, features.redDragons + 1))}>+</button>
                    </div>
                  </div>
                  
                  <div style={{ background: "rgba(255,255,255,0.02)", padding: "0.5rem", borderRadius: "4px", textAlign: "center" }}>
                    <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textTransform: "uppercase" }}>전령</div>
                    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: "0.5rem", marginTop: "0.25rem" }}>
                      <button style={{ background: "transparent", border: "none", color: "var(--red-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("redHeralds", Math.max(0, features.redHeralds - 1))}>-</button>
                      <span style={{ fontSize: "1rem", color: "var(--text-primary)" }}>{features.redHeralds}</span>
                      <button style={{ background: "transparent", border: "none", color: "var(--red-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("redHeralds", Math.min(1, features.redHeralds + 1))}>+</button>
                    </div>
                  </div>

                  <div style={{ background: "rgba(255,255,255,0.02)", padding: "0.5rem", borderRadius: "4px", textAlign: "center" }}>
                    <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textTransform: "uppercase" }}>포탑 파괴</div>
                    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: "0.5rem", marginTop: "0.25rem" }}>
                      <button style={{ background: "transparent", border: "none", color: "var(--red-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("redTowersDestroyed", Math.max(0, features.redTowersDestroyed - 1))}>-</button>
                      <span style={{ fontSize: "1rem", color: "var(--text-primary)" }}>{features.redTowersDestroyed}</span>
                      <button style={{ background: "transparent", border: "none", color: "var(--red-team)", cursor: "pointer", fontWeight: "bold" }} onClick={() => handleFeatureChange("redTowersDestroyed", Math.min(4, features.redTowersDestroyed + 1))}>+</button>
                    </div>
                  </div>
                </div>

                {/* Red Utility features */}
                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.5rem", marginTop: "1rem" }}>
                  <div className={highlightedFields.includes("redWardsPlaced") ? "highlight-pulse" : ""}>
                    <label style={{ fontSize: "0.75rem", color: "var(--text-muted)" }}>와드 설치</label>
                    <input type="number" className="range-slider red-slider" style={{ background: "rgba(255,255,255,0.05)", border: "1px solid var(--border-glass)", color: "white", padding: "0.25rem 0.5rem", borderRadius: "4px", width: "100%" }} value={features.redWardsPlaced} onChange={(e) => handleFeatureChange("redWardsPlaced", parseInt(e.target.value) || 0)} />
                  </div>
                  <div className={highlightedFields.includes("redAvgLevel") ? "highlight-pulse" : ""}>
                    <label style={{ fontSize: "0.75rem", color: "var(--text-muted)" }}>평균 레벨</label>
                    <input type="number" step="0.1" className="range-slider red-slider" style={{ background: "rgba(255,255,255,0.05)", border: "1px solid var(--border-glass)", color: "white", padding: "0.25rem 0.5rem", borderRadius: "4px", width: "100%" }} value={features.redAvgLevel} onChange={(e) => handleFeatureChange("redAvgLevel", parseFloat(e.target.value) || 0)} />
                  </div>
                </div>

              </div>

            </div>

            {/* FIRST BLOOD EXCLUSIVE TOGGLE */}
            <div className={highlightedFields.includes("blueFirstBlood") ? "highlight-pulse" : ""} style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: "2rem", marginTop: "2rem", borderTop: "1px solid rgba(255,255,255,0.05)", paddingTop: "1.5rem", padding: highlightedFields.includes("blueFirstBlood") ? "0.5rem" : "0", transition: "all 0.3s ease" }}>
              <span style={{ fontSize: "0.95rem" }}>퍼스트 블러드 진영:</span>
              <div style={{ display: "flex", gap: "1rem" }}>
                <button 
                  onClick={() => handleFeatureChange("blueFirstBlood", 1)}
                  style={{
                    padding: "0.5rem 1.5rem", border: "1px solid var(--blue-team)", borderRadius: "4px", cursor: "pointer", fontWeight: "bold",
                    background: features.blueFirstBlood === 1 ? "rgba(31,142,206,0.2)" : "transparent",
                    color: features.blueFirstBlood === 1 ? "var(--blue-glow)" : "var(--text-secondary)",
                    boxShadow: features.blueFirstBlood === 1 ? "var(--shadow-blue)" : "none",
                    transition: "all 0.2s ease"
                  }}
                >
                  블루팀 (Blue)
                </button>
                <button 
                  onClick={() => handleFeatureChange("blueFirstBlood", 0)}
                  style={{
                    padding: "0.5rem 1.5rem", border: "1px solid var(--red-team)", borderRadius: "4px", cursor: "pointer", fontWeight: "bold",
                    background: features.blueFirstBlood === 0 ? "rgba(232,64,87,0.2)" : "transparent",
                    color: features.blueFirstBlood === 0 ? "var(--red-glow)" : "var(--text-secondary)",
                    boxShadow: features.blueFirstBlood === 0 ? "var(--shadow-red)" : "none",
                    transition: "all 0.2s ease"
                  }}
                >
                  레드팀 (Red)
                </button>
              </div>
            </div>

          </div>
        </section>

        {/* RIGHT COLUMN: REAL-TIME OUTPUT & ANALYTICS */}
        <section style={{ display: "flex", flexDirection: "column", gap: "2rem" }}>
          
          {/* WINRATE PREDICTION RESULT */}
          <div className="card-hextech" style={{ padding: "2rem", border: prediction ? `1px solid ${prediction.prediction === 1 ? "rgba(31, 142, 206, 0.4)" : "rgba(232, 64, 87, 0.4)"}` : "1px solid var(--border-gold)" }}>
            <h2 style={{ fontSize: "1.4rem", marginBottom: "1.5rem", borderBottom: "1px solid var(--border-gold)", paddingBottom: "0.5rem" }}>
              📊 실시간 승률 예측 분석 (Outcome Analysis)
            </h2>

            {/* Model Selector Bar */}
            <div style={{ display: "flex", gap: "0.5rem", marginBottom: "1.5rem" }}>
              {["XGBoost", "Random Forest", "Logistic Regression"].map((modelName) => (
                <button
                  key={modelName}
                  onClick={() => {
                    setSelectedModel(modelName);
                    getPrediction(features, modelName);
                  }}
                  style={{
                    flex: 1, padding: "0.5rem", cursor: "pointer", borderRadius: "4px", fontSize: "0.85rem",
                    border: selectedModel === modelName ? "1px solid var(--gold-main)" : "1px solid var(--border-glass)",
                    background: selectedModel === modelName ? "linear-gradient(rgba(200,170,110,0.1), rgba(200,170,110,0.2))" : "rgba(255,255,255,0.02)",
                    color: selectedModel === modelName ? "var(--gold-bright)" : "var(--text-secondary)",
                    fontWeight: selectedModel === modelName ? "bold" : "normal",
                    transition: "all 0.2s ease"
                  }}
                >
                  {modelName}
                </button>
              ))}
            </div>

            <div style={{ position: "relative" }}>
              {isPredicting && (
                <div style={{ 
                  position: "absolute", top: 0, left: 0, right: 0, bottom: 0, 
                  background: "rgba(10, 12, 18, 0.4)", display: "flex", 
                  justifyContent: "center", alignItems: "center", zIndex: 10,
                  borderRadius: "8px", backdropFilter: "blur(2px)"
                }}>
                  <div style={{ width: "30px", height: "30px", border: "3px solid var(--gold-dark)", borderTop: "3px solid var(--gold-main)", borderRadius: "50%", animation: "spin 1s linear infinite" }}></div>
                </div>
              )}

              {prediction ? (
                <div style={{ display: "flex", flexDirection: "column", gap: "1.5rem", opacity: isPredicting ? 0.5 : 1, transition: "opacity 0.2s ease" }}>
                  
                  {/* Spectral Winrate Bar */}
                  <div>
                    <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "0.5rem" }}>
                      <span className="text-blue" style={{ fontWeight: "bold" }}>BLUE {toPercent(prediction.blue_win_probability)}</span>
                      <span className="text-red" style={{ fontWeight: "bold" }}>RED {toPercent(prediction.red_win_probability)}</span>
                    </div>
                    <div style={{ height: "30px", width: "100%", borderRadius: "15px", display: "flex", overflow: "hidden", border: "1px solid rgba(255,255,255,0.1)", boxShadow: "0 0 15px rgba(0,0,0,0.4)" }}>
                      <div style={{ width: toPercent(prediction.blue_win_probability), background: "linear-gradient(90deg, #103c61, var(--blue-team))", transition: "width 0.4s ease" }}></div>
                      <div style={{ width: toPercent(prediction.red_win_probability), background: "linear-gradient(90deg, var(--red-team), #631422)", transition: "width 0.4s ease" }}></div>
                    </div>
                  </div>

                  {/* Verdict Box */}
                  <div style={{
                    background: prediction.prediction === 1 ? "rgba(31,142,206,0.06)" : "rgba(232,64,87,0.06)",
                    border: `1px solid ${prediction.prediction === 1 ? "rgba(31,142,206,0.2)" : "rgba(232,64,87,0.2)"}`,
                    borderRadius: "8px", padding: "1.5rem", textAlign: "center"
                  }}>
                    <div style={{ color: "var(--text-secondary)", fontSize: "0.9rem", textTransform: "uppercase" }}>예상 유력 승리팀 (Verdict)</div>
                    <h3 style={{
                      fontSize: "2rem", marginTop: "0.5rem",
                      color: prediction.prediction === 1 ? "var(--blue-glow)" : "var(--red-glow)",
                      textShadow: prediction.prediction === 1 ? "var(--shadow-blue)" : "var(--shadow-red)"
                    }}>
                      {prediction.winner === "Blue" ? "블루팀 승리 유력" : "레드팀 승리 유력"}
                    </h3>
                    <p style={{ marginTop: "0.5rem", fontSize: "0.9rem", color: "var(--text-muted)" }}>
                      현재 입력된 {selectedModel}의 10분 지표를 바탕으로 블루팀의 예상 승률은 <strong>{toPercent(prediction.blue_win_probability)}</strong> 입니다.
                    </p>
                  </div>

                  {/* Score differences */}
                  <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem" }} className="grid-cols-2">
                    <div style={{ background: "rgba(255,255,255,0.02)", padding: "1rem", borderRadius: "6px", border: "1px solid var(--border-glass)" }}>
                      <div style={{ fontSize: "0.8rem", color: "var(--text-muted)" }}>골드 차이 (Gold Diff)</div>
                      <div style={{ fontSize: "1.2rem", fontWeight: "bold", marginTop: "0.25rem", color: features.blueTotalGold - features.redTotalGold >= 0 ? "var(--blue-team)" : "var(--red-team)" }}>
                        {features.blueTotalGold - features.redTotalGold >= 0 ? "+" : ""}{(features.blueTotalGold - features.redTotalGold).toLocaleString()}G
                      </div>
                    </div>
                    <div style={{ background: "rgba(255,255,255,0.02)", padding: "1rem", borderRadius: "6px", border: "1px solid var(--border-glass)" }}>
                      <div style={{ fontSize: "0.8rem", color: "var(--text-muted)" }}>경험치 차이 (EXP Diff)</div>
                      <div style={{ fontSize: "1.2rem", fontWeight: "bold", marginTop: "0.25rem", color: features.blueTotalExperience - features.redTotalExperience >= 0 ? "var(--blue-team)" : "var(--red-team)" }}>
                        {features.blueTotalExperience - features.redTotalExperience >= 0 ? "+" : ""}{(features.blueTotalExperience - features.redTotalExperience).toLocaleString()}
                      </div>
                    </div>
                  </div>

                </div>
              ) : predictionError ? (
                <div style={{ color: "var(--red-team)", padding: "1rem", textAlign: "center", background: "rgba(232,64,87,0.1)", borderRadius: "6px", border: "1px solid rgba(232,64,87,0.3)" }}>
                  {predictionError}
                </div>
              ) : (
                <div style={{ textAlign: "center", padding: "2rem", color: "var(--text-muted)" }}>
                  데이터 분석을 대기 중입니다...
                </div>
              )}
            </div>
          </div>

          {/* MODEL METRICS CARD & COMPARISON */}
          <div className="card-hextech" style={{ padding: "2rem" }}>
            <h2 style={{ fontSize: "1.4rem", marginBottom: "1.5rem", borderBottom: "1px solid var(--border-gold)", paddingBottom: "0.5rem", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <span>🏆 MODEL METRICS & BENCHMARKS</span>
              <button 
                onClick={handleRetrain} 
                disabled={isTraining}
                className="btn-hextech" 
                style={{ padding: "0.35rem 0.75rem", fontSize: "0.75rem", border: "1px solid var(--gold-main)" }}
              >
                {isTraining ? "재학습 중..." : "모델 재학습"}
              </button>
            </h2>

            {loadingMetrics ? (
              <div style={{ textAlign: "center", padding: "2rem" }}>
                <p style={{ color: "var(--gold-main)" }}>학습 평가지표 로드 중...</p>
              </div>
            ) : metricsError ? (
              <div style={{ color: "var(--red-team)", fontSize: "0.9rem" }}>{metricsError}</div>
            ) : metrics ? (
              <div style={{ display: "flex", flexDirection: "column", gap: "1.5rem" }}>
                
                {Object.entries(metrics).map(([modelName, m]) => (
                  <div key={modelName} style={{ background: "rgba(255,255,255,0.02)", padding: "1rem", borderRadius: "6px", border: selectedModel === modelName ? "1px solid var(--gold-main)" : "1px solid var(--border-glass)" }}>
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "0.5rem" }}>
                      <span style={{ fontWeight: "bold", color: "var(--text-primary)" }}>{modelName}</span>
                      <span style={{ fontSize: "0.8rem", background: "var(--bg-light)", padding: "0.2rem 0.5rem", borderRadius: "3px", color: "var(--gold-main)" }}>
                        AUC: {(m["ROC-AUC"] * 100).toFixed(1)}%
                      </span>
                    </div>

                    {/* Progress bars for accuracy and F1 score */}
                    <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
                      <div>
                        <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.8rem", color: "var(--text-secondary)" }}>
                          <span>정확도 (Accuracy)</span>
                          <strong>{(m.Accuracy * 100).toFixed(1)}%</strong>
                        </div>
                        <div className="progress-container">
                          <div className="progress-bar progress-gold" style={{ width: `${m.Accuracy * 100}%` }}></div>
                        </div>
                      </div>

                      <div>
                        <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.8rem", color: "var(--text-secondary)" }}>
                          <span>F1 Score</span>
                          <strong>{(m["F1-Score"] * 100).toFixed(1)}%</strong>
                        </div>
                        <div className="progress-container">
                          <div className="progress-bar progress-gold" style={{ width: `${m["F1-Score"] * 100}%` }}></div>
                        </div>
                      </div>
                    </div>
                  </div>
                ))}

              </div>
            ) : null}
          </div>

        </section>

      </main>

      {/* FOOTER & INFO */}
      <footer style={{ marginTop: "5rem", textAlign: "center", borderTop: "1px solid rgba(255,255,255,0.05)", paddingTop: "2rem", color: "var(--text-muted)", fontSize: "0.85rem" }}>
        <p>리그 오브 레전드 다이아몬드 이상 랭크 게임의 극초반 10분 경기 데이터 약 10,000건을 기계학습시켜 설계된 인공지능 예측 시스템입니다.</p>
        <p style={{ marginTop: "0.5rem" }}>&copy; 2026 Giheon-Jeon. Powered by Next.js, FastAPI & Machine Learning.</p>
      </footer>
    </div>
  );
}
