---
aliases: [Auto parts retail, Auto parts, Auto aftermarket, Aftermarket retail, Auto parts cluster]
tags: [sector, consumer, retail, auto-aftermarket, cluster-validation]
---

# Auto parts retail

> [!warning] Cluster status: PARTIAL — the label splits; the robust, ownable piece is the ORLY+AZO premium duopoly (strikingly non-retail), the rest a looser group (Jun 2026)
> The listed auto-parts names ([[O'Reilly Automotive|ORLY]]/[[AutoZone|AZO]]/[[Advance Auto Parts|AAP]]/[[Genuine Parts|GPC]]/[[LKQ Corporation|LKQ]]) do NOT trade as one factor — intra-corr 0.471 (below the 0.50 floor), and the threshold scan never returns the five as a clean cluster. They DO beat the random-basket and vol-matched nulls and carry a +0.157 intra-advantage versus the retail ETFs ([[XRT]]/[[XLY]]/SPY) — the aftermarket is distinct from broad retail, consistent with its counter-cyclical resilience (people repair older cars in downturns) — but the cohesion is concentrated in one sub-pair. The cohort splits into the premium DIY/DIFM duopoly [[O'Reilly Automotive|ORLY]]+[[AutoZone|AZO]] (sub-intra 0.762, threshold STABLE width 0.45 [0.25–0.70], and a striking +0.599 intra-advantage versus the retail ETFs) and a looser laggard group [[Advance Auto Parts|AAP]]/[[Genuine Parts|GPC]]/[[LKQ Corporation|LKQ]] that only merges with the leaders at 0.615. Own the ORLY+AZO pair for the distinct, robust aftermarket factor; the five-name basket dilutes it with three different stories.

The aftermarket-resilience story holds — but only for the premium duopoly. [[O'Reilly Automotive]] and [[AutoZone]] run the same high-quality DIY/DIFM model — dense store networks, commercial delivery, consistent mid-single-digit comps through cycles — and trade as a tight pair strikingly decoupled from broad retail. The other three are different businesses: [[Advance Auto Parts]] a multi-year turnaround, [[Genuine Parts]] a diversified industrial + NAPA distributor, [[LKQ Corporation]] an alternative/salvage-parts distributor with European exposure. So the "auto parts retail" label is really a robust duopoly plus three idiosyncratic names.

## Cluster validation

The candidate cohort is five listed auto-parts retail and distribution names — [[O'Reilly Automotive|ORLY]], [[AutoZone|AZO]], [[Advance Auto Parts|AAP]], [[Genuine Parts|GPC]], [[LKQ Corporation|LKQ]] — tested against the retail ETF [[XRT]], consumer discretionary (XLY), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.471 [0.264–0.762] | below the 0.50 floor; weekly 0.433 — a duopoly plus loose names |
| PC1 explained variance | 57.8% | with a large PC2 (20.1%) — the ORLY/AZO-vs-laggards axis |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0006 | real cohesion beyond a random 5-pick |
| Vol-matched null p | 0.0004 / 0.0005 | cohesion exceeds vol-matched baskets |
| Holdout (2Y split) | STRENGTHENING 1.16 | train 0.386 → test 0.447, but loadings corr 0.39 (structure shifted) |
| Threshold stable width | 0.00 (none) | the five never form a clean cluster |
| Intra-adv vs ETFs (XRT/XLY/SPY) | +0.157 | distinct from broad retail (the aftermarket-resilience signal) |

All US-listed. Config: `scripts/cluster_configs/orly.yaml`; sub-cohort `scripts/cluster_configs/sub_autoparts.yaml`; registry row 2026-06-20.

### Boundary — a premium duopoly, a laggard trio, and the ETFs all apart

![[autoparts-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Three separate clusters: the premium duopoly [[O'Reilly Automotive|ORLY]]+[[AutoZone|AZO]]; the laggard group [[Advance Auto Parts|AAP]]/[[Genuine Parts|GPC]]/[[LKQ Corporation|LKQ]]; and the retail ETFs [[XRT]]/[[XLY]]/SPY on their own. The aftermarket names are distinct from retail (the ETFs are a separate cluster), but they are not one auto-parts cluster — the label spans two different aftermarket stories.*

The threshold scan never returns the five as a clean cluster (zero stable width) — they split into the duopoly and the laggards, which only merge at 0.615 (above the cut). So the five-name cohort is PARTIAL: real cohesion and distinct from retail, but pair-concentrated. The decisive structure is in the sub-cohort, not the full basket.

### Topology — the ORLY+AZO pair is the core; the laggards a looser trio

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | ORLY + AZO | 0.238 | the premium DIY/DIFM duopoly — the tight core |
| 2 | GPC + LKQ | 0.396 | the distribution names pair up |
| 3 | AAP + (GPC+LKQ) | 0.482 | the turnaround joins the laggard group |
| 4 | (ORLY+AZO) + laggards | 0.615 | the two sub-groups merge only above the cut |

The cohort closes at 0.615 — above the 0.5 threshold — confirming it is not one cluster. PC1 (57.8%) is the shared aftermarket factor; the large PC2 (20.1%) is precisely the ORLY/AZO-vs-laggards split.

### PC1 index weights

![[autoparts-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 57.8% (weekly 55.1%) with a large PC2 (20.1%) — a two-axis cohort, not a single clean factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| ORLY | 0.467 | 20.9% | 23.5% | 27.8% |
| AZO | 0.443 | 19.9% | 28.7% | 21.7% |
| AAP | 0.452 | 20.2% | 52.2% | 12.1% |
| GPC | 0.465 | 20.8% | 31.0% | 21.1% |
| LKQ | 0.407 | 18.2% | 32.9% | 17.3% |

Loadings are fairly even, but the lower-vol leaders ([[O'Reilly Automotive|ORLY]]/[[AutoZone|AZO]]) carry the highest inverse-vol weights, while the high-vol [[Advance Auto Parts|AAP]] (52% vol, the turnaround) carries the least.

### Sub-structure — the ORLY+AZO duopoly is robust and strikingly non-retail

Sub-cohort robustness check (`scripts/cluster_configs/sub_autoparts.yaml`):

| Sub-cohort | Members | Internal intra | vs laggards | vs ETF | Threshold width | Verdict |
|---|---|---|---|---|---|---|
| Premium DIY/DIFM | ORLY/AZO | 0.762 | +0.377 | +0.599 | 0.45 [0.25–0.70] | ROBUST — distinct duopoly, far from retail |

The ORLY+AZO pair is one of the most robust, ETF-distinct sub-structures in the campaign: a +0.599 intra-advantage versus the retail ETFs (the names are far more correlated with each other than with [[XRT]]/[[XLY]]) and a stable threshold band 0.45 wide — the widest in the sub-cohort sweep. This is the real auto-aftermarket factor: a high-quality duopoly that trades as its own thing, decoupled from cyclical retail. The laggards ([[Advance Auto Parts|AAP]]/[[Genuine Parts|GPC]]/[[LKQ Corporation|LKQ]]) are +0.377 looser — a separate, more idiosyncratic group.

### Distinctness — distinct from retail; concentrated in the duopoly

![[autoparts-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A hot ORLY/AZO corner; the laggards warmer among themselves than with the leaders; XRT/XLY/SPY cool against all of them.*

The full cohort's +0.157 intra-advantage versus the ETFs says the aftermarket is distinct from broad retail — but the sub-cohort's +0.599 shows that distinctness is concentrated in the ORLY+AZO duopoly. The investable read: the premium aftermarket pair is a genuinely distinct, robust factor (own ORLY+AZO); the broader five-name basket dilutes it with [[Advance Auto Parts|AAP]]'s turnaround, [[Genuine Parts|GPC]]'s industrial mix, and [[LKQ Corporation|LKQ]]'s salvage/Europe exposure.

### Historical tightness evolution

![[autoparts-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Tight in 2020 (~0.77, COVID move), decohering to ~0.39–0.48 since as the leaders pulled away from the laggards.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.766 | 81.4% |
| 2021 | 0.610 | 68.9% |
| 2022 | 0.647 | 72.2% |
| 2023 | 0.488 | 60.2% |
| 2024 | 0.387 | 52.8% |
| 2025 | 0.400 | 52.9% |
| 2026 | 0.483 | 58.9% |

Latest 90-day reading: intra 0.513, PC1 61.1%. The five-name cohort was tight in 2020 (everything moved on the pandemic) and has decohered since to ~0.40–0.51 as the premium leaders ([[O'Reilly Automotive|ORLY]]/[[AutoZone|AZO]]) diverged from the laggards ([[Advance Auto Parts|AAP]]'s collapse and recovery, [[Genuine Parts|GPC]]/[[LKQ Corporation|LKQ]]'s industrial/salvage struggles). The durable, ownable factor is the duopoly, not the label.

## Related

- [[O'Reilly Automotive]], [[AutoZone]] — the robust premium DIY/DIFM duopoly (the real factor)
- [[Advance Auto Parts]], [[Genuine Parts]], [[LKQ Corporation]] — the looser laggard group
- [[Solid waste]], [[Railroads]] — distinct oligopoly factors (waste/rail); the auto duopoly is the pair-level analogue
- [[XRT]], [[XLY]] — the retail ETFs the aftermarket is distinct from
- [[Franchised auto dealers]] — the new-vehicle-retail leg of the auto complex (a full distinct cohort, +0.207 vs the retail ETFs); the aftermarket here is distinct only as the ORLY+AZO pair
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/orly.yaml`; sub-cohort `scripts/cluster_configs/sub_autoparts.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
