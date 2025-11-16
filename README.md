# Market Data Workbench

This project collects and serves multi-asset daily market data (stocks, ETFs, futures, FX, crypto) into a SQLite database, exposes a Flask API, and includes a charting sandbox UI.

## Steps

1.  **Builds instrument universes**: Curates lists across indices, ETFs, futures, FX, and crypto.
2.  **Downloads Price Data**: Pulls daily historical prices/volumes from Yahoo Finance.
3.  **Data Cleaning**: Processes the data, handles missing values, and filters out tickers with insufficient data.
4.  **Stores Data**: Saves the cleaned data and metadata into a SQLite database file (`market_data.db`).

## Project Overview

This repo includes three components:

-  __Data Collection__: Builds/updates the SQLite DB `market_data.db` with daily prices and volumes for stocks, ETFs, futures, FX, and more.
   - `download_single_ticker.py TICKER` - Add individual tickers (~5 sec each)
   - `update_market_data.py` - Daily updates (~3 min)
   - `download_all_assets.py` - Full rebuild (~3 min)
   - See **[WORKFLOW_CHECKLIST.md](WORKFLOW_CHECKLIST.md)** for detailed usage guide
-  __Web API__ (`charting_app/app.py`): Flask server exposing REST endpoints to read data from the DB and serve the sandbox UI.
-  __Frontend Sandbox__ (`charting_sandbox/`): Lightweight Charts-based UI for multi-ticker charting, averages, and workspace persistence.

## Documentation

For detailed information on specific topics, refer to these documentation files:

-  **[DATA_SOURCES.md](DATA_SOURCES.md)** - Critical distinction between database (local cache) vs yfinance API (source of truth). Always check yfinance first for data availability.
-  **[WORKFLOW_CHECKLIST.md](WORKFLOW_CHECKLIST.md)** - Quick reference guide for common data availability checks and workflow patterns.
-  **[charting_sandbox/REFACTORING_STATUS.md](charting_sandbox/REFACTORING_STATUS.md)** - Code refactoring history and architecture evolution.
-  **[charting_sandbox/COMPLETION_GUIDE.md](charting_sandbox/COMPLETION_GUIDE.md)** - Step-by-step implementation guides for card.js refactoring.

## Project Structure

```
financial-charts/
├── market_data.db              # SQLite database (generated)
├── constants.py                # Shared configuration constants
├── metadata_utils.py           # Automatic metadata management
├── update_market_data.py       # Main orchestrator script
├── download_all_assets.py      # Data download logic (stocks, ETFs, etc.)
├── download_futures.py         # Futures data download
├── backup_workspace.py         # Automatic workspace backup utility
│
├── charting_app/               # Backend Flask API
│   ├── app.py                  # Main Flask server (port 5000)
│   ├── workspace.json          # Persistent chart configurations
│   └── requirements.txt        # Backend dependencies
│
└── charting_sandbox/           # Frontend UI
    ├── index.html              # Main HTML entry point
    ├── config.js               # Frontend configuration
    ├── card.js                 # Core chart card logic
    ├── chart-*.js              # Chart component modules
    ├── data-fetcher.js         # API communication
    ├── state-manager.js        # State management
    └── pages.js                # Multi-page navigation
```

## Architecture & Data Flow

```
┌─────────────────┐
│  Yahoo Finance  │
└────────┬────────┘
         │ yfinance library
         v
┌─────────────────────────┐
│ download_all_assets.py  │ ← Define ticker lists (EV_STOCKS, etc.)
│ metadata_utils.py       │ ← Auto-fetch & clean company names
└─────────┬───────────────┘
          │ writes
          v
┌─────────────────────┐
│  market_data.db     │ ← SQLite database
│  - stock_prices     │   - Daily OHLCV data (wide format)
│  - ticker_metadata  │   - Company names, date ranges
└─────────┬───────────┘
          │ reads
          v
┌─────────────────────┐
│  Flask API (5000)   │ ← charting_app/app.py
│  - /api/data        │   - Serves price data
│  - /api/metadata    │   - Company name lookups
│  - /api/workspace   │   - Save/restore chart configs
└─────────┬───────────┘
          │ HTTP/JSON
          v
┌─────────────────────────┐
│  Frontend Sandbox       │ ← charting_sandbox/
│  - Lightweight Charts   │   - Interactive charting
│  - 28 themed pages      │   - Multi-page organization
│  - workspace.json sync  │   - Config persistence
└─────────────────────────┘
```

