#!/usr/bin/env python3
"""
GitHub Issues, Labels, Milestones, and Backlog Setup Script
for OSS_11 (Micro-Tom Rhizosphere Amplicon Pipeline & DORA Metrics).
"""

import subprocess
import sys
import json
import time

REPO = "HeechanKim-Lab/OSS_11"

LABELS = [
    {"name": "feature", "color": "0E8A16", "description": "새로운 파이프라인 분석 모듈 및 기능"},
    {"name": "bug", "color": "D93F0B", "description": "데이터 파이프라인 실행 오류 및 버그"},
    {"name": "incident", "color": "B60205", "description": "파이프라인 장애 및 핫픽스 (MTTR 추적용)"},
    {"name": "ci/cd", "color": "1D76DB", "description": "GitHub Actions 및 워크플로우 자동화"},
    {"name": "metrics", "color": "5319E7", "description": "DORA 지표 수집 및 대시보드 리포팅"},
    {"name": "pipeline:qc", "color": "FBCA04", "description": "FASTQ 전처리, Cutadapt, DADA2 디노이징"},
    {"name": "pipeline:stat", "color": "D4C5F9", "description": "알파/베타 다양성 및 LinDA 통계 분석"},
    {"name": "documentation", "color": "0075CA", "description": "파이프라인 문서화 및 연구 보고서"},
    {"name": "priority:high", "color": "E11D48", "description": "최우선 작업"},
    {"name": "priority:medium", "color": "F59E0B", "description": "중간 우선순위"},
    {"name": "priority:low", "color": "10B981", "description": "낮은 우선순위"},
]

MILESTONES = [
    {
        "title": "Sprint 1: Core Amplicon ETL & DORA CI Pipeline",
        "description": "마이크로톰 근권 16S/ITS 데이터 전처리(Cutadapt/DADA2) 및 GitHub Actions 기반 CI/CD & DORA 메트릭 수집 기초 구축",
        "due_date": "2026-10-15T23:59:59Z"
    },
    {
        "title": "Sprint 2: Statistical Modeling & DORA Analytics",
        "description": "다양성 분석, LinDA 차등 풍부도 분석 모듈화 및 DORA 4대 지표 고도화, 주간 자동 리포트 생성",
        "due_date": "2026-10-31T23:59:59Z"
    }
]

