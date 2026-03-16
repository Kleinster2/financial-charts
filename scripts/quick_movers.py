"""Quick vault mover check — scans actor aliases against market data.

Uses standard deviations of daily returns (rolling 60-day window) to flag
statistically unusual moves, not arbitrary percentage thresholds. A 3% move
on PG is a 3-sigma event; an 8% move on a volatile biotech might be 1-sigma.

Supports both DuckDB (long format: Date/Ticker/Close) and SQLite (wide format:
Date + ticker columns). Tries DuckDB first if it has fresher data.
"""
import argparse
import re
import sqlite3
import sys
import math
from pathlib import Path

try:
    import duckdb
    HAS_DUCKDB = True
except ImportError:
    HAS_DUCKDB = False

ACTORS = Path(__file__).parent.parent / "investing" / "Actors"
SQLITE_DB = Path(__file__).parent.parent / "market_data.db"
DUCK_DB = Path(__file__).parent.parent / "market_data.duckdb"
SKIP = {"AI","US","UK","EU","HQ","PE","RE","DC","VC","CEO","CTO","COO","CFO","IPO",
        "SA","SE","AG","NV","AB","LP","NA","AM","GP","BE","IT","OR","ON","TD","BN","BAM"}
DEFAULT_SIGMA = 2.5
LOOKBACK = 60  # trading days for rolling volatility


def get_vault_tickers():
    """Extract ticker candidates from vault actor notes."""
    candidates = {}
    for f in ACTORS.glob("*.md"):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")[:2000]
        except Exception:
            continue
        am = re.search(r"aliases:\s*\[(.*?)\]", text)
        if am:
            for a in am.group(1).split(","):
                a = a.strip().strip("'\"")
                if re.match(r"^[A-Z]{1,6}$", a) and a not in SKIP:
                    candidates[a] = f.stem
        tm = re.search(r"\|\s*Tickers?\s*\|\s*([^\|]+)\|", text, re.IGNORECASE)
        if tm:
            for part in re.split(r"[,;]", tm.group(1).strip()):
                m = re.match(r"([A-Z]{1,6})", part.strip())
                if m and m.group(1) not in SKIP:
                    candidates[m.group(1)] = f.stem
    return candidates


def pick_backend():
    """Choose DuckDB or SQLite based on data freshness."""
    duck_date = None
    sqlite_date = None

    if HAS_DUCKDB and DUCK_DB.exists():
        try:
            conn = duckdb.connect(str(DUCK_DB), read_only=True)
            r = conn.execute("SELECT MAX(Date) FROM prices").fetchone()
            duck_date = str(r[0]) if r and r[0] else None
            conn.close()
        except Exception:
            pass

    if SQLITE_DB.exists():
        try:
            conn = sqlite3.connect(str(SQLITE_DB))
            r = conn.execute("SELECT MAX(date) FROM stock_prices_daily").fetchone()
            sqlite_date = str(r[0])[:10] if r and r[0] else None
            conn.close()
        except Exception:
            pass

    if duck_date and sqlite_date:
        if duck_date >= sqlite_date:
            return "duckdb", duck_date
        else:
            return "sqlite", sqlite_date
    elif duck_date:
        return "duckdb", duck_date
    elif sqlite_date:
        return "sqlite", sqlite_date
    else:
        return None, None


def compute_sigma_duckdb(candidates, lookback=LOOKBACK):
    """Compute sigma moves using DuckDB long-format prices table."""
    conn = duckdb.connect(str(DUCK_DB), read_only=True)

    # Get tickers that exist in DB
    db_tickers = set(r[0] for r in conn.execute("SELECT DISTINCT Ticker FROM prices").fetchall())
    ticker_map = {t: a for t, a in candidates.items() if t in db_tickers}

    if not ticker_map:
        conn.close()
        return ticker_map, []

    tickers = list(ticker_map.keys())
    # Get the last (lookback+1) dates
    dates = conn.execute(
        f"SELECT DISTINCT Date FROM prices ORDER BY Date DESC LIMIT {lookback + 1}"
    ).fetchall()
    if len(dates) < 10:
        conn.close()
        return ticker_map, []

    min_date = dates[-1][0]
    ticker_list = ", ".join(f"'{t}'" for t in tickers)

    rows = conn.execute(f"""
        SELECT Ticker, Date, Close FROM prices
        WHERE Ticker IN ({ticker_list}) AND Date >= '{min_date}'
        ORDER BY Ticker, Date DESC
    """).fetchall()
    conn.close()

    # Group by ticker
    from collections import defaultdict
    by_ticker = defaultdict(list)
    for ticker, date, close in rows:
        if close is not None:
            by_ticker[ticker].append((str(date), close))

    return ticker_map, _compute_from_prices(by_ticker, ticker_map)


def compute_sigma_sqlite(candidates, lookback=LOOKBACK):
    """Compute sigma moves using SQLite wide-format stock_prices_daily table."""
    conn = sqlite3.connect(str(SQLITE_DB))
    cols = set(r[1] for r in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall())
    ticker_map = {t: a for t, a in candidates.items() if t in cols}

    if not ticker_map:
        conn.close()
        return ticker_map, []

    tickers = list(ticker_map.keys())
    col_str = ", ".join(f"[{t}]" for t in tickers)
    rows = conn.execute(
        f'SELECT date, {col_str} FROM stock_prices_daily ORDER BY date DESC LIMIT {lookback + 1}'
    ).fetchall()
    conn.close()

    if len(rows) < 10:
        return ticker_map, []

    # Convert wide to per-ticker price lists
    from collections import defaultdict
    by_ticker = defaultdict(list)
    for row in rows:
        date = str(row[0])[:10]
        for idx, ticker in enumerate(tickers):
            val = row[idx + 1]
            if val is not None:
                by_ticker[ticker].append((date, val))

    return ticker_map, _compute_from_prices(by_ticker, ticker_map)


def _compute_from_prices(by_ticker, ticker_map):
    """Shared sigma computation from per-ticker price lists (date desc order)."""
    results = []
    for ticker, price_list in by_ticker.items():
        if len(price_list) < 10:
            continue

        prices = [p for _, p in price_list]
        returns = []
        for i in range(len(prices) - 1):
            if prices[i + 1] and prices[i + 1] > 0:
                returns.append((prices[i] - prices[i + 1]) / prices[i + 1])

        if len(returns) < 5:
            continue

        today_return = returns[0]
        curr, prev = prices[0], prices[1]
        date = price_list[0][0]
        pct = today_return * 100

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

        actor = ticker_map.get(ticker, ticker)
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

    backend, latest_date = pick_backend()
    if not backend:
        print("No market data found (checked DuckDB and SQLite).")
        return

    print(f"Using {backend} (latest data: {latest_date})")
    candidates = get_vault_tickers()

    if backend == "duckdb":
        ticker_map, all_results = compute_sigma_duckdb(candidates, args.lookback)
    else:
        ticker_map, all_results = compute_sigma_sqlite(candidates, args.lookback)

    print(f"Found {len(ticker_map)} trackable tickers (in DB + vault).")

    movers = []
    for ticker, actor, prev, curr, pct, z_score, vol, date in all_results:
        flagged = abs(z_score) >= args.sigma
        if args.pct and abs(pct) >= args.pct:
            flagged = True
        if flagged:
            movers.append((ticker, actor, prev, curr, pct, z_score, vol, date))
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
