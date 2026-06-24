---
aliases: [Infrastructure construction, AI buildout contractors, Datacenter contractors, Buildout contractors, Infrastructure contractors]
tags: [sector, industrials, construction, infrastructure, data-center, cluster-validation]
---

# Infrastructure construction

> [!warning] Cluster status: validated cohesion but ETF-replicable (= the infrastructure ETF PAVE) — the AI-buildout contractors cohere, and are sharply distinct from the broad engineering/EPC firms, but the infrastructure ETF captures them; a recently-formed, buildout-driven cohort (Jun 2026)
> The specialty data-center / grid contractors — [[Quanta Services|PWR]], [[EMCOR|EME]], [[Comfort Systems|FIX]], [[MasTec|MTZ]], [[Sterling Infrastructure|STRL]] (ex the diversified outlier [[Primoris|PRIM]]) — cohere tightly (ex-PRIM intra 0.717, PC1 ~68%) and beat the random-basket null at p 0.00025. The standout finding is the specialty-vs-EPC split: +0.395 intra-advantage vs the big engineering/EPC firms (AECOM/Fluor/Jacobs) — the inside-the-building electrical/mechanical and power-delivery trade is a different business from project-based EPC. But the cohort is ETF-replicable: it carries only +0.053 vs the infrastructure ETF PAVE (which holds these names) and +0.111 vs broad industrials [[XLI]] — PAVE/XLI contaminate the cluster from threshold 0.40. And the cohesion is recent: rolling tightness jumped from ~0.6 to 0.75 in 2025 as the data-center and grid buildout pulled the names together, with the holdout WEAKENED (loadings-corr 0.26) — a buildout-era cohort, not a durable structural factor. [[Primoris|PRIM]] (renewables-EPC/gas) decouples. Own PAVE. See below.

The AI-buildout construction trade. The data-center and grid-electrification capex wave has been one of the biggest 2024–26 equity themes, and the listed beneficiaries are the specialty trade contractors: [[Quanta Services|Quanta]] (electric T&D, grid, data centers), [[EMCOR]] (data-center electrical/mechanical), [[Comfort Systems]] (data-center cooling/HVAC), [[MasTec]] (power delivery), and [[Sterling Infrastructure|Sterling]] (data-center sitework) — several of which compounded 5–10x. They share a driver (hyperscale + grid construction demand) that the market has repriced sharply, but it is the same driver the infrastructure ETF PAVE is built on, so the cohort resolves to PAVE rather than standing apart as its own factor.

## Sector performance

![[infra-build-performance.png]]
*Normalized total return since 2019 vs the infrastructure ETF PAVE. The buildout contractors ([[Quanta Services|PWR]]/[[EMCOR|EME]]/[[Comfort Systems|FIX]]/[[MasTec|MTZ]]/[[Sterling Infrastructure|STRL]]) take off together from 2023–24 as data-center and grid capex accelerates — several 5–10x — with PAVE (which holds them) riding the same wave at lower amplitude. The shared, recently-amplified buildout driver is the cohesion; that it is the same driver PAVE prices is the ETF-replicable verdict.*

## Cluster validation

The candidate cohort is the six listed AI-buildout / infrastructure contractors — [[Quanta Services|PWR]], [[EMCOR|EME]], [[Comfort Systems|FIX]], [[MasTec|MTZ]], [[Sterling Infrastructure|STRL]], [[Primoris|PRIM]] — tested against the broad engineering/EPC firms (AECOM/Fluor/Jacobs), the infrastructure ETF (PAVE), broad industrials ([[XLI]]), and the market ([[SPY]]). 1Y window through 2026-06-22 (199 obs); threshold 0.5. Tickers ingested 2026-06-24. Config: `scripts/cluster_configs/infra_build.yaml`; registry row 2026-06-24. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-corr (1Y) | 0.589 (6-name) / 0.717 (ex-PRIM core) | Tight core; [[Primoris\|PRIM]] the drag |
| PC1 explained variance | 67.6% | One buildout factor |
| Random-basket null p | 0.00025 | Real, strong co-movement |
| Holdout (2Y split) | WEAKENED 0.72, loadings-corr 0.26 | Cohesion is recent / unstable structure |
| Threshold stable width | 0.00 | PAVE/[[XLI]]/[[SPY]] contaminate from 0.40 |
| Intra-adv vs broad EPC (AECOM/Fluor/Jacobs) | +0.288 (6-name) / +0.395 (ex-PRIM) | Sharp — specialty contractors ≠ EPC firms |
| Intra-adv vs infra ETF (PAVE) | +0.000 / +0.053 | = the infrastructure ETF |
| Intra-adv vs industrials ([[XLI]]) | +0.055 / +0.111 | ≈ / marginal vs broad industrials |
| Intra-adv vs market (SPY) | +0.108 / +0.178 | Distinct from the market, not from infra/industrials |

### Boundary — distinct from EPC, captured by the infrastructure ETF

