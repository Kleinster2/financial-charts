---
name: rebuild-quartz-now
description: "Trigger an immediate Quartz site rebuild with atomic swap so vault edits made this session show up in the local viewer (localhost:8080) without waiting for the nightly 3 AM job. Use when the user invokes /rebuild-quartz-now, asks 'rebuild quartz', 'refresh the site', or 'make today's notes searchable in Quartz'. Skip if the user is asking about anything else — including starting the static server (the watchdog handles that)."
---

# Rebuild Quartz now

Run the rebuild script. It builds to `public-next/` and atomic-swaps it into `public/` only on success — if the build fails, the live site is untouched.

## Steps

1. Confirm there is no rebuild already in flight:
   ```bash
   powershell -Command "Test-Path '$env:USERPROFILE\financial-charts\logs\quartz-rebuild.lock'"
   ```
   - `True` → tell the user a rebuild is already running (likely the nightly job or a prior manual fire); show the lockfile age. Don't start a second one.
   - `False` → proceed.

2. Fire the script in the background and report the started state. The build typically takes 30-40 minutes (full re-parse of ~6,300 markdown files + emit). `serve_static.py` keeps serving the previous `public/` throughout; users see a brief swap at the end.

   ```bash
   powershell -Command "Start-Process -FilePath 'powershell.exe' -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-File','C:\Users\klein\financial-charts\scripts\rebuild_quartz.ps1' -WindowStyle Hidden"
   ```

3. Tell the user the rebuild started and how to monitor it:
   ```bash
   Get-Content "$env:USERPROFILE\financial-charts\logs\quartz-rebuild.log" -Tail 5
   ```

## What this skill does NOT do

- Does not start `serve_static.py` — the FinancialCharts-Watchdog scheduled task handles that every 5 minutes.
- Does not run `--serve` mode (continuous Node + esbuild watcher) — that path was tested and rejected: 38-minute cold start, 1-minute hot-reload latency in practice.
- Does not modify the nightly 3 AM scheduled rebuild — that is independent and remains armed.

## Failure modes to watch for

- **`logs/quartz-build.err.log`** has the build's stderr if `npx quartz build` failed. Common causes: a malformed YAML frontmatter in a new note, a Windows-illegal character in an alias.
- **`public-next/` left behind** after a crash means the lockfile may also be stale. The script auto-clears stale (>2h) lockfiles on next run; you can also `Remove-Item` both manually.
- **`public-old/` left behind** is harmless but takes disk space — gets cleaned on the next successful rebuild.

## Reference

- Script: `scripts/rebuild_quartz.ps1`
- Nightly task: `FinancialCharts-Quartz-Rebuild` (3 AM daily)
- Static server task: `FinancialCharts-Watchdog` (every 5 min)
- Docs: `docs/quartz-viewer.md` and `docs/ops/server-watchdog.md`
