---
aliases: [Managed care, Health insurers, Managed care organizations, MCO cluster, Health insurance cluster]
tags: [concept, cluster-validation, healthcare, health-insurance, managed-care, usa]
---

# Managed care

> [!warning] Cluster status: real but moderate factor, ETF-replicable; regime-dependent (Jun 2026)
> The big diversified US health insurers ([[UnitedHealth|UNH]]/[[Elevance Health|ELV]]/[[Humana|HUM]]/[[CVS Health|CVS]]) form a real managed-care factor — intra-corr 0.53, PC1 63%, rejects the random-basket null at p 0.0009, distinct from Medicaid MCOs (+0.13) and the broad market (+0.12). But it is not a tight, distinct basket: the health-providers ETF IHF sits inside the cluster (ETF-replicable), [[Cigna|CI]] is the PBM-heavy outlier (joins only at 0.58), and cohesion is strongly regime-dependent — it fragmented to 0.40 in 2024–25 and re-tightened to 0.59 in 2026 as the shared sector selloff (DOJ scrutiny, Medicare Advantage rate pressure, elevated medical-loss ratios) bound the names back together. The distinct, robust expression is the UNH/ELV/HUM/CVS core via IHF, not a five-name basket including Cigna.

The health-insurer cohort, and a test of whether a defensive sector coheres through a shared shock. Going in, the question was whether the 2024–25 managed-care crisis — [[UnitedHealth]]'s DOJ probe, the [[Medicare Advantage]] rate squeeze, and the medical-cost spike that blew through every insurer's loss ratio — drove the names apart on company-specific stories or bound them into one factor. The answer is both, sequentially: they decoupled as the problems first surfaced unevenly (2024 intra-corr 0.40), then re-cohered in 2026 (0.59) as the market began trading the whole group as one regulatory-and-medical-cost object. What it is not is a clean, separable basket — the providers ETF IHF is inside the cluster, so the managed-care factor is the ETF, and [[Cigna]], whose Express Scripts PBM dominates its mix, trades as an outlier rather than a core insurer.

## Cluster validation

