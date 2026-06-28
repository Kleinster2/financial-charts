---
aliases: [Mean-variance optimization, MVO, Markowitz optimization, modern portfolio theory, efficient frontier]
tags: [concept, portfolio-construction, quant]
---

# Mean-variance optimization

Mean-variance optimization (MVO), introduced by Harry Markowitz (1952), is the foundation of modern portfolio theory: given expected returns and a covariance matrix, it solves for the weights that minimize variance for a target return, tracing out the efficient frontier. It is the optimization that [[Risk Parity]], [[Equal Risk Contribution]], and [[Hierarchical Risk Parity]] were all developed in reaction to.

*Chart not applicable: this is a portfolio-construction method, not a tradeable instrument or price series.*

---

## The problem

$$\min_w \tfrac{1}{2} w^T \Sigma w \quad \text{s.t.} \quad w^T \mu = \mu_{\text{target}}, \;\; w^T \mathbf{1} = 1$$

The optimizer needs two inputs: expected returns $\mu$ and the covariance matrix $\Sigma$. The first is the problem.

## Why it disappoints out of sample

MVO is notoriously fragile, and the fragility traces to the return input:

- Return estimates are very hard; a ±1–2% error in one asset's expected return swings its optimal weight enormously, while a risk-only method's weight does not move at all.
- It inverts the covariance matrix, amplifying estimation error and producing concentrated, corner-solution portfolios that flip on small input changes.
- It is an "error maximizer" (Michaud): it overweights exactly the assets whose returns were overestimated — the opposite of what helps forward performance.

The empirical upshot is that naive MVO often underperforms equal weight and [[Risk Parity]] out of sample despite being optimal in sample.

## How the fixes converge toward risk parity

Every standard repair makes MVO behave more like a risk-based method: shrinkage pulls return estimates toward equal, weight constraints ban corner solutions, resampling averages over input uncertainty, and Black-Litterman anchors to an equilibrium (with no views it returns market-cap or risk-balanced weights). [[Risk Parity]] and [[Equal Risk Contribution]] take the limit case — drop the return forecast entirely and optimize on covariance alone. [[Hierarchical Risk Parity]] goes one step further and removes the matrix inversion too.

## The trade-off

MVO is the right tool only when you genuinely have a return edge — accurate forecasts, a short tactical horizon with momentum, or a mandate that requires optimizing to a return target. For most investors over full cycles, return forecasts are unreliable, and the risk-only methods' agnosticism wins. As the line goes: MVO is optimal for the wrong problem; risk parity is suboptimal for the right one.

## Related

- [[Risk Parity]] — the agnostic response to MVO's return-forecast fragility
- [[Equal Risk Contribution]] — drops returns, optimizes on covariance alone
- [[Hierarchical Risk Parity]] — also removes the unstable matrix inversion
- [[Diversification vs Correlation]] — the covariance structure both methods consume
