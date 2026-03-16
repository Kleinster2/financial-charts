"""Quick vault mover check — scans actor aliases against market_data.db.

Uses standard deviations of daily returns (rolling 60-day window) to flag
statistically unusual moves, not arbitrary percentage thresholds. A 3% move
on PG is a 3-sigma event; an 8% move on a volatile biotech might be 1-sigma.
"""
import argparse
import re
import sqlite3
import sys
import math
from pathlib import Path

ACTORS = Path(__file__).parent.parent / "investing" / "Actors"
DB = Path(__file__).parent.parent / "market_data.db"
SKIP = {"AI","US","UK","EU","HQ","PE","RE","DC","VC","CEO","CTO","COO","CFO","IPO",
        "SA","SE","AG","NV","AB","LP","NA","AM","GP","BE","IT","OR","ON","TD","BN","BAM"}
DEFAULT_SIGMA = 2.5
LOOKBACK = 60  # trading days for rolling volatility


def get_ticker_map(conn):
    """Map vault actor tickers to actor names."""
    cols = set(r[1] for r in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall())
    ticker_map = {}
    for f in ACTORS.glob("*.md"):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")[:2000]
        except Exception:
            continue
        am = re.search(r"aliases:\s*\[(.*?)\]", text)
        if am:
            for a in am.group(1).split(","):
                a = a.strip().strip("'\"")
                if re.match(r"^[A-Z]{1,5}$", a) and a not in SKIP and a in cols:
                    ticker_map[a] = f.stem
        tm = re.search(r"\|\s*Tickers?\s*\|\s*([^\|]+)\|", text, re.IGNORECASE)
        if tm:
            for part in re.split(r"[,;]", tm.group(1).strip()):
                m = re.match(r"([A-Z]{1,6})", part.strip())
                if m and m.group(1) not in SKIP and m.group(1) in cols:
                    ticker_map[m.group(1)] = f.stem
    return ticker_map


def compute_all_sigma_moves(conn, ticker_map, lookback=LOOKBACK):
    """Batch-compute sigma moves for all tickers in one query. Returns list of results."""
    tickers = list(ticker_map.keys())
    # Build one query that fetches the last (lookback+1) rows with all ticker columns
    cols = ", ".join(f"[{t}]" for t in tickers)
    try:
        rows = conn.execute(
            f'SELECT date, {cols} FROM stock_prices_daily ORDER BY date DESC LIMIT {lookback + 1}'
        ).fetchall()
    except Exception:
        return []

    if len(rows) < 10:
        return []

    results = []
    for idx, ticker in enumerate(tickers):
        col_idx = idx + 1  # offset by 1 for date column
        prices = [r[col_idx] for r in rows if r[col_idx] is not None]

        if len(prices) < 10:
            continue

        # Daily returns (most recent first in the prices list)
        returns = []
        for i in range(len(prices) - 1):
            if prices[i + 1] and prices[i + 1] > 0:
                returns.append((prices[i] - prices[i + 1]) / prices[i + 1])

        if len(returns) < 5:
            continue

        today_return = returns[0]
        curr, prev = prices[0], prices[1]
        date = rows[0][0][:10]
        pct = today_return * 100

        # Rolling volatility from prior returns (exclude today)
        hist_returns = returns[1:]
        if len(hist_returns) < 5:
            continue

        mean = sum(hist_returns) / len(hist_returns)
        variance = sum((r - mean) ** 2 for r in hist_returns) / len(hist_returns)
        std = math.sqrt(variance)

        if std < 1e-10:
            continue

        z_score = (today_return - mean) / std
        annualized_vol = std * math.sqrt(252) * 100

        actor = ticker_map[ticker]
        results.append((ticker, actor, prev, curr, pct, z_score, annualized_vol, date))

    return results


def main():
    parser = argparse.ArgumentParser(description="Check vault actors for statistically unusual moves.")
    parser.add_argument("--sigma", type=float, default=DEFAULT_SIGMA,
                        help=f"Standard deviation threshold (default: {DEFAULT_SIGMA})")
    parser.add_argument("--lookback", type=int, default=LOOKBACK,
                        help=f"Rolling window for volatility calc (default: {LOOKBACK} days)")
    parser.add_argument("--pct", type=float, default=None,
                        help="Optional: also flag moves above this %% regardless of sigma")
    args = parser.parse_args()

    if not DB.exists():
        print("No market_data.db found.")
        return

    conn = sqlite3.connect(str(DB))
    ticker_map = get_ticker_map(conn)
    print(f"Found {len(ticker_map)} trackable tickers (in DB + vault).")

    all_results = compute_all_sigma_moves(conn, ticker_map, args.lookback)

    movers = []
    for ticker, actor, prev, curr, pct, z_score, vol, date in all_results:
        flagged = abs(z_score) >= args.sigma
        if args.pct and abs(pct) >= args.pct:
            flagged = True
        if flagged:
            movers.append((ticker, actor, prev, curr, pct, z_score, vol, date))

    conn.close()
    movers.sort(key=lambda x: abs(x[5]), reverse=True)

    if movers:
        print(f"\n** VAULT ACTORS WITH UNUSUAL MOVES (>={args.sigma} sigma):\n")
        hdr = f"{'Ticker':<8} {'Actor':<30} {'Prev':>8} {'Last':>8} {'Change':>8} {'Sigma':>7} {'AnnVol':>7}"
        print(hdr)
        print("-" * len(hdr))
        for t, a, p, c, pct, z, vol, d in movers:
            sign = "+" if pct > 0 else ""
            zsign = "+" if z > 0 else ""
            print(f"{t:<8} {a:<30} ${p:>7.2f} ${c:>7.2f} {sign}{pct:>6.1f}% {zsign}{z:>5.1f}s {vol:>5.0f}%")
    else:
        print(f"\nNo vault actors exceeded +/-{args.sigma} sigma in the last session.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        sys.exit(1)
