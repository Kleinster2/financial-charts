# Breadth divergence

#concept #markets #technical #indicator

**Breadth divergence** — When market indexes and breadth indicators move in opposite directions. A leading indicator of trend reversals. Divergences in 2000 and 2007 preceded major bear markets by months. Core tool for distinguishing rotation from selloff.

---

## The family: concepts, indicators, patterns

These terms get used interchangeably but operate at three distinct layers.

| Layer | What it answers | Examples |
|-------|----------------|----------|
| **Concept** | What are we measuring? | Breadth, [[Single stock dispersion\|dispersion]] |
| **Indicator** | How do we measure it? | A/D line, McClellan Oscillator, RSP/SPY spread, % above 200 DMA |
| **Pattern** | What does the data tell us? | Divergence, [[Sector rotation\|rotation]], confirmation |

### Concepts

**Breadth** — *how many* stocks are participating in a move. The question is directional: are most stocks going up or down?

**[[Single stock dispersion|Dispersion]]** — *how far* individual stocks move relative to the index. You can have high breadth with low dispersion (most stocks up ~2%) or high breadth with high dispersion (some up 25%, others down 30%, but more winners than losers). They're independent dimensions.

### Indicators

Indicators are the instruments that *measure* the concepts.

| Indicator | Measures | How |
|-----------|----------|-----|
| A/D line | Breadth | Cumulative count of advancers minus decliners. Binary — magnitude doesn't matter |
| McClellan Oscillator | Breadth momentum | EMA of A/D spread. Like MACD for breadth |
| % above 200 DMA | Breadth (long-term) | Share of stocks in uptrends. Threshold: >50% = bullish |
| New highs vs new lows | Breadth (extremes) | Counts at the tails of the distribution |
| RSP vs SPY spread | Breadth + dispersion | Equal-weight vs cap-weight return gap. SPY overweights [[Mega-cap tech acronyms\|Mag 7]] (~30%); RSP treats every stock equally. When RSP outperforms, the average stock is beating the mega-caps |
| Cross-sectional return σ | Dispersion | Standard deviation of individual stock returns around the index. The pure dispersion metric |
| ±20% constituent count | Dispersion | How many stocks made extreme moves. Cruder but intuitive |

### Patterns

Patterns are what you *infer* from the indicators — they describe market regimes, not quantities.

**Divergence** — breadth indicators and the index moving in opposite directions. Index new highs + A/D lower highs = bearish divergence (top forming). Index new lows + A/D higher lows = bullish divergence (bottom forming).

**[[Sector rotation|Rotation]]** — money leaving one sector and entering another. Shows up as high dispersion (big moves both ways) with decent breadth (more winners than losers) and a flat index. Not a selloff — a leadership change.

**Confirmation** — breadth and the index agreeing. Both rising = healthy trend. Both falling = genuine weakness.

### Feb 2026 regime

Rotation out of tech → high breadth (7/11 sectors up) → high dispersion (20%+ moves in 1/5 of stocks) → RSP outperforming SPY → **no bearish divergence** because breadth is *confirming* the underlying strength, not contradicting it. The index is flat not because of weakness but because of cap-weight math.

---

## The concept

**Breadth** = participation. How many stocks are rising vs falling.

**Divergence** = index and breadth moving opposite directions.

| Scenario | Index | Breadth | [[Signal]] |
|----------|-------|---------|--------|
| **Bearish divergence** | New highs | Lower highs | Top forming, narrow leadership |
| **Bullish divergence** | New lows | Higher lows | Bottom forming, accumulation |
| **Confirmation** | Rising | Rising | Healthy trend |
| **Rotation** | Falling | Rising | Leadership change, not selloff |

---

## Why it matters

**Indexes lie.** Cap-weighted indexes can rise on a handful of mega-caps while most stocks decline. Breadth reveals the truth underneath.

> "Through decades of market cycles, one pattern consistently stands out: deterioration in market breadth nearly always precedes tops in large-cap-weighted indexes."

**The mechanism:**
1. Late-cycle rallies narrow to fewer leaders
2. Index makes new highs, but fewer stocks participate
3. Breadth indicators diverge (lower highs)
4. Eventually price catches down to breadth

---

## Key indicators

### Advance/Decline Line (A/D Line)

**The "granddaddy" of breadth indicators.**

| Metric | Calculation |
|--------|-------------|
| Net Advances | Advancing stocks − Declining stocks |
| A/D Line | Cumulative sum of Net Advances |

**[[Signal]]:** A/D Line making lower highs while index makes higher highs = bearish divergence.

### McClellan Oscillator

Momentum indicator for breadth (like MACD for advances/declines).

| Reading | [[Signal]] |
|---------|--------|
| Above +50 | Strong breadth thrust |
| Below −50 | Oversold breadth |
| Cross zero | Momentum shift |
| +100 point surge | Breadth thrust (bullish) |

### Percent Above Moving Averages

| Indicator | Timeframe | Threshold |
|-----------|-----------|-----------|
| % above 50 DMA | Short-medium term | >50% bullish, <50% bearish |
| % above 200 DMA | Long term | >50% bullish, <50% bearish |

**Divergence signal:** Index rising but % above 200 DMA falling = narrowing participation.

### New Highs vs New Lows

