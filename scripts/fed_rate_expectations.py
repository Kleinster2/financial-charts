#!/usr/bin/env python3
"""
Fed Funds rate expectations from futures markets.

Downloads ZQ (30-day Fed Funds futures) and SR3 (3-month SOFR futures) to build
the market-implied policy rate path. Shows what traders expect the Fed to do.

Modes:
    snapshot  — Current implied rate path (default)
    history   — How the Dec 2026 implied rate has shifted over time
    fomc      — Implied probability of cut/hold at each FOMC meeting

Usage:
    python scripts/fed_rate_expectations.py                    # snapshot
    python scripts/fed_rate_expectations.py --mode history     # shifting expectations
    python scripts/fed_rate_expectations.py --mode fomc        # meeting probabilities
    python scripts/fed_rate_expectations.py --table            # print data table only
"""
import argparse
import os
import sys
from datetime import datetime, date

# Force UTF-8 on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import logging
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
import yfinance as yf

# Suppress noisy yfinance 404 warnings for non-existent contracts
logging.getLogger("yfinance").setLevel(logging.CRITICAL)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "investing", "attachments")

MONTH_CODES = {
    'F': (1, 'Jan'), 'G': (2, 'Feb'), 'H': (3, 'Mar'), 'J': (4, 'Apr'),
    'K': (5, 'May'), 'M': (6, 'Jun'), 'N': (7, 'Jul'), 'Q': (8, 'Aug'),
    'U': (9, 'Sep'), 'V': (10, 'Oct'), 'X': (11, 'Nov'), 'Z': (12, 'Dec')
}
CODE_ORDER = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']

# FOMC meeting dates (decision day = day 2)
# Update annually from federalreserve.gov
FOMC_DATES = {
    2026: [
        date(2026, 1, 29), date(2026, 3, 18), date(2026, 5, 6),
        date(2026, 6, 17), date(2026, 7, 29), date(2026, 9, 16),
        date(2026, 10, 28), date(2026, 12, 16),
    ],
    2027: [
        date(2027, 1, 27), date(2027, 3, 17), date(2027, 5, 5),
        date(2027, 6, 16), date(2027, 7, 28), date(2027, 9, 22),
        date(2027, 10, 27), date(2027, 12, 15),
    ],
}


def get_current_target_range():
    """Fetch current Fed Funds target range from local database (FRED data)."""
    try:
        db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                "market_data.db")
        import sqlite3
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(
            "SELECT DFEDTARU, DFEDTARL FROM stock_prices_daily "
            "WHERE DFEDTARU IS NOT NULL ORDER BY Date DESC LIMIT 1"
        )
        row = cur.fetchone()
        conn.close()
        if row:
            return float(row[0]), float(row[1])  # upper, lower
    except Exception:
        pass
    return None, None


def download_zq_curve():
    """Download all available ZQ (30-day Fed Funds) futures contracts.
    Returns DataFrame with columns: contract, month_num, year, label, price, implied_rate
    """
    now = datetime.now()
    results = []

    for yr in range(now.year, now.year + 3):
        yr_short = yr % 100
        for code in CODE_ORDER:
            month_num, month_name = MONTH_CODES[code]
            # Skip expired contracts
            if yr == now.year and month_num < now.month:
                continue

            sym = f"ZQ{code}{yr_short:02d}.CBT"
            try:
                t = yf.Ticker(sym)
                hist = t.history(period="5d")
                if hist.empty:
                    continue
                price = float(hist["Close"].iloc[-1])
                implied = 100.0 - price
                label = f"{month_name} {yr}"
                contract_date = date(yr, month_num, 15)  # mid-month proxy
                results.append({
                    "contract": sym,
                    "month_num": month_num,
                    "year": yr,
                    "label": label,
                    "date": contract_date,
                    "price": price,
                    "implied_rate": implied,
                })
            except Exception:
                continue

    df = pd.DataFrame(results)
    if not df.empty:
        df = df.sort_values("date").reset_index(drop=True)
    return df


def download_sr3_curve():
    """Download SR3 (3-month SOFR) futures for longer-dated expectations."""
    now = datetime.now()
    results = []

    for yr in range(now.year, now.year + 3):
        yr_short = yr % 100
        for code in CODE_ORDER:
            month_num, month_name = MONTH_CODES[code]
            if yr == now.year and month_num < now.month:
                continue

            sym = f"SR3{code}{yr_short:02d}.CME"
            try:
                t = yf.Ticker(sym)
                hist = t.history(period="5d")
                if hist.empty:
                    continue
                price = float(hist["Close"].iloc[-1])
                implied = 100.0 - price
                label = f"{month_name} {yr}"
                contract_date = date(yr, month_num, 15)
                results.append({
                    "contract": sym,
                    "label": label,
                    "date": contract_date,
                    "price": price,
                    "implied_rate": implied,
                })
            except Exception:
                continue

    df = pd.DataFrame(results)
    if not df.empty:
        df = df.sort_values("date").reset_index(drop=True)
    return df


