"""
Populate stock display names in ticker_metadata for hover tooltips.

- Accepts a list of tickers via --tickers (comma/space separated)
- Resolves display names via yfinance (longName -> shortName -> displayName)
- Falls back to stock_metadata name if present
- Writes/updates ticker_metadata with data_type='stock'

Usage examples:
    python populate_stock_metadata.py --tickers APP,TTD,MGNI
"""
from __future__ import annotations
import argparse
import os
import sqlite3
from typing import List, Optional

# Local imports
from constants import DB_PATH, get_db_connection

# Optional dependency: yfinance
try:
    import yfinance as yf
    _HAS_YF = True
except Exception:
    _HAS_YF = False


def _ensure_table(conn: sqlite3.Connection):
    """Create ticker_metadata table if it doesn't exist (compatible schema)."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS ticker_metadata (
            ticker TEXT PRIMARY KEY,
            name TEXT,
            table_name TEXT,
            data_type TEXT,
            first_date TEXT,
            last_date TEXT,
            data_points INTEGER
        )
        """
    )
    conn.commit()


def _get_data_range(cursor: sqlite3.Cursor, ticker: str):
    """Return (first_date, last_date, data_points) for a given ticker column."""
    cursor.execute(
        f"""
        SELECT 
            MIN(Date) as first_date,
            MAX(Date) as last_date,
            COUNT(*) as data_points
        FROM stock_prices_daily
        WHERE "{ticker}" IS NOT NULL
        """
    )
    row = cursor.fetchone()
    return row if row else (None, None, 0)


def _fallback_name_from_stock_metadata(cursor: sqlite3.Cursor, ticker: str) -> Optional[str]:
    try:
        cursor.execute("SELECT name FROM stock_metadata WHERE ticker = ?", (ticker,))
        row = cursor.fetchone()
        if row and row[0]:
            name = str(row[0]).strip()
            return name or None
    except Exception:
        return None
    return None


def _yf_name_any(ticker: str) -> Optional[str]:
    if not _HAS_YF:
        return None
    try:
        t = yf.Ticker(ticker)
        info = {}
        try:
            info = t.get_info()
        except Exception:
            try:
                info = t.info  # fallback for older versions
            except Exception:
                info = {}
        name = (info.get('longName') or info.get('shortName') or info.get('displayName') or '').strip()
        return name or None
    except Exception:
        return None


def parse_tickers(s: str) -> List[str]:
    import re
    parts = re.split(r"[\s,]+", s.strip()) if s else []
    return [p.upper() for p in parts if p]


def main():
    parser = argparse.ArgumentParser(description="Populate stock names into ticker_metadata for hover display.")
    parser.add_argument("--tickers", type=str, required=True,
                        help="Comma/space-separated list of stock tickers to populate.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    tickers = parse_tickers(args.tickers)
    if not tickers:
        print("No tickers provided.")
        return

    print("=== Populating STOCK metadata ===")
    print(f"Using database: {DB_PATH}")
    if not os.path.exists(DB_PATH):
        print(f"Database not found: {DB_PATH}")
        return

    conn = get_db_connection()
    cursor = conn.cursor()
    _ensure_table(conn)

    # Load available stock columns to avoid inserting for non-existent symbols
    try:
        cursor.execute("PRAGMA table_info(stock_prices_daily)")
        stock_cols = {row[1] for row in cursor.fetchall() if row[1] != 'Date'}
    except sqlite3.OperationalError:
        stock_cols = set()

    # Filter to symbols present in DB (optional but recommended)
    present = [t for t in tickers if t in stock_cols]
    missing = [t for t in tickers if t not in stock_cols]
    if missing:
        print(f"Skipping {len(missing)} tickers not found in stock_prices_daily: {', '.join(missing)}")
    if not present:
        print("No provided tickers are present in stock_prices_daily. Nothing to do.")
        conn.close()
        return

    updated = 0
    inserted = 0

    for t in present:
        # Resolve name: yfinance first, then legacy stock_metadata
        name = _yf_name_any(t) or _fallback_name_from_stock_metadata(cursor, t) or t

        # Determine data range from prices table
        first_date, last_date, data_points = _get_data_range(cursor, t)

        # Upsert into ticker_metadata
        cursor.execute("SELECT ticker FROM ticker_metadata WHERE ticker = ?", (t,))
        row = cursor.fetchone()
        if row:
            cursor.execute(
                """
                UPDATE ticker_metadata
                SET name = ?, data_type = 'stock'
                WHERE ticker = ?
                """,
                (name, t),
            )
            updated += 1
            if args.verbose:
                print(f"Updated {t}: {name}")
        else:
            if data_points and data_points > 0:
                cursor.execute(
                    """
                    INSERT INTO ticker_metadata
                    (ticker, name, table_name, data_type, first_date, last_date, data_points)
                    VALUES (?, ?, 'stock_prices_daily', 'stock', ?, ?, ?)
                    """,
                    (t, name, first_date, last_date, data_points),
                )
                inserted += 1
                if args.verbose:
                    print(f"Inserted {t}: {name} (points={data_points})")
            else:
                if args.verbose:
                    print(f"Skipped insert for {t}: no data points.")

    conn.commit()
    conn.close()

    print(f"Done. Updated {updated}, Inserted {inserted}.")


if __name__ == "__main__":
    main()
