# Cluster validation framework — robustness audit (2026-06-09)

Plain-language companion: `investing/Reports/2026-06-10-cluster-framework-explainer.md` (narrative version of the audit, remediation, and OOS pass, readable without prior context).

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
- 2026-06-09/10: remediation items 1-4 complete; all 34 cohorts re-run. Details below.

### Remediation log (2026-06-10)

Code and data:

- `scripts/backfill_ticker_types.py` (new): classified 1,231 of 1,250 untyped `prices_long` tickers via pattern rules + Yahoo chart metadata — 830 stock, 230 etf, 105 currency, 48 crypto, 17 index, 1 other; 19 unresolvable (delisted names, internal `HL:*` series) left NULL and excluded. The 105 FX series were invisible to the original audit, which only measured macro/index/crypto pollution — the pool was dirtier than reported.
- `cluster_permutation_test.py`: default universe now stock/equity-typed, US-listed only (921 eligible in the trailing-1Y window vs 1,230 polluted); `date()`-wrapped SQL removes the cohort-vs-null end-day asymmetry; Phipson-Smyth (k+1)/(n+1) p-values (p = 0.0 impossible); loud missing-ticker warnings in console and txt artifacts; help text corrected.
- `cluster_analysis.py`: missing-ticker warnings in console and results.txt.
- `cluster_stability_check.py`: rewritten — canonical `prices_long`, shared YAML config schema, standardized PCA. The old version also ran PCA on raw (non-standardized) returns, a fourth defect found during the port: its PC1 column was dominated by the highest-vol name.
- `scripts/universes/us_common_stocks.txt` created (918 names, pinned snapshot); dangling doc references fixed.
- One incidental pool observation: the obs-coverage filter (>=80% of cohort obs) reduces the effective pool to ~206 continuously-tracked names — and in the old runs this *enriched* the pollution, because FX/crypto/macro series are refreshed daily as a block and survived the filter disproportionately while partially-covered stocks dropped out.

Re-run outcome (34 cohorts, 10,000 permutations, random-basket null + threshold scan + 2Y holdout; registry rows 2026-06-09/10 supersede 2026-05-13, which are kept for history):

- 20/34 pass Bonferroni (0.00147), 30/34 pass Benjamini-Hochberg at alpha 0.05.
- Outright failures: Foundry monopoly (p = 0.328), AI hyperscalers (0.135), Animal health (0.065), Cybersecurity consolidation (0.051) — every one was already marked falsified in the vault or never promoted to a note. No formerly-validated cohort lost certification.
- Empirical correction to finding 1's directional claim: the polluted pool distorted p-values in BOTH directions, split by cohort size. Small-N cohorts were penalized by same-asset clumps in the null (occasional all-crypto/all-FX draws fattened the right tail): AI Compute 0.023 → 0.0026, COIN pair 0.008 → 0.0018, Card networks 0.002 → 0.0012, Korea Memory 0.006 → 0.0031, Mag 7 0.010 → 0.0050. Mid/large-N and weak cohorts were flattered by cross-asset deflators: AI hyperscalers 0.028 → 0.135, Animal health 0.025 → 0.065, Cybersecurity 0.019 → 0.051, Fabless 0.0041 → 0.0173, ECPR 0.0030 → 0.0123, AIFD 0.0032 → 0.0099.
- Floor-value cohorts (p = 0.0001, beat all 10,000 draws): ALTM, Boutique advisory, Crypto-to-AI, Defense primes (both), Global luxury (first-time entry), Hyperscaler suppliers, Insurance brokers, Mega banks, P&C carriers, Platform cyber (0.0003), SCP, Space pure-plays, US Memory, WFE quartet (was 0.004).
- Indian metals intra-corr fell 0.581 → 0.418 and holdout 0.79 → 0.57 between the April-window baseline and the re-run window — the cohort is loosening on fresh data, independent of the pool fix. Watchlist item.
- US Memory 2Y holdout remains indeterminate (SNDK has no pre-Feb-2025 history; the train half is empty) — now flagged loudly instead of silently producing nan.

Open items: 5 (registry `definition_date` + post-definition out-of-sample re-validation pass), 6 (synthetic-data regression tests), 7 (secondary: holdout sign alignment, zero-variance guards in `pca_analysis`/rolling loop, beta/vol-matched null variant, weekly-return cross-check for cross-region cohorts).

### Item 5 — post-definition OOS pass (2026-06-10)

