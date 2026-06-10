---
name: news
description: "Ingest news articles from a specified source (Bloomberg, Reuters, FT, WSJ, or user-named) into the vault. Searches the source for vault-relevant articles, applies a 48-hour date gate, presents candidates, and ingests each selected article via /ingest. Closes with a downstream-impact check on any event/crisis notes updated. Use for /news SOURCE, ingest from Bloomberg, check FT for AI articles. NOT for daily movers (use /daily-scan) or newsletter sweep (use /substacks)."
---

# News Article Ingestion

Ingest news articles from a named source into the Obsidian vault. The skill orchestrates source discovery → article selection → ingestion → downstream impact. Per-article ingestion is delegated to `/ingest`.

**Before any vault edit**: read `CLAUDE.md` in the vault root.

**Boundary**:
- Daily movers, ticker audits, analyst commentary, earnings calendar → `/daily-scan`
- Curated newsletter/Substack archive sweep → `/substacks`
- This skill is for **named-source article ingestion** (Bloomberg, Reuters, FT, WSJ, or whatever the user specifies)

## Phase 1: Source Discovery

1. Search the specified source for recent articles, focused on vault areas: AI, semiconductors, energy, China, robotics, macro, SaaS, markets, cybersecurity/data breaches at AI companies, AI infrastructure or supply-chain security.
2. **Date gate**: check the publication date of every candidate. Only include articles from the last 48 hours. If an older article appears in a sidebar or recommendation module, skip it unless the user specifically requests historical ingestion.
3. Cross-reference each candidate against the vault — search daily notes and actor notes for existing coverage.
4. Present the candidate list as a numbered table:

| # | Article | Date | Status |
|---|---|---|---|
| 1 | Title | May 12 | New |
| 2 | Title | May 11 | Already in 2026-05-11.md |

**Always include publication dates so the user can spot strays.**

Wait for the user to select which articles to ingest.

## Phase 2: Article Ingestion (delegated)

For each selected article: run `/ingest URL`.

`/ingest` handles source acquisition, full entity enumeration, classification gates (verification, concept-vs-actor, vault-of-record, cold research), vault writes with compliance, and daily-note logging. Those rules live in the `/ingest` skill and `docs/research-workflow.md` — don't re-state them here.

## Phase 3: Downstream Impact Check

After all articles in the batch are ingested, scan the notes that got updated for second-order effects.

1. For each event/crisis note touched, look for a `## Watch for` section.
2. If one exists, scan each untracked item against the articles just ingested + run a quick web search for the top 2-3 most likely items.
3. If new coverage is found, ingest it (loop back to Phase 2) and update the watch-list status.
4. If no watch list exists but the note covers an ongoing crisis, war, supply shock, or policy shift, ask: *What downstream effects of this story haven't we tracked yet?* Then propose a watch list.

Batch the downstream-impact check at the **end** of all ingestions, not per-article — that lets the check see the full picture of what was just updated.

## Phase 4: Daily Note Synthesis

Before reporting completion, reopen `investing/Daily/YYYY-MM-DD.md` and make sure the batch has a non-empty `## Synthesis` section. This section is mandatory for `/news` batches.

Write the explanation that would otherwise live only in chat:

- the through-line tying the selected stories together, or a clear statement that they are unrelated;
- what changed versus what was already true;
- the causal mechanism and market/geopolitical/technology read-through;
- why selected items were ingested and lower-priority candidates were skipped;
- which vault got each part of the story and why.

The daily note should let future readers recover the "why this mattered" frame without scrolling the Telegram thread.

## Rules

Most ingestion rules are global and live in `CLAUDE.md` or `docs/`. Below are the rules specific to multi-article batched runs:

- **Batch downstream-impact check at end** — see Phase 3.
- **Cross-article corroboration** — when the same fact appears in multiple articles in the batch, cite the earliest reporting and link the corroborating sources rather than duplicating the claim across notes.
- **Daily synthesis is required** — the batch is incomplete until the explanation is in `## Synthesis`, not only in the final chat message.
