---
aliases: [Net-lease REITs, Net lease REITs, Triple-net REITs, Bond-proxy REITs, Net-lease cohort]
tags: [sector, real-estate, reit, net-lease, cluster-validation]
---

# Net-lease REITs

> [!success] Cluster status: marginally VALIDATED — a distinct, durable, defensive net-lease factor; the campaign's most marginal distinct factor, and NOT the bond-proxy it is reputed to be (Jun 2026)
> The net-lease REITs ([[Realty Income|O]]/[[W.P. Carey|WPC]]/[[NNN REIT|NNN]]/[[Agree Realty|ADC]]/[[Essential Properties|EPRT]]) trade as one tight, durable factor — intra-corr 0.699, PC1 76.1%, rejecting the independence, random-basket and vol-matched nulls at the 0.0001 floor, with a STABLE holdout (0.91). It clears the distinctness bar, but barely: a +0.106 intra-advantage versus broad REITs ([[VNQ]]/[[XLRE]]) and a NARROW separable band [0.35–0.40] (width 0.05 — the narrowest in the campaign; VNQ contaminates from 0.45). Two clean findings stand regardless of the marginal tier: (1) it is NOT a bond-proxy at the co-movement level — despite the reputation, these cluster with broad REITs, not Treasuries (+0.481 versus [[TLT]]/[[IEF]], which form their own separate cluster; the "bond-proxy" label is about valuation-to-rates over time, not daily co-movement); and (2) near-zero market beta (−0.008 versus SPY, +0.707 intra-advantage) — the most defensive REIT sub-sector, very low vol (16–18%). It completes the REIT sub-sector map: [[Residential REITs|residential]] distinct, [[Tower REITs|tower]] = VNQ, [[Self-storage REITs|self-storage]] = VNQ (big-three a sub-factor), net-lease marginally distinct.

The defensive, low-beta corner of REITs — distinct, but only just. Net-lease REITs own single-tenant properties on long (10–25 year) triple-net leases, so cash flows are bond-like and the equities are the most defensive, lowest-vol, least-market-correlated REITs. That homogeneity gives them a real, durable common factor — but it is only narrowly separable from the broad REIT complex, because at the end of the day they are still rate-sensitive real estate that VNQ largely captures. They are distinct enough to register a band, marginal enough that the band is the campaign's thinnest.

## Sector performance

![[net-lease-performance.png]]
*Normalized total return since Jan 2023, the five net-lease REITs vs broad REITs [[VNQ]]. A tight, low-vol, defensive block that tracks VNQ closely but with the campaign's thinnest distinct edge (+0.106) — the marginal-distinct REIT sub-sector.*

## Cluster validation

The candidate cohort is five net-lease REITs — [[Realty Income|O]], [[W.P. Carey|WPC]], [[NNN REIT|NNN]], [[Agree Realty|ADC]], [[Essential Properties|EPRT]] — tested against broad REITs ([[VNQ]]/[[XLRE]]), the duration/Treasury proxy ([[TLT]]/[[IEF]]), and the market (SPY). 1Y window through 2026-06-18, threshold 0.5. All US-listed/synchronous. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.699 [0.612–0.791] | Tight, no outlier; weekly 0.731 (synchronous) |
| PC1 explained variance | 76.1% | A strong single factor (weekly 78.5%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0001 | Far beyond a random 5-pick |
| Vol-matched null p (10k) | 0.0004 / 0.0006 | Real beyond shared vol |
| Holdout (2Y split) | STABLE 0.91 | train 0.770 → test 0.701 — durable |
| Threshold stable width | 0.05 [0.35–0.40] | NARROW — the campaign's thinnest band; VNQ contaminates from 0.45 |
| Intra-adv vs broad REITs (VNQ/XLRE) | +0.106 | Modest — marginally distinct from broad REITs |
| Intra-adv vs duration (TLT/IEF) | +0.481 | NOT a bond-proxy — clusters with REITs, not Treasuries |
| Intra-adv vs market (SPY) | +0.707 | Near-zero market beta (corr −0.008) — the most defensive REITs |

Config: `scripts/cluster_configs/net_lease_reits.yaml`; registry row 2026-06-20.

### Boundary — a narrow clean band; bonds stay out, broad REITs join at 0.45

![[net-lease-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The five net-lease REITs cluster with broad REITs [[VNQ]]/[[XLRE]] — but Treasuries [[TLT]]/[[IEF]] form their OWN separate cluster (the net-lease names do NOT move with bonds day-to-day), and SPY is separate. The "bond-proxy" sits with REITs, not bonds.*

The threshold scan returns a NARROW stable band — the five form a clean, uncontaminated cluster only across [0.35–0.40] (width 0.05):

| Threshold | Joins the cohort cluster | Read |
|---|---|---|
| 0.35–0.40 | (nothing) | the five net-lease names alone — the narrow separable band |
| 0.45 | VNQ, XLRE | broad REITs contaminate just above the band |
| 0.50+ | (REIT complex) | one rate-driven REIT cluster |

That broad REITs join at 0.45 — barely above the band — is why this is the campaign's most marginal distinct factor: the separation is real (a band exists, unlike [[Self-storage REITs|self-storage's]] 4-name) but thin. Treasuries never join (they are a different cluster entirely), confirming the no-bond-proxy finding.

