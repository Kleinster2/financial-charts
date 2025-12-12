import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import argparse
from datetime import datetime, timedelta

import requests


def check_health(base_url: str, timeout: float):
    """Check /api/health endpoint."""
    url = base_url.rstrip("/") + "/api/health"
    resp = requests.get(url, timeout=timeout)
    if resp.status_code != 200:
        raise RuntimeError(f"/api/health returned {resp.status_code}")
    try:
        return resp.json()
    except Exception:
        return resp.text.strip()


def fetch_data(base_url: str, tickers: list, timeout: float):
    """Fetch price data for given tickers."""
    url = base_url.rstrip("/") + "/api/data"
    resp = requests.get(url, params={"tickers": ",".join(tickers)}, timeout=timeout)
    if resp.status_code != 200:
        raise RuntimeError(f"/api/data returned {resp.status_code}: {resp.text[:200]}")
    return resp.json()


def fetch_revenue(base_url: str, tickers: list, timeout: float):
    """Fetch revenue data for given tickers."""
    url = base_url.rstrip("/") + "/api/revenue"
    resp = requests.get(url, params={"tickers": ",".join(tickers)}, timeout=timeout)
    if resp.status_code != 200:
        raise RuntimeError(f"/api/revenue returned {resp.status_code}: {resp.text[:200]}")
    return resp.json()


def check_ticker_aliases(base_url: str, timeout: float):
    """Check that aliased tickers (e.g., GOOGL→GOOG) return identical data."""
    # Test GOOGL and GOOG - should return identical revenue data
    data = fetch_revenue(base_url, ["GOOG", "GOOGL"], timeout)

    goog_data = data.get("GOOG", [])
    googl_data = data.get("GOOGL", [])

    if not goog_data:
        raise RuntimeError("GOOG revenue data is empty")
    if not googl_data:
        raise RuntimeError("GOOGL revenue data is empty")
    if goog_data != googl_data:
        raise RuntimeError(f"GOOG ({len(goog_data)} pts) != GOOGL ({len(googl_data)} pts) - alias resolution broken")

    return len(goog_data)


def trading_days_ago(n: int) -> datetime:
    """Return date n trading days ago (rough estimate: skip weekends)."""
    today = datetime.now()
    days_back = 0
    result = today
    while days_back < n:
        result -= timedelta(days=1)
        if result.weekday() < 5:  # Mon-Fri
            days_back += 1
    return result


def parse_date(date_val) -> datetime:
    """Parse date from API response (Unix timestamp or date string)."""
    # Handle Unix timestamp (integer or float)
    if isinstance(date_val, (int, float)):
        return datetime.fromtimestamp(date_val)

    # Handle date strings
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(date_val, fmt)
        except ValueError:
            continue
    raise ValueError(f"Cannot parse date: {date_val}")


def main():
    parser = argparse.ArgumentParser(
        description="Post-update smoke check: verify API responds and key tickers have fresh data."
    )
    parser.add_argument(
        "--base-url",
        default="http://localhost:5000",
        help="Flask API base URL (default: http://localhost:5000)",
    )
    parser.add_argument(
        "--tickers",
        default="SPY,AAPL,QQQ",
        help="Comma-separated tickers to check (default: SPY,AAPL,QQQ)",
    )
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=2,
        help="Max trading days since last data point (default: 2)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="Request timeout in seconds (default: 10)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only print on failure",
    )
    args = parser.parse_args()

    tickers = [t.strip().upper() for t in args.tickers.split(",") if t.strip()]
    errors = []

    # Check health
    try:
        health = check_health(args.base_url, args.timeout)
        if not args.quiet:
            print(f"[OK] /api/health: {health}")
    except Exception as e:
        errors.append(f"/api/health failed: {e}")
        print(f"[FAIL] /api/health: {e}")

    # Check data freshness
    try:
        data = fetch_data(args.base_url, tickers, args.timeout)
        cutoff = trading_days_ago(args.max_age_days)

        for ticker in tickers:
            if ticker not in data:
                errors.append(f"{ticker}: no data returned")
                print(f"[FAIL] {ticker}: no data returned")
                continue

            ticker_data = data[ticker]
            if not ticker_data:
                errors.append(f"{ticker}: empty data")
                print(f"[FAIL] {ticker}: empty data")
                continue

            # Get latest date
            latest = ticker_data[-1]
            latest_date = parse_date(latest.get("time", latest.get("date", "")))

            if latest_date < cutoff:
                errors.append(f"{ticker}: stale data ({latest_date.date()}, cutoff {cutoff.date()})")
                print(f"[FAIL] {ticker}: stale data - latest {latest_date.date()}, expected >= {cutoff.date()}")
            elif not args.quiet:
                print(f"[OK] {ticker}: latest {latest_date.date()}")

    except Exception as e:
        errors.append(f"/api/data failed: {e}")
        print(f"[FAIL] /api/data: {e}")

    # Check ticker alias resolution (GOOGL → GOOG)
    try:
        count = check_ticker_aliases(args.base_url, args.timeout)
        if not args.quiet:
            print(f"[OK] Ticker aliases: GOOGL=GOOG ({count} revenue points)")
    except Exception as e:
        errors.append(f"Ticker alias check failed: {e}")
        print(f"[FAIL] Ticker aliases: {e}")

    # Summary
    if errors:
        print(f"\nSmoke check FAILED with {len(errors)} error(s)")
        sys.exit(1)
    elif not args.quiet:
        print(f"\nSmoke check PASSED")
    sys.exit(0)


if __name__ == "__main__":
    main()
