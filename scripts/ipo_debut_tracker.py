"""IPO debut tracker — catch first-day IPO events that the standard
[[quick_movers.py]] mover screen misses by design.

The Phase 0 mover screen needs three things to flag a name:
1. The actor note's `aliases:` or `| Ticker |` cell exposes the ticker.
2. The ticker has price history in `prices_long` (>= 60 sessions for vol).
3. The latest close lands on the SPY session date.

Brand-new IPOs fail #2 (zero price history on day 1) and often #1 (the actor
note hasn't been updated post-IPO — see [[Chime]] May 2026 and
[[HawkEye 360]] May 2026 examples).

This tool addresses the IPO blind-spot in two complementary modes:

USAGE
-----
    # Mode 1: pass a list of candidate IPO tickers and cross-reference.
    python scripts/ipo_debut_tracker.py --tickers HAWK CHYM KLAR

    # Mode 2: scan vault for #private actor notes whose body mentions
    # NYSE: / NASDAQ: ticker patterns -> likely IPO'd, status stale.
    python scripts/ipo_debut_tracker.py --scan-stale-private

    # Mode 3: combine. Pass ticker list AND scan-stale-private.
    python scripts/ipo_debut_tracker.py --tickers HAWK --scan-stale-private

OUTPUT
------
For each candidate, the tool reports:
- Whether the ticker is in `prices_long` (data ingested?)
- Whether a vault actor note exists (file by name OR alias OR ticker pattern)
- Whether the actor note is tagged #private (status stale?)
- Suggested action (add_ticker.py, edit aliases, update tag)
"""
import argparse
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
ACTORS = ROOT / "investing" / "Actors"
DB = ROOT / "market_data.db"

TICKER_RE = re.compile(r"^[A-Z]{1,6}$")
SKIP = {
    "AI", "US", "UK", "EU", "HQ", "PE", "RE", "DC", "VC", "CEO", "CTO", "COO",
    "CFO", "IPO", "SA", "SE", "AG", "NV", "AB", "LP", "NA", "AM", "GP", "BE",
    "IT", "OR", "ON", "TD", "BN", "BAM", "PR", "PM", "RFP", "SEC", "FED", "GDP",
    "USA", "USD", "EUR", "JPY", "CNY", "GBP", "QE", "QT", "ECB", "DOJ", "DOD",
}

BODY_TICKER_PATTERNS = [
    re.compile(r"\b(?:NYSE|NASDAQ|NYSE Arca|AMEX)\s*:\s*([A-Z]{1,6})\b"),
    re.compile(r"\((?:NYSE|NASDAQ|NYSE Arca|AMEX)\s*:\s*([A-Z]{1,6})\)"),
    re.compile(r"\bTicker\s*:\s*([A-Z]{1,6})\b", re.IGNORECASE),
    re.compile(r"\btrades?\s+as\s+([A-Z]{1,6})\b"),
]


def get_db_tickers():
    if not DB.exists():
        return set()
    try:
        conn = sqlite3.connect(str(DB))
        rows = conn.execute("SELECT DISTINCT ticker FROM prices_long").fetchall()
        conn.close()
        return {r[0] for r in rows}
    except Exception:
        return set()


def extract_aliases(text):
    m = re.search(r"^aliases:\s*\[(.*?)\]", text, flags=re.MULTILINE)
    if not m:
        return set()
    raw = [a.strip().strip("'\"") for a in m.group(1).split(",") if a.strip()]
    return {a for a in raw if TICKER_RE.match(a) and a not in SKIP}


def extract_body_tickers(text):
    found = set()
    for pat in BODY_TICKER_PATTERNS:
        for m in pat.finditer(text):
            t = m.group(1).upper()
            if TICKER_RE.match(t) and t not in SKIP:
                found.add(t)
    return found


def find_note_by_ticker(ticker):
    """Locate an actor note that exposes the given ticker via aliases."""
    for path in ACTORS.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if ticker in extract_aliases(text):
            return path
    return None


