---
name: daily-scan
description: "Autonomous daily market scan: updates market data, screens vault actors for sigma movers (thresholds: docs/movers-screening.md), runs ticker-alias/price-freshness/IPO/private-capital audits, scans the analyst watchlist (docs/analyst-watchlist.md), checks the earnings calendar, and writes the briefing to the daily note and chat. Time-of-day agnostic. Use for /daily-scan, /morning-scan (legacy), daily sweep, what moved today, pre-market check, what's on the earnings calendar."
---

# Daily Scan

Autonomous market intelligence sweep. The daily heartbeat — produces a briefing that tells the user what happened, what moved, and what to watch. Runs at any time of day; the framing adapts to whether the user is checking pre-market, intraday, or after the close.

## Philosophy

Act like Eve at Epicenter Capital. Don't wait to be told what to look at. Scan everything, surface what matters, connect it to the vault. The briefing should be good enough that the user doesn't need to read any other source to know what's going on.

## Workflow

## Output contract

The daily note is the durable copy, but the chat is the user-facing output. Every `/daily-scan` run must end by showing the completed briefing in the conversation, not just a summary of files touched. If the scan was also written to `investing/Daily/YYYY-MM-DD.md`, say that briefly after the briefing; do not replace the briefing with a save confirmation.

### Phase 0: Data Update, Movers & Audits (local, fast)

Full screening logic and rationale: `docs/movers-screening.md`.

1. `python scripts/daily_scan.py --output /tmp/daily_scan.json` — updates market data universally (`update_market_data.py --lookback 5 --assets all`; FRED indicators apply a monthly-safe lookback floor), runs `quick_movers.py` with the three-trigger default (2.5σ / 2.0σ high-vol / 6% absolute), reports data freshness.

Run these four audit scripts in parallel with the sigma screen — they catch failure modes the sigma alone misses:

