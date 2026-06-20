---
aliases: [Residential REITs, Apartment REITs, Residential REIT cluster, Apartment REIT cluster]
tags: [sector, reit, real-estate, residential-reit, apartments, cluster-validation]
---

# Residential REITs

> [!success] Cluster status: VALIDATED — a distinct, extraordinarily tight apartment-REIT factor; the tightest cohort in the campaign, separable from broad REITs (Jun 2026)
> The listed apartment REITs ([[AvalonBay|AVB]]/[[Equity Residential|EQR]]/[[Essex Property Trust|ESS]]/[[Mid-America Apartment Communities|MAA]]/[[UDR]]/[[Camden Property Trust|CPT]]) trade as one factor — and it is the tightest in the whole campaign: intra-corr 0.849 (PC1 87.5%, all six joining below 0.165), rejecting every null at the 0.0001 floor, with a STABLE 2Y holdout (ratio 0.96) and durable 0.84–0.93 cohesion every year since 2020. It is distinct from broad real estate: a +0.360 intra-advantage over the REIT/real-estate ETFs ([[VNQ]]/[[XLRE]]), and a clean separable cluster across thresholds [0.20–0.35] (stable width 0.15). VNQ is the nearest broad proxy — it holds these names, so it absorbs them at the looser 0.50 cut — but the pure apartment-REIT basket is meaningfully tighter and separates at tighter thresholds. The seventh genuinely distinct non-ETF factor in the campaign, and the most cohesive of them all.

The purest single-factor cohort. Six apartment REITs own the same asset (US multifamily) and trade on the same two variables — long rates (cap rates/discount rates) and apartment fundamentals (rent growth, occupancy, supply) — so they move almost as one security. That homogeneity makes residential REITs the tightest cohort the campaign has measured, tighter even than the semiconductor-equipment quartet. The basket is a cleaner expression of the apartment-rate factor than broad [[VNQ]], which dilutes it with offices, retail, industrial, towers, and data centers.

## Cluster validation

