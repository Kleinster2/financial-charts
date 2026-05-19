#!/usr/bin/env python3
"""
Plot USD share of allocated FX reserves (IMF COFER, end-of-Q4 annual).

Series starts 2014 — IMF began separately reporting China's reserves that year,
which produces a cleaner methodology break from the pre-2014 series.

Data source: IMF Currency Composition of Official Foreign Exchange Reserves
(COFER) press releases. Q4 2025 figure cross-referenced against the IMF data
release dated 26 March 2026 (also published at coferdata.com).
"""
from __future__ import annotations

import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT = REPO_ROOT / "investing" / "attachments" / "usd-reserve-share-cofer.png"

# End-of-Q4 USD share of allocated FX reserves (%), IMF COFER releases.
SERIES = [
    (2014, 65.1),
    (2015, 65.7),
    (2016, 65.4),
    (2017, 62.7),
    (2018, 61.7),
    (2019, 60.7),
    (2020, 58.9),
    (2021, 58.8),
    (2022, 58.4),
    (2023, 58.4),
    (2024, 57.4),
    (2025, 56.77),
]

# Annotated events (year, label)
ANNOTATIONS = [
    (2022, "Russia reserve freeze\n(Feb 2022)"),
]


def build_chart(out_path: Path) -> None:
    years = [r[0] for r in SERIES]
    vals = [r[1] for r in SERIES]

    fig, ax = plt.subplots(figsize=(11, 6))

    ax.plot(years, vals, color="#1E88E5", linewidth=2.4, marker="o",
            markersize=6, zorder=5)

    # Endpoint annotations (first + last)
    ax.annotate(f"{vals[0]:.1f}%", xy=(years[0], vals[0]),
                xytext=(-10, 10), textcoords="offset points",
                fontsize=10, color="#1E88E5", fontweight="bold")
    ax.annotate(f"{vals[-1]:.2f}%", xy=(years[-1], vals[-1]),
                xytext=(8, -2), textcoords="offset points",
                fontsize=11, color="#1E88E5", fontweight="bold")

    # Annotate the 2022 Russia reserve freeze
    y_top = max(vals) + 0.5
    for ann_year, ann_label in ANNOTATIONS:
        ax.axvline(ann_year, color="#888", linewidth=1.0, linestyle="--",
                   alpha=0.7, zorder=2)
        ax.text(ann_year + 0.1, y_top, ann_label, fontsize=9, color="#555",
                ha="left", va="top", zorder=3)

    # Net change box
    net_pp = vals[-1] - vals[0]
    ax.text(0.02, 0.06,
            f"{years[0]} → {years[-1]}: {net_pp:+.1f} pp",
            transform=ax.transAxes, fontsize=10, color="#333",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor="#ccc", alpha=0.9))

    ax.set_ylabel("USD share of allocated FX reserves (%)", fontsize=11)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
    ax.set_ylim(55, 67)
    ax.set_xlim(years[0] - 0.5, years[-1] + 0.5)
    ax.grid(True, alpha=0.3)

    # Footer caption
    fig.text(0.5, 0.01,
             "Source: IMF Currency Composition of Official Foreign Exchange "
             "Reserves (COFER), end-of-Q4 values",
             fontsize=8.5, color="#666", ha="center", style="italic")

    plt.tight_layout(rect=(0, 0.03, 1, 1))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out_path} ({out_path.stat().st_size:,} bytes)")

    # Summary table
    print()
    print(f"{'Year':<6}{'USD share':>12}{'YoY Δ':>10}")
    print("-" * 28)
    prev = None
    for y, v in SERIES:
        delta = "" if prev is None else f"{v - prev:+.1f}"
        print(f"{y:<6}{v:>10.2f}%{delta:>10}")
        prev = v


if __name__ == "__main__":
    build_chart(OUT)
