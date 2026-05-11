"""Two final analyses on the Space pure-plays cohort:

(i) PC3 inspection — what does the third principal component capture, if anything?
(ii) Interest-rate correlation — does cohort move with rates (TLT inverse / 10Y yield)?
"""
from __future__ import annotations
import sqlite3
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

DB = Path(__file__).resolve().parent.parent / "market_data.db"
COHORT = ["RKLB", "RDW", "LUNR", "BKSY", "ASTS", "SPIR", "PL"]
END = date(2026, 5, 8)


def load(tickers, start, end):
    ph = ",".join("?" * len(tickers))
    sql = (
        f"SELECT Date, Ticker, Close FROM prices_long "
        f"WHERE Ticker IN ({ph}) AND Date BETWEEN ? AND ? ORDER BY Date"
    )
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=tickers + [start, end])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.pivot(index="Date", columns="Ticker", values="Close")
    df = df.apply(pd.to_numeric, errors="coerce")
    return df.replace({0: np.nan})


start = (END - timedelta(days=365)).isoformat()
end = (END + timedelta(days=1)).isoformat()

# === (i) PC3 INSPECTION ===
print("=" * 72)
print("(i) PC3 inspection — what does the third principal component capture?")
print("=" * 72)

prices = load(COHORT, start, end)
rets = np.log(prices / prices.shift(1)).dropna()
pca = PCA(n_components=7)
pca.fit(rets.values)

print(f"\nFull eigenvalue spectrum:")
for i in range(7):
    v = pca.explained_variance_ratio_[i]
    cum = pca.explained_variance_ratio_[:i+1].sum()
    print(f"  PC{i+1}: {v:.2%}  (cumulative: {cum:.2%})")

print(f"\nPC1 loadings (all positive = market factor):")
for t, w in zip(COHORT, pca.components_[0]):
    print(f"  {t}: {w:+.4f}")

print(f"\nPC2 loadings (data sleeve vs hardware sleeve):")
for t, w in zip(COHORT, pca.components_[1]):
    print(f"  {t}: {w:+.4f}")

print(f"\nPC3 loadings (the new question):")
pc3 = pca.components_[2]
ordered = sorted(zip(COHORT, pc3), key=lambda x: -x[1])
for t, w in ordered:
    print(f"  {t}: {w:+.4f}")

# Group PC3 loadings
pc3_pos = [t for t, w in zip(COHORT, pc3) if w > 0.2]
pc3_neg = [t for t, w in zip(COHORT, pc3) if w < -0.2]
print(f"\nPC3 sub-structure:")
print(f"  Positive PC3 (|w|>0.2): {pc3_pos}")
print(f"  Negative PC3 (|w|>0.2): {pc3_neg}")


# === (ii) INTEREST-RATE CORRELATION ===
print()
print("=" * 72)
print("(ii) Interest-rate correlation — rate sensitivity of the cohort")
print("=" * 72)

rate_proxies = ["TLT", "IEF", "SHY"]  # Long, intermediate, short Treasury ETFs
extras = load(rate_proxies, start, end)
rate_rets = np.log(extras / extras.shift(1)).dropna()

basket_rets = rets[COHORT].mean(axis=1)

aligned = pd.concat([basket_rets.rename("basket"), rate_rets], axis=1).dropna()
print(f"\nObservations: {len(aligned)}")

print(f"\nPairwise correlation of basket to rate proxies (1Y):")
for proxy in rate_proxies:
    if proxy not in aligned.columns:
        print(f"  {proxy}: -- not in DB --")
        continue
    corr = aligned["basket"].corr(aligned[proxy])
    print(f"  basket vs {proxy}: {corr:+.4f}  (positive = bond rally = cohort rally)")

# Per-name correlation to TLT
print(f"\nPer-name correlation to TLT (long-bond proxy):")
for t in COHORT:
    name_rets = rets[t].loc[rets.index.isin(aligned.index)]
    tlt_rets = aligned["TLT"]
    aligned_pair = pd.concat([name_rets, tlt_rets], axis=1).dropna()
    if len(aligned_pair) < 30:
        print(f"  {t}: insufficient obs")
        continue
    corr = aligned_pair.iloc[:, 0].corr(aligned_pair["TLT"])
    print(f"  {t}: {corr:+.4f}")

# Multivariate regression: basket ~ SPY + IWM + ITA + TLT
print(f"\nMultivariate regression: basket ~ SPY + IWM + ITA + TLT")
benchmarks = ["SPY", "IWM", "ITA"] + rate_proxies
prices_full = load(COHORT + benchmarks, start, end)
rets_full = np.log(prices_full / prices_full.shift(1)).dropna()

basket_full = rets_full[COHORT].mean(axis=1)
X = rets_full[["SPY", "IWM", "ITA", "TLT"]].values
y = basket_full.values

reg = LinearRegression()
reg.fit(X, y)
y_pred = reg.predict(X)
r2 = reg.score(X, y)
print(f"\nR-squared (var explained by SPY/IWM/ITA/TLT): {r2:.1%}")
print(f"Residual variance (pure-play factor): {1 - r2:.1%}")
print(f"\nBetas:")
for f, b in zip(["SPY", "IWM", "ITA", "TLT"], reg.coef_):
    print(f"  {f}: {b:+.4f}")
print(f"\nIncremental TLT beta contribution: ", end="")
# Compare to SPY+IWM+ITA only
X_no_tlt = rets_full[["SPY", "IWM", "ITA"]].values
reg2 = LinearRegression()
reg2.fit(X_no_tlt, y)
r2_no_tlt = reg2.score(X_no_tlt, y)
print(f"R² without TLT = {r2_no_tlt:.1%}; adding TLT moves R² to {r2:.1%} ({(r2-r2_no_tlt)*100:+.1f}pp)")