| Reading | [[Signal]] |
|---------|--------|
| Expanding new highs | Broad strength |
| Shrinking new highs (index up) | Bearish divergence |
| Expanding new lows | Broad weakness |
| Shrinking new lows (index down) | Bullish divergence |

---

## Historical warnings

| Year | Divergence | Lead time | What followed |
|------|------------|-----------|---------------|
| **2000** | A/D Line peaked before index | ~3 months | Dot-com crash (−49%) |
| **2007** | A/D Line lower highs Jul-Oct | ~3 months | GFC crash (−57%) |
| **2021** | Breadth peaked Nov 2021 | ~1 month | 2022 bear market (−25%) |

### The 2007 case study

**July 2007:** NYSE Composite at highs, A/D Line makes lower high → first warning

**October 2007:** Index surges to new highs, A/D Line well below July → second warning (double divergence)

**Result:** January 2008 support breaks, bear market begins.

> "2007 provided a near-picture perfect example of a breadth divergence with the S&P 500 making a clear higher high as both S&P and NYSE A-D Lines made lower highs."

---

## Rotation signature

**Distinct from bearish divergence:** In rotation, index falls but breadth is positive.

| Scenario | Index | Most stocks | Meaning |
|----------|-------|-------------|---------|
| **Bearish divergence** | Up | Weakening | Top forming |
| **Rotation** | Down | Up | Leadership change |
| **Selloff** | Down | Down | Risk-off |

**Jan 14, 2026 example:** S&P 500 −0.53%, but 300+ constituents rose. [[Nasdaq]] −1.0%. This is rotation — money leaving Mag 7, spreading to rest of market. Not a selloff.

See [[Sector rotation]] for current rotation dynamics.

---

## How to use

### For timing

| [[Signal]] | Action |
|--------|--------|
| Index highs + breadth lower highs | Reduce risk, tighten stops |
| Index lows + breadth higher lows | Accumulate, anticipate reversal |
| Index down + breadth up | Rotation — reposition, don't flee |

### Warning signs checklist

- [ ] A/D Line making lower highs while index rises
- [ ] % above 200 DMA declining while index rises
- [ ] New highs shrinking while index rises
- [ ] McClellan Oscillator negative divergence
- [ ] Fewer sectors participating in rally

### False signals

**Not every divergence leads to crash:**
- Can resolve with breadth catching up
- Divergences can persist for months
- Works better at extremes

---

## Current status (Feb 2026)

| Indicator | Reading | [[Signal]] |
|-----------|---------|--------|
| S&P sectors up | **7 of 11** | Decent sector-level breadth |
| Mag 7 YTD | **-5.6%** | Cap-weighted drag on index |
| S&P stocks beating index | **60%+** | More stocks up than down — but "beating a flat index" is a low bar |

**Interpretation (updated Feb 27):** Not a bearish divergence — the index is flat, not making new highs while breadth deteriorates. But the headline numbers need unpacking. 60%+ of stocks outperforming the index sounds like strong breadth, but the index is roughly flat — so "outperforming" mostly means "positive." The real story is **dispersion**, not breadth: [[Citadel Securities]] data shows single-stock dispersion at its highest since 2009, with >20% of S&P constituents moving ±20% YTD. That's extreme idiosyncratic repricing — big winners AND big losers — which is a different phenomenon from broad participation. Rotation (capital moving between sectors) can produce high dispersion without improving breadth if the buy side is narrow.

**What would confirm genuine breadth improvement:** A/D line making new highs, % above 200 DMA expanding, new highs broadening — not just "most stocks beat a flat index." Need to check actual breadth indicators, not just infer breadth from rotation and dispersion data.

See [[Sector rotation]] for the dispersion and rotation data (Feb 27 update).

### Previous reading (Jan 2026)

| Indicator | Reading | [[Signal]] |
|-----------|---------|--------|
| Russell 2000 vs S&P | 9-day outperformance streak | Rotation underway |
| S&P 500 breadth (Jan 14) | 300+ up on down day | Healthy rotation |
| Mag 7 vs S&P 493 | Mag 7 lagging since Oct 2025 | Leadership broadening |

---

## Related

### Sister concepts
- [[Market internals framework]] — positions breadth as one of four orthogonal dimensions for reading market structure; includes redundancy analysis of breadth indicators
- [[Sector rotation]] — current rotation uses breadth to distinguish from selloff
- [[Single stock dispersion]] — measures magnitude of moves (how far) vs breadth's direction count (how many); both elevated in Feb 2026

### [[Market structure]]
- [[Mega-cap tech acronyms]] — concentration that creates divergence risk
- [[Market forecasts]] — breadth as leading indicator
- [[Risk on risk off]] — breadth signals risk appetite

### Actors
- [[Goldman Sachs]] — tracks breadth in strategy research

---

## Sources

- [StockCharts - Advance-Decline Line](https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-line)
- [McClellan Financial - Oscillator](https://www.mcoscillator.com/learning_center/)
- [CMT Association - Breadth Reveals What Indexes Conceal](https://cmtassociation.org/chartadvisor/beneath-the-surface-what-breadth-reveals-that-indexes-conceal/)
- [[[Fidelity]] - Advance Decline Indicator](https://www.fidelity.com/learning-center/trading-investing/advance-decline)

*Created 2026-01-14, updated 2026-02-27*
