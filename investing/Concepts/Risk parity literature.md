---
aliases: [Risk parity literature, risk parity papers, risk parity bibliography]
tags: [concept, reference, portfolio-construction]
---

# Risk parity literature

The five works that built [[Risk Parity]] from a [[Bridgewater]] house style into a named, formalized, and explained strategy. Read in sequence they answer four questions in turn: what is it (Qian), is it well-defined (Maillard), why does it work (Asness), and how do you implement it robustly (Roncalli, López de Prado).

*Chart not applicable: this is a bibliography / reference note.*

---

## The five works

| Year | Work | Authors | Contribution |
|------|------|---------|--------------|
| 2005 | Risk Parity Portfolios | Edward Qian ([[PanAgora]]) | Coined "risk parity"; risk ≠ capital allocation |
| 2010 | Properties of ERC Portfolios | Maillard, Roncalli, Teïletche | Formalized [[Equal Risk Contribution]]; existence + uniqueness |
| 2012 | Leverage Aversion and Risk Parity | Asness, Frazzini, Pedersen ([[AQR]]) | The why: the betting-against-beta premium |
| 2013 | Introduction to Risk Parity and Budgeting | Thierry Roncalli | The canonical textbook; generalizes to [[Risk Budgeting]] |
| 2016 | Building Diversified Portfolios that Outperform OOS | Marcos López de Prado | [[Hierarchical Risk Parity]]; no matrix inversion |

## Qian (2005) — the name

Edward Qian at [[PanAgora]] gave the strategy its name and its core claim: a 60/40 portfolio allocates capital 60/40 but risk roughly 90/10, so it is "an equity portfolio with some bonds thrown in," not a balanced one. Real diversification means balancing risk contributions, then using leverage to lift the lower-risk, risk-balanced portfolio to a competitive return. This is the [[Risk Budgeting]] insight stated for the first time (backtest: 1983–2004 Sharpe 0.87 vs 0.62 for 60/40).

## Maillard, Roncalli & Teïletche (2010) — the proof

Published in the Journal of Portfolio Management, this gave [[Equal Risk Contribution]] its rigorous footing: for any positive-definite covariance matrix there exists a unique long-only ERC portfolio, it sits between the equal-weight and minimum-variance portfolios in concentration and variance, and for two assets it has the correlation-independent closed form $w_1 = \sigma_2/(\sigma_1+\sigma_2)$. It is the paper that made "balance the risk" a precise, solvable instruction.

## Asness, Frazzini & Pedersen (2012) — the why

The [[AQR]] paper that explained why risk parity earns a premium rather than merely rebalancing. Investors who cannot or will not use leverage bid up high-beta assets for their returns, flattening the security market line and leaving low-beta assets underpriced — the betting-against-beta (BAB) premium. Risk parity, by overweighting low-beta assets and levering, is an efficient way to harvest BAB across asset classes. This is the bridge to [[Factor investing]]: risk parity is partly a levered low-volatility factor bet.

## Roncalli (2013) — the textbook

Thierry Roncalli's "Introduction to Risk Parity and Budgeting" (Chapman & Hall/CRC) is the comprehensive reference: it generalizes ERC to [[Risk Budgeting]] with arbitrary budgets, extends risk contributions beyond volatility to VaR, expected shortfall, and drawdown, and works through constraints, estimation, and implementation. Where the earlier papers are arguments, this is the manual.

## López de Prado (2016) — the robust implementation

"Building Diversified Portfolios that Outperform Out-of-Sample" diagnosed the common failure of both mean-variance and ERC — reliance on inverting a noisy covariance matrix — and replaced it with [[Hierarchical Risk Parity]]: cluster assets by correlation distance, then allocate down the tree without ever inverting the matrix. It is risk parity made stable enough for large, short-history universes, and the method the vault's own cluster-validation work reuses.

## Related

- [[Risk Parity]] — the strategy these works define and justify
- [[Equal Risk Contribution]] — formalized by Maillard et al.
- [[Hierarchical Risk Parity]] — López de Prado's contribution
- [[Risk Budgeting]] — Qian's insight, Roncalli's generalization
- [[Factor investing]] — Asness et al. tie risk parity to the BAB / low-vol factor
- [[PanAgora]] — Qian's firm
