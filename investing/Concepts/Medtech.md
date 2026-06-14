---
aliases: [Medtech, Medical device makers, Medical devices, Medtech cohort, Medtech cluster]
tags: [concept, healthcare, medical-devices, market-structure, cluster-validation]
---

# Medtech

The listed US medical-device majors — [[Medtronic]] (MDT), [[Boston Scientific]] (BSX), [[Intuitive Surgical]] (ISRG), [[ResMed]] (RMD), [[Stryker]] (SYK), [[Edwards Lifesciences]] (EW), [[Abbott]] (ABT). A clear industry with a shared narrative (defensive secular-growth healthcare, procedure volumes, hospital capex, reimbursement) — but, as the validation shows, not a shared return factor. "Medtech" is a sector label, not a cluster.

> [!failure] Cluster status: falsified — a sector, not a factor (June 2026)
> The seven device makers do not trade as one factor: intra-corr 0.348 (well below the 0.50 floor; 0.266 on weekly returns — even lower, with no async-trading excuse since all are US-listed), PC1 only 44.8% with variance spread across PC2–PC4. Hierarchical clustering shatters the cohort into singletons — [[Edwards Lifesciences]], [[ResMed]], [[Abbott]] and [[Boston Scientific]] each stand alone; only [[Medtronic]]/[[Intuitive Surgical]]/[[Stryker]] loosely group (with the IHI ETF). The decisive number is the negative intra-advantage vs the ETFs (−0.078): the medtech names correlate more with IHI/[[XLV]] than with each other — the "Mag-7 is QQQ" signature, no medtech-specific factor beyond healthcare/market beta. Cohesion has fragmented from 0.672 (2022) to 0.292 (2026) as the franchises decoupled. The only real pair is [[Medtronic]]+[[Stryker]] (0.56), the two diversified generalists. See below.

Each name trades on its own franchise calendar — [[Intuitive Surgical]] on robotic-surgery procedure growth and multiple, [[Edwards Lifesciences]] on the TAVR cycle and trial read-outs, [[ResMed]] on sleep-apnea share and GLP-1 fears, [[Boston Scientific]] on electrophysiology/cardiology launches, [[Abbott]] on its diversified diagnostics-plus-nutrition mix. These catalysts are independent, so there is no common medtech factor for them to share.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.348 [0.08–0.56] | Weak — below the 0.50 floor; weekly 0.266 (lower, no async) |
| PC1 explained variance | 44.8% (PC2 13.8%, PC3 11.9%) | Below 50% — genuinely multi-factor |
| Random-basket p (10k) | 0.0096 | Marginal — barely beats random via shared healthcare beta |
| Vol-matched p (10k) | 0.0143 | Marginal |
| Threshold stable width | 0.00 — BOUNDARY-DEPENDENT | Never a clean cluster; the names shatter into singletons |
| Holdout ratio (2Y split) | 0.85 (WEAKENED at 0.33–0.39) | Durably weak; loadings corr 0.29 (unstable factor structure) |
| Intra-adv vs ETFs (IHI/[[XLV]]/[[SPY]]) | −0.078 | Negative — more correlated to the ETFs than to each other |
| Intra-adv vs pharma ([[Eli Lilly\|LLY]]/[[Merck\|MRK]]/[[Pfizer\|PFE]]) | +0.137 | Mildly distinct from pharma — but weak cohesion either way |

