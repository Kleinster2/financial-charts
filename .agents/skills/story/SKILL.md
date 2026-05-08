---
name: story
description: "Generate the daily 'what is the story' report from a Daily note. Reads the daily note plus notes created/expanded during the session, then writes concise story cards for every meaningful thread touched that day. Use when the user says /story, /daily-story, 'what is the story report', or asks for all stories from today's daily note."
---

# /story — Daily What-Is-The-Story Report

Daily synthesis artifact. This is the exhaustive companion to `/newsletter`: it turns the daily note's edit log into a set of concise "what is the story" cards covering every meaningful thread touched that day.

Use `/story [YYYY-MM-DD]`. If no date is provided, run the local date command and use today's daily note.

## What this skill is

- A saved vault artifact at `investing/Reports/YYYY-MM-DD-story-report.md`.
- A bridge from daily-note logging to actual thesis memory: every card says what changed, why it matters, and what tension remains.
- Comprehensive across the day, but grouped by story rather than mechanically one card per note.

## What this skill is not

- Not `/newsletter`: the newsletter selects the 2-5 most important stories and writes a polished end-of-day brief.
- Not `/report`: reports are on-demand synthesis for one topic across vaults.
- Not `/ingest`: do not add new source facts or expand entity notes while running `/story`.
- Not a compliance log: formatting fixes, chart plumbing, and stub cleanup only appear when they change the analytical read.

## Phase 1 — Resolve Date And Inputs

1. Confirm the date:
   ```powershell
   Get-Date -Format yyyy-MM-dd
   ```
   Use the requested date if the user supplied one.

2. Read `investing/Daily/YYYY-MM-DD.md`. If missing, stop and say the daily note does not exist.

3. Extract these sections when present:
   - `## Notes created/expanded`
   - `## Reports`
   - `## News ingestion`
   - `## Edit log`
   - any section with source-specific headings or synthesis text

4. Build a touched-note inventory from every `[[wikilink]]` in the daily note, then separate:
   - Primary touched notes: notes created, expanded, or materially reframed.
   - Supporting notes: stubs, attribution entities, securities companions, chart-only assets, and notes only mentioned as context.
   - Mechanical work: docs, scripts, Quartz, chart registry, formatting, compliance, or link cleanup.

## Phase 2 — Read The Notes

Read the daily note first, then read the primary touched notes. Use the daily note as the map, not as the source of truth.

For each primary note or thread, capture:
- What changed today: new fact, new section, new event, new chart, new framing.
- The story: one sentence naming the real arc.
- Why it matters: structural implication, cross-read, market relevance, or vault architecture relevance.
- The tension: what is unresolved, contradictory, or conditional.
- Watch item: the next data point, filing, price, event, or decision that would confirm or break the read.

Do not run web research by default. If the daily note says verification is incomplete, list that as a gap rather than quietly researching.

## Phase 3 — Group Into Story Cards

Group related notes into story cards. The output should usually have 5-15 cards depending on the size of the day.

Completeness rule: every substantive heading under `## Notes created/expanded` must either:
- appear as a story card,
- be named in a story card's `Touched:` line, or
- be listed under `## Mechanical / not a story` with a one-line reason.

Bundle routine stubs under the parent story. Example: if an article created `[[NBS]]`, `[[General Administration of Customs]]`, and `[[Capital Economics]]` as attribution stubs, the card is the macro story; the stubs are touched notes, not separate stories.

Mechanical work can still be a story if it changes how the vault works. A Quartz migration, chart registry rebuild, or note-taxonomy fix can be a workflow story.

## Phase 4 — Write The Report

Path: `investing/Reports/YYYY-MM-DD-story-report.md`.

If the file exists and the user asked to refresh or update it, edit it in place. If it exists and the user did not ask for refresh, create `YYYY-MM-DD-story-report-2.md`, then `-3`, etc.

Format:

```markdown
---
date: YYYY-MM-DD
type: daily-story-report
source: "[[YYYY-MM-DD]]"
generated: YYYY-MM-DD HH:MM
story_cards: N
touched_notes: M
tags: [report, daily-story]
---

# YYYY-MM-DD — What Is The Story

## Story map

| Thread | Touched notes |
|---|---|
| [short label] | [[Note A]], [[Note B]] |

## [Story headline — name the tension]

Touched: [[Note A]], [[Note B]], [[Note C]]

The story is [central insight in one sentence].

What changed: [specific facts, dates, figures, and source trail if already in the notes].

Why it matters: [structural implication or cross-read].

The tension: [unresolved constraint, contradiction, or threshold].

Watch: [next concrete thing to check].

## Mechanical / not a story

- [Thread or note] — [why it is logged but not analytically live].

## Gaps

- [Missing verification, stub, cross-vault gap, or follow-up surfaced by the daily note].
```

