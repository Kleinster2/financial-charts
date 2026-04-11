---
aliases:
  - PB
  - Prime broker
  - Prime services
  - Prime book
tags:
  - concept
  - finance
  - markets
  - positioning
---

# Prime brokerage

**Prime brokerage** — The division at major banks that services hedge funds: securities lending, margin financing, trade clearing/settlement, custody, and reporting. Not a product — an infrastructure relationship. The PB is the hedge fund's operational backbone, and the data it generates from that relationship is the most granular positioning signal available to institutional investors.

---

## What it is

A prime broker provides the full operational stack a hedge fund needs to trade: borrowing shares for short selling, financing leveraged positions on margin, clearing and settling trades, holding assets in custody, and generating portfolio reports. Revenue comes from securities lending fees, margin interest, transaction fees, and financing spreads.

The relationship is bilateral and sticky. A hedge fund's PB sees every share borrowed, every margin call, every cover. This makes the PB not just a service provider but an information aggregator — across hundreds of clients, it assembles a composite picture of institutional positioning that no other market participant can replicate.

---

## Why PB data is the best positioning signal

PBs see the actual ledger. [[Goldman Sachs]], [[Morgan Stanley]], and [[JPMorgan Chase]] collectively prime ~60-70% of institutional equity flow. The data products they generate from this:

| Product | What it shows |
|---------|---------------|
| Prime book snapshots | Aggregate long/short ratios across all HF clients |
| Most-shorted baskets (e.g., Goldman's GSMS) | Stocks with highest [[Short interest]] as % of float, tracked as an index |
| Gross/net leverage | Gross = total longs + total shorts as multiple of NAV; net = longs minus shorts. Gross measures systemic risk regardless of direction |
| Sector flow data | Which sectors clients are adding/cutting, broken out by long buys vs short covers vs new shorts |

These reports circulate to institutional clients as "Prime Services" notes — that's where [[Bloomberg]] and financial press pick up positioning numbers. When a headline says "hedge funds are selling at the fastest pace in X years," the source is almost always a PB desk.

---

## The Big Three PB desks

| Desk | Strength | Client tilt |
|------|----------|-------------|
| [[Goldman Sachs]] | Largest by HF assets serviced | Most-cited PB data in financial press |
| [[Morgan Stanley]] | Strong in systematic/quant | Quantitative and systematic funds |
| [[JPMorgan Chase]] | Growing share | Credit-oriented and multi-strategy funds |

Together they see the majority of institutional equity positioning, but each sees a different client base. No single PB has the complete picture — this is a structural feature of the post-Lehman multi-prime era.

---

## What PB data shows vs doesn't show

Visible:
- Direct short positions (shares borrowed and sold)
- Margin posted against positions
- When shares get bought back (covered)
- Net exposure (longs minus shorts) across client books
- Leverage ratios

Partially visible:
- Synthetic shorts via [[Total return swaps]] (TRS) — visible to the structuring desk but messier to aggregate
- Options-based short exposure (delta-adjusted)

Not visible:
- Funds primed at competing banks
- Retail short activity
- OTC/bilateral derivative positions outside the PB relationship
- Cross-asset hedges (e.g., shorting equity via credit default swaps at a different counterparty)

The visibility gap is important. A fund running 1.5x gross at Goldman and 1.5x at Morgan Stanley appears modestly levered to each PB individually — but is 3x gross in aggregate. No single prime sees the full picture.

---

## Gross vs net leverage — why it matters

Net leverage is what most people think of: longs minus shorts. Low net = hedged. Gross leverage is the total capital deployed: longs + shorts as a multiple of NAV.

A fund can be "net flat" (equal longs and shorts) but at 3x gross leverage — meaning 1.5x long and 1.5x short. If both sides move against them (longs drop, shorts spike), the losses are amplified by the gross number, not the net. This is why gross leverage is the better systemic risk indicator.

April 2026: gross leverage hit 2.9x books (5-year high) even as funds covered shorts — the system carried more total risk regardless of directional bets. [[LTCM]] (1998) was the canonical gross leverage blow-up: low net, enormous gross, catastrophic unwind when Russian default triggered correlated moves across positions that were supposed to be uncorrelated.

---

## PB as early warning system

| [[Signal]] | Implication |
|--------|-------------|
| Rising borrow costs for specific stocks | Shorts piling in |
| Utilization rate approaching 100% | Squeeze risk — nearly all lendable shares on loan |
| Rapid covering in PB data | Often precedes the price move — PB sees the order before the tape does |
| Gross leverage at multi-year highs | Systemic fragility regardless of directional positioning |

Dealer gamma positioning data combined with PB utilization = the earliest available signal that a mechanical move is loading. When PB data shows covering accelerating, the squeeze is already underway in the institutional plumbing — price follows.

---

## Historical context

The PB business grew massively post-2000 as hedge fund AUM expanded from ~$500B to $5T. The major banks built PB desks into profit centers, earning billions from securities lending and margin financing.

2008 — [[Lehman Brothers]]'s collapse as inflection point. When Lehman filed for bankruptcy, its prime brokerage trapped client assets in the estate. Hedge funds that had consolidated with a single PB found their capital frozen. This reshaped the industry: funds deliberately spread across 2-3 PBs (the "multi-prime model") to avoid single-counterparty risk.

The fragmentation means no single bank sees the complete picture anymore. But [[Goldman Sachs]] still sees the largest slice, and its PB data remains the most-cited source for institutional positioning. The trade-off is structural: multi-prime reduces counterparty risk but degrades the information quality of any single PB's aggregate view.

---

## April 2026 case study — PB data in real-time

The short squeeze triggered by [[Trump II|Trump]]'s ceasefire announcement with [[Iran]] on April 8 was the most documented instance of PB data tracking a positioning unwind in real time.

[[Goldman Sachs]]'s PB desk saw the buildup: a 7.6:1 short-to-long ratio (selling pace fastest in 13 years), 76% of shorts concentrated in ETF/index products (macro de-risking, not stock-picking), and gross leverage at 2.9x (5-year high). When the ceasefire hit, covering began immediately — GS's most-shorted basket surged 7.1% in a single session, with shorts closing at the fastest pace since March 2020.

The data was available to institutional clients via Prime Services notes before the price move completed. This is the core value proposition of PB data: the PB sees the covering orders before they show up on the tape, and the aggregate view (sector flows, leverage changes, utilization rates) gives directional context that no exchange-reported [[Short interest]] data can match.

The key nuance: the rally was covering, not conviction. Gross leverage at 2.9x meant the system remained fragile — the same leverage structure that amplified the squeeze would amplify the next shock in the opposite direction if the ceasefire broke.

*See [[Goldman Sachs]] for full data tables; [[Short interest]] for squeeze mechanics.*

---

## Related

- [[Goldman Sachs]] — largest PB desk, April 2026 data
- [[Morgan Stanley]] — second-largest PB
- [[JPMorgan Chase]] — growing PB share
- [[Short interest]] — PB data as primary source for positioning
- [[Hedge fund capital concentration]] — leverage and systemic risk
- [[2026 Iran conflict market impact]] — case study of PB data predicting squeeze
- [[Crowded trade risk]] — PB utilization as crowding signal
- [[LTCM]] — canonical gross leverage blow-up (1998)
- [[Total return swaps]] — synthetic short exposure, partially visible to PB
- [[Multi-manager hedge funds]] — pod shops as primary PB clients

---

*Created 2026-04-10*
