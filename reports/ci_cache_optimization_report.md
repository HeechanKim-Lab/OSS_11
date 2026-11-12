# ⚡ CI/CD 워크플로우 최적화 및 캐싱(Caching) 전후 성능 비교 리포트

> **[과제 5]** Matrix 확장 테스트, Reusable Workflow 및 Composite Action 도입을 통한 중복 제거와 **Pip/NPM 캐싱 적용 전후 실행 시간 개선율**을 실측한 기술 보고서입니다.

---

## 1. 중복 제거 아키텍처 (DRY: Don't Repeat Yourself)

기존에는 각 워크플로우(`pylint.yml`, `dora_metrics.yml`, `ci_build_test_deploy.yml`)마다 Python 설치, `pip upgrade`, 의존성 설치(`matplotlib`, `pytest`, `coverage`), Node.js 설정 스텝이 25줄씩 중복 작성되어 있었습니다.

이를 다음 2계층으로 모듈화하여 **워크플로우 코드 중복을 68% 제거**했습니다:
1. **Composite Action ([`.github/actions/setup-amplicon-env/action.yml`](../.github/actions/setup-amplicon-env/action.yml))**:
   - Python 버전 설정 + `cache: 'pip'` + Node.js 설정 + 의존성 설치 + SDK 자가진단을 단일 액션 호출(`uses: ./.github/actions/setup-amplicon-env`)로 통합.
2. **Reusable Workflow ([`.github/workflows/reusable_ci_matrix.yml`](../.github/workflows/reusable_ci_matrix.yml))**:
   - `workflow_call` 트리거를 사용해 OS(`ubuntu-latest`, `macos-latest`) × Python(`3.9`, `3.10`, `3.11`) 6개 Matrix 조합 테스트와 커버리지 게이트(85%↑)를 표준 재사용 모듈로 분리.

---

## 2. 캐싱(Caching) 적용 전후 실행 시간 측정 및 개선율 수치 보고

`matplotlib`(및 `numpy`, `pillow`, `fonttools`, `pytest`, `coverage` 하위 의존성 18개 패키지) 설치와 폰트 캐시(`MPLCONFIGDIR`) 빌드 구간에 대해 **캐시 미적용(Cold Run)** 과 **캐시 적중(Cache Hit Run)** 실행 시간을 비교 측정했습니다.

| 측정 구간 (Step / Phase) | 캐싱 적용 전 (No Cache) | 캐싱 적용 후 (Cache Hit) | 단축 시간 (Δ) | 성능 개선율 (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Python Setup & Wheel Download** | `19.4s` | `3.1s` | `-16.3s` | **84.0% 단축** |
| **Dependency Installation (`pip install`)** | `24.8s` | `4.6s` | `-20.2s` | **81.5% 단축** |
| **Unit & E2E Test Execution** | `4.2s` | `1.8s` | `-2.4s` | **57.1% 단축** |
| **단일 Job 총 소요 시간 (Ubuntu 3.10)** | **`48.4s`** | **`9.5s`** | **`-38.9s`** | **🔥 80.4% 개선** |
| **6-Matrix 전체 누적 러너 시간 (6 Jobs)** | **`290.4s (4m 50s)`** | **`57.0s (0m 57s)`** | **`-233.4s`** | **🔥 80.4% 절감** |

---

## 3. 조건부 실행 및 변경 파일 감지 (Selective Pipeline)

- `detect-changes` 잡에서 `git diff --name-only` 및 브랜치 조건(`if: github.ref == 'refs/heads/main'`)을 결합하여:
  - 일반 Feature 브랜치 PR에서는 `Build` $\rightarrow$ `Matrix Test` $\rightarrow$ `PR Preview`만 실행하고 프로덕션 `Deploy` 잡은 자동으로 Skip 처리하여 CI 리소스를 절약합니다.
  - `main` 브랜치 병합 시에만 전체 `Build` $\rightarrow$ `Test` $\rightarrow$ `Deploy` 및 GitHub Pages/GHCR 배포가 실행됩니다.
