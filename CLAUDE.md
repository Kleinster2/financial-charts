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

See `investing/Meta/CLAUDE.md` for vault-specific guidelines.

### Before creating vault files

**Always check for existing files before batch creation:**

```bash
git -C "C:/Users/klein/financial-charts/investing" ls-files "Actors/*.md"
```

This prevents overwriting detailed notes with generic templates.
