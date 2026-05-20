---
aliases: [BCOM, BCOMTR, Bloomberg Commodity TR, Bloomberg Commodity Index Total Return, BBG Commodity Index, Bloomberg Commodities Index, Dow Jones-UBS Commodity Index, Dow Jones-AIG Commodity Index]
tags: [asset, index, commodities, benchmark]
---

# Bloomberg Commodity Index

**Bloomberg Commodity Index** is [[Bloomberg LP]]'s flagship diversified commodity futures benchmark. The important traded/reference version is usually BCOMTR, the total-return index that represents a fully collateralized futures basket; BCOM itself is the excess-return futures index. It is a rules-based commodity beta engine, not spot commodities and not an ETF.

---

## Synthesis

BCOM is best understood as the "balanced" broad-commodity benchmark: more diversified than the energy-heavy S&P GSCI complex, more benchmark-like than active commodity ETFs, and more institutionally embedded than retail products like [[DBC]] or [[GSG]]. Its design deliberately prevents any one commodity or group from dominating at the annual rebalance: no group can exceed 33%, no single commodity can exceed 15%, and commodity weights are based on a two-thirds liquidity / one-third production framework. That makes BCOM a cleaner read on diversified commodity beta than an oil-heavy index, but it also means it can lag during pure energy shocks.

The 2026 version matters because the index moved back toward a broader inflation basket just as commodities re-accelerated. [[Bloomberg LP]]'s October 30, 2025 target-weight announcement put the 2026 target mix at 29.44% energy, 18.84% precious metals, 15.76% industrial metals, 21.15% grains, 9.17% softs, and 5.64% livestock. Cocoa returned to the benchmark in January 2026 after meeting inclusion criteria for two consecutive years. By the April 30, 2026 factsheet, market moves had pushed current weights to 39.28% energy and 26.64% agriculture, while precious metals had drifted down to 15.50% despite gold remaining the largest single component.

For this vault, the practical data-access issue is now mostly solved. `market_data.db` has `BCOM` and `BCOMTR` daily history in `prices_long` as of the May 19, 2026 import from Investing.com's historical index pages. The old `stock_prices_daily` wide table is already at SQLite's 2,000-column limit, so the official index series live in the canonical narrow table rather than as wide columns. [[COMB]] remains useful as a tradable ETF wrapper/proxy, while [[DBC]], [[GSG]], [[PDBC]], and [[COMT]] are comparison vehicles with different roll and sector exposures.

---

## Quick stats

| Metric | Value |
|---|---|
| Benchmark | Bloomberg Commodity Index |
| Bloomberg tickers | BCOM (excess return), BCOMTR (total return) |
| Administrator | [[Bloomberg LP\|Bloomberg Index Services Limited]] |
| Introduced | July 14, 1998 |
| Base value/date | 100 as of December 31, 1990 |
| Historical series | Bloomberg says historical information dates back to 1960 |
| 2026 estimated tracked AUM | $108.8B (Bloomberg, Oct 30 2025) |
| Current source | Bloomberg Professional service |
| Calculation frequency | Every 15 seconds |
| Rebalance | Annual target reweight; weights drift between rebalances |
| Roll schedule | Monthly roll, typically around the 6th-10th business days |
| Local DB status | `BCOM` in `prices_long` from 1991-01-03; `BCOMTR` from 2001-08-20; both through 2026-05-19 |

---

## Methodology

BCOM is a futures index. It owns no physical barrels, bushels, or metal inventories. Each constituent is represented through listed futures contracts on physical commodities, with collateral economics captured in the total-return version.

The weighting engine has three layers:

| Layer | Rule | Why it matters |
|---|---|---|
| Economic significance | Two-thirds liquidity, one-third production | Keeps the index tied to both financial tradability and real-world commodity scale |
| Diversification caps | No group >33%; no single commodity >15%; commodity plus derivatives >25% | Prevents the index from becoming a disguised oil or gold index at rebalance |
| Minimum floor | No single commodity below 2% as liquidity allows | Keeps smaller eligible commodities visible without overwhelming liquidity constraints |

