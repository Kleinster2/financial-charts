"""Deep-dive analysis for the Space pure-plays cluster:

1. Factor decomposition — regress cohort returns on broad benchmarks (SPY, IWM, ITA).
   Residual variance = the cohort-specific factor beyond what existing benchmarks
   explain. If residual is large, the basket has a genuine pure-play factor.

2. Missing-name screen — test candidates (DXYZ, IRDM, KARO, KTOS, AVAV, MNTS, SIDU)
   against the validated 7-name cohort. Candidates with high pairwise correlation
   to multiple cohort members are candidates for inclusion.

3. PC2 inspection — what does the second principal component capture? Often
   reveals sub-structure (e.g., launch vs data, defense-tied vs commercial).
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
BENCHMARKS = ["SPY", "IWM", "ITA"]
CANDIDATES = ["DXYZ", "IRDM", "KTOS", "AVAV", "KARO", "MNTS", "SIDU"]
END = date(2026, 5, 8)
START_1Y = (END - timedelta(days=365)).isoformat()


def load(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    cols = ", ".join(f'"{t}"' for t in tickers)
    sql = f"SELECT Date, {cols} FROM stock_prices_daily WHERE Date BETWEEN ? AND ? ORDER BY Date"
    with sqlite3.connect(DB) as conn:
        try:
            df = pd.read_sql(sql, conn, params=[start, end])
        except Exception as e:
            print(f"  query failed: {e}")
            return pd.DataFrame()
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date").apply(pd.to_numeric, errors="coerce")
    return df.replace({0: np.nan})


def returns(prices: pd.DataFrame) -> pd.DataFrame:
    return np.log(prices / prices.shift(1)).dropna(how="all")


# === 1. FACTOR DECOMPOSITION ===
print("=" * 70)
print("1. FACTOR DECOMPOSITION — pure-play factor beyond SPY/IWM/ITA")
print("=" * 70)

prices = load(COHORT + BENCHMARKS, START_1Y, END.isoformat())
rets = returns(prices).dropna()

# Cohort equal-weighted basket
basket_rets = rets[COHORT].mean(axis=1)
X = rets[BENCHMARKS].values
y = basket_rets.values

reg = LinearRegression()
reg.fit(X, y)
y_pred = reg.predict(X)
residuals = y - y_pred

total_var = np.var(y)
explained_var = np.var(y_pred)
residual_var = np.var(residuals)
r_squared = reg.score(X, y)

print(f"\nObservations: {len(y)}")
print(f"R-squared (var explained by SPY/IWM/ITA): {r_squared:.1%}")
print(f"Residual variance (pure-play factor): {1 - r_squared:.1%}")
print(f"\nBetas:")
for b, beta in zip(BENCHMARKS, reg.coef_):
    print(f"  {b}: {beta:+.3f}")
print(f"Intercept (alpha, daily): {reg.intercept_:+.5f} ({reg.intercept_ * 252 * 100:+.2f}% annualized)")

# Same regression on each individual cohort member
print(f"\nPer-name factor exposure (R² to SPY/IWM/ITA):")
for t in COHORT:
    y_t = rets[t].values
    reg_t = LinearRegression()
    reg_t.fit(X, y_t)
    r2_t = reg_t.score(X, y_t)
    print(f"  {t}: R² = {r2_t:.1%}  (residual {1-r2_t:.1%} is name-specific + cohort factor)")


# === 2. MISSING-NAME SCREEN ===
print("\n" + "=" * 70)
print("2. MISSING-NAME SCREEN — do other tickers belong in the cluster?")
print("=" * 70)

all_tickers = COHORT + CANDIDATES
prices_full = load(all_tickers, START_1Y, END.isoformat())
rets_full = returns(prices_full)

# For each candidate, compute average correlation to the validated 7-name cohort
print(f"\n{'Ticker':<8} {'avg corr to cohort':>22} {'data obs':>10} {'verdict'}")
print("-" * 70)
for cand in CANDIDATES:
    if cand not in rets_full.columns:
        print(f"{cand:<8} {'-- not in DB --':>22}")
        continue
    sub = rets_full[COHORT + [cand]].dropna()
    if len(sub) < 60:
        print(f"{cand:<8} {'-- insufficient obs --':>22} {len(sub):>10}")
        continue
    corrs = [sub[cand].corr(sub[m]) for m in COHORT]
    avg_corr = float(np.mean(corrs))
    verdict = "JOIN cluster" if avg_corr >= 0.50 else ("MAYBE" if avg_corr >= 0.35 else "exclude")
    print(f"{cand:<8} {avg_corr:>22.3f} {len(sub):>10} {verdict}")


# === 3. PC2 INSPECTION ===
print("\n" + "=" * 70)
print("3. PC2 INSPECTION — sub-structure within the cohort")
print("=" * 70)

cohort_rets = rets[COHORT].dropna()
pca = PCA(n_components=min(7, len(COHORT)))
pca.fit(cohort_rets.values)

print(f"\nExplained variance by component:")
for i, v in enumerate(pca.explained_variance_ratio_):
    cum = pca.explained_variance_ratio_[:i+1].sum()
    print(f"  PC{i+1}: {v:.1%}  (cumulative: {cum:.1%})")

print(f"\nPC1 loadings (all positive = market factor):")
for t, w in zip(COHORT, pca.components_[0]):
    print(f"  {t}: {w:+.4f}")

print(f"\nPC2 loadings (sign matters — reveals sub-structure):")
pc2 = pca.components_[1]
# Sort by magnitude
order = np.argsort(np.abs(pc2))[::-1]
for idx in order:
    t = COHORT[idx]
    w = pc2[idx]
    direction = "LONG" if w > 0 else "SHORT"
    print(f"  {t}: {w:+.4f}  ({direction} in PC2)")

# Interpret PC2 — which names are in the "positive" sleeve, which in "negative"
pc2_long = [COHORT[i] for i in range(len(COHORT)) if pc2[i] > 0.1]
pc2_short = [COHORT[i] for i in range(len(COHORT)) if pc2[i] < -0.1]
pc2_neutral = [COHORT[i] for i in range(len(COHORT)) if abs(pc2[i]) <= 0.1]
print(f"\nPC2 sub-structure interpretation:")
print(f"  Positive sleeve: {pc2_long}")
print(f"  Negative sleeve: {pc2_short}")
print(f"  Neutral: {pc2_neutral}")
