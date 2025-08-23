"""
Populate missing ticker names in ticker_metadata for any asset type present in stock_prices_daily.
- Uses yfinance when available to fetch longName/shortName and quoteType.
- Falls back to heuristic naming for FX (e.g., AUDUSD=X -> AUD/USD) and Crypto (e.g., AAVE-USD -> AAVE/USD).
- Preserves first_date, last_date, data_points by computing from stock_prices_daily.

Usage examples:
  python populate_missing_metadata.py --limit 200
  python populate_missing_metadata.py --types fx,crypto --limit 250
  python populate_missing_metadata.py --tickers "AAPL MSFT AUDUSD=X BTC-USD" --limit 50
"""
import argparse
import os
import re
import sqlite3
from typing import Optional, Tuple

from constants import DB_PATH, get_db_connection

try:
    import yfinance as yf
    _HAS_YF = True
except Exception:
    _HAS_YF = False

# Stable manual names for special tickers that often 404 on APIs
FIXED_NAMES = {
    "^DXY": "US Dollar Index",
    "DX-Y.NYB": "US Dollar Index (ICE)",
    "DX=F": "US Dollar Index Futures",
    "^RVX": "Cboe Russell 2000 Volatility Index",
    "^VXMT": "Cboe S&P 500 6-Month Volatility Index",
    "^VXST": "Cboe S&P 500 9-Day Volatility Index",
}


def _get_data_range(cursor: sqlite3.Cursor, ticker: str, dtype: Optional[str]):
    """Return (first_date, last_date, data_points) for ticker from the appropriate table.
    Uses futures_prices_daily for futures; stock_prices_daily for everything else.
    """
    table = 'futures_prices_daily' if (dtype and dtype.lower() == 'future') else 'stock_prices_daily'
    cursor.execute(
        f"""
        SELECT MIN(Date) AS first_date,
               MAX(Date) AS last_date,
               COUNT(*)   AS data_points
        FROM {table}
        WHERE "{ticker}" IS NOT NULL
        """
    )
    row = cursor.fetchone()
    return row if row else (None, None, 0)


def _infer_type_by_pattern(t: str) -> Optional[str]:
    if t.endswith("=X"):
        return "fx"
    if re.search(r"-(USD|USDT|EUR|BTC)$", t):
        return "crypto"
    if t.endswith("=F"):
        return "future"
    return None


def _yf_name_and_type(ticker: str) -> Tuple[Optional[str], Optional[str]]:
    if not _HAS_YF:
        return None, None
    try:
        t = yf.Ticker(ticker)
        info = {}
        try:
            info = t.get_info()
        except Exception:
            try:
                info = t.info
            except Exception:
                info = {}
        name = (info.get("longName") or info.get("shortName") or info.get("displayName") or "").strip()
        qt = str(info.get("quoteType") or "").upper()
        dtype = None
        if qt == "ETF":
            dtype = "etf"
        elif qt in ("EQUITY", "MUTUALFUND"):
            dtype = "stock"
        elif qt == "CURRENCY":
            dtype = "fx"
        elif qt == "CRYPTOCURRENCY":
            dtype = "crypto"
        elif qt == "FUTURE":
            dtype = "future"
        else:
            # Fallback by pattern
            dtype = _infer_type_by_pattern(ticker)
        return (name if name else None), dtype
    except Exception:
        return None, None


def _heuristic_name(t: str) -> Optional[str]:
    if t.endswith("=X") and len(t) >= 7:
        # e.g., AUDUSD=X -> AUD/USD
        base = t[:-2]
        if len(base) == 6:
            return f"{base[:3]}/{base[3:]}"
        # Best-effort split
        return base.replace("USD", "/USD")
    m = re.match(r"^([A-Z0-9]+)-(USD|USDT|EUR|BTC)$", t)
    if m:
        return f"{m.group(1)}/{m.group(2)}"
    return None


def _fallback_name_from_stock_metadata(cursor: sqlite3.Cursor, ticker: str) -> Optional[str]:
    """Fallback to legacy stock_metadata table for a display name if present."""
    try:
        cursor.execute("SELECT name FROM stock_metadata WHERE ticker = ?", (ticker,))
        row = cursor.fetchone()
        if row and row[0]:
            name = str(row[0]).strip()
            return name or None
    except Exception:
        return None
    return None


