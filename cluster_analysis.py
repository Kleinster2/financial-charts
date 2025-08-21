import sqlite3
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from constants import DB_PATH, get_db_connection

print(f"Using database: {DB_PATH}")

# --- CONFIG ---
N_COMPONENTS = 10  # Use top 10 PCs as features for clustering
MAX_CLUSTERS = 20  # Max number of clusters for elbow plot
FINAL_N_CLUSTERS = 10 # Default number of clusters to use

# 1. Load and process stock returns data
print("Loading and processing stock returns...")
df_prices = pd.read_sql(
    "SELECT * FROM stock_prices_daily",
    get_db_connection(row_factory=None),
    parse_dates=["Date"],
).set_index("Date")

stock_ret = np.log(df_prices).diff()
stock_ret = stock_ret.ffill().bfill()
row_thresh = int(0.95 * stock_ret.shape[1])
stock_ret = stock_ret.dropna(axis=0, thresh=row_thresh)
col_thresh = int(0.95 * len(stock_ret))
stock_ret = stock_ret.dropna(axis=1, thresh=col_thresh)

# 2. Perform PCA to get features (loadings)
print(f"Performing PCA to get {N_COMPONENTS} components...")
X_std = StandardScaler().fit_transform(stock_ret)
pca = PCA(n_components=N_COMPONENTS).fit(X_std)

# The features for clustering are the stocks' loadings on the PCs
# Transpose components_ so that rows are stocks and columns are PCs
features = pca.components_.T

# 3. Generate Elbow Plot to find optimal k
print(f"Generating Elbow Plot for up to {MAX_CLUSTERS} clusters...")
inertias = []
ks = range(2, MAX_CLUSTERS + 1)

for k in ks:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto').fit(features)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(ks, inertias, '-o')
plt.xlabel('Number of clusters, k')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.xticks(ks)
plt.grid(True)
plt.savefig('elbow_plot.png')
plt.close()
print("Elbow plot saved to elbow_plot.png")

# 4. Perform final clustering and print results
print(f"\nPerforming K-Means clustering with k={FINAL_N_CLUSTERS}...")
kmeans = KMeans(n_clusters=FINAL_N_CLUSTERS, random_state=42, n_init='auto').fit(features)

results = pd.DataFrame({
    'ticker': stock_ret.columns,
    'cluster': kmeans.labels_
})

print("\nSaving cluster representatives to cluster_representatives.txt...")
# Get the cluster centroids
centroids = kmeans.cluster_centers_

with open('cluster_representatives.txt', 'w') as f:
    f.write("--- Cluster Representatives (Closest to Centroid) ---\n")
    for i in range(FINAL_N_CLUSTERS):
        # Get all stocks in the current cluster
        cluster_mask = (results['cluster'] == i)
        cluster_tickers = results[cluster_mask]['ticker'].tolist()
        cluster_features = features[cluster_mask]
        
        # Get the centroid for the current cluster
        centroid = centroids[i]
        
        # Calculate the distance of each stock in the cluster to the centroid
        distances = np.linalg.norm(cluster_features - centroid, axis=1)
        
        # Create a DataFrame for this cluster's stocks and their distances
        dist_df = pd.DataFrame({'ticker': cluster_tickers, 'distance': distances})
        dist_df = dist_df.sort_values(by='distance').reset_index(drop=True)
        
        f.write(f"\nCluster {i}: ({len(cluster_tickers)} stocks)\n")
        
        # Get top 3 representatives
        representatives = dist_df.head(3)
        for idx, row in representatives.iterrows():
            f.write(f"  {idx+1}. {row['ticker']} (Distance: {row['distance']:.4f})\n")

        # Print all members for reference
        f.write("\n  Members:\n")
        f.write('  ' + ', '.join(cluster_tickers) + '\n')

print("Results saved successfully.")
