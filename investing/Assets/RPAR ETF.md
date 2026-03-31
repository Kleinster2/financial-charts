---
aliases: [RPAR, Risk Parity ETF, ARIS Risk Parity ETF]
tags: [actor, etf, risk-parity]
ticker: RPAR
---

# RPAR ETF

**RPAR** is the ARIS Risk Parity ETF, a systematic risk parity fund sub-advised by [[ARIS]] (Advanced Research Investment Solutions). Launched December 2019. Targets equal risk contribution across asset classes at sub-1x leverage (0.87x as of March 2026). The fund made a dramatic regime change in late 2025: sold its entire TIPS allocation (~40% of portfolio) and replaced it with Treasury futures (~41% bonds), fundamentally altering its inflation exposure.

---

## Synopsis

RPAR is the accessible version of risk parity — no leverage, 0.50% expense, holds actual ETFs ([[VTI]], [[VWO]], [[VEA]]) plus individual commodity stocks and [[GLDM]]. AUM of $592M (Mar 2026) makes it the second-largest risk parity ETF after [[ALLW]]. The portfolio runs at 0.87x gross notional — meaning ~13% sits in T-bills as cash drag, a deliberate conservatism that costs ~50-70bps/year in a rising market.

The defining event in RPAR's history is the Q4 2025 TIPS-to-bonds rotation. From May 2020 through September 2025, RPAR held 0% nominal bonds and ~27-43% TIPS. Between the December 2025 and January 2026 snapshots, TIPS went to 0% and Treasury futures (10yr + ultra bond) appeared at ~36% of NAV. This is the largest single allocation shift in the fund's history and represents a fundamental bet: ARIS concluded that nominal duration is now more attractive than inflation-linked duration. In a portfolio with 0% TIPS and 41% nominal bonds, RPAR is maximally exposed to a surprise inflation re-acceleration — the opposite of what risk parity was designed to protect against.

The commodity sleeve is unique: ~43% GLDM (physical gold) and ~57% in a basket of ~80 individual commodity-linked stocks (XOM, DE, CVX, BHP, RIO, etc.). This is active stock selection, not index exposure — RPAR is picking individual miners, energy producers, and agricultural companies. The basket gives real commodity producer exposure vs ALLW's synthetic BCOMTR swap, but at the cost of equity-like correlation (~0.7 to broad markets) rather than pure commodity beta.

---

## Quick stats

| Metric | Value |
|--------|-------|
| Ticker | RPAR |
| Issuer | Toroso Investments (now Tidal Financial Group) |
| Sub-adviser | [[ARIS]] |
| Inception | December 13, 2019 |
| Expense ratio | 0.50% |
| AUM | $592M (Mar 13, 2026) |
| Exchange | [[NYSE]] Arca |
| Leverage | 0.87x (Mar 13, 2026) |
| Holdings | ~106 positions |

---

## Allocation (March 13, 2026)

| Asset class | Deleveraged % | Notional % of NAV | Risk contribution |
|---|---|---|---|
| Bonds | 40.9% | 35.7% | 27% |
| Equities | 28.2% | 24.6% | 35% |
| TIPS | 0.0% | 0.0% | 0% |
| Commodities | 30.9% | 27.0% | 38% |
| Cash/T-bills | — | 12.7% | — |

### Allocation evolution

![[rpar-notional-pct-chart.png]]
*Asset class weights since May 2020 (66 snapshots: 23 quarterly N-PORT + 43 daily). TIPS (green) dominated at ~40% from mid-2021 through Q3 2025, then collapsed to 0% in Q4 2025 — replaced by bonds (blue) at ~41%. Equities (pink) drifted from ~38% to ~28% as ARIS reduced equity risk contribution. Commodities (yellow) ranged 22-36%. The TIPS→bonds rotation is the single largest allocation change in RPAR's history.*

### Holdings detail

