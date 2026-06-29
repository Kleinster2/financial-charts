@echo off
REM Daily fetch of risk-parity ETF holdings for the auto-fetch funds, writing dated
REM tracking notes into the Risk Parity vault. Run by the "RP Holdings Tracker"
REM scheduled task ~6:50 AM, 15 min before the 7:05 "RP Holdings Import" task that
REM loads these notes into market_data.db.
REM
REM Only the 7 HTTP-fetchable funds are pulled here. The 6 Cloudflare-gated funds
REM (NTSX / NTSI / NTSE / GDE / SWAN / TAIL) need a manual CSV download + re-run of
REM fetch_holdings.py and cannot be automated.
echo ==== %DATE% %TIME% ==== >> "%LOCALAPPDATA%\rp_holdings_tracker.log"
python "C:\Users\klein\obsidian\risk-parity\10 - Portfolio Tracking\_scripts\fetch_holdings.py" RPAR UPAR ALLW AOR DBMF KMLM CTA >> "%LOCALAPPDATA%\rp_holdings_tracker.log" 2>&1
echo exit code: %ERRORLEVEL% >> "%LOCALAPPDATA%\rp_holdings_tracker.log"
