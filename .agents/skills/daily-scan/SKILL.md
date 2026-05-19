---
name: daily-scan
description: "Autonomous daily market scan. Updates market data, screens vault actors for sigma movers (2.5σ standard / 2.0σ high-vol / 6% absolute — see docs/movers-screening.md), audits ticker aliases for Phase-0-invisible names, tracks IPO debuts and stale pre-IPO rounds, scans 8 tracked analysts (docs/analyst-watchlist.md) for new commentary, checks today's earnings calendar, and writes a briefing to the daily note. Time-of-day agnostic — pre-market, intraday, post-close all work. Use for /daily-scan, /morning-scan (legacy), daily sweep, what moved today, pre-market check, what's on the earnings calendar."
---

# Daily Scan

Autonomous market intelligence sweep. The daily heartbeat — produces a briefing that tells the user what happened, what moved, and what to watch. Runs at any time of day; the framing adapts to whether the user is checking pre-market, intraday, or after the close.

## Philosophy

Act like Eve at Epicenter Capital. Don't wait to be told what to look at. Scan everything, surface what matters, connect it to the vault. The briefing should be good enough that the user doesn't need to read any other source to know what's going on.

## Workflow

### Phase 0: Data Update, Movers & Audits (local, fast)

Full screening logic and rationale: `docs/movers-screening.md`.

1. `python scripts/daily_scan.py --output /tmp/daily_scan.json` — updates market data (5-day lookback: stocks, ETFs, ADRs, FX, futures), runs `quick_movers.py` with the three-trigger default (2.5σ / 2.0σ high-vol / 6% absolute), reports data freshness.

Run these three audit scripts in parallel with the sigma screen — they catch failure modes the sigma alone misses:

2. `python scripts/audit_vault_tickers.py --only-gaps` — actor notes with body-mentioned tickers missing from `aliases:` (Phase-0-invisible names).
3. `python scripts/ipo_debut_tracker.py --tickers <candidates> --scan-stale-private` — pass any IPO ticker candidates from overnight news + scan vault for `#private` notes whose body mentions a NYSE/NASDAQ ticker pattern (likely IPO'd, status stale).
4. `python scripts/ipo_debut_tracker.py --private-watch` — flags pre-IPO actors with funding rounds older than 120 days.

Read the JSON output. If any step failed, note it but continue — stale data is better than no scan.

### Phase 1: News Sweep (AI-powered)

For each sigma mover from Phase 0:
1. WebSearch for the catalyst (company name + "stock" + date range).
2. If catalyst found, note it for the briefing.
3. If the vault actor note is missing the catalyst, flag for update.

Then a broad sweep — overnight developments in:
- US markets (S&P 500 futures, major macro)
- AI/semiconductors (vault's core theme)
- Energy/oil (geopolitical sensitivity)
- China/trade (tariff developments)
- Any vault thesis with active catalysts

Use WebSearch, not Chrome — speed over depth at this phase. Chrome MCP only if WebSearch returns 403.

### Phase 2: Earnings Calendar

1. Check whether any vault actors report earnings today or this week.
2. WebSearch `"earnings calendar this week"` to cross-reference.
3. For upcoming reports, note consensus estimates if available.

Don't fold the calendar into the vault as a standalone note — earnings calendar items are data points, not durable entities (Hard Gate #10 in CLAUDE.md). Full earnings ingestion when a report drops uses `/earnings TICKER`.

### Phase 3: Analyst Scan

Scan the 8 tracked analysts in `docs/analyst-watchlist.md`. For each:
1. One WebSearch with the watchlist's search pattern, scoped to the last 48 hours.
2. Only flag if they published something new.
3. Check against the analyst's actor note to see if commentary is already captured.
4. Surface new material in the briefing's "Analyst signals" section.

Deep ingestion (quotes and data points into both the analyst note and the relevant concept/event notes) happens via `/ingest URL` — this phase only surfaces what's new.

### Phase 4: Generate Briefing

Write the morning briefing directly in chat. Format:

```
# Daily Scan — [Date]

## Market snapshot
[Futures, key levels, overnight moves. 3-5 lines max.]

## Sigma movers ([count])
[Table: ticker, move, sigma, trigger, catalyst (if found)]

## Audit findings
[Anything from audit_vault_tickers / ipo_debut_tracker / private-watch worth surfacing]

## Overnight developments
[2-4 paragraphs on the most important stories. Lead with vault-thesis-relevant. Exact figures, named sources.]

## Earnings watch
[This week's vault-relevant earnings. Dates, consensus.]

## Analyst signals
[Only if any of the 8 published overnight. Otherwise skip.]

## Vault actions needed
- [ ] Update [[Actor]] — catalyst from sigma move
- [ ] Check [[Concept]] — new development
- [ ] Create stub for [[New Entity]] — mentioned in overnight news

## Suggested follow-ups
- [ ] Run `/substacks` if >5 days since the last sweep
- [ ] Run `/news <source>` for any movers still lacking a vault catalyst after Phase 1
- [ ] Run `/earnings TICKER` for any vault actor that reported overnight
```

### Phase 5: Daily Note Setup

1. If today's daily note doesn't exist, create it with standard frontmatter.
2. Add a `## Daily scan` section at the top (before Notes created/expanded) with the briefing. If the day already has a scan section, append a new subsection with the timestamp rather than overwriting — multiple runs per day are fine.
3. The vault-actions checklist becomes the day's work queue.

## Voice

Same as `/newsletter`: analytical, structural, tensions not market reads, exact figures. Shorter — target 300-500 words for the briefing body.

## Scheduling

Designed to run on a cron schedule via `CronCreate`:
- Typical default: weekdays at ~6:45 AM ET (before US pre-market) — but any cadence works
- Uses `durable: true` so it survives session restarts
- Fires when Claude Code REPL is idle

If Claude Code isn't running when the cron fires, the scan doesn't happen that interval. The user can always run `/daily-scan` manually at any time.

## Failure modes

- Market data update fails → continue with stale data, note staleness in briefing
- WebSearch fails → note which searches failed, suggest Chrome MCP follow-up
- No movers → still run news sweep and earnings calendar check
- Weekend/holiday → skip market data update, still scan for news
