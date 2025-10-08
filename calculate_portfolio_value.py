#!/usr/bin/env python3
"""
calculate_portfolio_value.py

Calculate portfolio weights based on actual market prices and ALLW portfolio value.
Shows how many shares to buy of each component and the resulting dollar values.
"""

import sys
from datetime import datetime, timedelta
import pandas as pd

from constants import DB_PATH, get_db_connection


def get_latest_price(ticker: str, conn) -> float:
    """Get the most recent price for a ticker."""
    # Try stock_prices_daily first
    query = f"""
        SELECT Date, "{ticker}" as price
        FROM stock_prices_daily
        WHERE "{ticker}" IS NOT NULL
        ORDER BY Date DESC
        LIMIT 1
    """

    try:
        df = pd.read_sql_query(query, conn)
        if not df.empty and df['price'].notna().any():
            return float(df['price'].iloc[0])
    except Exception as e:
        pass

    return None


def get_allw_nav(conn) -> tuple:
    """Get ALLW's latest NAV (price) and date."""
    query = """
        SELECT Date, "ALLW" as price
        FROM stock_prices_daily
        WHERE "ALLW" IS NOT NULL
        ORDER BY Date DESC
        LIMIT 1
    """

    df = pd.read_sql_query(query, conn)
    if df.empty:
        return None, None

    return float(df['price'].iloc[0]), df['Date'].iloc[0]


def calculate_portfolio_positions(portfolio_name: str, as_of_date: str,
                                   investment_amount: float):
    """Calculate exact positions needed to replicate portfolio."""

    conn = get_db_connection()

    # Get portfolio weights
    query = """
        SELECT ticker, name, weight, category
        FROM replication_portfolios
        WHERE portfolio_name = ? AND as_of_date = ?
        AND ticker != 'CASH'
        ORDER BY weight DESC
    """

    df = pd.read_sql_query(query, conn, params=(portfolio_name, as_of_date))

    if df.empty:
        print(f"Error: Portfolio {portfolio_name} not found for date {as_of_date}")
        conn.close()
        return None

    # Get current prices
    positions = []
    total_value = 0

    print(f"\nFetching current prices...")
    for _, row in df.iterrows():
        ticker = row['ticker']
        weight = row['weight']
        target_value = investment_amount * weight

        price = get_latest_price(ticker, conn)

        if price is None:
            print(f"  Warning: No price found for {ticker}")
            positions.append({
                'ticker': ticker,
                'name': row['name'],
                'weight': weight,
                'target_value': target_value,
                'price': None,
                'shares': None,
                'actual_value': None
            })
            continue

        # Calculate shares (rounded down to avoid over-investing)
        shares = int(target_value / price)
        actual_value = shares * price
        total_value += actual_value

        positions.append({
            'ticker': ticker,
            'name': row['name'],
            'weight': weight,
            'target_value': target_value,
            'price': price,
            'shares': shares,
            'actual_value': actual_value
        })

    conn.close()

    return pd.DataFrame(positions), total_value


def calculate_from_allw_holdings(investment_amount: float, as_of_date: str):
    """Calculate positions based on actual ALLW holdings and their market values."""

    conn = get_db_connection()

    # Get ALLW holdings
    query = """
        SELECT ticker, name, weight, market_value
        FROM etf_holdings_daily
        WHERE etf = 'ALLW' AND snapshot_date = ?
        AND ticker != 'CASH'
        ORDER BY ABS(weight) DESC
    """

    df = pd.read_sql_query(query, conn, params=(as_of_date,))

    if df.empty:
        print(f"Error: No ALLW holdings found for {as_of_date}")
        conn.close()
        return None

    # Calculate total AUM from market values
    total_aum = df['market_value'].sum()

    print(f"\nALLW Estimated AUM: ${total_aum:,.2f}")
    print(f"Your Investment: ${investment_amount:,.2f}")
    print(f"Your portfolio is {investment_amount/total_aum*100:.4f}% of ALLW's size")

    # Get ETF tickers only (exclude futures)
    etf_tickers = ['SPLG', 'SPEM', 'GXC']
    df_etfs = df[df['ticker'].isin(etf_tickers)].copy()

    positions = []
    total_value = 0

    print(f"\nFetching current prices for replication...")

    for _, row in df_etfs.iterrows():
        ticker = row['ticker']
        weight = row['weight']
        target_value = investment_amount * weight

        price = get_latest_price(ticker, conn)

        if price is None:
            print(f"  Warning: No price found for {ticker}")
            continue

        shares = int(target_value / price)
        actual_value = shares * price
        total_value += actual_value

        positions.append({
            'ticker': ticker,
            'name': row['name'],
            'allw_weight': weight,
            'allw_market_value': row['market_value'],
            'target_value': target_value,
            'current_price': price,
            'shares_to_buy': shares,
            'actual_cost': actual_value
        })

    # Add GLD as proxy for gold futures
    gold_weight = df[df['name'].str.contains('GOLD', case=False, na=False)]['weight'].sum()
    if gold_weight != 0:
        ticker = 'GLD'
        target_value = investment_amount * gold_weight
        price = get_latest_price(ticker, conn)

        if price:
            shares = int(target_value / price)
            actual_value = shares * price
            total_value += actual_value

            positions.append({
                'ticker': ticker,
                'name': 'SPDR Gold Trust (proxy for gold futures)',
                'allw_weight': gold_weight,
                'allw_market_value': df[df['name'].str.contains('GOLD', case=False, na=False)]['market_value'].sum(),
                'target_value': target_value,
                'current_price': price,
                'shares_to_buy': shares,
                'actual_cost': actual_value
            })

    conn.close()

    return pd.DataFrame(positions), total_value


