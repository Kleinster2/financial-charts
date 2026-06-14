---
aliases: [Solar, Solar stocks, US solar, Solar equities]
tags: [concept, solar, clean-energy, cluster-validation]
---

# Solar

The listed US solar names — split across two halves of the value chain with different dominant drivers: utility-scale ([[First Solar]] FSLR thin-film panels, [[Nextracker]] NXT trackers — tariff/policy-driven) and residential ([[Enphase]] ENPH and [[SolarEdge]] SEDG inverters, [[Sunrun]] RUN installer/lease — interest-rate-driven). The validation finds a real solar complex that trades as solar-ETF beta and is internally split between those two halves.

> [!warning] Cluster status: real cohort, but solar-ETF beta and internally split (June 2026)
> The five solar names form a real, moderately cohesive cohort — intra-corr 0.514 (weekly 0.487), PC1 61.2%, rejecting the independence, random-basket and vol-matched nulls (p 0.0001 / 0.0005 / 0.0003). But two things keep it from being a clean, distinct single factor. First, it is not separable from the solar ETF: the intra-advantage vs TAN is −0.212 (each name correlates more with TAN, 0.726, than the names do with each other, 0.514) and TAN/ICLN contaminate the cohort from threshold 0.40 — own TAN for the sector, there is no stock-picking factor edge. Second, it splits by dominant driver: a residential sub-cohort ([[Enphase]]+[[SolarEdge]] at 0.293, [[Sunrun]] joining at 0.481 — rate-sensitive, 90–102% vol) and a utility-scale pair ([[First Solar]]+[[Nextracker]] at 0.427 — tariff/policy-driven, 58–70% vol), the two halves merging only at 0.530. Holdout WEAKENED (0.81) with PC1 loadings correlation just 0.29 — the factor structure is non-stationary as residential and utility-scale pull apart. Distinct only from the broad market (+0.175 vs SPY). See below.

