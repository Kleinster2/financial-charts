@echo off
REM Daily autonomous market scan via the Claude Code /daily-scan skill.
REM Run by the "FinancialCharts-Daily-Scan" scheduled task on weekdays ~7:15 AM ET,
REM after "RP Holdings Tracker" (6:50) and "RP Holdings Import" (7:05) so the scan's
REM Phase 0 risk-parity composition import sees same-day holdings notes.
REM
REM Runs only when user 'klein' is logged on: the daily-scan skill shells out to
REM `python` (Microsoft Store alias) and claude.exe reads user-scoped auth/config
REM under C:\Users\klein\.claude -- both need an interactive logon session.
REM
REM Headless flags:
REM   -p                      print mode (non-interactive, single conversation).
REM   bypassPermissions       no TTY to answer a permission prompt, so every tool
REM                           must be pre-authorized or the run dead-ends.
REM   --disallowedTools git*  GIT GUARD. bypassPermissions would otherwise let the
REM                           agent commit and push the working tree to main on its
REM                           own (it did, once). Deny rules override bypass, so the
REM                           scan can read git for context but never publishes.
REM   < nul                   skip the stdin wait (no pipe feeding the process).
REM
REM Prompt forces a SYNCHRONOUS single pass: a -p session is never re-woken by a
REM background-task notification the way the interactive REPL is, so if the agent
REM backgrounds the slow market-data update it exits before producing the briefing.
REM The instruction forbids run_in_background and requires the briefing be written
REM before exit. The briefing text is captured in the log; the durable copy is the
REM daily note (investing/Daily/YYYY-MM-DD.md).
cd /d C:\Users\klein\financial-charts
echo ==== %DATE% %TIME% ==== >> "%LOCALAPPDATA%\daily_scan_task.log"
"C:\Users\klein\.local\bin\claude.exe" -p "/daily-scan -- Run this start-to-finish in ONE headless pass. Execute every step synchronously and wait for each to finish; do NOT use run_in_background for the market-data update or any other step (a non-interactive -p session cannot resume on a background-task notification). Do not commit or push to git; leave changes uncommitted for review. Finish only after the full briefing has been written to today's daily note." --permission-mode bypassPermissions --disallowedTools "Bash(git commit:*)" "Bash(git push:*)" < nul >> "%LOCALAPPDATA%\daily_scan_task.log" 2>&1
echo exit code: %ERRORLEVEL% >> "%LOCALAPPDATA%\daily_scan_task.log"
