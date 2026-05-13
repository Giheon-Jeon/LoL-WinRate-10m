# 🎮 HEXTECH Early 10m Match Win-Rate Predictor
## ML 기반 리그오브레전드 다이아몬드 랭크 초반 10분 승부 예측기

<p align="center">
  <!-- 로고 이미지가 있다면 주소를 넣으시고, 없다면 이 주석을 삭제하세요 -->
  <img width="170" height="170" alt="project_logo" src="https://img.icons8.com/color/170/league-of-legends.png" />
</p>

<p align="center">
  <strong>Giheon-Jeon / LoL-WinRate-10m</strong><br>
  "10분의 경기 지표로 소환사의 협곡 미래를 예측하고 ML 모델을 비교 분석하세요."
</p>

---

## 📌 목차
- [주요 기능](#-주요-기능)
- [🛠 기술 스택 및 선정 이유](#-기술-스택-및-선정-이유)
- [🏗 아키텍처 및 폴더 구조](#-아키텍처-및-폴더-구조)
- [🤝 협업 및 자동화 규칙](#-협업-및-자동화-규칙)
- [🤖 AI 활용 방식](#-ai-활용-방식)

---

## ✨ 주요 기능
1. ** early 10m Sandbox**: 블루팀과 레드팀의 Kills, Gold, CS, 드래곤 등 10분 시점 핵심 게임 데이터를 실시간 슬라이더 및 카운터로 시뮬레이션할 수 있습니다.
2. **다중 ML 모델 승률 예측**: XGBoost, Random Forest, Logistic Regression 모델을 선택 및 교체하여, 각 알고리즘이 예측하는 실시간 승률 변화 및 최종 유력 팀 결과를 시각화합니다.
3. **상호 대화형 자동 밸런싱**: 블루팀 킬 증가 시 레드팀 데스 자동 동기화, CS 증가 시 획득 골드 자동 비례 증가 등 정형 데이터 샌드박스의 편의성을 제공합니다.
4. **모델 벤치마크 및 지표 비교**: 각 머신러닝 알고리즘의 Accuracy, F1-Score, ROC-AUC 메트릭을 카드 인터페이스와 스케일바로 투명하게 시각화하고 즉석에서 모델 재학습을 트리거할 수 있습니다.

---

## 🛠 기술 스택 및 선정 이유

### Frontend / Backend
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-1E2E42?style=for-the-badge&logo=xgboost&logoColor=white)

- **FastAPI**: 대규모 머신러닝 모델의 추론 및 재학습 요청을 비동기식 고성능 웹 API로 최적 서빙하기 위해 선정하였습니다.
- **Next.js & TypeScript**: 강력한 App Router 구조를 바탕으로, 실시간 데이터 반응성과 정밀한 예측 결과를 신속히 표현하는 프리미엄 유저 대시보드를 안정적으로 렌더링합니다.
- **XGBoost & Scikit-Learn**: 고차원 정형 데이터셋에서 최고 수준의 일반화 성능 및 정확도를 제공하는 그래디언트 부스팅 모델과 분류 알고리즘 구축을 위해 선정하였습니다.

### 인프라 및 환경 설정
![ESLint](https://img.shields.io/badge/ESLint-4B32C3?style=for-the-badge&logo=eslint&logoColor=white)
![Prettier](https://img.shields.io/badge/Prettier-F7B93E?style=for-the-badge&logo=prettier&logoColor=white)

---

## 🏗 아키텍처 및 폴더 구조
유지보수성과 확장성을 고려한 **기능 단위(Feature-based) 구조** 채택
```text
├── 📁 backend/               # Python FastAPI ML 서버
│   ├── 📁 models/            # 훈련 완료된 모델 가중치 및 metrics.json
│   ├── 📄 main.py            # FastAPI 라우터 및 예측 API
│   └── 📄 train.py           # pandas & scikit-learn 데이터 학습 스크립트
├── 📁 src/
│   └── 📁 app/               # Next.js App Router 메인 컴포넌트
│       ├── 📄 globals.css    # 헥스테크 프리미엄 테마 CSS
│       ├── 📄 layout.tsx     # Google Fonts(Cinzel, Inter) 및 SEO 설정
│       └── 📄 page.tsx       # 실시간 샌드박스 & 예측 대시보드 로직
├── 📁 public/                # 10분 다이아몬드 경기 CSV 원본 데이터
└── 📄 tsconfig.json          # TypeScript 설정 파일
```

<br>

## 🤝 협업 및 자동화 규칙

- `Git Flow`: main → develop → feature/기능명 브랜치 전략 (학습 및 린트 보안 스캔 연동)

- `Commit Convention`: `{이모지} {태그}: {작업 내용} 구현 (#이슈번호)` 규칙 엄수

- `Pull Request`: feature → develop로 PR, 최소 1명 이상 승인 후 머지

<br>

## 🤖 AI 활용 방식

- **Antigravity AI Tutor**: Git 워크플로우 제어, 정형 머신러닝 데이터 전처리 파이프라인 설계, 롤 무드의 화려한 다크-골드 헥스테크 대시보드 디자인 셋업 보조.
