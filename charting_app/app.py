import sqlite3
import time
import pandas as pd
import os
import sys
from flask import Flask, jsonify, render_template, request, redirect, send_from_directory
from flask_cors import CORS
from flask_compress import Compress
import logging
import numpy as np
import json
from functools import lru_cache

# Configure logging to output to stdout for easier debugging
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
CORS(app)
Compress(app)  # Enable gzip compression for responses

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    # Allow cross-origin requests (e.g., sandbox running on :5500)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

@app.context_processor
def inject_now():
    return {'now': time.time()}

# Get the absolute path of the directory containing this script (charting_app)
basedir = os.path.abspath(os.path.dirname(__file__))
# Construct the absolute path to the database in the parent directory
DB_PATH = os.path.join(basedir, '..', 'sp500_data.db')

# Schema cache for performance
_schema_cache = {}
_schema_cache_time = 0
SCHEMA_CACHE_TTL = 3600  # 1 hour in seconds

# --- Start of Diagnostic Logging ---
app.logger.info(f"SCRIPT_DIR: {basedir}")
app.logger.info(f"DB_PATH: {DB_PATH}")
if not os.path.exists(DB_PATH):
    app.logger.error("FATAL: DATABASE NOT FOUND AT THE CALCULATED PATH!")
else:
    app.logger.info("SUCCESS: Database file was found at the path.")
# --- End of Diagnostic Logging ---

# --- Helper Functions ---
def get_table_columns(table_name, conn=None, force_refresh=False):
    """Get column names for a table with caching."""
    global _schema_cache, _schema_cache_time
    
    # Check if cache needs refresh
    if force_refresh or time.time() - _schema_cache_time > SCHEMA_CACHE_TTL:
        _schema_cache = {}
        _schema_cache_time = time.time()
        app.logger.info(f"Schema cache refreshed")
    
    # Return cached result if available
    if table_name in _schema_cache:
        return _schema_cache[table_name]
    
    # Fetch and cache column names
    close_conn = False
    if conn is None:
        conn = get_db_connection()
        close_conn = True
    
    try:
        cursor = conn.execute(f"PRAGMA table_info({table_name})")
        columns = {row['name'] for row in cursor.fetchall()}
        _schema_cache[table_name] = columns
        app.logger.info(f"Cached schema for table {table_name}: {len(columns)} columns")
        return columns
    except sqlite3.OperationalError:
        _schema_cache[table_name] = set()
        return set()
    finally:
        if close_conn:
            conn.close()

