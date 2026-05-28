import os
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import joblib

# XGBoost 로드 시도
try:
    from xgboost import XGBClassifier
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

def preprocess_data(data_path, models_dir):
    """
    데이터 로드, 챔피언 멀티핫 인코딩 및 원핫 인코딩 전처리 수행
    """
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"데이터셋을 찾을 수 없습니다: {data_path}")
            
    df = pd.read_csv(data_path)
    
    # 1. 불필요 컬럼 제거 (매치 ID)
    if 'match_id' in df.columns:
        df = df.drop(columns=['match_id'])
    
    # 2. 블루/레드 챔피언 멀티핫 피처 생성
    blue_champion_cols = ['blue_top_champion', 'blue_jungle_champion', 'blue_middle_champion', 'blue_bottom_champion', 'blue_utility_champion']
    red_champion_cols = ['red_top_champion', 'red_jungle_champion', 'red_middle_champion', 'red_bottom_champion', 'red_utility_champion']
    
    all_champions = set()
    for col in blue_champion_cols + red_champion_cols:
        if col in df.columns:
            all_champions.update(df[col].dropna().unique())
    all_champions = sorted(list(all_champions))
    
    # 성능 최적화를 위해 각 행의 챔피언들을 set으로 사전 변환
    blue_champs_sets = df[blue_champion_cols].apply(lambda row: set(row.dropna().values), axis=1)
    red_champs_sets = df[red_champion_cols].apply(lambda row: set(row.dropna().values), axis=1)
    
    # DataFrame 파편화(PerformanceWarning) 방지를 위해 딕셔너리로 피처를 취합 후 일괄 concat
    champ_features = {}
    for champ in all_champions:
        champ_features[f'blue_champion_{champ}'] = blue_champs_sets.apply(lambda s: 1.0 if champ in s else 0.0)
        champ_features[f'red_champion_{champ}'] = red_champs_sets.apply(lambda s: 1.0 if champ in s else 0.0)
    
    champ_df = pd.DataFrame(champ_features, index=df.index)
    df = pd.concat([df, champ_df], axis=1)
    
    # 원본 챔피언명 컬럼들 제거
    existing_champion_cols = [c for c in blue_champion_cols + red_champion_cols if c in df.columns]
    df = df.drop(columns=existing_champion_cols)
    
    # 3. 문자열 컬럼 (태그, 조합 등) 원핫 인코딩
    categorical_cols = [c for c in df.columns if 'tag' in c or 'comp' in c]
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    # 4. 타겟 변수 분리
    if 'win' not in df.columns:
        raise ValueError("데이터셋에 'win' 컬럼이 없습니다.")
        
    X = df.drop(columns=['win']).astype(float)
    y = df['win']
    
    feature_names = list(X.columns)
    
    # 피처 이름 저장 (추후 백엔드 API에서 입력 맵핑 시 사용)
    with open(os.path.join(models_dir, "feature_names.json"), "w", encoding="utf-8") as f:
        json.dump(feature_names, f, indent=4, ensure_ascii=False)
    print(f"총 {len(feature_names)}개의 피처 이름이 저장되었습니다.")
    
    return X, y, feature_names, all_champions

def train_logistic_regression(X_tr_scaled, X_te_scaled, y_tr, y_te, feature_names, scaler, models_dir):
    """
    Logistic Regression 모델 학습 및 평가지표 계산
    """
    print("Logistic Regression 모델 학습 중...")
    lr_model = LogisticRegression(max_iter=2000, random_state=42)
    lr_model.fit(X_tr_scaled, y_tr)
    
    y_pred = lr_model.predict(X_te_scaled)
    y_pred_proba = lr_model.predict_proba(X_te_scaled)[:, 1]
    
    lr_coefs = lr_model.coef_[0]
    coefficients_dict = dict(zip(feature_names, lr_coefs.tolist()))
    
    # 비표준화(Unscaled) 계수 계산: w_i = beta_i / sigma_i
    unscaled_coeffs = {
        col: float(beta / sigma) if sigma != 0 else 0.0
        for col, beta, sigma in zip(feature_names, lr_coefs, scaler.scale_)
    }
    
    tn, fp, fn, tp = confusion_matrix(y_te, y_pred).ravel()
    
    metrics = {
        "Accuracy": float(accuracy_score(y_te, y_pred)),
        "Precision": float(precision_score(y_te, y_pred)),
        "Recall": float(recall_score(y_te, y_pred)),
        "F1-Score": float(f1_score(y_te, y_pred)),
        "ROC-AUC": float(roc_auc_score(y_te, y_pred_proba)),
        "Confusion_Matrix": {"TN": int(tn), "FP": int(fp), "FN": int(fn), "TP": int(tp)},
        "Coefficients": coefficients_dict,
        "Unscaled_Coefficients": unscaled_coeffs,
        "Dragon_Gold_Value": 1500.0
    }
    
    joblib.dump(lr_model, os.path.join(models_dir, "logistic_regression.joblib"))
    print(f"[Logistic Regression] 정확도: {metrics['Accuracy']:.4f}")
    return lr_model, metrics

