"""
Fetch income-statement fundamentals from Yahoo Finance (yfinance) into the same
income_statement_annual / income_statement_quarterly tables the chart and Sankey
endpoints read.

This is the fallback source for tickers Alpha Vantage's free tier does not cover —
notably Brazilian B3 names (Yahoo '.SA' suffix), for which fetch_fundamentals.py
(Alpha Vantage) silently returns nothing. Data is stored under the SAME ticker key
as the price series (the Yahoo key, e.g. 'MBRF3.SA'), so
/api/chart/lw?tickers=MBRF3.SA&metrics=revenue,netincome and
/api/chart/sankey?ticker=MBRF3.SA resolve it directly.

Usage:
    python fetch_fundamentals_yf.py MBRF3.SA EQTL3.SA
"""

import sys
import sqlite3
import argparse
from datetime import datetime

import yfinance as yf

from constants import DB_PATH

# our column -> ordered list of candidate yfinance income-statement row labels
ROW_MAP = {
    "total_revenue": ["Total Revenue", "Operating Revenue"],
    "cost_of_revenue": ["Cost Of Revenue", "Reconciled Cost Of Revenue"],
    "gross_profit": ["Gross Profit"],
    "operating_expenses": ["Operating Expense"],
    "operating_income": ["Operating Income", "Total Operating Income As Reported"],
    "ebitda": ["EBITDA", "Normalized EBITDA"],
    "net_income": [
        "Net Income",
        "Net Income Common Stockholders",
        "Net Income From Continuing Operation Net Minority Interest",
    ],
    "eps": ["Diluted EPS", "Basic EPS"],
    "research_and_development": ["Research And Development"],
    "selling_general_administrative": [
        "Selling General And Administration",
        "Selling General And Administrative",
    ],
    "interest_expense": ["Interest Expense", "Interest Expense Non Operating"],
    "income_tax_expense": ["Tax Provision", "Income Tax Expense"],
    "depreciation_amortization": [
        "Reconciled Depreciation",
        "Depreciation And Amortization In Income Statement",
        "Depreciation Amortization Depletion Income Statement",
    ],
}
COLS = list(ROW_MAP.keys())


def _pick(df, labels, col):
    """First non-null float for any candidate label in this period column."""
    for lab in labels:
        if lab in df.index:
            v = df.loc[lab, col]
            try:
                f = float(v)
            except (TypeError, ValueError):
                continue
            if f != f:  # NaN
                continue
            return f
    return None


def _store(ticker, df, table, conn):
    if df is None or getattr(df, "empty", True):
        return 0
    cur = conn.cursor()
    now = datetime.now().isoformat(timespec="seconds")
    colnames = "ticker, fiscal_date_ending, last_updated, " + ", ".join(COLS)
    placeholders = ", ".join(["?"] * (3 + len(COLS)))
    n = 0
    for col in df.columns:  # each period-end date
        try:
            fde = col.date().isoformat()
        except Exception:
            fde = str(col)[:10]
        vals = {k: _pick(df, labels, col) for k, labels in ROW_MAP.items()}
        if vals["gross_profit"] is None and vals["total_revenue"] and vals["cost_of_revenue"]:
            vals["gross_profit"] = vals["total_revenue"] - vals["cost_of_revenue"]
        if not vals["total_revenue"]:
            continue  # a period with no revenue is not a usable row
        cur.execute(
            f"INSERT OR REPLACE INTO {table} ({colnames}) VALUES ({placeholders})",
            [ticker, fde, now] + [vals[c] for c in COLS],
        )
        n += 1
    conn.commit()
    return n


def fetch_ticker(ticker, conn):
    t = yf.Ticker(ticker)
    annual = _store(ticker, getattr(t, "income_stmt", None), "income_statement_annual", conn)
    quarterly = _store(ticker, getattr(t, "quarterly_income_stmt", None), "income_statement_quarterly", conn)
    status = "OK" if (annual or quarterly) else "NO DATA"
    print(f"[{status}] {ticker}: {annual} annual, {quarterly} quarterly income-statement rows")
    return annual + quarterly


def main():
    ap = argparse.ArgumentParser(description="Fetch income-statement fundamentals from Yahoo Finance.")
    ap.add_argument("tickers", nargs="+", help="Yahoo tickers (e.g. MBRF3.SA EQTL3.SA)")
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    total = 0
    for tk in args.tickers:
        tk = tk.strip().upper()
        try:
            total += fetch_ticker(tk, conn)
        except Exception as e:
            print(f"[FAIL] {tk}: {e}")
    conn.close()

    if total == 0:
        print("WARNING: no rows stored for any ticker")
        sys.exit(1)


if __name__ == "__main__":
    main()
