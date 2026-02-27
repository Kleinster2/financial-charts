# Market internals framework

#concept #markets #technical #framework

**Market internals framework** — a minimal set of orthogonal indicators for understanding the structure of what's happening beneath the index surface at any given time. Most popular market internals are redundant with each other. Four independent dimensions capture the full picture.

---

## The redundancy problem

Most breadth and volatility indicators are measuring the same underlying signal with different instruments.

### Redundant clusters

| Cluster | Indicators | What they all measure |
|---------|-----------|----------------------|
| **Breadth** | A/D line, % above 200 DMA, % above 50 DMA, new highs/lows, McClellan Oscillator | How many stocks are participating in a move |
| **Concentration** | RSP vs SPY spread, top-10 contribution to index return, HHI of index returns | How dependent the index is on a few names |
| **Index fear** | VIX, VVIX, put/call ratio, SKEW | How much protection the market is pricing in |

Within each cluster, indicators will occasionally diverge at the margins, but they're answering the same fundamental question. Tracking all of them adds noise, not signal.

### Best-in-class per cluster

| Cluster | Pick | Why |
|---------|------|-----|
| Breadth | **% above 200 DMA** | Smoothed, long-term, less noisy than daily A/D. Threshold is intuitive: >50% = bullish |
| Concentration | **RSP vs SPY** | Tradeable, intuitive, captures breadth + mega-cap drag in one spread |
| Index fear | **VIX** | The standard. SKEW and VVIX add marginal info about tail risk |

---

## The four orthogonal dimensions

These are genuinely independent — each can be high or low regardless of the others.

| Dimension | Question | Best indicator | What it captures |
|-----------|----------|----------------|-----------------|
| **Breadth** | How many stocks are participating? | % above 200 DMA | Direction of the average stock |
| **Dispersion** | How far are individual stocks moving? | Cross-sectional return σ (or ±20% constituent count) | Magnitude of micro-level moves |
| **Correlation** | Are stocks moving together or independently? | Implied correlation (ICJ) or realized pairwise correlation | Macro vs micro driver dominance |
| **Volatility** | How much is the index itself moving? | VIX | Aggregate uncertainty / fear |

### Why these four?

**Breadth without dispersion** is incomplete — you know most stocks are up but not whether they moved 1% or 15%.

**Dispersion without correlation** is incomplete — high dispersion with high correlation means everything is swinging together (macro shock). High dispersion with low correlation means stocks are moving independently (micro narratives).

**VIX without correlation** is incomplete — VIX can be low while individual stocks are extremely volatile if their moves cancel out (low correlation). Feb 2026 is exactly this.

---

## Market regimes

The four dimensions map to recognizable regimes:

| Regime | Breadth | Dispersion | Correlation | VIX | Example |
|--------|---------|------------|-------------|-----|---------|
| **Calm bull** | High | Low | Moderate | Low | 2017 |
| **Stockpicker's market** | High | High | Low | Low | **Feb 2026** |
| **Narrow rally** | Low | Moderate | High | Low | 2023 (Mag 7 carry) |
| **Macro panic** | Low | Low | Very high | High | March 2020 (COVID) |
| **Crisis with differentiation** | Mixed | Very high | Moderate | Very high | 2008-09 |
| **Complacency** | High | Low | Low | Very low | Late 2017 (pre-volmageddon) |

### Feb 2026 regime in detail

| Dimension | Reading | Signal |
|-----------|---------|--------|
| Breadth | High (7/11 sectors up, >60% of S&P outperforming) | Broad participation |
| Dispersion | Highest since 2009 (>20% of S&P moved ±20% YTD) | Extreme individual moves |
| Correlation | Low (stocks moving on micro narratives, not macro) | Earnings and AI repricing driving idiosyncratic moves |
| VIX | Subdued | Index calm despite internal chaos |

This combination — high breadth, high dispersion, low correlation, low VIX — is the purest stockpicker's market. Individual research gets rewarded because moves are large (dispersion), differentiated (low correlation), and broad (breadth), while the index tells you nothing (low VIX).

---

## How to use

### The dashboard — four tickers