def main():
    parser = argparse.ArgumentParser(description="Auto-fill missing ticker names in ticker_metadata for any asset type.")
    parser.add_argument("--limit", type=int, default=200, help="Maximum number of tickers to process")
    parser.add_argument("--tickers", type=str, default="", help="Comma/space-separated list to restrict the scope")
    parser.add_argument("--types", type=str, default="", help="Only process these types (fx,crypto,stock,etf,future)")
    parser.add_argument("--allow-empty", action="store_true", help="Allow insert even when the ticker has zero data points")
    parser.add_argument("--fallback-ticker-name", action="store_true", help="If no name found, use the ticker symbol as the name")
    args = parser.parse_args()

    types_filter = set()
    if args.types:
        types_filter = {s.strip().lower() for s in re.split(r"[\s,]+", args.types) if s.strip()}

    print("=== Populate missing ticker metadata (all asset types) ===")
    print(f"Using database: {DB_PATH}")
    if not os.path.exists(DB_PATH):
        print(f"Database not found: {DB_PATH}")
        return

    conn = get_db_connection()
    cur = conn.cursor()

    # Gather universe from both spot and futures price tables (if they exist)
    columns: list[str] = []
    price_tables = []
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_prices_daily'")
        if cur.fetchone():
            price_tables.append('stock_prices_daily')
    except Exception:
        pass
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='futures_prices_daily'")
        if cur.fetchone():
            price_tables.append('futures_prices_daily')
    except Exception:
        pass

    for tbl in price_tables:
        try:
            cur.execute(f"PRAGMA table_info({tbl})")
            cols = [r[1] for r in cur.fetchall() if r[1] != 'Date']
            columns.extend(cols)
        except Exception:
            continue
    # Deduplicate
    columns = sorted(set(columns))

    # Find unknowns
    placeholders = ",".join(["?"] * len(columns)) if columns else None
    known = set()
    if placeholders:
        try:
            cur.execute(
                f"SELECT ticker FROM ticker_metadata WHERE ticker IN ({placeholders}) AND COALESCE(NULLIF(name,''), NULL) IS NOT NULL",
                columns,
            )
            known = {row[0] for row in cur.fetchall()}
        except Exception:
            known = set()

    unknown = [t for t in columns if t not in known]

    # Optional ticker scope filter
    if args.tickers:
        scope = {s.strip().upper() for s in re.split(r"[\s,]+", args.tickers) if s.strip()}
        unknown = [t for t in unknown if t in scope]

    # Optional type filter: pre-filter by pattern to reduce yfinance calls
    if types_filter:
        unknown = [t for t in unknown if (_infer_type_by_pattern(t) or "").lower() in types_filter or not types_filter]

    print(f"Unknown tickers to consider: {len(unknown)} (limit={args.limit})")
    to_process = unknown[: args.limit]

    updated = 0
    inserted = 0

    for t in to_process:
        name = None
        dtype = None

        # Fixed names first (indices, etc.)
        if t in FIXED_NAMES:
            name = FIXED_NAMES[t]
            # Prefer inferred type for fixed-name tickers (e.g., DX=F -> future)
            dtype = dtype or _infer_type_by_pattern(t) or "stock"
        
        # Try yfinance next
        if not name:
            name, dtype = _yf_name_and_type(t)

        # Fallbacks
        if not name:
            name = _fallback_name_from_stock_metadata(cur, t)
        if not name:
            name = _heuristic_name(t)
        if not dtype:
            dtype = _infer_type_by_pattern(t) or "stock"

        if not name and args.fallback_ticker_name:
            name = t
        if not name:
            # Skip if we still have no name
            continue

        # Update or insert
        cur.execute("SELECT ticker FROM ticker_metadata WHERE ticker = ?", (t,))
        exists = cur.fetchone()
        first_date, last_date, data_points = _get_data_range(cur, t, dtype)
        if exists:
            cur.execute(
                """
                UPDATE ticker_metadata
                SET name = ?, data_type = ?
                WHERE ticker = ?
                """,
                (name, dtype, t),
            )
            updated += 1
            print(f"Updated {t}: {name} ({dtype})")
        else:
            if (data_points and data_points > 0) or args.allow_empty:
                table_name = 'futures_prices_daily' if dtype == 'future' else 'stock_prices_daily'
                cur.execute(
                    """
                    INSERT INTO ticker_metadata
                    (ticker, name, table_name, data_type, first_date, last_date, data_points)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (t, name, table_name, dtype, first_date, last_date, data_points),
                )
                inserted += 1
                print(f"Inserted {t}: {name} ({dtype})")

    conn.commit()

    print("\n=== Summary ===")
    print(f"Updated: {updated}")
    print(f"Inserted: {inserted}")
    print(f"Processed: {len(to_process)} / {len(unknown)} unknowns")

    conn.close()
    print("\n✓ Missing metadata population complete")

if __name__ == "__main__":
    main()
