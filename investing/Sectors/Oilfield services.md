---
aliases: [Oilfield services, OFS, Oil services, Oilfield services cluster, Oilfield services equity beta, OFS cohort]
tags: [sector, energy, oil-gas, oilfield-services, cluster-validation]
---

# Oilfield services

> [!warning] Cluster status: validated factor, distinct from crude beta — but it IS the services ETF (OIH), and eroding (Jun 2026)
> The diversified oilfield-services + equipment majors ([[Schlumberger|SLB]]/[[Halliburton|HAL]]/[[Baker Hughes|BKR]]/[[NOV]]/[[TechnipFMC|FTI]]/[[Weatherford|WFRD]]) trade as one real factor — intra-corr 0.655 (weekly 0.773), PC1 71.4% (weekly 81.2%), rejecting the random-basket AND vol-matched nulls at the 0.0001 floor. The campaign's cleanest energy value-chain split: services is +0.254 distinct from the oil majors ([[Oil and gas equity beta|XOM/CVX/COP/EOG]]) and forms a separate dendrogram cluster — the activity/capex-cycle factor, not the spot-crude factor. But it is not a *distinct basket*: the oil-services ETF OIH sits inside the cohort from the tightest cut (threshold width 0.00), so it is OIH-replicable, the services analogue of majors = XLE. Holdout WEAKENED (0.74) — tight 0.90 in 2024–25, easing to 0.66 in 2026. Own OIH; the value chain forks (services ≠ crude), but each leg collapses to its ETF.

The middle of the energy value chain. The oil & gas majors ([[Oil and gas equity beta]]) are the equity expression of the crude price; the services names are paid on customer capex — the rigs, fracs, completions, and equipment that producers buy when activity rises — so they ride the drilling/capex cycle rather than spot crude directly. That is why they form their own factor, distinct from the majors. What they are NOT is a separable trade from the oil-services ETF: OIH holds these exact names, so the cohort is the ETF.

## Cluster validation

