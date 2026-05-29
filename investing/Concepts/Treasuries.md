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

T-bills are sold at a discount and mature at par—the difference is your return. Notes and bonds pay coupons semi-annually.

## Market size

The Treasury market is ~$30 trillion—the deepest, most liquid bond market in the world.

2025 issuance: ~$29.7 trillion across 444 auctions. Quarterly borrowing estimates:
- Q3 2025: $1.007 trillion
- Q4 2025: $590 billion

## The yield curve

The relationship between yields at different maturities. The shape signals economic expectations.

![[yield-curve-spread.png]]

### Shapes

| Shape | What it means | Economic signal |
| ----- | ------------- | --------------- |
| Normal (upward) | Long yields > short yields | Growth expected, stable economy |
| Flat | Similar yields across maturities | Uncertainty, transition |
| Inverted | Short yields > long yields | Recession warning |

Why longer maturities usually pay more: Investors demand compensation for locking up money longer and bearing more interest rate risk. Historically, 20-year bonds yield ~2% more than 3-month bills.

### Key spreads

| Spread | What it tracks |
| ------ | -------------- |
| 10Y-2Y (T10Y2Y) | Most-watched recession indicator |
| 10Y-3M | NY Fed's preferred recession model |
| 30Y-10Y | Long-end steepness |

The 10Y-2Y spread inverted before the 2001, 2008, and 2020 recessions. It was negative from Oct 2022 to Dec 2024.

## Why Treasuries matter

Risk-free rate: All other assets are priced as a spread over Treasuries. When Treasury yields rise, discount rates rise, and asset valuations fall.

Safe haven: In [[Risk-on risk-off|risk-off]] episodes, capital flows to Treasuries, pushing yields down. Exception: [[Sell America trade]] when even Treasuries get sold.

Fed policy transmission: The Fed controls short-term rates directly (fed funds). Long-term Treasury yields reflect market expectations for future Fed policy plus term premium.

Global reserve asset: Foreign central banks and investors hold ~$8 trillion in Treasuries as reserve assets and dollar liquidity.

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

Auction metrics to watch:
- Bid-to-cover ratio: Demand indicator (higher = stronger)
- Tail: Difference between auction yield and when-issued yield (positive tail = weak demand)
- Direct vs indirect bidders: Indirect often proxies foreign central banks

Weak auctions (low bid-to-cover, large tail) can spike yields across the curve.

## Term premium

The extra yield investors demand for holding long-duration bonds beyond expected future short rates. When term premium rises, long yields rise even if Fed expectations are unchanged. For full decomposition mechanics (ACM model, Kim-Wright, how to isolate term premium from [[Inflation expectations|inflation expectations]]), see [[Term premium]].

Drivers:
- Fiscal deficit concerns (dominant in 2026)
- Inflation uncertainty
- Supply/demand imbalance
- Safe-haven status erosion

2025 saw elevated term premium on deficit fears and Moody's downgrade. In Apr 2026, term premium rose further on fiscal overextension fears — yields climbing despite stable long-term inflation expectations and unchanged Fed rate path. See [[Term premium#April 2026: fiscal term premium|Term premium § April 2026]].

### Real-yield decomposition tracker (May 2026)

The live tracker now keeps the real-rate input series in `prices_long` because `stock_prices_daily` is at SQLite's 2000-column limit. The decomposition uses nominal Treasury yields, [[TIP|TIPS]] real yields, and breakevens from FRED:

![[treasury-5y-real-yield-decomposition-lw.png]]
*5Y nominal yield, 5Y TIPS real yield, and 5Y breakeven. This is the belly where the May selloff was more than fully explained by real yields.*

![[treasury-10y-real-yield-decomposition-lw.png]]
*10Y nominal yield, 10Y TIPS real yield, and 10Y breakeven. The 10Y move was almost entirely real-rate led.*

![[treasury-30y-real-yield-decomposition-lw.png]]
*30Y nominal yield and 30Y TIPS real yield. FRED does not provide the same daily 30Y breakeven series in this tracker, so the table below uses DGS30 - DFII30 as the residual.*

