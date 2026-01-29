@echo off
REM Batch script to add ORIX data and generate comparison chart
REM Run this from the financial-charts directory

echo ========================================
echo Step 1: Downloading ORIX (IX) data
echo ========================================
cd C:\Users\klein\financial-charts
.venv\Scripts\python.exe download_single_ticker.py IX
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to download IX data
    exit /b 1
)
echo.

echo ========================================
echo Step 2: Starting Flask API server
echo ========================================
echo Starting server in background...
start "Flask Server" cmd /c "cd C:\Users\klein\financial-charts && .venv\Scripts\python.exe charting_app\app.py"
echo Waiting for server to start...
timeout /t 5 /nobreak > nul
echo.

echo ========================================
echo Step 3: Generating chart
echo ========================================
REM Create attachments directory if it doesn't exist
if not exist "C:\Users\klein\financial-charts\investing\attachments" (
    mkdir "C:\Users\klein\financial-charts\investing\attachments"
)

REM Download chart using PowerShell
powershell -Command "Invoke-WebRequest -Uri 'http://localhost:5000/api/chart/lw?tickers=IX,SMFG,MFG,MUFG&normalize=true&primary=IX&start=2020-01-01&show_title=false' -OutFile 'C:\Users\klein\financial-charts\investing\attachments\orix-vs-peers.png'"

if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to generate chart
    echo Trying alternative method with curl...
    curl "http://localhost:5000/api/chart/lw?tickers=IX,SMFG,MFG,MUFG&normalize=true&primary=IX&start=2020-01-01&show_title=false" -o "C:\Users\klein\financial-charts\investing\attachments\orix-vs-peers.png"
)
echo.

echo ========================================
echo Step 4: Verification
echo ========================================
if exist "C:\Users\klein\financial-charts\investing\attachments\orix-vs-peers.png" (
    for %%I in ("C:\Users\klein\financial-charts\investing\attachments\orix-vs-peers.png") do (
        echo SUCCESS: Chart created at: C:\Users\klein\financial-charts\investing\attachments\orix-vs-peers.png
        echo File size: %%~zI bytes
    )
) else (
    echo ERROR: Chart file was not created
)
echo.

echo ========================================
echo Summary
echo ========================================
echo Tasks completed. The Flask server is still running.
echo To stop the server, close the 'Flask Server' window or press Ctrl+C in that window.
echo.
pause
