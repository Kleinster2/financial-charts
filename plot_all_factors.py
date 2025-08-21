import os
import sqlite3
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from constants import DB_PATH, get_db_connection

# --- CONFIG ---
START_DATE = "2023-12-29"
END_DATE = "2025-07-01"
ETF_TICKERS = ["SPY", "RSP"]

# 1. Download latest ETF prices
print("Downloading SPY and RSP prices …")
etf_prices = yf.download(
    ETF_TICKERS,
    start=START_DATE,
    end=END_DATE,
    progress=False,
    threads=True,
    auto_adjust=True,
)["Close"]

# 2. Load S&P 500 price table from SQLite
print(f"Loading database prices … Using {DB_PATH}")
df_prices = pd.read_sql(
    "SELECT * FROM stock_prices_daily",
    get_db_connection(),
    parse_dates=["Date"],
).set_index("Date")

# 3. Compute daily log-returns
print("Processing returns data…")
stock_ret = np.log(df_prices).diff()
stock_ret = stock_ret.ffill().bfill()
row_thresh = int(0.95 * stock_ret.shape[1])
stock_ret = stock_ret.dropna(axis=0, thresh=row_thresh)
col_thresh = int(0.95 * len(stock_ret))
stock_ret = stock_ret.dropna(axis=1, thresh=col_thresh)
etf_ret = np.log(etf_prices).diff().dropna()

# 4. Standardize stock returns and fit PCA to get PC-2 and PC-3 loadings
print("Calculating PC loadings …")
X_std = StandardScaler().fit_transform(stock_ret)
pca = PCA(n_components=3).fit(X_std)

loadings_pc2 = pd.Series(pca.components_[1], index=stock_ret.columns)
loadings_pc3 = pd.Series(pca.components_[2], index=stock_ret.columns)

# 5. Build PC2 and PC3 factor indices
# PC2
w2 = loadings_pc2 / loadings_pc2.abs().sum()
pc2_log_ret = stock_ret.dot(w2)
pc2_index = np.exp(pc2_log_ret.cumsum())
pc2_index = pc2_index / pc2_index.iloc[0]
pc2_index.name = "PC2_Factor"

# PC3
w3 = loadings_pc3 / loadings_pc3.abs().sum()
pc3_log_ret = stock_ret.dot(w3)
pc3_index = np.exp(pc3_log_ret.cumsum())
pc3_index = pc3_index / pc3_index.iloc[0]
pc3_index.name = "PC3_Factor"

# 6. Turn ETF prices into normalized index levels (start=1)
etf_index = (etf_prices / etf_prices.iloc[0]).rename(columns={t: f"{t}_Index" for t in ETF_TICKERS})

# 7. Align all series on common dates
combined = pd.concat([pc2_index, pc3_index, etf_index], axis=1, join="inner")

# 8. Plot
plt.figure(figsize=(12, 7))
for col in combined.columns:
    plt.plot(combined.index, combined[col], label=col)
plt.title("PC Factors vs. SPY and RSP (normalized to 1 on first date)")
plt.ylabel("Cumulative Growth of $1 (log scale)")
plt.yscale("log")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# 9. Print correlation matrix of daily returns
print("\nCorrelation matrix of daily returns:")
print(combined.pct_change().corr())
