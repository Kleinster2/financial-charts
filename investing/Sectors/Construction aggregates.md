---
aliases: [Construction aggregates, Aggregates, Vulcan and Martin Marietta, Crushed stone, Aggregates duopoly]
tags: [sector, materials, construction, aggregates, cluster-validation]
---

# Construction aggregates

> [!success] Cluster status: VALIDATED — a distinct, extraordinarily tight construction-aggregates pair ([[Vulcan Materials|VMC]]+[[Martin Marietta|MLM]]); the duopoly trades apart from the materials ETF, homebuilders, industrials, and the market, and no liquid ETF replicates it (Jun 2026)
> The two dominant US aggregates producers cohere at 0.88 (PC1 94%) — among the tightest pairs in the campaign, and durable at 0.78–0.94 every year since 2019. They are clearly distinct: +0.281 intra-advantage vs the materials ETF [[XLB]], +0.225 vs homebuilders ([[XHB]]), +0.266 vs industrials ([[XLI]]), and +0.448 vs the market. They beat the random-basket null (p 0.0002), form a clean cluster across a WIDE threshold band [0.20–0.40], and the holdout is STABLE 0.96. The distinctness is the [[Cable broadband|index-rule escape]]: [[XLB]] is dominated by chemicals and industrial gases ([[Linde]]/[[Air Products]]/Sherwin-Williams/[[Freeport-McMoRan]]), so it holds the aggregates names but tracks a different factor. A 2-name distinct non-ETF factor — the [[Cable broadband|cable]] / [[Card networks|V+MA]] pattern, but tighter than either. Own the pair; there is no aggregates ETF. See below.

The local-monopoly duopoly. [[Vulcan Materials|Vulcan]] and [[Martin Marietta]] are the two dominant US producers of construction aggregates — crushed stone, sand, and gravel — and the market trades them as one factor because they share one driver: aggregates demand (public infrastructure ~45%, private nonresidential, residential) and the pricing power of a low-value, high-weight product whose economics are local-monopoly (it is uneconomic to truck aggregates far, so each quarry owns its radius). That driver is specific and shared: it is not the chemical/industrial-gas cycle that dominates [[XLB]], not the rate-driven homebuilder cycle of [[XHB]], and not broad industrials. So the pair coheres tightly and stays distinct.

## Sector performance

![[aggregates-performance.png]]
*Normalized total return since 2019 vs the materials ETF [[XLB]] and homebuilders [[XHB]]. [[Vulcan Materials|VMC]] and [[Martin Marietta|MLM]] move almost as one line and compound above both benchmarks — pricing power on a non-discretionary, infrastructure-backed product — while [[XLB]] (chemicals-led) and [[XHB]] (rate-driven) take their own paths. The two aggregates lines overlapping, apart from the ETFs, is the distinct-factor verdict made visible.*

## Cluster validation

The candidate cohort is the US construction-aggregates pair — [[Vulcan Materials|VMC]] and [[Martin Marietta|MLM]] — tested against the materials ETF ([[XLB]] — the key benchmark), homebuilders ([[XHB]], residential-construction demand), broad industrials ([[XLI]]), and the market ([[SPY]]). 1Y window through 2026-06-22 (199 obs); threshold 0.5. A pair test (EXP/SUM/CRH not in the DB), the [[Cable broadband|cable]] / [[Card networks|V/MA]] analogue. Config: `scripts/cluster_configs/aggregates.yaml`; registry row 2026-06-23. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Pair correlation (1Y) | 0.883 | The tightest pair in the campaign's distinct set |
| PC1 explained variance | 94.4% | One factor, near-total |
| Random-basket null p | 0.0002 | Real — 0.88 vs random 2-pick mean 0.14 |
| Holdout (2Y split) | STABLE 0.96 | Durable (train 0.92 → test 0.89) |
| Threshold stable width | 0.20 [0.20–0.40] | WIDE — clean cluster; ETFs contaminate only from 0.45 |
| Intra-adv vs materials ETF ([[XLB]]) | +0.281 | Distinct — XLB is chemicals/gas-ruled (index-rule) |
| Intra-adv vs homebuilders ([[XHB]]) | +0.225 | Distinct from the residential cycle |
| Intra-adv vs industrials ([[XLI]]) | +0.266 | Distinct from broad industrials |
| Intra-adv vs market (SPY) | +0.448 | Among the campaign's largest — idiosyncratic |

### Boundary — one tight cluster apart from the ETFs

