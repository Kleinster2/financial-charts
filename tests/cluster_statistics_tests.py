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
  - the full-universe boundary sweep flags a planted outsider and honors its
    join-distance arithmetic and verdict bands (audit finding 3 closure)
  - the n_perm adequacy audit (Phipson-Smyth floor vs Bonferroni cutoff)
    classifies UNRESOLVABLE / AT-RISK / ok rows per the documented rules

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
    weekly_cross_check,
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
    run_vol_matched_null,
    vol_matched_sample,
)
from cluster_boundary_sweep import (
    boundary_distances,
    classify_boundary,
    internal_envelope,
    pc1_factor_series,
)
from cluster_registry import (
    is_floor_pinned,
    latest_p_rows,
    min_nperm_for_cutoff,
    nperm_adequacy,
    perm_floor,
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
    arr = np.array(values, dtype=float)  # writeable: df.values is read-only under pandas CoW
    np.fill_diagonal(arr, 1.0)
    return pd.DataFrame(arr, index=names, columns=names, dtype=float)


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


class Item7SecondaryFixTests(unittest.TestCase):
    def test_loading_stability_is_sign_invariant(self):
        # PCA component signs are arbitrary per fit; a flipped but identical
        # factor must read +1.0, not -1.0.
        v = pd.Series([0.45, 0.50, 0.55, 0.40])
        self.assertAlmostEqual(loading_stability(v, -v), 1.0)
        self.assertAlmostEqual(loading_stability(v, v), 1.0)

    def test_pca_analysis_zero_variance_guard_names_ticker(self):
        rets = correlated_returns([("A", 3, 0.5)], T=100, seed=9)
        rets["HALT"] = 0.0
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(SystemExit) as ctx:
                pca_analysis(rets, ["A0", "A1", "A2", "HALT"], Path(tmp) / "x.png", "test")
        self.assertIn("HALT", str(ctx.exception))

    def test_weekly_cross_check_recovers_async_lead_lag_pair(self):
        # B lags A by one day (the asynchronous-close geometry): daily
        # correlation is ~0 but weekly sums share 4 of 5 terms (~0.8).
        rng = np.random.default_rng(17)
        a = rng.standard_normal(2000)
        df = pd.DataFrame(
            {"A": a, "B": np.roll(a, 1)},
            index=pd.bdate_range("2018-01-01", periods=2000),
        ).iloc[1:]
        self.assertLess(abs(df.corr().loc["A", "B"]), 0.10)
        weekly = weekly_cross_check(df, ["A", "B"])
        self.assertIsNotNone(weekly)
        self.assertGreater(weekly["intra"], 0.60)

    def test_vol_matched_sampler_respects_vol_bands(self):
        # Two clearly separated vol regimes: a high-vol cohort must draw
        # exclusively from the high-vol half of the pool.
        low = [(f"L{i}", 0.009 + i * 1e-5) for i in range(50)]
        high = [(f"H{i}", 0.049 + i * 1e-5) for i in range(50)]
        names = [n for n, _ in low + high]
        vols = np.array([v for _, v in low + high])
        rng = np.random.default_rng(23)
        for _ in range(20):
            sample = vol_matched_sample(names, vols, np.array([0.05] * 5), rng)
            self.assertTrue(all(t.startswith("H") for t in sample), sample)

    def test_vol_matched_null_is_tougher_when_vol_and_correlation_coincide(self):
        # The bias the variant removes: if high-vol names are also more
        # correlated (the Space pure-plays situation), unmatched random
        # baskets dilute the null with low-vol independent names. The
        # vol-matched null must sit materially higher.
        low = correlated_returns([("L", 40, 0.0)], T=300, seed=41) * 0.01
        high = correlated_returns([("H", 40, 0.3)], T=300, seed=43) * 0.05
        universe = pd.concat([low, high], axis=1)
        cohort_vols = pd.Series([0.05] * 5)
        matched, _ = run_vol_matched_null(universe, cohort_vols, n_perm=200, seed=42)
        unmatched, _ = run_random_basket_null(universe, cohort_n=5, n_perm=200, seed=42)
        self.assertGreater(matched.mean(), unmatched.mean() + 0.10)
        self.assertAlmostEqual(matched.mean(), 0.30, delta=0.05)


class UniverseFilterTests(unittest.TestCase):
    def test_us_common_stock_ticker_filter(self):
        for ticker in ["AAPL", "BRK-B", "PWP", "MRSH"]:
            self.assertTrue(is_us_common_stock_ticker(ticker), ticker)
        for ticker in ["ABEV3.SA", "005930.KS", "MC.PA", "CFR.SW", "^VIX", "CL=F", "BTC-USD"]:
            self.assertFalse(is_us_common_stock_ticker(ticker), ticker)
        # Mutual funds (5 letters ending in X) and Yahoo FX pairs (=X) — the
        # 2026-07-01 pool-hygiene catch: 66 funds and 2 FX pairs were riding
        # in the "stock-only" null pool via mistyped ticker_metadata rows.
        for ticker in ["AGTHX", "DODGX", "BPTRX", "USDJPY=X", "JPYUSD=X"]:
            self.assertFalse(is_us_common_stock_ticker(ticker), ticker)
        # 4-letter X-enders are stocks, not funds (NFLX); 5-letter non-X too (GOOGL).
        for ticker in ["NFLX", "GOOGL"]:
            self.assertTrue(is_us_common_stock_ticker(ticker), ticker)


class BoundarySweepTests(unittest.TestCase):
    def test_join_distances_match_hand_arithmetic(self):
        # Cohort A,B at rho 0.8; outsider X at 0.6/0.5 to A/B; N independent.
        # Average-linkage join distance of X = 1 - mean(0.6, 0.5) = 0.45;
        # nearest member A at single-linkage distance 1 - 0.6 = 0.40.
        cov = np.array([
            [1.0, 0.8, 0.6, 0.0],
            [0.8, 1.0, 0.5, 0.0],
            [0.6, 0.5, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ])
        rng = np.random.default_rng(47)
        data = rng.standard_normal((20000, 4)) @ np.linalg.cholesky(cov).T
        rets = pd.DataFrame(data, index=pd.bdate_range("2020-01-01", periods=20000),
                            columns=["A", "B", "X", "N"])
        dist = boundary_distances(rets, ["A", "B"], ["X", "N"])
        self.assertEqual(list(dist.index), ["X", "N"])  # sorted nearest-first
        self.assertAlmostEqual(dist.loc["X", "join_dist_avg"], 0.45, delta=0.02)
        self.assertAlmostEqual(dist.loc["X", "join_dist_min"], 0.40, delta=0.02)
        self.assertEqual(dist.loc["X", "nearest_member"], "A")
        self.assertAlmostEqual(dist.loc["N", "join_dist_avg"], 1.0, delta=0.03)

    def test_classify_boundary_bands(self):
        dists = pd.Series([0.30, 0.45, 0.90])
        self.assertEqual(classify_boundary(dists, 0.5, 0.35), ("BOUNDARY-CONTAMINATED", 2, 1))
        self.assertEqual(classify_boundary(dists, 0.5, 0.25), ("BOUNDARY-PERMEABLE", 2, 0))
        self.assertEqual(classify_boundary(pd.Series([0.6, 0.9]), 0.5, 0.25), ("BOUNDARY-CLEAN", 0, 0))
        # Threshold uses <= (fcluster merge semantics); envelope uses strict <.
        self.assertEqual(classify_boundary(pd.Series([0.5]), 0.5, 0.5), ("BOUNDARY-PERMEABLE", 1, 0))
        # Undefined envelope (single-name candidate): threshold-only classification.
        self.assertEqual(classify_boundary(pd.Series([0.1]), 0.5, float("nan")), ("BOUNDARY-PERMEABLE", 1, 0))

    def test_planted_outsider_flagged_end_to_end(self):
        # 5-name rho=0.7 block; candidate = first 4, the 5th name is left in
        # the pool alongside independent noise. The sweep must rank the
        # planted outsider first, far below the noise, and not read CLEAN.
        rets = correlated_returns([("A", 5, 0.7), ("N", 6, 0.0)], T=8000, seed=41)
        candidate = ["A0", "A1", "A2", "A3"]
        pool = ["A4", "N0", "N1", "N2", "N3", "N4", "N5"]
        dist = boundary_distances(rets, candidate, pool)
        self.assertEqual(dist.index[0], "A4")
        self.assertLess(dist.loc["A4", "join_dist_avg"], 0.35)
        self.assertGreater(dist.loc["N0", "join_dist_avg"], 0.9)
        verdict, below, inside = classify_boundary(
            dist["join_dist_avg"], 0.4, internal_envelope(rets, candidate)
        )
        self.assertNotEqual(verdict, "BOUNDARY-CLEAN")
        self.assertGreaterEqual(below, 1)

    def test_internal_envelope(self):
        rets = correlated_returns([("A", 3, 0.8)], T=5000, seed=43)
        # Equicorrelated block: every merge lands near 1 - rho = 0.2.
        self.assertAlmostEqual(internal_envelope(rets, ["A0", "A1", "A2"]), 0.2, delta=0.03)
        self.assertTrue(np.isnan(internal_envelope(rets, ["A0"])))

    def test_pc1_factor_series_positive_and_tracks_members(self):
        rets = correlated_returns([("A", 4, 0.7)], T=5000, seed=45)
        factor = pc1_factor_series(rets, list(rets.columns))
        # Equicorrelation rho: corr(member, PC1 score) = sqrt((1+(N-1)rho)/N) ~ 0.88.
        for c in rets.columns:
            self.assertGreater(rets[c].corr(factor), 0.8, c)


class NpermAdequacyTests(unittest.TestCase):
    def test_perm_floor(self):
        self.assertAlmostEqual(perm_floor(10000), 1 / 10001)
        self.assertAlmostEqual(perm_floor(1000), 1 / 1001)
        self.assertTrue(np.isnan(perm_floor(float("nan"))))
        self.assertTrue(np.isnan(perm_floor(0)))

    def test_min_nperm_for_cutoff(self):
        self.assertEqual(min_nperm_for_cutoff(0.05 / 112), 2239)
        self.assertEqual(min_nperm_for_cutoff(0.05 / 500), 9999)  # the 10k standard's reach
        self.assertEqual(min_nperm_for_cutoff(-1.0), -1)

    def test_is_floor_pinned(self):
        self.assertTrue(is_floor_pinned(1 / 4001, 4000))
        self.assertFalse(is_floor_pinned(2 / 4001, 4000))
        self.assertFalse(is_floor_pinned(float("nan"), 4000))
        self.assertFalse(is_floor_pinned(0.0001, float("nan")))

    def test_nperm_adequacy_statuses(self):
        # At alpha=0.05, N=112: cutoff 0.000446. Five canonical cases:
        #   pinned at a floor above the cutoff      -> UNRESOLVABLE (indeterminate)
        #   near-cutoff p at a floor above cutoff   -> UNRESOLVABLE (resolution decides)
        #   evidence-fail far above the near-zone   -> ok (resolution moot)
        #   pinned at 4k (floor > cutoff/2)         -> AT-RISK
        #   pinned at 10k (floor < cutoff/2)        -> ok
        df = pd.DataFrame({
            "cohort_name": ["pinned_lowres", "near_cutoff_lowres", "evidence_fail", "pinned_4k", "pinned_10k"],
            "p_random_basket_intra": [1 / 1001, 2 / 1001, 0.30, 1 / 4001, 1 / 10001],
            "n_permutations": [1000.0, 1000.0, 1000.0, 4000.0, 10000.0],
        })
        out = nperm_adequacy(df, alpha=0.05, n_tests=112).set_index("cohort_name")
        self.assertTrue(out.loc["pinned_lowres", "nperm_status"].startswith("UNRESOLVABLE"))
        self.assertIn("INDETERMINATE", out.loc["pinned_lowres", "nperm_status"])
        self.assertEqual(out.loc["near_cutoff_lowres", "nperm_status"], "UNRESOLVABLE")
        self.assertEqual(out.loc["evidence_fail", "nperm_status"], "ok")
        self.assertEqual(out.loc["pinned_4k", "nperm_status"], "AT-RISK")
        self.assertEqual(out.loc["pinned_10k", "nperm_status"], "ok")
        # A 4k row becomes unresolvable once the registry reaches N ~= 200.
        self.assertAlmostEqual(out.loc["pinned_4k", "unresolvable_at_n"], 0.05 * 4001, delta=0.1)
        # Missing n_perm is flagged, not silently passed.
        no_nperm = pd.DataFrame({
            "cohort_name": ["x"], "p_random_basket_intra": [0.001], "n_permutations": [float("nan")],
        })
        self.assertEqual(
            nperm_adequacy(no_nperm, alpha=0.05, n_tests=112)["nperm_status"].iloc[0], "NO-NPERM"
        )

    def test_latest_p_rows_ignores_partial_diagnostic_rows(self):
        # A newer row WITHOUT a p-value (boundary sweep / holdout-only re-run)
        # must not eclipse the cohort's p-carrying row in the FDR dedup.
        df = pd.DataFrame({
            "cohort_name": ["A", "A", "B", "B"],
            "test_date": ["2026-06-01", "2026-07-01", "2026-06-01", "2026-07-01"],
            "p_random_basket_intra": [0.002, float("nan"), 0.010, 0.020],
            "n_permutations": [10000.0, float("nan"), 10000.0, 10000.0],
        })
        out = latest_p_rows(df).set_index("cohort_name")
        self.assertEqual(len(out), 2)
        self.assertEqual(out.loc["A", "test_date"], "2026-06-01")  # newer NaN row skipped
        self.assertAlmostEqual(out.loc["A", "p_random_basket_intra"], 0.002)
        self.assertEqual(out.loc["B", "test_date"], "2026-07-01")  # newer p row wins
        self.assertAlmostEqual(out.loc["B", "p_random_basket_intra"], 0.020)


if __name__ == "__main__":
    unittest.main(verbosity=2)
