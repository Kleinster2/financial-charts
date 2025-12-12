import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
#!/usr/bin/env python3
"""
create_synthetic_ticker.py

Calculate synthetic ticker values for replicated portfolios.
This creates a daily price series based on weighted returns of components.
"""

import sys
from datetime import datetime
import pandas as pd
import numpy as np

from constants import DB_PATH, get_db_connection


def get_portfolio_composition(portfolio_name: str, as_of_date: str):
    """Get portfolio weights as of a specific date."""
    conn = get_db_connection()

    query = """
        SELECT ticker, weight
        FROM replication_portfolios
        WHERE portfolio_name = ? AND as_of_date = ?
        AND ticker != 'CASH'
        ORDER BY weight DESC
    """

    df = pd.read_sql_query(query, conn, params=(portfolio_name, as_of_date))
    conn.close()

    if df.empty:
        return None

    return dict(zip(df['ticker'], df['weight']))


def get_component_prices(tickers: list, start_date: str = None):
    """Get historical prices for all component tickers."""
    conn = get_db_connection()

    # Build query to get all tickers
    ticker_cols = ', '.join([f'"{ticker}"' for ticker in tickers])

    query = f"""
        SELECT Date, {ticker_cols}
        FROM stock_prices_daily
        WHERE Date >= ?
        ORDER BY Date ASC
    """

    # Default to 2 years of history if not specified
    if start_date is None:
        start_date = '2023-01-01'

    df = pd.read_sql_query(query, conn, params=(start_date,))
    conn.close()

    return df


def calculate_synthetic_ticker(portfolio_name: str, as_of_date: str,
                               synthetic_ticker: str = None,
                               start_date: str = None,
                               initial_value: float = 100.0):
    """
    Calculate synthetic ticker value for a portfolio.

    Args:
        portfolio_name: Name of portfolio (e.g., 'ALLW_SCALED')
        as_of_date: Portfolio composition date
        synthetic_ticker: Ticker symbol (e.g., 'ALLW_SCALED_SYN')
        start_date: Start date for calculation (default: 2023-01-01)
        initial_value: Starting value (default: 100.0)

    Returns:
        DataFrame with Date and synthetic ticker value
    """

    if synthetic_ticker is None:
        synthetic_ticker = f"{portfolio_name}_SYN"

    print(f"\n{'='*70}")
    print(f"Creating Synthetic Ticker: {synthetic_ticker}")
    print(f"Portfolio: {portfolio_name} (as of {as_of_date})")
    print(f"{'='*70}\n")

    # Get portfolio composition
    weights = get_portfolio_composition(portfolio_name, as_of_date)
    if weights is None:
        print(f"Error: Portfolio {portfolio_name} not found for {as_of_date}")
        return None

    print("Portfolio Composition:")
    for ticker, weight in weights.items():
        print(f"  {ticker}: {weight*100:.2f}%")
    print()

    # Get component prices
    tickers = list(weights.keys())
    prices_df = get_component_prices(tickers, start_date)

    if prices_df.empty:
        print("Error: No price data found")
        return None

    print(f"Price data: {len(prices_df)} days from {prices_df['Date'].min()} to {prices_df['Date'].max()}")

    # Calculate daily returns for each component
    returns_data = {'Date': prices_df['Date'].values}

    for ticker in tickers:
        if ticker in prices_df.columns:
            prices = prices_df[ticker].values
            # Calculate percent change
            returns = np.zeros(len(prices))
            returns[0] = 0  # First day has no return

            for i in range(1, len(prices)):
                if pd.notna(prices[i]) and pd.notna(prices[i-1]) and prices[i-1] != 0:
                    returns[i] = (prices[i] - prices[i-1]) / prices[i-1]
                else:
                    returns[i] = 0

            returns_data[ticker] = returns

    returns_df = pd.DataFrame(returns_data)

    # Calculate portfolio daily return (weighted average)
    portfolio_returns = np.zeros(len(returns_df))

    for ticker, weight in weights.items():
        if ticker in returns_df.columns:
            portfolio_returns += returns_df[ticker].values * weight

    # Calculate cumulative value
    portfolio_value = np.zeros(len(portfolio_returns))
    portfolio_value[0] = initial_value

    for i in range(1, len(portfolio_returns)):
        portfolio_value[i] = portfolio_value[i-1] * (1 + portfolio_returns[i])

    # Create result dataframe
    result_df = pd.DataFrame({
        'Date': returns_df['Date'],
        synthetic_ticker: portfolio_value
    })

    # Calculate performance metrics
    total_return = (portfolio_value[-1] / portfolio_value[0] - 1) * 100
    days = len(portfolio_value)
    annualized_return = ((portfolio_value[-1] / portfolio_value[0]) ** (365.25 / days) - 1) * 100

    print(f"\nSynthetic Ticker Performance:")
    print(f"  Total Return: {total_return:.2f}%")
    print(f"  Annualized Return: {annualized_return:.2f}%")
    print(f"  Initial Value: ${initial_value:.2f}")
    print(f"  Final Value: ${portfolio_value[-1]:.2f}")

    return result_df


def store_synthetic_ticker(df: pd.DataFrame, ticker: str):
    """Store synthetic ticker in stock_prices_daily table."""
    conn = get_db_connection()

    # Check if column exists
    cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
    columns = [row[1] for row in cursor.fetchall()]

    if ticker not in columns:
        print(f"\nAdding column '{ticker}' to stock_prices_daily...")
        conn.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{ticker}" REAL')
        conn.commit()

    # Update values
    print(f"Storing {len(df)} prices for {ticker}...")

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

    print(f"[SUCCESS] Synthetic ticker '{ticker}' stored successfully")


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python create_synthetic_ticker.py <portfolio_name> <as_of_date> [ticker_symbol] [start_date] [--yes]")
        print("\nExamples:")
        print("  python create_synthetic_ticker.py ALLW_SCALED 2025-10-06")
        print("  python create_synthetic_ticker.py ALLW_SCALED 2025-10-06 ALLW_SYN")
        print("  python create_synthetic_ticker.py ALLW_SCALED 2025-10-06 ALLW_SYN 2024-01-01 --yes")
        print("\nAvailable portfolios:")
        conn = get_db_connection()
        cursor = conn.execute("""
            SELECT DISTINCT portfolio_name, as_of_date
            FROM replication_portfolios
            ORDER BY as_of_date DESC
        """)
        for portfolio_name, date in cursor.fetchall():
            print(f"  - {portfolio_name} ({date})")
        conn.close()
        sys.exit(1)

    # Parse arguments
    auto_yes = '--yes' in sys.argv or '-y' in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]

    portfolio_name = args[0]
    as_of_date = args[1]
    ticker_symbol = args[2] if len(args) > 2 else None
    start_date = args[3] if len(args) > 3 else '2023-01-01'

    # Calculate synthetic ticker
    result_df = calculate_synthetic_ticker(
        portfolio_name, as_of_date, ticker_symbol, start_date
    )

    if result_df is not None:
        ticker = result_df.columns[1]

        # Ask to store
        if auto_yes:
            response = 'y'
        else:
            print(f"\nStore '{ticker}' in database? (y/n): ", end='')
            response = input().strip().lower()

        if response == 'y':
            store_synthetic_ticker(result_df, ticker)
            print(f"\n[DONE] You can now chart '{ticker}' in your charting app")
        else:
            print("\nNot stored. Data preview:")
            print(result_df.tail(10))


if __name__ == "__main__":
    main()
