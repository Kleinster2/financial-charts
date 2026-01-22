# JGB

Japanese Government Bonds — the world's second-largest sovereign bond market (~$9T outstanding). JGB yields rising is a global macro event because Japan has been the anchor of low rates for decades, funding carry trades worldwide.

## Why JGBs matter globally

1. **Carry trade funding** — trillions borrowed in JPY at near-zero rates, invested globally
2. **BOJ holdings** — BOJ owns 50%+ of JGBs, market is structurally distorted
3. **Japanese institutions** — life insurers, pension funds are massive global bond/equity buyers
4. **Yield curve control legacy** — artificial suppression created global spillovers

When JGB yields rise, Japanese capital repatriates → sells foreign bonds → global yields rise.

## Market structure

| Metric | Value |
|--------|-------|
| Outstanding | ~¥1,200T (~$9T) |
| BOJ holdings | ~50% |
| 10Y yield (Jan 2026) | ~1.2% |
| 30Y yield (Jan 2026) | ~2.5% (record highs) |

The market is illiquid because BOJ absorbed so much supply. Price discovery is impaired.

## Yield history

| Period | 10Y yield | Context |
|--------|-----------|---------|
| 1990s | 2-4% | Post-bubble |
| 2000s | 1-2% | Deflation era |
| 2016-2022 | ~0% | YCC target |
| 2023 | 0.5-1% | YCC bands widened |
| 2024-25 | 1-1.5% | Post-YCC normalization |
| Jan 2026 | ~1.2% | BOJ tightening cycle |

## BOJ yield curve control (2016-2024)

BOJ explicitly targeted 10Y yields at ~0% with unlimited bond purchases. This:
- Suppressed domestic yields artificially
- Forced Japanese savers into foreign assets
- Created massive carry trade incentive
- Required constant intervention as global yields rose

YCC ended March 2024. Yields now "market-determined" but BOJ still intervenes to prevent disorderly moves.

## Transmission to global markets

**Rising JGB yields → yen strengthens → carry trade unwinds → global risk-off**

The mechanism:
1. Higher JGB yields make domestic bonds attractive
2. Japanese institutions sell foreign bonds, repatriate capital
3. JPY demand rises (repatriation requires buying yen)
4. Carry trade borrowers face margin calls
5. Forced liquidation of risk assets globally

See [[Carry trade]] for August 2024 unwind specifics.

## Tracking JGBs

**ETF proxy:** 2510.T (NEXT FUNDS Japan Bond ETF)
- Tracks JGB prices (inverse of yields)
- Falling 2510.T = rising JGB yields = BOJ tightening
- Listed on Tokyo Stock Exchange

**Direct yield data:**
- `jgb_yields` table in database (FRED source, monthly, lagged)
- Real-time: Bloomberg, TradingView "JP10Y"

## Current dynamics (Jan 2026)

- BOJ raised rates to 0.5% in Dec 2025 — highest in 30 years
- 30Y JGB yields at record highs (~2.5%)
- Market pricing further normalization
- Yen volatility elevated
- Carry trade remains structural risk

## Investment implications

| Scenario | Expression |
|----------|------------|
| JGB yields rise further | Short 2510.T, long JPY |
| BOJ stays dovish | Carry trade persists |
| Disorderly unwind | Long VIX, short EM FX |
| Japanese bank NIM expansion | Long Japanese bank stocks |

## Related

- [[BOJ policy]] — policy framework driving JGB yields
- [[Carry trade]] — JGBs as funding source
- [[Treasuries]] — US comparison
- [[Japan]] — macro context
- [[VIX ETPs]] — vol spike during unwinds
