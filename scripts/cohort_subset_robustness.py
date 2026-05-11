"""Two follow-up tests on the LUNR+BKSY 2-name finding:

(k) Robustness — is LUNR+BKSY outperformance consistent across rolling windows,
    or concentrated in specific periods?

(m) Complement test — how does the 5-name complement (RKLB+RDW+ASTS+SPIR+PL)
    perform? If LUNR+BKSY captured the high-return component, the complement
    should underperform the full basket.
"""
from __future__ import annotations
import sqlite3
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DB = Path(__file__).resolve().parent.parent / "market_data.db"
OUT = Path(__file__).resolve().parent.parent / "investing" / "attachments"
COHORT = ["RKLB", "RDW", "LUNR", "BKSY", "ASTS", "SPIR", "PL"]
TIGHT = ["LUNR", "BKSY"]
COMPLEMENT = [t for t in COHORT if t not in TIGHT]
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


# Use 2Y window for the rolling robustness check
start = (END - timedelta(days=730)).isoformat()
prices = load(COHORT, start, (END + timedelta(days=1)).isoformat())
rets = np.log(prices / prices.shift(1)).dropna()

tight_rets = rets[TIGHT].mean(axis=1)
full_rets = rets[COHORT].mean(axis=1)
comp_rets = rets[COMPLEMENT].mean(axis=1)


# === (k) ROBUSTNESS ===
print("=" * 72)
print("(k) Rolling robustness — LUNR+BKSY vs full basket")
print("=" * 72)

print(f"\nLookback comparisons (annualized Sharpe, ann vol, cum return):")
print(f"{'Window':<10} {'Pair Sharpe':>14} {'Basket Sharpe':>15} {'Pair vol':>11} {'Basket vol':>12} {'Pair cum %':>12} {'Basket cum %':>13}")
for label, lookback_days in [("3M", 90), ("6M", 180), ("1Y", 365), ("2Y", 730)]:
    cutoff = END - timedelta(days=lookback_days)
    p = tight_rets.loc[tight_rets.index >= pd.Timestamp(cutoff)]
    b = full_rets.loc[full_rets.index >= pd.Timestamp(cutoff)]
    p_sharpe = (p.mean() * 252) / (p.std() * np.sqrt(252))
    b_sharpe = (b.mean() * 252) / (b.std() * np.sqrt(252))
    p_cum = (np.exp(p.sum()) - 1) * 100
    b_cum = (np.exp(b.sum()) - 1) * 100
    p_vol = p.std() * np.sqrt(252) * 100
    b_vol = b.std() * np.sqrt(252) * 100
    print(f"{label:<10} {p_sharpe:>14.2f} {b_sharpe:>15.2f} {p_vol:>10.1f}% {b_vol:>11.1f}% {p_cum:>+11.1f}% {b_cum:>+12.1f}%")

# Rolling 60-day spread (LUNR+BKSY minus full basket cumulative log return)
window = 60
rolling_spread = (tight_rets.rolling(window).sum() - full_rets.rolling(window).sum())
rolling_spread = rolling_spread.dropna()
pct_pair_outperforms = (rolling_spread > 0).mean() * 100

print(f"\n% of rolling 60-day windows where LUNR+BKSY outperformed full basket: {pct_pair_outperforms:.1f}%")
print(f"Best 60-day spread: +{rolling_spread.max() * 100:.1f}% on {rolling_spread.idxmax().strftime('%Y-%m-%d')}")
print(f"Worst 60-day spread: {rolling_spread.min() * 100:.1f}% on {rolling_spread.idxmin().strftime('%Y-%m-%d')}")
print(f"Average 60-day spread: {rolling_spread.mean() * 100:+.2f}%")


# === (m) COMPLEMENT TEST ===
print()
print("=" * 72)
print("(m) Complement test — the 5-name basket WITHOUT LUNR/BKSY")
print("=" * 72)
print(f"Complement names: {', '.join(COMPLEMENT)}")

# Use 1Y for direct comparison
cutoff_1y = END - timedelta(days=365)
t1 = tight_rets.loc[tight_rets.index >= pd.Timestamp(cutoff_1y)]
f1 = full_rets.loc[full_rets.index >= pd.Timestamp(cutoff_1y)]
c1 = comp_rets.loc[comp_rets.index >= pd.Timestamp(cutoff_1y)]