![[infra-build-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. The buildout contractors [[Quanta Services|PWR]]/[[EMCOR|EME]]/[[Comfort Systems|FIX]]/[[MasTec|MTZ]]/[[Sterling Infrastructure|STRL]] cluster with the infrastructure ETF PAVE, broad industrials [[XLI]], and [[SPY]] (one infra/industrials block), while the big engineering firms AECOM/Jacobs form their own pair and [[Primoris|PRIM]] is a singleton. The cohort separates cleanly from broad EPC but not from PAVE/XLI, which contaminate from 0.40.*

The threshold scan returns no clean band — PAVE and [[XLI]] enter from 0.40, and the cohort's intra-advantage over PAVE is essentially zero. The infrastructure ETF is ruled by the same buildout/industrial-capex factor as its holdings, so the cohort collapses into it (the [[Factory automation|automation = XLI]] / [[Precious metals royalties|gold-royalties = GDX]] index-rule case). What it IS distinct from is the broad EPC engineering model (AECOM/Fluor/Jacobs, +0.395) — a real specialty-trade-vs-EPC split.

### Topology — a tight contractor core plus a diversified decoupler

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | PWR + MTZ | 0.183 | the power-infrastructure pair (corr 0.82) |
| 2 | FIX + (PWR+MTZ) | 0.204 | [[Comfort Systems\|FIX]] (mechanical) joins the tight core |
| 3 | EME + core | 0.294 | [[EMCOR\|EME]] (electrical) joins |
| 4 | STRL + core | ~0.34 | [[Sterling Infrastructure\|STRL]] (sitework) attaches |
| 5 | PRIM + core | ~0.66 | [[Primoris\|PRIM]] joins last, far out — the decoupler |

The cohesion lives in the five datacenter/grid contractors ([[Quanta Services|PWR]]/[[EMCOR|EME]]/[[Comfort Systems|FIX]]/[[MasTec|MTZ]]/[[Sterling Infrastructure|STRL]], ex-PRIM intra 0.717). [[Primoris|PRIM]] (renewables-EPC/gas, the most diversified) is the decoupler at 0.26–0.40. Dropping PRIM lifts the intra-advantage vs the broad EPC firms to +0.395 and vs [[XLI]] to +0.111 — but still only +0.053 vs PAVE, so even the clean core is captured by the infrastructure ETF.

### PC1 index weights

![[infra-build-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 67.6%; [[Quanta Services|PWR]]/[[EMCOR|EME]]/[[Comfort Systems|FIX]]/[[MasTec|MTZ]] load evenly (~0.42–0.46), [[Sterling Infrastructure|STRL]] high-vol (83%), [[Primoris|PRIM]] lowest (0.239, vol 96% — the decoupler).*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| PWR | 0.440 | 18.28% | 40.08% | 23.04% |
| EME | 0.421 | 17.50% | 41.54% | 21.29% |
| FIX | 0.457 | 19.00% | 53.23% | 18.03% |
| MTZ | 0.448 | 18.60% | 42.19% | 22.29% |
| STRL | 0.403 | 16.72% | 83.27% | 10.15% |
| PRIM | 0.239 | 9.91% | 96.26% | 5.20% |

### Distinctness — the specialty-vs-EPC split, but = the infra ETF

![[infra-build-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. The core five run 0.64–0.82; [[Primoris|PRIM]] is cool to all (0.26–0.40). The cohort is warm to the infrastructure ETF PAVE (≈0.59) — about as warm as to itself.*

The two numbers that frame the verdict: +0.395 (ex-PRIM) vs the broad EPC firms — the inside-the-building electrical/mechanical and power-delivery contractors are genuinely a different business from project-based engineering/EPC — and +0.053 vs PAVE — the infrastructure ETF that holds them captures the factor. So there is a real "buildout contractor" structure, distinct from broad E&C, but it is the infrastructure ETF's structure; the bespoke basket adds little over owning PAVE.

### Historical tightness evolution — a buildout-era cohort

![[infra-build-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion since 2019. Moderate (~0.6) through 2020–23, a dip to 0.43 in 2024, then a jump to 0.75 in 2025–26 as the data-center and grid buildout pulled the contractors together. The cohesion is a recent, demand-shock phenomenon — like [[Rare earth equity beta|rare earths]], a cohort amplified by a specific 2024–26 capex wave rather than a durable structural factor (hence the WEAKENED holdout and low loadings-corr).*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2020 | 0.618 | 68.3% |
| 2021 | 0.649 | 70.9% |
| 2022 | 0.608 | 67.6% |
| 2023 | 0.623 | 68.8% |
| 2024 | 0.426 | 52.8% |
| 2025 | 0.752 | 79.4% |
| 2026 | 0.713 | 76.4% |

## Where this sits in the campaign

Infrastructure construction is a Tier-2 ETF-replicable cohort (= PAVE) with a real sub-structure: a tight datacenter/grid contractor core sharply distinct from the broad EPC firms (+0.395), but captured by the infrastructure ETF. It pairs with the same week's [[Factory automation]] as the second "industrial-capex theme that resolves to its ETF" — automation to [[XLI]], buildout contractors to PAVE — both confirming that a real demand wave (reshoring/AI) does not automatically mint a distinct factor when a liquid ETF prices the same wave. It also adds a [[Rare earth equity beta|shock-born]] note: the cohesion is a 2024–26 buildout-era amplification, not a through-cycle structure. The ownable distinction is narrow — the specialty-contractor model versus broad EPC — and PAVE expresses the theme.

## Related

- [[Quanta Services]], [[EMCOR]], [[Comfort Systems]], [[MasTec]], [[Sterling Infrastructure]] — the tight buildout-contractor core; [[Primoris]] — the diversified decoupler
- [[Data Centers]] — the demand driver; [[Power constraints]] — the grid-electrification driver
- [[XLI]] — broad industrials (the cohort is only marginally distinct from it); [[Factory automation]] — the same-week industrial-capex-theme-resolves-to-its-ETF parallel
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-24. 1Y daily log returns through 2026-06-22; config `scripts/cluster_configs/infra_build.yaml`; registry row 2026-06-24. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
