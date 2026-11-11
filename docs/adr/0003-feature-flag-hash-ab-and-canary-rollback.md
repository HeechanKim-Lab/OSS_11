# ADR-0003: 결정론적 해시 기반 Feature Flag A/B 테스트 및 헬스체크 Canary 자동 롤백 아키텍처

- **상태 (Status)**: Accepted
- **결정 일자 (Date)**: 2026-10-12
- **의사결정자 (Deciders)**: `@HeechanKim-Lab`
- **관련 이슈/PR**: [#19](https://github.com/HeechanKim-Lab/OSS_11/issues/19), [#21](https://github.com/HeechanKim-Lab/OSS_11/issues/21), [#23](https://github.com/HeechanKim-Lab/OSS_11/issues/23)

---

## 1. 배경 및 문제 상황 (Context and Problem Statement)
신규 분석 알고리즘(병렬 Cutadapt, 적응형 Decontam, 3D PCoA 시각화)을 프로덕션에 배포할 때 전체 사용자에게 한 번에 노출하면 예상치 못한 메모리 급증이나 UI 혼란을 유발할 수 있습니다. 또한 외부 유료 SaaS(LaunchDarkly 등)에 의존하지 않고 오픈소스 자체 내장형 Feature Flag 및 Canary 롤아웃 제어기가 필요했습니다.

## 2. 고려한 대안들 (Considered Options)
* **대안 A: LaunchDarkly / Split.io 외부 유료 SDK 연동** — 기능은 강력하나 월 구독 비용 발생 및 오프라인 연구 환경 실행 불가.
* **대안 B: 단순 `random.random()` 확률 분기** — 새로고침할 때마다 사용자가 보는 UI Variant(A/B)가 바뀌어 실험 일관성이 깨짐.
* **대안 C: SHA-256 결정론적 해싱(Deterministic Hashing) 기반 자체 Feature Flag 엔진 + 단계별 Canary 컨트롤러** — 외부 비용 $0, 동일 `user_id`에 대해 100% 일관된 Variant 할당 보장.

## 3. 결정 내용 및 근거 (Decision Outcome)
**대안 C**를 채택합니다.
1. `SHA-256(f"{experiment_id}:{user_id}") % 100` 연산을 통해 버킷(0~99)을 고정 할당합니다.
2. Canary 배포는 `1% → 10% → 50% → 100%` 4단계로 점진 확대하며, 각 단계마다 헬스체크(`error_rate < 2.0%`, `p95_latency < 200ms`)를 수행해 위반 시 즉시 `0% (Stable 롤백)`로 자동 복구합니다.

## 4. 결과 및 영향 (Consequences)
* **긍정적 영향**: 외부 의존성 없이 100% 재현 가능한 A/B 실험 및 무중단 안전 배포 달성. DORA의 Change Failure Rate(7.4%)와 MTTR(1.95h)을 Elite/High 수준으로 유지.
