---
name: explain
description: "Plain-language briefing on a vault topic for a reader unfamiliar with the actors and subtopics — same cross-vault read as /report, journalistic-explainer voice with first-mention introductions and glosses. Use for /explain TOPIC, a primer / briefing / explainer, or 'what's the situation with X' for someone not steeped in the threads. NOT for new research (/deepdive), vault-reader synthesis (/report), or daily wrap-ups (/newsletter)."
---

# /explain — Plain-Language Briefing on a Vault Topic

Read-only briefing skill. Pulls the same vault material as `/report` but writes for a reader who doesn't know the actors, the subtopics, or the surrounding threads. Each named actor gets a one-sentence introduction on first appearance. Each subject-specific concept gets a one-line gloss. The narrative builds context as it goes so a generalist follows without prior reading.

Usage: `/explain <topic> [--depth short|standard|long]`

## What this skill is NOT

- Not `/report` — that's analytical synthesis for someone who knows the vault. Voice is sharp and assumes context. `/explain` assumes none.
- Not `/deepdive` — no web research, no SEC filings, no chart generation. If primary note is missing, stop and suggest `/deepdive`.
- Not `/newsletter` — that's today's market wrap.
- Not a note expansion — never touches entity notes. Only writes to `investing/Reports/`.

The audience test: `/report` is for the user reading the vault. `/explain` is for an intelligent friend who has not been following the topic and wants to be brought up to speed before reading the vault.

## Hard rules

- Output saved to `investing/Reports/YYYY-MM-DD-explain-<topic-slug>.md`. Always in-vault, always dated, always prefixed `explain-` for sortability.
- `[[wikilinks]]` preserved in body — explainers are printable per the repo printing rule.
- Voice baseline: `docs/vault-note-guide.md` → "Voice and Writing Standards" — no bold in body, no bull/bear framing or "the market isn't pricing X" claims, no investment recommendations, no emojis.
- Reports are disposable. Re-run anytime; old explainers are not load-bearing.

---

## Phase 0 — Resolve the topic

Same as `/report` Phase 0:

1. Slugify topic. `UAE OPEC exit` → `uae-opec-exit`.
2. Run `python scripts/check_before_create.py "<Topic>"` to find the primary note.
3. Branch on match:
   - **Exact match** → use that note as primary.
   - **Multiple candidates** → ask user to pick.
   - **No match in investing** → check sibling vaults (`grep -r` on `~/obsidian/{geopolitics,brazil,history,technologies}/`). If found, ask user whether to brief from that lens.
   - **No match anywhere** → stop, tell user, suggest `/deepdive`.
4. **Stub gate**: count substantive lines in primary (exclude frontmatter, Quick stats, Related). If under 30 lines, stop and suggest `/deepdive` first.

---

## Phase 1 — Gather

Same as `/report` Phase 1, with one addition:

1. **Primary note** — full read.
2. **Cross-vault links** — read counterpart notes referenced under the primary's `### Cross-vault` subsection.
3. **Related (1 hop)** — follow wikilinks in Related section. Cap at 8 within investing.
4. **Sibling-vault grep** — even if no Cross-vault subsection exists, grep across all four sibling vaults and read the top 1-2 hits per vault not already covered.
5. **Backlinks** — top 5 by mention count × section depth.
6. **Actor / concept inventory (explain-specific)**: as you read, build a running list of every named actor, concept, event, and acronym mentioned in the primary or its near-neighbors. For each, note whether the vault has a note (and ideally, a one-line gloss derivable from that note). This list drives the first-mention discipline in Phase 2.

Cap total reads at ~15 notes.

No cold-research pass — this skill is read-only on the vault and does not introduce framings the source notes don't already express.

---

## Phase 2 — Write the explainer

The structure is linear narrative, not analytical synthesis. It builds in this order:

1. **Lede (1 paragraph)** — what happened, when, in plain terms. The headline a generalist reader would want.
2. **Cast (1-2 paragraphs)** — who's involved. Each named actor introduced with a one-sentence role-and-stake gloss on first mention. After first mention, just use the name.
3. **Why it matters (1-2 paragraphs)** — what makes this consequential. State the stakes in concrete terms (barrels, dollars, jobs, alliances, policy outcomes).
4. **The context (2-4 paragraphs)** — the surrounding threads that make today's event intelligible. This is where most of the explainer work lives. Walk the reader through the prior conditions, the institutions involved, the recent history.
5. **What's contested / what to watch (1 paragraph)** — close with the open questions and the diagnostic markers a reader could track to see how the situation evolves.

