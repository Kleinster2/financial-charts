# Card.js Refactoring - Completion Guide

## Current Situation

✅ **Analysis & Planning**: Complete
✅ **Class Skeleton**: Ready (`card-refactored-temp.js` - 556 lines)
✅ **Helper Modules**: Identified and ready to use
⏳ **Implementation**: Ready to complete (~2-3 hours of focused work)

## What's Left: Fill in 5 Key Methods

The skeleton has TODO placeholders. Here's exactly what to implement:

### Method 1: `renderTickerChips()` - 10 minutes

**Location**: Line ~450 in `card-refactored-temp.js`

**Replace TODO with:**
```javascript
renderTickerChips() {
    window.ChartDomBuilder.addTickerChips(
        this.elements.selectedTickersDiv,
        this.selectedTickers,
        this.tickerColorMap,
        this.multiplierMap,
        this.hiddenTickers,
        (ticker) => this.handleChipRemove(ticker)
    );
}

handleChipRemove(ticker) {
    this.selectedTickers.delete(ticker);
    this.hiddenTickers.delete(ticker);
    this.multiplierMap.delete(ticker);
    this.renderTickerChips();
    this.saveState();
}
```

**Why it works**: Delegates to existing `ChartDomBuilder.addTickerChips()`

---

### Method 2: `async addTicker()` - 10 minutes

**Location**: Line ~400 in skeleton

**Replace with:**
```javascript
async addTicker() {
    const input = window.ChartDomBuilder.normalizeTicker(
        this.elements.tickerInput.value
    );

    if (!input || this.selectedTickers.has(input)) {
        this.elements.tickerInput.value = '';
        return;
    }

    this.selectedTickers.add(input);

    // Assign color
    if (!this.tickerColorMap.has(input)) {
        this.tickerColorMap.set(input, window.ChartConfig.getTickerColor(input));
    }

    this.renderTickerChips();
    this.elements.tickerInput.value = '';
    this.saveState();
}
```

**Why it works**: Uses existing `normalizeTicker()` and `getTickerColor()`

---

### Method 3: `async plot()` - 60 minutes

**Location**: Line ~300 in skeleton

**Strategy**: Copy from original (lines 598-1438) and convert variables

**Key conversions needed:**
- `chart` → `this.chart`
- `selectedTickers` → `this.selectedTickers`
- `useRaw` → `this.useRaw`
- `card._property` → `this.property`
- `chartBox` → `this.elements.chartBox`

**Simplified version** (if short on time):
```javascript
async plot() {
    if (!this.chart) {
        this.createChart();
    }

    if (this.selectedTickers.size === 0) return;

    // Clear existing
    window.ChartSeriesManager.clearAllSeries(
        this.chart, this.priceSeriesMap, new Map(), this.avgSeries
    );
    this.avgSeries = null;

    // Fetch data
    const tickerList = Array.from(this.selectedTickers);
    const interval = this.manualInterval || 'daily';
    const data = await window.DataFetcher.getPriceData(tickerList, null, null, interval);

    if (!data) return;

    // Plot each ticker
    for (const ticker of tickerList) {
        if (this.hiddenTickers.has(ticker)) continue;
        const tickerData = data[ticker];
        if (!tickerData) continue;

        const rawData = tickerData.filter(d => d.value != null);
        this.rawPriceMap.set(ticker, rawData);

        const mult = this.multiplierMap.get(ticker) || 1;
        const plotData = this.useRaw ? rawData :
            window.ChartSeriesManager.rebaseData(rawData, mult);

        if (!this.useRaw) {
            this.latestRebasedData[ticker] = plotData;
        }

        const color = this.tickerColorMap.get(ticker);
        window.ChartSeriesManager.createOrUpdateSeries(
            this.chart, ticker, plotData, color, this.priceSeriesMap,
            this.lastLabelVisible, !this.useRaw, this.decimalPrecision
        );
    }

    if (this.showAvg && !this.useRaw) {
        this.avgSeries = window.ChartSeriesManager.updateAverageSeries(
            this.chart, this.latestRebasedData, this.hiddenTickers,
            this.selectedTickers, this.avgSeries
        );
    }
}
```

