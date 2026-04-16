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

**Entity sweep at triage.** Before deciding whether content is worth ingesting, check ALL named entities — headline actors, secondary firms, origin firms, counterparties — for vault presence. Report which have notes and which don't. A story may not deserve ingestion, but a missing vault note for a mentioned entity is a gap worth surfacing regardless.

**Present before analyzing.** The user may not have read the source. Before any vault work, present:
- Source metadata (title, speaker(s), date, duration/length)
- Key points summary (5-10 bullets with exact figures)
- Themes identified

After presenting the summary, proceed immediately to Phase 1. Always assume full sweep — process every entity, every data point, every angle. Do not ask "what's the scope?" or "which slice?" — the answer is always "all."

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

## Phase 1.6: Classify content — concept vs. application

Before any vault writes, classify each substantive data point from Phase 1 by filing location. This is the gate that prevents framework material from getting buried inside actor notes through source-gravity alone.

**The test.** For each data point, ask: *does this describe what an entity IS or DOES, or does it describe a structure, mechanism, framework, or policy that exists regardless of the entity?*

- **What an entity is or does** → lives in the entity's note. Examples: "Rapidan is a DC energy consultancy founded by McNally," "Rapidan called X on date Y," "McNally's White House network is the source of the call."
- **Structure, mechanism, framework, or policy** → lives in a concept note, regardless of who articulated it. Examples: transmission math between oil prices and pump gasoline, legal authorities that activate export controls, historical precedent for a policy option, bidirectional scenario maps for an intervention.

**The warning signs.** A subsection inside an actor note starts looking like its own note when it contains any of:

- Historical context predating the actor's involvement (1975 legislation, 2015 repeal, 2022 precedent)
- Transmission math, formulas, or quantitative frameworks usable outside this source
- Structural consequences tables ("if X, then Y") that would apply to any analyst calling the same thing
- Asset-exposure mapping across unrelated names
- Activation pathways or legal mechanics
- A Synthesis paragraph — actor notes don't need one; concept notes do

If two or more of the above appear in a subsection, extract to a concept note. The actor keeps only the firm-specific call, pattern, and attribution.

**Attribution is not filing.** When a named analyst or firm says X, the default storage impulse is "put it in their note." Resist. Attribution tracks *who said it*; filing tracks *what it is*. Any other shop calling the same thing in six months should land in the same concept note with different attribution — not create a parallel discussion inside a different actor note.

**When in doubt, create the concept note.** The cost of a premature concept stub is low (it can grow over time). The cost of framework content trapped inside an actor note is high — it is invisible to future vault searches that reason by topic, not by source.

**Add the classification to the Phase 2 survey table** as an extra column so decisions are explicit before writes begin:

| Entity / data point | Status | What's new | Filing decision |
|---|---|---|---|
| [[Rapidan Energy Group]] | Full note | $150 trigger call | Actor: keep the call + pattern |
| $150 trigger framework | (concept-level) | Transmission math, legal mechanics, precedent | New concept: [[US crude export controls]] |

## Phase 1.7: Classify content — vault of record (lens test)

The concept-vs-actor gate (1.6) decides *where within this vault* content lives. This gate decides *which vault owns the content* in the first place. Run it after 1.6 but before any writes.

**The test.** For each substantive block of content, ask: *which vault's lens does this content primarily live in?*

Each sibling vault has its own lens — the angle it looks at the world through:

| Vault | Lens |
|---|---|
| Investing | Market impact, positioning, prices, portfolio implications — what should I own today and why |
| History | "How did we get here" — durability, precedent, structural breaks, long-arc patterns |
| Technologies | Foundational tech shifts — chip architectures, fab capacity, model breakthroughs, supply-chain evolution |
| Geopolitics | Statecraft, alliances, sanctions architecture, military operations, diplomatic timelines |
| Brazil | Brazilian actors, markets (BRL, B3, DI, Ibovespa, ADRs), domestic institutions, domestic policy |

Content can touch multiple lenses — an Iran oil story engages investing (WTI price), geopolitics (Strait of Hormuz), and possibly history (prior oil shocks). One lens is primary; the others get a 1-2 sentence gloss and an `obsidian://` link in the respective vaults.

