---
aliases: [Franchised auto dealers, Auto dealers, Auto dealerships, Auto retail, Dealer consolidators, Auto dealer cohort]
tags: [sector, consumer-discretionary, auto-retail, dealer, cluster-validation]
---

# Franchised auto dealers

> [!success] Cluster status: VALIDATED — a distinct auto-retail factor; the campaign's 10th, and the third leg of the auto complex (Jun 2026)
> The franchised auto-dealer consolidators ([[AutoNation|AN]]/[[Lithia Motors|LAD]]/[[Penske Automotive|PAG]]/[[Group 1 Automotive|GPI]]/[[Sonic Automotive|SAH]]/[[Asbury Automotive|ABG]]) trade as one tight, durable factor — intra-corr 0.719, PC1 76.7%, rejecting the independence, random-basket and vol-matched nulls all at the 0.0001 floor — and it is genuinely distinct. The six form their own cluster with a WIDE separable threshold band [0.35–0.50] (the retail ETFs [[XRT]]/[[XLY]] and SPY contaminate only at 0.55, used-car [[CarMax|KMX]] at 0.60), a +0.207 intra-advantage versus the retail ETFs (railroads/trucking territory), +0.279 versus used-car, and +0.391 versus the market. The holdout is STABLE (0.94) and the cohort is durable — 0.70–0.81 every year 2020–25 (softening to 0.64 in 2026 on auto-affordability pressure). No pure franchised-dealer ETF exists, so this is a distinct, ownable factor. It completes the auto complex: [[Automakers]] are falsified (driver-divergence), [[Auto parts retail|auto-parts retail]] is distinct only as the ORLY+AZO pair, and the franchised dealers are a full distinct cohort.

The homogeneous retail-consolidator model. The six are near-identical businesses — franchised new-vehicle dealerships plus used vehicles, finance & insurance (F&I), and high-margin parts & service, run as acquisitive roll-ups — all levered to the same US auto-retail cycle: new-vehicle SAAR, affordability and rates, used-vehicle pricing, and the consolidation of a still-fragmented dealer market. That shared model and driver make them one of the tighter consumer cohorts in the campaign, and crucially they separate from broad cyclical retail (XRT/XLY) rather than dissolving into it — unlike apparel or most discretionary labels. They are also distinct from used-only retail ([[CarMax|KMX]]), a different model on a different (used-pricing) cycle.

## Cluster validation

