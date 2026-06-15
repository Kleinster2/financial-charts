---
aliases: [Magnificent 7, Mag 7, M7]
tags: [concept/cluster, ai, mega-cap, equity]
---

# Mag 7 cluster

> [!failure] Cluster status: falsified as tradable basket (May 2026, re-confirmed May 11 with matched methodology)
> Intra-cluster correlation 0.316 (1Y window through 2026-05-07, threshold 0.5). PC1 explains only 41.82% of variance. Hierarchical clustering returns 6 effective singletons (NVDA joins the broader AI/semis cluster). Most damning: intra-advantage vs broad ETFs is NEGATIVE -0.215 — the Mag 7 names correlate MORE with broad market (QQQ/XLK/SPY at 0.531) than with each other (0.316). Factor decomposition: R² to SPY+QQQ+SMH+XLK is 85.4% — Mag 7 is essentially leveraged QQQ. Only 14.6% residual variance is a "Mag-7-specific factor." Use [[AI capex chain basket]] or specific subsets for AI exposure; Mag 7 as a basket adds no factor isolation. See [[Space pure-plays]] for what a validated cluster looks like (intra-corr 0.624, PC1 67.96%, 59.6% residual variance after benchmarks).
>
> OOS (preliminary, confirmed in the [[2026-06-15-cluster-validation-capstone|2026-06-15 capstone]]): the falsification holds out of sample — graded OOS-WEAKENED on post-definition data as the seven mega-caps continue to decohere (AI winners and laggards separating). The in-sample falsification and the post-definition data agree.

The seven largest US tech / mega-cap names — Apple, Microsoft, Alphabet, Amazon, Meta, NVIDIA, Tesla — are constantly discussed as a single entity in market commentary. The math says they are not. This note documents the falsification + the actual factor structure each name belongs to.

---

## What the math says

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation (1Y) | 0.33 (range 0.16-0.49) | Far below the 0.50 cluster floor |
| PC1 explained variance | 43.3% | Multi-factor cohort — no single dominant factor |
| Hierarchical clustering at 0.4 | ALL 7 names effectively singletons; NVDA migrates to AICX cluster | Cluster does not form |
| Cluster vs broad ETFs (QQQ/XLK/SMH/SPY) | 0.54 (NEGATIVE -0.21 advantage) | Mag 7 names trade with broad market MORE than each other |
| Cluster vs AI capex chain | 0.33 (+0.001 — basically zero) | No separation from the AICX cluster either |

PC1 loadings are wide (0.30-0.42) but the dispersion in pairwise correlations (0.16-0.49) means PC1 is capturing a generic mega-cap-tech beta that is shared with the broader market — not a Mag-7-specific factor.

### Pairwise correlations (1Y)

|  | AAPL | MSFT | GOOGL | AMZN | META | NVDA | TSLA |
|---|---|---|---|---|---|---|---|
| AAPL | — | — | — | — | 0.26 | 0.23 | 0.27 |
| MSFT | — | — | 0.17 | 0.34 | 0.27 | 0.37 | 0.32 |
| GOOGL | — | 0.17 | — | 0.41 | 0.35 | 0.31 | 0.39 |
| AMZN | — | 0.34 | 0.41 | — | 0.49 | 0.35 | 0.39 |
| META | 0.26 | 0.27 | 0.35 | 0.49 | — | 0.41 | 0.38 |
| NVDA | 0.23 | 0.37 | 0.31 | 0.35 | 0.41 | — | 0.47 |
| TSLA | 0.27 | 0.32 | 0.39 | 0.39 | 0.38 | 0.47 | — |

Tightest pair: AMZN-META = 0.49. Loosest: MSFT-GOOGL = 0.17 (the two most-frequently-paired names in cloud-wars commentary correlate barely above noise).

---

## What each name actually trades with

When the algorithm is given the Mag 7 cohort plus a wider universe (AI capex chain, broad ETFs, semi peers), the hierarchical clustering at 0.4 places each name in a different cluster:

