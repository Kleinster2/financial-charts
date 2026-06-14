---
name: event-tape
description: "Market-reaction measurement for listed-company events. Use when /ingest, /news, /earnings, event notes, actor notes, or securities notes need event-specific stock reaction adjusted for market, sector, and peer moves, with raw move, abnormal move, residual sigma, raw sigma, and abnormal/raw sigma outputs. Applies to after-close/pre-open announcements, intraday catalysts, M&A-adjacent events, financings, product launches, regulatory decisions, customer wins/losses, and peer read-throughs."
---

# Event Tape

Measure what the tape believed without confusing broad market beta, sector moves, or peer read-through with the company-specific event.

## Trigger

Use this whenever a listed-company event changes valuation, financing, competitive position, risk, or peer read-through. Run it before writing the final `## Market Reaction` section.

For public-company M&A, keep merger-arb fields from `docs/note-checklist.md#public-company-ma-market-reaction`; use this skill for the adjusted return and sigma stack.

## Event Window

- During market hours: use the pre-announcement regular-session price as the anchor, then the first stabilized post-announcement print after the initial noise subsides. Also update with the regular-session close when available.
- After close and before open: use the prior regular-session close to a stabilized next-day regular-session print around 10:00-10:30 ET. Also update with the next-day close when available.
- Weekend or holiday: use the prior regular-session close to the next regular-session stabilized print. Also update with that session's close when available.
- If the close is not available yet, write the status explicitly: `same-day close not yet available as of HH:MM ET; stabilized morning reaction is ...`. Do not use `TODO`, `TBD`, or `verify later`.

Match the historical volatility window to the reaction window when possible. If only daily data exists, label intraday sigma as approximate and prefer close-to-close sigma for the final close reaction.

## Price Sources

Use local `market_data.db` only when fresh for the relevant window. Otherwise verify price data from StockAnalysis, exchange data, company IR, broker market-data pages, or another reliable historical-price source. Record the source and timestamp in the output. Do not write precise price moves into vault notes from memory or secondary article commentary.

## Adjustment Model

Report four layers, in this order:

1. Raw move: company price change over the chosen event window.
2. Benchmark or sector-adjusted abnormal move: raw move minus expected move from broad market, sector ETF, and/or beta model.
3. Peer read-through: peer and competitor moves measured separately. Do not subtract peers by default when the event plausibly affects them indirectly; that peer move may be part of the event's market signal.
4. Peer-adjusted residual: diagnostic only when peer moves are judged unrelated background or when the question is narrow single-name idiosyncrasy.

Prefer a simple transparent model over a fragile overfit model. State the factor set used, such as `SPY + QQQ + SMH`, `sector ETF + market`, or `peer basket + market`.

## Sigma Stack

Use the model-adjusted abnormal move as the core event numerator. Show all three measurements:

| Metric | Numerator | Denominator | Meaning |
|---|---|---|---|
| Raw sigma | Raw move | Historical raw volatility | Holder impact: how unusual the experienced stock move was |
| Residual sigma | Model-adjusted abnormal move | Historical residual volatility from the same factor model | Event-specific surprise after discounting market, sector, and chosen factors |
| Abnormal/raw sigma | Model-adjusted abnormal move | Historical raw volatility | Event component compared with ordinary total stock volatility |

If using a peer-adjusted residual numerator, compare it with the historical residual volatility from that same peer model. Do not compare a peer-model residual against an unrelated residual denominator.

## Required Output

Include a table with these columns:

| Actor / ticker | Window | Raw move | Benchmark / sector move | Abnormal move | Raw sigma | Residual sigma | Abnormal/raw sigma | Peer read-through | Price source / timestamp | Status |
|---|---|---|---|---|---|---|---|---|---|---|

Then write one sentence answering: what did the tape believe?

Separate preliminary, stabilized, and final-close reactions. A morning measurement can be useful, but do not let it masquerade as the final close-to-close verdict.
