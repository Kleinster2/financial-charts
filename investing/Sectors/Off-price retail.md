---
aliases: [Off-price retail, Off-price retailers, Off-price apparel, Value retail, Treasure-hunt retail, Off-price cohort]
tags: [sector, consumer-discretionary, retail, off-price, cluster-validation]
---

# Off-price retail

> [!warning] Cluster status: NOT a distinct factor — off-price is broad-retail beta, statistically indistinguishable from [[XRT]] (+0.012); below the cohesion floor, it shatters into a [[TJX]]+[[Ross Stores|ROST]] pair and singletons (Jun 2026)
> The off-price / value retailers ([[TJX]]/[[Ross Stores|ROST]]/[[Burlington|BURL]]/[[Ollie's Bargain Outlet|OLLI]]) do not form a distinct factor. Intra-corr 0.390 — BELOW the 0.50 floor (weekly 0.467), PC1 54.7% — and the decisive number is a +0.012 intra-advantage versus the retail ETFs ([[XRT]]/[[XLY]]): the off-price names correlate with broad retail (0.378) essentially as much as with each other (0.390), so the cohort is just retail beta, not a separable off-price factor. The nulls reject only weakly (random-basket 0.015, vol-matched 0.018 — shared retail-cyclical beta, not the 0.0001 of a real factor), there is no clean threshold band ("boundary-dependent / falsification candidate"), and the holdout COLLAPSED (0.63; train 0.610 → test 0.387). At the 0.50 cut it shatters: only [[TJX]]+[[Ross Stores|ROST]] cohere (0.55), [[Burlington|BURL]] joins at 0.567, [[Ollie's Bargain Outlet|OLLI]] (closeout) is a near-orthogonal outlier (0.27-0.37, joins 0.693) — and [[XRT]] itself clusters with the department stores ([[Macy's|M]]/[[Kohl's|KSS]], 0.33-0.38), tighter than the off-price names are to each other. Only modestly distinct from the dept stores (+0.141) and the market (+0.134). Own XRT; the one real structure is the TJX+ROST pair. See below.

The category that the market does not trade as a category. Off-price retailers run the same counter-cyclical "treasure-hunt" model — buying excess inventory cheap and selling it at a discount — which makes them a recognizable consumer group, but recognizability is not a shared price factor. The names move on broad retail/discretionary cycles (consumer spending, inventory gluts, trade-down) that [[XRT]] already prices, plus large idiosyncratic components (TJX's quality-compounder premium, Burlington's turnaround, Ollie's closeout-supply story). The result is the apparel shape: a real retail-beta cohort with no distinct off-price factor on top of the ETF.

## Sector performance

![[off-price-performance.png]]
*Normalized total return since Jan 2023, the four names vs broad retail [[XRT]]. [[TJX]] is the steady compounder (low 18.5% vol); [[Ross Stores|ROST]] tracks it; [[Burlington|BURL]] and [[Ollie's Bargain Outlet|OLLI]] are higher-vol and divergent. The spread among the four — and their loose relationship to XRT — is the dispersion behind the not-a-factor verdict: there is no single "off-price" line.*

## Cluster validation

The candidate cohort is four off-price / value retailers — [[TJX]] (TJ Maxx/Marshalls/HomeGoods), [[Ross Stores|ROST]] (Ross/dd's), [[Burlington|BURL]], [[Ollie's Bargain Outlet|OLLI]] (closeout) — tested against broad retail ([[XRT]]/[[XLY]]), the department stores ([[Macy's|M]]/[[Kohl's|KSS]]), and the market (SPY). 1Y window through 2026-06-18 (198 obs), threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.390 [0.266–0.553] | BELOW the floor; weekly 0.467; only TJX+ROST tight |
| PC1 explained variance | 54.7% | Weak; big PC2+PC3 (35%) — idiosyncratic |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.015 | Beats a random retail 4-pick only WEAKLY |
| Vol-matched null p (10k) | 0.018 | Weak — shared retail-cyclical beta, not a factor |
| Holdout (2Y split) | WEAKENED 0.63, loadings-corr 0.80 | train 0.610 → test 0.387 — cohesion collapsed |
| Threshold stable width | 0.00 (none) | Never a clean cluster — boundary-dependent |
| Intra-adv vs retail ETFs (XRT/XLY) | +0.012 | ≈ ZERO — off-price IS broad retail |
| Intra-adv vs dept stores (M/KSS) | +0.141 | Modestly tighter than the struggling dept stores |
| Intra-adv vs market (SPY) | +0.134 | Retail-cyclical, not a separable factor |

Config: `scripts/cluster_configs/off_price_retail.yaml`; registry row 2026-06-22.

### Boundary — the off-price names shatter; the retail ETF sits with the department stores

![[off-price-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Only [[TJX]]+[[Ross Stores|ROST]] (orange) cohere; [[Burlington|BURL]] and [[Ollie's Bargain Outlet|OLLI]] are singletons. The retail ETF [[XRT]] clusters with the department stores [[Macy's|M]]/[[Kohl's|KSS]] (red, 0.33-0.38) — tighter than the off-price names are to each other — and [[XLY]]/[[SPY]] form the market block. There is no off-price cluster.*

The threshold scan returns no clean band — the four never form an uncontaminated single cluster at any cut, because only TJX+ROST are tight and BURL/OLLI join above 0.50. That, with the ~zero intra-advantage over [[XRT]], is the not-distinct signature: off-price is a slice of broad retail, not a separable factor.

### Topology — a TJX+ROST pair, then two stragglers

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | TJX + ROST | 0.447 | the two mega off-price names — the only real pair (corr 0.55) |
| 2 | BURL + (TJX+ROST) | 0.567 | Burlington joins above the cut |
| 3 | OLLI + core | 0.693 | [[Ollie's Bargain Outlet\|OLLI]] (closeout) joins last, far out — the outlier |

The cohort never closes below the cut: [[TJX]]+[[Ross Stores|ROST]] at 0.447 is the only sub-0.50 join; [[Burlington|BURL]] (0.567) and [[Ollie's Bargain Outlet|OLLI]] (0.693) attach above it. The TJX+ROST pair (0.55) sits below the ~0.60 sub-pair-robustness threshold, so it is not carved out as a distinct sub-factor.

### PC1 index weights — TJX/ROST carry it, OLLI the low-weight outlier

![[off-price-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 54.7% with 35% in PC2+PC3 — the names share little. [[TJX]] (low 18.5% vol) and [[Ross Stores|ROST]] anchor PC1; [[Ollie's Bargain Outlet|OLLI]] loads lowest (0.41).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| TJX | 0.510 | 25.70% | 18.54% | 37.82% |
| ROST | 0.571 | 28.73% | 25.27% | 31.03% |
| BURL | 0.496 | 24.95% | 40.65% | 16.75% |
| OLLI | 0.410 | 20.63% | 39.13% | 14.39% |

[[TJX]] is the low-vol quality compounder (18.5% vol, largest PC1-mimic weight); [[Burlington|BURL]] and [[Ollie's Bargain Outlet|OLLI]] are high-vol (39-41%) and carry the small weights — a cohort with no even common mode.

### Distinctness — indistinguishable from broad retail

![[off-price-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. Only TJX/ROST run warm (0.55); BURL and OLLI are cool against the others; the off-price block is no warmer to itself than to XRT.*

The +0.012 intra-advantage over the retail ETFs is the whole story: the off-price names correlate with [[XRT]]/[[XLY]] as much as with each other, so there is no off-price factor distinct from broad retail. The modest edges over the department stores (+0.141) and the market (+0.134) just say off-price is slightly more cohesive than the worst of retail and carries retail-cyclical beta. There is no separable factor to own beyond [[XRT]]; the only real co-movement is the [[TJX]]+[[Ross Stores|ROST]] pair, and even that is a moderate 0.55. This is the [[Athletic footwear and apparel|apparel]] outcome — a recognizable consumer category that dissolves into the retail ETF.

### Historical tightness evolution — chronically loose, regime-dependent

![[off-price-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Never durably tight — oscillating 0.37–0.58, with no sustained period above 0.58; it dropped to 0.42 in 2024, recovered to 0.55 in 2025, and collapsed to 0.37 in 2026 (latest 90-day 0.410). The collapse is what the holdout reads as WEAKENED 0.63.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.536 | 66.8% |
| 2022 | 0.559 | 68.0% |
| 2023 | 0.581 | 69.9% |
| 2024 | 0.424 | 57.4% |
| 2025 | 0.545 | 66.0% |
| 2026 | 0.370 | 53.4% |

*Loose throughout and currently at a low (0.37) — off-price cohesion comes and goes with the retail cycle rather than holding as a structural factor.*

## Where this sits in the campaign

Off-price retail joins the retail map as another not-a-factor, and the contrast across retail is consistent:

- [[Auto parts retail|Auto parts retail (ORLY+AZO)]] — a DISTINCT pair (+0.599 vs XRT): the premium aftermarket duopoly genuinely escapes broad retail.
- [[Athletic footwear and apparel]] — dissolves into XRT (the apparel shape).
- Off-price retail (this note) — also dissolves into XRT (+0.012); only TJX+ROST cohere, and below the sub-pair threshold.

The lesson: retail distinctness requires a driver broad retail does not price (the auto-aftermarket's counter-cyclical, non-discretionary demand). Off-price shares the broad consumer-spending/inventory cycle that [[XRT]] already captures, so — like apparel — it is retail beta, not a factor.

## Related

- [[TJX]], [[Ross Stores]], [[Burlington]], [[Ollie's Bargain Outlet]] — the cohort members (TJX+ROST the only real pair; OLLI the closeout outlier)
- [[XRT]], [[XLY]] — the retail ETFs the cohort is indistinguishable from (own these); [[Macy's]], [[Kohl's]] — the department-store controls (XRT clusters with them)
- [[Auto parts retail]] — the distinct retail pair (the contrast); [[Athletic footwear and apparel]] — the other XRT-dissolving retail cohort
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-22. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/off_price_retail.yaml`; registry row 2026-06-22. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
