# Claude Code Instructions

This project is an integrated system: **database → charts → vault**.

- **Database** stores raw data (prices, financials, short interest)
- **Charts** visualize that data as rich expressions
- **Vault** (Obsidian notes at `investing/`) provides meaning, narrative, and theses

They are not separate concerns—they are one system.

---

## Git Workflow

**Main branch is protected** - all changes require a PR with passing CI.

### Making Changes

1. Run tests before committing:
   ```bash
   npm run test:unit      # 109 unit tests
   npm run test:smoke     # 6 Playwright tests
   ```

2. Create a feature branch and PR (never push directly to main):
   ```bash
   git checkout -b feature-name
   git add <files>
   git commit -m "Description"
   git push -u origin feature-name
   ```

3. Create PR using gh CLI:
   ```bash
   /c/Users/klein/Downloads/gh_2.80.0_windows_amd64/bin/gh.exe pr create --title "Title" --body "Description"
   ```

4. After PR is approved/merged:
   ```bash
   /c/Users/klein/Downloads/gh_2.80.0_windows_amd64/bin/gh.exe pr merge <number> --merge --delete-branch
   git checkout main
   git pull
   git fetch --prune
   ```

5. Clean stale local branches:
   ```bash
   git branch | grep -v main | xargs git branch -D
   ```

## Tools

- **gh CLI**: `/c/Users/klein/Downloads/gh_2.80.0_windows_amd64/bin/gh.exe`
- **Playwright**: `npx playwright install chromium` (first-time setup)

## Key Locations

### App

- **Dashboard features**: `charting_sandbox/chart-dashboard.js`
- **Backend API**: `charting_app/app.py`
- **Unit tests**: `tests/unit/`
- **Smoke tests**: `tests/playwright/`

### Vault

- **Vault root**: `investing/`
- **Actors**: `investing/Actors/` (companies, orgs, people, geographies)
- **Concepts**: `investing/Concepts/` (ideas, dynamics, phenomena)
- **Events**: `investing/Events/` (discrete happenings)
- **Theses**: `investing/Theses/` (investment theses)
- **Daily notes**: `investing/Daily/` (inbox, changelog)
- **Sectors**: `investing/Sectors/` (industry hubs)

**DEPRECATED**: The old "My Vault" at `C:\Users\klein\onedrive\pictures\documents\my vault` is deprecated.

## Cache Busting

After modifying JS files, increment `?v=` in `charting_sandbox/index.html`.

## Generating Charts for the Vault

**ALWAYS use the charting app API. NEVER use matplotlib or other tools.**

### Headless export via API (preferred)

```bash
# Start the app
cd /c/Users/klein/financial-charts && python charting_app/app.py

# Single ticker
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&start=2020-01-01" \
  -o investing/attachments/aapl-price-chart.png

# Comparison (normalized)
curl "http://localhost:5000/api/chart/lw?tickers=AAPL,QQQ&start=2020-01-01&normalize=true" \
  -o investing/attachments/aapl-vs-qqq.png

# Fundamentals
curl "http://localhost:5000/api/chart/lw?tickers=AAPL&metrics=revenue" \
  -o investing/attachments/aapl-revenue.png
```

**API parameters:** `tickers` (required), `start`, `end`, `title`, `width` (1200), `height` (600), `show_title` (true), `normalize` (false), `metrics` (revenue, netincome, eps, fcf, operatingincome, ebitda, grossprofit)

**Naming:** `aapl-price-chart.png`, `tsmc-vs-samsung-foundry.png`, `nvda-2024-rally.png`

## Pending Design Decisions

### Short interest charting integration

**Status:** Database and API complete, UI integration pending.

**Options:**
- **A) Synthetic tickers** — `AAPL_SI_PCT`, `AAPL_SI_DAYS`, etc.
- **B) Separate chart overlay** — New UI component
- **C) Wide table** — Add to `/api/data` endpoint

---

# Vault Guidelines

## Philosophy

- **Atomic notes** — one idea per note, no mega-documents
- **Self-contained** — each note tells its complete story; links are for depth, not basic comprehension
- **Links over hierarchy** — structure emerges from `[[connections]]`, not folders
- **Organic at the bottom, deliberate at the top** — actors/concepts grow organically; sector hubs are deliberate scaffolding
- **Daily notes as inbox** — capture first, extract atomic notes when ideas mature

## Self-contained notes

**A reader should understand the full story without clicking any links.**

| Wrong | Right |
|-------|-------|
| "The $5B debt came from [[Saks-Neiman merger]]" | "In late 2024, Baker orchestrated a $2.7B acquisition of Neiman that loaded $5B in debt..." then link for details |
| "[[Richard Baker]] was replaced as CEO" | "Richard Baker—real estate investor who built Saks through acquisitions—was replaced as CEO" then link for history |

**Repetition is acceptable** when needed for comprehension. Each note should stand alone.

## Numbers matter

**Never overlook hard data.** Capture financial metrics, operational data, comparisons, source and date.

