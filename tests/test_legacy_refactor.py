"""
[과제 9 - 선택과제] Legacy Code Characterization & Refactoring Stability Tests.
Verifies backward compatibility and refactored behavior of legacy scripts in OSS_11.
"""

import unittest
from amplicon_platform.legacy_adapter import (
    compute_compound_interest_legacy,
    evaluate_polynomial_table,
    greet_workflow_status,
)


class TestLegacyRefactorStability(unittest.TestCase):
    """Ensures refactored legacy code preserves exact mathematical outputs."""

    def test_compound_interest_legacy_parity(self):
        # Legacy app.py calculated 10 years of compound growth from principal=24, rate=0.06
        history = compute_compound_interest_legacy(principal=24.0, rate=0.06, years=10)
        self.assertEqual(len(history), 10)
        self.assertAlmostEqual(history[0], 24.0 * 1.06, places=4)
        self.assertAlmostEqual(history[-1], 24.0 * (1.06 ** 10), places=4)

    def test_compound_interest_invalid_params(self):
        with self.assertRaises(ValueError):
            compute_compound_interest_legacy(principal=-10.0, rate=0.05, years=5)

    def test_evaluate_polynomial_table(self):
        # Legacy **.py calculated n, n**2, n**3, n**4 table for 1..5
        rows = evaluate_polynomial_table(max_n=5)
        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[0], (1, 1, 1, 1))
        self.assertEqual(rows[4], (5, 25, 125, 625))

    def test_greet_workflow_status(self):
        msg = greet_workflow_status("AmpliconSight")
        self.assertIn("AmpliconSight", msg)
        self.assertIn("READY", msg)


if __name__ == "__main__":
    unittest.main()
