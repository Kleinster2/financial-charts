---
aliases: [Ad-tech, Adtech, Ad technology, Programmatic ad-tech, Independent ad-tech]
tags: [concept, ad-tech, advertising, software, cluster-validation]
---

# Ad-tech

The listed independent programmatic-advertising names — the ad-tech companies outside the [[Google]]/[[Meta]] walled gardens: [[Trade Desk]] (TTD, the demand-side platform), [[AppLovin]] (APP, app monetization + the AXON AI ad engine), [[PubMatic]] (PUBM) and [[Magnite]] (MGNI, the supply-side platforms), and [[DoubleVerify]] (DV, ad verification / measurement). The validation falsifies "ad-tech" as a single factor: the label spans four different businesses that have decoupled.

> [!failure] Cluster status: falsified — a label spanning four businesses, not a factor (June 2026)
> The five ad-tech names do not trade as one cohort. Intra-corr is 0.374 daily / 0.507 weekly, PC1 only 50.8% (variance spread across PC2–PC4). The random-basket null is NOT rejected (p 0.051) and the vol-matched null fails too (0.069) — the cohesion is indistinguishable from a random pick of comparable high-beta names, explained by shared digital-ad / growth beta rather than a distinct ad-tech factor. The names shatter: at every threshold up to 0.45 they are five singletons, and they split by sub-business — a supply-side (SSP) pair [[PubMatic]]+[[Magnite]] (join 0.496, the one real micro-cohort), a loose demand/measurement pair [[Trade Desk]]+[[DoubleVerify]], and [[AppLovin]] a decoupled singleton (joins only at 0.757). Holdout REGIME-DEPENDENT (0.59), and the cohort fragmented over time as APP's AI ad engine pulled it away: intra 0.63 (2022) → 0.32 (2024) → 0.44 (2026). The "ad-tech" sector is a value-chain — DSP, SSP, measurement, app-monetization — not a factor. See below.

The decoupling is the story. Through 2022 the ad-tech names traded as a moderately tight group (intra 0.63) on a shared digital-ad-cycle factor. Then [[AppLovin]]'s AXON engine re-rated it from "ad-tech" into an AI-driven app-monetization mega-cap, [[Trade Desk]] hit a 2025 slowdown, and the supply-side names (PUBM/MGNI) and measurement (DV) went their own ways. By 2024 the cohesion had collapsed to 0.32. Each name now trades on its own dominant driver — the same dynamic that falsified [[GLP-1 receptor agonists|GLP-1]] and [[Medtech]] — leaving only the structural SSP pair underneath.

## Cluster validation