2. `python scripts/audit_vault_tickers.py --only-gaps` — actor notes with body-mentioned tickers missing from `aliases:` (Phase-0-invisible names).
3. `python scripts/ipo_debut_tracker.py --tickers <candidates> --scan-stale-private` — pass any IPO ticker candidates from overnight news + scan vault for `#private` notes whose body mentions a NYSE/NASDAQ ticker pattern (likely IPO'd, status stale).
4. `python scripts/ipo_debut_tracker.py --private-watch` — flags pre-IPO actors with funding rounds older than 120 days.
5. `python scripts/check_data_freshness.py` — per-ticker freshness: every vault-actor and cluster-config ticker whose last close lags the latest SPY session beyond allowance (3 US sessions / 6 foreign). The global SPY date can look fresh while individual series silently rot — `quick_movers` drops stale names instead of erroring, so a frozen series simply vanishes from screening (the Marsh McLennan legacy series sat three months stale undetected before this check existed, 2026-06). For stale names: `scripts/add_ticker.py TICKER` backfills and self-triages (delisted names report SKIPPED). Vault-actor and cluster-config tickers auto-refresh daily via dynamic groups in `download_all_assets.py`, so a persistent offender is a rename/delisting candidate: verify the corporate action, then add an `EXCLUDED_TICKERS` entry plus a vault "Former ticker" update.

6. `python scripts/check_split_discontinuities.py --verify-yf` — flags un-back-adjusted stock splits: a single-day price break at a clean split ratio (2:1, 10:1, ...) with a sustained level shift, in vault/cluster tickers. This is the failure `check_data_freshness` misses — a split-corrupted series is perfectly fresh but wrong, and it silently inverts cluster verdicts and `quick_movers` (the WFE quartet collapsed from intra 0.82 to 0.42 on an un-adjusted KLA 10:1 split, Jun 2026; `update_market_data.py --lookback N` structurally cannot back-adjust history for a split inside its window). `--verify-yf` cross-checks each flag against yfinance's recorded split history (targeted — only the flagged tickers — so it stays cheap) and SUPPRESSES any flag with no recorded split: a real −44% earnings crash (FISV, Oct 2025) or a 10x rally pattern-matches a split ratio but is not an un-back-adjusted split. It fails open (keeps the flag) on any yfinance error, so it never hides a real split. LIKELY-SPLIT rows that survive verification must be fixed before the series is trusted: `scripts/add_ticker.py TICKER` re-fetches the back-adjusted history (forward splits + most reverse splits), or a manual pre-break ×factor adjustment when the vendor hasn't recorded the split yet (common for fresh reverse splits). REVIEW rows are large clean-factor moves whose level shift isn't clearly sustained (possible split vs genuine crash / vol spike — eyeball); with `--verify-yf` they also include flags whose nearest recorded split is far from the flag date (a separate real move, split already adjusted). SUPPRESSED rows are the verified real moves. `--all` sweeps the whole DB, not just tracked tickers.

7. `python scripts/import_rp_holdings.py` — refresh the risk-parity composition tables (`rp_fund_metrics_long`, `rp_allocations_long`) from the Risk Parity vault's daily holdings-tracking notes. Idempotent (INSERT OR REPLACE) and independent of the audits, so it runs in parallel; keeps the `Risk Parity` concept note's leverage/allocation history current as the tracker writes new snapshots. No-op if the RP vault isn't present locally.

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

Scan the tracked analysts in `docs/analyst-watchlist.md` (that file is the list of record). For each:
1. One WebSearch with the watchlist's search pattern, scoped to the last 48 hours.
2. Only flag if they published something new.
3. Check against the analyst's `Analysts/` note to see if commentary is already captured.
4. Surface new material in the briefing's "Analyst signals" section.

Deep ingestion (quotes and data points into both the analyst note and the relevant concept/event notes) happens via `/ingest URL` — this phase only surfaces what's new.

### Phase 4: Generate Briefing

Draft the briefing in the exact form that will be both appended to the daily note and shown in chat. Format:

```
# Daily Scan — [Date]

## Market snapshot
[Futures, key levels, overnight moves. 3-5 lines max.]

## Sigma movers ([count])
[Table: ticker, move, sigma, trigger, catalyst (if found)]

## Audit findings
[Anything from audit_vault_tickers / ipo_debut_tracker / private-watch / check_data_freshness / check_split_discontinuities worth surfacing. Stale tickers get the count + worst offenders + the fix command; LIKELY-SPLIT discontinuities get the ticker + ratio + fix command.]

## Overnight developments
[2-4 paragraphs on the most important stories. Lead with vault-thesis-relevant. Exact figures, named sources.]

## Earnings watch
[This week's vault-relevant earnings. Dates, consensus.]

## Analyst signals
[Only if any tracked analyst published overnight. Otherwise skip.]

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
4. Final response: paste the complete briefing in chat, followed by a one-line durability note with the daily-note path and structured-output path when available.

## Voice

Same as `/newsletter`: analytical, structural, tensions not market reads, exact figures. Shorter — target 300-500 words for the briefing body.

## Scheduling

Two ways to run on a schedule; pick by whether it must fire while Claude is closed. Full reference: `docs/headless-scheduling.md`.

Unattended (recommended) — an OS scheduler launches its own headless Claude, so it does not depend on a REPL being open:
- Invocation: `claude -p "/daily-scan …" --permission-mode bypassPermissions --disallowedTools "Bash(git commit:*)" "Bash(git push:*)"`, run from the repo root with stdin redirected from null. `bypassPermissions` is mandatory (`-p` has no TTY to answer a permission prompt, so an unauthorized tool call dead-ends the run) but it also green-lights `git push`; the `--disallowedTools` deny-list stops the agent from committing or pushing the working tree on its own (deny overrides bypass).
- Two-stage wrapper (critical): the slow market-data update must not be the agent's job. Run `daily_scan.py` synchronously in the wrapper first, then invoke the agent with `--skip-update`. Forbidding `run_in_background` alone is not enough — denied the harness's background mechanism, the agent hand-rolls its own (detaches `update_market_data.py`, then polls a temp file in a shell loop) and hangs forever, because a `-p` session is never re-woken to observe the result. Pre-warming deletes the step the agent would otherwise background; the prompt still forbids `run_in_background` and requires the briefing be written before exit.
- This repo's installed instance: a Windows Task Scheduler job (`FinancialCharts-Daily-Scan`) runs `scripts/daily_scan_task.bat` on weekdays at 7:15 AM ET — after RP Holdings Import (7:05) so Phase 0's `import_rp_holdings.py` ingests same-day holdings.
- Runs only where Claude's auth and the `python` toolchain resolve. On Windows that is an interactive logon session (same constraint as the RP Holdings tasks): no run on a locked, logged-off, or sleeping machine.

In-session (lighter, fragile) — schedule with `CronCreate` and `durable: true`. It fires only while the Claude Code REPL is open and idle; if Claude is not running when the cron fires, that interval is skipped. Use only if you keep Claude open at the scheduled time.

Manual — run `/daily-scan` any time; the framing adapts to pre-market, intraday, or after the close.

## Failure modes

- Market data update fails → continue with stale data, note staleness in briefing
- WebSearch fails → note which searches failed, suggest Chrome MCP follow-up
- No movers → still run news sweep and earnings calendar check
- Weekend/holiday → skip market data update, still scan for news
