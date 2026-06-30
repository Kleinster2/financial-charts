# Headless Scheduling — Running a Skill Unattended

How to promote an interactive Claude Code skill (e.g. `/daily-scan`) to an unattended job that runs on a schedule and survives session close. Reference implementation: the `FinancialCharts-Daily-Scan` Windows task → [scripts/daily_scan_task.bat](../scripts/daily_scan_task.bat). The hard lessons here were learned 2026-06-29 promoting `/daily-scan`; three real bugs were caught only by running it.

## Scheduling layers — pick the right one

| Layer | Mechanism | Survives session close? | Fires when Claude is closed? |
|---|---|---|---|
| Session cron (in-memory) | `CronCreate` (default), `/loop`, `ScheduleWakeup` | No | No |
| Session cron (durable) | `CronCreate --durable` → `.claude/scheduled_tasks.json` | Yes (reloads on restart) | No — still needs the REPL open/idle |
| OS scheduler | Windows Task Scheduler / cron launches headless Claude | Yes | Yes |
| Cloud routine | `/schedule` (server-side) | Yes | Yes (runs off your machine) |

Only the OS scheduler and cloud routines run when no Claude session is open. A `CronCreate` job — durable or not — only fires while a REPL is idle, so it is the wrong tool for "run every weekday at 7:15 whether or not I'm at the machine." The reference task uses Windows Task Scheduler.

## The two-stage wrapper (the core pattern)

Do not let the headless agent own a slow, blocking step. Split the job:

- Stage 1 — pre-warm. Run the slow, deterministic work synchronously as plain Python in the `.bat`. No agent, no judgment, just I/O.
- Stage 2 — agent. Invoke headless Claude with a flag that makes it skip the slow step (e.g. `--skip-update`) so it reads the fresh result and goes straight to the reasoning/output phases, synchronously.

```bat
cd /d C:\Users\klein\financial-charts
echo ==== %DATE% %TIME% ==== >> "%LOCALAPPDATA%\daily_scan_task.log"
REM stage 1: slow deterministic step, synchronous
python scripts\daily_scan.py --output "%LOCALAPPDATA%\daily_scan.json" >> "%LOCALAPPDATA%\daily_scan_task.log" 2>&1
REM stage 2: agent, with the slow step skipped
"C:\Users\klein\.local\bin\claude.exe" -p "/daily-scan -- ... use --skip-update; never run_in_background; do not commit/push; finish only after the briefing is written." --permission-mode bypassPermissions --disallowedTools "Bash(git commit:*)" "Bash(git push:*)" < nul >> "%LOCALAPPDATA%\daily_scan_task.log" 2>&1
```

## Headless invocation flags — what each does and why

| Flag | Why it is mandatory |
|---|---|
| `-p` / `--print` | Non-interactive, single-conversation run. No TTY. |
| `--permission-mode bypassPermissions` | `-p` has no terminal to answer a permission prompt, so every tool must be pre-authorized or the run dead-ends. |
| `--disallowedTools "Bash(git commit:*)" "Bash(git push:*)"` | Git guard. `bypassPermissions` also green-lights `git push`; a deny-list overrides bypass so the run can read git for context but never publishes. |
| `< nul` (cmd) / `< /dev/null` (sh) | Skip the stdin wait; the process has no pipe feeding it. |

The prompt must also forbid `run_in_background` and require the durable artifact be written before exit (see failure modes below).

## Three failure modes (all caught by live testing)

1. Auto-commit / push. With `bypassPermissions` the agent will "tidy" a dirty working tree by committing and pushing to `main` on its own. Guard with the `--disallowedTools` git deny-list (deny beats bypass). A hook that runs git would not be stopped this way — trace the actor first; here it was the agent, so the deny-list is the right lever.
2. Silent truncation. A `-p` session is never re-woken by a background-task notification the way the interactive REPL is. If the agent backgrounds a slow step ("I'll continue when it finishes"), the print session simply ends with no output. Forbid `run_in_background`.
3. Hang. Forbidding `run_in_background` alone backfires: denied the harness mechanism, the agent hand-rolls its own — a detached OS process plus a shell loop polling for a result — and can hang indefinitely (observed: 90 minutes, ~80 CPU-seconds, the classic blocked-not-working signature). The fix is structural: pre-warm the slow step in the wrapper (stage 1) so the agent never has a reason to background anything.

## Verify by artifact, not exit code

A headless run can exit 0 and produce nothing (failure mode 2 did exactly that). Assert on the deliverable:

- Did the durable artifact appear? (e.g. a `## Daily scan` section in `investing/Daily/YYYY-MM-DD.md`.)
- Did the git guard hold? (`HEAD` unchanged, `0/0` vs origin.)
- A blocked process shows almost no CPU growth over wall-clock — check `(Get-Process claude).CPU` against elapsed time, not just task state.

## Operational constraints

- Interactive logon required. The task runs only when the user is logged on: the skill shells out to `python` (the Microsoft Store alias resolves only in an interactive session) and `claude.exe` reads user-scoped auth/config under `C:\Users\klein\.claude`. Mirror the RP Holdings tasks: run as the user, `LogonType=Interactive`, `RunLevel=Limited`. It does not run on a locked, logged-off, or sleeping machine.
- Execution time limit. A fully synchronous scan is slow; set `ExecutionTimeLimit` generously (the reference task uses `PT2H`). The data refresh is the dominant cost — the [freshness-skip in `download_all_assets.py`](../download_all_assets.py) cut it 59→6 min, which is what makes the unattended run light.
- Log location. The wrapper appends stdout to `%LOCALAPPDATA%\daily_scan_task.log`; the durable copy is the daily note. In `-p` text mode the agent prints only at the end, so the log stays at the header until the run finishes.

## Registering the task (PowerShell)

```powershell
$action    = New-ScheduledTaskAction -Execute "C:\Users\klein\financial-charts\scripts\daily_scan_task.bat"
$trigger   = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday,Tuesday,Wednesday,Thursday,Friday -At 7:15AM
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited
$settings  = New-ScheduledTaskSettingsSet -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 2) `
             -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskName "FinancialCharts-Daily-Scan" -Action $action -Trigger $trigger `
             -Principal $principal -Settings $settings -Description "Headless /daily-scan" -Force
```

A one-time validation run: `Start-ScheduledTask -TaskName "FinancialCharts-Daily-Scan"`, then watch task state (`Running` → `Ready`), `LastTaskResult` (0 = clean), the artifact, and that `HEAD` did not move.

## See also

- [.claude/skills/daily-scan/SKILL.md](../.claude/skills/daily-scan/SKILL.md) — the "Scheduling" section carries the condensed version of this.
- Memory: `project_headless_skill_scheduling` (pointer to this doc).