Style:
- Preserve `[[wikilinks]]` visibly.
- No bold in body text. Headers only.
- Prefer exact figures and dates already present in the touched notes.
- Do not claim "the market is missing" unless the vault contains positioning, spreads, flows, or options evidence.
- Cards must stand alone. Never look for connections between or among cards. No "see Card X," no "in the same way as," no synthesis paragraph that ties multiple cards together, no Watch items that reach into another card's territory. Each card answers "what is this story" in isolation. The Story map table is a pure index, not a thesis.
- Never assume the reader is familiar with the details. Every name gets a one-clause role tag the first time it appears (e.g., "Mike McKee, Bloomberg's Fed correspondent" not just "Mike McKee"); every acronym gets expanded on first use ("BDC — business development company"); every prior event referenced gets a brief in-card anchor ("Norway raised its wealth tax from 0.85% to 1.1% in 2022 and saw $54B in wealth leave the country" not just "the Norway 2022 case study"); every market level or threshold gets a why-it-matters clause ("4.25% on the 10Y is where Lyngen says duration becomes a buy"). The reader is not expected to have read the underlying notes, prior story reports, the daily note, or earlier cards. Cards are no longer length-capped — write the context that the story requires, not what fits in 80-150 words.

Charts (optional):
- The print pipeline resolves Obsidian image embeds (`![[chart.png]]` / `![[chart.png|caption]]`) to figures that span both columns. Use them sparingly: at most one chart per major story card, and only on the cards where a chart actually anchors the read.
- Only embed charts that already live in a touched note. Do not generate a fresh chart for the report — the chart must be one already in the vault. This keeps charts anchored to vault state.
- Place the embed inside the card, after the `Touched:` line and before the analytical sentences, so the chart sets up the read.
- The optional caption (after the `|`) renders as italic figcaption. Use it to name the chart's point in one clause.
- Mechanical / not a story cards never get charts.

## Phase 5 — Daily Note Log And Chat Output

Log the report under today's daily note `## Reports` section. Create the section if missing:

```markdown
## Reports

- HH:MM — `/story YYYY-MM-DD` → [[YYYY-MM-DD-story-report]] (N story cards, M touched notes)
```

Then summarize in chat:
- saved path,
- story-card count,
- the highest-level one-line theme for the day,
- any gaps that require follow-up.

Do not echo the full report unless the user asks for it.

## Phase 6 — Render audio (default)

After saving the report and logging it in the daily note, automatically render the spoken-version MP3:

```
python scripts/audio_newsletter.py YYYY-MM-DD --type story
```

What it does: reads `investing/Reports/YYYY-MM-DD-story-report.md`, adapts it for spoken delivery (strips wikilink brackets and table rows; expands percent ranges, dollar magnitudes including spelled-out forms like `$80 million` and FT-style `$230bn`, dollar ranges, quarter and fiscal-year abbreviations, bps, MoU, σ; smooths em-dashes into comma-pauses), then writes `investing/Reports/YYYY-MM-DD-story-report.mp3` via the auto-fallback chain: **ElevenLabs primary** (voice `sarah`, model `eleven_multilingual_v2`) → **OpenAI fallback** (voice `nova`, model `gpt-4o-mini-tts`) on any provider failure. The Story map table is stripped from the audio (it's an index, not narrative); the cards themselves carry the content.

Open the MP3 in the user's default player after generation:

```
start "" "investing/Reports/YYYY-MM-DD-story-report.mp3"
```

If the report has a numbered suffix (e.g., `-2`, `-3`), use `--input` instead of `--type`:

```
python scripts/audio_newsletter.py --input investing/Reports/YYYY-MM-DD-story-report-2.md
```

**Length note:** story reports are typically 2-4× the length of newsletters (5-15 cards each with 80-150+ words of context), so audio runs ~15-25 min and consumes a larger share of any quota window. Use `--preview` for a sample test before the full render. ElevenLabs free tier (10K chars/month) is exhausted by a single full story report, after which the chain auto-falls-through to OpenAI without intervention. Use `--dry-run` to inspect the adapted text without an API call. Pin to one provider with `--provider {elevenlabs,openai}` to disable fallback. Override voice with `--voice` (ElevenLabs: sarah, adam, rachel, charlotte, george, brian; OpenAI: alloy, echo, fable, onyx, nova, shimmer, ash, sage, coral).

If both providers fail, don't block the workflow — note the failure in chat and continue with print/save.

## Phase 7 — Print (only on user request)

When the user says "print", "send to print", "print it", etc., use the dedicated report-print script. Story reports auto-render in the same two-column layout as the newsletter (Georgia serif, 8.75pt, justified, column rule, visible gray wikilinks); the H1 and the `## Story map` table span both columns.

```
python scripts/print_report.py YYYY-MM-DD-story-report --print
```

What it does: renders the markdown to HTML with the two-column CSS, generates `investing/Reports/YYYY-MM-DD-story-report.pdf` via Chrome headless, then prints via Edge kiosk-printing to the default printer (`HPFA4FA6 (HP DeskJet 2700 series)`). Override the printer with `--printer NAME`. Force single-column with `--columns 1` if the user explicitly asks. Drop `--print` to generate the PDF only.

**Do not** improvise with `Out-Printer`, `notepad /p`, or a hand-rolled HTML. The two-column layout and visible wikilinks are the point — the same artifact the newsletter produces, just for the exhaustive story map.

If the report has a numbered suffix (e.g., `-2`, `-3`), pass the full stem: `python scripts/print_report.py YYYY-MM-DD-story-report-2 --print`.
