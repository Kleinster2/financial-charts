---
aliases: [Solid waste, Waste services, Waste and environmental services, Solid waste cohort, Waste oligopoly]
tags: [sector, industrials, environmental-services, waste, cluster-validation]
---

# Solid waste

> [!success] Cluster status: VALIDATED — a distinct, separable waste-services factor, NOT the environmental-services ETF; the run's most ETF-independent result (Jun 2026)
> The listed solid-waste majors ([[Waste Management|WM]]/[[Republic Services|RSG]]/[[Waste Connections|WCN]]/[[GFL Environmental|GFL]], with [[Casella Waste Systems|CWST]] as a loose satellite) trade as one factor — intra-corr 0.583 (weekly 0.656, HIGHER), PC1 67.2%, rejecting the random-basket and vol-matched nulls at the 0.0002 floor — and, unlike almost every other cohort in the campaign, they are NOT captured by their sector ETF. The decisive number is a +0.424 intra-advantage versus the environmental-services ETF [[EVX]] and the industrials/market ETFs (the largest distinctness margin in the campaign): EVX is diluted by smaller water/remediation/consulting names and clusters with [[XLI]]/SPY, not with the waste oligopoly. The big-4 form a clean cluster with a stable threshold band (width 0.15, [0.55–0.70]) — wider than railroads. Own the WM/RSG/WCN/GFL basket; the ETF does not give you this factor. This is the third genuinely distinct non-ETF factor in the fresh-cohort campaign, alongside [[Railroads]] and [[Tobacco majors basket|tobacco]].

The cleanest oligopoly in the campaign. Four national waste majors run the same business — route-density collection, landfill disposal, and pricing power well above inflation — with near-identical defensive, low-volatility, pricing-led economics. That shared model produces a tight, durable factor that a diversified environmental-services ETF cannot replicate, because the ETF spreads across smaller, different businesses. The waste majors are a basket, not an ETF trade.

## Sector performance

