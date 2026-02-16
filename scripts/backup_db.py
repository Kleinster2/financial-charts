"""Backup market_data.db using SQLite's online backup API.

Safe to run while the database is open (handles WAL mode correctly).
Keeps the most recent N backups and deletes older ones.

Usage:
    python scripts/backup_db.py              # backup with defaults
    python scripts/backup_db.py --keep 5     # keep last 5 backups
    python scripts/backup_db.py --list       # show existing backups
"""

import argparse
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "market_data.db"
BACKUP_DIR = Path("G:/My Drive/backups/financial-charts")
PREFIX = "market_data_"
SUFFIX = ".db"
DEFAULT_KEEP = 3


def list_backups():
    """Return existing DB backups sorted oldest-first."""
    if not BACKUP_DIR.exists():
        return []
    return sorted(
        f for f in BACKUP_DIR.iterdir()
        if f.name.startswith(PREFIX) and f.name.endswith(SUFFIX)
    )


def backup(keep: int = DEFAULT_KEEP):
    if not DB_PATH.exists():
        print(f"ERROR: {DB_PATH} not found")
        sys.exit(1)

    BACKUP_DIR.mkdir(exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = BACKUP_DIR / f"{PREFIX}{stamp}{SUFFIX}"

    print(f"Backing up {DB_PATH.name} ({DB_PATH.stat().st_size / 1e6:.0f} MB) ...")

    src_conn = sqlite3.connect(str(DB_PATH))
    dst_conn = sqlite3.connect(str(dest))
    try:
        src_conn.backup(dst_conn)
    finally:
        dst_conn.close()
        src_conn.close()

    print(f"  -> {dest}  ({dest.stat().st_size / 1e6:.0f} MB)")

    # Prune old backups
    existing = list_backups()
    to_delete = existing[:-keep] if keep > 0 else []
    for old in to_delete:
        old.unlink()
        print(f"  Deleted old backup: {old.name}")

    remaining = list_backups()
    print(f"Done. {len(remaining)} backup(s) retained.")


def show_list():
    existing = list_backups()
    if not existing:
        print("No backups found.")
        return
    print(f"{'File':<45} {'Size':>10}  {'Date'}")
    print("-" * 75)
    for f in existing:
        size_mb = f.stat().st_size / 1e6
        # Parse timestamp from filename
        ts_str = f.stem.replace(PREFIX, "")
        try:
            ts = datetime.strptime(ts_str, "%Y%m%d_%H%M%S")
            date_str = ts.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            date_str = "?"
        print(f"{f.name:<45} {size_mb:>7.0f} MB  {date_str}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup market_data.db")
    parser.add_argument("--keep", type=int, default=DEFAULT_KEEP,
                        help=f"Number of backups to retain (default: {DEFAULT_KEEP})")
    parser.add_argument("--list", action="store_true", help="List existing backups")
    args = parser.parse_args()

    if args.list:
        show_list()
    else:
        backup(keep=args.keep)