---

### Method 4: `setupEventHandlers()` - 30 minutes

**Location**: Line ~500 in skeleton

**Copy from original** (lines 1440-2310) and adapt:

**Key pattern**:
```javascript
// Original closure style:
plotBtn.addEventListener('click', plot);

// Convert to class style:
this.elements.plotBtn.addEventListener('click', () => this.plot());
```

**Essential handlers to implement**:
1. Add ticker button → `this.addTicker()`
2. Plot button → `this.plot()`
3. Fit button → fit to data range
4. Height slider → `this.setHeight()`
5. Font slider → `this.setFontSize()`
6. Interval select → update and replot
7. Title input → update nav link
8. Remove card → cleanup and remove

**Template**:
```javascript
setupEventHandlers() {
    const el = this.elements;

    // Add ticker
    el.addBtn?.addEventListener('click', () => this.addTicker());
    el.tickerInput?.addEventListener('keypress', e => {
        if (e.key === 'Enter') this.addTicker();
    });

    // Plot
    el.plotBtn?.addEventListener('click', () => this.plot());

    // Fit
    el.fitBtn?.addEventListener('click', () => {
        if (!this.chart) return;
        const dataRange = this.getCurrentDataRange();
        if (dataRange) {
            this.chart.timeScale().setVisibleRange(dataRange);
            this.visibleRange = dataRange;
            this.saveState();
        }
    });

    // Height slider
    el.heightSlider?.addEventListener('input', (e) => {
        this.height = parseInt(e.target.value);
        this.applyResize(this.height);
        if (el.heightValue) el.heightValue.textContent = this.height;
    });
    el.heightSlider?.addEventListener('change', () => this.saveState());

    // Font slider
    el.fontSlider?.addEventListener('input', (e) => {
        this.fontSize = parseInt(e.target.value);
        this.applyFont(this.fontSize);
        if (el.fontValue) el.fontValue.textContent = this.fontSize;
    });
    el.fontSlider?.addEventListener('change', () => this.saveState());

    // Interval
    el.intervalSelect?.addEventListener('change', (e) => {
        this.manualInterval = e.target.value;
        this.saveState();
        if (this.chart) {
            this.chart.remove();
            this.chart = null;
            this.plot();
        }
    });

    // Title
    el.titleInput?.addEventListener('change', (e) => {
        this.title = e.target.value;
        if (this.navLink) {
            this.navLink.textContent = this.title || `Card ${this.cardId}`;
        }
        this.saveState();
    });

    // Remove card
    el.removeCardBtn?.addEventListener('click', () => {
        if (confirm('Remove this chart?')) {
            if (this.chart) this.chart.remove();
            if (this.navLink) this.navLink.remove();
            this.element.remove();
            this.saveState();
        }
    });

    // Initialize slider displays
    if (el.heightSlider && el.heightValue) {
        el.heightSlider.value = this.height;
        el.heightValue.textContent = this.height;
    }
    if (el.fontSlider && el.fontValue) {
        el.fontSlider.value = this.fontSize;
        el.fontValue.textContent = this.fontSize;
    }
    if (el.intervalSelect && this.manualInterval) {
        el.intervalSelect.value = this.manualInterval;
    }
    if (el.titleInput) {
        el.titleInput.value = this.title;
    }
}
```

---

### Method 5: `createChart()` - Already in skeleton! ✓

This is already implemented in the skeleton. Just verify it works.

---

## Step-by-Step Completion Process

### Step 1: Open skeleton (5 min)
```bash
cd financial-charts/charting_sandbox
code card-refactored-temp.js  # or your editor
```

