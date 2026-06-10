"""Synthetic-data regression tests for the cluster-validation statistical layer.

Audit remediation item 6 (docs/cluster-validation-audit-2026-06-09.md): the
framework's math previously had zero test coverage — the polluted-null and
p=0.0 defects shipped silently. These tests pin the statistics to known
ground truth so regressions cannot ship silently again:

  - planted equicorrelation is recovered by intra_correlation
  - PC1 explained variance matches the closed-form (1 + (N-1)*rho) / N
  - hierarchical clustering recovers a planted 2-block structure exactly
  - threshold-cut semantics on a hand-built correlation matrix are exact
  - join-distance topology (average linkage) matches hand arithmetic
  - Phipson-Smyth p-values respect the (k+1)/(n+1) floor and never return 0
  - the random-basket null machinery passes a planted-signal / null-signal
    calibration check end-to-end
  - verdict-band functions (holdout, OOS) honor their documented cut-points

Hermetic: no database, no network, no git. Plots write to a temp dir.

Run: python tests/cluster_statistics_tests.py   (part of npm run test:consistency)
"""

import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from cluster_analysis import (
    candidate_join_distances,
    correlation_matrix,
    hierarchical_cluster,
    pca_analysis,
)
from cluster_holdout_test import loading_stability, stability_verdict
from cluster_oos_validation import grade, p_right_tail
from cluster_permutation_test import (
    block_shuffle,
    intra_correlation,
    is_us_common_stock_ticker,
    p_value_right_tail,
    pc1_explained_variance,
    run_random_basket_null,
)
from cluster_threshold_scan import assignments_at_threshold, scan


def correlated_returns(blocks, T, seed, start="2020-01-01"):
    """Gaussian returns with a block-diagonal correlation structure.

    blocks: list of (prefix, n_names, rho) — cross-block correlation is 0.
    """
    sizes = [n for _, n, _ in blocks]
    total = sum(sizes)
    cov = np.zeros((total, total))
    pos = 0
    cols = []
    for prefix, n, rho in blocks:
        cov[pos : pos + n, pos : pos + n] = rho
        for i in range(n):
            cov[pos + i, pos + i] = 1.0
            cols.append(f"{prefix}{i}")
        pos += n
    rng = np.random.default_rng(seed)
    data = rng.standard_normal((T, total)) @ np.linalg.cholesky(cov).T
    idx = pd.bdate_range(start, periods=T)
    return pd.DataFrame(data, index=idx, columns=cols)


def handbuilt_corr(values, names):
    m = pd.DataFrame(values, index=names, columns=names, dtype=float)
    np.fill_diagonal(m.values, 1.0)
    return m


class PlantedStructureRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_intra_correlation_recovers_planted_rho(self):
        rets = correlated_returns([("A", 5, 0.6)], T=20000, seed=7)
        self.assertAlmostEqual(intra_correlation(rets, list(rets.columns)), 0.6, delta=0.02)

    def test_pc1_explained_variance_matches_closed_form(self):
        # Equicorrelated N names at rho: top eigenvalue of the correlation
        # matrix is 1 + (N-1)*rho, so PC1 share = (1 + (N-1)*rho) / N.
        rets = correlated_returns([("A", 5, 0.6)], T=20000, seed=11)
        theory = (1 + 4 * 0.6) / 5
        self.assertAlmostEqual(pc1_explained_variance(rets, list(rets.columns)), theory, delta=0.02)

    def test_pca_analysis_loadings_equal_and_positive(self):
        rets = correlated_returns([("A", 5, 0.6)], T=20000, seed=13)
        result = pca_analysis(rets, list(rets.columns), self.out / "pca.png", "test")
        pc1 = result["loadings"]["PC1"]
        self.assertTrue((pc1 > 0).all())
        self.assertLess(pc1.max() / pc1.min(), 1.2)
        self.assertAlmostEqual(result["explained_variance_ratio"][0], (1 + 4 * 0.6) / 5, delta=0.02)
        self.assertTrue((self.out / "pca.png").exists())

    def test_pca_analysis_rejects_short_windows(self):
        rets = correlated_returns([("A", 4, 0.6)], T=10, seed=3)
        with self.assertRaises(SystemExit):
            pca_analysis(rets, list(rets.columns), self.out / "short.png", "test")

    def test_hierarchical_clustering_recovers_two_blocks_exactly(self):
        rets = correlated_returns([("A", 3, 0.8), ("B", 3, 0.8)], T=5000, seed=21)
        corr = correlation_matrix(rets)
        universe = {
            "cluster": {"color": "#2962FF", "tickers": ["A0", "A1", "A2"]},
            "ctrl": {"color": "#000000", "tickers": ["B0", "B1", "B2"]},
        }
        clusters = hierarchical_cluster(corr, universe, 0.4, self.out / "dendro.png", "test")
        memberships = sorted(tuple(sorted(m)) for m in clusters.values())
        self.assertEqual(memberships, [("A0", "A1", "A2"), ("B0", "B1", "B2")])

    def test_threshold_scan_intact_inside_block_band(self):
        rets = correlated_returns([("A", 3, 0.8), ("B", 3, 0.8)], T=5000, seed=23)
        corr = correlation_matrix(rets)
        scan_df = scan(corr, ["A0", "A1", "A2"], np.array([0.40, 0.60]))
        self.assertTrue(scan_df["intact"].all(), scan_df.to_string())


