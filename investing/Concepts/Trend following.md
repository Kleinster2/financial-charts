---
aliases: [Trend following, managed futures, time-series momentum, CTA strategy, crisis alpha]
tags: [concept, systematic, alternatives]
---

# Trend following

Trend following is a systematic strategy that goes long assets in uptrends and short assets in downtrends across many markets, using futures for leverage and short exposure. Its signature property is crisis alpha — because it can go short, it tends to profit precisely when long-only portfolios crash, which makes it a natural complement to [[Risk Parity]]. The investable form is the managed-futures fund ([[DBMF]], KMLM, CTA in the vault's sleeve set).

*Chart not applicable: trend following is a strategy; its investable sleeves are charted under [[Risk Parity]] (managed futures: DBMF, KMLM, CTA).*

---

## The signal

Position is the sign of the trend times a size:

$$\text{Position} = \text{sign}(\text{trend}) \times \text{size}$$

where the trend signal is some form of price momentum — price above a moving average, positive return over a lookback, or a breakout above a range. The strategy is direction-agnostic (long or short), trades across equities, bonds, commodities, and FX, and sizes positions with [[Volatility Targeting]].

## Crisis alpha

The reason risk parity and other long-biased books carry trend following is its behaviour in drawdowns. By flipping short as trends turn, it has historically delivered positive returns in the worst equity quarters:

| Crisis | 60/40-type book | Trend following |
|--------|-----------------|-----------------|
| 1987 crash | down | up sharply |
| 2000–02 dot-com | down | up |
| 2008 GFC | down | up |
| 2020 COVID | down | up modestly |
| 2022 rate shock | down | up |

The flip side is the cost of carry: in calm, trending-up bull markets it earns little or bleeds — the managed-futures sleeves tracked under [[Risk Parity]] lagged a +15% S&P over 2022–26 while staying near-uncorrelated. It is a diversifier judged on when it pays, not how much.

## Versus risk parity

| Aspect | [[Risk Parity]] | Trend following |
|--------|-----------------|-----------------|
| Market view | Agnostic | Trends persist |
| Direction | Always long | Long or short |
| Good times | Steady positive | Near-zero |
| Bad times | Negative (less than 60/40) | Positive (crisis alpha) |
| Correlation to stocks | Low positive | ~Zero |

The two correlate only ~0.2 to each other, which is why a blend (often around 60/40 risk-parity/trend) has historically produced higher risk-adjusted returns and shallower drawdowns than either alone — something is usually working, which also makes the blend easier to hold through dry spells.

## Related

- [[Risk Parity]] — the long-biased strategy trend following most complements
- [[Volatility Targeting]] — how trend positions are sized
- [[DBMF]] — managed-futures sleeve implementing the strategy (with KMLM, CTA)
- [[Stock-Bond Correlation Regime]] — trend following can go short bonds, its 2022 edge