The candidate cohort is the six diversified oilfield-services + equipment majors — [[Schlumberger|SLB]], [[Halliburton|HAL]], [[Baker Hughes|BKR]], [[NOV]], [[TechnipFMC|FTI]], [[Weatherford|WFRD]] — tested against the oil majors ([[Oil and gas equity beta|XOM/CVX/COP/EOG]]), drillers ([[Patterson-UTI|PTEN]]/[[Helmerich & Payne|HP]]/[[Transocean|RIG]]), and benchmarks (OIH oil-services ETF, XLE energy, XOP E&P, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.655 [0.534–0.787] | moderate daily; weekly 0.773 (the better estimate — see note) |
| PC1 explained variance | 71.4% | strong single factor (weekly 81.2%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | beats a random 6-pick at the floor |
| Vol-matched null p | 0.0001 (PC1 0.0001) | not just shared energy beta/vol — a real services factor |
| Holdout (2Y split) | WEAKENED 0.74 | eroding (train 0.902 → test 0.664; loadings corr 0.45) |
| Threshold clean width | 0.00 | OIH inside from 0.20 — embedded, ETF-replicable |
| Intra-adv vs oil majors (XOM/CVX/COP/EOG) | +0.254 | distinct — services is the activity-cycle factor, not crude |
| Intra-adv vs drillers (PTEN/HP/RIG) | +0.121 | weakly distinct (and drillers split — see boundary) |
| Intra-adv vs ETFs (OIH/XLE/XOP/SPY) | +0.166 | distinct from XLE/XOP/market, but OIH sits inside |

All US-listed. The weekly intra-corr (0.773) exceeds the daily (0.655) by >0.10; the script flags this as async, but the cohort is entirely US-listed — it is the smaller, higher-vol names' (WFRD/NOV/FTI) reaction-timing noise, the [[Ad-tech]] pattern, not cross-region async. The weekly reading is the better estimate of economic co-movement. Config: `scripts/cluster_configs/slb.yaml`; registry row 2026-06-19.

### Boundary — a distinct services pole (= OIH), separate from the crude pole

![[oilfield-services-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Two energy poles. Green: the six services names + the oil-services ETF OIH (SLB+OIH nearly the tightest pair) + offshore driller [[Transocean|RIG]]. Orange: the oil majors with XLE/XOP inside + onshore drillers [[Patterson-UTI|PTEN]]/[[Helmerich & Payne|HP]]. The two poles join only at ~0.52, above the cut. [[SPY]] sits apart.*

The threshold scan never isolates the six-name cohort: OIH joins from the very tightest cut (0.20), RIG at 0.50, and the oil majors only at 0.55. So the zero width is the "real but embedded" kind (high intra + nulls rejected), not a dispersion falsification. Two findings define the boundary. First, the value-chain split is real: services sits in a separate cluster from the majors (+0.254 intra-advantage), confirming the [[Oil and gas equity beta|oil-majors note's]] teaser that "the one genuinely distinct energy factor is oilfield services." Second, the split is OIH-replicable: the services ETF is inside the cohort at every threshold, so the distinct factor is captured by the ETF — own OIH, not a bespoke six-name basket.

### Topology — a homogeneous block; FTI the late joiner

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | SLB + WFRD | 0.213 | tightest pair |
| 2 | HAL + NOV | 0.303 | services/equipment pair |
| 3 | (SLB+WFRD) + (HAL+NOV) | 0.316 | the core merges |
| 4 | BKR + core | 0.334 | Baker Hughes joins |
| 5 | FTI + core | 0.413 | subsea ([[TechnipFMC]]) joins last |

All six join below distance 0.42 (correlation above 0.58) — a homogeneous block. [[Schlumberger]]+[[Weatherford]] are the tightest pair; [[TechnipFMC]] (subsea/offshore EPC, the most project-cycle-differentiated business) joins last. Note that against the full set, [[Schlumberger]]'s nearest neighbour is actually OIH — the cohort's true center of gravity is the ETF.

### PC1 index weights

![[oilfield-services-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 71.4% (weekly 81.2%) with near-identical loadings (0.37–0.43) — a clean single factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| SLB | 0.434 | 17.8% | 37.4% | 17.6% |
| HAL | 0.409 | 16.7% | 37.5% | 16.5% |
| BKR | 0.408 | 16.7% | 36.6% | 16.9% |
| NOV | 0.417 | 17.1% | 39.5% | 16.0% |
| FTI | 0.372 | 15.2% | 30.2% | 18.6% |
| WFRD | 0.407 | 16.7% | 42.8% | 14.4% |

Near-equal loadings — the six are interchangeable expressions of one services factor. The lower-vol [[TechnipFMC]] takes the largest raw PC1-mimic weight; the higher-vol [[Weatherford]] the smallest.

### Distinctness — distinct from crude, embedded in OIH

![[oilfield-services-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The services block is warm and warmest against OIH; the oil majors (XOM/CVX/COP/EOG) + XLE/XOP form a separate warm corner; SPY is cool against everything.*

The two numbers that define the cohort: +0.254 versus the oil majors (services is its own activity/capex-cycle factor, not spot crude) and OIH sitting inside the cluster (the factor is the services ETF). So the investable read forks like the broader energy complex: own XLE for crude-equity beta, own OIH for the services/capex-cycle beta — two distinct legs of the value chain — but within each leg the ETF replicates the basket, so single-name selection ([[Schlumberger]] vs [[Halliburton]]) is a company bet, not a factor bet. Distinct from XOP/E&P and from [[SPY]] (low market beta).

### Drilling splits by offshore vs onshore

The drillers control group does not trade as one, and the split is instructive: offshore driller [[Transocean|RIG]] joins the services pole (it is a deepwater-capex play, like subsea [[TechnipFMC]]), while the onshore pressure-pumping/contract drillers [[Patterson-UTI|PTEN]] and [[Helmerich & Payne|HP]] cluster with the oil majors and E&P names — they trade on US shale activity, closer to the producers than to the diversified services majors. Drilling is not a single factor; it bifurcates by basin geography onto the two energy poles.

### Historical tightness evolution

![[oilfield-services-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Moderately durable but regime-sensitive — tightened into the 2024–25 capex up-cycle (0.83), easing through 2026 (0.66).*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2022 | 0.657 | 72.2% |
| 2023 | 0.719 | 76.7% |
| 2024 | 0.723 | 77.0% |
| 2025 | 0.829 | 85.8% |
| 2026 | 0.662 | 72.0% |

Latest 90-day reading: intra 0.658, PC1 71.6%. Unlike the oil majors (holdout 0.97, durable through every regime because one exogenous price drives them), the services factor is conditional on the capex cycle: it tightened as the 2024–25 upstream-spending wave bound the names, and is loosening in 2026 as activity plateaus and the names diverge on backlog/exposure (subsea vs North America vs international). The WEAKENED holdout (0.74) and the loadings-corr drop to 0.45 are the same signal — a real but eroding factor, not the structurally permanent cohesion of the crude pole.

## Related

- [[Oil and gas equity beta]] — the oil-majors cohort (= XLE); the crude pole of the energy value-chain split (services is +0.254 distinct)
- [[Refiners]] — the downstream leg (= CRAK); sharply distinct from services (+0.403), but unlike services it stays attached to crude (only +0.193 from the majors)
- [[Schlumberger]], [[Halliburton]], [[Baker Hughes]] — the diversified big three
- [[NOV]], [[TechnipFMC]], [[Weatherford]] — equipment / subsea / services
- [[Transocean]], [[Patterson-UTI]], [[Helmerich & Payne]] — drillers (split offshore vs onshore across the two poles)
- [[Oil]] — the upstream commodity the customers produce
- [[Energy and Utilities]] — the broad sector hub
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-19. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/slb.yaml`; registry row 2026-06-19. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
