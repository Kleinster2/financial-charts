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
conn.execute('PRAGMA journal_mode=WAL')
conn.execute('PRAGMA synchronous=OFF')

# Create temp table
conn.execute('CREATE TEMP TABLE futu_prices (Date TEXT PRIMARY KEY, price REAL)')
rows = [(pd.Timestamp(d).strftime('%Y-%m-%d %H:%M:%S'), float(p)) for d, p in close.items()]
conn.executemany('INSERT INTO futu_prices VALUES (?,?)', rows)

# Single UPDATE from temp table
conn.execute('''UPDATE stock_prices_daily SET FUTU = (
    SELECT price FROM futu_prices WHERE futu_prices.Date = stock_prices_daily.Date
) WHERE Date IN (SELECT Date FROM futu_prices)''')

conn.execute('INSERT OR REPLACE INTO ticker_metadata (ticker, name, asset_type) VALUES (?,?,?)',
             ('FUTU', 'Futu Holdings', 'stock'))
conn.commit()
conn.close()
print(f"Done: {len(rows)} prices loaded", flush=True)
