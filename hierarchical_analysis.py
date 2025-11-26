"""
hierarchical_analysis.py - Hierarchical Clustering with Dendrograms
Uses Ward's method to cluster stocks by correlation distance
"""

import sqlite3
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
from constants import DB_PATH, get_db_connection

print(f"Using database: {DB_PATH}")

# --- CONFIG ---
MIN_DATA_POINTS = 200  # Minimum data points required
LOOKBACK_DAYS = 1260   # Use ~5 years of data for correlation
MAX_TICKERS_FULL = 100  # Max tickers for full dendrogram (readable)
N_CLUSTERS = 15        # Number of clusters to extract

# 1. Load and process stock returns data
print("Loading price data...")
df_prices = pd.read_sql(
    "SELECT * FROM stock_prices_daily ORDER BY Date DESC",
    get_db_connection(row_factory=None),
    parse_dates=["Date"],
).set_index("Date")

# Use most recent data
df_prices = df_prices.head(LOOKBACK_DAYS)
df_prices = df_prices.sort_index()

# Filter columns with sufficient data first
print("Filtering columns with sufficient data...")
valid_cols = df_prices.columns[df_prices.notna().sum() >= MIN_DATA_POINTS]
df_prices = df_prices[valid_cols]

# Convert to numeric and handle any remaining issues
df_prices = df_prices.apply(pd.to_numeric, errors='coerce')

# Calculate log returns (only on positive values)
print("Calculating returns...")
df_prices = df_prices.replace(0, np.nan)  # Replace 0s to avoid log(0)
returns = np.log(df_prices).diff()

# Drop columns with too many NaNs first, then rows
returns = returns.dropna(axis=1, thresh=int(0.3 * len(returns)))
returns = returns.dropna(axis=0, thresh=int(0.5 * len(returns.columns)))
returns = returns.fillna(0)

print(f"Analyzing {len(returns.columns)} tickers with {len(returns)} days of data")

# 2. Calculate correlation matrix
print("Calculating correlation matrix...")
corr_matrix = returns.corr()

# Handle any NaN correlations (can happen with constant columns)
corr_matrix = corr_matrix.fillna(0)

# Convert correlation to distance (1 - corr)
# Ward's method needs distances, not similarities
dist_matrix = 1 - corr_matrix

# Ensure symmetry and valid diagonal
dist_matrix = (dist_matrix + dist_matrix.T) / 2  # Force symmetry
np.fill_diagonal(dist_matrix.values, 0)

# Clip to valid range [0, 2] for correlation distance
dist_matrix = dist_matrix.clip(lower=0, upper=2)

# Convert to condensed form for linkage
dist_condensed = squareform(dist_matrix.values, checks=False)

# 3. Perform hierarchical clustering using Ward's method
print("Performing hierarchical clustering (Ward's method)...")
Z = linkage(dist_condensed, method='ward')

# 4. Extract cluster assignments
clusters = fcluster(Z, t=N_CLUSTERS, criterion='maxclust')
cluster_df = pd.DataFrame({
    'ticker': corr_matrix.columns,
    'cluster': clusters
})

# 5. Save cluster assignments
print(f"\nSaving {N_CLUSTERS} cluster assignments...")
with open('hierarchical_clusters.txt', 'w') as f:
    f.write(f"Hierarchical Clustering Results (Ward's Method)\n")
    f.write(f"=" * 50 + "\n")
    f.write(f"Tickers analyzed: {len(returns.columns)}\n")
    f.write(f"Data period: {returns.index.min().date()} to {returns.index.max().date()}\n")
    f.write(f"Number of clusters: {N_CLUSTERS}\n\n")

    for i in range(1, N_CLUSTERS + 1):
        members = cluster_df[cluster_df['cluster'] == i]['ticker'].tolist()
        f.write(f"\n--- Cluster {i} ({len(members)} stocks) ---\n")
        f.write(', '.join(sorted(members)) + '\n')

print("Cluster assignments saved to hierarchical_clusters.txt")

# 6. Generate full dendrogram (truncated for readability)
print("\nGenerating dendrogram...")
plt.figure(figsize=(20, 10))
dendrogram(
    Z,
    labels=corr_matrix.columns.tolist(),
    leaf_rotation=90,
    leaf_font_size=6,
    truncate_mode='lastp',
    p=50,  # Show last 50 merges
    show_contracted=True
)
plt.title(f'Stock Dendrogram (Ward\'s Method) - Top 50 Clusters\n{len(returns.columns)} stocks')
plt.xlabel('Stock / Cluster')
plt.ylabel('Distance (1 - Correlation)')
plt.tight_layout()
plt.savefig('dendrogram_truncated.png', dpi=150)
plt.close()
print("Truncated dendrogram saved to dendrogram_truncated.png")

# 7. Generate dendrogram for top correlated stocks subset
# Select most liquid/important stocks for readable dendrogram
print("\nGenerating detailed dendrogram for subset...")

# Get stocks with highest average correlation (most connected)
avg_corr = corr_matrix.abs().mean()
top_tickers = avg_corr.nlargest(MAX_TICKERS_FULL).index.tolist()