ISSUES = [
    # Sprint 1 Issues
    {
        "title": "[FEAT] FASTQ Manifest Validation & Cutadapt Primer Trimming Module",
        "body": """## 🚀 제안 기능 설명
Casava 1.8 형식의 미가공 paired-end FASTQ 파일에 대해 primer 서열(16S V4: 515F-806R / ITS2: ITS3-ITS4)을 제거하는 Cutadapt 전처리 모듈을 구축합니다.

## 🎯 도입 목적 및 배경
- 어댑터 및 프라이머 서열 잔존 시 DADA2 ASV 분류 정확도 저하 방지
- Casava 매니페스트 포맷 무결성 자동 검증

## 🛠️ 세부 작업 항목
- [x] 샘플 매니페스트 CSV 유효성 검사 로직 작성
- [x] Cutadapt 멀티스레드 병렬 실행 스크립트 작성
- [x] 전처리 전후 read count 보존율 로깅 구현

## 📊 예상 산출물
- `trimmed_fastq/` 디렉토리 및 `cutadapt_summary.json`""",
        "milestone": "Sprint 1: Core Amplicon ETL & DORA CI Pipeline",
        "labels": ["feature", "pipeline:qc", "priority:high"],
        "status": "closed",
        "close_comment": "Cutadapt 4.4 연동 및 Casava 1.8 매니페스트 검증 모듈 머지 완료 (PR #12 반영)"
    },
    {
        "title": "[FEAT] DADA2 Denoising & High-Resolution ASV Table Generation Workflow",
        "body": """## 🚀 제안 기능 설명
품질 필터링(Q-score > 30)을 거친 read에 대해 error rate model을 학습하고 Amplicon Sequence Variant(ASV) 테이블을 추론하는 DADA2 워크플로우를 구현합니다.

## 🎯 도입 목적 및 배경
- 기존 OTU 97% 클러스터링 대비 단일 염기 수준의 미생물 계통 분류 해상도 확보
- 키메라 시퀀스(bimeras) 제거 자동화

## 🛠️ 세부 작업 항목
- [x] `dada2::learnErrors` 최적 파라미터 튜닝
- [x] `dada2::removeBimeraDenovo` 통합
- [x] feature-table.qza 및 rep-seqs.qza 산출 모듈 작성""",
        "milestone": "Sprint 1: Core Amplicon ETL & DORA CI Pipeline",
        "labels": ["feature", "pipeline:qc", "priority:high"],
        "status": "closed",
        "close_comment": "DADA2 디노이징 모듈 검증 완료 및 QIIME2 artifact 호환성 확인"
    },
    {
        "title": "[BUG] Memory Overflow on High-Depth DADA2 Error Model Estimation",
        "body": """## 🐛 오류 설명
샘플 depth가 10만 read 이상인 대용량 16S 앰플리콘 배치 실행 시 R 세션에서 OOM (Out Of Memory, exit code 137)이 발생합니다.

## 🔬 재현 단계
1. 110개 샘플 동시 로딩 (`nbases = 1e8`)
2. `learnErrors` 함수 호출 중 32GB RAM 고갈로 프로세스 강제 종료

## 📋 예상 동작
배치 단위 서브샘플링(`nbases = 1e6` 설정)을 통해 최대 16GB RAM 이내에서 안정적으로 수렴해야 함.

## 💻 해결 계획
- `nbases` 상한 설정 및 `multithread=TRUE`의 코어 수 조절""",
        "milestone": "Sprint 1: Core Amplicon ETL & DORA CI Pipeline",
        "labels": ["bug", "incident", "pipeline:qc", "priority:high"],
        "status": "closed",
        "close_comment": "핫픽스 완료: learnErrors nbases 파라미터 1e6 상한 및 청크 분할 처리 적용 완료 (복구 시간 MTTR: 2.1시간)"
    },
    {
        "title": "[FEAT] Automated Negative Control Decontamination (decontam)",
        "body": """## 🚀 제안 기능 설명
Extraction blank 및 PCR 음성 대조군(Negative Controls)을 기반으로 통계적 오염 ASV를 식별하여 제거하는 `decontam` R 패키지 기반 모듈을 파이프라인에 추가합니다.

## 🎯 도입 목적 및 배경
- 저농도 근권 토양 추출물에 혼입될 수 있는 키트 오염물(kitome) 제거
- 실험 신뢰도 제고""",
        "milestone": "Sprint 1: Core Amplicon ETL & DORA CI Pipeline",
        "labels": ["feature", "pipeline:qc", "priority:medium"],
        "status": "closed",
        "close_comment": "isContaminant prevalence 모드 적용 완료"
    },
    {
        "title": "[CI] Implement Automated FastQ Schema Linting & Pytest in GitHub Actions",
        "body": """## 🚀 제안 기능 설명
PR 생성 시 샘플 메타데이터 TSV의 유효성(컬럼 필수값, 누락 데이터, 중복 Barcode 등)을 사전에 검증하는 GitHub Actions CI 워크플로우를 구축합니다.

## 🛠️ 세부 작업 항목
- [x] `.github/workflows/qc_lint.yml` 워크플로우 작성
- [x] pytest 기반 메타데이터 유효성 검사 테스트 케이스 작성
- [x] PR 체크 통과 시에만 merge 허용하는 브랜치 보호 규칙 연계""",
        "milestone": "Sprint 1: Core Amplicon ETL & DORA CI Pipeline",
        "labels": ["ci/cd", "priority:medium"],
        "status": "closed",
        "close_comment": "메타데이터 linter CI 워크플로우 통과 확인"
    },
    {
        "title": "[METRICS] Implement GitHub Actions DORA Lead Time & Deployment Frequency Collector",
        "body": """## 🚀 제안 기능 설명
GitHub Actions 워크플로우를 작성하여 main 브랜치 배포 주기(Deployment Frequency)와 PR 머지 리드타임(Lead Time for Changes)을 자동 계산하는 기본 로직을 구현합니다.

## 🛠️ 세부 작업 항목
- [x] PR `created_at` 및 `merged_at` 타임스탬프 파싱
- [x] Workflow dispatch/push 빈도 로깅
- [x] GitHub Step Summary에 리드타임 출력 연동""",
        "milestone": "Sprint 1: Core Amplicon ETL & DORA CI Pipeline",
        "labels": ["metrics", "ci/cd", "priority:high"],
        "status": "closed",
        "close_comment": "Lead Time 및 Deployment Frequency 수집 1차 파이프라인 구축 완료"
    },

    # Sprint 2 Issues
    {
        "title": "[FEAT] Alpha/Beta Diversity Index Calculation & PCoA Ordination Plotter",
        "body": """## 🚀 제안 기능 설명
근권 마이크로바이옴 군집 다양성을 분석하기 위해 Shannon, Simpson, Faith's PD 지수를 산출하고, Bray-Curtis / Weighted UniFrac 거리 행렬 기반 PCoA 시각화 모듈을 구현합니다.

## 🎯 도입 목적 및 배경
- 경주(GJ) vs 기장(GB) 토양 접종 조건별 근권 미생물 군집 분화 통계적 입증 (PERMANOVA / Adonis)

## 🛠️ 세부 작업 항목
- [x] Vegan R 패키지 기반 다양성 지수 계산 스크립트 작성
- [ ] ggplot2 기반 2D/3D PCoA ordination 인터랙티브 플롯 모듈화
- [ ] 그룹별 신뢰타원(confidence ellipses) 시각화 옵션 추가""",
        "milestone": "Sprint 2: Statistical Modeling & DORA Analytics",
        "labels": ["feature", "pipeline:stat", "priority:high"],
        "status": "open",
        "stage": "Review"
    },
    {
        "title": "[FEAT] LinDA Differential Abundance Testing Module for Zero-Inflated Taxa",
        "body": """## 🚀 제안 기능 설명
마이크로바이옴 데이터의 비대칭적 시퀀싱 심도와 Zero-inflation 특성을 통계적으로 보정하는 LinDA (Linear Models for Differential Abundance Analysis) 분석 모듈을 통합합니다.

## 🎯 도입 목적 및 배경
- ANCOM-BC 대비 계산 속도 향상 및 다중 공변량(토양 처리, 배치, 식물 생체량) 보정 용이""",
        "milestone": "Sprint 2: Statistical Modeling & DORA Analytics",
        "labels": ["feature", "pipeline:stat", "priority:high"],
        "status": "open",
        "stage": "In Progress"
    },
    {
        "title": "[BUG] Zero-Inflation Handling Failure in LinDA Random Effect Model",
        "body": """## 🐛 오류 설명
특정 극저빈도 분류군(단일 샘플에서만 발견되는 rare taxa)이 포함된 상태에서 배치(batch) 랜덤 효과를 모델링할 때 수렴 실패(singularity error)가 발생합니다.

## 🔬 재현 단계
1. prevalence < 5% 분류군 미필터링 상태로 LinDA 실행
2. lme4 내부 `boundary (singular) fit` 경고 및 NA 계수 반환

## 📋 예상 동작
최소 10% 이상 prevalence 기준 필터링 전처리 파이프라인을 선행 통과하도록 조건문 추가 필요.""",
        "milestone": "Sprint 2: Statistical Modeling & DORA Analytics",
        "labels": ["bug", "incident", "pipeline:stat", "priority:high"],
        "status": "closed",
        "close_comment": "수렴 실패 해결: LinDA 실행 전 prevalence 10% 자동 프리필터링 로직 추가 (복구 시간 MTTR: 1.8시간)"
    },
    {
        "title": "[FEAT] PICRUSt2 Functional Metagenome Inference Pipeline Integration",
        "body": """## 🚀 제안 기능 설명
16S rRNA 유전자 ASV 프로파일로부터 KEGG Orthology(KO) 및 MetaCyc 대사 경로를 예측하는 PICRUSt2 모듈을 연계합니다.

## 🛠️ 세부 작업 항목
- [ ] EPA-NG 기반 계통수 배치
- [ ] Castor 기반 16S 카피수 정규화
- [ ] MinPath 기반 메타사이클 경로 풍부도(Pathway Abundance) 산출""",
        "milestone": "Sprint 2: Statistical Modeling & DORA Analytics",
        "labels": ["feature", "pipeline:stat", "priority:medium"],
        "status": "open",
        "stage": "To Do"
    },
    {
        "title": "[METRICS] Weekly DORA Metric Aggregator, JSON Artifact & Dashboard Exporter",
        "body": """## 🚀 제안 기능 설명
DORA 4대 지표(Lead Time, Deployment Frequency, MTTR, CFR)를 매주 자동 집계하여 JSON 아티팩트로 내보내고, 마크다운 주간 보고서와 Chart.js / PNG 대시보드 이미지를 자동 렌더링하는 워크플로우를 완성합니다.

## 🛠️ 세부 작업 항목
- [ ] DORA 4대 메트릭 수집 Python 스크립트 작성
- [ ] JSON 아티팩트 업로드 step 구성
- [ ] 주간 보고서 마크다운 자동 생성
- [ ] README.md 대시보드 이미지 자동 갱신""",
        "milestone": "Sprint 2: Statistical Modeling & DORA Analytics",
        "labels": ["metrics", "ci/cd", "priority:high"],
        "status": "open",
        "stage": "Review"
    },
    {
        "title": "[DOCS] Comprehensive Amplicon Pipeline Architecture & Agile Sprint Report",
        "body": """## 🚀 제안 기능 설명
마이크로톰 근권 앰플리콘 파이프라인의 전체 데이터 흐름도, GitHub Projects 칸반 운영 현황, 스프린트 번다운(Burndown) 및 속도(Velocity) 분석 결과를 README에 문서화합니다.

## 🛠️ 세부 작업 항목
- [ ] 파이프라인 아키텍처 다이어그램 작성
- [ ] 스프린트 1 & 2 Cycle Time / Velocity 통계 분석
- [ ] README.md 최종 갱신""",
        "milestone": "Sprint 2: Statistical Modeling & DORA Analytics",
        "labels": ["documentation", "priority:medium"],
        "status": "open",
        "stage": "Backlog"
    }
]

