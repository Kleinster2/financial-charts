"""
Fetch hourly candles for main assets from yfinance.

Stores in intraday_candles table with 30-day rolling retention.
Prunes data older than --retain days on each run.

Usage:
  python scripts/fetch_hourly_candles.py                  # all defaults, 30 days, 30m
  python scripts/fetch_hourly_candles.py --lookback 7     # last 7 days only
  python scripts/fetch_hourly_candles.py --tickers SPY QQQ  # specific tickers
  python scripts/fetch_hourly_candles.py --retain 60      # keep 60 days
  python scripts/fetch_hourly_candles.py --interval 1h    # hourly instead of 30m

Default tickers: SPY, QQQ, IWM, DIA, GLD, SLV, USO, UNG
Default interval: 30m (synchronized with Hyperliquid perp candles)
"""

import os
import sys
import sqlite3
import logging
import argparse
from datetime import datetime, timedelta, timezone

import yfinance as yf
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DB_PATH

log = logging.getLogger(__name__)

# Index ETFs + commodity ETFs matching perp coverage
DEFAULT_TICKERS = [
    "SPY",   # S&P 500     → HL:SP500
    "QQQ",   # Nasdaq 100
    "IWM",   # Russell 2000
    "DIA",   # Dow Jones
    "GLD",   # Gold         → HL:GOLD
    "SLV",   # Silver       → HL:SILVER
    "USO",   # WTI Crude    → HL:CL
    "UNG",   # Natural Gas  → HL:NATGAS
]

# Perp-to-ETF mapping for analytical comparisons
PERP_ETF_MAP = {
    "HL:SP500":  "SPY",
    "HL:GOLD":   "GLD",
    "HL:SILVER": "SLV",
    "HL:CL":     "USO",
    "HL:NATGAS": "UNG",
}


def ensure_table(conn: sqlite3.Connection):
    """Create intraday_candles table if it doesn't exist."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS intraday_candles (
            timestamp TEXT NOT NULL,
            ticker TEXT NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume REAL,
            interval TEXT NOT NULL DEFAULT '1h',
            PRIMARY KEY (timestamp, ticker, interval)
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_intraday_candles_ticker
        ON intraday_candles(ticker)
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_intraday_candles_ts
        ON intraday_candles(timestamp)
    """)
    conn.commit()


def prune_old_data(conn: sqlite3.Connection, retain_days: int):
    """Delete candles older than retain_days."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=retain_days)
    cutoff_str = cutoff.strftime("%Y-%m-%d %H:%M:%S")
    cursor = conn.execute(
        "DELETE FROM intraday_candles WHERE timestamp < ?", (cutoff_str,)
    )
    if cursor.rowcount > 0:
        conn.commit()
        log.info(f"Pruned {cursor.rowcount} rows older than {cutoff_str}")


def fetch_and_store(conn: sqlite3.Connection, ticker: str, lookback: int,
                    interval: str = "30m"):
    """Fetch hourly candles from yfinance and store."""
    period = f"{lookback}d"
    try:
        data = yf.download(
            ticker, period=period, interval=interval,
            progress=False, auto_adjust=True
        )
    except Exception as e:
        log.error(f"  yfinance download failed for {ticker}: {e}")
        return 0

    if data.empty:
        log.warning(f"  No data returned for {ticker}")
        return 0

    # yfinance returns timezone-aware index; normalize to UTC
    if data.index.tz is not None:
        data.index = data.index.tz_convert("UTC")
    else:
        data.index = data.index.tz_localize("UTC")

    # Handle MultiIndex columns from yfinance (when single ticker)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    rows = []
    for ts, row in data.iterrows():
        ts_str = ts.strftime("%Y-%m-%d %H:%M:%S")
        o = float(row["Open"]) if pd.notna(row["Open"]) else None
        h = float(row["High"]) if pd.notna(row["High"]) else None
        l = float(row["Low"]) if pd.notna(row["Low"]) else None
        c = float(row["Close"]) if pd.notna(row["Close"]) else None
        v = float(row["Volume"]) if pd.notna(row["Volume"]) else None
        if c is None:
            continue
        rows.append((ts_str, ticker, o, h, l, c, v, interval))

    if rows:
        conn.executemany(
            "INSERT OR REPLACE INTO intraday_candles "
            "(timestamp, ticker, open, high, low, close, volume, interval) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            rows
        )
        conn.commit()

    return len(rows)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch hourly candles for main assets (yfinance)"
    )
    parser.add_argument(
        "--tickers", nargs="+", default=None,
        help=f"Tickers to fetch. Default: {', '.join(DEFAULT_TICKERS)}"
    )
    parser.add_argument(
        "--lookback", type=int, default=30,
        help="Days of history to fetch (default: 30, max: 730)"
    )
    parser.add_argument(
        "--retain", type=int, default=30,
        help="Days of data to retain; older data is pruned (default: 30)"
    )
    parser.add_argument(
        "--interval", default="30m",
        help="Candle interval (default: 30m). Options: 1m,5m,15m,30m,1h"
    )
    parser.add_argument(
        "--no-prune", action="store_true",
        help="Skip pruning old data"
    )
    parser.add_argument(
        "--db", default=DB_PATH,
        help=f"Database path (default: {DB_PATH})"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    tickers = args.tickers or DEFAULT_TICKERS
    lookback = min(args.lookback, 730)

    log.info(f"Fetching {len(tickers)} tickers, {lookback} days back")

    conn = sqlite3.connect(args.db)
    ensure_table(conn)

    # Prune old data first
    if not args.no_prune:
        prune_old_data(conn, args.retain)

    total = 0
    for ticker in tickers:
        log.info(f"--- {ticker} ---")
        n = fetch_and_store(conn, ticker, lookback, args.interval)
        total += n
        log.info(f"  {n} candles stored ({args.interval})")

    conn.close()
    log.info(f"\nDone. Total: {total} rows across {len(tickers)} tickers")


if __name__ == "__main__":
    main()
