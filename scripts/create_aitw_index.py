#!/usr/bin/env python3
"""
create_aitw_index.py

Create AI Transition Winners (AITW) basket index.
Tracks stocks repositioning as AI implementation partners/beneficiaries
despite initial thesis that they would be disruption victims.

Constituents (Feb 2026):
- HCLTECH.NS: HCL Tech (engineering focus, AI implementation)
- PUB.PA: Publicis (Epsilon first-party data moat)

Splintered from AIWD after performance divergence showed these names
are transition winners, not disruption victims.

Usage:
    python scripts/create_aitw_index.py [--store]
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime

DB_PATH = Path(__file__).parent.parent / 'market_data.db'

# Index constituents and weights
AITW_WEIGHTS = {
    # AI Implementation Partners
    'HCLTECH.NS': 0.50,  # HCL Tech - engineering services, AI implementation
    'PUB.PA': 0.50,      # Publicis - Epsilon data moat, data-driven marketing
}

# Base date for index = 100
BASE_DATE = '2026-02-03'
INITIAL_VALUE = 100.0


def get_component_prices(start_date: str = '2021-07-01'):
    """Get historical prices for all component tickers."""
    conn = sqlite3.connect(DB_PATH)

    tickers = list(AITW_WEIGHTS.keys())
    ticker_cols = ', '.join([f'"{ticker}"' for ticker in tickers])

    query = f"""
        SELECT Date, {ticker_cols}
        FROM stock_prices_daily
        WHERE Date >= ?
        ORDER BY Date ASC
    """

    df = pd.read_sql_query(query, conn, params=(start_date,))
    conn.close()

    return df


def calculate_aitw_index(start_date: str = '2021-07-01'):
    """Calculate AITW index values."""

    print(f"\n{'='*70}")
    print("AI Transition Winners (AITW) Index")
    print(f"{'='*70}\n")

    print("Constituents:")
    for ticker, weight in AITW_WEIGHTS.items():
        print(f"  {ticker:12s} {weight*100:5.1f}%")
    print(f"\n  Total: {sum(AITW_WEIGHTS.values())*100:.0f}%")
    print(f"\nBase date: {BASE_DATE} = {INITIAL_VALUE}")

    # Get prices
    prices_df = get_component_prices(start_date)

    if prices_df.empty:
        print("Error: No price data found")
        return None

    print(f"\nPrice data: {len(prices_df)} days from {prices_df['Date'].min()} to {prices_df['Date'].max()}")

    # Calculate daily returns
    tickers = list(AITW_WEIGHTS.keys())
    returns_data = {'Date': prices_df['Date'].values}

    for ticker in tickers:
        if ticker in prices_df.columns:
            prices = prices_df[ticker].values
            returns = np.zeros(len(prices))
            returns[0] = 0

            for i in range(1, len(prices)):
                if pd.notna(prices[i]) and pd.notna(prices[i-1]) and prices[i-1] != 0:
                    returns[i] = (prices[i] - prices[i-1]) / prices[i-1]
                else:
                    returns[i] = 0

            returns_data[ticker] = returns
        else:
            print(f"  Warning: {ticker} not in price data")

    returns_df = pd.DataFrame(returns_data)

    # Calculate weighted portfolio return
    portfolio_returns = np.zeros(len(returns_df))

    for ticker, weight in AITW_WEIGHTS.items():
        if ticker in returns_df.columns:
            portfolio_returns += returns_df[ticker].values * weight

    # Find base date index
    dates = returns_df['Date'].values
    base_idx = None
    for i, d in enumerate(dates):
        if str(d)[:10] >= BASE_DATE:
            base_idx = i
            break

    if base_idx is None:
        print(f"Warning: Base date {BASE_DATE} not found, using first date")
        base_idx = 0

    # Calculate cumulative value (working backwards and forwards from base date)
    portfolio_value = np.zeros(len(portfolio_returns))
    portfolio_value[base_idx] = INITIAL_VALUE

    # Forward from base date
    for i in range(base_idx + 1, len(portfolio_returns)):
        portfolio_value[i] = portfolio_value[i-1] * (1 + portfolio_returns[i])

    # Backward from base date
    for i in range(base_idx - 1, -1, -1):
        portfolio_value[i] = portfolio_value[i+1] / (1 + portfolio_returns[i+1])

    # Create result
    result_df = pd.DataFrame({
        'Date': returns_df['Date'],
        'AITW': portfolio_value
    })

    # Performance summary
    latest_value = portfolio_value[-1]
    base_value = portfolio_value[base_idx]

    print(f"\nIndex Values:")
    print(f"  Base ({BASE_DATE}): {base_value:.2f}")
    print(f"  Latest: {latest_value:.2f}")
    print(f"  Change from base: {(latest_value/base_value - 1)*100:+.2f}%")

    # Show recent values
    print(f"\nRecent values:")
    recent = result_df.tail(10)
    for _, row in recent.iterrows():
        print(f"  {str(row['Date'])[:10]}: {row['AITW']:.2f}")

    return result_df


def store_index(df: pd.DataFrame):
    """Store AITW index in stock_prices_daily table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if column exists
    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    columns = [row[1] for row in cursor.fetchall()]

    if 'AITW' not in columns:
        print(f"\nAdding column 'AITW' to stock_prices_daily...")
        cursor.execute('ALTER TABLE stock_prices_daily ADD COLUMN "AITW" REAL')
        conn.commit()

    # Update values
    print(f"Storing {len(df)} prices for AITW...")

    for _, row in df.iterrows():
        date = row['Date']
        value = row['AITW']

        cursor.execute('UPDATE stock_prices_daily SET "AITW" = ? WHERE Date = ?', (value, date))

    conn.commit()

    # Add to ticker_metadata
    cursor.execute('''
        INSERT OR REPLACE INTO ticker_metadata (ticker, name, table_name, data_type, first_date, last_date, data_points)
        VALUES ('AITW', 'AI Transition Winners Index', 'stock_prices_daily', 'index', ?, ?, ?)
    ''', (df['Date'].min(), df['Date'].max(), len(df)))

    conn.commit()
    conn.close()

    print(f"[SUCCESS] AITW index stored successfully")


def main():
    store = '--store' in sys.argv or '-s' in sys.argv

    result_df = calculate_aitw_index()

    if result_df is not None and store:
        store_index(result_df)
        print(f"\n[DONE] You can now chart 'AITW' in your charting app")
    elif result_df is not None:
        print(f"\nRun with --store to save to database")


if __name__ == "__main__":
    main()
