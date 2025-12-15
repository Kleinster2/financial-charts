# Ticker Labels Feature

## Overview
Custom HTML ticker labels that display ticker symbols on the right side of the chart at each series' last visible price level. This provides an alternative to the built-in LightweightCharts last value labels.

## Files Modified/Created

### New Files
- **chart-ticker-labels.js** - Core module for managing ticker label HTML elements and positioning

### Modified Files
- **index.html** - Added script tag for ticker labels module
- **chart-dom-builder.js** - Added "Last Ticker" toggle button
- **card.js** - Integrated ticker labels with chart lifecycle and event handling
- **chart-series-manager.js** - Added `onRebaseComplete` callback for label updates
- **config.js** - Replaced light pink colors with darker alternatives (#C71585, #C2185B)

## Architecture

### Module: ChartTickerLabels (chart-ticker-labels.js)

#### Key Methods

**`createLabelsContainer(chartContainer)`**
- Creates an absolutely positioned overlay container for all ticker labels
- Container spans the full chart area with pointer-events disabled
- Returns the container element

**`_createOrUpdateLabelWithPosition(container, ticker, price, color, series, visible, fontSize, coordinate)`** *(private)*
- Creates or updates an individual ticker label with explicit position
- Uses provided coordinate or calculates from `series.priceToCoordinate(price)`
- Applies contrasting text color (black/white) based on background
- Parameters:
  - `container` - Labels container element
  - `ticker` - Ticker symbol string
  - `price` - Current price value (for reference)
  - `color` - Background color for the label
  - `series` - LightweightCharts series object (for fallback calculation)
  - `visible` - Boolean to show/hide label
  - `fontSize` - Font size in pixels
  - `coordinate` - Y coordinate in pixels (if null, calculates from series)

**`_preventLabelOverlap(labelData, fontSize)`** *(private)*
- Detects and prevents label overlaps
- Two-pass algorithm: greedy stacking + group redistribution
- Modifies `adjustedCoordinate` property in place
- Parameters:
  - `labelData` - Array of label data objects with targetCoordinate
  - `fontSize` - Font size in pixels

**`_redistributeLabels(labelData, fontSize)`** *(private)*
- Second-pass redistribution for clustered labels
- Groups nearby labels and centers them around their average target
- Parameters:
  - `labelData` - Array of label data objects (must be sorted)
  - `fontSize` - Font size in pixels

**`updateAllLabels(container, priceSeriesMap, tickerColorMap, hiddenTickers, tickerDataSource, chart, labelsVisible, fontSize, preventOverlap = true)`**
- Updates all ticker labels in the chart
- Finds the last visible data point based on chart's visible time range
- Applies overlap prevention algorithm (if enabled)
- Creates/updates labels for all visible series with adjusted positions
- Removes labels for tickers no longer in the chart
- Parameters:
  - `container` - Labels container element
  - `priceSeriesMap` - Map of ticker to LightweightCharts series
  - `tickerColorMap` - Map of ticker to color
  - `hiddenTickers` - Set of hidden ticker symbols
  - `tickerDataSource` - Map or Object containing price data (raw or rebased)
  - `chart` - LightweightCharts instance
  - `labelsVisible` - Boolean to show/hide all labels
  - `fontSize` - Font size in pixels
  - `preventOverlap` - Enable collision detection (default: true)

**`removeLabel(container, ticker)`** - Removes a specific ticker label

**`clearAllLabels(container)`** - Removes all ticker labels

**`setLabelsVisibility(container, visible)`** - Shows/hides all labels

**`updateFontSize(container, fontSize)`** - Updates font size for all labels

**`_getContrastColor(hexColor)`** - Calculates contrasting text color (private)

### Integration Points

#### Module Integration

**State Management** (`chart-card-context.js`)
- `ctx.lastTickerVisible` - Boolean state for ticker label visibility
- `ctx.runtime.tickerLabelsContainer` - Container element reference
- `ctx.runtime.tickerLabelHandler` - Subscription handler for range changes

**Lifecycle Events** (`chart-card-plot.js`)

1. **Chart Creation** (`chart-card-plot.js:419`)
   ```javascript
   rt.tickerLabelsContainer = window.ChartTickerLabels.createLabelsContainer(chartBox);
   ```

2. **Initial Plot** (`chart-card-plot.js:642-648`)
   - Updates labels after series are created
   - Only updates if in raw mode or rebased data exists

3. **Range Change Subscription** (`chart-card-plot.js:659-663`)
   - Unsubscribes from previous handler to prevent memory leaks
   - In **raw mode**: Updates immediately (50ms delay)
   - In **percentage mode**: Skips update (rebasing callback handles it)

4. **Rebasing Complete** (`chart-card-plot.js:717-720`)
   - Updates labels after dynamic rebasing completes (500ms delay)
   - Called via `onRebaseComplete` callback

**Toggle Button** (`chart-card-toggles.js:151-152, 205-208`)
   - Shows/hides all labels via `setLabelsVisibility()`
   - Updates labels after mode switch via `updateAllLabels()`

**Chip Remove** (`chart-card-tickers.js:165-166`)
   - Removes label when ticker chip is deleted

**Font Size Wiring** (`card.js:421-422`)
   - Updates label font size via slider

#### Timing Strategy

**Raw Mode:**
- Initial update: Immediate (after plot)
- Range changes: 50ms delay
- Mode switching: Immediate via plot()

**Percentage Mode:**
- Initial update: Only if rebased data exists
- Range changes: No immediate update
- Rebasing: 500ms delay (via onRebaseComplete)
- Mode switching: Via plot() + rebasing

This prevents race conditions where labels update with stale data before rebasing completes.

## Key Design Decisions

### 1. HTML Overlay vs Canvas
Used HTML elements overlaid on the chart rather than canvas drawing:
- **Pros**: Easier styling, automatic text rendering, simple positioning
- **Cons**: More DOM elements, potential performance impact with many tickers
- **Rationale**: Better maintainability and styling flexibility

### 2. Series-Based Coordinate Conversion
Uses `series.priceToCoordinate(price)` instead of manual calculation:
- **Pros**: Automatically accounts for chart scale, padding, and transformations
- **Cons**: Requires access to the series object
- **Rationale**: More reliable and works with any chart configuration

### 3. Last Visible Point
Labels use the rightmost visible data point, not the absolute last point:
- **Pros**: Labels align with visible chart data when zoomed
- **Cons**: More complex logic
- **Rationale**: Better UX when user has zoomed or panned

### 4. Separate Toggle from Last Label
Independent "Last Ticker" button separate from "Last Label":
- **Pros**: Users can control ticker labels and price labels independently
- **Cons**: More UI buttons
- **Rationale**: Different use cases (tickers for identification vs prices for values)

### 5. Mode-Specific Update Strategy
Different update strategies for raw vs percentage modes:
- **Pros**: Prevents race conditions and stale data
- **Cons**: More complex logic
- **Rationale**: Percentage mode requires waiting for rebasing to complete

## Positioning

**Horizontal**: `right: 10px` - Near right edge in price scale area

**Vertical**: `series.priceToCoordinate(price) - (fontSize / 2)` - Centered on price level

**Z-Index**: `10` - Above chart, below tooltips

## Styling

```javascript
{
    position: 'absolute',
    padding: '2px 6px',
    borderRadius: '3px',
    fontWeight: 'bold',
    fontSize: `${fontSize}px`,
    fontFamily: 'Trebuchet MS, sans-serif',
    backgroundColor: color,
    color: contrastColor,  // Auto-calculated black or white
    transition: 'top 0.2s ease-out'
}
```

## Event Flow

### Initial Chart Load
1. Create labels container
2. Plot series data
3. Update ticker labels with initial data
4. Subscribe to range changes
5. Setup rebasing with onRebaseComplete callback

### User Zooms/Pans (Percentage Mode)
1. User changes visible range
2. Rebasing callback triggers (500ms debounce)
3. Chart data rebased to new leftmost point
4. `latestRebasedData` updated
5. `onRebaseComplete` callback fires
6. Ticker labels update with new rebased data

### User Zooms/Pans (Raw Mode)
1. User changes visible range
2. Range change handler triggers (50ms delay)
3. Ticker labels update positions (data unchanged)

### User Toggles Mode (Raw ↔ Percentage)
1. `useRaw` state flips
2. `plot()` called
3. Previous subscriptions cleaned up
4. New subscriptions created with current `useRaw` value
5. Labels update with appropriate data source

## Overlap Prevention

When multiple tickers have similar prices, labels can overlap. The module includes automatic collision detection and repositioning:

### Algorithm

**Two-Pass System:**
1. **First Pass**: Greedy stacking
   - Sort labels by vertical position (top to bottom)
   - For each label, check if it overlaps with the previous one
   - If overlap detected, push current label down by minimum spacing
   - Minimum spacing = `fontSize + 4px`

2. **Second Pass**: Group redistribution
   - Identify clusters of labels that were pushed close together
   - Calculate center point of each cluster
   - Redistribute cluster labels evenly around the center
   - Ensures labels stay near their target prices while preventing overlap

### Example

```
Before (overlapping):          After (adjusted):
IONQ  ────                     IONQ  ────
QUBT  ────  (overlap!)         RGTI  ────  (4px gap)
RGTI  ────                     QUBT  ────  (4px gap)
QBTS  ────                     QBTS  ────
```

### Configuration

Overlap prevention is **enabled by default**. To disable:

```javascript
window.ChartTickerLabels.updateAllLabels(
    container, priceSeriesMap, tickerColorMap, hiddenTickers,
    tickerData, chart, labelsVisible, fontSize,
    false  // preventOverlap = false
);
```

### Edge Cases

- **Top boundary**: Labels won't be pushed above Y=0
- **Small groups**: Labels with distant neighbors are not redistributed
- **Dynamic updates**: Positions recalculate on every zoom/pan

## Known Limitations

1. **Performance**: With 20+ tickers, DOM manipulation may cause slight lag
2. **Vertical space**: With many tickers in a small price range, labels may extend beyond chart bounds
3. **Mobile**: Labels may be too small on mobile devices (controlled by font slider)
4. **Export**: HTML labels don't appear in PNG exports (only chart canvas exports)
5. **Connector lines**: Adjusted labels don't show visual connectors to actual price (future enhancement)

## Future Enhancements

- [ ] Option to show price value alongside ticker
- [ ] Customizable label position (left/right/top/bottom)
- [ ] Visual connector lines from adjusted label to actual price level
- [ ] Include labels in chart exports
- [ ] Animation when labels move
- [ ] Smart label hiding when too many tickers
- [ ] Alternative layout modes (staggered, compact, etc.)
