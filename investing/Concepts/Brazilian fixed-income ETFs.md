---
aliases: [Brazilian fixed-income ETFs, B3 fixed-income ETFs, renda fixa ETF, LFTS11, LFTB11, Brazil cash ETF]
tags: [concept, fixed-income, etf, brazil]
---
#concept #fixed-income #etf #brazil

# Brazilian fixed-income ETFs

A family of B3-listed ETFs that hold Brazilian government fixed income — Tesouro Selic (floating / cash), IPCA-linked (IMA-B), and prefixado (IRF-M). Their pitch is a liquid, low-cost, exchange-traded cash-and-duration sleeve: an alternative to a bank [[CDB]] or a renda-fixa fund for parking and managing the fixed-income allocation, taxed at the 15% long-term bracket.

## The cash-sleeve use

In a Carteira Aberta portfolio review, the guest described moving his "caixa" (cash) out of bank renda-fixa funds and into these B3 ETFs — for the lower tax and daily liquidity. The Tesouro Selic ETF (LFTS11) is the money-market proxy: floating-rate, near-flat accrual, the cash leg of a portfolio.

## Correlation — it depends entirely on duration

The convenient shorthand that "Brazilian fixed-income ETFs are uncorrelated with equities" is only true for the cash leg. Daily-return correlation to [[EWZ]] (Brazilian equities), last ~2 years:

| ETF | Tracks | vs EWZ |
|-----|--------|--------|
| LFTS11 | Tesouro Selic (cash) | 0.08 |
| [[IRFM11]] | IRF-M prefixado | 0.39 |
| [[FIXA11]] | prefixado (futures) | 0.39 |
| [[IMAB11]] | IMA-B (IPCA, full duration) | 0.39 |
| [[B5P211]] | IMA-B 5 (short IPCA) | 0.41 |
| [[IB5M11]] | IMA-B 5+ (long IPCA) | 0.47 |

The floating-rate cash ETF (LFTS11, 0.08) is genuinely uncorrelated. But the duration ETFs carry real Brazil-rate beta (0.39–0.47, rising with duration) that overlaps with equities — because Brazilian stocks and long bonds both rally when the rate cycle turns (a Selic-cut expectation re-rates both). So the longer the duration, the more a "fixed-income" ETF shares the local rate-and-risk factor with the Ibovespa. Only the cash sleeve is a true diversifier; the duration sleeve is a leveraged bet on the same Brazil-rate cycle the equity book already rides.

![[br-fi-etf-duration-chart.png]]
*Normalized — LFTS11 (Selic / cash, near-flat) vs [[IMAB11]] (IPCA duration) vs [[IRFM11]] (prefixado). The cash line barely moves; duration adds the volatility that correlates with the Brazil cycle.*

![[br-fi-etf-vs-ewz-chart.png]]
*LFTS11 (cash) vs [[EWZ]] — the cash-vs-equity contrast.*

## The family (all tracked)

| Ticker | Tracks | Role |
|--------|--------|------|
| LFTS11 | Tesouro Selic (Investo Teva) | Cash / floating-rate money-market proxy |
| LFTB11 | Short Treasury 7–60 day (Investo MarketVector) | Cash-like; newly listed, only a stub price series so far |
| [[IMAB11]] | IMA-B (IPCA) | Full IPCA duration |
| [[B5P211]] | IMA-B 5 | Short IPCA duration (≤5y) |
| [[IB5M11]] | IMA-B 5+ | Long IPCA duration (5y+) |
| [[IRFM11]] | IRF-M | Prefixado duration |
| [[FIXA11]] | Prefixado (S&P/B3 rate futures) | Prefixado, futures-based |

The cash ETFs (LFTS11, LFTB11) live in this note; each duration ETF has its own note (linked above).

## Watch-outs

- Still smaller and less liquid than the US fixed-income ETF market — wider spreads and tracking error.
- The 15% tax rate applies only after the long-term holding period; short-term trades hit a higher bracket.
- The duration ETFs are not a cash substitute — they carry mark-to-market and rate risk, plus the equity-overlapping beta above. For an actual cash sleeve, LFTS11 is the only one that behaves like cash.

## Related

- [[Brazilian fixed income]] — the broader retail fixed-income menu
- [[CDB]] — the bank-deposit alternative for the cash sleeve
- [[FII]] — the listed real-estate B3 fund family
- [[EWZ]] — Brazil equity benchmark (the correlation reference)
