import lrModel from '../../models/logistic_regression.json';
import rfModel from '../../models/random_forest.json';
import scaler from '../../models/scaler.json';
import featureOrder from '../../models/feature_names.json';
import mlWinRates from '../../models/champion_ml_win_rates.json';
import { score as xgbScore } from '../../models/xgboost_code.js';
import { buildLaneFeatures, getChampionTags, determineComposition } from './lolEngine.js';

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
