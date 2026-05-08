"""IPO debut tracker + private-capital watch — catch capital events that
the standard [[quick_movers.py]] mover screen misses by design.

The Phase 0 mover screen needs three things to flag a name:
1. The actor note's `aliases:` or `| Ticker |` cell exposes the ticker.
2. The ticker has price history in `prices_long` (>= 60 sessions for vol).
3. The latest close lands on the SPY session date.

Three failure modes surfaced today (May 7, 2026):
- [[Chime]] -7.5%: missed because CHYM was not in `aliases:` (stale-alias miss)
- [[HawkEye 360]] +30% IPO: missed because HAWK had no DB history (IPO-day miss)
- [[Kalshi]] $1B Series F: missed because Kalshi is private (private-capital miss)

This tool addresses all three blind-spots:

USAGE
-----
    # Mode 1: cross-reference IPO tickers against vault + DB
    python scripts/ipo_debut_tracker.py --tickers HAWK CHYM KLAR

    # Mode 2: scan vault for #private notes that have IPO'd (body has
    # NYSE: / NASDAQ: pattern) -> likely status-tag-stale
    python scripts/ipo_debut_tracker.py --scan-stale-private

    # Mode 3: private-capital watch — show last funding round + age for
    # tracked pre-IPO actors. Highlight rounds > N days old.
    python scripts/ipo_debut_tracker.py --private-watch
    python scripts/ipo_debut_tracker.py --private-watch --stale-days 60
    python scripts/ipo_debut_tracker.py --private-watch --actors Kalshi Anthropic

OUTPUT
------
For each candidate, the tool reports:
- Whether the ticker is in `prices_long` (data ingested?)
- Whether a vault actor note exists (file by name OR alias OR ticker pattern)
- Whether the actor note is tagged #private (status stale?)
- Suggested action (add_ticker.py, edit aliases, update tag)

For --private-watch:
- Last funding round + date + valuation per tracked actor
- Days since last round (highlighted if > --stale-days threshold)
- Vault-note presence check
"""
import argparse
import re
import sqlite3
import sys
from datetime import datetime, date
from pathlib import Path

ROOT = Path(__file__).parent.parent
ACTORS = ROOT / "investing" / "Actors"
DB = ROOT / "market_data.db"

# Default tracked private-company watch list. Largest pre-IPO names whose
# capital events are vault-relevant but invisible to quick_movers.py.
# Order is rough valuation rank (highest first) but doesn't have to be exact.
DEFAULT_PRIVATE_WATCH = [
    # Megacap AI / infra
    "OpenAI", "Anthropic", "SpaceX", "xAI", "Stripe", "Databricks",
    # Prediction markets / fintech
    "Kalshi", "Polymarket", "Klarna", "Mercury", "Brex", "Ramp", "Plaid",
    # AI tooling
    "Cursor", "Anysphere", "Mistral", "ElevenLabs", "Cohere", "Perplexity",
    "Replit", "Glean", "Harvey", "EvenUp", "Suno", "Runway", "Sierra",
    # Consumer / design
    "Canva", "Figma", "Discord",
]

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


# Funding-section heading patterns (case-insensitive).
FUNDING_HEADERS = re.compile(
    r"^\s{0,3}#{2,3}\s+(funding\s+(?:rounds?|history)|cap\s+table|valuation\s+history)\s*$",
    re.IGNORECASE | re.MULTILINE,
)

# Date patterns commonly found in funding tables. Returns (date_obj, raw).
DATE_PATTERNS = [
    # "May 7, 2026", "Oct 2025"
    re.compile(r"(?P<full>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(?P<d>\d{1,2})?,?\s*(?P<y>\d{4}))"),
    # "2026-05-07", "2026-05"
    re.compile(r"(?P<full>(?P<y>\d{4})-(?P<m>\d{2})(?:-(?P<d>\d{2}))?)"),
    # Bare year "2024"
    re.compile(r"(?P<full>(?P<y>\d{4}))"),
]

MONTH_MAP = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], start=1)}


def parse_round_date(text):
    """Best-effort parse of 'Date' cell in a funding table. Returns date or None."""
    text = (text or "").strip().strip("|").strip()
    if not text or text in {"-", "—", "TBD", "?"}:
        return None
    # ISO first
    m = re.search(r"(\d{4})-(\d{2})(?:-(\d{2}))?", text)
    if m:
        try:
            y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3) or 1)
            return date(y, mo, d)
        except Exception:
            pass
    # Month + year
    m = re.search(
        r"\b(?P<mo>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(?:(?P<d>\d{1,2})\s*,\s*)?(?P<y>\d{4})",
        text, re.IGNORECASE)
    if m:
        try:
            mo = MONTH_MAP[m.group("mo").lower()[:3]]
            y = int(m.group("y"))
            d = int(m.group("d") or 1)
            return date(y, mo, d)
        except Exception:
            pass
    # Bare year
    m = re.search(r"\b(\d{4})\b", text)
    if m:
        try:
            return date(int(m.group(1)), 1, 1)
        except Exception:
            pass
    return None