| Name | Algorithmic placement | Dominant idiosyncratic factor |
|---|---|---|
| AAPL | Singleton | iPhone cycle + China exposure + AI Apple-Intelligence rollout |
| MSFT | Singleton | Cloud share, OpenAI partnership terms, Copilot monetization |
| GOOGL | Singleton | Search vs AI-answer cannibalization, antitrust (Search remedy) |
| AMZN | Singleton | E-commerce margins, AWS share losses to Azure, retail-vs-cloud weighting |
| META | Singleton | Ad market exposure, Reels/TikTok competition, Reality Labs burn |
| NVDA | **Joins [[AI capex chain basket]]** with TSM/ASML/AMAT/KLAC/LRCX/MU + broad semi ETFs | AI accelerator demand cycle |
| TSLA | Singleton | EV cycle, China demand, FSD / robotaxi narrative, Musk political volatility |

Six singletons + one defection to AICX. The "cluster" does not exist at the equity-return level.

---

## Why the framing persists despite the math

- Index-construction effects: the 7 names dominate market-cap-weighted indices (SPY, QQQ), so their COMBINED contribution to index returns is high — but that's a weighting effect, not a cluster signal. The names move with the index because they ARE the index.
- Narrative bundling: AI infrastructure capex story is real and concentrated in these names + their suppliers. But each name's exposure to the AI thesis differs substantially.
- Performance correlation in DRAWDOWNS: in broad risk-off events, the names sell off together — but that's broad-market beta, not Mag-7-specific factor.
- Earnings sequencing: all 7 report in roughly the same 2-week window each quarter, creating apparent co-movement around earnings season.

None of these is a structural factor. The math is unambiguous: there is no Mag 7 cluster at the equity-return level.

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long Mag 7 basket (equal-weighted) | Inferior to long QQQ — Mag 7 is the dominant constituent of QQQ; basket adds no factor isolation |
| Long Mag 7 / short SPY | Captures only mega-cap factor (already priced in QQQ-SPY spread) |
| Long Mag 7 / short XLK | Same — Mag 7 dominates XLK weighting |
| Long [[AI capex chain basket]] for AI exposure | Cleaner expression — NVDA + AI capex chain captures the AI factor without the 6 idiosyncratic mega-cap stories |
| Pair trades within Mag 7 (e.g., long MSFT short GOOGL on AI cloud) | Captures idiosyncratic story differentials, not factor differentials |

The math says: you cannot construct a "Mag 7 long-short" trade that isolates a meaningful factor. The factor doesn't exist.

---

## Why this finding matters

This is the most important falsification in the validation pass — Mag 7 is the most-discussed cluster in markets. The math says it is a media construct, not a tradable cluster. Three implications:

- Stop interpreting "Mag 7 led the market today" as a unified signal — it's just the largest names by weight contributing to index moves.
- Stop comparing companies against Mag 7 averages as if there's a factor to compare against. The names are too disparate.
- Use [[AI capex chain basket]] for AI exposure; use [[AI hyperscalers]] thesis as the framework for the demand-side story (not a tradable cluster).

---

## Matched-methodology re-validation (May 11, 2026)

Re-ran the diagnostic with methodology matched to [[Space pure-plays]] (1Y window through 2026-05-07, threshold 0.5) so the result is directly comparable to the canonical validated cohort. Falsification confirmed across every dimension.

### Stability across windows

| Window | Obs | Intra-corr | Range | PC1 | PC2 | Vs SPY | Gap |
|---|---|---|---|---|---|---|---|
| 3Y | 335 | 0.470 | [0.36, 0.63] | 57.2% | 14.9% | 0.896 | -0.426 |
| 2Y | 231 | 0.486 | [0.29, 0.60] | 59.5% | 11.5% | 0.913 | -0.427 |
| 1Y | 175 | 0.316 | [0.08, 0.46] | 46.6% | 14.1% | 0.863 | -0.547 |
| YTD 2026 | 88 | 0.324 | [0.09, 0.55] | 45.8% | 14.8% | 0.874 | -0.550 |

Two structural reads:

