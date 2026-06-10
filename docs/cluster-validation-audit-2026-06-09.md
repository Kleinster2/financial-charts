# Cluster validation framework — robustness audit (2026-06-09)

Point-in-time audit of the cluster identification routine, prompted by the question "is our cluster identification routine robust?" Scope: `scripts/cluster_analysis.py`, `scripts/cluster_permutation_test.py`, `scripts/cluster_holdout_test.py`, `scripts/cluster_threshold_scan.py`, `scripts/cluster_registry.py`, `scripts/cluster_stability_check.py`, `scripts/cluster_registry.csv` (33 rows), `docs/cluster-validation.md`, the 34 YAML configs in `scripts/cluster_configs/`, and direct queries against `market_data.db` to measure the random-basket null pool. No fixes were applied as of this audit date; findings reference the code as committed on 2026-06-09.

## Verdict

The architecture is unusually rigorous — a falsification layer (permutation nulls, temporal holdout, threshold scan, FDR-corrected registry) that most professional shops never build, and it demonstrably bites: Mag 7 (intra-corr 0.316, holdout ratio 0.44, zero threshold-stable width), Foundry (random-basket p = 0.29), and AI hyperscalers (PC1 p = 0.054) are all honestly recorded as failures in the registry. But the implementation has one material statistical hole sitting directly under the framework's strongest claim (the random-basket p-value), plus a cluster of silent-failure modes. As of this date: robust in design, not yet robust in execution.

## What the framework gets right

- The falsification layer exists and has falsified real cohorts. A routine that can say no (Mag 7, Foundry, AI hyperscalers) is not a rubber stamp.
- The random-basket null preserves the shared trading calendar: null baskets experience the same market days as the cohort, so market-wide jump days lift the null along with the observed statistic. Generic risk-on cohesion is automatically priced into the bar.
- The registry + Bonferroni/Benjamini-Hochberg correction (`cluster_registry.py`) is rare discipline — it acknowledges that screening 33 cohorts guarantees false discoveries at p < 0.05.
- Threshold scan, temporal holdout, and the 90-day rolling tightness history address the three obvious free knobs (cut threshold, window choice, regime dependence).
- Documented verdict bands in `docs/cluster-validation.md` prevent post-hoc threshold shopping.
- YAML configs with pinned `window_end` make runs reproducible.
- `1 - |corr|` average-linkage distance is acceptable for long-only equity cohorts (no metric requirement for average linkage; negative correlations are rare among stocks).

## Tier 1 — findings that affect published numbers

### 1. Random-basket null pool is polluted, in the anti-conservative direction

`default_universe_from_db` (`cluster_permutation_test.py:162-173`) pulls every ticker in `prices_long` with >=200 obs in the window — no asset-type filter. Measured composition of the eligible pool on 2026-06-09 (trailing 1Y, >=200 obs): 1,230 tickers total = 803 with NULL metadata type + 371 typed `stock` + 31 `macro` + 24 `index` + 1 `etf`.

The pool therefore contains:

- Macro series with near-zero daily correlation to equities (e.g., `AAA10Y`, a yield series)
- 24 synthetic indices, including the vault's own constructed `AIFD`, `AIWD`, `AITW`
- Crypto pairs (`ADA-USD`, `AAVE-USD`, `ALGO-USD`, ...) trading a 7-day calendar
- Asynchronous international listings (`.KS`, `.HK`, `.SA`, `.PA`, `.NS`)

Macro series and async foreign names drag null-basket cohesion down, shifting the null distribution left and making every cohort look more exceptional than it is. With macro + index series alone (55 of 1,230), ~27% of N=7 null baskets contain at least one deflating series; including crypto pairs and international listings the share is plausibly around half. Every "p < 0.001" in the registry was measured against this deflated null.

