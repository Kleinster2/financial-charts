---
aliases: [bond term premium, Treasury term premium, TP]
tags:
  - concept
  - rates
  - macro
  - fixed-income
---

# Term premium

The extra yield investors demand for holding long-duration bonds beyond their expectations for the path of short-term rates. When nominal yields rise but rate expectations and inflation expectations are unchanged, the move is term premium — compensation for uncertainty, not a forecast.

---

## Yield decomposition

Nominal bond yield = Expected path of short-term rates + Expected inflation + Term premium

The three components are not directly observable individually. Decomposition requires models or market proxies:

| Component | What it captures | Observable proxy |
|-----------|-----------------|------------------|
| Expected short rates | Where markets think the [[Federal Reserve\|Fed]] is heading | [[Fed Funds futures (ZQ)]], [[SOFR futures (SR3)]]. See [[Rate expectations]] |
| Expected inflation | Where markets think CPI/PCE is heading | Breakeven inflation (nominal Treasury minus [[TIP\|TIPS]]), inflation swaps. See [[Inflation expectations]] |
| Term premium | Residual: everything else | NY Fed ACM model, Fed Board Kim-Wright model |

The term premium is the residual — what's left after stripping out rate expectations and inflation expectations from the nominal yield. It's not directly tradeable, but it's the most important signal for understanding *why* long yields move.

---

## How to observe term premium

### NY Fed ACM model (Adrian-Crump-Mohanty)

The standard reference. Published monthly by the [[NY Fed]]. Decomposes the 10-year Treasury yield into expected average short rates over 10 years and the term premium. Uses a three-factor affine term structure model estimated from yield curve data.

Interpretation: when ACM term premium rises while Fed rate expectations are stable, it means investors are demanding more compensation for holding duration — not expecting tighter policy.

### Fed Board Kim-Wright model

Similar decomposition, different methodology. Uses survey expectations (Blue Chip, SPF) as inputs alongside yield curve data. Tends to produce smoother term premium estimates than ACM.

### Market-based triangulation

Even without the models, you can triangulate:

1. Check [[Rate expectations|Fed rate expectations]] ([[Fed Funds futures (ZQ)|ZQ]] / [[SOFR futures (SR3)|SR3]] futures) — are expected short rates moving?
2. Check [[Inflation expectations|breakeven inflation]] (TIPS spreads, 5Y5Y forward swaps) — are inflation expectations moving?
3. If nominal 10Y yield is rising but (1) and (2) are stable, the move is term premium