![[aggregates-cluster-dendrogram-1y.png]]
*Hierarchical clustering. [[Vulcan Materials|VMC]]+[[Martin Marietta|MLM]] join first and tightest (distance 0.12, corr 0.88); the materials/homebuilder/industrials ETFs and the market join only at the broad-market merge (≥0.45). The pair is its own factor — the ETFs are contaminants, not siblings.*

The threshold scan returns a WIDE stable band [0.20–0.40] (width 0.20): the aggregates pair is a clean, uncontaminated cluster across a broad range of cuts, and [[XLB]]/[[XHB]]/[[XLI]]/[[SPY]] enter only at 0.45. With the large positive intra-advantage over every control, that is the distinct-non-ETF-factor signature.

### Topology

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | VMC + MLM | 0.117 | the aggregates duopoly (corr 0.883) — the only join, and very tight |

### PC1 index weights

![[aggregates-cluster-pca-1y.png]]
*PCA on the pair. PC1 explains 94.4% — almost the entire common variance is one aggregates factor. Loadings are equal (0.707 each), and the two carry near-identical low volatility (~27%) — these are stable, infrastructure-backed compounders, not high-beta names.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| VMC | 0.707 | 50.00% | 27.57% | 49.50% |
| MLM | 0.707 | 50.00% | 27.02% | 50.50% |

### Distinctness — apart from materials, housing, industrials, and the market

![[aggregates-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. [[Vulcan Materials|VMC]]–[[Martin Marietta|MLM]] run very warm (0.88); both are only moderately correlated with [[XLB]]/[[XHB]]/[[XLI]] (0.60–0.66) and cool to the market (0.44).*

The intra-advantages are large and positive against everything: +0.281 vs [[XLB]] (the materials ETF is ruled by chemicals and industrial gases — [[Linde]]/[[Air Products]]/Sherwin-Williams — a different factor, so aggregates sit inside it but do not track it, the [[Analog and auto-industrial semiconductors|index-rule]] escape), +0.225 vs [[XHB]] (aggregates' infrastructure demand is not the rate-driven homebuilder cycle), +0.266 vs [[XLI]], and +0.448 vs the market. No liquid ETF isolates the aggregates pair, so the basket is the only expression.

### Historical tightness evolution

![[aggregates-cluster-rolling-tightness-90d.png]]
*Rolling 90-day pair correlation since 2019 — extraordinarily durable at 0.78–0.94 every single year, one of the most persistent pairs in the campaign. The two aggregates producers move as one factor through every regime (rates, infrastructure cycles, housing), because they sell the same product into the same demand with the same local-monopoly economics.*

| Year | Pair corr | PC1 |
|---|---|---|
| 2019 | 0.782 | 89.1% |
| 2020 | 0.930 | 96.5% |
| 2021 | 0.916 | 95.8% |
| 2022 | 0.938 | 96.9% |
| 2023 | 0.917 | 95.8% |
| 2024 | 0.861 | 93.1% |
| 2025 | 0.902 | 95.1% |
| 2026 | 0.852 | 92.6% |

## Where this sits in the campaign

Construction aggregates is a distinct non-ETF factor of the homogeneous-oligopoly type — the tightest in the campaign's distinct-pair set ([[Cable broadband|cable]] 0.73, [[Card networks|V+MA]] 0.83, aggregates 0.88), and the materials-map counterpart to them. It completes the building-materials map: where [[Building products]] split into HVAC and housing-products sub-cohorts (= XLI + XHB) and [[Industrial distributors]] resolved to XLI, the raw-aggregates duopoly stands apart — because [[XLB]], its only plausible ETF, is ruled by chemicals and industrial gases rather than construction materials. It is the same index-rule escape that let [[Cable broadband|cable]] separate from [[XLC]] the same week, in a sector where the ETF's dominant factor (specialty chemicals) is simply a different business from the cohort's (aggregates).

## Related

- [[Vulcan Materials]], [[Martin Marietta]] — the cohort pair (the US aggregates duopoly)
- [[XLB]] — the materials ETF the pair is distinct from (chemicals/industrial-gas-ruled); [[XHB]] — homebuilders (residential-construction demand); [[XLI]] — broad industrials
- [[Cable broadband]], [[Card networks]] — the same distinct-pair / index-rule-escape pattern; [[Building products]], [[Industrial distributors]] — the ETF-replicable building-materials cohorts this stands apart from
- [[Vault cluster taxonomy]] — cross-cohort meta-analysis; [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-23. 1Y daily log returns through 2026-06-22; config `scripts/cluster_configs/aggregates.yaml`; registry row 2026-06-23. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
