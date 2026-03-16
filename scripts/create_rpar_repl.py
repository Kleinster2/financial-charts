#!/usr/bin/env python3
"""
create_rpar_repl.py

RPAR Risk Parity ETF replication using 7-ETF proxies.

Equities:     VTI, VWO, VEA (exact — RPAR holds these directly)
Bonds:        IEF (10yr), TLT (ultra bond) — only from late 2025
TIPS:         TIP (proxy for individual TIPS bonds)
Commodities:  GLDM (exact), GNR (proxy for ~80 commodity stocks)

Reads weight history from Risk Parity vault:
  23 quarterly snapshots (May 2020 - Sep 2025)
  42+ daily snapshots (Jan 2026 onward)

Produces:
  RPAR_REPL      — static weights (latest), 7 ETFs
  RPAR_REPL_DYN  — dynamic weights from all snapshots

Usage:
    python scripts/create_rpar_repl.py [--store]
"""

import sys
import re
import yaml
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from replication_utils import (
    get_prices, compute_returns, build_index,
    interpolate_schedule, interpolate_weight_schedule, store_ticker
)
import sqlite3
import pandas as pd
import numpy as np

DB_PATH = Path(__file__).parent.parent / 'market_data.db'
VAULT_PATH = Path('C:/Users/klein/obsidian/Risk Parity/10 - Portfolio Tracking/RPAR')
BASE_DATE = '2019-12-13'  # RPAR inception in DB

# --- Proxy tickers ---

ALL_TICKERS = ['VTI', 'VWO', 'VEA', 'TIP', 'GLDM', 'GNR', 'IEF', 'TLT']

# --- Sub-weight defaults (within asset classes) ---

# Equity sub-weights (stable: VTI ~51%, VWO ~30%, VEA ~19%)
EQUITY_SUBS = {'VTI': 0.51, 'VWO': 0.30, 'VEA': 0.19}

# Bond sub-weights (only relevant from 2026: IEF ~50.5%, TLT ~49.5%)
BOND_SUBS = {'IEF': 0.505, 'TLT': 0.495}

# Commodity sub-weights: GLDM (gold) + GNR (commodity stocks)
# This ratio evolved: ~66/34 in 2020, ~43/57 in 2026
COMMOD_SUBS_DEFAULT = {'GLDM': 0.50, 'GNR': 0.50}

# --- Static weights (March 2026 notional % of NAV) ---

STATIC_WEIGHTS = {}
eq_pct, bond_pct, tips_pct, commod_pct = 0.246, 0.357, 0.0, 0.270
for t, w in EQUITY_SUBS.items():
    STATIC_WEIGHTS[t] = eq_pct * w
for t, w in BOND_SUBS.items():
    STATIC_WEIGHTS[t] = bond_pct * w
STATIC_WEIGHTS['TIP'] = tips_pct
# Mar 2026 commod: GLDM $68.9M, stocks $91.2M → 43/57
STATIC_WEIGHTS['GLDM'] = commod_pct * 0.43
STATIC_WEIGHTS['GNR'] = commod_pct * 0.57


