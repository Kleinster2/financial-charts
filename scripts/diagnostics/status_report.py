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


def get_sql_latest(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> tuple:
    """Get latest date and row count from a custom freshness query."""
    try:
        row = conn.execute(sql, params).fetchone()
        if row and row[0]:
            return datetime.strptime(str(row[0])[:10], "%Y-%m-%d"), row[1]
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
    cutoff_date = cutoff.date()
    today = datetime.now().date()

    checks = [
        {
            "name": "Stock Prices",
            "sql": """
                SELECT MAX(date(Date)), COUNT(*)
                FROM prices_long
                WHERE Close IS NOT NULL
                  AND Ticker IN ('SPY', 'QQQ', 'IWM', 'DIA')
            """,
            "source": "prices_long",
        },
        {
            "name": "Stock Volumes",
            "sql": """
                SELECT MAX(date(Date)), COUNT(*)
                FROM volumes_long
                WHERE Volume IS NOT NULL
                  AND Ticker IN ('SPY', 'QQQ', 'IWM', 'DIA')
            """,
            "source": "volumes_long",
        },
        {
            "name": "CBOE Indices",
            "table": "cboe_indices_daily",
            "date_col": "date",
            "source": "cboe_indices_daily",
        },
        {
            "name": "Implied Vol",
            "table": "implied_volatility_daily",
            "date_col": "date",
            "source": "implied_volatility_daily",
        },
        {
            "name": "Credit Spreads",
            "sql": """
                SELECT MAX(date(Date)), COUNT(*)
                FROM prices_long
                WHERE Close IS NOT NULL
                  AND Ticker IN ('BAMLH0A0HYM2', 'BAMLC0A0CM', 'BAMLC0A4CBBB')
            """,
            "source": "prices_long/FRED",
        },
        {
            "name": "FRED Yields",
            "sql": """
                SELECT
                    CASE WHEN COUNT(*) = 4 THEN MIN(latest_date) END,
                    COALESCE(SUM(row_count), 0)
                FROM (
                    SELECT Ticker, MAX(date(Date)) AS latest_date, COUNT(*) AS row_count
                    FROM prices_long
                    WHERE Close IS NOT NULL
                      AND Ticker IN ('DGS2', 'DGS5', 'DGS10', 'DGS30')
                    GROUP BY Ticker
                )
            """,
            "source": "prices_long/DGS2-DGS30",
        },
        {
            "name": "Futures Prices",
            "table": "futures_prices_long",
            "source": "futures_prices_long",
        },
        {
            "name": "Rate Futures",
            "table": "rate_futures_daily",
            "source": "rate_futures_daily",
        },
        {
            "name": "Individual Bonds",
            "table": "bond_prices_daily",
            "source": "bond_prices_daily",
            "manual": True,
        },
    ]

    results = []
    stale = []

    for check in checks:
        name = check["name"]
        if "sql" in check:
            latest, count = get_sql_latest(conn, check["sql"])
        else:
            latest, count = get_latest_date(
                conn,
                check["table"],
                check.get("date_col", "Date"),
            )

        source = check["source"]
        is_manual = check.get("manual", False)

        if latest is None:
            results.append((name, f"NO DATA [{source}]", True, is_manual))
            if not is_manual:
                stale.append(name)
        elif latest.date() < cutoff_date:
            age = (today - latest.date()).days
            status = f"{latest.date()} ({age}d ago"
            if count:
                status += f", {count:,} rows"
            status += f") [{source}]"
            results.append((name, status, True, is_manual))
            if not is_manual:
                stale.append(name)
        else:
            age = (today - latest.date()).days
            status = f"{latest.date()} ({age}d ago"
            if count:
                status += f", {count:,} rows"
            status += f") [{source}]"
            results.append((name, status, False, is_manual))

    # Check fundamentals separately (uses last_updated timestamp)
    fund_latest, fund_count = get_fundamentals_latest(conn)
    if fund_latest is None:
        results.append(("Fundamentals", "NO DATA [company_overview]", True, False))
        stale.append("Fundamentals")
    else:
        age = (today - fund_latest.date()).days
        # Fundamentals updated less frequently, use 7 day threshold
        is_stale = age > 7
        results.append(("Fundamentals", f"{fund_latest.date()} ({age}d ago, {fund_count} tickers) [company_overview]", is_stale, False))
        if is_stale:
            stale.append("Fundamentals")

    conn.close()

    # Output
    if args.brief:
        if stale:
            print(f"STALE: {', '.join(stale)}")
            sys.exit(1)
        else:
            print(f"OK: All data fresh (cutoff: {cutoff_date})")
            sys.exit(0)

    if not args.quiet or stale:
        print(f"""
{'='*60}
  DATA FRESHNESS REPORT
  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  Cutoff: {cutoff_date} ({args.max_age} trading days)
{'='*60}
""")
        for name, status, is_stale, is_manual in results:
            if is_manual and is_stale:
                flag = "[MANUAL]"
            else:
                flag = "[STALE]" if is_stale else "[OK]   "
            print(f"  {flag} {name:20} {status}")

        print(f"\n{'='*60}")
        if stale:
            print(f"  {len(stale)} table(s) need update: {', '.join(stale)}")
            sys.exit(1)
        else:
            print("  All tables up to date")
            print("  Manual sources are reported but do not fail freshness.")
            sys.exit(0)

    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