There is no analytical synthesis section. If you find yourself writing "the central insight is..." or "the structural read is..." — stop. That's `/report` voice. `/explain` describes; it does not synthesize.

### Voice rules

- **Journalistic explainer.** Think NYT/Reuters/FT primer or CFR backgrounder. Active verbs, concrete subjects, clean transitions.
- **Plain language.** No vault shorthand, no insider abbreviations on first use. The reader is smart and curious; do not condescend, but do not assume context.
- **First-mention discipline (the core innovation):**
  - Every named person: one-sentence role intro on first use. `Suhail Al Mazrouei, the UAE's energy minister, ...`
  - Every organization or institution: one-line gloss. `OPEC+, the broader oil-producing cartel that adds Russia and ten non-OPEC states to OPEC's eleven members, ...`
  - Every event already in the vault: one-line context. `the 2026 Strait of Hormuz crisis (which began in late February when Iran mined the chokepoint after Israeli strikes), ...`
  - Every domain-specific concept: one-line gloss. `the petrodollar (the post-1973 convention of pricing oil in US dollars, which has anchored global dollar demand for half a century), ...`
- **Wikilinks stay.** Even when introducing on first mention, wrap the entity in `[[wikilinks]]` so the reader can click through if reading inside Obsidian / Quartz. The gloss sits next to the wikilink.
- **Calibrate to "smart generalist."** Assume the reader knows: macro headline figures (GDP, CPI, oil prices roughly), G20 heads of state, major central banks, what a quarter is, what an IPO is, basic geopolitics (NATO exists, China and the US compete, etc.). Do not gloss those.

### Length by depth flag

| Flag | Words (body) | Use case |
|---|---|---|
| `--depth short` | 400-700 | Quick orientation — single-paragraph lede + condensed context. |
| `--depth standard` (default) | 800-1300 | Normal explainer. All five sections, each at appropriate length. |
| `--depth long` | 1500-2500 | Full primer when the topic spans many actors and threads (e.g., a multi-year geopolitical arc). Adds extended Context section. |

### Voice contrast (illustrative)

`/report` voice (analytical synthesis):
> The UAE leaves OPEC at the peak of its capacity arc, not the trough — distinct from every prior exit (Indonesia, Ecuador, Qatar, Angola). The "shock absorber" leaves with the cartel's discipline mechanism rather than its decline.

`/explain` voice (briefing):
> The United Arab Emirates — a Gulf federation of seven emirates, of which Abu Dhabi sits on most of the country's oil — announced on April 28, 2026 that it will leave OPEC, the cartel of major oil-producing countries it has belonged to since 1967. The exit takes effect May 1. OPEC, founded in 1960 by Saudi Arabia, Iran, Iraq, Venezuela, and Kuwait, coordinates production quotas to manage global oil prices; the UAE was its third-largest member. The move ends roughly six decades of membership, though the immediate market impact is muted because the [[2026 Strait of Hormuz crisis]] — Iran's two-month closure of the Gulf's main oil chokepoint, which began in late February — has already pushed crude into a tight supply regime where one producer's quota status barely registers.

Same facts. Different audience.

---

## Phase 3 — Output format

Path: `investing/Reports/YYYY-MM-DD-explain-<topic-slug>.md`

Confirm date: `date +%Y-%m-%d`. Use that exact date. If a same-day same-topic explainer exists, append `-2`, `-3`, etc.

```markdown
---
name: <Topic> — explainer
type: explainer
topic: "[[<Primary Note>]]"
depth: <short|standard|long>
generated: YYYY-MM-DD HH:MM
sources_read: N
tags: [report, explainer]
---

# <Topic> — what's going on, in plain terms

[Lede paragraph — what happened, when.]

## Who's involved

[Cast paragraph(s). One-sentence intro on first mention for each named actor, then the name alone after.]

## Why it matters

[Stakes in concrete terms. Barrels, dollars, alliances, policy.]

## The context

[2-4 paragraphs of background that makes today's event intelligible. This is where the work lives.]

## What's contested and what to watch

[Open questions, diagnostic markers.]

## Where to read deeper in the vault

- [[Primary Note]] — the full event note
- [[Concept Note]] — the framework
- [[Actor Note]] — the institution / person
- [Geopolitics: X](obsidian://...) — the other-vault lens

## Gaps

- [[Missing Entity]] — referenced but no note exists
- [[Stub Note]] — only N lines of substance
```