Equities: [[VTI]] $74.3M (51%), [[VWO]] $43.1M (30%), [[VEA]] $28.2M (19%)
Bonds: US 10yr futures $106.7M (50.5%), US Ultra Bond futures $104.4M (49.5%)
Commodities: [[GLDM]] $68.9M (43%) + ~80 individual commodity stocks $91.2M (57%)
Cash: US T-bill $68.3M + cash $7.1M

---

## Replication analysis

7-ETF replication using the fund's actual holdings where possible:

| RPAR holding | Mar 2026 value | Proxy | Mismatch |
|---|---|---|---|
| [[VTI]] | $74.3M | VTI | None — exact |
| [[VWO]] | $43.1M | VWO | None — exact |
| [[VEA]] | $28.2M | VEA | None — exact |
| US 10yr futures | $106.7M | [[IEF]] | Duration ~8yr vs 10yr |
| US Ultra Bond futures | $104.4M | [[TLT]] | Duration match ~20yr |
| Individual TIPS bonds | $0M (sold Q4 2025) | [[TIP]] | Good proxy when held |
| [[GLDM]] | $68.9M | GLDM | None — exact |
| Commodity stocks (~80) | $91.2M | [[GNR]] | Active picks vs index |

### Results

| Method | Total return | vs RPAR | Notes |
|---|---|---|---|
| RPAR (actual) | +29.23% | — | Dec 2019 - Mar 2026 |
| 7-ETF Dynamic | +31.62% | -2.39pp | Time-varying weights from 66 snapshots |
| 7-ETF Static | +46.33% | -17.10pp | Mar 2026 weights applied retroactively |

![[rpar-replication-comparison-chart.png]]
*Normalized comparison since inception. Dynamic replication (pink) tracks RPAR (blue) closely — only -2.39pp residual over 6+ years. Static replication (green) diverges upward because applying 2026's bond-heavy allocation retroactively captures bonds' post-2022 recovery that RPAR missed while holding TIPS. The 2022 drawdown (-18%) is captured almost exactly by the dynamic replication.*

### Gap analysis

The -2.39pp residual in the dynamic replication is remarkably small, confirming RPAR is easy to replicate. Residual sources:
- GNR vs actual commodity stock basket (~57% of commodity sleeve): ARIS actively picks ~80 stocks vs GNR's passive index. This is the primary alpha/tracking error source.
- TIP vs individual TIPS bonds: minor duration mismatch (TIP ~7yr weighted avg vs RPAR's specific maturity ladder)
- Rebalancing timing: quarterly N-PORT snapshots interpolated between dates vs RPAR's actual rebalancing schedule
- Cash drag: the 12.7% T-bill/cash position earns ~4.5% risk-free vs the proxy which allocates only 87.3% to risk assets (correctly captured)

The -17pp static vs dynamic gap reveals the cost of RPAR's allocation changes. Holding 2026 weights from inception would have returned +46% vs RPAR's actual +29% — the TIPS→bonds rotation was well-timed for 2026 but the years of heavy TIPS exposure (2021-2025) dragged performance vs a bonds-heavy counterfactual.

### Rolling correlation

![[rpar-rolling-correlation-chart.png]]
*30-day rolling correlation of RPAR vs 7-ETF replications. Dynamic replication (blue) sustains 0.8-0.95 correlation through most periods. Periodic drops to 0.6-0.7 correspond to the commodity stock basket diverging from GNR index — RPAR's active stock picks create short-term tracking error. Static replication (orange) correlation is more volatile, diverging when the actual allocation differed sharply from 2026 weights.*

---

## Price performance

![[allw-vs-rpar-price-chart.png]]

---

## Related

- [[ALLW]] — [[Bridgewater]]-backed competitor with TIPS but weak commodities
- [[UPAR ETF]] — leveraged version (~1.8x) from the same [[ARIS]] team
- [[Risk Parity]] — strategy overview
- [[VTI]], [[VWO]], [[VEA]] — equity holdings (exact)
- [[GLDM]] — gold holding (exact)
- [[GNR]] — proxy for commodity stock basket
- [[TIP]], [[TLT]], [[IEF]] — bond/TIPS proxies
