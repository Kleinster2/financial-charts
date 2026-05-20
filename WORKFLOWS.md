# Workflows

This repo is the **workflow hub** for cross-vault research. The codebase began as a charting/markets application and has grown into the home for the slash-command skills that orchestrate vault work across `investing/`, `geopolitics/`, `Brazil/`, `history/`, `technologies/`, and siblings.

**Why workflows live here even though outputs span many vaults**: workflows are colocated with each other (they delegate and reference each other), with their data inputs (e.g. `docs/newsletter-sources.md`), and with the compliance hooks that gate every vault edit (`scripts/check_before_create.py`, `scripts/check_note_compliance.py`, daily-note logging). Splitting them across vault repos would shatter that integration. The repo name is historical — read it as *vault research hub with a charting subsystem*, not *charting tool with a vault attached*.

## Slash-command skills

Definitions live in `.claude/skills/<name>/SKILL.md`. The cross-runtime mirrors live in `.agents/skills/` (Codex) and `~/clawd/skills/` (OpenClaw) — see "Skill parity" below.

| Skill | Purpose | Primary vault(s) |
|---|---|---|
| `/daily-scan` | Daily market scan: sigma movers, ticker audits, IPO debuts, analyst watchlist, earnings calendar, pre-market briefing | investing |
| `/substacks` | Sweep ~67 tracked newsletter/Substack sources for new posts; delegate per-post ingestion | investing, geopolitics, technologies, history (varies by post) |
| `/news <source>` | Article ingestion from a named source (Bloomberg, Reuters, FT, WSJ) with downstream-impact check | varies by article |
| `/ingest` | Single-source ingestion (interview, article, filing, screenshots) — handles entity sweep, image routing, note creation | varies by source |
| `/deepdive <entity>` | Comprehensive entity research and note creation for companies, people, concepts, countries, products | varies by entity |
| `/earnings <ticker>` | Earnings ingestion: DB check, data insert, chart regen, actor + daily note update | investing |
| `/replicate <ticker>` | ETF/fund replication: proxy mapping, synthetic indices, charts, vault-note update | investing |
| `/report <topic>` | Cross-vault topic synthesis — saves narrative brief to `investing/Reports/` | investing (read-only across siblings) |
| `/explain <topic>` | Plain-language briefing on a vault topic with first-mention introductions | investing (read-only across siblings) |
| `/story [date]` | Daily "what is the story" report from the daily note + notes touched that session | investing |
| `/newsletter` | EOD market brief in analytical voice; reads daily note + session-edited notes | investing |
| `/rebuild-quartz-now` | Trigger immediate Quartz site rebuild with atomic swap (local viewer) | none — viewer-only |

## Architecture

```
.claude/skills/                 Claude Code skill definitions (canonical source-of-truth)
.agents/skills/                 Codex mirror (synced via scripts/promote_shared_skill.py)
~/clawd/skills/                 OpenClaw mirror (synced via promote helper, env override)

skills/shared-workflows.json    Registry of workflow skills that must be parity-mirrored
scripts/check_skill_parity.py   Verifies all three runtimes are byte-aligned
scripts/promote_shared_skill.py Canonical update path: edit one runtime, promote to the others

docs/newsletter-sources.md      Data input for /substacks (mirrored at ~/clawd/TOOLS.md)
docs/research-workflow.md       Cross-cutting research rules
docs/cross-vault-rules.md       Cross-vault gates and obsidian:// URI format
docs/note-checklist.md          Per-edit compliance checklist
```

## Skill parity

Workflow skills in `skills/shared-workflows.json` must stay byte-aligned across Claude / Codex / OpenClaw runtimes — they're the same code that should behave identically regardless of which runtime invokes them.

**Update path**: edit any one runtime's `SKILL.md`, then:

```bash
python scripts/promote_shared_skill.py <skill> --from claude    # or codex / openclaw
python scripts/check_skill_parity.py --strict                    # verify
```

A pre-commit hook runs `npm run test:consistency` for consistency-sensitive edits, including shared workflow skill parity, note-compliance regressions, and the market-reaction peer sweep. See `docs/skill-parity.md` for details.

## Vault outputs

Workflow skills can write to any vault under `~/obsidian/` or to `investing/` in this repo. Cross-vault output uses the `obsidian://open?vault=NAME&file=PATH` URI format from `docs/cross-vault-rules.md` — never bare wikilinks across vaults (each vault's link resolver only sees its own notes).

When a workflow produces outputs in multiple vaults, the **investing daily note** (`investing/Daily/YYYY-MM-DD.md`) is the canonical activity log — sibling-vault edits get logged here under a `Cross-vault:` section so the work is recoverable from a single starting point.

## See also

- `CLAUDE.md` — project rules, hard gates, repo conventions
- `docs/vault-note-guide.md` — actor/securities split, synopsis voice, concept structure
- `docs/chart-api.md` — chart generation, naming conventions, embed rules
- `README.md` — application-level architecture (Flask backend, charting dashboard, tests)