def print_portfolio_report(df: pd.DataFrame, total_invested: float,
                           investment_amount: float, portfolio_name: str):
    """Print detailed portfolio report."""

    print(f"\n{'='*90}")
    print(f"Portfolio: {portfolio_name}")
    print(f"Investment Amount: ${investment_amount:,.2f}")
    print(f"{'='*90}\n")

    print(f"{'Ticker':<8} {'Price':>10} {'Weight %':>10} {'Shares':>10} {'Cost':>15} {'Target':>15}")
    print("-" * 90)

    for _, row in df.iterrows():
        ticker = row['ticker']

        if 'current_price' in row:
            price = row['current_price']
            shares = row['shares_to_buy']
            cost = row['actual_cost']
            weight = row['allw_weight']
            target = row['target_value']
        else:
            price = row['price']
            shares = row['shares']
            cost = row['actual_value']
            weight = row['weight']
            target = row['target_value']

        if price is None:
            print(f"{ticker:<8} {'N/A':>10} {weight*100:>9.2f}% {'N/A':>10} {'N/A':>15} ${target:>14,.2f}")
        else:
            print(f"{ticker:<8} ${price:>9.2f} {weight*100:>9.2f}% {shares:>10,} ${cost:>14,.2f} ${target:>14,.2f}")

    print("-" * 90)
    cash = investment_amount - total_invested
    print(f"{'CASH':<8} {'':>10} {(cash/investment_amount)*100:>9.2f}% {'':>10} ${cash:>14,.2f} ${cash:>14,.2f}")
    print(f"{'TOTAL':<8} {'':>10} {'100.00%':>10} {'':>10} ${investment_amount:>14,.2f}")
    print()

    # Performance metrics
    efficiency = (total_invested / investment_amount) * 100
    print(f"Portfolio Efficiency: {efficiency:.2f}% (amount actually invested in securities)")
    print(f"Cash Drag: {100-efficiency:.2f}%")

    # Get ALLW price for comparison
    conn = get_db_connection()
    allw_price, allw_date = get_allw_nav(conn)
    conn.close()

    if allw_price:
        allw_shares = int(investment_amount / allw_price)
        allw_cost = allw_shares * allw_price
        print(f"\nFor comparison:")
        print(f"  Buy ALLW directly: {allw_shares:,} shares @ ${allw_price:.2f} = ${allw_cost:,.2f}")
        print(f"  ALLW price as of: {allw_date}")


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python calculate_portfolio_value.py <amount> <portfolio_name> [date]")
        print("  python calculate_portfolio_value.py <amount> ALLW [date]")
        print("\nExamples:")
        print("  python calculate_portfolio_value.py 100000 ALLW_SCALED 2025-10-06")
        print("  python calculate_portfolio_value.py 50000 ALLW_ETF_ONLY 2025-10-06")
        print("  python calculate_portfolio_value.py 100000 ALLW 2025-10-06  (uses actual ALLW holdings)")
        sys.exit(1)

    investment_amount = float(sys.argv[1])
    portfolio_name = sys.argv[2]
    as_of_date = sys.argv[3] if len(sys.argv) > 3 else '2025-10-06'

    if portfolio_name == 'ALLW':
        # Use actual ALLW holdings
        df, total_invested = calculate_from_allw_holdings(investment_amount, as_of_date)
        if df is not None:
            print_portfolio_report(df, total_invested, investment_amount,
                                 f"ALLW Direct Holdings ({as_of_date})")
    else:
        # Use generated replication portfolio
        df, total_invested = calculate_portfolio_positions(portfolio_name, as_of_date,
                                                          investment_amount)
        if df is not None:
            print_portfolio_report(df, total_invested, investment_amount, portfolio_name)


if __name__ == "__main__":
    main()
