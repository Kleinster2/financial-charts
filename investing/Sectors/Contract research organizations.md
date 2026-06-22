---
aliases: [Contract research organizations, CROs, CRO cohort, Clinical research organizations, Pharma R&D services]
tags: [sector, healthcare, cro, pharma-services, cluster-validation]
---

# Contract research organizations

> [!warning] Cluster status: NOT a standalone factor — the cohort shatters; the large CROs are absorbed into life-science tools, the small ones are singletons (Jun 2026)
> The listed CROs ([[IQVIA|IQV]]/[[ICON plc|ICLR]]/[[Charles River Laboratories|CRL]]/[[Medpace|MEDP]]) do not hold together as a factor. Intra-corr is loose (0.529 daily, 0.683 weekly — async-depressed, [[ICON plc|ICON]] is Dublin-listed), PC1 65%, and the cohort beats the random-basket and vol-matched nulls only weakly (p 0.0010 / 0.0003) via shared pharma-R&D-services beta. The decisive numbers: a ~zero +0.021 intra-advantage versus the [[Life science tools]] complex ([[Thermo Fisher Scientific|TMO]]/[[Danaher|DHR]]/[[Agilent|A]]) and zero clean threshold width — at the 0.50 cut the cohort SHATTERS: [[IQVIA|IQV]]+[[Charles River Laboratories|CRL]] (the only tight pair, 0.74) merge with the life-science tools, while [[ICON plc|ICLR]] and [[Medpace|MEDP]] are idiosyncratic singletons (the tools contaminate from threshold 0.40). So "CROs" is not a distinct factor: the large CROs belong to the [[Life science tools|pharma-picks-and-shovels]] factor that already exists, and the smaller, biotech-funding-levered names trade on their own. Holdout WEAKENED (0.77, loadings corr 0.33). Own [[Life science tools]] for the services exposure; there is no separable CRO factor. See below.

The healthcare set's pattern holds. Across the campaign the healthcare label is a near-clean sweep of non-distinctness — [[Pharma majors|pharma]], [[GLP-1 receptor agonists|GLP-1]], [[Medtech]], [[DTC Telehealth]], and [[Biotech]] all resolve to their ETF or shatter — with exactly two exceptions, both services/supply-chain cohorts: [[Life science tools]] (distinct, +0.172) and [[Drug distributors]] (distinct, +0.502). CROs were the next picks-and-shovels candidate, sharing the pharma-R&D-budget and biotech-funding driver. They do not earn a third distinct factor. The coherent part of the cohort is real but it is the same factor life-science tools already captures; the rest is single-stock idiosyncrasy.

## Sector performance

![[cro-performance.png]]
*Normalized total return since Jan 2023 — the cohort vs [[XLV]] (the sector ETF it is tested against). See the cluster validation below for whether the cohort is distinct from or replicable by the ETF.*

## Cluster validation

