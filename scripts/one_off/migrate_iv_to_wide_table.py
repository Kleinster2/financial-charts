#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Migrate CBOE Implied Volatility data to stock_prices_daily table.

This script:
1. Adds IV ticker columns (^VXAPL, ^VIX, etc.) to stock_prices_daily
2. Migrates data from implied_volatility_daily table
3. Creates backup of implied_volatility_daily before deletion (optional)

Run with --dry-run to preview changes without modifying database.
"""

import sqlite3
import argparse
import sys
from datetime import datetime

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = 'market_data.db'

# CBOE tickers to migrate
CBOE_TICKERS = [
    '^VIX',      # S&P 500 Volatility
    '^VXN',      # Nasdaq-100 Volatility
    '^VXD',      # Dow Jones Volatility
    '^VXAPL',    # Apple Volatility
    '^VXAZN',    # Amazon Volatility
    '^VXGOG',    # Google Volatility
    '^VXGS',     # Goldman Sachs Volatility
    '^VXIBM',    # IBM Volatility
]


def check_existing_columns(cursor):
    """Check if IV columns already exist in stock_prices_daily."""
    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    existing_columns = {row[1] for row in cursor.fetchall()}

    already_exist = [ticker for ticker in CBOE_TICKERS if ticker in existing_columns]
    need_to_add = [ticker for ticker in CBOE_TICKERS if ticker not in existing_columns]

    return already_exist, need_to_add


def add_iv_columns(conn, cursor, dry_run=False):
    """Add IV ticker columns to stock_prices_daily."""
    print("\n" + "="*70)
    print("STEP 1: Adding IV Columns to stock_prices_daily")
    print("="*70)

    already_exist, need_to_add = check_existing_columns(cursor)

    if already_exist:
        print(f"\n✓ Already exist ({len(already_exist)} columns):")
        for ticker in already_exist:
            print(f"  - {ticker}")

    if need_to_add:
        print(f"\n→ Adding {len(need_to_add)} new columns:")
        for ticker in need_to_add:
            print(f"  - {ticker}")
            if not dry_run:
                cursor.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')

        if not dry_run:
            conn.commit()
            print(f"\n✓ Added {len(need_to_add)} columns successfully")
        else:
            print(f"\n[DRY RUN] Would add {len(need_to_add)} columns")
    else:
        print("\n✓ All IV columns already exist, skipping")

    return need_to_add


def get_migration_stats(cursor):
    """Get statistics about data to migrate."""
    stats = {}

    for ticker in CBOE_TICKERS:
        cursor.execute("""
            SELECT COUNT(*), MIN(date), MAX(date)
            FROM implied_volatility_daily
            WHERE ticker = ?
        """, (ticker,))

        count, min_date, max_date = cursor.fetchone()
        stats[ticker] = {
            'count': count,
            'min_date': min_date,
            'max_date': max_date
        }

    return stats


def migrate_iv_data(conn, cursor, dry_run=False):
    """Migrate IV data from implied_volatility_daily to stock_prices_daily."""
    print("\n" + "="*70)
    print("STEP 2: Migrating IV Data")
    print("="*70)

    stats = get_migration_stats(cursor)

    total_rows = 0
    for ticker, ticker_stats in stats.items():
        count = ticker_stats['count']
        total_rows += count
        print(f"\n{ticker}:")
        print(f"  Records: {count}")
        print(f"  Range: {ticker_stats['min_date']} to {ticker_stats['max_date']}")

    print(f"\n→ Total records to migrate: {total_rows}")

    if dry_run:
        print("\n[DRY RUN] Would migrate data, but skipping in dry-run mode")
        return

    # Migrate each ticker
    print("\nMigrating data:")
    for ticker in CBOE_TICKERS:
        # Update stock_prices_daily with IV data
        # Convert average_iv from decimal (0.2665) to percentage (26.65) for consistency
        cursor.execute(f"""
            UPDATE stock_prices_daily
            SET "{ticker}" = (
                SELECT average_iv * 100
                FROM implied_volatility_daily
                WHERE ticker = ?
                  AND date = DATE(stock_prices_daily.Date)
            )
        """, (ticker,))

        updated = cursor.rowcount
        print(f"  {ticker}: {updated} rows updated")

    conn.commit()
    print("\n✓ Migration complete")


def verify_migration(cursor):
    """Verify data was migrated correctly."""
    print("\n" + "="*70)
    print("STEP 3: Verification")
    print("="*70)

    # Check a few sample dates
    cursor.execute(f"""
        SELECT Date, "^VXAPL", "^VIX", "^VXN"
        FROM stock_prices_daily
        WHERE "^VXAPL" IS NOT NULL
        ORDER BY Date DESC
        LIMIT 5
    """)

    print("\nSample migrated data (recent 5 dates):")
    print(f"{'Date':<20} {'VXAPL':<10} {'VIX':<10} {'VXN':<10}")
    print("-" * 50)

    for row in cursor.fetchall():
        date, vxapl, vix, vxn = row
        print(f"{str(date):<20} {vxapl or 'NULL':<10.2f} {vix or 'NULL':<10.2f} {vxn or 'NULL':<10.2f}")

    # Count non-NULL values
    print("\nData coverage:")
    for ticker in CBOE_TICKERS:
        cursor.execute(f"""
            SELECT COUNT(*)
            FROM stock_prices_daily
            WHERE "{ticker}" IS NOT NULL
        """, )

        count = cursor.fetchone()[0]
        print(f"  {ticker}: {count} non-NULL values")


def backup_old_table(conn, cursor, dry_run=False):
    """Create backup of implied_volatility_daily table."""
    print("\n" + "="*70)
    print("STEP 4: Backup (Optional)")
    print("="*70)

    if dry_run:
        print("\n[DRY RUN] Would create backup table: implied_volatility_daily_backup")
        return

    # Check if backup already exists
    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name='implied_volatility_daily_backup'
    """)

    if cursor.fetchone():
        print("\n⚠ Backup table already exists: implied_volatility_daily_backup")
        print("  Skipping backup creation")
        return

    print("\nCreating backup: implied_volatility_daily_backup")
    cursor.execute("""
        CREATE TABLE implied_volatility_daily_backup AS
        SELECT * FROM implied_volatility_daily
    """)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM implied_volatility_daily_backup")
    count = cursor.fetchone()[0]
    print(f"✓ Backup created with {count} rows")