1. The cohort is loosening, not tightening. 2-3 year ago Mag 7 had marginal cluster cohesion (intra-corr 0.47-0.49, PC1 57-60%) — still below validated-cluster thresholds but not by much. Over the past year the cohort has decoupled materially: intra-corr dropped from 0.48 to 0.32, PC1 from 59.5% to 46.6%. The opposite trajectory from [[Space pure-plays]] (tightening from 0.48 to 0.64 over the same window).
2. The cluster-vs-SPY gap is consistently large and negative across all windows (-0.43 to -0.55). The Mag 7 names have always been MORE correlated with SPY than with each other — even in the period when their internal cohesion was strongest. This is the textbook signature of names that ARE the market rather than names that cluster within it.

### Factor decomposition — Mag 7 is leveraged QQQ

Regressing the equal-weighted Mag 7 basket against four major benchmarks over the 1Y window:

| Factor | Beta | Read |
|---|---|---|
| SPY | -0.127 | Slightly negative (small-cap exposure offset) |
| QQQ | +1.835 | Heavy leveraged QQQ beta — the dominant factor |
| SMH | -0.252 | Slightly negative |
| XLK | -0.199 | Slightly negative |

R² to all four benchmarks combined: 85.4%. Residual variance (Mag-7-specific factor): only 14.6%.

Comparison to [[Space pure-plays]] factor decomposition: Space pure-plays had R² of 40.4% to SPY+IWM+ITA → 59.6% pure-play factor. Mag 7 has R² of 85.4% to broad-market benchmarks → 14.6% specific factor. Space pure-plays has roughly 4x the cohort-specific factor share that Mag 7 does. The cleanest possible expression of "Mag 7 is not a cluster": after stripping out broad-market exposure, there's almost nothing left.

Per-name R² to QQQ alone:

| Ticker | R² to QQQ |
|---|---|
| NVDA | 48.1% |
| AMZN | 42.2% |
| TSLA | 38.8% |
| GOOGL | 37.4% |
| META | 28.9% |
| AAPL | 24.2% |
| MSFT | 21.3% |

NVDA is the most-QQQ-correlated single name. AAPL and MSFT — the two largest by market cap — are surprisingly LEAST correlated with QQQ despite dominating QQQ by weight. The mega-cap weighting effect creates a circular dependency where the names that drive QQQ aren't well-explained by QQQ at the daily-return level.

### PC2 — AI-narrative vs EV/non-AI sleeve

PC2 captures 14% of variance with cleanly separating loadings:

| Ticker | PC2 loading | Sleeve |
|---|---|---|
| META | +0.69 | AI-narrative |
| NVDA | +0.17 | AI-narrative |
| AMZN | +0.16 | AI-narrative |
| MSFT | +0.11 | AI-narrative |
| AAPL | -0.03 | Neutral |
| GOOGL | -0.23 | EV/non-AI |
| TSLA | -0.64 | EV/non-AI |

META's +0.69 and TSLA's -0.64 are the extreme loadings — they're at opposite ends of PC2. The cleanest interpretation: PC2 separates AI-narrative names (META Reality Labs + NVDA chips + AMZN AWS + MSFT Copilot) from EV/non-AI names (TSLA EV cycle + GOOGL search-disruption defense). AAPL is neutral.

### PC3 — Chips/compute vs ad/commerce platforms

PC3 captures 12% of variance:

| Ticker | PC3 loading | Sleeve |
|---|---|---|
| NVDA | +0.57 | Chips/compute |
| MSFT | +0.29 | Chips/compute |
| TSLA | +0.14 | Neutral |
| META | -0.13 | Platforms |
| AAPL | -0.18 | Neutral |
| AMZN | -0.50 | Platforms |
| GOOGL | -0.53 | Platforms |

PC3 separates AI infrastructure / chip exposure (NVDA + MSFT cloud + Azure GPU rentals) from ad/commerce platforms (AMZN retail+AWS, GOOGL search+ads, META social ads). NVDA's +0.57 is the highest loading.