# ---------------------------------------------------------------------------
# Snapshot parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Parse YAML frontmatter from markdown."""
    if not text.startswith('---'):
        return {}
    end = text.find('---', 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return {}


def parse_dollar_value(text):
    """Extract dollar value from text like '$74.3M'."""
    m = re.search(r'\$?([\d,]+\.?\d*)\s*[Mm]', str(text))
    if m:
        return float(m.group(1).replace(',', ''))
    return 0.0


def parse_snapshot(filepath):
    """Parse an RPAR snapshot file, return weight dict."""
    text = filepath.read_text(encoding='utf-8')
    fm = parse_frontmatter(text)
    if 'date' not in fm:
        return None

    result = {
        'date': str(fm['date']).split(' ')[0],
        'nav': float(fm.get('nav', 0)),
        'leverage': float(fm.get('leverage', 1.0)),
        'equities': float(fm.get('equities_notional', fm.get('equities', 0))) / 100,
        'bonds': float(fm.get('bonds_notional', fm.get('bonds', 0))) / 100,
        'tips': float(fm.get('tips_notional', fm.get('tips', 0))) / 100,
        'commodities': float(fm.get('commodities_notional', fm.get('commodities', 0))) / 100,
    }

    # Parse holdings detail for sub-weights
    gold_val = 0.0
    stock_val = 0.0
    vti_val = vwo_val = vea_val = 0.0
    ief_val = tlt_val = 0.0

    for line in text.split('\n'):
        if '|' not in line or line.strip().startswith('|--') or 'Holding' in line:
            continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if len(cells) < 3:
            continue

        name = cells[0].upper()
        val = 0.0
        for cell in cells:
            v = parse_dollar_value(cell)
            if v > 0:
                val = v
                break

        if val == 0:
            continue

        # Classify
        if 'VTI' in cells[1] if len(cells) > 1 else '' or 'TOTAL STOCK' in name:
            vti_val = val
        elif 'VWO' in (cells[1] if len(cells) > 1 else '') or 'EMERGING' in name:
            vwo_val = val
        elif 'VEA' in (cells[1] if len(cells) > 1 else '') or 'DEVELOPED' in name:
            vea_val = val
        elif 'GLDM' in (cells[1] if len(cells) > 1 else '') or 'GOLD MINISHARES' in name:
            gold_val += val
        elif 'BAR' in (cells[1] if len(cells) > 1 else '') or 'GRANITESHARES GOLD' in name:
            gold_val += val  # BAR was used in early years
        elif '10YR' in name or '10-YR' in name:
            ief_val = val
        elif 'ULTRA BOND' in name:
            tlt_val = val

    # Equity sub-weights
    total_eq = vti_val + vwo_val + vea_val
    if total_eq > 0:
        result['eq_vti'] = vti_val / total_eq
        result['eq_vwo'] = vwo_val / total_eq
        result['eq_vea'] = vea_val / total_eq
    else:
        result['eq_vti'] = EQUITY_SUBS['VTI']
        result['eq_vwo'] = EQUITY_SUBS['VWO']
        result['eq_vea'] = EQUITY_SUBS['VEA']

    # Bond sub-weights (only meaningful from 2026)
    total_bond = ief_val + tlt_val
    if total_bond > 0:
        result['bond_ief'] = ief_val / total_bond
        result['bond_tlt'] = tlt_val / total_bond
    else:
        result['bond_ief'] = BOND_SUBS['IEF']
        result['bond_tlt'] = BOND_SUBS['TLT']

    # Commodity sub-weights: gold vs stocks
    # Total commodity = gold + (total_commod_notional - gold)
    total_commod_dollar = result['commodities'] * result['nav'] if result['nav'] > 0 else 0
    if gold_val > 0 and total_commod_dollar > 0:
        result['commod_gldm'] = gold_val / total_commod_dollar
        result['commod_gnr'] = max(0, 1 - result['commod_gldm'])
    else:
        result['commod_gldm'] = COMMOD_SUBS_DEFAULT['GLDM']
        result['commod_gnr'] = COMMOD_SUBS_DEFAULT['GNR']

    return result


def parse_all_snapshots():
    """Parse all RPAR snapshot files."""
    snapshots = []
    for f in sorted(VAULT_PATH.glob('RPAR-*.md')):
        snap = parse_snapshot(f)
        if snap:
            snapshots.append(snap)
    return sorted(snapshots, key=lambda x: x['date'])


# ---------------------------------------------------------------------------
# Dynamic weight builder
# ---------------------------------------------------------------------------

def build_dynamic_weights(snapshots, dates):
    """Build daily weight arrays from snapshot schedule."""
    dates_dt = pd.to_datetime(dates, format='mixed')
    dates_int = dates_dt.astype(np.int64)

    snap_dates = pd.to_datetime([s['date'] for s in snapshots])
    snap_int = snap_dates.astype(np.int64)

    # Asset class weights (notional % of NAV)
    eq = np.interp(dates_int, snap_int, [s['equities'] for s in snapshots])
    bonds = np.interp(dates_int, snap_int, [s['bonds'] for s in snapshots])
    tips = np.interp(dates_int, snap_int, [s['tips'] for s in snapshots])
    commod = np.interp(dates_int, snap_int, [s['commodities'] for s in snapshots])

    # Clamp edges
    eq[dates_dt < snap_dates[0]] = snapshots[0]['equities']
    bonds[dates_dt < snap_dates[0]] = snapshots[0]['bonds']
    tips[dates_dt < snap_dates[0]] = snapshots[0]['tips']
    commod[dates_dt < snap_dates[0]] = snapshots[0]['commodities']
    eq[dates_dt > snap_dates[-1]] = snapshots[-1]['equities']
    bonds[dates_dt > snap_dates[-1]] = snapshots[-1]['bonds']
    tips[dates_dt > snap_dates[-1]] = snapshots[-1]['tips']
    commod[dates_dt > snap_dates[-1]] = snapshots[-1]['commodities']

    # Sub-weights (interpolated)
    eq_vti = np.interp(dates_int, snap_int, [s['eq_vti'] for s in snapshots])
    eq_vwo = np.interp(dates_int, snap_int, [s['eq_vwo'] for s in snapshots])
    eq_vea = np.interp(dates_int, snap_int, [s['eq_vea'] for s in snapshots])
    bond_ief = np.interp(dates_int, snap_int, [s['bond_ief'] for s in snapshots])
    bond_tlt = np.interp(dates_int, snap_int, [s['bond_tlt'] for s in snapshots])
    commod_gldm = np.interp(dates_int, snap_int, [s['commod_gldm'] for s in snapshots])
    commod_gnr = np.interp(dates_int, snap_int, [s['commod_gnr'] for s in snapshots])

    # Build per-ticker weight arrays
    weights = {
        'VTI': eq * eq_vti,
        'VWO': eq * eq_vwo,
        'VEA': eq * eq_vea,
        'IEF': bonds * bond_ief,
        'TLT': bonds * bond_tlt,
        'TIP': tips,
        'GLDM': commod * commod_gldm,
        'GNR': commod * commod_gnr,
    }

    return weights, {'equities': eq, 'bonds': bonds, 'tips': tips, 'commodities': commod}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    store = '--store' in sys.argv

    print(f"\n{'='*60}")
    print("RPAR 7-ETF Replication")
    print(f"{'='*60}\n")

    # Parse snapshots
    snapshots = parse_all_snapshots()
    print(f"Snapshots: {len(snapshots)} ({snapshots[0]['date']} to {snapshots[-1]['date']})")

    # Static weights
    print(f"\nStatic weights (Mar 2026 notional):")
    for t, w in STATIC_WEIGHTS.items():
        print(f"  {t:6s} {w*100:5.1f}%")
    print(f"  {'Total':6s} {sum(STATIC_WEIGHTS.values())*100:5.1f}%")

    # Get prices
    prices_df = get_prices(ALL_TICKERS + ['RPAR'], start_date='2019-12-01')
    print(f"\nPrice data: {len(prices_df)} days")

    returns = compute_returns(prices_df, ALL_TICKERS)
    dates = prices_df['Date'].values

    # RPAR anchor price
    rpar_prices = prices_df[prices_df['RPAR'].notna()]
    base_row = rpar_prices[rpar_prices['Date'].astype(str).str[:10] >= BASE_DATE].iloc[0]
    initial_price = float(base_row['RPAR'])
    print(f"Base: {BASE_DATE}, RPAR = ${initial_price:.2f}")

    # Tier 1: Static weights
    static_vals = build_index(dates, returns, STATIC_WEIGHTS,
                              base_date=BASE_DATE, initial_price=initial_price,
                              financing_rate=0)  # RPAR is unlevered

    # Tier 2: Dynamic weights
    dyn_weights, asset_classes = build_dynamic_weights(snapshots, dates)
    dyn_vals = build_index(dates, returns, dyn_weights,
                           base_date=BASE_DATE, initial_price=initial_price,
                           financing_rate=0)

    # Build result
    result_df = pd.DataFrame({
        'Date': dates,
        'RPAR_REPL': static_vals,
        'RPAR_REPL_DYN': dyn_vals,
    })
    result_df = result_df[result_df['RPAR_REPL'] > 0]

    # Merge RPAR actual
    rpar_df = prices_df[['Date', 'RPAR']].copy()
    rpar_df = rpar_df[rpar_df['RPAR'].notna()]
    result_df = result_df.merge(rpar_df, on='Date', how='inner')

    # Performance
    first = result_df.iloc[0]
    last = result_df.iloc[-1]
    rpar_ret = (last['RPAR'] / first['RPAR'] - 1) * 100
    s_ret = (last['RPAR_REPL'] / first['RPAR_REPL'] - 1) * 100
    d_ret = (last['RPAR_REPL_DYN'] / first['RPAR_REPL_DYN'] - 1) * 100

    print(f"\n{'='*55}")
    print(f"  Period: {str(first['Date'])[:10]} to {str(last['Date'])[:10]}")
    print(f"  RPAR actual:          {rpar_ret:+.2f}%")
    print(f"  RPAR_REPL_DYN:        {d_ret:+.2f}%  (dynamic)")
    print(f"  RPAR_REPL (static):   {s_ret:+.2f}%  (Mar 2026 weights)")
    print(f"  ---")
    print(f"  Residual (vs DYN):    {rpar_ret - d_ret:+.2f}pp")
    print(f"  Residual (vs static): {rpar_ret - s_ret:+.2f}pp")
    print(f"{'='*55}")

    # Snapshot allocation summary
    print(f"\nAllocation evolution:")
    key_dates = [snapshots[0], snapshots[len(snapshots)//4], snapshots[len(snapshots)//2],
                 snapshots[3*len(snapshots)//4], snapshots[-1]]
    for s in key_dates:
        print(f"  {s['date']}: E={s['equities']*100:.1f}% B={s['bonds']*100:.1f}% "
              f"T={s['tips']*100:.1f}% C={s['commodities']*100:.1f}% "
              f"(gold/stocks={s['commod_gldm']*100:.0f}/{s['commod_gnr']*100:.0f})")

    if store:
        for ticker in ['RPAR_REPL', 'RPAR_REPL_DYN']:
            store_ticker(result_df, 'Date', ticker, ticker,
                        f'RPAR 7-ETF Replication {"Dynamic" if "DYN" in ticker else "Static"}',
                        db_path=DB_PATH)

        print(f"\n[DONE] Stored. Chart: /api/chart/lw?tickers=RPAR,RPAR_REPL_DYN,RPAR_REPL"
              f"&start={BASE_DATE}&normalize=true&primary=RPAR")


if __name__ == "__main__":
    main()