def extract_latest_round(text):
    """Find the latest funding-round row in the actor note. Returns dict or None."""
    # Locate funding section
    m = FUNDING_HEADERS.search(text)
    if not m:
        return None
    section_start = m.end()
    # Section runs until the next ## heading (or end of file)
    next_h = re.search(r"^\s{0,3}#{2}\s+\S", text[section_start:], re.MULTILINE)
    section = text[section_start: section_start + next_h.start()] if next_h else text[section_start:]

    # Parse markdown table rows. Skip header + separator rows.
    rows = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("|-: "):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        rows.append(cells)

    if len(rows) < 2:
        return None
    # First row is header; remaining are data rows
    header = [c.lower() for c in rows[0]]
    data_rows = rows[1:]

    # Identify column indices
    def find_col(*names):
        for i, h in enumerate(header):
            for n in names:
                if n in h:
                    return i
        return None

    i_round = find_col("round")
    i_date = find_col("date", "year", "when")
    i_amount = find_col("amount", "size")
    i_val = find_col("valuation", "value", "post")
    i_lead = find_col("lead", "investor")

    # Pick the row with the most recent parseable date
    best = None
    best_date = None
    for r in data_rows:
        if i_date is None or i_date >= len(r):
            continue
        d = parse_round_date(r[i_date])
        if d is None:
            continue
        if best_date is None or d > best_date:
            best_date = d
            best = r

    if best is None:
        # Fall back to the last row in the table
        best = data_rows[-1]

    return {
        "round": best[i_round] if i_round is not None and i_round < len(best) else "",
        "date": best[i_date] if i_date is not None and i_date < len(best) else "",
        "date_parsed": best_date,
        "amount": best[i_amount] if i_amount is not None and i_amount < len(best) else "",
        "valuation": best[i_val] if i_val is not None and i_val < len(best) else "",
        "lead": best[i_lead] if i_lead is not None and i_lead < len(best) else "",
    }


def find_actor_path(name):
    """Locate an actor note by exact stem match (case-insensitive)."""
    target = name.lower()
    for p in ACTORS.glob("*.md"):
        if p.stem.lower() == target:
            return p
    return None


def report_private_watch(actors, stale_days):
    """Print private-capital watch report for the given actor list."""
    today = date.today()
    print(f"\n=== Private-capital watch ({len(actors)} actors, stale > {stale_days} days) ===")
    print()
    print(f"{'Actor':<20} {'Round':<14} {'Date':<14} {'Amount':<10} {'Valuation':<12} {'Age':>6}  Status")
    print("-" * 100)

    rows = []
    for name in actors:
        path = find_actor_path(name)
        if not path:
            rows.append({
                "name": name,
                "missing_note": True,
                "round": "", "date": "", "amount": "", "valuation": "",
                "age_days": None, "stale": False,
            })
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        latest = extract_latest_round(text)
        if not latest:
            rows.append({
                "name": name,
                "missing_note": False,
                "no_funding_section": True,
                "round": "", "date": "", "amount": "", "valuation": "",
                "age_days": None, "stale": False,
            })
            continue
        d = latest["date_parsed"]
        age = (today - d).days if d else None
        rows.append({
            "name": name,
            "missing_note": False,
            "no_funding_section": False,
            "round": latest["round"][:14],
            "date": latest["date"][:14],
            "amount": latest["amount"][:10],
            "valuation": latest["valuation"][:12],
            "age_days": age,
            "stale": age is not None and age > stale_days,
        })

    # Sort by age (youngest first; missing/unknown last)
    rows.sort(key=lambda r: (r.get("age_days") is None, r.get("age_days") or 99999))

    for r in rows:
        if r.get("missing_note"):
            print(f"{r['name']:<20} {'(no actor note found in vault)':<70}")
            continue
        if r.get("no_funding_section"):
            print(f"{r['name']:<20} {'(no funding section in actor note)':<70}")
            continue
        age_str = f"{r['age_days']}d" if r["age_days"] is not None else "?"
        status = "STALE -> verify recent rounds" if r["stale"] else "current"
        print(f"{r['name']:<20} {r['round']:<14} {r['date']:<14} {r['amount']:<10} {r['valuation']:<12} {age_str:>6}  {status}")

    stale_count = sum(1 for r in rows if r.get("stale"))
    missing_count = sum(1 for r in rows if r.get("missing_note") or r.get("no_funding_section"))
    print()
    print(f"Stale (>{stale_days}d): {stale_count}; Missing note or section: {missing_count}; Current: {len(rows) - stale_count - missing_count}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--tickers", nargs="*", default=[],
                        help="Candidate IPO tickers to cross-reference against vault + DB")
    parser.add_argument("--scan-stale-private", action="store_true",
                        help="Scan all actor notes for #private + body NYSE/NASDAQ ticker patterns")
    parser.add_argument("--private-watch", action="store_true",
                        help="Show last funding round + age for tracked pre-IPO private actors")
    parser.add_argument("--actors", nargs="*", default=None,
                        help="Override default private-watch actor list (e.g., --actors Kalshi Anthropic)")
    parser.add_argument("--stale-days", type=int, default=120,
                        help="Highlight rounds older than this (days). Default: 120")
    args = parser.parse_args()

    if not args.tickers and not args.scan_stale_private and not args.private_watch:
        parser.print_help()
        sys.exit(1)

    db_tickers = get_db_tickers()

    if args.tickers:
        print(f"=== IPO debut cross-reference ({len(args.tickers)} tickers) ===")
        for t in args.tickers:
            report_ticker(t.upper(), db_tickers)

    if args.scan_stale_private:
        scan_stale_private()

    if args.private_watch:
        watch_list = args.actors if args.actors else DEFAULT_PRIVATE_WATCH
        report_private_watch(watch_list, args.stale_days)


if __name__ == "__main__":
    main()
