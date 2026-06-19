"""
Check major stock movers against vault actor notes.

Scans the vault for actor notes that have ticker aliases,
then checks which ones had significant moves (±8%+).

Usage:
  python scripts/check_vault_movers.py                # check today's movers
  python scripts/check_vault_movers.py --threshold 5  # custom threshold (%)
  python scripts/check_vault_movers.py --list-tickers # just list known tickers

Requires: yfinance (pip install yfinance)
"""

import argparse
import os
import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent / "investing"
ACTORS_DIR = VAULT_ROOT / "Actors"


def extract_tickers_from_note(filepath):
    """Extract ticker symbols from actor note aliases and body."""
    tickers = set()
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return tickers

    # From aliases line: aliases: [AAPL, Apple Inc]
    alias_match = re.search(r"aliases:\s*\[(.*?)\]", text)
    if alias_match:
        for alias in alias_match.group(1).split(","):
            alias = alias.strip().strip("'\"")
            # Ticker-like: 1-5 uppercase letters, optionally with exchange prefix
            if re.match(r"^[A-Z]{1,5}$", alias):
                tickers.add(alias)

    # From quick stats table: | Ticker | AAPL |
    ticker_match = re.search(r"\|\s*Ticker[s]?\s*\|\s*([^\|]+)\|", text, re.IGNORECASE)
    if ticker_match:
        val = ticker_match.group(1).strip()
        # Handle "TEP (Euronext Paris), TLPFY (OTC)" style
        for part in re.split(r"[,;]", val):
            part = part.strip()
            match = re.match(r"([A-Z]{1,6})", part)
            if match:
                tickers.add(match.group(1))

    return tickers


def get_all_vault_tickers():
    """Scan all actor notes and return {ticker: actor_name} mapping."""
    ticker_map = {}
    if not ACTORS_DIR.exists():
        return ticker_map

    for f in ACTORS_DIR.glob("*.md"):
        tickers = extract_tickers_from_note(f)
        actor_name = f.stem
        for t in tickers:
            # Skip very common abbreviations that aren't tickers
            if t in ("AI", "US", "UK", "EU", "HQ", "PE", "RE", "DC", "VC", "CEO", "CTO", "COO", "CFO", "IPO"):
                continue
            ticker_map[t] = actor_name

    return ticker_map


def check_movers_from_db(ticker_map, threshold=8.0):
    """Check vault tickers against local market_data.db."""
    import sqlite3
    db_path = Path(__file__).parent.parent / "market_data.db"
    if not db_path.exists():
        print("No market_data.db found.")
        return []

    conn = sqlite3.connect(str(db_path))

    # Get column names to find which tickers we track
    cols = [r[1] for r in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()]

    movers = []
    for ticker, actor in ticker_map.items():
        # Try exact match and common yfinance suffixes
        col = None
        for candidate in [ticker, f"{ticker}.PA", f"{ticker}=X"]:
            if candidate in cols:
                col = candidate
                break
        if not col:
            continue

        rows = conn.execute(f"""
            SELECT date, "{col}" FROM stock_prices_daily
            WHERE "{col}" IS NOT NULL
            ORDER BY date DESC LIMIT 2
        """).fetchall()

        if len(rows) < 2:
            continue

        curr = rows[0][1]
        prev = rows[1][1]
        if prev == 0 or prev is None or curr is None:
            continue

        pct = ((curr - prev) / prev) * 100
        if abs(pct) >= threshold:
            movers.append({
                "ticker": ticker,
                "actor": actor,
                "prev_close": round(prev, 2),
                "last_close": round(curr, 2),
                "change_pct": round(pct, 1),
                "date": rows[0][0],
            })

    conn.close()
    movers.sort(key=lambda x: abs(x["change_pct"]), reverse=True)
    return movers


def check_movers(ticker_map, threshold=8.0):
    """Check which vault tickers had significant moves. Uses local DB first, falls back to yfinance."""
    # Try local DB first
    movers = check_movers_from_db(ticker_map, threshold)
    if movers:
        return movers

    # Fallback to yfinance if available
    try:
        import yfinance as yf
    except ImportError:
        print("No local market data and yfinance not installed.")
        print("Run: pip install yfinance")
        print("Or update market_data.db via the charting app.")
        return []

    tickers = list(ticker_map.keys())
    if not tickers:
        print("No tickers found in vault actor notes.")
        return []

    print(f"Checking {len(tickers)} vault tickers for ±{threshold}% moves via yfinance...\n")

    movers = []
    try:
        data = yf.download(tickers, period="2d", progress=False, threads=True)
        if data.empty:
            return []

        close = data["Close"]
        if len(close) < 2:
            return []

        for ticker in tickers:
            try:
                if ticker in close.columns:
                    prices = close[ticker].dropna()
                elif len(tickers) == 1:
                    prices = close.dropna()
                else:
                    continue

                if len(prices) < 2:
                    continue

                prev = prices.iloc[-2]
                curr = prices.iloc[-1]
                if prev == 0:
                    continue

                pct = ((curr - prev) / prev) * 100

                if abs(pct) >= threshold:
                    movers.append({
                        "ticker": ticker,
                        "actor": ticker_map[ticker],
                        "prev_close": round(prev, 2),
                        "last_close": round(curr, 2),
                        "change_pct": round(pct, 1),
                    })
            except Exception:
                continue

    except Exception as e:
        print(f"Download error: {e}")
        return []

    movers.sort(key=lambda x: abs(x["change_pct"]), reverse=True)
    return movers


def main():
    parser = argparse.ArgumentParser(description="Check vault actor movers")
    parser.add_argument("--threshold", type=float, default=8.0, help="Move threshold %%")
    parser.add_argument("--list-tickers", action="store_true", help="Just list known tickers")
    args = parser.parse_args()

    ticker_map = get_all_vault_tickers()
    print(f"Found {len(ticker_map)} tickers across vault actor notes.\n")

    if args.list_tickers:
        for t, name in sorted(ticker_map.items()):
            print(f"  {t:8s} → {name}")
        return

    movers = check_movers(ticker_map, args.threshold)

    if not movers:
        print(f"No vault actors moved ±{args.threshold}%+ in the last session.")
    else:
        print(f"\n🔴 VAULT ACTORS WITH MAJOR MOVES (±{args.threshold}%+):\n")
        print(f"{'Ticker':<8} {'Actor':<30} {'Prev':>8} {'Last':>8} {'Change':>8}")
        print("-" * 65)
        for m in movers:
            sign = "+" if m["change_pct"] > 0 else ""
            print(f"{m['ticker']:<8} {m['actor']:<30} ${m['prev_close']:>7.2f} ${m['last_close']:>7.2f} {sign}{m['change_pct']:>6.1f}%")


if __name__ == "__main__":
    main()
