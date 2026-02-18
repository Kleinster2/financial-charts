"""Generate 40-day rolling correlation chart between two tickers."""
import sqlite3, sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

db = sqlite3.connect(r'C:\Users\klein\financial-charts\market_data.db')
t1, t2 = sys.argv[1], sys.argv[2]
out = sys.argv[3] if len(sys.argv) > 3 else 'correlation.png'
window = int(sys.argv[4]) if len(sys.argv) > 4 else 40

df = pd.read_sql(f"SELECT Date, [{t1}], [{t2}] FROM stock_prices_daily WHERE [{t1}] IS NOT NULL AND [{t2}] IS NOT NULL ORDER BY Date", db)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# Daily returns
r1 = df[t1].pct_change()
r2 = df[t2].pct_change()

corr = r1.rolling(window).corr(r2)

# Plot last 2 years
corr = corr.loc['2024-01-01':]

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(corr.index, corr.values, color='#2563eb', linewidth=1.5)
ax.axhline(y=0.21, color='#dc2626', linewidth=1, linestyle='--', alpha=0.7, label='Current: 0.21')
ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='-', alpha=0.3)
ax.set_ylabel(f'{window}-Day Correlation')
ax.set_title(f'{t1} vs {t2} — {window}-Day Rolling Correlation')
ax.legend(loc='upper right')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
fig.autofmt_xdate()
ax.set_ylim(-0.2, 1.1)
ax.grid(True, alpha=0.2)
fig.tight_layout()
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f"Saved to {out}")
