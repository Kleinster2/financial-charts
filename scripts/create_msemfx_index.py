#!/usr/bin/env python3
"""
Create MSEMFX, a local spot-only proxy for the MSCI EM Currency Index.

This is not the licensed MSCI total-return series. MSCI's Global Currency
Indices include spot currency moves plus foreign-currency interest/forward
accrual and reset currency weights monthly. This proxy uses currently
available country-weight evidence and local spot FX pairs already stored in
prices_long.

Methodology:
- Weights follow the accessible iShares EEM geography breakdown as of
  May 22, 2026, which tracks the MSCI Emerging Markets Index.
- The official MSCI EM currency methodology weights currencies by the
  corresponding country weights in the MSCI EM equity index.
- This proxy captures only spot appreciation/depreciation versus USD.
- Malaysia plus "Other" are represented by an equal-weight residual basket
  of smaller EM currencies available in the local database.

Usage:
    python scripts/create_msemfx_index.py
    python scripts/create_msemfx_index.py --store
    python scripts/create_msemfx_index.py --store --duckdb
"""

from __future__ import annotations

import argparse
import sqlite3
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

try:
    import duckdb
except ImportError:  # pragma: no cover - optional local dependency
    duckdb = None


ROOT = Path(__file__).resolve().parent.parent
SQLITE_DB = ROOT / "market_data.db"
DUCKDB_DB = ROOT / "market_data.duckdb"

TICKER = "MSEMFX"
NAME = "MSCI EM Currency Proxy Index (spot only)"
START_DATE = "2005-01-01"
INITIAL_VALUE = 100.0
MAX_DAILY_FX_MOVE = 0.25


@dataclass(frozen=True)
class Component:
    country: str
    currency: str
    ticker: str
    orientation: str  # "direct" = USD per local unit; "inverse" = local units per USD
    weight_pct: float
    bucket: str = "explicit"


EXPLICIT_COMPONENTS = [
    Component("Taiwan", "TWD", "USDTWD=X", "inverse", 25.69),
    Component("Korea (South)", "KRW", "USDKRW=X", "inverse", 21.60),
    Component("China", "CNY", "CNYUSD=X", "direct", 21.38),
    Component("India", "INR", "INRUSD=X", "direct", 11.21),
    Component("Brazil", "BRL", "BRLUSD=X", "direct", 4.07),
    Component("South Africa", "ZAR", "ZARUSD=X", "direct", 3.04),
    Component("Saudi Arabia", "SAR", "USDSAR=X", "inverse", 2.51),
    Component("Mexico", "MXN", "MXNUSD=X", "direct", 1.80),
    Component("United Arab Emirates", "AED", "USDAED=X", "inverse", 1.10),
    Component("Poland", "PLN", "PLNUSD=X", "direct", 1.05),
]

# EEM table shows Malaysia 1.04% and Other 5.25%. We do not have MYR locally,
# so this residual is spread across smaller available EM currencies.
RESIDUAL_WEIGHT_PCT = 1.04 + 5.25
RESIDUAL_MEMBERS = [
    ("Chile", "CLP", "CLPUSD=X", "direct"),
    ("Colombia", "COP", "COPUSD=X", "direct"),
    ("Czech Republic", "CZK", "CZKUSD=X", "direct"),
    ("Greece", "EUR", "EURUSD=X", "direct"),
    ("Hungary", "HUF", "HUFUSD=X", "direct"),
    ("Indonesia", "IDR", "IDRUSD=X", "direct"),
    ("Kuwait", "KWD", "USDKWD=X", "inverse"),
    ("Philippines", "PHP", "PHPUSD=X", "direct"),
    ("Thailand", "THB", "THBUSD=X", "direct"),
    ("Turkey", "TRY", "TRYUSD=X", "direct"),
]

RESIDUAL_COMPONENTS = [
    Component(country, currency, ticker, orientation, RESIDUAL_WEIGHT_PCT / len(RESIDUAL_MEMBERS), "residual")
    for country, currency, ticker, orientation in RESIDUAL_MEMBERS
]

COMPONENTS = EXPLICIT_COMPONENTS + RESIDUAL_COMPONENTS


def fetch_component_prices(start_date: str) -> pd.DataFrame:
    tickers = sorted({component.ticker for component in COMPONENTS})
    placeholders = ",".join(["?"] * len(tickers))
    query = f"""
        SELECT Date, Ticker, Close
        FROM prices_long
        WHERE Ticker IN ({placeholders}) AND Date >= ?
        ORDER BY Date ASC
    """

    with sqlite3.connect(SQLITE_DB) as conn:
        raw = pd.read_sql_query(query, conn, params=tickers + [start_date])

    if raw.empty:
        raise RuntimeError("No component FX prices found in prices_long")

    pivot = raw.pivot(index="Date", columns="Ticker", values="Close").sort_index()
    missing = [ticker for ticker in tickers if ticker not in pivot.columns]
    if missing:
        raise RuntimeError(f"Missing component FX series: {', '.join(missing)}")

    converted = pd.DataFrame(index=pivot.index)
    for component in COMPONENTS:
        source = pivot[component.ticker].astype(float)
        if component.orientation == "direct":
            converted[component.country] = source
        elif component.orientation == "inverse":
            converted[component.country] = 1.0 / source
        else:
            raise ValueError(f"Unknown orientation for {component.country}: {component.orientation}")

    converted = converted.replace([np.inf, -np.inf], np.nan).dropna(how="any")
    if converted.empty:
        raise RuntimeError("No common date range across component FX series")
    return converted


