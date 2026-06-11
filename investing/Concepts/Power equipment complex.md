---
aliases: [Power equipment cohort, AI electrical equipment, Grid equipment complex]
---
#concept #power #ai #cohort

**Power equipment complex** — the electrical-equipment and grid-construction names the market narrates as one "AI buildout equipment" trade: [[Eaton]] (ETN), [[Quanta Services]] (PWR), [[GE Vernova]] (GEV), [[Vertiv]] (VRT), with [[Generac]] (GNRC) and the engine makers ([[Caterpillar]], Cummins) often lumped in. Formalization was triggered by the June 10, 2026 risk-off bloc (ETN/GNRC/PWR all -6%+ with no single catalyst). The validation verdict: real co-movement, no distinct boundary — this is AI-beta inside the broad industrial complex, not a standalone factor.

> [!warning] Cluster status: co-moving, boundary-dependent (Jun 10, 2026)
> Intra-correlation 0.650 (1y), PC1 73.8% — but the cohort never forms a clean cluster at any threshold: [[Caterpillar|CAT]]/CMI/XLI join its cluster from 0.40 and SPY by 0.45, while GEV and GNRC cut as singletons. Holdout WEAKENED (0.83 ratio, intra eroding -0.136); rolling tightness loosening 0.754 (2025) → 0.657 (2026). Permutation (cleaned stock-only null, 10,000 draws, Phipson-Smyth): random-basket AND vol-matched p = 0.0001 on intra and PC1 — the co-movement is real and not vol-driven; what fails is the boundary. Logged to the registry as boundary-dependent, not a validated standalone factor. Definition date 2026-06-10.

---

## Synthesis

The equipment complex is what a thematic basket looks like when the statistics say no. The four purest AI-electrical names co-move substantially — 0.650 average pairwise correlation, a common factor explaining 74% of variance, an [[Eaton]]+[[Vertiv]] core joining at 0.264 — but the boundary test fails everywhere: at the standard 0.4 threshold the cohort's cluster absorbs [[Caterpillar]], Cummins, and XLI itself, and by 0.45 it absorbs SPY. There is no threshold at which "AI electrical equipment" exists as a thing apart from "US industrials." The contrast with [[AI-power IPPs]] — validated the same evening with zero contamination across 0.25-0.50 — is the finding: in the AI-power trade, the merchant generators are a distinct factor; the equipment makers are the industrial complex wearing an AI hat. The rolling-tightness direction sharpens it: the complex was tighter in 2025 (0.754) and has been loosening through 2026 (0.657) as the capex-anxiety phase differentiates order-book stories ([[GE Vernova]]'s $163B backlog tape increasingly its own) from rate-sensitive electricals. June 10's bloc move was narrative correlation: [[Generac]] fell with ETN/PWR on the same headline but is a statistical singleton in every panel run this week. Structurally: hedge or express the AI-power theme through the IPP factor or single names; an "equipment basket" is XLI with extra beta.

## The cohort (as tested)

| Name | Role | Verdict |
|------|------|---------|
| [[Eaton]] | Electrical equipment (DC power distribution) | Core — tightest pair with [[Vertiv]] (0.264) |
| [[Vertiv]] | DC power/cooling pure-play | Core |
| [[Quanta Services]] | Grid/substation EPC | Joins core at 0.324 |
| [[GE Vernova]] | Turbines + grid equipment | Marginal — joins candidates at 0.396, cuts as a singleton in the full panel (CAT/CMI sit closer to the core than GEV does); its backlog story trades on its own events |
| [[Generac]] | Gensets/backup power | Not a member — singleton at every threshold despite moving with the Jun 10 bloc |
| [[Caterpillar]] / Cummins | Engines/industrials (control) | Contaminate the cohort's cluster from 0.40 — the boundary failure |

Config: `scripts/cluster_configs/power_equipment.yaml`. Controls: engines/gensets, the validated [[AI-power IPPs]], speed-to-power ([[Solaris Energy Infrastructure|SEI]]/[[Bloom Energy|BE]]), XLI/SPY/XLU.

## Cluster validation

![[power-equipment-cluster-dendrogram-1y.png]]
*1-year hierarchical clustering (cut 0.4): the candidate names land inside a mixed cluster with CAT, CMI, and XLI; GEV and GNRC are singletons; the [[AI-power IPPs]] cut cleanly as their own block. The equipment "cluster" has no edge of its own.*

### Headline diagnostics

| Diagnostic (1y to 2026-06-10) | Value | Read |
|---|---|---|
| Intra-cohort avg correlation | 0.650 (pairwise range 0.587-0.736) | Real co-movement |
| PC1 explained variance | 73.8% (PC2 11.0%) | One dominant factor among candidates |
| Weekly cross-check | 0.538 intra, PC1 65.6% | Direction holds on weekly returns |
| Holdout (2y temporal split) | Train 0.786/84.0% → test 0.650/73.8%; ratio 0.83; loadings corr 0.82 | WEAKENED — factor present but eroding (caveat: GEV listed Apr 2024, train half thin) |
| Threshold scan | No intact range at any threshold; CAT/CMI/XLI contaminate from 0.40, SPY from 0.45 | BOUNDARY-DEPENDENT — falsification of a distinct factor |
| Permutation p (random-basket, 10k) | 0.0001 intra / 0.0001 PC1 (null mean 0.136 / 37.8%) | Co-movement beats all 10,000 random baskets |
| Permutation p (vol-matched, 10k) | 0.0001 intra / 0.0001 PC1 (null mean 0.155 / 38.3%) | Not shared beta/vol — but the same is true of CAT/CMI/XLI, which is the boundary problem |