The two findings are causally linked. The cohort is hard to separate from TAN precisely because it is two sub-factors averaged: each name correlates more with the solar ETF — which holds both halves — than with names on the other side of the residential/utility split. And the unstable holdout structure (loadings corr 0.29) is that split widening in real time: residential solar, crushed by high interest rates, and utility-scale solar, driven by IRA incentives and tariff policy, are pulling apart. It is the structural inverse of [[Airlines]], where one shared driver (jet fuel) bound different business models; here two different drivers (rates vs tariffs) are splitting one sector.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.514 | Moderate; weekly 0.487 (all US-listed) |
| PC1 explained variance | 61.2% | One dominant factor, but a real PC2 (the split) |
| Independence null p | 0.0001 | Series co-move |
| Random-basket null p | 0.0005 | Beats a random 5-pick — real cohesion |
| Vol-matched null p | 0.0003 | Real beyond shared (extreme residential) vol |
| Holdout (2Y split) | WEAKENED 0.81 | Loadings corr 0.29 — structure non-stationary (split widening) |
| Threshold clean width | 0.00 | TAN/ICLN contaminate from 0.40 — not separable from the ETF |
| Intra-adv vs solar ETF (TAN) | −0.212 | Negative — it IS solar-ETF beta |
| Intra-adv vs clean energy (ICLN) | −0.095 | Clean-energy beta |
| Intra-adv vs market (SPY) | +0.175 | Distinct only from the broad market |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed (synchronous). [[Nextracker]] listed February 2023, so the rolling history is short. Config: `scripts/cluster_configs/solar.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — two sub-cohorts, not separable from the ETF

![[solar-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The cohort splits into a residential block ([[Enphase]]/[[SolarEdge]]/[[Sunrun]]) and a utility-scale pair ([[First Solar]]/[[Nextracker]]) — and the whole thing merges with the solar ETF (TAN) and clean-energy ETF (ICLN). Only the broad market (SPY) sits apart. Solar is a real complex, but it is its own ETF, and it is two sub-factors.*

The threshold scan returns zero clean width: TAN and ICLN contaminate the cohort from threshold 0.40, so the solar names cannot be separated from the solar/clean-energy ETFs. This is the [[Homebuilders]] / [[Datacenter power and cooling|DC power]] "real-but-= sector-ETF" signature, combined with the [[Title Insurance|housing]]-style value-chain split inside it.

### Topology — residential vs utility-scale

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | ENPH + SEDG | 0.293 | Residential inverter pair — tightest |
| 2 | FSLR + NXT | 0.427 | Utility-scale pair (panels + trackers) |
| 3 | RUN + (ENPH+SEDG) | 0.481 | Residential installer joins the residential block |
| 4 | (FSLR+NXT) + (RUN+ENPH+SEDG) | 0.530 | The two halves merge — above the 0.5 cut |

The cohort is two sub-cohorts that join only at 0.530: residential ([[Enphase]]+[[SolarEdge]]+[[Sunrun]]) on the interest-rate driver, and utility-scale ([[First Solar]]+[[Nextracker]]) on the tariff/policy driver. At the 0.5 threshold they are separate — solar is not one factor, it is two, split by what moves them.

### PC1 index weights

![[solar-cluster-pca-1y.png]]
*PCA on the cohort. PC1 explains 61.2% with a meaningful PC2 (14.6%) — the residential/utility split. Note the volatilities: the residential names ([[Enphase]] 91%, [[SolarEdge]] 102%, [[Sunrun]] 98%) are far higher-beta than utility-scale ([[First Solar]] 58%, [[Nextracker]] 70%).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| First Solar (FSLR) | 0.422 | 18.9% | 57.9% | 26.2% |
| Enphase (ENPH) | 0.460 | 20.6% | 90.6% | 18.3% |
| SolarEdge (SEDG) | 0.465 | 20.8% | 102.3% | 16.4% |
| Sunrun (RUN) | 0.443 | 19.9% | 97.9% | 16.3% |
| Nextracker (NXT) | 0.444 | 19.9% | 70.2% | 22.8% |

The lower-vol utility-scale names ([[First Solar]], [[Nextracker]]) take the largest raw PC1-mimic weights — the residential names are higher-beta but, on a risk-adjusted basis, the utility-scale leg is the calmer expression of the solar factor.

### Distinctness

![[solar-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. Two warm blocks (residential / utility-scale) with cooler cross-pairs between them, and the whole cohort warm against TAN/ICLN. The −0.212 negative intra-advantage vs TAN made visible: each name is warmer to the ETF than to the other half of its own cohort.*

The cohort is distinct only from the broad market (+0.175 vs SPY); it is negative-advantage vs both the solar ETF (−0.212) and clean energy (−0.095). The investable read: own TAN for solar-sector beta; to express a view, the real choice is residential (rate-sensitive, [[Enphase]]/[[SolarEdge]]/[[Sunrun]]) vs utility-scale (tariff/policy, [[First Solar]]/[[Nextracker]]) — the two halves can and do diverge.

### Historical tightness evolution

![[solar-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion. Moderate and eroding: 0.59 (2024) → 0.61 (2025) → 0.43 (2026) as the residential and utility-scale halves decoupled under opposite policy/rate pressures.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2024 | 0.587 | 67.3% | 0.506 |
| 2025 | 0.606 | 68.7% | 0.477 |
| 2026 | 0.431 | 54.8% | 0.642 |

*Eroding / regime-dependent: the solar factor was moderately tight in 2024–25 and loosened through 2026 as residential (hit by high rates) and utility-scale (supported by IRA/tariffs) diverged — the split is widening, which is why the holdout factor structure is unstable.*

### The read-through

- Own TAN, not the names. The solar names are a real cohort (passes all nulls) but solar-ETF beta (−0.212 vs TAN) — no stock-picking factor edge over the ETF.
- It is two factors, split by driver. Residential ([[Enphase]]/[[SolarEdge]]/[[Sunrun]]) trades on interest rates; utility-scale ([[First Solar]]/[[Nextracker]]) on tariffs/IRA policy. They join only at 0.530 and are pulling apart — the real expression of a solar view is one half vs the other.
- The only standalone micro-cluster is the residential-inverter pair. The sub-cohort robustness sweep ([[Vault cluster taxonomy#Sub-cohort robustness sweep]]) classifies [[Enphase]]+[[SolarEdge]] (intra-corr 0.70) as moderately robust — stable threshold band [0.35–0.45], the only sub-structure in solar that holds up on its own. [[Sunrun]] (the residential installer) and the utility-scale pair are looser. So the tradeable cluster inside solar is the ENPH+SEDG inverter duopoly, not "solar" — and even that is moderately, not strongly, robust.
- The split is widening in real time. Holdout loadings corr 0.29 (vs airlines' 0.97) and intra-corr eroding 0.61 → 0.43 — the factor structure is non-stationary as the two drivers diverge.
- The structural inverse of airlines. There one shared driver (fuel) bound different models; here two different drivers (rates vs tariffs) split one sector. The lesson is symmetric: cohesion tracks shared dominant drivers, not shared industry labels.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14).

## Related

- [[Energy and Utilities]] — the broad parent sector
- [[First Solar]], [[Nextracker]] — utility-scale leg (tariff/policy driver)
- [[Enphase]], [[SolarEdge]], [[Sunrun]] — residential leg (interest-rate driver)
- [[Airlines]] — the structural inverse (one shared driver binds different models)
- [[Homebuilders]], [[Datacenter power and cooling]] — sibling "real-but-= sector-ETF" cohorts
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
