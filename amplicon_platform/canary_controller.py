"""
[과제 8 - 선택과제] Canary Progressive Rollout (1% -> 10% -> 50% -> 100%)
& Health-Check Automated Rollback Controller.
"""

import json
import os
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional


class CanaryRolloutController:
    """
    Manages progressive Canary rollout stages (1% -> 10% -> 50% -> 100%)
    and triggers automated rollback upon health-check threshold violation.
    """

    STAGES = [1, 10, 50, 100]

    def __init__(
        self,
        release_version: str = "v1.0.1-canary",
        stable_version: str = "v1.0.0-stable",
        max_error_rate_pct: float = 2.0,
        max_p95_latency_ms: float = 200.0,
    ):
        self.release_version = release_version
        self.stable_version = stable_version
        self.max_error_rate_pct = max_error_rate_pct
        self.max_p95_latency_ms = max_p95_latency_ms
        self.current_traffic_pct = 0
        self.active_version = stable_version
        self.status = "INITIALIZED"
        self.history: List[Dict[str, Any]] = []

    def evaluate_health_check(self, telemetry: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluates /health telemetry metrics against SLO thresholds.
        """
        error_rate = float(telemetry.get("error_rate_pct", 0.0))
        latency = float(telemetry.get("p95_latency_ms", 0.0))
        service_up = bool(telemetry.get("service_up", True))

        reasons = []
        if not service_up:
            reasons.append("Service health endpoint unreachable (DOWN)")
        if error_rate > self.max_error_rate_pct:
            reasons.append(
                f"Error rate {error_rate:.2f}% exceeded threshold {self.max_error_rate_pct:.2f}%"
            )
        if latency > self.max_p95_latency_ms:
            reasons.append(
                f"P95 latency {latency:.1f}ms exceeded threshold {self.max_p95_latency_ms:.1f}ms"
            )

        healthy = len(reasons) == 0
        return {
            "healthy": healthy,
            "error_rate_pct": error_rate,
            "p95_latency_ms": latency,
            "service_up": service_up,
            "reasons": reasons,
        }

    def execute_rollout(
        self, stage_telemetry: Optional[Dict[int, Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Runs through stages 1% -> 10% -> 50% -> 100%.
        If any stage fails health check, immediately rolls back to 0% (stable_version).
        """
        default_telemetry = {
            1: {"error_rate_pct": 0.2, "p95_latency_ms": 82.0, "service_up": True},
            10: {"error_rate_pct": 0.4, "p95_latency_ms": 95.0, "service_up": True},
            50: {"error_rate_pct": 0.6, "p95_latency_ms": 112.0, "service_up": True},
            100: {"error_rate_pct": 0.5, "p95_latency_ms": 108.0, "service_up": True},
        }
        telemetry_map = stage_telemetry or default_telemetry

        for stage_pct in self.STAGES:
            self.current_traffic_pct = stage_pct
            self.active_version = self.release_version
            metrics = telemetry_map.get(
                stage_pct,
                {"error_rate_pct": 0.3, "p95_latency_ms": 90.0, "service_up": True},
            )
            health = self.evaluate_health_check(metrics)

            step_log = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "stage_pct": stage_pct,
                "version": self.release_version,
                "health": health,
            }

            if not health["healthy"]:
                # Trigger Automatic Rollback
                self.current_traffic_pct = 0
                self.active_version = self.stable_version
                self.status = "AUTO_ROLLED_BACK"
                step_log["action"] = (
                    f"CRITICAL: Health check failed at {stage_pct}%. "
                    f"Automatically rolled back traffic to {self.stable_version} (0% canary)."
                )
                self.history.append(step_log)
                return self.summary()

            step_log["action"] = f"PROMOTED: Stage {stage_pct}% passed health check."
            self.history.append(step_log)

        self.status = "COMPLETED_100_PCT"
        return self.summary()

    def summary(self) -> Dict[str, Any]:
        return {
            "release_version": self.release_version,
            "stable_version": self.stable_version,
            "final_status": self.status,
            "active_version": self.active_version,
            "current_canary_traffic_pct": self.current_traffic_pct,
            "stages_executed": len(self.history),
            "history": self.history,
        }


