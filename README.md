# Market Data Workbench

[![Playwright Smoke](https://github.com/Kleinster2/financial-charts/actions/workflows/playwright-smoke.yml/badge.svg)](https://github.com/Kleinster2/financial-charts/actions/workflows/playwright-smoke.yml)

Interactive financial charting application for visualizing stock prices, fundamentals, and technical indicators across 1,300+ time series.

## Quick Stats

- **1,310+ time series** (stocks, ETFs, futures, FX, crypto, FRED indicators)
- **86 years of data** (1939-2025)
- **53 themed pages** (sectors, countries, macro analysis)
- **~3 minute daily update**

## Technology Stack

- **Frontend**: Vanilla JavaScript with [LightweightCharts](https://tradingview.github.io/lightweight-charts/) v5.0.9
- **Backend**: Flask (Python)
- **Database**: SQLite with wide-column schema (~311 MB), optional DuckDB backend
- **Data Sources**: yfinance, FRED, Alpha Vantage (fundamentals)

## Data Notes

- **FX prices** use the 4pm EST close (NY market close) for alignment with US equity prices
- **Stock prices** are adjusted for splits and dividends (yfinance `auto_adjust=True`)
- **FRED indicators** update with varying lags (employment: monthly, GDP: quarterly)

## Critical Data Warning

Some data in `market_data.db` is **irreplaceable** and cannot be re-downloaded:

| Data | Description |
|------|-------------|
| **B3 DI Yield Curve** | 5,445 days of manually cleaned Brazilian interest rates (2003-present) |
| **Bond prices** | Corporate bond prices (no bulk API) |
| **Portfolio data** | User-created portfolios and transactions |

**See [DATABASE_GUIDE.md](DATABASE_GUIDE.md) for full documentation on data classification and backup procedures.**

Before running updates, use incremental mode to protect historical data:
```bash
python update_market_data.py  # Select option 1: Incremental (10 days)
```

## Project Structure

```
financial-charts/
├── market_data.db              # SQLite database (generated)
├── constants.py                # Shared configuration constants
├── metadata_utils.py           # Automatic metadata management
├── update_market_data.py       # Main data update script (unified)
├── download_all_assets.py      # Ticker lists and download logic
├── download_single_ticker.py   # Single ticker updates
│
├── scripts/                    # Auxiliary scripts (see scripts/README.md)
│   ├── one_off/                # Migrations, backfills, one-time setup
│   └── diagnostics/            # Audits, health checks
│
├── charting_app/               # Backend Flask API
│   ├── app.py                  # Main Flask server (port 5000)
│   ├── workspace.json          # Persistent chart configurations
│   └── requirements.txt        # Backend dependencies
│
├── charting_sandbox/           # Frontend UI
│   ├── index.html              # Main HTML entry point
│   ├── config.js               # Frontend configuration
│   ├── card.js                 # Chart card orchestrator (~660 lines)
│   ├── chart-card-context.js   # Card state + ctx.runtime (~450 lines)
│   ├── chart-card-plot.js      # Plot logic (~860 lines)
│   ├── chart-card-toggles.js   # Toggle handlers (~380 lines)
│   ├── chart-card-range.js     # Fit/range/interval handlers
│   ├── chart-card-meta.js      # Star/tags/notes UI
│   ├── chart-card-tickers.js   # Ticker chips + axis/context menu
│   ├── chart-card-registry.js  # Card type registry + restoreCard
│   ├── sandbox-init.js         # index.html bootstrap (workspace restore)
│   ├── chart-*.js              # Other chart component modules
│   ├── data-fetcher.js         # API communication
│   ├── state-manager.js        # State management
│   └── pages.js                # Multi-page navigation
│
├── tests/                      # Automated tests
│   ├── unit/                   # Node unit tests (74 tests)
│   │   ├── chart-card-context.test.js
│   │   ├── chart-card-registry.test.js
│   │   ├── chart-dashboard.test.js
│   │   ├── chart-macro-dashboard.test.js
│   │   ├── chart-utils.test.js
│   │   └── dashboard-base.test.js
│   └── playwright/             # Playwright smoke tests (6 tests)
│       ├── card-smoke.spec.js  # Card + dashboard tests
│       ├── helpers/            # Test utilities
│       └── stubs/              # LightweightCharts stub
│
└── .github/workflows/          # CI/CD
    └── playwright-smoke.yml    # Smoke test workflow
```

## Architecture & Data Flow

```
┌─────────────────┐     ┌─────────────────┐
│  Yahoo Finance  │     │      FRED       │
└────────┬────────┘     └────────┬────────┘
         │ yfinance              │ fredapi
         v                       v
┌─────────────────────────────────────────┐
│  update_market_data.py                  │
│  (unified: stocks, futures, FRED, etc.) │
└─────────────────┬───────────────────────┘
                  │ writes
                  v
┌─────────────────────────────────────────┐
│  market_data.db (SQLite)                │
│  - stock_prices_daily (wide format)     │
│  - stock_volumes_daily                  │
│  - ticker_metadata                      │
│  - company_overview, earnings, etc.     │
└─────────────────┬───────────────────────┘
                  │ reads
                  v
┌─────────────────────────────────────────┐
│  Flask API (localhost:5000)             │
│  - /api/data, /api/volume               │
│  - /api/metadata, /api/fundamentals     │
│  - /api/workspace                       │
└─────────────────┬───────────────────────┘
                  │ HTTP/JSON
                  v
┌─────────────────────────────────────────┐
│  Frontend Sandbox                       │
│  - Lightweight Charts rendering         │
│  - 53 themed pages                      │
│  - Workspace persistence                │
└─────────────────────────────────────────┘
```

## Setup

```powershell
# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Core install (daily updates + charting app)
pip install -r requirements.txt
pip install -r charting_app\requirements.txt

# Optional: dendrograms, DuckDB, JGB APIs
pip install -r requirements-optional.txt
```

**Dependency breakdown:**
- `requirements.txt` - Daily data updates (yfinance, pandas, python-dotenv, pytz)
- `charting_app/requirements.txt` - Flask API server
- `requirements-optional.txt` - Analysis tools (scipy, matplotlib, duckdb, fredapi)

## Quickstart

### Update Data (Unified Command)

```powershell
# Interactive mode (menu-driven)
python update_market_data.py

# Daily update: all assets, last 10 days (~5 min)
python update_market_data.py --assets all --lookback 10

# Check data freshness
python update_market_data.py --status

# Specific asset types only
python update_market_data.py --assets futures fredindices --lookback 10
python update_market_data.py --assets fundamentals
```

### Launch Application

```powershell
# Start the API server
python charting_app\app.py

# Open browser to http://localhost:5000/sandbox/
```

## Key Features

### Dynamic Interval Selection
Charts automatically adjust data granularity based on visible date range:
- **< 5 years**: Daily prices
- **5-10 years**: Weekly prices (Friday close)
- **> 10 years**: Monthly prices (month-end close)

Manual override available via dropdown (Auto/Daily/Weekly/Monthly).

### Multiple Visualization Modes
- **Percentage basis**: Rebase all series to 100% at first visible date
- **Raw prices**: Display absolute price values
- **Diff pane**: Show delta from first visible point
- **Volume pane**: Trading volume with SMA overlay
- **Revenue pane**: Fundamental revenue data overlay

### Fundamentals Integration
- Revenue, Net Income, EPS, Free Cash Flow
- Quarterly and annual data from Alpha Vantage
- Overlay on price charts or separate pane

### Multi-page Workspace
- 53 themed pages (Tech, Finance, Brazil, Crypto, Macro, etc.)
- Persistent workspace via backend API
- Resizable/draggable legend with position persistence

### Data Dashboard
- Spreadsheet view of all 1,300+ tickers with prices, changes, and metadata
- **Sortable columns**: Click headers to sort by ticker, price, day/week/month/year change
- **Filter**: Type to filter by ticker, name, or page name
- **Column visibility**: Show/hide columns via dropdown
- **Reset Layout**: One click to restore default sort, filter, and column settings
- **Export CSV**: Download filtered/sorted data with visible columns
- **State persistence**: Dashboard layout (sort, filter, columns) persists across sessions

## Database Schema

### Price and Volume Data (Wide-Column Format)

```sql
-- One column per ticker for efficient multi-ticker queries
CREATE TABLE stock_prices_daily (
    Date TEXT PRIMARY KEY,
    AAPL REAL,
    MSFT REAL,
    SPY REAL,
    ... (1,300+ columns)
);

CREATE TABLE stock_volumes_daily (
    Date TEXT PRIMARY KEY,
    AAPL REAL,
    MSFT REAL,
    ...
);
```

### Fundamental Data (Normalized Format)

```sql
CREATE TABLE company_overview (
    ticker TEXT PRIMARY KEY,
    name TEXT,
    sector TEXT,
    industry TEXT,
    ...
);

CREATE TABLE earnings_quarterly (
    ticker TEXT,
    fiscal_date_ending TEXT,
    reported_eps REAL,
    estimated_eps REAL,
    surprise REAL,
    PRIMARY KEY (ticker, fiscal_date_ending)
);
```

### Other Tables
- `ticker_metadata` - Ticker symbols and company names
- `etf_holdings_daily` - ETF composition tracking
- `futures_prices_daily` / `futures_volumes_daily` - Futures data
- `cboe_indices` - Volatility indices (VIX, VXN, etc.)

## DuckDB Backend (Optional)

An optional DuckDB backend provides faster queries using a normalized long-format schema.

**This is opt-in.** SQLite is always used by default. DuckDB is only enabled when:
1. Environment variable `USE_DUCKDB=1` is set
2. The `market_data.duckdb` file exists (created via migration)

### Why DuckDB?

| Aspect | SQLite (Wide) | DuckDB (Long) |
|--------|---------------|---------------|
| **Adding tickers** | `ALTER TABLE ADD COLUMN` | Just `INSERT` |
| **Query style** | Row-oriented (OLTP) | Columnar (OLAP) |
| **Aggregations** | Slower on wide tables | Optimized |
| **Compression** | Sparse columns waste space | Compact long format |

**When to use DuckDB:**
- Adding many new tickers frequently
- Running analytical queries (correlations, aggregations across tickers)
- If SQLite queries become slow as data grows

**When SQLite is fine:**
- Current scale (~1300 tickers, 311 MB) performs well
- Simple date-range queries on known tickers
- No need for complex analytics

### Schema Comparison

| Aspect | SQLite (Primary) | DuckDB (Optional) |
|--------|------------------|-------------------|
| **Format** | Wide (1 column per ticker) | Long (Date, Ticker, Value) |
| **Schema** | `stock_prices_daily.AAPL` | `prices WHERE Ticker='AAPL'` |
| **File** | `market_data.db` (~311 MB) | `market_data.duckdb` |
| **Queries** | Simple column select | PIVOT for wide format |

### DuckDB Tables

```sql
-- Long format with composite primary keys
prices:         (Date DATE, Ticker VARCHAR, Close DOUBLE, PRIMARY KEY (Date, Ticker))
volumes:        (Date DATE, Ticker VARCHAR, Volume DOUBLE, PRIMARY KEY (Date, Ticker))
futures_prices: (Date DATE, Ticker VARCHAR, Close DOUBLE, PRIMARY KEY (Date, Ticker))
futures_volumes:(Date DATE, Ticker VARCHAR, Volume DOUBLE, PRIMARY KEY (Date, Ticker))

-- Indexes for fast lookups
idx_prices_ticker, idx_prices_date, idx_volumes_ticker, idx_volumes_date
```

### Setup

```powershell
# 1. Install DuckDB
pip install duckdb

# 2. Initial migration from SQLite (one-time, ~30 seconds)
python scripts/one_off/migrate_to_duckdb.py

# 3. Enable DuckDB for the app
$env:USE_DUCKDB = "1"
python charting_app\app.py

# Or in one line (PowerShell)
$env:USE_DUCKDB="1"; python charting_app\app.py

# Unix/bash
USE_DUCKDB=1 python charting_app/app.py
```

### Dual-Write Mode

When `USE_DUCKDB=1`, data updates write to both databases:

```
update_market_data.py
    ├── SQLite (primary) - wide format
    └── DuckDB (shadow)  - long format via duckdb_writer.py
```

### Files

| File | Purpose |
|------|---------|
| `scripts/one_off/migrate_to_duckdb.py` | One-time SQLite → DuckDB migration |
| `duckdb_writer.py` | Write helpers for dual-write during updates |
| `charting_app/duckdb_queries.py` | Query layer with PIVOT for API compatibility |
| `constants.py` | `USE_DUCKDB`, `DUCKDB_PATH`, connection helpers |

### Checking Status

```powershell
# Check DuckDB stats
python duckdb_writer.py

# Test queries
python charting_app\duckdb_queries.py
```

## API Endpoints

### `/api/data`
Get historical price data with interval support.

```
GET /api/data?tickers=AAPL,MSFT&interval=weekly&from=1609459200&to=1704067200
```

**Response:**
```json
{
  "AAPL": [
    {"time": "2021-01-08", "value": 132.05},
    {"time": "2021-01-15", "value": 127.14}
  ],
  "MSFT": [...]
}
```

### `/api/volume`
Get trading volume data.

```
GET /api/volume?tickers=SPY,QQQ
```

### `/api/metadata`
Get company names for tickers.

```
GET /api/metadata?tickers=AAPL,MSFT
```

**Response:**
```json
{"AAPL": "Apple", "MSFT": "Microsoft"}
```

### `/api/fundamentals/{type}`
Get fundamental data (overview, earnings, income, balance, cashflow).

```
GET /api/fundamentals/earnings?ticker=AAPL
```

### `/api/ticker-aliases`
Returns ticker alias mapping for share classes with identical financials.

```
GET /api/ticker-aliases
→ { "GOOGL": "GOOG", "BRK-B": "BRK-A", ... }
```

Fundamentals endpoints automatically resolve aliases (e.g., GOOGL queries use GOOG data). The UI shows hints like "GOOGL → GOOG (fundamentals)" in chip tooltips and modal headers.

### `/api/workspace`
- **GET**: Load saved workspace configuration
- **POST**: Save current workspace

### `/api/health`
Basic server and database health check.

## Configuration

### Frontend (`charting_sandbox/config.js`)

```javascript
window.ChartConfig = {
    TRADING_DAYS_PER_YEAR: 252,
    COLORS: [...],              // 24-color palette
    VOLUME_WINDOW: 100,         // Rolling volume SMA window
    DEBOUNCE_MS: {
        REBASE: 500,
        SAVE: 2000,
        PLOT: 100
    },
    MAX_TICKERS_PER_CHART: 30,
    FONT_SIZE: { MIN: 8, MAX: 24, DEFAULT: 12 },
};
```

### Backend (`constants.py`)

```python
DB_PATH = "market_data.db"
TRADING_DAYS_PER_YEAR = 252
BATCH_SIZE = 50
MAX_RETRIES = 3
```

## Common Tasks

### Adding New Tickers

1. Add ticker to appropriate list in `download_all_assets.py`:
   ```python
   EV_STOCKS = ["TSLA", "RIVN", "NEWTICKER"]
   ```

2. Download data:
   ```powershell
   python download_single_ticker.py NEWTICKER
   # or full update:
   python update_market_data_fixed.py --batch-size 20
   ```

3. Metadata is fetched and cleaned automatically.

### Adding a Chart Feature

1. **UI Controls**: Add markup + IDs in `charting_sandbox/chart-dom-builder.js` (`createChartCard()`), then expose them in `getCardElements()`.
2. **State + Persistence**:
   - Add defaults + persisted fields in `charting_sandbox/chart-card-context.js` (`create()` + `syncToCard()`).
   - Read/write runtime state via `ctx.*` in `charting_sandbox/card.js` (use `persistState()` or `syncToCard(ctx)` + `saveCards()`).
   - Add the field to `saveCards()` in `charting_sandbox/card.js` and to `restoreCard()` so it round-trips through the workspace JSON.
3. **Event Binding**: Add handlers in `charting_sandbox/card.js`, then bind via `charting_sandbox/chart-event-handlers.js` (`bindAllWithCleanup()`).
   - Sliders: prefer `ChartUtils.bindSliderControl`.
   - Ticker chips: keep interactions in `charting_sandbox/card-event-binder.js`.
4. **Plot / Data**:
   - If it's a pane, implement a helper next to existing ones (`charting_sandbox/chart-volume.js`, `charting_sandbox/chart-fundamentals-pane.js`) and call it from `plot()`.
   - If it's price-series behavior, extend `charting_sandbox/chart-series-manager.js` instead of growing `plot()`.
   - Any API calls: use `ChartUtils.apiUrl()` / `DataFetcher.fetchWithRetry()` and pass an abort `signal` when called from `plot()`.
5. **UI Updates**: Put "derived UI state" helpers (button text, chip refresh, etc.) in `charting_sandbox/chart-updaters.js`.
6. **Cache Bust**: Increment `?v=` in `charting_sandbox/index.html` and `charting_sandbox/canada.html` for any changed JS files.

### Creating a New Page

Edit `charting_app/workspace.json`:

```json
{
  "pages": {
    "54": "My New Page"
  },
  "cards": [
    {
      "page": "54",
      "tickers": ["AAPL", "MSFT"],
      "title": "My Chart"
    }
  ]
}
```

### Database Queries

```python
import sqlite3
from constants import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Get all tickers
cursor.execute("PRAGMA table_info(stock_prices_daily);")
tickers = [row[1] for row in cursor.fetchall() if row[1] != 'Date']

# Get price data
cursor.execute("SELECT Date, AAPL FROM stock_prices_daily WHERE AAPL IS NOT NULL")
data = cursor.fetchall()

conn.close()
```

## Data Update Procedure

### Current Workflow

The update requires 3 separate commands run in sequence:

```powershell
python update_market_data.py --assets all --lookback 10
```

### What's Working Well

| Aspect | Implementation |
|--------|----------------|
| **Unified script** | Single command for all 19 asset types |
| **Error handling** | Batch downloads with fallback to individual ticker retry |
| **Data safety** | Atomic updates using staging table + rename |
| **Logging** | Progress tracking with failure summaries |
| **Parallelization** | Threaded downloads via yfinance |
| **Metadata** | Automatic company name fetching |
| **Diagnostics** | `--status` for freshness, `--smoke-check` for API verification |

### Known Issues

1. **~47 expected failures** - Delisted tickers that always fail (noise)
2. **Inefficient DB updates** - Full table read/write for incremental changes
3. **No verification** - No check that SPY/QQQ/AAPL have today's data

### Delisted Tickers to Exclude

Add to `EXCLUDED_TICKERS` in `download_all_assets.py`:

```python
# Acquired/delisted US stocks
'ABC', 'ABB', 'ABML', 'AJBU', 'AJRD', 'ANSS', 'CDAY', 'CONE', 'CTLT',
'DFS', 'FLT', 'FREYR', 'GIGA', 'HES', 'JNPR', 'LTHM', 'MRO', 'NOVA',
'PARA', 'PEAK', 'PKI', 'PLL', 'PXD', 'QTS', 'SDIG', 'SQ', 'WBA', 'WRK', 'ZNGA',

# Brazilian delistings
'BRFS3.SA', 'BRML3.SA', 'CCRO3.SA', 'CIEL3.SA', 'ENBR3.SA', 'HGTX3.SA', 'MRFG3.SA', 'TIMP3.SA',

# Yahoo removed precious metals FX
'XAGUSD=X', 'XAUUSD=X', 'XPDUSD=X', 'XPTUSD=X', 'VX=F',
```

## Troubleshooting

### Charts Not Loading
- Check Flask server is running on port 5000
- Check browser console for errors
- Verify database exists: `ls market_data.db`
- Check API health: `http://localhost:5000/api/health`

### No Data Showing
- Verify data exists: `sqlite3 market_data.db "SELECT Date, AAPL FROM stock_prices_daily ORDER BY Date DESC LIMIT 5;"`
- Check network tab for API errors
- Ensure ticker is uppercase

### Workspace Not Persisting
- Check `charting_app/workspace.json` permissions
- Check Flask logs for save errors
- Backups in `workspace_backups/`

### Cache Issues
Hard refresh to clear JavaScript cache:
- **Windows**: `Ctrl + Shift + R`
- **Mac**: `Cmd + Shift + R`

## Development Tips

### Debugging
1. **Browser Console**: JavaScript errors
2. **Network Tab**: API calls and responses
3. **Flask Logs**: Backend errors (printed to console)
4. **Database**: `sqlite3 market_data.db` for direct queries

### Cache Busting
When modifying JS files, increment version in `index.html`:
```html
<script src="card.js?v=NN"></script>
```

### State Management
- Card-level state: `card._property` pattern
- Auto-save: Debounced (2000ms) on user interactions
- Backend-first restore: Loads from `/api/workspace` on page load

## Testing

### Unit Tests (Node)

Fast deterministic tests for the extracted modules.

```powershell
npm run test:unit
```

**Files:**
| File | Purpose |
|------|---------|
| `tests/unit/chart-card-context.test.js` | Context create/serialize/apply round-trip |
| `tests/unit/chart-card-registry.test.js` | Card type registration + dispatch |
| `tests/unit/chart-dashboard.test.js` | Dashboard serialize/restore round-trip |
| `tests/unit/chart-macro-dashboard.test.js` | Macro dashboard serialize/restore |
| `tests/unit/chart-utils.test.js` | ensureStyleTag idempotency, mapToObject |
| `tests/unit/dashboard-base.test.js` | filterAndSortData, escapeHtml |
| `tests/unit/helpers/browser-stub.js` | Minimal window/document stub |
| `tests/unit/helpers/load-module.js` | vm-based module loader |

**Test architecture:**
- Uses Node's built-in test runner (`node --test`)
- Loads browser modules via `vm` (no jsdom dependency)
- Tests pure functions: state management, serialization, registry dispatch, dashboard filtering/sorting

### Playwright Smoke Tests

Automated browser tests ensure card.js refactoring doesn't break core functionality.

```powershell
# Install test dependencies (first time)
npm install
npx playwright install chromium

# Run smoke tests
npm run test:smoke
```

**Test coverage (6 tests):**
- Initial plot, Fit, range dropdown, and pane toggles
- Workspace restore with saved card state
- Page switching hides/shows correct pages
- Tag filtering in normal and highlights mode
- Nav label updates when removing ticker from an untitled card
- Dashboard Reset Layout and Export CSV buttons

**Test architecture:**
- Tests run against isolated static server (no Flask backend needed)
- LightweightCharts stubbed for deterministic behavior
- API responses mocked with synthetic data
- `Date.now()` frozen for reproducible timestamps

**Files:**
| File | Purpose |
|------|---------|
| `tests/playwright/card-smoke.spec.js` | Main test file |
| `tests/playwright/helpers/static-server.js` | Static file server |
| `tests/playwright/stubs/lightweight-charts-stub.js` | Chart library mock |
| `playwright.config.js` | Test configuration |

**CI Integration:**
Tests run automatically on GitHub Actions for all PRs and pushes to `main`. See `.github/workflows/playwright-smoke.yml`.

## Performance Considerations

- **Data Density**: LightweightCharts needs ~1 pixel per bar minimum
- **Interval Selection**: Auto-switching prevents rendering thousands of bars
- **Wide-Column Schema**: Single query fetches multiple tickers
- **Debouncing**: Range changes debounced to reduce re-renders

## Future Enhancements

### High Priority
- **Error boundaries in UI** - Show retry button when chart fails
- **Health dashboard** - Show data freshness per category

### Medium Priority
- **Batch API requests** - Single endpoint for multiple charts
- **Database indexes** - Speed up queries as data grows
- **Keyboard shortcuts** - `Ctrl+S` save, `R` reset zoom, `D/W/M` intervals

### Lower Priority
- **Web Worker** - Offload rebasing/SMA calculations
- **Options data integration**
- **Drawing tools** - Trendlines, Fibonacci retracements

### card.js Architecture (Current)

`charting_sandbox/card.js` is the orchestrator (~660 lines) handling card lifecycle, persistence wiring, and delegating to extracted modules. Most logic is split out:

**Core modules:**
- `chart-card-context.js` (~450 lines) — Persistent per-card state (`ctx.*`) + `initRuntime()` for mutable runtime state + `syncToCard()` bridge to `card._*` for workspace persistence.
- `chart-card-plot.js` (~860 lines) — Plot orchestration: `plot(ctx)`, `destroyChart(ctx)`, `destroyChartAndReplot(ctx)`, `applyResize(ctx)`, `updateZeroLine(ctx)`, `updateFixedLegend(ctx)`.
- `chart-card-toggles.js` (~380 lines) — Pane toggle handlers: `createToggleHandlers(ctx, callbacks)`, `createToggleMetric(ctx)`, `initMetricButtons(ctx)`.
- `chart-card-range.js` — Fit/range/interval handlers: `createRangeHandlers(ctx, callbacks)`.
- `chart-card-meta.js` — Star/tags/notes UI: `initAll(ctx)`.
- `chart-card-tickers.js` — Ticker chips + axis/context menu: `initGlobalChipContextMenu()`, `createHandlers(ctx, callbacks)`.
- `chart-card-registry.js` — Card type registry + restoreCard dispatch.
- `sandbox-init.js` — index.html bootstrap (workspace restore on DOMContentLoaded).

**Supporting modules:**
- `chart-dom-builder.js` — DOM creation + element lookup + ticker parsing.
- `chart-event-handlers.js` — Centralized event binding with cleanup (`bindAllWithCleanup()` returns `unbind()`).
- `chart-updaters.js` — UI-only update helpers.
- `card-event-binder.js` — Ticker chip interactions.
- `chart-series-manager.js` — Price series setup.
- `chart-volume.js` — Volatility + trading volume panes.
- `chart-fundamentals-pane.js` — Revenue + fundamentals panes.
- `chart-utils.js` — Shared utilities (`apiUrl`, pane bootstrap, alias cache, etc.).

**ctx.runtime contract:**
Mutable runtime state lives on `ctx.runtime` (initialized via `ChartCardContext.initRuntime(ctx)`):
```javascript
ctx.runtime = {
    // Chart instances (recreated on toggle)
    chart, volPane, volumePane, revenuePane, fundamentalsPane,

    // Series references
    avgSeries, zeroLineSeries, priceSeriesMap, volSeriesMap,
    volumeSeriesMap, revenueSeriesMap, fundamentalSeriesMap,

    // Data caches
    rawPriceMap, latestRebasedData,

    // Event handlers (for cleanup)
    crosshairHandler, rangeSaveHandler, tickerLabelHandler,
    fixedLegendCrosshairHandler, debouncedRebase,

    // Abort controller for cancelling in-flight fetches
    plotAbortController
};
```
Persisted state stays on `ctx` directly (e.g., `ctx.showVolPane`, `ctx.visibleRange`).

**Completed refactors:**
- Context/state-object migration (`ctx` authoritative at runtime; `syncToCard()` keeps persistence fields in sync).
- Event binding consolidation + teardown symmetry.
- Pane extraction into helpers + shared pane bootstrap.
- Abortable fetches (AbortController) to prevent stale async updates.
- Card type routing via `ChartCardRegistry`.
- `createChartCard` API normalization (string/array/options supported; positional args deprecated).
- Plot orchestration extracted to `chart-card-plot.js`.
- Toggle handlers extracted to `chart-card-toggles.js`.
- Range/interval handlers extracted to `chart-card-range.js`.
- Star/tags/notes UI extracted to `chart-card-meta.js`.
- Ticker/chip management extracted to `chart-card-tickers.js`.
- Registry + bootstrap extracted (`chart-card-registry.js`, `sandbox-init.js`).
- Regression coverage added (unit + Playwright smoke tests).

**Optional next steps:**
- Serialize directly from `ctx` (reduce reliance on `card._*` as the persistence source of truth).

## Dendrogram System

### Overview
`hierarchical_analysis.py` generates correlation dendrograms and clustermaps for stock groups.

### Regeneration
```powershell
python hierarchical_analysis.py
```
Outputs PNGs to root directory (gitignored with `*.png`), served via Flask at `/sandbox/dendrograms/`.

### Supported Groups
- US sectors: ai, tech, consumer, crypto, defense, energy, financials, reits, top50
- International: brazil, china, countries
- China sub-sectors: china_tech, china_consumer, china_energy, china_ev, china_financials, china_healthcare, china_industrials, china_realestate

### File Naming Convention
```
dendrogram_{group}.png           # Full history (2+ years)
dendrogram_{group}_2024.png      # Yearly
dendrogram_{group}_2024_Q1.png   # Quarterly
dendrogram_{group}_2024_01.png   # Monthly
clustermap_{group}_*.png         # Same pattern for clustermaps
```

### Name Mappings
Name mappings convert tickers to human-readable display names:
```python
BRAZIL_NAMES = {
    'PETR4.SA': 'Petrobras',
    'VALE3.SA': 'Vale',
    ...
}
```
Functions accept `name_map` parameter to override default ticker labels.

### Data Threshold
- Requires **30% of trading days** in the period to include a ticker
- For 2024 (~365 days), need ~109 data points minimum
- Sparse data causes empty dendrograms - run `update_market_data.py` to backfill

### Frontend
`charting_sandbox/chart-dendrograms.js` displays dendrograms via dropdown with time period selection.

---

## Documentation

### Core Reference
| Document | Purpose |
|----------|---------|
| **[CODEMAP.md](CODEMAP.md)** | Code architecture, line references, common patterns |
| **[UNIFIED_ARCHITECTURE.md](UNIFIED_ARCHITECTURE.md)** | Single-table design philosophy |

### How-To Guides
| Document | Purpose |
|----------|---------|
| **[CREATING_PAGES.md](CREATING_PAGES.md)** | Add pages, charts, dropdown categories |
| **[ADDING_TICKERS.md](ADDING_TICKERS.md)** | Add new tickers to database |
| **[BACKUP_README.md](BACKUP_README.md)** | Workspace backup system |

### Data Sources
| Document | Purpose |
|----------|---------|
| **[FRED_INDICATORS_GUIDE.md](FRED_INDICATORS_GUIDE.md)** | 31 economic indicators reference |
| **[MACRO_PAGES_GUIDE.md](MACRO_PAGES_GUIDE.md)** | Recession signals, macro interpretation |
| **[BOND_DATA_GUIDE.md](BOND_DATA_GUIDE.md)** | Bond data sources |
| **[IMPLIED_VOLATILITY_GUIDE.md](IMPLIED_VOLATILITY_GUIDE.md)** | CBOE IV indices |

### Design Docs
| Document | Purpose |
|----------|---------|
| **[Color Assignment System](docs/color-assignment-system.md)** | Hybrid color algorithm for chart series |
| **[INDEX_UPDATE_STRATEGY.md](INDEX_UPDATE_STRATEGY.md)** | Index update procedures |
| **[PORTFOLIO_GUIDE.md](PORTFOLIO_GUIDE.md)** | Portfolio management, ALLW replication |
