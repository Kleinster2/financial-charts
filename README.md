# Market Data Workbench

This project collects and serves multi-asset daily market data (stocks, ETFs, futures, FX, crypto) into a SQLite database, exposes a Flask API, and includes a charting sandbox UI.

## Steps

1.  **Builds instrument universes**: Curates lists across indices, ETFs, futures, FX, and crypto.
2.  **Downloads Price Data**: Pulls daily historical prices/volumes from Yahoo Finance.
3.  **Data Cleaning**: Processes the data, handles missing values, and filters out tickers with insufficient data.
4.  **Stores Data**: Saves the cleaned data and metadata into a SQLite database file (`market_data.db`).

## Project Overview

This repo includes three components:

-  __Data Collection__ (`update_market_data.py`, `download_all_assets.py`): Builds/updates the SQLite DB `market_data.db` with daily prices and volumes for stocks, ETFs, futures, FX, and more.
-  __Web API__ (`charting_app/app.py`): Flask server exposing REST endpoints to read data from the DB and serve the sandbox UI.
-  __Frontend Sandbox__ (`charting_sandbox/`): Lightweight Charts-based UI for multi-ticker charting, averages, and workspace persistence.

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