# Subset correlation and recalculate
corr_subset = corr_matrix.loc[top_tickers, top_tickers]
dist_subset = 1 - corr_subset
np.fill_diagonal(dist_subset.values, 0)
dist_condensed_subset = squareform(dist_subset.values)
Z_subset = linkage(dist_condensed_subset, method='ward')

plt.figure(figsize=(25, 12))
dendrogram(
    Z_subset,
    labels=top_tickers,
    leaf_rotation=90,
    leaf_font_size=8,
    color_threshold=0.7 * max(Z_subset[:, 2])
)
plt.title(f'Stock Dendrogram (Ward\'s Method) - Top {MAX_TICKERS_FULL} Most Connected Stocks')
plt.xlabel('Stock Ticker')
plt.ylabel('Distance (1 - Correlation)')
plt.tight_layout()
plt.savefig('dendrogram_detailed.png', dpi=150)
plt.close()
print(f"Detailed dendrogram saved to dendrogram_detailed.png")

# 8. Generate sector-focused dendrograms
def generate_sector_dendrogram(tickers, title, filename):
    """Generate dendrogram for a specific set of tickers"""
    valid_tickers = [t for t in tickers if t in corr_matrix.columns]
    if len(valid_tickers) < 3:
        print(f"  Skipping {title} - not enough tickers ({len(valid_tickers)})")
        return

    corr_sub = corr_matrix.loc[valid_tickers, valid_tickers]
    dist_sub = 1 - corr_sub
    np.fill_diagonal(dist_sub.values, 0)
    dist_cond = squareform(dist_sub.values)
    Z_sub = linkage(dist_cond, method='ward')

    fig_height = max(6, len(valid_tickers) * 0.15)
    plt.figure(figsize=(12, fig_height))
    dendrogram(
        Z_sub,
        labels=valid_tickers,
        orientation='right',
        leaf_font_size=9
    )
    plt.title(f'{title} Dendrogram (Ward\'s Method)')
    plt.xlabel('Distance (1 - Correlation)')
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"  {title} dendrogram saved to {filename}")

print("\nGenerating sector dendrograms...")

# Tech stocks
tech_tickers = ['AAPL', 'MSFT', 'GOOGL', 'META', 'AMZN', 'NVDA', 'AMD', 'INTC', 'TSM',
                'AVGO', 'QCOM', 'CRM', 'ORCL', 'ADBE', 'NOW', 'PLTR', 'SNOW', 'NET',
                'CRWD', 'PANW', 'DDOG', 'MDB', 'ARM', 'SMCI', 'APP', 'COIN', 'HOOD']
generate_sector_dendrogram(tech_tickers, 'Technology', 'dendrogram_tech.png')

# Financials
fin_tickers = ['JPM', 'BAC', 'WFC', 'GS', 'MS', 'C', 'USB', 'PNC', 'TFC', 'SCHW',
               'BLK', 'BX', 'KKR', 'AXP', 'V', 'MA', 'PYPL', 'SQ', 'SOFI', 'COIN',
               'COF', 'DFS', 'SYF', 'ALLY']
generate_sector_dendrogram(fin_tickers, 'Financials', 'dendrogram_financials.png')

# Energy
energy_tickers = ['XOM', 'CVX', 'COP', 'EOG', 'SLB', 'OXY', 'PSX', 'VLO', 'MPC',
                  'DVN', 'FANG', 'HAL', 'BKR', 'OKE', 'WMB', 'KMI', 'TRGP']
generate_sector_dendrogram(energy_tickers, 'Energy', 'dendrogram_energy.png')

# AI/Data Center plays
ai_tickers = ['NVDA', 'AMD', 'SMCI', 'AVGO', 'MRVL', 'ARM', 'TSM', 'INTC',
              'MSFT', 'GOOGL', 'META', 'AMZN', 'PLTR', 'SNOW', 'AI', 'BBAI', 'SOUN',
              'IREN', 'CORZ', 'CLSK', 'CIFR', 'WULF', 'VST', 'CEG', 'NRG']
generate_sector_dendrogram(ai_tickers, 'AI & Data Centers', 'dendrogram_ai.png')

# Crypto-related
crypto_tickers = ['COIN', 'HOOD', 'MSTR', 'MARA', 'RIOT', 'CLSK', 'IREN', 'CORZ',
                  'CIFR', 'WULF', 'BITF', 'HUT', 'HIVE']
generate_sector_dendrogram(crypto_tickers, 'Crypto & Mining', 'dendrogram_crypto.png')

# Consumer
consumer_tickers = ['AMZN', 'WMT', 'COST', 'TGT', 'HD', 'LOW', 'NKE', 'SBUX', 'MCD',
                    'CMG', 'DPZ', 'YUM', 'LULU', 'RH', 'ULTA', 'DG', 'DLTR']
generate_sector_dendrogram(consumer_tickers, 'Consumer', 'dendrogram_consumer.png')

print("\n" + "=" * 50)
print("Analysis complete! Generated files:")
print("  - hierarchical_clusters.txt (cluster assignments)")
print("  - dendrogram_truncated.png (overview)")
print("  - dendrogram_detailed.png (top 100 stocks)")
print("  - dendrogram_tech.png")
print("  - dendrogram_financials.png")
print("  - dendrogram_energy.png")
print("  - dendrogram_ai.png")
print("  - dendrogram_crypto.png")
print("  - dendrogram_consumer.png")
