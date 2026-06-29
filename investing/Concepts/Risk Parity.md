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
| [[Risk Budgeting]] | Allocate by each asset's risk contribution, not its capital weight |
| [[Equal Risk Contribution]] | Each asset contributes equally to portfolio variance — the equal-budget case |
| [[Hierarchical Risk Parity]] | Clustering-based allocation that avoids unstable covariance-matrix inversion |
| All Weather | [[Ray Dalio]]'s implementation — equal risk across the four [[Economic Environment Framework]] quadrants (growth × inflation) |
| [[Volatility Targeting]] | Scales total exposure to maintain constant portfolio vol |

## Vehicles tracked

| ETF | Strategy | Expense |
|-----|----------|---------|
| RPAR | Risk parity — stocks, bonds, commodities, TIPS, gold | 0.50% |
| UPAR | 1.5x levered RPAR | 0.65% |
| [[ALLW]] | All-weather balanced allocation | Varies |
| [[DBMF]] | Managed futures (trend-following complement) | 0.85% |
| KMLM | KFA Mount Lucas managed futures | 0.90% |
| CTA | Managed futures | Varies |
| NTSX | 90/60 capital-efficient (US equity + Treasuries) | 0.20% |
| NTSI | 90/60 capital-efficient (intl developed) | 0.26% |
| NTSE | 90/60 capital-efficient (emerging mkts) | 0.32% |
| GDE | 90/90 equity + gold futures | 0.20% |
| SWAN | Tail-hedged (Treasuries + S&P LEAP calls) | 0.49% |
| TAIL | Tail risk (rolling S&P puts + Treasuries) | 0.59% |
| AOR | 60/40 benchmark (iShares Core) | 0.15% |

## Key managers

| Manager | Strategy | Notes |
|---------|----------|-------|
| [[Bridgewater]] | All Weather / Pure Alpha | Largest risk parity manager (~$150B). [[Ray Dalio]] pioneered the approach |
| [[AQR]] | Risk Parity fund | [[Cliff Asness]]. Academic rigor, factor-aware implementation |
| PanAgora | Risk parity | Institutional-focused |
| [[Wealthfront]] | Risk Parity sleeve | Retail robo-advisor implementation |

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

## Sleeve performance

The full risk-parity sleeve universe — 13 ETFs across five strategy families — now lives in the financial-charts database, chartable from the hub for the first time. Grouped by what each sleeve actually bets on, normalized total return with dividends reinvested:

### Managed futures vs equities

![[rp-managed-futures-performance.png]]
*[[DBMF]], CTA and KMLM (managed futures) vs [[SPY]] — normalized total return since Mar 2022.*

| Sleeve | Strategy | Total return | CAGR | Since |
|--------|----------|--------------|------|-------|
| [[DBMF]] | Managed futures (SG CTA replication) | +32.8% | +6.8% | Mar 2022 |
| CTA | Managed futures (Altis) | +31.2% | +6.5% | Mar 2022 |
| KMLM | Trend following (Mount Lucas) | −3.9% | −0.9% | Mar 2022 |
| [[SPY]] | S&P 500 benchmark | +86.1% | +15.5% | Mar 2022 |

*Since CTA's 2022 inception. The point of this chart is what it does not show — correlation to equities. Managed futures trailed a roaring S&P by 50–90pp, but that lag is the price of the hedge: in the 2022 drawdown these sat above SPY (crisis alpha), which is exactly why risk parity bolts them on. DBMF and CTA delivered ~6.5% CAGR with low equity beta; pure-trend KMLM round-tripped to flat. Diversifiers, not return engines — judged on when they pay, not how much.*

### Capital-efficient (return-stacking)

![[rp-capital-efficient-performance.png]]
*NTSX/NTSI/NTSE (90/60 return-stacking) and GDE (equity + gold) vs [[SPY]] — normalized total return since Mar 2022.*

| Sleeve | Structure | Total return | CAGR | Since |
|--------|-----------|--------------|------|-------|
| GDE | 90% equity + 90% gold futures | +169.7% | +26.1% | Mar 2022 |
| NTSE | 90/60 emerging markets | +67.8% | +12.9% | Mar 2022 |
| NTSX | 90/60 US (S&P + Treasuries) | +54.4% | +10.7% | Mar 2022 |
| NTSI | 90/60 international developed | +44.6% | +9.0% | Mar 2022 |
| [[SPY]] | S&P 500 benchmark | +75.7% | +14.1% | Mar 2022 |

*Since GDE's 2022 inception. Capital-efficient funds stack bonds or gold on top of full equity exposure via futures — NTSX is 90% stocks plus 60% Treasuries, 150% notional per dollar. The 2022 rate shock punished the bond overlay, so US NTSX actually trailed plain SPY: the sleeve meant to diversify instead dragged. GDE is the outlier — equity plus levered gold rode gold's 2024–26 run to +170%, a reminder that the efficient wrapper only helps when the stacked asset works.*

