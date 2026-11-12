# 05. 지표

| 제품 | 버전 | 최종 수정 | 관련 가설 |
|---|---|---|---|
| AmpliconSight | 0.2 | 2026-11-12 | H1~H4 |

> v0.2 변경 (`Cycle 1` 반영): `M2` 목표 근거를 `"임의"`에서 `"Cycle 1 실측 82.5% (52/63)"`으로 갱신하되 목표치(`60%`) 자체는 유지.

## 1. North Star Metric

- NSM: **주간 Pre-flight QC 통과 후 파이프라인 스니펫 실행 건수 (Weekly Verified Pipeline Launches)** — 정의: 한 주 동안 AmpliconSight에서 매니페스트 검증을 통과하고 추천 파라미터를 수락(`qc_recommendation_accepted` & `cli_snippet_copied`)하여 실제 분석으로 이어진 배치 건수의 합
- 왜 이 지표인가: 연구자가 얻는 핵심 가치는 "웹 화면을 구경하는 것"이 아니라 **"에러 없는 설정으로 본 파이프라인을 실패 없이 시작하는 것"**이다. 추천 수락(`H2`)과 배치마다 재방문(`H3`)이 모두 반영된다.
- 현재 기준: 측정 전 (기존 수동 스크립트 환경) → MS3 종료 목표: **주 40배치** (활성 연구자 25명 × 주 1.6배치)

## 2. AARRR 지표

| ID | 단계 | 지표 | 정의 (계산식) | 기준값 | 목표 (MVP) | 목표 근거 | 검증 가설 |
|---|---|---|---|---|---|---|---|
| M1 | Acquisition (문제 확인) | 인터뷰 문제 확인율 | "최근 3개월 내 매니페스트·오염 기준으로 재실행 2회 이상" 응답자 / 전체 인터뷰 | 80% (내부 연구실 사전 관찰) | 70% 이상 (N=10) | 타 연구실 표본 편향을 고려해 10%p 보수적 설정 | H1 |
| M2 | Activation | Pre-flight QC 추천 수락률 | `qc_recommendation_accepted` / `qc_recommendation_shown` (세션 단위) | 없음 | 60% 이상 (추천 노출 60건 이상) | Cycle 1 실측 82.5% (52/63) (초기엔 임의 60% — "10번 중 6번은 추천 설정을 신뢰") | H2 |
| M3 | Retention | D14 코호트 리텐션 | 첫 검증 14일 뒤 7일 창 내 1회 이상 `manifest_uploaded` 수행 연구자 / 가입 코호트 | 38.6% (Variant A 정적 로그 기준) | 50% 이상 (코호트 20명 이상) | 정적 대조군 대비 +11.4%p 이상 개선 목표 | H3 |
| M4 | Revenue | 기관·코어 퍼실리티 유료 도입 의향률 | "연구실/기관당 월 49,000원이면 도입하겠다" 응답 / 설문 응답 | 없음 | 측정만 (목표 없음, MS3 이후) | 수익 모델은 학술 PMF 확인 후 | — (수익 가설은 MS3 이후 추가) |
| M5 | Referral | QC 인증 리포트 공유율 · K-factor | `qc_badge_shared` 발생 연구자 / 주간 활성 · (공유 수 × 공유 링크 유입 전환율) | 없음 | 공유율 20% 이상, K 0.25 이상 | 임의 — MS3 첫 실험 후 보정 | H4 |

보조 지표 (Guardrail):
- **G1 첫 QC 완료 시간 중앙값**: `workbench_entered`부터 `qc_recommendation_accepted`까지 소요 시간 — 기존 수동 방식(18.3분) 대비 **5.0분 이하** 유지. 5.0분 초과 시 UI 복잡도 과다 신호.
- **G2 파이프라인 첫 실행 성공률**: 생성된 CLI 스니펫으로 `run_pipeline.sh` 실행 시 매니페스트 에러 없이 DADA2 단계에 진입한 비율 — **85% 이상** 유지.

## 3. Actionable vs Vanity

| 보지 않을 숫자 (Vanity) | 이유 | 대신 볼 것 |
|---|---|---|
| GitHub 저장소 누적 Star / 페이지 단순 조회수 | 호기심 방문은 연구자의 실제 매니페스트 검증 행동과 무관함 | **M2** Pre-flight QC 추천 수락률, **NSM** |
| 업로드된 총 샘플 행(Row) 수 합계 | 한 연구자가 500개 샘플을 1번 넣어도 수치는 폭증하여 착시를 일으킴 | 연구자·배치 단위 **M2** 수락률 및 **M3** 코호트 리텐션 |
| 웹 페이지 체류 시간 (Session Duration) | Pre-flight QC 도구는 **짧게 검증하고 빨리 터미널로 나가는 것**이 성공임 | **G1** 첫 QC 완료 시간 중앙값 (5.0분 이하 목표) |
| 누적 생성된 스니펫 수 (비검증 포함) | 에러가 있는 상태로 복사한 횟수는 가치를 대변하지 못함 | 검증 통과 후 수락 비율(**M2**) 및 첫 실행 성공률(**G2**) |

## 4. 측정 방법과 이벤트

- 도구: **자체 결정론적 A/B 이벤트 로거(`amplicon_platform/feature_flags.py` → `logs/ab_experiment_events.jsonl`) + PostHog Cloud 무료 티어 병행** (확인 필요: `https://posthog.com/pricing`, 2026-11-01 기준 월 100만 이벤트 무료)
- 수집 및 자동 리포팅 주기: 실시간 JSONL 기록 + GitHub Actions(`.github/workflows/issue_pr_sla_automation.yml` 및 `dora_metrics.yml`)가 주간 리포트를 자동 갱신하고 임계값 미달 시 Issue 자동 생성.
- MS0 (Wizard of Oz) 기간에는 `experiments/cycle-1/woz-log.csv`에 추천 노출·수락 여부와 소요 시간을 동기화 기록한다.

| 이벤트 이름 | 지표 | 발생 시점 | 속성 |
|---|---|---|---|
| `workbench_entered` | 코호트, G1 | 워크벤치 접속 및 연구자 ID 해시 할당 | `user_id`, `variant` |
| `manifest_uploaded` | M3 | Casava 1.8 매니페스트 검증 클릭 | `sample_count`, `is_valid` |
| `qc_recommendation_shown` | M2 | Pre-flight QC 진단 및 추천 파라미터 카드 노출 | `variant`, `experiment_id` |
| `qc_recommendation_accepted` | M2, NSM, G1 | 추천 파라미터 "수락" 클릭 | `seconds_to_accept`, `decontam_threshold` |
| `qc_recommendation_rejected` | M2 | 추천 파라미터 "직접 수정(거절)" 클릭 | `reason` |
| `cli_snippet_copied` | NSM, G2 | 생성된 `run_pipeline.sh` CLI 스니펫 복사 | `flags_enabled` |
| `qc_badge_shared` | M5 | QC 인증 리포트 공유 링크 클릭 | `cohort_id` |

코호트 기준: 첫 매니페스트 검증 주차 (ISO Week) · 리텐션 관측 창: D7 / D14 (배치 시퀀싱 주기를 반영해 **D14**를 주 지표로 채택).