The candidate cohort is four US/Ireland-listed CROs — [[IQVIA|IQV]], [[ICON plc|ICLR]], [[Charles River Laboratories|CRL]], [[Medpace|MEDP]] — tested against the life-science tools ([[Thermo Fisher Scientific|TMO]]/[[Danaher|DHR]]/[[Agilent|A]]), the healthcare ETFs ([[XLV]]/IHI/[[XBI]], the last proxying biotech-funding demand), and the market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.529 [0.317–0.735] | Loose; weekly 0.683 (async-depressed — ICON Dublin-listed) |
| PC1 explained variance | 65.2% | A weak single factor (weekly 76.3%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0010 | Beats a random 4-pick only weakly (null mean 0.151, 99th 0.409) |
| Vol-matched null p (10k) | 0.0003 | Weakly beyond shared vol — via pharma-services beta |
| Holdout (2Y split) | WEAKENED 0.77 | train 0.689 → test 0.529; loadings corr 0.33 (eroding, unstable) |
| Threshold clean width | 0.00 | Life-science tools contaminate from 0.40 — never isolates |
| Intra-adv vs life-science tools (TMO/DHR/A) | +0.021 | ≈ZERO — the coherent CROs ARE the tools complex |
| Intra-adv vs healthcare ETFs (XLV/IHI/XBI) | +0.185 | Above broad healthcare — but via the tools factor, not its own |
| Intra-adv vs market (SPY) | +0.179 | Not market beta |

Config: `scripts/cluster_configs/cro_cdmo.yaml`; registry row 2026-06-20.

### Boundary — the cohort shatters; the large CROs join life-science tools

![[cro-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The cohort does not form one cluster: [[IQVIA|IQV]] and [[Charles River Laboratories|CRL]] cluster WITH the life-science tools ([[Thermo Fisher Scientific|TMO]]/[[Danaher|DHR]]/[[Agilent|A]]); [[ICON plc|ICLR]] and [[Medpace|MEDP]] are each singletons; the healthcare ETFs (XLV/IHI) and XBI/SPY form their own groups. The CRO label spans a tools-adjacent core and two idiosyncratic names.*

The threshold scan returns zero clean width — the contamination order shows what the CROs cannot be separated from:

| Threshold | Joins the cohort cluster | Read |
|---|---|---|
| 0.40 | TMO, DHR, A | the life-science tools — the large CROs merge with them early |
| 0.55 | + XLV, IHI | broad healthcare joins |
| 0.60+ | + more | the healthcare complex |

Life-science tools contaminating at 0.40 (below the 0.50 cut) is the signature: the coherent part of the CRO cohort is not separable from the tools factor. And the full four-name cohort never forms a clean cluster anyway — [[ICON plc|ICLR]] joins only at 0.555, above the cut.

### Topology — one tools-adjacent pair, two singletons

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | IQV + CRL | 0.265 | the only tight CRO pair (corr 0.74) — and both join life-science tools |
| 2 | MEDP + (IQV+CRL) | 0.448 | Medpace joins loosely |
| 3 | ICLR + core | 0.555 | ICON joins only above the 0.50 cut — a singleton |

The only real internal structure is the [[IQVIA|IQV]]+[[Charles River Laboratories|CRL]] pair (0.74) — the two largest, most diversified CROs, which are also the two that merge with life-science tools. [[ICON plc|ICLR]] (high-vol, 79% annualized, after a sharp 2024-25 CRO-funding drawdown) and [[Medpace|MEDP]] (small/mid-cap biotech-client concentration) trade on their own. PC1 explains only 65%.

### PC1 index weights

![[cro-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains only 65.2% (weekly 76.3%) — a weak factor with a large residual. [[IQVIA|IQV]]/[[Charles River Laboratories|CRL]] carry the high loadings; [[ICON plc|ICLR]] loads lowest, consistent with its singleton status.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| IQV | 0.550 | 27.6% | 39.9% | 33.7% |
| ICLR | 0.437 | 22.0% | 79.3% | 13.4% |
| CRL | 0.542 | 27.3% | 45.0% | 29.4% |
| MEDP | 0.461 | 23.2% | 47.8% | 23.5% |

[[ICON plc|ICLR]]'s 79% annualized vol (a violent 2024-25 drawdown on CRO/biotech-funding weakness) is the highest in the cohort and its loading the lowest — the mark of an idiosyncratic name, not a factor member.

### Distinctness — absorbed into life-science tools

![[cro-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. Only IQV/CRL is a warm pair; ICLR and MEDP are cool against everything — and the IQV/CRL pair is about as warm against the life-science tools (TMO/DHR/A) as against each other.*

The intra-advantage numbers make the verdict quantitative: +0.021 versus life-science tools (≈zero — the CROs are the tools complex), +0.185 versus the healthcare ETFs, +0.179 versus the market. A distinct CRO factor would show a clearly positive advantage versus the tools; +0.021 says the coherent CROs ([[IQVIA|IQV]]/[[Charles River Laboratories|CRL]]) belong to the same pharma-R&D-services factor that [[Life science tools]] already represents. The "CRO" label adds a slightly broader membership to that factor, not a new one — and the two smaller names are single-stock stories. Own [[Life science tools]] for the pharma-services exposure.

### Historical tightness evolution

![[cro-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Persistently loose-to-moderate (0.47–0.65) — never a tight cluster in any year, peaking only at 0.65 in the 2022-23 pharma-services window and back to 0.52 in 2026. A label, not a factor.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.469 | 60.7% |
| 2022 | 0.623 | 71.9% |
| 2023 | 0.646 | 73.7% |
| 2024 | 0.596 | 70.0% |
| 2025 | 0.631 | 73.0% |
| 2026 | 0.524 | 64.7% |

*Never tight in any year — unlike the durable distinct factors (which sit at 0.7–0.9). The 2024-25 CRO downturn (biotech-funding drought, pharma R&D cuts) widened the dispersion further, with [[ICON plc|ICLR]] in particular detaching. Holdout WEAKENED (0.77).*

## Related

- [[Life science tools]] — the distinct pharma-picks-and-shovels factor the large CROs are absorbed into (+0.021, the decisive number)
- [[Drug distributors]] — the other distinct healthcare services factor; CROs reach neither's bar
- [[IQVIA]], [[ICON plc]], [[Charles River Laboratories]], [[Medpace]] — the cohort members
- [[XBI]] — biotech ETF; the CRO demand driver (biotech funding)
- [[Biotech]], [[Pharma majors]], [[Medtech]], [[GLP-1 receptor agonists]], [[DTC Telehealth]] — the rest of the non-distinct healthcare set
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/cro_cdmo.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
