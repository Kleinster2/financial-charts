import warnings
warnings.filterwarnings('ignore')
import yfinance as yf
import sqlite3
import pandas as pd

data = yf.download('FUTU', period='max', progress=False)
print(f"Downloaded {len(data)} rows")

if isinstance(data.columns, pd.MultiIndex):
    data = data.droplevel('Ticker', axis=1)

close = data[['Close']].rename(columns={'Close': 'FUTU'})
close.index = pd.to_datetime(close.index).strftime('%Y-%m-%d %H:%M:%S')
close.index.name = 'Date'

conn = sqlite3.connect('market_data.db')
try:
    conn.execute('ALTER TABLE stock_prices_daily ADD COLUMN FUTU REAL')
    print("Added FUTU column")
except Exception as e:
    print(f"Column exists or error: {e}")

updated = 0
inserted = 0
for date, row in close.iterrows():
    conn.execute('UPDATE stock_prices_daily SET FUTU=? WHERE Date=?', (row['FUTU'], date))
    if conn.execute('SELECT changes()').fetchone()[0] == 0:
        conn.execute('INSERT INTO stock_prices_daily (Date, FUTU) VALUES (?, ?)', (date, row['FUTU']))
        inserted += 1
    else:
        updated += 1

conn.commit()
print(f"Updated: {updated}, Inserted: {inserted}")

conn.execute('INSERT OR REPLACE INTO ticker_metadata (ticker, name, asset_type) VALUES (?, ?, ?)',
             ('FUTU', 'Futu Holdings', 'stock'))
conn.commit()
conn.close()
print("Done!")