| Tenor | Nominal series | Real-yield series | Breakeven proxy | Common window | Nominal move | Real-yield move | Breakeven / residual move | Read |
|-------|----------------|-------------------|-----------------|---------------|--------------|-----------------|---------------------------|------|
| 5Y | DGS5 | DFII5 | T5YIE | May 13-19 2026 | +20 bp | +24 bp | -4 bp | More than all of the nominal selloff came from real yields |
| 10Y | DGS10 | DFII10 | T10YIE | May 13-19 2026 | +21 bp | +19 bp | +2 bp | Almost entirely a real-yield move |
| 30Y | DGS30 | DFII30 | DGS30 - DFII30 | May 13-19 2026 | +15 bp | +10 bp | +5 bp | Mostly real yields, with a smaller inflation/residual component |

This provides the reusable Treasury-market diagnostic behind [[Bhanu Baweja]]'s May 20 claim. Mechanically, the recent nominal selloff was mostly real yields, not breakevens. The interpretation remains separate: "real yields rose" is observable; whether that means nominal-growth repricing, fiscal term premium, duration supply, or a mix has to be triangulated against [[Rate expectations]], [[Inflation expectations]], and auction/demand data. The point-in-time visual check belongs with [[Bhanu Baweja]]'s rates view.

Operational refresh:

```bash
python update_fred_indicators.py --lookback 30 --skip-b3 --codes DGS5 DGS10 DGS30 T5YIE T10YIE DFII5 DFII10 DFII30
python scripts/chart_treasury_real_yield_decomposition.py --force
```

