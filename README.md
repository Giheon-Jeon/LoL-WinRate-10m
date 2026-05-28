# LoL Early WinRate Predictor (10m)

League of Legends 10분 지표를 기반으로 게임의 승패를 예측하는 머신러닝 엔진입니다.
기존의 복잡한 구조를 모두 제거하고 Flask 기반의 경량화된 구조로 재설계되었습니다.

## 🚀 주요 특징
- **경량화**: Node.js/Next.js 의존성 제거, Flask 단일 서버 구조
- **Hextech UI**: 리그 오브 레전드 테마의 프리미엄 디자인 적용
- **실시간 예측**: 데이터 수정 시 즉각적인 승률 분석
- **AI 스캔**: 인게임 스코어보드 스크린샷 분석 지원 (Gemini AI 연동)

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

## 📂 프로젝트 구조
- `app.py`: Flask 백엔드 서버 및 API 엔드포인트
- `train.py`: ML 모델 학습 스크립트
- `templates/index.html`: 통합 프론트엔드 UI
- `models/`: 학습된 모델 파일 (.joblib) 및 성능 리포트 (Git 추적 대상 제외)
- `high_diamond_ranked_10min.csv`: 학습용 데이터셋

## 🧪 모델 학습 방법
새로운 데이터로 모델을 다시 학습시키려면 다음 명령어를 실행하세요:
```bash
./.venv/Scripts/python train.py
```