def main():
    parser = argparse.ArgumentParser(
        description="Migrate CBOE IV data to stock_prices_daily table"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Preview changes without modifying database"
    )
    parser.add_argument(
        '--no-backup',
        action='store_true',
        help="Skip creating backup of implied_volatility_daily table"
    )
    parser.add_argument(
        '--delete-old-table',
        action='store_true',
        help="Delete implied_volatility_daily table after migration (requires confirmation)"
    )

    args = parser.parse_args()

    print("="*70)
    print("CBOE IV Migration to Wide Table")
    print("="*70)
    print(f"\nDatabase: {DB_PATH}")
    print(f"Tickers to migrate: {len(CBOE_TICKERS)}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE MIGRATION'}")
    print(f"Backup: {'Disabled' if args.no_backup else 'Enabled'}")

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Step 1: Add columns
        add_iv_columns(conn, cursor, dry_run=args.dry_run)

        # Step 2: Migrate data
        migrate_iv_data(conn, cursor, dry_run=args.dry_run)

        # Step 3: Verify (skip in dry-run)
        if not args.dry_run:
            verify_migration(cursor)

        # Step 4: Backup (optional)
        if not args.no_backup and not args.dry_run:
            backup_old_table(conn, cursor, dry_run=args.dry_run)

        # Step 5: Delete old table (optional, requires confirmation)
        if args.delete_old_table and not args.dry_run:
            print("\n" + "="*70)
            print("STEP 5: Delete Old Table")
            print("="*70)

            response = input("\n⚠ Delete implied_volatility_daily table? (type 'yes' to confirm): ")
            if response.lower() == 'yes':
                cursor.execute("DROP TABLE implied_volatility_daily")
                conn.commit()
                print("✓ Table deleted: implied_volatility_daily")
            else:
                print("✗ Deletion cancelled")

        print("\n" + "="*70)
        print("Migration Summary")
        print("="*70)

        if args.dry_run:
            print("\n[DRY RUN] No changes were made to the database")
            print("\nRun without --dry-run to perform actual migration:")
            print("  python migrate_iv_to_wide_table.py")
        else:
            print("\n✓ Migration completed successfully!")
            print(f"\nNext steps:")
            print("  1. Test queries on stock_prices_daily to verify IV data")
            print("  2. Update cboe_iv_fetcher.py to write to wide table")
            print("  3. Update Flask endpoints to use single table")
            print("  4. Simplify data-fetcher.js (remove IV routing)")

            if not args.delete_old_table:
                print("\n  Optional: Run with --delete-old-table to remove old table")

    except Exception as e:
        print(f"\n✗ Error during migration: {e}")
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == '__main__':
    main()
