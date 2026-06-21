---
aliases: [Tier-1 auto suppliers, Auto suppliers, Auto parts suppliers, Auto component makers, Tier-1 suppliers, Auto supplier cohort]
tags: [sector, consumer-discretionary, automotive, auto-supplier, cluster-validation]
---

# Tier-1 auto suppliers

> [!warning] Cluster status: NOT a durable factor — real and modestly distinct from the OEMs, the auto ETF and the market, but FRAGILE (a single-point 0.50 band) and regime-dependent (Jun 2026)
> The six Tier-1 auto suppliers ([[Aptiv|APTV]]/[[BorgWarner|BWA]]/[[Lear|LEA]]/[[Magna|MGA]]/[[Autoliv|ALV]]/[[Visteon|VC]]) co-move for real — they reject the independence, random-basket and vol-matched nulls at the 0.0001 floor — and they form their own cluster at the 0.50 cut, cleanly separate from the automakers ([[General Motors|GM]]/[[Ford|F]]), the auto ETF ([[CARZ]]) and broad discretionary/market ([[XLY]]/[[SPY]]), with positive intra-advantages over all of them (+0.112 vs OEMs, +0.100 vs the auto ETF, +0.120 vs SPY). But the cohesion is loose (intra 0.572, weekly 0.525; PC1 64.7%) and the distinctness is FRAGILE: the threshold scan keeps the six intact only at the single point 0.50 (width 0.00), and at 0.55 the entire auto + market complex (GM/F/CARZ/XLY/SPY) merges in. The holdout WEAKENED to 0.73 with a near-zero PC1-loadings correlation (0.09) — the factor does not persist out-of-sample — and rolling cohesion swings hard with the cycle (0.83 in the 2022–23 supply-chain crunch, 0.51 now). A real, not-ETF-replicable auto-production factor that is too fragile and regime-dependent to own; the only durable sub-structure is the [[Lear|LEA]]+[[Autoliv|ALV]] content pair (0.78). See below.

The auto-production cohort that only coheres under stress. Tier-1 suppliers sell components into the OEMs' build schedules, so their shared driver is global vehicle-production volume and content-per-vehicle. That makes them a genuine, distinct-from-the-OEMs cohort when production is the binding constraint — most visibly in the 2021–23 chip-shortage era, when every supplier moved together on allocation and volume. But in normal times the cohort disperses, because the six are really three different stories: a volume/content core (seating [[Lear|LEA]], safety [[Autoliv|ALV]], diversified [[Magna|MGA]]), an EV/ADAS-content pair ([[Aptiv|APTV]] electrical/software, [[BorgWarner|BWA]] powertrain) whose secular transition diverges from volume, and cockpit electronics ([[Visteon|VC]]). The result is real co-movement with no durable factor — distinct on paper, fragile in practice.

## Cluster validation