Sources: FRED series [DGS5](https://fred.stlouisfed.org/series/DGS5), [DGS10](https://fred.stlouisfed.org/series/DGS10), [DGS30](https://fred.stlouisfed.org/series/DGS30), [DFII5](https://fred.stlouisfed.org/series/DFII5), [DFII10](https://fred.stlouisfed.org/series/DFII10), [DFII30](https://fred.stlouisfed.org/series/DFII30), [T5YIE](https://fred.stlouisfed.org/series/T5YIE), and [T10YIE](https://fred.stlouisfed.org/series/T10YIE), refreshed May 20 2026.

### May 24, 2026 -- Washington borrowing-cost tolerance test

Reuters' May 24 analysis turned the May long-end selloff from a market-structure story into a political constraint story. The sequence was simple: the [[Operation Epic Fury|Iran war]] kept oil and inflation risk elevated; investors pushed the 10-year above 4.5%; those yields fed into [[Mortgage rates]], credit cards, and business loans; and the administration's room to keep pressing the war narrowed as midterm-election affordability risk rose.

The source-reported market level was that the 10-year Treasury had touched 4.69% earlier in the week, the highest since January 2025, before last trading at 4.56%. That lines up with the vault's FRED-backed close data: DGS10 closed at 4.67% and DGS30 at 5.18% on May 19, while the 10-year breakeven was still only 2.49%. The observable move remained mostly a real-yield / term-premium move rather than a pure inflation-expectations break.

The policy implication is the important part. [[Scott Bessent]] and the White House framed elevated long-end yields as temporary Iran-war disruption. Market participants quoted by Reuters were less categorical: if yields approach the 5% pain level while stocks and credit remain orderly, aggressive official intervention would look less like market stabilization and more like inflation accommodation. That is exactly where the [[Fiscal Dominance]] constraint becomes practical rather than theoretical.

Source: Reuters, [US Treasury rout tests Washington's tolerance for higher borrowing costs](https://wtvbam.com/2026/05/24/analysis-us-treasury-rout-tests-washingtons-tolerance-for-higher-borrowing-costs/), May 24 2026.

### May 27, 2026 -- 30-year yield stays in the war loser bucket

[[Reuters]]' May 27 cross-asset graphic placed government bonds firmly in the conflict's loser camp. The mechanism is the same one this note has been tracking: higher oil prices keep inflation risk alive, fiscal and military spending expectations pressure duration, and central banks have less room to lean against growth weakness. [[Reuters]] reported the U.S. 30-year Treasury yield trading above 5%, its highest since 2007.

The May 24 Washington-tolerance story and the May 27 global-winners/losers story are the same chain at different zoom levels. May 24 asked when higher Treasury yields become a political problem for Washington; May 27 showed that the bond selloff is not isolated to the U.S. German Bund yields hit their highest in more than 15 years as traders priced at least two ECB hikes by year-end. The shared driver is the Iran-war energy shock forcing rate markets to price inflation persistence even as PMIs and activity weaken.

Source: [[Reuters]], [GRAPHIC-Iran war splits global markets into clear winners and losers](https://www.lse.co.uk/news/graphic-iran-war-splits-global-markets-into-clear-winners-and-losers-f7nir94d9i1wz8l.html), May 27 2026.

### May 27, 2026 -- inflation expectations are not clean bond-market signals

Chartbook's May 27 bond-market link set is a useful measurement warning for this note. The FT caveat it highlighted is that market-implied inflation expectations, inflation swaps, TIPS, linkers, and "real yield" series are traded prices. They embed liquidity, supply/demand technicals, central-bank balance-sheet effects, and inflation-risk premia, so they should not be treated as direct survey-like reads of expected CPI.

Vault practice: keep real yields, breakevens, term premia, nominal yields, and survey expectations as separate diagnostics. The May Iran-war selloff can still be described as an inflation-volatility and supply-shock repricing, but the observed FRED decomposition remains real-yield / term-premium heavy rather than a clean breakeven-only break. That distinction matters for policy read-through: a central bank facing higher oil and long-end yields is not the same thing as a central bank facing a fully de-anchored expectations regime.

Source: [[Adam Tooze]], Chartbook Top Links 1114, May 27 2026; FT bond-market measurement caveat via Chartbook.

### Kalshi 10-year yield bucket (May 20, 2026)

[[Kalshi]]'s active KXTNOTED daily market for the May 20 10-year Treasury yield is thin, but directionally consistent with the broader tape: the only traded bucket in the API snapshot was 4.67-4.69%, last 56c with 24c / 72c bid-ask, $128 volume, and $128 open interest. Adjacent buckets from 4.64-4.72 had wide quotes and little or no volume.

Read-through: this is not liquid enough to treat as a standalone forecast. It is useful as a confirmation that the live prediction-market bucket is centered around the high-4.60s / low-4.70s, matching the daily macro tape where the 10-year Treasury yield is the main tightening channel. KX10Y3M, the year-end 10Y-3M spread market, was finalized on May 19 and should not be used as an active curve signal.

Source: [[Kalshi]] API series KXTNOTED and KX10Y3M, read May 20, 2026: https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KXTNOTED and https://external-api.kalshi.com/trade-api/v2/markets?limit=1000&series_ticker=KX10Y3M

## Trading Treasuries

Direct: TreasuryDirect (retail), primary dealers (institutional)

ETFs:
| Ticker | Exposure |
| ------ | -------- |
| SHY | 1-3 year |
| IEF | 7-10 year |
| TLT | 20+ year |
| GOVT | Broad market |
| TIP | TIPS |

Futures: 2Y, 5Y, 10Y, 30Y Treasury futures on CME—highly liquid, basis trade vehicle.

---

## Journal

| Date | Event | Impact |
|------|-------|--------|
| 2026-05-27 | Chartbook/FT warns against reading market-implied inflation as a clean expectations series | Keep real yields, breakevens, term premia, nominal yields, and surveys separate; May selloff still looks more real-yield / term-premium heavy than pure breakeven de-anchoring |
| 2026-05-27 | Reuters cross-asset graphic puts bonds in Iran-war loser camp | U.S. 30Y traded above 5%, highest since 2007; Bund yields highest in more than 15 years; at least two ECB hikes priced by year-end |
| 2026-05-24 | Reuters frames Treasury rout as Washington borrowing-cost tolerance test | 10Y touched 4.69% and last traded 4.56%; higher long-end yields now transmit directly into mortgage, credit, and midterm affordability risk |
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
- [[Term premium]] — yield decomposition and what drives the non-expectations component
- [[Inflation expectations]] — the other component of the decomposition
- [[Fiscal Dominance]] — regime context for elevated term premium