## Key Files & Their Roles

### Backend Core
- **`constants.py`** - Shared config: DB_PATH, PORT, asset categories
- **`download_single_ticker.py`** - Fast individual ticker downloads (~5 sec each)
- **`update_market_data.py`** - Daily price updates for all tickers
- **`download_all_assets.py`** - Full rebuild with ticker lists (EV_STOCKS, CRYPTO_STOCKS, etc.)
- **`metadata_utils.py`** - Auto metadata fetching/cleaning (NEW Nov 2025)

### Frontend Core
- **`charting_sandbox/card.js`** - Main chart card logic (~2000 lines)
  - Chart initialization, event handlers, plotting logic
  - Slider controls, persistence, rebase calculations
- **`charting_sandbox/chart-dom-builder.js`** - UI construction
- **`charting_sandbox/data-fetcher.js`** - API communication layer
- **`charting_sandbox/pages.js`** - Multi-page navigation system

### Configuration & State
- **`charting_app/workspace.json`** - Persistent chart configurations
  - All 28 pages with chart definitions
  - User customizations (height, font, tickers, etc.)
  - Auto-backed up on each save

## Setup

Windows PowerShell (recommended):

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r charting_app\requirements.txt
```

## Quickstart

1.  __Download data (creates DB file)__
    ```powershell
    python update_market_data.py
    ```
2.  __Start the API server__
    ```powershell
    python charting_app\app.py
    ```
3.  __Open the sandbox UI__
    - Visit: http://localhost:5000/sandbox/

Default paths and ports:
-  Database: resolved via `constants.DB_PATH` in the repo root. If `market_data.db` is missing but a legacy `sp500_data.db` exists, the resolver will use it and log a deprecation warning.
-  Port: `5000` (see `charting_app/app.py`)

## Orchestrator CLI: asset selection and verbosity

The orchestrator `update_market_data.py` supports selecting asset groups and controlling log verbosity.

- __Assets__: `--assets` chooses which groups to update. Options include: `stocks`, `etfs`, `adrs`, `fx`, `crypto`, `futures`.
- __Verbosity__: `--verbose` for detailed logs, `--quiet` to reduce output.

Examples (Windows PowerShell):

```powershell
# Full update (all assets)
python update_market_data.py --verbose

# Only futures
python update_market_data.py --assets futures

# Stocks + ETFs only (skip futures)
python update_market_data.py --assets stocks etfs --verbose

# Quiet mode
python update_market_data.py --quiet
```

Notes:
- Futures are handled via a dedicated module (`download_futures.py`), invoked by the orchestrator when `--assets futures` is selected.
- For non-futures groups, the orchestrator routes to `download_all_assets.update_sp500_data(assets=...)` and preserves existing DB columns on partial updates.

## Metadata Management

### Automatic Metadata Updates (New!)

As of November 2025, metadata is **automatically updated** when running `update_market_data.py` or `download_all_assets.py`. The system:

1. Detects any new tickers in the database without metadata
2. Fetches company names from yfinance
3. Automatically cleans names by removing corporate suffixes (Inc., Corp., Ltd., etc.)
4. Updates the `ticker_metadata` table

No manual intervention needed! Just run the normal data update and metadata will be handled automatically.

### Manual Metadata Population (Legacy)

For manual control or ETF-specific updates, use the legacy scripts:

```powershell
# Populate names for known ETFs from the built-in map
python populate_etf_metadata.py

# Auto-fill missing names using yfinance (limit requests to avoid rate limits)
python populate_etf_metadata.py --auto --limit 200

