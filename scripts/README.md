# Scripts

Auxiliary scripts moved out of repo root for cleaner organization.

## Directory Structure

```
scripts/
├── create_sample_db.py  # Generate sample_data.db for demo mode (10 tickers, 45 days)
│
├── one_off/      # Migrations, backfills, one-time setup
│                 # add_*, restore_*, migrate_*, cleanup_*, etc.
│                 # These ran once and are kept for reference
│
└── diagnostics/  # Audits, health checks, verification
                  # audit_*, check_*, verify_*, test_*
                  # Safe to re-run anytime (includes ad-hoc test scripts)
```

## Running Scripts

All scripts can be run from the repo root:

```bash
python scripts/diagnostics/check_db.py
python scripts/one_off/migrate_to_duckdb.py
```

Each script includes a path shim so imports work regardless of working directory.

## Core Scripts (in repo root)

Daily-use and core module scripts remain in the repo root:
- `update_*.py` - Daily data updates
- `download_*.py` - Data downloaders
- `fetch_*.py` - Data fetchers
- `constants.py`, `metadata_utils.py` - Shared config/utilities