### Topology — a tight tree, O+NNN the core

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | O + NNN | 0.209 | the tightest pair (corr 0.79) — the two retail-net-lease bellwethers |
| 2 | WPC + (O+NNN) | 0.282 | W.P. Carey joins |
| 3 | ADC + core | 0.299 | Agree joins |
| 4 | EPRT + core | 0.334 | Essential Properties closes the cohort |

All five close by 0.334 — a tight, single tree with no outlier. [[Realty Income|O]]/[[NNN REIT|NNN]] are the core; [[Essential Properties|EPRT]] (middle-market/service tenants) the loosest but still inside. PC1 explains 76.1%.

### PC1 index weights — a flat, very-low-vol factor

![[net-lease-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 76.1% (weekly 78.5%) with near-equal loadings (0.43–0.47) — a single common factor. The annualized vols (16–18%) are the lowest of any cohort this session — these are the defensive, low-beta REITs.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| O | 0.447 | 20.0% | 17.1% | 19.9% |
| WPC | 0.444 | 19.9% | 17.3% | 19.6% |
| NNN | 0.466 | 20.8% | 16.6% | 21.4% |
| ADC | 0.447 | 20.0% | 16.1% | 21.2% |
| EPRT | 0.431 | 19.3% | 18.3% | 18.0% |

Loadings are flat (0.43–0.47) and vols uniformly low (16–18%): a homogeneous, defensive factor. (The holdout's low PC1-loadings correlation, 0.28, is the near-flat-vector effect — both halves are tight, 0.77→0.70, so the factor is durable; the loadings-corr just measures noise around a near-uniform vector, as with the commodity cohorts.)

### Distinctness — a thin edge over VNQ, and decidedly not bonds

![[net-lease-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A uniformly warm five-name block (0.61–0.79); broad REITs warm against it; Treasuries (TLT/IEF) cool against it; SPY essentially uncorrelated.*

The intra-advantage numbers locate it precisely: +0.106 versus broad REITs (a thin but positive edge — enough, with the band, to register as distinct), +0.481 versus Treasuries, and +0.707 versus the market. The +0.481 over TLT/IEF is the decisive negative result: net-lease REITs are not the duration trade — their daily returns track the REIT complex, not the bond complex, even though their long fixed leases make them rate-sensitive in valuation. And the near-zero SPY correlation (−0.008) makes them the most defensive REIT sub-sector. Distinct from broad REITs, yes — but marginally, and there is no pure net-lease ETF, so the basket is the only way to own the thin edge.

### Historical tightness evolution — durable

![[net-lease-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Durably tight — 0.68–0.78 across the period, with no weak year (latest 90-day 0.764, tightening). The most consistent REIT sub-sector of the four.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.737 | 79.0% |
| 2022 | 0.684 | 74.8% |
| 2023 | 0.778 | 82.3% |
| 2024 | 0.706 | 76.5% |
| 2025 | 0.741 | 79.3% |
| 2026 | 0.684 | 74.8% |

*Durable and consistent — tight every year, never below 0.68, latest 0.764. Unlike [[Self-storage REITs|self-storage]] (which loosened to 0.64 in 2026), net-lease held together — its defensive, homogeneous character makes it the steadiest REIT factor, which is what earns it the marginal distinct status despite the thin ETF edge.*

## Related

- [[Residential REITs]] — the clearly-distinct single-asset REIT (rent/supply driver, +0.360); net-lease is the marginal one (+0.106)
- [[Self-storage REITs]] — the ETF-replicable single-asset REIT (+0.069); net-lease edges past it with a real (narrow) band
- [[Tower REITs]] — the other VNQ-embedded REIT sub-sector; net-lease completes the four-way REIT map
- [[Realty Income]], [[W.P. Carey]], [[NNN REIT]], [[Agree Realty]], [[Essential Properties]] — the cohort members
- [[VNQ]], [[XLRE]] — broad REIT ETFs (the cohort's thin edge is over these); [[TLT]], [[IEF]] — the duration control the cohort does NOT track
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/net_lease_reits.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
