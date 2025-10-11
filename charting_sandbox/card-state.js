/**
 * Card State Management
 * Encapsulates all state for a chart card
 */

class CardState {
    constructor(options = {}) {
        // UI state
        this.showDiff = options.showDiff || false;
        this.showAvg = options.showAvg || false;
        this.showVolPane = options.showVol || false;
        this.showVolumePane = options.showVolume || false;
        this.useRaw = options.useRaw || false;
        this.lastLabelVisible = options.lastLabelVisible !== false;
        this.showZeroLine = options.showZeroLine || false;
        this.showFixedLegend = options.showFixedLegend || false;

        // Chart objects
        this.chart = null;
        this.volPane = null;
        this.volumePane = null;
        this.avgSeries = null;
        this.zeroLineSeries = null;
        this.fixedLegendEl = null;

        // Event handlers
        this.crosshairHandler = null;
        this.debouncedRebase = null;
        this.rangeSaveHandler = null;
        this.skipRangeApplication = false;

        // Data stores
        this.selectedTickers = new Set();
        this.hiddenTickers = new Set(options.hidden || []);
        this.multiplierMap = new Map(Object.entries(options.multipliers || {}));
        this.tickerColorMap = new Map();
        this.priceSeriesMap = new Map();
        this.volSeriesMap = new Map();
        this.volumeSeriesMap = new Map();
        this.rawPriceMap = new Map();
        this.latestRebasedData = {};
        this.colorIndex = 0;

        // Card settings
        this.visibleRange = options.range || null;
        this.title = options.title || '';
        this.height = options.height || 400;
        this.fontSize = options.fontSize || 12;
        this.volumePaneStretchFactor = 1.0;
        this.fixedLegendPos = options.fixedLegendPos || { x: 10, y: 10 };
        this.fixedLegendMinimized = options.fixedLegendMinimized || false;
    }

    /**
     * Store state on card DOM element for persistence
     */
    storeOnElement(cardElement) {
        cardElement._selectedTickers = this.selectedTickers;
        cardElement._showDiff = this.showDiff;
        cardElement._showAvg = this.showAvg;
        cardElement._showVol = this.showVolPane;
        cardElement._showVolume = this.showVolumePane;
        cardElement._useRaw = this.useRaw;
        cardElement._multiplierMap = this.multiplierMap;
        cardElement._hiddenTickers = this.hiddenTickers;
        cardElement._visibleRange = this.visibleRange;
        cardElement._title = this.title;
        cardElement._lastLabelVisible = this.lastLabelVisible;
        cardElement._showZeroLine = this.showZeroLine;
        cardElement._showFixedLegend = this.showFixedLegend;
        cardElement._fixedLegendPos = this.fixedLegendPos;
        cardElement._fixedLegendMinimized = this.fixedLegendMinimized;
        cardElement._height = this.height;
        cardElement._fontSize = this.fontSize;
        cardElement._volumePaneStretchFactor = this.volumePaneStretchFactor;
    }

    /**
     * Get serializable state for persistence
     */
    toJSON() {
        return {
            tickers: Array.from(this.selectedTickers),
            showDiff: this.showDiff,
            showAvg: this.showAvg,
            showVol: this.showVolPane,
            showVolume: this.showVolumePane,
            useRaw: this.useRaw,
            multipliers: Object.fromEntries(this.multiplierMap.entries()),
            hidden: Array.from(this.hiddenTickers),
            range: this.visibleRange,
            title: this.title,
            lastLabelVisible: this.lastLabelVisible,
            showZeroLine: this.showZeroLine,
            showFixedLegend: this.showFixedLegend,
            fixedLegendPos: this.fixedLegendPos,
            fixedLegendMinimized: this.fixedLegendMinimized,
            height: this.height,
            fontSize: this.fontSize
        };
    }
}

window.CardState = CardState;
