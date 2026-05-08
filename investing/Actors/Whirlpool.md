---
aliases: [WHR]
tags: [actor, appliance, consumer-durable, housing, usa, public]
---

#actor #appliance #consumer-durable #housing #usa #public

> [!failure] Cluster status: WHR is a singleton inside the housing-cycle complex (May 2026)
> Intra-cluster correlation 0.47, PC1 58.4%. Hierarchical clustering at 0.4 returns a tight 11-name housing-cycle super-cluster (MAS, FBIN, SWK, DHI, LEN, NVR, PHM, HD, LOW, XHB, ITB) — but WHR is a SINGLETON, isolated from that cohort. NWL is also a singleton. The May 7 -14% reaction is statistically idiosyncratic, not a "housing-cycle" trade. WHR co-moves more with [[Newell Brands|NWL]] (0.31, both singletons) than with builders / retailers / building-products. See "Cluster validation" section below.

[[Whirlpool]] — Largest home-appliance maker in the United States. NYSE: WHR. ~$15-16B revenue (FY25), market cap ~$2.6B (May 7, 2026). Headquartered Benton Harbor, Michigan. CEO [[Marc Bitzer]] since 2017. Brands include [[Whirlpool brand]], [[Maytag]], [[KitchenAid]], [[JennAir]], [[Amana]].

The investment-vault relevance is the housing-cycle transmission. WHR is the cleanest large-cap appliance read on US new-construction + replacement-cycle dynamics — and the May 7, 2026 Q1 print is the cleanest dated evidence yet that the 2026 housing recovery the company telegraphed in January is now visibly failing.

---

## Sector correlation

> [!warning] Sector Orphan
> WHR does not trade tightly with any sector ETF (max r = 0.42 with XLI).

| Sector | ETF | Correlation |
|--------|-----|-------------|
| Industrials | XLI | 0.42 |
| [[Consumer]] | XLY | 0.42 |
| [[Banks\|Regional Banks]] | KRE | 0.39 |
| *S&P 500* | *SPY* | *0.36* |

WHR trades between Industrials and Consumer without a tight sector fit.

---

## Cluster validation (May 2026)

The most useful single result of the cluster analysis is *negative*: WHR is mathematically isolated from the housing-cycle super-cluster that should be its natural peer cohort. Run with `scripts/cluster_configs/whr.yaml` over the 1-year window (170 obs, 18 tickers).

| Diagnostic | Result | Threshold | Verdict |
|------------|--------|-----------|---------|
| Intra-cluster correlation (WHR + MAS + FBIN + NWL + SWK) | 0.466 | ≥0.50 | borderline fail |
| PC1 explained variance | 58.4% | ≥70% | fail |
| Hierarchical clustering at d=0.4 | WHR singleton; large housing super-cluster excludes WHR | Returns proposed cohort | fail |

The WHR singleton finding is the load-bearing one. At distance threshold 0.4, the dendrogram produces five clusters across the 18-ticker universe:

| Cluster | Members | Read |
|---------|---------|------|
| 1 | AVB, CPT | Multifamily REITs (apartment) — own factor |
| 2 | XLY, XLI, SPY | Broad-market ETFs |
| 3 | MAS, FBIN, SWK, DHI, LEN, NVR, PHM, HD, LOW, XHB, ITB | The 11-name housing-cycle super-cluster — building-products + builders + home-improvement retail + housing ETFs all together |
| 4 | WHR | SINGLETON |
| 5 | NWL | SINGLETON |

That's the finding: every other "should be a peer" name in the candidate-cohort + control-group list co-moves with the housing-cycle factor (cluster 3, 11 names) — except WHR and NWL. WHR's correlations confirm:

| Pair | Correlation (1y) |
|------|------------------|
| WHR — MAS | 0.44 |
| WHR — FBIN | 0.45 |
| WHR — NWL | 0.31 |
| WHR — SWK | 0.53 |
| WHR — DHI / LEN / NVR (builders) | (cluster-vs-homebuilders avg 0.49) |
| WHR — HD / LOW (home-improvement) | (cluster-vs-home-improvement avg 0.49) |
| MAS — FBIN | 0.69 |
| FBIN — SWK | 0.62 |
| MAS — SWK | 0.67 |

WHR's strongest correlation in the candidate cohort is with SWK (0.53) — modest. But MAS-FBIN-SWK pairwise correlations are 0.62-0.69, well above the cluster-validation threshold. SWK clusters with MAS and FBIN, and MAS-FBIN-SWK then clusters with the builders + retailers + ETFs into the giant 11-name housing-cycle group at d=0.4. WHR sits outside that whole structure.