Compounding it: the help text at `cluster_permutation_test.py:84-86` claims the default universe filters to `data_type='stock'` via `ticker_metadata`. That filter was never implemented — and cannot be as documented, because 1,371 of 2,274 `ticker_metadata` rows have NULL `data_type` (AAPL itself is untyped). Of the actual eligible pool, only 371 of 1,230 are typed `stock`. Both the code and the metadata need work before the documented behavior is achievable.

### 2. Permutation resolution does not support the multiplicity correction layered on top

All 33 registry rows were run on 2026-05-13 with `n_permutations=1000` (the documented default is 10,000), so the smallest resolvable nonzero p is 0.001 — yet Bonferroni across 33 cohorts cuts at 0.05/33 ≈ 0.0015. Sixteen cohorts sit in the 0.002–0.05 zone where the correction actually decides the verdict (WFE quartet p = 0.004, Korea Memory 0.006, Card networks 0.002, Fabless 0.0041, ECPR 0.0030, AIFD 0.0032, KTOS 0.0020, WHR 0.0010, ...).

Worse, p-values are computed as `(null >= observed).mean()` (`cluster_permutation_test.py:225-226`), which returns exactly 0.0 when no null draw exceeds the observed value. Sixteen of 33 registry rows store `p_random_basket_intra = 0.0` — statistically impossible (the Phipson–Smyth correction is (k+1)/(n+1), floor ≈ 0.001 at 1,000 permutations) and trivially passing any correction threshold in `cluster_registry.py::cmd_correction`.

### 3. Boundary validation is bounded by the config, not the market

The dendrogram boundary test ("the algorithm has no prior label", `docs/cluster-validation.md` §3) and the threshold scan's contamination check only see the ~15–20 names listed in the YAML. A cohort could be inseparable from 50 names not in the config and still scan "intact, no contamination." The celebrated Mag 7 finding ("first non-cohort tickers to join are semis") could only emerge because semis were in `mag7.yaml`'s control groups — the scan sees nothing else by construction. The one diagnostic that looks beyond the config (the random-basket null) is the one with the polluted universe (finding 1).

## Tier 2 — silent-failure modes

### 4. Silent ticker dropout

A config ticker absent from the DB (typo, alias drift — the same class of problem the daily-scan Phase-0 alias audit exists for) silently vanishes via the column filter at `cluster_analysis.py:125` and the candidate filter at `:566`. Nothing warns. A "7-name cohort" can be validated on 6 names without anyone noticing. The registry already shows the adjacent failure in the wild: the US Memory holdout row has `train_intra = nan` (SNDK only exists from its Feb 2025 WDC spinoff, so the 2Y train half was empty for it) with no flag — just a blank stability ratio.

### 5. `cluster_stability_check.py` reads the deprecated wide table

Line 26 queries `stock_prices_daily` — the stale-prone compatibility snapshot at the SQLite column limit, per CLAUDE.md — while every other script in the suite uses canonical `prices_long`. It also hardcodes `COHORT` (Space pure-plays) and `END = date(2026, 5, 7)` instead of using the YAML config schema. The stability table required for cohort-owner notes can silently run on stale data.

### 6. One-day window asymmetry between cohort and null

`cluster_analysis.load_returns` wraps comparisons in `date()` (`cluster_analysis.py:116-117`), so the `window_end` day is included. The permutation script's universe loaders (`default_universe_from_db`, `load_universe_returns` at `cluster_permutation_test.py:163-170, 183-185`) use raw string comparison against stored `'YYYY-MM-DD HH:MM:SS'` values: `'2026-05-08 00:00:00' <= '2026-05-08'` is False, so the end day is excluded from the null universe. For post-event validations the cohort gets the event day; the null baskets never see it.

### 7. Smaller defects