The candidate cohort is the six listed apartment REITs — [[AvalonBay|AVB]], [[Equity Residential|EQR]], [[Essex Property Trust|ESS]], [[Mid-America Apartment Communities|MAA]], [[UDR]], [[Camden Property Trust|CPT]] — tested against the broad REIT ETF [[VNQ]], the real-estate sector ETF (XLRE), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.849 [0.813–0.926] | the campaign's highest; weekly 0.836 (robust) |
| PC1 explained variance | 87.5% | a near-single-security cohort (weekly 86.4%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | far beyond a random 6-pick |
| Vol-matched null p | 0.0001 / 0.0001 | cohesion exceeds vol-matched baskets |
| Holdout (2Y split) | STABLE 0.96 | train 0.893 → test 0.860 — durable across regimes |
| Threshold stable width | 0.15 [0.20–0.35] | a clean separable cluster below the VNQ-contamination cut |
| Intra-adv vs ETFs (VNQ/XLRE/SPY) | +0.360 | distinct from broad real estate |

All US-listed. Config: `scripts/cluster_configs/avb.yaml`; registry row 2026-06-20.

### Boundary — the six apartment REITs separate from VNQ below 0.35

![[resireit-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. At this cut the six apartment REITs absorb the REIT ETFs [[VNQ]]/[[XLRE]] (which hold them), but the threshold scan shows the six form a clean cluster WITHOUT the ETFs across [0.20–0.35] (stable width 0.15). SPY is far apart — these are low-market-beta, rate-driven names.*

The cohort is so tight (closing at 0.165) that its separable band sits at low thresholds [0.20–0.35]; VNQ/XLRE join only above that. Combined with the +0.360 intra-advantage over the ETFs and the STABLE holdout, this is a VALIDATED, distinct factor: the apartment-REIT basket is a tighter, cleaner expression of the apartment-rate factor than broad VNQ. VNQ is the nearest proxy (it contains these names) but dilutes them with every other property type.

### Topology — a Sunbelt pair and a coastal pair, all extremely tight

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | MAA + CPT | 0.074 | the Sunbelt pair — the tightest pair in the campaign |
| 2 | UDR + (MAA+CPT) | 0.134 | the diversified name joins the Sunbelt core |
| 3 | AVB + EQR | 0.138 | the coastal pair |
| 4 | ESS + (AVB+EQR) | 0.149 | the West Coast name joins the coastal core |
| 5 | the two cores merge | 0.165 | the whole cohort closes — extraordinarily tight |

Every join is below 0.17. There is a faint geographic sub-structure — a Sunbelt cluster ([[Mid-America Apartment Communities|MAA]]/[[Camden Property Trust|CPT]]/[[UDR]]) and a coastal cluster ([[AvalonBay|AVB]]/[[Equity Residential|EQR]]/[[Essex Property Trust|ESS]]) — but they merge at 0.165, far below the cut, so it is one factor. PC1 explains 87.5%, the highest in the campaign.

### PC1 index weights

![[resireit-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 87.5% (weekly 86.4%) — the apartment-rate factor accounts for nearly all of the variance.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| AVB | 0.402 | 16.4% | 20.2% | 16.2% |
| EQR | 0.410 | 16.7% | 20.1% | 16.6% |
| ESS | 0.405 | 16.5% | 19.6% | 16.8% |
| MAA | 0.414 | 16.9% | 19.2% | 17.5% |
| UDR | 0.406 | 16.6% | 20.4% | 16.1% |
| CPT | 0.412 | 16.8% | 19.8% | 16.9% |

Loadings and vols are nearly identical across all six — the signature of a near-homogeneous cohort. An equal-weight basket essentially IS PC1.

### Distinctness — distinct from broad REITs; VNQ the nearest proxy

![[resireit-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A uniformly hot six-name block; VNQ/XLRE are warm (they hold these names) but cooler than the six are against each other, and SPY is cold.*

The +0.360 intra-advantage versus the ETFs is the verdict: the apartment REITs are far more correlated with each other than with broad [[VNQ]]/[[XLRE]], so the pure-apartment basket is a distinct, tighter factor — separable at tight thresholds even though VNQ (which contains them) absorbs them at 0.50. Distinct from SPY too (low market beta — these are rate-driven). Own the apartment basket for the cleanest apartment-rate exposure; own VNQ only for diversified-property-type REIT beta.

### Historical tightness evolution

![[resireit-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Exceptionally tight throughout (0.84–0.93), never below 0.83 in six years.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.932 | 94.4% |
| 2021 | 0.851 | 87.6% |
| 2022 | 0.892 | 91.1% |
| 2023 | 0.907 | 92.3% |
| 2024 | 0.872 | 89.4% |
| 2025 | 0.911 | 92.6% |
| 2026 | 0.838 | 86.5% |

Latest 90-day reading: intra 0.856, PC1 88.0%. The factor is the most durable in the campaign — intra never falls below 0.83 in six years and the holdout is STABLE (0.96) — because the six own the same asset and trade on the same rate-and-rent variables. The defensive-REIT analogue of [[Solid waste]] and [[Drug distributors]] (homogeneous, low-market-beta factors that escape their broad sector ETFs), and the tightest of them all.

## Related

- [[Tower REITs]] — the sibling REIT cohort (cell towers); distinct from data-center REITs but also VNQ-embedded
- [[Solid waste]], [[Drug distributors]], [[Railroads]], [[Tobacco majors basket]], [[Life science tools]], [[Trucking and LTL]] — the other distinct non-ETF factors
- [[AvalonBay]], [[Equity Residential]], [[Essex Property Trust]] — the coastal apartment REITs
- [[Mid-America Apartment Communities]], [[Camden Property Trust]], [[UDR]] — the Sunbelt/diversified apartment REITs
- [[VNQ]], [[XLRE]] — the broad REIT ETFs (nearest proxies, which dilute the apartment factor)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/avb.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
