---
aliases:
  - Nasdaq-100
  - NDX
  - Nasdaq 100 Index
tags:
  - concept
  - index
  - equities
---

# Nasdaq 100

The Nasdaq 100 is Nasdaq's large-cap non-financial growth index, tracked by [[QQQ]] and used as the flagship benchmark for the largest [[Nasdaq]]-listed technology and tech-enabled companies.

---

## Synthesis

The Nasdaq 100 is no longer a simple total-market-cap proxy for the biggest Nasdaq-listed companies. The May 1 2026 methodology update keeps full company market capitalization as the ranking and Fast Entry test, but uses modified market capitalization for weighting: only eligible listed share classes count, and low-float securities have their total shares outstanding capped at three times free-floating shares. That hybrid is the important distinction for [[SpaceX IPO 2026]]: a low-float mega-IPO can qualify because it is huge, but it does not receive a full $1.75T-$1.77T index weight on day one.

The design sits between pure float adjustment and full-market-cap weighting. A float-adjusted total-market index would treat a $75B public float as roughly $75B of investable market value. The Nasdaq 100 low-float cap can treat that same $75B float as up to about $225B for weighting, subject to final share-class treatment, price, free-float files, interpolation, and concentration caps. That is still much smaller than full economic value, but materially larger than a pure public-float weight.

---

## Quick stats

| Metric | Value |
|---|---|
| Ticker | NDX |
| ETF proxy | [[QQQ]] |
| Sponsor | [[Nasdaq]] |
| Constituents | 100 largest eligible Nasdaq-listed non-financial companies, plus temporary excess constituents after Fast Entry events |
| Ranking metric | Full market capitalization, including listed and unlisted shares for direct listings and primary ADRs |
| Weighting metric | Modified market capitalization |
| Low-float weighting cap | Lesser of reported TSO or 3x free-floating shares for each eligible listed security |
| Fast Entry | IPOs ranking in the top 40 current constituents can typically enter after 15 trading days |

## May 2026 methodology update

Nasdaq implemented the updated methodology on May 1, 2026 after a February consultation. The relevant mechanics:

| Mechanic | Treatment |
|---|---|
| Eligibility/ranking | Full company market capitalization is used for direct listings and primary ADRs, including listed and unlisted shares |
| Weighting | Modified market capitalization is used; foreign-listed and unlisted shares are disregarded |
| Low float | No minimum free-float criterion, but low-float securities are capped at three times free-floating shares for weighting |
| Fast Entry | IPOs are ranked after the seventh trading day and are typically added after 15 trading days if they rank in the top 40 |
| Temporary count | Fast Entry additions can temporarily lift the index above 100 constituents |

The practical result is a graduated weight path. As more shares become public float, a low-float security can move toward full listed-share weighting at scheduled rebalance dates rather than entering at either zero weight or full market capitalization immediately.

Sources: [Nasdaq methodology PDF](https://indexes.nasdaq.com/docs/Methodology_NDX.pdf), accessed Jun. 7 2026; [Nasdaq 2026 NDX changes FAQ](https://indexes.nasdaqomx.com/docs/2026_May_NDX_Changes_FAQ.pdf), accessed Jun. 7 2026; [Nasdaq methodology update interview](https://www.nasdaq.com/newsroom/nasdaq100-index-methodology-update-why-now), accessed Jun. 7 2026.

## Correlation structure

Use [[QQQ]] as the tradable proxy for Nasdaq 100 exposure. The index's day-to-day factor load is large-cap growth, software, semiconductors, and AI infrastructure, while the May 2026 low-float rules matter through inclusion weight and passive-flow mechanics rather than through a separate return factor.

## Related

- [[Nasdaq]] - index sponsor and listing venue
- [[QQQ]] - ETF proxy
- [[Nasdaq Fast Entry Rule]] - 2026 fast-entry and low-float methodology change
- [[Float-adjusted market capitalization]] - investable-float weighting concept
- [[SpaceX IPO 2026]] - current low-float mega-IPO test case