| Dimension | Ticker | Source | What it measures | Free? |
|-----------|--------|--------|-----------------|-------|
| **Breadth** | MMTH ($SPXA200R) | TradingView / StockCharts | % of S&P 500 above 200 DMA | Yes |
| **Dispersion** | DSPX | [[CBOE]] | Implied dispersion from single-stock vs index option vols | Yes (delayed) |
| **Correlation** | ICJ | CBOE | Implied correlation among S&P 500 constituents | Yes (delayed) |
| **Volatility** | VIX | CBOE / everywhere | 30-day implied volatility of S&P 500 | Yes |

### Measurement detail

**Breadth — % above 200 DMA (MMTH / $SPXA200R)**

% of S&P 500 constituents trading above their 200-day moving average. The 200 DMA version is the smoothed structural read. Thresholds: >50% = bullish, <30% = oversold, >70% = overheated. The 50 DMA version ($SPXA50R) is faster for tactical signals. Both available intraday.

**Dispersion — CBOE S&P 500 Dispersion Index (DSPX)**

The purpose-built indicator. Derived from individual stock option implied vols vs index option vol — the gap between them is dispersion. Higher DSPX = market expects more idiosyncratic moves. The realized equivalent is the cross-sectional standard deviation of constituent returns over a trailing window (20-day or 60-day), computable from price data. The ±20% constituent count that [[Citadel Securities]] cited is cruder but more intuitive.

**Correlation — CBOE Implied Correlation Index (ICJ)**

Measures implied correlation among S&P 500 stocks, derived from index vol vs single-stock vols. High ICJ = market expects stocks to move together (macro-driven). Low ICJ = stocks expected to move independently (micro-driven). Mathematically linked to dispersion: index vol ≈ avg stock vol × avg correlation. So DSPX high + ICJ low is the consistent "stockpicker's market" signal. Realized 20-day pairwise correlation is the backward-looking equivalent.

**Volatility — VIX**

30-day implied vol. For term structure context: VIX vs VIX3M (3-month). VIX > VIX3M = inverted term structure = near-term fear (backwardation). VIX < VIX3M = contango = calm. VVIX (vol of vol) is useful at extremes — very high VVIX means the market expects VIX itself to spike. SKEW measures tail risk but is noisy.

### Reading the dashboard

At any point, check these four to understand market structure:

1. **MMTH** → participation (>50% bullish, <30% oversold, >70% overheated)
2. **DSPX** → magnitude of individual moves (compare to historical range)
3. **ICJ** → macro vs micro (high = macro-driven, low = stockpicker's market)
4. **VIX** → index-level fear (<15 calm, 15-25 elevated, >25 fear, >35 panic)

### Regime shifts to watch for

| Shift | What changes | Meaning |
|-------|-------------|---------|
| Correlation rising + VIX rising | Macro takes over | Reduce active bets, go passive/defensive |
| Correlation falling + dispersion rising | Micro narratives dominate | Increase active bets, fundamental research matters |
| Breadth falling + VIX flat | [[Breadth divergence\|Bearish divergence]] | Rally narrowing, caution |
| Breadth rising + mega-caps lagging | Rotation | [[Sector rotation\|Leadership change]], not selloff |

### What makes each regime tradeable

**Stockpicker's market (current):** Active > passive. Concentrated portfolios with real research outperform. >50% of active large-cap funds beating benchmark in Feb 2026 — best hit rate in ~20 years.

**Narrow rally:** Passive > active. Just own the index and ride the concentration. Active managers lag because they're underweight the few names driving returns.

**Macro panic:** Correlations → 1, everything falls together. Diversification fails within equities. Cash, treasuries, and volatility are the only hedges.

---

## Related

### Sister concepts
- [[Breadth divergence]] — deep dive on breadth indicators and the divergence pattern
- [[Single stock dispersion]] — deep dive on dispersion, the Feb 2026 extreme, and active management revival
- [[Sector rotation]] — the rotation mechanism that produces breadth/dispersion readings

### Market context
- [[Mega-cap tech acronyms]] — concentration that distorts index readings and drives RSP/SPY spread
- [[February 2026 AI Disruption Cascade]] — AI repricing as a driver of current high dispersion
- [[Stock-Bond Correlation Regime]] — cross-asset correlation dynamics

### Actors
- [[Citadel Securities]] — dispersion data (Scott Rubner)
- [[Goldman Sachs]] — active fund performance tracking
- [[CBOE]] — VIX, implied correlation products

---

## Sources

- CBOE implied correlation index methodology
- Citadel Securities dispersion research (Scott Rubner, Feb 2026)
- Goldman Sachs active fund performance analysis, Feb 2026

*Created 2026-02-27*
