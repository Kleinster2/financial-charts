#!/usr/bin/env python3
"""
create_allw_repl_11etf.py

11-ETF replication of ALLW matching actual geographic exposure.

Equity (27.1%):  SPLG 8.6%, VGK 10.9%, EWJ 3.1%, SPEM 2.7%, GXC 1.8%
Bonds (42.9%):   BNDX 21.0%, TLT 13.1%, IEF 8.8%
TIPS (21.5%):    TIP 21.5%
Commodities (8.5%): GLD 6.1%, GSG 2.4%

Variants:
  ALLW_11ETF     — static 1x
  ALLW_11ETF_DYN — dynamic weights + leverage (interpolated from snapshots)

Usage:
    python scripts/create_allw_repl_11etf.py [--store]
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / 'charting_app'))

import sqlite3
import pandas as pd
import numpy as np

DB_PATH = Path(__file__).parent.parent / 'market_data.db'
BASE_DATE = '2025-03-06'
FINANCING_RATE = 0.048

# --- Sub-weights within each asset class (from Oct 2025 holdings) ---

# Equity sub-weights (% of equity sleeve, from notional values)
EQUITY_SUBS = {
    'SPLG': 0.316,  # US large cap
    'VGK':  0.401,  # Europe + UK + Australia equity futures
    'EWJ':  0.116,  # Japan (TOPIX)
    'SPEM': 0.100,  # EM
    'GXC':  0.068,  # China
}

# Bond sub-weights (from geographic breakdown in note)
BOND_SUBS = {
    'TLT':  0.51 * 0.6,   # US long bonds (60% of US sleeve)
    'IEF':  0.51 * 0.4,   # US intermediate (40% of US sleeve)
    'BNDX': 0.49,          # International (Euro-Bund, Gilt, Australian)
}

# Commodity sub-weights (from holdings)
COMMOD_SUBS = {
    'GLD': 0.72,   # Gold futures
    'GSG': 0.28,   # BCOMTR broad commodity
}

# --- Asset class weight snapshots (from allocation evolution table) ---

WEIGHT_SCHEDULE = [
    # date,         equity, bonds,  TIPS,   commodities
    ('2025-03-06',  0.250,  0.475,  0.194,  0.081),
    ('2025-05-15',  0.432,  0.344,  0.157,  0.067),
    ('2025-08-05',  0.539,  0.280,  0.131,  0.051),
    ('2025-12-15',  0.269,  0.452,  0.215,  0.064),
    ('2026-03-11',  0.271,  0.429,  0.215,  0.085),
]

LEVERAGE_SCHEDULE = [
    ('2025-03-06', 0.78),
    ('2025-05-15', 1.00),
    ('2025-08-05', 1.23),
    ('2025-12-15', 1.60),
    ('2026-03-11', 1.71),
]

# March 2026 static weights (for 1x version)
STATIC_WEIGHTS = {}
eq, bonds, tips, commod = 0.271, 0.429, 0.215, 0.085
for t, w in EQUITY_SUBS.items():
    STATIC_WEIGHTS[t] = eq * w
for t, w in BOND_SUBS.items():
    STATIC_WEIGHTS[t] = bonds * w
STATIC_WEIGHTS['TIP'] = tips
for t, w in COMMOD_SUBS.items():
    STATIC_WEIGHTS[t] = commod * w

ALL_TICKERS = list(STATIC_WEIGHTS.keys())


def get_component_prices():
    """Get prices for all 11 proxy ETFs."""
    conn = sqlite3.connect(DB_PATH)
    ticker_cols = ', '.join([f'"{t}"' for t in ALL_TICKERS])
    query = f"""
        SELECT Date, {ticker_cols}
        FROM stock_prices_daily
        WHERE Date >= '2025-03-01'
        ORDER BY Date ASC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_allw_prices():
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT Date, "ALLW" as price
        FROM stock_prices_daily
        WHERE Date >= '2025-03-01' AND "ALLW" IS NOT NULL
        ORDER BY Date ASC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def compute_returns(prices_df):
    """Compute daily returns for each ticker."""
    returns = {}
    for ticker in ALL_TICKERS:
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


