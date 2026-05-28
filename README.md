# 💎 LoL Early WinRate Predictor (10m)
## 리그 오브 레전드 다이아몬드+ 랭크 10분 지표 기반 실시간 승률 예측 솔루션

<p align="center">
  <img width="170" height="170" alt="project_logo" src="https://raw.githubusercontent.com/Giheon-Jeon/LoL-WinRate-10m/main/static/hextech_logo.png" />
</p>

<p align="center">
  <strong>HEXTECH Predictive Engine Team</strong><br>
  Advanced Analytics for Competitive LoL Play
</p>

---

## 📌 목차
<details>
  <summary>클릭하여 목차 열기/닫기</summary>
  
  - [✨ 주요 기능](#-주요-기능)
  - [🤖 머신러닝 파이프라인 구성 요약](#-머신러닝-파이프라인-구성-요약)
  - [🛠 기술 스택 및 선정 이유](#-기술-스택-및-선정-이유)
  - [🏗 아키텍처 및 폴더 구조 (상세)](#-아키텍처-및-폴더-구조-상세)
  - [🤝 협업 및 자동화 규칙](#-협업-및-자동화-규칙)
  - [📈 데이터 전처리 및 모델 학습 파이프라인](#-데이터-전처리-및-모델-학습-파이프라인)
</details>

---

## ✨ 주요 기능
<details open>
  <summary><b>1. Hextech UI/UX 대시보드</b></summary>
  리그 오브 레전드의 마법공학 테마를 살린 프리미엄 웹 인터페이스입니다. 실시간 인터랙티브 모델 분석 대시보드를 제공하며 매끄러운 사용자 경험을 선사합니다.
</details>
<details open>
  <summary><b>2. 3단계 머신러닝 다변화 엔진</b></summary>
  베이스라인(로지스틱 회귀), 비교(랜덤 포레스트), 최적화(XGBoost GridSearch) 모델들을 활용해 정밀한 성능 검증 체계를 운영합니다.
</details>
<details open>
  <summary><b>3. 데이터 기반 인사이트: 드래곤 골드 가치 환산</b></summary>
  로지스틱 회귀 모델의 비표준화 계수 비율을 분석해 드래곤 1마리의 골드 가치 환산 등 실용적이고 직관적인 전략 지표를 도출합니다.
</details>
<details open>
  <summary><b>4. 인터랙티브 시각화 차트</b></summary>
  Chart.js를 활용하여 각 모델의 <b>혼동 행렬(Confusion Matrix) TP/TN/FP/FN</b>, 모델별 중요 피처 분포 및 양수/음수 계수 그래프를 다이내믹하게 렌더링합니다.
</details>
<details open>
  <summary><b>5. Gemini 비전 스캔 연동</b></summary>
  Google Gemini 2.0 Flash AI 비전 인식 기능을 활용하여 인게임 스코어보드 스크린샷에서 10분 지표를 자동 추출하고 입력 폼에 즉시 매핑합니다.
</details>

---

## 🤖 머신러닝 파이프라인 구성 요약

프로젝트의 예측 정확도 향상과 수학적 해석 가능성을 동시에 달성하기 위해 3단계 모델 구조를 운용합니다.

| 구분 | 모델 | 역할 | 주요 분석 요소 | 주요 성능 지표 (Test ACC) |
| :--- | :--- | :--- | :--- | :--- |
| **베이스라인** | **Logistic Regression** | 성능 기준점 + 피처별 계수 해석 | 드래곤 가치를 골드로 직접 환산 | **79.2%** |
| **비교** | **Random Forest** | 중간 비교 기준 (의사결정 앙상블) | 비선형 관계 학습 및 중요도 비교 대조 | **78.2%** |
| **최적화** | **XGBoost** | 최고 성능 달성 (GridSearchCV 최적 튜닝) | 부스팅 피처 기여도 분석 및 최강 성능 입증 | **77.8%** |

---

## 🛠 기술 스택 및 선정 이유

### Frontend / Backend
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
</p>

* **Python**: 강력한 데이터 분석 및 머신러닝 생태계를 활용할 수 있는 핵심 언어
* **Flask**: API 서빙 및 정적 템플릿 렌더링에 적합한 가볍고 유연한 마이크로 프레임워크
* **NumPy**: 입력 데이터의 실시간 변형, 배열 관리 및 백엔드 고성능 행렬 연산 처리

### ML 및 시각화
<p>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/XGBoost-111111?style=for-the-badge&logo=xgboost&logoColor=white" />
  <img src="https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white" />
</p>

* **Scikit-learn**: 데이터 표준화(StandardScaler), 로지스틱 회귀, 랜덤 포레스트 및 GridSearchCV 기반 하이퍼파라미터 튜닝 지원
* **XGBoost**: 뛰어난 정형 데이터 예측력을 제공하는 부스팅 알고리즘으로 프로젝트 최고 성능 달성
* **Chart.js**: 브라우저상에서 계수 분포, 중요도 순위, 혼동 행렬 등을 애니메이션과 함께 렌더링하는 경량 시각화 도구
* **Google Gemini (2.0 Flash)**: 멀티모달 비전 인식을 통해 복잡한 게임 스크린샷 수치를 JSON 포맷으로 자동 변환

---

## 🛠️ 실행 방법

### 1. 가상환경 설정 및 패키지 설치
(이미 `.venv` 폴더가 존재한다면 이 단계를 건너뛰어도 됩니다)
```bash
py -m venv .venv
./.venv/Scripts/pip install flask flask-cors pandas joblib scikit-learn pillow google-generativeai xgboost
```

### 2. 서버 실행
```bash
./.venv/Scripts/python app.py
```

### 3. 접속
브라우저에서 다음 주소로 접속합니다:
> **http://localhost:5000**

---

## 🏗 아키텍처 및 폴더 구조 (상세)

각 폴더와 파일의 역할(설명)을 토글로 구성하여 한눈에 파악할 수 있도록 작성되었습니다.

<details>
  <summary>📂 <b>전체 디렉터리 트리 보기</b></summary>

```text
.
├── 📁 backend/                 # 챔피언 및 조합 데이터 처리 관련 디렉터리
│   ├── 📄 __init__.py
│   └── 📄 champion_data.py     # 챔피언 태그 정보, 조합 점수 계산 및 시너지 정의
├── 📁 models/                  # 학습 완료된 모델 파라미터(가중치) 및 메타 데이터 저장소 (Git 제외)
│   ├── 📄 feature_names.json   # 예측 시 사용되는 피처의 순서 정보 보장용
│   ├── 📄 scaler.json          # 스케일링 평균/분산 정보의 JSON 버전 백업
│   ├── 📄 metrics.json         # 각 모델의 성능 평가지표 (Accuracy, F1, ROC-AUC, CM 등) 기록
│   ├── 📄 logistic_regression_code.py # m2cgen 컴파일된 순수 파이썬 모델 (Logistic Regression)
│   ├── 📄 random_forest_code.py # m2cgen 컴파일된 순수 파이썬 모델 (Random Forest)
│   └── 📄 xgboost_code.py      # m2cgen 컴파일된 순수 파이썬 모델 (XGBoost)
├── 📁 templates/               # 프론트엔드 HTML 렌더링용 뷰(View) 템플릿
│   └── 📄 index.html           # 대시보드 UI를 구성하는 마법공학 테마 SPA (Single Page Application)
├── 📄 .gitignore               # Git 버전 관리에서 제외할 파일 및 폴더
├── 📄 LICENSE                  # 프로젝트 라이선스 공시
├── 📄 README.md                # 전체 프로젝트 소개 및 가이드 문서 (본 문서)
├── 📄 app.py                   # Flask 메인 애플리케이션 (라우팅, API 서빙, 모델 추론 통합)
├── 📄 lol_clean_final.csv      # 모델 학습 원천 데이터셋 (10분 구간 라인별 상세 데이터)
├── 📄 requirements.txt         # 파이썬 패키지 의존성 목록 명세서
└── 📄 train.py                 # 전처리 및 모델 학습 파이프라인의 메인 실행 스크립트
```
</details>

### 주요 파일 역할 세부 설명

* **`app.py`**: 서버의 심장부로 클라이언트와의 HTTP 통신을 담당합니다. `/api/predict` 등의 엔드포인트를 열어 전처리, 스케일링, 모델 추론 결과를 응답으로 반환합니다.
* **`train.py`**: 데이터셋의 챔피언 이름 등 예측 가치가 불명확하고 과적합을 일으키는 피처를 제거하고, 스케일링 및 하이퍼파라미터 튜닝을 거쳐 최종 코드 컴파일 모델을 생성합니다.
* **`templates/index.html`**: UI/UX 디자인이 집약된 클라이언트 파일입니다. 차트 렌더링(Chart.js), 비동기 페칭, 스크린샷 업로드 파싱 등 모든 브라우저 상호작용이 여기서 이루어집니다.

---

## 🤝 협업 및 자동화 규칙

* **Git Flow 전략**: `main` 브랜치를 기준으로 프로덕션 배포를 관리하며 기능 단위 패치 및 핫픽스 처리
* **Commit Convention**: 협업 커밋 시 이모지 컨벤션(`✨ Feat`, `🐛 Fix`, `⚡️ Perf`, `♻️ Refactor`)을 준수하여 가독성 강화
* **Model Code Compilation**: 무의존성 순수 파이썬 추론 엔진 적용을 위해 m2cgen 라이브러리를 활용하여 컴파일된 `*_code.py` 모델 가중치를 사용합니다.

---

## 📈 데이터 전처리 및 모델 학습 파이프라인

정교한 분석과 신뢰도 높은 평가를 위해 `train.py` 파이프라인에 최신 머신러닝 베스트 프랙티스를 적용했습니다.

```mermaid
graph TD
    A[lol_clean_final.csv] --> B[불필요 match_id 컬럼 제거]
    B --> C[피처 공간 최소화를 위해 champion 컬럼 제거]
    C --> D[tag 및 comp 컬럼 pd.get_dummies 원핫 인코딩 적용]
    D --> E[학습 및 테스트 데이터 분할 80:20 / stratify=y]
    
    E --> F{피처 스케일링 분기}
    
    F -- 로지스틱 회귀 전용 --> G[StandardScaler 표준화 적용]
    G --> H[Logistic Regression 학습]
    H --> I[계수 Coefficient 추출 및 스케일링 JSON 백업]
    
    F -- 트리 기반 모델 --> J[원본 비스케일링 데이터 활용]
    J --> K[Random Forest 학습]
    J --> L[XGBoost GridSearchCV 최적 파라미터 학습]
    
    K --> M[모델 평가 및 Confusion Matrix 저장]
    L --> M
    I --> M
    
    M --> N[models/metrics.json 저장 & m2cgen 컴파일 코드 생성]
```

<details open>
  <summary><b>🔥 데이터 전처리 핵심 포인트</b></summary>
  
  1. **챔피언 피처 제거 및 태그/시너지 활용**: 챔피언 이름 피처는 카디널리티가 너무 높아 과적합(Overfitting)을 일으키고 피처 차원을 극도로 비대하게 만드므로 이를 제외하고, 포지션별 챔피언 태그(`Fighter`, `Mage`, `Tank` 등)와 팀 시너지(`comp`)만 원핫 인코딩하여 최적의 예측 성능과 해석 가능성을 유지합니다.
  2. **스케일링 정밀 분기**: 경사하강법 기반이자 계수 해석이 중요한 로지스틱 회귀에는 표준화(`StandardScaler`)를 적용하여 정밀 계수를 유도한 반면, 변수 분할 기준을 따르는 트리 기반 모델(RF, XGBoost)은 정보 왜곡을 막기 위해 원래의 비스케일링 원본 데이터를 공급하여 학습 정확도를 극대화했습니다.
</details>
