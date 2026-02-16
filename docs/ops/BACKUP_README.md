# Backup Systems

## Database Backup (market_data.db)

`market_data.db` (~878 MB) contains irreplaceable data (B3 DI yield curve, bond prices, portfolio data) that cannot be re-downloaded from APIs.

### Automated Schedule

A Windows Task Scheduler job (`BackupMarketData`) runs weekly on Sundays at 6:00 AM. It uses SQLite's online backup API, which is safe to run while the database is open.

- **Script:** `scripts/backup_db.py`
- **Destination:** `G:\My Drive\backups\financial-charts\` (Google Drive, synced to cloud)
- **Retention:** Last 3 backups (~2.6 GB total)
- **Requires:** Machine awake at scheduled time; Google Drive running

### Manual Usage

```powershell
python scripts/backup_db.py              # backup now
python scripts/backup_db.py --keep 5     # backup, keep last 5
python scripts/backup_db.py --list       # show existing backups
```

Run manually before risky operations (migrations, schema changes, one-off scripts).

### Task Scheduler Management

```powershell
schtasks /query /tn "BackupMarketData" /v /fo list   # check status
schtasks /run /tn "BackupMarketData"                  # run now
schtasks /delete /tn "BackupMarketData" /f            # remove
```

---

## Workspace Backup (workspace.json)

### Overview

This backup system protects your chart configurations from accidental loss. It creates timestamped backups and maintains a history of your workspace changes.

### Usage

### Create a Backup

```bash
python backup_workspace.py backup
```

This creates a timestamped backup file in `workspace_backups/` directory.

**Important**: The script will refuse to backup if there are 0 charts, preventing overwriting good data with empty workspace.

### List Available Backups

```bash
python backup_workspace.py list
```

Shows the last 10 backups with details about charts and pages.

### Restore a Backup

```bash
python backup_workspace.py restore --file workspace_backup_20251030_041949.json
```

Or use just the timestamp:

```bash
python backup_workspace.py restore --file 20251030_041949
```

This will:
1. Create a backup of your current workspace before restoring
2. Restore the selected backup
3. Show you how many charts and pages were restored

## Automated Backups

### Automatic Backups (ENABLED)

**The backup system is now fully automated!** Every time you save changes to your workspace (add/remove charts, change tickers, etc.), a backup is automatically created.

- Backups happen automatically on every workspace save via the Flask API
- No manual intervention required
- Protection against accidental data loss
- Keeps last 50 backups

You can still run manual backups if desired:

```bash
python backup_workspace.py backup
```

### Scheduled Backups (Optional, Not Needed)

#### Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., Daily at 2 AM)
4. Action: Start a program
   - Program: `python`
   - Arguments: `C:\Users\klein\financial-charts\backup_workspace.py backup`
   - Start in: `C:\Users\klein\financial-charts`

#### Git Hook (Advanced)

Create `.git/hooks/pre-commit`:

```bash
#!/bin/sh
cd "$(git rev-parse --show-toplevel)"
python backup_workspace.py backup
```

## Backup Storage

- Location: `workspace_backups/`
- Retention: Last 50 backups (automatic cleanup)
- Format: JSON files with timestamped names

## Best Practices

1. **Backup Before Major Changes**: Always run `python backup_workspace.py backup` before:
   - Recreating many charts
   - Testing new features
   - Clearing browser localStorage

2. **Regular Backups**: Create backups daily or after adding significant charts

3. **Version Control**: The `workspace_backups/` directory is gitignored, but you can manually commit important backups

4. **Multiple Browsers**: If you use multiple browsers, the Flask backend at http://localhost:5000/api/workspace syncs your workspace

## Recovery

If you lose charts:

1. List backups: `python backup_workspace.py list`
2. Find the backup with the correct number of charts
3. Restore it: `python backup_workspace.py restore --file [filename]`
4. Reload your browser to see the restored charts

## Files

- `backup_workspace.py` - Main backup utility script
- `workspace_backups/` - Backup storage directory (auto-created)
- `charting_app/workspace.json` - Live workspace file

## Troubleshooting

**"No backups found"**: Run `python backup_workspace.py backup` to create your first backup

**"Workspace has 0 charts"**: The backup was skipped to protect existing backups. This is intentional.

**Backup shows wrong chart count**: Check if the Flask server has different data than the local file

