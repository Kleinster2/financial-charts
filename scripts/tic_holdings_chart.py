"""
TIC Holdings Chart: The Compositional Shift in Foreign Treasury Demand
Visualizes Cayman Islands (hedge fund proxy) vs China vs Japan holdings over time.
Source: US Treasury TIC data from market_data.db
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from pathlib import Path
import sys

DB_PATH = Path(__file__).parent.parent / "market_data.db"
OUTPUT_DIR = Path(__file__).parent.parent / "investing" / "attachments"

def get_holdings(conn, countries):
    """Fetch TIC holdings for specified countries."""
    placeholders = ",".join(["?"] * len(countries))
    query = f"""
        SELECT date, country, holdings_billions
        FROM tic_holdings
        WHERE country IN ({placeholders})
        AND holdings_billions IS NOT NULL
        ORDER BY date
    """
    df = pd.read_sql(query, conn, params=countries)
    df["date"] = pd.to_datetime(df["date"])
    return df.pivot(index="date", columns="country", values="holdings_billions")


def chart_top_holders(conn, output_path):
    """Cayman Islands vs China vs Japan — the compositional shift."""
    countries = ["Cayman Islands", "China, Mainland", "Japan", "United Kingdom"]
    df = get_holdings(conn, countries)
    df = df.rename(columns={"China, Mainland": "China"})

    fig, ax = plt.subplots(figsize=(14, 7))

    colors = {
        "Japan": "#1f77b4",
        "China": "#d62728",
        "United Kingdom": "#7f7f7f",
        "Cayman Islands": "#ff7f0e",
    }

    for col in ["Japan", "United Kingdom", "China", "Cayman Islands"]:
        if col in df.columns:
            series = df[col].dropna()
            lw = 2.8 if col == "Cayman Islands" else 1.8
            ls = "-" if col != "United Kingdom" else "--"
            ax.plot(series.index, series.values, label=col, color=colors[col],
                    linewidth=lw, linestyle=ls)

    # Annotate latest values
    for col in ["Japan", "China", "Cayman Islands"]:
        if col in df.columns:
            last = df[col].dropna().iloc[-1]
            last_date = df[col].dropna().index[-1]
            ax.annotate(f"${last:,.0f}B",
                        xy=(last_date, last),
                        xytext=(12, 0), textcoords="offset points",
                        fontsize=10, fontweight="bold", color=colors[col],
                        va="center")

    # Mark the 2024 data gap for Cayman
    ax.axvspan(pd.Timestamp("2024-01-01"), pd.Timestamp("2024-12-31"),
               alpha=0.06, color="orange", zorder=0)
    ax.text(pd.Timestamp("2024-06-15"), 150, "2024 gap\n(TIC data)",
            fontsize=8, color="#999", ha="center", style="italic")

    ax.set_ylabel("Holdings ($B)", fontsize=12)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}B"))
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    ax.legend(loc="upper left", fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(pd.Timestamp("2012-01-01"), pd.Timestamp("2026-06-01"))

    # Source attribution
    fig.text(0.99, 0.01, "Source: US Treasury TIC data",
             fontsize=8, color="#999", ha="right", style="italic")

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    print(f"Saved: {output_path}")
    plt.close()
    return output_path


def chart_cayman_vs_china_indexed(conn, output_path):
    """Cayman vs China indexed to 100 at Jan 2018 — the divergence."""
    countries = ["Cayman Islands", "China, Mainland"]
    df = get_holdings(conn, countries)
    df = df.rename(columns={"China, Mainland": "China"})

    # Index to Jan 2018
    base_date = pd.Timestamp("2018-01-31")
    for col in df.columns:
        base_val = df.loc[df.index <= base_date, col].dropna().iloc[-1]
        df[col] = (df[col] / base_val) * 100

    fig, ax = plt.subplots(figsize=(14, 5.5))

    ax.plot(df.index, df["Cayman Islands"], color="#ff7f0e", linewidth=2.8,
            label="Cayman Islands (hedge fund proxy)")
    ax.plot(df.index, df["China"], color="#d62728", linewidth=2.8,
            label="China")

    ax.axhline(100, color="#999", linewidth=0.8, linestyle=":")

    # Shade 2024 gap
    ax.axvspan(pd.Timestamp("2024-01-01"), pd.Timestamp("2024-12-31"),
               alpha=0.06, color="orange", zorder=0)

    ax.set_ylabel("Indexed (Jan 2018 = 100)", fontsize=12)
    ax.legend(loc="upper left", fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(pd.Timestamp("2012-01-01"), pd.Timestamp("2026-06-01"))
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    fig.text(0.99, 0.01, "Source: US Treasury TIC data",
             fontsize=8, color="#999", ha="right", style="italic")

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    print(f"Saved: {output_path}")
    plt.close()
    return output_path


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)

    p1 = chart_top_holders(
        conn,
        OUTPUT_DIR / "tic-foreign-treasury-holders-2012-2026.png"
    )
    p2 = chart_cayman_vs_china_indexed(
        conn,
        OUTPUT_DIR / "tic-cayman-vs-china-indexed-2018.png"
    )

    conn.close()
    print("Done.")
