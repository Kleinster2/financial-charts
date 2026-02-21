import warnings
warnings.filterwarnings('ignore')
import yfinance as yf
import sqlite3
import pandas as pd

data = yf.download('FUTU', period='max', progress=False)
if isinstance(data.columns, pd.MultiIndex):
    data = data.droplevel('Ticker', axis=1)

close = data['Close'].dropna()
conn = sqlite3.connect('market_data.db')

# Batch update using executemany
rows = [(float(price), pd.Timestamp(date).strftime('%Y-%m-%d %H:%M:%S')) for date, price in close.items()]
conn.executemany('UPDATE stock_prices_daily SET FUTU=? WHERE Date=?', rows)

# Insert any dates not already in DB
existing = set(r[0] for r in conn.execute('SELECT Date FROM stock_prices_daily WHERE FUTU IS NOT NULL'))
inserts = [(dt, val) for val, dt in rows if dt not in existing]
if inserts:
    conn.executemany('INSERT INTO stock_prices_daily (Date, FUTU) VALUES (?, ?)', inserts)

conn.execute('INSERT OR REPLACE INTO ticker_metadata (ticker, name, asset_type) VALUES (?, ?, ?)',
             ('FUTU', 'Futu Holdings', 'stock'))
conn.commit()
conn.close()
print(f"Done: {len(rows)} updated, {len(inserts)} inserted", flush=True)
