---
aliases: [Midstream and pipelines, Midstream, Pipelines, Midstream cohort, MLPs, Pipeline operators]
tags: [sector, energy, oil-gas, midstream, mlp, cluster-validation]
---

# Midstream and pipelines

> [!warning] Cluster status: validated but loose and eroding — the most crude-decoupled energy leg, yet = AMLP (Jun 2026)
> The large-cap US midstream operators ([[Kinder Morgan|KMI]]/[[Williams Companies|WMB]]/[[ONEOK|OKE]]/[[Enterprise Products|EPD]]/[[Energy Transfer|ET]]/[[MPLX]]) trade as one factor, but the loosest and least durable of the four energy legs — intra-corr 0.558 (weekly 0.641), PC1 63.5%, holdout WEAKENED 0.68 (eroding to 0.53 in 2026). It rejects the random-basket null at the floor and the vol-matched null at p 0.003. The standout is structural: midstream forms its own dendrogram cluster, separate from the crude pole (majors+XLE) AND from utilities (XLU) — the most crude-decoupled energy leg, confirming the fee-based/throughput thesis. But it is still ETF-bounded: AMLP (the Alerian MLP ETF) sits inside the cohort from threshold 0.40, so the factor is AMLP. [[MPLX]] is an outlier (singleton, joins at 0.55). Own AMLP for the fee/yield factor; the chain's most decoupled leg is also its least cohesive.

The bottom of the energy value chain. Midstream is paid on volume and capacity — fee-based tolls on pipelines, storage, and processing — not on the crude price itself, so in principle it should be the most decoupled energy equity from spot oil. The tape agrees: midstream is the one energy leg that forms its own cluster fully separate from the crude pole. But two things temper it — the factor is captured by AMLP (a bespoke basket adds nothing), and the cohort is loose and eroding, because fee/yield/distribution dynamics are more idiosyncratic across names (C-corp vs MLP, gas vs crude vs NGL exposure) than a single shared commodity price.

## Sector performance

