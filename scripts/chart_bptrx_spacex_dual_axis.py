"""Generate bptrx-spacex-dual-axis.png — BPTRX NAV (right, log) vs SpaceX private price (left, log).

Uses standalone matplotlib because LW Charts dual-axis log mode is broken
(see docs/chart-api.md "Known limitations").
"""
import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

DB = Path(r"C:\Users\klein\financial-charts\market_data.db")
OUT = Path(r"C:\Users\klein\financial-charts\investing\attachments\bptrx-spacex-dual-axis.png")

with sqlite3.connect(DB) as c:
    bptrx = pd.read_sql_query(
        "SELECT Date, Close FROM prices_long WHERE Ticker='BPTRX' AND Date >= '2002-01-01' ORDER BY Date",
        c, parse_dates=["Date"],
    )
    spacex = pd.read_sql_query(
        "SELECT Date, Close FROM prices_long WHERE Ticker='SPACEX_PRIVATE' ORDER BY Date",
        c, parse_dates=["Date"],
    )

fig, ax_spacex = plt.subplots(figsize=(13, 7))
ax_bptrx = ax_spacex.twinx()

color_spacex = "#dc2867"
color_bptrx  = "#3b82f6"

ax_bptrx.plot(bptrx["Date"], bptrx["Close"], color=color_bptrx, linewidth=0.9, label="BPTRX")
ax_spacex.plot(spacex["Date"], spacex["Close"], color=color_spacex, linewidth=2.4, label="SpaceX (private)")

ax_bptrx.set_yscale("log")
ax_spacex.set_yscale("log")

ax_spacex.set_ylabel("SpaceX (private)", color=color_spacex, fontsize=12, fontweight="bold")
ax_bptrx.set_ylabel("BPTRX", color=color_bptrx, fontsize=12, fontweight="bold")
ax_spacex.tick_params(axis="y", labelcolor=color_spacex)
ax_bptrx.tick_params(axis="y", labelcolor=color_bptrx)

ax_spacex.set_yticks([0.1, 0.5, 1, 5, 10, 50, 100, 500])
ax_spacex.set_yticklabels(["$0.10", "$0.50", "$1", "$5", "$10", "$50", "$100", "$500"])
ax_bptrx.set_yticks([3, 7, 15, 30, 60, 120, 250])
ax_bptrx.set_yticklabels(["$3", "$7", "$15", "$30", "$60", "$120", "$250"])

ax_spacex.grid(True, alpha=0.3)
ax_spacex.xaxis.set_major_locator(mdates.YearLocator(3))
ax_spacex.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

lines = [
    plt.Line2D([0], [0], color=color_bptrx, lw=0.9, label="BPTRX"),
    plt.Line2D([0], [0], color=color_spacex, lw=2.4, label="SpaceX (private)"),
]
ax_spacex.legend(handles=lines, loc="upper left", fontsize=12, frameon=True)

plt.tight_layout()
plt.savefig(OUT, dpi=110, bbox_inches="tight")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
print(f"BPTRX latest: {bptrx.iloc[-1]['Date'].date()} = ${bptrx.iloc[-1]['Close']:.2f}")
print(f"SpaceX latest: {spacex.iloc[-1]['Date'].date()} = ${spacex.iloc[-1]['Close']:.2f}")
print(f"SpaceX rows: {len(spacex)}")
