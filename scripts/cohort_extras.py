"""Three additional analyses on the Space pure-plays cohort:

(f) Vol regime check — has the cohort's volatility tightened like its correlation?
(g) KTOS-AVAV UAS micro-cluster — small validation of the 2-name candidate
(h) LUNR + BKSY 2-name basket — drawdown profile + risk metrics
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


# === (f) VOL REGIME ===
print("=" * 72)
print("(f) Volatility regime check — has cohort vol tightened?")
print("=" * 72)

start_3y = (END - timedelta(days=1095)).isoformat()
prices = load(COHORT + ["SPY", "IWM"], start_3y, (END + timedelta(days=1)).isoformat())
rets = np.log(prices / prices.shift(1)).dropna(how="all")

window = 60
basket_rets = rets[COHORT].mean(axis=1)
basket_vol = basket_rets.rolling(window).std() * np.sqrt(252)
spy_vol = rets["SPY"].rolling(window).std() * np.sqrt(252)
iwm_vol = rets["IWM"].rolling(window).std() * np.sqrt(252)

# Per-name vol summary at different time points
print(f"\nAnnualized {window}-day vol — start vs end of 1Y window:")
print(f"{'Ticker':<8} {'1Y ago':>10} {'Latest':>10} {'Change':>10}")
print("-" * 45)
one_year_ago = END - timedelta(days=365)
for t in COHORT:
    vol_t = rets[t].rolling(window).std() * np.sqrt(252)
    try:
        start_val = vol_t.asof(pd.Timestamp(one_year_ago))
        latest_val = vol_t.iloc[-1]
        change = (latest_val - start_val) * 100
        print(f"{t:<8} {start_val:>9.1%} {latest_val:>9.1%} {change:>+9.1f}pp")
    except Exception:
        pass

print(f"\nBasket 60-day vol — 1Y ago: {basket_vol.asof(pd.Timestamp(one_year_ago)):.1%}  Latest: {basket_vol.iloc[-1]:.1%}")
print(f"SPY 60-day vol  — 1Y ago: {spy_vol.asof(pd.Timestamp(one_year_ago)):.1%}  Latest: {spy_vol.iloc[-1]:.1%}")
print(f"IWM 60-day vol  — 1Y ago: {iwm_vol.asof(pd.Timestamp(one_year_ago)):.1%}  Latest: {iwm_vol.iloc[-1]:.1%}")

# Chart: basket vol over time
basket_vol_chart = basket_vol.dropna()
fig, ax = plt.subplots(figsize=(11, 5.5))
ax.plot(basket_vol_chart.index, basket_vol_chart.values * 100,
        color="#2962FF", linewidth=2.2, label="Space pure-plays basket")
spy_chart = spy_vol.reindex(basket_vol_chart.index).dropna()
ax.plot(spy_chart.index, spy_chart.values * 100,
        color="#9E9E9E", linewidth=1.5, label="SPY")
iwm_chart = iwm_vol.reindex(basket_vol_chart.index).dropna()
ax.plot(iwm_chart.index, iwm_chart.values * 100,
        color="#FF9800", linewidth=1.5, label="IWM (small-cap)")
ax.set_title("Cohort volatility regime — rolling 60-day annualized vol",
             fontsize=13, loc="left")
ax.set_ylabel("Annualized vol (%)", fontsize=10)
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right", fontsize=9)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(OUT / "space-pureplays-vol-regime.png", dpi=140, bbox_inches="tight")
plt.close()
print(f"\nChart saved: {OUT}/space-pureplays-vol-regime.png")


# === (g) KTOS-AVAV UAS micro-cluster ===
print()
print("=" * 72)
print("(g) KTOS-AVAV UAS micro-cluster validation")
print("=" * 72)

uas_cluster = ["KTOS", "AVAV"]
controls = ["LMT", "RTX", "NOC", "LHX", "SPY", "IWM", "ITA"]
extras = ["MRCY", "BWXT", "HEI", "LDOS", "PSN", "CACI"]

uas_prices = load(uas_cluster + controls + extras, start_3y, (END + timedelta(days=1)).isoformat())
uas_rets = np.log(uas_prices / uas_prices.shift(1)).dropna()

# 1Y window
one_yr_ago = END - timedelta(days=365)
uas_1y = uas_rets.loc[uas_rets.index >= pd.Timestamp(one_yr_ago)]
ktos_avav_corr = uas_1y["KTOS"].corr(uas_1y["AVAV"])
print(f"\n1Y KTOS-AVAV pairwise correlation: {ktos_avav_corr:.3f}")
print(f"Observations: {len(uas_1y)}")

# Cross-correlations to potential UAS-cluster extras
print(f"\nCandidates that could join a UAS / drone-defense micro-cluster:")
print(f"{'Ticker':<8} {'corr to KTOS':>14} {'corr to AVAV':>14} {'avg':>10}")
for c in extras:
    corr_k = uas_1y["KTOS"].corr(uas_1y[c])
    corr_a = uas_1y["AVAV"].corr(uas_1y[c])
    avg = (corr_k + corr_a) / 2
    print(f"{c:<8} {corr_k:>14.3f} {corr_a:>14.3f} {avg:>10.3f}")

# Pair vs primes
print(f"\nKTOS-AVAV pair vs defense-prime control:")
for c in ["LMT", "RTX", "NOC", "LHX"]:
    pair_avg = (uas_1y["KTOS"].corr(uas_1y[c]) + uas_1y["AVAV"].corr(uas_1y[c])) / 2
    print(f"  avg corr to {c}: {pair_avg:.3f}")

# Pair vs ETFs
for c in ["SPY", "IWM", "ITA"]:
    pair_avg = (uas_1y["KTOS"].corr(uas_1y[c]) + uas_1y["AVAV"].corr(uas_1y[c])) / 2
    print(f"  avg corr to {c}: {pair_avg:.3f}")


# === (h) LUNR + BKSY 2-name basket — drawdown profile ===
print()
print("=" * 72)
print("(h) LUNR + BKSY 2-name basket — drawdown analysis")
print("=" * 72)

end_iso = (END + timedelta(days=1)).isoformat()
hh_prices = load(COHORT, (END - timedelta(days=365)).isoformat(), end_iso)
hh_rets = np.log(hh_prices / hh_prices.shift(1)).dropna()

lunr_bksy = hh_rets[["LUNR", "BKSY"]].mean(axis=1)
basket = hh_rets[COHORT].mean(axis=1)

lunr_bksy_cum = lunr_bksy.cumsum()
basket_cum = basket.cumsum()

# Drawdown computation
def drawdown(cum_log_rets: pd.Series) -> pd.Series:
    cum_idx = np.exp(cum_log_rets)
    rolling_max = cum_idx.cummax()
    dd = (cum_idx - rolling_max) / rolling_max
    return dd


lb_dd = drawdown(lunr_bksy_cum)
basket_dd = drawdown(basket_cum)

print(f"\n  {'Metric':<35} {'LUNR+BKSY':>12} {'Full 7':>10}")
print("-" * 60)
print(f"  {'Cumulative log return':<35} {lunr_bksy_cum.iloc[-1]:>+12.2%} {basket_cum.iloc[-1]:>+10.2%}")
print(f"  {'Cumulative simple return':<35} {(np.exp(lunr_bksy_cum.iloc[-1])-1):>+12.2%} {(np.exp(basket_cum.iloc[-1])-1):>+10.2%}")
print(f"  {'Annualized vol':<35} {lunr_bksy.std()*np.sqrt(252):>12.2%} {basket.std()*np.sqrt(252):>10.2%}")
print(f"  {'Annualized Sharpe (rf=0)':<35} {(lunr_bksy.mean()*252)/(lunr_bksy.std()*np.sqrt(252)):>12.2f} {(basket.mean()*252)/(basket.std()*np.sqrt(252)):>10.2f}")
print(f"  {'Max drawdown':<35} {lb_dd.min():>12.2%} {basket_dd.min():>10.2%}")
print(f"  {'Best single day (log)':<35} {lunr_bksy.max():>12.2%} {basket.max():>10.2%}")
print(f"  {'Worst single day (log)':<35} {lunr_bksy.min():>12.2%} {basket.min():>10.2%}")
print(f"  {'% positive sessions':<35} {(lunr_bksy > 0).mean():>12.1%} {(basket > 0).mean():>10.1%}")

# Recovery time from max drawdown
def recovery_days(cum: pd.Series, dd: pd.Series) -> int | None:
    """How many days from max drawdown to recovery to the prior peak."""
    trough_date = dd.idxmin()
    cum_idx = np.exp(cum)
    prior_peak = cum_idx.loc[:trough_date].cummax().iloc[-1]
    post_trough = cum_idx.loc[trough_date:]
    recovered = post_trough[post_trough >= prior_peak]
    if len(recovered):
        return (recovered.index[0] - trough_date).days
    return None  # not yet recovered

lb_rec = recovery_days(lunr_bksy_cum, lb_dd)
basket_rec = recovery_days(basket_cum, basket_dd)
print(f"  {'Days to recover from max DD':<35} {str(lb_rec) if lb_rec else 'NOT YET':>12} {str(basket_rec) if basket_rec else 'NOT YET':>10}")
print(f"  {'Max DD trough date':<35} {lb_dd.idxmin().strftime('%Y-%m-%d'):>12} {basket_dd.idxmin().strftime('%Y-%m-%d'):>10}")

# Chart: drawdown comparison
fig, ax = plt.subplots(figsize=(11, 5.5))
ax.fill_between(lb_dd.index, lb_dd.values * 100, 0, color="#2962FF", alpha=0.25)
ax.plot(lb_dd.index, lb_dd.values * 100, color="#2962FF", linewidth=2,
        label=f"LUNR + BKSY (max DD {lb_dd.min():.1%})")
ax.plot(basket_dd.index, basket_dd.values * 100, color="#E91E63", linewidth=1.5,
        label=f"Full 7-name basket (max DD {basket_dd.min():.1%})", linestyle="--")
ax.axhline(0, color="black", linewidth=0.6)
ax.set_title("Drawdown profile — 2-name LUNR+BKSY vs full 7-name basket (1Y)",
             fontsize=13, loc="left")
ax.set_ylabel("Drawdown (%)", fontsize=10)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(OUT / "lunr-bksy-vs-basket-drawdown.png", dpi=140, bbox_inches="tight")
plt.close()
print(f"\n  Chart saved: {OUT}/lunr-bksy-vs-basket-drawdown.png")
