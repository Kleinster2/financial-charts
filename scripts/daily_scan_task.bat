@echo off
REM Daily autonomous market scan via the Claude Code /daily-scan skill.
REM Run by the "FinancialCharts-Daily-Scan" scheduled task on weekdays ~7:15 AM ET,
REM after "RP Holdings Tracker" (6:50) and "RP Holdings Import" (7:05) so the scan's
REM Phase 0 risk-parity composition import sees same-day holdings notes.
REM
REM Runs only when user 'klein' is logged on: the daily-scan skill shells out to
REM `python` (Microsoft Store alias) and claude.exe reads user-scoped auth/config
REM under C:\Users\klein\.claude -- both need an interactive logon session.
REM Headless flags: -p print mode; bypassPermissions so no permission prompt blocks
REM the run (no TTY to answer one); stdin redirected from nul so claude does not
REM wait on a non-existent pipe. The briefing is captured here for debugging; the
REM durable copy is the daily note (investing/Daily/YYYY-MM-DD.md).
cd /d C:\Users\klein\financial-charts
echo ==== %DATE% %TIME% ==== >> "%LOCALAPPDATA%\daily_scan_task.log"
"C:\Users\klein\.local\bin\claude.exe" -p "/daily-scan" --permission-mode bypassPermissions < nul >> "%LOCALAPPDATA%\daily_scan_task.log" 2>&1
echo exit code: %ERRORLEVEL% >> "%LOCALAPPDATA%\daily_scan_task.log"