> [!warning] Not async — small-cap reaction-timing noise
> `cluster_analysis.py` auto-flagged "asynchronous closes" because the weekly intra-corr (0.507) exceeds the daily (0.374) by >0.10. But all five names are US-listed, so this is not async — it is small-cap staggered-reaction noise (these names report and react to ad-cycle news on different days; weekly bars recapture co-movement the daily bars miss). The weekly 0.507 is the better cohesion estimate, but even on the weekly basis the cohort is loose, and on the daily basis the framework uses, it fails the random-basket null.

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.374 daily / 0.507 weekly | Loose; weekly higher (small-cap noise, not async) |
| PC1 explained variance | 50.8% | Multi-factor (PC2 17.6%, PC3 13.4%) |
| Independence null p | 0.0001 | Series co-move a little |
| Random-basket null p | 0.051 | NOT rejected — no better than a random 5-pick |
| Vol-matched null p | 0.069 | NOT rejected — cohesion is shared beta/vol |
| Holdout (2Y split) | REGIME-DEPENDENT 0.59 | Collapsed 0.49 → 0.29 as APP decoupled |
| Threshold clean width | 0.00 | Five singletons up to 0.45 |
| Intra-adv vs ad giants (META/GOOGL) | +0.199 | Moderately distinct from the walled gardens |
| Intra-adv vs growth (QQQ) | +0.091 | Barely distinct from growth |
| Intra-adv vs market (SPY) | +0.086 | Barely distinct from market |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed. Config: `scripts/cluster_configs/adtech.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — splits by sub-business

![[adtech-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The five names do not form one cluster: [[PubMatic]]+[[Magnite]] (the SSP pair) cluster, [[Trade Desk]]+[[DoubleVerify]] loosely group, and [[AppLovin]] sits alone. [[Meta]] is its own singleton; [[Google]] clusters with the market ETFs. Ad-tech is a value chain, not a factor.*

The threshold scan never returns a clean cohort — the names are five singletons up to 0.45, with the SSP pair forming first. This is the [[Medtech]] / [[Theatrical exhibition]] signature (a sector label, not a factor), driven here by the specific decoupling of [[AppLovin]] from the rest as it became an AI-ad-engine story.

### Topology — an SSP pair, a loose DSP/measurement pair, and a decoupled outlier

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | TTD + DV | 0.480 | Loose demand/measurement pair |
| 2 | PUBM + MGNI | 0.496 | The SSP pair — the one real micro-cohort |
| 3 | (TTD+DV) + (PUBM+MGNI) | 0.565 | The four loosely join — above the 0.5 cut |
| 4 | APP + rest | 0.757 | AppLovin joins last — essentially decoupled |

The only durable structure is the supply-side pair [[PubMatic]]+[[Magnite]] (both SSPs, same business). [[AppLovin]] is the outlier (lowest PC1 loading 0.302, joins at 0.757) — it has left the ad-tech factor for an AI-app-monetization one. The DSP ([[Trade Desk]]) and measurement ([[DoubleVerify]]) names sit loosely between.

### PC1 index weights

![[adtech-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains only 50.8% with a long tail — multi-factor. [[AppLovin]] carries the lowest loading (0.302) despite the highest vol (74%), the decoupled-outlier signature.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Trade Desk (TTD) | 0.450 | 20.4% | 54.6% | 21.4% |
| AppLovin (APP) | 0.302 | 13.7% | 73.5% | 10.7% |
| PubMatic (PUBM) | 0.465 | 21.1% | 65.5% | 18.4% |
| DoubleVerify (DV) | 0.499 | 22.6% | 46.8% | 27.6% |
| Magnite (MGNI) | 0.491 | 22.2% | 57.9% | 22.0% |

[[AppLovin]] takes the smallest raw PC1-mimic weight (10.7%) — the factor barely loads on it, confirming it is no longer part of the ad-tech trade.

### Distinctness

![[adtech-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The only warm cell is [[PubMatic]]–[[Magnite]] (the SSPs). [[AppLovin]] is cool against everything. The cohort is barely distinct from growth/market (+0.09) — what little it co-moves on is digital-ad / growth beta.*

The cohort is only moderately distinct from the ad giants (+0.199 vs [[Meta]]/[[Google]]) and barely from growth/market (+0.09) — there is no strong ad-tech-specific factor, just shared high-beta-software exposure plus a real SSP pair.

### Historical tightness evolution

![[adtech-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2022–2026. A fragmenting cohort: 0.63 in 2022, collapsing to 0.32 by 2024 as [[AppLovin]] decoupled, with only a partial recovery to 0.44. The opposite trajectory to the consolidating quantum/crypto cohorts.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2022 | 0.627 | 70.2% | 0.443 |
| 2023 | 0.517 | 62.0% | 0.592 |
| 2024 | 0.321 | 47.2% | 0.801 |
| 2026 | 0.443 | 56.3% | 0.660 |

*Fragmenting: the ad-tech factor was real in 2022 (0.63) but decohered as the names found different dominant drivers — the live, dated example of a sector losing its factor when its biggest name ([[AppLovin]]) changes what it is.*

### The read-through

- Ad-tech is not a trade. The five names fail the random-basket null and shatter into sub-businesses — owning an "ad-tech basket" buys four different businesses plus shared growth beta, not a theme.
- The one real structure is the SSP pair. [[PubMatic]]+[[Magnite]] (both supply-side platforms, 0.50) is the only durable micro-cohort — the same-business pair, the constructive residue of the falsification.
- AppLovin has left the sector. Lowest loading, joins at 0.757 — its AXON AI ad engine re-rated it into an app-monetization / AI factor; it is no longer part of the ad-tech trade despite the label.
- A sector can lose its factor. Ad-tech cohered at 0.63 in 2022 and decohered to 0.32 by 2024 — a dated, live case of the dominant-driver dynamic playing out in real time as the members diverged.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14).

## Related

- [[Digital Advertising]] — the broader ~$700B market (Google/Meta-dominated); this note is the independent-ad-tech cohort
- [[Trade Desk]], [[AppLovin]], [[PubMatic]], [[Magnite]], [[DoubleVerify]] — the cohort members
- [[CTV advertising]] — a key growth vector for TTD/PUBM/MGNI
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
