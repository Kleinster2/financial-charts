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
from brazil_rate_series_registry import (
    BRAZIL_RATE_FREQUENCY_LAG_DAYS,
    FREQUENCY_DAILY as BRAZIL_FREQUENCY_DAILY,
    active_brazil_rate_series,
)
from fred_series_registry import (
    FRED_FREQUENCY_LAG_DAYS,
    FREQUENCY_DAILY,
    active_prices_long_fred_series,
)


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


def get_fred_registry_freshness(
    conn: sqlite3.Connection,
    max_age: int,
    today,
) -> tuple[tuple[str, str, bool, bool], str | None]:
    """Check every active FRED registry series that is present in prices_long."""
    registry = active_prices_long_fred_series()
    if not registry:
        return ("FRED Series", "NO REGISTRY [prices_long/FRED]", True, False), "FRED Series"

    placeholders = ",".join("?" for _ in registry)
    rows = conn.execute(
        f"""
        SELECT Ticker, MAX(date(Date)), COUNT(*)
        FROM prices_long
        WHERE Close IS NOT NULL
          AND Ticker IN ({placeholders})
        GROUP BY Ticker
        """,
        tuple(registry.keys()),
    ).fetchall()
    present = {row[0]: (row[1], row[2]) for row in rows}

    daily_cutoff = trading_days_ago(max_age).date()
    checked = []
    stale_items = []
    missing_items = []
    oldest_by_frequency = {}
    total_rows = 0

    for code, series in sorted(registry.items()):
        row = present.get(code)
        if row is None:
            missing_items.append(f"{code} NO DATA")
            continue

        latest = datetime.strptime(str(row[0])[:10], "%Y-%m-%d").date()
        total_rows += row[1]
        checked.append(code)
        oldest = oldest_by_frequency.get(series.frequency)
        if oldest is None or latest < oldest:
            oldest_by_frequency[series.frequency] = latest

        if series.allowed_lag_days is not None:
            cutoff = today - timedelta(days=series.allowed_lag_days)
        elif series.frequency == FREQUENCY_DAILY:
            cutoff = daily_cutoff
        else:
            allowed_lag = series.allowed_lag_days or FRED_FREQUENCY_LAG_DAYS[series.frequency]
            cutoff = today - timedelta(days=allowed_lag)

        if latest < cutoff:
            age = (today - latest).days
            stale_items.append(f"{code} {latest} ({age}d, {series.frequency})")

    if stale_items or missing_items:
        details = stale_items + missing_items
        status = (
            f"{len(details)} stale/missing of {len(checked) + len(missing_items)} checked: "
            f"{', '.join(details)} [{total_rows:,} rows, prices_long/FRED registry]"
        )
        stale_label = f"FRED Series ({', '.join(item.split()[0] for item in details)})"
        return ("FRED Series", status, True, False), stale_label

    freshness_bits = [
        f"{frequency} oldest {latest}"
        for frequency, latest in sorted(oldest_by_frequency.items())
    ]
    status = (
        f"{len(checked)} checked; {', '.join(freshness_bits)} "
        f"({total_rows:,} rows) [prices_long/FRED registry]"
    )
    return ("FRED Series", status, False, False), None


def get_brazil_rate_freshness(
    conn: sqlite3.Connection,
    max_age: int,
    today,
) -> tuple[tuple[str, str, bool, bool], str | None]:
    """Check every active Brazil rate series expected in prices_long."""
    registry = active_brazil_rate_series()
    placeholders = ",".join("?" for _ in registry)
    rows = conn.execute(
        f"""
        SELECT Ticker, MAX(date(Date)), COUNT(*)
        FROM prices_long
        WHERE Close IS NOT NULL
          AND Ticker IN ({placeholders})
        GROUP BY Ticker
        """,
        tuple(registry.keys()),
    ).fetchall()
    present = {row[0]: (row[1], row[2]) for row in rows}

    daily_cutoff = trading_days_ago(max_age).date()
    checked = []
    stale_items = []
    missing_items = []
    oldest_by_source = {}
    total_rows = 0

    for code, series in sorted(registry.items()):
        row = present.get(code)
        if row is None:
            if series.required:
                missing_items.append(f"{code} NO DATA")
            continue

        latest = datetime.strptime(str(row[0])[:10], "%Y-%m-%d").date()
        total_rows += row[1]
        checked.append(code)
        oldest = oldest_by_source.get(series.source)
        if oldest is None or latest < oldest:
            oldest_by_source[series.source] = latest

        if series.allowed_lag_days is not None:
            cutoff = today - timedelta(days=series.allowed_lag_days)
        elif series.frequency == BRAZIL_FREQUENCY_DAILY:
            cutoff = daily_cutoff
        else:
            allowed_lag = BRAZIL_RATE_FREQUENCY_LAG_DAYS[series.frequency]
            cutoff = today - timedelta(days=allowed_lag)

        if latest < cutoff:
            age = (today - latest).days
            stale_items.append(f"{code} {latest} ({age}d, {series.source})")

    if stale_items or missing_items:
        details = stale_items + missing_items
        status = (
            f"{len(details)} stale/missing of {len(checked) + len(missing_items)} checked: "
            f"{', '.join(details)} [{total_rows:,} rows, prices_long/Brazil rates]"
        )
        stale_label = f"Brazil Rates ({', '.join(item.split()[0] for item in details)})"
        return ("Brazil Rates", status, True, False), stale_label

    freshness_bits = [
        f"{source} oldest {latest}"
        for source, latest in sorted(oldest_by_source.items())
    ]
    status = (
        f"{len(checked)} checked; {', '.join(freshness_bits)} "
        f"({total_rows:,} rows) [prices_long/Brazil rates]"
    )
    return ("Brazil Rates", status, False, False), None


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

    fred_result, fred_stale = get_fred_registry_freshness(conn, args.max_age, today)
    results.append(fred_result)
    if fred_stale:
        stale.append(fred_stale)

    brazil_result, brazil_stale = get_brazil_rate_freshness(conn, args.max_age, today)
    results.append(brazil_result)
    if brazil_stale:
        stale.append(brazil_stale)

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
