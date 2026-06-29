@echo off
REM Daily import of Risk Parity vault holdings composition into market_data.db.
REM Run by the "RP Holdings Import" scheduled task (run only when user is logged on,
REM so the Microsoft Store python alias resolves). Logs to %LOCALAPPDATA%.
cd /d C:\Users\klein\financial-charts
echo ==== %DATE% %TIME% ==== >> "%LOCALAPPDATA%\rp_holdings_import.log"
python scripts\import_rp_holdings.py >> "%LOCALAPPDATA%\rp_holdings_import.log" 2>&1
echo exit code: %ERRORLEVEL% >> "%LOCALAPPDATA%\rp_holdings_import.log"
