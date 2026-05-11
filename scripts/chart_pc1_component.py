"""Compute and chart the PC1 component for the Space pure-plays cluster.

PC1 = the synthetic "space pure-play factor" — daily returns projected onto the
first principal component of the 7-name cohort. Cumulates into an index level
that can be plotted alongside individual members + benchmarks.
"""
from __future__ import annotations
import sqlite3
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

DB = Path(__file__).resolve().parent.parent / "market_data.db"
OUT = Path(__file__).resolve().parent.parent / "investing" / "attachments"
COHORT = ["RKLB", "RDW", "LUNR", "BKSY", "ASTS", "SPIR", "PL"]
BENCHMARKS = ["SPY", "IWM", "ITA"]
END = date(2026, 5, 8)
START = date(2024, 1, 1)


def load(tickers: list[str], start: date, end: date) -> pd.DataFrame:
    cols = ", ".join(f'"{t}"' for t in tickers)
    sql = f"SELECT Date, {cols} FROM stock_prices_daily WHERE Date BETWEEN ? AND ? ORDER BY Date"
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql(sql, conn, params=[start.isoformat(), end.isoformat()])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date")
    df = df.apply(pd.to_numeric, errors="coerce")
    return df.replace({0: np.nan})


prices = load(COHORT + BENCHMARKS, START, END)
rets = np.log(prices / prices.shift(1)).dropna(how="all")
cohort_rets = rets[COHORT].dropna()

pca = PCA(n_components=3)
pca.fit(cohort_rets.values)
pc1_load = pca.components_[0]
pc1_var = pca.explained_variance_ratio_[0]

# Sign convention: positive returns should map to positive PC1 score
if pc1_load.mean() < 0:
    pc1_load = -pc1_load

pc1_returns = cohort_rets.values @ pc1_load
pc1_series = pd.Series(pc1_returns, index=cohort_rets.index, name="PC1 factor")

# Equal-weighted basket for comparison
ew_returns = cohort_rets.mean(axis=1)

# Cumulate each into index levels starting at 100
pc1_idx = (np.exp(pc1_series.cumsum())) * 100
ew_idx = (np.exp(ew_returns.cumsum())) * 100

# Aligned benchmark levels
bench_rets = rets[BENCHMARKS].reindex(cohort_rets.index).fillna(0)
bench_idx = (np.exp(bench_rets.cumsum())) * 100

# --- Chart 1: PC1 vs equal-weighted basket vs benchmarks ---
fig, ax = plt.subplots(figsize=(11, 6.5))
ax.plot(pc1_idx.index, pc1_idx.values, color="#2962FF", linewidth=2.5,
        label=f"PC1 factor (explains {pc1_var:.1%} of cohort variance)")
ax.plot(ew_idx.index, ew_idx.values, color="#E91E63", linewidth=2,
        label="Equal-weighted basket", alpha=0.85)
ax.plot(bench_idx.index, bench_idx["SPY"], color="#9E9E9E", linewidth=1.2,
        label="SPY", alpha=0.7)
ax.plot(bench_idx.index, bench_idx["ITA"], color="#7E57C2", linewidth=1.2,
        label="ITA (defense)", alpha=0.7)

ax.set_yscale("log")
ax.set_title("Space pure-plays — PC1 factor vs equal-weighted basket vs benchmarks",
             fontsize=13, loc="left")
ax.set_ylabel("Index level (start = 100, log scale)", fontsize=10)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=9, framealpha=0.95)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(OUT / "space-pureplays-pc1-index.png", dpi=140, bbox_inches="tight")
plt.close()

# --- Chart 2: PC1 vs each cohort member ---
fig, ax = plt.subplots(figsize=(11, 6.5))
member_palette = ["#2962FF", "#E91E63", "#4CAF50", "#FF9800", "#9C27B0", "#00BCD4", "#795548"]
for i, t in enumerate(COHORT):
    member_rets = cohort_rets[t]
    member_idx = (np.exp(member_rets.cumsum())) * 100
    ax.plot(member_idx.index, member_idx.values, color=member_palette[i],
            linewidth=1.2, alpha=0.65, label=t)
ax.plot(pc1_idx.index, pc1_idx.values, color="black", linewidth=2.8,
        label=f"PC1 factor ({pc1_var:.1%})", zorder=10)

ax.set_yscale("log")
ax.set_title("PC1 factor vs individual cohort members",
             fontsize=13, loc="left")
ax.set_ylabel("Index level (start = 100, log scale)", fontsize=10)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", fontsize=9, ncol=2, framealpha=0.95)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(OUT / "space-pureplays-pc1-vs-members.png", dpi=140, bbox_inches="tight")
plt.close()

# --- Chart 3: Rolling PC1 explained variance (cohort cohesion over time) ---
window = 60
rolling_pc1_var = []
for i in range(window, len(cohort_rets)):
    sub = cohort_rets.iloc[i - window:i].values
    p = PCA(n_components=3)
    p.fit(sub)
    rolling_pc1_var.append(p.explained_variance_ratio_[0])

rolling_dates = cohort_rets.index[window:]
rolling_series = pd.Series(rolling_pc1_var, index=rolling_dates)

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.fill_between(rolling_series.index, 0, rolling_series.values * 100,
                color="#2962FF", alpha=0.25)
ax.plot(rolling_series.index, rolling_series.values * 100,
        color="#2962FF", linewidth=2.5, label=f"PC1 explained variance ({window}-day rolling)")
ax.axhline(50, color="#666", linestyle="--", linewidth=0.8, alpha=0.6,
           label="50% threshold (single-factor cohort)")
ax.axhline(67.96, color="#E91E63", linestyle=":", linewidth=1.2, alpha=0.7,
           label="1Y point-in-time value (67.96%)")
ax.set_ylim(30, 90)
ax.set_title("Cohort cohesion over time — rolling 60-day PC1 explained variance",
             fontsize=13, loc="left")
ax.set_ylabel("% of cohort variance explained by PC1", fontsize=10)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9, framealpha=0.95)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(OUT / "space-pureplays-pc1-rolling-variance.png", dpi=140, bbox_inches="tight")
plt.close()

print(f"PC1 explained variance (full window): {pc1_var:.2%}")
print(f"PC1 loadings:")
for t, w in zip(COHORT, pc1_load):
    print(f"  {t}: {w:+.4f}")
print(f"\nPC1 vs equal-weighted correlation: {pc1_series.corr(ew_returns):.4f}")
print(f"PC1 final level: {pc1_idx.iloc[-1]:.1f}")
print(f"Equal-weighted final level: {ew_idx.iloc[-1]:.1f}")
print(f"SPY final level: {bench_idx['SPY'].iloc[-1]:.1f}")
print(f"\nRolling PC1 var: min={min(rolling_pc1_var):.2%}, max={max(rolling_pc1_var):.2%}, latest={rolling_pc1_var[-1]:.2%}")
print(f"\nCharts saved:")
print(f"  {OUT}/space-pureplays-pc1-index.png")
print(f"  {OUT}/space-pureplays-pc1-vs-members.png")
print(f"  {OUT}/space-pureplays-pc1-rolling-variance.png")
