#!/usr/bin/env python3
"""Fetch US Treasury TIC (Treasury International Capital) data and store in market_data.db.

Two datasets:
  1. tic_flows — Net foreign purchases/sales of US long-term securities by asset class
     (Treasuries, agencies, corporate bonds, equities). Per-country, monthly. Jan 2020+.
     Source: slt_table1.txt

  2. tic_holdings — Major foreign holders of US Treasury securities.
     Per-country, monthly. Mar 2000+.
     Source: mfhhis01.csv (full history) + slt_table5.txt (recent 13 months)

Usage:
  python scripts/fetch_tic_data.py              # Fetch both datasets
  python scripts/fetch_tic_data.py --flows       # Flows only
  python scripts/fetch_tic_data.py --holdings    # Holdings only
  python scripts/fetch_tic_data.py --chart       # Generate aggregate flows chart
  python scripts/fetch_tic_data.py --chart --country Japan  # Country-level holdings chart
"""

import argparse
import os
import re
import sqlite3
import sys
from io import StringIO

import pandas as pd
import requests

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "market_data.db")
BASE_URL = "https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Top holders to track individually (rest aggregated as "Other")
TOP_HOLDERS = [
    "Japan", "China, Mainland", "United Kingdom", "Luxembourg", "Canada",
    "Belgium", "Cayman Islands", "Ireland", "France", "Switzerland",
    "Taiwan", "India", "Brazil", "Hong Kong", "Singapore",
    "Saudi Arabia", "Korea, South", "Norway", "Germany", "Australia"
]

# Normalize country names for cleaner output
COUNTRY_MAP = {
    "China, Mainland": "China",
    "Korea, South": "South Korea",
    "United Kingdom": "UK",
}


def fetch_flows():
    """Fetch net foreign flows by asset class (slt_table1.txt)."""
    url = f"{BASE_URL}/slt_table1.txt"
    print(f"Fetching flows from {url} ...")
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    # Parse tab-delimited, skip 8 header rows
    df = pd.read_csv(StringIO(resp.text), sep="\t", skiprows=8)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Expected columns (may vary slightly)
    required = ["country", "date"]
    for col in required:
        if col not in df.columns:
            # Try case-insensitive match
            for c in df.columns:
                if c.lower() == col.lower():
                    df.rename(columns={c: col}, inplace=True)
                    break

    # Filter to rows with valid dates
    df = df[df["date"].notna() & df["date"].str.match(r"^\d{4}-\d{2}$", na=False)].copy()

    # Normalize date to YYYY-MM-DD HH:MM:SS (last day of month)
    df["date"] = pd.to_datetime(df["date"] + "-01") + pd.offsets.MonthEnd(0)
    df["date"] = df["date"].dt.strftime("%Y-%m-%d 00:00:00")

    # Select relevant columns
    flow_cols = {
        "for_lt_treas_pos": "treasury_position",
        "for_lt_treas_net": "treasury_net_flow",
        "for_lt_agcy_pos": "agency_position",
        "for_lt_agcy_net": "agency_net_flow",
        "for_lt_corp_pos": "corporate_position",
        "for_lt_corp_net": "corporate_net_flow",
        "for_lt_eqty_pos": "equity_position",
        "for_lt_eqty_net": "equity_net_flow",
        "for_lt_total_pos": "total_position",
        "for_lt_total_net": "total_net_flow",
    }

    available = {k: v for k, v in flow_cols.items() if k in df.columns}
    if not available:
        print("ERROR: No expected flow columns found. Available columns:")
        print(df.columns.tolist())
        return None

    keep = ["country", "date"] + list(available.keys())
    df = df[keep].rename(columns=available)

    # Convert numeric columns
    for col in available.values():
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print(f"  Parsed {len(df)} rows, {df['date'].nunique()} months, {df['country'].nunique()} countries")
    return df


