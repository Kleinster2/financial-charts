# VIX

The CBOE Volatility Index—the market's primary "fear gauge." Measures expected 30-day volatility of the S&P 500 derived from options prices.

![[vix-historical-full.png]]

## How to read it

| VIX level | Market state                              |
| --------- | ----------------------------------------- |
| 10-12     | Extreme calm, complacency risk            |
| < 15      | Low volatility, steady risk-on            |
| 15-20     | Normal, healthy bull market               |
| 20-30     | Elevated uncertainty, caution warranted   |
| 30-40     | High fear, significant stress             |
| > 50      | Crisis territory                          |

**Historical average:** 19.4 (since 1993), standard deviation 7.9.

## Interpreting spikes

A VIX spike means options traders are paying up for downside protection. It reflects *expected* volatility, not realized—so it can spike on anticipation before actual moves.

**Key insight:** VIX measures fear *intensity* but not *direction*. A spike says "something big is expected" but not what.

## Historical extremes

| Event                     | VIX peak | Date       |
| ------------------------- | -------- | ---------- |
| 2008 financial crisis     | 80+      | Oct 2008   |
| COVID crash               | 82       | Mar 2020   |
| April 2025 tariff crisis  | 50+      | Apr 2025   |
| 2011 debt ceiling / Europe| 48       | Aug 2011   |
| 2015 China deval          | 40       | Aug 2015   |

## 2025 performance

- **April 2025:** Spiked above 50 on Liberation Day tariffs—crisis-level reading
- **Recovery:** Dropped from > 50 to < 20 in under 100 days, one of only four such rapid declines in history
- **November 2025:** Peaked at 27.8 on tariff/Fed uncertainty
- **December 2025:** Settled near 15.8 after Fed cut

The year was "moderate volatility on average, punctuated by episodic spikes."

## Forward returns after spikes

When VIX closes above ~47, historical data (since 1990):

| Time horizon | Positive return % | Average return |
| ------------ | ----------------- | -------------- |
| 90 days      | 44%               | +3%            |
| 180 days     | 75%               | +13.4%         |
| 360 days     | 100%              | +35.3%         |

When VIX jumps > 50% in a month, S&P 500 averages +9.5% one year later (vs 8% historical average).

**Implication:** Extreme fear is typically a buying opportunity on 6-12 month horizons, though timing the bottom is difficult.

## VIX term structure

**Contango (normal):** Near-term VIX < longer-term VIX. Market expects current calm to give way to normal volatility.

**Backwardation (stressed):** Near-term VIX > longer-term VIX. Market expects current fear to subside. Often seen at panic peaks.

Backwardation flipping to contango can signal the worst is over.

![[vix-term-structure.png]]

## VIX family and variants

### VIX term structure

Cboe publishes five S&P 500 volatility gauges across timeframes:

| Index  | Timeframe | Use case                                      |
| ------ | --------- | --------------------------------------------- |
| VIX9D  | 9 days    | Fast-moving, captures imminent event risk     |
| VIX    | 30 days   | The standard, most-watched                    |
| VIX3M  | 3 months  | Smoother, less volatile than VIX              |
| VIX6M  | 6 months  | Medium-term expectations                      |
| VIX1Y  | 1 year    | Long-term baseline                            |

**Reading the term structure:**
- **Normal (contango):** VIX9D < VIX < VIX3M < VIX6M < VIX1Y — calm, upward-sloping
- **Inverted (backwardation):** VIX9D > VIX > VIX3M — near-term fear elevated, often at panic peaks
- **Fully inverted:** VIX1Y < VIX6M < VIX3M < VIX < VIX9D — serious stress, not a short-term blip

### VVIX (volatility of volatility)

Measures expected volatility of VIX itself. If VIX is "velocity of fear," VVIX is "acceleration of fear." High VVIX means VIX could move sharply in either direction.

### Cross-asset volatility indices

| Index | Asset            | Description                                    |
| ----- | ---------------- | ---------------------------------------------- |
| MOVE  | US Treasuries    | Bond market fear gauge, can lead VIX           |
| OVX   | Crude oil (USO)  | Energy volatility                              |
| GVZ   | Gold (GLD)       | Precious metals volatility                     |
| EVZ   | EUR/USD          | Currency volatility                            |
| VXEEM | EM equities      | Emerging market equity volatility              |

**MOVE Index:** Created by Harley Bassman at Merrill Lynch. Measures implied yield vol on 2Y, 5Y, 10Y, 30Y Treasury options. Often spikes before VIX—bond market sends earlier warnings. (Proprietary data, not in database.)

| MOVE level | Interpretation                    |
| ---------- | --------------------------------- |
| < 80       | Calm, stable policy expectations  |
| 80-120     | Normal uncertainty                |
| > 120      | Elevated stress                   |
| > 150      | Crisis (2008, 2020, 2023 banking) |

**STLFSI4 (St. Louis Financial Stress Index):** Free alternative to MOVE. Composite of 18 indicators including yield spreads, volatility, and credit metrics. Zero = normal, positive = above-average stress, negative = below-average.

![[stlfsi-historical.png]]

| STLFSI4 level | Interpretation              |
| ------------- | --------------------------- |
| < -1          | Very calm, complacency risk |
| -1 to 0       | Below-average stress        |
| 0 to 1        | Moderate stress             |
| > 1.5         | Elevated stress             |
| > 3           | Crisis (2008: peaked ~5.5)  |

### Tradable products

- **VXX, UVXY** — long volatility ETFs (decay in contango, poor long-term holds)
- **SVXY** — short volatility (risky, can blow up in spikes)
- **VIX futures** — term structure matters for roll yield

## Limitations

- Only measures S&P 500 implied vol, not other assets
- Can stay elevated during grinding selloffs or spike on quick drops
- Doesn't capture credit stress or rates volatility (use [[Credit spreads]], MOVE)

---

## Related

- [[Risk-on risk-off]] — framework VIX fits into
- [[Credit spreads]] — complementary risk indicator
- [[Sell America trade]] — when fear extends beyond equities
