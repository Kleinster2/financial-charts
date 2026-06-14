---
aliases: [CHL, China Mobile Limited, 0941.HK, 600941.SS, 中国移动]
tags: [actor, china, telecom, soe]
---

#actor #china #telecom #soe

**China Mobile** — [[China]]'s largest telecom operator and the dominant, most profitable of the three state-owned carriers (with [[China Unicom]] and [[China Telecom]]), with ~1.0bn mobile customers and ~RMB1.05tn revenue. The anchor of the China-telecom bloc: the lowest-volatility, highest-dividend member, run as a cash-returning value-up vehicle while it builds Mobile Cloud and computing capacity for its next leg of growth.

One-line read: China Mobile is the high-margin core of a tight, state-driven China-telecom bloc that has re-rated on the [[China special valuation|SOE value-up theme]], with the forward bet being whether ~RMB1tn of revenue can keep compounding at low-single-digits and the dividend keep ratcheting now that mobile is saturated and profit growth has stalled (net profit dipped −0.9% in 2025).

---

## Why China Mobile matters

| Metric | Value |
|--------|-------|
| Listings | [[China Mobile securities note\|0941.HK]] (Hong Kong), 600941.SS (Shanghai A-share) |
| Former ADR | CHL (NYSE, delisted Jan 2021 under [[Executive Order 13959]]) |
| Mobile customers | ~1.0bn (5G network customers 642mn) |
| FY2025 revenue | RMB 1,050.19bn (+0.9% YoY) |
| FY2025 net income | RMB 137.10bn (−0.9% YoY) |
| Net margin | ~13.1% (highest of the three) |
| Mobile Cloud revenue (H1 2025) | RMB 56.1bn (+11.3%) |
| Controlling shareholder | China Mobile Communications Group (SASAC) |

China Mobile is the largest member of the bloc by a wide margin — its ~RMB137bn net profit exceeds [[China Unicom]] (RMB20.8bn) and [[China Telecom]] (RMB33.2bn) combined, and its ~13% net margin roughly doubles theirs. It is the index-weight anchor of any China-telecom exposure and the cleanest dividend-yield expression of the [[China special valuation]] re-rating.

---

## Financials

0941.HK reporting (RMB mn, IFRS/HKFRS):

| FY | Revenue | Operating income | Net income | Net margin |
|----|--------:|-----------------:|-----------:|-----------:|
| 2021 | 848,258 | 120,185 | 115,937 | 13.67% |
| 2022 | 937,259 | 136,805 | 125,459 | 13.39% |
| 2023 | 1,009,309 | 139,349 | 131,766 | 13.05% |
| 2024 | 1,040,759 | 144,155 | 138,373 | 13.30% |
| 2025 | 1,050,187 | 149,230 | 137,095 | 13.05% |

*Source: company reporting via StockAnalysis. China Mobile crossed RMB1tn revenue in 2023, but growth has decelerated hard — +0.9% revenue in 2025 and the first net-income dip of the period (−0.9% to RMB137.1bn). Margins are stable ~13%, structurally far above the other two carriers. The slowing is mobile saturation: net adds were just ~854K customers in 2025 against a ~1bn base.*

*No fundamentals/Sankey/waterfall charts: [[Alpha Vantage]] provides no income-statement data for Hong Kong tickers (0941.HK), so the series above is sourced from company reporting. Cluster validation below uses price data, which is available.*

---

## Operations and the dividend

China Mobile's connectivity base is saturated; the equity story is increasingly the payout. The company raised its final dividend (HK$2.52/share; ~HK$5.27 annual) and has guided toward a rising cash-return ratio — the engine of its [[China special valuation]] re-rating. Capex is disciplined (RMB25.8bn on 5G in H1 2025; 2.6mn cumulative 5G base stations). 5G network customers reached 642mn. The growth optionality sits in:

- Mobile Cloud (移动云) — H1 2025 revenue RMB56.1bn (+11.3%), part of the same state-directed cloud/computing buildout the bloc is running (see [[East Data West Compute]]).
- Computing and AI infrastructure — China Mobile is one of the three telecoms converting their power/land/fiber footprint into intelligent-computing capacity.

The open question is identical to its peers: can fast-growing-but-small cloud/computing offset a flat connectivity core large enough that even double-digit cloud growth barely moves the consolidated line.

---

## A-share return (2022)

China Mobile's distinct corporate-finance event was its January 2022 return to the Shanghai exchange (600941.SS) — a ~RMB52bn (~$8.8bn) A-share IPO, the largest mainland listing in roughly a decade at the time. Where [[China Unicom]]'s reform story was the 2017 mixed-ownership sale (BATJ + China Life) and [[China Telecom]] returned to Shanghai in 2021, China Mobile's A-share debut came as US capital-markets access was being closed off (see below) — part of the broader repatriation of Chinese champions' listings toward home markets.

---

## NYSE delisting (2021)

China Mobile's ADR (CHL) was the first of the three telecom ADRs removed from the NYSE, in January 2021, under [[Executive Order 13959]] — the November 2020 Trump order barring US persons from holding "Communist Chinese military companies." [[China Unicom]] (CHU) and [[China Telecom]] (CHA) followed. The three now trade only in Hong Kong and on mainland exchanges. Mechanics in [[China Mobile securities note]].

---

## Cluster validation