The two PCs together describe the Mag 7's actual sub-structure: PC2 is "is this an AI story" and PC3 is "is this a chips/compute story or a platform story." Each name maps somewhere on this 2D space, and the cohort spreads out — confirming that the Mag 7 is structurally heterogeneous.

### Within-Mag-7 subset optimization

If Mag 7 doesn't cluster as a 7-name basket, does any 2-name subset cluster? Ranked all 21 pairs by intra-correlation:

| Rank | Pair | Intra-corr | Sharpe | Cum return |
|---|---|---|---|---|
| 1 | NVDA + TSLA | 0.462 | 1.45 | +39.6% |
| 2 | AMZN + META | 0.445 | -0.11 | -2.2% |
| 3 | GOOGL + AMZN | 0.432 | 2.19 | +46.2% |
| 4 | META + NVDA | 0.429 | 0.21 | +4.5% |
| 5 | GOOGL + TSLA | 0.406 | 2.22 | +58.6% |
| 6 | MSFT + NVDA | 0.386 | 0.49 | +9.1% |
| 7 | AMZN + TSLA | 0.386 | 1.27 | +30.7% |
| ... | ... | ... | ... | ... |
| 19 | MSFT + GOOGL | 0.080 | 1.53 | +23.9% |
| 20 | AAPL + MSFT | 0.161 | 0.31 | +4.0% |
| 21 | AAPL + NVDA | 0.225 | 1.72 | +31.2% |

The single tightest pair (NVDA-TSLA at 0.462) is BELOW the 0.50 cluster floor — the "Musk-loved" pair (NVDA on AI dominance + TSLA on AI/robotics narrative) doesn't even reach cluster status. No 2-name subset clusters.

Bottom pairs are diagnostic: MSFT-GOOGL at 0.080 means the two most-frequently-paired names in "cloud wars" commentary correlate barely above noise. AAPL-MSFT at 0.161 — the two largest names by market cap — also don't co-move. The mega-cap-tech bucket is structurally heterogeneous.

By Sharpe (different optimization objective): GOOGL+TSLA = 2.22, GOOGL+AMZN = 2.19, AAPL+NVDA = 1.72 — best Sharpe pairs don't overlap with tightest-correlation pairs. The objective decomposition lesson from [[Space pure-plays#Best Sharpe 2-name pair — diversification beats factor-tracking|the cohort note]] applies here too: factor-tracking ≠ Sharpe-optimal.

### Cross-cohort comparison

Putting Mag 7 on the same diagnostic axis as the validated vault clusters (matched methodology — 1Y window through 2026-05-07, threshold 0.5):

| Cluster | N | Avg intra-corr | PC1 variance | Verdict |
|---|---|---|---|---|
| [[WFE]] | 4 | 0.804 | 85.33% | Validated — tightest cluster |
| [[Korea Memory]] | 2 | 0.756 | 87.82% | Validated (pair) |
| [[US Memory]] | 3 | 0.696 | 79.72% | Validated |
| [[Space pure-plays]] | 7 | 0.624 | 67.96% | Validated — densest large-N |
| [[AI Compute]] | 3 | 0.600 | 73.37% | Validated |
| Mag 7 (this note) | 7 | 0.316 | 46.63% | FALSIFIED |

Mag 7's 0.316 intra-correlation is roughly half of Space pure-plays' 0.624 at the same N. Mag 7's PC1 (46.63%) is below the 50% single-factor threshold; Space pure-plays' (67.96%) is well above. The two N=7 cohorts are on opposite sides of the validated/falsified line. The contrast underscores that cohort size (N=7) alone doesn't determine cluster structure — the underlying business-model coherence does.

*Diagnostic source: `python scripts/cluster_analysis.py --config scripts/cluster_configs/mag7.yaml` + `python scripts/mag7_full_analysis.py`, May 11 2026 with methodology matched to [[Space pure-plays]].*

---

## Cluster validation compliance addendum (2026-06-07)

Generated from `scripts/cluster_configs/mag7.yaml` using `scripts/cluster_analysis.py` methodology. The 1Y diagnostic window is 2025-05-09 to 2026-05-08 (174 observations); the rolling history starts at `2020-01-01` where data are available.