def fetch_holdings_recent():
    """Fetch recent 13-month major foreign holders (slt_table5.txt)."""
    url = f"{BASE_URL}/slt_table5.txt"
    print(f"Fetching recent holdings from {url} ...")
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    lines = resp.text.strip().split("\n")

    # Find the header row (contains date columns like 2026-01)
    header_idx = None
    for i, line in enumerate(lines):
        if re.search(r"\d{4}-\d{2}", line):
            header_idx = i
            break

    if header_idx is None:
        print("ERROR: Could not find header row in slt_table5.txt")
        return None

    # Parse from header row onward
    df = pd.read_csv(StringIO("\n".join(lines[header_idx:])), sep="\t")
    df.columns = df.columns.str.strip()

    # First column is country
    country_col = df.columns[0]
    date_cols = [c for c in df.columns[1:] if re.match(r"\d{4}-\d{2}", c)]

    if not date_cols:
        print("ERROR: No date columns found")
        return None

    # Melt to long format
    df_long = df[[country_col] + date_cols].melt(
        id_vars=country_col, var_name="date_str", value_name="holdings_billions"
    )
    df_long.rename(columns={country_col: "country"}, inplace=True)

    # Clean
    df_long["country"] = df_long["country"].str.strip()
    df_long = df_long[df_long["country"].notna() & (df_long["country"] != "")]
    df_long["holdings_billions"] = pd.to_numeric(df_long["holdings_billions"], errors="coerce")

    # Normalize date
    df_long["date"] = pd.to_datetime(df_long["date_str"] + "-01") + pd.offsets.MonthEnd(0)
    df_long["date"] = df_long["date"].dt.strftime("%Y-%m-%d 00:00:00")
    df_long.drop(columns=["date_str"], inplace=True)

    print(f"  Parsed {len(df_long)} rows, {df_long['date'].nunique()} months")
    return df_long


def fetch_holdings_history():
    """Fetch full historical major foreign holders (mfhhis01.csv).

    File format: CSV with repeating blocks per year.
    Each block:
      - Month header row: ,Dec,Nov,...,Jan,,
      - Year row: Country,2023,2023,...,2023,,
      - Dash row: ,------,...
      - Data rows: Japan,1136.7,1127.5,...
      - Grand Total row
      - "Of which:" subtotals
      - Blank lines before next block
    """
    import csv

    url = f"{BASE_URL}/mfhhis01.csv"
    print(f"Fetching historical holdings from {url} ...")
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    lines = resp.text.strip().split("\n")

    month_map = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                 "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    month_names = set(month_map.keys())

    all_records = []
    months = []  # Current block's month list (positional)
    current_year = None

    for line in lines:
        # Parse CSV (handles quoted fields like "China, Mainland")
        reader = csv.reader(StringIO(line))
        fields = next(reader, None)
        if not fields:
            continue
        fields = [f.strip() for f in fields]

        # Skip empty/title lines
        if not any(fields):
            continue

        # Detect month header row: first field empty, rest are month names
        if not fields[0] and any(f in month_names for f in fields[1:6]):
            months = fields  # Keep positional alignment
            continue

        # Detect year row: "Country,YYYY,YYYY,..."
        if fields[0] == "Country" and len(fields) > 1:
            year_match = re.match(r"^(\d{4})$", fields[1])
            if year_match:
                current_year = int(year_match.group(1))
            continue

        # Skip dash rows
        if fields[0] == "" and any("---" in f for f in fields):
            continue

        # Skip "Of which:" and subtotal rows
        if fields[0].startswith("Of which") or fields[0].startswith("  "):
            continue

        # Data row: country followed by holdings values
        if current_year and months and fields[0]:
            country = fields[0]

            for i in range(1, min(len(fields), len(months))):
                month_name = months[i] if i < len(months) else ""
                if month_name not in month_map:
                    continue
                val = fields[i]
                if not val or val == "n.a.":
                    continue
                try:
                    h = float(val.replace(",", ""))
                except ValueError:
                    continue

                m = month_map[month_name]
                dt = pd.Timestamp(year=current_year, month=m, day=1) + pd.offsets.MonthEnd(0)
                all_records.append({
                    "country": country,
                    "date": dt.strftime("%Y-%m-%d 00:00:00"),
                    "holdings_billions": h
                })

    df = pd.DataFrame(all_records)
    if df.empty:
        print("WARNING: No records parsed from historical file")
        return df

    # Deduplicate (prefer later entries if overlap)
    df = df.drop_duplicates(subset=["country", "date"], keep="last")
    print(f"  Parsed {len(df)} rows, date range {df['date'].min()} to {df['date'].max()}")
    return df