**Durability corollary (history specifically).** For content that *could* live in history, a sharper test: *will this still be true, and still be the primary place to find this, in five years?* Yes → history owns it; investing gets a gloss. This is the cleanest version of the lens test for history because history's lens is fundamentally about durability. For the other sibling vaults, use the lens directly — "is this a tech-architecture story?", "is this a statecraft story?", "is this a Brazil-domestic story?"

**Vault ownership by content type:**

| Content type | Vault of record | Investing treatment |
|---|---|---|
| Legislation, statutes, policy regimes (1975 EPCA, Glass-Steagall, Dodd-Frank) | History | Gloss + link |
| Historical crises, prior-cycle patterns (1970s stagflation, 2008 GFC, 2015 CNY devaluation) | History | Gloss + link for precedent |
| Long-arc technology shifts (transistor, EUV origins, Bell Labs) | Technologies | Gloss + link when referenced |
| Foundational chip/model architectures (transformer, TPU, HBM origins) | Technologies | Ticker-level exposure only |
| Military operations, diplomatic timelines, sanctions architecture | Geopolitics | Market-impact lens only |
| Alliance shifts, multilateral frameworks (BRICS, AUKUS) | Geopolitics | Market-impact lens only |
| Brazilian domestic politics, institutions, Plano Real | Brazil | Market impact (BRL, B3, ADRs) only |
| Brazilian macro policy, Copom decisions, fiscal framework | Brazil | Market impact only |
| Current positioning, price action, portfolio impact | Investing | Full treatment |
| Live policy triggers, active frameworks (Rapidan $150) | Investing | Full treatment |
| Current event narratives being written in real time | Investing or event-specific vault | Full treatment |

**Warning signs that investing is being used as a dumping ground:**

- Content whose natural home is another vault's lens (legislation → history; chip architecture → technologies; diplomatic timeline → geopolitics; Brazilian institution → Brazil)
- Dates predating the vault's time horizon (investing thinks in months/quarters; 5+ years old is history)
- Passed legislation cited as live variable (it's history once enacted)
- Narrative arc with beginning-middle-end (that's a historical story; investing writes the open chapter)
- "How did we get here" framing (literally history's lede question)
- Content that doesn't change based on today's price, position, or catalyst

If two or more apply, the content's vault of record is a sibling vault. The investing note gets the gloss and link.

**Proximity bias warning.** The working directory pulls toward inlining. Writing across vaults requires a context switch. Pay the switch cost — future-retrieval from the wrong vault is more expensive than one context switch now.

**Durability mismatch.** Durable content inherits the half-life of whatever note it's embedded in. A 1975 statute embedded in a 2026-Rapidan concept note gets archived with that concept note. Keep durable content in durable vaults.

**Output the cross-vault filing decisions alongside the concept/actor decisions** before any writes begin. Flag any cases where a sibling vault needs a new note — that is a write to plan, not a link to add at the end.

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
- **Classify content before writing** — Phase 1.6 gate. Framework/mechanism/precedent material goes in concept notes, not subsections of actor notes. Attribution is not filing.
- **Classify vault of record before writing (lens test)** — Phase 1.7 gate. Each sibling vault has its own lens: history = "how did we get here" (durability, precedent), technologies = foundational tech shifts, geopolitics = statecraft/alliances/sanctions, Brazil = Brazilian actors/markets/institutions, investing = market impact/positioning. Content can touch multiple lenses; one is primary. The 5-year durability test is the sharp corollary for history specifically. Durability mismatch traps durable content with transient half-lives.
- **Charts follow concepts, not sources** — route images to concept notes, not actor/source notes
- **Images create the reason to touch a note** — even if that note wasn't otherwise on the update list
- **Full entity sweep** — every name, every number, every aside gets processed
- **Every chart needs a data table** — reader sees numbers alongside visualization
- **Daily note placement** — `## Notes created/expanded` section, before `## News ingestion` or `## Edit log`
- **Copyright** — max 15-word quotes from articles; short quotes only
