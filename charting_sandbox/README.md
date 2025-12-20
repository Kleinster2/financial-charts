# Charting Sandbox

Frontend UI for the Market Data Workbench.

## Architecture

`card.js` is the orchestrator (~610 lines) handling card lifecycle, persistence wiring, and delegating to extracted modules.

### Core Modules

| File | Lines | Purpose |
|------|-------|---------|
| `card.js` | ~610 | Orchestrator |
| `chart-card-plot.js` | ~860 | Plot logic, chart lifecycle |
| `chart-card-toggles.js` | ~380 | Toggle button handlers |
| `chart-card-context.js` | ~450 | Context + runtime state |
| `chart-card-range.js` | ~230 | Fit/range/interval handlers |
| `chart-card-meta.js` | ~200 | Star/tags/notes UI |
| `chart-card-tickers.js` | ~280 | Ticker chips + axis/context menu |
| `chart-card-nav.js` | ~100 | Nav link create/update/remove |
| `chart-card-registry.js` | ~125 | Card type registry + restoreCard |
| `sandbox-init.js` | ~180 | Sandbox bootstrap on load |

### Supporting Modules

- `chart-dom-builder.js` — DOM creation + element lookup + ticker parsing
- `chart-event-handlers.js` — Centralized event binding with cleanup
- `chart-updaters.js` — UI-only update helpers
- `card-event-binder.js` — Ticker chip interactions
- `chart-series-manager.js` — Price series setup
- `chart-volume.js` — Volatility + trading volume panes
- `chart-fundamentals-pane.js` — Revenue + fundamentals panes
- `chart-utils.js` — Shared utilities (`apiUrl`, pane bootstrap, alias cache, etc.)

### ctx.runtime Contract

All chart instance state lives in `ctx.runtime`, not as closure variables:

```javascript
ctx.runtime = {
    // Chart instances (LightweightCharts objects)
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

**Rules:**
1. Never add new closure `let` variables for chart/series/handler state
2. Always use `rt.xxx` (where `const rt = ctx.runtime`) for mutable runtime state
3. Persisted state stays on `ctx` (e.g., `ctx.showVolPane`, `ctx.visibleRange`)
4. Runtime state stays on `ctx.runtime` (chart instances, series maps, handlers)

---

## Ticker Labels Feature

Custom HTML ticker labels that display ticker symbols on the right side of the chart at each series' last visible price level.

### Module: ChartTickerLabels (`chart-ticker-labels.js`)

**Key Methods:**
- `createLabelsContainer(chartContainer)` — Creates overlay container for labels
- `updateAllLabels(container, priceSeriesMap, ...)` — Updates all ticker labels
- `removeLabel(container, ticker)` — Removes a specific label
- `clearAllLabels(container)` — Removes all labels
- `setLabelsVisibility(container, visible)` — Shows/hides all labels

### Overlap Prevention

When multiple tickers have similar prices, labels can overlap. Two-pass algorithm:
1. **Greedy stacking** — Push overlapping labels down
2. **Group redistribution** — Center clustered labels around average

### Timing Strategy

| Mode | Initial | Range Change | Rebasing |
|------|---------|--------------|----------|
| Raw | Immediate | 50ms delay | N/A |
| Percentage | After rebase | Skip | 500ms delay |

### Known Limitations

1. Performance: With 20+ tickers, DOM manipulation may lag
2. Vertical space: Many tickers in small price range may extend beyond bounds
3. Mobile: Labels may be too small (use font slider)
4. Export: HTML labels don't appear in PNG exports

---

## Script Load Order

```html
<script src="chart-card-context.js"></script>
<script src="chart-card-plot.js"></script>
<script src="chart-card-toggles.js"></script>
<script src="chart-card-range.js"></script>
<script src="chart-card-meta.js"></script>
<script src="chart-card-tickers.js"></script>
<script src="chart-card-nav.js"></script>
<!-- ... other modules ... -->
<script src="chart-card-registry.js"></script>
<script src="card.js"></script>
<script src="sandbox-init.js"></script>  <!-- Must be after card.js -->
```