def store_flows(df, conn):
    """Store flows data in tic_flows table."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tic_flows (
            date TEXT NOT NULL,
            country TEXT NOT NULL,
            treasury_position REAL,
            treasury_net_flow REAL,
            agency_position REAL,
            agency_net_flow REAL,
            corporate_position REAL,
            corporate_net_flow REAL,
            equity_position REAL,
            equity_net_flow REAL,
            total_position REAL,
            total_net_flow REAL,
            PRIMARY KEY (date, country)
        )
    """)

    before = conn.execute("SELECT COUNT(*) FROM tic_flows").fetchone()[0]

    df.to_sql("tic_flows", conn, if_exists="replace", index=False)

    # Recreate index after replace
    conn.execute("CREATE INDEX IF NOT EXISTS idx_tic_flows_date ON tic_flows(date)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_tic_flows_country ON tic_flows(country)")

    after = conn.execute("SELECT COUNT(*) FROM tic_flows").fetchone()[0]
    print(f"  tic_flows: {before} -> {after} rows")


def store_holdings(df, conn):
    """Store holdings data in tic_holdings table."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tic_holdings (
            date TEXT NOT NULL,
            country TEXT NOT NULL,
            holdings_billions REAL,
            PRIMARY KEY (date, country)
        )
    """)

    before = conn.execute("SELECT COUNT(*) FROM tic_holdings").fetchone()[0]

    # Upsert: replace existing rows, add new ones
    for _, row in df.iterrows():
        conn.execute("""
            INSERT OR REPLACE INTO tic_holdings (date, country, holdings_billions)
            VALUES (?, ?, ?)
        """, (row["date"], row["country"], row["holdings_billions"]))

    after = conn.execute("SELECT COUNT(*) FROM tic_holdings").fetchone()[0]
    print(f"  tic_holdings: {before} -> {after} rows")