Implemented `scripts/cluster_oos_validation.py` and extended the registry schema with `definition_date` + `oos_*` columns. Definition date = first git commit of the cohort's YAML config (override via a `definition_date:` config key); all statistics are computed on returns strictly after it, including a random-basket p-value against the cleaned stock pool on the same OOS window (null baskets face the identical short window, so validity holds at any length — only power is limited). Verdict bands mirror the holdout (>=1.10 OOS-STRENGTHENING / 0.85 OOS-CONFIRMED / 0.60 OOS-WEAKENED / below OOS-FAILED), with PRELIMINARY below 40 obs and INSUFFICIENT_HISTORY below 15. Documented as §5 of the Statistical falsification framework in `docs/cluster-validation.md`; quarterly cadence alongside the FDR correction. Definition dates recovered: 2026-05-03 for the main screening batch, 05-06..05-11 for the second wave, 05-28 for luxury — so the first pass is PRELIMINARY nearly everywhere by construction; first non-preliminary verdicts land ~July 2026.

The first pass's missing-ticker warnings immediately surfaced two data-layer defects the silent-dropout era would have swallowed:

1. Alias drift in configs. Marsh McLennan changed ticker MMC → MRSH on 2026-01-14; the MRSH series was complete and current the whole time, but four configs (`aifd`, `insurance_brokers` as cluster member; `pc_carriers`, `ins_carriers` as control) still referenced the dead alias — `aifd.yaml` even carried a comment treating the rename as "stale data, included anyway." The 2026-06-09/10 in-sample re-runs for AIFD (N=9 of 10) and Insurance brokers (N=5 of 6) ran without the name. Fixed: MMC → MRSH in all four configs.

2. Freeze-at-fetch-date refresh gap. Tickers added ad hoc via `add_ticker.py` for cluster analyses never joined any refresh list and silently froze at their fetch date — the frozen dates match config-creation dates exactly (ELAN/FBIN froze 2026-05-07, the day `zts.yaml`/`whr.yaml` were committed; the foreign luxury names froze 05-27/28 with `luxury_global.yaml`; PWP/LAZ/FSLY/SNDK froze 05-01 at the boutique-print analysis fetch; PJT at 04-20). Misread initially as delistings/pipeline rot; the vault's own boutique note (PJT "local price data stale at Apr 20") and Lazard's Apr-30 acquirer role disproved that. Fixed structurally: `download_all_assets.py` now unions a dynamic `get_cluster_config_tickers()` group (~206 names from `scripts/cluster_configs/*.yaml`, exchange-suffixed names left to their dedicated groups) into the stocks refresh — the same pattern as the existing `VAULT_BRAZIL_TICKERS` fix. All 13 frozen series backfilled to current via `add_ticker.py`.

Consequence for the first OOS table: Boutique advisory's OOS-WEAKENED (run on the 3 surviving names), ECPR's OOS-FAILED (2-name remnant after FSLY froze), US Memory's reading (without SNDK), and the zero-obs Animal health / Appliance rows were all corrupted-input artifacts. All affected cohorts were re-run on repaired inputs.

### Final OOS verdict table (2026-06-10, repaired inputs)

Full table: `investing/attachments/cluster-oos-validation-2026-06-10.txt`. Counts across 34 cohorts: 18 OOS-STRENGTHENING, 11 OOS-CONFIRMED, 3 OOS-WEAKENED, 1 OOS-FAILED, 1 INSUFFICIENT_HISTORY. All graded verdicts are PRELIMINARY (19-25 OOS obs vs the 40-obs bar); first non-preliminary readings land ~July 2026 for the May 3 batch.

Headline findings:

- ECPR (NET/AKAM/FSLY) is the framework's first genuine out-of-sample falsification, confirmed on full membership: in-sample intra-corr 0.444 → OOS −0.001 over 24 post-definition sessions, random-basket p = 0.69. The cohort passed every in-sample diagnostic (p = 0.0123, BH-pass) and then simply stopped existing on unseen data — exactly the failure mode the OOS pass was built to catch.
- Boutique advisory's cooling is real, not artifact: full 6 names, intra 0.724 → 0.530 (ratio 0.73), but still beats random at p = 0.0009 — a validated cluster descending from its May 1 print-event cohesion peak, not a falsification.
- Two falsified-in-sample cohorts cohere out-of-sample (tensions to watch, not verdict changes): Cybersecurity consolidation ratio 1.44 / p = 0.0091 and Animal health ratio 1.37 / p = 0.0143. AI hyperscalers scrapes OOS-CONFIRMED on ratio (1.06) but fails the OOS random-basket test (p = 0.079), consistent with its falsification. Mag 7 weakens further out-of-sample (ratio 0.73, p = 0.051) — consistent with falsified.
- Broad ratio inflation across the STRENGTHENING column (defense primes 1.33, core-6 1.54, Golden Dome 1.67, insurance carriers 1.40, brokers 1.35) indicates ambient market correlation rose in May-June 2026 (Hormuz, CPI anticipation); the OOS random-basket p is the control for this — those cohorts also beat random baskets on the same days at the p = 0.0001 floor, so they rose more than the tide.
- Korea Memory resolves to OOS-CONFIRMED (pair corr 0.801 post-definition, ratio 1.09, p = 0.0089); US Memory OOS-STRENGTHENING at full N=3 with SNDK restored (ratio 1.18, p = 0.0002). Only Global luxury (defined 05-28, 7 obs) remains INSUFFICIENT_HISTORY.