def find_note_by_name_substring(query):
    """Locate an actor note whose filename contains the query (case-insensitive)."""
    matches = []
    q_lower = query.lower()
    for path in ACTORS.glob("*.md"):
        if q_lower in path.stem.lower():
            matches.append(path)
    return matches


def is_private(text):
    return "#private" in text or "private" in re.findall(r"#([a-z][a-z0-9-]*)", text)


def report_ticker(ticker, db_tickers):
    """Report on a single candidate IPO ticker."""
    print(f"\n  {ticker}:")
    in_db = ticker in db_tickers
    print(f"    in prices_long: {'YES' if in_db else 'NO -> run: python scripts/add_ticker.py ' + ticker}")

    note = find_note_by_ticker(ticker)
    if note:
        text = note.read_text(encoding="utf-8", errors="ignore")
        private = is_private(text)
        print(f"    actor note (alias match): {note.relative_to(ROOT).as_posix()}")
        print(f"    tagged #private: {'YES -> update to #public + add Q1 print' if private else 'no'}")
    else:
        # Fall back to a name-substring search (the note may exist but lack the ticker alias).
        substring_hits = find_note_by_name_substring(ticker)
        if substring_hits:
            print(f"    actor note (no alias match, name-substring fallback):")
            for p in substring_hits[:3]:
                text = p.read_text(encoding="utf-8", errors="ignore")
                private = is_private(text)
                tag = " #private" if private else ""
                print(f"      {p.relative_to(ROOT).as_posix()}{tag}")
            print(f"    ACTION: edit aliases of the matching note to include {ticker}")
        else:
            print(f"    actor note: NOT FOUND -> consider creating actor stub for {ticker}")


def scan_stale_private():
    """Find actor notes tagged #private whose body has NYSE/NASDAQ ticker patterns."""
    print("\n=== Scanning for #private notes with public-ticker mentions ===")
    found = 0
    for path in sorted(ACTORS.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if not is_private(text):
            continue
        body_tickers = extract_body_tickers(text)
        if not body_tickers:
            continue
        # Skip notes whose body just mentions a competitor's ticker
        # (heuristic: the body must mention the actor's own name + ticker close together)
        actor_name_lower = path.stem.lower().replace(" ", "")
        text_normalized = re.sub(r"\s+", "", text.lower())
        own_tickers = set()
        for t in body_tickers:
            # If "ACTORNAME...NYSE: TICKER" within ~80 chars, count as own
            for m in re.finditer(rf"\b(?:NYSE|NASDAQ|NYSE Arca|AMEX)\s*:\s*{t}\b", text):
                start = max(0, m.start() - 200)
                ctx = text[start:m.end()].lower().replace(" ", "")
                if actor_name_lower[:8] in ctx or actor_name_lower[-8:] in ctx:
                    own_tickers.add(t)
        if not own_tickers:
            continue
        found += 1
        ticker_str = ", ".join(sorted(own_tickers))
        print(f"  {path.stem:<40} body mentions [{ticker_str}] -> remove #private + update aliases")
    if found == 0:
        print("  (no stale-private notes found)")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--tickers", nargs="*", default=[],
                        help="Candidate IPO tickers to cross-reference against vault + DB")
    parser.add_argument("--scan-stale-private", action="store_true",
                        help="Scan all actor notes for #private + body NYSE/NASDAQ ticker patterns")
    args = parser.parse_args()

    if not args.tickers and not args.scan_stale_private:
        parser.print_help()
        sys.exit(1)

    db_tickers = get_db_tickers()

    if args.tickers:
        print(f"=== IPO debut cross-reference ({len(args.tickers)} tickers) ===")
        for t in args.tickers:
            report_ticker(t.upper(), db_tickers)

    if args.scan_stale_private:
        scan_stale_private()


if __name__ == "__main__":
    main()
