# 🐤 Canary 점진적 롤아웃(1%-10%-50%-100%) 및 헬스체크 자동 롤백 검증 리포트

- **검증 모듈**: [`amplicon_platform/canary_controller.py`](../amplicon_platform/canary_controller.py)
- **실행 로그**: [`logs/canary_rollout_verification.json`](../logs/canary_rollout_verification.json)
- **SLO 임계치 기준**: 에러율 $\le 2.0\%$, P95 응답 지연 $\le 200\text{ms}$, `/health` 상태 `UP`

## 1. 시나리오 A: 정상 점진적 롤아웃 (`v1.0.1-rc1`)

| 단계 | 트래픽 비율 | 에러율 (%) | P95 지연 (ms) | 판정 및 조치 |
| :---: | :---: | :---: | :---: | :--- |
| Stage | `1%` | `0.2%` | `82.0ms` | 🟢 PROMOTED: Stage 1% passed health check. |
| Stage | `10%` | `0.4%` | `95.0ms` | 🟢 PROMOTED: Stage 10% passed health check. |
| Stage | `50%` | `0.6%` | `112.0ms` | 🟢 PROMOTED: Stage 50% passed health check. |
| Stage | `100%` | `0.5%` | `108.0ms` | 🟢 PROMOTED: Stage 100% passed health check. |

- **최종 상태**: `COMPLETED_100_PCT` (활성 버전: `v1.0.1-rc1`)

## 2. 시나리오 B: 50% 구간 장애 주입 및 자동 롤백 (`v1.0.2-experimental-3d`)

| 단계 | 트래픽 비율 | 에러율 (%) | P95 지연 (ms) | 판정 및 자동 롤백 조치 |
| :---: | :---: | :---: | :---: | :--- |
| Stage | `1%` | `0.3%` | `88.0ms` | 🟢 PROMOTED: Stage 1% passed health check. |
| Stage | `10%` | `0.8%` | `115.0ms` | 🟢 PROMOTED: Stage 10% passed health check. |
| Stage | `50%` | `5.8%` | `340.0ms` | 🔴 CRITICAL: Health check failed at 50%. Automatically rolled back traffic to v1.0.0-stable (0% canary). |

- **최종 상태**: `AUTO_ROLLED_BACK` (자동 복구된 안정 버전: `v1.0.0-stable`, Canary 트래픽: `0%`)
