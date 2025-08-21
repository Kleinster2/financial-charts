import sqlite3
import pandas as pd
from constants import DB_PATH, get_db_connection

print(f"Using database: {DB_PATH}")

# Connect to the database
conn = get_db_connection()

# --- Verify futures_prices_daily table ---
table_to_inspect = 'futures_prices_daily'
print(f"--- Verifying {table_to_inspect} table ---")

try:
    # Note: Column names with special characters like '=' need to be quoted.
    query = 'SELECT "Date", "ES=F", "CL=F", "GC=F" FROM futures_prices_daily ORDER BY "Date" DESC LIMIT 5'
    df_futures = pd.read_sql_query(query, conn)

    print("\nRecent data for ES=F (S&P 500), CL=F (Crude Oil), and GC=F (Gold):")
    print(df_futures)

    # Get total number of rows and columns
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_to_inspect}")
    num_rows = cursor.fetchone()[0]
    cursor.execute(f"PRAGMA table_info({table_to_inspect})")
    num_cols = len(cursor.fetchall())

    print(f"\nDatabase contains {num_rows} trading days of data for {num_cols - 1} futures contracts.")

except Exception as e:
    print(f"\nCould not verify {table_to_inspect}: {e}")

finally:
    conn.close()
    print("\nDatabase connection closed.")

