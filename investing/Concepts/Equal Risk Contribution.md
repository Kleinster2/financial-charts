---
aliases: [Equal Risk Contribution, ERC, equal risk contribution]
tags: [concept, portfolio-construction, risk]
---

# Equal Risk Contribution

Equal Risk Contribution (ERC) is a portfolio-construction method in which every asset contributes the same share of total portfolio risk, accounting for both volatilities and correlations. It is the formal core of [[Risk Parity]] — the precise answer to "balance risk, not dollars" — and the equal-budget special case of [[Risk Budgeting]].

*Chart not applicable: Equal Risk Contribution is a portfolio-construction method, not a tradeable instrument or price series.*

---

## The condition

Each asset's risk contribution is its weight times its marginal contribution to portfolio volatility:

$$RC_i = w_i \cdot \frac{\partial \sigma_p}{\partial w_i} = \frac{w_i (\Sigma w)_i}{\sigma_p}$$

ERC holds when every $RC_i$ is equal — so with $n$ assets each contributes exactly $\sigma_p / n$, i.e. $1/n$ of portfolio risk. Equivalently, $w_i (\Sigma w)_i = w_j (\Sigma w)_j$ for all $i, j$.

## Why there is no closed form

With non-zero correlations an asset's risk contribution depends on its own volatility, its weight, and its covariance with every other asset. That couples the weights into a system of nonlinear equations with no analytic solution (except the two-asset case). It is solved numerically — cyclical coordinate descent (Griveau-Billion et al.) converges in 5–20 iterations; a log-barrier formulation or direct minimization of $\sum_{i,j}(RC_i - RC_j)^2$ also work.

### Two-asset special case

For two assets a closed form exists and is independent of their correlation:

$$w_1 = \frac{\sigma_2}{\sigma_1 + \sigma_2}, \qquad w_2 = \frac{\sigma_1}{\sigma_1 + \sigma_2}$$

### Uncorrelated special case

When all correlations are zero, ERC collapses to inverse-volatility weighting, $w_i = (1/\sigma_i) / \sum_j (1/\sigma_j)$. The correlation terms are exactly what separate true ERC from this naive version.

## Worked example

Three assets — stocks (σ=15%), bonds (σ=5%), commodities (σ=20%) — with a stocks/commodities correlation of 0.3:

| Method | Stocks | Bonds | Commodities |
|--------|--------|-------|-------------|
| Inverse vol | 22% | 67% | 11% |
| ERC | 20% | 62% | 18% |

ERC gives commodities more weight than inverse vol: their positive correlation with stocks means they need a larger position to contribute an equal share of risk. That correction — penalizing assets that co-move — is the entire value-add over inverse vol.

## ERC vs mean-variance

| Aspect | ERC | Mean-variance |
|--------|-----|---------------|
| Inputs | Covariance only | Covariance + return forecasts |
| Return forecast | None (agnostic) | Required |
| Estimation-error sensitivity | Lower | Higher |
| Turnover | Lower | Higher |
| Concentrated positions | Never (long-only, unique solution) | Often |

ERC's appeal is that it never needs a return forecast — the input most prone to estimation error — which is why it is more stable out of sample than [[Mean-variance optimization|mean-variance optimization]].

## Generalized risk budgeting

ERC is the equal-budget case of [[Risk Budgeting]]: replace the $1/n$ target with arbitrary budgets $b_i$ (summing to 1) and solve $RC_i = b_i \sigma_p$. That generalization lets a manager tilt risk — GDP-weighting, conviction-weighting — while keeping the risk-based discipline. The robust way to reach these weights at scale, without the covariance-matrix inversion the ERC optimizer implicitly leans on, is [[Hierarchical Risk Parity]].

## Related

- [[Risk Parity]] — ERC is its construction core
- [[Risk Budgeting]] — ERC is the equal-budget special case
- [[Hierarchical Risk Parity]] — clustering-based alternative that avoids matrix inversion
- [[Stock-Bond Correlation Regime]] — the correlations ERC consumes are regime-dependent, which is what breaks risk parity when they shift
