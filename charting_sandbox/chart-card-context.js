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
                : saveCards,

            // ═══════════════════════════════════════════════════════════════
            // RUNTIME STATE (not persisted, used by plot/toggle modules)
            // Initialized via initRuntime() after card creation
            // ═══════════════════════════════════════════════════════════════
            runtime: null
        };

        return ctx;
    },

    /**
     * Initialize runtime state on context (chart instances, series maps, handlers)
     * Call this after card creation but before first plot()
     * @param {Object} ctx - The context object
     */
    initRuntime(ctx) {
        ctx.runtime = {
            // Chart instances
            chart: null,
            volPane: null,
            volumePane: null,
            revenuePane: null,
            fundamentalsPane: null,
            diffChart: null,

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
        return ctx.runtime;
    },

    /**
     * Get runtime state, initializing if needed
     * @param {Object} ctx - The context object
     * @returns {Object} Runtime state object
     */
    getRuntime(ctx) {
        if (!ctx.runtime) {
            this.initRuntime(ctx);
        }
        return ctx.runtime;
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
    },

    /**
     * Serialize context to a plain object for persistence
     * Single source of truth for the saved card schema
     * @param {Object} ctx - The context object
     * @returns {Object} Serialized card data
     */
    serialize(ctx) {
        const card = ctx?.card;
        const page = card?.closest('.page')?.dataset?.page || '1';

        return {
            page,
            type: card?._type || null,
            thesisId: card?._thesisId || null,
            tickers: Array.from(ctx?.selectedTickers || []),
            showDiff: !!ctx?.showDiff,
            showAvg: !!ctx?.showAvg,
            showVol: !!ctx?.showVolPane,
            showVolume: !!ctx?.showVolumePane,
            showRevenue: !!ctx?.showRevenuePane,
            showFundamentalsPane: !!ctx?.showFundamentalsPane,
            fundamentalsMetrics: ctx?.fundamentalsMetrics || ['revenue', 'netincome'],
            multipliers: window.ChartUtils.mapToObject(ctx?.multiplierMap),
            hidden: Array.from(ctx?.hiddenTickers || []),
            range: ctx?.visibleRange || null,
            useRaw: !!ctx?.useRaw,
            useLogScale: !!ctx?.useLogScale,
            title: ctx?.title || '',
            lastLabelVisible: ctx?.lastLabelVisible !== false,
            lastTickerVisible: !!ctx?.lastTickerVisible,
            showZeroLine: !!ctx?.showZeroLine,
            showFixedLegend: !!ctx?.showFixedLegend,
            showLegendTickers: !!ctx?.showLegendTickers,
            fixedLegendPos: ctx?.fixedLegendPos || { x: 10, y: 10 },
            fixedLegendSize: ctx?.fixedLegendSize || null,
            height: ctx?.height || window.ChartConfig?.DIMENSIONS?.CHART_MIN_HEIGHT || 400,
            fontSize: ctx?.fontSize || window.ChartConfig?.UI?.FONT_DEFAULT || 12,
            showNotes: !!ctx?.showNotes,
            notes: ctx?.notes || '',
            manualInterval: ctx?.manualInterval || null,
            decimalPrecision: ctx?.decimalPrecision ?? 2,
            tickerColors: window.ChartUtils.mapToObject(ctx?.tickerColorMap),
            priceScaleAssignments: window.ChartUtils.mapToObject(ctx?.priceScaleAssignmentMap),
            volumePaneStretchFactor: ctx?.volumePaneStretchFactor ?? 1.0,
            revenuePaneStretchFactor: ctx?.revenuePaneStretchFactor ?? 1.0,
            fundamentalsPaneStretchFactor: ctx?.fundamentalsPaneStretchFactor ?? 1.0,
            starred: !!ctx?.starred,
            tags: ctx?.tags || []
        };
    },

    /**
     * Apply saved card data to a context object (hydration)
     * Handles legacy field aliases and defensive defaults
     * @param {Object} ctx - The context object to hydrate
     * @param {Object} cardData - Saved card data
     */
    applyToCtx(ctx, cardData) {
        if (!ctx || !cardData) return;

        // ─── Helpers ───────────────────────────────────────────────────────
        const normalizeTicker = (t) =>
            typeof t === 'string' ? t.trim().toUpperCase() : String(t).toUpperCase();

        const parseList = (v) => {
            if (Array.isArray(v)) return v;
            if (typeof v === 'string' && window.ChartDomBuilder?.parseTickerInput) {
                // Delegate to ChartDomBuilder for consistent "TICKER - Name" handling
                return window.ChartDomBuilder.parseTickerInput(v);
            }
            return typeof v === 'string' ? v.split(/[,\s]+/).filter(Boolean) : [];
        };

        const toNumber = (v, fallback) => {
            const n = Number(v);
            return Number.isFinite(n) ? n : fallback;
        };

        const replaceSet = (target, values) => {
            target.clear();
            values.forEach(v => target.add(v));
        };

        const replaceArray = (target, values) => {
            target.length = 0;
            target.push(...values);
        };

        const replaceMap = (target, obj) => {
            target.clear();
            if (obj && typeof obj === 'object') {
                Object.entries(obj).forEach(([k, v]) => target.set(k, v));
            }
        };

        // ─── Tickers ───────────────────────────────────────────────────────
        const rawTickers = cardData.tickers ?? cardData.ticker ?? [];
        const tickerList = parseList(rawTickers).map(normalizeTicker);
        replaceSet(ctx.selectedTickers, tickerList);

        // ─── Hidden tickers ────────────────────────────────────────────────
        const rawHidden = cardData.hidden ?? [];
        replaceSet(ctx.hiddenTickers, parseList(rawHidden).map(normalizeTicker));

        // ─── Maps ──────────────────────────────────────────────────────────
        replaceMap(ctx.multiplierMap, cardData.multipliers);
        replaceMap(ctx.tickerColorMap, cardData.tickerColors);
        replaceMap(ctx.priceScaleAssignmentMap, cardData.priceScaleAssignments);

        // ─── Booleans ──────────────────────────────────────────────────────
        ctx.showDiff = !!cardData.showDiff;
        ctx.showAvg = !!cardData.showAvg;
        ctx.showVolPane = !!(cardData.showVol ?? cardData.showVolPane);  // legacy alias
        ctx.showVolumePane = !!cardData.showVolume;
        ctx.showRevenuePane = !!cardData.showRevenue;
        ctx.showFundamentalsPane = !!cardData.showFundamentalsPane;
        ctx.useRaw = !!cardData.useRaw;
        ctx.useLogScale = !!cardData.useLogScale;
        ctx.lastLabelVisible = cardData.lastLabelVisible !== false;
        ctx.lastTickerVisible = !!cardData.lastTickerVisible;
        ctx.showZeroLine = !!cardData.showZeroLine;
        ctx.showFixedLegend = !!cardData.showFixedLegend;
        ctx.showLegendTickers = !!cardData.showLegendTickers;
        ctx.showNotes = !!cardData.showNotes;
        ctx.starred = !!cardData.starred;

        // ─── Strings ───────────────────────────────────────────────────────
        ctx.title = cardData.title ?? '';
        ctx.notes = cardData.notes ?? '';
        ctx.manualInterval = cardData.manualInterval ?? null;

        // ─── Numbers ───────────────────────────────────────────────────────
        ctx.height = toNumber(cardData.height, window.ChartConfig?.DIMENSIONS?.CHART_MIN_HEIGHT || 400);
        ctx.fontSize = toNumber(cardData.fontSize, window.ChartConfig?.UI?.FONT_DEFAULT || 12);
        ctx.decimalPrecision = toNumber(cardData.decimalPrecision, 2);
        ctx.volumePaneStretchFactor = toNumber(cardData.volumePaneStretchFactor, 1.0);
        ctx.revenuePaneStretchFactor = toNumber(cardData.revenuePaneStretchFactor, 1.0);
        ctx.fundamentalsPaneStretchFactor = toNumber(cardData.fundamentalsPaneStretchFactor, 1.0);

        // ─── Range (legacy alias: range → visibleRange) ────────────────────
        ctx.visibleRange = cardData.range ?? cardData.visibleRange ?? null;

        // ─── Arrays ────────────────────────────────────────────────────────
        const defaultMetrics = ['revenue', 'netincome'];
        const metrics = Array.isArray(cardData.fundamentalsMetrics)
            ? cardData.fundamentalsMetrics
            : defaultMetrics;
        replaceArray(ctx.fundamentalsMetrics, metrics);

        const tags = Array.isArray(cardData.tags) ? cardData.tags : [];
        replaceArray(ctx.tags, tags);

        // ─── Objects ───────────────────────────────────────────────────────
        ctx.fixedLegendPos = cardData.fixedLegendPos ?? { x: 10, y: 10 };
        ctx.fixedLegendSize = cardData.fixedLegendSize ?? null;

        // ─── Sync to card properties ───────────────────────────────────────
        this.syncToCard(ctx);
    }
};
