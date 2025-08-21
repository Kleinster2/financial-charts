import sys
import os

print("--- DIAGNOSTIC SCRIPT START ---", flush=True)
print(f"Python Executable: {sys.executable}", flush=True)
print(f"Python Version: {sys.version}", flush=True)

try:
    import flask
    print(f"SUCCESS: Flask is installed (version {flask.__version__})", flush=True)
except ImportError:
    print("ERROR: Flask is NOT installed for this Python interpreter.", flush=True)

try:
    import pandas
    print(f"SUCCESS: Pandas is installed (version {pandas.__version__})", flush=True)
except ImportError:
    print("ERROR: Pandas is NOT installed for this Python interpreter.", flush=True)

# Database path check
basedir = os.path.abspath(os.path.dirname(__file__))
# Import DB helpers from project root
sys.path.append(os.path.join(basedir, '..'))
try:
    from constants import DB_PATH, get_db_connection
    print(f"Resolved DB_PATH from constants: {DB_PATH}", flush=True)
except Exception as e:
    print(f"ERROR: Could not import DB helpers from constants: {e}", flush=True)
    DB_PATH = os.path.join(basedir, '..', 'market_data.db')

print(f"Checking for database at: {DB_PATH}", flush=True)
if os.path.exists(DB_PATH):
    print("SUCCESS: Database file found.", flush=True)
else:
    print("ERROR: Database file NOT found at the expected path.", flush=True)

# Try a simple connection test
try:
    from constants import get_db_connection as _get_db
    conn = _get_db()
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"SUCCESS: Connected to DB. Tables found: {len(tables)}", flush=True)
    conn.close()
except Exception as e:
    print(f"ERROR: Unable to connect to DB via get_db_connection: {e}", flush=True)

print("--- DIAGNOSTIC SCRIPT END ---", flush=True)
