---
aliases: [Regional banks, US regional banks, Regional bank cluster, Mid-cap banks]
tags: [sector, financials, bank, regional-bank, cluster-validation]
---

# Regional banks

> [!warning] Cluster status: VALIDATED and extremely tight, but ETF-embedded (= KRE); a distinct bank pole from the money-centers, yet not separable from its own ETF (Jun 2026)
> The mid-cap US regional banks ([[Regions Financial|RF]]/[[KeyCorp|KEY]]/[[Citizens Financial Group|CFG]]/[[Huntington Bancshares|HBAN]]/[[Fifth Third|FITB]]/[[M&T Bank|MTB]]) trade as one very tight factor — intra-corr 0.871 (weekly 0.902, HIGHER), PC1 89.3%, the tightest cohort in the campaign — rejecting every null at the 0.0001 floor, with a STABLE 2Y holdout (0.95) and durable 0.83–0.91 cohesion every year since 2020. They are a distinct bank pole from the money-centers: a +0.248 intra-advantage over [[JPMorgan Chase|JPM]]/[[Bank of America|BAC]] (regionals ≠ megabanks). But they are ETF-embedded: the threshold scan never isolates them as a clean cluster (zero stable width), because the regional-bank ETF [[KRE]] holds these exact names and contaminates at every cut. The +0.197 intra-advantage over the broad ETFs reflects only that the six large regionals are tighter than KRE's ~140-name average — KRE is never separable. Own [[KRE]] for the regional-bank factor; the six-name basket is essentially KRE. This is the regional analogue of the [[Mega banks basket|money-center]] result (mega banks = XLF; regional banks = KRE).

The rate-and-credit factor of mid-cap banking. Six regionals run the same balance-sheet business — deposit funding, net interest margin, and commercial/CRE credit — so they move almost as one on the same variables: the level and shape of the curve, deposit betas, and the credit cycle (the 2023 regional-bank stress, then normalization). That homogeneity makes them the tightest cohort the campaign has measured. But because they ARE the [[KRE]] ETF's core holdings, the basket is not separable from KRE — it is the cleanest expression of the same factor KRE already provides.

## Sector performance

![[regbank-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[KRE]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is six mid-cap US regional banks — [[Regions Financial|RF]], [[KeyCorp|KEY]], [[Citizens Financial Group|CFG]], [[Huntington Bancshares|HBAN]], [[Fifth Third|FITB]], [[M&T Bank|MTB]] — tested against the money-center banks ([[JPMorgan Chase|JPM]]/[[Bank of America|BAC]]), the regional-bank ETF [[KRE]], broad financials (XLF), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.871 [0.826–0.907] | the campaign's highest; weekly 0.902 (even higher) |
| PC1 explained variance | 89.3% | a near-single-security cohort (weekly 91.8%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | far beyond a random 6-pick |
| Vol-matched null p | 0.0001 | cohesion exceeds vol-matched baskets |
| Holdout (2Y split) | STABLE 0.95 | train 0.912 → test 0.870 — durable across regimes |
| Threshold stable width | 0.00 (none) | never isolates — KRE/XLF contaminate at every cut |
| Intra-adv vs money-center (JPM/BAC) | +0.248 | distinct from the megabanks — a separate bank pole |
| Intra-adv vs ETFs (KRE/XLF/SPY) | +0.197 | tighter than the broad ETF average, but KRE is never separable |

All US-listed. Config: `scripts/cluster_configs/rf.yaml`; registry row 2026-06-20.

### Boundary — all banks + KRE + XLF in one cluster; only SPY apart

![[regbank-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The six regionals cluster with the money-centers ([[JPMorgan Chase|JPM]]/[[Bank of America|BAC]]), the regional-bank ETF [[KRE]], and broad financials [[XLF]] — everything financial fuses; only SPY is apart. The ETF sitting inside the cluster (KRE holds these names) is the mark of an ETF-replicable cohort.*

The threshold scan never returns the six as a clean cluster (zero stable width) — KRE and XLF contaminate at every threshold, because KRE is built from these names. So despite the campaign-high intra-correlation, this is "VALIDATED but ETF-replicable": a real, extremely tight factor that the [[KRE]] ETF already delivers. The distinct-factor finding is relative — regionals are a separate pole from the money-centers (+0.248), but within the regional pole, KRE is the vehicle.

### Topology — six near-interchangeable names

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | KEY + CFG | 0.093 | the tightest pair |
| 2 | RF + (KEY+CFG) | 0.102 | the core builds |
| 3 | HBAN + FITB | 0.113 | a second pair |
| 4 | MTB + core | 0.128 | M&T joins |
| 5 | the two groups merge | 0.142 | the whole cohort closes — extraordinarily tight |

Every join is below 0.15 — the six are nearly interchangeable. PC1 explains 89.3% with near-identical loadings (~0.40–0.42), the signature of a single dominant factor (rates + credit).

### PC1 index weights

![[regbank-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 89.3% (weekly 91.8%) — the rate-and-credit factor accounts for nearly all the variance.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| RF | 0.415 | 16.9% | 25.4% | 17.3% |
| KEY | 0.412 | 16.8% | 25.1% | 17.4% |
| CFG | 0.408 | 16.7% | 27.7% | 15.6% |
| HBAN | 0.402 | 16.4% | 27.8% | 15.3% |
| FITB | 0.408 | 16.7% | 27.8% | 15.5% |
| MTB | 0.404 | 16.5% | 22.7% | 18.9% |

Loadings and vols are nearly identical across all six — an equal-weight basket essentially IS PC1, and (because KRE holds them) essentially is KRE.

### Distinctness — distinct from money-centers, but = KRE

![[regbank-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A uniformly hot six-name block; KRE/XLF are nearly as warm (KRE holds these names), the money-centers a notch cooler (+0.248), and SPY cold.*

Two readings: +0.248 versus the money-center banks ([[JPMorgan Chase|JPM]]/[[Bank of America|BAC]]) — regionals are a distinct bank pole (the megabanks carry capital-markets and global drivers the regionals lack) — but only +0.197 versus the ETFs, with [[KRE]] never separable (threshold width 0.0). KRE is the regional-bank factor; the six-name basket is a slightly-tighter expression of the same thing. This mirrors the [[Mega banks basket|mega-banks]] result (mega banks = XLF): two bank poles, both ETF-replicable.

### Historical tightness evolution

![[regbank-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Exceptionally tight throughout (0.83–0.91), including through the 2023 regional-bank stress.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.880 | 90.2% |
| 2021 | 0.877 | 89.8% |
| 2022 | 0.880 | 90.1% |
| 2023 | 0.835 | 86.3% |
| 2024 | 0.866 | 88.9% |
| 2025 | 0.913 | 92.8% |
| 2026 | 0.854 | 87.9% |

Latest 90-day reading: intra 0.895, PC1 91.3%. The factor is among the most durable in the campaign — intra never falls below 0.83 in six years, including through the March 2023 regional-bank crisis (when, if anything, the names moved even more as one). The regionals are a real, tight, distinct-from-megabanks factor — but it is the [[KRE]] factor, owned most cleanly through the ETF.

## Related

- [[Mega banks basket]] — the money-center pole (= XLF); regionals are distinct from it (+0.248)
- [[Regions Financial]], [[KeyCorp]], [[Citizens Financial Group]], [[Huntington Bancshares]], [[Fifth Third]], [[M&T Bank]] — the six regionals
- [[KRE]] — the regional-bank ETF the cohort resolves to
- [[Residential REITs]], [[Solid waste]] — other extremely tight cohorts (those separable from their ETFs; this one is not)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/rf.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
