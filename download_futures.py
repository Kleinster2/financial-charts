"""Download daily futures prices via yfinance and store them in the existing SQLite
database resolved via constants.DB_PATH. The data is saved in a dedicated table `futures_prices_daily`.

This script mirrors the behaviour of the main updater `update_market_data.py` but targets a curated list
of liquid futures contracts. Most come from Yahoo Finance via yfinance, and selected
continuous futures can be sourced from TradingView when Yahoo does not provide usable
history. If you would like to broaden, shrink or otherwise customise the list,
modify the `FUTURES_TICKERS` constant below.

Run the script directly (python download_futures.py) or import and call
`update_futures_data()` from elsewhere.
"""

from __future__ import annotations

import sqlite3
import json
import random
import re
import string
import time
from datetime import datetime, timedelta, timezone
import sys

import pandas as pd
import websocket
import yfinance as yf
from constants import DB_PATH, get_db_connection

# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------
START_DATE = "2019-12-31"  # Earliest date to include
END_DATE = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

# A reasonably broad yet still concise universe of liquid futures contracts.
# Yahoo Finance uses the suffix "=F" to denote continuous (front-month) futures
# charts. You can amend this list as needed.
FUTURES_TICKERS: list[str] = [
    # Equity index futures - US
    "ES=F",  # S&P 500 E-Mini
    "NQ=F",  # Nasdaq-100 E-Mini
    "YM=F",  # Dow Jones 30 E-Mini
    "RTY=F",  # Russell 2000 E-Mini
    "MES=F",  # Micro E-mini S&P 500
    "MNQ=F",  # Micro E-mini Nasdaq 100
    "MYM=F",  # Micro E-mini Dow
    "M2K=F",  # Micro E-mini Russell 2000

    # Equity index futures - International
    "NIY=F",  # Nikkei 225 (Yen-denominated)
    "NKD=F",  # Nikkei 225 (USD-denominated)

    # Energy
    "CL=F",       # WTI Crude Oil
    "MCL=F",      # Micro WTI Crude Oil
    "BZ=F",       # Brent Crude Oil
    "NG=F",       # Natural Gas
    "RB=F",       # RBOB Gasoline
    "AGE1!",      # Gulf Coast Jet Fuel (Platts) default continuous contract series via TradingView/ICE
    "AKS1!",      # Singapore Jet Kerosene (Platts) default continuous contract series via TradingView/ICE

    # Precious & industrial metals
    "GC=F",  # Gold
    "MGC=F", # Micro Gold (10 oz)
    # Removed: YG=F — yfinance serves no data for Mini Gold (confirmed 2026-04-15); use GC=F/MGC=F
    "SI=F",  # Silver
    "SIL=F", # Mini Silver (1,000 oz, E-mini)
    "HG=F",  # Copper
    "PL=F",  # Platinum
    "PA=F",  # Palladium
    "TIO=F", # Iron Ore 62%, CFR China (TSI)
    # Removed: AL=F, ZI=F, NI=F, HRN00, HRC00, HRE00 — yfinance never served these (Mar 2026)
    "DBB",   # Invesco DB Base Metals Fund

    # US Treasuries
    "ZB=F",  # 30-Year Bond
    "ZN=F",  # 10-Year Note
    "ZF=F",  # 5-Year Note
    "ZT=F",  # 2-Year Note
    # Removed: FGBL=F — yfinance never served Euro-Bund (Mar 2026)

    # Currency futures (CME)
    "DX=F",   # US Dollar Index Futures (ICE)
    "6E=F",   # Euro FX
    "6J=F",   # Japanese Yen
    "6B=F",   # British Pound
    "6C=F",   # Canadian Dollar
    "6A=F",   # Australian Dollar
    "6S=F",   # Swiss Franc
    "6N=F",   # New Zealand Dollar
    "6M=F",   # Mexican Peso

    # Agriculture - Grains & Softs
    "ZC=F",  # Corn
    "ZS=F",  # Soybeans
    "ZL=F",  # Soybean Oil
    "ZM=F",  # Soybean Meal
    "ZW=F",  # Wheat (Chicago)
    "KE=F",  # Wheat (Kansas City)
    "SB=F",  # Sugar #11
    "KC=F",  # Coffee
    "CC=F",  # Cocoa
    "CT=F",  # Cotton
    "OJ=F",  # Orange Juice

    # Livestock
    "LE=F",  # Live Cattle
    "GF=F",  # Feeder Cattle
    "HE=F",  # Lean Hogs

    # Energy - Additional
    "HO=F",  # Heating Oil

    # Volatility
    # Removed: VX=F — yfinance never served VIX futures (Mar 2026); use ^VIX index instead

    # Lumber
    "LBR=F",  # Random Length Lumber

    # Dairy (CME)
    "DC=F",   # Milk Class III
    "GNF=F",  # Non-Fat Dry Milk
    "CB=F",   # Cash-Settled Butter
    "CSC=F",  # Cash-Settled Cheese

    # Crypto (CME)
    "MBT=F",  # Micro Bitcoin (0.1 BTC) — yfinance live-quote only; history builds forward from 2026-04-15
    "MET=F",  # Micro Ether (0.1 ETH) — yfinance live-quote only; history builds forward from 2026-04-15
]
# Note: MCL=F (Micro Crude) is live-quote only as well; history builds forward from 2026-04-15. For historical analysis use CL=F.

