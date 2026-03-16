#!/usr/bin/env python3
"""
replication_utils.py

Shared utilities for ETF/index replication scripts.

Functions:
  get_prices(tickers, start_date, db_path)  — fetch prices from wide or narrow table
  compute_returns(prices_df, tickers)        — daily returns from price DataFrame
  build_index(dates, returns, weights, ...)  — synthetic index from weighted returns
  interpolate_schedule(dates, schedule)      — linearly interpolate a dated schedule
  store_ticker(result_df, col, ticker, name, db_path) — upsert to prices_long + metadata
  generate_charts(ticker, comparisons, start, output_dir) — standard 4-chart set via API

Used by: create_allw_repl_*.py, create_aiwd_index.py, and any future replication scripts.
"""

import sqlite3
import numpy as np
import pandas as pd
from pathlib import Path

DEFAULT_DB = Path(__file__).parent.parent / 'market_data.db'


# ---------------------------------------------------------------------------
# Price retrieval
# ---------------------------------------------------------------------------

def get_prices(tickers, start_date='2020-01-01', db_path=None):
    """Fetch daily prices for tickers from wide table, falling back to narrow.

    Returns DataFrame with Date column + one column per ticker.
    """
    db = db_path or DEFAULT_DB
    conn = sqlite3.connect(str(db))

    # Try wide table first
    try:
        cols = ', '.join([f'"{t}"' for t in tickers])
        query = f"""
            SELECT Date, {cols}
            FROM stock_prices_daily
            WHERE Date >= '{start_date}'
            ORDER BY Date ASC
        """
        df = pd.read_sql_query(query, conn)
        # Check if any columns came back
        found = [t for t in tickers if t in df.columns and df[t].notna().any()]
        missing = [t for t in tickers if t not in found]
    except Exception:
        found = []
        missing = list(tickers)
        df = None

    # Fall back to narrow table for missing tickers
    if missing:
        placeholders = ', '.join(['?'] * len(missing))
        narrow_q = f"""
            SELECT Date, Ticker, Close
            FROM prices_long
            WHERE Ticker IN ({placeholders}) AND Date >= ?
            ORDER BY Date ASC
        """
        narrow_df = pd.read_sql_query(narrow_q, conn, params=missing + [start_date])
        if not narrow_df.empty:
            pivoted = narrow_df.pivot(index='Date', columns='Ticker', values='Close').reset_index()
            if df is not None and not df.empty:
                df = df.merge(pivoted, on='Date', how='outer', suffixes=('', '_narrow'))
                # Fill from narrow where wide was missing
                for t in missing:
                    if t in pivoted.columns:
                        if t not in df.columns:
                            df[t] = df.get(f'{t}_narrow', np.nan)
                        else:
                            df[t] = df[t].fillna(df.get(f'{t}_narrow', np.nan))
                # Drop _narrow suffixed columns
                df = df[[c for c in df.columns if not c.endswith('_narrow')]]
            else:
                df = pivoted

    conn.close()

    if df is None or df.empty:
        raise ValueError(f"No price data found for {tickers} after {start_date}")

    df = df.sort_values('Date').reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# Returns computation
# ---------------------------------------------------------------------------

def compute_returns(prices_df, tickers):
    """Compute daily returns for each ticker from a prices DataFrame.

    Returns dict: {ticker: np.array of daily returns (0 on first day)}.
    """
    returns = {}
    for ticker in tickers:
        if ticker not in prices_df.columns:
            print(f"  Warning: {ticker} not in price data")
            continue
        p = prices_df[ticker].values
        r = np.zeros(len(p))
        for i in range(1, len(p)):
            if pd.notna(p[i]) and pd.notna(p[i-1]) and p[i-1] != 0:
                r[i] = (p[i] - p[i-1]) / p[i-1]
        returns[ticker] = r
    return returns


# ---------------------------------------------------------------------------
# Index construction
# ---------------------------------------------------------------------------

def build_index(dates, returns, weights, leverage=None, financing_rate=0.048,
                base_date=None, initial_price=100.0):
    """Build a synthetic price series from weighted daily returns.

    Args:
        dates:          array of date strings
        returns:        dict {ticker: np.array} of daily returns
        weights:        dict {ticker: float} for static, or {ticker: np.array} for dynamic
        leverage:       None for 1x, or np.array of daily leverage ratios
        financing_rate: annual rate for leverage cost (default 4.8%)
        base_date:      date string to anchor initial_price (default: first date)
        initial_price:  price at base_date

    Returns:
        np.array of synthetic prices
    """
    daily_financing = financing_rate / 252
    n = len(dates)

    # Find base index
    base_idx = 0
    if base_date:
        for i, d in enumerate(dates):
            if str(d)[:10] >= base_date:
                base_idx = i
                break

    # Compute weighted portfolio returns
    portfolio_returns = np.zeros(n)
    for i in range(n):
        r = 0.0
        for ticker, w in weights.items():
            if ticker not in returns:
                continue
            wi = w if isinstance(w, (int, float)) else w[i]
            r += wi * returns[ticker][i]

        if leverage is not None:
            r = leverage[i] * r - (leverage[i] - 1) * daily_financing

        portfolio_returns[i] = r

    # Compound from base
    values = np.zeros(n)
    values[base_idx] = initial_price
    for i in range(base_idx + 1, n):
        values[i] = values[i-1] * (1 + portfolio_returns[i])
    for i in range(base_idx - 1, -1, -1):
        values[i] = values[i+1] / (1 + portfolio_returns[i+1])

    return values


