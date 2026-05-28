"""Audit vault actor notes for ticker / alias / DB completeness.

The Phase 0 mover screen ([[quick_movers.py]]) reads candidate tickers from
each actor note's `aliases:` frontmatter field and `| Tickers? | XXX |` table
cells. Notes that mention a ticker in the body (e.g., "NYSE: HAWK") but don't
expose it in either of those two places are invisible to the screen.

This script scans investing/Actors/*.md and reports three classes of gaps:

1. Body-mentioned ticker NOT in aliases (Phase 0 invisible). Both [[Chime]]
   (CHYM, mentioned in body but missing from aliases pre-2026-05-07) and
   [[HawkEye 360]] (HAWK, ditto) were silently slipping through Phase 0
   because of this exact gap.

2. Aliases-listed ticker NOT in prices_long. Surface candidates for
   `python scripts/add_ticker.py TICKER` so the screen has fresh data.

3. Notes tagged #private with a NYSE: / NASDAQ: pattern in body. Likely
   IPO'd; flag for status-update + alias-update + DB add.

Usage:
    python scripts/audit_vault_tickers.py                # human-readable report
    python scripts/audit_vault_tickers.py --json         # machine-readable
    python scripts/audit_vault_tickers.py --fix-aliases  # auto-add detected tickers to aliases (dangerous; review diff)
"""
import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - repo tooling normally has PyYAML
    yaml = None

ROOT = Path(__file__).parent.parent
ACTORS = ROOT / "investing" / "Actors"
DB = ROOT / "market_data.db"

# Tickers regex - 1-6 uppercase letters, possibly with dot for foreign exchanges
# (e.g., HINDALCO.NS, 7203.T). For body extraction we only look at simple US tickers.
TICKER_RE = re.compile(r"^[A-Z]{1,6}$")
SKIP = {
    "AI", "US", "UK", "EU", "HQ", "PE", "RE", "DC", "VC", "CEO", "CTO", "COO",
    "CFO", "IPO", "SA", "SE", "AG", "NV", "AB", "LP", "NA", "AM", "GP", "BE",
    "IT", "OR", "ON", "TD", "BN", "BAM", "PR", "PM", "RFP", "SEC", "FED", "GDP",
    "CPI", "PMI", "FX", "ARM", "DC", "USA", "USD", "EUR", "JPY", "CNY", "GBP",
    "QE", "QT", "ECB", "DOJ", "DOD",
}

# Body-mentioned ticker patterns. Order matters: the first pattern that matches
# wins. Each pattern must capture the ticker symbol in group 1.
BODY_TICKER_PATTERNS = [
    # "NYSE: HAWK", "NASDAQ: CHYM"
    re.compile(r"\b(?:NYSE|NASDAQ|NYSE Arca|AMEX)\s*:\s*([A-Z]{1,6})\b"),
    # "(NYSE: HAWK)", "(NASDAQ:CHYM)"
    re.compile(r"\((?:NYSE|NASDAQ|NYSE Arca|AMEX)\s*:\s*([A-Z]{1,6})\)"),
    # "Ticker: HAWK"
    re.compile(r"\bTicker\s*:\s*([A-Z]{1,6})\b", re.IGNORECASE),
    # "trades as HAWK", "trades as CHYM on NASDAQ"
    re.compile(r"\btrades?\s+as\s+([A-Z]{1,6})\b"),
]