FUTURES_NAME_OVERRIDES: dict[str, str] = {
    "AGE1!": "Gulf Coast Jet Fuel (Platts) Futures Continuous",
    "AKS1!": "Singapore Jet Kerosene (Platts) Futures Continuous",
}

TRADINGVIEW_CONTINUOUS_TICKERS: dict[str, dict[str, str]] = {
    "AGE1!": {
        "tv_symbol": "NYMEX:AGE1!",
        "name": "Gulf Coast Jet Fuel (Platts) Futures Continuous",
    },
    "AKS1!": {
        "tv_symbol": "NYMEX:AKS1!",
        "name": "Singapore Jet Kerosene (Platts) Futures Continuous",
    },
}

TABLE_NAME = "futures_prices_daily"  # New destination table
VOL_TABLE_NAME = "futures_volumes_daily"


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def _fetch_live_quote_fallback(ticker: str) -> tuple[float | None, float | None]:
    """Return a live/delayed fallback quote for tickers with no downloadable history."""
    try:
        fast_info = yf.Ticker(ticker).fast_info
    except Exception:
        return None, None

    try:
        price = fast_info.get("lastPrice") or fast_info.get("last_price")
    except Exception:
        price = None

    if price is None or pd.isna(price):
        return None, None

    try:
        volume = (
            fast_info.get("lastVolume")
            or fast_info.get("last_volume")
            or fast_info.get("volume")
        )
    except Exception:
        volume = None

    try:
        price = float(price)
    except (TypeError, ValueError):
        return None, None

    if price <= 0:
        return None, None

    try:
        volume = float(volume) if volume is not None and not pd.isna(volume) else None
    except (TypeError, ValueError):
        volume = None

    return price, volume


def _tv_generate_session(prefix: str) -> str:
    return prefix + ''.join(random.choice(string.ascii_lowercase) for _ in range(12))


def _tv_prepend_header(message: str) -> str:
    return f"~m~{len(message)}~m~{message}"


def _tv_send(ws, method: str, params: list) -> None:
    payload = json.dumps({"m": method, "p": params}, separators=(",", ":"))
    ws.send(_tv_prepend_header(payload))


def _tv_extract_json_messages(blob: str) -> list[str]:
    return [part for part in re.split(r"~m~\d+~m~", blob) if part.startswith("{")]