This is exactly the decomposition that identified the Apr 2026 bond sell-off as fiscal-driven rather than inflation-driven. See [[Fiscal Dominance#2026 oil shock — the regime's first test (Apr 2026)|Fiscal Dominance § 2026 oil shock]].

---

## What drives term premium

| Driver | Mechanism | Direction |
|--------|-----------|-----------|
| Fiscal deficit fears | More supply of bonds + uncertainty about debt sustainability | Higher |
| Treasury supply/demand imbalance | Auction sizes growing, foreign buyers retreating | Higher |
| Safe-haven status erosion | If [[Treasuries]] lose flight-to-safety bid, holders demand more | Higher |
| Inflation uncertainty (not level) | Even if expected inflation is 2.5%, *variance* around that matters | Higher |
| Central bank credibility loss | If Fed seen as fiscally dominated, long bonds carry regime risk | Higher |
| QE / central bank buying | Removes duration from market, compresses premium | Lower |
| Flight to safety (crises) | Demand surge for safe assets | Lower |

---

## Term premium vs. inflation expectations

Both push nominal yields higher, but the policy implications are opposite:

| | Rising inflation expectations | Rising term premium |
|--|-------------------------------|-------------------|
| Signal | Market expects higher future prices | Market wants more compensation for uncertainty/risk |
| Fed response | Tighten (raise rates) | Ambiguous — can't fix fiscal fears with rate policy |
| Observable in | Breakevens, inflation swaps, 5Y5Y forward | ACM/Kim-Wright residual; stable breakevens + rising nominal yields |
| Historical precedent | 1970s oil shocks | 2025-2026 fiscal expansion + Hormuz shock |

This distinction matters: if yields rise on inflation expectations, the Fed can respond with hikes. If yields rise on term premium (fiscal fear), the Fed is irrelevant — the problem is the borrower ([[Treasuries|Treasury]]), not the price level.

---

## April 2026: fiscal term premium

The [[2026 Strait of Hormuz crisis|Iran-Hormuz oil shock]] produced a textbook case of term premium isolation:

| Metric | Value | Implication |
|--------|-------|-------------|
| 10Y UST yield | +50bps since conflict began (to ~4.5%) | Nominal yields rising |
| 1Y inflation swaps | +60bps (to >3.1%) | Short-term inflation priced in |
| 5Y5Y forward | Flat at ~2.4% | Long-term expectations anchored |
| Fed rate expectations | 77.5% prob holds through year-end | No policy change priced |
| Fed inflation miss | 60 consecutive months above 2% target | Credibility strained but expectations anchored |

With inflation expectations stable and rate expectations unchanged, the yield rise is term premium. [[Ruchir Sharma]] ([[Rockefeller International]], FT Apr 6): markets fear the oil shock will trigger more fiscal spending on top of record deficits ($348tn global debt, US deficit ~6% GDP) — the term premium reflects fiscal overextension, not commodity-driven inflation.

Historical contrast: 1970s oil shocks pushed long rates up via inflation expectations (unanchored, pre-Volcker). 2026 pushes long rates up via term premium (anchored expectations but [[Fiscal Dominance|fiscal exhaustion]]). Different mechanism, different policy implications — and the Fed can't address the 2026 version with rate tools.

*Sources: FT (Apr 3, 2026 — Herbert/Smith), Ruchir Sharma FT (Apr 6, 2026)*

---

## June 2026 — falling breakevens, rising nominal

The [[US-Iran framework deal June 2026|Hormuz deal]] turned the April term-premium case into its cleaner form. In April the diagnostic was stable breakevens plus rising nominal yields, so the residual was term premium. By June the breakevens were not merely stable but falling: one- and two-year US inflation swaps collapsed to about 2.45% as oil round-tripped (see [[Inflation expectations#June 2026 — the expectations collapse, and the decoupling from rates|Inflation expectations]]), while the 2-year [[Treasuries|Treasury]] yield held near 4.1-4.2% and the [[Fed Funds futures (ZQ)|Dec-2026 fed funds future]] rose toward about 3.9%.

| Metric | April 2026 | June 2026 |
|--------|-----------|-----------|
| Inflation expectations (1yr swap) | rising (>3.1%) | falling (~2.45%) |
| Nominal 2yr UST | rising | held high (~4.1-4.2%) |
| Implied policy path | flat-to-up | up (Dec-26 fed funds ~3.9%) |
| Residual read | term premium (stable breakevens) | real rate + term premium (falling breakevens) |

![[term-premium-chart.png]]
*Kim-Wright 10Y term premium (blue) vs the 10Y [[Treasuries|Treasury]] yield (red), both in percent, 2010-2026. The term premium ran near zero or negative through the 2016-2021 low-rate/QE era, normalized across 2022-2024, and rose from ~0.46% (late Feb 2026) to ~0.80% (Jun 5) before settling ~0.75% on Jun 18 — still climbing through May-June even as breakevens fell, which is the residual this section describes. Source: Federal Reserve Board Kim-Wright model (FRED `THREEFYTP10`) and `DGS10`; see [[Treasuries]] for the nominal-yield series. The NY Fed ACM model gives a comparable but distinct estimate.*

When nominal yields hold or rise while inflation expectations fall, the real yield is rising mechanically, and the part not explained by a higher expected policy path is term premium. [[Toby Nangle]] (FT, Jun 18) attributes the move to a credibly hawkish [[Kevin Warsh|Warsh]]-led [[Federal Reserve|Fed]] plus a run of strong data — a real-rate/policy story more than a pure fiscal-term-premium one — while the [[Fiscal Dominance|fiscal]] component from April (about $348tn global debt, a US deficit near 6% of GDP) still sits underneath. The distinction matters for the same reason as in April: a real-rate/policy-driven rise is something the Fed is deliberately engineering, whereas the fiscal-term-premium component is not something rate policy can fix. See [[Rate expectations#Jun 18 2026 — the rate / inflation-expectations link breaks (Nangle)|Rate expectations]].

*Source: [[Toby Nangle]] (FT Alphaville, Jun 18 2026); levels cross-checked against `prices_long` (DGS2, DCOILBRENTEU) and `rate_futures_daily` (ZQZ26).*

---

## Related

- [[Treasuries]] — the asset class where term premium is embedded
- [[Rate expectations]] — the expected short-rate component of the decomposition
- [[Inflation expectations]] — the expected inflation component; breakevens and swaps
- [[Fiscal Dominance]] — the fiscal driver of elevated term premium in 2026
- [[Hormuz Permanent Risk Premium]] — geopolitical shock amplified by fiscal constraints
- [[2026 recession risk]] — fiscal vulnerability ranking tied to term premium dynamics
- [[Ruchir Sharma]] — policy ammunition exhaustion thesis (FT Apr 2026)
- [[Treasury safe asset erosion]] — structural erosion of the safe-haven bid
- [[Steepener trade]] — trading the term premium via curve shape
- [[Toby Nangle]] — Jun 2026 "why aren't bond yields lower?" decomposition

---

*Created 2026-04-06.*
