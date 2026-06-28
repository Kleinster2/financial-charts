---
aliases: [Diversification vs Correlation, diversification, effective number of bets, ENB]
tags: [concept, portfolio-construction, risk]
---

# Diversification vs Correlation

True diversification depends on balancing risk, not on counting positions. Holding many assets buys nothing if they share a risk driver — and correlations, which determine how much diversification you actually get, are unstable and tend to spike toward 1 in exactly the crises when diversification is most needed.

---

## The diversification illusion

Ten holdings are not diversified if they are highly correlated, if one position dominates portfolio risk, or if their correlations converge in a crisis. The canonical case: a 60/40 portfolio holds two assets but draws roughly 90% of its risk from one (see [[Risk Parity]]). Position count is not diversification; risk balance is.

## Correlation drives portfolio risk

For two assets, portfolio variance is:

$$\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2 w_1 w_2 \sigma_1 \sigma_2 \rho_{12}$$

The cross-term carries the correlation. As $\rho$ falls the cross-term shrinks and portfolio volatility drops — lower correlation is the entire source of the diversification benefit.

## Effective number of bets

A risk-based measure of how diversified a portfolio really is:

$$\text{ENB} = \frac{1}{\sum_i p_i^2}$$

where $p_i$ is asset i's share of total risk. It counts independent bets, not positions:

| Portfolio | ENB |
|-----------|-----|
| Single asset | 1.0 |
| 60/40 (by risk) | ~1.2 |
| Equal risk, 4 assets | 4.0 |

The 60/40's ENB of ~1.2 is the diversification illusion quantified: two assets, barely more than one bet.

## Correlations are regime-dependent

![[imf-stock-bond-correlation-2000-2025.jpg]]
*Rolling 12-month stock-bond correlations (US: S&P 500 vs 1–3yr Treasuries; G4 cap-weighted). Source: Bloomberg, IMF staff calculations (2025). The 20-year negative-correlation regime ended around 2020; the US trend crossed zero by 2022 and sits near +0.25, G4 near +0.55.*

| Regime | Stock-bond correlation | Implication |
|--------|------------------------|-------------|
| Normal | Low / negative | Diversification works |
| Crisis (pre-2000s) | Negative | Bonds hedge stocks |
| Inflation shock | Positive | Both fall together |
| Liquidity crisis | Spikes positive | Diversification fails when most needed |

This is the empirical core of the [[Stock-Bond Correlation Regime]] problem: a fixed risk budget assumes a correlation that 2022 showed can flip, turning a diversifier into an amplifier.

## Managing correlation risk

Because correlations are estimated with error, drift over time, and spike in crises, the practical defenses are longer estimation windows, shrinkage estimators (blend the sample toward a prior), factor models for more robust structure, regime-switching models, and simply assuming higher crisis correlations than the sample shows.

## Related

- [[Stock-Bond Correlation Regime]] — the regime shift this note's chart documents
- [[Risk Parity]] — balances risk contributions so no single bet dominates
- [[Risk Budgeting]] — ENB is maximized when risk budgets are equalized
- [[Equal Risk Contribution]] — the construction that pushes ENB toward the asset count
