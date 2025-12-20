# Workspace Backup System

## Overview

This backup system protects your chart configurations from accidental loss. It creates timestamped backups and maintains a history of your workspace changes.

## Current Status

**WARNING**: Your workspace was recently lost - you had 26 pages of charts but only 2 charts remain. The page names are preserved:

1. Main
2. Correlation Pairs
3. Brazil
4. Crypto
5. China
6. Cboe
7. Quantum
8. Ark
9. Semis
10. PAVE
11. Clean
12. RiskPar
13. Metals
14. STAR
15. Drugs
16. ICE
17. Portfolios
18. John Deere
19. ALLW
20. Global Markets
21. NatSec
22. Argentina
23. ICE
24. Global Markets
25. Gaming & iGaming
26. NEW

## Usage

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

## Next Steps

To prevent future data loss:

1. Set up daily automated backups using Task Scheduler
2. Manually backup before testing new features
3. Consider committing important workspace states to git