Operational footnote: the full re-run batch presumed dead mid-recovery was actually alive the whole time — a starved, block-buffered background process whose name (`python3.12`, the Windows Store shim) eluded a `Get-Process python` check. It was stopped cleanly via the harness task tools after the targeted recovery runs had already covered every repaired cohort; since it launched after the fixes, all its writes used repaired inputs and the registry stayed coherent. Lesson: judge background tasks by harness task state, not by process-name greps.

Item 5 status: COMPLETE. Open items remaining: 6 (synthetic-data regression tests), 7 (secondary fixes).

### Item 6 — synthetic-data regression tests (2026-06-10)

`tests/cluster_statistics_tests.py` (16 tests, ~3.5s, hermetic — no DB/network/git; wired into `npm run test:consistency`). The statistical layer previously had zero coverage, which is how the polluted null and p = 0.0 defects shipped silently. Now pinned to ground truth:

- Planted equicorrelation (rho 0.6, N=5, T=20k) recovered by `intra_correlation` within ±0.02; PC1 explained variance matches the closed form (1 + (N−1)ρ)/N; `pca_analysis` loadings positive and near-equal.
- Hierarchical clustering recovers a planted 2-block structure exactly; threshold-cut semantics exact on a hand-built correlation matrix (singletons below pair distance, two clusters at 0.4, one above cross distance); average-linkage join-distance topology matches hand arithmetic to 9 decimals.
- Phipson-Smyth p-values: floor exactly (k+1)/(n+1), never 0, ceiling 1.0; OOS `p_right_tail` returns nan on empty nulls.
- Random-basket machinery end-to-end calibration: a planted ρ=0.6 cohort hits the p-floor against an independent 40-name synthetic universe whose null distribution centers on 0; impossible observations return exactly 1.0; no spurious sample skips.
- Verdict bands (holdout STRENGTHENING/STABLE/WEAKENED/REGIME-DEPENDENT/INDETERMINATE; OOS grades + PRELIMINARY prefix) honor documented cut-points; `block_shuffle` permutation/bootstrap properties; `is_us_common_stock_ticker` accepts US names (incl. BRK-B) and rejects foreign suffixes, indices, futures, crypto pairs.

Item 6 status: COMPLETE. Open item remaining: 7 (secondary fixes — holdout sign alignment, zero-variance guards in `pca_analysis`/rolling loop, beta/vol-matched null variant, weekly-return cross-region check).

### Item 7 — secondary fixes (2026-06-10)

All four landed, each with regression tests (suite now 21 tests):

1. Holdout sign alignment (`cluster_holdout_test.loading_stability`): test-half PC1 loadings are flipped when their dot product with the train half is negative before correlating. A perfect factor match can no longer read as −1.0. Doc updated.
2. Zero-variance guards: `pca_analysis` aborts with a message naming the offending ticker(s) instead of dividing by zero; the 90-day rolling-tightness loop skips (and counts) windows containing a zero-variance series instead of crashing mid-history.
3. Vol-matched basket null (`--null vol-matched`, or `all`): each cohort member draws its null counterpart from the same realized-vol rank band (±5%, without replacement), so high-vol cohorts must beat comparably-volatile baskets rather than the large-cap-tilted pool. Registry gains `p_vol_matched_intra`/`p_vol_matched_pc1`. Empirical answer to Tier-3 finding 9 for the canonical case: Space pure-plays rejects even the vol-matched null at the Phipson-Smyth floor (p = 0.0001 at 10,000 draws; all three nulls floor-rejected in the regenerated artifact) — its cohesion is not just shared beta. The synthetic test pins the mechanism: when high vol and high correlation coincide in the pool, the matched null sits materially above the unmatched one (0.30 vs ~0.08 planted).
4. Weekly-return cross-check (`cluster_analysis.weekly_cross_check`, new `WEEKLY-RETURN CROSS-CHECK` section in results.txt): intra-corr/PC1 recomputed on calendar-week log returns; flags when the weekly reading exceeds daily by >0.10 (asynchronous-close depression — the cross-region cohort is tighter than daily numbers suggest). The regression test reproduces the exact geometry: a one-day lead-lag pair reads ~0 daily and ~0.8 weekly.

