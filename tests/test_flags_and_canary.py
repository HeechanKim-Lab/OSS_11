"""
[과제 8] Unit Tests for Feature Flags, Deterministic A/B Testing, and Canary Auto-Rollback.
"""

import os
import tempfile
import unittest
from amplicon_platform.feature_flags import (
    is_flag_enabled,
    assign_ab_variant,
    track_ab_event,
)
from amplicon_platform.canary_controller import CanaryRolloutController


class TestFeatureFlagsAndCanary(unittest.TestCase):
    """Tests Feature Flags, A/B hashing consistency, and Canary rollback scenarios."""

    def test_feature_flag_defaults_and_target_users(self):
        self.assertTrue(is_flag_enabled("FF_PARALLEL_CUTADAPT"))
        self.assertTrue(is_flag_enabled("FF_ADAPTIVE_DECONTAM"))
        # Target user beta_tester_01 is explicitly in allowlist for FF_INTERACTIVE_3D_PCOA
        self.assertTrue(is_flag_enabled("FF_INTERACTIVE_3D_PCOA", user_id="beta_tester_01"))

    def test_feature_flag_env_override(self):
        os.environ["FF_PARALLEL_CUTADAPT"] = "false"
        try:
            self.assertFalse(is_flag_enabled("FF_PARALLEL_CUTADAPT", user_id="admin_lab"))
        finally:
            del os.environ["FF_PARALLEL_CUTADAPT"]

        os.environ["FF_AUTO_PICRUST2_CACHE"] = "true"
        try:
            self.assertTrue(is_flag_enabled("FF_AUTO_PICRUST2_CACHE"))
        finally:
            del os.environ["FF_AUTO_PICRUST2_CACHE"]

    def test_unknown_flag_raises_key_error(self):
        with self.assertRaises(KeyError):
            is_flag_enabled("FF_NON_EXISTENT_FLAG")

    def test_ab_variant_deterministic_consistency(self):
        # Calling assign_ab_variant 50 times for the same user must return identical variant
        first = assign_ab_variant("user_microbiome_42")
        self.assertIn(first, ("variant_A", "variant_B"))
        for _ in range(50):
            self.assertEqual(assign_ab_variant("user_microbiome_42"), first)

        # Across 100 distinct users, both variant_A and variant_B must be represented
        variants = [assign_ab_variant(f"researcher_{i}") for i in range(100)]
        count_a = variants.count("variant_A")
        count_b = variants.count("variant_B")
        self.assertGreater(count_a, 30)
        self.assertGreater(count_b, 30)

        with self.assertRaises(ValueError):
            assign_ab_variant("   ")

    def test_track_ab_event_writes_jsonl(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = os.path.join(tmpdir, "events.jsonl")
            evt = track_ab_event(
                user_id="researcher_01",
                event_name="qc_completed",
                metadata={"sample_count": 110, "duration_sec": 14.2},
                log_path=log_file,
            )
            self.assertEqual(evt["event_name"], "qc_completed")
            self.assertTrue(os.path.exists(log_file))

    def test_canary_full_promotion_1_10_50_100(self):
        controller = CanaryRolloutController(release_version="v1.0.1")
        summary = controller.execute_rollout()
        self.assertEqual(summary["final_status"], "COMPLETED_100_PCT")
        self.assertEqual(summary["current_canary_traffic_pct"], 100)
        self.assertEqual(summary["stages_executed"], 4)

    def test_canary_auto_rollback_on_health_breach(self):
        controller = CanaryRolloutController(release_version="v1.0.2-bad")
        bad_telemetry = {
            1: {"error_rate_pct": 0.4, "p95_latency_ms": 90.0, "service_up": True},
            10: {"error_rate_pct": 0.9, "p95_latency_ms": 110.0, "service_up": True},
            50: {"error_rate_pct": 4.5, "p95_latency_ms": 280.0, "service_up": True},
            100: {"error_rate_pct": 5.0, "p95_latency_ms": 300.0, "service_up": True},
        }
        summary = controller.execute_rollout(stage_telemetry=bad_telemetry)
        self.assertEqual(summary["final_status"], "AUTO_ROLLED_BACK")
        self.assertEqual(summary["current_canary_traffic_pct"], 0)
        self.assertEqual(summary["active_version"], "v1.0.0-stable")
        self.assertEqual(summary["stages_executed"], 3)  # Stopped at 50%


if __name__ == "__main__":
    unittest.main()
