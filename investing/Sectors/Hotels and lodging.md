---
aliases: [Hotels and lodging, Hotels, Lodging, Hotel franchisors, Hotel operators]
tags: [sector, consumer-discretionary, travel, hotels, lodging, usa, cluster-validation]
---

# Hotels and lodging

> [!warning] Cluster status: real cohesion but not a distinct factor — the big-3 are travel-cyclical/discretionary beta (= XLY/PEJ); the cohort splits by scale (Jun 2026)
> The US-listed hotel franchisors ([[Marriott|MAR]]/[[Hilton|HLT]]/[[Hyatt|H]]/[[Wyndham|WH]]/[[Choice Hotels|CHH]]) co-move — intra-corr 0.597 (weekly 0.675), PC1 67%, rejecting the random-basket and vol-matched nulls at the floor — but they are not a distinct hotel factor and the cohort splits by scale. The global upscale big-3 ([[Marriott|MAR]]/[[Hilton|HLT]]/[[Hyatt|H]]) cluster with the broad travel-cyclical/discretionary complex (airlines, cruises, XLY, the leisure ETF PEJ) — they are RevPAR/travel-demand/discretionary beta, not a separable lodging factor. The domestic economy franchisors ([[Wyndham|WH]]+[[Choice Hotels|CHH]]) split off as their own fee-stable pair. Holdout WEAKENED 0.69 — tight only in the travel-recovery windows (0.86 in 2022, 0.78 in 2025), loose otherwise. Hotels are the odd one out of the four travel cyclicals: airlines, cruises, and OTAs each validated as distinct factors; hotels are the one that is just discretionary beta.

The fourth and last travel cyclical. The campaign validated [[Airlines]] (fuel-driven), [[Cruise lines]] (the demand channel, +0.178 distinct from airlines), and [[Online travel]] (OTAs, +0.178, no pure ETF) as distinct travel sub-factors. Hotels complete the set — and break the pattern. The asset-light hotel franchisors earn fees on RevPAR (occupancy × rate), which is travel-demand-driven like the rest, but the big global brands trade as generic travel-cyclical/discretionary beta rather than a separable hotel factor, and the cohort fractures between the global upscale brands and the domestic economy franchisors.

## Sector performance

