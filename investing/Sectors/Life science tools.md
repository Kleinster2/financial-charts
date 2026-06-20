---
aliases: [Life science tools, Life sciences tools, Tools and diagnostics, Life science tools cluster, Bioprocessing tools]
tags: [sector, healthcare, life-science-tools, cluster-validation]
---

# Life science tools

> [!success] Cluster status: VALIDATED — a durable, distinct life-science-tools factor, separate from broad healthcare and medical devices; narrowly bounded (Jun 2026)
> The life-science tools and diagnostics names ([[Thermo Fisher Scientific|TMO]]/[[Danaher|DHR]]/[[Agilent|A]]/[[Mettler-Toledo|MTD]]/[[Waters|WAT]]/[[IQVIA|IQV]]/[[Revvity|RVTY]]) trade as one factor — intra-corr 0.620 (PC1 67.6%), rejecting the random-basket and vol-matched nulls at the 0.0001 floor, and the 2Y holdout is STABLE (ratio 0.89, durable across regimes). All seven cluster together with a +0.172 intra-advantage versus the healthcare and medical-device ETFs ([[XLV]]/IHI) — so the cohort is distinct from broad healthcare beta AND from medtech: it is its own bioprocessing / lab-instrument / pharma-R&D-capex factor. Unlike [[Solid waste|waste]] (a wide separable band), the separable threshold here is narrow (clean at the 0.50 cut, not across a band) — below 0.50 it splits into instruments vs CRO/diagnostics sub-pairs, above 0.50 healthcare contaminates — so it is a real distinct factor but a narrowly-bounded one. There is no liquid pure-tools ETF; own the basket for the factor XLV does not isolate.

The picks-and-shovels of biopharma. These companies sell the instruments, consumables, reagents, and outsourced research that every drug developer and lab consumes — so they share one dominant driver: pharma and biotech R&D budgets and lab capex, plus a large recurring-consumables base. That driver is distinct from the drug-and-device demand that moves broad healthcare ([[XLV]]) and medical devices (IHI), which is why the cohort separates from both — and why it behaves as a single, durable factor through cycles.

## Cluster validation

