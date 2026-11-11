"""
[과제 8] Feature Flag Management & Deterministic A/B Testing Engine.
Supports:
- 4 Feature Flags controlled via Environment Variables, Target User Allowlists, and Rollout Percentages
- Deterministic SHA-256 user bucketing for A/B Variant assignment (variant_A vs variant_B)
- Structured event tracking logger for conversion and engagement analysis
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from typing import Dict, Any, Optional

DEFAULT_FLAGS: Dict[str, Dict[str, Any]] = {
    "FF_PARALLEL_CUTADAPT": {
        "description": "Enable multi-core pigz/cutadapt parallel primer trimming",
        "default": True,
        "rollout_pct": 100,
        "target_users": ["researcher_01", "admin_lab", "bioinfo_lead"],
    },
    "FF_ADAPTIVE_DECONTAM": {
        "description": "Enable adaptive negative-control prevalence decontamination model",
        "default": True,
        "rollout_pct": 100,
        "target_users": ["researcher_01", "researcher_02"],
    },
    "FF_INTERACTIVE_3D_PCOA": {
        "description": "Enable interactive 3D PCoA ordination & one-click QC banner in Web Workbench",
        "default": False,
        "rollout_pct": 50,
        "target_users": ["beta_tester_01", "admin_lab"],
    },
    "FF_AUTO_PICRUST2_CACHE": {
        "description": "Enable pre-computed KEGG Orthology pathway cache for PICRUSt2",
        "default": False,
        "rollout_pct": 25,
        "target_users": ["admin_lab"],
    },
}


def _compute_bucket(key: str) -> int:
    """Computes a deterministic bucket (0..99) using SHA-256."""
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return int(digest[:8], 16) % 100


def is_flag_enabled(
    flag_name: str,
    user_id: Optional[str] = None,
    custom_registry: Optional[Dict[str, Dict[str, Any]]] = None,
) -> bool:
    """
    Evaluates whether a feature flag is enabled for the current environment/user.
    Priority:
    1. Environment variable override (e.g., FF_PARALLEL_CUTADAPT="true" / "false")
    2. Target user allowlist
    3. Deterministic rollout percentage (if user_id provided)
    4. Flag default boolean
    """
    registry = custom_registry or DEFAULT_FLAGS
    if flag_name not in registry:
        raise KeyError(f"Unknown feature flag: {flag_name}")

    env_val = os.environ.get(flag_name)
    if env_val is not None:
        normalized = env_val.strip().lower()
        if normalized in ("1", "true", "yes", "on"):
            return True
        if normalized in ("0", "false", "no", "off"):
            return False

    cfg = registry[flag_name]
    if user_id:
        if user_id in cfg.get("target_users", []):
            return True
        rollout_pct = int(cfg.get("rollout_pct", 0))
        if 0 < rollout_pct < 100:
            bucket = _compute_bucket(f"{flag_name}:{user_id}")
            return bucket < rollout_pct

    return bool(cfg.get("default", False))


def assign_ab_variant(
    user_id: str, experiment_id: str = "exp_pcoa_workbench_v1"
) -> str:
    """
    Deterministically assigns a user to 'variant_A' (Control: 2D static table)
    or 'variant_B' (Treatment: Interactive 3D PCoA + One-Click QC Summary).
    Guarantees 100% assignment consistency across sessions for the same user_id.
    """
    if not user_id or not user_id.strip():
        raise ValueError("user_id must be a non-empty string")

    bucket = _compute_bucket(f"{experiment_id}:{user_id.strip()}")
    return "variant_B" if bucket < 50 else "variant_A"


def track_ab_event(
    user_id: str,
    event_name: str,
    experiment_id: str = "exp_pcoa_workbench_v1",
    metadata: Optional[Dict[str, Any]] = None,
    log_path: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Records an A/B testing interaction event with consistent variant metadata.
    """
    variant = assign_ab_variant(user_id=user_id, experiment_id=experiment_id)
    event_record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "experiment_id": experiment_id,
        "user_id": user_id,
        "variant": variant,
        "event_name": event_name,
        "flags_snapshot": {
            flag: is_flag_enabled(flag, user_id=user_id) for flag in DEFAULT_FLAGS
        },
        "metadata": metadata or {},
    }

    if log_path:
        os.makedirs(os.path.dirname(os.path.abspath(log_path)), exist_ok=True)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event_record, ensure_ascii=False) + "\n")

    return event_record
