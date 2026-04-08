---
name: ingest
description: "Single-source ingestion pipeline: process one source (interview transcript, podcast, article, video, filing, screenshot set) that mentions many entities and data points into the vault. Handles source acquisition (YouTube transcription, article fetch, screenshot reading), full entity/data point enumeration, vault survey, image routing by concept, note creation/expansion, and daily note logging. Use whenever the user provides a URL, transcript, set of screenshots, or other single source for vault processing. Triggers on /ingest, or when the user pastes a YouTube URL, article link, or says 'ingest this', 'process this interview', 'add this to the vault'."
---

# Single-Source Ingestion

Process one source into the vault. Usage: `/ingest URL` or `/ingest` (then provide source in chat).

CLAUDE.md defines note structure, formatting, and hard gates. `docs/research-workflow.md` defines source separation and two-track verification. `docs/vault-note-guide.md` defines note voice and update discipline. This skill sequences the ingestion workflow and codifies rules that only emerge during single-source processing.

## Phase 0: Source Acquisition

Detect source type and acquire content:

| Source type | Acquisition |
|---|---|
| YouTube URL | `python scripts/transcribe_youtube.py URL --save /tmp/transcript.txt` (`--language pt` for Portuguese) |
| Screenshots/images | Read all images via Read tool |
| Article URL | WebFetch; if 403 → Chrome MCP (`get_page_text`); if interactive → visual scrolling |
| SEC filing | `python scripts/parse_sec_filing.py TICKER` (never WebFetch on sec.gov) |
| User-pasted text | Use directly |

**Present before analyzing.** The user may not have read the source. Before any vault work, present:
- Source metadata (title, speaker(s), date, duration/length)
- Key points summary (5-10 bullets with exact figures)
- Themes identified

Wait for user to confirm direction before proceeding. The summary is their only preview.

## Phase 1: Full Enumeration

Process the entire source. Every paragraph, every aside, every throwaway detail.

Enumerate three lists:

**Entities** — every actor, concept, product, event, country, person, firm mentioned. Include secondary mentions ("they're competing with X" counts). Absence of evidence is not evidence of absence.

**Data points** — every price, AUM figure, percentile, growth rate, date, deal term, production volume, headcount. Exact figures with attribution.

**Images/charts** — for each screenshot or chart provided, identify which CONCEPT it depicts, not which source it came from. A yield percentile chart is a "CLO yield data" chart, not a "Rieder interview chart."

Present enumeration to user as a table before vault work begins.

## Phase 1.5: Verification

Classify every data point from Phase 1 before writing anything into the vault:

**Verifiable facts** — numbers, dates, policy decisions, market data that can be independently checked:
- Central bank rates → check each CB's actual latest decision
- AUM/fund flow figures → check ICI, fund filings, or provider data
- GDP/economic data → check BEA, FRED, or official releases
- Earnings revisions → check FactSet, Bloomberg, or S&P data
- Prices, yields, spreads → check against DB or market data sources

For each verifiable fact: research it. If confirmed, write with attribution to both the source speaker and the confirming data. If contradicted, flag the discrepancy in the note — "Rieder cited X; [source] shows Y." If unverifiable (no accessible source), write as a claim attributed to the speaker, not as established fact.

**Sourced opinions** — views, predictions, frameworks, interpretive claims:
- Market positioning rationale ("credit markets amazingly resilient")
- Policy predictions ("employment is the bigger structural problem")
- Strategic preferences ("tech investing better in equities")
- Macro interpretations ("very far from crisis")

For each opinion: attribute to the speaker. Note whether it aligns with or contradicts existing vault views (check the relevant concept note for other voices). If contrarian, say so. If consensus, say so. Don't present one person's view as established truth.

**The gate:** Do not write unverified factual claims as facts. The vault's value depends on accuracy — a wrong number written confidently is worse than a gap.

## Phase 2: Vault Survey

For each enumerated entity:

1. Check vault: `python scripts/check_before_create.py "Name"` for new entities
2. If exists → read the note, assess what's already covered vs. what's new
3. If missing → flag for creation

Report a survey table:

| Entity | Status | What's new from this source |
|---|---|---|
| [[Entity A]] | Full note | New AUM figure, quote |
| [[Entity B]] | Stub | Full expansion warranted |
| [[Entity C]] | Missing | Create — mentioned 3x with hard data |

Every row gets processed. No silent skips.

## Phase 3: Image Routing

**Charts follow concepts, not sources.** For each image:

1. Ask: "What concept does this depict?" — the answer determines the destination note
2. Save to `investing/attachments/` with a descriptive name tied to the concept (e.g., `clo-yield-percentile-mar2026.png`), not the source
3. Embed in the concept note with italic caption and source attribution, even if that note is not otherwise on the update list — the image creates the reason to touch the note
4. If the image also contextualizes the source actor (e.g., a fund's own allocation), embed in BOTH the concept note and the actor note

**New tickers:**
1. `python scripts/add_ticker.py TICKER`
2. Generate price chart: `/api/chart/lw?tickers=TICKER&start=...&primary=TICKER`
3. Verify: `wc -c` — under 1KB = error JSON, not PNG
4. Embed in note with data table

## Phase 4: Note Updates

Process the full survey table:

**Existing notes — expand:**
- Add new data inline where it belongs thematically (no dated appendix blocks — see `docs/vault-note-guide.md`)
- Separate facts from framing per `docs/research-workflow.md`
- Wikilink every entity mentioned
- No bold in note bodies

**New notes — create:**
- Hard gate: `python scripts/check_before_create.py "Name"`
- Follow CLAUDE.md folder rules and note structure for the entity type
- Products require a parent Actor note
- Run `python scripts/check_note_compliance.py <file>` on actor notes

**Stubs for dead links:** frontmatter + one-liner + Quick stats + Related

**3+ actors touched by one event** → create Event note in `Events/`. Actor notes carry short summary + wikilink.

## Phase 5: Daily Note

Update `investing/Daily/YYYY-MM-DD.md`. Run `date` to confirm current date.

**Placement rule:** Entries go in the `## Notes created/expanded` section — BEFORE any `## News ingestion`, `## Edit log`, or other `## ` headers. The section boundary is the next `## ` header (two hashes + space), not `---` horizontal rules.

Format:

```markdown
### [Source title] ([source type], [date])

- **[[Entity A]]** — one-line summary of what was added/changed
- **[[Entity B]]** — one-line summary
```

Every entity touched must appear here — the daily note hook validates this.

**Cross-vault gate:** After completing updates, check sibling vaults per `docs/cross-vault-rules.md`. Flag to user.

## Rules

These rules are specific to single-source ingestion. General vault rules live in CLAUDE.md and docs/.

- **Present before analyzing** — summary first, vault work after user confirms
- **Charts follow concepts, not sources** — route images to concept notes, not actor/source notes
- **Images create the reason to touch a note** — even if that note wasn't otherwise on the update list
- **Full entity sweep** — every name, every number, every aside gets processed
- **Every chart needs a data table** — reader sees numbers alongside visualization
- **Daily note placement** — `## Notes created/expanded` section, before `## News ingestion` or `## Edit log`
- **Copyright** — max 15-word quotes from articles; short quotes only
