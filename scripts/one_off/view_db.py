import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
import sqlite3
import pandas as pd

from constants import DB_PATH, get_db_connection

print(f"Connecting to {DB_PATH}...")
with get_db_connection(row_factory=None) as conn:
    # Get a list of tables
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    
    if not tables:
        print("No tables found in the database.")
    else:
        print(f"Tables in '{DB_PATH}': {tables}\n")

        # Print the head of each table
        for table_name in tables:
            print(f"--- First 5 rows of '{table_name}' ---")
            try:
                df = pd.read_sql(f'SELECT * FROM \"{table_name}\" LIMIT 5', conn)
                print(df)
            except Exception as e:
                print(f"Could not read table '{table_name}': {e}")
            print("\n")

print("Script finished.")
