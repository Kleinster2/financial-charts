---
aliases: [AI interconnect, AI optics, AI networking, AI optics/networking, AI datacenter interconnect, Datacenter interconnect, AI connectivity silicon]
tags: [concept, ai-infrastructure, datacenter, optical, interconnect, networking, cluster-validation]
---

# AI interconnect

The listed equities that sell the "plumbing" of the AI datacenter buildout — the bandwidth between chips, racks and campuses rather than the compute itself. Two business types get bundled under the "AI optics / networking" label: the optical layer — transceivers and lasers ([[Coherent]] COHR) and optical networking systems ([[Ciena]] CIEN) — and the electrical-interconnect silicon — active electrical cables ([[Credo Technology Group]] CRDO) and PCIe/CXL retimers ([[Astera Labs]] ALAB). The audit asked whether these four trade as one "AI interconnect" factor. They do not: they decompose into an optical sleeve that is not distinct from the broad optical complex and an interconnect-silicon pair that is the only genuinely new micro-cohort.

> [!warning] Cluster status: not one cohort — an optical sleeve and an interconnect pair (June 2026)
> The four AI-interconnect names share real AI-datacenter-capex beta — they reject the independence, random-basket and vol-matched nulls (p 0.0001 / 0.0023 / 0.0002). But the random-basket pass is ~20× weaker than the validated cohorts (which hit the 0.0001 floor), and every structural test says this is two sub-cohorts, not one factor. The cohort never forms a clean single cluster at any threshold (zero stable width): it splits into an optical pair ([[Coherent]]+[[Ciena]], 0.71) and a connectivity-silicon pair ([[Credo Technology Group]]+[[Astera Labs]], 0.61) that join only at distance 0.589 — above the 0.5 cut. The broad optical peers [[Lumentum]] and [[Fabrinet]] contaminate the optical half from threshold 0.25, so the intra-advantage vs optical peers is negative (−0.054): the four names correlate more with the broad optics complex than with each other. Holdout WEAKENED (ratio 0.73) and the factor structure flips between halves (PC1 loadings corr 0.12). The constructive read: the optical sleeve belongs to the [[AI fiber supercycle]] optical complex, and the [[Credo Technology Group]]+[[Astera Labs]] interconnect-silicon pair is the new micro-cohort, sitting under [[Connectivity]]. "AI optics/networking" is a thematic label spanning two factors, not a tradeable cohort. See below.

AI interconnect is the equity expression of a real bottleneck — as GPU clusters scale, the value of moving bits between accelerators rises faster than the accelerators themselves, and the market now prices fiber, transceivers, cables and retimers as direct constraints on AI scaling (the [[AI fiber supercycle]] rerating). But "the interconnect trade" is not one tape. Optical components (COHR/CIEN/LITE/FN) move on the transceiver/laser capacity cycle; connectivity silicon (CRDO/ALAB) moves on the AEC/retimer attach rate inside the rack. The two share the AI-capex driver but trade on different supply cycles, which is exactly what the cluster test recovers.

## Cluster validation

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.495 [0.363–0.715] | Two tight pairs averaged; weekly 0.284 (drops hard) |
| PC1 explained variance | 62.2% | Moderate; large PC2 (21.2%) = a second factor |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0023 | Passes, but ~20× weaker than the floor-passing cohorts |
| Vol-matched null p (10k) | 0.0002 | Cohesion exceeds same-vol baskets — real shared beta |
| Holdout (2Y split) | WEAKENED 0.73 | Loadings corr 0.12 — factor structure flips between halves |
| Threshold clean width | 0.00 | Never a clean single cluster — optical peers contaminate from 0.25 |
| Intra-adv vs optical peers (LITE/FN) | −0.054 | Negative — optical half is not distinct from broad optics |
| Intra-adv vs networking giants (ANET/AVGO) | +0.032 | Weakly distinct from the switching tier |
| Intra-adv vs AI-compute (NVDA) | +0.085 | Weakly distinct from GPU demand |

1Y daily log returns through 2026-06-12, threshold 0.5. All four US-listed (no async-close issue) — the weekly drop to 0.284 is genuine looseness, not a stale-quote artifact. Config: `scripts/cluster_configs/ai_optics.yaml`; registry row 2026-06-14. Terminology: [[Cohort, cluster, basket]].

### Boundary — the four never form one cluster