def _normalize_daily_index(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize any daily-like index to midnight and collapse duplicate same-day rows."""
    if df.empty:
        return df

    out = df.copy()
    idx = pd.DatetimeIndex(pd.to_datetime(out.index))
    if idx.tz is not None:
        idx = idx.tz_convert("America/New_York").tz_localize(None)
    out.index = idx.normalize()
    out = out.groupby(level=0).agg(lambda col: col.dropna().iloc[-1] if col.notna().any() else float("nan"))
    out.sort_index(inplace=True)
    return out


def _fetch_tradingview_history(tv_symbol: str, bars: int = 6000, interval: str = "1D") -> pd.DataFrame:
    """Fetch daily continuous-futures history from TradingView's public chart websocket."""
    ws = websocket.create_connection(
        "wss://data.tradingview.com/socket.io/websocket",
        timeout=20,
        origin="https://www.tradingview.com",
    )
    try:
        chart_session = _tv_generate_session("cs_")
        _tv_send(ws, "set_auth_token", ["unauthorized_user_token"])
        _tv_send(ws, "chart_create_session", [chart_session, ""])
        symbol_payload = "=" + json.dumps(
            {"symbol": tv_symbol, "adjustment": "splits", "session": "regular"},
            separators=(",", ":"),
        )
        _tv_send(ws, "resolve_symbol", [chart_session, "symbol_1", symbol_payload])
        _tv_send(ws, "create_series", [chart_session, "s1", "s1", "symbol_1", interval, bars])

        messages: list[str] = []
        started = time.time()
        while time.time() - started < 20:
            raw = ws.recv()
            parts = _tv_extract_json_messages(raw)
            messages.extend(parts)
            if any("series_completed" in part for part in parts):
                break

        rows: dict[int, list[float]] = {}
        for msg in messages:
            payload = json.loads(msg)
            if payload.get("m") != "timescale_update":
                continue
            args = payload.get("p", [])
            series_rows = args[1].get("s1", {}).get("s", []) if len(args) > 1 else []
            for row in series_rows:
                values = row.get("v", [])
                if len(values) >= 5:
                    rows[int(values[0])] = values

        if not rows:
            return pd.DataFrame()

        ordered = [rows[key] for key in sorted(rows)]
        df = pd.DataFrame(
            {
                "Date": [pd.Timestamp.fromtimestamp(values[0], tz="UTC").tz_convert("America/New_York").tz_localize(None).normalize() for values in ordered],
                "Close": [float(values[4]) for values in ordered],
            }
        )
        df = df.dropna(subset=["Close"]).drop_duplicates(subset=["Date"]).sort_values("Date")
        df = df[df["Date"] >= pd.Timestamp(START_DATE)]
        return df.set_index("Date")
    finally:
        ws.close()


# -----------------------------------------------------------------------------
# Main update routine
# -----------------------------------------------------------------------------

def update_futures_data(verbose: bool = True) -> None:
    """Download/refresh daily settlement prices for the tickers in
    `FUTURES_TICKERS` and persist them to the SQLite database.
    Existing data (if any) is merged with new downloads so that previously
    collected series are preserved.
    """

    def vprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    vprint(f"Connecting to database… Using {DB_PATH}")
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
            (TABLE_NAME,),
        )
        table_exists = cursor.fetchone() is not None

        # Check if the volumes table already exists
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
            (VOL_TABLE_NAME,),
        )
        vol_table_exists = cursor.fetchone() is not None

        existing_df = pd.DataFrame()
        existing_vol_df = pd.DataFrame()
        if table_exists:
            vprint("Reading existing futures table…")
            existing_df = _normalize_daily_index(
                pd.read_sql(f"SELECT * FROM {TABLE_NAME}", conn, parse_dates=["Date"])
                .set_index("Date")
                .sort_index()
            )
        if vol_table_exists:
            vprint("Reading existing futures volume table…")
            existing_vol_df = _normalize_daily_index(
                pd.read_sql(f"SELECT * FROM {VOL_TABLE_NAME}", conn, parse_dates=["Date"])
                .set_index("Date")
                .sort_index()
            )

        yahoo_tickers = [ticker for ticker in FUTURES_TICKERS if ticker not in TRADINGVIEW_CONTINUOUS_TICKERS]

        vprint(f"Downloading data for {len(FUTURES_TICKERS)} futures contracts…")
        # Futures are quoted as *prices* (no dividends) so auto_adjust=False is fine.
        raw = yf.download(
            yahoo_tickers,
            start=START_DATE,
            end=END_DATE,
            auto_adjust=False,
            group_by="ticker",
        )

        processed: list[pd.DataFrame] = []
        processed_vol: list[pd.DataFrame] = []
        live_only_date = pd.DatetimeIndex([pd.Timestamp(datetime.now(timezone.utc).date())])
        for ticker in yahoo_tickers:
            if ticker in raw and not raw[ticker].empty:
                close = raw[ticker][["Close"]].rename(columns={"Close": ticker})
                processed.append(close)
                # Volume may be present for many futures; collect where available
                if "Volume" in raw[ticker].columns:
                    vol = raw[ticker][["Volume"]].rename(columns={"Volume": ticker})
                    processed_vol.append(vol)
            else:
                live_price, live_volume = _fetch_live_quote_fallback(ticker)
                if live_price is not None:
                    processed.append(pd.DataFrame({ticker: [live_price]}, index=live_only_date))
                    if live_volume is not None:
                        processed_vol.append(pd.DataFrame({ticker: [live_volume]}, index=live_only_date))
                    print(f"Warning: {ticker} returned no history; seeded with live quote fallback only.")
                else:
                    print(f"Warning: {ticker} returned no data and will be skipped.")

        for ticker, meta in TRADINGVIEW_CONTINUOUS_TICKERS.items():
            try:
                tv_df = _fetch_tradingview_history(meta["tv_symbol"])
                if tv_df.empty:
                    print(f"Warning: {ticker} returned no TradingView history and will be skipped.")
                    continue
                processed.append(tv_df.rename(columns={"Close": ticker}))
            except Exception as exc:
                print(f"Warning: TradingView history fetch failed for {ticker}: {exc}")

        if not processed:
            print("No valid futures data processed. Nothing to store.")
            return

        new_df = pd.concat(processed, axis=1)
        new_df.index = pd.to_datetime(new_df.index)
        new_df = _normalize_daily_index(new_df)

        # Assemble volume dataframe if any were collected
        new_vol_df = pd.DataFrame()
        if processed_vol:
            new_vol_df = pd.concat(processed_vol, axis=1)
            new_vol_df.index = pd.to_datetime(new_vol_df.index)
            new_vol_df = _normalize_daily_index(new_vol_df)

        # Merge with existing data, giving precedence to freshly downloaded values
        if not existing_df.empty:
            all_cols = sorted(set(existing_df.columns) | set(new_df.columns))
            existing_df = existing_df.reindex(columns=all_cols)
            new_df = new_df.reindex(columns=all_cols)
            combined_df = new_df.combine_first(existing_df)
        else:
            combined_df = new_df

        # Merge volume with existing, if any
        combined_vol_df = pd.DataFrame()
        if not new_vol_df.empty or not existing_vol_df.empty:
            if new_vol_df.empty:
                combined_vol_df = existing_vol_df.copy()
            elif existing_vol_df.empty:
                combined_vol_df = new_vol_df.copy()
            else:
                vol_cols = sorted(set(existing_vol_df.columns) | set(new_vol_df.columns))
                existing_vol_df = existing_vol_df.reindex(columns=vol_cols)
                new_vol_df = new_vol_df.reindex(columns=vol_cols)
                combined_vol_df = new_vol_df.combine_first(existing_vol_df)

        vprint("Writing combined dataset to database…")
        # Ensure index label is 'Date' for consistency
        combined_df.index.name = combined_df.index.name or "Date"
        combined_df.to_sql(TABLE_NAME, conn, if_exists="replace", index=True, index_label=combined_df.index.name)
        if not combined_vol_df.empty:
            combined_vol_df.index.name = combined_vol_df.index.name or "Date"
            combined_vol_df.to_sql(VOL_TABLE_NAME, conn, if_exists="replace", index=True, index_label=combined_vol_df.index.name)

        for ticker, display_name in FUTURES_NAME_OVERRIDES.items():
            if ticker not in combined_df.columns:
                continue
            series = combined_df[ticker].dropna()
            if series.empty:
                continue
            first_date = pd.Timestamp(series.index.min()).strftime("%Y-%m-%d %H:%M:%S")
            last_date = pd.Timestamp(series.index.max()).strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(
                """
                INSERT OR REPLACE INTO ticker_metadata
                (ticker, name, table_name, data_type, first_date, last_date, data_points)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (ticker, display_name, TABLE_NAME, "future", first_date, last_date, int(series.shape[0]))
            )
        conn.commit()

        vprint(
            f"Success: {TABLE_NAME} now contains "
            f"{combined_df.shape[1]} contracts × {combined_df.shape[0]} dates."
        )
        if not combined_vol_df.empty:
            vprint(
                f"Success: {VOL_TABLE_NAME} now contains "
                f"{combined_vol_df.shape[1]} contracts × {combined_vol_df.shape[0]} dates."
            )
    finally:
        conn.close()
        vprint("Database connection closed.")


# -----------------------------------------------------------------------------
# Entry-point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    argv = sys.argv[1:]
    verbose = True
    if any(a in ("--quiet", "-q") for a in argv):
        verbose = False
    if any(a in ("--verbose", "-v") for a in argv):
        verbose = True
    update_futures_data(verbose=verbose)
