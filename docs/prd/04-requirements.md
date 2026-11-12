# 04. 요구사항

| 제품 | 버전 | 최종 수정 | 관련 가설 |
|---|---|---|---|
| AmpliconSight | 0.2 | 2026-11-12 | H2, H3 |

범위: `03-solution-and-mvp.md` §3의 **In 항목만** 포함한다 (`v0.2`: `Cycle 1` 피드백에 따라 `FR8` 추가).

## 1. 사용자 스토리

| ID | 스토리 | 수용 기준 | 검증 가설 |
|---|---|---|---|
| US1 | 김지훈(Wet-lab 석사생)으로서 FASTQ 파일 목록을 붙여넣고 3초 안에 R1/R2 짝 오류를 확인하고 싶다, 그래야 서버에서 2시간 대기 후 에러가 나지 않는다 | Given 워크벤치 접속, When 매니페스트 텍스트 입력 후 검증 클릭, Then 누락된 R2 파일·중복 샘플 ID가 행 번호와 함께 표시되고 `manifest_uploaded` 이벤트가 기록된다 | H2 |
| US2 | 김지훈으로서 내 시료의 어댑터 트리밍 수율과 음성대조군(NTC) 오염 여부에 맞춘 추천 파라미터 카드를 보고 싶다, 그래야 스스로 임계값을 고민하지 않는다 | Given 유효한 매니페스트 입력, When Pre-flight 진단 완료, Then Cutadapt 최소 잔존율(70%)·Decontam 임계값 추천 카드가 노출되고 `qc_recommendation_shown`이 1회 기록된다 | H2 |
| US3 | 김지훈으로서 추천 파라미터를 수락해 즉시 실행 가능한 명령어를 받고 싶다, 그래야 터미널에 붙여넣기만 하면 끝난다 | When "추천 수락" 탭 클릭, Then `qc_recommendation_accepted` 및 `cli_snippet_copied`가 기록되고 클립보드에 실행 스크립트 인자가 복사된다 | H2 |
| US4 | 박소연(포닥)으로서 추천 파라미터가 내 실험 설계와 다르면 수동 조정(거절)하고 싶다, 그래야 통제권을 잃지 않는다 | When "직접 수정(거절)" 클릭, Then `qc_recommendation_rejected{reason}`가 기록되고 수동 파라미터 입력 모드로 전환된다 | H2 |
| US5 | 박소연으로서 Feature Flag 토글로 3D PCoA 프리뷰와 적응형 Decontam 효과를 비교하고 싶다, 그래야 다음 시퀀싱 배치 때도 이 워크벤치를 다시 찾게 된다 | Given `FF_INTERACTIVE_3D_PCOA` 활성화, When 샘플 데이터 로드, Then PC1/PC2/PC3 분산 설명력과 오염 제거 전·후 ASV 수가 즉시 갱신된다 | H3 |
| US6 | 연구자로서 별도 회원가입 절차 없이 연구자 ID만으로 일관된 실험 환경(Variant A/B)을 유지하고 싶다, 그래야 진입장벽 없이 바로 쓴다 | Given `researcher_id` 입력, When SHA-256 해시 버킷 평가, Then 동일 ID에 대해 항상 동일한 A/B Variant가 할당되고 `workbench_entered`가 기록된다 | — (최소 동작 조건) |

## 2. 기능 요구사항

