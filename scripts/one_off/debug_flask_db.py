import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
import sqlite3
import os
from constants import DB_PATH, get_db_connection

# Check resolved database path from centralized constants
print(f"Resolved DB_PATH: {DB_PATH}")
print(f"Absolute path: {os.path.abspath(DB_PATH)}")
print(f"Exists: {os.path.exists(DB_PATH)}")

# Try to connect directly
try:
    conn = get_db_connection()  # default row_factory=sqlite3.Row
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"\nTables found: {len(tables)}")
    for t in tables:
        print(f"  - {t['name'] if isinstance(t, sqlite3.Row) else t[0]}")
    
    # Check stock_prices_daily
    cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
    cols = cursor.fetchall()
    print(f"\nColumns in stock_prices_daily: {len(cols)}")
    
    conn.close()
except Exception as e:
    print(f"Error: {e}")

print("\n--- Testing centralized get_db_connection() ---")
try:
    conn = get_db_connection()
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"Tables via centralized helper: {len(tables)}")
    conn.close()
except Exception as e:
    print(f"Error with centralized helper: {e}")
