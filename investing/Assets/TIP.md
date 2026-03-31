---
aliases: [TIPS, Treasury Inflation-Protected Securities, iShares TIPS Bond ETF, iShares TIPS, inflation-linked bonds, linkers]
tags: [actor, etf, fixed-income]
ticker: TIP
---

# TIP

**TIP** is the iShares TIPS Bond ETF ([[BlackRock]]), tracking Treasury Inflation-Protected Securities — US government bonds whose principal adjusts with CPI. The largest TIPS ETF by AUM and the standard vehicle for inflation-linked exposure. TIPS are issued by the [[US Treasury]] in 5, 10, and 30-year maturities with quarterly auctions.

---

## Synopsis

TIPS occupy a unique position in fixed income: they guarantee a real return by adjusting principal to CPI, but they carry duration risk like any long bond. The trade-off is the core tension. In a demand-shock recession (2008, 2020), nominal [[Treasuries]] rally harder because deflation fears compress breakevens — TIPS underperform. In a supply-shock stagflation (1970s, 2022, March 2026), TIPS should outperform because inflation adjustment compensates for price declines. But the March 2026 [[2026 Iran conflict market impact|Iran conflict]] tested this directly and the result was mixed: TIPS duration losses partially offset the inflation linkage as real rates repriced higher alongside nominal rates. [[Gama Asset Management]]'s [[Rajeev de Mello]] (Mar 13, 2026): *"Inflation-linked bonds and gold isn't protecting portfolios."*

The structural question is whether TIPS can hedge inflation when the [[Stock-Bond Correlation Regime]] is positive. In negative-correlation eras (2000-2020), falling equities meant falling yields, so bond duration was a feature. In positive-correlation regimes (stagflation), duration becomes a liability — bonds and equities fall together, and TIPS' CPI adjustment can't overcome a 10-year duration hit from rising real rates. This is why [[ALLW]] (21.5% TIPS) and [[RPAR ETF|RPAR]] (0% TIPS, 27% commodities) represent opposing bets on which inflation hedge survives the regime shift.

---

## Sector correlation

> [!warning] Sector Orphan
> TIP does not trade tightly with any sector ETF (max r = 0.27 with XLU).

| Sector | ETF | Correlation |
|--------|-----|-------------|
| Utilities | XLU | 0.27 |
| [[Consumer Staples]] | XLP | 0.27 |
| [[Real estate\|Real Estate]] | XLRE | 0.24 |
| *S&P 500* | *SPY* | *0.00* |

TIP trades between Utilities and Consumer Staples without a tight sector fit.

---

## Price performance

![[tip-vs-tlt-price-chart.png]]
*TIP vs [[TLT]] normalized since Jan 2022. TIP roughly flat (+1%) while TLT down ~30% — the CPI principal adjustment has fully offset the 2022-2026 rate shock for TIPS, but not for nominal long bonds. The gap is cumulative inflation realized since 2022.*

---

## How TIPS work

The US Treasury issues TIPS with a fixed real coupon. The principal adjusts semi-annually based on the non-seasonally adjusted CPI-U (Consumer Price Index for All Urban Consumers).

| Feature | Mechanism |
|---------|-----------|
| Principal | Adjusts with CPI — if CPI rises 3%, principal rises 3% |
| Coupon | Fixed real rate applied to adjusted principal |
| Maturity | Par or adjusted principal, whichever is greater (deflation floor) |
| Tax treatment | Phantom income — CPI adjustment is taxable annually even though not received until maturity |
| Maturities | 5, 10, 30 years |
| Auction frequency | Quarterly |

The deflation floor means TIPS holders never receive less than par at maturity, even if cumulative CPI is negative.

---

## Breakeven inflation

The breakeven rate is the market's implied inflation expectation, derived from the spread between nominal Treasuries and TIPS of the same maturity.

Breakeven = Nominal yield - TIPS real yield