# ---------------------------------------------------------------------------
# Schedule interpolation
# ---------------------------------------------------------------------------

def interpolate_schedule(dates, schedule):
    """Linearly interpolate a list of (date_str, value) pairs over trading dates.

    Args:
        dates:    array of date strings (trading calendar)
        schedule: list of (date_str, value) tuples

    Returns:
        np.array of interpolated values, clamped at edges
    """
    dates_dt = pd.to_datetime(dates, format='mixed')
    dates_int = dates_dt.astype(np.int64)
    sched_dates = pd.to_datetime([d for d, _ in schedule])
    sched_int = sched_dates.astype(np.int64)
    sched_vals = [v for _, v in schedule]

    result = np.interp(dates_int, sched_int, sched_vals)
    result[dates_dt < sched_dates[0]] = sched_vals[0]
    result[dates_dt > sched_dates[-1]] = sched_vals[-1]
    return result


def interpolate_weight_schedule(dates, schedule):
    """Interpolate a multi-asset weight schedule.

    Args:
        dates:    array of date strings
        schedule: list of (date_str, w1, w2, ..., wN) tuples

    Returns:
        list of np.arrays, one per weight column
    """
    dates_dt = pd.to_datetime(dates, format='mixed')
    dates_int = dates_dt.astype(np.int64)
    sched_dates = pd.to_datetime([row[0] for row in schedule])
    sched_int = sched_dates.astype(np.int64)

    n_weights = len(schedule[0]) - 1  # exclude date column
    results = []
    for col in range(n_weights):
        vals = [row[col + 1] for row in schedule]
        interp = np.interp(dates_int, sched_int, vals)
        interp[dates_dt < sched_dates[0]] = vals[0]
        interp[dates_dt > sched_dates[-1]] = vals[-1]
        results.append(interp)
    return results


# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------

def store_ticker(result_df, date_col, value_col, ticker, name, db_path=None):
    """Upsert a synthetic ticker to prices_long + ticker_metadata.

    Args:
        result_df:  DataFrame with dates and values
        date_col:   column name for dates
        value_col:  column name for price values
        ticker:     ticker string (e.g. 'ALLW_REPL')
        name:       human-readable name
        db_path:    path to SQLite database
    """
    db = db_path or DEFAULT_DB
    df_narrow = result_df[[date_col, value_col]].rename(
        columns={value_col: 'Close', date_col: 'Date'}
    ).copy()
    df_narrow['Ticker'] = ticker
    df_narrow = df_narrow[df_narrow['Close'] > 0]

    conn = sqlite3.connect(str(db), timeout=30)
    try:
        rows = list(zip(df_narrow['Date'], df_narrow['Ticker'], df_narrow['Close']))
        conn.executemany(
            'INSERT OR REPLACE INTO prices_long (Date, Ticker, Close) VALUES (?, ?, ?)',
            rows
        )
        conn.commit()
        print(f"  {ticker}: upserted {len(rows):,} rows")
    finally:
        conn.close()

    conn = sqlite3.connect(str(db), timeout=30)
    try:
        conn.execute('''
            INSERT OR REPLACE INTO ticker_metadata
            (ticker, name, table_name, data_type, first_date, last_date, data_points)
            VALUES (?, ?, 'prices_long', 'index', ?, ?, ?)
        ''', (ticker, name,
              str(df_narrow['Date'].min()),
              str(df_narrow['Date'].max()),
              len(df_narrow)))
        conn.commit()
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Chart generation helpers
# ---------------------------------------------------------------------------

def rolling_correlation(prices_df, target_col, compare_cols, window=30):
    """Compute rolling correlation of target vs multiple comparison series.

    Args:
        prices_df:    DataFrame with Date + price columns
        target_col:   the reference ticker column
        compare_cols: list of ticker columns to correlate against target
        window:       rolling window in trading days

    Returns:
        DataFrame with Date + one column per comparison ticker (correlation values)
    """
    df = prices_df.copy()
    # Compute returns
    for col in [target_col] + compare_cols:
        df[f'{col}_ret'] = df[col].pct_change()

    result = pd.DataFrame({'Date': df['Date']})
    for col in compare_cols:
        result[col] = df[f'{target_col}_ret'].rolling(window).corr(df[f'{col}_ret'])

    return result


def notional_breakdown(dates, weights_dict, nav=None, leverage=None):
    """Compute notional exposure by asset class.

    Args:
        dates:        array of dates
        weights_dict: dict {class_name: np.array of weight fractions}
        nav:          np.array of NAV values (optional, for absolute chart)
        leverage:     np.array of leverage ratios (optional)

    Returns:
        dict with 'dates', 'pct' (percentages), and optionally 'abs' (dollar amounts)
    """
    # Percentages
    total_w = sum(weights_dict.values())
    pct = {name: w / total_w * 100 for name, w in weights_dict.items()}

    result = {'dates': dates, 'pct': pct}

    # Absolute amounts
    if nav is not None and leverage is not None:
        gross = nav * leverage
        result['abs'] = {name: gross * w for name, w in weights_dict.items()}
        result['nav'] = nav

    return result
