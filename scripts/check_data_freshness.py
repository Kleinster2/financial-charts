"""Per-ticker price-freshness audit: which tracked tickers lag the latest SPY session?

Why: daily_scan.py's freshness check looks only at SPY's max date, so the DB
can look fresh while individual series rot. The 2026-06-09/10 cluster audit
found Marsh McLennan's legacy series three months stale, PWP/LAZ/FSLY/SNDK
frozen since May 1, and ELAN/FBIN frozen on the day their cluster configs
were created — invisible to every workflow, because quick_movers silently
drops stale names rather than erroring.

Universe checked = vault actor tickers (investing/Actors/ aliases +
quick-stats rows, via check_vault_movers.get_all_vault_tickers) plus
cluster-config tickers (scripts/cluster_configs/*.yaml), intersected with
what actually exists in prices_long, minus download_all_assets
EXCLUDED_TICKERS (documented dead/renamed names — e.g. the legacy MMC
series is excluded because Marsh McLennan trades as MRSH).

Lag is measured in SPY trading sessions (count of SPY dates after the
ticker's last close), so weekends and US holidays never false-positive.
Exchange-suffixed foreign listings get a higher allowance (different
holiday calendars).

Usage:
  python scripts/check_data_freshness.py                       # human table
  python scripts/check_data_freshness.py --json                # machine-readable
  python scripts/check_data_freshness.py --max-lag 3 --max-lag-foreign 6

Exit code 1 when any ticker exceeds its allowance (cron/CI alert-friendly).
Part of /daily-scan Phase 0 (see .claude/skills/daily-scan/SKILL.md).
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from bisect import bisect_right
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from check_vault_movers import get_all_vault_tickers  # noqa: E402
from download_all_assets import EXCLUDED_TICKERS, get_cluster_config_tickers  # noqa: E402

DB = ROOT / "market_data.db"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--max-lag", type=int, default=3, help="Allowed lag in SPY sessions for US-listed tickers (default 3)")
    p.add_argument("--max-lag-foreign", type=int, default=6, help="Allowed lag for exchange-suffixed foreign listings (default 6)")
    p.add_argument("--json", action="store_true", help="Machine-readable output")
    return p.parse_args()


def is_foreign(ticker: str) -> bool:
    return "." in ticker


def last_dates_for(conn: sqlite3.Connection, tickers: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for i in range(0, len(tickers), 500):
        chunk = tickers[i : i + 500]
        placeholders = ",".join("?" for _ in chunk)
        rows = conn.execute(
            f"SELECT Ticker, MAX(Date) FROM prices_long "
            f"WHERE Ticker IN ({placeholders}) AND Close IS NOT NULL GROUP BY Ticker",
            chunk,
        ).fetchall()
        out.update({t: d for t, d in rows if d})
    return out


def main() -> None:
    args = parse_args()
    conn = sqlite3.connect(DB)

    spy_dates = [
        r[0] for r in conn.execute(
            "SELECT DISTINCT Date FROM prices_long WHERE Ticker = 'SPY' AND Close IS NOT NULL ORDER BY Date"
        )
    ]
    if not spy_dates:
        raise SystemExit("No SPY data in prices_long — cannot benchmark freshness.")
    benchmark = spy_dates[-1]

    vault_map = get_all_vault_tickers()  # {ticker: actor_name}
    universe: dict[str, str] = {t: f"actor: {a}" for t, a in vault_map.items()}
    for t in get_cluster_config_tickers():
        universe.setdefault(t, "cluster config")
    excluded = set(EXCLUDED_TICKERS)
    # Macro series (GDP, yields, ...) update on monthly/quarterly calendars —
    # daily-session lag is meaningless for them, and vault-note regexes can
    # collide with their symbols (e.g. GDP).
    macro = {
        r[0] for r in conn.execute(
            "SELECT ticker FROM ticker_metadata WHERE data_type IN ('macro', 'index') AND ticker IS NOT NULL"
        )
    }
    universe = {t: src for t, src in universe.items() if t not in excluded and t not in macro}

    last_dates = last_dates_for(conn, sorted(universe))
    conn.close()
    not_in_db = len(universe) - len(last_dates)

    stale = []
    for ticker, last in last_dates.items():
        lag = len(spy_dates) - bisect_right(spy_dates, last)
        allowance = args.max_lag_foreign if is_foreign(ticker) else args.max_lag
        if lag > allowance:
            stale.append({
                "ticker": ticker,
                "source": universe[ticker],
                "last_close": last[:10],
                "sessions_behind": lag,
                "allowance": allowance,
            })
    stale.sort(key=lambda r: -r["sessions_behind"])

    if args.json:
        print(json.dumps({
            "benchmark_spy_date": benchmark[:10],
            "tickers_checked": len(last_dates),
            "tickers_not_in_db": not_in_db,
            "stale_count": len(stale),
            "stale": stale,
        }, indent=2))
    else:
        print(f"Freshness benchmark: SPY last close {benchmark[:10]}")
        print(f"Checked {len(last_dates)} tracked tickers present in prices_long "
              f"({not_in_db} tracked symbols not in DB — alias-audit territory, not freshness)")
        if not stale:
            print(f"All fresh within allowance ({args.max_lag} US / {args.max_lag_foreign} foreign sessions).")
        else:
            print(f"\nSTALE ({len(stale)}):")
            print(f"{'Ticker':<12} {'last close':<12} {'behind':>7} {'allow':>6}  source")
            for r in stale:
                print(f"{r['ticker']:<12} {r['last_close']:<12} {r['sessions_behind']:>7} {r['allowance']:>6}  {r['source']}")
            print("\nFix: scripts/add_ticker.py TICKER ... to backfill, then check why the name "
                  "is missing from the refresh lists in download_all_assets.py (or whether it "
                  "renamed/delisted -> EXCLUDED_TICKERS + vault 'Former ticker').")

    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