PC1 loadings on the 5-name candidate cohort: WHR 0.42, MAS 0.50, FBIN 0.47, NWL 0.31, SWK 0.51. WHR and NWL are the two lowest loadings — the two singletons in the dendrogram are also the two PC1 outliers, confirming the same finding two ways.

### What this means for WHR positioning

The May 7 -14% guide-cut reaction is statistically idiosyncratic, not a housing-cycle factor move. The structural read:

1. WHR's price action is dominated by company-specific factors (tariff drag, brand-portfolio mix, FY-guide cycles, [[Marc Bitzer]] cost-and-pricing actions, balance-sheet leverage, [[2024 Capri merger collapse|merger-cancellation history]]) more than by the housing-cycle factor that drives MAS / FBIN / SWK / builders.
2. The "housing-pulse" framing in the consumer-cycle write-up (the May 7 daily note synthesis) is conceptually accurate but does not produce a tradable basket — going long WHR vs short DHI / LEN to hedge company-specific risk wouldn't work because WHR doesn't co-move with builders enough for the hedge to absorb factor risk.
3. The cleanest cross-name read for the May 7 consumer-cycle thesis is *not* WHR + MAS + SWK as a housing-cycle proxy; it is WHR + NWL as the two consumer-durables-singleton names, both with idiosyncratic management challenges and modest peer correlations.

This is consistent with the [[Sector Orphan]] finding from the basic ETF-correlation analysis above (max r = 0.42 with XLI). Cluster validation confirms the orphan status holds when the candidate cohort is expanded from 4 ETFs to 18 named comparators.

![[whr-cluster-dendrogram-1y.png]]
*Hierarchical clustering tree at distance threshold 0.4. Note the large housing-cycle super-cluster on the left (MAS-FBIN-SWK + builders + HD/LOW + ETFs all aggregating below 0.4), while WHR and NWL each sit alone at much higher distances.*

![[whr-cluster-correlation-1y.png]]
*Pairwise return-correlation heatmap (1y). MAS-FBIN-SWK form a clear high-correlation block (0.62-0.69); WHR's row shows weaker correlations across the entire universe.*

![[whr-cluster-pca-1y.png]]
*PCA scree + PC1 loadings on the 5-name candidate cohort. PC1 explains only 58.4% of variance — below the 70% validated-basket threshold. WHR (0.42) and NWL (0.31) are the lowest PC1 loadings, consistent with their singleton status in the dendrogram.*

*Source: `scripts/cluster_configs/whr.yaml`, run via `python scripts/cluster_analysis.py --primary WHR` (2026-05-07).*

---

## Why Whirlpool matters

| Metric | Value |
|--------|-------|
| Ticker | WHR ([[NYSE]]) |
| Revenue | ~$15.5B (FY25 base) |
| Market cap | ~$2.6B (May 7, 2026) |
| CEO | [[Marc Bitzer]] (since 2017) |
| HQ | Benton Harbor, Michigan |
| Major brands | Whirlpool, Maytag, KitchenAid, JennAir, Amana |

![[whirlpool-price-chart.png]]
*WHR price since 2020. The May 7, 2026 close at $47.14 sits at a multi-year low; the chart shows the compounded damage of the 2024 [[2024 Capri merger collapse|merger collapse]], the 2025 housing-cycle disappointment, and the May 7, 2026 FY guide cut from ~$6.25 to $2.45-2.95 GAAP EPS.*

## Financials

![[whirlpool-fundamentals-chart.png]]
*WHR revenue and net income trajectory; cyclical compression visible across the housing-cycle window and now sharpening on the Q1 2026 print.*

![[whirlpool-sankey.png]]
*WHR latest annual income-statement flow; the compressed operating margin (driven by tariff drag + housing-cycle volume softness) is structural rather than transient at current revenue levels.*

The macro signal value sits in the FY26 guide trajectory. In January 2026, Bitzer guided FY26 GAAP EPS to roughly $6.25, framed by "confidence based on recent product launches, reduced promotional intensity and a gradual recovery of the housing market." The May 7 Q1 print revised that to $2.45-2.95 GAAP EPS — a >50% guide cut in four months on an already-cyclical name.

---

## Q1 2026 earnings (May 7, 2026) — guide cut by half on housing reversal

WHR reported Q1 2026 May 6 after close, conference call May 7 8 AM EDT. Stock closed -13.9% on May 7 to $47.14 from $54.73 — the largest single-day move since the July 2024 merger-cancellation reaction.

