#!/usr/bin/env python3
"""
Persist the ZQ (Fed Funds) and SR3 (3-month SOFR) futures strips to the DB.

Creates `rate_futures_daily` on first run, then backfills and/or appends.
Read side:  scripts/fed_rate_expectations.py (currently downloads fresh each call;
            after this script runs a few times, swap that script to prefer DB).

DATA SOURCE LIMITATIONS (May 2026):
    ZQ  — yfinance returns up to ~2 years of per-contract daily history. Backfill works.
    SR3 — yfinance returns ONLY today's snapshot per contract (period flag ignored).
          Stooq has no coverage either. Free-tier providers do not give SR3 history.
          Practical path: run this script daily to accumulate SR3 history going forward.
          For a one-shot historical SR3 strip, you need CME QuikStrike (paid) or to
          scrape Barchart / Investing.com (fragile). Both are out of scope for this script.

Schema:
    Date            TEXT       'YYYY-MM-DD HH:MM:SS' to match the rest of the DB
    contract        TEXT       'ZQK26.CBT', 'SR3M27.CME', ...
    root            TEXT       'ZQ' or 'SR3'
    delivery_year   INTEGER    e.g. 2026
    delivery_month  INTEGER    1-12
    delivery_code   TEXT       single-letter CME month code (F G H J K M N Q U V X Z)
    price           REAL       futures close (e.g. 96.3650)
    implied_rate    REAL       100 - price (annualized %, e.g. 3.6350)
    PRIMARY KEY (Date, contract)

Usage:
    python scripts/update_rate_futures.py                    # incremental daily update
    python scripts/update_rate_futures.py --backfill         # fetch full history per contract
    python scripts/update_rate_futures.py --backfill --period 5y
    python scripts/update_rate_futures.py --roots ZQ         # ZQ only
    python scripts/update_rate_futures.py --years-out 4      # enumerate 4 years of contracts
    python scripts/update_rate_futures.py --table-only       # print a summary, no writes
"""
from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from datetime import datetime, date
from pathlib import Path
from typing import Iterable

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import logging
import pandas as pd
import yfinance as yf

logging.getLogger("yfinance").setLevel(logging.CRITICAL)

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = REPO_ROOT / "market_data.db"

MONTH_CODES = {
    "F": (1, "Jan"), "G": (2, "Feb"), "H": (3, "Mar"), "J": (4, "Apr"),
    "K": (5, "May"), "M": (6, "Jun"), "N": (7, "Jul"), "Q": (8, "Aug"),
    "U": (9, "Sep"), "V": (10, "Oct"), "X": (11, "Nov"), "Z": (12, "Dec"),
}
ALL_CODES = ["F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z"]
QUARTERLY_CODES = ["H", "M", "U", "Z"]   # IMM months — SR3 lists quarterly

ROOT_SPECS = {
    "ZQ":  {"exchange": "CBT", "codes": ALL_CODES,       "lists_n_years": 3},
    "SR3": {"exchange": "CME", "codes": QUARTERLY_CODES, "lists_n_years": 5},
}


def build_symbol(root: str, code: str, year: int) -> str:
    """Build yfinance contract symbol. yy is the 2-digit year."""
    yy = year % 100
    spec = ROOT_SPECS[root]
    return f"{root}{code}{yy:02d}.{spec['exchange']}"


def enumerate_contracts(roots: Iterable[str], years_out: int) -> list[tuple[str, str, int]]:
    """Return list of (root, code, year) tuples for contracts to query.

    For an incremental update we want active contracts (delivery month >= today).
    For backfill the caller can pass a wider years_out window to also pick up
    contracts already expired — yfinance still returns their final-quote history.
    """
    today = date.today()
    results: list[tuple[str, str, int]] = []
    for root in roots:
        codes = ROOT_SPECS[root]["codes"]
        # Range starts at current_year - 1 to catch contracts that expired
        # this year but still have useful trailing history
        for year in range(today.year - 1, today.year + years_out):
            for code in codes:
                month = MONTH_CODES[code][0]
                # Skip clearly future-listings beyond exchange listing depth
                if year > today.year + ROOT_SPECS[root]["lists_n_years"]:
                    continue
                results.append((root, code, year))
    return results