def calculate_index(start_date: str = START_DATE) -> pd.DataFrame:
    prices = fetch_component_prices(start_date)
    returns = prices.pct_change(fill_method=None).fillna(0.0)
    outliers = returns.abs() > MAX_DAILY_FX_MOVE
    returns = returns.mask(outliers, 0.0)

    weights = pd.Series(
        {component.country: component.weight_pct for component in COMPONENTS},
        dtype=float,
    )
    weights = weights / weights.sum()

    portfolio_returns = returns.mul(weights, axis=1).sum(axis=1)
    values = INITIAL_VALUE * (1.0 + portfolio_returns).cumprod()

    result = pd.DataFrame({
        "Date": pd.to_datetime(values.index).strftime("%Y-%m-%d 00:00:00"),
        TICKER: values.values,
    })
    result.attrs["outlier_count"] = int(outliers.to_numpy().sum())
    result.attrs["outliers_by_country"] = {
        country: int(count)
        for country, count in outliers.sum().items()
        if int(count) > 0
    }
    return result


def print_summary(df: pd.DataFrame) -> None:
    print(f"\n{TICKER}: {NAME}")
    print(f"Dates: {df['Date'].min()} to {df['Date'].max()} ({len(df):,} rows)")
    print(f"First value: {df[TICKER].iloc[0]:.2f}")
    print(f"Latest value: {df[TICKER].iloc[-1]:.2f}")

    first = df[TICKER].iloc[0]
    latest = df[TICKER].iloc[-1]
    print(f"Full-period change: {(latest / first - 1) * 100:+.2f}%")

    ytd = df[df["Date"] >= "2026-01-01 00:00:00"]
    if not ytd.empty:
        print(f"2026 YTD change: {(ytd[TICKER].iloc[-1] / ytd[TICKER].iloc[0] - 1) * 100:+.2f}%")

    outlier_count = df.attrs.get("outlier_count", 0)
    if outlier_count:
        print(
            f"Neutralized outlier component returns: {outlier_count} "
            f"(absolute daily move > {MAX_DAILY_FX_MOVE:.0%})"
        )
        outliers = df.attrs.get("outliers_by_country", {})
        print("Outlier countries: " + ", ".join(f"{k}={v}" for k, v in outliers.items()))

    print("\nWeights:")
    for component in COMPONENTS:
        print(
            f"  {component.country:22s} {component.currency:3s} "
            f"{component.weight_pct:5.2f}% {component.ticker:10s} {component.bucket}"
        )


def store_sqlite(df: pd.DataFrame) -> None:
    rows = list(zip(df["Date"], [TICKER] * len(df), df[TICKER].astype(float)))
    with sqlite3.connect(SQLITE_DB, timeout=30) as conn:
        conn.executemany(
            "INSERT OR REPLACE INTO prices_long (Date, Ticker, Close) VALUES (?, ?, ?)",
            rows,
        )
        conn.execute(
            """
            INSERT OR REPLACE INTO ticker_metadata
            (ticker, name, table_name, data_type, first_date, last_date, data_points)
            VALUES (?, ?, 'prices_long', 'index', ?, ?, ?)
            """,
            (TICKER, NAME, df["Date"].min(), df["Date"].max(), len(df)),
        )
        conn.commit()
    print(f"\nStored {len(rows):,} {TICKER} rows in SQLite prices_long")


def store_duckdb(df: pd.DataFrame) -> None:
    if duckdb is None:
        print("DuckDB module not available; skipping DuckDB store")
        return
    if not DUCKDB_DB.exists():
        print("market_data.duckdb not found; skipping DuckDB store")
        return

    rows = [
        (date[:10], TICKER, float(value))
        for date, value in zip(df["Date"], df[TICKER])
    ]
    con = duckdb.connect(str(DUCKDB_DB), read_only=False)
    try:
        existing = con.execute("SELECT COUNT(*) FROM prices WHERE Ticker = ?", [TICKER]).fetchone()[0]
        if existing:
            print(f"DuckDB already has {existing:,} {TICKER} rows; leaving them unchanged")
            return
        con.executemany("INSERT INTO prices (Date, Ticker, Close) VALUES (?, ?, ?)", rows)
        con.execute(
            """
            INSERT INTO ticker_metadata
            (ticker, name, table_name, data_type, first_date, last_date, data_points)
            VALUES (?, ?, 'prices', 'index', ?, ?, ?)
            """,
            (TICKER, NAME, df["Date"].min(), df["Date"].max(), float(len(df))),
        )
        print(f"Stored {len(rows):,} {TICKER} rows in DuckDB prices")
    finally:
        con.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--store", action="store_true", help="Store MSEMFX in SQLite prices_long")
    parser.add_argument("--duckdb", action="store_true", help="Also insert MSEMFX into market_data.duckdb if absent")
    parser.add_argument("--start", default=START_DATE, help=f"Start date for component prices (default {START_DATE})")
    args = parser.parse_args()

    df = calculate_index(args.start)
    print_summary(df)

    if args.store:
        store_sqlite(df)
    if args.duckdb:
        store_duckdb(df)

    if not args.store:
        print("\nRun with --store to save the series")


if __name__ == "__main__":
    main()
