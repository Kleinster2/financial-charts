---
aliases: [Fertilizer producers, Fertilizers, Fertilizer makers, Ag inputs, Nutrient producers, Fertilizer cohort]
tags: [sector, materials, fertilizer, agriculture, cluster-validation]
---

# Fertilizer producers

> [!warning] Cluster status: NOT a distinct factor — a loose, shock-dependent cohort that splits (Mosaic defects); the factor structure is unstable (Jun 2026)
> The fertilizer nutrient producers ([[Nutrien|NTR]]/[[Mosaic|MOS]]/[[CF Industries|CF]]/[[Intrepid Potash|IPI]]) do not hold as a clean factor. Intra-corr is loose (0.575, weekly 0.549), PC1 68%, and the cohort beats the random-basket and vol-matched nulls only weakly (p 0.0005) via shared ag/fertilizer beta. The decisive diagnostics: zero clean threshold width — [[Mosaic|MOS]] defects (loads lowest at 0.439, joins only at 0.511, clustering with the broad agribusiness ETF [[MOO]], seeds ([[Corteva|CTVA]]), and materials instead of the nutrient core) — and a NEGATIVE PC1-loadings correlation across the 2Y holdout split (−0.37), meaning the factor structure inverts between regimes (the automated "STABLE 0.87" intra-ratio label is contradicted by it). The cohort is modestly distinct from the broad market (+0.423) and the agribusiness ETF (+0.283), but it is too loose, shock-dependent, and unstable to be an ownable factor. Two structural notes: the fertilizer equities are NOT the crop-commodity trade ([[DBA]], the ag-futures basket, sits off on its own), and cohesion is shock-dependent (tight 0.77 in the 2022-23 Russia/Ukraine fertilizer-price spike, ~0.55-0.62 otherwise). See below.

The multi-nutrient label that doesn't cohere. The premise was a commodity-beta test in a multi-commodity setting — the steel+aluminum shape — asking whether the nutrient producers form one "fertilizer" factor or split by nutrient (potash NTR/MOS/IPI, nitrogen CF, phosphate MOS). The answer is messier than steel/aluminum: there is a moderate [[Nutrien|NTR]]/[[CF Industries|CF]]/[[Intrepid Potash|IPI]] core (~0.65), but [[Mosaic|MOS]] — the most phosphate- and ag-commodity-levered name — defects to the broad agribusiness/materials group, and the whole thing is loose and regime-unstable. Fertilizer is a cyclical ag-input complex that tightens when nutrient prices spike and disperses otherwise, not a durable standalone factor.

## Cluster validation

The candidate cohort is four fertilizer nutrient producers — [[Nutrien|NTR]], [[Mosaic|MOS]], [[CF Industries|CF]], [[Intrepid Potash|IPI]] — tested against seeds/crop-protection ([[Corteva|CTVA]]), the agribusiness ETF + ag-commodity basket ([[MOO]]/[[DBA]]), and materials/market ([[XLB]]/SPY). 1Y window through 2026-06-18, threshold 0.5. Terminology: [[Cohort, cluster, basket]].

### Diagnostics summary

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster corr (1Y) | 0.575 [0.397–0.678] | Loose; weekly 0.549; MOS the loose member |
| PC1 explained variance | 68.4% | A weak-to-moderate factor (weekly 66.7%) |
| Independence null p (10k) | 0.0001 | Series co-move |
| Random-basket null p (10k) | 0.0005 | Beats a random 4-pick only weakly (via ag/fertilizer beta) |
| Vol-matched null p (10k) | 0.0005 | Weakly beyond shared vol |
| Holdout (2Y split) | UNSTABLE | intra ratio 0.87 ("STABLE") but loadings corr −0.37 (structure inverts) |
| Threshold clean width | 0.00 | MOS defects — never a clean 4-name cluster |
| Intra-adv vs seeds (CTVA) | +0.145 | Distinct from seeds/crop-chem (a different model) |
| Intra-adv vs ag ETF (MOO/DBA) | +0.283 | Above the broad agribusiness ETF — but the cohort is loose |
| Intra-adv vs materials/market (XLB/SPY) | +0.423 | Not market beta |

Config: `scripts/cluster_configs/fertilizers.yaml`; registry row 2026-06-20.

### Boundary — Mosaic defects; the nutrient core never isolates cleanly

![[fertilizers-cluster-dendrogram-1y.png]]
*Hierarchical clustering at 0.5. [[Nutrien|NTR]]/[[CF Industries|CF]]/[[Intrepid Potash|IPI]] form one cluster, but [[Mosaic|MOS]] defects — it clusters with [[Corteva|CTVA]] (seeds), [[MOO]] (agribusiness ETF), and [[XLB]] (materials) instead. The ag-commodity basket [[DBA]] sits on its own, and SPY separately: the fertilizer equities are neither one tight cohort nor the crop-price trade.*

The threshold scan returns zero clean width — the four-name cohort never forms a single uncontaminated cluster, because [[Mosaic|MOS]] joins only at 0.511 (above the cut), and above that the broad agribusiness/materials names (CTVA/MOO/XLB) merge in at 0.65. There is no threshold at which the four nutrient producers stand alone together.

