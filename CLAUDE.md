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

## Pending Design Decisions

### Short interest charting integration

**Status:** Database and API complete, UI integration pending.

**Context:** Short interest data is stored in `short_interest` table (normalized: ticker + settlement_date) with API endpoints `/api/short-interest` and `/api/short-interest/latest`. Need to decide how to expose SI time series in the charting UI.

**Options:**
- **A) Synthetic tickers** — `AAPL_SI_PCT`, `AAPL_SI_DAYS`, etc. Most consistent with existing architecture.
- **B) Separate chart overlay** — New UI component to overlay SI on price charts.
- **C) Wide table** — Add to existing `/api/data` endpoint via wide-format table.

**Related files:**
- `scripts/update_short_interest.py` — fetcher (yfinance)
- `charting_app/app.py` — API endpoints
- `investing/Concepts/Short interest.md` — vault concept note

## Obsidian Vault

For vault work, run Claude from `investing/` directory to get vault-specific context.

**DEPRECATED**: The old "My Vault" at `C:\Users\klein\onedrive\pictures\documents\my vault` is deprecated. All vault work should use `investing/` in this repo.
