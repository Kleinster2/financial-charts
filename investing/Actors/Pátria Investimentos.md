---
aliases:
  - Patria Investimentos
  - Patria Investments
  - PAX
tags:
  - actor
  - company
  - finance
  - private-equity
  - brazil
  - public
---

#actor #company #finance #private-equity #brazil #public

Pátria Investimentos — one of Latin America's largest alternative-asset managers (NASDAQ: PAX), founded in 1988 in Brazil and spanning private equity, infrastructure, credit, real estate and a growing public-equities/advisory business. [[Blackstone]] has held a non-controlling stake since 2010 and was a selling shareholder in the January 2021 IPO. The firm has scaled fee-earning assets to roughly $33 billion (~$44.7B total) and is often framed as the "mini-Blackstone of Latin America." In the investing vault it appears as the seller of vehicle-tracking firm [[Omnilink]] to family office [[Cleam Capital]] in 2019.

One-line read: a structurally growing LatAm alternatives platform — fee-related earnings compounding double digits — whose stock has de-rated since IPO on the EM/Brazil discount and the broader compression of listed-alt multiples.

What to watch: fee-earning AUM growth and the FRE trajectory (the stable fee engine, vs. lumpy performance fees); fundraising pace ($5.5B raised in 2024 vs a $5B target); the BRL and Brazil rate cycle, which drive both the EM discount and dollar-reported results; and M&A — Pátria has grown partly by acquiring managers (credit, infrastructure) across the region.

## Quick stats

| Field | Value |
|-------|-------|
| Type | Alternative-asset manager (PE, infrastructure, credit, real estate, public equities, advisory) |
| Ticker | PAX (NASDAQ, Class A) |
| Founded | 1988, Brazil |
| Domicile | Grand Cayman; operations led from São Paulo |
| IPO | January 26, 2021 at $17.00/share |
| Minority holder | [[Blackstone]] (non-controlling, since 2010) |
| Fee-earning AUM | ~$33B (2024, +38% YoY) |
| Total AUM | ~$44.7B (2024) |
| FY2024 revenue | $374.2M (+14% YoY) |
| FY2024 FRE | $170M (+15% YoY) |
| 2024 fundraising | $5.5B (vs $5B target) |
| Price (Jun 9 2026) | $11.47 |
| Status | Public |

## Why it matters

- The listed LatAm alternatives pure-play: Pátria is the cleanest public way to own the secular growth of private capital in Latin America — institutional allocations to PE/infra/credit in a region that is structurally under-penetrated. Fee-earning AUM grew 38% in 2024.
- Fee engine vs. performance lumpiness: revenue has compounded steadily ($105.7M in 2018 to $374.2M in 2024), but net income is volatile because performance fees swing year to year. The durable metric is fee-related earnings (FRE), which hit the $170M target in 2024 (+15%). The market increasingly prices alts on FRE, not GAAP net income.
- Inorganic build-out: Pátria has expanded beyond Brazilian PE into pan-regional infrastructure, credit and public equities, partly via acquisitions of regional managers — a roll-up of LatAm alternatives under one listed platform.
- The [[Blackstone]] lineage: Blackstone's 2010 minority investment and continued stake give Pátria credibility and a template; the "mini-Blackstone of Latin America" tag is the equity story, but the cluster work below shows the stock does not actually trade with the US alt complex.

## Financials

| FY | Revenue ($M) | Net income ($M) |
|----|--------------|------------------|
| 2018 | 105.7 | 43.7 |
| 2019 | 123.5 | 58.5 |
| 2020 | 115.0 | 62.2 |
| 2021 | 235.5 | 122.5 |
| 2022 | 258.9 | 93.0 |
| 2023 | 327.6 | 118.4 |
| 2024 | 374.2 | 71.9 |
| 2025 | 383.8 | 85.6 |

![[pax-fundamentals-chart.png]]
*Revenue (compounding) vs net income (performance-fee-driven volatility), with PAX price on the left axis. Source: company filings via Alpha Vantage; figures in USD millions. 2024 net income fell despite record revenue as performance fees normalized and FRE — the stable fee line — grew to $170M.*

![[pax-sankey.png]]
*FY2024 income-statement flow. The fee-based model carries a high gross margin; operating income converts to net income after the performance-comp and tax lines.*

![[pax-waterfall.png]]
*FY2024 revenue-to-net-income waterfall.*

See [[Pátria Investimentos securities note]] for price history, peer-relative performance and correlation structure.

## Cluster validation — where does PAX actually trade?

Candidate cohort: PAX plus the listed US alternative-asset managers ([[Blackstone\|BX]], [[KKR]], [[Apollo Global Management\|APO]], [[Ares Management\|ARES]], [[Carlyle Group\|CG]], [[Blue Owl Capital\|OWL]], [[TPG]]); controls = traditional asset managers ([[BlackRock\|BLK]], [[Brookfield Asset Management\|BAM]]) and ETFs (SPY, XLF, EWZ). Config: `scripts/cluster_configs/pax.yaml`; 1-year window to 2026-06-10.