def train_random_forest(X_tr, X_te, y_tr, y_te, feature_names, models_dir):
    """
    Random Forest 모델 학습 및 평가지표 계산
    """
    print("Random Forest 모델 학습 중...")
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    rf_model.fit(X_tr, y_tr)
    
    y_pred = rf_model.predict(X_te)
    y_pred_proba = rf_model.predict_proba(X_te)[:, 1]
    
    rf_importances = rf_model.feature_importances_
    rf_importances_dict = dict(zip(feature_names, rf_importances.tolist()))
    
    tn, fp, fn, tp = confusion_matrix(y_te, y_pred).ravel()
    
    metrics = {
        "Accuracy": float(accuracy_score(y_te, y_pred)),
        "Precision": float(precision_score(y_te, y_pred)),
        "Recall": float(recall_score(y_te, y_pred)),
        "F1-Score": float(f1_score(y_te, y_pred)),
        "ROC-AUC": float(roc_auc_score(y_te, y_pred_proba)),
        "Confusion_Matrix": {"TN": int(tn), "FP": int(fp), "FN": int(fn), "TP": int(tp)},
        "Feature_Importances": rf_importances_dict
    }
    
    joblib.dump(rf_model, os.path.join(models_dir, "random_forest.joblib"))
    print(f"[Random Forest] 정확도: {metrics['Accuracy']:.4f}")
    return rf_model, metrics

def train_xgboost(X_tr, X_te, y_tr, y_te, feature_names, models_dir):
    """
    XGBoost 모델 학습, GridSearchCV 튜닝 및 평가지표 계산
    """
    if not HAS_XGBOOST:
        print("XGBoost가 설치되어 있지 않아 학습을 건너뜁니다.")
        return None, None
        
    print("XGBoost 모델 학습 및 튜닝 중...")
    xgb_base = XGBClassifier(random_state=42, eval_metric="logloss")
    xgb_param_grid = {
        'n_estimators': [50, 100],
        'max_depth': [3, 5],
        'learning_rate': [0.05, 0.1]
    }
    xgb_grid = GridSearchCV(xgb_base, xgb_param_grid, cv=3, scoring='accuracy', n_jobs=-1)
    xgb_grid.fit(X_tr, y_tr)
    
    xgb_model = xgb_grid.best_estimator_
    best_params = xgb_grid.best_params_
    print(f"XGBoost 최적 파라미터: {best_params}")
    
    y_pred = xgb_model.predict(X_te)
    y_pred_proba = xgb_model.predict_proba(X_te)[:, 1]
    
    xgb_importances = xgb_model.feature_importances_
    xgb_importances_dict = dict(zip(feature_names, xgb_importances.tolist()))
    
    tn, fp, fn, tp = confusion_matrix(y_te, y_pred).ravel()
    
    metrics = {
        "Accuracy": float(accuracy_score(y_te, y_pred)),
        "Precision": float(precision_score(y_te, y_pred)),
        "Recall": float(recall_score(y_te, y_pred)),
        "F1-Score": float(f1_score(y_te, y_pred)),
        "ROC-AUC": float(roc_auc_score(y_te, y_pred_proba)),
        "Confusion_Matrix": {"TN": int(tn), "FP": int(fp), "FN": int(fn), "TP": int(tp)},
        "Feature_Importances": xgb_importances_dict,
        "Best_Params": best_params
    }
    
    joblib.dump(xgb_model, os.path.join(models_dir, "xgboost.joblib"))
    print(f"[XGBoost] 정확도: {metrics['Accuracy']:.4f}")
    return xgb_model, metrics

def compile_models_with_m2cgen(lr_model, rf_model, xgb_model, scaler, models_dir):
    """
    m2cgen을 사용하여 무의존성 순수 파이썬 추론 코드로 각 모델 컴파일
    """
    try:
        import m2cgen as m2c
        print("m2cgen으로 순수 파이썬 모델 코드 컴파일 중...")
        
        # 1. Logistic Regression 컴파일
        lr_code = m2c.export_to_python(lr_model)
        with open(os.path.join(models_dir, "logistic_regression_code.py"), "w", encoding="utf-8") as f:
            f.write(lr_code)
            
        # 2. Random Forest 컴파일
        rf_code = m2c.export_to_python(rf_model)
        with open(os.path.join(models_dir, "random_forest_code.py"), "w", encoding="utf-8") as f:
            f.write(rf_code)
            
        # 3. XGBoost 컴파일
        if HAS_XGBOOST and xgb_model is not None:
            xgb_model.base_score = 0.5
            xgb_code = m2c.export_to_python(xgb_model)
            with open(os.path.join(models_dir, "xgboost_code.py"), "w", encoding="utf-8") as f:
                f.write(xgb_code)
                
        # 4. 스케일러 파라미터 JSON 백업
        scaler_data = {
            "mean": scaler.mean_.tolist(),
            "scale": scaler.scale_.tolist()
        }
        with open(os.path.join(models_dir, "scaler.json"), "w", encoding="utf-8") as f:
            json.dump(scaler_data, f, indent=4)
            
        print("m2cgen 모델 컴파일 성공!")
    except Exception as e:
        print(f"m2cgen 컴파일 에러: {str(e)}")

