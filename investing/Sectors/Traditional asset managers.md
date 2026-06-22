---
aliases: [Traditional asset managers, Asset managers, Long-only asset managers, Traditional asset manager cluster]
tags: [sector, financials, asset-management, cluster-validation]
---

# Traditional asset managers

> [!warning] Cluster status: real cohesion but NOT a distinct factor — traditional asset managers are levered market/financials beta (= XLF/SPY), not separable from alt managers (Jun 2026)
> The listed traditional asset managers ([[BlackRock|BLK]]/[[T. Rowe Price|TROW]]/[[Franklin Templeton|BEN]]/[[Invesco|IVZ]]/[[Affiliated Managers Group|AMG]]) cohere moderately — intra-corr 0.596, PC1 68% — but it is pure market beta, not a distinct factor. The two decisive numbers are ~zero distinctness margins: a +0.011 intra-advantage versus [[XLF]]/SPY (they correlate with the market essentially as much as with each other) and a NEGATIVE −0.007 versus the alt managers ([[Blackstone|BX]]/[[KKR]]). At the 0.50 cut the whole financial complex fuses — the traditional managers, the alts, [[XLF]], and SPY all in one cluster, with only [[Affiliated Managers Group|AMG]] (the multi-boutique outlier) a singleton. And the weekly intra-corr (0.409) collapses well below the daily (0.596), the signature of same-day market beta rather than a shared idiosyncratic driver. Asset managers are AUM-fee businesses whose stocks are levered plays on the equity market — own [[XLF]] (or SPY with beta); there is no separable asset-manager factor.

The levered-beta sector. An asset manager's revenue is a fee on assets under management, and AUM rises and falls with the market — so these stocks are high-beta proxies for equities, amplified by flows (and, for the active managers, the secular bleed to passive). That makes them cohere, but the cohesion IS market beta: they track [[XLF]] and SPY as much as each other, and they don't separate from the alternative managers. There is no distinct "traditional asset manager" factor to own beyond financial-market beta.

## Sector performance

![[tradam-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[XLF]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is five listed traditional asset managers — [[BlackRock|BLK]], [[T. Rowe Price|TROW]], [[Franklin Templeton|BEN]], [[Invesco|IVZ]], [[Affiliated Managers Group|AMG]] — tested against the alternative managers ([[Blackstone|BX]]/[[KKR]]), financials (XLF), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.596 [0.459–0.720] | above the floor; weekly 0.409 (much LOWER — daily market beta) |
| PC1 explained variance | 68.0% | one factor — but it is the market (weekly PC1 only 53.6%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0002 | beats a random 5-pick — via shared financials/market beta |
| Vol-matched null p | 0.0001 / 0.0001 | beats vol-matched baskets too |
| Holdout (2Y split) | WEAKENED 0.71 | train 0.841 → test 0.597 (eroding) |
| Threshold stable width | 0.00 (none) | never isolates — XLF/SPY/alts contaminate at every cut |
| Intra-adv vs alt managers (BX/KKR) | −0.007 | NEGATIVE — not distinct from the alts |
| Intra-adv vs ETFs (XLF/SPY) | +0.011 | ≈ zero — the cohort IS market/financials beta |

All US-listed. Config: `scripts/cluster_configs/blk.yaml`; registry row 2026-06-20.

### Boundary — the whole financial complex fuses; AMG the lone singleton

![[tradam-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The traditional managers ([[BlackRock|BLK]]/[[T. Rowe Price|TROW]]/[[Franklin Templeton|BEN]]/[[Invesco|IVZ]]) cluster with the alt managers ([[Blackstone|BX]]/[[KKR]]), [[XLF]], and SPY — the entire financial-market-beta complex fuses. Only [[Affiliated Managers Group|AMG]] (the multi-boutique holding company) is a singleton. There is no traditional-asset-manager cluster distinct from the market.*

The ~zero intra-advantage over the ETFs (+0.011) and the negative advantage over the alts (−0.007) are the decisive falsifiers of distinctness: the asset managers are no more correlated with each other than with XLF/SPY or with BX/KKR. The threshold scan never isolates them (zero stable width). The cohort beats the random/vol-matched nulls only because it is shared market/financials beta — which SPY and XLF already are.

### Topology — a market-beta core, AMG apart

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | BLK + IVZ | 0.280 | the largest passive/active managers |
| 2 | BEN + (BLK+IVZ) | 0.343 | Franklin joins |
| 3 | TROW + core | 0.371 | T. Rowe joins |
| 4 | AMG + core | 0.489 | the multi-boutique outlier joins, just under the cut |

The four core names close at 0.371 — but that is market beta, and [[XLF]]/SPY join at the same range (which is why they sit inside the cluster). [[Affiliated Managers Group|AMG]] is the loosest (0.489), its multi-boutique/minority-stake structure setting it apart.

### PC1 index weights

![[tradam-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 68.0% daily but only 53.6% weekly — the daily figure is inflated by same-day market beta.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| BLK | 0.459 | 20.6% | 28.0% | 21.4% |
| TROW | 0.442 | 19.8% | 23.9% | 24.1% |
| BEN | 0.454 | 20.3% | 28.7% | 20.6% |
| IVZ | 0.484 | 21.7% | 33.8% | 18.7% |
| AMG | 0.392 | 17.6% | 33.5% | 15.2% |

Loadings are fairly even (the names share market beta); [[Affiliated Managers Group|AMG]] loads lowest, consistent with being the singleton.

### Distinctness — ≈ zero; the cohort is the market

![[tradam-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The asset managers, the alts, XLF, and SPY are all about equally warm — no asset-manager block distinct from the market.*

The +0.011 intra-advantage over the ETFs is the lowest distinctness margin in the campaign — effectively zero. The asset managers correlate with [[XLF]]/SPY as much as with one another, so there is no separable factor; they are levered market beta. And they are not distinct from the alternative managers (−0.007) — asset management is one market-beta complex. Own [[XLF]] (or SPY) for the exposure.

### Historical tightness evolution

![[tradam-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Tight in risk-off/rate windows (0.77–0.81), looser otherwise; 0.57 in 2026.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.727 | 78.2% |
| 2022 | 0.768 | 81.4% |
| 2023 | 0.768 | 81.5% |
| 2024 | 0.669 | 73.9% |
| 2025 | 0.813 | 85.1% |
| 2026 | 0.567 | 66.0% |

Latest 90-day reading: intra 0.593, PC1 68.2%. Cohesion rises in market-stress windows (when everything financial sells off together on rates/risk) and falls otherwise — the pattern of a beta complex, not a distinct factor. The holdout is WEAKENED. Like the [[Mega banks basket|mega banks]] and [[Reinsurers and specialty P&C|reinsurers]], asset managers are an ETF-replicable financial pole — here the ETF is essentially the market itself.

## Related

- [[Mega banks basket]], [[Regional banks]], [[Reinsurers and specialty P&C]] — the other ETF-replicable financial poles
- [[BlackRock]], [[T. Rowe Price]], [[Franklin Templeton]], [[Invesco]] — the traditional managers
- [[Affiliated Managers Group]] — the multi-boutique singleton
- [[Blackstone]], [[KKR]] — the alt managers the cohort isn't distinct from
- [[XLF]] — the financials ETF the cohort resolves to
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/blk.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
