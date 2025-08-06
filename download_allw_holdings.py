"""download_allw_holdings.py

Download and store the daily holdings for the State Street ALLW ETF
into a SQLite table called `etf_holdings_daily`.

The holdings XLSX is published each trading day after market close at:
https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-allw.xlsx

Schema of `etf_holdings_daily` (if the table doesn't exist it will be
created automatically):
    snapshot_date TEXT  (YYYY-MM-DD)
    etf           TEXT  (e.g. "ALLW")
    ticker        TEXT
    name          TEXT
    weight        REAL  (decimal, e.g. 0.0234 -> 2.34%)
    shares        REAL
    market_value  REAL  (USD)

Primary key (snapshot_date, etf, ticker).

Run this once per day after the XLSX file is available.  The script is
idempotent – running it again on the same day will upsert rows without
creating duplicates.
"""

from __future__ import annotations

import datetime as _dt
import io
import sqlite3
import sys
from pathlib import Path
from typing import Final

import pandas as pd
import requests

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
HOLDINGS_URL: Final[str] = (
    "https://www.ssga.com/us/en/intermediary/library-content/products/"
    "fund-data/etfs/us/holdings-daily-us-en-allw.xlsx"
)

DB_PATH: Final[Path] = Path(__file__).with_name("sp500_data.db")
ETF_SYMBOL: Final[str] = "ALLW"
TABLE_NAME: Final[str] = "etf_holdings_daily"


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def _fetch_holdings_xlsx(url: str) -> bytes:
    """Download the XLSX file and return its binary content."""
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.content


def _parse_holdings(xlsx_data: bytes) -> pd.DataFrame:
    """Parse XLSX binary into a DataFrame with canonical columns."""

    # State Street places the holdings on the first sheet starting at row 5.
    # But _pandas_ will usually auto-detect the header row, so just read.
    df = pd.read_excel(io.BytesIO(xlsx_data), engine="openpyxl")

    # Expect columns like: "Ticker", "Name", "Weight (%)", "Shares", "Market Value ($)".
    # Standardise column names.
    rename_map = {
        col: col.strip().lower().replace(" (% )", "").replace(" ($)", "")
        for col in df.columns
    }
    df.rename(columns=rename_map, inplace=True)

    # Keep only required cols; some ETFs report extra internal columns.
    expected = {
        "ticker": "ticker",
        "name": "name",
        "weight": "weight",
        "shares": "shares",
        "market value": "market_value",
    }
    cleaned = {}
    for col_lower, canonical in expected.items():
        # find first col that startswith expected string
        match = next((c for c in df.columns if c.lower().startswith(col_lower)), None)
        if match is None:
            raise ValueError(f"Expected column starting with '{col_lower}' not found in XLSX")
        cleaned[canonical] = df[match]

    out = pd.DataFrame(cleaned)

    # Convert weights to decimal fractions (0.0234 instead of 2.34)
    if out["weight"].dtype == object:
        out["weight"] = (
            out["weight"].astype(str)
            .str.replace("%", "", regex=False)
            .str.strip()
            .astype(float)
            / 100.0
        )

    return out


def _store_holdings(df: pd.DataFrame, snapshot_date: str, conn: sqlite3.Connection) -> None:
    """Insert/replace the day's holdings into SQLite."""
    df = df.copy()
    df.insert(0, "snapshot_date", snapshot_date)
    df.insert(1, "etf", ETF_SYMBOL)

    # Upsert using REPLACE into a staging table then move.
    df.to_sql("_tmp_holdings", conn, if_exists="replace", index=False)

    with conn:
        conn.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                snapshot_date TEXT NOT NULL,
                etf           TEXT NOT NULL,
                ticker        TEXT NOT NULL,
                name          TEXT,
                weight        REAL,
                shares        REAL,
                market_value  REAL,
                PRIMARY KEY (snapshot_date, etf, ticker)
            );
            """
        )
        conn.execute(
            f"""
            INSERT OR REPLACE INTO {TABLE_NAME}
            SELECT snapshot_date, etf, ticker, name, weight, shares, market_value
            FROM _tmp_holdings;
            """
        )
        conn.execute("DROP TABLE _tmp_holdings;")


# -----------------------------------------------------------------------------
# Main entry point
# -----------------------------------------------------------------------------

def main() -> None:
    as_of = _dt.date.today().strftime("%Y-%m-%d")
    if len(sys.argv) == 2:
        as_of = sys.argv[1]  # allow override date YYYY-MM-DD

    print(f"⏬ Downloading ALLW holdings for {as_of}…")
    try:
        xlsx_bytes = _fetch_holdings_xlsx(HOLDINGS_URL)
        holdings_df = _parse_holdings(xlsx_bytes)
    except Exception as exc:
        print(f"ERROR: failed to download or parse holdings – {exc}")
        sys.exit(1)

    with sqlite3.connect(DB_PATH) as conn:
        _store_holdings(holdings_df, as_of, conn)
        rows = conn.execute(
            f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE snapshot_date=? AND etf=?",
            (as_of, ETF_SYMBOL),
        ).fetchone()[0]

    print(f"✅ Stored {rows} holdings rows for {ETF_SYMBOL} on {as_of}.")


if __name__ == "__main__":
    main()
