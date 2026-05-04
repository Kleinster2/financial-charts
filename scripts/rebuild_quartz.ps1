# Rebuild Quartz public/ with atomic swap.
#
# Builds to public-next/ alongside public/, then renames atomically so
# serve_static.py never sees a partial directory. On build failure, public/
# is left untouched.
#
# Run modes:
#   - Scheduled task: fires daily at 3 AM (FinancialCharts-Quartz-Rebuild).
#   - Manual: invoke directly when same-session freshness is needed.
#
# Idempotent under concurrency via a lockfile in logs/.

$ErrorActionPreference = "Stop"

$QuartzDir   = "C:\Users\klein\quartz-investing"
$PublicDir   = Join-Path $QuartzDir "public"
$NextDir     = Join-Path $QuartzDir "public-next"
$OldDir      = Join-Path $QuartzDir "public-old"
$LogDir      = "$env:USERPROFILE\financial-charts\logs"
$LogFile     = "$LogDir\quartz-rebuild.log"
$LockFile    = "$LogDir\quartz-rebuild.lock"

if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
}

function Write-Log {
    param([string]$msg)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $LogFile -Value "$ts $msg"
}

# Lock check - refuse to run if another rebuild is in flight.
if (Test-Path $LockFile) {
    $lockAge = (Get-Date) - (Get-Item $LockFile).LastWriteTime
    if ($lockAge.TotalHours -lt 2) {
        Write-Log "SKIP: lockfile present (age $([int]$lockAge.TotalMinutes)m) - concurrent rebuild?"
        exit 0
    }
    Write-Log "WARN: stale lockfile (age $([int]$lockAge.TotalHours)h) - clearing"
    Remove-Item -Path $LockFile -Force
}
New-Item -ItemType File -Path $LockFile -Force | Out-Null

try {
    Write-Log "START rebuild"
    $startedAt = Get-Date

    # Pre-clean any leftover sibling dirs from a prior failed run.
    if (Test-Path $NextDir) {
        Write-Log "Removing leftover public-next/ from prior run"
        Remove-Item -Path $NextDir -Recurse -Force
    }
    if (Test-Path $OldDir) {
        Write-Log "Removing leftover public-old/ from prior run"
        Remove-Item -Path $OldDir -Recurse -Force
    }

    # Run the build. -o public-next directs output away from the live dir.
    Push-Location $QuartzDir
    try {
        $buildLog = "$LogDir\quartz-build.out.log"
        $buildErr = "$LogDir\quartz-build.err.log"
        $proc = Start-Process -FilePath "npx.cmd" `
            -ArgumentList @("quartz", "build", "-o", "public-next", "--concurrency", "4") `
            -WorkingDirectory $QuartzDir `
            -RedirectStandardOutput $buildLog `
            -RedirectStandardError $buildErr `
            -NoNewWindow -Wait -PassThru
        if ($proc.ExitCode -ne 0) {
            Write-Log "FAIL: npx quartz build exit code $($proc.ExitCode) - see $buildErr"
            if (Test-Path $NextDir) { Remove-Item -Path $NextDir -Recurse -Force }
            exit 1
        }
    } finally {
        Pop-Location
    }

    if (-not (Test-Path $NextDir)) {
        Write-Log "FAIL: build reported success but public-next/ doesn't exist"
        exit 1
    }

    # Atomic swap. On NTFS same-volume renames are effectively atomic;
    # serve_static.py may briefly 404 during the rename pair.
    Write-Log "Swapping public/ -> public-old/ -> remove; public-next/ -> public/"
    if (Test-Path $PublicDir) {
        Rename-Item -Path $PublicDir -NewName "public-old"
    }
    Rename-Item -Path $NextDir -NewName "public"

    # Cleanup the old dir in the background - don't hold up the script.
    if (Test-Path $OldDir) {
        Start-Job -ScriptBlock {
            param($p)
            Remove-Item -Path $p -Recurse -Force -ErrorAction SilentlyContinue
        } -ArgumentList $OldDir | Out-Null
    }

    $elapsed = (Get-Date) - $startedAt
    Write-Log "DONE rebuild in $([int]$elapsed.TotalMinutes)m $([int]($elapsed.TotalSeconds % 60))s"
} catch {
    Write-Log "ERROR: $_"
    if (Test-Path $NextDir) {
        Write-Log "Cleaning failed public-next/"
        Remove-Item -Path $NextDir -Recurse -Force -ErrorAction SilentlyContinue
    }
    exit 1
} finally {
    Remove-Item -Path $LockFile -Force -ErrorAction SilentlyContinue
}
