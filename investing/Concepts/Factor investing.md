---
aliases: [Factor-based investing, Smart beta, Factor premia]
tags: [concept, investing, quant]
---

Factor investing is a systematic investment approach that targets specific, empirically identified return drivers (factors) across asset classes, forming the intellectual foundation for smart beta ETFs, quantitative hedge funds, and risk parity strategies.

## Synopsis

The academic roots trace to Fama-French (1993), which demonstrated that two factors — value (cheap stocks outperform expensive) and size (small caps outperform large caps) — explained equity returns better than CAPM's single market factor. Subsequent research added momentum (Jegadeesh-Titman, 1993), profitability/quality (Novy-Marx, 2013), and low volatility (Baker-Bradley-Wurgler, 2011). These five or six canonical factors now underpin a ~$2T smart beta ETF industry and the strategies of quantitative firms like [[AQR Capital]], [[Dimensional Fund Advisors]], and [[Two Sigma]]. The practical insight: most active manager "alpha" decomposes into factor exposures — [[Berkshire Hathaway]]'s outperformance, for instance, is largely quality + low-volatility + leverage per the [[Buffett's Alpha]] paper (Frazzini-Kabiller-Pedersen, 2018).

The investment debate centers on whether factor premia persist after they become widely known and traded. Value has underperformed growth dramatically since ~2015 (driven by tech/growth mega-caps), leading some to argue the value premium is arbitraged away. Momentum remains robust but crashes spectacularly in regime changes (momentum lost 40%+ in the 2009 reversal). Low volatility works — until it becomes crowded and the "low vol" basket trades at growth-stock valuations. The pragmatic approach is multi-factor diversification: combining factors that are negatively correlated (value and momentum tend to offset) to smooth returns. [[Risk Parity]] strategies like [[RPAR]] incorporate factor thinking by diversifying across risk premia rather than asset classes. The key insight for portfolio construction: if you cannot identify which factor you are exposed to, you are taking uncompensated risk.

## Canonical factors

| Factor | Definition | Empirical basis |
|--------|-----------|-----------------|
| Market | Equity risk premium over risk-free | CAPM (Sharpe, 1964) |
| Value | Cheap vs expensive (B/P, E/P) | Fama-French (1993) |
| Size | Small cap vs large cap | Fama-French (1993) |
| Momentum | Recent winners vs losers | Jegadeesh-Titman (1993) |
| Quality/Profitability | Profitable vs unprofitable | Novy-Marx (2013) |
| Low Volatility | Low-beta vs high-beta | Baker-Bradley-Wurgler (2011) |

## Factor performance (since 2013)

![[factor-zoo-performance.png]]
*The five canonical factor ETFs vs [[SPY]], normalized total return since July 2013 (common inception window).*

| Factor ETF | Factor | Total return | CAGR |
|------------|--------|--------------|------|
| MTUM | Momentum | +597% | +16.2% |
| QUAL | Quality | +410% | +13.4% |
| VLUE | Value | +393% | +13.1% |
| SIZE | Size | +315% | +11.6% |
| USMV | Low volatility | +262% | +10.5% |
| [[SPY]] | Market (cap-weight) | +438% | +13.9% |

*The persistence debate made empirical: over 2013–26 only momentum beat the cap-weighted market. Value, size, and quality lagged SPY through the mega-cap growth era, and low-vol lagged most on raw return — the trade it makes for lower drawdowns. This single-factor decay is the case for multi-factor diversification rather than a single tilt.*

## vs risk parity

Factor investing and [[Risk Parity]] are both anti-benchmark, diversification-first approaches, but they differ on the unit of diversification: factor investing spreads risk across return drivers (value, momentum, carry), risk parity across asset-class risk. They overlap most at the low-volatility factor — Asness, Frazzini and Pedersen (2012) showed risk parity is partly a levered bet on the low-vol / betting-against-beta premium, since both overweight low-risk assets and rest on the same leverage-aversion rationale. Decomposed into factors, a risk-parity portfolio reads as long duration, long low-vol, and long carry. The two combine as factor risk parity: budget risk equally across factors rather than asset classes. The trade-off mirrors this note's persistence debate — factor investing needs a view on which premia survive crowding, while risk parity needs only a covariance estimate and the assumption that diversification holds.

## Related

- [[Risk Parity]] — diversifies across asset-class risk rather than factors; overlaps at the low-vol premium
- [[Buffett's Alpha]] — Berkshire's returns decomposed into factor exposures
- [[Berkshire Hathaway]] — case study in quality + low-beta + leverage
- [[RPAR]] — risk parity ETF incorporating factor diversification
- [[AQR Capital]] — leading factor-based quantitative manager
- [[Dimensional Fund Advisors]] — systematic factor tilts in mutual funds/ETFs
