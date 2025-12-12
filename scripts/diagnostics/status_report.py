"""
Data freshness dashboard - check latest dates across all core tables.

Usage:
    python scripts/diagnostics/status_report.py           # Full report
    python scripts/diagnostics/status_report.py --brief   # One-line summary
    python scripts/diagnostics/status_report.py --max-age 3  # Fail if >3 trading days stale
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import argparse
import sqlite3
from datetime import datetime, timedelta

from constants import DB_PATH


def trading_days_ago(n: int) -> datetime:
    """Return date n trading days ago (rough estimate: skip weekends)."""
    today = datetime.now()
    days_back = 0
    result = today
    while days_back < n:
        result -= timedelta(days=1)
        if result.weekday() < 5:  # Mon-Fri
            days_back += 1
    return result


def get_latest_date(conn: sqlite3.Connection, table: str, date_col: str = "Date") -> tuple:
    """Get latest date and row count from a table."""
    try:
        cur = conn.execute(f"SELECT MAX({date_col}), COUNT(*) FROM {table}")
        row = cur.fetchone()
        if row and row[0]:
            # Parse date
            date_str = row[0]
            for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S"):
                try:
                    return datetime.strptime(date_str[:10], "%Y-%m-%d"), row[1]
                except ValueError:
                    continue
        return None, row[1] if row else 0
    except sqlite3.OperationalError:
        return None, 0


def get_wide_table_latest(conn: sqlite3.Connection, table: str) -> tuple:
    """Get latest date from wide-format table (Date as row index)."""
    try:
        cur = conn.execute(f"SELECT MAX(Date) FROM {table}")
        row = cur.fetchone()
        if row and row[0]:
            return datetime.strptime(row[0][:10], "%Y-%m-%d"), None
        return None, None
    except sqlite3.OperationalError:
        return None, None


def get_fundamentals_latest(conn: sqlite3.Connection) -> tuple:
    """Get latest update from company_overview table."""
    try:
        cur = conn.execute("SELECT MAX(last_updated), COUNT(*) FROM company_overview")
        row = cur.fetchone()
        if row and row[0]:
            # Handle various timestamp formats
            ts = row[0]
            for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"):
                try:
                    return datetime.strptime(ts[:19], fmt), row[1]
                except ValueError:
                    continue
        return None, row[1] if row else 0
    except sqlite3.OperationalError:
        return None, 0


def main():
    parser = argparse.ArgumentParser(description="Data freshness dashboard")
    parser.add_argument("--max-age", type=int, default=2,
                        help="Max trading days since last update before flagging stale (default: 2)")
    parser.add_argument("--brief", action="store_true",
                        help="One-line summary only")
    parser.add_argument("--quiet", action="store_true",
                        help="Only output on failure")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    cutoff = trading_days_ago(args.max_age)
    today = datetime.now().date()

    # Define tables to check: (display_name, table_name, is_wide_table)
    tables = [
        ("Stock Prices", "stock_prices_daily", True),
        ("Stock Volumes", "stock_volumes_daily", True),
        ("CBOE Indices", "cboe_indices_daily", True),
        ("Implied Vol", "implied_volatility_daily", True),
        ("Credit Spreads", "credit_spreads_daily", True),
        ("Bond Prices", "bond_prices_daily", True),
        ("Futures Prices", "futures_prices_daily", True),
    ]

    results = []
    stale = []

    for name, table, is_wide in tables:
        if is_wide:
            latest, _ = get_wide_table_latest(conn, table)
        else:
            latest, _ = get_latest_date(conn, table)

        if latest is None:
            results.append((name, "NO DATA", True))
            stale.append(name)
        elif latest < cutoff:
            age = (today - latest.date()).days
            results.append((name, f"{latest.date()} ({age}d ago)", True))
            stale.append(name)
        else:
            age = (today - latest.date()).days
            results.append((name, f"{latest.date()} ({age}d ago)", False))

    # Check fundamentals separately (uses last_updated timestamp)
    fund_latest, fund_count = get_fundamentals_latest(conn)
    if fund_latest is None:
        results.append(("Fundamentals", "NO DATA", True))
        stale.append("Fundamentals")
    else:
        age = (today - fund_latest.date()).days
        # Fundamentals updated less frequently, use 7 day threshold
        is_stale = age > 7
        results.append(("Fundamentals", f"{fund_latest.date()} ({age}d ago, {fund_count} tickers)", is_stale))
        if is_stale:
            stale.append("Fundamentals")

    conn.close()

    # Output
    if args.brief:
        if stale:
            print(f"STALE: {', '.join(stale)}")
            sys.exit(1)
        else:
            print(f"OK: All data fresh (cutoff: {cutoff.date()})")
            sys.exit(0)

    if not args.quiet or stale:
        print(f"""
{'='*60}
  DATA FRESHNESS REPORT
  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  Cutoff: {cutoff.date()} ({args.max_age} trading days)
{'='*60}
""")
        for name, status, is_stale in results:
            flag = "[STALE]" if is_stale else "[OK]   "
            print(f"  {flag} {name:20} {status}")

        print(f"\n{'='*60}")
        if stale:
            print(f"  {len(stale)} table(s) need update: {', '.join(stale)}")
            sys.exit(1)
        else:
            print("  All tables up to date")
            sys.exit(0)

    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