Between annual rebalances, actual weights move with prices. That is why the April 30, 2026 factsheet shows energy at 39.28% even though the 2026 target weight was 29.44%: the rebalance starts diversified, then the tape pulls the index toward whatever commodity complex is winning.

BCOMTR is the better performance reference than BCOM for allocators because it reflects a fully collateralized commodity futures investment. The excess-return BCOM series captures futures price and roll effects; BCOMTR adds collateral return. In a higher-rate world, that collateral leg is not background noise.

---

## 2026 Composition

### Target vs current sector drift

| Sector/group | 2026 target | Apr 30 2026 current | Read |
|---|---:|---:|---|
| Energy | 29.44% | 39.28% | Oil and gas strength pulled the index above its rebalance cap after the January reset |
| Agriculture | 30.32% | 26.64% | Bloomberg target groups: grains 21.15% + softs 9.17%; current factsheet rolls these into agriculture |
| Precious metals | 18.84% | 15.50% | Gold is still largest single line, but the group lost relative share after rebalance |
| Industrial metals | 15.76% | 13.48% | Copper remains the key industrial line but weight drifted below target |
| Livestock | 5.64% | 5.10% | Small diversifier; live cattle dominates lean hogs |

### Individual weights (Apr 30 2026)

| Sector | Contract | Weight |
|---|---|---:|
| Energy | Brent Crude Oil (CO) | 12.41% |
| Energy | WTI Crude Oil (CL) | 9.50% |
| Energy | [[Natural gas]] (NG) | 6.07% |
| Energy | Low Sulphur Gas Oil (QS) | 4.47% |
| Energy | RBOB Gasoline (XB) | 3.48% |
| Energy | ULS Diesel (HO) | 3.35% |
| Agriculture | Soybeans (S) | 4.84% |
| Agriculture | Corn (C) | 4.74% |
| Agriculture | Soybean Oil (BO) | 3.44% |
| Agriculture | Chicago Wheat (W) | 2.70% |
| Agriculture | Soybean Meal (SM) | 2.47% |
| Agriculture | Sugar (SB) | 2.32% |
| Agriculture | Kansas City Wheat (KW) | 1.88% |
| Agriculture | Coffee (KC) | 1.79% |
| Agriculture | Cotton (CT) | 1.63% |
| Agriculture | Cocoa (CC) | 0.83% |
| Precious metals | [[Gold]] (GC) | 12.46% |
| Precious metals | Silver (SI) | 3.03% |
| Industrial metals | [[Copper]] (HG) | 5.24% |
| Industrial metals | Aluminum (LA) | 3.62% |
| Industrial metals | Nickel (LN) | 1.96% |
| Industrial metals | Zinc (LX) | 1.93% |
| Industrial metals | Lead (LL) | 0.73% |
| Livestock | Live Cattle (LC) | 3.37% |
| Livestock | Lean Hogs (LH) | 1.73% |

Source: Bloomberg Commodity Indices factsheet dated April 30, 2026.

---

## Performance

### Official BCOMTR returns (Apr 30 2026)

| Period | BCOMTR return |
|---|---:|
| 1M | 4.21% |
| 3M | 17.47% |
| YTD | 29.65% |
| 2025 | 15.77% |
| 1Y | 44.82% |
| 3Y annualized | 15.75% |
| 5Y annualized | 13.17% |
| 10Y annualized | 7.58% |
| Since Jan 2 1991 annualized | 3.67% |

The official return table confirms the 2020s regime shift: BCOMTR was no longer a dead diversifier by 2026. The 5-year annualized return above 13% reflects the combined effect of post-COVID commodity inflation, the 2022 energy shock, the 2025-2026 metals/gold move, and higher collateral yield.

### Local official performance

Verified against `market_data.db` after importing Investing.com historical index levels on 2026-05-19.

| Period | Start date | End date | BCOM | BCOMTR |
|---|---|---|---:|---:|
| YTD | 2026-01-02 | 2026-05-19 | 30.4% | 32.2% |
| 1Y | 2025-05-19 | 2026-05-19 | 41.6% | 47.3% |
| 3Y | 2023-05-19 | 2026-05-19 | 41.3% | 62.5% |
| 5Y | 2021-05-19 | 2026-05-19 | 56.2% | 86.8% |
| 10Y | 2016-05-19 | 2026-05-19 | 68.7% | 113.5% |

