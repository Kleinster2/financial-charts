---
aliases: [Risk Budgeting, risk budget, risk budgeting]
tags: [concept, portfolio-construction, risk]
---

# Risk Budgeting

Risk Budgeting allocates a portfolio by deciding how much each position should contribute to total portfolio risk — the risk budget — rather than how much capital it receives. It is the general frame of which [[Equal Risk Contribution]] is the equal-budget special case, and the conceptual root of [[Risk Parity]].

*Chart not applicable: Risk Budgeting is a portfolio-construction framework, not a tradeable instrument or price series.*

---

## Capital weight vs risk budget

A 60/40 stock/bond portfolio is a capital budget: 60% of dollars to stocks. But because equities run roughly 3x the volatility of bonds, that same portfolio is about a 90/10 risk budget — nearly all the risk sits in equities (see [[Risk Parity]]). Risk budgeting inverts the question: set the risk shares first, then solve for the capital weights that deliver them.

## The general form

Each asset is assigned a budget $b_i$ (with $\sum_i b_i = 1$), and weights are chosen so that risk contributions match the budgets:

$$RC_i = w_i \frac{(\Sigma w)_i}{\sigma_p} = b_i \,\sigma_p$$

- Equal budgets ($b_i = 1/n$) give [[Equal Risk Contribution]].
- Custom budgets express a view: GDP-weighting, conviction tilts, or capping any single risk source.

Because the risk contributions couple through the covariance matrix, this is solved numerically — the same optimization, or the robust clustering-based [[Hierarchical Risk Parity]] approximation, used for ERC.

## Why budget risk instead of capital

- Risk, not capital, is what actually diversifies — a capital-balanced book can still be dominated by one volatile sleeve.
- It needs no return forecast, only a covariance estimate, so it sidesteps the most error-prone input in mean-variance optimization.
- It makes hidden concentration explicit: the 60/40's ~90% equity-risk share is invisible in capital terms and obvious in risk-budget terms.

The catch is that the budget is only as good as the covariance estimate, and covariances move with regime — the [[Stock-Bond Correlation Regime]] flip of 2022 is precisely a case where the realized risk budget diverged violently from the intended one.

## Related

- [[Equal Risk Contribution]] — the equal-budget ($1/n$) special case
- [[Hierarchical Risk Parity]] — robust, inversion-free way to hit risk budgets at scale
- [[Risk Parity]] — the strategy built on equal risk budgeting
- [[Stock-Bond Correlation Regime]] — why a fixed risk budget drifts when correlations shift