| Metric | Q1 2026 | Prior implied | Read |
|--------|---------|----------------|------|
| Revenue | -9.6% YoY | flat-to-slightly-up | Demand weaker than recessionary trough levels per CEO commentary |
| FY26 GAAP EPS guide | $2.45-2.95 | ~$6.25 (Jan 2026) | >50% cut in four months |
| FY26 ongoing EPS guide | $3.00-3.50 | — | First time ongoing guide separated explicitly |

Management called the Q1 demand environment "weak appliance demand reminiscent of recession levels" — a sharp departure from the January framing. The accelerated cost-and-pricing actions cited in the press release headline ("Accelerates Cost and Pricing Actions to Restore Margins") indicate the response is volume-defensive: protect operating profitability through pricing and cost discipline rather than chase volume in a softening market.

The macro read is the cleanest. The January 2026 [[Marc Bitzer]] guide implicitly priced a gradual housing recovery starting in H1 2026. The May 7 print confirms the recovery has not arrived — and the cost-action language is consistent with management positioning for an extended weakness through H2. This sits alongside [[Tapestry]] -8.7%, [[Zoetis]] -21.1%, and [[Vital Farms]] -23.8% on the same day as the cleanest cross-name signal of consumer-discretionary fade in the May 7 tape.

For the [[2026 recession risk]] thread, WHR is now the cleanest single-name housing-pulse signal: capital-goods consumer exposure (kitchen / laundry / refrigeration replacement + new-construction), high cyclical leverage to housing turnover, and a four-month management-guide cut sequence. The next read is whether the cost-action playbook restores margins or whether revenue continues to compress through Q3-Q4.

*Sources: [Whirlpool Q1 2026 release](https://www.prnewswire.com/news-releases/whirlpool-corporation-announces-first-quarter-results-accelerates-cost-and-pricing-actions-to-restore-margins-302764444.html); [Moody on the Market — Whirlpool earnings miss expectations; CEO bases 2026 confidence on gradual housing recovery](https://www.moodyonthemarket.com/whirlpool-corporation-earnings-miss-expectations-ceo-bases-2026-confidence-on-gradual-housing-recovery/); [Whirlpool Jan 2026 Q4/FY guidance](https://www.prnewswire.com/news-releases/whirlpool-corporation-announces-fourth-quarter-and-full-year-results-provides-2026-guidance-302673163.html).*

---

## Brands

| Brand | Position |
|-------|----------|
| [[Whirlpool brand]] | Mass-market core |
| [[Maytag]] | Heritage / durability positioning |
| [[KitchenAid]] | Premium, kitchen-focused |
| [[JennAir]] | Luxury / built-in segment |
| [[Amana]] | Value / multifamily |

---

## Macro transmission

WHR's quarterly volume and pricing data are watched by housing-sensitive analysts as a leading-coincident indicator on:

- US existing-home turnover (~70% of demand is replacement, ~30% new construction)
- Kitchen + laundry remodeling activity (kitchen renovation a particularly cyclical sub-segment)
- Multifamily new construction (Amana brand exposure)
- Discretionary consumer spending in major durables

The cross-name pairings: [[Home Depot]] / [[Lowe's]] big-box appliance segment, [[Best Buy]] for the consumer-electronics-adjacent appliance pull, and the [[Homebuilders]] cohort ([[D.R. Horton]], [[Lennar]], [[Toll Brothers]]) for the new-construction read.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | WHR |
| Exchange | [[NYSE]] |
| Founded | 1911 |
| HQ | Benton Harbor, Michigan |
| CEO | [[Marc Bitzer]] |
| Revenue | ~$15.5B |
| Market cap | ~$2.6B (May 7, 2026) |

---

## Related

- [[Tapestry]] — sold off same day on tariff guide; consumer-discretionary cluster
- [[Zoetis]] — premium-pet pulse; same-day -21.1%
- [[Vital Farms]] — premium-egg pulse; same-day -23.8%
- [[2026 recession risk]] — housing-cycle macro framing
- [[Home Depot]] — replacement-channel exposure
- [[Lowe's]] — replacement-channel exposure
- [[D.R. Horton]] — new-construction read
- [[Marc Bitzer]] — CEO + Chair
- [[Maytag]] · [[KitchenAid]] · [[JennAir]] · [[Amana]] — brand portfolio
- [[Homebuilders]] — primary cyclical-coincident upstream cohort

### Securities

- [[Whirlpool securities]] — WHR price history, valuation, ratings (companion securities note)

---

*Created 2026-05-07.*
