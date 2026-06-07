---
aliases: [SOX, PHLX SOX, Philadelphia Semiconductor Index, PHLX Semiconductor Sector Index]
tags: [concept, index, semiconductors, benchmark]
---

# PHLX Semiconductor

The Philadelphia Semiconductor Index (ticker SOX), a Nasdaq-administered, modified market-cap-weighted benchmark of 30 of the largest US-listed semiconductor companies — design, manufacturing, equipment, and distribution. The standard reference gauge for the semiconductor cycle and the headline number in chip-rally reporting.

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | SOX |
| Administrator | Nasdaq (formerly Philadelphia Stock Exchange) |
| Constituents | 30 largest US-listed semiconductor names |
| Weighting | Modified market-cap |
| Tradeable proxies | [[SOXX]] (iShares), [[SMH]] (VanEck) |

The SOX index itself is not stored in `prices_long`; the vault tracks it through the [[SOXX]] and [[SMH]] ETF proxies. Reported moves: +65% YTD through May 8 2026 ([[Reuters]]); roughly +75% YTD by May 28 2026 (FT) — the best start to a year since the 1999 dotcom peak, with [[SOXX]] confirming +79.9% YTD at the May 27 close.

## Correlation structure

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Avg correlation | 0.982 | [[SOXX]] / [[SMH]] proxy correlation over trailing 252 sessions through Jun. 5 2026 |
| Stored proxy | [[SOXX]], [[SMH]] | SOX index level is not stored directly in `prices_long` |
| Sector role | Benchmark, not cluster note | Headline semiconductor-cycle gauge |
| Jun. 5 beta | SOXX beta to [[QQQ]] 1.93 | Index proxy behaves like high-beta AI/tech exposure |
| Jun. 5 residual | -1.17pp vs QQQ-implied SOXX move | Additional chip pressure, but not a pure semiconductor break |

The SOX is the reporting benchmark for semiconductor tape, while the tradable analysis lives in [[SOXX]], [[SMH]], and the child clusters under [[Semiconductors]].

## Jun. 5 2026 drawdown

FT reported the PHLX Semiconductor Index down 10.3% on Jun. 5, 2026, its worst one-day fall since March 2020. The vault proxies match the magnitude: [[SOXX]] closed -10.44% and [[SMH]] -9.22%, versus [[QQQ]] -4.80% and [[SPY]] -2.58%. See [[Nasdaq semiconductor selloff June 2026]] for the full event tape.

The important attribution nuance is beta. SOXX's 90-session beta to QQQ was 1.93, so QQQ's -4.80% implied about -9.27% for SOXX before alpha; the actual -10.44% left a -1.17 percentage-point beta-adjusted shortfall. The selloff was therefore not a pure semiconductor idiosyncratic break. It was a broad AI-duration/rates shock with additional chip-specific pressure layered on top.

*Sources: [FT](https://www.ft.com/content/2929bbd3-1f71-4424-a577-f016c3c65603), Jun. 5 2026; local `prices_long` closes through Jun. 5 2026.*

## Related

- [[Semiconductors]] — parent sector hub; dated rally series tracks SOX moves
- [[SOXX]], [[SMH]] — tradeable ETF proxies
- [[AI capex arms race]] — demand backdrop driving the index
- [[Jonathan Krinsky]] — flagged 25-30% SOX correction risk (May 8 2026)

---

*Stub created 2026-05-29*
