import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))
import sqlite3
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from constants import DB_PATH, get_db_connection

# --- CONFIG ---
N_CLUSTERS = 10
N_PROXY_STOCKS = 3
CLUSTER_NAMES = {
    0: "Tech/Growth", 1: "Defensive/Utilities", 2: "Financials",
    3: "Healthcare", 4: "Industrials/Manufacturing", 5: "Consumer Discretionary",
    6: "Energy", 7: "Real Estate/REITs", 8: "Materials/Commodities",
    9: "Communication Services"
}

# --- FUNCTIONS ---
def get_sp500_info():
    """Fetches S&P 500 metadata from the database and filters by tickers present in price data."""
    with get_db_connection() as conn:
        sp500_info = pd.read_sql("SELECT ticker, name, sector FROM stock_metadata", conn)
        price_tickers_df = pd.read_sql("PRAGMA table_info(stock_prices_daily);", conn)
        price_tickers = set(price_tickers_df['name']) - {'Date'}
        sp500_info = sp500_info[sp500_info['ticker'].isin(price_tickers)]
    return sp500_info.set_index('ticker')

# --- SCRIPT ---
# 1. Load All Data from Database
print(f"Loading price data from database... Using {DB_PATH}")
conn = get_db_connection()
prices = pd.read_sql("SELECT * FROM stock_prices_daily", conn, index_col='Date', parse_dates=['Date'])
conn.close()

# 2. Separate Stocks for Clustering from Benchmarks
sp500_info = get_sp500_info()
stock_tickers = sp500_info.index.tolist()
# Ensure we only use tickers that are actually in the prices dataframe
stock_tickers = [t for t in stock_tickers if t in prices.columns]
stock_prices = prices[stock_tickers]

# 3. Data Preparation for Clustering
print("Preparing data for clustering...")
stock_prices = stock_prices.dropna(axis=1, thresh=int(len(stock_prices) * 0.95))
# Recalculate stock_tickers after dropping columns
stock_tickers = stock_prices.columns.tolist()
returns = np.log(stock_prices / stock_prices.shift(1)).dropna()
scaler = StandardScaler()
scaled_returns = scaler.fit_transform(returns.T)

# 4. K-Means Clustering
print(f"Running K-Means clustering with {N_CLUSTERS} clusters...")
kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=10)
kmeans.fit(scaled_returns)
clusters = pd.Series(kmeans.labels_, index=returns.columns, name='cluster_id')

# 5. Identify Representative Stocks and Build Proxies
print(f"Identifying {N_PROXY_STOCKS} proxy stocks for each cluster...")
cluster_proxies = []
cluster_members_info = {}

for cluster_id in range(N_CLUSTERS):
    members = clusters[clusters == cluster_id].index
    centroid = kmeans.cluster_centers_[cluster_id]
    member_data = scaled_returns[clusters == cluster_id]
    distances = np.linalg.norm(member_data - centroid, axis=1)
    
    closest_stocks = members[np.argsort(distances)[:N_PROXY_STOCKS]]
    cluster_proxies.append(closest_stocks)
    
    all_members_sorted = members[np.argsort(distances)]
    cluster_members_info[cluster_id] = {
        'proxies': closest_stocks.tolist(),
        'all_members': all_members_sorted.tolist()
    }

# 6. Calculate Performance of Proxy Portfolios
proxy_portfolios = pd.DataFrame(index=returns.index)
for i, proxy_group in enumerate(cluster_proxies):
    portfolio_returns = returns[proxy_group].mean(axis=1)
    proxy_portfolios[f'Cluster_{i}'] = portfolio_returns

cumulative_performance = proxy_portfolios.cumsum().apply(np.exp)
normalized_performance = cumulative_performance / cumulative_performance.iloc[0]

# --- Generate Cluster Members File ---
print("Generating cluster_members.txt...")
with open("cluster_members.txt", "w") as f:
    f.write("S&P 500 Stock Clusters and Their Members\n=========================================\n\n")
    for cluster_id, info in cluster_members_info.items():
        cluster_name = CLUSTER_NAMES.get(cluster_id, f"Cluster {cluster_id}")
        f.write(f"--- {cluster_name} (Cluster {cluster_id}) ---\n")
        f.write(f"Proxy Stocks: {', '.join(info['proxies'])}\n\n")
        for i, ticker in enumerate(info['all_members']):
            name = sp500_info.loc[ticker, 'name'] if ticker in sp500_info.index else "N/A"
            proxy_marker = " (Proxy)" if ticker in info['proxies'] else ""
            f.write(f"{i+1}. {ticker} - {name}{proxy_marker}\n")
        f.write("\n")

# --- Plotting ---
print("Generating plot...")
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(15, 10))

# Plot each cluster proxy portfolio
for col in normalized_performance.columns:
    cluster_id = int(col.split('_')[1])
    tickers_in_legend = cluster_members_info[cluster_id]['proxies']
    label = f"{CLUSTER_NAMES.get(cluster_id, '')}: {', '.join(tickers_in_legend)}"
    plt.plot(normalized_performance.index, normalized_performance[col], label=label)

# Prepare and plot benchmarks (SPY, RSP)
benchmark_tickers = ['SPY', 'RSP', 'VTI', 'QQQ', 'DIA', 'IWM', 'AGG', 'GLD']
all_returns = np.log(prices[benchmark_tickers] / prices[benchmark_tickers].shift(1))
benchmark_returns = all_returns.loc[normalized_performance.index[0]:] # Align dates
benchmark_cumulative_returns = benchmark_returns.cumsum().apply(np.exp)
normalized_benchmarks = benchmark_cumulative_returns / benchmark_cumulative_returns.iloc[0]

# Plot each benchmark
for ticker in benchmark_tickers:
    plt.plot(normalized_benchmarks.index, normalized_benchmarks[ticker], label=f'{ticker} (Benchmark)', linestyle='--')

plt.title(f'Performance of {N_CLUSTERS} Cluster Proxy Portfolios vs. Benchmarks')
plt.ylabel('Cumulative Growth of $1')
plt.xlabel('Date')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Clusters & Proxies")
plt.grid(True)
plt.tight_layout(rect=[0, 0, 0.8, 1])
plt.savefig("cluster_portfolio_performance.png", dpi=300)
plt.show()

print("\nScript finished. Check for 'cluster_portfolio_performance.png' and 'cluster_members.txt'.")
