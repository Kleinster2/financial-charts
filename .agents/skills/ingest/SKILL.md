---
name: ingest
description: "Single-source ingestion pipeline: process one source (interview transcript, podcast, article, video, filing, screenshot set) that mentions many entities and data points into the vault. Handles source acquisition (YouTube transcription, article fetch, screenshot reading), full entity/data point enumeration, vault survey, image routing by concept, note creation/expansion, and daily note logging. Use whenever the user provides a URL, transcript, set of screenshots, or other single source for vault processing. Triggers on /ingest, or when the user pastes a YouTube URL, article link, or says 'ingest this', 'process this interview', 'add this to the vault'."
---

# Single-Source Ingestion

Process one source into the vault. Usage: `/ingest URL` or `/ingest` (then provide source in chat).

This skill is a sequencing harness for ingestion. The substantive rules live in docs and are pointed to from each phase:

- `docs/research-workflow.md` — verification, two-track sources, cold research pass
- `docs/vault-note-guide.md` — concept-vs-actor classification, note voice, structure
- `docs/cross-vault-rules.md` — vault-of-record lens test, sibling-vault gates
- `.agents/skills/event-tape/SKILL.md` — adjusted market-reaction windows, peer read-through, and sigma stack
- `CLAUDE.md` — folder rules, hard gates, formatting

The skill enforces the *order* — verify → classify (filing) → classify (vault) → research → survey → write — that's specific to single-source processing.

## Phase 0: Source Acquisition

Detect source type and acquire content:

| Source type | Acquisition |
|---|---|
| YouTube URL | `python scripts/transcribe_youtube.py URL --save /tmp/transcript.txt` (`--language pt` for Portuguese) |
| Screenshots/images | Read all images via Read tool; treat chart screenshots as first-class source material |
| Article URL | WebFetch; if 403 → Chrome MCP (`get_page_text`); if interactive → visual scrolling |
| SEC filing | `python scripts/parse_sec_filing.py TICKER` (never WebFetch on sec.gov) |
| User-pasted text | Use directly |

**Entity sweep at triage.** Before deciding whether content is worth ingesting, check ALL named entities — headline actors, secondary firms, origin firms, counterparties — for vault presence. Report which have notes and which don't. A story may not deserve ingestion, but a missing vault note for a mentioned entity is a gap worth surfacing regardless.

**Present before analyzing.** The user may not have read the source. Before any vault work, present:
- Source metadata (title, speaker(s), date, duration/length)
- Key points summary (5-10 bullets with exact figures)
- Themes identified

After presenting the summary, proceed immediately to Phase 1. Always assume full sweep — process every entity, every data point, every angle. Do not ask "what's the scope?" or "which slice?" — the answer is always "all."

## Phase 1: Full Enumeration

Process the entire source. Every paragraph, every aside, every throwaway detail.

Enumerate three lists:

- **Entities** — every actor, concept, product, event, country, person, firm mentioned. Include secondary mentions ("they're competing with X" counts).
- **Data points** — every price, AUM figure, percentile, growth rate, date, deal term, production volume, headcount. Exact figures with attribution.
- **Images/charts** — every provided chart, screenshot, table-like graphic, or source visualization. Identify which CONCEPT it depicts, not which source it came from. A yield percentile chart is a "CLO yield data" chart, not a "Rieder interview chart." Each chart must have a disposition: saved/embeded if rights allow, or extracted into note text/tables if copying is inappropriate.

Present enumeration to user as a table before vault work begins.

**Public-company M&A reaction trigger.** If the source is a merger, acquisition, take-private, spin-merger, or strategic combination involving any listed company, enumerate market-reaction data as first-class data points: acquirer move, target move, premium/exchange-ratio value, current implied consideration, gross and annualized spread, break-value assumption, crude implied close/fail odds when defensible, external probability/spread proxies, and "what did the tape believe?" Treat this as separate from the strategic rationale. Strategic logic answers why the deal could make sense; market reaction records whether investors agreed.