def download_zq_history(contract_sym, period="6mo"):
    """Download historical prices for a single ZQ contract to track shifting expectations."""
    try:
        t = yf.Ticker(contract_sym)
        hist = t.history(period=period)
        if hist.empty:
            return None
        hist["implied_rate"] = 100.0 - hist["Close"]
        return hist[["Close", "implied_rate"]]
    except Exception:
        return None


def calc_fomc_probabilities(zq_df):
    """
    Calculate implied probability of a 25bp cut at each FOMC meeting.

    Logic: If the ZQ contract for the month AFTER a meeting implies a lower rate
    than the month before, the difference ÷ 0.25 gives the probability of a cut.
    """
    if zq_df.empty:
        return []

    results = []
    rate_by_month = {}
    for _, row in zq_df.iterrows():
        key = (row["year"], row["month_num"])
        rate_by_month[key] = row["implied_rate"]

    for yr, meetings in sorted(FOMC_DATES.items()):
        for meeting_date in meetings:
            m = meeting_date.month
            y = meeting_date.year
            day = meeting_date.day

            # Rate before meeting: prior month's ZQ, or same month if meeting is late
            pre_key = (y, m - 1) if m > 1 else (y - 1, 12)
            post_key = (y, m)

            # If meeting is in first week, pre-meeting rate is from 2 months prior
            # because current month ZQ already reflects the decision
            if day <= 7:
                pre_key = (y, m - 1) if m > 1 else (y - 1, 12)
                post_key = (y, m)
            else:
                # Meeting later in month: same-month ZQ is mix of pre/post
                # Use month-before as pre, month-after as post for cleaner signal
                pre_key = (y, m)
                next_m = m + 1 if m < 12 else 1
                next_y = y if m < 12 else y + 1
                post_key = (next_y, next_m)

            pre_rate = rate_by_month.get(pre_key)
            post_rate = rate_by_month.get(post_key)

            if pre_rate is not None and post_rate is not None:
                rate_change = pre_rate - post_rate  # positive = cut
                prob_cut = min(max(rate_change / 0.25, 0), 1.0)
                implied_post = post_rate
            elif post_rate is not None:
                # Use front month as pre-rate proxy
                front = zq_df.iloc[0]["implied_rate"]
                rate_change = front - post_rate
                prob_cut = min(max(rate_change / 0.25, 0), 1.0)
                implied_post = post_rate
            else:
                continue

            results.append({
                "meeting": meeting_date,
                "label": meeting_date.strftime("%b %d, %Y"),
                "pre_rate": pre_rate or zq_df.iloc[0]["implied_rate"],
                "post_rate": post_rate,
                "change_bps": rate_change * 100,
                "prob_cut_25bp": prob_cut,
            })

    return results


