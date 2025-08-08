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


def _parse_holdings(xlsx_data: bytes, verbose: bool = False) -> tuple[pd.DataFrame, str]:
    """Parse XLSX binary into a DataFrame with canonical columns.

    State Street's file sometimes includes several preamble rows before the real
    header.  We therefore scan dynamically for the row that contains the word
    *Ticker* and use that as the header row.

    Returns:
        Tuple of (holdings_dataframe, as_of_date_string)
    """

    raw_df = pd.read_excel(
        io.BytesIO(xlsx_data), engine="openpyxl", header=None, dtype=str
    )

    # Extract the "As of" date from the file
    as_of_date = None
    for i in range(min(20, len(raw_df))):
        for j in range(min(5, len(raw_df.columns))):
            val = raw_df.iloc[i, j]
            if pd.notna(val) and "as of" in str(val).lower():
                # Try to extract date from format like "As of 05-Aug-2025"
                import re
                date_match = re.search(r'(\d{1,2})-(\w{3})-(\d{4})', str(val))
                if date_match:
                    day, month_str, year = date_match.groups()
                    # Convert month abbreviation to number
                    month_map = {
                        'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04',
                        'may': '05', 'jun': '06', 'jul': '07', 'aug': '08',
                        'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'
                    }
                    month = month_map.get(month_str.lower(), '01')
                    as_of_date = f"{year}-{month}-{day.zfill(2)}"
                    break
        if as_of_date:
            break

    if not as_of_date:
        msg = "Could not extract 'As of' date from file; aborting."
        if verbose:
            print(f"❌ {msg}")
        raise ValueError(msg)

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
    if verbose:
        print(f"Header row detected at index {header_idx}")

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
    if verbose:
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
    before_rows = len(out)

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

    if verbose:
        after_rows = len(out)
        print(f"Rows parsed: {before_rows}; after filtering invalid rows: {after_rows}; removed: {before_rows - after_rows}")

    return out, as_of_date


def _store_holdings(df: pd.DataFrame, snapshot_date: str, conn: sqlite3.Connection, verbose: bool = False) -> bool:
    """Insert/replace the day's holdings into SQLite.
    
    Returns:
        True if data was stored, False if snapshot already exists
    """
    # Check if this snapshot already exists
    existing = conn.execute(
        f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE etf = ? AND snapshot_date = ?",
        (ETF_SYMBOL, snapshot_date)
    ).fetchone()[0]
    
    if existing > 0:
        if verbose:
            print(f"⏭️ Snapshot for {snapshot_date} already exists, skipping")
        return False
    
    row_count = len(df)
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
    if verbose:
        print(f"✅ Inserted {row_count} holdings for {snapshot_date} into {TABLE_NAME}")
    return True


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

    # Verbosity flags (verbose by default)
    verbose = True
    argv = sys.argv[1:]
    if any(a in ("--quiet", "-q") for a in argv):
        verbose = False
    if any(a in ("--verbose", "-v") for a in argv):
        verbose = True

    # Helper for conditional printing
    def vprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    # Parse positionals (date and/or local file), ignoring flags
    positionals = [a for a in argv if not a.startswith("-")]
    explicit_date: str | None = None
    if len(positionals) == 1:
        candidate = positionals[0]
        if candidate.lower().endswith(".xlsx"):
            local_file = candidate
        else:
            explicit_date = candidate
    elif len(positionals) >= 2:
        explicit_date = positionals[0]
        local_file = positionals[1]

    if explicit_date:
        as_of = explicit_date

    if local_file:
        vprint(f"📂 Loading local XLSX: {local_file}")
        try:
            xlsx_bytes = Path(local_file).read_bytes()
        except Exception as exc:
            print(f"ERROR: could not read file – {exc}")
            sys.exit(1)
    else:
        vprint("📥 Downloading XLSX file from State Street...")
        try:
            xlsx_bytes = _fetch_holdings_xlsx(HOLDINGS_URL)
        except Exception as exc:
            print(f"ERROR: failed to download holdings – {exc}")
            sys.exit(1)

    try:
        vprint("🔄 Parsing holdings file...")
        holdings_df, extracted_date = _parse_holdings(xlsx_bytes, verbose=verbose)
        
        # Determine the snapshot date: prefer explicit date, else use the file's "As of"
        actual_date = explicit_date if explicit_date else extracted_date
        if not explicit_date and actual_date != as_of:
            vprint(f"📅 Using 'As of' date from file: {actual_date}")

        with sqlite3.connect(DB_PATH) as conn:
            _store_holdings(holdings_df, actual_date, conn, verbose=verbose)
    except Exception as exc:
        print(f"ERROR: failed to process holdings – {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