Finding: PAX does not belong to the US alt-manager cluster. The seven US alts form a tight bloc (pairwise join distances 0.15–0.27) that absorbs even the traditional managers and the financials ETF before PAX attaches — PAX joins only at distance 0.494, and hierarchical clustering at threshold 0.5 leaves PAX as its own singleton while everything else collapses into one US-financials cluster. PAX's own pairwise correlations to the cohort run only ~0.49–0.56 (the 0.70 cohort-average is inflated by the tight US-alt-to-US-alt pairs); its low absolute correlations and high idiosyncratic variance — reflecting Brazil/EM and firm-specific drivers — are what push it out as a singleton.

| Diagnostic | Value | Read |
|-----------|-------|------|
| Avg intra-cohort correlation (1Y) | 0.698 | Moderately tight as a group |
| Cohort vs traditional AM | 0.645 (advantage +0.052) | Weak separation from plain asset managers |
| Cohort vs ETF | 0.451 (advantage +0.247) | Clear separation from broad market |
| Hierarchical boundary (thr 0.5) | PAX = singleton | PAX splits off; US alts + BLK/BAM/XLF form one cluster |
| PAX join distance | 0.494 (last to join) | Joins after BLK, BAM, XLF — a satellite, not a core member |
| PC1 explained variance | 74.2% | Strong common "alt-manager beta" factor |
| PAX PC1 loading | 0.262 (lowest; peers 0.35–0.38) | PAX loads weakest on the shared factor |
| Weekly cross-check | intra 0.658, PC1 70.5% | Robust to async US/Brazil close timing |
| Rolling tightness (latest 90D) | avg 0.709, PC1 75.1%, satellite 0.526 | PAX sits in the satellite, not the core |
| Random-basket p, 10k draws (intra / PC1) | 0.0001 / 0.0001 | Cohort cohesion at the Phipson-Smyth floor — but the signal is the US-alt core, not PAX |
| Threshold-stable width | 0.00 (none) | The PAX-inclusive cohort never assembles cleanly: BAM joins the US-alt cluster from 0.30 and BLK/XLF by 0.40, all before PAX attaches (~0.55) |

![[pax-cluster-dendrogram-1y.png]]
*Hierarchical clustering (1Y, distance = 1−|corr|). The US alt managers join tightly; PAX is the last, most-distant join — a statistical singleton rather than a cohort member.*

![[pax-cluster-pca-1y.png]]
*PCA on the candidate cohort: PC1 explains 74.2% of variance (a real shared alt-manager factor), but PAX carries the lowest PC1 loading.*

![[pax-cluster-rolling-tightness-90d.png]]
*90-day rolling cohort tightness. The 2024 loosening and 2025 re-tightening track the global risk cycle; PAX persistently reads as satellite, not core.*

Takeaway: "mini-Blackstone of Latin America" is a business analogy, not a trading relationship. PAX is a low-correlation, idiosyncratic name — it tracks the US alts only marginally more than the broad market (most with [[KKR]] at 0.56, vs [[SPY]] at 0.49) and is not captured by a Brazil factor either ([[EWZ]] at 0.50). It reads as a singleton because its absolute correlations to everything are low — a genuine diversifier rather than a cohort member. The 2026-06-12 statistical suite sharpens the point: the cohort's cohesion rejects the random-basket null at the floor (that's the US-alt core talking), but the threshold scan shows [[Brookfield Asset Management|BAM]] and [[BlackRock|BLK]] joining the US-alt cluster before PAX does — the "mini-Blackstone" is statistically farther from Blackstone than BlackRock is.

## Sector correlation

1-year daily-return correlations to 2026-06-10:

| Benchmark | Ticker | Correlation |
|-----------|--------|-------------|
| US alt manager | [[KKR]] | 0.56 |
| Brazil equities | [[EWZ]] | 0.50 |
| US alt manager | [[Blackstone]] (BX) | 0.49 |
| US large-cap | [[SPY]] | 0.49 |
| US financials | [[XLF]] | 0.45 |

PAX's correlations are uniformly moderate (~0.45–0.56) — it tracks the US alt managers only marginally more than the broad market or Brazil, and no single factor captures it. That low, undifferentiated profile is exactly why the hierarchical cluster leaves PAX a singleton: not a Brazil-cluster captive, but a low-correlation diversifier whose own variance dominates.

## Related

- [[Cleam Capital]] — bought [[Omnilink]] from Pátria (2019)
- [[Omnilink]] — divested holding
- [[Blackstone]] — minority holder since 2010; US alt-manager comparator
- [[Brazil]] — home market / EM factor driver
- [[Pátria Investimentos securities note]] — price history, peer-relative chart, correlation heatmap

*Created 2026-06-10 as a stub during the Grano/Cleam ingest; fleshed to a full deepdive 2026-06-11. Sources: company FY2024 results (GlobeNewswire/IR), F-1 and 6-K filings (SEC), Bloomberg (IPO), Seeking Alpha; price/fundamentals from market_data.db.*
