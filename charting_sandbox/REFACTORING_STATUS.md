# Card.js Refactoring Status

## Completed: Incremental Module Extraction (Dec 2024)

Instead of a full class-based rewrite, we took an incremental approach:
- Extracted `plot()` and related functions to `chart-card-plot.js`
- Extracted toggle handlers to `chart-card-toggles.js`
- Extracted range/interval handlers to `chart-card-range.js`
- Extracted star/tags/notes UI to `chart-card-meta.js`
- Extracted ticker chips + context menu to `chart-card-tickers.js`
- Extracted card type registry to `chart-card-registry.js`
- Extracted workspace restore to `sandbox-init.js`
- Added `ctx.runtime` to `ChartCardContext` for shared mutable state

### Results

| File | Lines | Purpose |
|------|-------|---------|
| `card.js` | ~660 | Orchestrator (down from ~2,400) |
| `chart-card-plot.js` | ~860 | Plot logic, chart lifecycle |
| `chart-card-toggles.js` | ~380 | Toggle button handlers |
| `chart-card-context.js` | ~450 | Context + runtime state |
| `chart-card-range.js` | ~230 | Fit/range/interval handlers |
| `chart-card-meta.js` | ~200 | Star/tags/notes UI |
| `chart-card-tickers.js` | ~280 | Ticker chips + axis/context menu |
| `chart-card-registry.js` | ~125 | Card type registry + restoreCard |
| `sandbox-init.js` | ~180 | Sandbox bootstrap on load |

---

## ctx.runtime Contract

**IMPORTANT**: All chart instance state lives in `ctx.runtime`, not as closure variables.

### What belongs in ctx.runtime

```javascript
ctx.runtime = {
    // Chart instances (LightweightCharts objects)
    chart: null,
    volPane: null,
    volumePane: null,
    revenuePane: null,
    fundamentalsPane: null,

    // Series references
    avgSeries: null,
    zeroLineSeries: null,
    tickerLabelsContainer: null,
    fixedLegendEl: null,

    // Series maps (ticker -> series)
    priceSeriesMap: new Map(),
    volSeriesMap: new Map(),
    volumeSeriesMap: new Map(),
    revenueSeriesMap: new Map(),
    fundamentalSeriesMap: new Map(),

    // Data maps
    rawPriceMap: new Map(),
    latestRebasedData: {},

    // Event handlers (for cleanup)
    crosshairHandler: null,
    debouncedRebase: null,
    rangeSaveHandler: null,
    tickerLabelHandler: null,
    fixedLegendCrosshairHandler: null,

    // Abort controller for cancelling in-flight fetches
    plotAbortController: null,

    // Flags
    skipRangeApplication: false
};
```

### Rules

1. **Never add new closure `let` variables** for chart/series/handler state in `card.js`
2. **Always use `rt.xxx`** (where `const rt = ctx.runtime`) for mutable runtime state
3. **Persisted state stays on `ctx`** (e.g., `ctx.showVolPane`, `ctx.visibleRange`)
4. **Runtime state stays on `ctx.runtime`** (chart instances, series maps, handlers)

### Why this matters

- Extracted modules (`chart-card-plot.js`, `chart-card-toggles.js`, `chart-card-range.js`, `chart-card-meta.js`, `chart-card-tickers.js`) receive `ctx` and access `ctx.runtime`
- No "parameter hell" - just pass `ctx`
- Single source of truth for chart state
- Easier to debug (inspect `card._ctx.runtime` in console)

---

## Module Responsibilities

### card.js
- Card DOM creation via `ChartDomBuilder`
- Context initialization via `ChartCardContext`
- Event binding via `ChartEventHandlers`
- Delegates most behavior to extracted modules

### chart-card-plot.js (ChartCardPlot)
- `plot(ctx, options)` - main plot function
- `destroyChart(ctx)` - cleanup chart instance
- `destroyChartAndReplot(ctx, plotFn)` - save range, destroy, replot
- `applyResize(ctx, baseH)` - resize chart box
- `updateZeroLine(ctx)` - zero line visibility
- `updateFixedLegend(ctx)` - fixed legend content
- `getCurrentDataRange(ctx)` - compute data time range
- `ensureNames(tickers, chipNodes)` - company name cache
- `nameCache` - shared name cache

### chart-card-toggles.js (ChartCardToggles)
- `createToggleHandlers(ctx, callbacks)` - returns toggle handler dictionary
- `createToggleMetric(ctx, plot)` - metric toggle helper
- `initMetricButtons(ctx)` - initialize metric button visibility
- `updateMetricButtonStates(ctx)` - update metric button styles

### chart-card-context.js (ChartCardContext)
- `create(card, elements, options)` - create context with persisted state
- `initRuntime(ctx)` - initialize `ctx.runtime` with mutable state
- `getRuntime(ctx)` - get or init runtime
- `syncToCard(ctx)` - sync context to card element properties
- `getButtonStates(ctx)` - get button states for UI
- `serialize(ctx)` - serialize for persistence
- `applyToCtx(ctx, cardData)` - hydrate from saved data

### chart-card-range.js (ChartCardRange)
- `createRangeHandlers(ctx, callbacks)` - returns `{ handleFit, handleRangeChange, handleIntervalChange }`

### chart-card-meta.js (ChartCardMeta)
- `initAll(ctx)` - binds star/tags/notes UI + persistence hooks

### chart-card-tickers.js (ChartCardTickers)
- `initGlobalChipContextMenu()` - idempotent global context menu setup
- `createHandlers(ctx, callbacks)` - returns `{ addTickerFromInput, handleChipRemove, bindChipInteractions, ... }`

### chart-card-registry.js (ChartCardRegistry)
- `register(type, handler)` - register card type handler
- `hasType(type)` - check if type registered
- `getHandler(type)` - get handler for type
- `dispatchCreate(type, ...)` - create card via handler
- `restoreCard(cardData)` - restore card from saved data

### sandbox-init.js
- DOMContentLoaded handler for workspace restore
- Calls `ChartCardRegistry.restoreCard()` for each saved card

---

## Script Load Order (index.html)

```html
<script src="chart-card-context.js"></script>
<script src="chart-card-plot.js"></script>
<script src="chart-card-toggles.js"></script>
<script src="chart-card-range.js"></script>
<script src="chart-card-meta.js"></script>
<script src="chart-card-tickers.js"></script>
<!-- ... other modules ... -->
<script src="chart-card-registry.js"></script>
<script src="card.js"></script>
<script src="sandbox-init.js"></script>  <!-- Must be after card.js -->
```

---

## Future Improvements (Optional)

1. ~~**Extract event handlers** - Move `handleFit`, `handleRangeChange`, etc. to a dedicated module~~ ✓ Done (`chart-card-range.js`)
2. ~~**Extract chip management** - `handleChipRemove`, `addTicker` could be `chart-card-tickers.js`~~ ✓ Done (`chart-card-tickers.js`)
3. **Dashboard consolidation** - Create `DashboardBase` for shared table/sort/filter logic across `chart-dashboard.js`, `chart-macro-dashboard.js`, `chart-thesis-performance.js`
4. **Extract nav link handling** - Centralize `updateNavLabel(ctx)` to replace duplicate callsites in `card.js` and `chart-card-tickers.js`
