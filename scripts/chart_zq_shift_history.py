#!/usr/bin/env python3
"""
Plot multi-contract ZQ implied-rate shift history.

Reads from market_data.db `rate_futures_daily` table (populated by
`scripts/update_rate_futures.py`) and produces a chart showing how several
chosen ZQ contracts' implied rates have evolved over time. The point of this
chart is to make the "same contract, different rate at different times" idea
visual — what does the strip not show you that the per-contract history does.

Usage:
    python scripts/chart_zq_shift_history.py
    python scripts/chart_zq_shift_history.py --contracts ZQZ26.CBT ZQM27.CBT ZQZ27.CBT
    python scripts/chart_zq_shift_history.py --annotate-date 2026-05-12 --annotate-label "Apr CPI 3.8%"
    python scripts/chart_zq_shift_history.py --output investing/attachments/zq-shift-custom.png
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import date, datetime
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = REPO_ROOT / "market_data.db"
DEFAULT_OUT = REPO_ROOT / "investing" / "attachments" / "zq-multi-contract-shift-history.png"

# Sequential blue→orange→green palette (near→mid→far term)
DEFAULT_COLORS = ["#1E88E5", "#FB8C00", "#43A047", "#8E24AA", "#5C6BC0", "#00897B"]

DEFAULT_CONTRACTS = ["ZQZ26.CBT", "ZQM27.CBT", "ZQZ27.CBT"]

# Key dated events worth annotating by default (extend as the vault accumulates them)
DEFAULT_ANNOTATIONS = [
    ("2026-05-12", "Apr CPI 3.8% YoY"),
]


def load_series(conn: sqlite3.Connection, contract: str) -> pd.DataFrame:
    df = pd.read_sql_query(
        """
        SELECT Date, implied_rate
          FROM rate_futures_daily
         WHERE contract = ?
         ORDER BY Date
        """,
        conn,
        params=[contract],
    )
    if df.empty:
        return df
    df["Date"] = pd.to_datetime(df["Date"])
    return df.set_index("Date")


def label_for(contract: str) -> str:
    """Human label, e.g. ZQZ26.CBT → 'Dec 2026 (ZQZ26)'."""
    if not contract.startswith("ZQ"):
        return contract
    code_to_name = {
        "F": "Jan", "G": "Feb", "H": "Mar", "J": "Apr", "K": "May", "M": "Jun",
        "N": "Jul", "Q": "Aug", "U": "Sep", "V": "Oct", "X": "Nov", "Z": "Dec",
    }
    code = contract[2]
    yy = contract[3:5]
    return f"{code_to_name.get(code, code)} 20{yy} ({contract[:5]})"


def build_chart(
    contracts: list[str],
    annotations: list[tuple[str, str]],
    output_path: Path,
) -> None:
    conn = sqlite3.connect(DB_PATH)
    series = {c: load_series(conn, c) for c in contracts}
    conn.close()

    series = {c: df for c, df in series.items() if not df.empty}
    if not series:
        print(f"ERROR: no data in rate_futures_daily for {contracts}")
        sys.exit(1)

    fig, ax = plt.subplots(figsize=(14, 6))

    summary_rows = []
    for (contract, df), color in zip(series.items(), DEFAULT_COLORS):
        label = label_for(contract)
        ax.plot(df.index, df["implied_rate"], color=color, linewidth=2.0,
                label=label, zorder=5)
        # Endpoint annotation (last value)
        last_x = df.index[-1]
        last_y = float(df["implied_rate"].iloc[-1])
        ax.annotate(
            f"{last_y:.2f}%",
            xy=(last_x, last_y),
            xytext=(8, 0),
            textcoords="offset points",
            fontsize=9,
            fontweight="bold",
            color=color,
            va="center",
        )

        first_y = float(df["implied_rate"].iloc[0])
        peak_y = float(df["implied_rate"].max())
        trough_y = float(df["implied_rate"].min())
        peak_d = df["implied_rate"].idxmax().strftime("%Y-%m-%d")
        trough_d = df["implied_rate"].idxmin().strftime("%Y-%m-%d")
        net_bp = (last_y - first_y) * 100
        summary_rows.append({
            "contract": contract,
            "label": label,
            "obs": len(df),
            "first": df.index[0].strftime("%Y-%m-%d"),
            "first_rate": first_y,
            "last": df.index[-1].strftime("%Y-%m-%d"),
            "last_rate": last_y,
            "peak_rate": peak_y, "peak_date": peak_d,
            "trough_rate": trough_y, "trough_date": trough_d,
            "net_bp": net_bp,
        })

    # Event annotations (vertical dashed line + label at top)
    y_top = ax.get_ylim()[1]
    for ann_date, ann_label in annotations:
        try:
            d = pd.Timestamp(ann_date)
        except Exception:
            continue
        ax.axvline(d, color="#888", linewidth=1.0, linestyle="--", alpha=0.7, zorder=2)
        ax.text(
            d, y_top, f"  {ann_label}",
            fontsize=8.5, color="#555",
            ha="left", va="top", rotation=90,
            zorder=3,
        )

    ax.set_ylabel("Implied rate (%)", fontsize=12)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.2f"))
    ax.legend(fontsize=10, loc="lower left", frameon=True, framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {output_path} ({output_path.stat().st_size:,} bytes)")
    print()

    # Print a summary table for embedding alongside the chart
    print(f"{'Contract':<20}{'Obs':>5}{'First':>13}{'First rate':>12}"
          f"{'Last':>13}{'Last rate':>11}{'Peak':>9}{'Trough':>9}{'Net':>8}")
    print("-" * 100)
    for r in summary_rows:
        print(f"{r['label']:<20}{r['obs']:>5}"
              f"  {r['first']:<10}{r['first_rate']:>11.4f}%"
              f"  {r['last']:<10}{r['last_rate']:>10.4f}%"
              f"  {r['peak_rate']:>7.3f}%  {r['trough_rate']:>6.3f}%"
              f"  {r['net_bp']:>+5.0f}bp")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Multi-contract ZQ shift-history chart")
    p.add_argument("--contracts", nargs="+", default=DEFAULT_CONTRACTS,
                   help="ZQ contracts to plot (default: ZQZ26 ZQM27 ZQZ27)")
    p.add_argument("--annotate-date", action="append", default=[],
                   help="Add a vertical line at YYYY-MM-DD (repeatable)")
    p.add_argument("--annotate-label", action="append", default=[],
                   help="Label for each annotate-date (repeatable, must pair)")
    p.add_argument("--output", default=str(DEFAULT_OUT),
                   help=f"Output path (default {DEFAULT_OUT})")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    # Pair user annotations; fall back to DEFAULT_ANNOTATIONS if none given
    if args.annotate_date or args.annotate_label:
        annotations = list(zip(args.annotate_date, args.annotate_label))
    else:
        annotations = DEFAULT_ANNOTATIONS
    build_chart(
        contracts=args.contracts,
        annotations=annotations,
        output_path=Path(args.output),
    )


if __name__ == "__main__":
    main()
