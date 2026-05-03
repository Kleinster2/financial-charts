# Watchdog for Flask (5000) and Quartz static server (8080).
# Idempotent: starts whichever server isn't currently listening.
# Used by two Task Scheduler entries: one OnLogon, one every 5 minutes.

$ErrorActionPreference = "Continue"

$Pythonw = "C:\Users\klein\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\pythonw.exe"
$LogDir  = "$env:USERPROFILE\financial-charts\logs"
$LogFile = "$LogDir\watchdog.log"

if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
}

function Write-Log {
    param([string]$msg)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $LogFile -Value "$ts $msg"
}

function Test-Port {
    param([int]$port)
    $listeners = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
    if (-not $listeners) { return $false }
    $alive = $listeners | ForEach-Object { Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue } | Where-Object { $_ }
    [bool]$alive
}

function Start-ServerIfDown {
    param(
        [int]$port,
        [string]$name,
        [string]$workDir,
        [string[]]$pyArgs,
        [string]$logTag
    )
    if (Test-Port $port) { return }
    Write-Log "Starting $name (port $port)..."
    $stdout = "$LogDir\$logTag.out.log"
    $stderr = "$LogDir\$logTag.err.log"
    try {
        Start-Process -FilePath $Pythonw -ArgumentList $pyArgs `
            -WorkingDirectory $workDir -WindowStyle Hidden `
            -RedirectStandardOutput $stdout -RedirectStandardError $stderr
    } catch {
        Write-Log "FAILED to start $name : $_"
    }
}

Start-ServerIfDown -port 5000 -name "Flask charting" -logTag "flask" `
    -workDir "C:\Users\klein\financial-charts" `
    -pyArgs @("C:\Users\klein\financial-charts\charting_app\app.py")

Start-ServerIfDown -port 8080 -name "Quartz static" -logTag "quartz" `
    -workDir "C:\Users\klein\quartz-investing\public" `
    -pyArgs @("C:\Users\klein\quartz-investing\serve_static.py", "8080")