1Y daily log returns through 2026-06-12, threshold 0.5. Config: `scripts/cluster_configs/medtech.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — the cohort shatters into singletons

![[medtech-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The seven device makers never form one cluster: [[Edwards Lifesciences]], [[ResMed]], [[Abbott]], [[Boston Scientific]] are each singletons; only MDT/ISRG/SYK loosely group, and they pull in IHI (the medical-devices ETF) before cohering tightly. The pharma names (LLY/MRK) and the ETFs sit in their own clusters. There is no medtech factor in the tape.*

The threshold scan returns zero width — like [[Mag 7 cluster|Mag 7]] and [[Exchange operators]], the cohort never isolates as one cluster. But where the exchanges falsification had a constructive sub-structure (ICE/NDAQ → [[Financial data providers|data toll roads]]), medtech is pure dispersion: no clean sub-cluster, just idiosyncratic singletons plus the MDT/SYK generalist pair.

### Topology — one loose pair, then nothing tight

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | MDT + SYK | 0.445 | The only sub-0.50 pair — the two diversified device generalists |
| 2 | + RMD | 0.511 | ResMed attaches above the threshold |
| 3 | + ABT | 0.600 | Abbott joins loosely |
| 4 | ISRG + EW | 0.606 | The two high-growth franchise pure-plays pair, but far out |
| 5 | (MDT+SYK+RMD+ABT) + (ISRG+EW) | 0.682 | The halves connect only at very high distance |
| 6 | + BSX | 0.728 | Boston Scientific is the loosest — joins last |

Only [[Medtronic]]+[[Stryker]] join below the 0.50 threshold (0.445); everything else connects above it. A cohort whose members first cohere at 0.51–0.73 is not a cluster — it is a list.

### PC1 index weights

![[medtech-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains only 44.8% and the scree is flat (PC2 13.8%, PC3 11.9%, PC4 10.3%) — the hallmark of a multi-factor set with no dominant common driver. [[Stryker]] (0.459) and [[Medtronic]] (0.431) load highest; [[Boston Scientific]] (0.303) lowest.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| MDT | 0.431 | 16.4% | 21.9% | 19.8% |
| BSX | 0.303 | 11.6% | 39.9% | 7.7% |
| ISRG | 0.378 | 14.4% | 31.6% | 12.1% |
| RMD | 0.368 | 14.0% | 25.5% | 14.6% |
| SYK | 0.459 | 17.5% | 24.2% | 19.1% |
| EW | 0.325 | 12.4% | 25.0% | 13.2% |
| ABT | 0.358 | 13.7% | 26.5% | 13.6% |

With PC1 at only 44.8%, the PC1-mimic basket is not a meaningful single trade — more than half the cohort's variance lives outside the first factor, in the names' independent franchise paths.

### Distinctness

![[medtech-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The block is patchy, not uniformly warm: MDT-SYK (0.56) and RMD-SYK (0.50) are the warm spots, but RMD-BSX (0.08), ABT-BSX (0.23), and EW-RMD (0.23) are cold. A real cluster's heatmap is warm everywhere; this one is mottled.*

### Historical tightness evolution

![[medtech-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion. Medtech cohered in macro-driven windows — the 2020 COVID-healthcare rotation (0.593) and the 2022 defensive bid (0.672) — but has fragmented to 0.29 by 2026 as rates normalized and each franchise reverted to its own catalysts. The cohort is a beta trade in risk-off regimes, not a structural factor.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2022 | 0.672 | 72.2% | 0.400 |
| 2024 | 0.344 | 44.3% | 0.742 |
| 2026 | 0.292 | 40.4% | 0.779 |

*Regime-dependent, not durable: medtech tightens when a macro factor (a defensive rotation, a rate move) temporarily dominates single-name fundamentals, and disperses when it passes. The monotonic decline from 2022 is the fragmentation signature.*

### The read-through

- Do not trade "medtech" as one basket. There is no medtech factor (intra 0.348, PC1 44.8%, negative intra-advantage vs the sector ETFs). The names move on independent franchise calendars.
- If you want the sector, the ETF is the cohort. IHI (medical devices) or [[XLV]] (healthcare) captures the only common driver — healthcare/market beta — at least as well as an equal-weighted basket, because the basket is more correlated to the ETF than to itself.
- Trade the franchises, not the sector. The investable theses are single-name — robotic surgery ([[Intuitive Surgical]]), structural heart ([[Edwards Lifesciences]]), the GLP-1 read-through on devices ([[ResMed]]) — each on its own catalyst path, not a shared cohort.
- The contrast with [[Financial data providers]] is the lesson. Both are "defensive compounder" sectors, but the data toll roads share a revenue model (recurring subscriptions) that binds them into one factor (intra 0.607); medtech shares only a GICS code, and a code is not a factor.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation is moot for a falsified cohort; definition date 2026-06-14 is logged.

## Related

- [[Vault cluster taxonomy]] — cross-cohort comparison; this joins [[Mag 7 cluster]], [[Foundry monopoly consolidation|Foundry monopoly]], and [[Exchange operators]] as documented falsifications
- [[Financial data providers]] — the contrast: a defensive sector that IS a cluster (shared revenue model)
- [[Medtronic]], [[Boston Scientific]], [[Intuitive Surgical]], [[ResMed]], [[Stryker]], [[Edwards Lifesciences]], [[Abbott]] — the seven members
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