# Restrict to specific tickers (space or comma separated)
python populate_etf_metadata.py --auto --tickers "EWZ EWW DTCR"
```

### Metadata Cleaning

The `metadata_utils.py` module automatically cleans company names by removing:
- Corporate suffixes: Inc., Corp., Corporation, Ltd., Limited, PLC, N.V., SE, AG
- Business structure terms: Co., Company, Holdings, Group
- Trailing punctuation and commas

Example: "Apple Inc." → "Apple", "Honda Motor Co., Ltd." → "Honda Motor"

### API Verification

Check metadata via API:

```text
/api/metadata?tickers=EWZ,EWW,AAPL
```

The API prioritizes `ticker_metadata.name`, then falls back to `stock_metadata.name`, then the ticker itself.

## API Endpoints (selected)

-  __GET__ `/api/health` → basic server/DB health
-  __GET__ `/api/tickers` → array of available tickers
-  __GET__ `/api/data?tickers=SPY,QQQ` → per-ticker price series: `{ "SPY": [{time,value}, ...], ... }`
-  __GET__ `/api/volume?tickers=SPY,QQQ` → per-ticker volume series
-  __GET__ `/api/metadata?tickers=AAPL,MSFT` → `{ "AAPL": "Apple Inc.", ... }`
-  __GET__ `/api/commentary?tickers=SPY&from=1700000000&to=1800000000` → simple rule-based summaries
-  __GET/POST__ `/api/workspace` → persist/restore sandbox layout (accepts object schema or legacy array)
-  __GET__ `/api/etf/series?etf=ALLW&metrics=value,shares&from=YYYY-MM-DD&to=YYYY-MM-DD` → derived series

Notes:
-  Current server endpoints operate on __daily__ data.
-  CORS is enabled; responses are gzip-compressed.

## Frontend Sandbox

Open at `http://localhost:5000/sandbox/` once the server is running.

### Features

-  __Flexible timeframe selection__: Choose between Daily, Weekly, or Monthly intervals, or use Auto mode which selects based on date range (<5yr = daily, 5-10yr = weekly, >10yr = monthly).
-  __Interactive sliders__ for real-time chart customization:
   - **Font size**: 8-24pt with live preview
   - **Chart height**: 400-800px
   - **Volume pane height**: 0.5x-3.0x stretch factor
-  __Dynamic rebase on visible range change__ with debounce (`500ms`).
-  __Workspace persistence__ via backend-first restore at `/api/workspace` (cross-browser persistence).
-  __Resizable and draggable fixed legend__ with size/position persistence.
-  __Percentage-based Y-axis formatting__ showing change from base 100 (e.g., +50%, -25%).
-  __Multi-page organization__ with 28 themed pages including sectors, countries, asset classes, and specialized topics.

### Recent Improvements (Nov 2025)

#### UI Enhancements
- Replaced +/- buttons with sliders for Font, Height, and Volume pane controls
- Added real-time value display next to each slider
- Consistent slider UI design across all controls

#### Bug Fixes
- **Fixed interval persistence**: Daily/Weekly/Monthly selection now persists across page refreshes
- **Fixed legend resize persistence**: Custom legend sizes now save correctly (no more 0x0 resets)
- **Fixed Y-axis format bug**: Charts now consistently display percentage format instead of base 100 values
- Price scale format updates correctly when toggling between raw prices and percentage mode

#### Data Expansion
- **Electric Vehicles**: Added 10 new EV stocks including Chinese leaders (BYD, Li Auto, XPeng, Polestar) and traditional automakers (Honda, Stellantis, Porsche)
- **Comprehensive EV coverage**: Database now includes pure-play EVs, Chinese manufacturers, and legacy automakers with EV initiatives

## Usage

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the script:**
    ```bash
    python update_market_data.py
    ```

This will create the `market_data.db` file in the same directory.

## Common Tasks

### Adding New Tickers

1. **Add ticker to appropriate list** in `download_all_assets.py`:
   ```python
   # Example: Adding to EV_STOCKS list
   EV_STOCKS = [
       "BYDDY", "LI", "XPEV", "PSNY",  # Existing
       "NEWTICKER",  # Add here
   ]
   ```

2. **Download data**:
   ```powershell
   python update_market_data.py --assets stocks
   ```

3. **Metadata is automatic** - Company names are fetched and cleaned automatically!

