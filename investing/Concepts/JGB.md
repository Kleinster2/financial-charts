#concept #bonds #japan #rates

# JGB

Japanese Government Bonds — the world's third-largest sovereign bond market (~$7.2T outstanding). JGB yields rising is a global macro event because Japan has been the anchor of low rates for decades, funding carry trades worldwide.

## Why JGBs matter globally

1. **Carry trade funding** — trillions borrowed in JPY at near-zero rates, invested globally
2. **BOJ holdings** — BOJ owns 50%+ of JGBs, market is structurally distorted
3. **Japanese institutions** — life insurers, pension funds are massive global bond/equity buyers
4. **Yield curve control legacy** — artificial suppression created global spillovers

When JGB yields rise, Japanese capital repatriates → sells foreign bonds → global yields rise.

## Market structure

| Metric | Value |
|--------|-------|
| Outstanding | ~¥1,100T (~$7.2T) |
| BOJ holdings | ~50% |
| Foreign share | 65% of monthly cash transactions (up from 12% in 2009) |
| 10Y yield (Jan 2026) | ~1.8% |
| 30Y yield (Jan 2026) | **~3.66%** (record highs post-crash) |
| 40Y yield (Jan 2026) | **>4%** — first JGB maturity above 4% in 30+ years |

The market is dangerously illiquid because BOJ absorbed so much supply. Price discovery is impaired. See [[JGB crash January 2026]] — $280M of trading caused $41B wipeout.

![[jgb-ownership-breakdown.png]]
*BOJ holdings surged from ~10% (2012) to ~50%+ (2023), crowding out other buyers.*

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
- **40Y yields >4%** — first JGB maturity above 4% in 30+ years
- **30Y JGB yields at ~3.66%** (record highs post-Jan 21 crash)
- Bloomberg dislocation index hit all-time high
- Market structure fragility exposed — [[JGB crash January 2026]]
- Big 4 life insurers: **$60B combined unrealized losses** on domestic bonds (4x prior year)
- Foreign investors now 65% of cash trading volume
- Japan has steepest yield curve among major markets (10Y-30Y spread ~140-160 bps)
- Carry trade remains structural risk

**BOJ QT:** Cutting monthly purchases — slowing from ¥400B/month reduction to ¥200B/quarter from April. Ueda said bank would increase purchases "in exceptional cases" to stabilize market.

**Key risk:** $280M of trading caused $41B wipeout. Thin liquidity + constrained dealer balance sheets = vulnerable to further shocks.

## Investment implications

| Scenario | Expression |
|----------|------------|
| JGB yields rise further | Short 2510.T, long JPY |
| BOJ stays dovish | Carry trade persists |
| Disorderly unwind | Long VIX, short EM FX |
| Japanese bank NIM expansion | Long Japanese bank stocks |

## Related

- [[JGB crash January 2026]] — $280M trading → $41B wipeout
- [[BOJ policy]] — policy framework driving JGB yields
- [[Carry trade]] — JGBs as funding source
- [[Treasuries]] — US comparison
- [[Japan]] — macro context
- [[VIX ETPs]] — vol spike during unwinds
- [[UK gilt crisis]] — comparison (Truss moment)
- [[Bond market fragility]] — structural theme
