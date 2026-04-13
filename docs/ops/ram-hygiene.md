# RAM Hygiene (Windows)

Surface ships with limited RAM and Windows 11 accumulates background processes (Edge WebView2 instances, UWP bloatware, zombie Flask/Python from the charting app). This doc is the triage playbook.

## When to run

- Surface feels sluggish; fans ramping.
- After a long Flask/update_market_data session — zombie `python3.12` processes perpetuate DB locks (see `project_narrow_write_db_lock.md`).
- WAL file `market_data.db-wal` is >100MB (strong signal of lock contention from zombie holders).
- First thing after waking from a multi-day sleep/hibernate cycle.

## Step 1 — Inventory

Top 20 individual processes by working set:
```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 20 Name, @{N='RAM_MB';E={[math]::Round($_.WorkingSet64/1MB,0)}}, @{N='CPU_s';E={[math]::Round($_.CPU,1)}}, Id | Format-Table -AutoSize
```

Grouped by process name (catches many small instances of the same thing — Edge WebView2, Chrome, python):
```powershell
Get-Process | Group-Object -Property Name | ForEach-Object { [PSCustomObject]@{ Name = $_.Name; Count = $_.Count; Total_MB = [math]::Round(($_.Group | Measure-Object WorkingSet64 -Sum).Sum / 1MB, 0) } } | Sort-Object Total_MB -Descending | Select-Object -First 25 | Format-Table -AutoSize
```

## Step 2 — Identify Edge WebView2 culprits

WebView2 runs inside many apps (Teams, Outlook new, LinkedIn, Copilot, Widgets, etc.). To find which parent app is spawning the heavy instances:
```powershell
Get-Process msedgewebview2 -ErrorAction SilentlyContinue | Select-Object Id, @{N='MB';E={[math]::Round($_.WorkingSet64/1MB)}}, @{N='Parent';E={(Get-CimInstance Win32_Process -Filter ('ProcessId=' + $_.Id)).ParentProcessId}} | ForEach-Object { $parent = Get-Process -Id $_.Parent -ErrorAction SilentlyContinue; [PSCustomObject]@{PID=$_.Id; MB=$_.MB; ParentName=if($parent){$parent.Name}else{'?'}; ParentPID=$_.Parent} } | Sort-Object MB -Descending | Select-Object -First 15 | Format-Table -AutoSize
```

## Step 3 — Kill known bloatware

Transient kills (will respawn on reboot unless you uninstall):
```powershell
Get-Process LinkedIn -ErrorAction SilentlyContinue | Stop-Process -Force
Get-Process M365Copilot -ErrorAction SilentlyContinue | Stop-Process -Force
Get-Process PhoneExperienceHost -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Step 4 — Uninstall permanently

AppxPackage removal (UWP apps — LinkedIn, Copilot, YourPhone, etc.):
```powershell
Get-AppxPackage Microsoft.YourPhone | Remove-AppxPackage
Get-AppxPackage *linkedin* | Remove-AppxPackage
Get-AppxPackage *M365Copilot* | Remove-AppxPackage
```

Classic apps via winget:
```powershell
winget uninstall "Windows Web Experience Pack" --accept-source-agreements
```

Check status after:
```powershell
Get-AppxPackage *linkedin* | Select-Object Name, Status
```

## Step 5 — Project-specific zombies

Charting app stack accumulates Flask instances and stuck update scripts. Check via Git Bash:
```bash
tasklist | grep python3.12
```

If zombies hold `market_data.db`, see `project_narrow_write_db_lock.md`. Kill with `taskkill //F //PID <pid>` (Git Bash) or `Stop-Process -Id <pid> -Force` (PowerShell).

## Usual suspects (known heavy)

| Process | Source | Action |
|---------|--------|--------|
| `msedgewebview2` × many | Teams/Outlook/Widgets/LinkedIn/Copilot | Identify parent, uninstall parent |
| `PhoneExperienceHost` | YourPhone (Microsoft) | Uninstall AppxPackage |
| `M365Copilot` | Office Copilot stub | Uninstall AppxPackage |
| `LinkedIn` | LinkedIn UWP | Uninstall AppxPackage |
| `python3.12` × many | Flask/update scripts | Kill zombies; see narrow_write doc |
| `msedge` × many | Edge tab sprawl | Close tabs; consider Edge profile cleanup |

## Notes

- `Stop-Process -Force` doesn't release instantly if the process is in a syscall — give it a few seconds.
- Removing AppxPackage for a signed-in Microsoft account app (LinkedIn, Copilot) is account-local; it will not re-provision unless you sign in and trigger it.
- Do not kill processes you don't recognize — check parent with the WebView2 query above first.