def interpolate_series(dates, schedule):
    """Linearly interpolate a schedule over trading dates."""
    sched_dates = pd.to_datetime([d for d, *_ in schedule])
    dates_dt = pd.to_datetime(dates, format='mixed')
    dates_int = dates_dt.astype(np.int64)
    sched_int = sched_dates.astype(np.int64)
    return dates_dt, dates_int, sched_int


def interpolate_leverage(dates):
    dates_dt, dates_int, sched_int = interpolate_series(dates, LEVERAGE_SCHEDULE)
    values = [v for _, v in LEVERAGE_SCHEDULE]
    lev = np.interp(dates_int, sched_int, values)
    lev[dates_dt < pd.to_datetime(LEVERAGE_SCHEDULE[0][0])] = values[0]
    lev[dates_dt > pd.to_datetime(LEVERAGE_SCHEDULE[-1][0])] = values[-1]
    return lev


def interpolate_asset_weights(dates):
    """Interpolate 4 asset class weights, then distribute to sub-ETFs."""
    dates_dt, dates_int, sched_int = interpolate_series(dates, WEIGHT_SCHEDULE)
    sched_dates = pd.to_datetime([d for d, *_ in WEIGHT_SCHEDULE])

    # Interpolate each asset class
    asset_classes = {}
    for idx, name in enumerate(['equity', 'bonds', 'tips', 'commod']):
        values = [row[idx + 1] for row in WEIGHT_SCHEDULE]
        w = np.interp(dates_int, sched_int, values)
        w[dates_dt < sched_dates[0]] = values[0]
        w[dates_dt > sched_dates[-1]] = values[-1]
        asset_classes[name] = w

    # Distribute to individual ETFs using static sub-weights
    weights = {}
    for t, sub_w in EQUITY_SUBS.items():
        weights[t] = asset_classes['equity'] * sub_w
    for t, sub_w in BOND_SUBS.items():
        weights[t] = asset_classes['bonds'] * sub_w
    weights['TIP'] = asset_classes['tips']
    for t, sub_w in COMMOD_SUBS.items():
        weights[t] = asset_classes['commod'] * sub_w

    return weights


def build_index(dates, returns, weights_dict, leverage=None, initial_price=25.0):
    """
    Build price series from returns and weights.

    weights_dict: {ticker: float} for static, {ticker: np.array} for dynamic
    leverage: None for 1x, np.array for levered
    """
    daily_financing = FINANCING_RATE / 252
    n = len(dates)

    base_idx = None
    for i, d in enumerate(dates):
        if str(d)[:10] >= BASE_DATE:
            base_idx = i
            break
    if base_idx is None:
        base_idx = 0

    portfolio_returns = np.zeros(n)
    for i in range(n):
        r = 0.0
        for ticker in ALL_TICKERS:
            if ticker not in returns:
                continue
            w = weights_dict[ticker] if isinstance(weights_dict[ticker], (int, float)) else weights_dict[ticker][i]
            r += w * returns[ticker][i]

        if leverage is not None:
            r = leverage[i] * r - (leverage[i] - 1) * daily_financing

        portfolio_returns[i] = r

    values = np.zeros(n)
    values[base_idx] = initial_price
    for i in range(base_idx + 1, n):
        values[i] = values[i-1] * (1 + portfolio_returns[i])
    for i in range(base_idx - 1, -1, -1):
        values[i] = values[i+1] / (1 + portfolio_returns[i+1])

    return values