**Listed-company event / peer-reaction trigger.** If the source is a joint venture, strategic partnership, product launch, financing, customer win/loss, regulatory event, or competitive announcement involving listed companies or a listed peer set, run `/event-tape` before writing the analysis. Enumerate raw primary-actor moves, benchmark/sector-adjusted abnormal moves, obvious peer/competitor read-through, listed peers already named elsewhere in the note/entity list/read-through, relevant benchmark/sector ETF moves, same-day and next-day reactions when available, and the three-sigma stack: raw sigma, residual sigma, and abnormal/raw sigma. Do not subtract peer moves by default when the event plausibly affects peers indirectly; measure peer read-through separately and use peer-adjusted residuals only as diagnostics. If local price data is stale or missing, verify with an external historical-price source (StockAnalysis, exchange data, company IR, or another reliable market-data page) rather than leaving `TODO verify`. A `## Market Reaction` section with unresolved TODO/TBD/verify placeholders is not complete.

**Physical-bottleneck trigger.** If the source mentions infrastructure capital, MW/GW capacity, data centers, power, grid access, interconnections, PPAs, site selection, land, permits, construction, transformers, cooling, "energy and digital infrastructure," "long-term capacity," or "supply assurance," enumerate the physical constraint alongside the capital stack. Ask: who provides money, who provides technology/offtake, and who converts that into powered/operable capacity? Scope the write to existing constraint hubs where relevant (`[[Power constraints]]`, `[[Power purchase agreement]]`, `[[Power grid primer]]`, `[[Power-constrained geography]]`, `[[AI infrastructure financing]]`, `[[AI infrastructure deals]]`, `[[AI infrastructure financing risk]]`). Do not overclaim: if no power plant, PPA, utility interconnection, grid region, or site is disclosed, state that explicitly. See `docs/note-checklist.md#physical-bottleneck--constraint-cluster-sweep`.

## Phase 1.5: Classify before writing

Four gates run in order before any vault writes. Each gate filters what gets written, where it goes, and how confident the framing is. Run cold research (gate 4) last because it depends on knowing what concept-level writes are planned.

**Output a single classification matrix to the user before writes start** — one row per entity / data point, columns for the four gate outputs. The matrix makes the decisions visible so the user can object before writes begin. Example:

| Entity / data point | Verified? | Filing (concept vs actor) | Vault of record | Cold research run? |
|---|---|---|---|---|
| [[Rapidan Energy Group]] founding date | ✓ wiki | Actor | Investing | n/a (data) |
| Rapidan $150 trigger call | speaker | Actor (call + pattern) | Investing | n/a (data) |
| US crude export-controls framework | ✓ multi-source | New concept note | Investing primary; History gloss | yes |
| 1975 EPCA statute | ✓ wiki | n/a (history vault) | History | n/a (history-side write) |

### Gate 1: Verify — facts vs. opinions

Split every data point into:

- **Verifiable facts** (numbers, dates, policy decisions, market data) — research and confirm. If confirmed, write with attribution to source AND confirming data. If contradicted, flag the discrepancy. If unverifiable, attribute to the speaker — don't promote a claim to fact just because the source asserted it.
- **Sourced opinions** (views, predictions, frameworks) — attribute to the speaker. Note alignment or contradiction with existing vault views; don't present one person's view as established truth.

**Why it matters:** the vault's value depends on accuracy — a wrong number written confidently is worse than a gap.

Full process: `docs/research-workflow.md#two-track-source-verification` and `#fact-checking-non-filing-sources`.

### Gate 2: Classify content — concept vs. actor

For each substantive data point, ask: *does this describe what an entity IS or DOES, or does it describe a structure, mechanism, framework, or policy that exists regardless of the entity?*

- Entity behavior → entity's note
- Structure / mechanism / framework / policy → concept note, regardless of who articulated it