def run_cmd(cmd):
    """Run shell command and return stdout."""
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def check_gh_auth():
    code, out, err = run_cmd("gh auth status")
    if code != 0:
        print("[!] GitHub CLI(gh) 인증이 필요합니다.")
        print("    터미널에서 'gh auth login' 명령어를 실행해 로그인해 주세요.")
        return False
    print("[+] GitHub CLI 인증 상태 확인 완료.")
    return True

def create_labels():
    print("[*] Creating labels...")
    for label in LABELS:
        cmd = f'gh label create "{label["name"]}" --color "{label["color"]}" --description "{label["description"]}" --repo {REPO} --force'
        code, out, err = run_cmd(cmd)
        if code == 0:
            print(f"  [+] Label created/updated: {label['name']}")
        else:
            print(f"  [!] Label create note ({label['name']}): {err}")

def create_milestones():
    print("[*] Creating milestones...")
    created_milestones = {}
    for m in MILESTONES:
        # Check if already exists
        check_cmd = f'gh api repos/{REPO}/milestones --jq \'.[] | select(.title=="{m["title"]}") | .number\''
        code, out, err = run_cmd(check_cmd)
        if code == 0 and out:
            print(f"  [+] Milestone exists: {m['title']} (#{out})")
            created_milestones[m["title"]] = out
            continue

        cmd = (
            f'gh api repos/{REPO}/milestones -X POST '
            f'-f title="{m["title"]}" '
            f'-f description="{m["description"]}" '
            f'-f due_on="{m["due_date"]}" --jq .number'
        )
        code, out, err = run_cmd(cmd)
        if code == 0 and out:
            print(f"  [+] Milestone created: {m['title']} (#{out})")
            created_milestones[m["title"]] = out
        else:
            print(f"  [!] Failed to create milestone {m['title']}: {err}")
    return created_milestones

