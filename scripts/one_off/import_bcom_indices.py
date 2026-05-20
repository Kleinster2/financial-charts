#!/usr/bin/env python3
"""
Import Bloomberg Commodity Index series into market_data.db.

Data source:
  Investing.com financialdata historical API

Series:
  BCOM   - Bloomberg Commodity Index
  BCOMTR - Bloomberg Commodity Index Total Return
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from curl_cffi import requests

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from constants import DB_PATH, get_db_connection  # noqa: E402


API_URL = "https://api.investing.com/api/financialdata/historical/{instrument_id}"
DATE_FMT = "%Y-%m-%d"


@dataclass(frozen=True)
class SeriesConfig:
    ticker: str
    name: str
    instrument_id: str
    start_date: date
    referer: str


SERIES = {
    "BCOM": SeriesConfig(
        ticker="BCOM",
        name="Bloomberg Commodity Index",
        instrument_id="948434",
        start_date=date(1991, 1, 1),
        referer="https://www.investing.com/indices/bloomberg-commodity-historical-data",
    ),
    "BCOMTR": SeriesConfig(
        ticker="BCOMTR",
        name="Bloomberg Commodity Index Total Return",
        instrument_id="951148",
        start_date=date(2001, 1, 1),
        referer="https://www.investing.com/indices/bbg-commodity-tr-historical-data",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Import BCOM and BCOMTR daily levels into market_data.db"
    )
    parser.add_argument(
        "--end-date",
        default=date.today().strftime(DATE_FMT),
        help="Last date to request from Investing.com (YYYY-MM-DD; default: today)",
    )
    parser.add_argument(
        "--start-date",
        default=None,
        help=(
            "First date to request (YYYY-MM-DD). "
            "Default: full configured history for each series"
        ),
    )
    parser.add_argument(
        "--chunk-years",
        type=int,
        default=5,
        help="Years per API request window (default: 5)",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.25,
        help="Pause between API requests in seconds (default: 0.25)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and validate but do not write to the database",
    )
    return parser.parse_args()


def date_windows(start: date, end: date, years: int) -> Iterable[Tuple[date, date]]:
    if years < 1:
        raise ValueError("--chunk-years must be >= 1")

    cursor = start
    while cursor <= end:
        try:
            window_end = cursor.replace(year=cursor.year + years) - timedelta(days=1)
        except ValueError:
            window_end = cursor.replace(month=2, day=28, year=cursor.year + years)
        if window_end > end:
            window_end = end
        yield cursor, window_end
        cursor = window_end + timedelta(days=1)


def request_headers(config: SeriesConfig) -> Dict[str, str]:
    return {
        "accept": "application/json, text/plain, */*",
        "domain-id": "www",
        "referer": config.referer,
        "user-agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/128.0.0.0 Safari/537.36"
        ),
    }


def parse_close(raw_value: object) -> float:
    if raw_value is None:
        raise ValueError("missing close")
    if isinstance(raw_value, (int, float)):
        return float(raw_value)
    return float(str(raw_value).replace(",", ""))


def fetch_window(config: SeriesConfig, start: date, end: date) -> List[dict]:
    headers = request_headers(config)
    params = {
        "start-date": start.strftime(DATE_FMT),
        "end-date": end.strftime(DATE_FMT),
        "time-frame": "Daily",
        "add-missing-rows": "false",
    }
    response = requests.get(
        API_URL.format(instrument_id=config.instrument_id),
        params=params,
        headers=headers,
        impersonate="chrome120",
        timeout=60,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"{config.ticker} {start}..{end} returned HTTP {response.status_code}: "
            f"{response.text[:200]}"
        )

    payload = response.json()
    return payload.get("data") or []


def merge_rows(values: Dict[str, float], rows: List[dict]) -> None:
    for row in rows:
        timestamp = row.get("rowDateTimestamp") or ""
        day = timestamp[:10]
        if not day:
            continue
        close_raw = row.get("last_closeRaw", row.get("last_close"))
        try:
            close = parse_close(close_raw)
        except ValueError:
            continue
        values[f"{day} 00:00:00"] = close


def sparse_years(
    values: Dict[str, float],
    config: SeriesConfig,
    end_date: date,
    min_full_year_rows: int = 200,
) -> List[int]:
    counts: Dict[int, int] = {}
    for db_date in values:
        counts[int(db_date[:4])] = counts.get(int(db_date[:4]), 0) + 1

    sparse: List[int] = []
    for year in range(config.start_date.year, end_date.year + 1):
        # BCOMTR's public Investing.com history starts during 2001, and the
        # current end year is often partial. Do not treat those as gaps.
        if year == config.start_date.year:
            continue
        if year == end_date.year and end_date < date(year, 12, 15):
            continue
        if counts.get(year, 0) < min_full_year_rows:
            sparse.append(year)
    return sparse


def fetch_and_merge(
    config: SeriesConfig,
    values: Dict[str, float],
    start: date,
    end: date,
    sleep: float,
    label: str = "",
) -> None:
    rows = fetch_window(config, start, end)
    prefix = f"  {label} " if label else "  "
    print(f"{prefix}{start}..{end}: {len(rows):,} rows")
    merge_rows(values, rows)
    if sleep > 0:
        time.sleep(sleep)


def fetch_series(
    config: SeriesConfig,
    end_date: date,
    chunk_years: int,
    sleep: float,
    start_date: date | None = None,
) -> List[Tuple[str, float]]:
    values: Dict[str, float] = {}
    fetch_start = max(config.start_date, start_date) if start_date else config.start_date

    print(f"\nFetching {config.ticker} ({config.instrument_id})")
    for start, end in date_windows(fetch_start, end_date, chunk_years):
        fetch_and_merge(config, values, start, end, sleep)

    # Investing.com occasionally returns sparse data for one window size and
    # complete data for another. Backfill sparse full years with annual windows,
    # then with a surrounding five-year window if the annual request is sparse.
    if start_date is None:
        candidate_sparse_years = sparse_years(values, config, end_date)
    else:
        candidate_sparse_years = []

    for year in candidate_sparse_years:
        start = date(year, 1, 1)
        end = date(year, 12, 31)
        fetch_and_merge(config, values, start, end, sleep, label="annual backfill")

    if start_date is None:
        candidate_sparse_years = sparse_years(values, config, end_date)

    for year in candidate_sparse_years:
        start = date(max(config.start_date.year, year - 2), 1, 1)
        end = date(min(end_date.year, year + 2), 12, 31)
        if end > end_date:
            end = end_date
        fetch_and_merge(config, values, start, end, sleep, label="range backfill")

    if start_date is None:
        remaining_sparse = sparse_years(values, config, end_date)
        if remaining_sparse:
            print(f"  Warning: sparse years remain for {config.ticker}: {remaining_sparse}")

    result = sorted(values.items())
    if not result:
        raise RuntimeError(f"No rows fetched for {config.ticker}")
    return result


def max_sqlite_columns(conn: sqlite3.Connection) -> int:
    options = [row[0] for row in conn.execute("PRAGMA compile_options").fetchall()]
    for option in options:
        match = re.match(r"MAX_COLUMN=(\d+)", option)
        if match:
            return int(match.group(1))
    return 2000


def ensure_prices_long(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS prices_long (
            Date TEXT NOT NULL,
            Ticker TEXT NOT NULL,
            Close REAL,
            PRIMARY KEY (Date, Ticker)
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_prices_long_ticker ON prices_long(Ticker)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_prices_long_date ON prices_long(Date)")


def maybe_update_wide_table(
    conn: sqlite3.Connection,
    fetched: Dict[str, List[Tuple[str, float]]],
) -> List[str]:
    table_row = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily'"
    ).fetchone()
    if not table_row:
        print("\nWide table stock_prices_daily not found; skipping wide-table write.")
        return []

    pragma = conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()
    existing_cols = {row[1] for row in pragma}
    missing = [ticker for ticker in fetched if ticker not in existing_cols]
    max_cols = max_sqlite_columns(conn)
    available_slots = max_cols - len(pragma)

    if missing and len(missing) > available_slots:
        print(
            "\nWide table is full: "
            f"{len(pragma):,}/{max_cols:,} columns. "
            f"Skipping new wide columns: {', '.join(missing)}"
        )
        wide_tickers = [ticker for ticker in fetched if ticker in existing_cols]
    else:
        wide_tickers = list(fetched)
        for ticker in missing:
            print(f"Adding wide-table column {ticker}")
            conn.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')

    if not wide_tickers:
        return []

    print(f"\nUpdating wide table for: {', '.join(wide_tickers)}")
    for ticker in wide_tickers:
        for db_date, close in fetched[ticker]:
            exists = conn.execute(
                "SELECT 1 FROM stock_prices_daily WHERE Date = ?",
                (db_date,),
            ).fetchone()
            if exists:
                conn.execute(
                    f'UPDATE stock_prices_daily SET "{ticker}" = ? WHERE Date = ?',
                    (close, db_date),
                )
            else:
                conn.execute(
                    f'INSERT INTO stock_prices_daily (Date, "{ticker}") VALUES (?, ?)',
                    (db_date, close),
                )
    return wide_tickers


def write_database(fetched: Dict[str, List[Tuple[str, float]]]) -> None:
    conn = get_db_connection(row_factory=None)
    try:
        ensure_prices_long(conn)

        print("\nWriting prices_long")
        for ticker, rows in fetched.items():
            conn.executemany(
                "INSERT OR REPLACE INTO prices_long (Date, Ticker, Close) VALUES (?, ?, ?)",
                [(db_date, ticker, close) for db_date, close in rows],
            )
            print(f"  {ticker}: upserted {len(rows):,} rows")

        wide_written = maybe_update_wide_table(conn, fetched)

        print("\nUpdating ticker_metadata")
        for ticker in fetched:
            config = SERIES[ticker]
            first_date, last_date, data_points = conn.execute(
                "SELECT MIN(Date), MAX(Date), COUNT(*) FROM prices_long WHERE Ticker = ?",
                (ticker,),
            ).fetchone()
            if not first_date:
                raise RuntimeError(f"No prices_long rows found for {ticker} after upsert")
            table_name = "stock_prices_daily" if ticker in wide_written else "prices_long"
            conn.execute(
                """
                INSERT OR REPLACE INTO ticker_metadata
                    (ticker, name, table_name, data_type, first_date, last_date, data_points)
                VALUES (?, ?, ?, 'index', ?, ?, ?)
                """,
                (ticker, config.name, table_name, first_date, last_date, data_points),
            )
            print(
                f"  {ticker}: {first_date[:10]}..{last_date[:10]} "
                f"({data_points:,} rows, {table_name})"
            )

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def verify_database(tickers: Iterable[str]) -> None:
    conn = get_db_connection(row_factory=None)
    try:
        print("\nVerification")
        for ticker in tickers:
            stats = conn.execute(
                "SELECT MIN(Date), MAX(Date), COUNT(*) FROM prices_long WHERE Ticker = ?",
                (ticker,),
            ).fetchone()
            latest = conn.execute(
                """
                SELECT Date, Close
                FROM prices_long
                WHERE Ticker = ?
                ORDER BY Date DESC
                LIMIT 3
                """,
                (ticker,),
            ).fetchall()
            apr30 = conn.execute(
                """
                SELECT Close
                FROM prices_long
                WHERE Ticker = ? AND Date = '2026-04-30 00:00:00'
                """,
                (ticker,),
            ).fetchone()
            print(f"  {ticker}: {stats[0]}..{stats[1]} ({stats[2]:,} rows)")
            print(f"    latest: {latest}")
            if apr30:
                print(f"    2026-04-30 close: {apr30[0]:.6f}")
    finally:
        conn.close()


def print_fetch_summary(fetched: Dict[str, List[Tuple[str, float]]]) -> None:
    print("\nFetched series summary")
    for ticker, rows in fetched.items():
        latest_date, latest_close = rows[-1]
        first_date, first_close = rows[0]
        print(
            f"  {ticker}: {len(rows):,} rows, "
            f"{first_date[:10]} ({first_close:.6f}) to "
            f"{latest_date[:10]} ({latest_close:.6f})"
        )
        apr30 = next((close for db_date, close in rows if db_date == "2026-04-30 00:00:00"), None)
        if apr30 is not None:
            print(f"    2026-04-30 close: {apr30:.6f}")


def main() -> int:
    args = parse_args()
    end_date = datetime.strptime(args.end_date, DATE_FMT).date()
    start_date = datetime.strptime(args.start_date, DATE_FMT).date() if args.start_date else None
    if end_date < min(config.start_date for config in SERIES.values()):
        raise ValueError("--end-date is before all configured series start dates")
    if start_date and start_date > end_date:
        raise ValueError("--start-date is after --end-date")

    print(f"Database: {DB_PATH}")
    if start_date:
        print(f"Requested start date: {start_date}")
    print(f"Requested end date: {end_date}")

    fetched = {
        ticker: fetch_series(config, end_date, args.chunk_years, args.sleep, start_date=start_date)
        for ticker, config in SERIES.items()
        if config.start_date <= end_date and (start_date is None or start_date <= end_date)
    }
    print_fetch_summary(fetched)

    if args.dry_run:
        print("\nDry run complete; database not changed.")
        return 0

    write_database(fetched)
    verify_database(fetched.keys())
    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
