---
name: report
description: "Cross-vault topic synthesis. Reads existing notes across investing + sibling vaults (geopolitics, Brazil, history, technologies) and writes a 400-800 word narrative brief saved to investing/Reports/. Read-only — never modifies entity notes. Use when the user asks to brief them on a topic, says /report TOPIC, or wants a pointed read on something already in the vault. NOT for new research (use /deepdive) or daily wrap-ups (use /newsletter)."
---

# /report — Cross-Vault Topic Synthesis

Read-only synthesis skill. Pulls existing notes across all vaults that have content on a topic and produces a narrative brief. Never edits entity notes; only writes the report itself.

Usage: `/report <topic> [--lens neutral|allocator|contrarian|what-changed] [--since YYYY-MM-DD] [--full]`

## What this skill is NOT

- Not `/deepdive` — no web research, no SEC filings, no DB lookups, no chart generation. If primary note is missing, stop and suggest `/deepdive`.
- Not `/newsletter` — that's today's daily wrap. This is on-demand for any topic.
- Not `/ingest` — that processes a single source. This synthesizes existing vault content.
- Not a note expansion — never touches the entity notes it reads. Only writes to `investing/Reports/`.

## Hard rules

- Output saved to `investing/Reports/YYYY-MM-DD-<topic-slug>.md`. Always in-vault, always dated.
- `[[wikilinks]]` preserved in body — reports are printable per CLAUDE.md printing rule.
- No bold in body. Headers only. Same voice rules as `/newsletter`.
- All four sibling vaults (geopolitics, Brazil, history, technologies) consulted on every run; report integrates whatever they have.
- Reports are disposable. Re-run anytime; old reports are not load-bearing.

---

## Phase 0 — Resolve the topic

1. **Parse the input shape** — classify before anything else. The word joining the topics matters:

   | Input pattern | Behavior |
   |---|---|
   | Single topic (`CUDA moat`) | Proceed with steps 2-5 below. |
   | `<A> vs <B>` or `<A> versus <B>` | **Comparison report** — one file, dual anchors. Slug keeps `vs` (`brazil-carry-vs-us-ai-capex`). Resolve both anchors in step 3; Phase 1 gathers ~7-8 notes per side; Phase 2 arc is the tension between them. |
   | Comma-separated (`<A>, <B>, ...`) | **Sequential reports** — run the full skill once per topic. One file + one daily-note line per topic. Do NOT synthesize across them. |
   | Ambiguous connectives (`and`, `&`, `plus`, `+`) | **Stop and ask** — "Comparison report (one file, juxtaposition is the point) or separate reports (N files)?" Do not guess. |

2. **Slugify** the topic: lowercase, hyphenate. `CUDA moat` → `cuda-moat`. Keep the original case for display. For comparison reports, slugify the full phrase including `vs`.

3. **Resolve in investing vault** (primary):
   ```bash
   python scripts/check_before_create.py "<Topic>"
   ```
   Use the same resolver vault uses for entity matching. Catches aliases. For comparison reports, resolve each anchor independently; if either fails, stop and report which one.

4. **Branch:**
   - **Exact match** → use that note as primary. (Comparison reports require exact match on both anchors.)
   - **Multiple candidates** → ask user to pick.
   - **No match in investing** → check sibling vaults (`grep -r` on `~/obsidian/{geopolitics,brazil,history,technologies}/`). If found in a sibling, ask user: "Primary note is in `<sibling>` vault. Generate report from that lens?"
   - **No match anywhere** → stop, tell user, suggest `/deepdive`.

5. **Stub gate** — count substantive lines in primary note (exclude frontmatter, Quick stats, Related). If under 30 lines:
   - Stop. Output: "`<Topic>` is a stub (N lines of substance). Run `/deepdive <Topic>` first, or re-run with `--force` to synthesize what's there."
   - For comparison reports, apply the stub gate to both anchors; if either is a stub, stop.

---

## Phase 1 — Gather

Read in this order, capping at ~15 notes total to keep the synthesis tractable:

1. **Primary note** — full read.
2. **Cross-vault links** — parse the `### Cross-vault` subsection of the primary's Related section. Resolve each `obsidian://` URI to a real path and read the counterpart. These are the user-curated cross-vault siblings.
3. **Related (1 hop)** — follow wikilinks in the primary's Related section. Cap at 8 within investing.
4. **Sibling-vault grep** — even if no `Cross-vault` subsection exists, run a grep for the topic across all four sibling vaults:
   ```bash
   grep -rli "<topic>" ~/obsidian/geopolitics ~/obsidian/brazil ~/obsidian/history ~/obsidian/technologies
   ```
   Read the top 1-2 hits per vault that aren't already covered by Cross-vault links.
