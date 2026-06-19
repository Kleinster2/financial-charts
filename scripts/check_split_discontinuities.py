"""Scan tracked price series for un-back-adjusted stock splits.

Why: a freshness check (check_data_freshness.py) asks "is the last close
recent?" — but a series can be perfectly fresh and still wrong. When a stock
splits and an incremental `update_market_data.py --lookback N` appends the
post-split prices onto un-adjusted history, the series gets a single-day
discontinuity at the split ratio. That break silently inverts downstream
analysis: it shows the name as a huge `quick_movers` outlier, pollutes the
random-basket null pool, and can flip a cluster verdict (the WFE quartet
collapsed from intra 0.82 to 0.42 on an un-adjusted KLA 10:1 split, Jun 2026;
earlier the same bug hit a BKNG 25:1 and a 12-series batch). `--lookback N`
structurally cannot back-adjust history for a split inside its window, so every
recent splitter is a latent corruption until a full re-fetch runs. This scan is
the cheap guard that catches it automatically instead of when a verdict breaks.

Signature of an un-adjusted split (vs a genuine crash / meme spike / penny
oscillation): a single-day move at (a) a ratio close to a CLEAN split factor
(2,3,...,10,...) AND (b) a SUSTAINED level shift — the price stays at the new
level rather than reverting. Genuine earnings moves miss (a) (arbitrary ratio);
volatility spikes and penny oscillations miss (b) (the level reverts / never
really shifts). A min-price floor drops sub-$1 penny noise; index symbols (^...)
are skipped (spiking and reverting is their nature).

Universe = vault actor tickers + cluster-config tickers (same as
check_data_freshness.py), intersected with prices_long, minus EXCLUDED_TICKERS
and macro/index series. Pass --all to scan every ticker in prices_long.

Usage:
  python scripts/check_split_discontinuities.py                 # human table
  python scripts/check_split_discontinuities.py --json          # machine-readable
  python scripts/check_split_discontinuities.py --all           # whole DB, not just tracked
  python scripts/check_split_discontinuities.py --window-days 60

Exit code 1 when any LIKELY-SPLIT is found (cron/CI alert-friendly); REVIEW-only
or clean exits 0. Part of /daily-scan Phase 0 (see
.claude/skills/daily-scan/SKILL.md). Read-only — never mutates the DB.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sqlite3
import sys
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from check_vault_movers import get_all_vault_tickers  # noqa: E402
from download_all_assets import EXCLUDED_TICKERS, get_cluster_config_tickers  # noqa: E402

DB = ROOT / "market_data.db"

# Clean forward/reverse split factors a real corporate action snaps to.
CLEAN_FACTORS = [2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--window-days", type=int, default=45,
                   help="Calendar lookback for the discontinuity scan (default 45)")
    p.add_argument("--min-ratio", type=float, default=1.7,
                   help="Min single-day price ratio to flag (default 1.7 ~= a 41%% drop / 70%% jump)")
    p.add_argument("--factor-tol", type=float, default=0.08,
                   help="Max relative error vs nearest clean split factor for LIKELY (default 0.08)")
    p.add_argument("--min-price", type=float, default=3.0,
                   help="Min price on the higher side of the break — drops sub-$1 penny noise (default 3.0)")
    p.add_argument("--max-noise", type=float, default=0.08,
                   help="Max median surrounding daily move for LIKELY; above this the series is too "
                        "volatile to call a split vs normal vol (default 0.08)")
    p.add_argument("--all", action="store_true",
                   help="Scan every ticker in prices_long, not just tracked vault/cluster tickers")
    p.add_argument("--json", action="store_true", help="Machine-readable output")
    return p.parse_args()


def nearest_factor(ratio: float) -> tuple[int, float]:
    f = min(CLEAN_FACTORS, key=lambda c: abs(c - ratio))
    return f, abs(f - ratio) / f


def build_universe(conn: sqlite3.Connection, scan_all: bool) -> dict[str, str]:
    if scan_all:
        rows = conn.execute("SELECT DISTINCT Ticker FROM prices_long").fetchall()
        return {t: "all" for (t,) in rows}
    universe = {t: f"actor: {a}" for t, a in get_all_vault_tickers().items()}
    for t in get_cluster_config_tickers():
        universe.setdefault(t, "cluster config")
    macro = {
        r[0] for r in conn.execute(
            "SELECT ticker FROM ticker_metadata WHERE data_type IN ('macro','index') AND ticker IS NOT NULL"
        )
    }
    excluded = set(EXCLUDED_TICKERS)
    return {t: s for t, s in universe.items() if t not in excluded and t not in macro}


def series_in_window(conn: sqlite3.Connection, tickers: list[str], cutoff: str) -> dict[str, list[tuple[str, float]]]:
    out: dict[str, list[tuple[str, float]]] = {}
    for i in range(0, len(tickers), 500):
        chunk = tickers[i:i + 500]
        ph = ",".join("?" for _ in chunk)
        rows = conn.execute(
            f"SELECT Ticker, Date, Close FROM prices_long "
            f"WHERE Ticker IN ({ph}) AND Date >= ? AND Close IS NOT NULL AND Close > 0 "
            f"ORDER BY Ticker, Date",
            (*chunk, cutoff),
        ).fetchall()
        for t, d, c in rows:
            out.setdefault(t, []).append((d, c))
    return out


def analyze(ticker: str, rows: list[tuple[str, float]], args) -> dict | None:
    """Return a finding dict for the largest split-shaped break, or None."""
    if ticker.startswith("^") or len(rows) < 6:
        return None
    closes = [c for _, c in rows]
    rets = [abs(closes[k] / closes[k - 1] - 1) for k in range(1, len(closes))]  # rets[k-1] = move into day k
    best = None
    for i in range(1, len(rows)):
        prev, curr = closes[i - 1], closes[i]
        ratio = max(prev / curr, curr / prev)
        if ratio < args.min_ratio:
            continue
        direction = "DROP" if prev > curr else "JUMP"  # DROP=fwd split, JUMP=reverse
        before = closes[max(0, i - 5):i]
        after = closes[i:i + 5]
        med_b, med_a = median(before), median(after)
        hi, lo = max(med_b, med_a), min(med_b, med_a)
        if hi < args.min_price:            # penny noise
            continue
        level_ratio = hi / lo if lo else 0.0
        factor, ferr = nearest_factor(ratio)
        # surrounding volatility EXCLUDING the break day: a true split sits in an
        # otherwise-calm series; a meme/penny name's big move is just its normal vol.
        others = rets[:i - 1] + rets[i:]
        noise = median(others) if others else 0.0
        sustained = level_ratio >= 1.5 and abs(level_ratio - ratio) / ratio < 0.30
        likely = ferr < args.factor_tol and sustained and noise < args.max_noise
        cand = {
            "ticker": ticker, "date": rows[i][0][:10], "prev": round(prev, 4),
            "curr": round(curr, 4), "direction": direction, "ratio": round(ratio, 3),
            "nearest_factor": factor, "factor_err": round(ferr, 3),
            "level_ratio": round(level_ratio, 3), "surrounding_noise": round(noise, 3),
            "med_before": round(med_b, 3), "med_after": round(med_a, 3),
            "classification": "LIKELY-SPLIT" if likely else "REVIEW",
        }
        # keep the most split-like break: prefer LIKELY, then larger ratio
        key = (likely, ratio)
        if best is None or key > (best["classification"] == "LIKELY-SPLIT", best["ratio"]):
            best = cand
    return best


def fix_hint(f: dict) -> str:
    t = f["ticker"]
    if f["direction"] == "DROP":
        return (f"  {t}: forward {f['nearest_factor']}:1 split on {f['date']} — "
                f"`python scripts/add_ticker.py {t}` (yfinance auto_adjust back-adjusts the history).")
    return (f"  {t}: reverse 1:{f['nearest_factor']} split on {f['date']} — re-fetch first; if the vendor "
            f"hasn't recorded it yet (common for fresh reverse splits), back-adjust pre-break closes manually "
            f"(x{f['nearest_factor']}).")


def main() -> None:
    try:  # avoid cp1252 mojibake on Windows consoles
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = parse_args()
    conn = sqlite3.connect(DB)

    max_date = conn.execute("SELECT MAX(Date) FROM prices_long").fetchone()[0]
    if not max_date:
        raise SystemExit("prices_long is empty — nothing to scan.")
    cutoff = (dt.date.fromisoformat(max_date[:10]) - dt.timedelta(days=args.window_days)).isoformat()

    universe = build_universe(conn, args.all)
    series = series_in_window(conn, sorted(universe), cutoff + " 00:00:00")
    conn.close()

    findings = [f for t in sorted(series) if (f := analyze(t, series[t], args))]
    for f in findings:
        f["source"] = universe.get(f["ticker"], "?")
    likely = [f for f in findings if f["classification"] == "LIKELY-SPLIT"]
    review = [f for f in findings if f["classification"] == "REVIEW"]

    if args.json:
        print(json.dumps({
            "scan_window_start": cutoff, "scan_window_end": max_date[:10],
            "tickers_scanned": len(series), "likely_count": len(likely),
            "review_count": len(review), "likely": likely, "review": review,
        }, indent=2))
    else:
        print(f"Split-discontinuity scan: {cutoff} .. {max_date[:10]}  "
              f"({len(series)} tickers{' — whole DB' if args.all else ' — vault+cluster'})")
        if not likely and not review:
            print("Clean — no split-shaped discontinuities in window.")
        if likely:
            print(f"\nLIKELY SPLITS ({len(likely)}) — un-back-adjusted, fix before trusting the series:")
            print(f"{'ticker':<10} {'date':<11} {'dir':<5} {'ratio':>6} {'~fac':>5} {'facErr':>7} {'lvlShift':>8}  source")
            for f in likely:
                print(f"{f['ticker']:<10} {f['date']:<11} {f['direction']:<5} {f['ratio']:>6} "
                      f"{f['nearest_factor']:>5} {f['factor_err']*100:>6.1f}% {f['level_ratio']:>8}  {f['source']}")
            print("\nFix:")
            for f in likely:
                print(fix_hint(f))
            print("After fixing: re-verify continuity and re-run any affected cluster validation "
                  "(docs/cluster-validation.md step 11).")
        if review:
            print(f"\nREVIEW ({len(review)}) — large clean-factor move but level shift not clearly sustained "
                  f"(could be a split, a genuine crash, or a vol spike — eyeball it):")
            for f in review:
                print(f"  {f['ticker']:<10} {f['date']} {f['direction']} ratio {f['ratio']} "
                      f"(~{f['nearest_factor']}, err {f['factor_err']*100:.0f}%, lvlShift {f['level_ratio']}, "
                      f"noise {f['surrounding_noise']*100:.0f}%)  {f['source']}")

    sys.exit(1 if likely else 0)


if __name__ == "__main__":
    main()
