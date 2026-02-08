import sqlite3
import time
import json
import os
import sys
import logging
import traceback
import io
from flask import Flask, jsonify, request, Response, redirect, send_from_directory
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for server
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from flask_cors import CORS
from flask_compress import Compress
import pandas as pd
import numpy as np
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import (DB_PATH, get_db_connection, SCHEMA_CACHE_TTL, DEFAULT_PORT,
                      CACHE_CONTROL_MAX_AGE, WORKSPACE_FILENAME,
                      WORKSPACE_TEMP_SUFFIX, HTTP_OK, HTTP_BAD_REQUEST,
                      HTTP_NOT_FOUND, HTTP_INTERNAL_ERROR,
                      resolve_ticker_alias, TICKER_ALIASES)
from constants import USE_DUCKDB

# Shared helpers (schema cache, DuckDB availability, utilities)
from helpers import (
    basedir as _helpers_basedir, get_table_columns, fetch_ticker_data,
    fiscal_to_calendar_quarter, _check_playwright, FRED_INDICATORS,
    DUCKDB_AVAILABLE, USE_DUCKDB as _USE_DUCKDB,
    _schema_cache, _schema_cache_time,
)
# Re-import DuckDB query functions when available (used directly by routes still in app.py)
if USE_DUCKDB and DUCKDB_AVAILABLE:
    from duckdb_queries import (
        get_price_data, get_volume_data,
        get_all_tickers_list, get_available_tickers, get_futures_tickers,
        get_bond_tickers, get_metadata, get_dashboard_prices
    )

# Import backup functionality
import subprocess
from pathlib import Path

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
    response.headers['Cache-Control'] = f'max-age={CACHE_CONTROL_MAX_AGE}, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    # Allow cross-origin requests (e.g., sandbox running on :5500)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

# basedir, schema cache, and other shared state now live in helpers.py
basedir = _helpers_basedir

# --- Start of Diagnostic Logging ---
app.logger.info(f"SCRIPT_DIR: {basedir}")
app.logger.info(f"DB_PATH: {DB_PATH}")
app.logger.info(f"USE_DUCKDB: {USE_DUCKDB}, DUCKDB_AVAILABLE: {DUCKDB_AVAILABLE}")
if not os.path.exists(DB_PATH):
    app.logger.error("FATAL: DATABASE NOT FOUND AT THE CALCULATED PATH!")
else:
    app.logger.info("SUCCESS: Database file was found at the path.")
# --- End of Diagnostic Logging ---

# get_table_columns() now imported from helpers.py

# fetch_ticker_data() now imported from helpers.py
# Diag routes (/, /api/health, /api/diag, /api/diag_reduce, /api/diag_series) moved to diag_routes.py

# Sandbox, workspace, commentary, and ETF routes moved to content_routes.py

# Data routes (tickers, metadata, ticker-aliases, data, volume) moved to data_routes.py



# Fundamentals routes (revenue, overview, earnings, income, balance, cashflow, chart) moved to fundamentals_routes.py

# Short interest routes moved to short_interest_routes.py
# IV routes moved to iv_routes.py


# Dashboard routes (dashboard, export, sparklines, macro-dashboard) moved to dashboard_routes.py

# Chart routes (image, lw, segment) moved to chart_routes.py

# Register chart routes
try:
    from chart_routes import chart_bp
    app.register_blueprint(chart_bp)
    app.logger.info("Chart routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Chart routes not available: {e}")

# Register dashboard routes
try:
    from dashboard_routes import dashboard_bp
    app.register_blueprint(dashboard_bp)
    app.logger.info("Dashboard routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Dashboard routes not available: {e}")

# Register fundamentals routes
try:
    from fundamentals_routes import fundamentals_bp
    app.register_blueprint(fundamentals_bp)
    app.logger.info("Fundamentals routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Fundamentals routes not available: {e}")

# Register data routes
try:
    from data_routes import data_bp
    app.register_blueprint(data_bp)
    app.logger.info("Data routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Data routes not available: {e}")

# Register diag routes
try:
    from diag_routes import diag_bp
    app.register_blueprint(diag_bp)
    app.logger.info("Diag routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Diag routes not available: {e}")

# Register short interest routes
try:
    from short_interest_routes import short_interest_bp
    app.register_blueprint(short_interest_bp)
    app.logger.info("Short interest routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Short interest routes not available: {e}")

# Register IV routes
try:
    from iv_routes import iv_bp
    app.register_blueprint(iv_bp)
    app.logger.info("IV routes registered successfully")
except ImportError as e:
    app.logger.warning(f"IV routes not available: {e}")

# Register content routes
try:
    from content_routes import content_bp
    app.register_blueprint(content_bp)
    app.logger.info("Content routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Content routes not available: {e}")

# Register portfolio routes
try:
    from portfolio_routes import portfolio_bp
    app.register_blueprint(portfolio_bp)
    app.logger.info("Portfolio routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Portfolio routes not available: {e}")

# Register thesis routes
try:
    from thesis_routes import thesis_bp
    app.register_blueprint(thesis_bp)
    app.logger.info("Thesis routes registered successfully")
except ImportError as e:
    app.logger.warning(f"Thesis routes not available: {e}")

if __name__ == '__main__':
    app.run(debug=True, port=DEFAULT_PORT)