`scripts/cluster_configs/china_telecom.yaml` (China Mobile as primary). The full cohort analysis lives in [[China Unicom]]; the verdict is shared because the cohort is the same three names. China Mobile (0941.HK) trades as a member of a tight, durable China-telecom bloc — distinct from US telecoms and broad China equity.

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster correlation (1Y) | 0.668 (range 0.62–0.75) | real co-movement |
| Hierarchical clusters (0.5 cut) | 3 clean groups | {0762, 0941, 0728} separate from {[[AT&T\|T]], [[Verizon\|VZ]], [[T-Mobile\|TMUS]]} and {[[FXI]], [[KWEB]], [[SPY]]} |
| PC1 explained variance | 77.9% | one dominant common factor |
| China Mobile ann. vol | 11.76% | lowest in the bloc — the stable anchor |
| China Mobile PC1-mimic weight | 47.0% (raw, vol-adjusted) | highest — low vol makes it the natural index core |
| Cluster vs china_etf / us_telecom | 0.19 / 0.05 | not generic China beta, not a global-telecom co-mover |

![[china-mobile-cluster-dendrogram-1y.png]]
*Three clean clusters at the 0.5 threshold — the China telecoms (0941 with 0762/0728) fuse with each other long before joining US telecoms or the China/US-market ETFs.*

![[china-mobile-cluster-pca-1y.png]]
*PC1 explains 77.9% of cohort variance — a single common factor (Chinese telecom regulation + SOE value-up policy + state ownership).*

China Mobile is the lowest-volatility member (11.8% annualized vs [[China Unicom]]'s 21.7%), which makes it the highest vol-adjusted weight in any bloc index and the natural core holding — the defensive, dividend-anchored way to own the China-telecom factor, where Unicom is the higher-beta expression.

---

## What to watch

- Profit inflection — 2025's −0.9% net-income dip is the first of the period. Whether this is a one-off or the start of mobile-saturation margin pressure determines if the dividend case still has earnings behind it.
- Dividend ratio — the [[China special valuation]] re-rating rests on a rising payout. China Mobile's guided cash-return increases are the single most-watched dial.
- Mobile Cloud / computing scale — RMB56.1bn H1 and +11.3% growth; the question is whether it can grow large enough to offset a flat ~RMB1tn connectivity core.
- The bloc — with PC1 ~78%, China Mobile co-moves with [[China Unicom]] and [[China Telecom]]; watch sector-wide dividend/policy signals.

---

## Analysis

China Mobile is the bloc's centre of gravity and its safest expression: lowest volatility, highest margin, biggest dividend, and a balance sheet that lets it keep raising the payout. The cluster work (PC1 ~78%, the three telecoms a clean group separate from both US telecoms and China ETFs) says owning China Mobile is owning the China-telecom-policy factor in its most defensive form — Unicom is the higher-beta version of the same trade, Telecom the cloud-tilted one.

The tension is that the engine driving the re-rating — a ratcheting dividend funded by capex discipline on a saturated, ~13%-margin business — is now bumping against the growth ceiling: revenue +0.9% and the first net-profit decline of the cycle in 2025. A dividend story needs earnings that at least hold; a sustained profit slide would force the choice between payout growth and reinvestment in the cloud/computing pivot. That pivot (Mobile Cloud +11.3%, the [[East Data West Compute]] buildout) is real but small relative to a RMB1tn base — the same arithmetic problem all three carriers face. China Mobile has the most cash to fund both the dividend and the buildout, which is exactly why it trades as the bloc's anchor rather than its option.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Tickers | 0941.HK (HK), 600941.SS (Shanghai) |
| Former ADR | CHL (NYSE, delisted 2021) |
| Close (0941.HK, 2026-06-12) | HK$81.80 |
| FY2025 revenue | RMB 1,050.19bn |
| FY2025 net income | RMB 137.10bn |
| Mobile customers | ~1.0bn (642mn 5G) |
| Net margin | ~13.1% |
| Annualized vol | ~11.8% (lowest in the bloc) |
| Controlling shareholder | China Mobile Group (SASAC) |
| HQ | [[Beijing]], [[China]] |

*Updated 2026-06-13 (deepdive). Prices verified against canonical DB closes (0941.HK HK$81.80, 2026-06-12).*

---

## Related

### Securities
- [[China Mobile securities note]] — H-share / A-share / delisted-ADR structure, price history, peer chart

### Peers / cluster
- [[China Unicom]] — bloc peer (0762.HK); carries the full cluster cohort analysis; higher-beta member
- [[China Telecom]] — bloc peer (0728.HK); the cloud/AI leader of the three
- [[China Tower]] — jointly-owned tower company

### Themes
- [[China special valuation]] — China special valuation / SOE value-up re-rating
- [[East Data West Compute]] — East Data West Compute; the national computing buildout
- [[Executive Order 13959]] — the 2021 NYSE delisting trigger

### Infrastructure
- [[Chile-China Express]] — submarine cable project (co-operator)
- [[Submarine Cables]] — infrastructure context
- [[US Chile cable visa sanctions]] — diplomatic fallout from the cable project

### Cross-vault
- [Geopolitics: Executive Order 13959](obsidian://open?vault=geopolitics&file=Events%2FExecutive%20Order%2013959) — the delisting in the US-China decoupling frame