def plot_snapshot(zq_df, sr3_df, output_path):
    """Plot current implied rate path from ZQ and SR3 futures."""
    fig, ax = plt.subplots(figsize=(14, 6))

    # Current effective rate (front ZQ contract)
    current_rate = zq_df.iloc[0]["implied_rate"] if not zq_df.empty else None

    # Plot ZQ implied rates
    if not zq_df.empty:
        dates = pd.to_datetime(zq_df["date"])
        ax.plot(dates, zq_df["implied_rate"], color="#2962FF", linewidth=2.5,
                marker="o", markersize=6, label="Fed Funds futures (ZQ)", zorder=5)

        # Annotate first and last
        ax.annotate(f'{zq_df.iloc[0]["implied_rate"]:.2f}%',
                     xy=(dates.iloc[0], zq_df.iloc[0]["implied_rate"]),
                     xytext=(0, 12), textcoords="offset points",
                     fontsize=9, fontweight="bold", color="#2962FF", ha="center")
        ax.annotate(f'{zq_df.iloc[-1]["implied_rate"]:.2f}%',
                     xy=(dates.iloc[-1], zq_df.iloc[-1]["implied_rate"]),
                     xytext=(0, 12), textcoords="offset points",
                     fontsize=9, fontweight="bold", color="#2962FF", ha="center")

    # Plot SR3 implied rates (lighter, dashed)
    if not sr3_df.empty:
        dates_sr3 = pd.to_datetime(sr3_df["date"])
        ax.plot(dates_sr3, sr3_df["implied_rate"], color="#FF6D00", linewidth=1.5,
                marker="s", markersize=4, linestyle="--", alpha=0.7,
                label="3M SOFR futures (SR3)")

    # FOMC meeting dates as vertical lines
    for yr, meetings in FOMC_DATES.items():
        for i, md in enumerate(meetings):
            md_ts = pd.Timestamp(md)
            if not zq_df.empty:
                min_date = pd.Timestamp(zq_df["date"].min())
                max_date = pd.Timestamp(zq_df["date"].max())
                if min_date <= md_ts <= max_date:
                    ax.axvline(md_ts, color="#E0E0E0", linewidth=0.8,
                               linestyle=":", zorder=1)
                    if i == 0:  # label only first per year
                        ax.text(md_ts, ax.get_ylim()[1], "FOMC", fontsize=7,
                                color="#999", ha="center", va="bottom", rotation=90)

    # Current target range band from database
    upper_target, lower_target = get_current_target_range()
    if upper_target is not None:
        ax.axhspan(lower_target, upper_target, alpha=0.08, color="#2962FF",
                    label=f"Current target range ({lower_target:.2f}%\u2013{upper_target:.2f}%)")
    elif current_rate is not None:
        # Fallback: approximate from effective rate
        mid = round(current_rate * 4) / 4
        ax.axhspan(mid - 0.125, mid + 0.125, alpha=0.08, color="#2962FF",
                    label=f"Approx target range")

    ax.set_ylabel("Implied Rate (%)", fontsize=12)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))
    ax.legend(fontsize=10, loc="upper right")
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # Calculate total implied cuts
    if current_rate and not zq_df.empty:
        terminal = zq_df.iloc[-1]["implied_rate"]
        total_cuts_bp = (current_rate - terminal) * 100
        n_cuts = total_cuts_bp / 25
        subtitle = (f"Market pricing {total_cuts_bp:.0f}bp of easing "
                     f"(~{n_cuts:.1f} cuts) by {zq_df.iloc[-1]['label']}")
        ax.set_title(subtitle, fontsize=10, color="#666", style="italic", pad=8)

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {output_path} ({os.path.getsize(output_path):,} bytes)")


def plot_history(contract_sym, label, output_path, period="6mo"):
    """Plot how a single contract's implied rate has shifted over time."""
    hist = download_zq_history(contract_sym, period=period)
    if hist is None or hist.empty:
        print(f"No history for {contract_sym}")
        return

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(hist.index, hist["implied_rate"], color="#2962FF", linewidth=2)
    ax.fill_between(hist.index, hist["implied_rate"].min() - 0.05,
                     hist["implied_rate"], alpha=0.1, color="#2962FF")

    # Annotate endpoints
    ax.annotate(f'{hist["implied_rate"].iloc[0]:.3f}%',
                 xy=(hist.index[0], hist["implied_rate"].iloc[0]),
                 xytext=(10, 10), textcoords="offset points",
                 fontsize=9, color="#2962FF")
    ax.annotate(f'{hist["implied_rate"].iloc[-1]:.3f}%',
                 xy=(hist.index[-1], hist["implied_rate"].iloc[-1]),
                 xytext=(-10, 10), textcoords="offset points",
                 fontsize=9, fontweight="bold", color="#2962FF", ha="right")

    ax.set_ylabel("Implied Rate (%)", fontsize=12)
    ax.set_title(f"Market-implied rate for {label} (shifting expectations)",
                  fontsize=10, color="#666", style="italic")
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.3f'))
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
    fig.autofmt_xdate()

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {output_path} ({os.path.getsize(output_path):,} bytes)")


def plot_fomc_probabilities(probs, output_path):
    """Bar chart of implied cut probability at each FOMC meeting."""
    if not probs:
        print("No FOMC probability data")
        return

    fig, ax = plt.subplots(figsize=(14, 5))

    labels = [p["label"] for p in probs]
    cut_probs = [p["prob_cut_25bp"] * 100 for p in probs]
    colors = ["#43A047" if p > 50 else "#FF9800" if p > 25 else "#E53935"
              for p in cut_probs]

    bars = ax.bar(range(len(labels)), cut_probs, color=colors, alpha=0.85, width=0.6)

    # Label each bar
    for bar, prob in zip(bars, cut_probs):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                f"{prob:.0f}%", ha="center", va="bottom", fontsize=9, fontweight="bold")

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=9)
    ax.set_ylabel("Probability of 25bp cut (%)", fontsize=11)
    ax.set_ylim(0, 110)
    ax.axhline(50, color="#999", linewidth=0.8, linestyle="--", alpha=0.5)
    ax.grid(True, alpha=0.2, axis="y")

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#43A047", alpha=0.85, label=">50% — cut likely"),
        Patch(facecolor="#FF9800", alpha=0.85, label="25-50% — toss-up"),
        Patch(facecolor="#E53935", alpha=0.85, label="<25% — hold likely"),
    ]
    ax.legend(handles=legend_elements, fontsize=9, loc="upper right")

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {output_path} ({os.path.getsize(output_path):,} bytes)")


