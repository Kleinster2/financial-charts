import sqlite3
import pandas as pd

DB_PATH = "sp500_data.db"

print(f"Connecting to {DB_PATH}...")
with sqlite3.connect(DB_PATH) as conn:
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
