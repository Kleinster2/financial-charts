"""
Data API routes.
Routes: /api/tickers, /api/metadata, /api/ticker-aliases, /api/data, /api/volume
"""
import sqlite3
import logging
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request
import pandas as pd
import numpy as np
from constants import (get_db_connection, USE_DUCKDB, TICKER_ALIASES)
from helpers import DUCKDB_AVAILABLE

# Conditional DuckDB imports
if USE_DUCKDB and DUCKDB_AVAILABLE:
    from duckdb_queries import (
        get_price_data, get_volume_data, get_all_tickers_list,
    )

logger = logging.getLogger(__name__)

data_bp = Blueprint('data', __name__)


@data_bp.route('/api/tickers')
def get_tickers():
    """Provides a sorted list of all available tickers from the database."""
    logger.info("Request received for /api/tickers")
    try:
        # Use DuckDB if enabled
        if USE_DUCKDB and DUCKDB_AVAILABLE:
            tickers = get_all_tickers_list()
            # Add portfolios from SQLite (portfolio data not migrated yet)
            conn = get_db_connection()
            try:
                cursor = conn.execute("SELECT portfolio_id FROM portfolios ORDER BY portfolio_id")
                for row in cursor.fetchall():
                    tickers.append(f"PORTFOLIO_{row[0]}")
            except sqlite3.OperationalError:
                pass
            conn.close()
            tickers = sorted(set(tickers))
            logger.info(f"[DuckDB] Found {len(tickers)} tickers")
            return jsonify(tickers)

        # SQLite fallback
        conn = get_db_connection()
        tickers_set = set()

        # Collect columns from stock table
        try:
            cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
            # PRAGMA returns tuples: (cid, name, type, notnull, dflt_value, pk)
            tickers_set.update(row[1] for row in cursor.fetchall() if row[1] != 'Date')
        except sqlite3.OperationalError:
            logger.warning("Table 'stock_prices_daily' not found.")

        # Collect columns from futures table
        try:
            cursor = conn.execute("PRAGMA table_info(futures_prices_daily)")
            # PRAGMA returns tuples: (cid, name, type, notnull, dflt_value, pk)
            tickers_set.update(row[1] for row in cursor.fetchall() if row[1] != 'Date')
        except sqlite3.OperationalError:
            logger.warning("Table 'futures_prices_daily' not found.")

        # Collect columns from bonds table
        try:
            cursor = conn.execute("PRAGMA table_info(bond_prices_daily)")
            # PRAGMA returns tuples: (cid, name, type, notnull, dflt_value, pk)
            tickers_set.update(row[1] for row in cursor.fetchall() if row[1] != 'Date')
        except sqlite3.OperationalError:
            logger.warning("Table 'bond_prices_daily' not found.")

        # Collect columns from FRED series table
        try:
            cursor = conn.execute("PRAGMA table_info(fred_series)")
            tickers_set.update(row[1] for row in cursor.fetchall() if row[1] != 'Date')
        except sqlite3.OperationalError:
            logger.warning("Table 'fred_series' not found.")

        # Add portfolios
        try:
            cursor = conn.execute("SELECT portfolio_id, name FROM portfolios ORDER BY portfolio_id")
            for row in cursor.fetchall():
                portfolio_id = row[0]
                tickers_set.add(f"PORTFOLIO_{portfolio_id}")
        except sqlite3.OperationalError:
            logger.info("Table 'portfolios' not found - portfolio feature not available.")

        conn.close()
        tickers = sorted(tickers_set)
        logger.info(f"Found {len(tickers)} tickers across stock, futures, bonds, and portfolio tables.")
        if not tickers:
            logger.warning("WARNING: Ticker list is empty. Check if table 'stock_prices_daily' exists and is populated.")
        return jsonify(sorted(tickers))
    except Exception as e:
        logger.error(f"An error occurred in get_tickers: {e}")
        return jsonify([]), 500


