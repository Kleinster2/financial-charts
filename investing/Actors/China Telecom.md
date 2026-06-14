---
aliases: [CHA, China Telecom Corporation, 0728.HK, 601728.SS, 中国电信]
tags: [actor, china, telecom, soe]
---

#actor #china #telecom #soe

**China Telecom** — the third of [[China]]'s three state-owned carriers (with [[China Mobile]] and [[China Unicom]]), strong in fixed-line broadband and the clear cloud/AI leader of the bloc through Tianyi Cloud (天翼云), the #2 public-cloud IaaS provider in China. The strongest performer of the three telecoms in the 2021–2026 re-rating.

One-line read: China Telecom is the cloud-tilted, highest-beta-on-fundamentals member of the China-telecom bloc, with the forward bet being whether Tianyi Cloud (>RMB120bn revenue, #2 in China public cloud) and 91 EFLOPS of computing make it a genuine cloud platform inside an SOE wrapper rather than a flat-growth carrier with a dividend.

---

## Why China Telecom matters

| Metric | Value |
|--------|-------|
| Listings | [[China Telecom securities note\|0728.HK]] (Hong Kong), 601728.SS (Shanghai A-share) |
| Former ADR | CHA (NYSE, delisted 2021 under [[Executive Order 13959]]) |
| Mobile subscribers | 439mn (5G penetration 68.8%) |
| Broadband subscribers | 201mn (gigabit penetration 31.6%) |
| FY2025 revenue | RMB 523.93bn (~flat) |
| FY2025 net income | RMB 33.19bn (+0.5% YoY) |
| Tianyi Cloud revenue | >RMB 120bn (#2 China public-cloud IaaS) |
| Intelligent computing | 91 EFLOPS |
| Controlling shareholder | China Telecommunications Corporation (SASAC) |

China Telecom sits between its two peers on profitability (~6.3% net margin vs [[China Mobile]]'s ~13% and [[China Unicom]]'s ~5.3%) but leads decisively on cloud: Tianyi Cloud's >RMB120bn revenue dwarfs Mobile Cloud (RMB56bn H1) and Unicom's cloud, and ranks #2 in China's public-cloud IaaS market behind only [[Alibaba Cloud]]. That makes it the bloc's clearest "telecom-as-cloud-platform" expression.

---

## Financials

0728.HK reporting (RMB mn, IFRS/HKFRS):

| FY | Revenue | Operating income | Net income | Net margin |
|----|--------:|-----------------:|-----------:|-----------:|
| 2021 | 439,553 | 30,948 | 25,949 | 5.90% |
| 2022 | 481,448 | 33,427 | 27,593 | 5.73% |
| 2023 | 513,551 | 37,128 | 30,446 | 5.93% |
| 2024 | 523,569 | 39,117 | 33,012 | 6.30% |
| 2025 | 523,925 | 40,325 | 33,185 | 6.33% |

*Source: company reporting via StockAnalysis. Steady margin-led improvement — net income compounded ~6.3%/yr while net margin widened from 5.90% to 6.33%. Like the bloc, the top line has plateaued (~RMB524bn in 2024–2025); profit growth comes from cost control and mix shift toward higher-value services.*

*No fundamentals/Sankey/waterfall charts: [[Alpha Vantage]] provides no income-statement data for Hong Kong tickers (0728.HK), so the series above is sourced from company reporting. Cluster validation below uses price data, which is available.*

---

## Cloud and computing leadership

China Telecom's differentiator is Tianyi Cloud (天翼云):

- Revenue exceeded RMB120bn — the second-largest public-cloud IaaS provider in China behind [[Alibaba Cloud]], and far larger than either peer's cloud business.
- Intelligent computing capacity reached 91 EFLOPS — roughly double [[China Unicom]]'s 45 EFLOPS.
- Smart/AI-related revenue grew ~89% (H1 2025).

This is the same state-directed cloud/computing buildout the whole bloc is running (see [[East Data West Compute]]), but China Telecom is furthest along in turning it into a material business line. Where [[China Mobile]] is the dividend anchor and [[China Unicom]] the laggard/data-asset pioneer, China Telecom is the cloud platform — which is why it has been the strongest performer of the three since 2021.

---

## Shanghai return (2021)

China Telecom returned to the Shanghai exchange (601728.SS) in August 2021 via a ~RMB47bn IPO — a homecoming listing that, like [[China Mobile]]'s January 2022 A-share debut, coincided with the closing of US capital-markets access to Chinese champions. Its mainland listing predates China Mobile's by a few months.

---

## NYSE delisting (2021)

China Telecom's ADR (CHA) was removed from the NYSE in 2021 under [[Executive Order 13959]], alongside [[China Mobile]] (CHL) and [[China Unicom]] (CHU). Mechanics in [[China Telecom securities note]].

---

## Cluster validation

`scripts/cluster_configs/china_telecom.yaml` (China Telecom as primary). Full cohort analysis in [[China Unicom]]; the verdict is shared because the cohort is the same three names. China Telecom (0728.HK) trades as a member of a tight, durable China-telecom bloc.

| Diagnostic | Value | Read |
|---|---|---|
| Intra-cluster correlation (1Y) | 0.668 (range 0.62–0.75) | real co-movement; 0728–0762 the tightest pair at 0.75 |
| Hierarchical clusters (0.5 cut) | 3 clean groups | {0762, 0941, 0728} separate from {[[AT&T\|T]], [[Verizon\|VZ]], [[T-Mobile\|TMUS]]} and {[[FXI]], [[KWEB]], [[SPY]]} |
| PC1 explained variance | 77.9% | one dominant common factor |
| China Telecom ann. vol | 22.83% | highest in the bloc |
| Cluster vs china_etf / us_telecom | 0.19 / 0.05 | not generic China beta, not a global-telecom co-mover |
| Random-basket / vol-matched p (10k) | 0.0007 / 0.018 | validated — beats random and same-vol baskets; holdout STABLE 0.85 |

![[china-telecom-cluster-dendrogram-1y.png]]
*Three clean clusters at the 0.5 threshold — the China telecoms fuse with each other (0728 pairs first with 0762 at distance 0.25) long before joining US telecoms or the China/US-market ETFs.*

![[china-telecom-cluster-pca-1y.png]]
*PC1 explains 77.9% of cohort variance — a single common factor across the three carriers.*

China Telecom is the highest-volatility member of the bloc (22.8% annualized) and its best performer since 2021 (~+250% normalized) — the cloud-growth tilt on top of the shared dividend/value-up factor.

### Context test — telecom vs cloud vs SOE-energy

`scripts/cluster_configs/china_telecom_context.yaml`. To test whether [[Tianyi Cloud]] has pulled China Telecom toward the cloud complex (and whether the telecom bloc is really a telecom factor or just China-SOE-H-share beta), the three telecoms were clustered against the China cloud/internet complex ([[Alibaba|9988.HK]], [[Tencent|0700.HK]], [[Baidu|9888.HK]]), the SOE-energy majors ([[PetroChina|0857.HK]], [[CNOOC|0883.HK]], [[Sinopec|0386.HK]]), and ETF controls — all HK-listed for same-session correlations.

![[china-telecom-context-dendrogram-1y.png]]
*Five clean clusters at the 0.5 threshold: the three telecoms (blue) stay their own group; the cloud trio (purple) forms a separate tight cluster; the SOE-energy names (orange) cluster apart (Sinopec a singleton); KWEB+SPY are market beta. Notably the telecom and cloud branches are siblings — they join each other (~0.75) before anything else.*

| Relationship | Avg corr (1Y) | Read |
|---|---|---|
| Intra-telecom | 0.635 | the bloc holds |
| Telecom vs cloud | 0.253 | adjacent but not merged |
| Telecom vs SOE-energy | 0.219 | a telecom factor, not generic SOE-H-share beta |
| Telecom vs ETF | 0.027 | not market beta |

Two findings. First, the bloc is genuinely a telecom factor: the telecoms cluster separately from the SOE-energy majors (correlation 0.219 vs 0.635 intra), so this is not just "China state-champion H-share" beta. Second, despite Tianyi Cloud being #2 in China IaaS in the fundamentals, China Telecom still trades with [[China Unicom]] and [[China Mobile]] (joining them at distances 0.29 and 0.40), not with the cloud complex (correlation 0.253). The cloud story is real in the income statement but has not yet migrated into the stock's return behavior — the telecom and cloud clusters are sibling branches, the closest thing to a bridge, but the merge has not happened.

---

## What to watch

- Tianyi Cloud scale and margin — >RMB120bn and #2 in China IaaS; whether cloud keeps growing fast enough to re-rate China Telecom away from a pure utility multiple is the central question.
- Computing capacity — 91 EFLOPS and rising; the [[East Data West Compute]] buildout is the supply side of the cloud story.
- Dividend — like the bloc, the [[China special valuation]] re-rating rests on cash returns (FY2025 total dividend RMB0.272/share); payout trajectory matters.
- The bloc — PC1 ~78%; China Telecom co-moves with [[China Mobile]] and [[China Unicom]] on the shared policy factor, with cloud as its idiosyncratic tilt.

---

## Analysis

China Telecom is the most interesting of the three on fundamentals because it is the one with a credible non-utility growth story. Tianyi Cloud at >RMB120bn and #2 in China's public-cloud IaaS is not a rounding error bolted onto a connectivity business — it is a genuine cloud platform that happens to sit inside an SOE. That is why China Telecom has been the bloc's best performer since 2021 (~+250% vs Mobile's ~+180% and Unicom's ~+130%): the market is paying for cloud growth on top of the shared [[China special valuation]] dividend re-rating.

The cluster math complicates the stock-picking case, though. PC1 at ~78% means China Telecom still mostly trades the China-telecom factor — its cloud-driven outperformance shows up as the highest beta/volatility in the bloc (22.8% annualized), not as decoupling. So the cloud story is real in the fundamentals and visible in the levels, but on daily returns China Telecom remains a high-beta expression of the same policy trade rather than an independent cloud name. The investable question is whether Tianyi Cloud eventually grows large enough to break China Telecom out of the bloc — at which point it would start trading with [[Alibaba Cloud]] and the cloud complex rather than with [[China Mobile]] and [[China Unicom]]. The context test above answers it empirically for now: it has not happened. China Telecom clusters with its telecom peers, not with [[Alibaba]]/[[Tencent]]/[[Baidu]] (telecom-vs-cloud correlation 0.253 vs 0.635 intra-bloc) — though the telecom and cloud branches are statistical siblings, the nearest thing to a bridge. The cloud tilt is visible in the fundamentals and in the levels (China Telecom's outperformance) but not yet in daily co-movement. The signal to watch is the telecom-vs-cloud correlation rising over time — that would be the cluster fracturing in real time.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Tickers | 0728.HK (HK), 601728.SS (Shanghai) |
| Former ADR | CHA (NYSE, delisted 2021) |
| Close (0728.HK, 2026-06-12) | HK$4.91 |
| FY2025 revenue | RMB 523.93bn |
| FY2025 net income | RMB 33.19bn |
| Mobile subscribers | 439mn |
| Broadband subscribers | 201mn |
| Tianyi Cloud revenue | >RMB 120bn (#2 China IaaS) |
| Intelligent computing | 91 EFLOPS |
| Annualized vol | ~22.8% (highest in the bloc) |
| HQ | [[Beijing]], [[China]] |

*Updated 2026-06-13 (deepdive). Prices verified against canonical DB closes (0728.HK HK$4.91, 2026-06-12).*

---

## Related

### Securities
- [[China Telecom securities note]] — H-share / A-share / delisted-ADR structure, price history, peer chart

### Peers / cluster
- [[China Unicom]] — bloc peer (0762.HK); carries the full cluster cohort analysis
- [[China Mobile]] — bloc peer (0941.HK); the dividend anchor
- [[China Tower]] — jointly-owned tower company

### Themes
- [[Tianyi Cloud]] — its #2-in-China public cloud platform
- [[Alibaba Cloud]] — #1 China public cloud; the name China Telecom would trade with if cloud broke it out of the bloc
- [[China special valuation]] — China special valuation / SOE value-up re-rating
- [[East Data West Compute]] — East Data West Compute; the national computing buildout
- [[Executive Order 13959]] — the 2021 NYSE delisting trigger

### Cross-vault
- [Geopolitics: Executive Order 13959](obsidian://open?vault=geopolitics&file=Events%2FExecutive%20Order%2013959) — the delisting in the US-China decoupling frame
