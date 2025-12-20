#!/usr/bin/env python3
"""
Create a minimal sample database for demo mode.

Generates ~30 days of synthetic price data for 10 representative tickers,
allowing the UI to run without access to the full market_data.db.

Usage:
    python scripts/create_sample_db.py

Output:
    sample_data.db in project root
"""

import sqlite3
import os
import random
from datetime import datetime, timedelta

# Output path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
SAMPLE_DB_PATH = os.path.join(PROJECT_ROOT, 'sample_data.db')

# Sample tickers - representative mix
SAMPLE_TICKERS = [
    ('SPY', 'SPDR S&P 500 ETF', 'ETF'),
    ('AAPL', 'Apple Inc.', 'Technology'),
    ('GOOGL', 'Alphabet Inc.', 'Technology'),
    ('MSFT', 'Microsoft Corporation', 'Technology'),
    ('AMZN', 'Amazon.com Inc.', 'Consumer Cyclical'),
    ('TSLA', 'Tesla Inc.', 'Consumer Cyclical'),
    ('^GSPC', 'S&P 500 Index', 'Index'),
    ('^VIX', 'CBOE Volatility Index', 'Index'),
    ('BTC-USD', 'Bitcoin USD', 'Cryptocurrency'),
    ('GLD', 'SPDR Gold Shares', 'ETF'),
]

# Base prices for each ticker
BASE_PRICES = {
    'SPY': 580.0,
    'AAPL': 195.0,
    'GOOGL': 175.0,
    'MSFT': 430.0,
    'AMZN': 225.0,
    'TSLA': 350.0,
    '^GSPC': 5900.0,
    '^VIX': 15.0,
    'BTC-USD': 100000.0,
    'GLD': 230.0,
}

# Volatility for each ticker (daily % std dev)
VOLATILITIES = {
    'SPY': 0.01,
    'AAPL': 0.015,
    'GOOGL': 0.018,
    'MSFT': 0.014,
    'AMZN': 0.02,
    'TSLA': 0.035,
    '^GSPC': 0.01,
    '^VIX': 0.05,
    'BTC-USD': 0.04,
    'GLD': 0.008,
}


def generate_prices(ticker: str, days: int = 30) -> list:
    """Generate synthetic price data with random walk."""
    base = BASE_PRICES.get(ticker, 100.0)
    vol = VOLATILITIES.get(ticker, 0.02)

    prices = []
    price = base

    # Start from 30 days ago
    start_date = datetime.now() - timedelta(days=days)

    for i in range(days):
        date = start_date + timedelta(days=i)
        # Skip weekends for non-crypto
        if ticker != 'BTC-USD' and date.weekday() >= 5:
            continue

        # Random daily return
        daily_return = random.gauss(0.0003, vol)  # Slight upward drift
        price = price * (1 + daily_return)

        # Generate OHLC-like values
        high = price * (1 + abs(random.gauss(0, vol * 0.3)))
        low = price * (1 - abs(random.gauss(0, vol * 0.3)))

        prices.append({
            'date': date.strftime('%Y-%m-%d'),
            'close': round(price, 2),
            'high': round(high, 2),
            'low': round(low, 2),
            'volume': random.randint(1000000, 50000000),
        })

    return prices


def create_sample_db():
    """Create the sample database with all required tables."""
    # Remove existing sample DB
    if os.path.exists(SAMPLE_DB_PATH):
        os.remove(SAMPLE_DB_PATH)
        print(f"Removed existing {SAMPLE_DB_PATH}")

    conn = sqlite3.connect(SAMPLE_DB_PATH)
    cursor = conn.cursor()

    # Get all dates we'll use
    all_tickers = [t[0] for t in SAMPLE_TICKERS]
    all_prices = {ticker: generate_prices(ticker, 45) for ticker in all_tickers}

    # Get union of all dates
    all_dates = sorted(set(
        p['date']
        for prices in all_prices.values()
        for p in prices
    ))

    # 1. Create stock_prices_daily (wide format like production)
    ticker_cols = ', '.join(f'"{t}" REAL' for t in all_tickers)
    cursor.execute(f'''
        CREATE TABLE stock_prices_daily (
            "Date" TEXT,
            {ticker_cols}
        )
    ''')

    # Insert price data
    for date in all_dates:
        values = [date]
        for ticker in all_tickers:
            price_data = next((p for p in all_prices[ticker] if p['date'] == date), None)
            values.append(price_data['close'] if price_data else None)

        placeholders = ', '.join(['?' for _ in values])
        cursor.execute(f'INSERT INTO stock_prices_daily VALUES ({placeholders})', values)

    # 2. Create stock_volumes_daily (wide format)
    cursor.execute(f'''
        CREATE TABLE stock_volumes_daily (
            "Date" TIMESTAMP,
            {ticker_cols}
        )
    ''')

    # Insert volume data
    for date in all_dates:
        values = [date]
        for ticker in all_tickers:
            price_data = next((p for p in all_prices[ticker] if p['date'] == date), None)
            values.append(price_data['volume'] if price_data else None)

        placeholders = ', '.join(['?' for _ in values])
        cursor.execute(f'INSERT INTO stock_volumes_daily VALUES ({placeholders})', values)

    # 3. Create stock_metadata
    cursor.execute('''
        CREATE TABLE stock_metadata (
            ticker TEXT,
            name TEXT,
            sector TEXT
        )
    ''')
    for ticker, name, sector in SAMPLE_TICKERS:
        cursor.execute('INSERT INTO stock_metadata VALUES (?, ?, ?)', (ticker, name, sector))

    # 4. Create ticker_metadata
    cursor.execute('''
        CREATE TABLE ticker_metadata (
            ticker TEXT PRIMARY KEY,
            name TEXT,
            table_name TEXT,
            data_type TEXT,
            first_date TEXT,
            last_date TEXT,
            data_points INTEGER
        )
    ''')
    for ticker, name, sector in SAMPLE_TICKERS:
        prices = all_prices[ticker]
        if prices:
            first_date = prices[0]['date']
            last_date = prices[-1]['date']
            data_points = len(prices)
        else:
            first_date = last_date = None
            data_points = 0

        table_name = 'stock_prices_daily'
        data_type = 'stock'
        if ticker.startswith('^'):
            data_type = 'index'
        elif ticker.endswith('-USD'):
            data_type = 'crypto'

        cursor.execute('''
            INSERT INTO ticker_metadata VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (ticker, name, table_name, data_type, first_date, last_date, data_points))

    # 5. Create empty tables that the app might query
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS futures_prices_daily (
            "Date" TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bond_prices_daily (
            "Date" TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cboe_indices_daily (
            "Date" TEXT
        )
    ''')

    conn.commit()
    conn.close()

    # Report file size
    size_kb = os.path.getsize(SAMPLE_DB_PATH) / 1024
    print(f"Created {SAMPLE_DB_PATH}")
    print(f"  Size: {size_kb:.1f} KB")
    print(f"  Tickers: {len(SAMPLE_TICKERS)}")
    print(f"  Dates: {len(all_dates)}")
    print(f"  Tickers: {', '.join(all_tickers)}")


if __name__ == '__main__':
    create_sample_db()
