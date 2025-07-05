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
DB_PATH = os.path.join(basedir, '..', 'sp500_data.db')
print(f"Checking for database at: {DB_PATH}", flush=True)
if os.path.exists(DB_PATH):
    print("SUCCESS: Database file found.", flush=True)
else:
    print("ERROR: Database file NOT found at the expected path.", flush=True)

print("--- DIAGNOSTIC SCRIPT END ---", flush=True)
