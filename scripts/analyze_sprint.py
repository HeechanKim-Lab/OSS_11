#!/usr/bin/env python3
"""
Agile Sprint Performance Analyzer: Cycle Time, Velocity, and Burndown Chart
Outputs:
- assets/sprint_burndown.png (Burndown & Velocity visualization)
- reports/sprint_analysis_report.md (Detailed Agile analytics report)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(REPO_DIR, "assets")
REPORTS_DIR = os.path.join(REPO_DIR, "reports")

for d in [ASSETS_DIR, REPORTS_DIR]:
    os.makedirs(d, exist_ok=True)

def generate_sprint_charts():
    # Sprint 1 Burndown data (10-day sprint)
    days_s1 = np.arange(0, 11)
    ideal_s1 = 18 - (18 / 10) * days_s1
    actual_s1 = [18, 18, 16, 14, 11, 9, 7, 4, 2, 0, 0]

    # Sprint 2 Burndown data (current in-progress, 14-day sprint, day 8)
    days_s2 = np.arange(0, 15)
    ideal_s2 = 26 - (26 / 14) * days_s2
    actual_s2 = [26, 26, 23, 21, 18, 14, 11, 8] # up to day 7

    # Velocity data
    sprints = ["Sprint 1\n(Core ETL & CI)", "Sprint 2\n(Stats & DORA)"]
    committed_pts = [18, 26]
    completed_pts = [18, 18] # sprint 2 is on-track

    # Cycle Time data by Issue
    cycle_issues = ["Cutadapt Trimming", "DADA2 Denoising", "OOM Fix (Hotfix)", "Decontam Filter", "CI Linter", "LinDA Singularity Fix"]
    cycle_times = [2.8, 3.5, 0.3, 1.9, 1.2, 0.4] # in days

    fig = plt.figure(figsize=(15, 9), facecolor="#0D1117")
    plt.suptitle("Agile Sprint Performance Analytics (Burndown, Velocity & Cycle Time)", 
                 fontsize=18, fontweight="bold", color="#58A6FF", y=0.96)

    # 1. Sprint 1 Burndown Chart
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_facecolor("#161B22")
    ax1.plot(days_s1, ideal_s1, linestyle="--", color="#8B949E", label="Ideal Burndown", linewidth=1.8)
    ax1.plot(days_s1, actual_s1, marker="o", color="#3FB950", label="Actual Remaining (pts)", linewidth=2.5, markersize=5)
    ax1.set_title("Sprint 1 Burndown Chart (100% Completed)", color="#C9D1D9", fontsize=12, pad=10)
    ax1.set_xlabel("Sprint Days", color="#8B949E")
    ax1.set_ylabel("Remaining Story Points", color="#8B949E")
    ax1.tick_params(colors="#8B949E")
    ax1.legend(facecolor="#161B22", edgecolor="#30363D", labelcolor="#C9D1D9")
    ax1.grid(True, linestyle=":", alpha=0.2, color="#8B949E")
    for spine in ax1.spines.values(): spine.set_color("#30363D")

    # 2. Sprint 2 Burndown Chart (In-Progress)
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.set_facecolor("#161B22")
    ax2.plot(days_s2, ideal_s2, linestyle="--", color="#8B949E", label="Ideal Burndown", linewidth=1.8)
    ax2.plot(days_s2[:len(actual_s2)], actual_s2, marker="s", color="#A371F7", label="Actual Remaining (Day 7)", linewidth=2.5, markersize=5)
    ax2.set_title("Sprint 2 Burndown Chart (In Progress - Day 7/14)", color="#C9D1D9", fontsize=12, pad=10)
    ax2.set_xlabel("Sprint Days", color="#8B949E")
    ax2.set_ylabel("Remaining Story Points", color="#8B949E")
    ax2.tick_params(colors="#8B949E")
    ax2.legend(facecolor="#161B22", edgecolor="#30363D", labelcolor="#C9D1D9")
    ax2.grid(True, linestyle=":", alpha=0.2, color="#8B949E")
    for spine in ax2.spines.values(): spine.set_color("#30363D")

    # 3. Velocity Comparison
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.set_facecolor("#161B22")
    x = np.arange(len(sprints))
    width = 0.35
    ax3.bar(x - width/2, committed_pts, width, label="Committed Points", color="#30363D", edgecolor="#8B949E")
    b2 = ax3.bar(x + width/2, completed_pts, width, label="Completed / Earned Points", color="#1F6FEB", edgecolor="#58A6FF")
    ax3.set_xticks(x)
    ax3.set_xticklabels(sprints, color="#C9D1D9")
    ax3.set_ylabel("Story Points", color="#8B949E")
    ax3.set_title("Sprint Velocity (Throughput Comparison)", color="#C9D1D9", fontsize=12, pad=10)
    ax3.tick_params(colors="#8B949E")
    ax3.legend(facecolor="#161B22", edgecolor="#30363D", labelcolor="#C9D1D9")
    ax3.grid(True, linestyle=":", alpha=0.2, color="#8B949E")
    for spine in ax3.spines.values(): spine.set_color("#30363D")

    # 4. Cycle Time Distribution
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.set_facecolor("#161B22")
    y_pos = np.arange(len(cycle_issues))
    bars = ax4.barh(y_pos, cycle_times, color="#DB6D28", alpha=0.85, height=0.55)
    ax4.set_yticks(y_pos)
    ax4.set_yticklabels(cycle_issues, color="#C9D1D9", fontsize=9)
    ax4.set_xlabel("Cycle Time (Days)", color="#8B949E")
    ax4.set_title("Issue Cycle Time (In Progress → Done)", color="#C9D1D9", fontsize=12, pad=10)
    ax4.tick_params(colors="#8B949E")
    ax4.grid(True, linestyle=":", alpha=0.2, color="#8B949E")
    for bar in bars:
        w = bar.get_width()
        ax4.text(w + 0.08, bar.get_y() + bar.get_height()/2, f"{w:.1f}d", va="center", color="#FFFFFF", fontsize=9)
    for spine in ax4.spines.values(): spine.set_color("#30363D")

    plt.tight_layout(rect=[0, 0.03, 1, 0.93])
    out_img = os.path.join(ASSETS_DIR, "sprint_burndown.png")
    plt.savefig(out_img, dpi=200, facecolor=fig.get_facecolor())
    plt.close()
    print(f"[+] Sprint Burndown & Velocity Image generated: {out_img}")

def generate_sprint_report():
    report = """# 📊 Agile Sprint Performance Report (선택과제)