The candidate cohort is seven life-science tools and diagnostics names — [[Thermo Fisher Scientific|TMO]], [[Danaher|DHR]], [[Agilent|A]], [[Mettler-Toledo|MTD]], [[Waters|WAT]], [[IQVIA|IQV]], [[Revvity|RVTY]] — tested against healthcare (XLV), medical devices (IHI), and market (SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.620 [0.459–0.739] | above the 0.50 floor; weekly 0.581 |
| PC1 explained variance | 67.6% | dominant single factor (weekly 64.8%) |
| Independence null p | 0.0001 | series co-move |
| Random-basket null p | 0.0001 | real cohesion beyond a random 7-pick |
| Vol-matched null p | 0.0001 / 0.0001 | cohesion exceeds vol-matched baskets — a real factor |
| Holdout (2Y split) | STABLE 0.89 | train 0.697 → test 0.620 — durable across regimes |
| Threshold stable width | 0.00 [0.50 point] | distinct at the cut but a narrow band, not a wide island |
| Intra-adv vs ETFs (XLV/IHI/SPY) | +0.172 | distinct from broad healthcare AND medical devices |

All US-listed. Config: `scripts/cluster_configs/tmo.yaml`; registry row 2026-06-20.

### Boundary — all seven cluster; healthcare and medtech ETFs sit apart

![[lst-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. All seven tools/diagnostics names ([[Thermo Fisher Scientific|TMO]]/[[Danaher|DHR]]/[[Agilent|A]]/[[Mettler-Toledo|MTD]]/[[Waters|WAT]]/[[IQVIA|IQV]]/[[Revvity|RVTY]]) form one cluster; the healthcare ETF [[XLV]] and medical-device ETF IHI cluster together separately, and SPY is its own node. The cohort is on the right side of the boundary from broad healthcare — a distinct factor — though only at this cut (the band is narrow).*

The threshold scan returns the cohort clean only at the 0.50 cut (zero stable width): below it, the cohort resolves into an instruments core (TMO/DHR/A/MTD/WAT) and a CRO/diagnostics pair (IQV/RVTY); above it, XLV/IHI contaminate. So the factor is real and durable but narrowly separable — distinct from healthcare/medtech at the natural cut, without the wide robust band that [[Solid waste|waste]] or [[Railroads|railroads]] show. The decisive distinctness evidence is the +0.172 intra-advantage versus the ETFs and the STABLE holdout, not threshold width.

### Topology — an instruments core plus a CRO/diagnostics pair

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | TMO + DHR | 0.261 | the two diversified-tools giants — the core |
| 2 | A + (TMO+DHR) | 0.312 | Agilent joins |
| 3 | MTD + core | 0.349 | Mettler-Toledo joins |
| 4 | IQV + RVTY | 0.363 | the CRO/diagnostics pair forms separately |
| 5 | instruments core + (IQV+RVTY) | 0.401 | the two sleeves merge |
| 6 | WAT + all | 0.450 | the highest-vol name joins last |

The cohort closes at 0.450 — a tight seven-name cluster — with a mild internal split between the instruments core (TMO/DHR/A/MTD/WAT) and the CRO/diagnostics pair (IQV/RVTY). PC1 explains 67.6% with near-uniform loadings, the signature of a genuine shared factor.

### PC1 index weights

![[lst-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 67.6% (weekly 64.8%) — a dominant common factor (pharma-R&D/lab-capex).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| TMO | 0.409 | 15.5% | 30.5% | 17.5% |
| DHR | 0.383 | 14.5% | 28.0% | 17.9% |
| A | 0.401 | 15.2% | 33.6% | 15.6% |
| MTD | 0.361 | 13.7% | 33.8% | 14.0% |
| WAT | 0.345 | 13.1% | 41.5% | 10.9% |
| IQV | 0.361 | 13.7% | 39.9% | 11.8% |
| RVTY | 0.380 | 14.4% | 40.0% | 12.4% |

Near-uniform loadings (~0.35–0.41) confirm a single shared factor; the lower-vol diversified names ([[Thermo Fisher Scientific|TMO]]/[[Danaher|DHR]]) carry the highest inverse-vol weights.

### Distinctness — distinct from both healthcare and medical devices

![[lst-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A warm seven-name tools block; XLV/IHI are cooler against the names than the names are against each other.*

The +0.172 intra-advantage versus the ETFs is the verdict: the tools names track each other more than they track broad healthcare ([[XLV]]) or medical devices (IHI), so the cohort is a distinct sub-sector factor — not healthcare beta and not medtech. The mechanism is the shared pharma-R&D-budget and lab-capex driver, with a large recurring-consumables base, which is specific to the tools complex. Because no liquid ETF isolates this factor (XLV is far broader, IHI is devices), the basket is the only clean expression.

### Historical tightness evolution

![[lst-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2020–2026. Durably tight (0.51–0.72), peaking in the 2022–23 and 2025 pharma-capex/rate regimes; never breaking down.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.606 | 66.5% |
| 2021 | 0.514 | 58.9% |
| 2022 | 0.714 | 75.7% |
| 2023 | 0.720 | 76.3% |
| 2024 | 0.615 | 67.6% |
| 2025 | 0.720 | 76.2% |
| 2026 | 0.600 | 66.4% |

Latest 90-day reading: intra 0.623, PC1 67.9%. The factor is durable — intra never falls below 0.51 in seven years and the holdout is STABLE (0.89) — tightening in pharma-capex/rate regimes (2022–23, 2025) and easing modestly otherwise, but always a coherent factor. A real, ownable life-science-tools factor; less robustly separable at the boundary than [[Solid waste|waste]], but more durable through time.

## Related

- [[Solid waste]], [[Railroads]], [[Tobacco majors basket]] — the other distinct, non-ETF-replicable factors in the campaign
- [[Thermo Fisher Scientific]], [[Danaher]] — the diversified-tools core
- [[Agilent]], [[Mettler-Toledo]], [[Waters]] — the instruments names
- [[IQVIA]], [[Revvity]] — the CRO/diagnostics sleeve
- [[Biotech]], [[Pharma majors]] — the demand side (R&D budgets) the tools sell into
- [[XLV]] — the healthcare ETF the cohort is distinct from
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/tmo.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
