# 00. 제품 개요

| 제품 | 버전 | 최종 수정 | 관련 가설 |
|---|---|---|---|
| AmpliconSight | 0.2 | 2026-11-12 | 전체 |

> 기본 가정 (사용자 미응답 항목): 없음 — 입력 수집 5문항 모두 답변 (`11-bml-log.md` Cycle 0 참조)
> v0.2 (`Cycle 1` 반영): `MS0` 통과(`M2 = 82.5%`, `M1 = 80.0%`)에 따라 현재 단계를 `MS0` → `MS1 리텐션 검증`으로 전환.

## 1. 한 줄 정의

**16S rRNA 앰플리콘 시퀀싱을 수행하는 대학원생·연구원**이 **매니페스트 포맷 오류와 오염 제거 기준 설정 때문에 수 시간의 파이프라인 재실행 지연을 겪을 때** **AmpliconSight**로 **원시 FASTQ 업로드 없이 3초 만에 Pre-flight QC 진단과 즉시 실행 가능한 파이프라인 명령어를 얻는다.**

## 2. 비전과 현재 단계

- 비전 (3년): 유전체 분석 파이프라인을 돌리기 전 모든 연구실과 시퀀싱 코어 퍼실리티가 표준으로 거치는 **"Zero-Upload Pre-flight QC & Reproducible CLI 게이트웨이"**.
- 현재 단계: **MS1 리텐션 검증 진행 중** (`MS0` 통과 — 추천 수락률 `M2 = 82.5%`, 문제 확인율 `M1 = 80.0%`)
- 이번 PRD 범위: `MS0`~`MS3` (`2026-11-01` ~ `2026-12-26`, 총 8주, 1인 0.50 FTE)
- 출발점: Micro-Tom 토마토 근권 마이크로바이옴 16S 연구 파이프라인(`modules/00`~`13`) 운영 경험 및 다중 페르소나 시나리오 평가(`과제 10`)

## 3. Lean Canvas 요약

| 칸 | 내용 (2줄 이내) | 상세 |
|---|---|---|
| 문제 | ① Casava 1.8 R1/R2 매니페스트 오타로 인한 수 시간 대기 후 실패 ② 음성대조군(NTC) 오염 ASV 제거 기준 모호성 ③ 반복적인 R/CLI 파라미터 수동 수정 피로 | [01](01-problem-and-hypotheses.md) |
| 고객 세그먼트 | 농생명·미생물학 대학원생 및 포닥(얼리어답터: 소속 및 공동연구실 10명). 2차: 시퀀싱 코어 퍼실리티 매니저 | [02](02-target-customer.md) |
| 고유 가치 제안 | 원시 FASTQ 업로드 없이 브라우저에서 3초 만에 매니페스트·오염 기준을 진단하고 한 번에 돌아가는 `run_pipeline.sh` 명령어를 생성한다 | [03](03-solution-and-mvp.md) |
| 솔루션 | Zero-Upload 매니페스트 검증 → Pre-flight QC 추천 카드 → 수락 시 CLI 스니펫 자동 복사 + 3D PCoA 프리뷰 | [03](03-solution-and-mvp.md) |
| 채널 | 연구실 DM·Slack(첫 10명) → 대학원 연합 세미나·실습 단톡방(50명) → QC 인증 리포트 배지 및 코어 퍼실리티 납품 안내문(200명) | [02](02-target-customer.md) |
| 수익 흐름 | MS0~MS3 무료 오픈소스. MS3에서 시퀀싱 코어 퍼실리티·기관용 유료 도입 의향(`M4`, 월 49,000원) 측정만 수행 | [05](05-metrics.md) |
| 비용 구조 | GitHub Pages + GitHub Actions + 로컬 CLI 브리지 구조로 **월 인프라 고정비 0원** (예산 상한 월 2만 원) | [08](08-tech-stack.md) |
| 핵심 지표 | NSM 주간 검증 통과 파이프라인 실행 건수. `M2` 추천 수락률 ≥ 60%, `M3` D14 리텐션 ≥ 50%, `G1` 완료 시간 ≤ 5.0분 | [05](05-metrics.md) |
| 경쟁 우위 | 실제 Micro-Tom 근권 16S 연구(`amplicon_logs/01`~`11`)에서 축적된 저바이오매스 Decontam·LinDA 실전 규칙셋과 Zero-Upload 보안성 | [10](10-risks-and-pivot.md) |

## 4. 문서 맵

| 파일 | 답하는 질문 | 변경 빈도 |
|---|---|---|
| [01-problem-and-hypotheses](01-problem-and-hypotheses.md) | 무엇이 틀리면 제품이 실패하는가? (`H1`~`H4`) | 사이클마다 |
| [02-target-customer](02-target-customer.md) | 당장 이번 주에 만날 첫 10명은 누구인가? | 세그먼트 Pivot(`P2`) 시 |
| [03-solution-and-mvp](03-solution-and-mvp.md) | 가설을 가장 싸게 검증할 최소 제품은? (`In/Out`) | 사이클마다 |
| [04-requirements](04-requirements.md) | 개발자는 무엇을 구현하고 어떤 이벤트를 심는가? (`FR1`~`FR7`) | MVP 범위 변경 시 |
| [05-metrics](05-metrics.md) | 어떤 숫자로 성공과 실패를 판정하는가? (`M1`~`M5`, `G1`~`G2`) | 목표치 보정 시 |
| [06-experiment-plan](06-experiment-plan.md) | 각 가설을 어떤 실험과 임계값으로 검증하는가? (`E1`~`E4`) | 사이클마다 |
| [07-team](07-team.md) | 1인(0.5 FTE) 체제에서 역할을 어떻게 나누고 언제 외주/자문을 쓰는가? | 마일스톤 전환 시 |
| [08-tech-stack](08-tech-stack.md) | 왜 Zero-Upload 정적 웹 + 로컬 CLI 브리지인가? (`ADR-1`, `ADR-2`) | 드묾 (`ADR` 조건 충족 시) |
| [09-milestones](09-milestones.md) | `MS0`~`MS3` 각 검증 게이트의 Go/No-Go 조건은 무엇인가? | 사이클마다 |
| [10-risks-and-pivot](10-risks-and-pivot.md) | 어떤 숫자 트리거(`T1`~`T5`)가 발동하면 어디로 Pivot(`P1`~`P4`)하는가? | Pivot 시 |
| [11-bml-log](11-bml-log.md) | 초기 가정(`Cycle 0`)과 실험에서 무엇을 배웠는가? (`Cycle 1` + `검토 메모`) | 사이클·검토마다 추가 |
