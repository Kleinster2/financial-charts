#!/usr/bin/env python3
"""
Workspace Backup Utility
Backs up chart workspace configurations with timestamped versions
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

# Configuration
WORKSPACE_FILE = Path(__file__).parent / "charting_app" / "workspace.json"
BACKUP_DIR = Path(__file__).parent / "workspace_backups"
MAX_BACKUPS = 50  # Keep last 50 backups


def ensure_backup_dir():
    """Create backup directory if it doesn't exist"""
    BACKUP_DIR.mkdir(exist_ok=True)
    print(f"Backup directory: {BACKUP_DIR}")


def create_backup():
    """Create a timestamped backup of the workspace"""
    if not WORKSPACE_FILE.exists():
        print(f"Error: Workspace file not found at {WORKSPACE_FILE}")
        return False

    # Read current workspace
    with open(WORKSPACE_FILE, 'r') as f:
        workspace_data = json.load(f)

    # Count charts
    num_charts = len(workspace_data.get('cards', []))
    num_pages = len(workspace_data.get('pages', {}).get('pages', []))

    if num_charts == 0:
        print("Warning: Workspace has 0 charts. Skipping backup to avoid overwriting good data.")
        return False

    # Create timestamped backup filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = BACKUP_DIR / f"workspace_backup_{timestamp}.json"

    # Write backup
    with open(backup_file, 'w') as f:
        json.dump(workspace_data, f, indent=2)

    print(f"[OK] Backup created: {backup_file.name}")
    print(f"  Charts: {num_charts}, Pages: {num_pages}")

    return True


def cleanup_old_backups():
    """Remove old backups keeping only MAX_BACKUPS most recent"""
    backups = sorted(BACKUP_DIR.glob("workspace_backup_*.json"))

    if len(backups) > MAX_BACKUPS:
        to_remove = backups[:-MAX_BACKUPS]
        for backup in to_remove:
            backup.unlink()
            print(f"Removed old backup: {backup.name}")


def list_backups():
    """List all available backups"""
    backups = sorted(BACKUP_DIR.glob("workspace_backup_*.json"), reverse=True)

    if not backups:
        print("No backups found.")
        return

    print(f"\nAvailable backups ({len(backups)} total):")
    print("-" * 80)

    for i, backup in enumerate(backups[:10], 1):  # Show last 10
        try:
            with open(backup, 'r') as f:
                data = json.load(f)
            num_charts = len(data.get('cards', []))
            num_pages = len(data.get('pages', {}).get('pages', []))

            # Parse timestamp from filename
            timestamp_str = backup.stem.replace('workspace_backup_', '')
            try:
                dt = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
                date_str = dt.strftime("%Y-%m-%d %H:%M:%S")
            except:
                date_str = timestamp_str

            print(f"{i:2d}. {backup.name}")
            print(f"    Date: {date_str}")
            print(f"    Charts: {num_charts}, Pages: {num_pages}")
            print(f"    Size: {backup.stat().st_size:,} bytes")
            print()
        except Exception as e:
            print(f"{i:2d}. {backup.name} - Error reading: {e}")


def restore_backup(backup_file):
    """Restore a specific backup"""
    if not backup_file.exists():
        print(f"Error: Backup file not found: {backup_file}")
        return False

    # Create backup of current workspace before restoring
    if WORKSPACE_FILE.exists():
        current_backup = BACKUP_DIR / f"workspace_before_restore_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        shutil.copy(WORKSPACE_FILE, current_backup)
        print(f"Current workspace backed up to: {current_backup.name}")

    # Restore the backup
    shutil.copy(backup_file, WORKSPACE_FILE)

    # Read restored data
    with open(WORKSPACE_FILE, 'r') as f:
        data = json.load(f)

    num_charts = len(data.get('cards', []))
    num_pages = len(data.get('pages', {}).get('pages', []))

    print(f"[OK] Workspace restored from: {backup_file.name}")
    print(f"  Charts: {num_charts}, Pages: {num_pages}")

    return True


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Workspace Backup Utility')
    parser.add_argument('command', choices=['backup', 'list', 'restore'],
                        help='Command to execute')
    parser.add_argument('--file', help='Backup file to restore (for restore command)')

    args = parser.parse_args()

    ensure_backup_dir()

    if args.command == 'backup':
        if create_backup():
            cleanup_old_backups()

    elif args.command == 'list':
        list_backups()

    elif args.command == 'restore':
        if not args.file:
            print("Error: --file argument required for restore command")
            list_backups()
            return

        backup_file = BACKUP_DIR / args.file
        if not backup_file.exists():
            # Try with just the filename
            backup_file = BACKUP_DIR / f"workspace_backup_{args.file}.json"

        restore_backup(backup_file)


if __name__ == '__main__':
    main()