The candidate cohort is the five big diversified managed-care insurers — [[UnitedHealth|UNH]], [[Elevance Health|ELV]], [[Humana|HUM]], [[Cigna|CI]], [[CVS Health|CVS]] — tested against the Medicaid-focused MCOs (Centene CNC, Molina MOH), and benchmarks (XLV health-care ETF, IHF health-providers ETF, SPY).

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.532 [0.357–0.653] | moderate; weekly 0.506 (synchronous) |
| PC1 explained variance | 63.0% | dominant factor, real substructure (PC2 14.1%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0009 (PC1 0.0015) | rejects — real cohesion, not a random 5-pick |
| Holdout (2Y split) | STABLE 1.08 | cohesion durable, but loadings corr −0.26 — factor structure shifted |
| Threshold clean width | 0.00 | BOUNDARY-DEPENDENT — the CI outlier + IHF inside block a clean isolate |
| Intra-adv vs Medicaid MCOs (CNC/MOH) | +0.131 | distinct — government-program insurers trade on a different factor |
| Intra-adv vs broad ETF/market | +0.124 | distinct from XLV/SPY — but IHF specifically sits inside the cluster |

1Y daily log returns through 2026-06-12, threshold 0.5. All US-listed (synchronous). Config: `scripts/cluster_configs/unh.yaml`; registry row 2026-06-15. Terminology: [[Cohort, cluster, basket]].

### Boundary — four insurers + IHF cluster; Cigna and Medicaid split off

![[managed-care-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. UNH/ELV/HUM/CVS cluster with IHF (the health-providers ETF, green) — the managed-care factor is the ETF. [[Cigna|CI]] is a singleton outlier (joins at 0.58); the Medicaid MCOs CNC/MOH form their own cluster (orange); XLV and SPY sit apart.*

The threshold scan never isolates a clean cohort — IHF is inside the insurer cluster at every cut, and CI only attaches above 0.5. The Medicaid MCOs (Centene/CNC, Molina/MOH) cluster separately, a +0.131 intra-advantage: the government-program insurers trade on their own factor (rate notices, redeterminations, Medicaid expansion) distinct from the diversified commercial-plus-Medicare names. So health insurance is at least two equity factors split by end-market (diversified vs Medicaid), with the diversified core itself = the providers ETF.

### Topology — a UNH/ELV/CVS core, Cigna the outlier

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | UNH + CVS | 0.347 | core pair |
| 2 | ELV + (UNH+CVS) | 0.399 | Elevance joins the core |
| 3 | HUM + (ELV+UNH+CVS) | 0.408 | Humana joins |
| 4 | CI + (HUM+ELV+UNH+CVS) | 0.578 | Cigna the outlier — above the 0.5 cut |

The four diversified insurers join below 0.41; [[Cigna]] joins only at 0.578 and has the lowest PC1 loading (0.365 vs ~0.46–0.48 for the rest). Its Express Scripts PBM and smaller direct-insurance book give it a different return mix — it is in the managed-care neighborhood but not in the tight core.

### PC1 index weights

![[managed-care-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 63.0% with a meaningful PC2 (14.1%) — the secondary axis is the Cigna outlier and the high-vol Humana.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| UnitedHealth (UNH) | 0.480 | 21.5% | 41.4% | 20.2% |
| Elevance (ELV) | 0.463 | 20.8% | 38.8% | 20.8% |
| Humana (HUM) | 0.456 | 20.5% | 50.8% | 15.7% |
| CVS Health (CVS) | 0.463 | 20.8% | 32.5% | 24.9% |
| Cigna (CI) | 0.365 | 16.4% | 34.7% | 18.4% |

The four core insurers carry near-equal PC1 loadings; the high-vol [[Humana]] (50.8% — the Medicare Advantage exposure) takes the smallest raw PC1-mimic weight, the lower-vol [[CVS Health]] the largest. [[Cigna]]'s low loading marks it as the outlier.

### Distinctness — = IHF, distinct from Medicaid and broad health

![[managed-care-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The UNH/ELV/HUM/CVS block is warm and just as warm against IHF; Cigna is cooler against the core; the Medicaid MCOs (CNC/MOH) form a separate warm cell.*

The cohort rejects the random-basket null (p 0.0009) and is distinct from the Medicaid MCOs (+0.131) and the broad market (+0.124 vs XLV/SPY) — a real, distinct managed-care factor. But the health-providers ETF IHF is inside the cluster, so the factor is ETF-replicable: own IHF for managed-care exposure rather than a hand-built five-name basket, and note that IHF concentrates the same UNH/ELV/HUM/CVS names. Picking [[UnitedHealth]] over [[Elevance Health]] is a company bet (Optum, the DOJ overhang) on top of the shared factor.

### Historical tightness evolution

![[managed-care-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Tight in 2020 (0.78), eroded through 2021–23, fragmented hard in 2024–25 (0.40) as company-specific problems surfaced unevenly, then re-tightened to 0.59 in 2026 as the sector selloff bound the names back together.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.777 | 82.5% |
| 2021 | 0.641 | 72.6% |
| 2022 | 0.592 | 67.7% |
| 2023 | 0.645 | 72.3% |
| 2024 | 0.401 | 52.9% |
| 2025 | 0.415 | 53.7% |
| 2026 | 0.591 | 68.2% |

The regime-dependence is the story: managed care is not a structurally permanent factor like homebuilders or airlines, but a sometimes-factor that tightens when a common shock dominates (the 2020 COVID-deferral trade, the 2025–26 regulatory/medical-cost selloff) and fragments when each insurer trades its own book (2024–25). The 2026 re-cohesion answers the question the cohort was built for — yes, the shared selloff bound them — but the holdout's negative loadings correlation (−0.26) warns that the factor's internal structure reshuffled across the regime, so it is a moderate, conditional cluster, not a durable one.

## Related

- [[UnitedHealth]], [[Elevance Health]], [[Humana]], [[CVS Health]] — the diversified core
- [[Cigna]] — the PBM-heavy outlier
- [[Healthcare]] — the broad sector hub
- [[Medicare Advantage]] — the shared rate/medical-cost driver
- [[DTC Telehealth]] — an adjacent (falsified) health cohort
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis

---

*Created 2026-06-15. 1Y daily log returns through 2026-06-12; config `scripts/cluster_configs/unh.yaml`; registry row 2026-06-15. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