### Join distance topology

| Step | Left | Right | Distance (1-\|corr\|) | Members |
|------|------|-------|----------------------|---------|
| 1 | ETN | VRT | 0.264 | ETN+VRT |
| 2 | PWR | ETN+VRT | 0.324 | PWR+ETN+VRT |
| 3 | GEV | PWR+ETN+VRT | 0.396 | GEV+PWR+ETN+VRT |

The candidates do join below 0.4 among themselves — the failure is not internal looseness but external indistinctness: the controls join at nearly the same distances.

### PC1 index weights

![[power-equipment-cluster-pca-1y.png]]
*PCA on the candidate cohort: one dominant factor, near-equal loadings — but the factor extends beyond the candidate set.*

| Member | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|--------|-------------|----------------|---------|----------------------|
| ETN | 0.516 | 25.79% | 34.89% | 32.86% |
| PWR | 0.498 | 24.92% | 39.74% | 27.87% |
| GEV | 0.472 | 23.62% | 51.85% | 20.25% |
| VRT | 0.513 | 25.67% | 60.00% | 19.02% |

### Historical tightness evolution

![[power-equipment-cluster-rolling-tightness-90d.png]]
*Rolling 90-day tightness: loosening through 2026 — the opposite shape from the [[AI-power IPPs]], whose factor tightened as the PPA wave hit.*

| Year | Avg corr | PC1 | Core corr | Satellite corr | Final join distance |
|------|----------|-----|-----------|----------------|---------------------|
| 2025 | 0.754 | 81.7% | 0.719 | 0.789 | 0.298 |
| 2026 | 0.657 | 74.3% | 0.647 | 0.672 | 0.382 |

Latest 90d: avg corr 0.650, PC1 73.8%, final join distance 0.367. The 2025 buildout-mania phase traded the complex as one thing; 2026's capex anxiety is differentiating it.

### Correlation structure

![[power-equipment-cluster-correlation-1y.png]]
*1-year pairwise correlations: the candidate block is warm but so are its edges into CAT/CMI/XLI — the visual version of the boundary failure.*

Full numerics: `investing/attachments/power-equipment-cluster-results.txt`, `-holdout.txt`, `-threshold-scan.txt`.

## Boundary findings

- Not distinct from industrials: XLI joins the cohort's own cluster at the standard threshold — the defining failure. An equipment basket replicates leveraged XLI.
- Distinct from the [[AI-power IPPs]]: the IPP block cuts cleanly away (their intra 0.773 vs cross-group ~0.44-0.47) — the merchant-generation factor is the real standalone trade in AI power.
- [[Generac]] is narrative-correlated only: it fell with the bloc on June 10 but is a singleton in every statistical panel — its residential/genset mix trades its own cycle.
- [[GE Vernova]] is semi-detached: backlog-driven idiosyncratic tape (Apr 2026: backlog +$13B to $163B) keeps it from full membership despite the obvious economic linkage.

## What to watch

- Continued differentiation — if 2026 tightness keeps decaying, the complex resolves into single-name stories (GEV backlog conversion, VRT cooling cycle, PWR grid EPC) and the basket framing dies; a re-tightening (e.g., a new capex-acceleration phase) would justify a re-test.
- June 10 follow-through — whether the bloc move extends (shared repricing of AI-buildout duration) or disperses within days; the [[AI-power IPPs]] note carries the same watch from the factor side.
- GEV order book vs the complex — the cleanest tell for whether equipment trades on backlogs (idiosyncratic) or on the AI-capex narrative (common factor).
- Re-test trigger — re-run `power_equipment.yaml` after the next earnings round; if CAT/CMI decouple, the boundary may sharpen enough to revisit.

## Related

- [[AI-power IPPs]] — the validated factor next door; this note's contrast case
- [[Power constraints]] — the demand narrative both groups monetize
- [[Eaton]] / [[Quanta Services]] / [[GE Vernova]] / [[Vertiv]] — candidates
- [[Generac]] — tested, not a member
- [[Caterpillar]] — boundary contaminant (with Cummins)
- [[Solaris Energy Infrastructure]] / [[Bloom Energy]] — speed-to-power controls
- [[Long datacenter infrastructure]] — the thesis note this finding disciplines
- [[Hyperscaler capex]] — demand driver
- [[Data center infrastructure]] — category context

*Created 2026-06-10. Validation artifacts in `investing/attachments/power-equipment-cluster-*`; config `scripts/cluster_configs/power_equipment.yaml`.*
