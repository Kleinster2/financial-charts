/**
* Lightweight Charts Card Module (Refactored)
* Main orchestrator that uses modular components for chart functionality
*/
(() => {
    const WRAPPER_ID = 'charts-wrapper';
    // Use global config
    const config = window.ChartConfig;
    const VOL_WINDOW = config.VOLUME_WINDOW;
    const PLOT_DEFER_MS = config.DEBOUNCE_MS.PLOT;

    let globalCardCounter = 0;
    const nameCache = {};

    // Height adjust helpers
    const HEIGHT_MIN = window.ChartConfig?.DIMENSIONS?.CHART_MIN_HEIGHT || 400;
    const HEIGHT_MAX = window.ChartConfig?.DIMENSIONS?.CHART_MAX_HEIGHT || 800;
    const PANE_HEIGHT = window.ChartConfig?.DIMENSIONS?.PANE_HEIGHT || 100; // Height to add per active pane

    // Font size controls (axis font only)
    const FONT_MIN = window.ChartConfig?.UI?.FONT_MIN || 8;
    const FONT_MAX = window.ChartConfig?.UI?.FONT_MAX || 24;

    // Global context menu handler for ticker chips
    document.addEventListener('click', () => {
        const menu = document.getElementById('chip-context-menu');
        if (menu) menu.classList.remove('visible');
    });

    document.addEventListener('DOMContentLoaded', () => {
        const menu = document.getElementById('chip-context-menu');
        if (menu) {
            menu.addEventListener('click', (e) => {
                const item = e.target.closest('.chip-context-menu-item');
                if (!item) return;

                const action = item.dataset.action;
                const chip = menu._targetChip;
                const ticker = menu._targetTicker;

                if (!chip || !ticker) return;

                if (action === 'axis-left' || action === 'axis-right') {
                    const newAxis = action === 'axis-left' ? 'left' : 'right';
                    chip._currentAxis = newAxis;
                    if (chip._axisIndicator) {
                        chip._axisIndicator.textContent = newAxis === 'left' ? 'L' : '';
                    }
                    if (typeof chip._onAxisChange === 'function') {
                        chip._onAxisChange(ticker, newAxis);
                    }
                } else if (action === 'hide') {
                    // Toggle hidden state via chip click
                    chip.click();
                }

                menu.classList.remove('visible');
            });
        }
    });

    // ═══════════════════════════════════════════════════════════════════════
    // CARD TYPE REGISTRY
    // Extensible registry for special card types (dashboard, dendrograms, etc.)
    // ═══════════════════════════════════════════════════════════════════════
    const CARD_TYPE_REGISTRY = {
        'dashboard': {
            module: () => window.ChartDashboard,
            create: (wrapper, opts) => window.ChartDashboard.createDashboardCard(wrapper),
            restore: (cardData, wrapper) => ({ type: 'dashboard', wrapperEl: wrapper })
        },
        'macro-dashboard': {
            module: () => window.ChartMacroDashboard,
            create: (wrapper, opts) => window.ChartMacroDashboard.createMacroDashboardCard(wrapper),
            restore: (cardData, wrapper) => ({ type: 'macro-dashboard', wrapperEl: wrapper })
        },
        'dendrograms': {
            module: () => window.ChartDendrograms,
            create: (wrapper, opts) => window.ChartDendrograms.createDendrogramCard(wrapper),
            restore: (cardData, wrapper) => ({ type: 'dendrograms', wrapperEl: wrapper })
        },
        'thesis-performance': {
            module: () => window.ChartThesisPerformance,
            create: (wrapper, opts) => window.ChartThesisPerformance.createThesisPerformanceCard(wrapper, { thesisId: opts.thesisId }),
            restore: (cardData, wrapper) => ({ type: 'thesis-performance', wrapperEl: wrapper, thesisId: cardData.thesisId })
        }
    };

    /**
     * Restore a card from saved data
     * @param {Object} cardData - Saved card configuration
     */
    function restoreCard(cardData) {
        const wrapper = window.PageManager ? window.PageManager.ensurePage(cardData.page || '1') : null;

        // Check type registry for special card types
        const typeHandler = CARD_TYPE_REGISTRY[cardData.type];
        if (typeHandler) {
            console.log(`[Restore] Creating ${cardData.type} card on page`, cardData.page);
            createChartCard(typeHandler.restore(cardData, wrapper));
            return;
        }

        createChartCard({
            tickers: Array.isArray(cardData.tickers) ? cardData.tickers.join(', ') : (cardData.tickers || ''),
            showDiff: !!cardData.showDiff,
            showAvg: !!cardData.showAvg,
            showVol: !!cardData.showVol,
            showVolume: !!cardData.showVolume,
            showRevenue: !!cardData.showRevenue,
            useRaw: cardData.useRaw || false,
            useLogScale: cardData.useLogScale || false,
            multipliers: cardData.multipliers || {},
            tickerColors: cardData.tickerColors || {},
            priceScaleAssignments: cardData.priceScaleAssignments || {},
            hidden: cardData.hidden || [],
            range: cardData.range || null,
            title: cardData.title || '',
            lastLabelVisible: cardData.lastLabelVisible ?? true,
            lastTickerVisible: !!cardData.lastTickerVisible,
            showZeroLine: cardData.showZeroLine || false,
            wrapperEl: wrapper,
            height: cardData.height || (window.ChartConfig?.DIMENSIONS?.CHART_MIN_HEIGHT || 400),
            fontSize: cardData.fontSize || (window.ChartConfig?.UI?.FONT_DEFAULT || 12),
            showFixedLegend: !!cardData.showFixedLegend,
            fixedLegendPos: cardData.fixedLegendPos || { x: 10, y: 10 },
            fixedLegendSize: cardData.fixedLegendSize || null,
            showNotes: !!cardData.showNotes,
            notes: cardData.notes || '',
            manualInterval: cardData.manualInterval || null,
            decimalPrecision: cardData.decimalPrecision || 2,
            settingsPanelOpen: !!cardData.settingsPanelOpen,
            starred: !!cardData.starred
        });
    }

    // Company name fetching
    // Fetch company names for tickers; optionally pass in chipNodes to avoid global DOM scan
    async function ensureNames(tickers, chipNodes = null) {
        const missing = tickers.filter(t => !(t in nameCache));
        // Fetch aliases in parallel with metadata (uses shared ChartUtils cache)
        const aliasPromise = window.ChartUtils.getAliases();

        if (missing.length) {
            try {
                const metadata = await window.DataFetcher.getMetadata(missing);
                Object.assign(nameCache, metadata);
            } catch (error) {
                console.error('Failed to fetch metadata:', error);
            }
        }

        // Wait for aliases before updating tooltips
        const aliases = await aliasPromise;

        // Update chip tooltips with company name + alias hint
        const chips = chipNodes ? Array.from(chipNodes) : document.querySelectorAll('.chip');
        chips.forEach(ch => {
            const t = ch.dataset.ticker;
            let tooltip = nameCache[t] || '';
            // Add alias hint if this ticker is aliased
            if (aliases[t]) {
                const hint = `${t} → ${aliases[t]} (fundamentals)`;
                tooltip = tooltip ? `${tooltip}\n${hint}` : hint;
            }
            if (tooltip) ch.title = tooltip;
        });
    }

    // Save all chart states
    function saveCards() {
        const cards = Array.from(document.querySelectorAll('.chart-card')).map(card => ({
            page: card.closest('.page')?.dataset.page || '1',
            type: card._type || null,
            thesisId: card._thesisId || null,
            tickers: Array.from(card._selectedTickers || []),
            showDiff: !!card._showDiff,
            showAvg: !!card._showAvg,
            showVol: !!card._showVol,
            showVolume: !!card._showVolume,
            showRevenue: !!card._showRevenue,
            showFundamentalsPane: !!card._showFundamentalsPane,
            fundamentalsMetrics: card._fundamentalsMetrics || ['revenue', 'netincome'],
            multipliers: window.ChartUtils.mapToObject(card._multiplierMap),
            hidden: Array.from(card._hiddenTickers || []),
            range: card._visibleRange || null,
            useRaw: card._useRaw || false,
            useLogScale: card._useLogScale || false,
            title: card._title || '',
            lastLabelVisible: card._lastLabelVisible !== false,
            lastTickerVisible: !!card._lastTickerVisible,
            showZeroLine: !!card._showZeroLine,
            showFixedLegend: !!card._showFixedLegend,
            showLegendTickers: !!card._showLegendTickers,
            fixedLegendPos: card._fixedLegendPos || { x: 10, y: 10 },
            fixedLegendSize: card._fixedLegendSize || null,
            height: card._height || (() => { try { const el = card.querySelector('.chart-box'); return el ? parseInt(getComputedStyle(el).height, 10) : undefined; } catch (_) { return undefined; } })(),
            fontSize: card._fontSize || (window.ChartConfig?.UI?.FONT_DEFAULT || 12),
            showNotes: !!card._showNotes,
            notes: card._notes || '',
            manualInterval: card._manualInterval || null,
            decimalPrecision: card._decimalPrecision || 2,
            tickerColors: window.ChartUtils.mapToObject(card._tickerColorMap),
            priceScaleAssignments: window.ChartUtils.mapToObject(card._priceScaleAssignmentMap),
            settingsPanelOpen: !!card._state?.settingsPanelOpen,
            starred: !!card._starred,
            tags: card._tags || []
        }));

        window.ChartUtils.safeSetJSON(window.ChartConfig.STORAGE_KEYS.CARDS, cards);
        if (window.StateManager && typeof window.StateManager.saveCards === 'function') {
            window.StateManager.saveCards(cards);
        }
    }
    window.saveCards = saveCards;
    // Global tag management
    window._allTags = new Set();

    function getAllTags() {
        const tags = new Set();
        document.querySelectorAll('.chart-card').forEach(card => {
            (card._tags || []).forEach(tag => tags.add(tag));
        });
        window._allTags = tags;
        return Array.from(tags).sort();
    }

    function updateTagFilterDropdown() {
        const select = document.getElementById('tag-filter-select');
        if (!select) return;
        const currentValue = select.value;
        const tags = getAllTags();
        select.innerHTML = '<option value="">All</option>' +
            tags.map(t => `<option value="${t}"${t === currentValue ? ' selected' : ''}>${t}</option>`).join('');
    }

    function applyTagFilter() {
        const select = document.getElementById('tag-filter-select');
        if (!select) return;
        const filterTag = select.value;
        const highlightsMode = window.highlightsMode || false;

        document.querySelectorAll('.chart-card').forEach(card => {
            const page = card.closest('.page');
            const isActivePage = page && page.classList.contains('active');
            const hasTag = !filterTag || (card._tags || []).includes(filterTag);
            const isStarred = !highlightsMode || card._starred;

            if (isActivePage && hasTag && isStarred) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Initialize tag filter
    document.addEventListener('DOMContentLoaded', () => {
        const select = document.getElementById('tag-filter-select');
        if (select) {
            select.addEventListener('change', applyTagFilter);
        }
        // Update tag filter after cards are loaded (delayed to ensure cards exist)
        setTimeout(() => {
            if (window.updateTagFilterDropdown) window.updateTagFilterDropdown();
        }, 1000);
    });

    window.updateTagFilterDropdown = updateTagFilterDropdown;
    window.applyTagFilter = applyTagFilter;
    window.getAllTags = getAllTags;



    /**
     * Create a chart card with the given options
     * @param {Object} options - Options object with card configuration
     * @returns {HTMLElement} The created card element
     */
    function createChartCard(options = {}) {
        // Check type registry for special card types
        if (options.type && CARD_TYPE_REGISTRY[options.type]) {
            const typeHandler = CARD_TYPE_REGISTRY[options.type];
            const wrapper = options.wrapperEl || document.getElementById(WRAPPER_ID);
            const module = typeHandler.module();

            if (wrapper && module) {
                console.log(`[createChartCard] ${options.type} type detected`);
                return typeHandler.create(wrapper, options);
            }
            console.error(`${options.type} module not loaded`);
            return null;
        }

        // Handle array shorthand: createChartCard(['SPY', 'QQQ'])
        if (Array.isArray(options)) {
            options = { tickers: options.join(', ') };
        }

        // Handle string shorthand: createChartCard('SPY') - this is fine
        // Only warn once if multiple positional args were passed (deprecated pattern)
        if (typeof options === 'string') {
            if (arguments.length > 1 && !createChartCard._warnedPositional) {
                createChartCard._warnedPositional = true;
                console.warn('[createChartCard] Positional arguments are deprecated. Use options object instead.');
            }
            options = { tickers: options };
        }

        // Normalize options.tickers: accept array or string
        if (Array.isArray(options.tickers)) {
            options.tickers = options.tickers.join(', ');
        }

        // Destructure with defaults
        const {
            tickers: initialTickers = 'SPY',
            showDiff: initialShowDiff = false,
            showAvg: initialShowAvg = false,
            showVol: initialShowVol = false,
            showVolume: initialShowVolume = false,
            showRevenue: initialShowRevenue = false,
            showFundamentalsPane: initialShowFundamentalsPane = false,
            fundamentalsMetrics: initialFundamentalsMetrics = ['revenue', 'netincome'],
            useRaw: initialUseRaw = false,
            useLogScale: initialUseLogScale = false,
            multipliers: initialMultipliers = {},
            tickerColors: initialTickerColors = {},
            priceScaleAssignments: initialPriceScaleAssignments = {},
            hidden: initialHidden = [],
            range: initialRange = null,
            title: initialTitle = '',
            lastLabelVisible: initialLastLabelVisible = true,
            lastTickerVisible: initialLastTickerVisible = false,
            showZeroLine: initialShowZeroLine = false,
            wrapperEl = null,
            height: initialHeight = (window.ChartConfig?.DIMENSIONS?.CHART_MIN_HEIGHT || 400),
            fontSize: initialFontSize = (window.ChartConfig?.UI?.FONT_DEFAULT || 12),
            showFixedLegend: initialShowFixedLegend = false,
            showLegendTickers: initialShowLegendTickers = false,
            fixedLegendPos: initialFixedLegendPos = { x: 10, y: 10 },
            fixedLegendSize: initialFixedLegendSize = null,
            showNotes: initialShowNotes = false,
            notes: initialNotes = '',
            manualInterval: initialManualInterval = null,
            decimalPrecision: initialDecimalPrecision = 2,
            volumePaneStretchFactor: initialVolumePaneStretchFactor = 1.0,
            revenuePaneStretchFactor: initialRevenuePaneStretchFactor = 1.0,
            fundamentalsPaneStretchFactor: initialFundamentalsPaneStretchFactor = 1.0,
            starred: initialStarred = false,
            tags: initialTags = []
        } = options;
        const wrapper = wrapperEl || document.getElementById(WRAPPER_ID);
        if (!wrapper) {
            console.error('Missing charts wrapper');
            return;
        }

        // Determine which page this card is on
        const pageEl = wrapper.closest('.page');
        const targetPage = pageEl ? pageEl.dataset.page : '1';

        // Create card DOM
        globalCardCounter += 1;
        const cardId = `chart-${globalCardCounter}`;
        const card = window.ChartDomBuilder.createChartCard(cardId, initialTitle, initialHeight);
        wrapper.appendChild(card);
        // --- navigation link ---
        const nav = document.getElementById('chart-nav');
        let navLabel = initialTitle || '';
        if (!navLabel) {
            const firstTicker = initialTickers && typeof initialTickers === 'string'
                ? initialTickers.split(/[,\s]+/).filter(Boolean)[0]
                : '';
            navLabel = firstTicker || `Card ${globalCardCounter}`;
        }
        let navLink = null;
        if (nav) {
            navLink = document.createElement('a');
            navLink.href = `#${cardId}`;
            navLink.textContent = navLabel;
            navLink.dataset.page = targetPage;

            // Add click handler to switch pages and scroll to chart
            navLink.addEventListener('click', (e) => {
                e.preventDefault();

                // Find which page contains this card
                const targetCard = document.getElementById(cardId);
                if (!targetCard) {
                    console.warn(`[Navigation] Card ${cardId} not found`);
                    return;
                }

                // Find the page that contains this card
                const pageEl = targetCard.closest('.page');
                if (!pageEl) {
                    console.warn(`[Navigation] No page found for card ${cardId}`);
                    return;
                }

                const pageNum = pageEl.dataset.page;
                console.log(`[Navigation] Switching to page ${pageNum} for card ${cardId}`);

                // Switch to the correct page
                if (window.PageManager && window.PageManager.showPage) {
                    window.PageManager.showPage(parseInt(pageNum, 10));
                }

                // Scroll to the chart after a brief delay to ensure page switch completes
                setTimeout(() => {
                    targetCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }, 100);
            });

            nav.appendChild(navLink);
        }
        card._navLink = navLink;

        // Get DOM elements
        const elements = window.ChartDomBuilder.getCardElements(card);
        const { tickerInput, addBtn, plotBtn, fitBtn, toggleDiffBtn, toggleVolBtn, toggleVolumeBtn, toggleRevenueBtn, toggleFundamentalsPaneBtn, toggleRevenueMetricBtn, toggleNetIncomeMetricBtn, toggleEpsMetricBtn, toggleFcfMetricBtn, toggleRawBtn,
            toggleAvgBtn, toggleLastLabelBtn, toggleLastTickerBtn, reshuffleColorsBtn, toggleZeroLineBtn, toggleFixedLegendBtn, toggleLegendTickersBtn, toggleNotesBtn, starBtn, heightSlider, heightValue, volPaneHeightSlider, volPaneHeightValue, fontSlider, fontValue, decimalsSlider, decimalsValue, exportBtn, rangeSelect, intervalSelect, selectedTickersDiv, chartBox, titleInput, removeCardBtn, addChartBtn, notesSection, notesTextarea } = elements;

        // ═══════════════════════════════════════════════════════════════
        // CONTEXT INITIALIZATION (State Object Pattern)
        // ═══════════════════════════════════════════════════════════════
        const ctx = window.ChartCardContext.create(card, elements, {
            initialTickers,
            initialShowDiff,
            initialShowAvg,
            initialShowVol,
            initialShowVolume,
            initialShowRevenue,
            initialShowFundamentalsPane,
            initialFundamentalsMetrics,
            initialUseRaw,
            initialMultipliers,
            initialTickerColors,
            initialPriceScaleAssignments,
            initialHidden,
            initialRange,
            initialTitle,
            initialLastLabelVisible,
            initialLastTickerVisible,
            initialShowZeroLine,
            initialShowFixedLegend,
            initialShowLegendTickers,
            initialFixedLegendPos,
            initialFixedLegendSize,
            initialHeight,
            initialFontSize,
            initialShowNotes,
            initialNotes,
            initialManualInterval,
            initialDecimalPrecision,
            initialVolumePaneStretchFactor,
            initialRevenuePaneStretchFactor,
            initialFundamentalsPaneStretchFactor,
            cardId,
            targetPage,
            saveCards
        });
        card._ctx = ctx;
        // Initial sync to card._ for persistence (ctx already has starred/tags from options)
        window.ChartCardContext.syncToCard(ctx);

        // ═══════════════════════════════════════════════════════════════
        // All toggle/display state now lives in ctx.* (via ChartCardContext)
        // ═══════════════════════════════════════════════════════════════

        // Chart instances (will be set on ctx after creation)
        let chart = null;
        let volPane = null;
        let volumePane = null;
        let revenuePane = null;
        let fundamentalsPane = null;
        let avgSeries = null;
        let tickerLabelsContainer = null;
        let zeroLineSeries = null;
        let fixedLegendEl = null;
        let diffChart = null;

        // Event handlers
        let crosshairHandler = null;
        let debouncedRebase = null;
        let rangeSaveHandler = null;
        let tickerLabelHandler = null;
        let fixedLegendCrosshairHandler = null;
        let skipRangeApplication = false;
        let plotAbortController = null;  // For cancelling in-flight fetches on rapid replot/remove

        // Debounced save (reference ctx version)
        const debouncedSaveCards = ctx.debouncedSaveCards;

        // ═══════════════════════════════════════════════════════════════
        // COLLECTION REFERENCES (shared with context - auto-sync!)
        // ═══════════════════════════════════════════════════════════════
        const selectedTickers = ctx.selectedTickers;
        const hiddenTickers = ctx.hiddenTickers;
        const multiplierMap = ctx.multiplierMap;
        const tickerColorMap = ctx.tickerColorMap;
        const priceScaleAssignmentMap = ctx.priceScaleAssignmentMap;

        // Runtime-only state (not persisted, recreated on each card init)
        const priceSeriesMap = new Map();
        const volSeriesMap = new Map();
        const volumeSeriesMap = new Map();
        const revenueSeriesMap = new Map();
        const fundamentalSeriesMap = new Map();
        const rawPriceMap = new Map();
        const latestRebasedData = {};

        // ═══════════════════════════════════════════════════════════════
        // SYNC STATE TO CARD ELEMENT (for persistence via saveCards)
        // ═══════════════════════════════════════════════════════════════
        window.ChartCardContext.syncToCard(ctx);

        // Helper to persist partial state updates to ctx and card
        function persistState(partial) {
            Object.assign(ctx, partial);
            window.ChartCardContext.syncToCard(ctx);
            saveCards();
        }

        // Initialize notes UI
        if (notesSection && notesTextarea) {
            notesSection.style.display = initialShowNotes ? 'block' : 'none';
            notesTextarea.value = initialNotes;
        }

        // Helper to get current button states for updateButtonStates()
        function getButtonStates() {
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
                showLegendTickers: ctx.showLegendTickers
            };
        }

        // Get current font size with fallback
        function getCurrentFontSize() {
            return ctx.fontSize || window.ChartConfig.UI.FONT_DEFAULT || 12;
        }

        // Compute min/max time across currently visible tickers with loaded data
        function getCurrentDataRange() {
            let minT = Infinity;
            let maxT = -Infinity;
            let has = false;
            selectedTickers.forEach(t => {
                if (hiddenTickers.has(t)) return;
                const arr = rawPriceMap.get(t);
                if (!arr || !arr.length) return;
                has = true;
                // raw data is sorted ASC by time
                minT = Math.min(minT, arr[0].time);
                maxT = Math.max(maxT, arr[arr.length - 1].time);
            });
            return has ? { from: minT, to: maxT } : null;
        }

        /**
         * Destroy chart instance and cleanup all subscriptions/series/panes.
         * Shared by destroyChartAndReplot() and handleRemoveCard().
         */
        function destroyChart() {
            // Abort any in-flight fetches
            if (plotAbortController) {
                plotAbortController.abort();
                plotAbortController = null;
            }

            if (!chart) return;

            // Unsubscribe all handlers
            try {
                if (crosshairHandler && chart.unsubscribeCrosshairMove) {
                    chart.unsubscribeCrosshairMove(crosshairHandler);
                }
            } catch (_) { }
            try {
                if (fixedLegendCrosshairHandler && chart.unsubscribeCrosshairMove) {
                    chart.unsubscribeCrosshairMove(fixedLegendCrosshairHandler);
                }
            } catch (_) { }
            try {
                if (debouncedRebase && chart.timeScale && typeof chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                    chart.timeScale().unsubscribeVisibleTimeRangeChange(debouncedRebase);
                    if (typeof debouncedRebase.cancel === 'function') debouncedRebase.cancel();
                }
            } catch (_) { }
            try {
                if (rangeSaveHandler && chart.timeScale && typeof chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                    chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                }
            } catch (_) { }
            try {
                if (tickerLabelHandler && chart.timeScale && typeof chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                    chart.timeScale().unsubscribeVisibleTimeRangeChange(tickerLabelHandler);
                }
            } catch (_) { }

            // Remove chart instance
            try {
                chart.remove();
            } catch (_) { }

            // Clear references
            chart = null;
            volPane = null;
            volumePane = null;
            revenuePane = null;
            fundamentalsPane = null;
            fixedLegendCrosshairHandler = null;
            avgSeries = null;
            zeroLineSeries = null;

            // Clear series maps
            priceSeriesMap.clear();
            volSeriesMap.clear();
            volumeSeriesMap.clear();
            revenueSeriesMap.clear();
            fundamentalSeriesMap.clear();

            // Cleanup fixed legend (ResizeObserver + document listeners + DOM)
            if (fixedLegendEl) {
                if (typeof fixedLegendEl._cleanup === 'function') {
                    fixedLegendEl._cleanup();
                }
                fixedLegendEl.remove();
                fixedLegendEl = null;
            }

            // Remove overlay DOM elements to prevent duplicates on replot
            if (chartBox) {
                const tickerLabels = chartBox.querySelector('.ticker-labels-container');
                if (tickerLabels) tickerLabels.remove();
                const floatingLegend = chartBox.querySelector('.floating-legend');
                if (floatingLegend) floatingLegend.remove();
            }
        }

        /**
         * Save visible range, destroy chart, clear all panes/series, and replot.
         * Used by pane toggle handlers to ensure clean chart recreation.
         */
        function destroyChartAndReplot() {
            // Save current visible range
            if (chart && chart.timeScale) {
                try {
                    const visible = chart.timeScale().getVisibleRange();
                    if (visible && visible.from && visible.to) {
                        ctx.visibleRange = { from: Math.round(visible.from), to: Math.round(visible.to) };
                        window.ChartCardContext.syncToCard(ctx);
                    }
                } catch (_) { }
            }

            destroyChart();

            // Skip automatic range application and replot
            skipRangeApplication = true;
            saveCards();
            plot();
        }

        function applyResize(baseH) {
            if (!chartBox) return;
            // Calculate total height: base + active panes
            let paneCount = 0;
            if (ctx.showVolumePane) paneCount++;
            if (ctx.showRevenuePane) paneCount++;
            if (ctx.showFundamentalsPane) paneCount++;
            if (ctx.showVolPane) paneCount++; // Volatility pane
            const totalH = baseH + (paneCount * PANE_HEIGHT);
            chartBox.style.height = `${totalH}px`;
            if (chart && typeof chart.resize === 'function') {
                const width = chartBox.clientWidth || chartBox.getBoundingClientRect().width || 800;
                console.log(`[Card:${cardId}] Resizing chart to ${width} x ${totalH} (base: ${baseH}, panes: ${paneCount})`);
                try { chart.resize(width, totalH); } catch (e) { console.warn(`[Card:${cardId}] chart.resize failed`, e); }
            }
        }

        function setHeight(newHeight) {
            const height = window.ChartUtils.clamp(parseInt(newHeight), HEIGHT_MIN, HEIGHT_MAX);
            console.log(`[Card:${cardId}] Height change to ${height}`);
            ctx.height = height;
            window.ChartCardContext.syncToCard(ctx);
            applyResize(height);
            // Update slider and display
            if (heightSlider) heightSlider.value = height;
            if (heightValue) heightValue.textContent = height;
            saveCards();
        }
        // Height slider event handler
        window.ChartUtils.bindSliderControl(heightSlider, heightValue, {
            initialValue: ctx.height || initialHeight,
            onInput: (v) => { ctx.height = v; window.ChartCardContext.syncToCard(ctx); applyResize(v); }
        });

        // Volume pane height adjustment
        function setVolumePaneHeight(newFactor) {
            const factor = window.ChartUtils.clamp(parseFloat(newFactor), 0.5, 3.0);
            console.log(`[Card:${cardId}] Volume pane stretch factor change to ${factor}`);
            ctx.volumePaneStretchFactor = factor;
            window.ChartCardContext.syncToCard(ctx);

            // Apply to existing volume pane if it exists
            if (volumePane && typeof volumePane.setStretchFactor === 'function') {
                volumePane.setStretchFactor(factor);
                console.log(`[Card:${cardId}] Applied stretch factor ${factor} to volume pane`);
            }

            // Update slider and display
            if (volPaneHeightSlider) volPaneHeightSlider.value = factor;
            if (volPaneHeightValue) volPaneHeightValue.textContent = factor.toFixed(1);
            saveCards();
        }
        // Volume pane height slider event handler
        window.ChartUtils.bindSliderControl(volPaneHeightSlider, volPaneHeightValue, {
            initialValue: ctx.volumePaneStretchFactor,
            onInput: (v) => {
                ctx.volumePaneStretchFactor = v;
                if (volumePane && typeof volumePane.setStretchFactor === 'function') {
                    volumePane.setStretchFactor(v);
                }
            },
            formatDisplay: (v) => v.toFixed(1)
        });

        function applyFont(newSize) {
            if (chart && typeof chart.applyOptions === 'function') {
                console.log(`[Card:${cardId}] Applying axis font size ${newSize}`);
                try { chart.applyOptions({ layout: { fontSize: newSize } }); } catch (e) { console.warn(`[Card:${cardId}] chart.applyOptions(layout.fontSize) failed`, e); }
            }
            // Update ticker labels font size
            if (tickerLabelsContainer) {
                window.ChartTickerLabels.updateFontSize(tickerLabelsContainer, newSize);
            }
        }
        function setFontSize(newSize) {
            const size = window.ChartUtils.clamp(parseInt(newSize), FONT_MIN, FONT_MAX);
            console.log(`[Card:${cardId}] Font size change to ${size}`);
            ctx.fontSize = size;
            window.ChartCardContext.syncToCard(ctx);
            applyFont(size);
            // Update slider and display
            if (fontSlider) fontSlider.value = size;
            if (fontValue) fontValue.textContent = size;
            saveCards();
        }
        // Font slider event handler
        window.ChartUtils.bindSliderControl(fontSlider, fontValue, {
            initialValue: ctx.fontSize || (window.ChartConfig?.UI?.FONT_DEFAULT || 12),
            onInput: (v) => { ctx.fontSize = v; window.ChartCardContext.syncToCard(ctx); applyFont(v); }
        });

        // Decimals slider event handler
        function updatePriceFormat(precision) {
            if (chart && chart.priceScale) {
                const priceFormat = window.ChartUtils.createPriceFormatter(ctx.useRaw, precision);

                try {
                    chart.priceScale('right').applyOptions({ priceFormat });
                    console.log(`[Card:${cardId}] Updated price format precision to ${precision}`);
                } catch (e) {
                    console.warn('[Card] Could not update price scale format:', e);
                }
            }
        }

        // Decimals slider
        window.ChartUtils.bindSliderControl(decimalsSlider, decimalsValue, {
            initialValue: ctx.decimalPrecision !== undefined ? ctx.decimalPrecision : 2,
            onInput: (v) => { ctx.decimalPrecision = v; window.ChartCardContext.syncToCard(ctx); updatePriceFormat(v); }
        });

        // Update button states
        window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());

        // Remove ticker handler: updates state and removes corresponding series
        function handleChipRemove(ticker, chipEl) {
            try {
                if (!selectedTickers.has(ticker)) {
                    if (chipEl && chipEl.parentElement) chipEl.parentElement.removeChild(chipEl);
                    return;
                }
                selectedTickers.delete(ticker);
                hiddenTickers.delete(ticker);
                multiplierMap.delete(ticker);
                tickerColorMap.delete(ticker);
                rawPriceMap.delete(ticker);
                try { delete latestRebasedData[ticker]; } catch (_) { }

                // Remove price series
                const s = priceSeriesMap.get(ticker);
                if (s && chart) {
                    try { chart.removeSeries(s); } catch (_) { }
                }
                priceSeriesMap.delete(ticker);

                // Remove volume series (if present)
                if (volSeriesMap && chart) {
                    const vs = volSeriesMap.get(ticker);
                    if (vs) {
                        try { chart.removeSeries(vs); } catch (_) { }
                        volSeriesMap.delete(ticker);
                    }
                    // If no volume series remain, remove the pane
                    if (volPane && volSeriesMap.size === 0) {
                        try { volPane = window.ChartVolumeManager.clearVolumeSeries(chart, volPane, volSeriesMap); } catch (_) { }
                    }
                }

                // Update average series
                if (ctx.showAvg && !ctx.useRaw) {
                    try {
                        avgSeries = window.ChartSeriesManager.updateAverageSeries(
                            chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, ctx.lastLabelVisible
                        );
                    } catch (_) { }
                }

                // Remove ticker label
                if (tickerLabelsContainer) {
                    window.ChartTickerLabels.removeLabel(tickerLabelsContainer, ticker);
                }

                // Remove chip element
                if (chipEl && chipEl.parentElement) chipEl.parentElement.removeChild(chipEl);

                // Update nav label if title empty
                if (navLink && titleInput && !titleInput.value) {
                    navLink.textContent = titleInput.value || (selectedTickers.size ? Array.from(selectedTickers)[0] : cardId);
                }

                saveCards();
            } catch (e) {
                console.warn('[Card] handleChipRemove failed:', e);
            }
        }

        // Initialize tickers
        if (initialTickers) {
            const tickers = window.ChartDomBuilder.parseTickerInput(initialTickers);
            tickers.forEach(t => {
                selectedTickers.add(t);
            });
            // Assign consistent hash-based colors
            selectedTickers.forEach(ticker => {
                if (!tickerColorMap.has(ticker)) {
                    tickerColorMap.set(ticker, window.ChartConfig.getTickerColor(ticker));
                }
            });
            window.ChartDomBuilder.addTickerChips(
                selectedTickersDiv, selectedTickers, tickerColorMap, multiplierMap, hiddenTickers, handleChipRemove
            );
        }

        // Add ticker function
        const addTicker = () => {
            const input = window.ChartDomBuilder.normalizeTicker(tickerInput.value);
            if (!input || selectedTickers.has(input)) return;

            selectedTickers.add(input);

            // Assign hash-based color for new ticker
            if (!tickerColorMap.has(input)) {
                tickerColorMap.set(input, window.ChartConfig.getTickerColor(input));
            }

            window.ChartDomBuilder.addTickerChips(
                selectedTickersDiv, selectedTickers, tickerColorMap, multiplierMap, hiddenTickers, handleChipRemove
            );

            tickerInput.value = '';
            saveCards();
        };

        /**
         * Execute pane operations while preserving visible range
         * Wraps pane-specific logic with range save/restore and subscription management
         * @param {string} paneName - Name for logging (e.g., 'volume', 'revenue')
         * @param {Function} operation - Async function to execute
         */
        async function withRangePreservation(paneName, operation) {
            const rangeBefore = ctx.visibleRange;
            if (rangeBefore) {
                console.log(`[Plot] Using saved range for ${paneName} ops: from ${rangeBefore.from}, to ${rangeBefore.to}`);
            }

            // Temporarily unsubscribe from range changes
            if (rangeSaveHandler) {
                try {
                    chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                } catch (_) { }
            }

            // Execute pane-specific operation
            await operation();

            // Final range restoration
            if (rangeBefore && !ctx.skipRangeRestoration) {
                try {
                    chart.timeScale().setVisibleRange(rangeBefore);
                    console.log(`[Plot] Final range restoration after ${paneName} operations`);
                } catch (_) { }
            } else if (ctx.skipRangeRestoration) {
                console.log(`[Plot] Skipping ${paneName} range restoration (manual range was set)`);
                if (paneName === 'fundamentals') {
                    ctx.skipRangeRestoration = false;  // Reset flag after last pane
                }
            }

            // Resubscribe to range changes
            if (rangeSaveHandler) {
                try {
                    chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);
                } catch (_) { }
            }
        }

        // Main plot function
        async function plot() {
            // Cancel any in-flight fetches from previous plot
            if (plotAbortController) {
                plotAbortController.abort();
            }
            plotAbortController = new AbortController();
            const plotSignal = plotAbortController.signal;

            if (!chart) {
                // Set price format based on mode and decimal precision
                const precision = ctx.decimalPrecision !== undefined ? ctx.decimalPrecision : 2;
                const priceFormat = window.ChartUtils.createPriceFormatter(ctx.useRaw, precision);

                chart = LightweightCharts.createChart(chartBox, {
                    layout: { background: { type: 'solid', color: '#ffffff' }, textColor: '#333', fontSize: (ctx.fontSize || (window.ChartConfig?.UI?.FONT_DEFAULT || 12)) },
                    grid: { vertLines: { color: '#eee' }, horzLines: { color: '#eee' } },
                    timeScale: { secondsVisible: false, rightOffset: 3, fixLeftEdge: true },
                    leftPriceScale: {
                        visible: true,
                        mode: LightweightCharts.PriceScaleMode.Logarithmic,
                        scaleMargins: { top: 0.1, bottom: 0.1 },
                        priceFormat
                    },
                    rightPriceScale: {
                        visible: true,
                        mode: LightweightCharts.PriceScaleMode.Logarithmic,
                        scaleMargins: { top: 0.1, bottom: 0.1 },
                        priceFormat
                    },
                    crosshair: {
                        horzLine: { visible: false, labelVisible: false },
                        vertLine: { visible: true, labelVisible: true }
                    }
                });

                // Create ticker labels container
                tickerLabelsContainer = window.ChartTickerLabels.createLabelsContainer(chartBox);

                // Ensure initial size reflects stored height
                applyResize(ctx.height || initialHeight);

                // Apply rightOffset dynamically (in case chart already exists)
                chart.applyOptions({
                    timeScale: { rightOffset: 3 }
                });

                // Add legend
                const legendEl = window.ChartLegend.createLegendElement(chartBox);
                crosshairHandler = window.ChartLegend.subscribeToCrosshair(chart, legendEl, {
                    useRaw: ctx.useRaw,
                    priceSeriesMap,
                    hiddenTickers,
                    tickerColorMap,
                    selectedTickers,
                    rawPriceMap,
                    latestRebasedData,
                    getName: (t) => nameCache[t]
                });

                // Subscribe to crosshair for fixed legend dual mode
                if (chart) {
                    fixedLegendCrosshairHandler = (param) => {
                        if (!ctx.showFixedLegend || !fixedLegendEl) return;

                        // If hovering, show crosshair values; otherwise show latest
                        if (param && param.point && param.time !== undefined) {
                            // Get current visible range
                            let visibleRange = null;
                            try {
                                visibleRange = chart.timeScale().getVisibleRange();
                            } catch (e) {
                                console.warn('[FixedLegend] Could not get visible range:', e);
                            }

                            const legendData = [];
                            const time = param.time !== undefined ?
                                (typeof param.time === 'string' ? Date.parse(param.time) / 1000 : param.time) : null;

                            selectedTickers.forEach(ticker => {
                                if (hiddenTickers.has(ticker)) return;

                                // Get data array
                                const dataArray = ctx.useRaw ? rawPriceMap.get(ticker) : latestRebasedData[ticker];
                                if (!dataArray) return;

                                // If we have a visible range, check if ticker has any data points in that range
                                if (visibleRange && visibleRange.from && visibleRange.to) {
                                    const hasVisibleData = dataArray.some(point =>
                                        point.time >= visibleRange.from && point.time <= visibleRange.to
                                    );
                                    if (!hasVisibleData) return; // Skip this ticker if it has no visible data
                                }

                                // Get value at crosshair time
                                const point = dataArray.find(p => p.time === time);
                                if (point && point.value != null) {
                                    legendData.push({
                                        ticker,
                                        value: point.value,
                                        color: tickerColorMap.get(ticker)
                                    });
                                }
                            });

                            if (legendData.length > 0) {
                                window.ChartFixedLegend.updateContent(fixedLegendEl, legendData, {
                                    useRaw: ctx.useRaw,
                                    hiddenTickers,
                                    tickerColorMap,
                                    getName: (t) => nameCache[t]
                                });
                            }
                        } else {
                            // Not hovering, show latest values
                            updateFixedLegend();
                        }
                    };
                    chart.subscribeCrosshairMove(fixedLegendCrosshairHandler);
                }
            }

            if (selectedTickers.size === 0) return;

            // Clear existing series first
            window.ChartSeriesManager.clearAllSeries(chart, priceSeriesMap, volSeriesMap, avgSeries);
            avgSeries = null;

            // Remove volume pane if hiding it (do this AFTER clearing series)
            if (!ctx.showVolPane && volPane) {
                try {
                    console.log('[Plot] Attempting to remove volume pane');
                    chart.removePane(volPane);
                    console.log('[Plot] Volume pane removed successfully');
                } catch (e) {
                    console.warn('[Plot] Could not remove volume pane:', e);
                }
                volPane = null;
                volSeriesMap.clear();
            }

            // Ensure company names
            // Pass chip nodes to avoid global DOM scan
            ensureNames(Array.from(selectedTickers), selectedTickersDiv.querySelectorAll('.chip'));

            // Fetch price data with auto-interval selection
            try {
                const tickerList = Array.from(selectedTickers);

                // Determine optimal interval: manual override takes precedence
                let interval = 'daily';
                if (ctx.manualInterval && ctx.manualInterval !== 'auto') {
                    interval = ctx.manualInterval;
                    console.log(`Using manual interval: ${interval}`);
                } else if (ctx.visibleRange) {
                    const rangeSeconds = ctx.visibleRange.to - ctx.visibleRange.from;
                    const rangeDays = rangeSeconds / (24 * 3600);

                    // Auto-select interval based on range:
                    // < 5 years (~1825 days): daily
                    // 5-10 years: weekly
                    // > 10 years: monthly
                    if (rangeDays > 3650) {  // > 10 years
                        interval = 'monthly';
                        console.log(`Auto-selected monthly interval for ${Math.floor(rangeDays / 365)} year range`);
                    } else if (rangeDays > 1825) {  // > 5 years
                        interval = 'weekly';
                        console.log(`Auto-selected weekly interval for ${Math.floor(rangeDays / 365)} year range`);
                    }
                }

                // UNIFIED DATA FETCH - handles all tickers the same way
                // Backend automatically detects if ticker is IV or price data
                console.log(`Fetching data for ${tickerList.length} tickers: ${tickerList.join(', ')} (interval: ${interval})`);
                const data = await window.DataFetcher.getData(tickerList, 5475, interval, { signal: plotSignal });

                // Check if aborted during fetch
                if (plotSignal.aborted) {
                    console.log('[plot] Aborted during data fetch');
                    return;
                }

                if (!data || Object.keys(data).length === 0) {
                    console.warn('No data received');
                    // Don't show toast here - getData() already showed error if it was API failure
                    // Empty response could be legitimate (ticker not found in DB)
                    return;
                }

                // Process each ticker - delegated to ChartSeriesManager
                window.ChartSeriesManager.setupPriceSeries(
                    chart, tickerList, data, priceSeriesMap, rawPriceMap, latestRebasedData,
                    {
                        hiddenTickers,
                        tickerColorMap,
                        multiplierMap,
                        priceScaleAssignmentMap,
                        useRaw: ctx.useRaw,
                        lastLabelVisible: ctx.lastLabelVisible,
                        decimalPrecision: ctx.decimalPrecision
                    }
                );

                // Volatility (σ) pane - delegated to ChartVolumeManager
                if (ctx.showVolPane) {
                    const result = await window.ChartVolumeManager.setupVolatilityPane(
                        chart, tickerList, volPane, volSeriesMap,
                        {
                            rawPriceMap,
                            tickerColorMap,
                            hiddenTickers,
                            visibleRange: ctx.visibleRange,
                            lastLabelVisible: ctx.lastLabelVisible
                        },
                        withRangePreservation,
                        VOL_WINDOW
                    );
                    volPane = result.volPane;
                }

                // Trading Volume pane - delegated to ChartVolumeManager
                if (ctx.showVolumePane) {
                    const result = await window.ChartVolumeManager.setupTradingVolumePane(
                        chart, tickerList, volumePane, volumeSeriesMap,
                        {
                            tickerColorMap,
                            hiddenTickers,
                            visibleRange: ctx.visibleRange,
                            lastLabelVisible: ctx.lastLabelVisible,
                            stretchFactor: ctx.volumePaneStretchFactor
                        },
                        withRangePreservation
                    );
                    volumePane = result.volumePane;
                }

                // Revenue pane - delegated to FundamentalsPane
                if (ctx.showRevenuePane && window.FundamentalsPane) {
                    const result = await window.FundamentalsPane.setupRevenuePane(
                        chart, tickerList, revenuePane, revenueSeriesMap,
                        {
                            tickerColorMap,
                            hiddenTickers,
                            visibleRange: ctx.visibleRange,
                            lastLabelVisible: ctx.lastLabelVisible,
                            stretchFactor: ctx.revenuePaneStretchFactor,
                            signal: plotSignal
                        },
                        withRangePreservation
                    );
                    revenuePane = result.revenuePane;
                }

                // Fundamentals pane - delegated to FundamentalsPane
                if (ctx.showFundamentalsPane && window.FundamentalsPane) {
                    const result = await window.FundamentalsPane.setupFundamentalsPane(
                        chart, tickerList, fundamentalsPane, fundamentalSeriesMap,
                        {
                            hiddenTickers,
                            visibleRange: ctx.visibleRange,
                            stretchFactor: ctx.fundamentalsPaneStretchFactor,
                            activeMetrics: ctx.fundamentalsMetrics,
                            signal: plotSignal
                        },
                        withRangePreservation
                    );
                    fundamentalsPane = result.fundamentalsPane;
                }

                // Average series
                if (ctx.showAvg && !ctx.useRaw) {
                    avgSeries = window.ChartSeriesManager.updateAverageSeries(
                        chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, ctx.lastLabelVisible
                    );
                }

                // Update ticker labels
                if (tickerLabelsContainer) {
                    const currentFontSize = getCurrentFontSize();
                    const tickerData = ctx.useRaw ? rawPriceMap : latestRebasedData;

                    // Initial update (only for raw mode or if rebased data exists)
                    if (ctx.useRaw || Object.keys(latestRebasedData).length > 0) {
                        window.ChartTickerLabels.updateAllLabels(
                            tickerLabelsContainer, priceSeriesMap, tickerColorMap, hiddenTickers,
                            tickerData, chart, ctx.lastTickerVisible, currentFontSize
                        );
                    }

                    // Subscribe to range changes to update label positions
                    // Unsubscribe from previous handler first
                    if (tickerLabelHandler) {
                        chart.timeScale().unsubscribeVisibleTimeRangeChange(tickerLabelHandler);
                    }

                    // In raw mode: update immediately (data doesn't change)
                    // In percentage mode: skip immediate update (rebasing callback will handle it)
                    tickerLabelHandler = () => {
                        if (ctx.useRaw && tickerLabelsContainer && chart) {
                            // Raw mode: just update positions with same data
                            setTimeout(() => {
                                const currentFontSize = getCurrentFontSize();
                                window.ChartTickerLabels.updateAllLabels(
                                    tickerLabelsContainer, priceSeriesMap, tickerColorMap, hiddenTickers,
                                    rawPriceMap, chart, ctx.lastTickerVisible, currentFontSize
                                );
                            }, 50);
                        }
                        // Percentage mode: labels will be updated by rebasing callback (500ms delay)
                    };
                    chart.timeScale().subscribeVisibleTimeRangeChange(tickerLabelHandler);
                }

                // Subscribe to save visible range changes (debounced)
                if (rangeSaveHandler) {
                    chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                }
                rangeSaveHandler = (visible) => {
                    if (visible && visible.from && visible.to) {
                        const from = Math.round(visible.from);
                        const to = Math.round(visible.to);
                        ctx.visibleRange = { from, to };
                        window.ChartCardContext.syncToCard(ctx);
                        console.log(`[RangeSave:${cardId}] Visible time range changed => from ${from}, to ${to}`);
                        debouncedSaveCards();
                        // Update fixed legend when range changes
                        if (ctx.showFixedLegend) {
                            updateFixedLegend();
                        }
                    }
                };
                chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);

                // Setup range-based rebasing
                if (!ctx.useRaw) {
                    // Debug: Log when setting up rebasing
                    const pageNum = card.closest('[data-page]')?.dataset?.page || '1';
                    const isVisible = card.closest('.page')?.classList?.contains('visible');
                    console.log(`[Rebasing Setup] Chart on page ${pageNum}, visible: ${isVisible}, tickers: ${Array.from(selectedTickers).join(',')}`);

                    // Clear any existing subscription before setting up new one
                    if (debouncedRebase) {
                        chart.timeScale().unsubscribeVisibleTimeRangeChange(debouncedRebase);
                        if (typeof debouncedRebase.cancel === 'function') debouncedRebase.cancel();
                    }

                    debouncedRebase = window.ChartSeriesManager.setupRangeBasedRebasing(chart, {
                        priceSeriesMap,
                        rawPriceMap,
                        multiplierMap,
                        latestRebasedData,
                        showAvg: ctx.showAvg,
                        updateAverageSeries: () => {
                            if (ctx.showAvg) {
                                avgSeries = window.ChartSeriesManager.updateAverageSeries(
                                    chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, ctx.lastLabelVisible
                                );
                            }
                        },
                        onRebaseComplete: () => {
                            // Update ticker labels after rebasing completes
                            if (tickerLabelsContainer) {
                                const currentFontSize = getCurrentFontSize();
                                window.ChartTickerLabels.updateAllLabels(
                                    tickerLabelsContainer, priceSeriesMap, tickerColorMap, hiddenTickers,
                                    latestRebasedData, chart, ctx.lastTickerVisible, currentFontSize
                                );
                            }
                        },
                        useRaw: () => ctx.useRaw  // Pass as function to get current value
                    });

                    // Force an initial rebase after a small delay if page is not visible
                    if (!isVisible) {
                        setTimeout(() => {
                            const visible = chart.timeScale().getVisibleRange();
                            if (visible && debouncedRebase) {
                                console.log(`[Rebasing] Forcing initial rebase for hidden chart on page ${pageNum}`);
                                debouncedRebase(visible);
                            }
                        }, 100);
                    }
                }

                // Apply saved or smart default visible range (unless skipped)
                if (!skipRangeApplication) {
                    const saved = ctx.visibleRange || initialRange;
                    const dataRange = getCurrentDataRange();
                    const minCoverage = (window.ChartConfig && window.ChartConfig.RANGE && typeof window.ChartConfig.RANGE.FIT_MIN_COVERAGE === 'number')
                        ? window.ChartConfig.RANGE.FIT_MIN_COVERAGE : 0;
                    const applyRange = (rng, reason = 'saved') => {
                        try {
                            chart.timeScale().setVisibleRange(rng);
                            console.log(`[RangeApply:${cardId}] Applied ${reason} range => from ${rng.from}, to ${rng.to}`);
                        } catch (e) {
                            chart.timeScale().fitContent();
                        }
                    };

                    if (saved && saved.from && saved.to) {
                        let shouldFit = false;
                        if (dataRange) {
                            const dataW = dataRange.to - dataRange.from;
                            const savedW = saved.to - saved.from;
                            if (dataW > 0 && savedW >= 0) {
                                const coverage = savedW / dataW;
                                if (coverage < minCoverage) {
                                    shouldFit = true;
                                }
                            }
                        }
                        if (shouldFit && dataRange) {
                            applyRange(dataRange, 'auto-fit');
                            ctx.visibleRange = dataRange;
                            window.ChartCardContext.syncToCard(ctx);
                            saveCards();
                        } else {
                            applyRange(saved, 'saved');
                        }
                    } else if (dataRange) {
                        applyRange(dataRange, 'data');
                        ctx.visibleRange = dataRange;
                        window.ChartCardContext.syncToCard(ctx);
                        saveCards();
                    } else {
                        chart.timeScale().fitContent();
                    }
                } else {
                    // Manual range application when skipping automatic logic
                    console.log(`[RangeApply:${cardId}] Skipping automatic range application`);
                    const saved = ctx.visibleRange;
                    if (saved && saved.from && saved.to) {
                        try {
                            chart.timeScale().setVisibleRange(saved);
                            console.log(`[RangeApply:${cardId}] Manually applied saved range => from ${saved.from}, to ${saved.to}`);
                        } catch (e) {
                            console.warn(`[RangeApply:${cardId}] Could not apply saved range:`, e);
                            chart.timeScale().fitContent();
                        }
                    }
                    skipRangeApplication = false;  // Reset flag
                }

                // Ensure rightOffset is applied
                if (chart && chart.applyOptions) {
                    chart.applyOptions({
                        timeScale: { rightOffset: 3 }
                    });
                }

            } catch (error) {
                console.error('Plot error:', error);
            } finally {
                // Update zero line if it's enabled
                setTimeout(() => updateZeroLine(), 100);

                // Restore/create fixed legend if it was enabled before
                setTimeout(() => {
                    if (ctx.showFixedLegend && !fixedLegendEl) {
                        console.log(`[Card:${cardId}] Restoring fixed legend after plot`);
                        fixedLegendEl = window.ChartFixedLegend.createFixedLegend(chartBox, {
                            initialX: ctx.fixedLegendPos?.x || 10,
                            initialY: ctx.fixedLegendPos?.y || 10,
                            initialWidth: ctx.fixedLegendSize?.width || null,
                            initialHeight: ctx.fixedLegendSize?.height || null
                        });

                        // Setup state change handler
                        fixedLegendEl._onStateChange = (changes) => {
                            if (changes.x !== undefined || changes.y !== undefined) {
                                ctx.fixedLegendPos = {
                                    x: changes.x !== undefined ? changes.x : ctx.fixedLegendPos?.x || 10,
                                    y: changes.y !== undefined ? changes.y : ctx.fixedLegendPos?.y || 10
                                };
                            }
                            if (changes.width !== undefined || changes.height !== undefined) {
                                ctx.fixedLegendSize = {
                                    width: changes.width !== undefined ? changes.width : ctx.fixedLegendSize?.width || null,
                                    height: changes.height !== undefined ? changes.height : ctx.fixedLegendSize?.height || null
                                };
                            }
                            window.ChartCardContext.syncToCard(ctx);
                            debouncedSaveCards();
                        };

                        // Show it
                        window.ChartFixedLegend.show(fixedLegendEl);
                    }

                    // Update fixed legend if it's enabled
                    updateFixedLegend();
                }, 100);
            }
        }

        // Phase 1: Simple toggle handlers using dictionary pattern
        // NOTE: These are now bound via bindAllWithCleanup at the end of createChartCard
        const toggleHandlers = {
            diff: () => {
                persistState({ showDiff: !ctx.showDiff });
                toggleDiffBtn.textContent = ctx.showDiff ? 'Hide Diff Pane' : 'Show Diff Pane';
            },
            vol: () => {
                ctx.showVolPane = !ctx.showVolPane;
                window.ChartCardContext.syncToCard(ctx);
                toggleVolBtn.textContent = ctx.showVolPane ? 'Hide Vol (σ) Pane' : 'Show Vol (σ) Pane';
                destroyChartAndReplot();
            },
            volume: () => {
                ctx.showVolumePane = !ctx.showVolumePane;
                window.ChartCardContext.syncToCard(ctx);
                toggleVolumeBtn.textContent = ctx.showVolumePane ? 'Hide Volume Pane' : 'Show Volume Pane';
                destroyChartAndReplot();
            },
            revenue: () => {
                ctx.showRevenuePane = !ctx.showRevenuePane;
                window.ChartCardContext.syncToCard(ctx);
                toggleRevenueBtn.textContent = ctx.showRevenuePane ? 'Hide Revenue Pane' : 'Show Revenue Pane';
                destroyChartAndReplot();
            },
            fundamentalsPane: () => {
                ctx.showFundamentalsPane = !ctx.showFundamentalsPane;
                window.ChartCardContext.syncToCard(ctx);
                toggleFundamentalsPaneBtn.textContent = ctx.showFundamentalsPane ? 'Hide Fundamentals Pane' : 'Show Fundamentals Pane';

                // Show/hide metric buttons based on pane state
                const metricButtonsDisplay = ctx.showFundamentalsPane ? 'inline-block' : 'none';
                if (toggleRevenueMetricBtn) toggleRevenueMetricBtn.style.display = metricButtonsDisplay;
                if (toggleNetIncomeMetricBtn) toggleNetIncomeMetricBtn.style.display = metricButtonsDisplay;
                if (toggleEpsMetricBtn) toggleEpsMetricBtn.style.display = metricButtonsDisplay;
                if (toggleFcfMetricBtn) toggleFcfMetricBtn.style.display = metricButtonsDisplay;

                destroyChartAndReplot();
            },
            raw: () => {
                ctx.useRaw = !ctx.useRaw;
                toggleRawBtn.textContent = ctx.useRaw ? 'Show % Basis' : 'Show Raw';

                // Update price scale format immediately
                if (chart && chart.priceScale) {
                    const precision = ctx.decimalPrecision !== undefined ? ctx.decimalPrecision : 2;
                    const priceFormat = ctx.useRaw
                        ? {
                            type: 'custom', minMove: 0.01, formatter: (price) => {
                                // Magnitude-based decimals for raw prices, capped by slider maximum
                                const absPrice = Math.abs(price);
                                const magDecimals = absPrice >= 1000 ? 0 : absPrice >= 100 ? 1 : absPrice >= 1 ? 2 : absPrice >= 0.01 ? 4 : 6;
                                const dec = Math.min(magDecimals, precision);
                                return price.toFixed(dec);
                            }
                        }
                        : {
                            type: 'custom', minMove: 0.1, formatter: (v) => {
                                const diff = v - 100;
                                const sign = diff > 0 ? '+' : diff < 0 ? '-' : '';
                                // Magnitude-based decimals, capped by slider maximum
                                const magDecimals = Math.abs(diff) >= 100 ? 0 : Math.abs(diff) >= 10 ? 1 : 2;
                                const dec = Math.min(magDecimals, precision);
                                return `${sign}${Math.abs(diff).toFixed(dec)}%`;
                            }
                        };

                    try {
                        chart.priceScale('right').applyOptions({ priceFormat });
                    } catch (e) {
                        console.warn('[Card] Could not update price scale format:', e);
                    }
                }

                window.ChartCardContext.syncToCard(ctx);
                saveCards();
                plot();
                // Update zero line after mode change
                setTimeout(() => updateZeroLine(), 100);
            },
            logScale: () => {
                ctx.useLogScale = !ctx.useLogScale;
                elements.toggleLogScaleBtn.textContent = ctx.useLogScale ? 'Linear Scale' : 'Log Scale';

                // Apply log scale to chart
                if (chart && chart.priceScale) {
                    chart.priceScale('right').applyOptions({
                        mode: ctx.useLogScale ? 1 : 0  // 0=Normal, 1=Logarithmic
                    });
                }

                window.ChartCardContext.syncToCard(ctx);
                saveCards();
            },
            lastLabel: () => {
                ctx.lastLabelVisible = !ctx.lastLabelVisible;
                console.log(`[Card:${cardId}] Last value label ${ctx.lastLabelVisible ? 'enabled' : 'disabled'}`);
                window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());
                // Apply to all existing series
                priceSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: ctx.lastLabelVisible }));
                if (avgSeries) avgSeries.applyOptions({ lastValueVisible: ctx.lastLabelVisible });
                if (volPane && volSeriesMap) {
                    volSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: ctx.lastLabelVisible }));
                }
                // Apply to volume pane series (trading volume)
                if (volumePane && volumeSeriesMap) {
                    volumeSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: ctx.lastLabelVisible }));
                }
                // Apply to revenue pane series
                if (revenuePane && revenueSeriesMap) {
                    revenueSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: ctx.lastLabelVisible }));
                }
                window.ChartCardContext.syncToCard(ctx);
                saveCards();
            },
            lastTicker: () => {
                ctx.lastTickerVisible = !ctx.lastTickerVisible;
                console.log(`[Card:${cardId}] Last ticker label ${ctx.lastTickerVisible ? 'enabled' : 'disabled'}`);
                window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());
                // Update ticker labels visibility
                if (tickerLabelsContainer) {
                    window.ChartTickerLabels.setLabelsVisibility(tickerLabelsContainer, ctx.lastTickerVisible);
                }
                window.ChartCardContext.syncToCard(ctx);
                saveCards();
            },
            zeroLine: () => {
                ctx.showZeroLine = !ctx.showZeroLine;
                console.log(`[Card:${cardId}] Zero line ${ctx.showZeroLine ? 'enabled' : 'disabled'}`);

                updateZeroLine();

                window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());
                window.ChartCardContext.syncToCard(ctx);
                saveCards();
            },
            reshuffleColors: () => {
                console.log(`[Card:${cardId}] Reshuffling colors`);

                // Create shuffled copy of colors array
                const shuffledColors = [...window.ChartConfig.COLORS].sort(() => Math.random() - 0.5);

                // Reassign random colors to all tickers
                const tickersArray = Array.from(selectedTickers);
                tickersArray.forEach((ticker, index) => {
                    tickerColorMap.set(ticker, shuffledColors[index % shuffledColors.length]);
                });

                // Update UI
                window.ChartDomBuilder.addTickerChips(
                    selectedTickersDiv, selectedTickers, tickerColorMap, multiplierMap, hiddenTickers, handleChipRemove
                );

                // Update chart series colors
                priceSeriesMap.forEach((series, ticker) => {
                    const newColor = tickerColorMap.get(ticker);
                    if (newColor) {
                        series.applyOptions({
                            color: newColor,
                            lineColor: newColor
                        });
                    }
                });

                // Update ticker labels colors
                if (tickerLabelsContainer) {
                    window.ChartTickerLabels.updateAllLabels(
                        tickerLabelsContainer, priceSeriesMap, tickerColorMap, hiddenTickers,
                        ctx.useRaw ? rawPriceMap : latestRebasedData, chart, ctx.lastTickerVisible,
                        getCurrentFontSize()
                    );
                }

                saveCards();
            },
            avg: () => {
                ctx.showAvg = !ctx.showAvg;
                toggleAvgBtn.textContent = ctx.showAvg ? 'Hide Avg' : 'Show Avg';
                window.ChartCardContext.syncToCard(ctx);
                saveCards();
                if (ctx.showAvg && !ctx.useRaw) {
                    avgSeries = window.ChartSeriesManager.updateAverageSeries(
                        chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, ctx.lastLabelVisible
                    );
                } else if (avgSeries) {
                    chart.removeSeries(avgSeries);
                    avgSeries = null;
                }
            },
            fixedLegend: () => {
                ctx.showFixedLegend = !ctx.showFixedLegend;
                console.log(`[Card:${cardId}] Fixed legend ${ctx.showFixedLegend ? 'enabled' : 'disabled'}`);

                if (ctx.showFixedLegend) {
                    // Create fixed legend if it doesn't exist
                    if (!fixedLegendEl) {
                        fixedLegendEl = window.ChartFixedLegend.createFixedLegend(chartBox, {
                            initialX: ctx.fixedLegendPos?.x || 10,
                            initialY: ctx.fixedLegendPos?.y || 10,
                            initialWidth: ctx.fixedLegendSize?.width || null,
                            initialHeight: ctx.fixedLegendSize?.height || null
                        });

                        // Setup state change handler
                        fixedLegendEl._onStateChange = (changes) => {
                            if (changes.x !== undefined || changes.y !== undefined) {
                                ctx.fixedLegendPos = {
                                    x: changes.x !== undefined ? changes.x : ctx.fixedLegendPos?.x || 10,
                                    y: changes.y !== undefined ? changes.y : ctx.fixedLegendPos?.y || 10
                                };
                            }
                            if (changes.width !== undefined || changes.height !== undefined) {
                                ctx.fixedLegendSize = {
                                    width: changes.width !== undefined ? changes.width : ctx.fixedLegendSize?.width || null,
                                    height: changes.height !== undefined ? changes.height : ctx.fixedLegendSize?.height || null
                                };
                            }
                            window.ChartCardContext.syncToCard(ctx);
                            debouncedSaveCards();
                        };
                    }

                    // Show legend and update with latest values
                    window.ChartFixedLegend.show(fixedLegendEl);
                    updateFixedLegend();
                } else {
                    // Hide legend
                    if (fixedLegendEl) {
                        window.ChartFixedLegend.hide(fixedLegendEl);
                    }
                }

                window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());
                window.ChartCardContext.syncToCard(ctx);
                saveCards();
            },
            legendTickers: () => {
                ctx.showLegendTickers = !ctx.showLegendTickers;
                console.log(`[Card:${cardId}] Legend tickers ${ctx.showLegendTickers ? 'enabled' : 'disabled'}`);

                // Update fixed legend to reflect new setting
                if (ctx.showFixedLegend && fixedLegendEl) {
                    updateFixedLegend();
                }

                window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());
                window.ChartCardContext.syncToCard(ctx);
                saveCards();
            },
            notes: () => {
                const showNotes = notesSection.style.display !== 'none';
                notesSection.style.display = showNotes ? 'none' : 'block';
                ctx.showNotes = !showNotes;
                ctx.notes = notesTextarea.value;
                window.ChartCardContext.syncToCard(ctx);

                window.ChartDomBuilder.updateButtonStates(elements, { ...getButtonStates(), showNotes: !showNotes });
                saveCards();
            }
        };

        // Helper function to update metric button states
        function updateMetricButtonStates() {
            if (toggleRevenueMetricBtn) {
                toggleRevenueMetricBtn.style.fontWeight = ctx.fundamentalsMetrics.includes('revenue') ? 'bold' : 'normal';
                toggleRevenueMetricBtn.style.opacity = ctx.fundamentalsMetrics.includes('revenue') ? '1' : '0.5';
            }
            if (toggleNetIncomeMetricBtn) {
                toggleNetIncomeMetricBtn.style.fontWeight = ctx.fundamentalsMetrics.includes('netincome') ? 'bold' : 'normal';
                toggleNetIncomeMetricBtn.style.opacity = ctx.fundamentalsMetrics.includes('netincome') ? '1' : '0.5';
            }
            if (toggleEpsMetricBtn) {
                toggleEpsMetricBtn.style.fontWeight = ctx.fundamentalsMetrics.includes('eps') ? 'bold' : 'normal';
                toggleEpsMetricBtn.style.opacity = ctx.fundamentalsMetrics.includes('eps') ? '1' : '0.5';
            }
            if (toggleFcfMetricBtn) {
                toggleFcfMetricBtn.style.fontWeight = ctx.fundamentalsMetrics.includes('fcf') ? 'bold' : 'normal';
                toggleFcfMetricBtn.style.opacity = ctx.fundamentalsMetrics.includes('fcf') ? '1' : '0.5';
            }
        }

        // Initialize metric button visibility and states
        if (ctx.showFundamentalsPane) {
            if (toggleRevenueMetricBtn) toggleRevenueMetricBtn.style.display = 'inline-block';
            if (toggleNetIncomeMetricBtn) toggleNetIncomeMetricBtn.style.display = 'inline-block';
            if (toggleEpsMetricBtn) toggleEpsMetricBtn.style.display = 'inline-block';
            if (toggleFcfMetricBtn) toggleFcfMetricBtn.style.display = 'inline-block';
        }
        updateMetricButtonStates();

        // Metric toggle helper
        function toggleMetric(metricName) {
            const index = ctx.fundamentalsMetrics.indexOf(metricName);
            if (index > -1) {
                ctx.fundamentalsMetrics.splice(index, 1);
            } else {
                ctx.fundamentalsMetrics.push(metricName);
            }
            window.ChartCardContext.syncToCard(ctx);
            updateMetricButtonStates();
            saveCards();
            if (ctx.showFundamentalsPane) plot();
        }

        // Show Fundamentals button
        const showFundamentalsBtn = card.querySelector('.show-fundamentals-btn');
        if (showFundamentalsBtn) {
            showFundamentalsBtn.addEventListener('click', () => {
                if (window.ChartFundamentals && typeof window.ChartFundamentals.toggle === 'function') {
                    window.ChartFundamentals.toggle(card);
                } else {
                    console.error('[Card] ChartFundamentals module not loaded');
                }
            });
        }

        // Function to update zero line visibility and data
        function updateZeroLine() {
            if (!chart) return;

            if (ctx.showZeroLine) {
                if (!zeroLineSeries) {
                    zeroLineSeries = chart.addSeries(LightweightCharts.LineSeries, {
                        color: '#666666',
                        lineWidth: 1,
                        lineStyle: LightweightCharts.LineStyle.Dashed,
                        lastValueVisible: false,
                        priceLineVisible: false,
                        crosshairMarkerVisible: false,
                        title: ''
                    });
                }

                // Update zero line data based on current mode
                const zeroValue = ctx.useRaw ? 0 : 100; // 0 for raw prices, 100 for percentage (rebased to 100)

                // Get visible time range
                const timeScale = chart.timeScale();
                const visibleRange = timeScale.getVisibleRange();

                if (visibleRange) {
                    // Create a simple horizontal line across the visible range
                    const lineData = [
                        { time: visibleRange.from, value: zeroValue },
                        { time: visibleRange.to, value: zeroValue }
                    ];
                    zeroLineSeries.setData(lineData);
                } else {
                    // Fallback: use a wide time range
                    const now = Math.floor(Date.now() / 1000);
                    const tenYearsAgo = now - (10 * 365 * 24 * 60 * 60);
                    const lineData = [
                        { time: tenYearsAgo, value: zeroValue },
                        { time: now, value: zeroValue }
                    ];
                    zeroLineSeries.setData(lineData);
                }
            } else {
                // Remove zero line
                if (zeroLineSeries) {
                    chart.removeSeries(zeroLineSeries);
                    zeroLineSeries = null;
                }
            }
        }

        // Star button click handler
        if (starBtn) {
            // Set initial star state
            starBtn.textContent = ctx.starred ? '★' : '☆';
            starBtn.style.color = ctx.starred ? '#f5a623' : '#666';

            starBtn.addEventListener('click', () => {
                ctx.starred = !ctx.starred;
                window.ChartCardContext.syncToCard(ctx);
                starBtn.textContent = ctx.starred ? '★' : '☆';
                starBtn.style.color = ctx.starred ? '#f5a623' : '#666';
                saveCards();
            });
        }

        // Tag management
        const { tagContainer } = elements;
        if (tagContainer) {
            if (!ctx.tags) ctx.tags = [];

            function renderTags() {
                tagContainer.innerHTML = '';
                ctx.tags.forEach(tag => {
                    const tagEl = document.createElement('span');
                    tagEl.className = 'tag';
                    tagEl.innerHTML = `${tag}<span class="tag-remove" data-tag="${tag}">&times;</span>`;
                    tagContainer.appendChild(tagEl);
                });

                // Add "+" button
                const addBtn = document.createElement('button');
                addBtn.className = 'tag-add-btn';
                addBtn.textContent = '+';
                addBtn.title = 'Add tag';
                addBtn.addEventListener('click', showTagInput);
                tagContainer.appendChild(addBtn);

                // Remove tag handler
                tagContainer.querySelectorAll('.tag-remove').forEach(btn => {
                    btn.addEventListener('click', (e) => {
                        const tagToRemove = e.target.dataset.tag;
                        ctx.tags = ctx.tags.filter(t => t !== tagToRemove);
                        window.ChartCardContext.syncToCard(ctx);
                        renderTags();
                        saveCards();
                        if (window.updateTagFilterDropdown) window.updateTagFilterDropdown();
                    });
                });
            }

            function showTagInput() {
                const inputContainer = document.createElement('div');
                inputContainer.className = 'tag-input-container';

                const input = document.createElement('input');
                input.type = 'text';
                input.className = 'tag-input';
                input.placeholder = 'Tag...';

                const suggestions = document.createElement('div');
                suggestions.className = 'tag-suggestions';

                inputContainer.appendChild(input);
                inputContainer.appendChild(suggestions);

                // Replace add button with input
                const addBtn = tagContainer.querySelector('.tag-add-btn');
                if (addBtn) addBtn.style.display = 'none';
                tagContainer.appendChild(inputContainer);
                input.focus();

                function updateSuggestions() {
                    const val = input.value.toLowerCase().trim();
                    const allTags = window.getAllTags ? window.getAllTags() : [];
                    const matches = allTags.filter(t =>
                        t.toLowerCase().includes(val) && !ctx.tags.includes(t)
                    );

                    if (matches.length > 0 && val) {
                        suggestions.innerHTML = matches.map(t =>
                            `<div class="tag-suggestion" data-tag="${t}">${t}</div>`
                        ).join('');
                        suggestions.classList.add('show');

                        suggestions.querySelectorAll('.tag-suggestion').forEach(el => {
                            el.addEventListener('click', () => {
                                addTag(el.dataset.tag);
                            });
                        });
                    } else {
                        suggestions.classList.remove('show');
                    }
                }

                function addTag(tag) {
                    tag = tag.trim();
                    if (tag && !ctx.tags.includes(tag)) {
                        ctx.tags.push(tag);
                        window.ChartCardContext.syncToCard(ctx);
                        renderTags();
                        saveCards();
                        if (window.updateTagFilterDropdown) window.updateTagFilterDropdown();
                    } else {
                        inputContainer.remove();
                        if (addBtn) addBtn.style.display = '';
                    }
                }

                input.addEventListener('input', updateSuggestions);

                input.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        addTag(input.value);
                    } else if (e.key === 'Escape') {
                        inputContainer.remove();
                        if (addBtn) addBtn.style.display = '';
                    }
                });

                input.addEventListener('blur', () => {
                    setTimeout(() => {
                        if (document.activeElement !== input) {
                            inputContainer.remove();
                            if (addBtn) addBtn.style.display = '';
                        }
                    }, 200);
                });
            }

            renderTags();
        }

        // Notes section handlers
        if (notesTextarea) {
            // Auto-save notes on input
            notesTextarea.addEventListener('input', () => {
                ctx.notes = notesTextarea.value;
                window.ChartCardContext.syncToCard(ctx);
                saveCards();
            });
        }

        // Function to update fixed legend with latest values
        function updateFixedLegend() {
            if (!ctx.showFixedLegend || !fixedLegendEl) return;

            // Get current visible range
            let visibleRange = null;
            if (chart && chart.timeScale) {
                try {
                    visibleRange = chart.timeScale().getVisibleRange();
                } catch (e) {
                    console.warn('[FixedLegend] Could not get visible range:', e);
                }
            }

            const legendData = [];
            selectedTickers.forEach(ticker => {
                if (hiddenTickers.has(ticker)) return;

                // Get data array
                const dataArray = ctx.useRaw ? rawPriceMap.get(ticker) : latestRebasedData[ticker];
                if (!dataArray || dataArray.length === 0) return;

                // If we have a visible range, check if ticker has any data points in that range
                if (visibleRange && visibleRange.from && visibleRange.to) {
                    const hasVisibleData = dataArray.some(point =>
                        point.time >= visibleRange.from && point.time <= visibleRange.to
                    );
                    if (!hasVisibleData) return; // Skip this ticker if it has no visible data
                }

                // Get latest value
                const latestPoint = dataArray[dataArray.length - 1];
                if (latestPoint && latestPoint.value != null) {
                    legendData.push({
                        ticker,
                        value: latestPoint.value,
                        color: tickerColorMap.get(ticker)
                    });
                }
            });

            window.ChartFixedLegend.updateContent(fixedLegendEl, legendData, {
                useRaw: ctx.useRaw,
                hiddenTickers,
                tickerColorMap,
                getName: (t) => nameCache[t],
                showTickers: ctx.showLegendTickers
            });
        }

        // ═══════════════════════════════════════════════════════════════
        // PHASE A EVENT HANDLERS - Named functions for bindAllWithCleanup
        // ═══════════════════════════════════════════════════════════════

        // Fit button handler: fit chart to full data range and persist
        function handleFit() {
            if (!chart) return;
            const dataRange = getCurrentDataRange();
            if (dataRange) {
                try {
                    chart.timeScale().setVisibleRange(dataRange);
                    ctx.visibleRange = dataRange;
                    window.ChartCardContext.syncToCard(ctx);
                    saveCards();
                } catch (e) {
                    chart.timeScale().fitContent();
                }
            } else {
                chart.timeScale().fitContent();
            }
        }

        // Interval select handler
        function handleIntervalChange() {
            const val = intervalSelect.value;
            ctx.manualInterval = val === 'auto' ? null : val;
            window.ChartCardContext.syncToCard(ctx);
            console.log(`Interval changed to: ${val}`);
            debouncedSaveCards();
            // Replot to fetch data with new interval
            if (selectedTickers.size > 0) {
                plot();
            }
        }

        // Range select handler
        function handleRangeChange() {
            const val = rangeSelect.value;
            if (!val) return;

            // Temporarily unsubscribe from range changes to prevent interference
            if (rangeSaveHandler && chart && chart.timeScale) {
                try {
                    chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                    console.log('[RangeSelect] Unsubscribed from range changes');
                } catch (_) { }
            }

            // Special case: if selecting 1995 (or any year before 2000), find earliest data across all series
            if (val === '1995' || (val !== 'ytd' && parseInt(val, 10) < 2000)) {
                // Find earliest timestamp across all series (price + fundamentals)
                let earliestTime = null;

                // Check price series
                priceSeriesMap.forEach((series, ticker) => {
                    try {
                        const data = rawPriceMap.get(ticker);
                        if (data && data.length > 0 && data[0].time) {
                            const firstTime = data[0].time;
                            if (!earliestTime || firstTime < earliestTime) {
                                earliestTime = firstTime;
                            }
                        }
                    } catch (e) { /* ignore */ }
                });

                // Check fundamental series
                fundamentalSeriesMap.forEach((series, seriesKey) => {
                    try {
                        // Get data from the series - LightweightCharts doesn't expose data directly,
                        // so we need to track it separately or use a different approach
                        // For now, if we have fundamentals pane, assume it goes back to ~1996
                        if (ctx.showFundamentalsPane && !earliestTime) {
                            // Use 1996 as earliest for fundamentals (AAPL data goes back to 1996-04-01)
                            earliestTime = Date.UTC(1996, 0, 1) / 1000;
                        }
                    } catch (e) { /* ignore */ }
                });

                // If we have fundamental data showing, use 1996 as earliest
                if (ctx.showFundamentalsPane && fundamentalSeriesMap.size > 0) {
                    earliestTime = Date.UTC(1996, 0, 1) / 1000;
                }

                // Default to price data earliest if no fundamentals
                if (!earliestTime) {
                    chart.timeScale().fitContent();
                    const timeScale = chart.timeScale();
                    const visibleRange = timeScale.getVisibleRange();
                    if (visibleRange) {
                        ctx.visibleRange = { from: visibleRange.from, to: visibleRange.to };
                        window.ChartCardContext.syncToCard(ctx);
                    }
                    saveCards();

                    // Resubscribe to range changes
                    if (rangeSaveHandler) {
                        try {
                            chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);
                        } catch (_) { }
                    }
                    return;
                }

                // Set flag to skip range restoration in pane operations
                ctx.skipRangeRestoration = true;

                // For fundamentals, we know the earliest data is 2005-06-30
                // Set explicit range to show all fundamental data
                const fundamentalsEarliest = Date.UTC(2005, 5, 30) / 1000;  // June 30, 2005
                const from = fundamentalsEarliest;
                const to = Math.floor(Date.now() / 1000);

                console.log(`[RangeSelect] Setting explicit range from ${new Date(from * 1000).toISOString()} to ${new Date(to * 1000).toISOString()}`);

                // Update ctx state
                ctx.visibleRange = { from, to };
                window.ChartCardContext.syncToCard(ctx);

                // Set the range
                chart.timeScale().setVisibleRange({ from, to });

                // Verify what range was actually set
                setTimeout(() => {
                    const actualRange = chart.timeScale().getVisibleRange();
                    if (actualRange) {
                        console.log(`[RangeSelect] Actual visible range after setting: from ${new Date(actualRange.from * 1000).toISOString()} to ${new Date(actualRange.to * 1000).toISOString()}`);
                        // Update with actual range if different
                        ctx.visibleRange = { from: actualRange.from, to: actualRange.to };
                        window.ChartCardContext.syncToCard(ctx);
                        saveCards();
                    }
                }, 100);

                // Resubscribe to range changes AFTER a delay
                setTimeout(() => {
                    if (rangeSaveHandler) {
                        try {
                            chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);
                            console.log('[RangeSelect] Resubscribed to range changes');
                        } catch (_) { }
                    }
                }, 500);
                return;
            }

            let startYear;
            if (val === 'ytd') {
                startYear = new Date().getUTCFullYear();
            } else {
                startYear = parseInt(val, 10);
            }
            const from = Date.UTC(startYear, 0, 1) / 1000;
            const to = Math.floor(Date.now() / 1000);

            // Update ctx state FIRST
            ctx.visibleRange = { from, to };
            window.ChartCardContext.syncToCard(ctx);

            // Then set the visual range
            chart.timeScale().setVisibleRange({ from, to });

            saveCards();

            // Resubscribe to range changes
            if (rangeSaveHandler) {
                try {
                    chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);
                } catch (_) { }
            }
        }

        // Title input handler
        function handleTitleChange() {
            ctx.title = titleInput.value;
            window.ChartCardContext.syncToCard(ctx);
            if (navLink) {
                navLink.textContent = titleInput.value || (selectedTickers.size ? Array.from(selectedTickers)[0] : cardId);
            }
            saveCards();
        }

        // Add chart button handler
        function handleAddChart() {
            // Get the current active page wrapper
            let targetWrapper = null;
            if (window.PageManager && window.PageManager.getActivePage) {
                const activePage = window.PageManager.getActivePage();
                targetWrapper = window.PageManager.ensurePage(activePage);
            }
            // Create new chart on the active page with default settings (all panes off)
            const newCard = createChartCard({
                tickers: '',
                wrapperEl: targetWrapper,
                height: 500,
                fontSize: window.ChartConfig?.UI?.FONT_DEFAULT || 12
            });
            saveCards();
            // Insert new card after the current card (within the same page)
            if (card.nextSibling) {
                (targetWrapper || wrapper).insertBefore(newCard, card.nextSibling);
            }
        }

        // Remove card button handler (includes event cleanup)
        function handleRemoveCard() {
            try {
                // Cleanup bound event listeners first
                if (card._unbindEvents) {
                    card._unbindEvents();
                }

                // Cleanup global keydown listener for settings panel
                if (card._escapeHandler) {
                    document.removeEventListener('keydown', card._escapeHandler);
                }

                // Remove nav link
                if (navLink && navLink.parentElement) {
                    navLink.parentElement.removeChild(navLink);
                }

                // Destroy chart (unsubscribes all handlers, removes chart, clears series)
                destroyChart();
            } catch (e) {
                console.warn('Cleanup on remove failed:', e);
            }

            // Remove card from DOM and persist
            if (card && card.parentElement) {
                card.parentElement.removeChild(card);
            }
            saveCards();
        }

        // ═══════════════════════════════════════════════════════════════
        // BIND PHASE A EVENTS via ChartEventHandlers
        // ═══════════════════════════════════════════════════════════════
        card._unbindEvents = window.ChartEventHandlers.bindAllWithCleanup(card, elements, {
            toggles: toggleHandlers,
            toggleMetric: toggleMetric,
            ticker: {
                onAddTicker: addTicker,
                onPlot: plot,
                onFit: handleFit,
                onRangeChange: handleRangeChange,
                onIntervalChange: handleIntervalChange
            },
            card: {
                onTitleChange: handleTitleChange,
                onAddChart: handleAddChart,
                onRemoveCard: handleRemoveCard,
                onExport: async () => {
                    if (!chart) {
                        alert('No chart to export. Please plot a chart first.');
                        return;
                    }
                    console.log('[Export] Exporting chart for LinkedIn');
                    const title = titleInput ? titleInput.value : '';
                    try {
                        const result = await window.ChartExport.exportForLinkedIn(chart, title, chartBox);
                        if (result.success) {
                            console.log('[Export] Export successful');
                        } else {
                            console.error('[Export] Export failed:', result.message);
                            alert(`Export failed: ${result.message}`);
                        }
                    } catch (error) {
                        console.error('[Export] Export error:', error);
                        alert(`Export error: ${error.message}`);
                    }
                }
            }
        });

        // Set initial interval value (handler bound via bindAllWithCleanup)
        if (intervalSelect && ctx.manualInterval) {
            intervalSelect.value = ctx.manualInterval;
        }

        // Bind chip toggle & multiplier events via helper
        window.CardEventBinder.bindTickerInteractions(
            selectedTickersDiv,
            hiddenTickers,
            multiplierMap,
            () => { ctx.hiddenTickers = hiddenTickers; window.ChartCardContext.syncToCard(ctx); },
            () => plot(),
            saveCards,
            () => ctx.useRaw
        );

        // Auto-plot if we have initial tickers and the page is visible
        if (selectedTickers.size > 0) {
            // Check if this card's page is currently visible
            const page = card.closest('.page');
            if (page && page.style.display !== 'none') {
                setTimeout(plot, PLOT_DEFER_MS);
            }
            // If page is hidden, pages.js will trigger plot when it becomes visible
        }

        return card;
    }

    // Initialize on DOM ready
    document.addEventListener('DOMContentLoaded', () => {
        const addBtn = document.getElementById('add-chart-btn');
        if (addBtn) {
            addBtn.addEventListener('click', () => createChartCard(''));
        }

        // Populate autocomplete with tickers and metadata
        (async () => {
            try {
                const [tickersResp, metadataResp] = await Promise.all([
                    fetch(window.ChartUtils.apiUrl('/api/tickers')),
                    fetch(window.ChartUtils.apiUrl('/api/metadata?tickers=ALL'))
                ]);

                const tickers = await tickersResp.json();
                const metadata = await metadataResp.json();

                const dl = document.getElementById('ticker-list');
                if (dl) {
                    dl.innerHTML = '';

                    // Add ticker options with company names
                    tickers.forEach(t => {
                        const opt = document.createElement('option');

                        // If we have metadata, create option as "TICKER - Company Name"
                        // This allows searching by either ticker or company name
                        if (metadata[t] && metadata[t] !== t) {
                            opt.value = `${t} - ${metadata[t]}`;
                        } else {
                            opt.value = t;
                        }

                        dl.appendChild(opt);
                    });

                    // Add special tickers
                    ['ALLW_VALUE', 'ALLW_SHARES'].forEach(x => {
                        const opt = document.createElement('option');
                        opt.value = x;
                        dl.appendChild(opt);
                    });
                }
            } catch (e) {
                console.warn('Failed to populate autocomplete:', e);
            }
        })();

        // Restore or create cards (backend-first for cross-browser persistence)
        const urlParams = new URLSearchParams(window.location.search);
        const startBlank = urlParams.has('blank');
        if (startBlank) {
            createChartCard('');
            return;
        }

        (async () => {
            try {
                const resp = await fetch(window.ChartUtils.apiUrl('/api/workspace'));
                const ws = await resp.json();
                if (Array.isArray(ws) && ws.length) {
                    console.log('[Restore] Loaded legacy workspace (array) from server');
                    ws.forEach(c => restoreCard(c));
                    window.ChartUtils.safeSetJSON(window.ChartConfig.STORAGE_KEYS.CARDS, ws);
                    return;
                } else if (ws && typeof ws === 'object') {
                    const cards = Array.isArray(ws.cards) ? ws.cards : [];
                    const pagesMeta = (ws.pages && typeof ws.pages === 'object') ? ws.pages : null;
                    if (pagesMeta) {
                        window.ChartUtils.safeSetJSON('sandbox_pages', pagesMeta);
                        const nameCount = pagesMeta.names ? Object.keys(pagesMeta.names).length : 0;
                        console.log(`[Restore] Loaded workspace (object) from server; pages meta present (pageNames=${nameCount})`);
                        if (window.PageManager) {
                            if (Array.isArray(pagesMeta.pages)) {
                                pagesMeta.pages.filter(n => n !== 1).forEach(n => window.PageManager.ensurePage(n));
                            }
                            if (pagesMeta.names && typeof pagesMeta.names === 'object') {
                                Object.entries(pagesMeta.names).forEach(([num, name]) => {
                                    window.PageManager.renamePage(Number(num), String(name));
                                });
                            }
                            if (pagesMeta.active) {
                                window.PageManager.showPage(pagesMeta.active);
                            }
                        }
                    } else {
                        console.log('[Restore] Workspace object has no pages meta');
                    }
                    cards.forEach(c => restoreCard(c));
                    window.ChartUtils.safeSetJSON(window.ChartConfig.STORAGE_KEYS.CARDS, cards);
                    // Refresh navigation filtering after cards are loaded
                    if (window.PageManager && typeof window.PageManager.refreshNavigation === 'function') {
                        window.PageManager.refreshNavigation();
                    }
                    if (cards.length > 0) return;
                    console.log('[Restore] Workspace object had no cards; checking localStorage');
                } else {
                    console.log('[Restore] Server returned empty workspace; checking localStorage');
                }
            } catch (e) {
                console.warn('[Restore] Server load failed, falling back to localStorage', e);
            }
            const stored = window.ChartUtils.safeGetJSON(window.ChartConfig.STORAGE_KEYS.CARDS, []);
            if (Array.isArray(stored) && stored.length) {
                console.log('[Restore] Loaded workspace from localStorage fallback');
                stored.forEach(c => restoreCard(c));
                // Refresh navigation filtering after cards are loaded
                if (window.PageManager && typeof window.PageManager.refreshNavigation === 'function') {
                    window.PageManager.refreshNavigation();
                }
                // Push local state to server to sync
                if (window.StateManager && typeof window.StateManager.saveCards === 'function') {
                    window.StateManager.saveCards(stored);
                }
            } else {
                console.log('[Restore] No stored workspace found; creating default card');
                createChartCard('SPY');
            }
        })();
    });

    window.createChartCard = createChartCard;
})();