def main():
    store = '--store' in sys.argv

    print(f"\n{'='*60}")
    print("ALLW 11-ETF Replication")
    print(f"{'='*60}\n")

    print("Components:")
    for t, w in STATIC_WEIGHTS.items():
        print(f"  {t:6s} {w*100:5.1f}%")
    print(f"  {'Total':6s} {sum(STATIC_WEIGHTS.values())*100:5.1f}%")

    # Get data
    prices_df = get_component_prices()
    allw_df = get_allw_prices()
    allw_df['Date'] = allw_df['Date'].astype(str).str[:10]

    print(f"\nPrice data: {len(prices_df)} days")

    returns = compute_returns(prices_df)
    dates = prices_df['Date'].values

    # Filter to ALLW inception
    mask = prices_df['Date'] >= BASE_DATE
    dates_f = dates[mask]
    returns_f = {t: r[mask] for t, r in returns.items()}

    # ALLW initial price
    allw_base = allw_df.loc[allw_df['Date'] >= BASE_DATE[:10], 'price']
    initial_price = float(allw_base.iloc[0]) if not allw_base.empty else 25.0

    # 1. Static 1x
    static_vals = build_index(dates_f, returns_f, STATIC_WEIGHTS, initial_price=initial_price)

    # 2. Dynamic weights + leverage
    leverage = interpolate_leverage(dates_f)
    dyn_weights = interpolate_asset_weights(dates_f)
    dyn_vals = build_index(dates_f, returns_f, dyn_weights, leverage=leverage, initial_price=initial_price)

    # Build result
    result_df = pd.DataFrame({
        'Date': dates_f,
        'ALLW_11ETF': static_vals,
        'ALLW_11ETF_DYN': dyn_vals,
    })
    result_df = result_df[result_df['ALLW_11ETF'] > 0]

    # Performance
    s_ret = (result_df['ALLW_11ETF'].iloc[-1] / result_df['ALLW_11ETF'].iloc[0] - 1) * 100
    d_ret = (result_df['ALLW_11ETF_DYN'].iloc[-1] / result_df['ALLW_11ETF_DYN'].iloc[0] - 1) * 100
    allw_ret = (float(allw_base.iloc[-1]) / float(allw_base.iloc[0]) - 1) * 100 if not allw_base.empty else 0

    print(f"\n{'='*55}")
    print(f"  ALLW actual:          {allw_ret:+.2f}%")
    print(f"  ALLW_11ETF_DYN:       {d_ret:+.2f}%  (dynamic + lev)")
    print(f"  ALLW_11ETF (1x):      {s_ret:+.2f}%  (static)")
    print(f"  ---")
    print(f"  Residual (vs DYN):    {allw_ret - d_ret:+.2f}pp")
    print(f"  4-ETF residual was:   +8.59pp")
    print(f"  Gap closed:           {8.59 - (allw_ret - d_ret):.2f}pp")
    print(f"{'='*55}")

    if store:
        for ticker in ['ALLW_11ETF', 'ALLW_11ETF_DYN']:
            df_narrow = result_df[['Date', ticker]].rename(columns={ticker: 'Close'}).copy()
            df_narrow['Ticker'] = ticker
            conn = sqlite3.connect(DB_PATH, timeout=30)
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

            conn = sqlite3.connect(DB_PATH, timeout=30)
            conn.execute('''
                INSERT OR REPLACE INTO ticker_metadata
                (ticker, name, table_name, data_type, first_date, last_date, data_points)
                VALUES (?, ?, 'prices_long', 'index', ?, ?, ?)
            ''', (ticker,
                  f'ALLW 11-ETF Replication {"Dynamic Lev" if "DYN" in ticker else "1x"}',
                  result_df['Date'].min(), result_df['Date'].max(), len(result_df)))
            conn.commit()
            conn.close()

        print(f"\n[DONE] Stored. Chart: /api/chart/lw?tickers=ALLW,ALLW_11ETF_DYN,ALLW_11ETF&start=2025-03-06&normalize=true&primary=ALLW")


if __name__ == "__main__":
    main()