def generate_flows_chart(conn, output_path=None):
    """Generate Brooks-style aggregate net flows chart by asset class."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    df = pd.read_sql("""
        SELECT date,
               SUM(treasury_net_flow) as treasury,
               SUM(agency_net_flow) as agency,
               SUM(corporate_net_flow) as corporate,
               SUM(equity_net_flow) as equity
        FROM tic_flows
        WHERE country = 'Grand Total' OR country = 'Total'
        GROUP BY date
        ORDER BY date
    """, conn)

    if df.empty:
        # Try summing all countries instead
        df = pd.read_sql("""
            SELECT date,
                   SUM(treasury_net_flow) as treasury,
                   SUM(agency_net_flow) as agency,
                   SUM(corporate_net_flow) as corporate,
                   SUM(equity_net_flow) as equity
            FROM tic_flows
            WHERE country NOT LIKE 'Total%' AND country NOT LIKE 'Grand%'
                  AND country NOT LIKE 'Of Which%'
            GROUP BY date
            ORDER BY date
        """, conn)

    if df.empty:
        print("ERROR: No flow data found for chart")
        return None

    df["date"] = pd.to_datetime(df["date"])

    # Convert millions to billions for readability
    for col in ["treasury", "agency", "corporate", "equity"]:
        df[col] = df[col] / 1000

    # 12-month rolling sum for smoother visualization
    df = df.sort_values("date")
    for col in ["treasury", "agency", "corporate", "equity"]:
        df[f"{col}_12m"] = df[col].rolling(12, min_periods=6).sum()

    fig, ax = plt.subplots(figsize=(14, 7))

    colors = {"treasury": "#d32f2f", "agency": "#ff9800", "corporate": "#1976d2", "equity": "#7b1fa2"}
    labels = {"treasury": "Treasury Notes & Bonds", "agency": "Agency Debt",
              "corporate": "Corporate Debt", "equity": "Equities"}

    for col in ["treasury", "agency", "corporate", "equity"]:
        ax.plot(df["date"], df[f"{col}_12m"], color=colors[col], label=labels[col], linewidth=2)

    ax.axhline(y=0, color="gray", linewidth=0.5, linestyle="--")
    ax.set_ylabel("Net Foreign Purchases ($B, 12-month rolling sum)", fontsize=12)
    ax.set_title("Net Foreign Purchases of US Long-Term Securities", fontsize=14, fontweight="bold")
    ax.legend(loc="upper left", fontsize=11)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.grid(axis="y", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()

    if output_path is None:
        output_path = os.path.join(os.path.dirname(DB_PATH), "investing", "attachments",
                                   "tic-net-foreign-flows.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Chart saved: {output_path}")
    return output_path


def generate_holdings_chart(conn, country=None, output_path=None):
    """Generate top foreign holders chart."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    if country:
        # Single country over time
        df = pd.read_sql("""
            SELECT date, holdings_billions FROM tic_holdings
            WHERE country = ? ORDER BY date
        """, conn, params=[country])

        if df.empty:
            # Try normalized name
            for orig, norm in COUNTRY_MAP.items():
                if norm == country:
                    df = pd.read_sql("""
                        SELECT date, holdings_billions FROM tic_holdings
                        WHERE country = ? ORDER BY date
                    """, conn, params=[orig])
                    break

        if df.empty:
            print(f"ERROR: No holdings data found for {country}")
            return None

        df["date"] = pd.to_datetime(df["date"])

        fig, ax = plt.subplots(figsize=(14, 7))
        ax.plot(df["date"], df["holdings_billions"], color="#1976d2", linewidth=2)
        ax.fill_between(df["date"], df["holdings_billions"], alpha=0.1, color="#1976d2")
        ax.set_ylabel("Holdings ($B)", fontsize=12)
        ax.set_title(f"{country} — US Treasury Holdings", fontsize=14, fontweight="bold")
        ax.grid(axis="y", alpha=0.3)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        slug = country.lower().replace(" ", "-").replace(",", "")
        if output_path is None:
            output_path = os.path.join(os.path.dirname(DB_PATH), "investing", "attachments",
                                       f"tic-holdings-{slug}.png")
    else:
        # Top holders latest snapshot
        df = pd.read_sql("""
            SELECT country, holdings_billions FROM tic_holdings
            WHERE date = (SELECT MAX(date) FROM tic_holdings)
            AND country != 'Grand Total'
            AND country NOT LIKE 'Of which%'
            AND country NOT LIKE 'Of Which%'
            AND country NOT LIKE '  %'
            AND country NOT LIKE 'All Other'
            AND holdings_billions IS NOT NULL
            ORDER BY holdings_billions DESC
            LIMIT 20
        """, conn)

        if df.empty:
            print("ERROR: No holdings data found")
            return None

        # Normalize country names
        df["country"] = df["country"].replace(COUNTRY_MAP)

        fig, ax = plt.subplots(figsize=(14, 8))
        bars = ax.barh(range(len(df)), df["holdings_billions"], color="#1976d2", alpha=0.8)
        ax.set_yticks(range(len(df)))
        ax.set_yticklabels(df["country"], fontsize=11)
        ax.invert_yaxis()
        ax.set_xlabel("Holdings ($B)", fontsize=12)
        ax.set_title("Top Foreign Holders of US Treasury Securities", fontsize=14, fontweight="bold")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        # Add value labels
        for bar, val in zip(bars, df["holdings_billions"]):
            ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2,
                    f"${val:,.0f}B", va="center", fontsize=10)

        if output_path is None:
            output_path = os.path.join(os.path.dirname(DB_PATH), "investing", "attachments",
                                       "tic-holdings-top20.png")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Chart saved: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Fetch US Treasury TIC data")
    parser.add_argument("--flows", action="store_true", help="Fetch flows data only")
    parser.add_argument("--holdings", action="store_true", help="Fetch holdings data only")
    parser.add_argument("--chart", action="store_true", help="Generate charts after fetching")
    parser.add_argument("--country", type=str, help="Country for holdings chart (e.g., Japan)")
    parser.add_argument("--output", type=str, help="Output path for chart")
    args = parser.parse_args()

    # Default: fetch both
    fetch_both = not args.flows and not args.holdings

    conn = sqlite3.connect(DB_PATH)

    try:
        if fetch_both or args.flows:
            df_flows = fetch_flows()
            if df_flows is not None:
                store_flows(df_flows, conn)
                conn.commit()

        if fetch_both or args.holdings:
            # Fetch historical first, then overlay recent
            df_hist = fetch_holdings_history()
            if df_hist is not None and not df_hist.empty:
                store_holdings(df_hist, conn)
                conn.commit()

            df_recent = fetch_holdings_recent()
            if df_recent is not None and not df_recent.empty:
                store_holdings(df_recent, conn)
                conn.commit()

        if args.chart:
            if args.flows or fetch_both:
                generate_flows_chart(conn, args.output)
            if args.holdings or fetch_both or args.country:
                generate_holdings_chart(conn, args.country, args.output)

    finally:
        conn.close()

    print("\nDone.")


if __name__ == "__main__":
    main()