class ExactHandbuiltTests(unittest.TestCase):
    def setUp(self):
        # AB and CD pairs at corr 0.75 (distance 0.25); all cross pairs 0.10.
        names = ["A", "B", "C", "D"]
        v = [
            [1.00, 0.75, 0.10, 0.10],
            [0.75, 1.00, 0.10, 0.10],
            [0.10, 0.10, 1.00, 0.75],
            [0.10, 0.10, 0.75, 1.00],
        ]
        self.corr = handbuilt_corr(v, names)

    def test_assignments_at_threshold_semantics(self):
        def n_clusters(threshold):
            return len(set(assignments_at_threshold(self.corr, threshold).values()))

        self.assertEqual(n_clusters(0.20), 4)  # below pair distance: singletons
        self.assertEqual(n_clusters(0.40), 2)  # pairs merged, blocks separate
        self.assertEqual(n_clusters(0.95), 1)  # above cross distance: one cluster

    def test_join_distance_topology_average_linkage(self):
        names = ["A", "B", "C"]
        v = [
            [1.0, 0.9, 0.2],
            [0.9, 1.0, 0.2],
            [0.2, 0.2, 1.0],
        ]
        corr = handbuilt_corr(v, names)
        joins = candidate_join_distances(corr, names)
        self.assertEqual(len(joins), 2)
        self.assertAlmostEqual(joins.iloc[0]["Distance"], 0.1, places=9)
        self.assertEqual(sorted(joins.iloc[0]["Members"].split("+")), ["A", "B"])
        self.assertAlmostEqual(joins.iloc[1]["Distance"], 0.8, places=9)  # mean(0.8, 0.8)


class PValueTests(unittest.TestCase):
    def test_phipson_smyth_floor_and_ceiling(self):
        null = np.arange(100) / 100.0
        self.assertAlmostEqual(p_value_right_tail(2.0, null), 1 / 101)   # beats all draws
        self.assertAlmostEqual(p_value_right_tail(-1.0, null), 1.0)      # beats none
        self.assertAlmostEqual(p_value_right_tail(0.5, null), 51 / 101)  # 50 draws >= 0.5
        self.assertGreater(p_value_right_tail(np.inf, null), 0.0)        # never exactly 0

    def test_oos_p_right_tail_guards(self):
        self.assertTrue(np.isnan(p_right_tail(0.5, np.array([]))))
        self.assertTrue(np.isnan(p_right_tail(float("nan"), np.arange(10) / 10)))

    def test_random_basket_null_calibration_end_to_end(self):
        # Universe of 40 independent series; a planted rho=0.6 cohort must hit
        # the Phipson-Smyth floor against it, and an impossible observation
        # below the entire null must return 1.0.
        universe = correlated_returns([(f"U", 40, 0.0)], T=250, seed=31)
        cohort = correlated_returns([("C", 5, 0.6)], T=250, seed=37)
        observed = intra_correlation(cohort, list(cohort.columns))
        intra_null, pc1_null = run_random_basket_null(universe, cohort_n=5, n_perm=400, seed=42)
        self.assertEqual(len(intra_null), 400)  # no skips on clean synthetic data
        self.assertLess(abs(intra_null.mean()), 0.02)  # independent universe: null centered on 0
        self.assertLess(p_value_right_tail(observed, intra_null), 0.01)
        self.assertEqual(p_value_right_tail(-0.5, intra_null), 1.0)
        self.assertTrue((pc1_null > 0).all() and (pc1_null < 1).all())

    def test_block_shuffle_properties(self):
        rng = np.random.default_rng(5)
        arr = np.arange(100.0)
        perm = block_shuffle(arr, 1, rng)
        self.assertEqual(sorted(perm.tolist()), sorted(arr.tolist()))  # pure permutation
        blocks = block_shuffle(arr, 5, rng)
        self.assertEqual(len(blocks), len(arr))  # block bootstrap preserves length
        self.assertTrue(set(blocks.tolist()).issubset(set(arr.tolist())))


class VerdictBandTests(unittest.TestCase):
    def test_holdout_stability_bands(self):
        self.assertTrue(stability_verdict(0.5, 0.6).startswith("STRENGTHENING"))
        self.assertTrue(stability_verdict(0.8, 0.74).startswith("STABLE"))
        self.assertTrue(stability_verdict(0.8, 0.60).startswith("WEAKENED"))
        self.assertTrue(stability_verdict(0.8, 0.30).startswith("REGIME-DEPENDENT"))
        self.assertTrue(stability_verdict(float("nan"), 0.5).startswith("INDETERMINATE"))
        self.assertTrue(stability_verdict(0.0, 0.5).startswith("INDETERMINATE"))

    def test_loading_stability_degenerate_inputs(self):
        flat = pd.Series([0.5, 0.5, 0.5])
        varied = pd.Series([0.1, 0.5, 0.9])
        self.assertTrue(np.isnan(loading_stability(flat, varied)))
        self.assertAlmostEqual(loading_stability(varied, varied), 1.0)

    def test_oos_grade_bands_and_preliminary_prefix(self):
        self.assertEqual(grade(1.20, 50), "OOS-STRENGTHENING")
        self.assertEqual(grade(0.90, 50), "OOS-CONFIRMED")
        self.assertEqual(grade(0.70, 50), "OOS-WEAKENED")
        self.assertEqual(grade(0.30, 50), "OOS-FAILED")
        self.assertEqual(grade(0.90, 39), "PRELIMINARY OOS-CONFIRMED")
        self.assertEqual(grade(float("nan"), 50), "INDETERMINATE")


class UniverseFilterTests(unittest.TestCase):
    def test_us_common_stock_ticker_filter(self):
        for ticker in ["AAPL", "BRK-B", "PWP", "MRSH"]:
            self.assertTrue(is_us_common_stock_ticker(ticker), ticker)
        for ticker in ["ABEV3.SA", "005930.KS", "MC.PA", "CFR.SW", "^VIX", "CL=F", "BTC-USD"]:
            self.assertFalse(is_us_common_stock_ticker(ticker), ticker)


if __name__ == "__main__":
    unittest.main(verbosity=2)
