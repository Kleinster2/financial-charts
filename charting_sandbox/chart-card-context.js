/**
 * Chart Card Context Module
 *
 * Provides a structured state object for chart cards, replacing closure-based state.
 * This is the foundation for extracting functions from the monolithic card.js.
 *
 * Usage:
 *   const ctx = window.ChartCardContext.create(card, elements, options);
 *   // Access state via ctx.showDiff, ctx.selectedTickers, etc.
 *   // All state is explicit and passable to external functions
 */

window.ChartCardContext = {
    /**
     * Create a new card context with all state initialized
     * @param {HTMLElement} card - The card DOM element
     * @param {Object} elements - DOM elements from ChartDomBuilder.getCardElements()
     * @param {Object} options - Initial options/config
     * @returns {Object} Context object with all card state
     */
    create(card, elements, options = {}) {
        const {
            initialTickers = 'SPY',
            initialShowDiff = false,
            initialShowAvg = false,
            initialShowVol = false,
            initialShowVolume = false,
            initialShowRevenue = false,
            initialShowFundamentalsPane = false,
            initialFundamentalsMetrics = ['revenue', 'netincome'],
            initialUseRaw = false,
            initialUseLogScale = false,
            initialMultipliers = {},
            initialTickerColors = {},
            initialPriceScaleAssignments = {},
            initialHidden = [],
            initialRange = null,
            initialTitle = '',
            initialLastLabelVisible = true,
            initialLastTickerVisible = false,
            initialShowZeroLine = false,
            initialShowFixedLegend = false,
            initialShowLegendTickers = false,
            initialFixedLegendPos = { x: 10, y: 10 },
            initialFixedLegendSize = null,
            initialHeight = (window.ChartConfig?.DIMENSIONS?.CHART_MIN_HEIGHT || 400),
            initialFontSize = (window.ChartConfig?.UI?.FONT_DEFAULT || 12),
            initialShowNotes = false,
            initialNotes = '',
            initialManualInterval = null,
            initialDecimalPrecision = 2,
            initialVolumePaneStretchFactor = 1.0,
            initialRevenuePaneStretchFactor = 1.0,
            initialFundamentalsPaneStretchFactor = 1.0,
            initialStarred = false,
            initialTags = [],
            cardId = null,
            targetPage = '1',
            saveCards = () => {}
        } = options;

        const ctx = {
            // ═══════════════════════════════════════════════════════════════
            // IDENTITY
            // ═══════════════════════════════════════════════════════════════
            cardId,
            targetPage,

            // ═══════════════════════════════════════════════════════════════
            // DOM REFERENCES
            // ═══════════════════════════════════════════════════════════════
            card,
            elements,
            chartBox: elements.chartBox,

            // ═══════════════════════════════════════════════════════════════
            // TICKER STATE (persisted)
            // ═══════════════════════════════════════════════════════════════
            selectedTickers: new Set(),
            hiddenTickers: new Set(initialHidden),
            multiplierMap: new Map(Object.entries(initialMultipliers)),
            tickerColorMap: new Map(Object.entries(initialTickerColors)),
            priceScaleAssignmentMap: new Map(Object.entries(initialPriceScaleAssignments)),

            // ═══════════════════════════════════════════════════════════════
            // VISIBILITY FLAGS
            // ═══════════════════════════════════════════════════════════════
            showDiff: initialShowDiff,
            showAvg: initialShowAvg,
            showVolPane: initialShowVol,
            showVolumePane: initialShowVolume,
            showRevenuePane: initialShowRevenue,
            showFundamentalsPane: initialShowFundamentalsPane,
            showZeroLine: initialShowZeroLine,
            showFixedLegend: initialShowFixedLegend,
            showLegendTickers: initialShowLegendTickers,
            showNotes: initialShowNotes,

            // ═══════════════════════════════════════════════════════════════
            // DISPLAY OPTIONS
            // ═══════════════════════════════════════════════════════════════
            useRaw: initialUseRaw,
            useLogScale: initialUseLogScale,
            lastLabelVisible: initialLastLabelVisible,
            lastTickerVisible: initialLastTickerVisible,
            fundamentalsMetrics: [...initialFundamentalsMetrics],

            // ═══════════════════════════════════════════════════════════════
            // SIZING & LAYOUT
            // ═══════════════════════════════════════════════════════════════
            height: initialHeight,
            fontSize: initialFontSize,
            volumePaneStretchFactor: initialVolumePaneStretchFactor,
            revenuePaneStretchFactor: initialRevenuePaneStretchFactor,
            fundamentalsPaneStretchFactor: initialFundamentalsPaneStretchFactor,
            decimalPrecision: initialDecimalPrecision,
            fixedLegendPos: { ...initialFixedLegendPos },
            fixedLegendSize: initialFixedLegendSize ? { ...initialFixedLegendSize } : null,

            // ═══════════════════════════════════════════════════════════════
            // OTHER STATE
            // ═══════════════════════════════════════════════════════════════
            title: initialTitle,
            notes: initialNotes,
            visibleRange: initialRange,
            manualInterval: initialManualInterval,
            starred: initialStarred,
            tags: [...initialTags],

            // ═══════════════════════════════════════════════════════════════
            // INTERNAL FLAGS
            // ═══════════════════════════════════════════════════════════════
            skipRangeRestoration: false,  // Skip range restoration in pane operations (vs local skipRangeApplication for initial plot)

            // ═══════════════════════════════════════════════════════════════
            // CALLBACKS (for persistence)
            // ═══════════════════════════════════════════════════════════════
            saveCards,
            debouncedSaveCards: (window.ChartUtils?.debounce)
                ? window.ChartUtils.debounce(saveCards, 300)
                : saveCards
        };

        return ctx;
    },

    /**
     * Sync context state to card element properties (for persistence)
     * @param {Object} ctx - The context object
     */
    syncToCard(ctx) {
        const { card } = ctx;
        card._selectedTickers = ctx.selectedTickers;
        card._showDiff = ctx.showDiff;
        card._showAvg = ctx.showAvg;
        card._showVol = ctx.showVolPane;
        card._showVolume = ctx.showVolumePane;
        card._showRevenue = ctx.showRevenuePane;
        card._showFundamentalsPane = ctx.showFundamentalsPane;
        card._fundamentalsMetrics = ctx.fundamentalsMetrics;
        card._useRaw = ctx.useRaw;
        card._useLogScale = ctx.useLogScale;
        card._multiplierMap = ctx.multiplierMap;
        card._tickerColorMap = ctx.tickerColorMap;
        card._priceScaleAssignmentMap = ctx.priceScaleAssignmentMap;
        card._hiddenTickers = ctx.hiddenTickers;
        card._visibleRange = ctx.visibleRange;
        card._title = ctx.title;
        card._lastLabelVisible = ctx.lastLabelVisible;
        card._lastTickerVisible = ctx.lastTickerVisible;
        card._showZeroLine = ctx.showZeroLine;
        card._showFixedLegend = ctx.showFixedLegend;
        card._showLegendTickers = ctx.showLegendTickers;
        card._fixedLegendPos = ctx.fixedLegendPos;
        card._fixedLegendSize = ctx.fixedLegendSize;
        card._height = ctx.height;
        card._fontSize = ctx.fontSize;
        card._volumePaneStretchFactor = ctx.volumePaneStretchFactor;
        card._revenuePaneStretchFactor = ctx.revenuePaneStretchFactor;
        card._fundamentalsPaneStretchFactor = ctx.fundamentalsPaneStretchFactor;
        card._showNotes = ctx.showNotes;
        card._notes = ctx.notes;
        card._manualInterval = ctx.manualInterval;
        card._decimalPrecision = ctx.decimalPrecision;
        card._starred = ctx.starred;
        card._tags = ctx.tags;
    },

    /**
     * Get button states object for ChartDomBuilder.updateButtonStates()
     * @param {Object} ctx - The context object
     * @returns {Object} Button states
     */
    getButtonStates(ctx) {
        return {
            showDiff: ctx.showDiff,
            showVol: ctx.showVolPane,
            showVolume: ctx.showVolumePane,
            showRevenue: ctx.showRevenuePane,
            showFundamentalsPane: ctx.showFundamentalsPane,
            useRaw: ctx.useRaw,
            useLogScale: ctx.useLogScale,
            showAvg: ctx.showAvg,
            lastLabelVisible: ctx.lastLabelVisible,
            lastTickerVisible: ctx.lastTickerVisible,
            showZeroLine: ctx.showZeroLine,
            showFixedLegend: ctx.showFixedLegend,
            showLegendTickers: ctx.showLegendTickers,
            showNotes: ctx.showNotes
        };
    },

    /**
     * Get current font size from context
     * @param {Object} ctx - The context object
     * @returns {number} Font size
     */
    getCurrentFontSize(ctx) {
        return ctx.fontSize || window.ChartConfig?.UI?.FONT_DEFAULT || 12;
    }
};
