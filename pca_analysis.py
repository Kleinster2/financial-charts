import sqlite3
import numpy as np
import sqlite3
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from constants import DB_PATH, get_db_connection

N_COMPONENTS = 10  # number of principal components to keep

# 1. Load prices
print(f"Loading prices from database: {DB_PATH}")
df = pd.read_sql("SELECT * FROM stock_prices_daily", get_db_connection(), parse_dates=["Date"]).set_index("Date")

# 2. Compute daily log-returns
returns = np.log(df).diff().dropna()

# 3. Drop columns with any missing values (rare after ffill)
returns = returns.dropna(axis=1)

# 4. Standardize
scaler = StandardScaler()
X_std = scaler.fit_transform(returns.values)

# 5. PCA
pca = PCA(n_components=N_COMPONENTS)
principal_components = pca.fit_transform(X_std)

# 6. Show variance explained (already printed earlier if needed)
explained = pca.explained_variance_ratio_ * 100
print("Explained variance (%):")
for i, v in enumerate(explained, 1):
    print(f"PC{i}: {v:.2f}%")
print(f"Total (first {N_COMPONENTS} PCs): {explained.sum():.2f}%")

# 7. Compute loadings for first two PCs
loadings = pd.DataFrame(pca.components_[:2].T,
                        index=returns.columns,
                        columns=["PC1", "PC2"])

print("\nTop 10 positive PC1 loadings:")
print(loadings["PC1"].sort_values(ascending=False).head(10).to_string())
print("\nTop 10 negative PC1 loadings:")
print(loadings["PC1"].sort_values().head(10).to_string())
print("\nTop 10 positive PC2 loadings:")
print(loadings["PC2"].sort_values(ascending=False).head(10).to_string())
print("\nTop 10 negative PC2 loadings:")
print(loadings["PC2"].sort_values().head(10).to_string())

# 6. Report variance explained
explained = pca.explained_variance_ratio_ * 100
print("Explained variance (%):")
for i, v in enumerate(explained, 1):
    print(f"PC{i}: {v:.2f}%")
print(f"Total (first {N_COMPONENTS} PCs): {explained.sum():.2f}%")

# 8. Optional plot
plt.figure(figsize=(8,4))
plt.bar(range(1, len(explained)+1), explained, alpha=0.7)
plt.ylabel("Variance Explained (%)")
plt.xlabel("Principal Component")
plt.title("S&P 500 Daily Return PCA - Variance Explained")
plt.tight_layout()
plt.show()