Attribution is not filing. When a named analyst says X, the storage impulse is "put it in their note" — resist. Any other shop calling the same thing in six months should land in the same concept note with different attribution.

Warning signs that an actor-note subsection should be a concept note: contains historical context predating the actor's involvement, transmission math or formulas, structural consequences tables, asset-exposure mapping across unrelated names, activation pathways, or its own Synthesis paragraph. Two or more → extract.

**Why it matters:** framework content trapped inside an actor note is invisible to future vault searches that reason by topic, not by source. Premature concept stubs are cheap; trapped framework content is expensive.

Full discussion: `docs/vault-note-guide.md#concept-vs-actor-classification`.

### Gate 3: Classify vault of record — lens test

For each substantive block, ask: *which vault's lens does this primarily live in?*

| Vault | Lens |
|---|---|
| Investing | Market impact, positioning, prices, portfolio implications |
| History | "How did we get here" — durability, precedent (5-year test) |
| Technologies | Foundational tech shifts — chip architectures, fab capacity, model breakthroughs |
| Geopolitics | Statecraft, alliances, sanctions, military operations |
| Brazil | Brazilian actors, markets, institutions |

One lens is primary. Others get a 1-2 sentence gloss + `obsidian://` link. Durable content embedded in transient notes inherits the transient half-life — keep durable content in durable vaults.

Warning signs investing is being used as a dumping ground (passed legislation cited as live variable, "how did we get here" framing, narrative arc with beginning-middle-end, content that doesn't change based on today's price/position) → vault of record is a sibling. Two or more apply → write the primary content in the sibling vault, gloss + link in investing.

Cross-vault writes are real writes to plan in this phase, not links to add at the end.

Full ownership table + warning signs: `docs/cross-vault-rules.md#vault-of-record--the-lens-test`.

### Gate 4: Cold research pass — when framing-level writes are planned

Triggers when the planned write would change *framing*: new concept note, new `## Synthesis` section, framework expansion in an existing concept note, retitling/rewriting an existing section, reframing an actor note's thesis or "Why X matters" paragraphs.

Does NOT trigger for: dated subsections under existing framing, new rows in existing tables, quarterly earnings sections, price refreshes, Related-section additions, stub creation (no synthesis to bias yet).

The discipline: WebSearch the *concept itself* — not the source — and pull authoritative framings (agency reports, academic work, research houses). If the field's framing diverges from the source's, the concept note's structural framing follows the field. The source contributes data points and attribution inside the structural frame.

Test question before writing: *"If I hadn't ingested this source, what would a domain-independent research pass say is central?"* Anything that fails this test is source anchoring; rewrite.

**Why it matters:** ingestion is the single largest generator of recency and source-anchoring bias. The source you just processed has the most gravity in your context. Skipping this gate is the dominant source of synthesis bias in ingested content.

Full process: `docs/research-workflow.md#cold-research-pass`.

## Phase 2: Vault Survey + Gap Audit

For each enumerated entity:

1. Check vault: `python scripts/check_before_create.py "Name"` for new entities
2. If exists → read the note, assess what's already covered vs. what's new
3. If missing → flag for creation
4. **Gap audit.** While reading each existing note, identify *structural* gaps — content the note should have regardless of this source. Reading the existing note in detail is the rare moment when gaps become visible; catch them then or they stay.

Structural gap categories: taxonomy entries missing from a list, engineering / mechanism content missing on a tech topic, hub/sub-hub branches the concept tree should have, relationship gaps in Related sections, pre-2024 historical arc on actors whose recent decisions need backstory, quantitative series missing on a public entity (ratings history, fund flows, debt-to-GDP).

Survey table:

