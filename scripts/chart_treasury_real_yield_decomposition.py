#!/usr/bin/env python
"""
Chart Treasury nominal / real-yield / breakeven decomposition from FRED series.

Outputs are saved under investing/attachments and are intended for embedding in
investing/Concepts/Treasuries.md.
"""

import argparse
import json
import sqlite3
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from constants import DB_PATH

ATTACHMENTS = ROOT / "investing" / "attachments"

MOVE_CHART = ATTACHMENTS / "treasury-real-yield-decomposition-may13-19-2026.png"

LW_CHARTS = [
    (
        ATTACHMENTS / "treasury-5y-real-yield-decomposition-lw.png",
        {
            "tickers": "DGS5,DFII5,T5YIE",
            "start": "2026-01-01",
            "normalize": "false",
            "log_y": "false",
            "labels": "DGS5:5Y nominal,DFII5:5Y real yield,T5YIE:5Y breakeven",
            "width": "1200",
            "height": "650",
            "show_last_value": "true",
            "show_last_date": "false",
        },
    ),
    (
        ATTACHMENTS / "treasury-10y-real-yield-decomposition-lw.png",
        {
            "tickers": "DGS10,DFII10,T10YIE",
            "start": "2026-01-01",
            "normalize": "false",
            "log_y": "false",
            "labels": "DGS10:10Y nominal,DFII10:10Y real yield,T10YIE:10Y breakeven",
            "width": "1200",
            "height": "650",
            "show_last_value": "true",
            "show_last_date": "false",
        },
    ),
    (
        ATTACHMENTS / "treasury-30y-real-yield-decomposition-lw.png",
        {
            "tickers": "DGS30,DFII30",
            "start": "2026-01-01",
            "normalize": "false",
            "log_y": "false",
            "labels": "DGS30:30Y nominal,DFII30:30Y real yield",
            "width": "1200",
            "height": "650",
            "show_last_value": "true",
            "show_last_date": "false",
        },
    ),
]

SERIES = {
    "DGS5": "5Y nominal",
    "DFII5": "5Y real yield",
    "T5YIE": "5Y breakeven",
    "DGS10": "10Y nominal",
    "DFII10": "10Y real yield",
    "T10YIE": "10Y breakeven",
    "DGS30": "30Y nominal",
    "DFII30": "30Y real yield",
}


def require_nonexistent(path: Path, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists; pass --force to overwrite")


def load_series(start: str) -> pd.DataFrame:
    codes = list(SERIES)
    placeholders = ",".join("?" for _ in codes)
    query = f"""
        SELECT Date, Ticker, Close
        FROM prices_long
        WHERE Ticker IN ({placeholders}) AND Date >= ?
        ORDER BY Date, Ticker
    """
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql(query, conn, params=codes + [start])

    if df.empty:
        raise RuntimeError("No decomposition data found in prices_long")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.normalize()
    df = df.dropna(subset=["Date", "Close"])
    wide = df.pivot_table(index="Date", columns="Ticker", values="Close", aggfunc="last")

    missing = [code for code in codes if code not in wide.columns or wide[code].dropna().empty]
    if missing:
        raise RuntimeError(f"Missing required series in prices_long: {', '.join(missing)}")

    wide["T30Y_RESIDUAL"] = wide["DGS30"] - wide["DFII30"]
    return wide


def plot_move(df: pd.DataFrame, output: Path, force: bool) -> None:
    require_nonexistent(output, force)

    move_start = pd.Timestamp("2026-05-13")
    move_end = pd.Timestamp("2026-05-19")
    window = df.loc[move_start:move_end].copy()

    rows = []
    for tenor, nominal, real, breakeven in [
        ("5Y", "DGS5", "DFII5", "T5YIE"),
        ("10Y", "DGS10", "DFII10", "T10YIE"),
        ("30Y", "DGS30", "DFII30", "T30Y_RESIDUAL"),
    ]:
        x = window[[nominal, real, breakeven]].dropna()
        if x.empty:
            raise RuntimeError(f"No common May 13-19 window for {tenor}")
        start = x.iloc[0]
        end = x.iloc[-1]
        rows.extend(
            [
                {"Tenor": tenor, "Component": "Nominal", "Move": (end[nominal] - start[nominal]) * 100},
                {"Tenor": tenor, "Component": "Real yield", "Move": (end[real] - start[real]) * 100},
                {"Tenor": tenor, "Component": "Breakeven / residual", "Move": (end[breakeven] - start[breakeven]) * 100},
            ]
        )

    moves = pd.DataFrame(rows)
    components = ["Nominal", "Real yield", "Breakeven / residual"]
    colors = {"Nominal": "#223b7b", "Real yield": "#b33a3a", "Breakeven / residual": "#2b7a4b"}

    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    fig.patch.set_facecolor("white")
    x_base = range(len(moves["Tenor"].unique()))
    width = 0.24

    for i, component in enumerate(components):
        values = [
            moves[(moves["Tenor"] == tenor) & (moves["Component"] == component)]["Move"].iloc[0]
            for tenor in ["5Y", "10Y", "30Y"]
        ]
        xs = [x + (i - 1) * width for x in x_base]
        bars = ax.bar(xs, values, width=width, label=component, color=colors[component])
        for bar, value in zip(bars, values):
            va = "bottom" if value >= 0 else "top"
            offset = 0.7 if value >= 0 else -0.7
            ax.text(bar.get_x() + bar.get_width() / 2, value + offset, f"{value:.0f}", ha="center", va=va, fontsize=9)

    ax.axhline(0, color="#111827", linewidth=0.9)
    ax.set_xticks(list(x_base), ["5Y", "10Y", "30Y"])
    ax.set_ylabel("bp move")
    ax.set_title("May 13-19, 2026: Selloff Was Mostly Real Yields", loc="left", fontsize=14, fontweight="bold")
    ax.set_ylim(-6, 30)
    ax.grid(True, axis="y", color="#d9dee7", linewidth=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper right", frameon=False, ncol=3)
    fig.text(0.05, 0.015, "Source: FRED via local market_data.db. 30Y residual = DGS30 - DFII30.", fontsize=9, color="#4b5563")
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)


def render_lw_charts(force: bool) -> None:
    charting_app_path = ROOT / "charting_app"
    sys.path.insert(0, str(charting_app_path))

    from app import app

    with app.test_client() as client:
        for output, params in LW_CHARTS:
            require_nonexistent(output, force)
            response = client.get("/api/chart/lw", query_string=params)
            if response.status_code != 200:
                body = response.get_data(as_text=True)[:500]
                raise RuntimeError(f"Lightweight chart failed for {output.name}: {response.status_code} {body}")

            data = response.data
            if len(data) < 1000 or not data.startswith(b"\x89PNG"):
                preview = data[:80]
                raise RuntimeError(
                    f"Lightweight chart returned invalid PNG for {output.name}: "
                    f"{len(data)} bytes, prefix={json.dumps(preview.decode('latin1', errors='ignore'))}"
                )

            output.write_bytes(data)
            print(f"Wrote {output}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create Treasury real-yield decomposition charts")
    parser.add_argument("--start", default="2026-01-01", help="Start date for level chart")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output files")
    args = parser.parse_args()

    ATTACHMENTS.mkdir(parents=True, exist_ok=True)
    df = load_series(args.start)
    render_lw_charts(force=args.force)
    plot_move(df, MOVE_CHART, force=args.force)

    print(f"Wrote {MOVE_CHART}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