![[hotels-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs PEJ (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is the five US-listed hotel franchisors — [[Marriott|MAR]], [[Hilton|HLT]], [[Hyatt|H]] (global upscale), [[Wyndham|WH]], [[Choice Hotels|CHH]] (domestic economy) — tested against the other validated travel cyclicals (airlines [[Delta Air Lines|DAL]]/UAL, cruises [[Carnival|CCL]]/[[Royal Caribbean|RCL]], OTAs [[Booking Holdings|BKNG]]/[[Airbnb|ABNB]]) and benchmarks (PEJ leisure ETF, XLY discretionary, SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.597 [0.394–0.834] | moderate; weekly 0.675 |
| PC1 explained variance | 67.2% | moderate, with a big-3/economy split (PC2 18%); weekly 74.4% |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0002 | beats a random 5-pick |
| Vol-matched null p | 0.0001 | real beyond shared vol |
| Holdout (2Y split) | WEAKENED 0.69 | regime-dependent (train 0.847 → test 0.584) |
| Threshold clean width | 0.00 | airlines/cruises/PEJ join from 0.50 — embedded in travel-cyclical/discretionary |
| Intra-adv vs travel cyclicals (airlines/cruises/OTAs) | +0.150 | moderately distinct — but the big-3 merge with airlines/cruises at ~0.46 |
| Intra-adv vs ETFs (PEJ/XLY/SPY) | +0.144 | distinct from SPY, but PEJ/XLY sit with the big-3 |

All US-listed. Config: `scripts/cluster_configs/mar.yaml`; registry row 2026-06-19.

### Boundary — big-3 in the travel-cyclical block; economy splits off

![[hotels-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Red: the global big-3 ([[Hyatt|H]]/[[Marriott|MAR]]/[[Hilton|HLT]]) merge with XLY/SPY, airlines (DAL/UAL), the leisure ETF PEJ, and cruises (CCL/RCL) — one broad travel-cyclical/discretionary block. Orange: the economy franchisors [[Wyndham|WH]]+[[Choice Hotels|CHH]] (a separate domestic-fee pair, joining only at ~0.60). Green: the OTAs [[Booking Holdings|BKNG]]/[[Airbnb|ABNB]] (separate). The hotel cohort does not hold as one cluster.*

The threshold scan never isolates the cohort: from 0.50, airlines, cruises, and PEJ join the big-3's cluster, so the cohort is embedded in the broad travel-cyclical/discretionary complex. Two structural reads. First, the big-3 (MAR/HLT/H) are a tight sub-group (join ≤0.23) but they are not separable from the travel-cyclical/discretionary block — they merge with airlines/cruises/XLY/PEJ at ~0.46, so the global hotel brands are RevPAR/travel-demand/discretionary beta, captured by XLY or the leisure ETF PEJ, not a distinct hotel factor. Second, the cohort splits by scale: the domestic economy franchisors (WH/CHH) form their own pair and join the big-3 only at 0.51 — they are more franchise-fee-stable and less travel-cyclical than the global upscale brands.

### Topology — a tight big-3 core, an economy satellite pair

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | MAR + HLT | 0.166 | the global-brand pair (tightest) |
| 2 | H + (MAR+HLT) | 0.232 | the upscale big-3 core |
| 3 | WH + CHH | 0.324 | the domestic economy pair (separate) |
| 4 | (big-3) + (WH+CHH) | 0.514 | cohort closes just ABOVE the 0.5 cut |

The big-3 ([[Marriott]]/[[Hilton]]/[[Hyatt]]) are a tight core (join ≤0.23 — RevPAR-correlated global operators), but the cohort closes only at 0.514, above the cut, because the economy franchisors ([[Wyndham]]/[[Choice Hotels]]) trade apart (more US-domestic, franchise-fee-driven). Against the full set, the big-3's nearest neighbours include XLY and the airlines, not the economy franchisors — the cohort's center of gravity is travel-cyclical/discretionary beta.

### PC1 index weights

![[hotels-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 67.2% (weekly 74.4%) with a sizeable PC2 (18%) — the big-3/economy split. CHH has the lowest loading.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| MAR | 0.484 | 21.8% | 27.4% | 23.8% |
| HLT | 0.480 | 21.6% | 23.5% | 27.5% |
| H | 0.463 | 20.8% | 34.4% | 18.1% |
| WH | 0.429 | 19.3% | 31.4% | 18.4% |
| CHH | 0.369 | 16.6% | 40.2% | 12.3% |

The global big-3 carry the highest loadings; the lowest-vol [[Hilton]] takes the largest raw PC1-mimic weight. [[Choice Hotels]] (the highest-vol, most-domestic economy name) has the lowest loading (0.369) and weight — the cohort outlier, consistent with the economy/upscale split.

### Distinctness — travel-cyclical/discretionary beta, not a distinct lodging factor

![[hotels-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The big-3 block is warm and just as warm against XLY and the airlines/cruises; the economy pair (WH/CHH) is cooler against everything except each other.*

The +0.150 intra-advantage versus the other travel cyclicals is real but modest, and the dendrogram shows why it does not amount to a distinct factor: the big-3 merge with airlines/cruises/XLY/PEJ at ~0.46, so the global hotel brands are travel-demand/discretionary beta — own XLY or the leisure ETF PEJ. This is the contrast that completes the travel-cyclicals set: [[Airlines]] (fuel-inverse, market-neutral), [[Cruise lines]] (+0.178), and [[Online travel]] (+0.178, no pure ETF) each carry a distinct travel sub-factor; hotels do not — the big global brands are generic discretionary beta, and only the economy franchisors trade apart (and as a fee-stable pair, not a hotel factor either). Distinct from [[SPY]] only via the discretionary/travel tilt.

### Historical tightness evolution

![[hotels-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2022–2026. Regime-dependent — tight in travel-recovery windows (0.86 in 2022, 0.78 in 2025), loose otherwise (0.54 in 2024).*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2022 | 0.859 | 88.7% |
| 2023 | 0.788 | 83.2% |
| 2024 | 0.539 | 65.1% |
| 2025 | 0.778 | 82.5% |
| 2026 | 0.630 | 70.5% |

Latest 90-day reading: intra 0.558, PC1 65.6%. The hotel cohort tightens when travel demand is the dominant market story (the 2022 reopening, the 2025 travel-spending wave) and loosens otherwise — the regime-dependent signature of a travel-cyclical, not a structural factor. The holdout WEAKENED (0.69) and the big-3/economy split confirm it: hotels are a conditional travel-demand expression, best held as XLY/PEJ rather than a bespoke lodging basket.

## Related

- [[Online travel]] — OTAs, the distinct travel sub-factor (+0.178); hotels are the travel leg that is NOT distinct
- [[Airlines]] — the fuel-inverse travel cyclical
- [[Cruise lines]] — the demand-channel travel cyclical (+0.178 from airlines)
- [[Marriott]], [[Hilton]], [[Hyatt]] — the global upscale big-3 (the travel-cyclical/discretionary core)
- [[Wyndham]], [[Choice Hotels]] — the domestic economy franchisors (the separate fee-stable pair)
- [[Consumer Staples]] — contrast: staples is the defensive discretionary; hotels are the cyclical discretionary
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-19. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/mar.yaml`; registry row 2026-06-19. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