| Measure | Calculation | Jan 2026 |
|---------|-------------|----------|
| 5-year breakeven | 5Y Treasury - 5Y TIPS | 2.42% |
| 10-year breakeven | 10Y Treasury - 10Y TIPS | ~2.3% |
| 5Y5Y forward | Expected 5Y inflation starting 5Y from now | ~2.2% |

If actual inflation exceeds the breakeven, TIPS outperform nominals. If inflation undershoots, nominals win. The breakeven is not a pure inflation forecast — it includes a liquidity premium (TIPS are less liquid than nominals) and an inflation risk premium.

See [[Inflation expectations]] for the full framework (survey-based vs market-based measures, Fed's CIE index).

---

## The duration problem

TIPS carry the same interest rate sensitivity as nominal bonds of similar maturity. A 10-year TIPS has ~8-9 years of duration. When real rates rise, TIPS prices fall — regardless of the inflation adjustment.

This creates the paradox: TIPS are an inflation hedge that can lose money during inflationary episodes if real rates rise simultaneously.

| Scenario | Nominal bonds | TIPS | Winner |
|----------|--------------|------|--------|
| Demand shock (deflation fears) | Rally hard | Rally less | Nominals |
| Supply shock (inflation + growth) | Fall | Fall less (CPI offsets) | TIPS |
| Stagflation + rate repricing | Fall | Fall (duration > CPI offset) | Neither |
| Disinflation (falling inflation, stable rates) | Rally | Rally less | Nominals |

2022: TIPS lost ~12% (TIP ETF) despite inflation running at 6-9%. Real rates surged from -1% to +1.5%, overwhelming the CPI adjustment. [[Bridgewater]]'s institutional All Weather reportedly lost ~22%.

March 2026: The [[Iran conflict portfolio hedging|correlation breakdown]] — bonds and stocks falling together on Hormuz oil shock stagflation — tested TIPS again. 2Y yields rose ~9bp on Mar 12 while equities fell 1.5%.

---

## Risk parity positioning

TIPS allocation is the key differentiator between competing risk parity funds:

| Fund | TIPS | Commodities | Logic |
|------|------|-------------|-------|
| [[ALLW]] | 21.5% | 8.5% | Bridgewater model — TIPS as primary inflation sleeve |
| [[RPAR ETF\|RPAR]] | 0% | 27.1% | ARIS model — commodities as inflation hedge instead |
| [[UPAR ETF\|UPAR]] | 0% | ~27% | Leveraged RPAR, same 0% TIPS bet |

The ALLW vs RPAR divergence is a live experiment: TIPS-based inflation hedging vs commodity-based. Through March 2026, RPAR's commodity tilt outperformed ALLW's TIPS tilt.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | TIP |
| Issuer | [[BlackRock]] (iShares) |
| Index | Bloomberg US TIPS Index |
| Inception | December 2003 |
| Expense ratio | 0.19% |
| Exchange | NYSE Arca |
| Duration | ~6.5 years (fund average) |

Other TIPS ETFs: STIP (short-duration), VTIP ([[Vanguard]], short), SCHP ([[Schwab]], broad).

---

## Related

- [[Treasuries]] — TIPS as one of five Treasury security types
- [[Inflation expectations]] — breakeven framework, survey vs market measures
- [[Inflation]] — TIPS as row 1 in inflation hedges taxonomy
- [[Stock-Bond Correlation Regime]] — determines whether TIPS duration is feature or bug
- [[ALLW]] — 21.5% TIPS allocation, Bridgewater All Weather
- [[RPAR ETF]] — 0% TIPS, commodity-based alternative
- [[Risk Parity]] — TIPS as inflation-linked sleeve
- [[Iran conflict portfolio hedging]] — March 2026 case study of TIPS-as-hedge failure
- [[Russell Napier]] — financial repression thesis (real yields kept below inflation)
- [[Lyn Alden]] — fiscal dominance, structurally suppressed real yields
