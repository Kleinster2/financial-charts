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
| Expected short rates | Where markets think the [[Federal Reserve|Fed]] is heading | Fed Funds futures (ZQ), [[SOFR]] futures (SR3). See [[Rate expectations]] |
| Expected inflation | Where markets think CPI/PCE is heading | Breakeven inflation (nominal Treasury minus [[TIP|TIPS]]), inflation swaps. See [[Inflation expectations]] |
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

1. Check [[Rate expectations|Fed rate expectations]] (ZQ/SR3 futures) — are expected short rates moving?
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

---

*Created 2026-04-06.*
