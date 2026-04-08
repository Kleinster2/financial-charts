---
aliases: [zero-day options, 0DTE, zero-day-to-expiry options]
---
#concept #derivatives #market-structure

**0DTE options** — Options contracts expiring the same day they are traded. Became dominant force in US equity markets after [[CBOE]] introduced daily SPX expirations in 2022, growing from ~5% to ~50% of SPX options volume by 2024.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Share of SPX options volume | ~50% (2024) |
| Daily expirations introduced | 2022 ([[CBOE]]) |
| Primary index | SPX (S&P 500) |
| Primary participants | Retail traders, market makers, hedge funds |

---

## US options volume growth

![[us-options-daily-volume-2023-2025.png]]
*Average number (mn) of contracts traded daily in the US. Source: Bloomberg Intelligence.*

US options volumes have tripled since 2019. As of mid-2025, approximately 61mn contracts change hands daily (Bloomberg Intelligence), up from ~42mn in early 2023. The growth has been supercharged by the popularity of 0DTE products used to navigate daily market shifts, and has attracted new exchange entrants — [[IEX]] applied in Sep 2025 to add options, becoming the 19th platform.

*Source: [[Financial Times]] (Sep 1, 2025), Bloomberg Intelligence*

---

## Mechanics

Prior to 2022, SPX options expired only on Mondays, Wednesdays, and Fridays. [[CBOE]] filled the gaps with Tuesday and Thursday expirations, enabling daily 0DTE trading. The result: a contract bought at market open expires worthless or in-the-money by 4 PM — binary-like payoffs at options pricing.

Retail traders use 0DTE for directional bets with defined risk and rapid resolution. The appeal is identical to [[Ultra-short-term contracts]] on [[prediction markets]]: instant feedback, small stakes, lottery-ticket payoffs.

---

## Gamma risk

Dealer hedging of large near-expiry option positions can amplify intraday moves. When a wall of 0DTE puts expires near the money, dealers sell futures to stay delta-neutral, accelerating selloffs. The reverse applies with calls. [[JPMorgan]] and others have flagged this as a structural fragility — the same hedging flows that dampen volatility when options are far from expiry can spike it when they're near the money at expiry.

The magnitude of this risk is debated. [[CBOE]] and some academics argue 0DTE flows are diversified enough that gamma effects net out. Market makers counter that concentrated positioning around round-number strikes creates flash-crash conditions.

---

## Related

- [[Ultra-short-term contracts]] — broader trend across derivatives, prediction markets, binary options
- [[Prediction markets]] — 5/15-minute crypto bets as the prediction market equivalent
- [[CBOE]] — introduced daily SPX expirations enabling 0DTE
- [[Derivatives]] — 0DTE options are a derivative instrument
- [[IEX]] — new options platform application driven by volume boom
- [[Latency arbitrage]] — amplified in options markets
- [[Market structure]] — exchange competition context
