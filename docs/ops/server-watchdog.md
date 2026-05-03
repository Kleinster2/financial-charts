# Server watchdog

Auto-start and auto-restart for the two long-running servers behind the local + Tailscale-accessible vault viewer:

| Server | Port | Purpose |
|---|---|---|
| `charting_app/app.py` (Flask) | 5000 | Chart rendering API used by Quartz iframes and ad-hoc requests |
| `quartz-investing/serve_static.py` | 8080 | Static server for Quartz `public/` with extensionless-URL fallback |

Both bind to `0.0.0.0`, so they're reachable on localhost, the LAN, and the Tailscale interface (`gilssurface` / `100.116.132.71`).

## Layout

| Path | Role |
|---|---|
| `scripts/server_watchdog.ps1` | The watchdog. Idempotent — does nothing if both ports are already listening. |
| `~/financial-charts/logs/watchdog.log` | Watchdog actions (start attempts, failures). |
| `~/financial-charts/logs/flask.{out,err}.log` | Flask stdout/stderr (rolling, overwritten on each restart). |
| `~/financial-charts/logs/quartz.{out,err}.log` | Static-server stdout/stderr. |
| Task Scheduler `FinancialCharts-OnLogon` | Fires watchdog at user logon. |
| Task Scheduler `FinancialCharts-Watchdog` | Fires watchdog every 5 minutes for the rest of the session. |

## Why these choices

- **Single watchdog script for both triggers.** The script checks each port and only spawns what's missing, so the OnLogon task and the every-5-min task share logic and can't double-start anything.
- **`pythonw.exe` (no console)** keeps the desktop free of console windows. Using `python.exe` would flash a console at every spawn.
- **`-RedirectStandardOutput` / `-RedirectStandardError`** is mandatory. Without it, `pythonw` processes hang on the first `print()` once stdout has no console to write to. Symptom: process binds the port but never serves a request.
- **5-minute interval.** Long enough to avoid log spam, short enough that a crash recovers before you notice. With 12 logical cores and one Flask + one HTTP server, the cost of a watchdog tick when both servers are up is negligible (a couple of `Get-NetTCPConnection` calls).
- **`LogonType Interactive`, `RunLevel Limited`** — runs as the current user, no SYSTEM-level access needed because both servers only need user-profile files.
- **`-AllowStartIfOnBatteries -DontStopIfGoingOnBatteries`** in task settings, so the watchdog still fires when the Surface is unplugged.

## Surface sleep setting (required)

Even with auto-restart, lid-close-induced sleep kills both servers. To keep them running 24/7:

```
Settings → System → Power & battery → Screen and sleep
  When plugged in, put my device to sleep after → Never
  When plugged in, turn my screen off after → (whatever you want)
```

Set the same on battery power if you want phone access while the Surface is unplugged.

## Management

```powershell
# Status of both tasks
Get-ScheduledTask -TaskName "FinancialCharts-*" | Format-Table TaskName,State

# Last-run result for the watchdog
Get-ScheduledTaskInfo -TaskName "FinancialCharts-Watchdog"

# Tail the watchdog log
Get-Content "$env:USERPROFILE\financial-charts\logs\watchdog.log" -Tail 20 -Wait

# Manual fire (useful for debugging)
Start-ScheduledTask -TaskName "FinancialCharts-Watchdog"

# Disable temporarily
Disable-ScheduledTask -TaskName "FinancialCharts-Watchdog"
Disable-ScheduledTask -TaskName "FinancialCharts-OnLogon"

# Remove entirely
Unregister-ScheduledTask -TaskName "FinancialCharts-Watchdog" -Confirm:$false
Unregister-ScheduledTask -TaskName "FinancialCharts-OnLogon"  -Confirm:$false
```

## Re-registering after a Python upgrade

The watchdog hardcodes the path to `pythonw.exe`. If the Microsoft Store Python is upgraded (the version segment in the path changes), update `$Pythonw` at the top of `scripts/server_watchdog.ps1`. To find the new path:

```powershell
# While Flask is running, infer the install dir from its process
$dir = Split-Path (Get-Process -Id (Get-NetTCPConnection -LocalPort 5000 -State Listen).OwningProcess).Path
"$dir\pythonw.exe"
```

That returns the canonical `C:\Users\klein\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.X.YZ_qbz5n2kfra8p0\pythonw.exe`.

Note: the WindowsApps path is a 0-byte alias stub. Direct invocation (`& $Pythonw`) works and the OS resolves it transparently. The real binary in `C:\Program Files\WindowsApps\` is ACL-protected and can't be referenced directly from user-space scripts.

## Failure modes seen during setup

| Symptom | Cause | Fix |
|---|---|---|
| Task `LastTaskResult: 0x80070002` (FILE_NOT_FOUND) | Action used bare `powershell.exe`; not on the scheduled-task PATH in some contexts | Hardcoded full path `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` in the action |
| Watchdog logs "Starting...", port binds, but `curl` returns empty reply | `pythonw.exe` blocks on `print()` with no attached console | Added `-RedirectStandardOutput` / `-RedirectStandardError` to `Start-Process` |
| Repetition stops after first run | `RepetitionDuration` defaulted to empty with `StopAtDurationEnd: True` | Set explicit `New-TimeSpan -Days 3650` (10 years, effectively indefinite) |
| Two listeners on port 8080, IPv4 + IPv6 | Normal — Python's `ThreadingHTTPServer` with `0.0.0.0` registers both. Not a bug. | — |

## Reinstall from scratch

If the tasks ever get deleted or you want to re-bootstrap on a fresh machine, the registration block is:

```powershell
$script = "C:\Users\klein\financial-charts\scripts\server_watchdog.ps1"
$psExe = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$action = New-ScheduledTaskAction -Execute $psExe `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$script`""
$user = "$env:USERDOMAIN\$env:USERNAME"
$principal = New-ScheduledTaskPrincipal -UserId $user -LogonType Interactive -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 5)

$logonTrigger = New-ScheduledTaskTrigger -AtLogOn -User $user
$watchdogTrigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) `
    -RepetitionInterval (New-TimeSpan -Minutes 5) `
    -RepetitionDuration (New-TimeSpan -Days 3650)

Register-ScheduledTask -TaskName "FinancialCharts-OnLogon" `
    -Action $action -Trigger $logonTrigger -Settings $settings `
    -Principal $principal -Force | Out-Null
Register-ScheduledTask -TaskName "FinancialCharts-Watchdog" `
    -Action $action -Trigger $watchdogTrigger -Settings $settings `
    -Principal $principal -Force | Out-Null
```
