#!/usr/bin/env python3
"""
Probe yfinance coverage for a set of Cboe indices and print a concise report.

- Attempts to download daily history via yfinance for each ticker.
- Reports status (OK/EMPTY/ERROR), row count, first/last date, non-NaN Close count,
  duplicates and monotonic date order.
- Intended to help decide which tickers should be sourced from Cboe CSV instead of Yahoo.

Usage:
  python scripts/probe_cboe_yf_coverage.py --verbose
  python scripts/probe_cboe_yf_coverage.py --tickers ^BXM,^BXMD,^BXY --start 2005-01-01

Note: Makes external HTTP requests.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, date
from typing import List, Tuple, Dict, Any

import pandas as pd

try:
    import yfinance as yf
except Exception as e:
    print("yfinance is required. Please install with: pip install yfinance", file=sys.stderr)
    raise

DEFAULT_TICKERS = [
    # Strategy indices (S&P 500)
    "^BXM", "^BXMD", "^BXY", "^PUT", "^PPUT", "^BXD", "^CLL", "^CLLZ",
    # Volatility family
    "^VVIX", "^SKEW", "^VIX1D", "^VIX9D", "^VIX3M", "^VIX6M",
    # Other index vols
    "^RVX", "^VXN", "^VXD",
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Probe yfinance coverage for Cboe indices")
    p.add_argument("--tickers", type=str, default=",".join(DEFAULT_TICKERS),
                   help="Comma-separated list of tickers to probe")
    p.add_argument("--start", type=str, default="2005-01-01",
                   help="Start date YYYY-MM-DD (default: 2005-01-01)")
    p.add_argument("--end", type=str, default=None,
                   help="End date YYYY-MM-DD (default: today)")
    p.add_argument("--verbose", action="store_true", help="Print extra details per ticker")
    return p.parse_args()


def _fmt_dt(x: Any) -> str:
    if x is None:
        return "-"
    # Handle pandas NaT/NaN early
    try:
        if pd.isna(x):
            return "-"
    except Exception:
        pass
    # Coerce to datetime safely; fallback to string if not a date
    try:
        ts = pd.to_datetime(x, errors="coerce")
        if pd.isna(ts):
            return "-"
        return pd.Timestamp(ts).strftime("%Y-%m-%d")
    except Exception:
        return str(x)


def probe_ticker(ticker: str, start: str | None, end: str | None, verbose: bool) -> Dict[str, Any]:
    """Download via yfinance and return a structured summary."""
    result: Dict[str, Any] = {
        "ticker": ticker,
        "status": "",
        "rows": 0,
        "first_date": None,
        "last_date": None,
        "non_nan_close": 0,
        "dupe_dates": 0,
        "is_monotonic": None,
        "error": None,
    }
    try:
        df = yf.download(
            tickers=ticker,
            start=start if start else None,
            end=end if end else None,
            interval="1d",
            auto_adjust=False,
            progress=False,
            threads=False,
        )
        # yfinance returns empty DataFrame or a MultiIndex in some cases. Normalize.
        if isinstance(df.columns, pd.MultiIndex):
            # Single ticker with multi-level columns -> take the first level (e.g., ('Close', '') style)
            # Or select by ticker level if present.
            if ticker in df.columns.get_level_values(0):
                df = df[ticker]
            else:
                # collapse by taking the first level name when possible
                df.columns = [c[0] for c in df.columns]
        
        if df is None or df.empty:
            result["status"] = "EMPTY"
            return result

        df = df.sort_index()
        result["rows"] = int(len(df))
        result["first_date"] = df.index[0]
        result["last_date"] = df.index[-1]
        if "Close" in df.columns:
            result["non_nan_close"] = int(df["Close"].notna().sum())
        else:
            # Some indices might come with 'Adj Close' only; count non-nan across any value column
            value_cols = [c for c in ["Close", "Adj Close", "close", "adjclose"] if c in df.columns]
            if value_cols:
                result["non_nan_close"] = int(df[value_cols[0]].notna().sum())

        # Check duplicates and monotonicity of index
        dupe_mask = df.index.duplicated(keep=False)
        result["dupe_dates"] = int(dupe_mask.sum())
        result["is_monotonic"] = bool(df.index.is_monotonic_increasing)

        result["status"] = "OK"
        if verbose:
            tail_cols = [c for c in ["Close", "Adj Close"] if c in df.columns]
            print(f"\n[{ticker}] sample tail:")
            print(df[tail_cols].tail(3) if tail_cols else df.tail(3))

        return result
    except Exception as e:
        result["status"] = "ERROR"
        result["error"] = str(e)
        return result


def main() -> int:
    args = parse_args()
    tickers: List[str] = [t.strip() for t in args.tickers.split(",") if t.strip()]
    start = args.start
    end = args.end
    verbose = args.verbose

    print("Probing yfinance coverage for tickers (daily):")
    print(", ".join(tickers))

    summaries: List[Dict[str, Any]] = []
    for t in tickers:
        s = probe_ticker(t, start, end, verbose)
        summaries.append(s)

    # Render summary table
    df = pd.DataFrame(summaries)
    cols = [
        "ticker", "status", "rows",
        "first_date", "last_date", "non_nan_close",
        "dupe_dates", "is_monotonic", "error",
    ]
    df = df[cols]

    # Format date columns for printing
    df_print = df.copy()
    df_print["first_date"] = df_print["first_date"].map(_fmt_dt)
    df_print["last_date"] = df_print["last_date"].map(_fmt_dt)

    print("\nSummary:")
    try:
        # Nice tabular display if available
        from tabulate import tabulate  # type: ignore
        print(tabulate(df_print, headers="keys", tablefmt="github", showindex=False))
    except Exception:
        print(df_print.to_string(index=False))

    # Quick guidance: which should use Cboe direct ingestion
    missing_or_bad = df[(df["status"] != "OK") | (df["rows"] <= 5)]
    if not missing_or_bad.empty:
        print("\nCandidates for Cboe CSV ingestion (missing/empty/too short):")
        for _, r in missing_or_bad.iterrows():
            print(f"- {r['ticker']}: status={r['status']}, rows={r['rows']}, error={r['error']}")
    else:
        print("\nAll probed tickers returned usable data from yfinance.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
