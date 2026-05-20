---
aliases: [commodities, commodity, DBC, GSG, raw materials]
---
#concept #commodities #macro

**Commodities** — Raw materials traded on global markets: energy, metals, agriculture. Inflation hedge, growth proxy, and diversifier. Primary benchmarks: [[Bloomberg Commodity Index|BCOM]] for diversified institutional futures beta, DBC (Invesco DB Commodity Index), GSG (iShares S&P GSCI).

---

## Price performance

![[commodities-ytd.png]]

*GLD (gold), USO (oil), Coffee (KC=F) normalized since Jan 2025. Gold dominates at +97%, oil flat at +5%, coffee down -12% after a mid-2025 spike to +40%.*

---

## Major sectors

| Sector | Key commodities | Primary drivers |
|--------|-----------------|-----------------|
| **Energy** | Oil, natural gas | [[OPEC]], demand, geopolitics |
| **Precious metals** | Gold, silver, platinum, palladium | Rates, dollar, safe haven |
| **Base metals** | Copper, aluminum, zinc, nickel | China, industry, green capex |
| **Agriculture** | Corn, wheat, soybeans, softs | Weather, trade, biofuels |

---

## Kalshi commodity pricing layer (May 20, 2026)

[[Kalshi]] announced a dedicated commodities hub on April 15, 2026, expanding from existing [[WTI]], [[Brent crude]], [[Gold]], and [[Silver]] markets into additional physical-market categories. For the vault, the useful signal is not that these contracts replace futures curves; it is that [[Prediction markets]] now provide a retail-accessible, 24/7 probability layer around commodity thresholds when futures markets are closed or hard to interpret.

May 20 API pull, weekly contracts expiring May 22:

| Series | Market | Read |
|--------|--------|------|
| KXBRENTW | [[Brent crude]] close above thresholds | >$105.99 traded at 60c last, >$107.99 at 46c, >$111.99 at 25c, and >$115.99 at 12c. Brent is still priced with a large oil-shock right tail, but not a clean $120 base case. |
| KXWTIW | [[WTI]] July 2026 settlement range | The range bins cluster around $102-$107, with >$107.99 at 29c and below $95 at 5c. WTI remains the more shielded US benchmark relative to Brent. |
| KXGOLDW | [[Gold]] close above thresholds | Bid/ask crosses around the mid-$4,400/oz area; >$4,735.99 had a 0c / 5c bid-ask despite a large stale last-volume footprint. Treat the gold ladder as useful but noisy. |
| KXSILVERW | [[Silver]] close above thresholds | >$73.99 traded at 54c last, >$75.99 at 35c, and >$79.99 at 6c. The near-term center is far below the January $93.75 spike, but the contract ladder still prices a visible upper tail. |
| KXCOPPERW | [[Copper]] close above thresholds | Bid/ask crosses near $6.17-$6.20/lb; >$6.29 was 19c / 21c and >$6.38 was 4c / 11c. Copper remains a live AI/infrastructure scarcity expression, but the weekly Kalshi liquidity is thin. |
| KXNATGASW | [[Natural gas]] close above thresholds | >$3.199 traded at 74c, >$3.299 at 38c, >$3.399 at 25c, and >$3.499 at 5c. Henry Hub is not pricing an immediate $4+ spike. |

Scope note: obvious D/W series probes for [[Lithium]], [[Nickel]], and [[Diesel fuel]] returned no active markets in this pull, so those were not written as live market-implied signals.

*Sources: [Kalshi commodities hub announcement](https://news.kalshi.com/p/kalshi-launches-commodities-hub-new-markets), Apr 15 2026; [[Kalshi]] API series KXBRENTW, KXWTIW, KXGOLDW, KXSILVERW, KXCOPPERW, and KXNATGASW, read May 20 2026.*

---

## Index composition

### BCOM (Bloomberg Commodity Index)

[[Bloomberg Commodity Index|BCOM]] is the institutional broad-commodity benchmark. Its target weights use a two-thirds liquidity / one-third production framework with diversification caps: no group above 33%, no single commodity above 15%, and annual rebalancing. The total-return version, BCOMTR, is the relevant allocation benchmark because it captures the collateralized futures return.

As of Bloomberg's April 30, 2026 factsheet, BCOM's current sector weights were 39.28% energy, 26.64% agriculture, 15.50% precious metals, 13.48% industrial metals, and 5.10% livestock. The local DB has `BCOM` and `BCOMTR` in `prices_long`; use [[COMB]] when a tradable Bloomberg-linked ETF proxy is needed.

### DBC (Invesco DB Commodity Index)

| Sector | Weight |
|--------|--------|
| Energy | ~55% |
| Agriculture | ~22% |
| Base metals | ~13% |
| Precious metals | ~10% |

Optimized roll methodology to reduce contango drag.

### GSG (iShares S&P GSCI)

| Sector | Weight |
|--------|--------|
| Energy | ~60% |
| Agriculture | ~17% |
| Industrial metals | ~11% |
| Precious metals | ~5% |
| Livestock | ~7% |

Production-weighted — heavily energy-tilted.

---

## Key drivers

| Driver | Impact |
|--------|--------|
| **[[US dollar]]** | Inverse — strong USD pressures prices |
| **China demand** | 50%+ of base metals, major ag importer |
| **Interest rates** | High rates = opportunity cost of holding |
| **Inflation** | Commodities hedge inflation |
| **Supply disruptions** | Weather, geopolitics, [[OPEC]] |
| **Green transition** | Copper, lithium, nickel demand |

---

## Commodity supercycles

Historical supercycles driven by:
1. **1970s** — Oil shocks, inflation
2. **2000s** — China industrialization
3. **2020s?** — Green transition, supply underinvestment

Current debate: Are we in early stages of new supercycle driven by electrification and underinvestment?

---

## Contango vs backwardation

| Structure | Meaning | Impact on ETFs |
|-----------|---------|----------------|
| **Contango** | Futures > spot | Negative roll yield (drag) |
| **Backwardation** | Spot > futures | Positive roll yield (boost) |

Most commodity ETFs hold futures, not physical. Roll yield matters for long-term returns.

---

## Investment vehicles

| Ticker | Name | Structure |
|--------|------|-----------|
| COMB | GraniteShares Bloomberg Commodity Broad Strategy | BCOM-linked, no K-1 |
| DBC | Invesco DB Commodity | Optimized roll |
| GSG | iShares S&P GSCI | Production-weighted |
| PDBC | Invesco Optimized Commodity | K-1 free |
| COMT | iShares Commodity | K-1 free |
| USCI | United States Commodity | Momentum-based |

---

## Sector-specific ETFs

| Sector | Tickers |
|--------|---------|
| **Energy** | USO, UNG, UGA |
| **Precious metals** | GLD, SLV, PPLT, PALL |
| **Base metals** | DBB, CPER |
| **Agriculture** | DBA, CORN, WEAT, SOYB |

---

## Related

- [[Oil]] — largest commodity market
- [[Bloomberg Commodity Index]] — institutional broad commodity benchmark
- [[COMB]] — Bloomberg-linked ETF proxy
- [[Natural gas]] — energy sector
- [[Gold]] — safe haven precious metal
- [[Copper]] — industrial bellwether
- [[Base metals]] — industrial metals
- [[Agriculture]] — grains and softs
- [[Inflation]] — commodity linkage
- [[China]] — demand driver

---

*Created Jan 2026.*
