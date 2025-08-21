import sys
import sqlite3
import pandas as pd
import os
from constants import DB_PATH, get_db_connection

if not os.path.exists(DB_PATH):
    print(f'Database not found at {DB_PATH}')
    sys.exit(1)

if len(sys.argv) < 2:
    print('Usage: python drop_columns.py <COL1> <COL2> ...')
    sys.exit(1)

cols_to_drop = [c.upper() for c in sys.argv[1:]]

print(f"Using database: {DB_PATH}")
conn = get_db_connection(row_factory=None)
try:
    df = pd.read_sql('SELECT * FROM stock_prices_daily', conn, parse_dates=['Date'])
    existing = [c for c in cols_to_drop if c in df.columns]
    if not existing:
        print('None of the specified columns exist in the table. No action taken.')
        sys.exit(0)

    print('Dropping columns:', ', '.join(existing))
    df = df.drop(columns=existing)

    # Replace the table atomically
    tmp_table = 'stock_prices_daily_tmp'
    df.to_sql(tmp_table, conn, index=False, if_exists='replace')
    conn.execute('DROP TABLE stock_prices_daily')
    conn.execute(f'ALTER TABLE {tmp_table} RENAME TO stock_prices_daily')
    conn.commit()
    print('Columns dropped and table updated successfully.')
finally:
    conn.close()