![[bcomtr-vs-bcom-price-chart.png]]
*BCOMTR vs BCOM normalized to 100 at the start of local BCOMTR history, August 20, 2001. The widening gap is the collateral-return leg compounding on top of futures excess return.*

The spread between BCOM and BCOMTR is the collateral leg. It is small day to day, but it compounds hard once short rates stop living near zero.

### Local ETF proxy performance

Verified against `market_data.db` after refreshing ETF prices on 2026-05-19.

| Period | Start date | End date | [[COMB]] | [[DBC]] | [[GSG]] | [[PDBC]] | COMT |
|---|---|---|---:|---:|---:|---:|---:|
| YTD | 2026-01-02 | 2026-05-19 | 31.3% | 41.2% | 50.7% | 41.9% | 46.8% |
| 1Y | 2025-05-20 | 2026-05-19 | 32.5% | 47.5% | 60.5% | 46.3% | 44.4% |
| 3Y | 2023-05-22 | 2026-05-19 | 47.5% | 53.7% | 80.7% | 50.6% | 56.5% |
| 5Y | 2021-05-21 | 2026-05-19 | 67.4% | 93.6% | 130.7% | 89.3% | 92.4% |

![[comb-vs-dbc-vs-gsg-vs-pdbc-price-chart.png]]
*COMB vs [[DBC]], [[GSG]], and [[PDBC]] normalized since May 2021. The Bloomberg-linked COMB proxy captured the broad commodity rally but lagged the more energy-sensitive GSG/DBC complex during the 2021-2026 energy-led run.*

---

## Correlation structure

BCOM exposure should sit in the broad-commodity cluster: high correlation to [[COMB]], [[DBC]], [[GSG]], [[PDBC]], and [[COMT]], but with meaningful tracking differences from sector weights and roll methodology. Avg correlation: COMB's correlation to DBC/GSG/PDBC/COMT was 0.83 using local daily returns from 2025-05-20 through 2026-05-19, with a range of 0.81 to 0.84. The practical distinction is energy beta. [[GSG]] is the more energy-sensitive line, [[DBC]] is also energy-heavy, while BCOM/COMB is closer to a capped diversified commodity allocation with larger precious-metals and agriculture offsets.

For portfolio work, treat BCOM as a real-asset/inflation sleeve rather than an equity sector. Its equity correlation can rise during growth shocks because energy and industrial metals are cyclical, but the underlying drivers are still futures curves, collateral yield, supply shocks, [[US dollar]], and [[Inflation|inflation]] rather than earnings revisions.

---

## Evolution

1998 - Dow Jones-AIG architecture. The benchmark began as the Dow Jones-AIG Commodity Index family, built to give investors diversified futures exposure across physical commodities. The original design was already the important part: a commodity benchmark that was investable through futures and constrained by diversification rules rather than pure production weights.

2009 - AIG forced-sale context. After the financial crisis, [[AIG]] sold its commodity index business to [[UBS]]. The business included rights to the Dow Jones-AIG Commodity Index and the index family was renamed Dow Jones-UBS Commodity Indexes. The transaction moved a crisis-era AIG asset into UBS's equities/structured-products franchise and preserved the benchmark through the post-2008 unwind.

2014 - [[Bloomberg LP|Bloomberg]] takes over calculation and brand. [[Bloomberg LP]] acquired the Dow Jones-UBS Commodity Indexes in April 2014, and the index family became the Bloomberg Commodity Index family on July 1, 2014. [[CME Group]] amended futures and cleared swap naming at the same time, noting that the title change did not alter contract economics. This is why older product documents refer to DJUBS/DJ-UBS tickers while current market convention uses BCOM.

2026 - Cocoa returns and the index broadens again. Cocoa was reintroduced during the January 2026 rebalance after meeting inclusion criteria for two consecutive years. Bloomberg's announcement framed the reconstitution as continuity rather than a reshaping event: the softs bucket rose, grains lost weight, and no single commodity target weight fell by more than 61 bps. The bigger story was not cocoa itself; it was that BCOM's rules can adapt without turning the benchmark into a different asset.

