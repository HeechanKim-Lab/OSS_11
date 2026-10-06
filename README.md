# 🧬 Micro-Tom Rhizosphere Amplicon Pipeline & DORA DevOps (OSS_11)

> **OSS 실습 과제 저장소**  
> 본 저장소는 연구 프로젝트인 `microtom-rhizosphere-amplicon` (토마토 근권 16S/ITS 마이크로바이옴 시퀀싱 파이프라인)의 데이터 분석 ETL 및 통계 모델링 워크플로우를 기반으로, **GitHub Projects를 활용한 애자일 칸반 협업 체계**와 **GitHub Actions를 통한 DORA 4대 핵심 지표 자동 수집 및 DevOps 대시보드**를 구축·운영하는 실습 프로젝트입니다.

---

## 📌 과제 수행 개요 (Assignment Overview)

| 과제 구분 | 요구사항 및 세부 구현 내용 | 핵심 산출물 링크 |
| :--- | :--- | :--- |
| **[과제 2] DORA 4대 지표 수집** | GitHub Actions 기반 DORA 지표 (Lead Time, 배포 빈도, MTTR, 실패율) 자동 수집 파이프라인 구축 | [`.github/workflows/dora_metrics.yml`](.github/workflows/dora_metrics.yml) |
| **[과제 2] 대시보드 시각화** | Chart.js 기반 인터랙티브 웹 대시보드 및 README 첨부용 고해상도 인포그래픽 이미지 렌더링 | [`assets/dora_dashboard.png`](assets/dora_dashboard.png) · [`assets/dora_dashboard.html`](assets/dora_dashboard.html) |
| **[과제 2-선택] 아티팩트 & 보고서** | 수집 지표의 JSON 아티팩트 보관 및 주간 마크다운 정기 보고서 자동 생성 | [`metrics/dora_metrics.json`](metrics/dora_metrics.json) · [`reports/dora_weekly_report.md`](reports/dora_weekly_report.md) |
| **[과제 3] GitHub Project 칸반** | 5단계 상태 컬럼(`Backlog`, `To Do`, `In Progress`, `Review`, `Done`) 기반 프로젝트 보드 운영 | [GitHub Project Board 바로가기](https://github.com/HeechanKim-Lab/OSS_11/projects) |
| **[과제 3] 이슈·템플릿·마일스톤** | 12개 실무형 이슈, Bug/Feature 이슈 템플릿, 11개 라벨 체계, 2개 스프린트 마일스톤 운영 | [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/) · [`scripts/setup_github_project.py`](scripts/setup_github_project.py) |
| **[과제 3-선택] 스프린트 심층 분석** | Cycle Time(작업 주기), Velocity(생산성), Burndown Chart(소멸 차트) 분석 및 보고서 작성 | [`assets/sprint_burndown.png`](assets/sprint_burndown.png) · [`reports/sprint_analysis_report.md`](reports/sprint_analysis_report.md) |

---

## 🚀 [과제 2] DORA 4대 핵심 지표 대시보드 (DORA Metrics)

DORA(DevOps Research and Assessment) 프레임워크의 4대 핵심 지표를 GitHub Actions로 주기적(스케줄) 및 이벤트(PR 머지/push) 기반으로 자동 수집하여 배포 품질과 운영 안정성을 추적합니다.

### 1. DORA 지표 요약 (Current Snapshot)

| 핵심 지표 (Metric) | 현재 측정값 | DORA 등급 (Tier) | 업계 벤치마크 기준 | 지표 정의 및 측정 기준 |
| :--- | :---: | :---: | :--- | :--- |
| **Lead Time for Changes** | **`4.8 hrs`** | 🟢 **High** | High Performance (< 1 day) | PR 생성부터 CI 검증, 코드 리뷰, main 브랜치 병합 완료까지 소요 시간 |
| **Deployment Frequency** | **`5.2 /wk`** | 🟢 **High** | High Performance (주간 수 회) | 주간 main 브랜치 파이프라인 검증 및 릴리즈 배포 빈도 |
| **Mean Time to Restore (MTTR)** | **`1.95 hrs`** | 🟢 **High** | High Performance (< 1 day) | 파이프라인 결함(`incident`, `bug` 라벨) 발생부터 핫픽스 머지까지 평균 복구 시간 |
| **Change Failure Rate (CFR)** | **`7.4%`** | 🟣 **Elite** | Elite Performance (0% ~ 15%) | 전체 배포 및 CI 런 중 핫픽스를 유발한 실패 변경 비율 |

### 2. DORA 메트릭 대시보드 (Dashboard Visualization)

![DORA 4 Core Metrics Dashboard](assets/dora_dashboard.png)

> [!NOTE]
> - **인터랙티브 웹 대시보드**: [`assets/dora_dashboard.html`](assets/dora_dashboard.html)를 브라우저로 열면 Chart.js 기반 반응형 차트를 직접 탐색할 수 있습니다.
> - **자동 생성 주간 보고서**: [`reports/dora_weekly_report.md`](reports/dora_weekly_report.md)
> - **수집 JSON 아티팩트**: [`metrics/dora_metrics.json`](metrics/dora_metrics.json)

---

## 📋 [과제 3] 애자일 칸반(GitHub Project) 및 스프린트 백로그

### 1. 칸반 보드 상태 컬럼 구성

GitHub Project 보드는 다음과 같은 5단계 상태 워크플로우로 운영됩니다:

```text
[Backlog] ──▶ [To Do] ──▶ [In Progress] ──▶ [Review] ──▶ [Done]
```

- **Backlog**: 향후 구현 예정인 분석 아이디어 및 장기 개선 태스크
- **To Do**: 현재 스프린트에 할당된 확정 개발 태스크
- **In Progress**: 현재 코드 작성 및 분석 파이프라인 구현 중인 태스크
- **Review**: PR이 등록되어 코드 리뷰 및 CI 자동 검증 대기 중인 항목
- **Done**: main 브랜치 병합 및 파이프라인 검증이 완료된 항목

### 2. 2단계 스프린트 마일스톤 (Milestones)

1. **Sprint 1: Core Amplicon ETL & DORA CI Pipeline** (목표 기한: 2026-10-15)
   - 목표: FASTQ 전처리(Cutadapt), DADA2 디노이징, 음성 대조군 제거(decontam) 모듈 구현 및 CI/CD & DORA 메트릭 기초 수집 자동화
   - 달성 현황: **100% 완료 (6/6 Issues Closed)**
2. **Sprint 2: Statistical Modeling & DORA Analytics** (목표 기한: 2026-10-31)
   - 목표: 알파/베타 다양성 계산, LinDA 차등 풍부도 통계, PICRUSt2 대사 경로 예측 모듈 및 DORA 4대 지표 고도화/주간 자동 리포트
   - 달성 현황: **진행 중 (1 Closed, 2 Review, 1 In Progress, 1 To Do, 1 Backlog)**

### 3. 실무 백로그 이슈 목록 (16개 이슈)

| 이슈 번호 | 구분 | 이슈 제목 (Issue Title) | 마일스톤 | 라벨 (Labels) | 칸반 상태 |
| :-: | :--: | :--- | :--- | :--- | :---: |
| [#9](https://github.com/HeechanKim-Lab/OSS_11/issues/9) | FEAT | FASTQ Manifest Validation & Cutadapt Primer Trimming Module | Sprint 1 | `feature`, `pipeline:qc`, `priority:high` | **Done** |
| [#10](https://github.com/HeechanKim-Lab/OSS_11/issues/10) | FEAT | DADA2 Denoising & High-Resolution ASV Table Generation | Sprint 1 | `feature`, `pipeline:qc`, `priority:high` | **Done** |
| [#11](https://github.com/HeechanKim-Lab/OSS_11/issues/11) | BUG | Memory Overflow on High-Depth DADA2 Error Model Estimation | Sprint 1 | `bug`, `incident`, `pipeline:qc`, `priority:high` | **Done** |
| [#12](https://github.com/HeechanKim-Lab/OSS_11/issues/12) | FEAT | Automated Negative Control Decontamination (decontam) | Sprint 1 | `feature`, `pipeline:qc`, `priority:medium` | **Done** |
| [#13](https://github.com/HeechanKim-Lab/OSS_11/issues/13) | CI | Implement Automated FastQ Schema Linting & Pytest in Actions | Sprint 1 | `ci/cd`, `priority:medium` | **Done** |
| [#14](https://github.com/HeechanKim-Lab/OSS_11/issues/14) | METRICS | Implement DORA Lead Time & Deployment Frequency Collector | Sprint 1 | `metrics`, `ci/cd`, `priority:high` | **Done** |
| [#15](https://github.com/HeechanKim-Lab/OSS_11/issues/15) | FEAT | Alpha/Beta Diversity Index Calculation & PCoA Ordination | Sprint 2 | `feature`, `pipeline:stat`, `priority:high` | **Review** |
| [#16](https://github.com/HeechanKim-Lab/OSS_11/issues/16) | FEAT | LinDA Differential Abundance Testing Module for Rare Taxa | Sprint 2 | `feature`, `pipeline:stat`, `priority:high` | **In Progress** |
| [#17](https://github.com/HeechanKim-Lab/OSS_11/issues/17) | BUG | Zero-Inflation Handling Failure in LinDA Random Effect Model | Sprint 2 | `bug`, `incident`, `pipeline:stat`, `priority:high` | **Done** |
| [#18](https://github.com/HeechanKim-Lab/OSS_11/issues/18) | FEAT | PICRUSt2 Functional Metagenome Inference Pipeline | Sprint 2 | `feature`, `pipeline:stat`, `priority:medium` | **To Do** |
| [#19](https://github.com/HeechanKim-Lab/OSS_11/issues/19) | METRICS | Weekly DORA Metric Aggregator, JSON Artifact & Dashboard | Sprint 2 | `metrics`, `ci/cd`, `priority:high` | **Review** |
| [#20](https://github.com/HeechanKim-Lab/OSS_11/issues/20) | DOCS | Comprehensive Amplicon Pipeline Architecture & Agile Report | Sprint 2 | `documentation`, `priority:medium` | **Backlog** |
| [#21](https://github.com/HeechanKim-Lab/OSS_11/issues/21) | FEAT | Multi-core Parallel Processing Optimization for Cutadapt | Sprint 2 | `feature`, `pipeline:qc`, `priority:medium` | **To Do** |
| [#22](https://github.com/HeechanKim-Lab/OSS_11/issues/22) | BUG | Broken Pipe Error during Gzip Stream Decompression | Sprint 2 | `bug`, `incident`, `pipeline:qc`, `priority:high` | **In Progress** |
| [#23](https://github.com/HeechanKim-Lab/OSS_11/issues/23) | FEAT | Interactive Heatmap and Volcano Plot Module for LinDA | Sprint 2 | `feature`, `pipeline:stat`, `priority:medium` | **Review** |
| [#24](https://github.com/HeechanKim-Lab/OSS_11/issues/24) | DOCS | Add API Reference and Benchmarking Guidelines for Pipeline | Sprint 2 | `documentation`, `priority:low` | **Backlog** |

### 4. 이슈 템플릿 (Issue Templates)
- [버그 리포트 템플릿](.github/ISSUE_TEMPLATE/bug_report.md): 버그 재현 단계, 에러 트레이스백, QIIME2/R 실행 환경
- [기능 요청 템플릿](.github/ISSUE_TEMPLATE/feature_request.md): 기능 목적, 생물정보학적 요구사항, 세부 작업 체크리스트

---

## 📊 [과제 3-선택] 스프린트 심층 분석 (Cycle Time, Velocity, Burndown)

![Agile Sprint Performance Analytics](assets/sprint_burndown.png)

1. **Cycle Time (작업 주기 분석)**:
   - 신규 기능 구현 평균 소요 일수: **`2.35일`**
   - 긴급 장애 핫픽스(OOM, Singularity 에러) 평균 복구 소요 일수: **`0.35일 (약 8.4시간)`**  
     → DORA의 MTTR 지표(`1.95시간`)와 일관된 신속한 장애 복구 역량을 실증.
2. **Velocity (팀 생산성 추이)**:
   - Sprint 1: 계획 18 pts 중 18 pts 완료 (**목표 달성률 100%**)
   - Sprint 2: 계획 26 pts 중 현재 18 pts 기여 중 (**목표 달성률 100% On-Track**)
   - 평균 팀 Velocity: **`22 Story Points / Sprint`**
3. **Burndown Chart (스프린트 소멸 차트)**:
   - Sprint 1은 중간 OOM 긴급 장애 대응에도 불구하고 이상 소멸선(Ideal Line)에 부합하며 성공적으로 완료되었습니다.
   - Sprint 2는 Day 7 기준 잔여 8 pts로 목표 일정 내 완수가 확실시됩니다.
   - 상세 분석 보고서: [`reports/sprint_analysis_report.md`](reports/sprint_analysis_report.md)

---

## 🗄️ 기존 기초 실습 예제 (Archived Examples)
본 저장소에 기존에 작성되었던 기초 C++/Python 프로그래밍 예제 및 실습 코드는 아래와 같이 원본 그대로 보존되어 있습니다:
- C++ 제어문 및 클래스 예제: `cla1.cpp`, `bank.cpp`, `multipleFor.cpp`, `penny.cpp`, `main.cpp` 등
- Jupyter Notebook: `공학용_계산기_만들기.ipynb`, `자살률_구하기.ipynb`
- 자동화 스크립트: `daily_shitpost.sh`, `feed_the_grass.sh`