def parse_frontmatter(text):
    """Return YAML frontmatter as a dict when present and parseable."""
    if yaml is None or not text.startswith("---"):
        return {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*", text, re.DOTALL)
    if not match:
        return {}
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def list_field(data, key):
    value = data.get(key)
    if isinstance(value, list):
        return [str(item).strip().strip("'\"") for item in value if str(item).strip()]
    if isinstance(value, str):
        text = value.strip()
        if text.startswith("[") and text.endswith("]"):
            text = text[1:-1]
        return [item.strip().strip("'\"") for item in text.split(",") if item.strip()]
    return []


def extract_aliases(text):
    """Return exposed ticker aliases plus the raw aliases/ticker list."""
    fm = parse_frontmatter(text)
    raw = list_field(fm, "aliases") + list_field(fm, "ticker")
    if not raw:
        # Legacy fallback for malformed notes without parseable frontmatter.
        m = re.search(r"^aliases:\s*\[(.*?)\]", text, flags=re.MULTILINE)
        if m:
            raw = [a.strip().strip("'\"") for a in m.group(1).split(",") if a.strip()]
    tickers = set()
    for item in raw:
        token = item.upper()
        for candidate in (token, re.split(r"[-.]", token)[0]):
            if TICKER_RE.match(candidate) and candidate not in SKIP:
                tickers.add(candidate)
    return tickers, raw


def extract_table_tickers(text):
    """Return tickers from `| Ticker[s] | XXX |` table cells."""
    matches = re.findall(r"\|\s*Tickers?\s*\|\s*([^\|]+)\|", text, flags=re.IGNORECASE)
    found = set()
    for cell in matches:
        for part in re.split(r"[,;]", cell.strip()):
            m = re.match(r"([A-Z]{1,6})", part.strip())
            if m and m.group(1) not in SKIP:
                found.add(m.group(1))
    return found


def _name_marker(name):
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def _looks_like_own_ticker(text, match, actor_name):
    """Heuristic: exchange/trades-as mentions must name this actor nearby first."""
    if not actor_name:
        return True
    marker = _name_marker(actor_name)
    if not marker:
        return True
    before = text[max(0, match.start() - 240):match.start()]
    before = re.sub(r"[^a-z0-9]+", "", before.lower())
    # Prefer the start/end of the stem so "Altice USA" still matches "Altice".
    probes = {marker}
    if len(marker) > 8:
        probes.add(marker[:8])
        probes.add(marker[-8:])
    nearby = text[max(0, match.start() - 120):match.start()]
    nearby_lower = nearby.lower()
    relationship_terms = (
        "subsidiary of",
        "acquired by",
        "owned by",
        "parent",
        "former ticker",
        "formerly",
        "founder of",
        "co-founder of",
        "competitor",
        "buyer",
        "investor",
        "stake",
        "joint venture between",
        "separately listed",
    )
    if any(term in nearby_lower for term in relationship_terms):
        return False

    # If the immediate subject is a wikilink, require that subject to be the
    # current actor. This avoids turning parent/peer tickers into child aliases.
    links = list(re.finditer(r"\[\[([^\]|#]+)", nearby))
    if links and links[-1].end() >= len(nearby) - 40:
        subject = _name_marker(links[-1].group(1))
        return any(probe and probe in subject for probe in probes)

    bold = list(re.finditer(r"\*\*([^*]+)\*\*", nearby))
    if bold and bold[-1].end() >= len(nearby) - 40:
        subject = _name_marker(bold[-1].group(1))
        return any(probe and probe in subject for probe in probes)

    clause = re.split(r"[\n.;|:]", nearby)[-1]
    clause = re.sub(r"[^a-z0-9]+", "", clause.lower())
    return any(probe and probe in clause for probe in probes)


def extract_body_tickers(text, actor_name=None):
    """Return own tickers mentioned in body via NYSE:/NASDAQ:/Ticker: patterns."""
    found = set()
    for pat in BODY_TICKER_PATTERNS:
        for m in pat.finditer(text):
            t = m.group(1).upper()
            # "Ticker: XYZ" is usually an explicit self-description. Exchange
            # and "trades as" mentions often refer to parents, buyers, peers, or
            # counterparties, so require the actor's name nearby before them.
            explicit_ticker_field = pat.pattern.startswith(r"\bTicker")
            if (
                TICKER_RE.match(t)
                and t not in SKIP
                and (explicit_ticker_field or _looks_like_own_ticker(text, m, actor_name))
            ):
                found.add(t)
    return found


def extract_tags(text):
    """Return the set of #tags in the note body."""
    tags = {
        tag
        for tag in list_field(parse_frontmatter(text), "tags")
        if re.match(r"^[a-z][a-z0-9-]*$", tag)
    }
    for m in re.finditer(r"(?:^|\s)#([a-z][a-z0-9-]*)", text):
        tags.add(m.group(1))
    return tags


def get_db_tickers():
    """Return set of tickers present in prices_long."""
    if not DB.exists():
        return set()
    try:
        conn = sqlite3.connect(str(DB))
        rows = conn.execute("SELECT DISTINCT ticker FROM prices_long").fetchall()
        conn.close()
        return {r[0] for r in rows}
    except Exception:
        return set()


def audit_note(path, db_tickers):
    """Return dict of issues for a single actor note."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None

    alias_tickers, _ = extract_aliases(text)
    table_tickers = extract_table_tickers(text)
    body_tickers = extract_body_tickers(text, path.stem)
    tags = extract_tags(text)

    exposed = alias_tickers | table_tickers  # what quick_movers.py sees

    issues = {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "name": path.stem,
        "tags": sorted(tags),
        "exposed_tickers": sorted(exposed),
        "body_tickers": sorted(body_tickers),
    }

    # Gap 1: body mentions ticker but it's not exposed to quick_movers.py
    missing_from_aliases = body_tickers - exposed
    if missing_from_aliases:
        issues["missing_from_aliases"] = sorted(missing_from_aliases)

    # Gap 2: ticker exposed but not in prices_long
    missing_from_db = exposed - db_tickers
    if missing_from_db:
        issues["missing_from_db"] = sorted(missing_from_db)

    # Gap 3: tagged #private but body looks public
    if "private" in tags and body_tickers:
        issues["stale_private_tag"] = True
        issues["likely_public_tickers"] = sorted(body_tickers)

    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON instead of human-readable report")
    parser.add_argument("--only-gaps", action="store_true",
                        help="Hide notes with no detected gaps")
    parser.add_argument("--limit", type=int, default=0,
                        help="Cap number of reported entries (0 = no limit)")
    args = parser.parse_args()

    if not ACTORS.exists():
        print(f"Actors directory not found: {ACTORS}", file=sys.stderr)
        sys.exit(1)

    db_tickers = get_db_tickers()
    if not db_tickers:
        print("Warning: prices_long is empty or unreadable; DB-coverage check disabled.",
              file=sys.stderr)

    notes = sorted(ACTORS.glob("*.md"))
    audited = []
    for p in notes:
        result = audit_note(p, db_tickers)
        if not result:
            continue
        has_gap = any(k in result for k in
                      ("missing_from_aliases", "missing_from_db", "stale_private_tag"))
        if args.only_gaps and not has_gap:
            continue
        audited.append(result)

    if args.limit and args.limit > 0:
        audited = audited[: args.limit]

    if args.json:
        print(json.dumps(audited, indent=2))
        return

    # Human-readable summary
    g1 = [a for a in audited if "missing_from_aliases" in a]
    g2 = [a for a in audited if "missing_from_db" in a]
    g3 = [a for a in audited if "stale_private_tag" in a]

    print(f"Vault ticker audit — {len(notes)} actor notes scanned")
    print(f"  prices_long ticker count: {len(db_tickers)}")
    print()
    print(f"Gap 1 — body-mentioned ticker NOT in aliases (Phase 0 invisible): {len(g1)}")
    for r in g1:
        miss = ", ".join(r["missing_from_aliases"])
        print(f"  {r['name']:<40} body has [{miss}]; aliases expose {r['exposed_tickers'] or '[]'}")
    print()
    print(f"Gap 2 — ticker exposed but NOT in prices_long (run add_ticker.py): {len(g2)}")
    for r in g2:
        miss = ", ".join(r["missing_from_db"])
        print(f"  {r['name']:<40} exposed [{miss}] missing from DB")
    print()
    print(f"Gap 3 — tagged #private but body has NYSE/NASDAQ ticker (likely IPO'd): {len(g3)}")
    for r in g3:
        body = ", ".join(r["likely_public_tickers"])
        print(f"  {r['name']:<40} body has public-ticker pattern [{body}]")

    total_gaps = len(g1) + len(g2) + len(g3)
    print()
    print(f"Total gaps: {total_gaps}")
    if total_gaps == 0:
        print("Vault ticker exposure is complete.")


if __name__ == "__main__":
    main()
