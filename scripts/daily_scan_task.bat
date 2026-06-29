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
REM TWO-STAGE DESIGN (learned from a hung headless run, 2026-06-29):
REM   Stage 1 -- pre-warm. Run the slow market-data update + sigma screen SYNCHRONOUSLY
REM     here as plain python. This is deterministic and needs no agent. Doing it in the
REM     wrapper is the whole point: when the agent owned this step it backgrounded
REM     update_market_data.py and then hung forever polling for the result, because a
REM     -p print session is never re-woken by a background-task notification.
REM   Stage 2 -- agent. Invoke headless Claude with --skip-update so it does NOT re-run
REM     the slow update; it reads fresh data and goes straight to the news / earnings /
REM     analyst / briefing phases, synchronously.
REM
REM Guards on the agent call:
REM   bypassPermissions       no TTY to answer a permission prompt (pre-authorize all).
REM   --disallowedTools git*  deny commit/push (deny overrides bypass) so the unattended
REM                           run never publishes; it leaves changes uncommitted for review.
REM   < nul                   skip the stdin wait.
REM The briefing text is captured in the log; the durable copy is the daily note.
cd /d C:\Users\klein\financial-charts
echo ==== %DATE% %TIME% ==== >> "%LOCALAPPDATA%\daily_scan_task.log"
echo ---- stage 1: pre-warm daily_scan.py (synchronous data update + movers) ---- >> "%LOCALAPPDATA%\daily_scan_task.log"
python scripts\daily_scan.py --output "%LOCALAPPDATA%\daily_scan.json" >> "%LOCALAPPDATA%\daily_scan_task.log" 2>&1
echo pre-warm exit: %ERRORLEVEL% >> "%LOCALAPPDATA%\daily_scan_task.log"
echo ---- stage 2: headless agent (--skip-update, synchronous) ---- >> "%LOCALAPPDATA%\daily_scan_task.log"
"C:\Users\klein\.local\bin\claude.exe" -p "/daily-scan -- Market data was already refreshed by this wrapper before you started, so do NOT run the full market-data update again: when you run daily_scan.py, pass --skip-update. Never use run_in_background for any step; run everything synchronously and wait inline. Do not commit or push to git. Finish only after the briefing has been written to today's daily note." --permission-mode bypassPermissions --disallowedTools "Bash(git commit:*)" "Bash(git push:*)" < nul >> "%LOCALAPPDATA%\daily_scan_task.log" 2>&1
echo exit code: %ERRORLEVEL% >> "%LOCALAPPDATA%\daily_scan_task.log"