The candidate cohort is six Tier-1 automotive suppliers — [[Aptiv|APTV]] (electrical/ADAS), [[BorgWarner|BWA]] (powertrain/EV), [[Lear|LEA]] (seating/electrical), [[Magna|MGA]] (diversified), [[Autoliv|ALV]] (safety), [[Visteon|VC]] (cockpit electronics) — tested against the automakers they supply ([[General Motors|GM]]/[[Ford|F]]), the auto ETF ([[CARZ]]) and broad discretionary ([[XLY]]), and the market (SPY). 1Y window through 2026-06-18 (198 obs), threshold 0.5. [[Magna|MGA]] is Canada-listed/synchronous; the weekly cross-check controls for any residual. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.572 [0.413–0.783] | Loose; weekly 0.525; LEA+ALV the only tight pair |
| PC1 explained variance | 64.7% | A moderate single factor (weekly 60.5%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0001 | More cohesive than a random 6-pick — real |
| Vol-matched null p (10k) | 0.0001 | Real beyond shared vol |
| Holdout (2Y split) | WEAKENED 0.73, loadings-corr 0.09 | train 0.781 → test 0.572; factor does NOT persist out-of-sample |
| Threshold stable width | 0.00 (point at 0.50) | FRAGILE — own cluster only at exactly 0.50; merges at 0.55 |
| Intra-adv vs automakers (GM/F) | +0.112 | Distinct from the OEM customers — two auto poles |
| Intra-adv vs auto ETF (CARZ/XLY) | +0.100 | Not ETF-replicable — CARZ is market beta (0.83 to SPY) |
| Intra-adv vs market (SPY) | +0.120 | A modest supplier-specific factor over the market |

Config: `scripts/cluster_configs/auto_suppliers.yaml`; registry row 2026-06-21.

### Boundary — own cluster, but only in a razor-thin window at 0.50

![[auto-suppliers-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. Three clean clusters below the cut: the automakers {[[General Motors|GM]]/[[Ford|F]]}, the market/ETF block {[[XLY]]/[[CARZ]]/[[SPY]]}, and the six suppliers (red). The suppliers are genuinely their own group — separate from both the OEMs and the auto ETF — but their cluster closes at 0.497 and the three groups merge just above (~0.53), so the separation is razor-thin.*

The threshold scan returns a single-point stable band — the six are a clean, uncontaminated cluster only at exactly 0.50:

| Threshold | State of the cohort | Read |
|---|---|---|
| 0.50 | the six suppliers alone | the only clean point (width 0.00) |
| 0.55 | + GM, F, CARZ, XLY, SPY | the whole auto + market complex merges |
| 0.60+ | (one complex) | everything together |

A width-0.00 band means the cohort's distinctness depends entirely on the threshold pick — it is real at 0.50 (the suppliers do separate from the OEMs and the ETF there) but it has no robustness margin. Contrast a true distinct factor like [[Franchised auto dealers]] (band [0.35–0.50], width 0.15) or even the marginal [[Net-lease REITs|net-lease REITs]] (width 0.05) — both keep daylight before the parent complex joins; the suppliers have none.

### Topology — a content core, an EV-transition fringe

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | LEA + ALV | 0.217 | the content/volume core — seating + safety (corr 0.78) |
| 2 | MGA + (LEA+ALV) | 0.362 | diversified Magna joins |
| 3 | VC + core | 0.382 | cockpit electronics joins |
| 4 | APTV + core | 0.463 | Aptiv (ADAS/software) joins late |
| 5 | BWA + core | 0.497 | BorgWarner (powertrain/EV) closes the cohort at the cut |

The cohort does not close until 0.497 — right at the threshold. [[Lear|LEA]]+[[Autoliv|ALV]] (0.78) are the durable core (volume/content names); the EV-transition names [[Aptiv|APTV]] (ADAS/software) and [[BorgWarner|BWA]] (powertrain) join last and are the loosest pair in the matrix (0.41), pulling the cohort apart. PC1 explains only 64.7%.

### PC1 index weights — an even but weak factor, content names anchor it

![[auto-suppliers-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 64.7% (a coherent factor runs ~75%+) with a meaningful PC2+PC3 (19%) carrying the content-vs-EV-transition split. Loadings are highest for the content/volume names (LEA 0.448, ALV 0.447) and lowest for the EV-transition pair (APTV 0.371, BWA 0.366).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| APTV | 0.371 | 15.21% | 41.60% | 12.96% |
| BWA | 0.366 | 14.99% | 40.59% | 13.10% |
| LEA | 0.448 | 18.36% | 32.82% | 19.83% |
| MGA | 0.405 | 16.59% | 36.47% | 16.13% |
| ALV | 0.447 | 18.31% | 28.38% | 22.88% |
| VC | 0.404 | 16.54% | 38.84% | 15.09% |

The content/volume names ([[Lear|LEA]], [[Autoliv|ALV]]) carry the highest loadings and (being lower-vol) the highest PC1-mimic weights; the EV-transition names ([[Aptiv|APTV]], [[BorgWarner|BWA]]) load lowest. The near-zero holdout PC1-loadings correlation (0.09) confirms this composition is not stable across regimes — which names anchor the factor shifts, so the cohort is not a durable structure (the [[Alcohol and spirits|alcohol]] −0.24 / [[Fertilizer producers|fertilizer]] −0.37 pattern, milder here).

### Distinctness — real and not an ETF, but fragile

![[auto-suppliers-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A warm-but-uneven supplier block (0.41–0.78): the LEA/ALV/MGA content corner is warmest; the APTV–BWA pair is the coolest cell (0.41). The automakers (GM/F) and the auto ETF/market (CARZ/XLY/SPY) are cooler against the block.*

The intra-advantage numbers are the unusual part: positive against every control — +0.112 vs the OEMs, +0.100 vs the auto ETF, +0.120 vs the market. Unlike the campaign's ETF-replicable cohorts (negative intra-advantage), the suppliers are genuinely distinct from the things you might use to proxy them: they separate from their own OEM customers (two auto poles), and the auto ETF [[CARZ]] does not capture them because CARZ runs as broad market/discretionary beta (0.83 correlation to SPY). So there is no liquid ETF that prices the Tier-1 supplier factor — which is the distinctness signature. What it lacks is robustness: the separable band is a single point (width 0.00) and the factor does not persist out-of-sample (holdout 0.73, loadings-corr 0.09). Distinct, but fragile — the separation is real only at one threshold and only in some regimes.

### Historical tightness evolution — the supply-chain-crunch factor

![[auto-suppliers-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Strongly regime-dependent — tight (0.81–0.83) through the 2022–23 chip-shortage/supply-chain crunch when production was the binding constraint, loose (0.51–0.62) in 2024 and 2026 as the EV-transition names diverged. Latest 90-day 0.527, near the cycle low.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.685 | 73.8% |
| 2022 | 0.809 | 84.1% |
| 2023 | 0.829 | 85.9% |
| 2024 | 0.615 | 68.0% |
| 2025 | 0.740 | 78.3% |
| 2026 | 0.509 | 59.8% |

*The cohort tightens when global auto production is supply-constrained (2022–23: every supplier rationed together) and disperses when it is not (2024, 2026: the EV-content winners separate from the volume names). A durable factor holds across regimes; this one is a function of the production cycle, which is why the holdout reads WEAKENED — the test window (2026) caught it near a cohesion trough.*

## Where this sits in the auto complex

This completes the campaign's auto map, and the four pieces fail and pass for different reasons:

- [[Automakers]] — FALSIFIED (the OEMs do not cohere as a clean factor).
- [[Franchised auto dealers]] — VALIDATED distinct (the 10th distinct factor; a homogeneous dealer-consolidator model with a wide band).
- [[Auto parts retail|Auto parts retail (ORLY+AZO)]] — a distinct pair (the premium aftermarket duopoly), not a full cohort.
- Tier-1 auto suppliers (this note) — real and distinct-leaning but FRAGILE (single-point band) and regime-dependent; not ownable.

The suppliers are the most "almost distinct" of the auto cohorts that did not make it: they clear cohesion and the not-an-ETF test, and fail only on band width and durability. The dealers earned distinctness with a homogeneous model and a wide separable band; the suppliers, split between a volume/content core and an EV-transition fringe, cohere cleanly only when the production cycle forces them together.

## Related

- [[Aptiv]], [[BorgWarner]], [[Lear]], [[Magna]], [[Autoliv]], [[Visteon]] — the Tier-1 supplier cohort members
- [[Automakers]] — the OEM customers (a separate, falsified auto pole); [[Franchised auto dealers]] — the distinct auto-retail factor
- [[CARZ]], [[XLY]] — the auto/discretionary ETFs the cohort is distinct from (no ETF prices the supplier factor)
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-21. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/auto_suppliers.yaml`; registry row 2026-06-21. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
