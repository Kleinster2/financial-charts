---
aliases: [Datacenter power and cooling, DC power and cooling, AI power equipment, datacenter electrification, power and cooling equipment, AI datacenter power]
tags: [concept, ai-infrastructure, datacenter, power, electrical, industrials, cluster-validation]
---

# Datacenter power and cooling

The listed equipment names that supply the electrical and thermal "plumbing" of the AI buildout — power distribution, switchgear, and liquid/air cooling inside the datacenter, plus the generation equipment that feeds it. The cohort: [[Vertiv]] (VRT, the marquee power+thermal pure-play), [[Eaton]] (ETN, electrical equipment), [[nVent Electric]] (NVT, enclosures + liquid cooling), [[GE Vernova]] (GEV, gas turbines + grid), and [[Powell Industries]] (POWL, custom switchgear). The validation shows a real, cohesive cohort — but one that trades as the AI-levered sleeve of industrials, not as a separable factor.

> [!warning] Cluster status: real cohort, but not a separable factor — AI-levered industrials (June 2026)
> The five power/cooling names form a genuine, single-factor cohort — intra-corr 0.597 (weekly 0.544), PC1 68.0%, rejecting the independence, random-basket and vol-matched nulls all at the 0.0001–0.0002 floor, with all five joining a clean tree ([[Vertiv]]+[[Eaton]] at 0.27 → [[nVent Electric]] 0.34 → [[GE Vernova]] 0.39 → [[Powell Industries]] 0.48). Power *generation* (GEV) binds with in-datacenter distribution/cooling rather than splitting off, so the "AI power" theme is one equity structure. But it is not a *distinct* factor: the cohort clusters with the industrials ETF (XLI) and the market (SPY), the intra-advantage vs XLI is −0.011 (the names correlate more with industrials than with each other), and the threshold scan is boundary-dependent (XLI/SPY contaminate from 0.45). It IS distinct from the power-generation/utility trade (+0.384 vs XLU — this is not the [[AI-power IPPs]] / merchant-power factor) and partly from AI-compute (+0.183 vs NVDA — not just NVDA beta). Holdout WEAKENED (0.83, off a tight 0.72 in 2024–25) but loadings corr 0.91 — durable structure, eroding tightness. Same shape as [[Brazil fintech]] and copper: a real cohort replicable by its sector ETF, here XLI with an AI tilt. See below.

