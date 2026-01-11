# Claude Code Instructions

Project-specific instructions for Claude Code sessions.

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

- **Dashboard features**: `charting_sandbox/chart-dashboard.js`
- **Backend API**: `charting_app/app.py`
- **Unit tests**: `tests/unit/`
- **Smoke tests**: `tests/playwright/`

## Cache Busting

After modifying JS files, increment `?v=` in `charting_sandbox/index.html`.

## Obsidian Vault

The investing vault lives at `investing/` within this project.

**DEPRECATED**: The old "My Vault" at `C:\Users\klein\onedrive\pictures\documents\my vault` is deprecated. All vault work should use `investing/` in this repo.

See `investing/Meta/CLAUDE.md` for full vault guidelines. Key rules below:

### Philosophy

- **Atomic notes** — one idea per note, no mega-documents
- **Links over hierarchy** — structure via `[[wikilinks]]`, not folders
- **Daily notes as inbox** — capture first, extract atomic notes when mature
- **Numbers matter** — always capture hard data with sources

### Folder structure

| Folder | Purpose |
|--------|---------|
| Actors | Companies, orgs, individuals, geographies |
| Concepts | Ideas, dynamics, phenomena |
| Theses | Investment theses (Long/Short/Pairs) |
| Events | Discrete happenings |
| Daily | Daily notes (inbox) |
| Sectors | Sector overview hubs |
| Regions | Geographic hubs |

### Actor conventions

- **Non-investable actors are valid** — policy-makers, private companies, individuals, geographies
- **Private companies need cap tables** — investors, rounds, valuations
- **End notes with annotated `## Related`** — explain why each link matters

### Daily note structure

1. Market data (levels, moves)
2. News by topic
3. Thesis implications table (Thesis | Evidence | Direction)
4. Open threads checklist

### Before creating vault files

**CRITICAL: Always verify actors exist before proposing creation.**

```bash
cd /c/Users/klein/financial-charts/investing && git ls-files "Actors/*.md" | sed 's|.*/||; s|.md$||' | grep -iE "name1|name2"

```

**Use broad, partial patterns** — names may be stored differently:
```bash
# Use partial matches, tickers, abbreviations:
grep -iE "bank.*america|bofa|bac"    # Bank of America
grep -iE "servicenow|service.*now"   # ServiceNow
grep -iE "at&t|att|at.t"             # AT&T
```

Then explicitly state each result:
```
Honeywell  — NOT FOUND (safe to create)
NVIDIA     — EXISTS (do not create)
```

This is non-negotiable. The vault has 400+ actors with detailed research that must not be overwritten.
