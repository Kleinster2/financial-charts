import sqlite3
import pandas as pd
from constants import DB_PATH, get_db_connection

print(f"Using database: {DB_PATH}")

# Connect to database
conn = get_db_connection()

# Check tables
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in database:", [t[0] for t in tables])

# Check stock_prices_daily columns
try:
    cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
    columns = cursor.fetchall()
    print(f"\nColumns in stock_prices_daily: {len(columns)}")
    print("First 10 columns:", [col[1] for col in columns[:10]])
    
    # Check if RSP is there
    col_names = [col[1] for col in columns]
    if 'RSP' in col_names:
        print("✓ RSP found in columns!")
    else:
        print("✗ RSP NOT found in columns!")
        
except Exception as e:
    print(f"Error checking stock_prices_daily: {e}")

# Check futures_prices_daily columns
try:
    cursor = conn.execute("PRAGMA table_info(futures_prices_daily)")
    columns = cursor.fetchall()
    print(f"\nColumns in futures_prices_daily: {len(columns)}")
    print("First 10 columns:", [col[1] for col in columns[:10]])
except Exception as e:
    print(f"Error checking futures_prices_daily: {e}")

# Check a sample of data
try:
    df = pd.read_sql("SELECT * FROM stock_prices_daily LIMIT 3", conn)
    print(f"\nSample data shape: {df.shape}")
    print(f"First 5 columns: {list(df.columns[:5])}")
except Exception as e:
    print(f"Error reading data: {e}")

conn.close()
