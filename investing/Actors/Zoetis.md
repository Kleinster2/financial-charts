---
aliases: [ZTS]
tags: [actor, pharma, animal-health, usa, public]
---

#actor #pharma #animal-health #usa #public

> [!failure] Cluster status: falsified as basket (May 2026)
> Intra-cluster correlation 0.32, PC1 49.8% explained variance. Hierarchical clustering at 0.4 returns ZTS, ELAN, IDXX, HSIC as four separate singletons — no coherent "animal health" basket. Cluster intra-correlation (0.32) is *lower* than the cluster's correlation to the broader healthcare ETF (0.37), meaning XLV explains more of ZTS's return than its named peers do. ZTS is a sector orphan; trade it as a single name, not as part of a cohort. See "Cluster validation" section below.

[[Zoetis]] — Largest pure-play animal health company globally. ~$9.5B revenue. Spun out of [[Pfizer]] in 2013 IPO. NYSE: ZTS, market cap ~$40B (May 7, 2026). Headquartered Parsippany, NJ. CEO [[Kristin Peck]] since 2020.

The portfolio splits roughly 65% companion animal (pets — dogs, cats, horses) and 35% livestock (cattle, swine, poultry, fish). Companion animal carries the higher growth + margin profile and includes the [[Apoquel]] (atopic dermatitis), [[Cytopoint]], [[Simparica]] (parasiticides), [[Librela]] (osteoarthritis monoclonal antibody) franchises. The Q4 2026-targeted close of the [[Neogen]] genomics acquisition is the next major strategic pivot — adds a livestock-genomics testing business at a moment when livestock organic growth has flattened.

---

## Sector correlation

> [!warning] Sector Orphan
> ZTS does not trade tightly with any sector ETF (max r = 0.44 with XLI).

| Sector | ETF | Correlation |
|--------|-----|-------------|
| Industrials | XLI | 0.44 |
| [[Consumer]] | XLY | 0.43 |
| [[Healthcare]] | XLV | 0.39 |
| *S&P 500* | *SPY* | *0.40* |

ZTS trades between Industrials and Consumer without a tight sector fit.

---

## Cluster validation (May 2026)

The animal-health basket — ZTS + [[Elanco|ELAN]] + [[Idexx Laboratories|IDXX]] + [[Henry Schein|HSIC]] — is mathematically falsified as a tradable cluster. The "where does this name actually trade" question, run with `scripts/cluster_configs/zts.yaml` over the 1-year window (170 obs), produces three separate failures:

| Diagnostic | Result | Threshold | Verdict |
|------------|--------|-----------|---------|
| Intra-cluster correlation | 0.324 | ≥0.50 | fail |
| PC1 explained variance | 49.8% | ≥70% | fail |
| Hierarchical clustering at d=0.4 | All four names singletons | Returns the candidate cohort | fail |

The most diagnostic single number: cluster intra-correlation (0.324) is *lower* than the cluster's average correlation to the broad healthcare ETF (0.370 vs XLV / IBB / SPY). The named animal-health peers explain less of each other's variance than the broad-pharma factor does. Pairwise correlations (1y):

| | ZTS | ELAN | IDXX | HSIC |
|---|---|---|---|---|
| ZTS  | 1.00 | 0.49 | 0.37 | 0.07 |
| ELAN | 0.49 | 1.00 | 0.36 | 0.27 |
| IDXX | 0.37 | 0.36 | 1.00 | 0.37 |
| HSIC | 0.07 | 0.27 | 0.37 | 1.00 |

ZTS-HSIC correlation of 0.07 is the cleanest single number — the diagnostics company ([[Henry Schein|HSIC]] is dental + medical distribution; not pure animal health) is essentially independent of the pure-play animal-health pharma. ZTS-ELAN at 0.49 is the only meaningful pair correlation, and it sits below the 0.50 threshold for "validated cluster" status.

Hierarchical clustering at d=0.4 returns 12 separate clusters across the 14-ticker universe, including:
- Cluster 1: PG, CL (consumer staples comparator pair — these *do* cluster)
- Cluster 3: LLY, XLV (Eli Lilly pulls XLV)
- Singletons: ZTS, ELAN, IDXX, HSIC, MRK, PFE, FRPT, CHWY, SPY (each its own cluster)