| Entity | Status | What's new from this source | Gaps exposed (fill or TODO) |
|---|---|---|---|
| [[Entity A]] | Full note | New AUM figure, quote | — |
| [[Entity B]] | Stub | Full expansion warranted | Governance, debt profile, post-2024 history |
| [[Entity C]] | Missing | Create — mentioned 3x with hard data | — |
| [[Robotics]] (cross-vault) | Full note (technologies) | Nothing technical | UUV/USV row missing from Types taxonomy |

Every row gets processed. No silent skips on either column.

**Gap disposition.** If the source can close the gap cleanly with a primary source *right now*, do it in the same pass — the ingestion paid the cost of opening the file. If not, log the gap in the daily note as a research follow-up with what kind of source would close it.

Two biases to resist: "I noticed a gap so I should write something" (manufactures source-anchored content pretending to be category-level) and "I noticed a gap but the source can't fill it so I'll move on silently" (lets the gap stay invisible). Log the gap; don't fabricate filler.

## Phase 3: Image Routing

**Every provided chart is ingested.** A chart supplied by the user or present in the source is never optional. If rights allow, preserve the image. If publisher terms or copyright make copying inappropriate, ingest the chart by extracting the axes, series, dates, visible values/estimates, and takeaway into the relevant note with source attribution, and log that the image itself was not copied.

**Charts follow concepts, not sources.** For each image:

1. Ask: "What concept does this depict?" — the answer determines the destination note
2. Save to `investing/attachments/` with a descriptive name tied to the concept (e.g., `clo-yield-percentile-mar2026.png`), not the source, when rights allow
3. Embed in the concept note with italic caption and source attribution, even if that note is not otherwise on the update list — the image creates the reason to touch the note
4. If the image cannot be copied, add a chart-derived table or paragraph to the concept note instead, including axes/series/time period, visible values or estimates, and the source attribution
5. If the image also contextualizes the source actor (e.g., a fund's own allocation), embed or extract it in BOTH the concept note and the actor note
6. Record chart disposition in the daily note: `saved/embedded`, `extracted/not copied`, or `needs follow-up` with the reason

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

**Public-company M&A event gate:** when the event is M&A involving at least one listed company, the event note must include `## Market Reaction` with acquirer/target stock moves, premium or exchange-ratio implications, current implied consideration, gross and annualized spread, break-value assumption, crude implied close/fail odds when defensible, external probability/spread proxies, and one sentence answering "what did the tape believe?" Mirror the short version into the public acquirer/target securities notes as `## Market reaction` sections that link back to the event note. See `docs/note-checklist.md#public-company-ma-market-reaction`.

**Listed-company event / peer-reaction gate:** when the event is not M&A but changes the competitive or financing map for listed actors, the event note must include a completed `## Market Reaction` section using `/event-tape`: primary listed actors, obvious second-order exposed peers, any listed peers already named elsewhere in the note, relevant benchmarks, adjusted abnormal move, raw sigma, residual sigma, abnormal/raw sigma, peer read-through, price source/timestamp, and status. Do not mark the note done with `TODO verify`, `TBD`, or "verify later" inside that section. If the market has not closed yet, write the status explicitly ("same-day close not yet available as of HH:MM ET") and log a daily-note follow-up to fill it after the close. See `docs/note-checklist.md#listed-company-event--peer-reaction`.

**Copyright on quoted material:** max 15-word quotes from copyrighted articles. Paraphrase the rest with attribution.

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

**Explanation requirement.** The daily note must also contain a non-empty `## Synthesis` section for the ingestion. This is not an edit log. It preserves the reusable explanation: what changed, why it matters, the causal mechanism, who benefits or is pressured, and which vault got which part of the story. If the user receives a chat explanation, the same analytical frame must be promoted into this section before the session closes.

For single-source ingestions, the synthesis can be 1-3 tight paragraphs. For multi-article batches, write the through-line across articles plus any deliberate skips or source-quality caveats. The test: a reader opening only the daily note should understand the story, not just which files were touched.

**Cross-vault gate.** After completing updates, check sibling vaults per `docs/cross-vault-rules.md`. Flag to user.
