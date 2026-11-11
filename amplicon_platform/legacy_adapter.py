"""
Refactored Legacy Code Adapter for OSS_11.
Wraps legacy financial and mathematical utility calculations with type safety,
input validation, and deterministic return structures for regression testing.
"""

from typing import List, Tuple


def compute_compound_interest_legacy(
    principal: float = 24.0, rate: float = 0.06, years: int = 10
) -> List[float]:
    """
    Refactored version of legacy `app.py` compound interest loop.
    Returns yearly accumulated balances while validating inputs.
    """
    if principal <= 0 or years <= 0 or rate < -1.0:
        raise ValueError("Invalid financial parameters for compound growth")

    balances: List[float] = []
    current = float(principal)
    for _ in range(years):
        current = current * (1.0 + rate)
        balances.append(round(current, 6))
    return balances


def evaluate_polynomial_table(max_n: int = 5) -> List[Tuple[int, int, int, int]]:
    """
    Refactored version of legacy `**.py` power table generator.
    Computes (n, n^2, n^3, n^4) for n in 1..max_n.
    """
    if max_n < 1:
        raise ValueError("max_n must be >= 1")
    return [(n, n ** 2, n ** 3, n ** 4) for n in range(1, max_n + 1)]


def greet_workflow_status(service_name: str = "AmpliconSight") -> str:
    """
    Refactored version of `.github/workflows/my.py` status greeting.
    """
    clean_name = service_name.strip() or "AmpliconSight"
    return f"[{clean_name}] Pipeline Status: READY"
