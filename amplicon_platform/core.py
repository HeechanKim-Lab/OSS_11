"""
Core Microbiome Amplicon Analysis Engine (TDD Green Implementation).
Implements 5 core functions derived from the Micro-Tom Rhizosphere Amplicon Pipeline:
1. validate_fastq_manifest
2. calculate_trimming_yield
3. identify_contaminant_asvs
4. compute_diversity_indices
5. run_linda_differential_test
"""

import math
from typing import Dict, List, Any


def validate_fastq_manifest(manifest_records: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Validates Casava 1.8 paired-end FASTQ manifest records.
    Checks sample_id uniqueness, non-empty fields, and _R1_ / _R2_ filename pairing.
    """
    errors: List[str] = []
    seen_ids = set()
    valid_count = 0

    for idx, rec in enumerate(manifest_records):
        sample_id = str(rec.get("sample_id", "")).strip()
        fwd = str(rec.get("forward_fastq", "")).strip()
        rev = str(rec.get("reverse_fastq", "")).strip()

        row_errors = []
        if not sample_id:
            row_errors.append(f"Row {idx}: Missing sample_id")
        elif sample_id in seen_ids:
            row_errors.append(f"Row {idx}: Duplicate sample_id '{sample_id}'")
        else:
            seen_ids.add(sample_id)

        if not fwd.endswith(".fastq.gz") or "_R1_" not in fwd:
            row_errors.append(f"Row {idx} ({sample_id}): Invalid forward_fastq '{fwd}'")

        if not rev.endswith(".fastq.gz") or "_R2_" not in rev:
            row_errors.append(f"Row {idx} ({sample_id}): Invalid reverse_fastq '{rev}'")

        if row_errors:
            errors.extend(row_errors)
        else:
            valid_count += 1

    return {
        "is_valid": len(errors) == 0 and len(manifest_records) > 0,
        "total_records": len(manifest_records),
        "valid_count": valid_count,
        "errors": errors,
    }


def calculate_trimming_yield(
    raw_reads: int,
    trimmed_reads: int,
    avg_length: float,
    min_retention: float = 0.70,
    min_length: float = 180.0,
) -> Dict[str, Any]:
    """
    Calculates Cutadapt primer trimming retention yield and assigns QC status.
    """
    if raw_reads <= 0:
        raise ValueError("raw_reads must be strictly positive")
    if trimmed_reads < 0 or trimmed_reads > raw_reads:
        raise ValueError("trimmed_reads must be between 0 and raw_reads")

    retention_rate = round(trimmed_reads / float(raw_reads), 4)

    if avg_length < min_length:
        qc_status = "FAIL_SHORT_READS"
    elif retention_rate < min_retention:
        qc_status = "WARN_LOW_YIELD"
    else:
        qc_status = "PASS"

    return {
        "raw_reads": raw_reads,
        "trimmed_reads": trimmed_reads,
        "retention_rate": retention_rate,
        "avg_length": avg_length,
        "qc_status": qc_status,
    }


def identify_contaminant_asvs(
    sample_counts: Dict[str, List[int]],
    neg_control_counts: Dict[str, List[int]],
    ratio_threshold: float = 1.0,
) -> Dict[str, Any]:
    """
    Identifies kitome/reagent contaminant ASVs by comparing mean abundance in
    negative controls against biological samples (decontam prevalence/frequency model).
    """
    contaminants: List[str] = []
    clean_asvs: List[str] = []
    contamination_scores: Dict[str, float] = {}

    for asv_id, s_vals in sample_counts.items():
        neg_vals = neg_control_counts.get(asv_id, [0])
        mean_sample = sum(s_vals) / max(len(s_vals), 1)
        mean_neg = sum(neg_vals) / max(len(neg_vals), 1)

        ratio = mean_neg / (mean_sample + 1e-6)
        contamination_scores[asv_id] = round(ratio, 4)

        if ratio >= ratio_threshold:
            contaminants.append(asv_id)
        else:
            clean_asvs.append(asv_id)

    return {
        "contaminants": sorted(contaminants),
        "clean_asvs": sorted(clean_asvs),
        "scores": contamination_scores,
    }


def compute_diversity_indices(abundances: List[int]) -> Dict[str, float]:
    """
    Computes Alpha Diversity indices: Richness (Observed ASVs), Shannon (H'),
    Simpson (1 - D), and Pielou's Evenness (J').
    """
    if any(x < 0 for x in abundances):
        raise ValueError("Abundance values cannot be negative")

    positive = [float(x) for x in abundances if x > 0]
    total = sum(positive)
    richness = len(positive)

    if richness == 0 or total <= 0:
        return {
            "richness": 0,
            "shannon": 0.0,
            "simpson": 0.0,
            "evenness": 0.0,
        }

    proportions = [x / total for x in positive]
    shannon = -sum(p * math.log(p) for p in proportions)
    simpson = 1.0 - sum(p * p for p in proportions)
    evenness = shannon / math.log(richness) if richness > 1 else 1.0

    return {
        "richness": richness,
        "shannon": round(shannon, 4),
        "simpson": round(simpson, 4),
        "evenness": round(evenness, 4),
    }


def run_linda_differential_test(
    feature_matrix: Dict[str, List[int]],
    group_labels: List[str],
    min_prevalence: float = 0.10,
    pseudocount: float = 0.5,
) -> Dict[str, Any]:
    """
    Performs zero-inflated prevalence pre-filtering (preventing lme4 singularity)
    and computes bias-corrected Log2 Fold Change between control and treatment cohorts.
    """
    if not group_labels or len(set(group_labels)) < 2:
        raise ValueError("At least two distinct groups are required for differential testing")

    n_samples = len(group_labels)
    unique_groups = sorted(list(set(group_labels)))
    ref_group, treat_group = unique_groups[0], unique_groups[1]

    filtered_out_rare: List[str] = []
    results: Dict[str, Dict[str, Any]] = {}

    for asv_id, counts in feature_matrix.items():
        if len(counts) != n_samples:
            raise ValueError(f"Count length mismatch for {asv_id}")

        non_zero = sum(1 for c in counts if c > 0)
        prevalence = non_zero / float(n_samples)

        if prevalence < min_prevalence:
            filtered_out_rare.append(asv_id)
            continue

        ref_vals = [c + pseudocount for c, g in zip(counts, group_labels) if g == ref_group]
        treat_vals = [c + pseudocount for c, g in zip(counts, group_labels) if g == treat_group]

        mean_ref = sum(ref_vals) / max(len(ref_vals), 1)
        mean_treat = sum(treat_vals) / max(len(treat_vals), 1)

        log2_fc = math.log2(mean_treat / mean_ref)
        significant = abs(log2_fc) >= 1.0

        results[asv_id] = {
            "prevalence": round(prevalence, 4),
            "mean_ref": round(mean_ref, 2),
            "mean_treat": round(mean_treat, 2),
            "log2_fc": round(log2_fc, 4),
            "significant": significant,
        }

    return {
        "total_asvs": len(feature_matrix),
        "ref_group": ref_group,
        "treat_group": treat_group,
        "filtered_out_rare": sorted(filtered_out_rare),
        "results": results,
    }