@data_bp.route('/api/metadata')
def get_metadata():
    """Return a mapping of ticker -> display name for provided tickers.
    Priority: ticker_metadata.name -> stock_metadata.name -> futures_metadata -> ticker itself.
    Special: ?tickers=ALL returns all available metadata.
    """
    tickers_str = request.args.get('tickers', '')

    # Handle special "ALL" case
    if tickers_str.strip().upper() == 'ALL':
        try:
            conn = get_db_connection()
            names = {}

            # Get all from ticker_metadata
            try:
                df = pd.read_sql("SELECT ticker, name FROM ticker_metadata WHERE name IS NOT NULL AND name != ''", conn)
                for _, row in df.iterrows():
                    names[row['ticker']] = row['name'].strip()
                logger.info(f"/api/metadata: ALL mode returned {len(names)} entries")
            except Exception as e:
                logger.warning(f"/api/metadata: ALL mode failed: {e}")

            conn.close()
            return jsonify(names)
        except Exception as e:
            logger.error(f"/api/metadata ALL error: {e}")
            return jsonify({}), 500

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    # Empty query -> empty JSON
    if not tickers:
        return jsonify({})

    try:
        conn = get_db_connection()
        placeholders = ','.join(['?'] * len(tickers))
        names = {}

        # 1) Try unified ticker_metadata first (if present)
        try:
            q1 = f"SELECT ticker, name FROM ticker_metadata WHERE ticker IN ({placeholders})"
            df1 = pd.read_sql(q1, conn, params=tickers)
            for _, row in df1.iterrows():
                n = (row['name'] or '').strip()
                if n:
                    names[row['ticker']] = n
            logger.info(f"/api/metadata: ticker_metadata hits={len(names)}")
        except Exception as e:
            logger.warning(f"/api/metadata: ticker_metadata lookup skipped/failed: {e}")

        # 2) Fallback to legacy stock_metadata for any missing
        missing = [t for t in tickers if t not in names]
        if missing:
            try:
                ph = ','.join(['?'] * len(missing))
                q2 = f"SELECT ticker, name FROM stock_metadata WHERE ticker IN ({ph})"
                df2 = pd.read_sql(q2, conn, params=missing)
                add = 0
                for _, row in df2.iterrows():
                    n = (row['name'] or '').strip()
                    if n and row['ticker'] not in names:
                        names[row['ticker']] = n
                        add += 1
                logger.info(f"/api/metadata: stock_metadata hits={add}")
            except Exception as e:
                logger.warning(f"/api/metadata: stock_metadata lookup failed: {e}")

        # 3) Check for futures metadata for any remaining missing
        missing = [t for t in tickers if t not in names]
        if missing:
            # Futures metadata hardcoded from download_futures.py
            futures_metadata = {
                "ES=F": "S&P 500 E-Mini",
                "NQ=F": "Nasdaq-100 E-Mini",
                "YM=F": "Dow Jones 30 E-Mini",
                "RTY=F": "Russell 2000 E-Mini",
                "CL=F": "WTI Crude Oil",
                "BZ=F": "Brent Crude Oil",
                "NG=F": "Natural Gas",
                "RB=F": "RBOB Gasoline",
                "GC=F": "Gold",
                "SI=F": "Silver",
                "HG=F": "Copper",
                "PL=F": "Platinum",
                "PA=F": "Palladium",
                "TIO=F": "Iron Ore 62%, CFR China (TSI)",
                "AL=F": "Aluminum",
                "ZI=F": "Zinc",
                "NI=F": "Nickel",
                "HRN00": "HRC Steel (Hot-Rolled Coil) Futures",
                "HRC00": "HRC Steel (Hot-Rolled Coil) Futures",
                "HRE00": "HRC Steel (Hot-Rolled Coil) Futures",
                "DBB": "Invesco DB Base Metals Fund",
                "ZB=F": "30-Year Bond",
                "ZN=F": "10-Year Note",
                "ZF=F": "5-Year Note",
                "ZT=F": "2-Year Note",
                "FGBL=F": "Euro-Bund (Germany 10Y)",
                "DX=F": "US Dollar Index Futures (ICE)",
                "ZC=F": "Corn",
                "ZS=F": "Soybeans",
                "ZW=F": "Wheat (Chicago)",
                "KE=F": "Wheat (Kansas City)",
                "SB=F": "Sugar #11",
                "KC=F": "Coffee",
                "CC=F": "Cocoa",
                "CT=F": "Cotton",
                "OJ=F": "Orange Juice",
            }

            futures_hits = 0
            for ticker in missing:
                if ticker in futures_metadata:
                    names[ticker] = futures_metadata[ticker]
                    futures_hits += 1

            logger.info(f"/api/metadata: futures_metadata hits={futures_hits}")

        conn.close()

        # 4) Final mapping: fallback to ticker itself for any missing
        mapping = {t: names.get(t, t) for t in tickers}
        resolved = sum(1 for t in tickers if mapping[t] != t)
        logger.info(f"/api/metadata: requested={len(tickers)} resolved={resolved} missing={len(tickers)-resolved}")
        return jsonify(mapping)
    except Exception as e:
        logger.error(f"/api/metadata error: {e}")
        return jsonify({}), 500


