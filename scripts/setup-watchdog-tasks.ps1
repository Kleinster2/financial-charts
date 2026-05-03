# Reverts FinancialCharts-Watchdog from S4U back to Interactive,
# and switches both tasks (Watchdog + OnLogon) to launch via the
# silent .vbs wrapper instead of powershell.exe directly.
# Run from an admin PowerShell.

$ErrorActionPreference = "Stop"

$action = New-ScheduledTaskAction `
    -Execute "C:\Windows\System32\wscript.exe" `
    -Argument '"C:\Users\klein\financial-charts\scripts\run-watchdog.vbs"'

$principal = New-ScheduledTaskPrincipal `
    -UserId klein `
    -LogonType Interactive `
    -RunLevel Limited

Write-Host "=== Backing up OnLogon task ==="
Export-ScheduledTask -TaskName "FinancialCharts-OnLogon" |
    Out-File -Encoding UTF8 "C:\Users\klein\financial-charts\scripts\onlogon-task-backup.xml"

Write-Host "=== Updating FinancialCharts-Watchdog (action + Interactive principal) ==="
Set-ScheduledTask -TaskName "FinancialCharts-Watchdog" -Action $action -Principal $principal | Out-Null

Write-Host "=== Updating FinancialCharts-OnLogon (action only) ==="
Set-ScheduledTask -TaskName "FinancialCharts-OnLogon" -Action $action | Out-Null

Write-Host "`n=== Verify ==="
Get-ScheduledTask -TaskName "FinancialCharts-Watchdog","FinancialCharts-OnLogon" | ForEach-Object {
    Write-Host "--- $($_.TaskName) ---"
    $_.Actions    | Format-List Execute, Arguments
    $_.Principal  | Format-List UserId, LogonType, RunLevel
}

Write-Host "`n=== Manual trigger of Watchdog ==="
Start-ScheduledTask -TaskName "FinancialCharts-Watchdog"
Start-Sleep 8
Get-ScheduledTaskInfo "FinancialCharts-Watchdog" | Format-List LastRunTime, LastTaskResult
