# 💬 GitHub Discussions 카테고리 설계 및 RFC-001 토론 기록

> **[과제 2 - 선택과제]** GitHub Discussions 카테고리 설계 기준과 실제로 운영된 **RFC(Request for Comments) 형식의 아키텍처 토론** 문서입니다.

---

## 1. GitHub Discussions 카테고리 설계

오픈소스 커뮤니티와 연구자 간 소통을 구조화하기 위해 다음 5개 카테고리를 설계했습니다:

| 아이콘 | 카테고리명 | 형식 (Format) | 목적 및 운영 규칙 |
| :---: | :--- | :---: | :--- |
| 📣 | **Announcements** | Announcement | 신규 버전 릴리즈(v1.0.1), 주간 DORA/SLA 요약 리포트 공지 (메인테이너 전용) |
| 💡 | **RFCs (Architecture & Ideas)** | Open-ended Discussion | 주요 기능 도입 전 `[RFC-번호]` 양식으로 설계안 제안 및 찬반/대안 토론 |
| 🙏 | **Q&A (Pipeline Troubleshooting)** | Question / Answer | QIIME2, DADA2, LinDA 실행 오류 질의응답 (`✅ Mark as Answer` 채택 기능 활성화) |
| 🧪 | **Experiments & BML Results** | Open-ended Discussion | Feature Flag A/B 테스트 결과 및 Lean PRD 가설 검증 데이터 공유 |
| 🙌 | **Show and Tell** | Open-ended Discussion | 본 파이프라인을 활용해 도출한 마이크로바이옴 PCoA 플롯 및 연구 성과 공유 |

---

## 2. 운영된 RFC 토론 전문: `[RFC-001] CLI 중심 앰플리콘 파이프라인의 웹 워크벤치(AmpliconSight) 전환 및 Feature Flag 도입 제안`

- **카테고리**: 💡 RFCs (Architecture & Ideas)
- **작성자**: `@HeechanKim-Lab`
- **작성일**: 2026-10-08
- **상태**: `Accepted & Implemented` (반영 ADR: [ADR-0003](../adr/0003-feature-flag-hash-ab-and-canary-rollback.md))

### 2.1 요약 (Summary)
현재 13개의 Bash/R 스크립트(`modules/00`~`13`)로 구성된 토마토 근권 마이크로바이옴 파이프라인을 비전공 연구자도 브라우저에서 즉시 검증·시각화할 수 있도록 **웹 워크벤치(`AmpliconSight`)** 와 **Python/NPM 통합 패키지**로 확장하고, 실험적 기능들을 **Feature Flag**로 안전하게 제어할 것을 제안합니다.

### 2.2 배경 및 동기 (Motivation)
1. Wet-lab(생물학 실험) 연구원들이 FASTQ 매니페스트 작성 실수(오타, 경로 누락)로 인해 DADA2 단계에서 실패하는 비율이 전체 실행의 38%에 달함.
2. CLI 실행 전에 웹 화면에서 **즉시 매니페스트 검증 + 음성 대조군(Decontam) 프리뷰 + PCoA 시각화**를 제공하면 연구 리드타임을 획기적으로 줄일 수 있음.

### 2.3 상세 설계안 (Detailed Design)
- **Feature Flag 3종 도입**:
  1. `FF_PARALLEL_CUTADAPT`: 멀티코어 트리밍 가속화
  2. `FF_ADAPTIVE_DECONTAM`: AI/통계 기반 적응형 오염 ASV 탐지
  3. `FF_INTERACTIVE_3D_PCOA`: 2D 기본 플롯(Variant A) vs 인터랙티브 3D PCoA + 원클릭 QC 요약 뷰(Variant B) A/B 테스트

### 2.4 커뮤니티/팀 토론 스레드 (Discussion Thread)

> **💬 Reviewer 1 (`@bioinfo-dev`, Ph.D. Candidate)**:  
> `[SHOULD]` 웹 대시보드에서 대용량 FASTQ 원시 파일을 직접 업로드하면 브라우저 메모리가 터질 수 있습니다. 파일 전체 업로드 대신 **메타데이터 TSV와 요약 Count Table(JSON/CSV)만 클라이언트에서 검증**하도록 범위를 제한하는 것이 어떨까요?

> **💬 Author (`@HeechanKim-Lab`)**:  
> 훌륭한 지적입니다! Lean PRD의 MVP In/Out 범위(`docs/prd/03-solution-and-mvp.md`)에 반영하여, 원시 FASTQ 스트리밍은 로컬/컨테이너 CLI가 담당하고 웹 워크벤치는 **매니페스트 스키마 검증, Decontam 시뮬레이션, PCoA/LinDA 인터랙티브 시각화**에 집중하도록 확정하겠습니다.

> **💬 Reviewer 2 (`@devops-lead`, M.S. Student)**:  
> `[MUST]` 3D PCoA 렌더링(`FF_INTERACTIVE_3D_PCOA`)이 저사양 노트북에서 프레임 드랍이나 스크립트 오류를 일으킬 경우에 대비해, Canary 롤아웃(`1% → 10% → 50% → 100%`)과 에러율 2% 초과 시 자동 롤백 메커니즘을 반드시 포함해야 합니다.

> **💬 Author (`@HeechanKim-Lab`)**:  
> 동의합니다. `amplicon_platform/canary_controller.py`에 헬스체크 기반 자동 롤백 로직을 구현하여 CI에서 매 배포마다 검증하도록 조치했습니다.

### 2.5 최종 결정 (Resolution)
- **승인 (Approved)**: 본 RFC-001 안건은 만장일치로 승인되어 Sprint 2 백로그([#21](https://github.com/HeechanKim-Lab/OSS_11/issues/21), [#23](https://github.com/HeechanKim-Lab/OSS_11/issues/23)) 및 Lean PRD에 공식 반영되었습니다.