The theme is real in the businesses — VRT, ETN, NVT, GEV and POWL are all riding the step-change in datacenter power density and the grid/cooling buildout that AI capex requires. But at the equity-factor level they trade as industrials with an AI beta, not as a bespoke "AI power" object. The key bifurcation: this equipment cohort is a different factor from the power-*generation* trade — the [[AI-power IPPs]] (merchant nuclear/gas generators like Constellation/Vistra) sit on the utility side (+0.384 distinct here), while the equipment makers sit on the industrials side. Both monetize AI electricity demand; they are not one trade.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.597 [0.407–0.734] | Cohesive; weekly 0.544 (all US-listed) |
| PC1 explained variance | 68.0% | Single-factor cohort |
| Independence null p | 0.0001 | Series co-move |
| Random-basket null p | 0.0001 | Beats a random 5-pick at the floor — real cohesion |
| Vol-matched null p | 0.0001 | Real beyond shared vol |
| Holdout (2Y split) | WEAKENED 0.83 | Loadings corr 0.91 — durable structure, eroding tightness |
| Threshold clean width | 0.00 | XLI/SPY contaminate from 0.45 — not separable from industrials |
| Intra-adv vs industrials (XLI) | −0.011 | Negative — it IS industrials beta |
| Intra-adv vs utilities (XLU) | +0.384 | Distinct from the generation / IPP trade |
| Intra-adv vs AI-compute (NVDA) | +0.183 | Partly distinct — not just NVDA beta |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed (synchronous). [[GE Vernova]] spun off April 2024, so the rolling history is short. Config: `scripts/cluster_configs/dc_power_cooling.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — cohesive, but merges with industrials

![[dcpower-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The five power/cooling names form one cluster — but it merges with the industrials ETF (XLI) and the market (SPY). [[NVIDIA]] and the utilities ETF (XLU) sit apart. The cohort is real and single-factor, but it is the AI-levered slice of industrials, not a standalone factor.*

The threshold scan returns zero clean width: the five names build up cleanly through threshold 0.40, but the moment the cohort becomes fully intact (0.50) the industrials ETF and SPY have already joined (XLI/SPY contaminate from 0.45). This is the [[Brazil fintech]] / [[Nuclear renaissance|nuclear]] signature — a real cohort that cannot be separated from its sector benchmark — with XLI as the parent here.

### Topology — generation joins distribution and cooling

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | VRT + ETN | 0.266 | Power core — Vertiv + Eaton |
| 2 | NVT + (VRT+ETN) | 0.340 | nVent (cooling/enclosures) joins |
| 3 | GEV + core | 0.391 | Generation equipment binds — does not split off |
| 4 | POWL + rest | 0.477 | Small-cap switchgear joins last (LNG-tilted) |

The notable result is step 3: [[GE Vernova]] (power generation — turbines, grid) joins the in-datacenter distribution/cooling names at 0.391, well inside the cohort. Generation equipment and distribution/cooling equipment trade as one factor — the market prices the whole AI-power-equipment chain together. [[Powell Industries]] is the loosest member (joins at 0.477, lowest PC1 loading), its partly LNG/oil-gas order book diluting the datacenter signal.

### PC1 index weights

![[dcpower-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 68.0% with near-even loadings (0.40–0.48) — a clean single factor with no dominant name.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| Vertiv (VRT) | 0.468 | 21.0% | 59.9% | 16.6% |
| Eaton (ETN) | 0.483 | 21.7% | 35.2% | 29.2% |
| nVent (NVT) | 0.454 | 20.4% | 42.1% | 23.0% |
| GE Vernova (GEV) | 0.424 | 19.0% | 51.9% | 17.4% |
| Powell (POWL) | 0.401 | 18.0% | 61.9% | 13.8% |

Volatilities span a wide range (ETN 35% to POWL 62%), so the raw PC1-mimic basket tilts heavily to the lower-vol [[Eaton]] (29.2%) and away from the high-vol pure-plays — the diversified large-cap is the calm anchor, the pure-plays the high-beta expression.

### Distinctness

![[dcpower-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The cohort block is warm — but it is just as warm against XLI (industrials), which is the −0.011 intra-advantage made visible. It is clearly cooler against XLU (utilities) and [[NVIDIA]].*

The cohort is distinct from the two adjacent factors that matter — utilities/generation (+0.384 vs XLU) and AI-compute (+0.183 vs NVDA) — but not from broad industrials (−0.011 vs XLI). The investable read: this is an AI-tilted industrials trade, a different object from both the [[AI-power IPPs]] (utility-side generation) and the GPU names ([[NVIDIA]]).

### Historical tightness evolution

![[dcpower-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion. Short history — the cohort only became measurable once [[GE Vernova]] listed (April 2024) — but tight in 2025 (0.678) and eroding into 2026 (0.576) as the initial AI-power-trade surge matured.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2025 | 0.678 | 75.0% | 0.477 |
| 2026 | 0.576 | 66.4% | 0.527 |
| Latest 90d | 0.608 | 68.8% | 0.420 |

*Newly formed and eroding: the cohort was tightest in the 2024–25 AI-power-trade surge (holdout train half 0.72) and has loosened since (0.58 in 2026), though the factor structure persists (loadings corr 0.91). Durability is unproven on this short history — call it a real, currently-eroding cohort, not yet a structural one.*

### The read-through

- Real cohort, but own industrials to replicate it. The five names are one single-factor trade (intra 0.597, all nulls at the floor) — but it is the AI-levered slice of industrials (−0.011 vs XLI), so an XLI position with an AI-power tilt captures most of it. There is no bespoke-basket edge over industrials beta.
- It is NOT the AI-power generation trade. +0.384 distinct from XLU — the equipment makers (VRT/ETN/NVT/GEV/POWL) are a different factor from the [[AI-power IPPs]] (Constellation/Vistra merchant generators). "AI electricity demand" bifurcates: equipment trades as industrials, generation as utilities/merchant power.
- It is NOT just NVDA beta. +0.183 vs [[NVIDIA]] — the power/cooling names have their own factor one rung downstream of AI compute, not a pure GPU proxy.
- The whole equipment chain trades together. Power generation ([[GE Vernova]]) binds with in-datacenter distribution/cooling rather than splitting — the market prices the AI-power-equipment supply chain as one object.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14).

## Related

- [[AI-power IPPs]] — the generation/utility side of AI electricity demand (a distinct factor, +0.384 here)
- [[Vertiv]], [[Eaton]], [[nVent Electric]], [[GE Vernova]], [[Powell Industries]] — the cohort members
- [[Data Centers]] — the end market
- [[NVIDIA]] — the AI-capex driver upstream (partly distinct, +0.183)
- [[Aeroderivative turbines for data centers]] — adjacent generation-equipment theme
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
