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
    """Parse XLSX binary into a DataFrame with canonical columns.

    State Street's file sometimes includes several preamble rows before the real
    header.  We therefore scan dynamically for the row that contains the word
    *Ticker* and use that as the header row.
    """

    raw_df = pd.read_excel(
        io.BytesIO(xlsx_data), engine="openpyxl", header=None, dtype=str
    )

    # Locate header row – the first row whose first 5 cells contain 'Ticker'
    header_idx = None
    for i in range(min(20, len(raw_df))):  # scan top rows for header
        row_vals = (
            raw_df.iloc[i].astype(str).str.strip().str.lower().tolist()
        )
        contains_ticker = any("ticker" in v or "identifier" in v for v in row_vals)
        contains_other = any(
            any(key in v for key in ("weight", "shares", "market value"))
            for v in row_vals
        )
        if contains_ticker and contains_other:
            header_idx = i
            break

    if header_idx is None:
        raise ValueError("Could not locate header row containing 'Ticker' in XLSX")

    df = pd.read_excel(
        io.BytesIO(xlsx_data),
        engine="openpyxl",
        header=header_idx,
    )

    # Standardise column names
    def _clean(col: str) -> str:
        col = col.strip().lower()
        col = col.replace("(%)", "").replace("($)", "")
        col = col.replace("( %)", "").replace("( %) ", "")
        return col

    df.columns = [_clean(c) for c in df.columns]

    # DEBUG: print columns list once
    print("Columns detected in holdings file:", list(df.columns)[:20])

    expected_map = {
        "ticker": "ticker",
        "identifier": "ticker",  # fallback col label sometimes used
        "name": "name",
        "security name": "name",
        "weight": "weight",
        "weight %": "weight",
        "shares": "shares",
        "market value": "market_value",
        "market value ": "market_value",
    }

    # Build cleaned dict selecting the first matching column for each canonical field
    # Map canonical fields to list of acceptable substrings that may appear in column headers
    patterns = {
        "ticker": ["ticker", "identifier"],
        "name": ["name", "security name", "company name"],
        "weight": ["weight"],
        "shares": ["shares"],
        "market_value": ["market value", "marketvalue", "market value usd", "market value $"],
    }

    cleaned = {}
    for canonical, pats in patterns.items():
        match_cols = [c for c in df.columns if any(p in c for p in pats)]
        if not match_cols:
            raise ValueError(f"Expected a column containing one of {pats} but none found in XLSX")
        cleaned[canonical] = df[match_cols[0]]
    for key, canonical in {
        "ticker": "ticker",
        "name": "name",
        "weight": "weight",
        "shares": "shares",
        "market value": "market_value",
    }.items():
        match_cols = [c for c in df.columns if c.startswith(key)]
        if not match_cols:
            # Try alternate labels
            alt_matches = [c for k, c in expected_map.items() if k.startswith(key)]
            match_cols = [c for c in df.columns if c in alt_matches]
        if not match_cols:
            raise ValueError(f"Expected column starting with '{key}' not found in XLSX")
        cleaned[canonical] = df[match_cols[0]]

    out = pd.DataFrame(cleaned)

    # Convert weights to decimal fractions (0.0234 instead of 2.34)
    out["weight"] = (
        out["weight"].astype(str)
        .str.replace("%", "", regex=False)
        .str.strip()
        .astype(float)
        .div(100.0)
    )

    # Remove rows without a valid ticker (e.g., summary lines like 'Total')
    # Drop rows where ticker is NaN or empty after stripping
    out = out[out["ticker"].notna()]
    out["ticker"] = out["ticker"].astype(str).str.strip()
    out = out[out["ticker"].str.len() > 0]
    out = out[~out["ticker"].str.lower().isin(["total", "cash", "nan"])]

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
    # Usage:
    #   python download_allw_holdings.py             -> fetch today from web
    #   python download_allw_holdings.py YYYY-MM-DD -> fetch given date from web (for re-runs)
    #   python download_allw_holdings.py YYYY-MM-DD path/to/file.xlsx -> ingest local file
    #
    # A bare 2-arg call where the 2nd arg is a *.xlsx file will treat that as the local file

    as_of = _dt.date.today().strftime("%Y-%m-%d")
    local_file: str | None = None

    if len(sys.argv) == 2:
        # Could be either a snapshot date or a file path
        candidate = sys.argv[1]
        if candidate.lower().endswith(".xlsx"):
            local_file = candidate
        else:
            as_of = candidate
    elif len(sys.argv) == 3:
        as_of = sys.argv[1]
        local_file = sys.argv[2]

    if local_file:
        print(f"📂 Loading local XLSX: {local_file}")
        try:
            xlsx_bytes = Path(local_file).read_bytes()
        except Exception as exc:
            print(f"ERROR: could not read file – {exc}")
            sys.exit(1)
    else:
        print("📥 Downloading XLSX file from State Street...")
        try:
            xlsx_bytes = _fetch_holdings_xlsx(HOLDINGS_URL)
        except Exception as exc:
            print(f"ERROR: failed to download holdings – {exc}")
            sys.exit(1)

    try:
        print("🔄 Parsing holdings file...")
        holdings_df = _parse_holdings(xlsx_bytes)

        with sqlite3.connect(DB_PATH) as conn:
            _store_holdings(holdings_df, as_of, conn)
            rows = conn.execute(
                f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE snapshot_date=? AND etf=?",
                (as_of, ETF_SYMBOL),
            ).fetchone()[0]

        print(f"✅ Stored {rows} holdings rows for {ETF_SYMBOL} on {as_of}.")
    except Exception as exc:
        print(f"ERROR: failed to process holdings – {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