### Required validation plots

![[mag7-cluster-correlation-1y.png]]

*One-year correlation heatmap for the `Mag 7` validation universe.*

![[mag7-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree using average linkage on distance `1-|corr|`.*

![[mag7-cluster-pca-1y.png]]

*PCA diagnostic for the candidate cohort; PC1 explains 41.7% of standardized daily-return variance.*

### PC1 index weights vs cluster topology

The topology table answers which names join the tree first or last. The raw PC1-mimic table answers which raw-return weights best replicate the standardized common factor after realized-volatility scaling. These are deliberately different readings of the same cluster.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---|---|---|---|---|
| 1 | NVDA | TSLA | 0.537 | Tightest merge |
| 2 | AMZN | META | 0.554 | Candidate cohort merge step |
| 3 | NVDA+TSLA | AMZN+META | 0.629 | Candidate cohort merge step |
| 4 | GOOGL | NVDA+TSLA+AMZN+META | 0.667 | Candidate cohort merge step |
| 5 | MSFT | GOOGL+NVDA+TSLA+AMZN+META | 0.725 | Candidate cohort merge step |
| 6 | AAPL | MSFT+GOOGL+NVDA+TSLA+AMZN+META | 0.749 | Final cohort join / loosest boundary |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| AAPL | 0.306 | 11.66% | 22.01% | 16.46% |
| MSFT | 0.319 | 12.14% | 26.31% | 14.34% |
| GOOGL | 0.352 | 13.39% | 28.71% | 14.49% |
| AMZN | 0.421 | 16.01% | 30.46% | 16.33% |
| META | 0.392 | 14.91% | 36.51% | 12.69% |
| NVDA | 0.411 | 15.64% | 35.33% | 13.76% |
| TSLA | 0.426 | 16.23% | 42.26% | 11.93% |

Interpretation: use the dendrogram / join-distance topology to identify the tight core and later-joining members; use the Raw PC1-mimic weight column only for investable factor-replication sizing.

### Historical tightness evolution

![[mag7-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling tightness diagnostic: avg intra-correlation, PC1 share, core correlation, satellite-to-core correlation, and final candidate join distance.*

| Year | Avg corr median | PC1 median | Core corr median | Satellite-to-core median | Final join distance median |
|---|---|---|---|---|---|
| 2021 | 0.593 | 66.1% | 0.557 | 0.685 | 0.578 |
| 2022 | 0.625 | 68.9% | 0.600 | 0.686 | 0.560 |
| 2023 | 0.610 | 67.1% | 0.592 | 0.639 | 0.536 |
| 2024 | 0.424 | 52.4% | 0.461 | 0.359 | 0.747 |
| 2025 | 0.639 | 69.4% | 0.629 | 0.664 | 0.452 |
| 2026 | 0.301 | 40.7% | 0.326 | 0.238 | 0.793 |

Latest 90D through 2026-05-08: avg corr 0.324, PC1 42.6%, core corr 0.352, satellite-to-core corr 0.254, final join distance 0.746.

Historical verdict: regime-dependent / fragmenting cluster; current rolling cohesion is below durable-cluster thresholds.

---

## Related

- [[AI hyperscalers]] — the 5-name subset (MSFT, GOOGL, AMZN, META, ORCL) that also failed cluster validation
- [[AI capex chain basket]] — where NVDA actually clusters; the validated AI tradable basket
- [[Apple]] — Mag 7 member
- [[Microsoft]] — Mag 7 member
- [[Google]] — Mag 7 member
- [[Amazon]] — Mag 7 member
- [[Meta]] — Mag 7 member
- [[NVIDIA]] — Mag 7 member; clusters with [[AI capex chain basket]]
- [[Tesla]] — Mag 7 member
- `docs/cluster-validation.md` — methodology
- `scripts/cluster_configs/mag7.yaml` — config for this test

*Created 2026-05-03 — falsified-cluster note documenting the most widely-discussed market construct that fails statistical validation*
