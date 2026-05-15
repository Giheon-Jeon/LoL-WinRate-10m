# 💎 LoL Early WinRate Predictor (10m) - Hextech Edition

League of Legends Diamond+ 랭크 게임의 10분 지표를 분석하여 실시간 승률을 예측하는 프리미엄 머신러닝 솔루션입니다. 
기존의 복잡한 Full-stack 구조를 탈피하고, Flask 단일 프레임워크를 기반으로 한 **초경량 통합 아키텍처**로 재설계되었습니다.

## 🚀 주요 특징
- **Hextech UI/UX**: 리그 오브 레전드 고유의 마법공학 미학을 적용한 고품질 웹 인터페이스
- **초경량 통합 구조**: Node.js/Next.js 의존성을 완전히 제거하고 Flask 하나로 UI와 API를 동시 서빙
- **실시간 예측 엔진**: 수치 변경 시 지연 없는 즉각적인 승률 업데이트 (XGBoost, Random Forest, Logistic Regression 지원)
- **AI 성능 대시보드**: 각 모델의 Accuracy, F1-Score, ROC-AUC 등 정밀 지표 실시간 확인 가능
- **인공지능 스코어보드 스캔**: Gemini Vision AI를 연동하여 스크린샷 한 장으로 모든 인게임 지표 자동 추출

## 🛠️ 실행 방법

### 1. 가상환경 설정 및 패키지 설치
(현재 저장소에 포함된 가상환경을 그대로 사용하거나, 아래 명령어로 새로 구축할 수 있습니다.)
```bash
py -m venv .venv
source .venv/Scripts/activate  # 또는 .\.venv\Scripts\activate
pip install flask flask-cors pandas joblib scikit-learn pillow google-generativeai xgboost
```

### 2. 서버 실행
프로젝트 루트 폴더에서 다음 명령어를 실행합니다.
```bash
# 가상환경 직접 실행 방식
./.venv_new/Scripts/python app.py
```

### 3. 웹 접속
브라우저를 열고 아래 주소로 이동합니다.
> **http://localhost:5000**

## 📂 프로젝트 구조
- `app.py`: 통합 웹 서버, API 핸들러 및 모델 서빙 로직
- `train.py`: 머신러닝 모델 학습 및 성능 지표 생성 스크립트
- `templates/index.html`: Hextech 테마 기반의 단일 페이지 프론트엔드
- `models/`: 학습 완료된 모델 파라미터 및 스케일러 저장소
- `high_diamond_ranked_10min.csv`: 다이아몬드+ 티어 10분 데이터셋

## 🧪 AI 모델 학습
데이터셋이 업데이트되었거나 새로운 모델 파라미터를 적용하려면 아래 명령어를 실행하세요.
```bash
./.venv_new/Scripts/python train.py
```
학습이 완료되면 `models/` 디렉토리에 새로운 파일과 `metrics.json`이 자동 생성됩니다.

---
© 2026 HEXTECH Predictive Engine. Designed for Advanced LoL Analytics.