| ID | 요구사항 | 관련 스토리 | 우선순위 |
|---|---|---|---|
| FR1 | Casava 1.8 Paired-end 매니페스트 검증기 (`validate_fastq_manifest`): 샘플 ID 공백·중복, `.fastq.gz` 확장자, `_R1_`↔`_R2_` 대칭성 검사 | US1 | Must |
| FR2 | Pre-flight QC 추천 카드 생성: `calculate_trimming_yield` 및 `identify_contaminant_asvs` 결과 기반 권장 파라미터 제시 | US2 | Must |
| FR3 | MS0 Wizard of Oz 운영: 연구자 제출 매니페스트에 대해 본인이 연구실 기준(`modules/00`~`13`)으로 추천 파라미터 검수 후 `woz-log.csv` 기록 | US2 | Must (MS0) |
| FR4 | MS1 자동화: 브라우저/경량 SDK(`@heechankim-lab/oss-11`) 및 Python 코어 엔진으로 실시간 추천 계산 + Feature Flag 4종 연동 | US2, US5 | Must (MS1) |
| FR5 | 추천 "수락" / "직접 수정(거절)" 버튼 및 `qc_recommendation_accepted` / `qc_recommendation_rejected` 이벤트 수집 | US3, US4 | Must |
| FR6 | 결정론적 SHA-256 `assign_ab_variant` 기반 사용자 세션 식별 및 A/B Variant 고정 할당 | US6 | Must |
| FR7 | GitHub Pages 정적 웹 배포 및 `/health.json` SLO 헬스체크 엔드포인트 제공 | US5, US6 | Should |
| FR8 | NTC 오염 ASV 제거 근거 한 줄 툴팁 표시 및 매니페스트 `_R1_`↔`_R2_` 오타 원클릭 자동 치환 버튼 (v0.2 추가) | US1, US2 | Must (MS1) |

## 3. 비기능 요구사항

| 영역 | 요구사항 |
|---|---|
| 성능 | 브라우저 내 매니페스트 100개 행 검증 응답 시간 **100ms 이내**, 페이지 초기 로드(LCP) **1.5초 이내** |
| 보안·데이터 주권 | **Zero-Upload 원칙**: 원시 FASTQ 시퀀스 데이터는 서버로 절대 전송하지 않으며 파일명·요약 카운트만 클라이언트에서 처리. 공공기관 보안 규정 100% 준수 |
| 비용 | GitHub Pages + GitHub Actions 무료 티어 내 운영으로 **월 인프라 비용 0원** 유지 (상한 월 2만 원) |
| 신뢰성·복구 | Canary 롤아웃(`1% -> 10% -> 50% -> 100%`) 중 에러율 > 2.0% 또는 p95 지연 > 800ms 감지 시 즉시 `v1.0.0-stable`로 자동 롤백 |
| 분석 이벤트 | 아래 표의 7종 `snake_case` 이벤트 — `05-metrics.md` §4와 100% 동일 |

| 이벤트 이름 | 발생 시점 | 속성 |
|---|---|---|
| `workbench_entered` | 워크벤치 진입 및 연구자 ID 해시 할당 시 | `user_id`, `variant` |
| `manifest_uploaded` | Casava 1.8 매니페스트 검증 실행 시 | `sample_count`, `is_valid` |
| `qc_recommendation_shown` | Pre-flight QC 진단 및 추천 파라미터 카드 노출 시 | `variant`, `experiment_id` |
| `qc_recommendation_accepted` | 추천 파라미터 "수락" 버튼 클릭 시 | `seconds_to_accept`, `decontam_threshold` |
| `qc_recommendation_rejected` | 추천 파라미터 "직접 수정(거절)" 클릭 시 | `reason` |
| `cli_snippet_copied` | 생성된 `run_pipeline.sh` CLI 스니펫 복사 시 | `flags_enabled` |
| `qc_badge_shared` | (MS3) QC 인증 리포트 링크 공유 클릭 시 | `cohort_id` |

## 4. 우선순위 (MoSCoW)

| 등급 | 항목 |
|---|---|
| Must | Casava 매니페스트 검증기(FR1), Pre-flight QC 추천 카드(FR2, FR3→FR4), 수락/거절 액션(FR5), 결정론적 세션/Variant 할당(FR6), 분석 이벤트 7종 — `03` §3 In과 일치 |
| Should | GitHub Pages 무중단 배포 및 `/health.json` 헬스체크(FR7), 거절 사유 선택 옵션 |
| Could | QC 인증 배지 및 마크다운 리포트 공유(MS3 예정), 교육용 프리셋 3종 버튼(MS2 예정) |
| Won't (이번 범위) | 원시 FASTQ 클라우드 업로드·서버 DADA2 실행, 600 DPI TIFF 렌더러, SampleSheet 변환기, 다중 배치 공변량 UI — `03` §3 Out과 일치 |
