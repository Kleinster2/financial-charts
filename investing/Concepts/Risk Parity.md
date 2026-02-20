---
tags: [concept, portfolio-construction, macro]
aliases: [risk parity, equal risk contribution, risk budgeting]
---

# Risk Parity

Portfolio construction strategy that allocates by risk contribution rather than capital weight. Instead of 60/40 (which is ~90% equity risk), risk parity equalizes each asset class's contribution to total portfolio volatility, typically using leverage on lower-vol assets (bonds, commodities) to achieve target returns.

---

## Core idea

A traditional 60/40 portfolio appears diversified but is dominated by equity risk. Risk parity asks: what if you balanced risk instead of dollars?

| Approach | Stocks | Bonds | Commodities | Gold | Equity risk share |
|----------|--------|-------|-------------|------|-------------------|
| 60/40 | 60% | 40% | 0% | 0% | ~90% |
| Risk parity (typical) | ~20% | ~50% | ~15% | ~15% | ~25% |

The bond/commodity allocation is levered to match equity volatility. This works beautifully when stock-bond correlation is negative — and breaks when it isn't.

## The correlation problem

Risk parity's core assumption is that bonds hedge equities. The [[Stock-Bond Correlation Regime]] shift since 2020 is the strategy's biggest challenge:

- 2000-2020: negative correlation → bonds cushioned equity drawdowns → risk parity outperformed
- 2022+: positive correlation → levered bonds amplified losses → 2022 was the worst year for risk parity in decades
- G4 stock-bond correlation now ~+0.55 (IMF 2025 data)

This doesn't invalidate the concept — it means the implementation needs to adapt (more commodities, trend-following overlays, regime detection).

## Key frameworks

| Framework | What it does |
|-----------|-------------|
| Equal Risk Contribution (ERC) | Each asset contributes equally to portfolio variance |
| Hierarchical Risk Parity (HRP) | Uses clustering to avoid unstable covariance matrix inversion |
| All Weather | [[Ray Dalio]]'s implementation — balances across economic environments (growth/inflation × rising/falling) |
| Volatility targeting | Scales total exposure to maintain constant portfolio vol |

## Vehicles tracked

| ETF | Strategy | Expense |
|-----|----------|---------|
| RPAR | Risk parity — stocks, bonds, commodities, TIPS, gold | 0.50% |
| UPAR | 1.5x levered RPAR | 0.65% |
| ALLW | All-weather balanced allocation | Varies |
| DBMF | Managed futures (trend-following complement) | 0.85% |
| KMLM | KFA Mount Lucas managed futures | 0.90% |
| CTA | Managed futures | Varies |

## Key managers

| Manager | Strategy | Notes |
|---------|----------|-------|
| [[Bridgewater]] | All Weather / Pure Alpha | Largest risk parity manager (~$150B). [[Ray Dalio]] pioneered the approach |
| [[AQR]] | Risk Parity fund | [[Cliff Asness]]. Academic rigor, factor-aware implementation |
| PanAgora | Risk parity | Institutional-focused |
| Wealthfront | Risk Parity sleeve | Retail robo-advisor implementation |

## Historical stress tests

| Period | What happened | Risk parity result |
|--------|--------------|-------------------|
| 2008 GFC | Equities crashed, bonds rallied | Outperformed — bonds hedged perfectly |
| 2013 Taper Tantrum | Bonds sold off on Fed signaling | Underperformed — duration hurt |
| 2020 COVID | Brief correlation spike, then reversion | Mixed — recovered fast |
| 2022 Rate Shock | Stocks AND bonds fell together | Worst year — correlation flip destroyed the hedge |

## Current relevance (2026)

The post-2020 correlation regime shift has forced risk parity practitioners to evolve:
- More allocation to commodities and gold (uncorrelated to both stocks and bonds)
- Managed futures / trend-following overlays (CTA, DBMF, KMLM) as "crisis alpha"
- Dynamic regime detection — shift weights based on correlation environment
- Reduced bond leverage vs. pre-2020 implementations

The question isn't whether risk parity is dead — it's whether the implementation can adapt to a world where the bond hedge is unreliable.

## Who thinks about this

- [[Ray Dalio]] / [[Bridgewater]] — invented the modern framework
- [[Cliff Asness]] / [[AQR]] — academic formalization, "Risk Parity: Why We Bother"
- [[Lyn Alden]] — fiscal dominance thesis explains why correlation shifted
- [[Russell Napier]] — financial repression framework predicts sustained positive correlation
- [[Jim Bianco]] — bond bear market thesis directly challenges risk parity assumptions

---

## Detailed vault

Full research lives in the dedicated Risk Parity vault (`C:\Users\klein\obsidian\Risk Parity`), organized as:

| Section | Contents |
|---------|----------|
| 01 - Core Concepts | What is risk parity, diversification, leverage, economic environments |
| 02 - Asset Classes | Deep dives on each asset class's role |
| 03 - Risk Measurement | Correlation, VaR, regime detection, volatility estimation |
| 04 - Portfolio Construction | ERC, HRP, HERC, optimization algorithms |
| 05 - Implementation | ETFs, futures, rebalancing, costs, tax |
| 06 - Historical Performance | Crisis backtests, drawdown analysis, regime performance |
| 07 - Funds & Managers | Bridgewater, AQR, RPAR, UPAR, DBMF, KMLM profiles |
| 08 - Research & Papers | Qian (2005), Maillard (2010), López de Prado HRP |
| 09 - Comparisons | vs 60/40, vs trend following, vs factor investing |
| 10 - Portfolio Tracking | Daily tracking of RPAR, UPAR, ALLW, DBMF, KMLM, CTA |

---

## Related

- [[Stock-Bond Correlation Regime]] — the macro variable that determines whether risk parity works
- [[Bridgewater]] — largest risk parity practitioner
- [[AQR]] — academic leader in risk parity research
- [[Ray Dalio]] — invented All Weather
- [[Analysts and Strategists]] — macro thinkers on correlation regimes
