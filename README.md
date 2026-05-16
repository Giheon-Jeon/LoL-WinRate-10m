# 💎 LoL Early WinRate Predictor (10m) - Hextech Edition

League of Legends Diamond+ 랭크 게임의 10분 지표를 분석하여 실시간 승률을 예측하는 프리미엄 머신러닝 솔루션입니다. 

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel">
</div>

## 🚀 주요 특징
- **Hextech UI/UX**: 리그 오브 레전드 고유의 마법공학 미학을 적용한 고품질 웹 인터페이스
- **초경량 Vercel 배포**: `m2cgen`을 통한 모델 코드화로 Scikit-learn 의존성 없이 500MB 미만 배포 실현
- **실시간 예측 엔진**: 수치 변경 시 지연 없는 즉각적인 승률 업데이트 (MoE Ensemble, RF, LR 지원)
- **AI 성능 대시보드**: 각 모델의 Accuracy, F1-Score 등 정밀 지표 실시간 확인 가능
- **인공지능 스코어보드 스캔**: Gemini Vision AI를 연동하여 스크린샷 한 장으로 인게임 지표 자동 추출

## 📂 프로젝트 구조

.
├── 📁 models/               # 학습된 모델 파이썬 코드 및 스케일러 (Colab 추출물)
│   ├── logistic_regression_code.py  # 순수 파이썬으로 변환된 로직
│   ├── random_forest_code.py       # 순수 파이썬으로 변환된 로직
│   ├── moe_expert_*.py             # MoE 앙상블 전문가 모델들
│   ├── scaler.json                 # 데이터 정규화 파라미터 (Mean, Scale)
│   └── metrics.json                # 모델 성능 지표 데이터
├── 📁 templates/            # Hextech UI HTML 템플릿
│   └── index.html           # 단일 페이지 애플리케이션 (SPA)
├── 📄 app.py                # Flask 서버, API 핸들러 및 모델 서빙 로직
├── 📄 train.py              # 로컬 백업용 학습 스크립트 (m2cgen 포함)
├── 📄 requirements.txt      # Vercel 배포용 최소 의존성 (scikit-learn 제외)
├── 📄 .vercelignore         # Vercel 배포 최적화 설정
├── 📄 high_diamond_ranked_10min.csv # 10분 지표 학습 데이터셋
└── 📄 README.md             # 프로젝트 문서화

## 🧪 모델 학습 워크플로우

본 프로젝트는 배포 효율성과 학습 성능을 극대화하기 위해 **Hybrid Workflow**를 사용합니다.

### 1. Google Colab 학습 (권장)
고성능 리소스를 활용하여 학습을 진행하고, 결과를 `m2cgen`으로 코드화하여 반영합니다.
- **주 작업**: 모델 학습, 하이퍼파라미터 튜닝, `.py` 코드 추출
- **방법**: 제공된 Colab 노트북 코드를 실행 후 `models/` 내 파일들을 다운로드하여 프로젝트에 덮어쓰기

### 2. 로컬 학습 (백업)
인터넷 연결이 어렵거나 긴급한 수정을 위한 백업용 스크립트입니다.
```bash
python train.py
```
*주의: 로컬 학습 시에는 `m2cgen`, `scikit-learn` 등의 라이브러리가 설치되어 있어야 합니다.*

## 🛠️ 실행 방법

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. 서버 실행
```bash
python app.py
```

### 3. 웹 접속
브라우저를 열고 아래 주소로 이동합니다.
> **http://localhost:5000**

---
© 2026 HEXTECH Predictive Engine. Designed for Advanced LoL Analytics.
