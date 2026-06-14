---
aliases: [Airlines, US airlines, Airline stocks, Passenger airlines]
tags: [concept, airlines, transport, cyclical, cluster-validation]
---

# Airlines

The big US passenger airlines — [[Delta Air Lines]] (DAL), [[United Airlines]] (UAL), [[American Airlines]] (AAL), [[Southwest Airlines]] (LUV) and [[Alaska Air Group]] (ALK). A classic cyclical driven by two exogenous variables — jet-fuel cost and travel demand — overlaid with capacity discipline. The validation confirms a single tight factor: the legacy network carriers and the low-cost carriers trade together, and the cohort's defining signature is a strong inverse correlation to oil.

> [!success] Cluster status: validated — one cyclical factor, no business-model split (June 2026)
> The five airlines trade as one tight, durable factor: intra-corr 0.763 (weekly 0.781), PC1 81.1%, rejecting the independence, random-basket and vol-matched nulls all at the 0.0001 floor, with all five joining a tight tree ([[Delta Air Lines|DAL]]+[[United Airlines|UAL]] at 0.11 → [[American Airlines|AAL]] 0.17 → [[Alaska Air Group|ALK]] 0.24 → [[Southwest Airlines|LUV]] 0.30). Holdout STRENGTHENING (1.10) with PC1 loadings correlation 0.97 — near-perfect factor persistence. The built-in split test resolves cleanly: there is NO legacy-vs-low-cost split — the low-cost names (LUV, ALK) sit inside the cluster with the legacy carriers, near-identical PC1 loadings (0.42–0.47, no outlier). Business model is second-order. The cohort's defining feature is a strong INVERSE correlation to oil (−0.494 vs USO — the widest control relationship in the vault's cluster set): jet fuel is the dominant cost and exogenous driver. It is distinct from the broad market (+0.213 vs SPY) but only weakly from broad transports (+0.079 vs IYT — airlines ARE most of the transports ETF, which joins the cohort at threshold 0.35). See below.

