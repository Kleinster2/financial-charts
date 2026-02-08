import os
import sys
import logging

from flask import Flask
from flask_cors import CORS
from flask_compress import Compress

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DB_PATH, DEFAULT_PORT, CACHE_CONTROL_MAX_AGE, USE_DUCKDB
from helpers import basedir, DUCKDB_AVAILABLE

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


# --- Diagnostic Logging ---
app.logger.info(f"SCRIPT_DIR: {basedir}")
app.logger.info(f"DB_PATH: {DB_PATH}")
app.logger.info(f"USE_DUCKDB: {USE_DUCKDB}, DUCKDB_AVAILABLE: {DUCKDB_AVAILABLE}")
if not os.path.exists(DB_PATH):
    app.logger.error("FATAL: DATABASE NOT FOUND AT THE CALCULATED PATH!")
else:
    app.logger.info("SUCCESS: Database file was found at the path.")

# --- Blueprint Registration ---
_blueprints = [
    ('chart_routes', 'chart_bp', 'Chart'),
    ('dashboard_routes', 'dashboard_bp', 'Dashboard'),
    ('fundamentals_routes', 'fundamentals_bp', 'Fundamentals'),
    ('data_routes', 'data_bp', 'Data'),
    ('diag_routes', 'diag_bp', 'Diag'),
    ('short_interest_routes', 'short_interest_bp', 'Short interest'),
    ('iv_routes', 'iv_bp', 'IV'),
    ('content_routes', 'content_bp', 'Content'),
    ('portfolio_routes', 'portfolio_bp', 'Portfolio'),
    ('thesis_routes', 'thesis_bp', 'Thesis'),
]

for module_name, bp_name, label in _blueprints:
    try:
        mod = __import__(module_name)
        bp = getattr(mod, bp_name)
        app.register_blueprint(bp)
        app.logger.info(f"{label} routes registered successfully")
    except ImportError as e:
        app.logger.warning(f"{label} routes not available: {e}")

if __name__ == '__main__':
    app.run(debug=True, port=DEFAULT_PORT)
