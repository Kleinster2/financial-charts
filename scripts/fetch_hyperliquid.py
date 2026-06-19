"""
Fetch perpetual contract data from Hyperliquid API.

Collects:
  - Hourly candles → perp_candles table (for weekend/off-hours analysis)
  - Daily closes   → prices_long table (for chart compatibility, HL: prefix)
  - Funding rates  → perp_funding_rates table

Usage:
  python scripts/fetch_hyperliquid.py                    # all default contracts, 7 days, 30m
  python scripts/fetch_hyperliquid.py --lookback 30      # 30 days back
  python scripts/fetch_hyperliquid.py --contracts SP500 CL GOLD   # specific contracts
  python scripts/fetch_hyperliquid.py --funding-only     # only funding rates
  python scripts/fetch_hyperliquid.py --list              # list available contracts
  python scripts/fetch_hyperliquid.py --interval 1h      # hourly instead of 30m

No authentication required — all Hyperliquid market data is public.
"""

import os
import sys
import json
import time
import sqlite3
import logging
import argparse
from datetime import datetime, timezone, timedelta

import requests
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DB_PATH

log = logging.getLogger(__name__)

API_URL = "https://api.hyperliquid.xyz/info"

# Mapping: our ticker label → Hyperliquid symbol
# HL: prefix distinguishes from regular tickers in prices_long
DEFAULT_CONTRACTS = {
    "HL:SP500":  "xyz:SP500",
    "HL:CL":     "xyz:CL",
    "HL:GOLD":   "xyz:GOLD",
    "HL:SILVER": "xyz:SILVER",
    "HL:VIX":    "xyz:VIX",
    "HL:NATGAS": "xyz:NATGAS",
    "HL:COPPER": "xyz:COPPER",
    "HL:DXY":    "xyz:DXY",
}

# Reverse lookup for CLI convenience: user types "SP500", we resolve
SHORT_NAMES = {v.split(":")[1]: k for k, v in DEFAULT_CONTRACTS.items()}

MAX_CANDLES = 5000
MAX_FUNDING = 500
REQUEST_DELAY = 0.3  # seconds between API calls (stay within 1200 weight/min)


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def _post(payload: dict) -> list:
    """POST to Hyperliquid info endpoint."""
    resp = requests.post(API_URL, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_candles(symbol: str, interval: str, start_ms: int, end_ms: int) -> list:
    """Fetch candle data, paginating if needed (max 5000 per call)."""
    all_candles = []
    cursor = start_ms
    while cursor < end_ms:
        payload = {
            "type": "candleSnapshot",
            "req": {
                "coin": symbol,
                "interval": interval,
                "startTime": cursor,
                "endTime": end_ms,
            }
        }
        batch = _post(payload)
        if not batch:
            break
        all_candles.extend(batch)
        # Advance cursor past last candle
        last_t = batch[-1]["T"]
        if last_t <= cursor:
            break
        cursor = last_t + 1
        if len(batch) < MAX_CANDLES:
            break
        time.sleep(REQUEST_DELAY)
    return all_candles


def fetch_funding(symbol: str, start_ms: int, end_ms: int = None) -> list:
    """Fetch funding rate history, paginating if needed (max 500 per call)."""
    all_funding = []
    cursor = start_ms
    while True:
        payload = {
            "type": "fundingHistory",
            "coin": symbol,
            "startTime": cursor,
        }
        if end_ms:
            payload["endTime"] = end_ms
        batch = _post(payload)
        if not batch:
            break
        all_funding.extend(batch)
        last_t = batch[-1]["time"]
        if last_t <= cursor:
            break
        cursor = last_t + 1
        if len(batch) < MAX_FUNDING:
            break
        time.sleep(REQUEST_DELAY)
    return all_funding


def list_xyz_contracts():
    """List all trade.xyz HIP-3 contracts."""
    payload = {"type": "metaAndAssetCtxs", "dex": "xyz"}
    data = _post(payload)
    meta = data[0]  # universe metadata
    ctxs = data[1]  # live context (price, OI, etc.)
    results = []
    for asset, ctx in zip(meta["universe"], ctxs):
        name = asset['name']
        results.append({
            "symbol": name if ":" in name else f"xyz:{name}",
            "maxLeverage": asset.get("maxLeverage"),
            "markPx": ctx.get("markPx"),
            "funding": ctx.get("funding"),
            "openInterest": ctx.get("openInterest"),
            "dayNtlVlm": ctx.get("dayNtlVlm"),
        })
    return results


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------

def ensure_tables(conn: sqlite3.Connection):
    """Create perp-specific tables if they don't exist."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS perp_candles (
            timestamp TEXT NOT NULL,
            ticker TEXT NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume REAL,
            trades INTEGER,
            interval TEXT NOT NULL DEFAULT '1h',
            PRIMARY KEY (timestamp, ticker, interval)
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_perp_candles_ticker
        ON perp_candles(ticker)
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_perp_candles_ts
        ON perp_candles(timestamp)
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS perp_funding_rates (
            timestamp TEXT NOT NULL,
            ticker TEXT NOT NULL,
            funding_rate REAL,
            premium REAL,
            PRIMARY KEY (timestamp, ticker)
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_perp_funding_ticker
        ON perp_funding_rates(ticker)
    """)
    conn.commit()


