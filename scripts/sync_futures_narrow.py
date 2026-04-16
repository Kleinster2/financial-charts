"""One-off: sync futures_prices_daily (wide) -> futures_prices_long (narrow)."""
import sqlite3
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'charting_app'))
from sqlite_queries import sync_wide_to_narrow

DB = str(Path(__file__).resolve().parent.parent / 'market_data.db')
conn = sqlite3.connect(DB)
df = pd.read_sql_query("SELECT * FROM futures_prices_daily", conn, index_col='Date')
print(f"Loaded wide futures: {df.shape[0]} dates x {df.shape[1]} contracts")
sync_wide_to_narrow(df, table='futures_prices_long', value_col='Close', verbose=True)

cur = conn.cursor()
cur.execute("SELECT MAX(date), COUNT(*) FROM futures_prices_long WHERE ticker='ES=F'")
print(f"After sync, futures_prices_long ES=F: {cur.fetchone()}")
conn.close()