Item 7 status: COMPLETE.

### Audit ledger: all remediation items (1-7) CLOSED as of 2026-06-10

Tier 1-2 defects fixed and re-run; Tier 3 design limits addressed by the OOS pass (8), vol-matched null (9), weekly cross-check (10); N=2 cohorts (11) remain a documented caveat rather than a code change; test coverage (12) in place and wired to `npm run test:consistency`.

Standing follow-up BUILT 2026-06-10: `scripts/check_data_freshness.py` — per-ticker freshness audit (vault-actor + cluster-config tickers vs the latest SPY session, lag in trading sessions, foreign-calendar allowance, macro/index series excluded), wired into `/daily-scan` Phase 0 as audit script #5 (skill promoted to all three runtimes, parity clean). First live run found 51 stale tracked tickers — including Jefferies frozen since Mar 16, Masimo since Mar 23, and a 20-name wave frozen on exactly May 1 (Wayfair, Grab, Qualys, Tenable, Magna, Amkor, the Saudi ETF...) — far beyond the cluster-era sample. Bulk `add_ticker.py` backfill repaired 47; the 4 survivors were classified with verified sourcing on 2026-06-10 and added to `EXCLUDED_TICKERS`: FM = the iShares Frontier & Select EM ETF, liquidated 2025-01-09 per BlackRock/OCC notices — NOT First Quantum, which is alive under FM.TO with full current data (the actor note's ticker row carried the collision; fixed); NKLA = Nikola, bankrupt Feb 2025 (vault-recorded); HOUS = Anywhere Real Estate, acquired by Compass, closed Jan 2026 (vault-recorded; series ends 2026-01-05); CTRA = Coterra, merged into Devon Energy with close 2026-05-07 (vault-recorded; series ends that exact day). The structural gap is also closed: `get_vault_actor_tickers()` in `download_all_assets.py` (581 names — actor-note tickers already typed stock/equity/etf in metadata) joins the stocks refresh group alongside the cluster-config group, so backfilled names no longer re-freeze. Freshness audit after classification + group build: zero stale.

### Finding 3 closure + hardening pass (2026-07-01)

Three hardening items landed, closing the last structurally-open Tier-1 finding and two operational drifts flagged in the 2026-07-01 robustness re-assessment.