Airlines are the clean counterexample to the value-chain-split law. Housing splits into construction vs transaction; AI power into equipment vs generation; ad-tech shatters into DSP/SSP/measurement. Airlines do not split, despite legacy and low-cost being genuinely different business models — because the model difference does not change the dominant driver. Every airline, legacy or low-cost, lives on the same jet-fuel cost and travel-demand cycle. The split law's real predicate is not "different business models" but "different dominant drivers": same models can split when drivers diverge (ad-tech), different models stay bound when the driver is shared (airlines).

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.763 | Tight; weekly 0.781 (all US-listed) |
| PC1 explained variance | 81.1% | Strong single factor |
| Independence null p | 0.0001 | Series co-move |
| Random-basket null p | 0.0001 | Beats a random 5-pick at the floor |
| Vol-matched null p | 0.0001 | Real beyond shared vol |
| Holdout (2Y split) | STRENGTHENING 1.10 | Loadings corr 0.97 — near-perfect persistence |
| Threshold clean width | 0.00 (point at 0.30) | FRAGILE — IYT joins at 0.35 (airlines are most of IYT) |
| Intra-adv vs oil (USO) | +1.257 | Inverse to oil (−0.494) — fuel is the driver |
| Intra-adv vs market (SPY) | +0.213 | Distinct from the broad market |
| Intra-adv vs transports (IYT) | +0.079 | Weak — a tight sub-cluster of transports |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed (synchronous). Config: `scripts/cluster_configs/airlines.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — one airline factor, inside transports

![[airlines-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The five airlines form one tight cluster with the transports ETF (IYT) and the market (SPY). Oil (USO) sits in a separate cluster — negatively correlated. There is no legacy/low-cost sub-split; the five names are one block.*

The threshold scan is FRAGILE: the cohort is intact and clean only at threshold 0.30, and IYT joins at 0.35 — airlines are the dominant component of broad transports, so the two are hard to separate. This is the same "validated sector cohort that is its own ETF" signature as [[Homebuilders]] (which merges with ITB). The airline factor is real and tight; its nearest neighbor is the transport sector it largely constitutes.

### Topology — a homogeneous five-name block, no split

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | DAL + UAL | 0.111 | Tightest pair (corr 0.89) — the big legacy carriers |
| 2 | AAL + (DAL+UAL) | 0.174 | American joins the legacy core |
| 3 | ALK + core | 0.241 | Alaska (low-cost-leaning) joins inside |
| 4 | LUV + rest | 0.297 | Southwest (low-cost) joins — still tight |

The low-cost carriers ([[Southwest Airlines]], [[Alaska Air Group]]) join the legacy core ([[Delta Air Lines]]/[[United Airlines]]/[[American Airlines]]) below distance 0.30 — there is no legacy/LCC sub-cluster. The differences in business model (network hub-and-spoke vs point-to-point, cost structure) are second-order to the shared fuel/demand cycle.

### PC1 index weights

![[airlines-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 81.1% with near-identical loadings (0.42–0.47) — a clean single factor with no dominant or peripheral name.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Delta (DAL) | 0.465 | 20.8% | 41.5% | 23.8% |
| United (UAL) | 0.463 | 20.7% | 50.0% | 19.7% |
| American (AAL) | 0.449 | 20.1% | 48.0% | 19.8% |
| Southwest (LUV) | 0.418 | 18.7% | 46.1% | 19.2% |
| Alaska (ALK) | 0.439 | 19.7% | 53.5% | 17.4% |

The loadings are almost identical — the five airlines are interchangeable expressions of one cyclical factor. The lower-vol [[Delta Air Lines]] takes the largest raw PC1-mimic weight; otherwise the basket is close to equal-weighted.

### Distinctness — inverse to oil

![[airlines-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The airline block is uniformly hot (0.66–0.89) and warm against IYT (transports). It is strikingly COOL — negative — against oil (USO), the cohort's defining signature.*

The −0.494 correlation to oil (USO) is the widest control relationship in the vault's cluster set, and it is negative: airlines rise when fuel falls and vice versa. This inverse-fuel exposure, plus the shared demand cycle, is the single factor binding the group — distinct from the market (+0.213) and only weakly from transports (+0.079, because airlines dominate IYT).

### Historical tightness evolution

![[airlines-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Cyclically tight: extreme in the 2020–22 COVID-shock and recovery (0.85–0.91, everything moved together), easing to 0.57 in 2024 as carriers diverged on idiosyncratic issues, then re-tightening to 0.74–0.86. A durable cyclical factor.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2022 | 0.907 | 92.5% | 0.128 |
| 2023 | 0.788 | 83.1% | 0.250 |
| 2024 | 0.574 | 66.7% | 0.550 |
| 2026 | 0.739 | 79.4% | 0.364 |

*Durable but cyclical: tightest in shared shocks (COVID 2020–22), loosening when carriers face idiosyncratic problems (2024) and re-tightening since. The factor is structural — the shared fuel/demand driver always reasserts.*

### The read-through

- One airline factor, five interchangeable names. The cohort is tight (0.763, all nulls at the floor) with near-equal loadings — there is no stock-picking factor edge, and no legacy/low-cost split to trade.
- The driver is fuel and demand, not business model. The −0.494 inverse-oil correlation is the defining signature; legacy and low-cost carriers stay bound because they share the dominant driver despite different models — the value-chain-split law's clean counterexample.
- It is a tight sub-cluster of transports. +0.079 vs IYT — airlines are the dominant component of broad transports; own the airlines via the names or the sector, but the factor largely IS transports-cyclical with an inverse-fuel tilt.
- Cyclical, not structural-stable. Tightest in shared shocks (COVID 0.91), loosest when carriers diverge idiosyncratically (2024, 0.57) — the cohesion is regime-dependent on whether a common shock dominates.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14).

## Related

- [[Transport]] — the broad transport sector (airlines are its dominant cyclical component)
- [[Delta Air Lines]], [[United Airlines]], [[American Airlines]], [[Southwest Airlines]], [[Alaska Air Group]] — the cohort members
- [[Crack spread]] — jet-fuel cost dynamics (the inverse driver)
- [[Travel]] — demand-side context
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
