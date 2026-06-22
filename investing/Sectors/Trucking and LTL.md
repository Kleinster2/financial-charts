---
aliases: [Trucking and LTL, Trucking, LTL carriers, Truckload, Trucking cohort, Freight trucking]
tags: [sector, industrials, transports, trucking, ltl, cluster-validation]
---

# Trucking and LTL

> [!success] Cluster status: VALIDATED — a tight, distinct freight-trucking factor, separable from both rails and the transports ETF; the tightest fresh cohort in the batch (Jun 2026)
> The truckload and less-than-truckload carriers ([[Old Dominion Freight Line|ODFL]]/[[Saia|SAIA]]/[[XPO]]/[[Knight-Swift|KNX]]/[[Werner Enterprises|WERN]]/[[ArcBest|ARCB]]) trade as one very tight factor — intra-corr 0.742, PC1 78.6%, the tightest of the four fresh cohorts — rejecting the random-basket and vol-matched nulls at the 0.0001 floor, with a STRENGTHENING 2Y holdout (ratio 1.11; the cohort tightened in the recent half). It is distinct on two fronts: +0.280 versus the [[Railroads|rails]] ([[Union Pacific|UNP]]/[[CSX]]) — trucking and rail are two different freight factors — and +0.203 versus the transports ETF [[IYT]], separable as a clean cluster across thresholds 0.30–0.45 (stable width 0.15). [[IYT]] is the nearest ETF and absorbs the cohort at the looser 0.50 cut only because IYT is itself truck/parcel-heavy; the pure-trucker basket is tighter and separates below 0.45. This is the fourth genuinely distinct freight/oligopoly factor in the campaign alongside [[Railroads]], [[Solid waste]], and [[Tobacco majors basket|tobacco]] — though, unlike waste (whose ETF is far away), trucking's ETF is a close proxy.

The freight-cycle pure-play. Truckers — both truckload (the spot/contract rate cycle) and LTL (industrial shipment density and pricing) — all rise and fall on the same North American freight cycle, which makes them one of the tightest cohorts in the campaign. That freight cycle is also most of what the transports ETF [[IYT]] holds, so IYT is the nearest proxy; but the pure-trucker basket is tighter than the diluted ETF (which also carries rails, airlines, and parcel), and it separates cleanly at tighter thresholds. Rails run on a distinct volume/pricing dynamic and separate further — two freight factors, both distinct from the transports blend.

## Sector performance

