# PowerShell script to add ORIX data and generate comparison chart
# Run this from the financial-charts directory or right-click and select "Run with PowerShell"

$ErrorActionPreference = "Stop"

# Configuration
$ProjectDir = "C:\Users\klein\financial-charts"
$PythonExe = "$ProjectDir\.venv\Scripts\python.exe"
$OutputPath = "$ProjectDir\investing\attachments\orix-vs-peers.png"
$ServerUrl = "http://localhost:5000"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ORIX Corporation Data Download and Chart Generation" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Download ORIX data
Write-Host "Step 1: Downloading ORIX (IX) data..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

Set-Location $ProjectDir
& $PythonExe download_single_ticker.py IX

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to download IX data" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Data download completed successfully" -ForegroundColor Green
Write-Host ""

# Step 2: Start Flask server
Write-Host "Step 2: Starting Flask API server..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

$ServerJob = Start-Job -ScriptBlock {
    param($ProjectDir, $PythonExe)
    Set-Location $ProjectDir
    & $PythonExe charting_app/app.py
} -ArgumentList $ProjectDir, $PythonExe

Write-Host "Server started in background job (ID: $($ServerJob.Id))"
Write-Host "Waiting for server to initialize..."
Start-Sleep -Seconds 5

# Check if server is running
try {
    $Response = Invoke-WebRequest -Uri "$ServerUrl/api/health" -UseBasicParsing -TimeoutSec 5
    Write-Host "✓ Server is responding (Status: $($Response.StatusCode))" -ForegroundColor Green
} catch {
    Write-Host "WARNING: Server health check failed, but continuing..." -ForegroundColor Yellow
}

Write-Host ""

# Step 3: Generate chart
Write-Host "Step 3: Generating chart..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

# Create output directory if needed
$OutputDir = Split-Path $OutputPath -Parent
if (!(Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
}

$ChartUrl = "$ServerUrl/api/chart/lw?tickers=IX,SMFG,MFG,MUFG&normalize=true&primary=IX&start=2020-01-01&show_title=false"

try {
    Invoke-WebRequest -Uri $ChartUrl -OutFile $OutputPath -TimeoutSec 60
    Write-Host "✓ Chart saved to: $OutputPath" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to download chart: $_" -ForegroundColor Red
    
    # Try alternative with curl
    Write-Host "Trying with curl..." -ForegroundColor Yellow
    curl $ChartUrl -o $OutputPath
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: curl also failed" -ForegroundColor Red
    }
}

Write-Host ""

# Step 4: Verification
Write-Host "Step 4: Verification" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

if (Test-Path $OutputPath) {
    $FileSize = (Get-Item $OutputPath).Length
    if ($FileSize -gt 0) {
        Write-Host "✓ SUCCESS: Chart file created" -ForegroundColor Green
        Write-Host "  Path: $OutputPath"
        Write-Host "  Size: $([math]::Round($FileSize / 1KB, 2)) KB ($FileSize bytes)"
    } else {
        Write-Host "✗ ERROR: File exists but is empty (0 bytes)" -ForegroundColor Red
    }
} else {
    Write-Host "✗ ERROR: File not found at $OutputPath" -ForegroundColor Red
}

Write-Host ""

# Cleanup: Stop server
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Cleanup: Stopping Flask server..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Stop-Job $ServerJob -ErrorAction SilentlyContinue
Remove-Job $ServerJob -ErrorAction SilentlyContinue
Write-Host "✓ Server stopped" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "ALL TASKS COMPLETED" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Chart saved to: $OutputPath" -ForegroundColor Yellow

Pause