def calculate_champ_ml_win_rates(lr_model, rf_model, xgb_model, scaler, feature_names, all_champions, models_dir):
    """
    모든 피처가 0인 가상 중립 상태에서 특정 챔피언 기여도(멀티핫=1.0)를 주었을 때의 블루팀 승률을 추출하여 저장
    """
    print("3대 알고리즘별 챔피언 기본 승률 예측 및 추출 중...")
    champ_win_rates = {
        "Logistic Regression": {},
        "Random Forest": {},
        "XGBoost": {}
    }
    
    # 모든 피처가 0.0인 1행짜리 기본 DataFrame 생성
    neutral_row = pd.DataFrame(0.0, index=[0], columns=feature_names)
    
    for champ in all_champions:
        # 블루팀에 해당 챔피언 투입
        champ_row = neutral_row.copy()
        blue_champ_col = f'blue_champion_{champ}'
        if blue_champ_col in champ_row.columns:
            champ_row[blue_champ_col] = 1.0
            
        # 1. Logistic Regression 예측
        champ_row_scaled = scaler.transform(champ_row)
        lr_prob = lr_model.predict_proba(champ_row_scaled)[0][1]
        champ_win_rates["Logistic Regression"][champ] = float(lr_prob)
        
        # 2. Random Forest 예측
        rf_prob = rf_model.predict_proba(champ_row)[0][1]
        champ_win_rates["Random Forest"][champ] = float(rf_prob)
        
        # 3. XGBoost 예측
        if HAS_XGBOOST and xgb_model is not None:
            xgb_prob = xgb_model.predict_proba(champ_row)[0][1]
            champ_win_rates["XGBoost"][champ] = float(xgb_prob)
        else:
            champ_win_rates["XGBoost"][champ] = float(rf_prob)
            
    # 결과를 JSON 파일로 저장
    win_rates_path = os.path.join(models_dir, "champion_ml_win_rates.json")
    with open(win_rates_path, "w", encoding="utf-8") as f:
        json.dump(champ_win_rates, f, indent=4, ensure_ascii=False)
    print(f"머신러닝 기반 챔피언 동적 승률이 저장되었습니다: {win_rates_path}")

def train_and_evaluate():
    print("머신러닝 모델 학습을 시작합니다...")
    
    # 1. 데이터 로드 및 전처리
    data_path = os.path.join(os.path.dirname(__file__), "lol_clean_final.csv")
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(models_dir, exist_ok=True)
    
    X, y, feature_names, all_champions = preprocess_data(data_path, models_dir)
    
    # 학습/테스트 데이터 분할 (80:20 비율, 클래스 비율 유지)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # 피처 스케일러 학습 및 백업
    scaler = StandardScaler()
    X_tr_scaled = scaler.fit_transform(X_tr)
    X_te_scaled = scaler.transform(X_te)
    joblib.dump(scaler, os.path.join(models_dir, "scaler.joblib"))
    print("StandardScaler 학습 및 저장 완료.")
    
    metrics_report = {}
    
    # 2단계. Logistic Regression 학습
    lr_model, lr_metrics = train_logistic_regression(
        X_tr_scaled, X_te_scaled, y_tr, y_te, feature_names, scaler, models_dir
    )
    metrics_report["Logistic Regression"] = lr_metrics
    
    # 3단계. Random Forest 학습
    rf_model, rf_metrics = train_random_forest(
        X_tr, X_te, y_tr, y_te, feature_names, models_dir
    )
    metrics_report["Random Forest"] = rf_metrics
    
    # 4단계. XGBoost 학습 및 튜닝
    xgb_model, xgb_metrics = train_xgboost(
        X_tr, X_te, y_tr, y_te, feature_names, models_dir
    )
    if xgb_metrics is not None:
        metrics_report["XGBoost"] = xgb_metrics
        
    # m2cgen 컴파일 및 스케일러 JSON 저장
    compile_models_with_m2cgen(lr_model, rf_model, xgb_model, scaler, models_dir)
    
    # 5단계. 챔피언 기여도 기반 동적 승률 계산
    calculate_champ_ml_win_rates(lr_model, rf_model, xgb_model, scaler, feature_names, all_champions, models_dir)
    
    # 모델 성능 지표 리포트 저장
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_report, f, indent=4, ensure_ascii=False)
    print(f"모델 지표가 저장되었습니다: {metrics_path}")
        
    return metrics_report

if __name__ == "__main__":
    train_and_evaluate()
