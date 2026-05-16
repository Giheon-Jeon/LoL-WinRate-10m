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
- [주요 기능](#✨-주요-기능)
- [🛠 기술 스택 및 선정 이유](#🛠-기술-스택-및-선정-이유)
- [🏗 아키텍처 및 폴더 구조](#🏗-아키텍처-및-폴더-구조)
- [🤝 협업 및 자동화 규칙](#🤝-협업-및-자동화-규칙)
- [🤖 AI 활용 방식](#🤖-ai-활용-방식)

---

## ✨ 주요 기능
1. **Hextech UI/UX**: 리그 오브 레전드 마법공학 테마를 적용한 프리미엄 웹 인터페이스 및 다이내믹 게이지 시스템
2. **MoE 앙상블 예측**: Logistic Regression과 Random Forest 모델을 결합한 혼합 전문가 시스템(MoE) 기반의 정밀 승률 분석
3. **Gemini 비전 스캔**: Gemini 2.0 Flash AI를 활용하여 인게임 스코어보드 스크린샷에서 10분 지표 자동 추출
4. **초경량 서버리스 배포**: m2cgen을 통한 모델 코드화로 Scikit-learn 의존성을 제거하여 Vercel 환경 최적화(500MB 미만)

---

## 🛠 기술 스택 및 선정 이유

### Frontend / Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

- **Python**: 강력한 데이터 처리 및 머신러닝 라이브러리 생태계를 활용하기 위한 핵심 언어
- **Flask**: 마이크로 웹 프레임워크를 통해 API 서빙과 정적 페이지 렌더링을 가볍고 빠르게 처리
- **NumPy**: 모델 연산 및 데이터 전처리를 위한 고성능 수치 계산 라이브러리

### ML 및 인프라
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

- **m2cgen**: 학습된 ML 모델을 순수 파이썬 코드로 변환하여 배포 시 Scikit-learn/Scipy 의존성(약 1GB) 제거
- **Google Colab**: 고성능 GPU/RAM 환경에서 모델을 학습시키고 배포용 소스 코드를 추출하는 하이브리드 워크플로우 지원
- **Vercel**: 서버리스 환경의 빠른 배포와 안정적인 API 서빙 환경 제공

---

## 🏗 아키텍처 및 폴더 구조
배포 용량 최소화와 유지보수 편의성을 위한 **하이브리드 코드화 구조** 채택

```text
.
├── 📁 models/               # 학습된 모델의 순수 파이썬 코드 및 스케일러 (Colab 추출)
│   ├── *_code.py            # m2cgen으로 생성된 무의존성 모델 로직
│   ├── scaler.json          # 데이터 정규화(StandardScaler) 파라미터
│   └── metrics.json         # 모델 성능 지표 데이터 (Accuracy, F1-Score)
├── 📁 templates/            # 단일 페이지 애플리케이션(SPA) HTML 템플릿
│   └── index.html           # Hextech 테마 기반 프론트엔드
├── 📄 app.py                # Flask 메인 서버 및 비즈니스 로직 핸들러
├── 📄 train.py              # 로컬 백업 및 모델 코드 추출용 학습 스크립트
├── 📄 requirements.txt      # Vercel 배포를 위한 최소 패키지 구성 (Numpy 중심)
├── 📄 .vercelignore         # 불필요한 바이너리 배포 제외 설정
└── README.md                # 프로젝트 통합 문서
```

<br>

## 🤝 협업 및 자동화 규칙

- `Git Flow`: main 브랜치를 중심으로 기능 단위의 브랜치 전략(BE-전기헌-번호) 활용

- `Commit Convention`: 이모지를 포함한 직관적인 태그 시스템 준수 (✨ Feat, 🐛 Fix, ⚡️ Perf 등)

- `Deployment`: Vercel 연동을 통한 자동 CI/CD 및 500MB Ephemeral Storage 최적화 준수

<br>

## 🤖 AI 활용 방식

인게임 스코어보드 스크린샷을 분석하여 10분 시점의 핵심 지표를 자동으로 정형 데이터화

**처리 과정:**

1. **이미지 캡처**: 사용자가 게임 내 10분 시점의 스코어보드 스크린샷을 업로드
2. **비전 분석**: Gemini 2.0 Flash 모델이 이미지 내의 KDA, CS, Gold, 경험치, 오브젝트 정보를 추출
3. **예측 모델**: 추출된 데이터를 m2cgen 기반 순수 파이썬 모델에 전달하여 즉각적인 승률 예측값 산출

**기술 스택:**

- Google Generative AI (Gemini 2.0 Flash)
- m2cgen (Model to Code Generator)
- Scikit-learn (Offline Training)
