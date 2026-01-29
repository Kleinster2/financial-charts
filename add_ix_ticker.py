#!/usr/bin/env python3
"""Add ORIX Corporation (IX) ticker data to market_data.db"""

import sqlite3
import yfinance as yf
from datetime import datetime

DB_PATH = 'financial-charts/market_data.db'
TICKER = 'IX'
COMPANY_NAME = 'ORIX Corp'

print("=" * 60)
print("Adding ORIX Corporation (IX) to market_data.db")
print("=" * 60)

try:
    # Step 1: Fetch historical data from yfinance
    print("\n[1/6] Fetching historical data for ticker 'IX' from yfinance...")
    ticker_obj = yf.Ticker(TICKER)
    hist_data = ticker_obj.history(period='max')
    
    if hist_data.empty:
        print("ERROR: No data returned from yfinance")
        exit(1)
    
    num_rows = len(hist_data)
    print(f"  ✓ Fetched {num_rows} rows of historical data")
    print(f"  ✓ Date range: {hist_data.index[0].strftime('%Y-%m-%d')} to {hist_data.index[-1].strftime('%Y-%m-%d')}")
    
    # Step 2: Connect to database
    print(f"\n[2/6] Connecting to database: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    print("  ✓ Connected successfully")
    
    # Step 3: Check if column exists in stock_prices_daily
    print(f"\n[3/6] Checking if '{TICKER}' column exists in stock_prices_daily...")
    cursor.execute("PRAGMA table_info(stock_prices_daily)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if TICKER not in columns:
        cursor.execute(f'ALTER TABLE stock_prices_daily ADD COLUMN "{TICKER}" REAL')
        conn.commit()
        print(f"  ✓ Column '{TICKER}' ADDED to stock_prices_daily")
    else:
        print(f"  ✓ Column '{TICKER}' already exists (skipped)")
    
    # Also check stock_volumes_daily
    cursor.execute("PRAGMA table_info(stock_volumes_daily)")
    vol_columns = [col[1] for col in cursor.fetchall()]
    
    if TICKER not in vol_columns:
        cursor.execute(f'ALTER TABLE stock_volumes_daily ADD COLUMN "{TICKER}" INTEGER')
        conn.commit()
        print(f"  ✓ Column '{TICKER}' ADDED to stock_volumes_daily")
    else:
        print(f"  ✓ Column '{TICKER}' already exists in volumes (skipped)")
    
    # Step 4: Insert price data
    print(f"\n[4/6] Inserting price data into stock_prices_daily...")
    price_updates = 0
    for idx, row in hist_data.iterrows():
        date_str = idx.strftime('%Y-%m-%d 00:00:00')
        price = float(row['Close']) if not row.isna()['Close'] else None
        
        if price is not None:
            # Check if date exists
            cursor.execute('SELECT 1 FROM stock_prices_daily WHERE date = ?', (date_str,))
            if cursor.fetchone():
                cursor.execute(f'UPDATE stock_prices_daily SET "{TICKER}" = ? WHERE date = ?', (price, date_str))
            else:
                cursor.execute(f'INSERT INTO stock_prices_daily (date, "{TICKER}") VALUES (?, ?)', (date_str, price))
            price_updates += 1
    
    conn.commit()
    print(f"  ✓ Inserted/updated {price_updates} price rows")
    
    # Step 5: Insert volume data
    print(f"\n[5/6] Inserting volume data into stock_volumes_daily...")
    volume_updates = 0
    for idx, row in hist_data.iterrows():
        date_str = idx.strftime('%Y-%m-%d 00:00:00')
        volume = int(row['Volume']) if not row.isna()['Volume'] else None
        
        if volume is not None:
            # Check if date exists
            cursor.execute('SELECT 1 FROM stock_volumes_daily WHERE date = ?', (date_str,))
            if cursor.fetchone():
                cursor.execute(f'UPDATE stock_volumes_daily SET "{TICKER}" = ? WHERE date = ?', (volume, date_str))
            else:
                cursor.execute(f'INSERT INTO stock_volumes_daily (date, "{TICKER}") VALUES (?, ?)', (date_str, volume))
            volume_updates += 1
    
    conn.commit()
    print(f"  ✓ Inserted/updated {volume_updates} volume rows")
    
    # Step 6: Add/update metadata
    print(f"\n[6/6] Adding metadata to ticker_metadata...")
    cursor.execute('SELECT 1 FROM ticker_metadata WHERE ticker = ?', (TICKER,))
    if cursor.fetchone():
        cursor.execute(
            'UPDATE ticker_metadata SET name = ?, type = ?, source = ?, last_updated = ? WHERE ticker = ?',
            (COMPANY_NAME, 'stock', 'yfinance', datetime.now().isoformat(), TICKER)
        )
        print(f"  ✓ Updated existing metadata for '{TICKER}'")
    else:
        cursor.execute(
            'INSERT INTO ticker_metadata (ticker, name, type, source, last_updated) VALUES (?, ?, ?, ?, ?)',
            (TICKER, COMPANY_NAME, 'stock', 'yfinance', datetime.now().isoformat())
        )
        print(f"  ✓ Added new metadata for '{TICKER}'")
    
    conn.commit()
    
    # Verification
    print(f"\n[Verification] Checking data counts...")
    cursor.execute(f'SELECT COUNT(*) FROM stock_prices_daily WHERE "{TICKER}" IS NOT NULL')
    price_count = cursor.fetchone()[0]
    cursor.execute(f'SELECT COUNT(*) FROM stock_volumes_daily WHERE "{TICKER}" IS NOT NULL')
    volume_count = cursor.fetchone()[0]
    
    print(f"  ✓ Price rows with IX data: {price_count}")
    print(f"  ✓ Volume rows with IX data: {volume_count}")
    
    # Sample data
    print(f"\n[Sample Data] Last 5 price entries:")
    cursor.execute(f'SELECT date, "{TICKER}" FROM stock_prices_daily WHERE "{TICKER}" IS NOT NULL ORDER BY date DESC LIMIT 5')
    for row in cursor.fetchall():
        print(f"    {row[0]}: ${row[1]:.2f}")
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("SUCCESS: ORIX Corporation (IX) data added to database!")
    print("=" * 60)
    
except Exception as e:
    print(f"\nERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
