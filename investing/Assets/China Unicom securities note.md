---
aliases: [0762.HK, 600050.SS, CHU, China Unicom Hong Kong stock, China Unicom shares]
tags: [security, china, telecom, h-share, adr-delisted]
---

#security #china #telecom

**China Unicom securities note** — the tradeable instruments of [[China Unicom]]. The company has two live listings and one delisted line: the Hong Kong H-share (0762.HK, primary), the Shanghai A-share (600050.SS), and the former NYSE ADR (CHU), removed in 2021. This note carries the instrument structure, price history, and trading relationships; the business and strategy live in [[China Unicom]].

---

## Instruments

| Line | Ticker | Venue | Status |
|---|---|---|---|
| H-share | 0762.HK | Hong Kong (HKEX, June 2000) | live — primary |
| A-share | 600050.SS | Shanghai (2002) | live |
| ADR | CHU | NYSE | delisted May 2021 |

The H-share (0762.HK) is the cleanest proxy for the operating telecom and the line tracked in the database (6,468 daily closes back to June 2000). The A-share (600050.SS) is the entity where the 2017 mixed-ownership reform investors ([[Tencent]], [[Alibaba]], [[Baidu]], [[JD.com]], China Life) hold their stakes; it trades at a structurally different valuation from the H-share (the persistent A/H premium). The ADR is dead — see below.

---

## ADR delisting (2021)

China Unicom's ADR (CHU) was forcibly delisted from the NYSE in 2021 under [[Executive Order 13959]], the November 2020 order barring US persons from holding securities of designated "Communist Chinese military companies." Timeline:

- Dec 31, 2020 — NYSE announces intent to delist CHU, CHL ([[China Mobile]]), CHA ([[China Telecom]]).
- Jan 4, 2021 — NYSE reverses after consulting regulators.
- Jan 6, 2021 — NYSE reverses again, proceeds with delisting.
- Jan 11, 2021 — NSCC withdraws clearing services; without clearing, trading cannot occur.
- May 2021 — formal Form 25-NSE filed; ADRs removed from listing and registration.

US holders were left to convert to the Hong Kong line or exit. The episode is a clean, early case of US-China capital-markets decoupling — the securities were delisted for the issuer's identity, not any disclosure or financial failing.

---

## Price history

0762.HK closed HK$7.20 (2026-06-12). The instrument's defining feature is the 2021–2026 re-rating: after years as a flat, unloved utility (the blue line spent 2021–2022 below its starting level), all three Chinese telecoms inflected upward through 2023–2025 on the [[China special valuation|China special-valuation / SOE value-up theme]] — high dividend yield, state "national team" buying, capex discipline turning into free cash flow. A shared step-change in early 2025 lifted the whole bloc.

![[0762.HK-vs-0941.HK-vs-0728.HK-price-chart.png]]
*0762.HK (blue) vs [[China Mobile\|0941.HK]] (red) and [[China Telecom\|0728.HK]] (green), normalized from January 2021. China Telecom led (~+250%), China Mobile next (~+180%), China Unicom the laggard (~+130%) — but all three trace the same path, the visible signature of the China-telecom cluster. The early-2025 common jump is the bloc re-rating in unison.*

China Unicom is the laggard and the highest-volatility member of the bloc (21.7% annualized vs China Mobile's 11.8%): it moves with the group but underperforms the re-rating, which makes it the higher-beta way to express the same China-telecom-policy view.

---

## Trading relationships

Cluster validation (`scripts/cluster_configs/china_telecom.yaml`, full diagnostics in [[China Unicom]]) establishes that 0762.HK trades as a member of a tight, durable China-telecom bloc:

- Intra-bloc correlation 0.668 (1Y); the three telecoms form a clean hierarchical cluster separate from US telecoms and China ETFs.
- PC1 explains 77.9% of cohort variance — one dominant common factor.
- Correlation to US telecoms ([[AT&T|T]]/[[Verizon|VZ]]/[[T-Mobile|TMUS]]) just 0.05; to China ETFs ([[FXI]]/[[KWEB]]) just 0.19 — neither a global-telecom nor a generic-China-beta instrument.

Hedge/expression: 0762.HK is hedgeable against 0941.HK and 0728.HK (same factor), but offers little diversification against them; it is not a substitute for, nor hedged by, global telecoms or a broad China ETF.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Primary ticker | 0762.HK |
| Close (2026-06-12) | HK$7.20 |
| DB history | 6,468 closes from 2000-06-22 |
| Annualized vol | ~21.7% (highest in the bloc) |
| A-share line | 600050.SS |
| Delisted ADR | CHU (NYSE, 2021) |
| Market cap | ~HK$220bn |

*Created 2026-06-12. Prices verified against canonical DB closes.*

---

## Related

- [[China Unicom]] — the operating business, financials, strategy, cluster diagnostics
- [[China Mobile]] — cluster peer (0941.HK)
- [[China Telecom]] — cluster peer (0728.HK)
- [[Executive Order 13959]] — the ADR delisting trigger
- [[China special valuation]] — the SOE value-up re-rating driving the 2021–2026 price action