PC1 loadings on the candidate cohort are all positive but unequal (ZTS 0.50, ELAN 0.55, IDXX 0.54, HSIC 0.39) — HSIC is the outlier (lowest loading) consistent with its non-pure-animal-health business mix.

### What this means for ZTS positioning

Trade ZTS as a single name, not as a basket-relative or sector-relative trade. The May 7 -21% reaction sits inside a name-level idiosyncratic-risk regime — [[Elanco|ELAN]] is the only peer that meaningfully co-moves (0.49), and even that is below the basket-validation threshold. The "premium-pet consumer pulse" framing in the May 7 commentary is real, but it does not translate to ELAN automatically — and HSIC / IDXX have their own cyclical drivers that overwhelm whatever animal-health-sector beta exists.

For the [[2026 recession risk]] cross-name read on May 7, the cleanest pair is ZTS + [[Vital Farms]] (premium-suburban consumer demographic overlap), not ZTS + ELAN (sector overlap, low correlation overlap).

![[zts-cluster-dendrogram-1y.png]]
*Hierarchical clustering tree: ZTS, ELAN, IDXX, HSIC each in their own cluster at the 0.4 distance threshold. Compare to the PG-CL pair (consumer staples) which clusters tightly, or LLY-XLV (mega-cap pharma pulls the ETF).*

![[zts-cluster-correlation-1y.png]]
*Pairwise return-correlation heatmap (1y window). Note the ZTS-HSIC correlation of 0.07 — effectively independent. The strongest internal correlation is ZTS-ELAN at 0.49, still below cluster-validation threshold.*

![[zts-cluster-pca-1y.png]]
*PCA scree + PC1 loadings on the candidate cohort. PC1 captures only 49.8% of return variance — below the 70% threshold for a validated single-factor basket.*

*Source: `scripts/cluster_configs/zts.yaml`, run via `python scripts/cluster_analysis.py --primary ZTS` (2026-05-07).*

---

## Why Zoetis matters

| Metric | Value |
|--------|-------|
| Ticker | ZTS ([[NYSE]]) |
| Revenue | ~$9.5B (FY26 implied) |
| Market cap | ~$40B (May 7, 2026) |
| Spun from | [[Pfizer]] (2013 IPO) |
| CEO | [[Kristin Peck]] |
| Pipeline | 12+ potential blockbusters |

![[zoetis-price-chart.png]]
*ZTS price since 2020. May 7, 2026 close $87.75 — sharp pullback from ~$200 peaks during the 2022 cycle and the more recent ~$120 trading range that compressed on the Q1 2026 print.*

## Financials

![[zoetis-fundamentals-chart.png]]
*ZTS revenue and net income trajectory; the smooth uptrend through the [[2026 State of the Union economic claims|premium-pet thesis]] period now visibly inflecting on the Q1 2026 print.*

![[zoetis-sankey.png]]
*ZTS latest annual income-statement flow; companion-animal franchise concentration (Apoquel + Cytopoint + Simparica + Librela) carries most of the operating leverage.*

The company is the consensus "premium-consumer pet exposure" name in the [[2026 recession risk]] mover tape — pet care has historically been recession-resistant ("families don't downgrade Fluffy"), and ZTS has traded at a premium multiple to the broader pharma cohort on that durability assumption. The May 7 print is the first quarter that thesis fractured publicly.

---

## Q1 2026 earnings (May 7, 2026) — premium pet consumer cracked

ZTS closed -21.1% on May 7 to $87.75 from $111.22, the steepest single-day move in the company's public history and the cleanest dual signal with [[Vital Farms]] -23.8% of premium-consumer-pulse fade in the May 7 tape.

| Metric | Q1 2026 | Consensus | YoY |
|--------|---------|-----------|-----|
| Revenue | $2.262B | $2.330B | +3% reported / flat organic |
| Net income | $601M | — | — |
| Diluted EPS (GAAP) | $1.42 | — | — |
| Adjusted net income | $646M | — | +2% reported, +9% on adj. EPS basis |
| Adjusted diluted EPS | $1.53 | $1.63 | -$0.10 miss |

