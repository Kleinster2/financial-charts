"""
Morning scan — automated pre-market data gathering.

Runs before the AI synthesis step to prepare structured data:
1. Updates market data (stocks, ETFs, ADRs, FX, futures)
2. Runs sigma movers against vault actors
3. Checks earnings calendar for today/this week
4. Outputs structured JSON for the morning briefing skill

Usage:
    python scripts/morning_scan.py [--skip-update] [--output FILE]
"""

import argparse
import json
import os
import sqlite3
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent.parent
DB_PATH = BASEDIR / "market_data.db"
VAULT_DIR = BASEDIR / "investing"
DAILY_DIR = VAULT_DIR / "Daily"


def run_cmd(cmd, cwd=None):
    """Run a command, return (stdout, stderr, returncode)."""
    result = subprocess.run(
        cmd, capture_output=True, text=True,
        cwd=cwd or str(BASEDIR), shell=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def update_market_data():
    """Update prices with a 5-day lookback."""
    print("[1/4] Updating market data...")
    stdout, stderr, rc = run_cmd(
        "python update_market_data.py --lookback 5 --assets stocks etfs adrs fx futures"
    )
    if rc != 0:
        print(f"  WARN: update_market_data exited {rc}")
        if stderr:
            print(f"  {stderr[:500]}")
    else:
        print("  OK")
    return rc == 0


def run_movers():
    """Run quick_movers.py, return parsed output."""
    print("[2/4] Scanning sigma movers...")
    stdout, stderr, rc = run_cmd("python scripts/quick_movers.py --sigma 2.5")
    if rc != 0:
        print(f"  WARN: quick_movers exited {rc}")
        return []

    movers = []
    for line in stdout.split("\n"):
        line = line.strip()
        if not line or line.startswith("=") or line.startswith("Scanning") or line.startswith("Found"):
            continue
        # Parse output lines — format varies, capture what we can
        movers.append(line)

    print(f"  Found {len(movers)} mover(s)")
    return movers


def check_earnings_calendar():
    """Check for upcoming earnings from vault actors using DB metadata."""
    print("[3/4] Checking earnings calendar...")
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
    """Check when data was last updated."""
    print("[4/4] Checking data freshness...")
    if not DB_PATH.exists():
        return None

    conn = sqlite3.connect(str(DB_PATH))
    try:
        cursor = conn.execute("""
            SELECT MAX(Date) FROM stock_prices_daily
        """)
        row = cursor.fetchone()
        if row and row[0]:
            print(f"  Latest price date: {row[0]}")
            return row[0]
        return None
    except Exception as e:
        print(f"  WARN: {e}")
        return None
    finally:
        conn.close()


def check_daily_note_exists(date_str):
    """Check if today's daily note exists."""
    path = DAILY_DIR / f"{date_str}.md"
    return path.exists()


def main():
    parser = argparse.ArgumentParser(description="Morning scan — pre-market data gathering")
    parser.add_argument("--skip-update", action="store_true",
                        help="Skip market data update (use existing data)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON file (default: stdout)")
    args = parser.parse_args()

    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Morning scan — {today}")
    print("=" * 50)

    # Step 1: Update market data
    update_ok = True
    if not args.skip_update:
        update_ok = update_market_data()
    else:
        print("[1/4] Skipping market data update")

    # Step 2: Sigma movers
    movers = run_movers()

    # Step 3: Earnings calendar
    earnings = check_earnings_calendar()

    # Step 4: Data freshness
    latest_date = check_data_freshness()

    # Check daily note
    daily_exists = check_daily_note_exists(today)

    # Build output
    result = {
        "scan_date": today,
        "scan_time": datetime.now().strftime("%H:%M:%S"),
        "data_update_ok": update_ok,
        "latest_price_date": latest_date,
        "daily_note_exists": daily_exists,
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
