# 기여 가이드 (Contributing Guide)

`Micro-Tom Rhizosphere Amplicon Pipeline & AmpliconSight Workbench (OSS_11)` 오픈소스 프로젝트에 기여해 주셔서 감사합니다! 본 문서는 Feature 브랜치 전략, Conventional Commits 규칙, Pull Request 절차 및 구조화된 코드 리뷰(`[MUST]` / `[SHOULD]`) 가이드를 정의합니다.

---

## 1. 브랜치 전략 (Feature Branch Workflow)

본 저장소는 `main` 브랜치를 항상 배포 가능한 안정 상태(Production-Ready)로 유지하는 **Feature Branch 전략**을 따릅니다.

```text
main (Protected) ──●──────────────────────●───────────────────●──▶ (Release / Deploy)
                    \                    /                   /
                     └── feat/core-tdd ─┘ (PR #1)           /
                                         └── fix/dada2-oom ┘ (PR #2)
```

### 브랜치 명명 규칙
- `feat/<기능명>`: 새로운 분석 모듈, 대시보드 기능, Feature Flag 도입 (예: `feat/core-amplicon-tdd`)
- `fix/<버그명>`: 파이프라인 오류 수정 및 핫픽스 (예: `fix/gzip-stream-pipe`)
- `docs/<문서명>`: 문서, ADR, PRD, Wiki 업데이트 (예: `docs/adr-and-wiki`)
- `ci/<작업명>`: GitHub Actions 워크플로우, Docker/패키지 배포 파이프라인 수정
- `refactor/<대상>`: 레거시 코드 리팩토링 및 아키텍처 개선

---

## 2. 커밋 메시지 규칙 (Conventional Commits)

모든 커밋은 [Conventional Commits v1.0.0](https://www.conventionalcommits.org/) 규격을 엄격히 준수합니다.

```text
<type>(<scope>): <subject>

[optional body]
[optional footer(s)]
```

### 허용되는 Type 목록
| Type | 설명 | 예시 |
| :--- | :--- | :--- |
| **`feat`** | 새로운 기능 또는 분석 모듈 추가 (TDD Green 단계 포함) | `feat(qc): implement Casava 1.8 FASTQ manifest validator` |
| **`fix`** | 버그 및 파이프라인 런타임 오류 패치 | `fix(dada2): resolve memory overflow by chunking nbases` |
| **`test`** | 단위 테스트(TDD Red 단계) 및 E2E 테스트 추가 | `test(red): add failing unit tests for Shannon diversity` |
| **`refactor`** | 기능 변경 없는 코드 구조 개선 (TDD Refactor 단계) | `refactor(legacy): modularize legacy app.py with type hints` |
| **`ci`** | GitHub Actions, Matrix, Docker, 배포 설정 변경 | `ci(matrix): add reusable workflow and composite action` |
| **`docs`** | README, ADR, Wiki, Lean PRD 문서 작성 및 갱신 | `docs(prd): update 11-bml-log after cycle-1 experiment` |
| **`chore`** | 패키지 버전 범프, 의존성 관리 | `chore(release): bump package version from 1.0.0 to 1.0.1` |

---

## 3. 개발 및 TDD(Test-Driven Development) 절차

1. **Red (실패하는 테스트 작성)**: 구현할 요구사항에 대한 단위 테스트를 `tests/` 아래에 먼저 작성하고 실행하여 실패를 확인합니다. (`test(red): ...`)
2. **Green (최소 통과 코드 구현)**: 테스트를 통과하는 핵심 비즈니스 로직을 `amplicon_platform/`에 구현합니다. (`feat(green): ...`)
3. **Refactor (코드 정리 및 최적화)**: 중복을 제거하고 타입 힌트와 독스트링을 보강합니다. 전체 테스트 커버리지는 **80% 이상**을 유지해야 합니다. (`refactor: ...`)

### 로컬 테스트 실행 명령어
```bash
# 단위 테스트 및 커버리지 측정 (80% 이상 필수)
pytest tests/ --cov=amplicon_platform --cov-report=term-missing

# 정적 린트 검사
pylint amplicon_platform/ --exit-zero
```

---

## 4. Pull Request 및 구조화된 코드 리뷰 규칙 (`[MUST]` / `[SHOULD]`)

1. 작업이 완료되면 `.github/PULL_REQUEST_TEMPLATE.md` 양식에 맞춰 PR을 생성합니다.
2. `CODEOWNERS`에 지정된 메인테이너에게 자동으로 리뷰가 요청됩니다.
3. 모든 리뷰어는 피드백의 우선순위와 강제성을 명확히 전달하기 위해 다음 **구조화된 태그**를 반드시 사용합니다 (상세 내용: [`docs/REVIEW_GUIDE.md`](docs/REVIEW_GUIDE.md)):
   - **`[MUST]`**: 병합(Merge) 전 **반드시 수정**해야 하는 치명적 결함, 보안 이슈, 테스트 누락, 데이터 무결성 오류.
   - **`[SHOULD]`**: 아키텍처 개선, 가독성 향상, 성능 최적화를 위해 **강력히 권장**하는 사항 (합당한 사유가 있으면 후속 이슈로 이관 가능).
   - **`[NIT]`**: 사소한 타이포, 변수명 스타일 등 비차단(Non-blocking) 제안.
   - **`[PRAISE]`**: 훌륭한 TDD 설계나 깔끔한 리팩토링에 대한 긍정적 피드백.
4. 모든 CI 체크(Matrix Test, Lint, Security Audit)가 통과하고 `[MUST]` 지적 사항이 해결되면 `Squash and merge` 또는 `Merge pull request`로 병합합니다.