1. Finding 3 CLOSED — `scripts/cluster_boundary_sweep.py` (full-universe boundary sweep). For every name in the cleaned stock pool it computes the average-linkage join distance to the candidate cohort (`1 − mean(|corr|)` — exactly the height the name would join the candidate dendrogram at if added alone), plus its correlation to the cohort's standardized PC1 factor. Two reference points: the config threshold (≤ ⇒ merged at the cut) and the cohort's internal envelope (final internal merge; strictly inside ⇒ closer than the cohort's own loosest member). Verdicts BOUNDARY-CLEAN / PERMEABLE / CONTAMINATED; config controls reported as calibration rows, never contamination. Registry columns `boundary_*`; wired into the checklist (step 7) and required for new cluster notes alongside the p-value and threshold width. First live results: [[Space pure-plays]] PERMEABLE (5 of 1,050 below the 0.5 cut — KTOS, NNE, QBTS, UMAC, OKLO, i.e. the defense-tech/nuclear/quantum/drone speculative complex; none inside the 0.432 envelope), [[WFE]] PERMEABLE (45 below 0.5, led by MKSI 0.273, MPWR, ENTG, TER, AMKR; none inside the 0.217 envelope) — the WFE zero-width verdict is therefore genuinely "embedded in the semi complex", not a control-choice artifact, with the owning names now identified.

2. n_perm adequacy guard — `cluster_registry.py correction` now audits every row's Phipson-Smyth floor `1/(n_perm+1)` against the current Bonferroni cutoff (which tightens as the registry grows): UNRESOLVABLE when the floor exceeds the cutoff and resolution could decide the verdict (floor-pinned ⇒ INDETERMINATE, not fail), AT-RISK when floor-pinned within 2x of the cutoff, with the registry size at which each row becomes unresolvable and the minimum adequate n_perm. First pass caught 3 rows the manual scan missed or confirmed: 中特估 at 1k (floor 0.000999 > cutoff — already unresolvable), Coal miners + Infrastructure construction at 4k floor-pinned (unresolvable at N ≥ 200).

3. Under-resolved rows re-run at the 10k standard (8 cohorts, windows pinned so the change is resolution/pool only): Infrastructure construction 0.00025→0.0001 and Coal miners 0.00025→0.0001 (both were floor-truncated; true p at or below the 10k floor), Construction aggregates 0.0002→0.0012 (floor-pinned at 5k, resolved higher — drops off the strict-Bonferroni tier, stays FDR-clean), Packaging 0.0005→0.0020, Factory automation 0.0006→0.0033, Cable broadband 0.0020→0.0059, Grain processors 0.0027→0.0074, 中特估 0.0020→0.0018. No BH/FDR verdict changed. The upward drift on non-pinned rows is a pool-vintage effect, verified against the June 23 artifact: the eligible pool grew 1,121 → 1,213 names in the same pinned window because later sessions added whole tight cohorts to the DB with backfilled history — permutation p-values are pool-vintage-relative, and the registry stores them as measured. Note callouts updated (7 Sectors notes + [[China special valuation]], where the previously cited 中特估 p 0.0006 was a transcription error — no run ever produced it; registry read 0.0020 at 1k).

4. Pool hygiene (found BY the new sweep on its first live run — the dirty-pool RKLB sweep returned BOUNDARY-CONTAMINATED on ARKX, the ARK Space ETF, sitting inside the cohort envelope): `ticker_metadata.data_type` mislabels 152 pool members as `stock` — 84 ETFs (ARKX, EEM, BIL, SPYM, the AOA/AOK/AOM/AOR allocation family...), 66 mutual funds (AGTHX, DODGX...), 2 Yahoo FX pairs (USDJPY=X/JPYUSD=X) — because `add_ticker.py` defaults inserts to `stock` and the 2026-06-10 backfill was NULL-only by design, never re-checking existing labels. Every name was verified against Yahoo `instrumentType` (full TSV in session scratch; SPYM required a second pass — Yahoo intermittently returns EQUITY for it). Fixes within the query-time discipline: `is_us_common_stock_ticker` now rejects `=X` FX pairs and 5-letter-ending-X mutual-fund tickers (verified exact on this pool: all 66 funds match, zero equities do), and `scripts/universes/us_common_stocks.txt` was regenerated as a TWO-PASS Yahoo-verified 1,061-name snapshot (supersedes the 2026-06-09 file, which itself carried ITA/TLT/XAR). The 84 ETFs carry no ticker pattern, so until the metadata is corrected the DB-default pool remains ETF-contaminated — pass the snapshot file explicitly for a verified-clean run. PROPOSED (needs DB-mutation authorization per the repo's Gate 5): correct the 152 labels from the verification TSV, either via a `--verify` extension to `backfill_ticker_types.py` or a one-shot UPDATE. Bias direction: fund/ETF pollution inflates null cohesion, i.e. conservative for validations but anti-conservative for falsifications — the July 2026 quarterly capstone should re-baseline the registry against the clean pool before re-grading the 12 FDR-failers.

5. FDR dedup fix — `cluster_registry.py` deduped to the latest row per cohort BEFORE dropping p-less rows, so a newer partial-diagnostic row (boundary sweep, holdout-only) silently eclipsed the cohort's p-carrying row and removed it from the FDR set. Extracted as `latest_p_rows()` (drop-NaN-then-dedup) with a regression test. Retroactive effect: the corrected denominator is 114 p-carrying cohorts (some earlier counts, including the 2026-06-15 capstone's 83, were mildly understated by the same eclipse).

Regression suite: 21 → 31 tests (`tests/cluster_statistics_tests.py` — boundary-sweep join-distance arithmetic vs hand math, planted-outsider end-to-end, verdict bands, envelope, PC1-factor series, n_perm floor/adequacy statuses, mutual-fund/FX ticker filter, `latest_p_rows` eclipse). Post-fix correction over the live registry: 102/114 uncorrected == BH (zero expected false discoveries among passes), 58/114 Bonferroni, adequacy audit clean — no row's resolution is inadequate at the current N; the 10k standard resolves registries to N=500.