![[midstream-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs AMLP (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is the six large-cap US midstream operators — [[Kinder Morgan|KMI]], [[Williams Companies|WMB]], [[ONEOK|OKE]] (C-corps), [[Enterprise Products|EPD]], [[Energy Transfer|ET]], [[MPLX]] (MLPs) — tested against the oil majors ([[Oil and gas equity beta|XOM/CVX/COP/EOG]]) and benchmarks (AMLP MLP ETF, XLE energy, XLU utilities/yield proxy, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.558 [0.425–0.834] | loose-moderate; weekly 0.641 — the loosest energy leg |
| PC1 explained variance | 63.5% | a factor with real sub-structure (PC2 11%, PC3 11%; weekly 70.6%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | beats a random 6-pick at the floor |
| Vol-matched null p | 0.0026 (PC1 0.0042) | rejects, but weaker than the other energy legs (they hit 0.0001) |
| Holdout (2Y split) | WEAKENED 0.68 | eroding hard (train 0.818 → test 0.557; loadings corr 0.71) |
| Threshold clean width | 0.00 | AMLP inside from 0.40 — embedded, ETF-replicable |
| Intra-adv vs oil majors (XOM/CVX/COP/EOG) | +0.138 | distinct — forms its OWN cluster, separate from crude |
| Intra-adv vs ETFs (AMLP/XLE/XLU/SPY) | +0.214 | distinct from XLE/XLU/market, but AMLP sits inside |

All US-listed. As with the other energy legs, the weekly intra (0.641) exceeds the daily (0.558) — reaction-timing among the lower-liquidity MLPs, not async (all US). Config: `scripts/cluster_configs/kmi.yaml`; registry row 2026-06-19.

### Boundary — its own cluster, distinct from crude AND utilities, but = AMLP

![[midstream-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Green: five midstream names (KMI/WMB/ET/EPD/OKE) + the MLP ETF AMLP — the midstream pole. Orange: the oil majors with XLE inside — the crude pole. The two poles join only at ~0.50. [[MPLX]] (far left), XLU (utilities), and [[SPY]] are separate singletons. Midstream is decoupled from crude AND from utilities — but AMLP is inside its cluster.*

The threshold scan never isolates the cohort cleanly: AMLP contaminates from threshold 0.40, the oil majors from 0.55, and below 0.40 the cohort fragments (MPLX splits, the C-corps and MLPs separate). So the structural reads are three. First, midstream is the most crude-decoupled energy leg — it forms its own dendrogram cluster separate from the majors+XLE crude pole (unlike refiners, which sat inside the crude cluster), confirming the fee-based thesis that toll revenue decouples from spot oil. Second, it is NOT a utility/yield proxy — XLU sits apart as its own singleton, so despite midstream's bond-like distributions it does not trade as a rate/utility cohort. Third, it is still ETF-bounded: AMLP is inside the cohort from 0.40, so the decoupled factor is exactly what the MLP ETF captures — own AMLP.

### Topology — a loose block; MPLX the outlier, C-corps tighter than MLPs

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | KMI + WMB | 0.166 | tightest pair (the gas-pipeline C-corps) |
| 2 | OKE + EPD | 0.329 | a C-corp/MLP cross-pair |
| 3 | ET + (OKE+EPD) | 0.411 | Energy Transfer joins |
| 4 | (KMI+WMB) + (ET+OKE+EPD) | 0.430 | the five-name core merges |
| 5 | MPLX + core | 0.547 | MPLX joins ABOVE the 0.5 cut — an outlier (singleton at 0.5) |

Five of six join below 0.43, but [[MPLX]] joins only at 0.547 — above the threshold, so it is a singleton in the cut. MPLX (the Marathon-affiliated, refining-logistics-tilted MLP) trades on its parent/sponsor dynamics more than the broad midstream factor. The tightest pair is [[Kinder Morgan]]+[[Williams Companies]] (the large gas-pipeline C-corps).

### PC1 index weights

![[midstream-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 63.5% — a real factor but with meaningful sub-structure (PC2 11%, PC3 11%), looser than the tighter energy legs. MPLX has the lowest loading.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| KMI | 0.451 | 18.5% | 20.6% | 17.5% |
| WMB | 0.420 | 17.2% | 23.1% | 14.6% |
| OKE | 0.424 | 17.4% | 27.3% | 12.5% |
| EPD | 0.402 | 16.5% | 17.1% | 18.9% |
| ET | 0.404 | 16.6% | 16.5% | 19.7% |
| MPLX | 0.339 | 13.9% | 16.1% | 16.9% |

The defining feature versus the rest of energy is volatility: midstream runs 16–27% annualized vol, roughly half the refiners (35–65%) — the fee/income/distribution profile. The lower-vol MLPs ([[Energy Transfer]], [[Enterprise Products]]) take the largest raw PC1-mimic weights; [[ONEOK]] (the highest-vol, NGL-levered name) the smallest. [[MPLX]] carries the lowest PC1 loading (0.339), consistent with its outlier status.

### Distinctness — distinct from crude and utilities, but = AMLP

![[midstream-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The midstream block is moderately warm and warmest against AMLP; cooler against the majors/XLE than the other energy legs are; cool against XLU and SPY.*

Midstream is the energy leg that most cleanly leaves the crude pole: it forms its own cluster (+0.138 vs the majors, and a clean dendrogram separation that refiners never achieved), because fee-based toll revenue is structurally less crude-linked than refining margin or upstream production. It is also distinct from utilities (XLU apart) — the bond-like distribution does not make it a rate/yield cohort. But the decoupled factor is AMLP: the MLP ETF sits inside the cohort from threshold 0.40, so own AMLP for the midstream fee/yield factor rather than a bespoke six-name basket. Distinct from [[SPY]] (low market beta — a defensive income sleeve).

### Historical tightness evolution

![[midstream-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. The least durable energy leg — 0.65–0.76 in 2021–25, then a sharp 2026 erosion to 0.53.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.709 | 75.8% |
| 2022 | 0.728 | 77.4% |
| 2023 | 0.742 | 78.5% |
| 2024 | 0.648 | 70.8% |
| 2025 | 0.756 | 79.7% |
| 2026 | 0.533 | 61.6% |

Latest 90-day reading: intra 0.600, PC1 67.3%. Midstream is the least cohesive and least durable of the four energy legs (holdout 0.68 vs majors 0.97, refiners 0.88, services 0.74). The 2026 erosion to 0.53 reflects the names diverging on idiosyncratic catalysts (M&A, distribution policy, gas vs NGL vs crude mix, the [[MPLX]]/Marathon relationship) — fee-based midstream has no single exogenous price to bind it the way crude binds the majors. A real, distinct, but loose and fading factor — captured by AMLP.

## Energy value chain — the four legs

This completes the energy value-chain mapping. The pattern: moving down the chain from crude, the legs decouple from spot oil but lose cohesion and durability — and every leg collapses to its own sector ETF.

| Leg | Cohort note | = ETF | Distinct from crude? | Intra | Holdout |
|---|---|---|---|---|---|
| Upstream / integrated | [[Oil and gas equity beta]] | XLE | — (is crude) | 0.80 | 0.97 |
| Downstream / refining | [[Refiners]] | CRAK | weakly (+0.193, embedded) | 0.77 | 0.88 |
| Services / equipment | [[Oilfield services]] | OIH | yes (+0.254, own cluster) | 0.66 | 0.74 |
| Midstream / transport | this note | AMLP | most (own cluster, also ≠ utilities) | 0.56 | 0.68 |

The commodity-beta law extended down the value chain: business position determines which sector ETF you own (XLE → CRAK → OIH → AMLP), never whether you can avoid one. No energy equity leg escaped its ETF.

## Related

- [[Oil and gas equity beta]] — the crude pole (= XLE); midstream is distinct from it (forms its own cluster)
- [[Refiners]] — the downstream leg (= CRAK); the leg that stayed attached to crude
- [[Oilfield services]] — the services leg (= OIH); the other decoupled leg
- [[Kinder Morgan]], [[Williams Companies]], [[ONEOK]] — the C-corp pipeline operators
- [[Enterprise Products]], [[Energy Transfer]], [[MPLX]] — the MLPs (MPLX the outlier)
- [[Energy and Utilities]] — the broad sector hub
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-19. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/kmi.yaml`; registry row 2026-06-19. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