def ensure_table(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS rate_futures_daily (
            Date           TEXT    NOT NULL,
            contract       TEXT    NOT NULL,
            root           TEXT    NOT NULL,
            delivery_year  INTEGER NOT NULL,
            delivery_month INTEGER NOT NULL,
            delivery_code  TEXT    NOT NULL,
            price          REAL    NOT NULL,
            implied_rate   REAL    NOT NULL,
            PRIMARY KEY (Date, contract)
        );
        CREATE INDEX IF NOT EXISTS idx_rfd_contract ON rate_futures_daily(contract);
        CREATE INDEX IF NOT EXISTS idx_rfd_date     ON rate_futures_daily(Date);
        CREATE INDEX IF NOT EXISTS idx_rfd_root     ON rate_futures_daily(root, delivery_year, delivery_month);
        """
    )
    conn.commit()


def fetch_contract_history(symbol: str, period: str) -> pd.DataFrame | None:
    """Pull yfinance OHLC for a contract. Return DataFrame indexed by Date with 'Close'."""
    try:
        t = yf.Ticker(symbol)
        hist = t.history(period=period)
    except Exception:
        return None
    if hist is None or hist.empty:
        return None
    df = hist[["Close"]].copy()
    df = df[df["Close"].notna()]
    if df.empty:
        return None
    return df


def upsert_rows(conn: sqlite3.Connection, rows: list[tuple]) -> int:
    if not rows:
        return 0
    cur = conn.cursor()
    cur.executemany(
        """
        INSERT INTO rate_futures_daily
            (Date, contract, root, delivery_year, delivery_month,
             delivery_code, price, implied_rate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(Date, contract) DO UPDATE SET
            price        = excluded.price,
            implied_rate = excluded.implied_rate
        """,
        rows,
    )
    conn.commit()
    return cur.rowcount


def run(roots: list[str], years_out: int, period: str, backfill: bool,
        table_only: bool) -> None:
    contracts = enumerate_contracts(roots, years_out=years_out)
    print(f"Enumerated {len(contracts)} contract slots "
          f"(roots={roots}, years_out={years_out}, period={period})")

    if table_only:
        print("--table-only: skipping fetch + write")
        return

    conn = sqlite3.connect(DB_PATH)
    ensure_table(conn)

    # When not backfilling, only fetch ~5 days history per contract — cheap incremental
    fetch_period = period if backfill else "5d"

    total_rows = 0
    total_contracts_with_data = 0
    failed = 0

    for i, (root, code, year) in enumerate(contracts, 1):
        symbol = build_symbol(root, code, year)
        month_num, month_name = MONTH_CODES[code]
        df = fetch_contract_history(symbol, fetch_period)
        if df is None:
            failed += 1
            if i % 25 == 0 or i == len(contracts):
                print(f"  [{i}/{len(contracts)}] last={symbol} (no data)")
            continue

        rows: list[tuple] = []
        for ts, row in df.iterrows():
            # Normalize to the 'YYYY-MM-DD HH:MM:SS' convention the rest of the DB uses
            date_str = pd.Timestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
            price = float(row["Close"])
            implied = 100.0 - price
            rows.append((date_str, symbol, root, year, month_num,
                         code, price, implied))
        written = upsert_rows(conn, rows)
        total_rows += len(rows)
        total_contracts_with_data += 1
        if i % 25 == 0 or i == len(contracts):
            print(f"  [{i}/{len(contracts)}] last={symbol} rows={len(rows):3} "
                  f"latest={df.index[-1].strftime('%Y-%m-%d')} "
                  f"price={df['Close'].iloc[-1]:.4f}")

    print()
    print(f"Contracts fetched : {total_contracts_with_data}/{len(contracts)} "
          f"(failed: {failed})")
    print(f"Rows written      : {total_rows}")

    # Quick summary by root
    cur = conn.cursor()
    cur.execute(
        """
        SELECT root,
               COUNT(DISTINCT contract) AS contracts,
               COUNT(*) AS rows,
               MIN(Date) AS first_date,
               MAX(Date) AS last_date
          FROM rate_futures_daily
         GROUP BY root
         ORDER BY root
        """
    )
    print()
    print(f"{'Root':<6}{'Contracts':>11}{'Rows':>10}  {'First':<12}{'Last':<12}")
    print("-" * 55)
    for root, n_contracts, n_rows, first, last in cur.fetchall():
        first_s = first.split(" ")[0] if first else "-"
        last_s  = last.split(" ")[0]  if last  else "-"
        print(f"{root:<6}{n_contracts:>11}{n_rows:>10}  {first_s:<12}{last_s:<12}")
    conn.close()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Persist ZQ + SR3 rate-futures strip to market_data.db")
    p.add_argument("--roots", nargs="+", choices=["ZQ", "SR3"], default=["ZQ", "SR3"])
    p.add_argument("--years-out", type=int, default=3,
                   help="Enumerate contracts up to N years past current year (default 3)")
    p.add_argument("--period", default="2y",
                   help="yfinance lookback period for --backfill mode (default 2y; try 5y, max)")
    p.add_argument("--backfill", action="store_true",
                   help="Pull full per-contract history (slower; use sparingly)")
    p.add_argument("--table-only", action="store_true",
                   help="Print enumeration summary without fetching / writing")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    run(
        roots=args.roots,
        years_out=args.years_out,
        period=args.period,
        backfill=args.backfill,
        table_only=args.table_only,
    )


if __name__ == "__main__":
    main()