@data_bp.route('/api/ticker-aliases')
def get_ticker_aliases():
    """
    Return the ticker alias mapping.
    Used for fundamentals where share classes have identical financials.
    Response: { "GOOGL": "GOOG", "BRK-B": "BRK-A", ... }
    """
    return jsonify(TICKER_ALIASES)


@data_bp.route('/api/data')
def get_data():
    """Provides raw historical price data for a list of tickers.

    Query params:
        tickers: comma-separated list of ticker symbols (required)
        interval: 'daily' (default), 'weekly', or 'monthly' (optional)
    """
    tickers_str = request.args.get('tickers')
    if not tickers_str:
        return jsonify({'error': 'At least one ticker is required'}), 400

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    interval = request.args.get('interval', 'daily').lower()

    # Use DuckDB if enabled
    if USE_DUCKDB and DUCKDB_AVAILABLE:
        chart_data = get_price_data(tickers)

        # Apply interval resampling if needed
        if interval in ('weekly', 'monthly'):
            for ticker in chart_data:
                if not chart_data[ticker]:
                    continue
                # Convert to DataFrame for resampling
                df = pd.DataFrame(chart_data[ticker])
                df['Date'] = pd.to_datetime(df['time'], unit='s')
                df = df.set_index('Date')

                if interval == 'weekly':
                    df = df.resample('W-FRI')['value'].last().dropna().reset_index()
                else:  # monthly
                    df = df.resample('M')['value'].last().dropna().reset_index()

                df['time'] = (df['Date'].astype('int64') // 10**9).astype(int)
                chart_data[ticker] = df[['time', 'value']].to_dict(orient='records')

        logger.info(f"[DuckDB] /api/data: returned {len(chart_data)} tickers")
        return jsonify(chart_data)

    # SQLite fallback
    conn = get_db_connection()

    # --- Determine which tickers belong to which table ---
    stock_cols, futures_cols, bond_cols, fred_cols = set(), set(), set(), set()
    try:
        cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
        stock_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass
    try:
        cursor = conn.execute("PRAGMA table_info(futures_prices_daily)")
        futures_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass
    try:
        cursor = conn.execute("PRAGMA table_info(bond_prices_daily)")
        bond_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass
    try:
        cursor = conn.execute("PRAGMA table_info(fred_series)")
        fred_cols = {row['name'] for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        pass

    # Assign each requested ticker to *exactly one* source table to prevent
    # duplicate column names that break pd.concat (InvalidIndexError).
    # Build chart_data per ticker to avoid column duplication issues entirely
    chart_data = {}
    for ticker in tickers:
        # Check futures table first for =F tickers (has more recent data)
        if ticker in futures_cols and ticker.endswith('=F'):
            table = 'futures_prices_daily'
        elif ticker in stock_cols:
            table = 'stock_prices_daily'
        elif ticker in futures_cols:
            table = 'futures_prices_daily'
        elif ticker in bond_cols:
            table = 'bond_prices_daily'
        elif ticker in fred_cols:
            table = 'fred_series'
        else:
            chart_data[ticker] = []
            continue

        q = (
            f'SELECT date(Date) AS Date, MAX("{ticker}") as value '
            f'FROM {table} '
            f'WHERE "{ticker}" IS NOT NULL '
            f'GROUP BY date(Date) '
            f'ORDER BY date(Date) ASC'
        )
        df = pd.read_sql_query(q, conn, parse_dates=['Date'])
        if df.empty:
            chart_data[ticker] = []
            continue
        # Coerce any invalid dates to NaT and drop rows with invalid date or value
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        before = len(df)
        df = df.dropna(subset=['Date', 'value'])
        # Coerce 'value' to numeric in case of mixed types from SQLite/pandas parsing
        try:
            df['value'] = pd.to_numeric(df['value'], errors='coerce')
        except Exception as e:
            logger.warning(f"/api/data: to_numeric failed for {ticker}: {e}")
        df = df.dropna(subset=['value'])
        dropped = before - len(df)
        if dropped:
            logger.warning(f"/api/data: dropped {dropped} invalid rows for {ticker} due to NaT/NaN")
        # Ensure sorted by date
        df = df.sort_values('Date')
        # Normalize to calendar day and collapse by median for each day (always)
        # This protects against mixed 'YYYY-MM-DD' vs 'YYYY-MM-DD 00:00:00' rows
        # and duplicated ingests for the same day.
        day = df['Date'].dt.normalize()
        before_rows = len(df)
        df = df.assign(Date=day).groupby('Date', as_index=False)['value'].median()
        after_rows = len(df)
        dropped_dup = before_rows - after_rows
        if dropped_dup:
            logger.warning(f"/api/data: collapsed duplicate day rows for {ticker}: {dropped_dup} rows dropped")
        # Apply interval aggregation if requested
        if interval == 'weekly':
            # Resample to week-end (Friday) closing prices
            df = df.set_index('Date')
            df = df.resample('W-FRI')['value'].last().dropna().reset_index()
            logger.info(f"/api/data: resampled {ticker} to weekly, rows={len(df)}")
        elif interval == 'monthly':
            # Resample to month-end closing prices
            df = df.set_index('Date')
            df = df.resample('M')['value'].last().dropna().reset_index()
            logger.info(f"/api/data: resampled {ticker} to monthly, rows={len(df)}")

        # Compute unix seconds; guard against negative epochs from NaT
        df['time'] = (df['Date'].astype('int64') // 10**9).astype(int)
        neg = int((df['time'] < 0).sum())
        if neg:
            logger.warning(f"/api/data: filtered {neg} rows with negative epoch for {ticker}")
        df = df[df['time'] >= 0]
        chart_data[ticker] = df[['time', 'value']].to_dict(orient='records')

    conn.close()

    return jsonify(chart_data)


@data_bp.route('/api/volume')
def get_volume():
    """Provides raw historical volume data for a list of tickers.
    Query params:
        tickers: comma-separated symbols (required)
    """
    tickers_str = request.args.get('tickers')
    if not tickers_str:
        return jsonify({'error': 'At least one ticker is required'}), 400

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]

    # Use DuckDB if enabled
    if USE_DUCKDB and DUCKDB_AVAILABLE:
        out = get_volume_data(tickers)
        logger.info(f"[DuckDB] /api/volume: returned {len(out)} tickers")
        return jsonify(out)

    # SQLite fallback
    conn = get_db_connection()

    # Determine which requested tickers are present in the stock and futures volume tables
    try:
        stock_cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_volumes_daily)").fetchall()}
    except sqlite3.OperationalError:
        stock_cols = set()
    try:
        fut_cols = {row['name'] for row in conn.execute("PRAGMA table_info(futures_volumes_daily)").fetchall()}
    except sqlite3.OperationalError:
        fut_cols = set()

    selected_stock = [t for t in tickers if t in stock_cols]
    selected_fut = [t for t in tickers if t in fut_cols]

    # Initialize default empty arrays for all requested tickers
    out = {t: [] for t in tickers}

    if selected_stock:
        safe_cols = '", "'.join(selected_stock)
        q = f'SELECT Date, "{safe_cols}" FROM stock_volumes_daily ORDER BY Date ASC'
        df = pd.read_sql_query(q, conn, parse_dates=['Date']).set_index('Date')
        # Convert index to unix seconds
        df['time'] = (df.index.astype('int64') // 10**9).astype(int)
        for t in selected_stock:
            tmp = df[['time', t]].copy()
            tmp.rename(columns={t: 'value'}, inplace=True)
            tmp['value'] = tmp['value'].replace({np.nan: None})
            out[t] = tmp.to_dict(orient='records')

    if selected_fut:
        safe_cols = '", "'.join(selected_fut)
        q = f'SELECT Date, "{safe_cols}" FROM futures_volumes_daily ORDER BY Date ASC'
        df = pd.read_sql_query(q, conn, parse_dates=['Date']).set_index('Date')
        df['time'] = (df.index.astype('int64') // 10**9).astype(int)
        for t in selected_fut:
            tmp = df[['time', t]].copy()
            tmp.rename(columns={t: 'value'}, inplace=True)
            tmp['value'] = tmp['value'].replace({np.nan: None})
            out[t] = tmp.to_dict(orient='records')

    conn.close()
    return jsonify(out)