### Tail risk / defensive

![[rp-tail-defensive-performance.png]]
*SWAN and TAIL (tail-hedged) vs [[SPY]] — normalized total return since Nov 2018.*

| Sleeve | Structure | Total return | CAGR | Since |
|--------|-----------|--------------|------|-------|
| SWAN | 90% [[Treasuries]] + 10% S&P LEAP calls | +66.2% | +6.9% | Nov 2018 |
| TAIL | Treasuries + rolling S&P puts | −38.8% | −6.2% | Nov 2018 |
| [[SPY]] | S&P 500 benchmark | +197.9% | +15.4% | Nov 2018 |

*Since SWAN's 2018 inception — the clearest "insurance has a cost" picture in the set. TAIL buys put protection and bleeds premium every quarter equities don't crash: down 39% over 7.5 years, its only green spikes at the 2020 and 2025 selloffs. SWAN's asymmetric build — Treasuries plus call options rather than puts — captured roughly a third of SPY's return with far shallower drawdowns. Both are hedges; TAIL is convexity you rent outright, SWAN is convexity partly funded by carry.*

## Composition history

The Risk Parity vault tracks each sleeve's holdings daily; that composition history now lives in `market_data.db` (`rp_fund_metrics_long`, `rp_allocations_long`), parsed from 456 dated tracking notes back to 2020. Two reads stand out.

### Leverage: defensive vs designed

![[rp-leverage-history.png]]
*Gross leverage estimated from disclosed holdings. ALLW runs ~1.6x (levered as designed); RPAR (~0.87x) and UPAR (~0.98x) sit at or below unlevered — far under their ~1.2x and ~1.8x targets. This is the post-2022 defensive positioning made visible: the two ARIS funds have effectively stopped levering, which is why UPAR (nominally "1.5x RPAR") has tracked RPAR so closely.*

| Fund | Leverage (Jun 2026) | Target | Read |
|------|---------------------|--------|------|
| RPAR | 0.87x | ~1.2x | Defensive — cash buffer |
| UPAR | 0.98x | ~1.8x | Essentially unlevered — defeats the 1.5x design |
| ALLW | 1.63x | — | Levered as designed |

### RPAR allocation drift

![[rpar-allocation-history.png]]
*RPAR's deleveraged sleeve weights, 2020–2026. Rates (nominal bonds + [[TIPS]]) built from ~25% to ~40%; equities drifted down from ~40% to ~30%; commodities recovered from a 2021 trough to ~28–30%. The bonds/TIPS split is combined here because RPAR shifted its rates sleeve from TIPS to nominal late 2025, and the 2020–25 SEC N-PORT data classifies rates differently from the 2026 daily feed — so read the blue line as the rates sleeve, not a nominal/TIPS breakdown. The durable signal is a fund that de-risked equity and leaned into commodities and rates across the cycle.*

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
- [[Iran conflict portfolio hedging]] — Mar 2026: second correlation breakdown in four years, practitioner hedging strategies
- [[Bridgewater]] — largest risk parity practitioner
- [[AQR]] — academic leader in risk parity research
- [[Ray Dalio]] — invented All Weather
- [[Analysts and Strategists]] — macro thinkers on correlation regimes
- [[iShares Core Asset Allocation ETFs]] — the capital-weighted, unlevered allocation ladder this strategy is measured against
- [[Risk Budgeting]] — the allocate-by-risk frame; [[Equal Risk Contribution]] is its equal-budget core
- [[Hierarchical Risk Parity]] — robust clustering-based construction; reuses the vault's cluster-validation machinery
- [[Economic Environment Framework]] — the growth×inflation quadrants risk parity is built to span
- [[Diversification vs Correlation]] — why position count isn't diversification; the effective-number-of-bets metric
- [[Volatility Targeting]] — time-series risk scaling, the complement to cross-sectional ERC
- [[Trend following]] — the crisis-alpha complement; the strategy the managed-futures sleeves run
- [[Mean-variance optimization]] — the return-forecast-dependent optimizer risk parity reacts against
- [[Factor investing]] — diversify across factors vs across asset-class risk
- [[Risk parity literature]] — the five foundational papers (Qian, Maillard, Asness, Roncalli, López de Prado)

### Cross-vault
- [Risk Parity vault](obsidian://open?vault=Risk%20Parity&file=Home) — full research vault: theory, backtests, fund tracking (RPAR/UPAR/ALLW), regime analysis
- [Risk Parity: Performance by Regime](obsidian://open?vault=Risk%20Parity&file=06%20-%20Historical%20Performance%2FPerformance%20by%20Regime) — four-quadrant framework, RP advantage in stagflation (+5.7pp vs 60/40)
- [Risk Parity: 2022 Rate Shock](obsidian://open?vault=Risk%20Parity&file=06%20-%20Historical%20Performance%2F2022%20Rate%20Shock) — RPAR fund attribution, post-2022 recovery tracking, regime change verdict