- Holdout PC1-loadings correlation (`cluster_holdout_test.py:156-159`) never sign-aligns train vs test factors; sklearn's per-fit sign convention can flip between halves, so a perfect factor match can read as −1.0 in edge cases. `diagnostics()` applies no sign normalization.
- Zero-variance guard present in the permutation script (`intra_correlation`, `pc1_explained_variance`) but absent in `cluster_analysis.pca_analysis` and the rolling-tightness loop — a halted ticker in a 90-day window produces inf and crashes mid-run.
- `scripts/universes/large_cap_us.txt` is referenced in the docs and the `--universe-file` examples but `scripts/universes/` does not exist.
- No gap guard on `log(px / px.shift(1))`: a trading suspension produces a multi-week "daily" return injected as an outlier.
- Rolling-tightness "satellite" is defined as the first ticker in the YAML list (`cluster_analysis.py:313-314`), not the highest-join-distance member; the chart label can point at the wrong name. Documented, but a naming trap.

## Tier 3 — design limits (partly acknowledged in the docs)

### 8. Everything is in-sample relative to discovery

`rklb.yaml`'s header states the cohort was proposed because of the May 8 2026 basket rally — then permutation, holdout, and threshold scan all run on windows containing that rally. Holdout splits within the discovery window; permutation resamples across it; threshold-scan re-cuts it. None can catch selection-on-the-dependent-variable. The docs' "one-day tape is a watchlist signal, not a validation trigger" rule shows awareness, but there is no mechanism: the registry has no `definition_date` column and no post-definition out-of-sample re-validation pass. This is the single highest-value methodological addition available — survival on data after the definition date is the only test discovery bias cannot game.

### 9. The null is not beta/vol-matched

Space pure-plays are ~2x-beta small caps tested against a mostly large-cap pool; part of their "exceptional cohesion" is shared high beta, not a cluster factor. A vol- or beta-matched sampling frame, or a market-residualized intra-corr in the basic pass (`cluster_deep_dive.py` has the machinery but it is deferred-by-default), would separate "cluster factor" from "shared beta."

### 10. Asynchronous closes bias cross-region configs both ways

Cross-region daily correlations are structurally depressed by non-overlapping trading hours regardless of economics. This deflates intra-corr for mixed-region cohorts and inflates "intra advantage" against foreign control groups (Indian metals, Korea Memory vs US controls). No weekly-return or lead-lag (Scholes-Williams/Dimson-style) robustness check exists for cross-region cohorts.

### 11. N=2 cohorts

Four of 33 registry rows are two-name "clusters" (Korea Memory, Card networks duopoly, Life insurers pair, COIN pair). A two-name cluster is one correlation coefficient; the framework processes it without comment.

### 12. Zero regression tests on the statistical layer

No test file touches any cluster script; `npm run test:consistency` covers note compliance only. A synthetic-data test (planted 2-block correlation matrix recovers exactly 2 clusters; known eigenstructure reproduces PC1 within tolerance; permutation p-value calibration on null data) would lock the math against regressions.

## Remediation, in priority order

1. Clean the null pool: filter to common stocks via a `data_type` backfill in `ticker_metadata` or an explicit curated universe file; re-run the 33 registry cohorts so the published p-values are real.
2. Phipson–Smyth p-values ((k+1)/(n+1)) + `n_perm=10000` so the FDR layer has resolution; never store p = 0.0.
3. Loud warnings on missing/short-history tickers; echo the resolved cohort (with obs counts per ticker) in every output artifact.
4. Port `cluster_stability_check.py` to `prices_long` and the YAML config schema; fix the raw string date comparisons in the universe loaders (wrap in `date()`).
5. Add `definition_date` to the registry and a quarterly post-definition out-of-sample re-validation pass.
6. Add a synthetic-data regression test file for the statistical layer.
7. Secondary: sign-align holdout loadings (or report |corr|), zero-variance guards in `pca_analysis` and the rolling loop, beta/vol-matched null variant, weekly-return cross-check for cross-region configs.

Items 1–4 are mechanical; 5 is the methodological upgrade; 6 protects everything thereafter.

## Status

- 2026-06-09: audit written; no fixes applied. Registry p-values (all 33 rows, batch of 2026-05-13, n_perm=1000) predate any null-pool fix and should be treated as anti-conservative until re-run.
