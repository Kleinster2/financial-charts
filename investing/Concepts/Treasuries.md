# Treasuries

US Treasury securities—the benchmark "risk-free" asset class. Backed by the full faith and credit of the US government, they set the floor for all other yields and serve as the global safe haven in risk-off episodes.

## Security types

| Type | Maturity | Coupon | Auction frequency |
| ---- | -------- | ------ | ----------------- |
| T-bills | ≤ 1 year (4, 8, 13, 17, 26, 52 weeks) | Zero (discount) | Weekly |
| T-notes | 2-10 years (2, 3, 5, 7, 10) | Semi-annual | Monthly |
| T-bonds | 20-30 years | Semi-annual | Monthly |
| TIPS | 5, 10, 30 years | Real + inflation adjustment | Quarterly |
| FRNs | 2 years | Floating (T-bill + spread) | Monthly |

**T-bills** are sold at a discount and mature at par—the difference is your return. **Notes and bonds** pay coupons semi-annually.

## Market size

The Treasury market is ~$30 trillion—the deepest, most liquid bond market in the world.

**2025 issuance:** ~$29.7 trillion across 444 auctions. Quarterly borrowing estimates:
- Q3 2025: $1.007 trillion
- Q4 2025: $590 billion

## The yield curve

The relationship between yields at different maturities. The shape signals economic expectations.

![[yield-curve-spread.png]]

### Shapes

| Shape | What it means | Economic signal |
| ----- | ------------- | --------------- |
| **Normal (upward)** | Long yields > short yields | Growth expected, stable economy |
| **Flat** | Similar yields across maturities | Uncertainty, transition |
| **Inverted** | Short yields > long yields | Recession warning |

**Why longer maturities usually pay more:** Investors demand compensation for locking up money longer and bearing more interest rate risk. Historically, 20-year bonds yield ~2% more than 3-month bills.

### Key spreads

| Spread | What it tracks |
| ------ | -------------- |
| **10Y-2Y (T10Y2Y)** | Most-watched recession indicator |
| **10Y-3M** | NY Fed's preferred recession model |
| **30Y-10Y** | Long-end steepness |

The 10Y-2Y spread inverted before the 2001, 2008, and 2020 recessions. It was negative from Oct 2022 to Dec 2024.

## Why Treasuries matter

**Risk-free rate:** All other assets are priced as a spread over Treasuries. When Treasury yields rise, discount rates rise, and asset valuations fall.

**Safe haven:** In [[Risk-on risk-off|risk-off]] episodes, capital flows to Treasuries, pushing yields down. Exception: [[Sell America trade]] when even Treasuries get sold.

**Fed policy transmission:** The Fed controls short-term rates directly (fed funds). Long-term Treasury yields reflect market expectations for future Fed policy plus term premium.

**Global reserve asset:** Foreign central banks and investors hold ~$8 trillion in Treasuries as reserve assets and dollar liquidity.

## Foreign holdings

Foreigners hold ~30% of outstanding Treasuries (~$9 trillion as of late 2025).

| Holder | Amount | Share |
| ------ | ------ | ----- |
| [[Japan]] | $1.2T | 12.4% |
| [[UK]] | ~$750B | 8.4% |
| [[China]] | $759B | 8.9% |

Foreign flows matter: net selling pressures yields higher regardless of Fed policy. This is a key [[Sell America trade]] dynamic.

## Auction dynamics

Treasury announces a tentative auction schedule quarterly (first Wednesday of Feb, May, Aug, Nov).

**Auction metrics to watch:**
- **Bid-to-cover ratio:** Demand indicator (higher = stronger)
- **Tail:** Difference between auction yield and when-issued yield (positive tail = weak demand)
- **Direct vs indirect bidders:** Indirect often proxies foreign central banks

Weak auctions (low bid-to-cover, large tail) can spike yields across the curve.

## Term premium

The extra yield investors demand for holding long-duration bonds beyond expected future short rates. When term premium rises, long yields rise even if Fed expectations are unchanged.

**Drivers:**
- Inflation uncertainty
- Fiscal deficit concerns
- Supply/demand imbalance
- Safe-haven status erosion

2025 saw elevated term premium on deficit fears and Moody's downgrade.

## Trading Treasuries

**Direct:** TreasuryDirect (retail), primary dealers (institutional)

**ETFs:**
| Ticker | Exposure |
| ------ | -------- |
| SHY | 1-3 year |
| IEF | 7-10 year |
| TLT | 20+ year |
| GOVT | Broad market |
| TIP | TIPS |

**Futures:** 2Y, 5Y, 10Y, 30Y Treasury futures on CME—highly liquid, basis trade vehicle.