**Final checks before save:**
- Every named actor introduced with a role gloss on first mention
- Every domain concept glossed inline
- All `[[wikilinks]]` preserved (printable rule)
- No bold in body
- No editorial frame (bull/bear, "market isn't pricing")
- Linear narrative — no central-insight / synthesis structure

---

## Phase 4 — Daily note + chat output

1. **Log to today's daily note** under a `## Reports` section (create if missing):
   ```markdown
   ## Reports

   - 14:23 — `/explain <Topic>` → `[[YYYY-MM-DD-explain-<topic-slug>]]` (depth: <flag>, N sources)
   ```

2. **Echo the explainer body to chat** so the user reads it without opening the file. Mention the saved path in one line at the end:
   > Saved to `investing/Reports/YYYY-MM-DD-explain-<topic-slug>.md`. Disposable — re-run anytime.

---

## Phase 5 — Post-explainer vault audit

The first-mention discipline doubles as a vault audit. Every concept that required an inline gloss is a vault gap signal — a recurring analytical concept the vault is using as shorthand without a definitional anchor.

After completing the explainer:

1. Scan the explainer body for inline glosses (parenthetical or em-dash-style explanations of concepts/actors/events).
2. For each glossed term, run a vault grep to count mentions across notes:
   ```bash
   grep -rli "<term>" investing/ | wc -l
   ```
   High-mention-count terms (5+ notes) without a dedicated note are strong gap candidates.
3. Distinguish: terms used as *vocabulary* (shorthand for a structural concept) vs. terms used as *labels* (incidental name-drops). Vocabulary terms are gap candidates; labels are not.
4. Surface findings to the user with mention counts as evidence, ranked by structural importance, before creating anything. Don't silently create notes — present the audit, let the user pick which to fill.

Worked example (UAE OPEC exit, 2026-04-29): five gaps surfaced by inline glosses — `Shock absorber`, `2014-2016 Saudi oil price war`, `Marc Lynch`, `Baker Institute`, `2025 Saudi-UAE Yemen rupture` — plus one cascading stub (`Jim Krane`). `Shock absorber` appeared in 10 notes without a concept-note anchor; that's the kind of signal worth filling.

The same audit can be applied to `/report` runs, though less mechanically — `/report` doesn't enforce first-mention discipline, so the glosses don't surface as cleanly.

---

## Reports/ folder hygiene

- Same as `/report`. Saved to `investing/Reports/`. Tags `[report, explainer]` so compliance scans can filter.
- Not entity notes. `check_note_compliance.py` should not run against them.
- Old explainers stay on disk; user clears manually when noisy.

---

## Failure modes to avoid

- **Insider voice creeping in.** "The exit-cascade dynamic is the load-bearing question" — that's `/report` voice. `/explain` would say "Whether other Gulf states follow the UAE out is the question that decides whether this is a one-off or the start of OPEC unwinding."
- **Skipping first-mention introductions.** If the reader meets `[[Suhail Al Mazrouei]]` without a role gloss, the skill failed.
- **Glossing terms a smart generalist already knows.** Don't define "GDP" or "OPEC" past first mention. Don't gloss "Trump" or "Xi" or "the Federal Reserve."
- **Importing analytical claims the vault doesn't already make.** This skill is read-only. If the source notes don't say "X is the structural story," the explainer doesn't either. Describe what the vault says, in plain terms; don't add new framings.
- **Vault-by-vault sections.** "Investing perspective:", "Geopolitics perspective:" — same anti-pattern as `/report`. Weave inline.
- **Dropping wikilinks.** `[[NVIDIA]]` stays as `[[NVIDIA]]` in the output. The repo printing rule applies.
- **Section dump masquerading as explainer.** If your output reads like a Wikipedia summary of the primary note, you skipped the synthesis-into-narrative step. The cast / context / matters / watch structure is the test — restructure if needed.
