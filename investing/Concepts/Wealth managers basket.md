---
aliases: [WLTHMGR, Wealth manager basket, Retail wealth platforms]
tags: [basket/internal, wealth-management, advisory]
---

# Wealth managers basket

> [!warning] Cluster status: partial validation (May 2026)
> Intra-cluster correlation 0.50 (just at the floor), PC1 64.3%. Hierarchical clustering at 0.4 returns 3-name tight core (SCHW, RJF, LPLA); SF is singleton with weaker PC1 loading (0.33 vs 0.53-0.56 for the others). The 3-name tight core is the cleanly tradable sub-basket; SF tracks separately. Cluster vs insurance brokers: +0.39 advantage — completely uncorrelated despite both being "fee-income financial services." See "Cluster validation" section below.

The mathematically-validated public retail-and-advisor wealth management cohort. Surfaced as one of the two sub-clusters when [[AI financial disintermediation basket]] (AIFD, 10-name combined cohort) failed cluster validation: AIFD splits cleanly into insurance brokers + wealth managers, which trade as two completely separate factors despite sharing the AI-disruption narrative.

The 4-name candidate cohort partially validates: SCHW + RJF + LPLA form a tight 3-name core (intra ~0.69), SF is a borderline singleton with substantially weaker factor loading. Treat the 3-name core as the tradable basket; SF as adjacent.

---

## Constituents

3-name tight core + SF as adjacency.

| Ticker | Company | PC1 loading | Tier |
|--------|---------|-------------|------|
| SCHW | [[Charles Schwab]] | 0.544 | Tight core |
| RJF | [[Raymond James]] | 0.559 | Tight core |
| LPLA | [[LPL Financial]] | 0.533 | Tight core |
| SF | [[Stifel Financial]] | 0.329 | Adjacency (singleton at 0.4 threshold; mid-IB exposure differs from pure retail wealth) |

Total: 4 candidates; 3-name tight core. Internal ticker proposal: WLTHMGR.

### Why each name belongs

- [[Charles Schwab]] — largest US retail brokerage + advisor custodian; bank holding company structure; net interest income exposure
- [[Raymond James]] — full-service broker + advisor (RJFS); also has investment-banking and asset-management businesses
- [[LPL Financial]] — pure-play independent broker-dealer / advisor custody platform; recurring fee revenue
- [[Stifel Financial]] — full-service brokerage + investment bank + capital markets; mid-IB exposure makes it a partial fit (also surfaced as standalone in [[Boutique advisory consolidation]] mid-IB controls)

### Excluded — and why

