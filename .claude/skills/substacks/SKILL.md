---
name: substacks
description: "Sweep ~82 tracked newsletter/Substack sources (Chartbook, ChinaTalk, Robin Brooks, Vizier Report, Chips and Wafers, etc. — full list in docs/newsletter-sources.md) for new posts in a configurable window (default 48 hours). Cross-references vault coverage, presents a candidate table, and delegates ingestion to /ingest URL for each selected post. Use for /substacks, newsletter sweep, what did the substacks publish, weekend reading."
---

# Substack Sweep

Scan tracked newsletters and Substacks for new posts and ingest the vault-relevant ones.

**Before any vault edit**: read `CLAUDE.md` in the vault root.

**Boundary**:
- Daily movers, ticker audits, analyst commentary, earnings → `/morning-scan`
- Named-source article ingestion (Bloomberg, Reuters, FT, WSJ) → `/news <source>`
- This skill is for the curated newsletter/Substack archive list

## Phase 1: Source Scan

1. Read `docs/newsletter-sources.md` for the full source list (~82 publications).
2. Default window: posts in the last 48 hours. User can override (`/substacks 7d` for a week, `/substacks 14d` for two).
3. For each source: navigate to the archive/homepage. WebFetch first; fall back to Chrome MCP on 403 (per `[[feedback_chrome_on_403]]`).
4. Capture title, date, and a one-line summary for each post in the window.

## Phase 1.5: Auto-expand tracked list

If the scan surfaces posts from publications **not yet in `docs/newsletter-sources.md`**, add them to the tracked list before Phase 2. Any publication appearing in Gil's Substack inbox has already passed his curation — the curated list should auto-expand to match.

For each new pub:
1. Add a row to `docs/newsletter-sources.md` (URL + vault tag inferred from focus area)
2. Mirror the row to `~/clawd/TOOLS.md`
3. Subscribe via `POST {pub}/api/v1/free` (idempotent — no-op if already subscribed; use the Chrome-MCP same-origin navigate-then-fetch pattern from `investing/Daily/2026-05-16.md` Round 3)

At end of run, bump count references in `CLAUDE.md` + SKILL.md descriptions (one update covers all increments). Promote SKILL.md to Codex + OpenClaw mirrors via `python scripts/promote_shared_skill.py substacks --from claude` and verify parity.

## Phase 2: Candidate Table

Present candidates as a numbered table with vault cross-reference:

| # | Publication | Title | Date | Status |
|---|---|---|---|---|
| 1 | Chartbook | "Title" | May 12 | New |
| 2 | ChinaTalk | "Title" | May 11 | Already in 2026-05-11.md |
| 3 | Vizier Report | "Title" | May 10 | New |

**Always include publication dates** — strays from older archive pages happen.

Wait for the user to select. They may pick by number (`1,3,5`), by source (`all from Chartbook`), or `all new`.

## Phase 3: Ingestion (delegated)

For each selected post: run `/ingest URL`.

`/ingest` handles source acquisition, full entity enumeration, classification gates (verification, concept-vs-actor, vault-of-record, cold research), vault writes with compliance, and daily-note logging. Don't duplicate those rules here.

## Phase 4: Daily Note Wrap

After all ingestions complete, append a `## Substack sweep` section to today's daily note listing the ingested posts with their URLs and one-line takeaways.

## Cadence

No fixed cadence. `/morning-scan`'s "Suggested follow-ups" surfaces "5+ days since last substack sweep" as a soft trigger. Weekend reading and quiet-news afternoons are natural moments.

## Failure modes

- Source homepage 403 → Chrome MCP fallback
- Substack archive paginated → check page 1 only by default; dig deeper only if the user asks
- Source temporarily down → note in candidate table, continue with others
- Dead link in `docs/newsletter-sources.md` → flag to user, don't silently skip
