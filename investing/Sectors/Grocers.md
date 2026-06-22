---
aliases: [Grocers, Supermarkets, Grocery retail, Grocers cohort, Food retail]
tags: [sector, consumer-staples, grocery, retail, cluster-validation]
---

# Grocers

> [!failure] Cluster status: falsified — grocers do not trade as one factor; the only structure is the blocked Kroger–Albertsons merger pair (Jun 2026)
> The listed supermarket operators ([[Kroger|KR]]/[[Albertsons|ACI]]/[[Sprouts Farmers Market|SFM]]/[[Grocery Outlet|GO]]) do NOT cohere — intra-corr 0.293 (weekly 0.193, lower), PC1 only 48%, and the cohort FAILS to reject the random-basket null (p 0.106) and the vol-matched null (p 0.095): the four are no more cohesive than a random 4-pick of comparable names. This is a grade-1 falsification (pure dispersion). The only real structure is [[Kroger|KR]]+[[Albertsons|ACI]] (join 0.352), and that pair cohered on merger arbitrage — their proposed combination was blocked by the courts/FTC in December 2024 — not on a grocery factor; [[Sprouts Farmers Market|SFM]] and [[Grocery Outlet|GO]] are idiosyncratic singletons ([[Grocery Outlet|GO]] barely loads, PC1 0.265). Thin-margin grocery is a set of single-name stories (merger saga, premium-format growth, deep-value model), not an ownable factor — even the staples ETF [[XLP]] does not cluster with them.

The anti-factor of food retail. Grocery is a low-margin, operationally idiosyncratic business: Kroger and Albertsons spent two years in a merger saga (and now litigation), Sprouts is a high-growth premium-natural-foods format, and Grocery Outlet is an extreme-value closeout operator on an independent-operator model. Those are four different stories with little common driver — which is exactly why the cohort fails the random-basket null. There is no grocery factor to own.

## Sector performance

![[grocers-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[XLP]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is four listed supermarket operators — [[Kroger|KR]], [[Albertsons|ACI]], [[Sprouts Farmers Market|SFM]], [[Grocery Outlet|GO]] — tested against consumer staples (XLP), retail (XRT), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.293 [0.068–0.648] | far below the 0.50 floor; weekly 0.193 (lower) |
| PC1 explained variance | 48.3% | below 50% with big PC2 (25%) — multi-factor |
| Independence null p | 0.0001 | series co-move at all (necessary, not sufficient) |
| Random-basket null p | 0.106 | FAILS — no more cohesive than a random 4-pick (grade-1) |
| Vol-matched null p | 0.095 / 0.092 | FAILS — confirms pure dispersion |
| Holdout (2Y split) | STABLE 0.99 | "stable" only because it is consistently weak (train 0.289 → test 0.287) |
| Threshold stable width | 0.00 (none) | never a clean cluster |
| Intra-adv vs ETFs (XLP/XRT/SPY) | +0.148 | weakly above retail/staples beta, but the cohort itself doesn't cohere |

All US-listed. Config: `scripts/cluster_configs/kr.yaml`; registry row 2026-06-20.

### Boundary — only KR+ACI cluster; SFM and GO are singletons

![[grocers-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Only [[Kroger|KR]]+[[Albertsons|ACI]] form a pair (the blocked-merger arbitrage); [[Sprouts Farmers Market|SFM]] and [[Grocery Outlet|GO]] are singletons, and the staples ETF [[XLP]] sits on its own (the grocers don't even cluster with broad staples). Four proposed names, no grocery cluster.*

The cohort fails the random-basket and vol-matched nulls — the decisive grade-1 falsification signal — so the four grocers are statistically indistinguishable from a random pick of comparable names. The threshold scan never returns them as a clean cluster. The only structure ([[Kroger|KR]]+[[Albertsons|ACI]]) is an event (the merger and its blocking), not a sector factor.

### Topology — a merger pair plus two singletons

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | KR + ACI | 0.352 | the only pair — merger-arb, not a grocery factor |
| 2 | SFM + (KR+ACI) | 0.685 | the premium-format name joins far above the cut |
| 3 | GO + core | 0.840 | the deep-value name barely connects at all |

Only KR+ACI join below the 0.5 cut. [[Sprouts Farmers Market|SFM]] (0.685) and [[Grocery Outlet|GO]] (0.840) join far above it — singletons in practice. PC1 explains only 48% with a huge PC2 (25%) — a genuinely multi-factor (or no-factor) set.

### PC1 index weights

![[grocers-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 48.3% (weekly 47.5%) with a large PC2 (25%) — the signature of a non-cluster.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| KR | 0.584 | 30.4% | 28.7% | 38.6% |
| ACI | 0.616 | 32.1% | 32.2% | 36.3% |
| SFM | 0.457 | 23.8% | 52.4% | 16.5% |
| GO | 0.265 | 13.8% | 58.6% | 8.6% |

The merger pair ([[Kroger|KR]]/[[Albertsons|ACI]]) carries almost all the PC1 weight; [[Grocery Outlet|GO]] barely loads (0.265) — it is essentially orthogonal to the others.

### Distinctness — not even a coherent cohort to be distinct

![[grocers-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A warm KR/ACI corner; SFM and GO are cool against everything, including each other.*

The +0.148 intra-advantage versus the ETFs is moot: the cohort fails the random-basket null, so there is no grocery factor to be distinct in the first place. The only warm cell ([[Kroger|KR]]–[[Albertsons|ACI]]) is merger-driven. Grocery is a sector where stock-specific events and formats dominate, leaving no shared factor — the consumer-staples analogue of the [[Theatrical exhibition]] result (a shared end-market, not a shared factor).

### Historical tightness evolution

![[grocers-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Loose throughout (0.22–0.51), decohering after 2023.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.421 | 58.2% |
| 2022 | 0.422 | 59.6% |
| 2023 | 0.514 | 64.2% |
| 2024 | 0.221 | 42.1% |
| 2025 | 0.266 | 45.8% |
| 2026 | 0.283 | 50.7% |

Latest 90-day reading: intra 0.294, PC1 51.9%. Grocers were modestly correlated during the 2021–23 inflation/merger-news window and have decohered since to ~0.22–0.29 — the holdout's STABLE 0.99 just means it is consistently weak, not that a factor persists. There is no ownable grocery factor; the names trade on their own events and formats.

## Related

- [[Kroger]], [[Albertsons]] — the blocked-merger pair (the only structure)
- [[Sprouts Farmers Market]], [[Grocery Outlet]] — the idiosyncratic singletons
- [[Theatrical exhibition]] — the analogue (shared end-market, not a shared factor; fails the random-basket null)
- [[XLP]] — the staples ETF the grocers do not cluster with
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/kr.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