def store_candles(conn: sqlite3.Connection, ticker: str, candles: list,
                  interval: str = "1h"):
    """Store candle data in perp_candles table."""
    if not candles:
        return 0
    rows = []
    for c in candles:
        ts = datetime.fromtimestamp(c["t"] / 1000, tz=timezone.utc)
        ts_str = ts.strftime("%Y-%m-%d %H:%M:%S")
        rows.append((
            ts_str, ticker,
            float(c["o"]), float(c["h"]), float(c["l"]), float(c["c"]),
            float(c["v"]), int(c["n"]),
            interval,
        ))
    conn.executemany(
        "INSERT OR REPLACE INTO perp_candles "
        "(timestamp, ticker, open, high, low, close, volume, trades, interval) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        rows
    )
    conn.commit()
    return len(rows)


def store_daily_closes(conn: sqlite3.Connection, ticker: str, candles: list):
    """Extract daily closes from hourly candles and store in prices_long."""
    if not candles:
        return 0
    # Group by date, take last candle of each day as daily close
    daily = {}
    for c in candles:
        ts = datetime.fromtimestamp(c["t"] / 1000, tz=timezone.utc)
        date_str = ts.strftime("%Y-%m-%d")
        # Keep overwriting — last candle of the day wins
        daily[date_str] = float(c["c"])

    rows = []
    for date_str, close in sorted(daily.items()):
        ts_str = f"{date_str} 00:00:00"
        rows.append((ts_str, ticker, close))

    conn.executemany(
        "INSERT OR REPLACE INTO prices_long (Date, Ticker, Close) "
        "VALUES (?, ?, ?)",
        rows
    )
    conn.commit()
    return len(rows)


