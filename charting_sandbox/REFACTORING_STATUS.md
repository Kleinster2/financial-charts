# Card.js Refactoring Status

## Completed: Incremental Module Extraction (Dec 2024)

Instead of a full class-based rewrite, we took an incremental approach:
- Extracted `plot()` and related functions to `chart-card-plot.js`
- Extracted toggle handlers to `chart-card-toggles.js`
- Added `ctx.runtime` to `ChartCardContext` for shared mutable state

### Results

| File | Lines | Purpose |
|------|-------|---------|
| `card.js` | ~1,180 | Orchestrator (down from ~2,400) |
| `chart-card-plot.js` | ~760 | Plot logic, chart lifecycle |
| `chart-card-toggles.js` | ~330 | Toggle button handlers |
| `chart-card-context.js` | ~400 | Context + runtime state |

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

- Extracted modules (`chart-card-plot.js`, `chart-card-toggles.js`) receive `ctx` and access `ctx.runtime`
- No "parameter hell" - just pass `ctx`
- Single source of truth for chart state
- Easier to debug (inspect `card._ctx.runtime` in console)

---

## Module Responsibilities

### card.js
- Card DOM creation via `ChartDomBuilder`
- Context initialization via `ChartCardContext`
- Event binding via `ChartEventHandlers`
- Delegates plot/toggle logic to extracted modules

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

---

## Script Load Order (index.html)

```html
<script src="chart-card-context.js"></script>
<script src="chart-card-plot.js"></script>
<script src="chart-card-toggles.js"></script>
<!-- ... other modules ... -->
<script src="card.js"></script>  <!-- Must be last -->
```

---

## Future Improvements (Optional)

1. **Extract event handlers** - Move `handleFit`, `handleRangeChange`, etc. to a dedicated module
2. **Extract chip management** - `handleChipRemove`, `addTicker` could be `chart-card-tickers.js`
3. **Dashboard consolidation** - Create `DashboardBase` for shared table/sort/filter logic across `chart-dashboard.js`, `chart-macro-dashboard.js`, `chart-thesis-performance.js`