| Excluded | Why excluded |
|----------|--------------|
| Insurance brokers (WTW, AJG, AON, BRO, MMC) | The OTHER half of AIFD. Different end-market (commercial vs retail). Cluster correlation 0.09 = essentially uncorrelated. See [[Insurance brokers basket]]. |
| Alt asset managers (BX, KKR, OWL) | Capital allocation, not retail distribution. See [[Alternative asset managers basket]]. Cluster correlation 0.44 — moderate but well below intra-cluster floor. |
| Traditional asset managers (BLK, TROW, BEN) | Manufacturing of products, not distribution platforms. Cluster correlation 0.42 — moderate. |
| Execution platforms ([[Interactive Brokers]], [[Robinhood]]) | No advisory layer; pure execution. Cluster correlation 0.39 — moderate; algorithmically clustered with SPY (broad market beta). |
| Banks (XLF) | Diversified financials; cluster correlation 0.46 — moderate. |

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/wealth_managers.yaml`. Full standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.503 (range 0.27-0.73) | At the cluster floor; SF drags the 4-name average; tight 3-name core is ~0.69 |
| Tightest pair | SCHW-RJF = 0.73 | Two largest full-service platforms |
| 3-name tight core intra-corr | ~0.69 (SCHW + RJF + LPLA) | Strong sub-cohesion |
| PC1 explained variance | 64.3% | Dominant single factor; SF loads weaker |
| Hierarchical clustering at 0.4 | SCHW + RJF + LPLA cluster; SF singleton | 3-name boundary clean |
| Cluster vs insurance brokers | 0.113 (+0.390 advantage) | Cleanest separation in financial services |
| Cluster vs alt asset managers | 0.441 (+0.063 advantage) | Small separation |
| Cluster vs traditional asset managers | 0.417 (+0.087 advantage) | Small separation |
| Cluster vs broad ETFs | 0.458 (+0.045 advantage) | Marginal separation — wealth platforms share more broad-market beta than insurance brokers do |

### Pairwise correlations (1Y, 4-name candidate cohort)

|  | SCHW | RJF | LPLA | SF |
|---|---|---|---|---|
| SCHW | — | 0.73 | 0.67 | 0.27 |
| RJF | 0.73 | — | 0.67 | 0.38 |
| LPLA | 0.67 | 0.67 | — | 0.30 |
| SF | 0.27 | 0.38 | 0.30 | — |

Pairwise structure shows the same pattern as the dendrogram: SCHW + RJF + LPLA form a tight triangle (0.67-0.73 across all 3 pairs), while SF correlates 0.27-0.38 with the others. The 3-name tight core (intra ~0.69) is the validated tradable cluster; SF is a related but distinct name.

### Why SF is singleton at this threshold

[[Stifel Financial]] has substantial investment banking + capital markets exposure (~25-30% of revenue) on top of its wealth management business. The mid-IB / capital markets factor pulls SF away from pure retail-wealth co-movement. SF surfaced as a standalone in the [[Boutique advisory consolidation]] mid-IB controls test as well — it doesn't cluster cleanly with either pure boutique advisory or pure retail wealth, sitting in between.

---

## YTD 2026 cohort tracking

![[wealth-mgr-basket-2026ytd-price-chart.png]]

*SCHW (blue, primary) vs RJF, LPLA, SF normalized from 2025-12-31. The 3-name tight core (SCHW, RJF, LPLA) tracks visibly together through the Q1 2026 sentiment swings — including the Feb 10 Altruist selloff and recovery. SF's path is visibly more independent, consistent with its singleton status.*

---

## Trade implications

| Trade | Expression | Factor isolated |
|---|---|---|
| Long retail wealth platform factor | Equal-weighted SCHW + RJF + LPLA | Retail wealth distribution / advisor-custody economics |
| Long with adjacency | Add SF (mid-IB exposure included) | Broader wealth+IB sentiment; loosens factor |
| Pair: long wealth managers / short insurance brokers | WLTHMGR vs INSBROK basket | The two AIFD halves trade independently — captures cross-sub-sector factor differential |
| Pair: long wealth managers / short broad market | WLTHMGR vs SPY | Smaller advantage (+0.05) — wealth platforms have more broad-market beta than insurance brokers |
| AVOID: long WLTHMGR / short XLF | Marginal +0.04 advantage; near zero |

---

## Why the cluster works (3-name tight core)

Retail wealth management platforms share business-model exposure:
- Net interest income from sweep deposits (SCHW especially) + fee-based advisor revenue
- AUM growth tied to equity-market beta (asset levels drive fees) + advisor headcount
- Switching costs from advisor relationships and ACAT (account transfer) friction
- Same end-market sensitivity (US retail investor flows, advisor M&A activity)
- Shared exposure to interest-rate cycle (sweep deposit spreads, NII)
- Comparable advisory-revenue margin structures (~30-50% pretax margin)

Different scale, similar economics. SCHW dwarfs RJF and LPLA in size but trades on the same factor.

---

## What could break the cluster

| Scenario | Effect on cluster |
|---|---|
| AI advisory tools (Altruist Hazel, ChatGPT-style planners) penetrate retail | All 3 names re-rate together; cluster cohesion increases on the way down |
| Sustained Fed cuts (NII compression at SCHW) | SCHW decouples from RJF/LPLA — SCHW has heaviest NII exposure |
| LPLA acquired by larger platform | Acquirer + LPLA both decouple around deal-noise |
| Crypto / alts replace traditional advisor channels | All 3 names re-rate; potential decoupling vs IBKR/HOOD execution platforms |
| Mid-IB cycle recovery (deal volume up) | SF re-couples to wealth manager core via revenue-mix improvement |

---

## Tracking

- Re-run validation quarterly: `python scripts/cluster_analysis.py --config scripts/cluster_configs/wealth_managers.yaml`.
- Watch SF's PC1 loading — if it rises above 0.45, SF re-joins tight core.
- Watch SCHW idiosyncratically — its size + NII exposure could pull it out of cluster on rate cycle.
- Cross-check vs [[Insurance brokers basket]] — if cross-cluster correlation rises, AIFD parent narrative is re-asserting.

---

## Cluster validation compliance addendum (2026-06-07)

Generated from `scripts/cluster_configs/wealth_managers.yaml` using `scripts/cluster_analysis.py` methodology. The 1Y diagnostic window is 2025-05-01 to 2026-04-30 (171 observations); the rolling history starts at `2020-01-01` where data are available.

### Required validation plots

![[wealth-mgr-cluster-correlation-1y.png]]

*One-year correlation heatmap for the `Wealth managers basket` validation universe.*

![[wealth-mgr-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree using average linkage on distance `1-|corr|`.*

![[wealth-mgr-cluster-pca-1y.png]]

*PCA diagnostic for the candidate cohort; PC1 explains 64.3% of standardized daily-return variance.*

### PC1 index weights vs cluster topology

The topology table answers which names join the tree first or last. The raw PC1-mimic table answers which raw-return weights best replicate the standardized common factor after realized-volatility scaling. These are deliberately different readings of the same cluster.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---|---|---|---|---|
| 1 | SCHW | RJF | 0.269 | Tightest merge |
| 2 | LPLA | SCHW+RJF | 0.330 | Candidate cohort merge step |
| 3 | SF | LPLA+SCHW+RJF | 0.684 | Final cohort join / loosest boundary |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| SCHW | 0.543 | 27.65% | 24.46% | 34.17% |
| RJF | 0.559 | 28.44% | 25.06% | 34.30% |
| LPLA | 0.533 | 27.12% | 36.24% | 22.62% |
| SF | 0.330 | 16.78% | 56.90% | 8.91% |

Interpretation: use the dendrogram / join-distance topology to identify the tight core and later-joining members; use the Raw PC1-mimic weight column only for investable factor-replication sizing.

### Historical tightness evolution

![[wealth-mgr-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling tightness diagnostic: avg intra-correlation, PC1 share, core correlation, satellite-to-core correlation, and final candidate join distance.*

| Year | Avg corr median | PC1 median | Core corr median | Satellite-to-core median | Final join distance median |
|---|---|---|---|---|---|
| 2021 | 0.745 | 81.0% | 0.782 | 0.714 | 0.286 |
| 2022 | 0.774 | 83.1% | 0.815 | 0.750 | 0.253 |
| 2023 | 0.742 | 80.8% | 0.802 | 0.706 | 0.310 |
| 2024 | 0.556 | 67.9% | 0.559 | 0.556 | 0.605 |
| 2025 | 0.805 | 85.4% | 0.811 | 0.777 | 0.242 |
| 2026 | 0.492 | 64.3% | 0.416 | 0.567 | 0.732 |

Latest 90D through 2026-04-30: avg corr 0.524, PC1 67.1%, core corr 0.460, satellite-to-core corr 0.588, final join distance 0.727.

Historical verdict: structurally durable cluster; rolling cohesion has usually stayed in single-factor territory.

---

## Related

### Member actors

- [[Charles Schwab]] — tight core
- [[Raymond James]] — tight core
- [[LPL Financial]] — tight core
- [[Stifel Financial]] — adjacency (singleton at 0.4)

### Adjacent concept notes

- [[AI financial disintermediation basket]] — parent (10-name AIFD that splits into this basket + insurance brokers)
- [[Insurance brokers basket]] — the other half of AIFD; opposite cluster (cluster correlation 0.09)
- [[Alternative asset managers basket]] — sibling validated cluster (different business model: origination vs distribution)
- [[Boutique advisory consolidation]] — sibling validated cluster (different business model: M&A advisory; SF is a standalone there too)
- [[Altruist wealth management selloff February 2026]] — Feb 10 catalyst that revealed the cluster
- [[AI disintermediation]] — thesis driving the AI-narrative leg

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/wealth_managers.yaml` — config for this cluster

*Created 2026-05-03 — fifth concept note created under the new cluster-validation standard*
