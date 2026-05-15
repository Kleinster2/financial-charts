"""Generate dxyz-price-vs-nav.png — DXYZ daily price + quarterly NAV/share step + premium subplot."""
import sqlite3, sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

DB = Path(r"C:\Users\klein\financial-charts\market_data.db")
OUT = Path(r"C:\Users\klein\financial-charts\investing\attachments\dxyz-price-vs-nav.png")

# Quarterly NAV/share, per DXYZ note's NAV history table
NAV_DATA = [
    ("2023-12-31",  4.84),
    ("2024-03-31",  5.07),
    ("2024-06-30",  5.15),
    ("2024-09-30",  5.32),
    ("2024-12-31",  6.44),
    ("2025-03-31",  6.31),
    ("2025-06-30",  6.92),
    ("2025-09-30", 11.37),
    ("2025-12-31", 19.97),
]

with sqlite3.connect(DB) as c:
    px = pd.read_sql_query(
        "SELECT Date, Close FROM prices_long WHERE Ticker='DXYZ' ORDER BY Date",
        c, parse_dates=["Date"],
    )

nav = pd.DataFrame(NAV_DATA, columns=["Date", "NAV"])
nav["Date"] = pd.to_datetime(nav["Date"])

px = px[px["Date"] >= "2024-03-26"].reset_index(drop=True)

nav_ff = nav.set_index("Date").reindex(px["Date"].values, method="ffill").reset_index()
nav_ff.columns = ["Date", "NAV"]
premium = (px["Close"].values / nav_ff["NAV"].values - 1) * 100

peak_idx = px["Close"].idxmax()
peak_date = px.loc[peak_idx, "Date"]
peak_price = px.loc[peak_idx, "Close"]
prem_peak_idx = premium.argmax()
prem_peak_val = premium[prem_peak_idx]
prem_peak_date = px.loc[prem_peak_idx, "Date"]
ipo_date = pd.Timestamp("2026-03-26") if False else pd.Timestamp("2024-03-26")
ipo_price = px.iloc[0]["Close"]
last_date = px.iloc[-1]["Date"]
last_price = px.iloc[-1]["Close"]
last_nav = nav.iloc[-1]["NAV"]
last_premium = premium[-1]

may11_idx = px[px["Date"] == "2026-05-11"].index
may11_price = px.loc[may11_idx[0], "Close"] if len(may11_idx) else None

plt.style.use("dark_background")
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(12, 8),
    gridspec_kw={"height_ratios": [3, 1], "hspace": 0.08},
    sharex=True,
)
fig.patch.set_facecolor("#0d1117")
for ax in (ax1, ax2):
    ax.set_facecolor("#0d1117")
    ax.grid(True, alpha=0.15, linestyle="-", color="gray")
    for spine in ax.spines.values():
        spine.set_color("#444")

ax1.plot(px["Date"], px["Close"], color="#3b82f6", linewidth=1.0, label="DXYZ Stock Price")
ax1.step(nav["Date"], nav["NAV"], where="post", color="#f59e0b", linewidth=2.0, label="NAV/Share (quarterly)")
ax1.set_ylabel("Price ($)", color="#ddd")
ax1.tick_params(colors="#ccc")
ax1.legend(loc="upper left", facecolor="#0d1117", edgecolor="#444", labelcolor="#ddd")

ax1.annotate(f"Peak ${peak_price:.0f}", xy=(peak_date, peak_price),
             xytext=(peak_date, peak_price + 6),
             color="#ddd", fontsize=9, ha="center",
             arrowprops=dict(arrowstyle="-", color="#888", lw=0.5))
ax1.annotate(f"IPO ${ipo_price:.0f}", xy=(ipo_date, ipo_price),
             xytext=(ipo_date + pd.Timedelta(days=20), ipo_price + 12),
             color="#ddd", fontsize=9,
             arrowprops=dict(arrowstyle="-", color="#888", lw=0.5))
if may11_price:
    ax1.annotate(f"May 11 ${may11_price:.0f}", xy=(pd.Timestamp("2026-05-11"), may11_price),
                 xytext=(pd.Timestamp("2026-05-11") - pd.Timedelta(days=70), may11_price + 8),
                 color="#ddd", fontsize=9,
                 arrowprops=dict(arrowstyle="-", color="#888", lw=0.5))
ax1.annotate(f"NAV ${last_nav:.2f}", xy=(nav.iloc[-1]["Date"], last_nav),
             xytext=(nav.iloc[-1]["Date"] + pd.Timedelta(days=10), last_nav - 8),
             color="#f59e0b", fontsize=9,
             arrowprops=dict(arrowstyle="-", color="#888", lw=0.5))
ax1.annotate(f"${last_price:.2f}", xy=(last_date, last_price),
             xytext=(last_date + pd.Timedelta(days=5), last_price),
             color="#3b82f6", fontsize=9, va="center")

ax2.fill_between(px["Date"], premium, 0, color="#d97706", alpha=0.6)
ax2.plot(px["Date"], premium, color="#f59e0b", linewidth=0.8)
ax2.axhline(0, color="#666", linewidth=0.5)
ax2.set_ylabel("Premium to NAV (%)", color="#ddd")
ax2.tick_params(colors="#ccc")
ax2.annotate(f"{prem_peak_val:.0f}%", xy=(prem_peak_date, prem_peak_val),
             xytext=(prem_peak_date + pd.Timedelta(days=8), prem_peak_val - 100),
             color="#f59e0b", fontsize=9)
ax2.annotate(f"{last_premium:.0f}%", xy=(last_date, last_premium),
             xytext=(last_date + pd.Timedelta(days=5), last_premium),
             color="#f59e0b", fontsize=9, va="center")

ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax2.get_xticklabels(), rotation=0, ha="center", color="#ccc")

plt.savefig(OUT, dpi=110, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
print(f"Latest: {last_date.date()} price=${last_price:.2f} NAV=${last_nav:.2f} premium={last_premium:.1f}%")
print(f"Peak price: ${peak_price:.2f} on {peak_date.date()}")
print(f"Peak premium: {prem_peak_val:.1f}% on {prem_peak_date.date()}")