5. **Backlinks** — get ranked backlinks within investing:
   ```bash
   "/c/Users/klein/AppData/Local/Programs/Obsidian/Obsidian.com" vault=investing backlinks file="<primary-note>"
   ```
   Rank by mention count × section depth. Use top 5 for context. Show all under "Other vault references" footer.
6. **Cold research pass (mandatory)** — before Phase 2, run WebSearch on the concept itself, not on whatever was most recently ingested. Use domain-independent queries ("X market structure 2026 analyst consensus," "X regulatory framework 2026 academic," "X structural analysis CSIS/IEA/Wood Mackenzie"). Pull authoritative framings from agencies, academic work, law-firm annual reviews, and research houses. The gate applies to framing writes (new concept notes, `## Synthesis` sections, and critically **retitled or rewritten sections in existing notes** — framing-shift, not just new-note creation). See `docs/research-workflow.md#cold-research-pass` for the full discipline, failure modes, scope, and the test question. **Skipping this step is the single largest source of bias in report output.**

If `--since YYYY-MM-DD` is set, use `git log --since="YYYY-MM-DD" -- <note-path>` to identify what's been added; bias the gather to those edits.

---

## Phase 2 — Synthesize

The narrative arc (per `feedback_synthesis_voice.md`):

> central insight → constraint → counter-example → one-line

This is the only acceptable structure. If you find yourself writing "Background:" / "Current state:" / "Outlook:" — stop. That's the source notes' structure, not synthesis.

**Discipline:** the report must produce framing the source notes don't already express. If the synthesis is "the primary note rearranged," it failed. Ask: what do I see when I look at investing + history + geopolitics + tech + Brazil together that I don't see in any single note?

**Lens behavior** (`--lens` flag, default `neutral`):

| Flag | Angle |
|---|---|
| `neutral` (default) | Present dynamics. Name tensions. No editorial frame. |
| `allocator` | Lead with what an investor would do today. Position-implication framing. |
| `contrarian` | Lead with the case the consensus notes are missing. Stress-test the dominant read. |
| `what-changed` | Chronological delta only. What's moved since the topic was last fresh in the vault. Pairs naturally with `--since`. |

**Voice rules** — inherit from `/newsletter`:
- Analytical, not editorial. No bull/bear calls. No "the market isn't pricing X" claims.
- Exact figures with sources. No "significant" or "substantial."
- Sharp, not sterile. Reader is a macro-focused investor who has the vault context.
- Tensions over conclusions. Surface contradictions; let the reader decide.

**Calibrate for high general knowledge, low subject-specific knowledge.** The reader is an informed macro investor — assume they know sigma, beta, IRR, EPS, NII, ROE, CDS, ETFs, OPEC, shipping incoterms (CIF, FOB), off-take, Mitsui / Sumitomo / other major trading houses, G20 heads of state (Milei, Lula, Boric, Xi, Trump), basic commodity terminology. Do NOT gloss any of those.

DO gloss *subject-specific* jargon on first use in the report body, with a 3-10 word parenthetical. This does NOT mean dumbing down or cutting detail — keep every figure, every attribution, every nuance. It means a reader with strong macro context but no lithium-industry (or rare-earth, or Brazilian-fiscal, etc.) vocabulary can still parse the synthesis.

Examples of what to gloss:
- Industry-specific abbreviations most finance readers would not know: `tonnes per year of lithium carbonate equivalent (LCE, the standard industry unit)`, `1.6nm A16 node (backside power delivery generation)`, `WTI basis (Cushing vs Brent spread)`
- Domain policy / political shorthand: `"anti-involution" — Beijing's campaign against overcapacity-driven price collapses in strategic industries`, `Arcabouço Fiscal (Brazil's 2023 fiscal framework replacing the spending cap)`
- Specialist geographic or geological terms: `Puna Plateau salt flats`, `Smackover Formation (underground brine reservoir across Arkansas-Louisiana)`, `CoWoS (TSMC advanced packaging)`
- Niche pricing agencies, research houses, or indices: `the pricing-agency Fastmarkets`, `Benchmark Mineral Intelligence`, `the Shanghai Metals Market (SMM) price`
- Newly-introduced proper nouns for recent events: `Nova Andino Litio JV (Dec 2025 Codelco-SQM partnership)` on first mention; subsequent mentions just the name

Examples of what NOT to gloss:
- Statistical and market-structure terms: σ, beta, basis points, standard deviation, z-score
- Standard financial metrics: IRR, EPS, NII, ROTCE, CDS, NAV, AUM
- Shipping / trade incoterms: CIF, FOB, EXW, CFR
- G20-level political figures and central bankers: Milei, Lula, Boric, Trump, Xi, Powell, Lagarde
- Major well-known trading houses and banks: Mitsui, Mitsubishi, Glencore, Trafigura, Goldman Sachs
- Terms already glossed earlier in the same report
- Concepts that have their own [[wikilinked]] vault note (the wikilink itself is the pointer)

