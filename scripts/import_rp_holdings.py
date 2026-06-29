#!/usr/bin/env python3
"""Import Risk Parity vault holdings-tracking composition data into market_data.db.

The RP vault's `10 - Portfolio Tracking/{FUND}/{FUND}-{DATE}.md` notes carry YAML
frontmatter with each fund's asset-class allocation, leverage, and NAV/AUM as of a
date. This script parses that frontmatter (no provider re-fetch needed) and upserts
it into two long-format tables so the composition history is queryable and chartable
alongside prices:

  rp_fund_metrics_long(Date, Fund, Leverage, NAV, AUM)
  rp_allocations_long(Date, Fund, AssetClass, Weight, NotionalPct, RiskPct)

Idempotent: INSERT OR REPLACE keyed on (Date, Fund[, AssetClass]). Re-run as the
tracker adds notes. Date stored as 'YYYY-MM-DD 00:00:00' per the DB date convention.

Usage:
    python scripts/import_rp_holdings.py
"""
import os
import sqlite3
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "market_data.db"
TRACKING = Path(r"C:\Users\klein\obsidian\risk-parity") / "10 - Portfolio Tracking"

FUNDS = ["RPAR", "UPAR", "ALLW", "AOR", "DBMF", "KMLM", "CTA",
         "NTSX", "NTSI", "NTSE", "GDE", "SWAN", "TAIL"]
ASSET_CLASSES = [("bonds", "Bonds"), ("equities", "Equities"),
                 ("tips", "TIPS"), ("commodities", "Commodities")]


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    data = {}
    for line in text[3:end].splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("["):  # skip flow lists (tags)
            continue
        data[k.strip()] = v
    return data


def to_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS rp_fund_metrics_long(
        Date TEXT, Fund TEXT, Leverage REAL, NAV REAL, AUM REAL,
        PRIMARY KEY (Date, Fund))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS rp_allocations_long(
        Date TEXT, Fund TEXT, AssetClass TEXT, Weight REAL, NotionalPct REAL, RiskPct REAL,
        PRIMARY KEY (Date, Fund, AssetClass))""")

    files = m_rows = a_rows = 0
    for fund in FUNDS:
        fdir = TRACKING / fund
        if not fdir.exists():
            continue
        for fp in sorted(fdir.glob(f"{fund}-*.md")):
            fm = parse_frontmatter(fp.read_text(encoding="utf-8"))
            if not fm or "date" not in fm:
                continue
            files += 1
            date = fm["date"].strip()[:10] + " 00:00:00"
            cur.execute("INSERT OR REPLACE INTO rp_fund_metrics_long VALUES (?,?,?,?,?)",
                        (date, fund, to_float(fm.get("leverage")),
                         to_float(fm.get("nav")), to_float(fm.get("aum"))))
            m_rows += 1
            for key, label in ASSET_CLASSES:
                w = to_float(fm.get(key))
                n = to_float(fm.get(key + "_notional"))
                r = to_float(fm.get(key + "_risk"))
                if w is None and n is None and r is None:
                    continue
                cur.execute("INSERT OR REPLACE INTO rp_allocations_long VALUES (?,?,?,?,?,?)",
                            (date, fund, label, w, n, r))
                a_rows += 1
    conn.commit()

    print(f"files parsed: {files}")
    print(f"rp_fund_metrics_long upserts: {m_rows}")
    print(f"rp_allocations_long upserts: {a_rows}")
    print("--- coverage by fund ---")
    for fund in FUNDS:
        row = cur.execute(
            "SELECT COUNT(*), MIN(Date), MAX(Date) FROM rp_fund_metrics_long WHERE Fund=?",
            (fund,)).fetchone()
        if row[0]:
            print(f"  {fund:<5} {row[0]:>4} dates  {row[1][:10]} -> {row[2][:10]}")
    conn.close()


if __name__ == "__main__":
    main()
