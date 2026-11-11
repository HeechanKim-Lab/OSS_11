"""
[과제 9] TDD (Red-Green-Refactor) Unit Tests for 5 Core Amplicon Pipeline Functions.
Covers:
1. validate_fastq_manifest (Casava 1.8 format & paired-end validation)
2. calculate_trimming_yield (Cutadapt primer trimming yield & quality status)
3. identify_contaminant_asvs (Negative control prevalence/ratio decontamination)
4. compute_diversity_indices (Shannon, Simpson, Evenness, Richness)
5. run_linda_differential_test (Prevalence filtering & Log2FC differential abundance)
"""

import unittest
from amplicon_platform.core import (
    validate_fastq_manifest,
    calculate_trimming_yield,
    identify_contaminant_asvs,
    compute_diversity_indices,
    run_linda_differential_test,
)


class TestCoreAmpliconTDD(unittest.TestCase):
    """Unit test suite for the 5 core microbiome pipeline functions."""

    # 1. Feature 1: FASTQ Manifest Validator
    def test_validate_fastq_manifest_valid(self):
        manifest = [
            {
                "sample_id": "GJ_01",
                "forward_fastq": "GJ_01_S1_L001_R1_001.fastq.gz",
                "reverse_fastq": "GJ_01_S1_L001_R2_001.fastq.gz",
                "batch": "B1",
            },
            {
                "sample_id": "GB_02",
                "forward_fastq": "GB_02_S2_L001_R1_001.fastq.gz",
                "reverse_fastq": "GB_02_S2_L001_R2_001.fastq.gz",
                "batch": "B1",
            },
        ]
        res = validate_fastq_manifest(manifest)
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["valid_count"], 2)
        self.assertEqual(len(res["errors"]), 0)

    def test_validate_fastq_manifest_detects_errors(self):
        manifest = [
            {
                "sample_id": "",
                "forward_fastq": "bad_file.txt",
                "reverse_fastq": "GB_02_S2_L001_R2_001.fastq.gz",
            },
            {
                "sample_id": "DUP_01",
                "forward_fastq": "DUP_01_S1_L001_R1_001.fastq.gz",
                "reverse_fastq": "DUP_01_S1_L001_R1_001.fastq.gz",  # Missing _R2_
            },
        ]
        res = validate_fastq_manifest(manifest)
        self.assertFalse(res["is_valid"])
        self.assertGreaterEqual(len(res["errors"]), 2)

    # 2. Feature 2: Cutadapt Primer Trimming Yield Calculator
    def test_calculate_trimming_yield_pass_and_warn(self):
        res_high = calculate_trimming_yield(raw_reads=100000, trimmed_reads=92500, avg_length=245.0)
        self.assertAlmostEqual(res_high["retention_rate"], 0.925, places=3)
        self.assertEqual(res_high["qc_status"], "PASS")

        res_low = calculate_trimming_yield(raw_reads=100000, trimmed_reads=45000, avg_length=210.0)
        self.assertEqual(res_low["qc_status"], "WARN_LOW_YIELD")

        res_short = calculate_trimming_yield(raw_reads=100000, trimmed_reads=90000, avg_length=120.0, min_length=180.0)
        self.assertEqual(res_short["qc_status"], "FAIL_SHORT_READS")

    def test_calculate_trimming_yield_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_trimming_yield(raw_reads=0, trimmed_reads=100, avg_length=200.0)
        with self.assertRaises(ValueError):
            calculate_trimming_yield(raw_reads=100, trimmed_reads=200, avg_length=200.0)

    # 3. Feature 3: Negative Control Decontamination Filter (decontam)
    def test_identify_contaminant_asvs(self):
        sample_counts = {
            "ASV_001": [450, 520, 610, 490],   # Authentic rhizosphere taxon
            "ASV_002": [5, 0, 2, 1],           # Kitome contaminant enriched in blank
            "ASV_003": [120, 140, 95, 110],    # Authentic taxon
        }
        neg_control_counts = {
            "ASV_001": [1, 0],
            "ASV_002": [45, 60],
            "ASV_003": [0, 0],
        }
        result = identify_contaminant_asvs(sample_counts, neg_control_counts, ratio_threshold=1.0)
        self.assertIn("ASV_002", result["contaminants"])
        self.assertIn("ASV_001", result["clean_asvs"])
        self.assertIn("ASV_003", result["clean_asvs"])
        self.assertEqual(len(result["clean_asvs"]), 2)

    # 4. Feature 4: Alpha Diversity Indices Calculator
    def test_compute_diversity_indices(self):
        abundances = [100, 100, 100, 100]  # Perfectly even 4-species community
        metrics = compute_diversity_indices(abundances)
        self.assertEqual(metrics["richness"], 4)
        self.assertAlmostEqual(metrics["shannon"], 1.3863, places=3)
        self.assertAlmostEqual(metrics["simpson"], 0.75, places=3)
        self.assertAlmostEqual(metrics["evenness"], 1.0, places=3)

        empty_metrics = compute_diversity_indices([0, 0, 0])
        self.assertEqual(empty_metrics["richness"], 0)
        self.assertEqual(empty_metrics["shannon"], 0.0)

    # 5. Feature 5: LinDA Differential Abundance & Prevalence Filter
    def test_run_linda_differential_test(self):
        feature_matrix = {
            "ASV_PGPR_1": [10, 12, 15, 100, 120, 110],     # Enriched in treatment (GJ)
            "ASV_RARE_9": [0, 0, 0, 0, 0, 5],              # Rare taxon (< 30% prevalence)
            "ASV_CTRL_2": [80, 90, 85, 20, 15, 18],        # Depleted in treatment
        }
        groups = ["CTRL", "CTRL", "CTRL", "GJ", "GJ", "GJ"]
        res = run_linda_differential_test(feature_matrix, groups, min_prevalence=0.30)

        self.assertIn("ASV_RARE_9", res["filtered_out_rare"])
        self.assertIn("ASV_PGPR_1", res["results"])
        self.assertGreater(res["results"]["ASV_PGPR_1"]["log2_fc"], 2.0)
        self.assertTrue(res["results"]["ASV_PGPR_1"]["significant"])
        self.assertLess(res["results"]["ASV_CTRL_2"]["log2_fc"], -1.5)


if __name__ == "__main__":
    unittest.main()