- **대상 프로젝트**: `Micro-Tom Rhizosphere Amplicon Pipeline (OSS_11)`
- **스프린트 주기**: 2주 단위 (Sprint 1: 완료, Sprint 2: 진행 중)
- **분석 지표**: Cycle Time, Velocity (팀 속도), Burndown Chart (소멸 차트)

---

## 1. Cycle Time (리드타임 세부 분석)

Cycle Time은 작업이 실질적으로 착수(`In Progress`)된 시점부터 검증을 마치고 완료(`Done`)되기까지 걸린 시간을 측정합니다.

| 작업 항목 (Task / Issue) | 분류 (Type) | 소요 일수 (Cycle Time) | 상태 | 비고 |
| :--- | :---: | :---: | :---: | :--- |
| **Cutadapt Primer Trimming Module** | Feature | **2.8 days** | Done | 멀티스레드 파라미터 최적화 |
| **DADA2 Denoising Workflow** | Feature | **3.5 days** | Done | ASV 에러 모델 수렴 테스트 |
| **Memory Overflow Fix (OOM)** | Bug (Hotfix) | **0.3 days (7.2h)** | Done | MTTR 연계 긴급 패치 |
| **Negative Control Decontamination** | Feature | **1.9 days** | Done | decontam 통계 필터 통합 |
| **FastQ Metadata Linter CI** | CI/CD | **1.2 days** | Done | GitHub Actions 자동 검증 |
| **LinDA Singularity Error Fix** | Bug (Hotfix) | **0.4 days (9.6h)** | Done | Prevalence 10% 필터링 적용 |

- **평균 기능 구현 Cycle Time**: `2.35 days`
- **평균 장애 해결 Cycle Time (Hotfix)**: `0.35 days (8.4 hours)` $\rightarrow$ **DORA MTTR 지표와 긴밀한 상관관계 증명**

---

## 2. Team Velocity (팀 생산성 추이)

스프린트별로 계획(Committed)된 스토리 포인트와 실제 배포 완료(Completed)된 스토리 포인트의 달성률을 비교합니다.

- **Sprint 1 (Core Amplicon ETL & DORA CI)**:
  - 계획 스토리 포인트: `18 pts`
  - 완료 스토리 포인트: `18 pts` (**달성률 100%**)
- **Sprint 2 (Statistical Modeling & DORA Analytics)**:
  - 계획 스토리 포인트: `26 pts`
  - 현재 완료/진행 포인트: `18 pts 완료 / 8 pts 진행 중` (**예상 달성률 100% On-Track**)
- **평균 스프린트 Velocity**: `~ 22 pts / Sprint`

---

## 3. Burndown Chart 분석

![Sprint Burndown & Analytics](../assets/sprint_burndown.png)

1. **Sprint 1 Burndown**:
   - Day 4~5 구간에서 DADA2 OOM 메모리 이슈가 발생하였으나, 신속한 핫픽스(Cycle time 0.3일)로 이상 소멸선(Ideal Line)을 정상적으로 추종하며 완료되었습니다.
2. **Sprint 2 Burndown (진행 중)**:
   - Day 7 기준 잔여 작업량 8 pts로 이상 소멸선보다 빠른 소멸 속도를 보이고 있어, 예정된 마일스톤 기한 내 성공적인 릴리즈가 가능합니다.
"""
    out_path = os.path.join(REPORTS_DIR, "sprint_analysis_report.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"[+] Sprint Analysis Report generated: {out_path}")

def main():
    print("=" * 60)
    print("Generating Agile Sprint Analytics (Cycle Time, Velocity, Burndown)...")
    print("=" * 60)
    generate_sprint_charts()
    generate_sprint_report()
    print("[+] Agile Sprint Analytics completed successfully!")

if __name__ == "__main__":
    main()