**Bad:** "TSMC's US fabs have lower margins"
**Good:** "Taiwan 62% gross margin vs US 8%, depreciation +386%, labor +100% (SemiAnalysis, Nov 2025)"

## Charts and images

When the user shares images: (1) confirm you see them, (2) extract key data points, (3) add data to relevant notes.

**Saving images:** Find in `~/.claude/image-cache/`, copy to `investing/attachments/`, embed with `![[name.png]]`.

## Author framing matters

Capture the thesis, not just data. Note hedging language. Don't assume causation. Capture the author's interpretation.

## Dating investment calls

**Always include dates on positioning.** Calls go stale. Include date in section header, source attribution, note if position changed.

## When creating notes

- **Always do deep research** before creating — web search, multiple sources, hard data
- Link liberally with `[[wikilinks]]`
- **No thin stubs** — if no time to research, add to daily note instead

See [[Note structures]] for actor requirements and templates.

### "What makes X, X" analysis

Go beyond facts to explain why something works: flywheel, moats, structural advantage, the math.

## When editing existing notes

**Every edit is an opportunity to rebuild.** Check for: thin stubs, missing financials/cap tables, outdated data, no Related section. Make the requested edit first, then assess quality gaps.

## Processing new information

**Every piece of news needs an atomic home — daily notes are never the only location.**

1. **Check existing notes first** — search vault before web
2. **Find the right home** — actors taking actions, not catch-all concepts
3. **Regional actors stay high-level** — specific news goes on specific actors
4. **Always update daily notes** — use event date, not article date
5. **Check for events** — M&A, bankruptcy, IPO → create Event note

See [[Note structures]] for event criteria and templates.

## Conventions

See [[Thesis conventions]] for thesis naming. See [[Taxonomy discussion]] for hashtag structure.

## Daily note structure

See [[Note structures]] for the standard daily note template. **Vault activity is mandatory** — journal all note creation/modification.

## Research workflow

1. **Web search** for major news
2. **X/Twitter lists** for commentary (Chips & Semiconductors, AI Infrastructure, SemiAnalysis)
3. Add findings to daily note first, extract to actor/concept notes if substantial

## Key actors to track

Foundry: [[TSMC]], [[Samsung]], [[Intel Foundry Services]], [[GlobalFoundries]]
Memory: [[SK Hynix]], [[Micron]], [[Samsung]]
GPU/AI: [[NVIDIA]], [[AMD]], [[Broadcom]]
AI Labs: [[OpenAI]], [[Anthropic]], [[xAI]], [[Google DeepMind]]
Equipment: [[ASML]], [[Applied Materials]], [[Lam Research]], [[Tokyo Electron]]

## Note decisions

- **Major standalone topic** → new atomic note
- **Update to existing actor/concept** → add section
- **Incremental news** → daily note only

### Frame notes for intrinsic value

Don't frame around what triggered creation. Notes should explain why the topic matters on its own terms.

### Check for intermediate levels

Before linking specific → general, check for intermediates. See [[Linking and hierarchy]] for patterns.

## Events vs Actor sections

**Prefer Event notes for corporate events.** Events are atomic — specific time, specific actors, own narrative.

See [[Note structures]] for when to create events and the event template.

## Folder and hierarchy

See [[Linking and hierarchy]] for folder structure, Concept vs Sector criteria, and Sub-sector/Sister Concept patterns.

## Before creating files

### CRITICAL: Always verify before creating

**Every time you propose creating actors, you MUST first check if they already exist.**

```bash
cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md" | sed 's|.*/||; s|\.md$||' | grep -iE "name1|name2|name3"
```

Use broad patterns (abbreviations, tickers, variants). Explicitly state result for each:
```
Honeywell  — NOT FOUND (safe to create)
NVIDIA     — EXISTS (do not create)
```

**WARNING:** Do NOT use `xargs basename -a` — corrupts filenames with spaces.

### After creating/updating notes

1. **Journal** — update today's daily note Vault activity
2. **Link mentions** — search vault, convert to `[[wikilinks]]`
3. **Add backlinks** — update Related sections of connected notes

## Actor conventions

### Actors don't need to be investable

Track policy-makers, private companies, geographies, individuals — anyone affecting investment outcomes.

### Regional actors stay high-level

Geographic actors are scaffolding, not repositories. Specific news → specific actors. Regional notes link to those actors.

### Concepts don't need theses

Concepts capture knowledge, not just trade ideas. If you'd reference it from multiple notes, it deserves a concept note.

### Financials and cap tables

- **Public companies**: Historical financials (see [[Financials templates]])
- **Private companies**: Cap table with investors, rounds, valuations
- **Banks**: Use bank-specific metrics (see [[Financials templates]])

## Finding links

See [[Linking and hierarchy]] for systematic approach: check what exists, steal from peers, category checklists, reverse lookup, concept connections.

## Related section convention

See [[Note structures]] for format and annotation types.