---

## How To Use It

BCOM is useful when the question is diversified commodity beta: inflation sensitivity, supply shock exposure, collateralized futures carry, and portfolio diversification. It is the right reference for an institutional commodity sleeve, especially in risk-parity or all-weather portfolios where the point is not just oil or gold.

BCOM is less useful when the question is a specific commodity shock. [[Oil]] disruptions show up, but the index is structurally diluted by metals, agriculture, livestock, and diversification caps. If the view is "crude oil goes up," [[USO]], [[BNO]], energy futures, or energy equities may express it more directly. If the view is "commodity inflation broadens," BCOM is a cleaner benchmark.

For local charting:

| Need | Best local vehicle | Caveat |
|---|---|---|
| Official excess-return benchmark | BCOM | Stored in `prices_long`; not added to the full wide table |
| Official total-return benchmark | BCOMTR | Public local history begins 2001-08-20 from Investing.com |
| Tradable Bloomberg-linked ETF proxy | [[COMB]] | ETF wrapper; shorter history and fund mechanics |
| Longest broad commodity ETF history | [[DBC]] | Invesco DB methodology, not BCOM |
| Energy-heavy commodity beta | [[GSG]] | Tracks S&P GSCI, much more oil-linked |
| K-1-free diversified commodity ETF | [[PDBC]] | Active/optimized roll; Invesco wrapper |
| iShares dynamic commodity strategy | COMT | Different roll and index methodology |

---

## Key Risks And Distortions

| Risk | Why it matters |
|---|---|
| Roll yield dominates spot intuition | A futures index can underperform or outperform spot commodities depending on contango/backwardation and contract selection |
| Collateral yield matters | BCOMTR includes collateral return; high short rates lift total return relative to excess return |
| Annual rebalance creates flow events | Target-weight resets can force buying/selling in crowded futures markets, especially after large commodity moves |
| Diversification caps dilute pure shocks | A major oil or gold move may not translate one-for-one into BCOM because the index is deliberately capped |
| No direct investability | Bloomberg states investors cannot invest directly in an index; exposure comes through swaps, futures, notes, or ETF wrappers |
| Data licensing | Official BCOM/BCOMTR history is a Bloomberg index data product; the local DB uses public Investing.com historical levels, while Bloomberg remains the methodology/source of record |

---

## Sources

- [Bloomberg Commodity Indices factsheet, April 30 2026](https://data.bloomberglp.com/professional/sites/27/BCOM.pdf)
- [Bloomberg Commodity Index 2026 target weights announcement, October 30 2025](https://www.bloomberg.com/company/press/bloomberg-commodity-index-2026-target-weights-announced/)
- [Bloomberg Commodity Index Methodology, February 2026](https://assets.bbhub.io/professional/sites/27/BCOM-Methodology-FEB-2026.pdf)
- [SEC pricing supplement describing the 2014 Bloomberg rename](https://www.sec.gov/Archives/edgar/data/70858/000089109215010075/e67081_424b2.htm)
- [CME Group SER-7121 naming amendments, June 17 2014](https://www.cmegroup.com/tools-information/lookups/advisories/ser/SER-7121.html)
- [GraniteShares COMB product page](https://graniteshares.com/etfs/comb/)
- [Investing.com BCOM historical data](https://www.investing.com/indices/bloomberg-commodity-historical-data)
- [Investing.com BCOMTR historical data](https://www.investing.com/indices/bbg-commodity-tr-historical-data)

---

## Related

- [[Commodities]] - parent concept
- [[COMB]] - Bloomberg-linked ETF proxy in the local DB
- [[DBC]] - Invesco broad commodity ETF proxy
- [[GSG]] - energy-heavy S&P GSCI proxy
- [[PDBC]] - Invesco K-1-free commodity ETF proxy
- [[ALLW]] - uses BCOMTR swap exposure in its commodity sleeve
- [[Bloomberg LP]] - index administrator / owner
- [[UBS]] - acquired AIG's commodity index business in 2009
- [[AIG]] - original commodity-index business seller
- [[CME Group]] - venue/clearing context for BCOM-linked futures and swaps