The candidate cohort is six franchised auto-dealer groups — [[AutoNation|AN]], [[Lithia Motors|LAD]], [[Penske Automotive|PAG]], [[Group 1 Automotive|GPI]], [[Sonic Automotive|SAH]], [[Asbury Automotive|ABG]] — tested against used-car retail ([[CarMax|KMX]]), the retail / discretionary ETFs ([[XRT]]/[[XLY]]), and the market (SPY). 1Y window through 2026-06-18, threshold 0.5. All US-listed/synchronous. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.719 [0.549–0.779] | Tight and uniform, no outlier; weekly 0.729 (synchronous) |
| PC1 explained variance | 76.7% | A strong single factor (weekly 77.5%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0001 | Far beyond a random 6-pick |
| Vol-matched null p (10k) | 0.0001 | Real beyond shared vol — a genuine factor |
| Holdout (2Y split) | STABLE 0.94 | train 0.768 → test 0.719; loadings corr 0.77 (same factor, durable) |
| Threshold stable width | 0.15 [0.35–0.50] | WIDE — clean; XRT/XLY/SPY contaminate only at 0.55, KMX at 0.60 |
| Intra-adv vs retail ETFs (XRT/XLY) | +0.207 | Distinct from cyclical retail — the decisive number |
| Intra-adv vs used-car (KMX) | +0.279 | Distinct from used-only retail (a different model) |
| Intra-adv vs market (SPY) | +0.391 | Not market beta |

Config: `scripts/cluster_configs/auto_dealers.yaml`; registry row 2026-06-20.

### Boundary — a clean cluster across [0.35–0.50]; retail and used-car stay out

![[auto-dealers-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The six dealers form their own cluster; the retail/discretionary ETFs [[XRT]]/[[XLY]] and SPY are a separate cluster, and used-car [[CarMax|KMX]] is a singleton. The dealers separate from both broad retail and used-only retail.*

The threshold scan returns a WIDE stable band — the six are one intact, uncontaminated cluster across [0.35–0.50] (width 0.15):

| Threshold | Joins the cohort cluster | Read |
|---|---|---|
| 0.35–0.50 | (nothing) | the six dealers alone — the separable band |
| 0.55 | XRT, XLY, SPY | broad retail / discretionary / market join together |
| 0.60 | + KMX | used-car retail joins last |

That broad retail and the market join together at 0.55 (the generic risk-on threshold), with used-car [[CarMax|KMX]] joining even later, is the distinct-factor signature: below 0.55 the dealers stand alone. Same shape as [[Trucking and LTL|trucking]] and [[Tankers|tankers]].

### Topology — a tight tree, LAD the last to join

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | PAG + ABG | 0.221 | the tightest pair (corr 0.78) |
| 2 | AN + (PAG+ABG) | 0.231 | AutoNation joins |
| 3 | GPI + core | 0.240 | Group 1 joins |
| 4 | SAH + core | 0.286 | Sonic joins |
| 5 | LAD + core | 0.333 | Lithia closes the cohort |

All six close by 0.333 — a tight, single tree with no outlier. [[Penske Automotive|PAG]]/[[Asbury Automotive|ABG]]/[[AutoNation|AN]] form the tight core; [[Sonic Automotive|SAH]] (largest used/EchoPark exposure) and [[Lithia Motors|LAD]] (the most acquisitive consolidator) are the loosest but still well inside the cut. PC1 explains 76.7%.

### PC1 index weights — a flat, balanced factor

![[auto-dealers-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 76.7% (weekly 77.5%) with near-equal loadings (0.38–0.42) — a single common factor, no name dominating.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| AN | 0.420 | 17.2% | 28.3% | 19.3% |
| LAD | 0.383 | 15.7% | 33.3% | 15.0% |
| PAG | 0.419 | 17.1% | 26.4% | 20.6% |
| GPI | 0.414 | 16.9% | 33.7% | 16.0% |
| SAH | 0.390 | 16.0% | 40.8% | 12.4% |
| ABG | 0.421 | 17.2% | 32.8% | 16.7% |

Loadings are flat (0.38–0.42): no single name carries the factor. The lowest-vol names [[Penske Automotive|PAG]] (26%, premium/diversified) and [[AutoNation|AN]] take the largest vol-adjusted weights; the higher-vol [[Sonic Automotive|SAH]] (41%, EchoPark) the smallest.

### Distinctness — a retail sub-factor that doesn't dissolve into retail

![[auto-dealers-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A uniformly warm six-name block (0.55–0.78); the retail ETFs cooler against it, used-car ([[CarMax|KMX]]) cooler still — the dealers are warmer with each other than with either.*

The intra-advantage numbers make the verdict quantitative: +0.207 versus the retail ETFs (the dealers cohere more with each other than with cyclical retail), +0.279 versus used-car [[CarMax|KMX]], and +0.391 versus the market. A distinct factor needs to out-cohere the relevant ETF; +0.207 over XRT/XLY (with a WIDE separable band) clears it cleanly — the same margin as [[Railroads]] and [[Trucking and LTL]]. There is no franchised-dealer ETF, so the only way to own this factor is the basket. The contrast with [[Athletic footwear and apparel|apparel]] (which dissolved into XRT at −0.053) is instructive: a homogeneous business model with a shared operating driver separates from broad retail; a set of brand-momentum names does not.

### Historical tightness evolution — durable across the cycle

![[auto-dealers-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Durably tight — 0.70–0.81 across the period, peaking in the 2022 and 2025 auto-retail windows and easing to 0.64 in 2026 as affordability/rate pressure introduced some dispersion. A real factor varying in strength with the auto cycle, not in existence.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.745 | 78.8% |
| 2021 | 0.705 | 75.5% |
| 2022 | 0.812 | 84.4% |
| 2023 | 0.741 | 78.7% |
| 2024 | 0.739 | 78.4% |
| 2025 | 0.805 | 83.8% |
| 2026 | 0.642 | 70.5% |

*Durable, not regime-dependent in existence — a real cluster every year (0.70–0.81), with the 2026 softening (0.64) the only weak spot, on auto-affordability/rate pressure. The holdout STABLE (0.94) confirms the factor structure is preserved across the split (loadings corr 0.77).*

## Related

- [[Automakers]] — the OEM leg of the auto complex (falsified — TSLA/legacy/EV-startups diverge)
- [[Auto parts retail]] — the aftermarket leg (distinct only as the ORLY+AZO pair); franchised dealers are the third, full-cohort leg
- [[AutoNation]], [[Lithia Motors]], [[Penske Automotive]], [[Group 1 Automotive]], [[Sonic Automotive]], [[Asbury Automotive]] — the cohort members
- [[CarMax]] — used-car-retail control; the dealers are distinct from it (+0.279)
- [[XRT]], [[XLY]] — the retail/discretionary ETFs the cohort out-coheres (+0.207)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/auto_dealers.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
