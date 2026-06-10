---
name: substacks
description: "Sweep the tracked newsletter/Substack sources (Chartbook, ChinaTalk, Robin Brooks, Vizier Report, etc. — list of record: docs/newsletter-sources.md) for new posts in a configurable window (default 48 hours). Cross-references vault coverage, presents a candidate table, clusters posts into themes when useful, and delegates ingestion to /ingest URL for each selected post. Use for /substacks, newsletter sweep, themed Substack ingestion, what did the substacks publish, weekend reading."
---

# Substack Sweep

Scan tracked newsletters and Substacks for new posts and ingest the vault-relevant ones.

**Before any vault edit**: read `CLAUDE.md` in the vault root.

**Boundary**:
- Daily movers, ticker audits, analyst commentary, earnings → `/daily-scan`
- Named-source article ingestion (Bloomberg, Reuters, FT, WSJ) → `/news <source>`
- This skill is for the curated newsletter/Substack archive list

## Phase 1: Source Scan

1. Read `docs/newsletter-sources.md` for the full source list — that file is the count of record; prose never embeds the source count.
2. Default window: posts in the last 48 hours. User can override (`/substacks 7d` for a week, `/substacks 14d` for two).
3. For each source: navigate to the archive/homepage. WebFetch first; fall back to Chrome MCP on 403 (per `[[feedback_chrome_on_403]]`).
4. Capture title, date, and a one-line summary for each post in the window.

## Phase 1.5: Auto-expand tracked list

If the scan surfaces posts from publications **not yet in `docs/newsletter-sources.md`**, add them to the tracked list before Phase 2. Any publication appearing in Gil's Substack inbox has already passed his curation — the curated list should auto-expand to match.

For each new pub:
1. Add a row to `docs/newsletter-sources.md` (URL + vault tag inferred from focus area)
2. Mirror the row to `~/clawd/TOOLS.md`
3. Subscribe via `POST {pub}/api/v1/free` (idempotent — no-op if already subscribed; use the Chrome-MCP same-origin navigate-then-fetch pattern from `investing/Daily/2026-05-16.md` Round 3)

No count bumping: source counts live only in `docs/newsletter-sources.md`, never in skill descriptions or CLAUDE.md prose. Adding rows there (plus the `~/clawd/TOOLS.md` mirror) is the whole update.

## Phase 2: Candidate Table

Present candidates as a numbered table with vault cross-reference:

| # | Publication | Title | Date | Status |
|---|---|---|---|---|
| 1 | Chartbook | "Title" | May 12 | New |
| 2 | ChinaTalk | "Title" | May 11 | Already in 2026-05-11.md |
| 3 | Vizier Report | "Title" | May 10 | New |

**Always include publication dates** — strays from older archive pages happen.

Wait for the user to select. They may pick by number (`1,3,5`), by source (`all from Chartbook`), or `all new`.

## Phase 2.5: Theme Clustering

When the candidate set has multiple related posts, add a thematic view after the numbered table. This is for choosing an ingestion path, not for replacing source-level attribution.

For each theme, include:

| Theme | Label | Posts | Target vaults | Core question |
|-------|-------|-------|---------------|---------------|
| 1 | AI ROI, control, and verification | 8, 27, 37 | Investing, Technologies | Is agentic AI becoming an economic system or a control problem? |

Guidelines:
- Keep themes structural: mechanisms, bottlenecks, policy regimes, market transmission channels, technology stacks.
- Do not create a theme just because two posts share a named actor. A theme needs a common causal question.
- Flag posts that are better ingested individually because they are discrete events, narrow earnings/ticker items, or paid teasers with too little public body.
- Accept user selections like `theme 1`, `do theme 2`, `AI ROI theme`, or `your priorities`.
- Before writing a theme, state the proposed split up front: sources in scope, target vaults, likely durable notes, paid-content caveats, and any deep-dive gates that may activate.

## Phase 3: Ingestion (delegated)

For each selected post: run `/ingest URL`.

`/ingest` handles source acquisition, full entity enumeration, classification gates (verification, concept-vs-actor, vault-of-record, cold research), vault writes with compliance, and daily-note logging. Don't duplicate those rules here.

For a selected theme:
1. Run `/ingest URL` for each in-scope post, preserving source-by-source attribution and paid-content boundaries.
2. After the individual ingestions, run a synthesis pass across the touched notes: connect repeated mechanisms, reconcile conflicting claims, and move the durable interpretation into concept/actor notes rather than leaving it only in the daily note.
3. Avoid ephemeral theme notes unless the theme itself is durable and likely to recur. Prefer expanding existing concept, sector, event, and actor notes.

## Phase 3.5: Gated Deep-Dive Layer

Themed ingestion should include deep dives selectively. This is a second layer that complements source ingestion; it is not a default full research project for every article.

Activate the deep-dive layer when at least one gate is true:
- **Durable mechanism**: the theme points to a recurring concept, not just a one-day news item.
- **Conflicting claims**: sources disagree or imply different causal mechanisms.
- **High impact**: the gap affects market interpretation, policy/geopolitics, security architecture, or a major actor cluster.
- **Gated or shallow source**: a paid teaser/public excerpt raises a material question that cannot be responsibly written without external triangulation.
- **New actor/product cluster**: the theme introduces entities that need enumeration before they can be linked safely.
- **Technical/regulatory mechanism**: the causal mechanism depends on law, accounting, engineering, security architecture, energy/power constraints, or domain-specific terms.

When a gate activates:
1. Do the minimum contextual research needed to keep the vault update accurate and non-shallow. Prefer primary sources, filings, papers, standards, official docs, and high-quality reporting.
2. Add a `Deep-dive queue` to the wrap-up with 1-3 entries. Each entry should include:
   - research question
   - why it matters
   - target vaults/notes
   - best starting sources
   - recommendation: `run now`, `defer`, or `watch`
3. Run a full `/deepdive ENTITY/CONCEPT` only when the user explicitly selects it, or when the theme ingestion would otherwise create a misleading or structurally incomplete note.

## Phase 4: Daily Note Wrap

After all ingestions complete, append a `## Substack sweep` section to today's daily note listing the ingested posts with their URLs and one-line takeaways.

For themed ingestion, also log:
- theme label and source list
- target vaults touched
- durable notes created/expanded
- paid-source limits
- deep-dive gates activated
- deep-dive queue decisions (`run now`, `defer`, `watch`)

## Cadence

No fixed cadence. `/daily-scan`'s "Suggested follow-ups" surfaces "5+ days since last substack sweep" as a soft trigger. Weekend reading and quiet-news afternoons are natural moments.

## Failure modes

- Source homepage 403 → Chrome MCP fallback
- Substack archive paginated → check page 1 only by default; dig deeper only if the user asks
- Source temporarily down → note in candidate table, continue with others
- Dead link in `docs/newsletter-sources.md` → flag to user, don't silently skip
- Theme too broad → split it before ingesting; broad themes produce shallow notes
- Deep-dive sprawl → cap the queue at 1-3 items and tie each item to a concrete vault gap
