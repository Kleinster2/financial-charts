"""Download daily futures prices via yfinance and store them in the existing SQLite
`sp500_data.db` database. The data is saved in a dedicated table `futures_prices_daily`.

This script mirrors the behaviour of `download_sp500.py` but targets a curated list
of liquid futures contracts that are available on Yahoo Finance (yfinance uses the
same symbols). If you would like to broaden, shrink or otherwise customise the list,
modify the `FUTURES_TICKERS` constant below.

Run the script directly (python download_futures.py) or import and call
`update_futures_data()` from elsewhere.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime

import pandas as pd
import yfinance as yf

# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------
START_DATE = "2019-12-31"  # Earliest date to include
END_DATE = datetime.today().strftime("%Y-%m-%d")

# A reasonably broad yet still concise universe of liquid futures contracts.
# Yahoo Finance uses the suffix "=F" to denote continuous (front-month) futures
# charts. You can amend this list as needed.
FUTURES_TICKERS: list[str] = [
    # Equity index futures
    "ES=F",  # S&P 500 E-Mini
    "NQ=F",  # Nasdaq-100 E-Mini
    "YM=F",  # Dow Jones 30 E-Mini
    "RTY=F",  # Russell 2000 E-Mini

    # Energy
    "CL=F",  # WTI Crude Oil
    "BZ=F",  # Brent Crude Oil
    "NG=F",  # Natural Gas
    "RB=F",  # RBOB Gasoline

    # Precious & industrial metals
    "GC=F",  # Gold
    "SI=F",  # Silver
    "HG=F",  # Copper
    "PL=F",  # Platinum
    "PA=F",  # Palladium
    "TIO=F", # Iron Ore 62%, CFR China (TSI)
    "AL=F",  # Aluminum
    "ZI=F",  # Zinc
    "NI=F",  # Nickel
    "HRN00", # HRC Steel (Hot-Rolled Coil) Futures
    "HRC00", # HRC Steel (Hot-Rolled Coil) Futures
    "HRE00", # HRC Steel (Hot-Rolled Coil) Futures
    "DBB",   # Invesco DB Base Metals Fund

    # US Treasuries
    "ZB=F",  # 30-Year Bond
    "ZN=F",  # 10-Year Note
    "ZF=F",  # 5-Year Note
    "ZT=F",  # 2-Year Note
    "FGBL=F",  # Euro-Bund (Germany 10Y)

    # Agriculture
    "ZC=F",  # Corn
    "ZS=F",  # Soybeans
    "ZW=F",  # Wheat (Chicago)
    "KE=F",  # Wheat (Kansas City)
    "SB=F",  # Sugar #11
    "KC=F",  # Coffee
    "CC=F",  # Cocoa
    "CT=F",  # Cotton
    "OJ=F",  # Orange Juice
]

DB_PATH = "sp500_data.db"  # Re-use the existing database in the project root
TABLE_NAME = "futures_prices_daily"  # New destination table


# -----------------------------------------------------------------------------
# Main update routine
# -----------------------------------------------------------------------------

def update_futures_data() -> None:
    """Download/refresh daily settlement prices for the tickers in
    `FUTURES_TICKERS` and persist them to the SQLite database.
    Existing data (if any) is merged with new downloads so that previously
    collected series are preserved.
    """

    print("Connecting to database…")
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
            (TABLE_NAME,),
        )
        table_exists = cursor.fetchone() is not None

        existing_df = pd.DataFrame()
        if table_exists:
            print("Reading existing futures table…")
            existing_df = (
                pd.read_sql(f"SELECT * FROM {TABLE_NAME}", conn, parse_dates=["Date"])
                .set_index("Date")
                .sort_index()
            )

        print(f"Downloading data for {len(FUTURES_TICKERS)} futures contracts…")
        # Futures are quoted as *prices* (no dividends) so auto_adjust=False is fine.
        raw = yf.download(
            FUTURES_TICKERS,
            start=START_DATE,
            end=END_DATE,
            auto_adjust=False,
            group_by="ticker",
        )

        if raw.empty:
            print("No data returned from Yahoo Finance — aborting.")
            return

        processed: list[pd.DataFrame] = []
        for ticker in FUTURES_TICKERS:
            if ticker in raw and not raw[ticker].empty:
                close = raw[ticker][["Close"]].rename(columns={"Close": ticker})
                processed.append(close)
            else:
                print(f"Warning: {ticker} returned no data and will be skipped.")

        if not processed:
            print("No valid futures data processed. Nothing to store.")
            return

        new_df = pd.concat(processed, axis=1)
        new_df.index = pd.to_datetime(new_df.index)
        new_df.sort_index(inplace=True)

        # Merge with existing data, giving precedence to freshly downloaded values
        if not existing_df.empty:
            all_cols = sorted(set(existing_df.columns) | set(new_df.columns))
            existing_df = existing_df.reindex(columns=all_cols)
            new_df = new_df.reindex(columns=all_cols)
            combined_df = new_df.combine_first(existing_df)
        else:
            combined_df = new_df

        print("Writing combined dataset to database…")
        combined_df.to_sql(TABLE_NAME, conn, if_exists="replace")
        print(
            f"Success: {TABLE_NAME} now contains "
            f"{combined_df.shape[1]} contracts × {combined_df.shape[0]} dates."
        )
    finally:
        conn.close()
        print("Database connection closed.")


# -----------------------------------------------------------------------------
# Entry-point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    update_futures_data()