The test: if a finance professional who follows markets daily but doesn't know the specific subject would pause and wonder what a word means, gloss it. If they'd roll their eyes at the gloss, don't.

**Cross-vault weave** — when content from multiple vaults bears on a single point, integrate inline (don't section-by-vault):

> The real today reflects a 1,100bp carry advantage [[Selic]] vs Fed funds, anchored by the [[Arcabouço Fiscal]] credibility regime — a fiscal architecture Brazil has only had for two cycles, against a five-decade history of regime collapses ([History: Plano Real](obsidian://...)). The carry is the easy story; the durability of the regime is the harder one.

That paragraph pulls investing (rate differential), Brazil (fiscal framework), and history (regime durability) into one analytical thread. That's the test.

---

## Phase 3 — Gap surface

Before closing the report, scan what you read for:

- **Dead wikilinks** in the primary note (entities mentioned but no note exists) — list under "Gaps."
- **Stub notes** referenced as if substantive — flag them.
- **Cross-vault counterparts that should exist but don't** — e.g., the investing note covers a topic with deep historical roots but there's no history vault entry.

The Gaps section is the feature that makes `/report` a vault tool, not just a prose generator. It tells the user what to research next.

---

## Phase 4 — Write the report

Path: `investing/Reports/YYYY-MM-DD-<topic-slug>.md`

Confirm date: `date +%Y-%m-%d`. Use that exact date in filename and frontmatter. If file already exists for today and topic, append `-2`, `-3`, etc.

**Format:**

```markdown
---
name: <Topic>
type: report
topic: "[[<Primary Note>]]"
lens: <neutral|allocator|contrarian|what-changed>
generated: YYYY-MM-DD HH:MM
sources_read: N
tags: [report]
---

# <Topic> — <one-line theme>

[2-4 paragraphs synthesizing across vaults. Narrative arc, not section dump.
Inline `[[wikilinks]]` to entities. Inline `[History: X](obsidian://...)` to cross-vault.]

## What's new (only if --lens what-changed or --since)

[Chronological delta. Specific dates, exact figures.]

## Other vault references

- [[Note A]] — what it adds
- [[Note B]] — what it adds
- [Geopolitics: Note C](obsidian://...) — what the other lens adds

## Gaps

- [[Missing Entity]] — referenced in [[Primary]] but no note exists
- [[Stub Note]] — only N lines of substance; consider `/deepdive`
```

**Length:** target 400-800 words in body (excluding frontmatter and footer sections). Shorter is fine if the topic is narrow.

**Final check before save:**
- All `[[wikilinks]]` preserved (printable rule)
- No bold in body
- No bull/bear framing
- Exact figures, attributed
- Synthesis arc, not source-note rearrangement

---

## Phase 5 — Daily note + chat output

1. **Log to today's daily note** under a `## Reports` section (create if missing):
   ```markdown
   ## Reports

   - 14:23 — `/report <Topic>` → `[[YYYY-MM-DD-<topic-slug>]]` (lens: <flag>, N sources)
   ```

2. **Echo the report body to chat** so the user reads it without opening the file. Mention the saved path in one line at the end:
   > Saved to `investing/Reports/YYYY-MM-DD-<topic-slug>.md`. Disposable — re-run anytime.

---

## Reports/ folder hygiene

- `investing/Reports/` is the canonical location.
- Reports carry `tags: [report]` and `type: report` so they can be filtered out of compliance scans, vault-of-record gates, and cross-vault gates (none of those apply to disposable synthesis).
- Reports are NOT entity notes — `check_note_compliance.py` should not run against them. If a hook trips on a report, exclude `investing/Reports/` in the hook config.
- Old reports stay on disk indefinitely. The user manually clears `investing/Reports/` when it gets noisy. No auto-expiry.

---

## Failure modes to avoid

- **Re-stating the primary note.** If the report could be generated by reading just the primary note alone, the cross-vault gather added nothing. Re-do the synthesis or surface the actual cross-vault tension.
- **Vault-by-vault sections.** "Investing perspective:", "History perspective:" is concatenation, not synthesis. Weave them inline.
- **Editorial framing.** "This is bullish for X" is wrong. "The setup that would make X bullish requires Y; today Y is at Z" is right.
- **Touching entity notes.** This skill is read-only on the rest of the vault. The only file this skill writes is the report itself plus the daily note line.
- **Dropping wikilinks.** `[[NVIDIA]]` stays as `[[NVIDIA]]` in the output, never collapsed to "NVIDIA" or "Nvidia". CLAUDE.md printing rule applies.
