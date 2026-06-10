"""Backfill ticker_metadata.data_type for tickers present in prices_long.

Why: the cluster-validation random-basket null pool must be filterable to
common stocks (see docs/cluster-validation-audit-2026-06-09.md, finding 1).
As of the 2026-06-09 audit, 1,371 of 2,274 ticker_metadata rows had NULL
data_type (AAPL included), so the documented data_type='stock' filter was
unimplementable.

Strictly additive: only fills NULL/missing data_type values, never overwrites
an existing one, and touches no price tables.

Classification order per ticker:
  1. Pattern rules (no network): *-USD -> crypto, ^* -> index, *=F -> future
  2. yfinance chart metadata instrumentType:
       EQUITY -> stock, ETF -> etf, INDEX -> index,
       CRYPTOCURRENCY -> crypto, MUTUALFUND -> fund, FUTURE -> future,
       CURRENCY -> currency, anything else -> lowercased as-is
Tickers that cannot be classified (delisted, synthetic, not on Yahoo) stay
NULL and are conservatively excluded from the random-basket pool.

Usage:
  python scripts/backfill_ticker_types.py --dry-run
  python scripts/backfill_ticker_types.py --limit 20   # smoke test, writes
  python scripts/backfill_ticker_types.py              # full run
"""

from __future__ import annotations

import argparse
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "market_data.db"

INSTRUMENT_TYPE_MAP = {
    "EQUITY": "stock",
    "ETF": "etf",
    "INDEX": "index",
    "CRYPTOCURRENCY": "crypto",
    "MUTUALFUND": "fund",
    "FUTURE": "future",
    "CURRENCY": "currency",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--dry-run", action="store_true", help="Classify but write nothing")
    p.add_argument("--limit", type=int, help="Only process the first N unclassified tickers")
    p.add_argument("--sleep", type=float, default=0.15, help="Seconds between Yahoo calls (default 0.15)")
    return p.parse_args()


def classify_by_pattern(ticker: str) -> str | None:
    if ticker.endswith("-USD"):
        return "crypto"
    if ticker.startswith("^"):
        return "index"
    if ticker.endswith("=F"):
        return "future"
    return None


def classify_by_yahoo(ticker: str) -> str | None:
    import yfinance as yf

    try:
        meta = yf.Ticker(ticker).get_history_metadata()
    except Exception:
        return None
    itype = (meta or {}).get("instrumentType")
    if not itype:
        return None
    return INSTRUMENT_TYPE_MAP.get(itype, str(itype).lower())


def main() -> None:
    args = parse_args()
    conn = sqlite3.connect(DB)

    tickers = [r[0] for r in conn.execute("SELECT DISTINCT Ticker FROM prices_long ORDER BY Ticker")]
    meta = dict(conn.execute("SELECT ticker, data_type FROM ticker_metadata"))

    unclassified = [t for t in tickers if meta.get(t) in (None, "")]
    print(f"prices_long distinct tickers: {len(tickers)}")
    print(f"already typed:                {len(tickers) - len(unclassified)}")
    print(f"to classify:                  {len(unclassified)}")
    if args.limit:
        unclassified = unclassified[: args.limit]
        print(f"limited to first {len(unclassified)}")

    results: dict[str, str] = {}
    failures: list[str] = []
    network_calls = 0

    for i, t in enumerate(unclassified, start=1):
        dtype = classify_by_pattern(t)
        if dtype is None:
            dtype = classify_by_yahoo(t)
            network_calls += 1
            time.sleep(args.sleep)
        if dtype is None:
            failures.append(t)
        else:
            results[t] = dtype
        if i % 50 == 0:
            print(f"  {i}/{len(unclassified)}  classified={len(results)}  failed={len(failures)}")
        # Abort early if Yahoo is clearly blocking us rather than burn the whole run
        if network_calls >= 100 and len(failures) > 0.5 * i:
            print(f"ABORT: failure rate {len(failures)}/{i} after {network_calls} network calls — Yahoo likely throttling. Re-run later.")
            break

    by_type: dict[str, int] = {}
    for dtype in results.values():
        by_type[dtype] = by_type.get(dtype, 0) + 1
    print("\nClassification summary:")
    for dtype, n in sorted(by_type.items(), key=lambda kv: -kv[1]):
        print(f"  {dtype:>10}: {n}")
    print(f"  unclassified (left NULL): {len(failures)}")
    if failures:
        print(f"  failed tickers (first 30): {', '.join(failures[:30])}")

    if args.dry_run:
        print("\nDRY RUN — nothing written.")
        conn.close()
        return

    updated = inserted = 0
    for t, dtype in results.items():
        if t in meta:
            cur = conn.execute(
                "UPDATE ticker_metadata SET data_type = ? WHERE ticker = ? AND (data_type IS NULL OR data_type = '')",
                (dtype, t),
            )
            updated += cur.rowcount
        else:
            conn.execute(
                "INSERT INTO ticker_metadata (ticker, table_name, data_type) VALUES (?, 'prices_long', ?)",
                (t, dtype),
            )
            inserted += 1
    conn.commit()
    conn.close()
    print(f"\nWrote: {updated} updates (NULL->value only), {inserted} inserts.")


if __name__ == "__main__":
    main()