### Adding Tickers to a Chart

1. **Edit `charting_app/workspace.json`**:
   ```python
   import json

   with open('charting_app/workspace.json', 'r') as f:
       workspace = json.load(f)

   # Find chart by page and title
   for chart in workspace['cards']:
       if chart.get('page') == '28' and 'Electric' in chart.get('title', ''):
           chart['tickers'].append('NEWTICKER')
           chart['multipliers']['NEWTICKER'] = 1

   with open('charting_app/workspace.json', 'w') as f:
       json.dump(workspace, f, indent=2)
   ```

2. **Refresh browser** - Changes appear immediately

### Creating a New Page

Pages are defined in `charting_app/workspace.json`:

```json
{
  "pages": {
    "1": "Tech",
    "2": "Finance",
    "29": "My New Page"  // Add new page
  },
  "cards": [
    {
      "page": "29",
      "tickers": ["AAPL", "MSFT"],
      "title": "My First Chart",
      "height": 500,
      // ... other default properties
    }
  ]
}
```

### Modifying UI Controls

**Backend (API endpoints)** - `charting_app/app.py`
**Frontend (UI logic)** - `charting_sandbox/card.js`

Example: Adding a new slider
1. Add HTML in `chart-dom-builder.js`
2. Add element reference in `getCardElements()`
3. Add event handlers in `card.js`
4. Save value to `card._propertyName`
5. Add to workspace save/load logic

### Database Queries

```python
import sqlite3
from constants import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Get all tickers
cursor.execute("PRAGMA table_info(stock_prices_daily);")
tickers = [row[1] for row in cursor.fetchall() if row[1] != 'Date']

# Get price data for a ticker
cursor.execute("SELECT Date, AAPL FROM stock_prices_daily WHERE AAPL IS NOT NULL")
data = cursor.fetchall()

# Get metadata
cursor.execute("SELECT ticker, name FROM ticker_metadata WHERE ticker = 'AAPL'")
metadata = cursor.fetchone()

conn.close()
```

## Troubleshooting

### Charts Not Loading
- **Check Flask server is running** on port 5000
- **Check browser console** for API errors
- **Verify database exists**: `ls market_data.db`
- **Check API health**: Visit `http://localhost:5000/api/health`

### Metadata Not Showing
- **Run metadata update**: `python -c "from metadata_utils import auto_update_new_tickers; auto_update_new_tickers()"`
- **Check ticker_metadata table**: `sqlite3 market_data.db "SELECT * FROM ticker_metadata LIMIT 5"`

### Workspace Changes Not Persisting
- **Check workspace.json permissions** - Should be writable
- **Check Flask logs** - Shows save success/failure
- **Automatic backup**: Check `workspace_backups/` folder

### Price Data Missing
- **Ticker might be delisted** - Check Yahoo Finance manually
- **Re-download**: `python update_market_data.py --assets stocks --verbose`
- **Check column exists**: `sqlite3 market_data.db "PRAGMA table_info(stock_prices_daily)" | grep TICKER`

### Hard Refresh Browser
If frontend changes don't appear:
- **Windows**: `Ctrl + Shift + R` or `Ctrl + F5`
- **Mac**: `Cmd + Shift + R`
- Clears JavaScript cache and reloads all files

## Development Notes

### Database Schema
- **Wide format**: Each ticker is a column, dates are rows
- **Efficient for time-series queries** across multiple tickers
- **stock_prices_daily**: Close prices (adjusted)
- **stock_volumes_daily**: Trading volumes
- **ticker_metadata**: Company names, data ranges

### Frontend State Management
- **Card-level state**: Each chart card maintains its own state (`card._property`)
- **Workspace sync**: State saved to workspace.json on changes
- **Auto-save**: Triggered by user interactions (slider release, ticker add/remove)
- **Backend-first restore**: Loads from server on page load

### Code Organization
- **Modular JS files**: Each chart feature in separate file (legend, export, volume, etc.)
- **Event-driven**: User actions trigger state updates → re-render → save
- **Defensive coding**: Extensive null checks, try-catch blocks for robustness