def store_funding(conn: sqlite3.Connection, ticker: str, funding: list):
    """Store funding rate history."""
    if not funding:
        return 0
    rows = []
    for f in funding:
        ts = datetime.fromtimestamp(f["time"] / 1000, tz=timezone.utc)
        ts_str = ts.strftime("%Y-%m-%d %H:%M:%S")
        rows.append((
            ts_str, ticker,
            float(f["fundingRate"]),
            float(f["premium"]),
        ))
    conn.executemany(
        "INSERT OR REPLACE INTO perp_funding_rates "
        "(timestamp, ticker, funding_rate, premium) "
        "VALUES (?, ?, ?, ?)",
        rows
    )
    conn.commit()
    return len(rows)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Fetch Hyperliquid perpetual contract data"
    )
    parser.add_argument(
        "--contracts", nargs="+", default=None,
        help="Contract short names (e.g., SP500 CL GOLD). Default: all."
    )
    parser.add_argument(
        "--lookback", type=int, default=7,
        help="Days of history to fetch (default: 7)"
    )
    parser.add_argument(
        "--interval", default="30m",
        help="Candle interval (default: 30m). Options: 1m,5m,15m,30m,1h,4h,1d"
    )
    parser.add_argument(
        "--funding-only", action="store_true",
        help="Only fetch funding rates, skip candles"
    )
    parser.add_argument(
        "--candles-only", action="store_true",
        help="Only fetch candles, skip funding rates"
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List available trade.xyz contracts and exit"
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

    # List mode
    if args.list:
        log.info("Fetching trade.xyz contract list...")
        contracts = list_xyz_contracts()
        print(f"\n{'Symbol':<20} {'Price':<12} {'OI':<15} {'24h Vol':<15} {'Funding':<12} {'MaxLev'}")
        print("-" * 90)
        for c in sorted(contracts, key=lambda x: float(x["dayNtlVlm"] or 0), reverse=True):
            print(f"{c['symbol']:<20} {c['markPx'] or '-':<12} "
                  f"{c['openInterest'] or '-':<15} {c['dayNtlVlm'] or '-':<15} "
                  f"{c['funding'] or '-':<12} {c['maxLeverage'] or '-'}")
        return

    # Resolve contracts
    if args.contracts:
        selected = {}
        for name in args.contracts:
            name_upper = name.upper()
            if name_upper in SHORT_NAMES:
                hl_ticker = SHORT_NAMES[name_upper]
                selected[hl_ticker] = DEFAULT_CONTRACTS[hl_ticker]
            elif f"HL:{name_upper}" in DEFAULT_CONTRACTS:
                selected[f"HL:{name_upper}"] = DEFAULT_CONTRACTS[f"HL:{name_upper}"]
            else:
                # Assume it's a raw Hyperliquid symbol
                selected[f"HL:{name_upper}"] = f"xyz:{name_upper}"
        contracts = selected
    else:
        contracts = DEFAULT_CONTRACTS.copy()

    # Time range
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=args.lookback)
    start_ms = int(start.timestamp() * 1000)
    end_ms = int(now.timestamp() * 1000)

    log.info(f"Fetching {len(contracts)} contracts, {args.lookback} days back")
    log.info(f"Range: {start.strftime('%Y-%m-%d %H:%M')} → {now.strftime('%Y-%m-%d %H:%M')} UTC")

    # Database setup
    conn = sqlite3.connect(args.db)
    ensure_tables(conn)

    total_candles = 0
    total_daily = 0
    total_funding = 0

    for hl_ticker, hl_symbol in contracts.items():
        log.info(f"--- {hl_ticker} ({hl_symbol}) ---")

        # Candles
        if not args.funding_only:
            try:
                candles = fetch_candles(hl_symbol, args.interval, start_ms, end_ms)
                n = store_candles(conn, hl_ticker, candles, args.interval)
                total_candles += n
                log.info(f"  Candles: {n} rows stored ({args.interval})")

                # Daily closes for prices_long
                nd = store_daily_closes(conn, hl_ticker, candles)
                total_daily += nd
                log.info(f"  Daily closes: {nd} rows → prices_long")
            except Exception as e:
                log.error(f"  Candle fetch failed: {e}")
            time.sleep(REQUEST_DELAY)

        # Funding rates
        if not args.candles_only:
            try:
                funding = fetch_funding(hl_symbol, start_ms, end_ms)
                nf = store_funding(conn, hl_ticker, funding)
                total_funding += nf
                log.info(f"  Funding rates: {nf} rows stored")
            except Exception as e:
                log.error(f"  Funding fetch failed: {e}")
            time.sleep(REQUEST_DELAY)

    conn.close()

    log.info(f"\nDone. Candles: {total_candles}, Daily: {total_daily}, Funding: {total_funding}")


if __name__ == "__main__":
    main()
