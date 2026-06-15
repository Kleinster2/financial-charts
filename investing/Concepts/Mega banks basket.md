---
aliases: [Mega banks, US universal banks, MEGABANK]
tags: [concept/cluster, banking, financials]
---

# Mega banks basket

> [!success] Cluster status: validated as cohort, but boundary equals XLF (May 2026)
> Intra-cluster correlation 0.70 (range 0.61-0.78), PC1 75.8% explained variance — strong cohesion. BUT hierarchical clustering at 0.4 merges JPM/BAC/C/WFC/USB with GS, MS, KRE (regional banks), and XLF (financials ETF) into ONE block. The cluster IS the financials sector. There is no "mega bank" sub-factor distinct from XLF — at the equity level, the 5 names ARE the dominant constituents of XLF. The +0.59 separation from insurance carriers is the only meaningful within-financials distinction. See "Cluster validation" section below.
>
> Refreshed 2026-06-14 (1Y to 2026-06-12): verdict holds — commercial-5 intra 0.697, PC1 75.83%, stable to two decimals. The sub-cohort sweep sharpens it: the commercial core (JPM/BAC/WFC/USB) is boundary-dependent — XLF contaminates at threshold 0.30 and it never forms a clean island at any threshold — while the GS/MS investment-bank pair holds only across a narrow band (stable width 0.10, intra 0.839, SPY contaminates at 0.35). Citigroup now defects to the capital-markets pole, trading with GS/MS/SPY rather than the deposit-lending core. See the [[#Current-window refresh and sub-cohort sweep (2026-06-14)]] subsection.

The five largest US universal banks — JPMorgan, Bank of America, Citigroup, Wells Fargo, US Bancorp — cohere tightly as a cluster (intra 0.70, PC1 76%) but the cluster boundary at 0.4 threshold extends to include investment banks (GS, MS), regional banks (KRE), and the broad financials ETF (XLF). Translation: at the 1-year horizon, "mega banks" = "banks" = "XLF financials." The math validates the cluster but says it isn't a separable basket from XLF.

---

## Constituents

5-name candidate cohort. Dendrogram shows it merging with the broader XLF block.

| Ticker | Company | PC1 loading | Note |
|--------|---------|-------------|------|
| JPM | [[JPMorgan Chase]] | 0.434 | Largest US bank; bellwether |
| BAC | [[Bank of America]] | 0.474 | Largest deposit franchise |
| C | [[Citigroup]] | 0.450 | Most international; restructuring story |
| WFC | [[Wells Fargo]] | 0.441 | Domestic-focused; asset cap recently lifted |
| USB | [[US Bancorp]] | 0.436 | Smallest of the major commercial banks |

Internal ticker proposal: MEGABANK.

---

## Cluster validation

Procedure: `scripts/cluster_analysis.py --config scripts/cluster_configs/mega_banks.yaml`. Standard in `docs/cluster-validation.md`.

### Headline numbers (1Y, 2025-04-30 to 2026-04-30)

| Diagnostic | Result | Interpretation |
|---|---|---|
| Avg intra-cluster correlation | 0.696 (range 0.61-0.78) | Strong cohesion |
| Tightest pair | BAC-C = 0.78, BAC-WFC = 0.78 | BAC is the central node |
| PC1 explained variance | 75.8% | Strong single-factor cohort |
| Hierarchical clustering at 0.4 | JPM+BAC+C+WFC+USB+GS+MS+KRE+XLF all merge as ONE cluster | Boundary == financials sector |
| Cluster vs investment banks (GS, MS) | 0.66 (+0.04 advantage) | Barely separates — investment banks ARE in the same factor at this threshold |
| Cluster vs regional banks (KRE) | 0.68 (+0.02 advantage) | Barely separates — regionals are in the same factor too |
| Cluster vs broad ETFs (XLF, SPY) | 0.65 (+0.05 advantage) | Cluster IS the financials factor |
| Cluster vs insurance carriers | 0.109 (+0.587 advantage) | Only meaningful within-financials separation |

### Pairwise correlations (1Y)

|  | JPM | BAC | C | WFC | USB |
|---|---|---|---|---|---|
| JPM | — | 0.73 | 0.71 | 0.64 | 0.61 |
| BAC | 0.73 | — | 0.78 | 0.78 | 0.72 |
| C | 0.71 | 0.78 | — | 0.63 | 0.68 |
| WFC | 0.64 | 0.78 | 0.63 | — | 0.69 |
| USB | 0.61 | 0.72 | 0.68 | 0.69 | — |

### What the boundary-equals-XLF finding means

The cluster validation says: the 5-name cohort IS the dominant factor inside XLF. There is no clean way to construct a "mega banks vs XLF" trade — the cohort accounts for so much of XLF's weighting that the long-short collapses to near-zero net exposure.

Three implications:
- Trading the basket directly = trading XLF with cleaner mega-bank concentration. Useful if you want pure mega-bank exposure without REITs / insurance / consumer-finance dilution.
- Investment banks (GS, MS) trade with the mega bank cohort at the 0.4 threshold — at this horizon, the i-bank vs commercial-bank distinction is not a separable factor. Tighter threshold (0.3) might separate them.
- Regional banks (KRE) also merge with mega banks at 0.4 — the rate-cycle and credit-cycle factors dominate within-banking distinctions at the 1Y horizon.
- The ONLY clean within-financials separation is from insurance carriers (+0.59) — see [[Insurance carriers basket]] / [[P&C insurance carriers basket]].

### Current-window refresh and sub-cohort sweep (2026-06-14)

Re-run on the 2025-06-13 to 2026-06-12 window confirms the May verdict and answers the open question above (whether a tighter threshold separates the investment banks). Two new findings.

First, a dendrogram defection. At the 0.4 threshold the block no longer reads as one undifferentiated cluster: JPM, BAC, WFC, USB merge with KRE and XLF (Cluster 1), while Citigroup splits off with GS, MS and SPY (Cluster 2). Citi trades with the investment banks and market beta, not the deposit-lending core — its large markets/trading desk and global footprint pull it toward the capital-markets pole. The May note flagged C as the obvious idiosyncratic name; the refresh shows the lean is systematic, not event-noise.

Second, the sub-cohort robustness sweep (per `docs/cluster-validation.md` §10) measures whether either business-model leg is a tradeable sub-factor:

| Sub-cohort | Intra-corr | Stable width | Label | Why it is not separable |
|---|---|---|---|---|
| Commercial core (JPM, BAC, WFC, USB) | 0.722 | 0.00 | boundary-dependent | XLF contaminates at threshold 0.30; never a clean island |
| Investment-bank pair (GS, MS) | 0.839 | 0.10 (band 0.20-0.30) | fragile | SPY contaminates at 0.35 — what binds them is market beta |

The juxtaposition is the cleanest illustration in the vault that correlation is not separability. GS+MS is the highest-correlated pair measured anywhere in the cluster campaign (0.839) yet only fragile, because the two investment banks are bound by broad market beta rather than any idiosyncratic investment-banking factor that would wall them off from SPY. The commercial core is tighter than it looks (0.722) but even less separable — XLF sits directly on top of it. Compare the Macau casino pair documented in [[Casino industry structure]] (LVS+WYNN, intra 0.631, stable width 0.20): less correlated than either bank leg, yet more separable, because a specific Macau gaming-policy factor walls it off from US consumer and market beta. Inside US banking there is no such idiosyncratic wall — the commercial banks ARE XLF, the investment banks ARE market beta, and the only thing that ever decouples is a single name on a restructuring story.

---

## Trade implications

| Trade | Verdict |
|---|---|
| Long MEGABANK basket | Equivalent to long XLF with mega-bank concentration; useful for pure US universal-bank exposure |
| Long MEGABANK / short XLF | Near-zero net exposure — cluster IS the dominant factor in XLF |
| Long MEGABANK / short KRE | Captures size-tier differential; at 0.4 horizon, this is mostly noise |
| Long MEGABANK / short investment banks (GS+MS) | Captures commercial banking vs investment banking; small but real differential |
| Long MEGABANK / short insurance carriers | Captures the +0.59 within-financials separation — meaningful trade |
| Pair trades within MEGABANK | Captures idiosyncratic restructuring stories (C is the obvious one); not factor exposures |

---

## What could break the cluster (or sharpen it)

| Scenario | Effect on cluster |
|---|---|
| Yield-curve steepening | Cluster cohesion increases — all banks benefit from NII expansion together |
| Credit-cycle deterioration | Cluster cohesion increases — all banks re-rate on credit losses together |
| One-bank idiosyncratic event (WFC asset cap, C restructuring) | Affected name decouples around event-noise |
| Fed cuts in front-end (rate-cycle pivot) | KRE may decouple from MEGABANK as smaller banks have higher NIM sensitivity |
| Banking crisis (2023-style) | Cluster cohesion increases on the way down |

---

## Cluster validation compliance addendum (2026-06-07)

Generated from `scripts/cluster_configs/mega_banks.yaml` using `scripts/cluster_analysis.py` methodology. The 1Y diagnostic window is 2025-05-01 to 2026-04-30 (171 observations); the rolling history starts at `2020-01-01` where data are available.

### Required validation plots

![[mega-banks-cluster-correlation-1y.png]]

*One-year correlation heatmap for the `Mega banks` validation universe.*

![[mega-banks-cluster-dendrogram-1y.png]]

*Hierarchical clustering tree using average linkage on distance `1-|corr|`.*

![[mega-banks-cluster-pca-1y.png]]

*PCA diagnostic for the candidate cohort; PC1 explains 75.7% of standardized daily-return variance.*

### PC1 index weights vs cluster topology

The topology table answers which names join the tree first or last. The raw PC1-mimic table answers which raw-return weights best replicate the standardized common factor after realized-volatility scaling. These are deliberately different readings of the same cluster.

| Step | Left | Right | Distance (1-\|corr\|) | Read |
|---|---|---|---|---|
| 1 | BAC | C | 0.219 | Tightest merge |
| 2 | JPM | BAC+C | 0.282 | Candidate cohort merge step |
| 3 | WFC | USB | 0.309 | Candidate cohort merge step |
| 4 | JPM+BAC+C | WFC+USB | 0.325 | Final cohort join / loosest boundary |

| Ticker | PC1 loading | Normalized loading weight | Ann. vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| JPM | 0.434 | 19.42% | 22.99% | 21.08% |
| BAC | 0.474 | 21.23% | 22.80% | 23.24% |
| C | 0.449 | 20.11% | 30.31% | 16.56% |
| WFC | 0.441 | 19.74% | 27.83% | 17.71% |
| USB | 0.436 | 19.50% | 22.73% | 21.42% |

Interpretation: use the dendrogram / join-distance topology to identify the tight core and later-joining members; use the Raw PC1-mimic weight column only for investable factor-replication sizing.

### Historical tightness evolution

![[mega-banks-cluster-rolling-tightness-90d.png]]

*Ninety-day rolling tightness diagnostic: avg intra-correlation, PC1 share, core correlation, satellite-to-core correlation, and final candidate join distance.*

| Year | Avg corr median | PC1 median | Core corr median | Satellite-to-core median | Final join distance median |
|---|---|---|---|---|---|
| 2020 | 0.900 | 92.0% | 0.893 | 0.910 | 0.118 |
| 2021 | 0.782 | 82.7% | 0.763 | 0.810 | 0.253 |
| 2022 | 0.785 | 82.9% | 0.767 | 0.816 | 0.254 |
| 2023 | 0.732 | 78.8% | 0.741 | 0.721 | 0.352 |
| 2024 | 0.716 | 77.5% | 0.740 | 0.686 | 0.335 |
| 2025 | 0.835 | 86.8% | 0.835 | 0.834 | 0.190 |
| 2026 | 0.754 | 80.4% | 0.774 | 0.713 | 0.290 |

Latest 90D through 2026-04-30: avg corr 0.771, PC1 81.7%, core corr 0.780, satellite-to-core corr 0.758, final join distance 0.258.

Historical verdict: structurally durable cluster; rolling cohesion has usually stayed in single-factor territory.

---

## Related

### Member actors

- [[JPMorgan Chase]] — bellwether
- [[Bank of America]] — central PC1 node
- [[Citigroup]] — restructuring story
- [[Wells Fargo]] — domestic franchise
- [[US Bancorp]] — smallest of majors

### Adjacent concept notes

- [[Banking concentration]] — structural backdrop
- [[Bank cronyism]] — political-economy frame
- [[Banking primer]] — sector hub
- [[Goldman Sachs]] — investment bank (clusters with mega banks at 0.4)
- [[Morgan Stanley]] — investment bank (clusters with mega banks at 0.4)

### Methodology

- `docs/cluster-validation.md` — standard procedure
- `scripts/cluster_analysis.py` — generalized cluster validation script
- `scripts/cluster_configs/mega_banks.yaml` — config for this cluster

*Created 2026-05-03 — validated cluster note with boundary-equals-XLF caveat*