FY 2026 guidance reset to:
- Revenue: $9.680-9.960B
- Adjusted net income: $2.870-2.950B
- Adjusted diluted EPS: $6.85-7.00
- Implied organic operational revenue growth: 2-5%

Management commentary attributed the miss to "more challenging operating environment" with three named pressures: (1) pet owners showing increased price sensitivity, (2) decline in veterinary visits, (3) softer demand for premium innovative products. Competition was characterized as intensifying across two specific categories — dermatology ([[Apoquel]] / [[Cytopoint]] franchise) and parasiticides ([[Simparica]] franchise) — both core companion-animal growth pillars.

The forward unknowns: whether the [[Neogen]] genomics acquisition closes in H2 2026 (livestock-genomics adjacency), whether [[Librela]] osteoarthritis monoclonal antibody launches into the dermatology-parasiticide consumer-pressure environment without being repriced down, and whether the 12+ blockbuster pipeline materializes in 2027 in time to offset the 2026 organic-growth flattening.

Cross-name read: ZTS + VITL on the same day form the cleanest premium-consumer-pulse signal in the vault since [[Tapestry]] sold off post-Q3 (May 7, also). The customer overlap is the durable suburban household consumer that the [[2026 State of the Union economic claims]] thread had been pricing as resilient. Three names cracking the same day on the same demographic argues for [[2026 recession risk]] consumer-side framing more than for individual-name attribution.

*Sources: [Zoetis Q1 2026 release](https://news.zoetis.com/press-releases/press-release-details/2026/Zoetis-Announces-First-Quarter-2026-Results/default.aspx); [stocktitan — Zoetis Q1 2026 results show mixed trends and new guidance](https://www.stocktitan.net/sec-filings/ZTS/8-k-zoetis-inc-reports-material-event-06288aa1b11d.html); [Yahoo Finance — Zoetis (NYSE:ZTS) Misses Q1 CY2026 Revenue Estimates, Stock Drops 13%](https://finance.yahoo.com/markets/stocks/articles/zoetis-nyse-zts-misses-q1-114729483.html); [Morningstar — Zoetis Announces First Quarter 2026 Results](https://www.morningstar.com/news/business-wire/20260506864676/zoetis-announces-first-quarter-2026-results).*

---

## Products

| Franchise | Indication | Notes |
|-----------|-----------|-------|
| [[Apoquel]] | Canine atopic dermatitis | Cornerstone derm franchise |
| [[Cytopoint]] | Canine atopic dermatitis | Anti-IL-31 monoclonal antibody |
| [[Simparica]] | Parasiticides (flea/tick) | Companion-animal core |
| [[Librela]] | Canine osteoarthritis | Anti-NGF monoclonal antibody — newer launch |
| [[Solensia]] | Feline osteoarthritis | Feline anti-NGF analog |
| Diagnostics | Various | Smaller franchise |

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | ZTS |
| Exchange | [[NYSE]] |
| Headquarters | Parsippany, NJ |
| CEO | [[Kristin Peck]] |
| Spun from | [[Pfizer]] 2013 |
| Revenue | ~$9.5B (FY26) |
| Pipeline blockbusters | 12+ |
| Pending acquisition | [[Neogen]] (livestock genomics) |

---

## Related

- [[Vital Farms]] — premium-consumer-fade pair on May 7
- [[Pfizer]] — 2013 IPO parent
- [[Neogen]] — pending acquisition (H2 2026 close target)
- [[2026 recession risk]] — consumer-pulse cluster framing
- [[Kristin Peck]] — CEO since 2020
- [[Apoquel]] — derm franchise (oral JAK inhibitor)
- [[Cytopoint]] — derm franchise (anti-IL-31 monoclonal)
- [[Simparica]] — parasiticide franchise (isoxazoline)
- [[Librela]] — canine OA pain (anti-NGF monoclonal)
- [[Solensia]] — feline OA pain (anti-NGF monoclonal)

### Securities

- [[Zoetis securities]] — ZTS price history, valuation, ratings (companion securities note)

---

*Created 2026-05-07.*
