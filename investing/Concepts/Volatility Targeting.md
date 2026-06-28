---
aliases: [Volatility Targeting, vol targeting, volatility scaling]
tags: [concept, portfolio-construction, risk]
---

# Volatility Targeting

Volatility targeting scales total position size to hold portfolio volatility constant over time, rather than holding weights constant. When measured volatility rises, exposure is cut; when it falls, exposure is increased — the portfolio targets constant risk, not constant capital.

*Chart not applicable: volatility targeting is a position-sizing technique, not a tradeable instrument or price series.*

---

## The mechanism

$$w_t^{\text{scaled}} = w_t^{\text{base}} \times \frac{\sigma_{\text{target}}}{\hat{\sigma}_t}$$

Base weights are multiplied by the ratio of a target volatility (say 10%) to the current volatility forecast $\hat{\sigma}_t$. When the forecast doubles, exposure halves.

## Estimating volatility

| Method | Description | Typical lookback |
|--------|-------------|------------------|
| Rolling standard deviation | Simple, equal-weighted | 20–60 days |
| EWMA | Exponentially weighted, recent-heavy | λ ≈ 0.94 |
| GARCH | Autoregressive volatility model | model-dependent |
| Realized | Intraday high-frequency | intraday |

The estimator is a responsiveness-vs-stability trade-off: shorter or EWMA reacts fast but whipsaws; longer is stable but lags regime change.

## Why it helps, and where it bites

It delivers consistent risk exposure across regimes, de-risks automatically when volatility spikes (crisis protection), and has historically improved risk-adjusted returns. The costs: it trades most in volatile periods (transaction costs), it can sell after a vol spike and miss the recovery (volatility whipsaw), and it needs a leverage cap to avoid over-levering in calm markets.

## In risk parity

Risk-parity portfolios apply risk control in two dimensions at once: [[Equal Risk Contribution]] balances risk across assets (cross-sectional), and volatility targeting scales the whole book to a target (time-series). The first decides the mix; the second decides the gross exposure.

## Related

- [[Risk Budgeting]] — the cross-sectional counterpart to time-series vol targeting
- [[Equal Risk Contribution]] — balances risk across assets; vol targeting scales the total
- [[Risk Parity]] — combines both dimensions
- [[Stock-Bond Correlation Regime]] — volatility and correlation regimes drive the scaling