def print_table(zq_df, fomc_probs=None):
    """Print a formatted table of the rate curve."""
    print("\n" + "=" * 70)
    print("FED FUNDS FUTURES — IMPLIED RATE PATH")
    print("=" * 70)

    if not zq_df.empty:
        current = zq_df.iloc[0]["implied_rate"]
        print(f"\nCurrent implied effective rate: {current:.4f}%")
        upper_t, lower_t = get_current_target_range()
        if upper_t is not None:
            print(f"Current target range: {lower_t:.2f}% - {upper_t:.2f}%\n")
        else:
            mid = round(current * 4) / 4
            print(f"Approximate target range: {mid - 0.125:.3f}% - {mid + 0.125:.3f}%\n")

        print(f"{'Contract':<16} {'Month':<12} {'Price':>8} {'Implied':>8} {'Δ from now':>10}")
        print("-" * 58)
        for _, row in zq_df.iterrows():
            delta = (row["implied_rate"] - current) * 100
            print(f"{row['contract']:<16} {row['label']:<12} {row['price']:>8.4f} "
                  f"{row['implied_rate']:>7.4f}% {delta:>+9.1f}bp")

        terminal = zq_df.iloc[-1]["implied_rate"]
        total_bp = (current - terminal) * 100
        print(f"\nTotal implied easing: {total_bp:.0f}bp (~{total_bp/25:.1f} cuts of 25bp)")
        print(f"Terminal rate: {terminal:.4f}% by {zq_df.iloc[-1]['label']}")

    if fomc_probs:
        print("\n" + "=" * 70)
        print("FOMC MEETING PROBABILITIES")
        print("=" * 70)
        print(f"\n{'Meeting':<16} {'Pre-rate':>8} {'Post-rate':>9} {'Δ bps':>7} {'P(cut)':>8}")
        print("-" * 52)
        cumulative_cuts = 0
        for p in fomc_probs:
            cumulative_cuts += p["change_bps"]
            marker = "*" if p["prob_cut_25bp"] > 0.5 else " "
            print(f"{p['label']:<16} {p['pre_rate']:>7.3f}% {p['post_rate']:>8.3f}% "
                  f"{p['change_bps']:>+6.1f} {p['prob_cut_25bp']*100:>6.0f}% {marker}")
        print(f"\nCumulative implied cuts: {cumulative_cuts:.0f}bp")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Fed Funds rate expectations from futures markets")
    parser.add_argument("--mode", choices=["snapshot", "history", "fomc"],
                         default="snapshot",
                         help="snapshot=current curve, history=shifting expectations, "
                              "fomc=meeting probabilities")
    parser.add_argument("--table", action="store_true",
                         help="Print data table (all modes)")
    parser.add_argument("--no-chart", action="store_true",
                         help="Skip chart generation")
    parser.add_argument("--history-contract", default=None,
                         help="ZQ contract for history mode (e.g. ZQZ26.CBT for Dec 2026)")
    parser.add_argument("--history-period", default="6mo",
                         help="Lookback for history mode (default: 6mo)")
    parser.add_argument("--output", default=None,
                         help="Custom output path for chart")
    args = parser.parse_args()

    print("Downloading Fed Funds futures curve...")
    zq_df = download_zq_curve()

    if zq_df.empty:
        print("ERROR: No ZQ data downloaded. Check network/yfinance.")
        sys.exit(1)

    print(f"Got {len(zq_df)} ZQ contracts: {zq_df.iloc[0]['label']} -> {zq_df.iloc[-1]['label']}")

    fomc_probs = calc_fomc_probabilities(zq_df)

    if args.table or args.mode in ("snapshot", "fomc"):
        print_table(zq_df, fomc_probs if args.mode == "fomc" or args.table else None)

    if args.no_chart:
        return

    if args.mode == "snapshot":
        print("\nDownloading SOFR futures for extended curve...")
        sr3_df = download_sr3_curve()
        print(f"Got {len(sr3_df)} SR3 contracts")

        out = args.output or os.path.join(OUTPUT_DIR, "fed-rate-expectations.png")
        plot_snapshot(zq_df, sr3_df, out)

    elif args.mode == "history":
        contract = args.history_contract
        if not contract:
            # Default: Dec of current year or next year
            now = datetime.now()
            yr = now.year if now.month <= 6 else now.year + 1
            contract = f"ZQZ{yr % 100:02d}.CBT"
        label = contract.replace(".CBT", "")
        out = args.output or os.path.join(OUTPUT_DIR, "fed-rate-history.png")
        plot_history(contract, label, out, period=args.history_period)

    elif args.mode == "fomc":
        out = args.output or os.path.join(OUTPUT_DIR, "fed-fomc-probabilities.png")
        plot_fomc_probabilities(fomc_probs, out)


if __name__ == "__main__":
    main()