![[waste-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[EVX]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is the five listed solid-waste names — [[Waste Management|WM]], [[Republic Services|RSG]], [[Waste Connections|WCN]], [[GFL Environmental|GFL]], [[Casella Waste Systems|CWST]] — tested against the environmental-services ETF [[EVX]], industrials (XLI), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.583 [0.448–0.812] | above the 0.50 floor; weekly 0.656 (HIGHER — robust, not async noise) |
| PC1 explained variance | 67.2% | dominant single factor (weekly 73.3%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0002 | real cohesion beyond a random 5-pick |
| Vol-matched null p | 0.0002 / 0.0002 | cohesion exceeds vol-matched baskets — a real factor, not shared vol |
| Holdout (2Y split) | WEAKENED 0.74 | train 0.785 → test 0.582, but PC1 loadings corr 0.83 (same factor structure) |
| Threshold stable width | 0.15 [0.55–0.70] | a clean, separable cluster across a wide band (wider than railroads' 0.10) |
| Intra-adv vs ETFs (EVX/XLI/SPY) | +0.424 | the campaign's largest — the names track each other FAR more than the ETFs |

All US/Canada-listed. Config: `scripts/cluster_configs/wm.yaml`; registry row 2026-06-20 (cohort "Waste management").

### Boundary — the big-4 form their own cluster; the ETF sits elsewhere

![[waste-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. [[Waste Management|WM]]/[[Republic Services|RSG]]/[[Waste Connections|WCN]]/[[GFL Environmental|GFL]] form one clean cluster; the environmental-services ETF [[EVX]] does NOT join them — it clusters with [[XLI]]/SPY (broad industrials), because EVX is diluted by smaller non-waste environmental names. [[Casella Waste Systems|CWST]] is a singleton satellite (small-cap, higher vol). The ETF is on the wrong side of the boundary — the defining mark of a distinct, non-replicable factor.*

The threshold scan returns the cohort as a clean cluster across [0.55–0.70] (stable width 0.15), with no ETF/control contamination — robustly separable. Together with the +0.424 intra-advantage (the ETF does not capture the names) and the null rejections, this is a VALIDATED, distinct factor in the strict sense: not just real cohesion, but cohesion a liquid ETF cannot give you. It joins [[Railroads]] and [[Tobacco majors basket|tobacco]] as the only such results among the fresh cohorts.

### Topology — a tight big-4 core, CWST the satellite

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | WM + RSG | 0.188 | the tightest pair — the two largest, most alike majors |
| 2 | WCN + (WM+RSG) | 0.265 | the #3 joins the core |
| 3 | GFL + core | 0.446 | the deleveraging Canadian #4 joins, looser |
| 4 | CWST + core | 0.529 | the small-cap satellite, just above the 0.5 cut |

The big-4 (WM/RSG/WCN/GFL) close at 0.446 — a tight, separable core — while [[Casella Waste Systems|CWST]] joins only at 0.529 (above the cut), the loose small-cap satellite. PC1 explains 67.2%, with WM/RSG/WCN carrying near-equal top loadings.

### PC1 index weights

![[waste-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 67.2% (weekly 73.3%) — a genuine dominant factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| WM | 0.481 | 21.6% | 19.9% | 25.0% |
| RSG | 0.487 | 21.9% | 18.7% | 27.1% |
| WCN | 0.477 | 21.4% | 23.1% | 21.4% |
| GFL | 0.409 | 18.4% | 27.1% | 15.7% |
| CWST | 0.370 | 16.7% | 35.5% | 10.8% |

The big-3 ([[Waste Management|WM]]/[[Republic Services|RSG]]/[[Waste Connections|WCN]]) load almost identically (~0.48) and, being the lowest-vol names, carry the highest inverse-vol weights — the defensive core of the factor. [[GFL Environmental|GFL]] and [[Casella Waste Systems|CWST]] load lower (more idiosyncratic).

### Distinctness — the ETF is on the wrong side

![[waste-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A hot WM/RSG/WCN/GFL block; EVX/XLI/SPY are conspicuously cooler against the waste names than the names are against each other.*

The +0.424 intra-advantage versus the ETFs is the campaign's largest distinctness margin. The mechanism is specific: [[EVX]] is a small, equal-spread environmental-services ETF whose holdings reach well beyond the waste majors into water, remediation, and consulting — so its beta resembles broad industrials ([[XLI]]) more than the waste oligopoly, and it lands in the XLI/SPY cluster rather than with the names it nominally tracks. There is no liquid ETF that delivers the waste-major factor; it must be owned as the [[Waste Management|WM]]/[[Republic Services|RSG]]/[[Waste Connections|WCN]]/[[GFL Environmental|GFL]] basket.

### Historical tightness evolution

![[waste-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Durably moderate-to-tight (0.50–0.71), peaking in 2025; never breaking down.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.505 | 62.8% |
| 2022 | 0.549 | 65.7% |
| 2023 | 0.591 | 68.6% |
| 2024 | 0.504 | 61.5% |
| 2025 | 0.710 | 77.1% |
| 2026 | 0.572 | 66.2% |

Latest 90-day reading: intra 0.614, PC1 69.6%. The factor is durable — intra never falls below 0.50 in six years and the PC1 loadings are stable across the holdout (corr 0.83), so the WEAKENED 0.74 holdout ratio reflects a tightening-then-normalizing level (the 2025 peak at 0.71), not a breakdown of structure. A persistent, ownable factor — the defensive-oligopoly analogue of [[Railroads]] (the Class I rail oligopoly), with the same "basket beats the ETF" conclusion.

## Related

- [[Railroads]], [[Tobacco majors basket]] — the other genuinely distinct, non-ETF-replicable factors in the campaign
- [[Waste Management]], [[Republic Services]], [[Waste Connections]], [[GFL Environmental]] — the big-4 core
- [[Casella Waste Systems]] — the small-cap satellite
- [[EVX]] — the environmental-services ETF that fails to capture the factor
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/wm.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
