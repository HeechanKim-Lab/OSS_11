# 🚀 Getting Started (시작하기 가이드)

> **Wiki 네비게이션**: [🏠 Home](Home.md) | **🚀 Getting Started** | [🛠️ Development Guide](Development-Guide.md) | [🧯 Troubleshooting](Troubleshooting.md)

본 문서는 `Micro-Tom Rhizosphere Amplicon Pipeline & AmpliconSight Workbench`를 로컬 환경 및 Docker 컨테이너에서 설치하고 첫 번째 분석과 웹 대시보드를 실행하는 방법을 안내합니다.

---

## 1. 사전 요구사항 (Prerequisites)

| 구성 요소 | 최소 버전 | 권장 버전 | 용도 |
| :--- | :---: | :---: | :--- |
| **Python** | `3.9+` | `3.10` / `3.11` | 코어 QC/다양성 분석 엔진, Feature Flag, DORA/Sprint 분석 |
| **Node.js & npm** | `18.x+` | `20 LTS` | `@heechankim-lab/oss-11` 패키지 및 프런트엔드 빌드 |
| **Docker** | `24.0+` | 최신 안정 버전 | 재현 가능한 컨테이너 실행 및 헬스체크 검증 |
| **QIIME2 / R** *(선택)* | `2024.5` / `4.3+` | 최신 안정 버전 | 원시 FASTQ 대용량 쉘 파이프라인(`modules/`) 직접 실행 시 |

---

## 2. 설치 방법 (Installation)

### 2.1 저장소 클론 및 Python 환경 구성
```bash
git clone https://github.com/HeechanKim-Lab/OSS_11.git
cd OSS_11

# 가상환경 생성 및 의존성 설치
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2.2 npm 패키지 설치
```bash
npm install
```

---

## 3. 빠른 실행 (Quick Start)

### 3.1 코어 파이프라인 단위 테스트 및 커버리지 검증
```bash
pytest tests/ --cov=amplicon_platform --cov-report=term-missing
```

### 3.2 Feature Flag 및 Canary 롤아웃 시뮬레이션 실행
```bash
# Feature Flag 토글 및 A/B 테스트 할당 검증
python3 -m amplicon_platform.cli --Verify-flags --user-id "researcher_01"

# Canary 1% -> 10% -> 50% -> 100% 롤아웃 및 자동 롤백 시나리오 실행
python3 -m amplicon_platform.canary_controller
```

### 3.3 웹 대시보드 로컬 실행
```bash
python3 -m http.server 8080 --directory web
# 브라우저에서 http://localhost:8080 접속
```

---

## 4. 다음 단계 (Next Steps)

- 코드 구조와 TDD 개발 절차, Feature Flag 추가 방법을 알아보려면 👉 **[🛠️ Development Guide (개발자 가이드)](Development-Guide.md)** 로 이동하세요.
- 설치나 실행 중 메모리 부족(OOM) 또는 패키지 충돌이 발생했다면 👉 **[🧯 Troubleshooting (문제 해결 가이드)](Troubleshooting.md)** 를 확인하세요.
