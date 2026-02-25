"""Quick vault mover check — scans actor aliases against market_data.db."""
import re
import sqlite3
import sys
from pathlib import Path

ACTORS = Path(__file__).parent.parent / "investing" / "Actors"
DB = Path(__file__).parent.parent / "market_data.db"
SKIP = {"AI","US","UK","EU","HQ","PE","RE","DC","VC","CEO","CTO","COO","CFO","IPO",
        "SA","SE","AG","NV","AB","LP","NA","AM","GP","BE","IT","OR","ON","TD","BN","BAM"}
THRESHOLD = 8.0

def main():
    if not DB.exists():
        print("No market_data.db found.")
        return

    conn = sqlite3.connect(str(DB))
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

    print(f"Found {len(ticker_map)} trackable tickers (in DB + vault).")

    movers = []
    for ticker, actor in ticker_map.items():
        try:
            rows = conn.execute(
                f'SELECT date, [{ticker}] FROM stock_prices_daily WHERE [{ticker}] IS NOT NULL ORDER BY date DESC LIMIT 2'
            ).fetchall()
        except Exception:
            continue
        if len(rows) < 2:
            continue
        curr, prev = rows[0][1], rows[1][1]
        if not prev:
            continue
        pct = ((curr - prev) / prev) * 100
        if abs(pct) >= THRESHOLD:
            movers.append((ticker, actor, prev, curr, pct, rows[0][0][:10]))

    conn.close()
    movers.sort(key=lambda x: abs(x[4]), reverse=True)

    if movers:
        print(f"\n🔴 VAULT ACTORS WITH MAJOR MOVES (±{THRESHOLD}%+):\n")
        print(f"{'Ticker':<8} {'Actor':<35} {'Prev':>8} {'Last':>8} {'Change':>8}")
        print("-" * 70)
        for t, a, p, c, pct, d in movers:
            sign = "+" if pct > 0 else ""
            print(f"{t:<8} {a:<35} ${p:>7.2f} ${c:>7.2f} {sign}{pct:>6.1f}%")
    else:
        print(f"\nNo vault actors moved ±{THRESHOLD}%+ in the last session.")

if __name__ == "__main__":
    main()