![[aioptics-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The named cohort does not form a single cluster: [[Credo Technology Group]]+[[Astera Labs]] form a connectivity-silicon cluster, while [[Coherent]]+[[Ciena]] join the broad optical peers [[Lumentum]]+[[Fabrinet]] — the optical sleeve is part of the optical complex, not a distinct "AI optics" factor. [[Arista Networks]] sits alone; [[Broadcom]]/[[NVIDIA]] cluster with the ETFs. Four separate structures, not one.*

The threshold scan returns zero stable width — the cohort never returns as a clean single cluster at any cut. [[Lumentum]] contaminates the optical half from threshold 0.25, [[Lumentum]]+[[Fabrinet]] from 0.35; the four only sit in one cluster at 0.60, by which point seven outside names (the optics peers, the networking giants, NVDA, the ETFs) have also joined. This is the same boundary-dependent signature as [[Exchange operators]] — two decoupled sub-factors under one label — but here the random-basket and vol-matched nulls pass, so the sub-pairs are genuinely cohesive rather than a bag of singletons like [[Medtech]].

### Topology — an optical pair and an interconnect pair

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | COHR + CIEN | 0.285 | Optical pair (transceivers/lasers + optical systems) |
| 2 | CRDO + ALAB | 0.390 | Interconnect-silicon pair (AECs + retimers) |
| 3 | (COHR+CIEN) + (CRDO+ALAB) | 0.589 | The two sleeves merge — above the 0.5 cut |

The cohort is two pairs from two different supply cycles. [[Coherent]]+[[Ciena]] (optical, 0.71) and [[Credo Technology Group]]+[[Astera Labs]] (connectivity silicon, 0.61) are each tight; the cross-pairs are loose (COHR–CRDO 0.38, CIEN–CRDO 0.36). They do not join until 0.589 — so at the 0.5 threshold there is no four-name cohort, only two pairs. The interconnect-silicon pair is the genuinely new structure the audit surfaced; the optical pair was already inside the optical complex.

### PC1 index weights

![[aioptics-cluster-pca-1y.png]]
*PCA scree and PC1 loadings. PC1 explains only 62.2% with a large PC2 (21.2%) — the signature of two factors, not one. Loadings are near-uniform (0.46–0.52), so a PC1-mimic basket cannot tell the two pairs apart; the second component is where the optical-vs-interconnect split lives.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| COHR | 0.522 | 26.1% | 75.8% | 28.0% |
| CIEN | 0.509 | 25.5% | 69.6% | 29.8% |
| CRDO | 0.463 | 23.2% | 90.8% | 20.7% |
| ALAB | 0.503 | 25.2% | 95.0% | 21.5% |

The connectivity-silicon pair (CRDO/ALAB, 91–95% vol) is far more volatile than the optical pair (COHR/CIEN, 70–76%) — a second tell that these are different risk objects bundled under one name.

### Distinctness

![[aioptics-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. Two warm blocks — the COHR/CIEN optical corner and the CRDO/ALAB interconnect corner — with cool cross-pairs between them. The optical block is not cooler against [[Lumentum]]/[[Fabrinet]] than it is internally (the negative intra-advantage made visible). The whole cohort is clearly cooler against [[NVIDIA]] — it is not just AI-compute beta.*

The named cohort is weakly distinct from the networking giants ([[Arista Networks]]/[[Broadcom]], +0.032) and from AI-compute ([[NVIDIA]], +0.085) — it is not simply NVDA beta — but it is not distinct from the broad optical complex at all (−0.054 vs [[Lumentum]]/[[Fabrinet]]). The optical sleeve has no separate identity from "optics"; only the interconnect-silicon pair is new.

### Historical tightness evolution

![[aioptics-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion. Short, non-monotonic history — tightened through the 2025 optical rerating then loosened through 2026 as the two supply cycles diverged. Not a durable single factor.*

| Window | Avg intra-corr | PC1 | Final join distance |
|---|---|---|---|
| 2024 | 0.417 | 56.4% | 0.625 |
| 2025 | 0.631 | 72.4% | 0.396 |
| 2026 | 0.505 | 63.1% | 0.583 |
| Latest 90d | 0.491 | 61.9% | 0.604 |

*Regime-dependent: the four names tightened into one block during the 2025 AI-optics rerating (final join 0.396, briefly a real cluster) then decoupled through 2026 (final join 0.583, back above the 0.5 cut). The holdout confirms it — the test half is 0.73 of the train half and the PC1 loadings barely correlate across the split (0.12), so the factor structure itself is not stable. The 2025 episode was a correlated rerating, not a standing factor.*

### The read-through

- AI interconnect is not one trade. The four names pass the cohesion nulls on shared AI-capex beta but split into an optical pair and a connectivity-silicon pair that only merge at 0.589 — there is no four-name cohort at the standard cut. A single "AI optics/networking basket" averages two different supply cycles.
- The optical sleeve belongs to the optical complex. [[Coherent]]+[[Ciena]] trade with [[Lumentum]]/[[Fabrinet]] (negative intra-advantage vs them) — they are the listed expression of the [[AI fiber supercycle]], not a separate factor. To own "AI optics," own the optical complex; these two do not isolate it.
- The interconnect-silicon pair is the new micro-cohort. [[Credo Technology Group]]+[[Astera Labs]] (AECs + retimers, 0.61, 91–95% vol) is the genuinely distinct structure — the in-rack electrical-interconnect attach trade, sitting under [[Connectivity]] alongside the networking-semis names. It is the constructive output of this falsification.
- It is regime-dependent, not durable. The 2025 tightening was a correlated optical rerating that decoupled in 2026 (holdout 0.73, loadings corr 0.12). Do not treat "AI interconnect" as a standing factor; treat the two pairs as separate, cyclical trades.

Method and terminology: `docs/cluster-validation.md`, [[Cohort, cluster, basket]], [[Vault cluster taxonomy]]. Post-definition OOS re-validation queued for the next quarterly pass (definition date 2026-06-14).

## Related

- [[AI fiber supercycle]] — the optical-demand theme; home of the COHR/CIEN optical sleeve (with [[Lumentum]]/[[Fabrinet]]/[[Corning]])
- [[Connectivity]] — the networking-semiconductors cluster; home of the CRDO/ALAB interconnect-silicon pair
- [[Coherent]], [[Ciena]] — the optical sleeve; [[Credo Technology Group]], [[Astera Labs]] — the interconnect-silicon pair
- [[Lumentum]], [[Fabrinet]] — broad optical peers the optical sleeve is not distinct from
- [[Arista Networks]], [[Broadcom]] — networking giants tested as a control
- [[NVIDIA]] — AI-compute driver and customer/backer
- [[AI datacenter architecture]], [[Advanced packaging]] — adjacent AI-infrastructure concepts
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

*Created 2026-06-14.*