def stats(r: pd.Series) -> dict:
    cum_log = r.sum()
    cum_simple = (np.exp(cum_log) - 1) * 100
    vol = r.std() * np.sqrt(252) * 100
    sharpe = (r.mean() * 252) / (r.std() * np.sqrt(252))
    cum_idx = np.exp(r.cumsum())
    rolling_max = cum_idx.cummax()
    dd = (cum_idx - rolling_max) / rolling_max
    return {
        "cum_simple": cum_simple,
        "vol": vol,
        "sharpe": sharpe,
        "max_dd": dd.min() * 100,
        "best_day": r.max() * 100,
        "worst_day": r.min() * 100,
    }


t_stats = stats(t1)
f_stats = stats(f1)
c_stats = stats(c1)

print(f"\n  {'Metric':<25} {'LUNR+BKSY':>12} {'Full 7':>10} {'Complement (5)':>16}")
print("-" * 70)
for key, label in [
    ("cum_simple", "Cumulative return %"),
    ("vol", "Annualized vol %"),
    ("sharpe", "Sharpe (rf=0)"),
    ("max_dd", "Max drawdown %"),
    ("best_day", "Best day (log %)"),
    ("worst_day", "Worst day (log %)"),
]:
    fmt = "+{:.2f}" if key != "sharpe" else "{:.2f}"
    print(f"  {label:<25} {fmt.format(t_stats[key]):>12} {fmt.format(f_stats[key]):>10} {fmt.format(c_stats[key]):>16}")

# Per-name contribution to cohort return (1Y)
per_name = {}
for t in COHORT:
    r_t = rets[t].loc[rets.index >= pd.Timestamp(cutoff_1y)]
    per_name[t] = (np.exp(r_t.sum()) - 1) * 100

print(f"\nPer-name 1Y cumulative return:")
for t, ret in sorted(per_name.items(), key=lambda x: -x[1]):
    in_tight = "(in LUNR+BKSY)" if t in TIGHT else "(complement)"
    print(f"  {t:<6} {ret:>+10.1f}%  {in_tight}")


# === CHART ===
fig, axes = plt.subplots(2, 1, figsize=(11, 9), gridspec_kw={"height_ratios": [2, 1]})
tight_cum_idx = (np.exp(tight_rets.cumsum()) - 1) * 100
full_cum_idx = (np.exp(full_rets.cumsum()) - 1) * 100
comp_cum_idx = (np.exp(comp_rets.cumsum()) - 1) * 100

axes[0].plot(tight_cum_idx.index, tight_cum_idx.values, color="#2962FF", linewidth=2.2,
             label=f"LUNR+BKSY (2-name) +{tight_cum_idx.iloc[-1]:.0f}%")
axes[0].plot(full_cum_idx.index, full_cum_idx.values, color="black", linewidth=1.6,
             label=f"Full 7-name basket +{full_cum_idx.iloc[-1]:.0f}%")
axes[0].plot(comp_cum_idx.index, comp_cum_idx.values, color="#E91E63", linewidth=1.6,
             label=f"5-name complement +{comp_cum_idx.iloc[-1]:.0f}%", linestyle="--")
axes[0].set_title("LUNR+BKSY vs full basket vs 5-name complement (2Y cumulative simple return)",
                  fontsize=13, loc="left")
axes[0].set_ylabel("Cumulative return %", fontsize=10)
axes[0].grid(True, alpha=0.3)
axes[0].legend(loc="upper left", fontsize=10)
axes[0].spines["top"].set_visible(False)
axes[0].spines["right"].set_visible(False)

# Rolling spread
axes[1].fill_between(rolling_spread.index, rolling_spread.values * 100, 0,
                     where=(rolling_spread.values * 100 > 0),
                     color="#2962FF", alpha=0.3, label="LUNR+BKSY outperformed")
axes[1].fill_between(rolling_spread.index, rolling_spread.values * 100, 0,
                     where=(rolling_spread.values * 100 <= 0),
                     color="#E91E63", alpha=0.3, label="LUNR+BKSY underperformed")
axes[1].plot(rolling_spread.index, rolling_spread.values * 100, color="#666", linewidth=1)
axes[1].axhline(0, color="black", linewidth=0.6)
axes[1].set_title(f"Rolling 60-day spread (LUNR+BKSY minus full basket)",
                  fontsize=12, loc="left")
axes[1].set_ylabel("Spread (log %)", fontsize=10)
axes[1].grid(True, alpha=0.3)
axes[1].legend(loc="upper left", fontsize=9)
axes[1].spines["top"].set_visible(False)
axes[1].spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(OUT / "lunr-bksy-robustness-vs-complement.png", dpi=140, bbox_inches="tight")
plt.close()
print(f"\nChart saved: {OUT}/lunr-bksy-robustness-vs-complement.png")
