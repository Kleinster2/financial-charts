import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
#!/usr/bin/env python3
"""
create_portfolio_value_series.py

Create ALLW_VALUE and ALLW_SHARES series based on actual holdings.
This tracks the dollar value of your portfolio if you hold a fixed number of shares.
"""

import sys
from datetime import datetime
import pandas as pd
import numpy as np

from constants import DB_PATH, get_db_connection


def create_portfolio_value_series(num_shares: int, portfolio_name: str, as_of_date: str,
                                  start_date: str = '2024-01-01'):
    """
    Create VALUE and SHARES series for tracking portfolio holdings.

    Args:
        num_shares: Number of shares you're tracking (e.g., 100 shares of ALLW_SCALED)
        portfolio_name: Portfolio composition (e.g., 'ALLW_SCALED')
        as_of_date: Date of portfolio composition
        start_date: Start date for historical series
    """

    conn = get_db_connection()

    # Get portfolio composition
    query = """
        SELECT ticker, weight
        FROM replication_portfolios
        WHERE portfolio_name = ? AND as_of_date = ?
        AND ticker != 'CASH'
        ORDER BY weight DESC
    """

    df_portfolio = pd.read_sql_query(query, conn, params=(portfolio_name, as_of_date))

    if df_portfolio.empty:
        print(f"Error: Portfolio {portfolio_name} not found for {as_of_date}")
        conn.close()
        return None

    weights = dict(zip(df_portfolio['ticker'], df_portfolio['weight']))

    print(f"\n{'='*70}")
    print(f"Creating Portfolio Value Series")
    print(f"Portfolio: {portfolio_name} ({as_of_date})")
    print(f"Tracking: {num_shares} shares")
    print(f"{'='*70}\n")

    print("Portfolio Composition:")
    for ticker, weight in weights.items():
        print(f"  {ticker}: {weight*100:.2f}%")
    print()

    # Get component prices
    tickers = list(weights.keys())
    ticker_cols = ', '.join([f'"{ticker}"' for ticker in tickers])

    query = f"""
        SELECT Date, {ticker_cols}
        FROM stock_prices_daily
        WHERE Date >= ?
        ORDER BY Date ASC
    """

    prices_df = pd.read_sql_query(query, conn, params=(start_date,))
    conn.close()

    if prices_df.empty:
        print("Error: No price data found")
        return None

    print(f"Price data: {len(prices_df)} days from {prices_df['Date'].min()} to {prices_df['Date'].max()}\n")

    # Calculate portfolio value per share
    portfolio_values = np.zeros(len(prices_df))

    for idx, row in prices_df.iterrows():
        daily_value = 0
        for ticker, weight in weights.items():
            if ticker in prices_df.columns and pd.notna(row[ticker]):
                # This is the value of the weighted component
                daily_value += row[ticker] * weight

        portfolio_values[idx] = daily_value

    # Calculate total portfolio value (if holding num_shares)
    total_values = portfolio_values * num_shares
    shares_series = np.full(len(prices_df), num_shares)

    # Create result dataframes
    value_df = pd.DataFrame({
        'Date': prices_df['Date'],
        f'{portfolio_name}_VALUE': total_values
    })

    shares_df = pd.DataFrame({
        'Date': prices_df['Date'],
        f'{portfolio_name}_SHARES': shares_series
    })

    # Performance stats
    initial_value = total_values[0]
    final_value = total_values[-1]
    total_return = (final_value / initial_value - 1) * 100

    print("Portfolio Value Series Created:")
    print(f"  Per-Share Value (start): ${portfolio_values[0]:.2f}")
    print(f"  Per-Share Value (end): ${portfolio_values[-1]:.2f}")
    print(f"  Total Value (start): ${initial_value:,.2f}")
    print(f"  Total Value (end): ${final_value:,.2f}")
    print(f"  Total Return: {total_return:.2f}%")

    return value_df, shares_df


def store_series(df: pd.DataFrame, ticker: str):
    """Store series in stock_prices_daily table."""
    conn = get_db_connection()

    # Check if column exists
    cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
    columns = [row[1] for row in cursor.fetchall()]

    if ticker not in columns:
        print(f"\nAdding column '{ticker}' to stock_prices_daily...")
        conn.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')
        conn.commit()

    # Update values
    print(f"Storing {len(df)} values for {ticker}...")

    for _, row in df.iterrows():
        date = row['Date']
        value = row[ticker]

        # Check if date exists
        cursor = conn.execute("SELECT 1 FROM stock_prices_daily WHERE Date = ?", (date,))
        exists = cursor.fetchone() is not None

        if exists:
            conn.execute(f'UPDATE stock_prices_daily SET "{ticker}" = ? WHERE Date = ?',
                        (value, date))
        else:
            conn.execute(f'INSERT INTO stock_prices_daily (Date, "{ticker}") VALUES (?, ?)',
                        (date, value))

    conn.commit()
    conn.close()

    print(f"[SUCCESS] Series '{ticker}' stored successfully")


def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print("  python create_portfolio_value_series.py <num_shares> <portfolio_name> <as_of_date> [start_date] [--yes]")
        print("\nExamples:")
        print("  python create_portfolio_value_series.py 100 ALLW_SCALED 2025-10-06 --yes")
        print("  python create_portfolio_value_series.py 1000 ALLW_SCALED 2025-10-06 2024-01-01 --yes")
        print("\nThis creates two series:")
        print("  - {PORTFOLIO}_VALUE: Total dollar value of your holdings")
        print("  - {PORTFOLIO}_SHARES: Number of shares (constant)")
        sys.exit(1)

    # Parse arguments
    auto_yes = '--yes' in sys.argv or '-y' in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]

    num_shares = int(args[0])
    portfolio_name = args[1]
    as_of_date = args[2]
    start_date = args[3] if len(args) > 3 else '2024-01-01'

    # Create series
    result = create_portfolio_value_series(num_shares, portfolio_name, as_of_date, start_date)

    if result is not None:
        value_df, shares_df = result

        value_ticker = value_df.columns[1]
        shares_ticker = shares_df.columns[1]

        # Ask to store
        if auto_yes:
            response = 'y'
        else:
            print(f"\nStore '{value_ticker}' and '{shares_ticker}' in database? (y/n): ", end='')
            response = input().strip().lower()

        if response == 'y':
            store_series(value_df, value_ticker)
            store_series(shares_df, shares_ticker)
            print(f"\n[DONE] You can now chart '{value_ticker}' and '{shares_ticker}' in your charting app")
        else:
            print("\nNot stored.")


if __name__ == "__main__":
    main()
