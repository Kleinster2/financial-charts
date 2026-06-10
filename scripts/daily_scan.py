"""
Daily scan — automated market data gathering for the /daily-scan skill.

Runs before the AI synthesis step to prepare structured data:
1. Updates market data across all configured asset groups
2. Runs sigma movers against vault actors
3. Checks earnings calendar for today/this week
4. Checks prediction-market overlay freshness
5. Outputs structured JSON for the daily briefing skill

Renamed from morning_scan.py 2026-05-19 — the script is time-of-day agnostic.

Usage:
    python scripts/daily_scan.py [--skip-update] [--output FILE] [--write-daily-note]
"""

import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent.parent
DB_PATH = BASEDIR / "market_data.db"
VAULT_DIR = BASEDIR / "investing"
DAILY_DIR = VAULT_DIR / "Daily"
ANALYSTS_DIR = VAULT_DIR / "Analysts"
ACTORS_DIR = VAULT_DIR / "Actors"
ANALYST_WATCHLIST = BASEDIR / "docs" / "analyst-watchlist.md"


def run_cmd(cmd, cwd=None):
    """Run a command, return (stdout, stderr, returncode)."""
    result = subprocess.run(
        cmd, capture_output=True, text=True,
        cwd=cwd or str(BASEDIR), shell=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def update_market_data():
    """Update all configured market data; FRED applies a monthly-safe lookback floor."""
    print("[1/6] Updating market data...")
    stdout, stderr, rc = run_cmd(
        "python update_market_data.py --lookback 5 --assets all"
    )
    if rc != 0:
        print(f"  WARN: update_market_data exited {rc}")
        if stderr:
            print(f"  {stderr[:500]}")
    else:
        print("  OK")
    return rc == 0


def run_movers():
    """Run quick_movers.py with three-trigger defaults and return structured movers."""
    print("[2/6] Scanning sigma movers...")
    stdout, stderr, rc = run_cmd(
        "python scripts/quick_movers.py --json --sigma 2.5 --high-vol-sigma 2.0 --pct-floor 6.0"
    )
    if rc != 0:
        print(f"  WARN: quick_movers exited {rc}")
        return []

    # Informational lines (backend, skip counts, SPY return) precede the JSON
    # block on stdout; none of them contain a brace.
    json_start = stdout.find("{")
    if json_start == -1:
        print("  WARN: no JSON found in quick_movers output")
        return []
    try:
        data = json.loads(stdout[json_start:])
    except json.JSONDecodeError as e:
        print(f"  WARN: could not parse quick_movers JSON: {e}")
        return []

    movers = data.get("movers", [])
    for m in movers:
        if isinstance(m.get("trigger"), list):
            m["trigger"] = ", ".join(m["trigger"])
    print(f"  Found {len(movers)} mover(s)")
    return movers


def check_earnings_calendar():
    """Check for upcoming earnings from vault actors using DB metadata."""
    print("[3/6] Checking earnings calendar...")
    if not DB_PATH.exists():
        print("  WARN: market_data.db not found")
        return []

    # Check income_statement_quarterly for most recent entries
    # to identify which vault actors reported recently
    conn = sqlite3.connect(str(DB_PATH))
    try:
        # Get tickers that have quarterly data
        cursor = conn.execute("""
            SELECT DISTINCT ticker, MAX(fiscal_date_ending) as last_report
            FROM income_statement_quarterly
            GROUP BY ticker
            ORDER BY last_report DESC
            LIMIT 20
        """)
        recent = cursor.fetchall()
        print(f"  {len(recent)} tickers with quarterly data")
        return [{"ticker": r[0], "last_report": r[1]} for r in recent]
    except Exception as e:
        print(f"  WARN: {e}")
        return []
    finally:
        conn.close()


def check_data_freshness():
    """Check when canonical price data was last updated."""
    print("[4/6] Checking data freshness...")
    if not DB_PATH.exists():
        return None

    conn = sqlite3.connect(str(DB_PATH))
    try:
        cursor = conn.execute("""
            SELECT MAX(Date)
            FROM prices_long
            WHERE Ticker = 'SPY'
              AND Close IS NOT NULL
        """)
        row = cursor.fetchone()
        if row and row[0]:
            print(f"  Latest canonical price date (SPY): {row[0]}")
            return row[0]

        # Compatibility fallback for pre-narrow sample databases.
        cursor = conn.execute("""
            SELECT MAX(Date)
            FROM stock_prices_daily
            WHERE SPY IS NOT NULL
        """)
        row = cursor.fetchone()
        if row and row[0]:
            print(f"  Latest legacy wide price date (SPY): {row[0]}")
            return row[0]

        return None
    except Exception as e:
        print(f"  WARN: {e}")
        return None
    finally:
        conn.close()


def check_prediction_market_watchlist():
    """Run offline prediction-market overlay freshness check."""
    print("[5/6] Checking prediction-market overlay freshness...")
    script = BASEDIR / "scripts" / "refresh_kalshi_watchlist.py"
    config = BASEDIR / "kalshi_watchlist.yml"
    if not script.exists() or not config.exists():
        print("  WARN: prediction-market watchlist tooling not found")
        return None

    result = subprocess.run(
        [sys.executable, str(script), "--json"],
        cwd=str(BASEDIR),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  WARN: prediction-market watchlist exited {result.returncode}")
        if result.stderr:
            print(f"  {result.stderr[:500]}")
        return {"error": result.stderr.strip() or result.stdout.strip()}

    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        print(f"  WARN: could not parse prediction-market watchlist JSON: {exc}")
        return {"error": result.stdout[:500]}

    counts = payload.get("counts", {})
    comparisons = len(payload.get("comparisons") or [])
    print(
        "  "
        f"{comparisons} comparisons, "
        f"{counts.get('stale', 0)} stale, "
        f"{counts.get('material', 0)} material, "
        f"{counts.get('review', 0)} review"
    )
    return payload


def _extract_watchlist_names(text: str) -> list[str]:
    """Return analyst names from docs/analyst-watchlist.md table links."""
    names: list[str] = []
    seen: set[str] = set()

    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        match = re.search(r"\|\s*\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", line)
        if not match:
            continue
        name = match.group(1).strip()
        if name and name not in seen:
            names.append(name)
            seen.add(name)

    return names


def resolve_analyst_note(name: str) -> dict:
    """Resolve an analyst source-person note, preferring Analysts/ over Actors/."""
    candidates = [
        ("Analysts", ANALYSTS_DIR / f"{name}.md"),
        ("Actors", ACTORS_DIR / f"{name}.md"),
    ]
    for folder, path in candidates:
        if path.exists():
            return {
                "name": name,
                "folder": folder,
                "path": str(path.relative_to(BASEDIR)).replace("\\", "/"),
                "status": "ok",
            }
    return {
        "name": name,
        "folder": None,
        "path": None,
        "status": "missing",
    }


def check_analyst_watchlist_notes():
    """Check that tracked analyst notes resolve, preferring investing/Analysts."""
    print("[6/6] Resolving analyst watchlist notes...")
    if not ANALYST_WATCHLIST.exists():
        print("  WARN: docs/analyst-watchlist.md not found")
        return {"error": "docs/analyst-watchlist.md not found", "analysts": []}

    text = ANALYST_WATCHLIST.read_text(encoding="utf-8")
    names = _extract_watchlist_names(text)
    analysts = [resolve_analyst_note(name) for name in names]
    missing = [row["name"] for row in analysts if row["status"] != "ok"]
    fallback = [row["name"] for row in analysts if row["folder"] == "Actors"]

    print(f"  {len(analysts)} tracked, {len(missing)} missing, {len(fallback)} still in Actors/")
    return {
        "source": str(ANALYST_WATCHLIST.relative_to(BASEDIR)).replace("\\", "/"),
        "analysts": analysts,
        "missing": missing,
        "fallback_actors": fallback,
    }


def check_daily_note_exists(date_str):
    """Check if today's daily note exists."""
    path = DAILY_DIR / f"{date_str}.md"
    return path.exists()


def write_movers_section(movers: list[dict], date_str: str, latest_price_date: str | None):
    """Append a ready-to-use Quick Movers section to the daily note."""
    if not movers:
        print("  [write-daily-note] No movers to record.")
        return

    daily_path = DAILY_DIR / f"{date_str}.md"
    daily_path.parent.mkdir(parents=True, exist_ok=True)

    # Avoid duplicate section if already present
    existing = ""
    if daily_path.exists():
        existing = daily_path.read_text(encoding="utf-8")
        if "## Quick Movers" in existing:
            print("  [write-daily-note] Section already present; skipping.")
            return

    header = f"## Quick Movers — {date_str}"
    subhead = (
        f"*Beta-adjusted idiosyncratic moves (three-trigger: σ≥2.5 / high-vol σ≥2.0 / ≥6% abs). "
        f"Data as of {latest_price_date or 'latest session'}.*"
    )

    lines = [header, "", subhead, "", "| Ticker | Actor | Δ% | σ | Trigger | β | Idio Vol |", "|--------|-------|----|---|---------|---|----------|"]

    for m in movers:
        ticker = m.get("ticker", "")
        actor = m.get("actor", ticker)
        # Make actor a wikilink if it looks like a note name
        actor_link = f"[[{actor}]]" if actor and not actor.startswith("(") else actor
        change = m.get("change_pct", 0)
        sign = "+" if change > 0 else ""
        sigma = m.get("sigma", 0)
        trigger = m.get("trigger", "")
        beta = m.get("beta", 0)
        idio = m.get("idio_vol", 0)
        lines.append(
            f"| {ticker} | {actor_link} | {sign}{change:.1f}% | {sigma:.1f}s | {trigger} | {beta:.2f}x | {idio:.0f}% |"
        )

    lines.append("")
    lines.append("_Generated by daily_scan.py --write-daily-note_")
    section = "\n".join(lines)

    with daily_path.open("a", encoding="utf-8") as f:
        if existing and not existing.endswith("\n\n"):
            f.write("\n\n")
        f.write(section + "\n")

    print(f"  [write-daily-note] Appended section to {daily_path.name}")


def main():
    parser = argparse.ArgumentParser(description="Daily scan — market data gathering")
    parser.add_argument("--skip-update", action="store_true",
                        help="Skip market data update (use existing data)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON file (default: stdout)")
    parser.add_argument("--write-daily-note", action="store_true",
                        help="Append a ready-to-use Quick Movers section to investing/Daily/<date>.md")
    args = parser.parse_args()

    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Daily scan — {today}")
    print("=" * 50)

    # Step 1: Update market data
    update_ok = True
    if not args.skip_update:
        update_ok = update_market_data()
    else:
        print("[1/6] Skipping market data update")

    # Step 2: Sigma movers
    movers = run_movers()

    # Step 3: Earnings calendar
    earnings = check_earnings_calendar()

    # Step 4: Data freshness
    latest_date = check_data_freshness()

    if args.write_daily_note:
        write_movers_section(movers, today, latest_date)

    # Step 5: prediction-market overlay freshness
    prediction_market_watchlist = check_prediction_market_watchlist()

    # Step 6: analyst watchlist note paths
    analyst_watchlist = check_analyst_watchlist_notes()

    # Check daily note
    daily_exists = check_daily_note_exists(today)

    # Build output
    result = {
        "scan_date": today,
        "scan_time": datetime.now().strftime("%H:%M:%S"),
        "data_update_ok": update_ok,
        "latest_price_date": latest_date,
        "daily_note_exists": daily_exists,
        "prediction_market_watchlist": prediction_market_watchlist,
        "kalshi_watchlist": prediction_market_watchlist,
        "analyst_watchlist": analyst_watchlist,
        "sigma_movers": movers,
        "recent_earnings": earnings,
    }

    print("\n" + "=" * 50)
    print(f"Scan complete. {len(movers)} movers, {len(earnings)} earnings records.")

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(json.dumps(result, indent=2))
        print(f"Output written to {output_path}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