### Step 2: Fill in methods (90 min)
1. Add `renderTickerChips()` and `handleChipRemove()` - 10 min
2. Add `addTicker()` - 10 min
3. Add `plot()` (use simplified version first) - 60 min
4. Add `setupEventHandlers()` - 30 min

### Step 3: Test (15 min)
```bash
# Keep original as backup
cp card.js card-original-safe.js

# Deploy new version
cp card-refactored-temp.js card.js

# Start server (if not running)
cd ../charting_app
python app.py

# Open browser
# http://localhost:5000/sandbox/
```

**Test checklist:**
- [ ] Page loads without errors
- [ ] Can create a card
- [ ] Can type and add ticker (try SPY)
- [ ] Click Plot - chart appears
- [ ] Can add another ticker (try QQQ)
- [ ] Height slider works
- [ ] Font slider works
- [ ] Can remove ticker (click × on chip)
- [ ] Refresh page - workspace restores

### Step 4: If it works
```bash
# Success! Keep the new version
rm card-original-safe.js
git add card.js
git commit -m "Refactor card.js to class-based architecture"
```

### Step 5: If it breaks
```bash
# Restore original
cp card-original-safe.js card.js
# Debug issues in card-refactored-temp.js
# Try again
```

---

## Quick Wins vs Full Implementation

### Minimal (get it working): 2 hours
- Simplified `plot()` (no volume panes, no diff, just basic charts)
- Essential event handlers only
- Basic ticker management
- **Result**: Clean class structure, basic functionality works

### Full Implementation: 4-6 hours
- Complete `plot()` with all features (volume, diff, fundamentals panes)
- All event handlers (20+ buttons)
- Export functionality
- Advanced UI features
- **Result**: Feature parity with original

**Recommendation**: Start with minimal, test thoroughly, then add features incrementally.

---

## Common Issues & Fixes

### Issue: "chart is not defined"
**Fix**: Change `chart` to `this.chart`

### Issue: "Cannot read property of undefined"
**Fix**: Check `this.elements.propertyName` - might be `null`

### Issue: Colors not working
**Fix**: Ensure `window.ChartConfig.getTickerColor()` exists or fallback:
```javascript
const colors = ['#2962FF', '#E91E63', '#00C853', '#FF6D00'];
this.tickerColorMap.set(ticker, colors[this.selectedTickers.size % colors.length]);
```

### Issue: "plot is not a function"
**Fix**: Change `plot()` to `this.plot()` in event handlers

---

## Benefits You Get

Even with minimal implementation:

✅ **Navigable code**: Jump to methods in IDE
✅ **Clear structure**: 6 logical sections
✅ **Testable**: `new ChartCard()` in console
✅ **Debuggable**: Set breakpoints on specific methods
✅ **Maintainable**: Easy to find and modify features
✅ **Extensible**: Add new methods naturally

---

## Files Reference

| File | Purpose |
|------|---------|
| `card-refactored-temp.js` | Your working file (edit this) |
| `card-pre-refactor-backup.js` | Safe original backup |
| `extracted_methods.txt` | Reference for method implementations |
| `REFACTORING_STATUS.md` | Overall project status |
| `this file` | Step-by-step how-to |

---

## Next Session Checklist

When you're ready to complete this:

- [ ] Read this guide start to finish
- [ ] Open `card-refactored-temp.js`
- [ ] Fill in Method 1 (renderTickerChips) - test it
- [ ] Fill in Method 2 (addTicker) - test it
- [ ] Fill in Method 3 (plot simplified version) - test it
- [ ] Fill in Method 4 (setupEventHandlers) - test it
- [ ] Deploy and test full workflow
- [ ] If working: commit and celebrate! 🎉
- [ ] If not: debug, fix, repeat

**Estimated time**: 2-3 hours of focused work

**Difficulty**: Moderate (mostly copy-paste-adapt)

**Reward**: 2,534-line monolith → clean, maintainable class! ⭐
