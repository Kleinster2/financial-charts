# Code Map - Quick Reference

Quick navigation to key code areas. Prefer symbol/function search over line numbers (they shift during refactors).

## Frontend (`charting_sandbox/`)

### HTML entrypoints
- `index.html` is the main entrypoint.
- Other entrypoints (e.g. `canada.html`, `israel.html`) must include the same card module chain before `card.js`.

**Card module load order (must be before `card.js`):**
- `chart-card-context.js`
- `chart-card-plot.js`
- `chart-card-toggles.js`
- `chart-card-range.js`
- `chart-card-meta.js`
- `chart-card-tickers.js`
- `chart-card-nav.js`
- `chart-card-registry.js`

**Bootstrap (must be after `card.js`):**
- `sandbox-init.js` (workspace restore + autocomplete on `DOMContentLoaded`)

### `card.js` (Chart Card Orchestrator)
Owns DOM creation + wiring; delegates behavior to extracted modules.

**Globals:**
- `window.createChartCard(options)`
- `window.saveCards()`

**Main responsibilities:**
- Card DOM: `ChartDomBuilder.createChartCard()`, `ChartDomBuilder.getCardElements()`
- Context + runtime: `ChartCardContext.create()`, `ChartCardContext.initRuntime()`
- Event binding: `ChartEventHandlers.bindAllWithCleanup()`
- Delegation:
  - Plot/lifecycle: `ChartCardPlot.plot(ctx, options)`
  - Pane/metric toggles: `ChartCardToggles.createToggleHandlers(ctx, callbacks)`
  - Fit/range/interval: `ChartCardRange.createRangeHandlers(ctx, callbacks)`
  - Star/tags/notes: `ChartCardMeta.initAll(ctx)`
  - Ticker chips: `ChartCardTickers.createHandlers(ctx, callbacks)`
  - Nav links: `ChartCardNav.createNavLink()`, `updateNavLabel()`, `removeNavLink()`
  - Special card types + restore: `ChartCardRegistry`

### `chart-card-context.js` (ChartCardContext)
Per-card state object + persistence schema.

**Key APIs:**
- `create(card, elements, options)`
- `initRuntime(ctx)` / `getRuntime(ctx)`
- `syncToCard(ctx)` (bridge to `card._*` for persistence)
- `serialize(ctx)` / `applyToCtx(ctx, cardData)` (workspace schema)

### `chart-card-plot.js` (ChartCardPlot)
Core rendering and chart lifecycle.

**Key APIs:**
- `plot(ctx, options)`
- `destroyChart(ctx)` / `destroyChartAndReplot(ctx)`
- `applyResize(ctx, baseH)`
- `updateFixedLegend(ctx)` / `updateZeroLine(ctx)`
- `getCurrentDataRange(ctx)`
- `ensureNames(tickers, chipNodes)`

**High-level data flow:**
- Chooses `interval` from `ctx.manualInterval` or visible range.
- Fetches via `DataFetcher.getData(tickerList, days, interval, { signal })` (single endpoint for all tickers).
- Creates/updates series via `ChartSeriesManager.setupPriceSeries(...)`.
- Optional panes via `ChartVolumeManager` and `FundamentalsPane`.

### `chart-card-toggles.js` (ChartCardToggles)
Pane + metric toggles.

**Key APIs:**
- `createToggleHandlers(ctx, callbacks)`
- `createToggleMetric(ctx, plot)`
- `initMetricButtons(ctx)` / `updateMetricButtonStates(ctx)`

### `chart-card-range.js` (ChartCardRange)
Fit + range + interval dropdown logic.

**Key APIs:**
- `createRangeHandlers(ctx, callbacks)`
- `handleFit(ctx)`
- `handleRangeChange(ctx)`
- `handleIntervalChange(ctx, plot)`

### `chart-card-meta.js` (ChartCardMeta)
Star/tags/notes UI.

**Key API:**
- `initAll(ctx)`

### `chart-card-tickers.js` (ChartCardTickers)
Ticker chips (add/remove), axis assignment, global chip context menu.

**Key APIs:**
- `initGlobalChipContextMenu()`
- `createHandlers(ctx, { plot })` returning:
  - `addTickerFromInput()`
  - `handleChipRemove(ticker, chipEl)`
  - `renderChips()`
  - `bindChipInteractions()`
  - `getAxis(ticker)` / `onAxisChange(ticker, axis)`

### `chart-card-nav.js` (ChartCardNav)
Navigation link management for chart cards in sidebar.

**Key APIs:**
- `createNavLink(cardId, title, tickers, page)` - Creates nav link with click handler
- `updateNavLabel(navLink, title, tickers, cardId)` - Updates label text
- `removeNavLink(navLink)` - Removes from DOM
- `computeLabel(title, tickers, cardId)` - Shared label logic (title > first ticker > cardId)

### `chart-card-registry.js` (ChartCardRegistry)
Card type registry + workspace restore dispatch.

**Key APIs:**
- `register(type, handler)`
- `hasType(type)` / `getHandler(type)`
- `dispatchCreate(type, wrapper, options)`
- `restoreCard(cardData)`

### `sandbox-init.js` (SandboxInit)
Index-only bootstrap (autocomplete population + workspace restore).

**Key APIs:**
- `populateAutocomplete()`
- `restoreWorkspace()`

### Other important frontend modules
- `chart-dom-builder.js` - card DOM template + `getCardElements()` + ticker parsing
- `chart-event-handlers.js` - event binding with teardown support
- `card-event-binder.js` - chip click + multiplier input wiring
- `pages.js` - multi-page UI + combined filters (tag + highlights)
- `data-fetcher.js` - API client + workspace save/load
- `state-manager.js` - localStorage + debounced backend persistence
- `dashboard-base.js` - shared dashboard utilities (styles, filter/sort, sortable headers)

## Tests

### Unit (`tests/unit/`)
- `tests/unit/chart-card-context.test.js` - context create/serialize/apply round-trip
- `tests/unit/chart-card-registry.test.js` - registry dispatch/restore
- `tests/unit/helpers/` - browser stubs + vm-based module loader

Run: `npm run test:unit`

### Smoke (`tests/playwright/`)
- `tests/playwright/card-smoke.spec.js` - end-to-end regression smoke (5 tests)

Run: `npm run test:smoke`

## Backend (`charting_app/`)

### `app.py` (Flask API Server)
**Key endpoints:**
- `/api/health`
- `/api/tickers`
- `/api/metadata`
- `/api/data` (supports `interval=daily|weekly|monthly`)
- `/api/volume`
- `/api/revenue`
- `/api/fundamentals`
- `/api/workspace` (cards + pages metadata)

## Common Patterns

### Add a New Persisted Per-Card Setting
1. Add UI control in `chart-dom-builder.js` and selector in `getCardElements()`.
2. Add persisted field to `ChartCardContext.create()` (default + init).
3. Ensure persistence via:
   - `ChartCardContext.syncToCard(ctx)` (sets `card._yourField`)
   - `ChartCardContext.serialize(ctx)` (workspace schema)
   - `ChartCardContext.applyToCtx(ctx, cardData)` (hydration)
4. Bind behavior in the most relevant extracted module:
   - update `ctx`
   - call `ChartCardContext.syncToCard(ctx)`
   - call `ctx.saveCards()` / `ctx.debouncedSaveCards()`
   - call `plot()` if it affects rendering

### Cache Busting
Increment the `?v=` query param in `index.html` for the file you changed.