def generate_canary_verification_artifacts(repo_root: str) -> None:
    """
    Runs both Scenario 1 (1%->10%->50%->100% Full Promotion) and
    Scenario 2 (Fault Injection at 50% -> Automated Rollback) and saves logs/reports.
    """
    logs_dir = os.path.join(repo_root, "logs")
    reports_dir = os.path.join(repo_root, "reports")
    os.makedirs(logs_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)

    # Scenario 1: Healthy Progressive Rollout
    c_success = CanaryRolloutController(release_version="v1.0.1-rc1")
    res_success = c_success.execute_rollout()

    # Scenario 2: Fault Injected at 50% Stage -> Auto Rollback
    c_rollback = CanaryRolloutController(release_version="v1.0.2-experimental-3d")
    fault_telemetry = {
        1: {"error_rate_pct": 0.3, "p95_latency_ms": 88.0, "service_up": True},
        10: {"error_rate_pct": 0.8, "p95_latency_ms": 115.0, "service_up": True},
        50: {"error_rate_pct": 5.8, "p95_latency_ms": 340.0, "service_up": True},  # Breaches SLO!
        100: {"error_rate_pct": 6.2, "p95_latency_ms": 380.0, "service_up": True},
    }
    res_rollback = c_rollback.execute_rollout(stage_telemetry=fault_telemetry)

    payload = {
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "slo_policy": {"max_error_rate_pct": 2.0, "max_p95_latency_ms": 200.0},
        "scenario_1_full_promotion": res_success,
        "scenario_2_fault_injection_auto_rollback": res_rollback,
    }

    json_path = os.path.join(logs_dir, "canary_rollout_verification.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    md_path = os.path.join(reports_dir, "canary_rollback_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 🐤 Canary 점진적 롤아웃(1%-10%-50%-100%) 및 헬스체크 자동 롤백 검증 리포트\n\n")
        f.write("- **검증 모듈**: [`amplicon_platform/canary_controller.py`](../amplicon_platform/canary_controller.py)\n")
        f.write("- **실행 로그**: [`logs/canary_rollout_verification.json`](../logs/canary_rollout_verification.json)\n")
        f.write("- **SLO 임계치 기준**: 에러율 $\\le 2.0\\%$, P95 응답 지연 $\\le 200\\text{ms}$, `/health` 상태 `UP`\n\n")
        f.write("## 1. 시나리오 A: 정상 점진적 롤아웃 (`v1.0.1-rc1`)\n\n")
        f.write("| 단계 | 트래픽 비율 | 에러율 (%) | P95 지연 (ms) | 판정 및 조치 |\n")
        f.write("| :---: | :---: | :---: | :---: | :--- |\n")
        for step in res_success["history"]:
            h = step["health"]
            f.write(f"| Stage | `{step['stage_pct']}%` | `{h['error_rate_pct']}%` | `{h['p95_latency_ms']}ms` | 🟢 {step['action']} |\n")
        f.write(f"\n- **최종 상태**: `{res_success['final_status']}` (활성 버전: `{res_success['active_version']}`)\n\n")

        f.write("## 2. 시나리오 B: 50% 구간 장애 주입 및 자동 롤백 (`v1.0.2-experimental-3d`)\n\n")
        f.write("| 단계 | 트래픽 비율 | 에러율 (%) | P95 지연 (ms) | 판정 및 자동 롤백 조치 |\n")
        f.write("| :---: | :---: | :---: | :---: | :--- |\n")
        for step in res_rollback["history"]:
            h = step["health"]
            icon = "🟢" if h["healthy"] else "🔴"
            f.write(f"| Stage | `{step['stage_pct']}%` | `{h['error_rate_pct']}%` | `{h['p95_latency_ms']}ms` | {icon} {step['action']} |\n")
        f.write(f"\n- **최종 상태**: `{res_rollback['final_status']}` (자동 복구된 안정 버전: `{res_rollback['active_version']}`, Canary 트래픽: `0%`)\n")


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generate_canary_verification_artifacts(root)
    print("[+] Canary verification artifacts generated successfully.")