---

## Journal

| Date | Event | Impact |
|------|-------|--------|
| 2026-04-03 | Fund managers buying sovereign bonds on growth fears | See below — shift from inflation to growth pricing |
| 2026-01-30 | [[Kevin Warsh]] nominated Fed Chair | Curve steepened: 10Y +2bp (4.25%), 2Y -2bp (3.53%), 30Y +3bp (4.89%). Long end up on balance sheet concerns — Warsh opposes Fed holding bonds/MBS |
| 2026-01-28 | FOMC holds at 3.50-3.75% | First pause since July. Waller/Miran dissented for 25bp cut |

---

## Iran conflict — inflation vs growth repricing (Apr 2026)

*Source: FT, Apr 3 2026 (Emily Herbert, Ian Smith)*

The [[Operation Epic Fury|Iran conflict]] triggered a two-phase sovereign bond dynamic: first an inflation-driven sell-off, now a growth-fear-driven buy.

### Phase 1: Inflation sell-off (early March)

[[Brent crude]] surged from ~$72 to ~$120, triggering a bond rout:

| Market | Yield move | Peak level |
|--------|-----------|------------|
| 10Y UST | +50 bps | ~4.5% |
| 10Y gilt | +90 bps | >5.1% |

![[ft-5y-bond-yields-us-uk-iran-conflict-2026.png]]
*5-year sovereign yields: UK (blue) and US (pink) since Jan 2026. UK yields rose faster — pre-existing fiscal fragility + higher energy import dependence. Source: LSEG*

### Phase 2: Growth repricing (late March–April)

Yields have come off conflict highs as managers argue the market over-priced inflation and under-priced the growth hit. The term structure of inflation expectations supports this: short-term expectations surged, but long-term remained anchored.

| Metric | Pre-conflict | Post-conflict | Move |
|--------|-------------|---------------|------|
| 1Y US inflation swaps | ~2.5% | >3.1% | +60 bps |
| 5Y5Y forward | ~2.4% | ~2.4% | Flat |

The gap between short and long inflation expectations suggests markets see the oil shock as transitory — damaging to growth but not structurally inflationary.

### Who's buying and what

| Investor | Firm | Position | Rationale |
|----------|------|----------|-----------|
| Ben Nicholl | [[Royal London Asset Management]] | Buying 3-7yr gilts | *"Market is underpricing the probability that central banks will have to cut rates further out to offset the growth shock"* |
| Iain Stealey | [[JPMorgan]] AM | Buying long-term debt globally (Europe, Asia, N. America) | Inflation focus "probably overdone"; central bankers will "wait and see" |
| James Bilson | [[Schroders]] | Buying Canadian govt bonds | Rate rises priced by market "inconsistent with economic fundamentals" — soft labor market, cooling economy |
| Andrew Chorlton | [[M&G]] | Added gilts when market priced >2 BoE rate hikes | *"Given the underlying weakness, we felt that was too much"* |
| Steve Ryder | [[Aviva Investors]] | Adding short-dated gilts | Even if BoE hikes, *"those hikes would be reversed in the following years"* given UK's slow pre-crisis growth |
| Andrew Sheets | [[Morgan Stanley]] | Bullish UST recommendation (late March) | *"Market previously overly focused on inflation risks"* and not reflecting the demand hit |
| Arun Sai | [[Pictet]] AM | Bonds present value in both de-escalation and escalation scenarios | Asymmetric setup |

### Caution

Jamie Searle, [[Citi]] (European rates strategist): *"We're watchful, but not yet ready to say this is a great opportunity to buy. The risk is that we get a headline that prompts oil prices to jump sharply higher, and yields follow."*

Even in a quick de-escalation, *"there would still be significant uncertainty over long-term disruption to energy supply. The market should pivot more to pricing the medium-term growth consequences."*

### Implications

This marks a regime shift from the [[Iran conflict portfolio hedging|early-conflict 60/40 breakdown]] where bonds and stocks fell together. If the growth repricing continues, the traditional bond hedge may reassert itself — but only if central banks prioritize growth over inflation. The UK is the test case: pre-existing fiscal weakness + energy import dependence makes gilts the highest-conviction "growth will win" trade.

---

## Related

- [[Steepener trade]] — betting on curve shape changes
- [[Basis trade]] — Treasury vs futures arbitrage
- [[Sell America trade]] — when Treasuries lose safe-haven status
- [[Risk-on risk-off]] — Treasuries rally in risk-off
- [[Federal Reserve]] — sets short-term rates
- [[Credit spreads]] — corporate bonds priced as spread over Treasuries
