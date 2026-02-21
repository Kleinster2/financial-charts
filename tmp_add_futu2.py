import warnings
warnings.filterwarnings('ignore')
import yfinance as yf
import sqlite3
import pandas as pd
import sys

data = yf.download('FUTU', period='max', progress=False)
print(f"Downloaded {len(data)} rows", flush=True)

if isinstance(data.columns, pd.MultiIndex):
    data = data.droplevel('Ticker', axis=1)

close = data['Close'].dropna()
print(f"Valid close prices: {len(close)}", flush=True)

conn = sqlite3.connect('market_data.db')

# Check column exists
cols = [r[1] for r in conn.execute('PRAGMA table_info(stock_prices_daily)')]
if 'FUTU' not in cols:
    conn.execute('ALTER TABLE stock_prices_daily ADD COLUMN FUTU REAL')
    print("Added FUTU column", flush=True)

# Get existing dates
existing = set(r[0] for r in conn.execute('SELECT Date FROM stock_prices_daily'))
print(f"Existing dates in DB: {len(existing)}", flush=True)

count = 0
for date, price in close.items():
    dt = pd.Timestamp(date).strftime('%Y-%m-%d %H:%M:%S')
    if dt in existing:
        conn.execute('UPDATE stock_prices_daily SET FUTU=? WHERE Date=?', (float(price), dt))
    else:
        conn.execute('INSERT INTO stock_prices_daily (Date, FUTU) VALUES (?, ?)', (float(price), dt))
    count += 1
    if count % 200 == 0:
        conn.commit()
        print(f"  processed {count}...", flush=True)

conn.commit()
conn.execute('INSERT OR REPLACE INTO ticker_metadata (ticker, name, asset_type) VALUES (?, ?, ?)',
             ('FUTU', 'Futu Holdings', 'stock'))
conn.commit()
conn.close()
print(f"Done! Total: {count} rows", flush=True)