![[trucking-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[IYT]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is six truckload and LTL carriers — [[Old Dominion Freight Line|ODFL]], [[Saia|SAIA]], [[XPO]], [[Knight-Swift|KNX]], [[Werner Enterprises|WERN]], [[ArcBest|ARCB]] — tested against the rails ([[Union Pacific|UNP]]/[[CSX]]), the transports ETF (IYT), industrials (XLI), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.742 [0.571–0.853] | well above the floor; weekly 0.742 — the tightest of the four fresh cohorts |
| PC1 explained variance | 78.6% | a strong single factor (weekly 78.8%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | real cohesion well beyond a random 6-pick |
| Vol-matched null p | 0.0001 / 0.0001 | cohesion exceeds vol-matched baskets — a real factor |
| Holdout (2Y split) | STRENGTHENING 1.11 | train 0.668 → test 0.742 — tightening, durable |
| Threshold stable width | 0.15 [0.30–0.45] | a clean, separable cluster below the IYT-contamination cut |
| Intra-adv vs rails (UNP/CSX) | +0.280 | distinct from rail — two freight factors |
| Intra-adv vs ETFs (IYT/XLI/SPY) | +0.203 | distinct from the transports blend; IYT is the nearest proxy |

All US-listed. Config: `scripts/cluster_configs/odfl.yaml`; registry row 2026-06-20.

### Boundary — truckers separate from IYT below 0.45; rails apart throughout

![[trucking-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. At this cut the truckers absorb the transports ETF [[IYT]] (and XLI/SPY), because IYT is itself truck/parcel-heavy — but the threshold scan shows the six truckers form a clean cluster WITHOUT IYT across 0.30–0.45 (stable width 0.15). The rails [[Union Pacific|UNP]]/[[CSX]] form their own separate cluster throughout: trucking and rail are two distinct freight factors.*

The threshold scan returns the cohort as a clean, contamination-free cluster across [0.30–0.45] (stable width 0.15, wider than railroads' 0.10) — IYT joins only at the looser 0.50 cut. Combined with the +0.203 intra-advantage over the ETFs and the +0.280 over rails, this is a VALIDATED, distinct factor: tighter than the transports ETF that mostly contains it. The one caveat versus [[Solid waste|waste]] (whose ETF EVX is far away, +0.424) is that IYT is a close proxy here (+0.203) — so trucking is distinct but cheaply approximated by IYT, whereas the waste factor has no ETF substitute.

### Topology — an LTL core and a truckload pair, all very tight

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | ODFL + SAIA | 0.147 | the tightest LTL pair |
| 2 | ARCB + (ODFL+SAIA) | 0.215 | the LTL core builds |
| 3 | KNX + WERN | 0.221 | the truckload pair forms |
| 4 | XPO + LTL core | 0.240 | XPO joins the LTL side |
| 5 | (KNX+WERN) + rest | 0.294 | truckload joins LTL — the cohort closes very tight |

Every join is below 0.30 — an unusually tight cohort, closing at 0.294. There is a mild internal split between the LTL names (ODFL/SAIA/XPO/ARCB) and the truckload pair (KNX/WERN), but they merge well below the cut. PC1 explains 78.6%, the highest of the four fresh cohorts.

### PC1 index weights

![[trucking-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 78.6% (weekly 78.8%) — a dominant freight-cycle factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| ODFL | 0.422 | 17.2% | 40.3% | 19.0% |
| SAIA | 0.424 | 17.3% | 49.1% | 15.7% |
| XPO | 0.391 | 16.0% | 45.7% | 15.5% |
| KNX | 0.407 | 16.6% | 41.4% | 17.8% |
| WERN | 0.389 | 15.9% | 41.9% | 16.9% |
| ARCB | 0.415 | 17.0% | 49.5% | 15.2% |

Near-uniform loadings (~0.39–0.42) — a clean single freight factor; the lower-vol [[Old Dominion Freight Line|ODFL]]/[[Knight-Swift|KNX]] carry the highest inverse-vol weights.

### Distinctness — distinct from rail and from the transports blend

![[trucking-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A uniformly hot trucker block; IYT is warm against the truckers (it largely holds them) but the truckers are warmer against each other, while UNP/CSX are cooler (distinct freight mode).*

The two intra-advantage numbers: +0.280 versus the rails (trucking is a distinct freight factor from rail) and +0.203 versus the ETFs. The +0.203 is the same margin railroads carry over IYT — both freight modes are distinct sub-factors inside the transports blend. The asymmetry is in the ETF's composition: IYT is truck/parcel-heavy, so it overlaps the truckers far more than the rails (which is why IYT joins the truckers at 0.50 but never the rails). The practical read: the trucker basket is a tighter, distinct factor, but IYT approximates it cheaply — unlike [[Railroads|rail]] or [[Solid waste|waste]], where the basket is the only clean expression.

### Historical tightness evolution

![[trucking-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Durably tight (0.58–0.75), tightening into freight-cycle stress; currently near its highs.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.586 | 65.5% |
| 2022 | 0.734 | 77.9% |
| 2023 | 0.754 | 79.6% |
| 2024 | 0.578 | 65.0% |
| 2025 | 0.685 | 74.2% |
| 2026 | 0.730 | 77.6% |

Latest 90-day reading: intra 0.780, PC1 81.7%. The freight factor is durable and currently strengthening (holdout 1.11, intra near six-year highs). Trucking and [[Railroads|rail]] are two separable freight factors; both are distinct from the broad transports ETF, but trucking's ETF (IYT) is a much closer proxy than rail's, because IYT is built mostly out of truckers and parcel.

## Related

- [[Railroads]] — the sibling freight cohort; distinct from trucking (+0.280), and (unlike trucking) far from IYT
- [[Solid waste]], [[Tobacco majors basket]] — other distinct oligopoly factors in the campaign
- [[Old Dominion Freight Line]], [[Saia]], [[XPO]], [[ArcBest]] — the LTL names
- [[Knight-Swift]], [[Werner Enterprises]] — the truckload pair
- [[IYT]] — the transports ETF (the nearest proxy)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/odfl.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
