# S&P 500 Data Downloader

This script downloads historical stock price data for all S&P 500 companies and stores it in a SQLite database.

## Steps

1.  **Fetches S&P 500 Companies**: Retrieves the list of S&P 500 companies from Wikipedia.
2.  **Downloads Price Data**: Downloads daily historical stock prices for each company from Yahoo Finance.
3.  **Data Cleaning**: Processes the data, handles missing values, and filters out tickers with insufficient data.
4.  **Stores Data**: Saves the cleaned price data and company metadata into an SQLite database file (`sp500_data.db`).

## Project Overview

This repo includes three components:

-  __Data Collection__ (`download_sp500.py`): Builds/updates the SQLite DB `sp500_data.db` with daily prices and volumes for stocks, ETFs, futures, FX, and more.
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
    python download_sp500.py
    ```
2.  __Start the API server__
    ```powershell
    python charting_app\app.py
    ```
3.  __Open the sandbox UI__
    - Visit: http://localhost:5000/sandbox/

Default paths and ports:
-  Database: `sp500_data.db` at repo root (server resolves `../sp500_data.db` from `charting_app/`)
-  Port: `5000` (see `charting_app/app.py`)

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

-  __Daily timeframe__ always (no auto-switch to weekly/monthly).
-  __Last-price dotted lines hidden__ on all series.
-  __Dynamic rebase on visible range change__ with debounce (`500ms`).
-  __Workspace persistence__ via backend-first restore at `/api/workspace` (cross-browser persistence).

## Usage

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the script:**
    ```bash
    python download_sp500.py
    ```

This will create the `sp500_data.db` file in the same directory.