### Topology — a nitrogen+potash core, Mosaic the defector

Reading the candidate cohort by join distance (average linkage, 1−|corr|):

| Join step | Names | Distance (1-\|corr\|) | Read |
|---|---|---|---|
| 1 | CF + IPI | 0.322 | nitrogen + small-cap potash (corr 0.68) |
| 2 | NTR + (CF+IPI) | 0.349 | Nutrien joins — the moderate core closes |
| 3 | MOS + core | 0.511 | Mosaic joins only above the 0.5 cut — the defector |

The [[Nutrien|NTR]]/[[CF Industries|CF]]/[[Intrepid Potash|IPI]] core closes at 0.349 (a moderate ~0.65 cohesion — not the 0.7+ of a distinct factor), and [[Mosaic|MOS]] joins only at 0.511. Notably the core mixes nutrients (nitrogen CF + potash NTR/IPI), so even the coherent part is not nutrient-pure — the split is not cleanly by nutrient but by ag-commodity/phosphate leverage (MOS) versus the rest.

### PC1 index weights

![[fertilizers-cluster-pca-1y.png]]
*PCA on the candidate cohort. PC1 explains 68% with a large residual; [[Mosaic|MOS]] loads lowest (0.439), consistent with being the defector.*

| Ticker | PC1 loading | Loading weight | Ann vol | Raw PC1-mimic weight |
|---|---|---|---|---|
| NTR | 0.521 | 26.1% | 33.5% | 34.0% |
| MOS | 0.439 | 22.0% | 45.7% | 21.0% |
| CF | 0.510 | 25.5% | 43.4% | 25.6% |
| IPI | 0.525 | 26.3% | 58.8% | 19.5% |

[[Mosaic|MOS]] carries the lowest loading; [[Intrepid Potash|IPI]] the highest but also the highest vol (59%), so it takes the smallest vol-adjusted weight. The factor is weak and the loadings uneven — and, per the holdout, they re-order across regimes (loadings corr −0.37).

### Distinctness — loose and unstable, not the crop trade

![[fertilizers-cluster-correlation-1y.png]]
*1Y pairwise correlation heatmap. A patchy block — NTR/CF/IPI moderately warm (0.62–0.68), MOS cool against them (0.40–0.54); the ag-commodity basket DBA cool against all of them.*

The intra-advantage numbers are positive (+0.283 versus the agribusiness ETF, +0.423 versus the market, +0.145 versus seeds), which would matter if the cohort were tight — but at intra 0.575 with MOS defecting and a negative holdout loadings correlation, the positive ETF margin reflects a loose, regime-unstable group, not a distinct ownable factor. Critically, the fertilizer equities are not the crop-commodity trade: [[DBA]] (corn/wheat/soy futures) clusters apart, because fertilizer-equity returns track nutrient prices (potash/nitrogen/phosphate) and producer economics, not the grain complex. There is no pure-fertilizer ETF, but there is also no stable pure-fertilizer factor here to own.

### Historical tightness evolution — shock-dependent

![[fertilizers-cluster-rolling-tightness-90d.png]]
*Rolling 90-day cohesion, 2021–2026. Moderate and shock-dependent — peaking at 0.77 in the 2022-23 Russia/Ukraine fertilizer-price spike (when potash/nitrogen prices surged and the names moved together), then easing to 0.55–0.62 as nutrient prices normalized.*

| Year | Avg intra-corr | PC1 |
|---|---|---|
| 2021 | 0.626 | 72.7% |
| 2022 | 0.726 | 79.6% |
| 2023 | 0.767 | 82.6% |
| 2024 | 0.597 | 69.9% |
| 2025 | 0.645 | 73.4% |
| 2026 | 0.624 | 71.9% |

*Cohesion tracks the nutrient-price cycle — tight during the 2022-23 supply shock, loose otherwise (latest 90-day 0.539). Combined with the negative holdout loadings correlation, this is a shock-dependent cyclical complex, not a durable factor.*

## Related

- [[Steel and aluminum equity beta]] — the multi-commodity-split precedent (a two-metal label = two factors); fertilizers are messier — loose, with MOS defecting
- [[Copper equity beta]], [[Lithium equity beta]] — the commodity-beta family; fertilizer equities, unlike miners, are NOT their commodity ([[DBA]] is separate)
- [[Nutrien]], [[Mosaic]], [[CF Industries]], [[Intrepid Potash]] — the cohort members
- [[Corteva]] — seeds/crop-protection (a different ag-input model); the cohort is distinct from it (+0.145)
- [[MOO]], [[DBA]] — the agribusiness ETF and ag-commodity controls
- [[Vault cluster taxonomy]] — cross-cohort comparison
- [[Cohort, cluster, basket]] — terminology

---

*Created 2026-06-20. 1Y daily log returns through 2026-06-18; config `scripts/cluster_configs/fertilizers.yaml`; registry row 2026-06-20. Cluster validation is structure, not a performance ranking — see `docs/cluster-validation.md`.*
