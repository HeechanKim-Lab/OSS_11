# 🧯 Troubleshooting (문제 해결 가이드)

> **Wiki 네비게이션**: [🏠 Home](Home.md) | [🚀 Getting Started](Getting-Started.md) | [🛠️ Development Guide](Development-Guide.md) | **🧯 Troubleshooting**

본 문서는 파이프라인 실행, 테스트 및 CI/CD 배포 과정에서 자주 발생하는 오류와 해결 방법을 정리합니다. 기본 환경 설정은 **[🚀 Getting Started](Getting-Started.md)** 를, 모듈 구조는 **[🛠️ Development Guide](Development-Guide.md)** 를 참조하세요.

---

## 1. DADA2 Error Model 학습 시 Memory Overflow (Exit Code 137)

- **관련 이슈**: [#11](https://github.com/HeechanKim-Lab/OSS_11/issues/11)
- **증상**: 시퀀싱 심도(depth)가 10만 read 이상인 샘플 110개를 동시 처리할 때 R 세션이 OOM(Out Of Memory)으로 강제 종료됨.
- **원인**: `dada2::learnErrors()`의 기본 `nbases = 1e8` 설정이 전체 배치 메모리를 과점유함.
- **해결 방법**:
  ```r
  # modules/03_dada2_denoise.sh 내부 파라미터 조정
  errF <- learnErrors(filtFs, nbases = 1e6, multithread = 4, randomize = TRUE)
  ```
  또는 `FF_PARALLEL_CUTADAPT` 플래그와 함께 청크 단위 서브샘플링을 활성화하세요.

---

## 2. LinDA Random Effect 모델 수렴 실패 (`boundary (singular) fit`)

- **관련 이슈**: [#17](https://github.com/HeechanKim-Lab/OSS_11/issues/17)
- **증상**: 단일 배치 또는 1~2개 샘플에서만 관찰되는 희귀 분류군(Rare Taxa) 포함 시 `lme4` 내부에서 Singularity 경고가 발생하며 계수가 `NA`로 반환됨.
- **원인**: Zero-inflation 비율이 95%를 초과하는 ASV에 대해 랜덤 효과 분산 추정이 불가능함.
- **해결 방법**:
  `amplicon_platform.core.run_linda_differential_test()` 호출 시 `min_prevalence=0.10` (최소 10% 이상 샘플에서 출현) 필터가 선행 적용되도록 설정합니다.

---

## 3. 저사양 노드에서 Gzip 스트림 해제 중 `Broken pipe (EPIPE)` 오류

- **관련 이슈**: [#22](https://github.com/HeechanKim-Lab/OSS_11/issues/22)
- **증상**: 8GB 이하 RAM 환경에서 대용량 `.fastq.gz` 파이프 연결 시 `SIGPIPE` 발생.
- **해결 방법**: `zcat` 대신 `gzip -dc`와 `pigz -p 2` 스트림 버퍼링을 사용하고, 매니페스트 검증기(`validate_fastq_manifest`)로 손상된 압축 파일을 사전 격리합니다.

---

## 4. Canary 배포 중 에러율 급증으로 인한 자동 롤백 발생 시

- **증상**: Canary 롤아웃 단계(`10%` 또는 `50%`)에서 응답 지연(> 200ms) 또는 에러율(> 2.0%)이 감지되어 `v1.0.0 Stable`로 자동 롤백됨.
- **조치 절차**:
  1. `logs/canary_rollout_verification.json`에서 실패한 단계의 `error_rate`와 `p95_latency_ms`를 확인합니다.
  2. 해당 배포에서 켜진 Feature Flag를 환경변수에서 `false`로 비활성화합니다.
  3. **[🛠️ Development Guide](Development-Guide.md)** 의 로컬 TDD 검증 절차를 다시 수행한 뒤 재배포합니다.