def fetch_ticker_data(table_name, tickers, date_column='Date', value_columns=None, conn=None):
    """Fetch ticker data from any table with consistent interface.
    
    Args:
        table_name: Name of the table to query
        tickers: List of ticker symbols
        date_column: Name of the date column (default: 'Date')
        value_columns: List of columns to fetch (defaults to tickers)
        conn: Database connection (will create if None)
    
    Returns:
        dict: {ticker: DataFrame} mapping
    """
    close_conn = False
    if conn is None:
        conn = get_db_connection()
        close_conn = True
    
    if value_columns is None:
        value_columns = tickers
    
    result = {}
    try:
        # Get available columns
        table_cols = get_table_columns(table_name, conn)
        valid_tickers = [t for t in value_columns if t in table_cols]
        
        if not valid_tickers:
            return result
        
        # Build query
        columns_str = f"{date_column}, " + ", ".join([f'"{t}"' for t in valid_tickers])
        query = f"SELECT {columns_str} FROM {table_name} ORDER BY {date_column}"
        
        # Log slow queries
        start_time = time.time()
        df = pd.read_sql(query, conn, parse_dates=[date_column], index_col=date_column)
        query_time = time.time() - start_time
        
        if query_time > 1.0:  # Log queries taking more than 1 second
            app.logger.warning(f"Slow query ({query_time:.2f}s): {table_name} for {len(valid_tickers)} tickers")
        
        # Split into per-ticker DataFrames
        for ticker in valid_tickers:
            if ticker in df.columns:
                result[ticker] = df[[ticker]].dropna()
    
    except Exception as e:
        app.logger.error(f"Error fetching from {table_name}: {e}")
    finally:
        if close_conn:
            conn.close()
    
    return result

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Redirect root to sandbox UI"""
    return redirect('/sandbox/')

@app.route('/api/health')
def health():
    """Health check endpoint for monitoring."""
    try:
        # Test database connection
        conn = get_db_connection()
        cursor = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
        table_count = cursor.fetchone()[0]
        conn.close()
        
        return jsonify({
            'status': 'healthy',
            'timestamp': time.time(),
            'database': 'connected',
            'table_count': table_count,
            'cache_size': len(_schema_cache),
            'cache_age': time.time() - _schema_cache_time if _schema_cache_time > 0 else None
        }), 200
    except Exception as e:
        app.logger.error(f"Health check failed: {e}")
        return jsonify({
            'status': 'unhealthy',
            'timestamp': time.time(),
            'error': str(e)
        }), 503

# Sandbox static serving
@app.route('/sandbox/')
@app.route('/sandbox/<path:filename>')
def sandbox_static(filename='index.html'):
    sandbox_dir = os.path.abspath(os.path.join(basedir, '..', 'charting_sandbox'))
    return send_from_directory(sandbox_dir, filename)

@app.route('/api/tickers')
def get_tickers():
    """Provides a sorted list of all available tickers from the database."""
    app.logger.info("Request received for /api/tickers")
    try:
        conn = get_db_connection()
        tickers_set = set()

        # Collect columns from stock table
        try:
            cursor = conn.execute("PRAGMA table_info(stock_prices_daily)")
            tickers_set.update(row['name'] for row in cursor.fetchall() if row['name'] != 'Date')
        except sqlite3.OperationalError:
            app.logger.warning("Table 'stock_prices_daily' not found.")

        # Collect columns from futures table
        try:
            cursor = conn.execute("PRAGMA table_info(futures_prices_daily)")
            tickers_set.update(row['name'] for row in cursor.fetchall() if row['name'] != 'Date')
        except sqlite3.OperationalError:
            app.logger.warning("Table 'futures_prices_daily' not found.")

        conn.close()
        tickers = sorted(tickers_set)
        app.logger.info(f"Found {len(tickers)} tickers across stock and futures tables.")
        if not tickers:
            app.logger.warning("WARNING: Ticker list is empty. Check if table 'stock_prices_daily' exists and is populated.")
        return jsonify(sorted(tickers))
    except Exception as e:
        app.logger.error(f"An error occurred in get_tickers: {e}")
        return jsonify([]), 500

@app.route('/api/metadata')
def get_metadata():
    """Return a mapping of ticker -> display name for provided tickers.
    Priority: ticker_metadata.name → stock_metadata.name → ticker itself.
    """
    tickers_str = request.args.get('tickers', '')
    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    # Empty query → empty JSON
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
            app.logger.info(f"/api/metadata: ticker_metadata hits={len(names)}")
        except Exception as e:
            app.logger.warning(f"/api/metadata: ticker_metadata lookup skipped/failed: {e}")

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
                app.logger.info(f"/api/metadata: stock_metadata hits={add}")
            except Exception as e:
                app.logger.warning(f"/api/metadata: stock_metadata lookup failed: {e}")

        conn.close()

        # 3) Final mapping: fallback to ticker itself for any missing
        mapping = {t: names.get(t, t) for t in tickers}
        resolved = sum(1 for t in tickers if mapping[t] != t)
        app.logger.info(f"/api/metadata: requested={len(tickers)} resolved={resolved} missing={len(tickers)-resolved}")
        return jsonify(mapping)
    except Exception as e:
        app.logger.error(f"/api/metadata error: {e}")
        return jsonify({}), 500


@app.route('/api/data')
def get_data():
    """Provides raw historical price data for a list of tickers."""
    tickers_str = request.args.get('tickers')
    if not tickers_str:
        return jsonify({'error': 'At least one ticker is required'}), 400

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]
    
    conn = get_db_connection()

        # --- Determine which tickers belong to which table ---
    stock_cols, futures_cols = set(), set()
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

    # Assign each requested ticker to *exactly one* source table to prevent
    # duplicate column names that break pd.concat (InvalidIndexError).
    # Build chart_data per ticker to avoid column duplication issues entirely
    chart_data = {}
    for ticker in tickers:
        if ticker in stock_cols:
            table = 'stock_prices_daily'
        elif ticker in futures_cols:
            table = 'futures_prices_daily'
        else:
            chart_data[ticker] = []
            continue

        q = f'SELECT Date, "{ticker}" as value FROM {table} WHERE "{ticker}" IS NOT NULL ORDER BY Date ASC'
        df = pd.read_sql_query(q, conn, parse_dates=['Date'])
        if df.empty:
            chart_data[ticker] = []
            continue
        df['time'] = (df['Date'].astype("int64") // 10**9).astype(int)
        chart_data[ticker] = df[['time', 'value']].to_dict(orient='records')

    conn.close()

    return jsonify(chart_data)




@app.route('/api/volume')
def get_volume():
    """Provides raw historical volume data for a list of tickers.
    Query params:
        tickers: comma-separated symbols (required)
    """
    tickers_str = request.args.get('tickers')
    if not tickers_str:
        return jsonify({'error': 'At least one ticker is required'}), 400

    tickers = [t.strip().upper() for t in tickers_str.split(',') if t.strip()]

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
        safe_cols = '\", \"'.join(selected_stock)
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
        safe_cols = '\", \"'.join(selected_fut)
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



# --- Workspace Persistence API ---
@app.route('/api/workspace', methods=['GET', 'POST'])
def workspace():
    """Persist or retrieve the multi-chart workspace layout.
    The workspace is stored as JSON in a file so it survives server restarts
    and is shared across browser origins/ports.
    """
    workspace_path = os.path.join(basedir, 'workspace.json')

    if request.method == 'POST':
        try:
            state = request.get_json(force=True) or []
            # Write atomically by first dumping to a temp file
            tmp_path = workspace_path + '.tmp'
            with open(tmp_path, 'w', encoding='utf-8') as fh:
                json.dump(state, fh)
            os.replace(tmp_path, workspace_path)
            return jsonify({'status': 'saved', 'items': len(state)}), 200
        except Exception as e:
            app.logger.error(f"Failed to save workspace: {e}")
            return jsonify({'error': 'failed to save'}), 500

    # GET
    if os.path.exists(workspace_path):
        try:
            with open(workspace_path, 'r', encoding='utf-8') as fh:
                state = json.load(fh)
        except Exception as e:
            app.logger.error(f"Failed to read workspace file: {e}")
            state = []
    else:
        state = []
    return jsonify(state)


# --- Lightweight commentary endpoint ---
@app.route('/api/commentary')
def commentary():
    """Return rule-based text summary for each requested ticker.
    Query params:
        tickers: comma-separated symbols
        from, to: unix seconds (optional)
    """
    tickers_param = request.args.get('tickers', '')
    if not tickers_param:
        return jsonify({}), 400

    tickers = [t.strip().upper() for t in tickers_param.split(',') if t.strip()]
    try:
        t_from = int(request.args.get('from', 0))
    except ValueError:
        t_from = 0
    try:
        t_to = int(request.args.get('to', 10**12))
    except ValueError:
        t_to = 10**12

    conn = get_db_connection()
    safe_cols = '"' + '", "'.join(tickers) + '"'
    query = f'SELECT Date, {safe_cols} FROM stock_prices_daily ORDER BY Date ASC'
    df = pd.read_sql_query(query, conn, parse_dates=['Date'])
    conn.close()

    # Limit range
    ts = (df['Date'].astype('int64') // 10**9)
    df = df[(ts >= t_from) & (ts <= t_to)].set_index('Date')

    out = {}
    for t in tickers:
        series = df[t].dropna()
        if series.empty:
            out[t] = 'No data for selected period.'
            continue
        start, end = series.iloc[[0, -1]]
        pct = (end / start - 1) * 100
        peak_date = series.idxmax().date()
        trough_date = series.idxmin().date()
        direction = 'rose' if pct > 0 else 'fell'
        out[t] = (f'From {series.index[0].date()} to {series.index[-1].date()}, '
                  f'{t} {direction} {pct:+.1f} %. Peak on {peak_date}, low on {trough_date}.')
    return jsonify(out)


# --- ETF series endpoint (Option A) ---
@app.route('/api/etf/series')
def etf_series():
    """Return derived ETF series like portfolio value and shares outstanding.
    Query params:
        etf: e.g., 'ALLW' (required)
        metrics: comma-separated subset of ['value','shares'] (default 'value,shares')
        from: ISO date YYYY-MM-DD (optional)
        to: ISO date YYYY-MM-DD (optional)
    Response JSON keys present only for requested metrics.
    Each series is a list of {time: <unix_sec>, value: <number>}.
    """
    try:
        etf = (request.args.get('etf', '') or '').strip().upper()
        if not etf:
            return jsonify({'error': 'etf is required'}), 400

        metrics_param = request.args.get('metrics', 'value,shares')
        allowed = {'value', 'shares'}
        metrics = {m.strip().lower() for m in metrics_param.split(',') if m.strip().lower() in allowed}
        if not metrics:
            metrics = {'value'}

        from_str = request.args.get('from')
        to_str = request.args.get('to')

        conn = get_db_connection()

        # Aggregate portfolio value by snapshot_date
        q_hold = (
            "SELECT snapshot_date as Date, SUM(market_value) as total_value "
            "FROM etf_holdings_daily "
            "WHERE etf = ? "
            "GROUP BY snapshot_date "
            "ORDER BY snapshot_date ASC"
        )
        df_hold = pd.read_sql_query(q_hold, conn, params=[etf], parse_dates=['Date'])

        # Filter by date range if provided
        if not df_hold.empty and (from_str or to_str):
            if from_str:
                try:
                    start_ts = pd.to_datetime(from_str)
                    df_hold = df_hold[df_hold['Date'] >= start_ts]
                except Exception:
                    pass
            if to_str:
                try:
                    end_ts = pd.to_datetime(to_str)
                    df_hold = df_hold[df_hold['Date'] <= end_ts]
                except Exception:
                    pass

        result = {}

        # Metric: portfolio value over time
        if 'value' in metrics:
            if df_hold.empty:
                result['value'] = []
            else:
                tmp = df_hold.copy()
                tmp['time'] = (tmp['Date'].astype('int64') // 10**9).astype(int)
                result['value'] = (
                    tmp[['time', 'total_value']]
                    .rename(columns={'total_value': 'value'})
                    .to_dict(orient='records')
                )

        # Metric: shares outstanding = total_value / price
        if 'shares' in metrics:
            shares_series = []
            if not df_hold.empty:
                # Check price column exists for ETF
                try:
                    cols = {row['name'] for row in conn.execute("PRAGMA table_info(stock_prices_daily)").fetchall()}
                except sqlite3.OperationalError:
                    cols = set()
                app.logger.info(f"/api/etf/series shares: df_hold rows={len(df_hold)}; price_col_exists={etf in cols}")
                if etf in cols:
                    q_price = f'SELECT Date, "{etf}" as price FROM stock_prices_daily ORDER BY Date ASC'
                    df_price = pd.read_sql_query(q_price, conn, parse_dates=['Date'])
                    app.logger.info(f"/api/etf/series shares: df_price rows={len(df_price)}")
                    if not df_price.empty:
                        if from_str or to_str:
                            if from_str:
                                try:
                                    start_ts = pd.to_datetime(from_str)
                                    df_price = df_price[df_price['Date'] >= start_ts]
                                except Exception:
                                    pass
                            if to_str:
                                try:
                                    end_ts = pd.to_datetime(to_str)
                                    df_price = df_price[df_price['Date'] <= end_ts]
                                except Exception:
                                    pass
                        # Use asof merge to tolerate non-trading-day snapshots; align to previous available price (up to 5 days back)
                        df_hold_sorted = df_hold[['Date', 'total_value']].sort_values('Date')
                        df_price_sorted = df_price[['Date', 'price']].sort_values('Date')
                        try:
                            df_m = pd.merge_asof(
                                df_hold_sorted,
                                df_price_sorted,
                                on='Date',
                                direction='backward',
                                tolerance=pd.Timedelta('5D')
                            )
                        except Exception as me:
                            app.logger.warning(f"/api/etf/series shares: merge_asof failed ({me}); falling back to inner merge")
                            df_m = pd.merge(df_hold_sorted, df_price_sorted, on='Date', how='inner')
                        df_m = df_m[df_m['price'].notna()]
                        app.logger.info(f"/api/etf/series shares: merged rows={len(df_m)}")
                        if not df_m.empty:
                            df_m['shares'] = df_m['total_value'] / df_m['price']
                            df_m['time'] = (df_m['Date'].astype('int64') // 10**9).astype(int)
                            shares_series = (
                                df_m[['time', 'shares']]
                                .rename(columns={'shares': 'value'})
                                .to_dict(orient='records')
                            )
                            app.logger.info(f"/api/etf/series shares: output points={len(shares_series)}")
            result['shares'] = shares_series

        conn.close()
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"/api/etf/series error: {e}")
        return jsonify({'error': 'failed to compute series'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
