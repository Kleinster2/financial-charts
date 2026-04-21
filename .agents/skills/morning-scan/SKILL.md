---
name: morning-scan
description: "Autonomous morning market scan — Eve-style. Updates market data, identifies sigma movers, scans news, checks earnings, and generates a pre-market briefing. Runs automatically via scheduled cron or manually via /morning-scan. The goal: consume 10x more information in 10x less time, surface what matters before the user reads anything."
---

# Morning Scan

Autonomous pre-market intelligence sweep. This is the daily heartbeat — it runs every morning and produces a briefing that tells the user what happened, what moved, and what to watch.

## Philosophy

Act like Eve at Epicenter Capital. Don't wait to be told what to look at. Scan everything, surface what matters, connect it to the vault. The briefing should be good enough that the user doesn't need to read any other source to know what's going on.

## Workflow

### Phase 0: Data Update & Movers (local, fast)

1. Run `python scripts/morning_scan.py --output /tmp/morning_scan.json`
   - This updates market data (5-day lookback: stocks, ETFs, ADRs, FX, futures)
   - Runs `quick_movers.py` (2.5σ, 60-day rolling) against vault actors
   - Checks earnings calendar
   - Reports data freshness
2. Read the output JSON
3. If market data update failed, note it but continue — stale data is better than no scan

### Phase 1: News Sweep (AI-powered)

For each sigma mover from Phase 0:
1. WebSearch for the catalyst (company name + "stock" + date range)
2. If catalyst found, note it for the briefing
3. If the vault actor note is missing the catalyst, flag for update

Then do a broad sweep — search for overnight developments in:
- US markets (S&P 500 futures, major macro)
- AI/semiconductors (vault's core theme)
- Energy/oil (geopolitical sensitivity)
- China/trade (tariff developments)
- Any vault thesis that has active catalysts

Use WebSearch, not Chrome — speed over depth at this phase. Chrome MCP only if WebSearch returns 403.

### Phase 2: Earnings Check

1. Check if any vault actors report earnings today or this week
2. WebSearch for "earnings calendar this week" to cross-reference
3. For upcoming reports, note consensus estimates if available

### Phase 3: Analyst Scan (abbreviated)

Quick check on the 8 tracked analysts (from /news skill):
- Helima Croft, Jeff Currie, Natasha Kaneva, Francisco Blanch
- Lyn Alden, Zoltan Pozsar, Ed Yardeni, Mike Wilson

One WebSearch per analyst: `"[name]" [today's date or yesterday]`
Only flag if they published something new. Don't deep-dive — that's for /news.

### Phase 4: Generate Briefing

Write the morning briefing directly in chat. Format:

```
# Morning Scan — [Date]

## Market snapshot
[Futures, key levels, overnight moves. 3-5 lines max.]

## Sigma movers ([count])
[Table: ticker, move, sigma, catalyst (if found)]

## Overnight developments
[2-4 paragraphs on the most important stories. Lead with what matters for vault theses. Exact figures, named sources.]

## Earnings watch
[This week's vault-relevant earnings. Dates, consensus if available.]

## Analyst signals
[Only if any of the 8 tracked analysts published overnight. Otherwise skip.]

## Vault actions needed
[Checklist of notes that need updating based on today's scan:]
- [ ] Update [[Actor]] — catalyst from sigma move
- [ ] Check [[Concept]] — new development
- [ ] Create stub for [[New Entity]] — mentioned in overnight news
```

### Phase 5: Daily Note Setup

1. If today's daily note doesn't exist, create it with standard frontmatter
2. Add a `## Morning scan` section at the top (before Notes created/expanded) with a summary of the scan results
3. The vault actions checklist becomes the day's work queue

## Voice

Same as /newsletter: analytical, structural, tensions not market reads, exact figures. But shorter — this is a scan, not a deep brief. Target 300-500 words for the briefing body.

## Scheduling

This skill is designed to run on a cron schedule via `CronCreate`:
- Weekdays at ~6:45 AM ET (before US pre-market)
- Uses `durable: true` so it survives session restarts
- Fires when Claude Code REPL is idle

If Claude Code isn't running when the cron fires, the scan simply doesn't happen that day. The user can always run `/morning-scan` manually.

## Failure modes

- Market data update fails → continue with stale data, note staleness in briefing
- WebSearch fails → note which searches failed, suggest Chrome MCP follow-up
- No movers → still run news sweep and earnings check
- Weekend/holiday → skip market data update, still scan for news
