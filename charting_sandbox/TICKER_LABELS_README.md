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

**`createOrUpdateLabel(container, ticker, price, color, series, visible, fontSize)`**
- Creates or updates an individual ticker label
- Uses `series.priceToCoordinate(price)` to convert price to pixel Y position
- Applies contrasting text color (black/white) based on background
- Parameters:
  - `container` - Labels container element
  - `ticker` - Ticker symbol string
  - `price` - Current price value to position at
  - `color` - Background color for the label
  - `series` - LightweightCharts series object (for coordinate conversion)
  - `visible` - Boolean to show/hide label
  - `fontSize` - Font size in pixels

**`updateAllLabels(container, priceSeriesMap, tickerColorMap, hiddenTickers, tickerDataSource, chart, labelsVisible, fontSize)`**
- Updates all ticker labels in the chart
- Finds the last visible data point based on chart's visible time range
- Creates/updates labels for all visible series
- Removes labels for tickers no longer in the chart
- Parameters:
  - `tickerDataSource` - Map or Object containing price data (raw or rebased)
  - Other parameters control visibility, styling, and data access

**`removeLabel(container, ticker)`** - Removes a specific ticker label

**`clearAllLabels(container)`** - Removes all ticker labels

**`setLabelsVisibility(container, visible)`** - Shows/hides all labels

**`updateFontSize(container, fontSize)`** - Updates font size for all labels

**`_getContrastColor(hexColor)`** - Calculates contrasting text color (private)

### Integration Points

#### Card.js Integration

**State Management**
- `lastTickerVisible` - Boolean state for ticker label visibility
- `tickerLabelsContainer` - Container element reference
- `tickerLabelHandler` - Subscription handler for range changes

**Lifecycle Events**

1. **Chart Creation** (line 619)
   ```javascript
   tickerLabelsContainer = window.ChartTickerLabels.createLabelsContainer(chartBox);
   ```

2. **Initial Plot** (lines 1221-1232)
   - Updates labels after series are created
   - Only updates if in raw mode or rebased data exists

3. **Range Change Subscription** (lines 1234-1255)
   - Unsubscribes from previous handler to prevent memory leaks
   - In **raw mode**: Updates immediately (50ms delay)
   - In **percentage mode**: Skips update (rebasing callback handles it)

4. **Rebasing Complete** (lines 1303-1312)
   - Updates labels after dynamic rebasing completes (500ms delay)
   - Called via `onRebaseComplete` callback

5. **Toggle Button** (lines 1790-1805)
   - Shows/hides all labels
   - Persists state to workspace

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

## Known Limitations

1. **Performance**: With 20+ tickers, DOM manipulation may cause slight lag
2. **Overlap**: Labels can overlap if prices are very close together
3. **Mobile**: Labels may be too small on mobile devices (controlled by font slider)
4. **Export**: HTML labels don't appear in PNG exports (only chart canvas exports)

## Future Enhancements

- [ ] Auto-adjust label position to prevent overlaps
- [ ] Option to show price value alongside ticker
- [ ] Customizable label position (left/right/top/bottom)
- [ ] Label collision detection
- [ ] Include labels in chart exports
- [ ] Animation when labels move