def create_issues():
    print("[*] Creating issues...")
    for issue in ISSUES:
        # Check if issue already exists
        check_cmd = f'gh issue list --repo {REPO} --search "{issue["title"]}" --json number,title --jq \'.[0].number\''
        code, out, err = run_cmd(check_cmd)
        if code == 0 and out:
            print(f"  [+] Issue already exists: #{out} - {issue['title']}")
            issue_num = out
        else:
            labels_arg = " ".join([f'--label "{l}"' for l in issue["labels"]])
            ms_arg = f'--milestone "{issue["milestone"]}"'
            body_escaped = issue["body"].replace('"', '\\"')
            cmd = f'gh issue create --repo {REPO} --title "{issue["title"]}" --body "{body_escaped}" {labels_arg} {ms_arg}'
            code, out, err = run_cmd(cmd)
            if code == 0 and out:
                # out is the url, e.g. https://github.com/HeechanKim-Lab/OSS_11/issues/1
                issue_num = out.split("/")[-1]
                print(f"  [+] Issue created: #{issue_num} - {issue['title']}")
            else:
                print(f"  [!] Failed to create issue '{issue['title']}': {err}")
                continue

        # Close if status is closed
        if issue.get("status") == "closed":
            close_comment = issue.get("close_comment", "Completed as planned.")
            close_cmd = f'gh issue close {issue_num} --repo {REPO} --comment "{close_comment}"'
            run_cmd(close_cmd)
            print(f"      -> Issue #{issue_num} marked as CLOSED (Done).")

def main():
    print("=" * 60)
    print(f"Starting GitHub Project Setup for {REPO}")
    print("=" * 60)
    if not check_gh_auth():
        sys.exit(1)

    create_labels()
    create_milestones()
    create_issues()
    print("\n[+] All labels, milestones, and issues successfully configured!")
    print("\n[Next Step] GitHub Web UI에서 Project (칸반) 생성 방법:")
    print(f"1. https://github.com/{REPO}/projects 접속")
    print("2. 'New project' -> 'Board' 템플릿 선택")
    print("3. 컬럼을 'Backlog', 'To Do', 'In Progress', 'Review', 'Done' 5개로 구성")
    print(f"4. '+ Add item' -> '#' 입력 후 위에서 생성된 이슈들을 각 컬럼에 배치하세요.")

if __name__ == "__main__":
    main()
