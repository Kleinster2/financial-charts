---
aliases: [Self-storage REITs, Self-storage, Storage REITs, Self storage REITs, Self-storage cohort]
tags: [sector, real-estate, reit, self-storage, cluster-validation]
---

# Self-storage REITs

> [!warning] Cluster status: the four-name cohort is ETF-replicable (= VNQ), but the PSA/EXR/CUBE big-three is a distinct, durable sub-factor — NSA is the drag (Jun 2026)
> The public self-storage REITs ([[Public Storage|PSA]]/[[Extra Space Storage|EXR]]/[[CubeSmart|CUBE]]/[[National Storage Affiliates|NSA]]) cohere — intra-corr 0.710, PC1 79.0%, rejecting the independence, random-basket and vol-matched nulls (0.0001/0.0002/0.0001) — but they are not a distinct factor. The decisive numbers: only a +0.069 intra-advantage versus the broad REIT ETF [[VNQ]]/[[XLRE]] (which contaminate the cohort from threshold 0.35) and zero clean threshold width. They ARE distinct from the residential REITs (+0.275 versus [[Residential REITs|AVB/EQR]] — storage and apartments are different single-asset factors), but they correlate with broad REITs almost as much as with each other, so the basket adds nothing over [[VNQ]]. The internal structure is a tight big-three ([[Public Storage|PSA]]/[[Extra Space Storage|EXR]]/[[CubeSmart|CUBE]], ~0.87, closing at 0.143) plus [[National Storage Affiliates|NSA]] as a looser satellite (~0.55, joining only at 0.450). Holdout WEAKENED (0.80): tight 2021-25 (0.76-0.88) then loosening sharply in 2026 (0.66). But a dedicated three-name check flips the read for the core — drop the [[National Storage Affiliates|NSA]] satellite and the [[Public Storage|PSA]]/[[Extra Space Storage|EXR]]/[[CubeSmart|CUBE]] big-three ARE a distinct, durable sub-factor (intra 0.869, +0.173 versus VNQ, a separable band [0.20–0.30], STABLE holdout 0.96): the [[Auto parts retail|ORLY+AZO]] pattern, distinctness in the core with NSA the ETF-replicable drag. The contrast with [[Residential REITs]] is the lesson — not every single-asset REIT cohort is distinct; it depends on whether the asset's demand driver decouples from the broad rate/REIT factor. See below.

The single-asset REIT that didn't separate. Residential REITs validated a clean law: one asset (US apartments), one driver (rates plus market rents and supply), produces a factor distinct from the diluted [[VNQ]]. Self-storage looked like the same setup — one asset (storage units), a specific demand story (the "4 Ds": death, divorce, dislocation, downsizing, plus moves and small-business inventory). But it does not separate from broad REITs the way apartments do. Storage demand is real and idiosyncratic, yet the equities trade primarily on the same rate sensitivity that moves the whole REIT complex, so [[VNQ]] sits inside the cohort and the storage-specific premium over it is thin (+0.069). The names are distinct from apartments but not from REITs-in-general.

## Cluster validation

The candidate cohort is four public self-storage REITs — [[Public Storage|PSA]], [[Extra Space Storage|EXR]], [[CubeSmart|CUBE]], [[National Storage Affiliates|NSA]] — tested against the broad REIT ETFs ([[VNQ]]/[[XLRE]]), the residential REITs ([[Residential REITs|AVB]]/[[Residential REITs|EQR]]), and the market (SPY). 1Y window through 2026-06-18, threshold 0.5. All US-listed/synchronous. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.710 [0.507–0.894] | Tight big-three, loose NSA; weekly 0.707 (synchronous) |
| PC1 explained variance | 79.0% | One factor, with a notable PC2 (14.6%, the NSA axis) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0002 | Beats a random 4-pick |
| Vol-matched null p (10k) | 0.0001 | Real beyond shared vol |
| Holdout (2Y split) | WEAKENED 0.80 | train 0.889 → test 0.710 (loadings corr 0.81 — same factor, eroding) |
| Threshold clean width | 0.00 | VNQ/XLRE contaminate from 0.35; never isolates |
| Intra-adv vs broad REIT ETF (VNQ/XLRE) | +0.069 | Thin — correlates with broad REITs almost as much as itself |
| Intra-adv vs residential REITs (AVB/EQR) | +0.275 | Distinct from apartments — a different single-asset factor |
| Intra-adv vs market (SPY) | +0.432 | Not market beta (it is REIT/rate beta) |

Config: `scripts/cluster_configs/self_storage_reits.yaml`; registry row 2026-06-20.

### Boundary — VNQ joins at 0.35; the cohort never isolates

![[self-storage-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The big-three ([[Public Storage|PSA]]/[[Extra Space Storage|EXR]]/[[CubeSmart|CUBE]]) cluster with [[VNQ]], [[XLRE]], and the residential REITs (AVB/EQR) — the broad REIT complex — while [[National Storage Affiliates|NSA]] is a singleton and SPY stays out. The broad REIT ETF sitting inside the cohort is the ETF-replicable mark.*

The threshold scan returns zero clean width — the contamination order shows what the storage names cannot be separated from:

| Threshold | Joins the cohort cluster | Read |
|---|---|---|
| 0.35 | VNQ, XLRE | The broad REIT ETF — the cohort bleeds into REITs-in-general |
| 0.45 | + AVB, EQR | The residential REITs join the REIT complex |
| 0.50–0.70 | (REIT complex intact) | One rate-driven REIT cluster |

There is a narrow window below the VNQ-contamination cut where the big-three stand alone: [[Extra Space Storage|EXR]]+[[CubeSmart|CUBE]] close at 0.106 and [[Public Storage|PSA]] joins at 0.143, while VNQ does not contaminate until 0.35. So a big-three sub-cluster (PSA/EXR/CUBE, excluding the satellite NSA) separates from VNQ across [0.20–0.30] — a distinct sub-factor in the [[Auto parts retail|ORLY+AZO]] mold, confirmed by a dedicated three-name check (see "Sub-cohort" below). The cohort as defined (with NSA) never forms a clean cluster: NSA joins only at 0.450, after VNQ has already contaminated.

### Topology — a tight big-three and a satellite

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | EXR + CUBE | 0.106 | the tightest pair (corr 0.89) |
| 2 | PSA + (EXR+CUBE) | 0.143 | the big-three core closes |
| 3 | NSA + core | 0.450 | the satellite joins late — well above the VNQ cut |

The big-three close at 0.143 — as tight as any distinct cohort — but [[National Storage Affiliates|NSA]] joins only at 0.450. NSA's mid-cap size, secondary/tertiary-market footprint, and participating-regional-operator (PRO) structure make it the loose member (pairwise 0.51–0.59). PC1 explains 79.0% with a sizeable PC2 (14.6%) — the NSA-vs-big-three axis.

### Sub-cohort — the big-three (PSA/EXR/CUBE) ARE a distinct factor; NSA is the drag

![[sub-self-storage-big3-cluster-dendrogram-1y.png]]
*The three big self-storage REITs without NSA. At the 0.5 cut they still sit with the REIT complex, but the threshold scan isolates them across [0.20–0.30] before VNQ contaminates — a separable band the four-name cohort never had.*

A dedicated three-name check (`scripts/cluster_configs/sub_self_storage_big3.yaml`, registry row 2026-06-20) confirms the [[Public Storage|PSA]]/[[Extra Space Storage|EXR]]/[[CubeSmart|CUBE]] core is a genuine distinct, durable sub-factor — the ETF-replicable verdict on the four-name cohort is driven by the [[National Storage Affiliates|NSA]] satellite, not the core:

| Diagnostic | 4-name cohort (with NSA) | Big-three (PSA/EXR/CUBE) |
|---|---|---|
| Intra-corr (1Y) | 0.710 | 0.869 |
| PC1 variance | 79.0% | 91.3% |
| Intra-adv vs VNQ/XLRE | +0.069 | +0.173 |
| Threshold stable band | 0.00 (none) | [0.20–0.30], width 0.10 |
| Holdout (2Y) | WEAKENED 0.80 | STABLE 0.96 |

Removing NSA lifts the ETF intra-advantage from +0.069 to +0.173 ([[Railroads|railroads]]/[[Life science tools|life-science-tools]] territory), opens a separable band [0.20–0.30] before VNQ contaminates at 0.35, and — most tellingly — flips the holdout from WEAKENED to STABLE: the 2026 loosening that weakened the four-name cohort was almost entirely NSA diverging, while the big-three stayed tight (train 0.906 → test 0.870). All three nulls reject at the 0.0001 floor. This is the [[Auto parts retail|ORLY+AZO]] pattern — distinctness concentrated in a tight core sub-group, with a looser name dragging the full label into ETF-replicability. The ownable self-storage factor is the PSA/EXR/CUBE big-three; NSA adds broad-REIT drag.

### PC1 index weights

![[self-storage-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 79.0%; the big-three load ~0.52–0.53 and [[National Storage Affiliates|NSA]] loads lowest (0.404) — the satellite contributes least to the shared factor.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| PSA | 0.518 | 26.1% | 23.3% | 28.2% |
| EXR | 0.533 | 26.8% | 23.6% | 28.7% |
| CUBE | 0.533 | 26.8% | 22.4% | 30.2% |
| NSA | 0.404 | 20.3% | 39.6% | 12.9% |

The big-three are low-vol (22–24% annualized, investment-grade large-caps) and carry the factor; [[National Storage Affiliates|NSA]] is higher-vol (40%) and loads least. Unlike the flat-vector commodity cohorts, the loadings here are genuinely uneven (NSA lower) — which is why the holdout's PC1-loadings correlation (0.81) is meaningful: the factor structure is stable, it is only the strength that is eroding.

### Distinctness — distinct from apartments, not from REITs

![[self-storage-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A warm big-three block (0.85–0.89); a cool NSA row (0.51–0.59); the broad REIT ETF about as warm against the big-three as they are against the residential names — there is no storage-specific factor that sits apart from broad REITs.*

The intra-advantage numbers split cleanly: +0.275 versus the residential REITs (storage and apartments are genuinely different single-asset factors — they do not move together), but only +0.069 versus the broad REIT ETF (storage moves with REITs-in-general almost as much as with itself). A distinct storage factor would beat VNQ clearly; +0.069, with VNQ contaminating from 0.35, says the cohort is broad-REIT/rate beta plus a thin storage premium. Own [[VNQ]] (or [[XLRE]]); the bespoke storage basket adds little — though the PSA/EXR/CUBE big-three is the part with any separable content.

### Historical tightness evolution

![[self-storage-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Tight through 2021-25 (0.76–0.88, peaking in the 2022-23 storage boom), then loosening sharply in 2026 (0.66) as post-COVID storage demand normalized and the names diverged (the EXR/Life Storage integration, NSA's PRO-structure questions).*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.756 | 81.7% |
| 2022 | 0.862 | 89.7% |
| 2023 | 0.865 | 89.9% |
| 2024 | 0.811 | 85.9% |
| 2025 | 0.883 | 91.3% |
| 2026 | 0.656 | 75.8% |

*The cohesion was strong and durable for five years, then weakened in 2026 (holdout WEAKENED 0.80, latest 90-day 0.644). Even at its tight-2025 peak it was broad-REIT-embedded; the 2026 loosening only widens the gap from being a distinct factor.*

## Related

- [[Residential REITs]] — the distinct single-asset REIT factor; the instructive contrast (apartments decouple from VNQ, storage does not), and the cohort self-storage is most distinct from (+0.275)
- [[Public Storage]], [[Extra Space Storage]], [[CubeSmart]], [[National Storage Affiliates]] — the cohort members
- [[VNQ]], [[XLRE]] — the broad REIT ETFs the cohort cannot be distinguished from (contaminate from 0.35)
- [[Auto parts retail]] — the pair/sub-group distinctness pattern (ORLY+AZO); the PSA/EXR/CUBE big-three may be the analogue
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/self_storage_reits.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
