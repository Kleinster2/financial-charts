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

        // Normal chart card: pass saved payload through directly
        // Schema owned by ChartCardContext.serialize/applyToCtx
        createChartCard({
            ...cardData,
            wrapperEl: wrapper,
            hydrateData: cardData
        });
    }

    // Company name fetching - delegated to ChartCardPlot module (single nameCache)
    async function ensureNames(tickers, chipNodes = null) {
        return window.ChartCardPlot.ensureNames(tickers, chipNodes);
    }

    // Save all chart states
    function saveCards() {
        const cards = Array.from(document.querySelectorAll('.chart-card')).map(card => {
            // Prefer ctx-based serialization when available
            if (card._ctx && window.ChartCardContext?.serialize) {
                return window.ChartCardContext.serialize(card._ctx);
            }
            // Fallback for cards without ctx (special types like dashboard, macro, etc.)
            return {
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
                starred: !!card._starred,
                tags: card._tags || []
            };
        });

        window.ChartUtils.safeSetJSON(window.ChartConfig.STORAGE_KEYS.CARDS, cards);
        if (window.StateManager && typeof window.StateManager.saveCards === 'function') {
            window.StateManager.saveCards(cards);
        }
    }
    window.saveCards = saveCards;

    // Tag filtering is now centralized in pages.js
    // The following globals are provided by pages.js:
    //   window.getAllTags, window.updateTagFilterDropdown, window.applyFilters, window.applyTagFilter

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
            hydrateData = null,
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
            initialUseLogScale,
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
            initialStarred,
            initialTags,
            cardId,
            targetPage,
            saveCards
        });
        card._ctx = ctx;
        // Hydrate ctx from saved payload (restore), otherwise do initial sync
        if (hydrateData && window.ChartCardContext?.applyToCtx) {
            window.ChartCardContext.applyToCtx(ctx, hydrateData);
        } else {
            window.ChartCardContext.syncToCard(ctx);
        }

        // ═══════════════════════════════════════════════════════════════
        // RUNTIME STATE INITIALIZATION
        // All chart instances, series maps, and handlers live in ctx.runtime
        // ═══════════════════════════════════════════════════════════════
        const rt = window.ChartCardContext.initRuntime(ctx);

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

        // Convenience aliases for runtime maps (used by local code)
        const priceSeriesMap = rt.priceSeriesMap;
        const volSeriesMap = rt.volSeriesMap;
        const volumeSeriesMap = rt.volumeSeriesMap;
        const revenueSeriesMap = rt.revenueSeriesMap;
        const fundamentalSeriesMap = rt.fundamentalSeriesMap;
        const rawPriceMap = rt.rawPriceMap;
        const latestRebasedData = rt.latestRebasedData;

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

        // ═══════════════════════════════════════════════════════════════
        // DELEGATED FUNCTIONS (use extracted modules with ctx)
        // ═══════════════════════════════════════════════════════════════

        // Compute min/max time across currently visible tickers with loaded data
        function getCurrentDataRange() {
            return window.ChartCardPlot.getCurrentDataRange(ctx);
        }

        // Destroy chart instance and cleanup all subscriptions/series/panes
        function destroyChart() {
            window.ChartCardPlot.destroyChart(ctx);
        }

        // Save visible range, destroy chart, and replot
        function destroyChartAndReplot() {
            window.ChartCardPlot.destroyChartAndReplot(ctx, plot);
        }

        // Apply resize to chart box based on height and active panes
        function applyResize(baseH) {
            window.ChartCardPlot.applyResize(ctx, baseH);
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
            if (rt.volumePane && typeof rt.volumePane.setStretchFactor === 'function') {
                rt.volumePane.setStretchFactor(factor);
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
                if (rt.volumePane && typeof rt.volumePane.setStretchFactor === 'function') {
                    rt.volumePane.setStretchFactor(v);
                }
            },
            formatDisplay: (v) => v.toFixed(1)
        });

        function applyFont(newSize) {
            if (rt.chart && typeof rt.chart.applyOptions === 'function') {
                console.log(`[Card:${cardId}] Applying axis font size ${newSize}`);
                try { rt.chart.applyOptions({ layout: { fontSize: newSize } }); } catch (e) { console.warn(`[Card:${cardId}] chart.applyOptions(layout.fontSize) failed`, e); }
            }
            // Update ticker labels font size
            if (rt.tickerLabelsContainer) {
                window.ChartTickerLabels.updateFontSize(rt.tickerLabelsContainer, newSize);
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
            if (rt.chart && rt.chart.priceScale) {
                const priceFormat = window.ChartUtils.createPriceFormatter(ctx.useRaw, precision);

                try {
                    rt.chart.priceScale('right').applyOptions({ priceFormat });
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
                if (s && rt.chart) {
                    try { rt.chart.removeSeries(s); } catch (_) { }
                }
                priceSeriesMap.delete(ticker);

                // Remove volume series (if present)
                if (volSeriesMap && rt.chart) {
                    const vs = volSeriesMap.get(ticker);
                    if (vs) {
                        try { rt.chart.removeSeries(vs); } catch (_) { }
                        volSeriesMap.delete(ticker);
                    }
                    // If no volume series remain, remove the pane
                    if (rt.volPane && volSeriesMap.size === 0) {
                        try { rt.volPane = window.ChartVolumeManager.clearVolumeSeries(rt.chart, rt.volPane, volSeriesMap); } catch (_) { }
                    }
                }

                // Update average series
                if (ctx.showAvg && !ctx.useRaw) {
                    try {
                        rt.avgSeries = window.ChartSeriesManager.updateAverageSeries(
                            rt.chart, rt.avgSeries, priceSeriesMap, hiddenTickers, undefined, ctx.lastLabelVisible
                        );
                    } catch (_) { }
                }

                // Remove ticker label
                if (rt.tickerLabelsContainer) {
                    window.ChartTickerLabels.removeLabel(rt.tickerLabelsContainer, ticker);
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

        // ═══════════════════════════════════════════════════════════════
        // PLOT FUNCTION (delegated to ChartCardPlot module)
        // ═══════════════════════════════════════════════════════════════
        async function plot() {
            return window.ChartCardPlot.plot(ctx, { initialHeight, initialRange });
        }

        // NOTE: Legacy plot_legacy() removed - now delegated to ChartCardPlot.plot(ctx)
        // See chart-card-plot.js for implementation

        // ═══════════════════════════════════════════════════════════════
        // TOGGLE HANDLERS (delegated to ChartCardToggles module)
        // ═══════════════════════════════════════════════════════════════
        const toggleHandlers = window.ChartCardToggles.createToggleHandlers(ctx, {
            plot,
            destroyChartAndReplot,
            persistState,
            handleChipRemove
        });

        // Initialize metric buttons
        window.ChartCardToggles.initMetricButtons(ctx);

        // Metric toggle helper
        const toggleMetric = window.ChartCardToggles.createToggleMetric(ctx, plot);


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

        // Function to update zero line visibility and data (delegated to module)
        function updateZeroLine() {
            window.ChartCardPlot.updateZeroLine(ctx);
        }

        // ═══════════════════════════════════════════════════════════════
        // META UI (star, tags, notes) - delegated to ChartCardMeta module
        // ═══════════════════════════════════════════════════════════════
        window.ChartCardMeta.initAll(ctx);

        // Function to update fixed legend with latest values (delegated to module)
        function updateFixedLegend() {
            window.ChartCardPlot.updateFixedLegend(ctx);
        }

        // ═══════════════════════════════════════════════════════════════
        // RANGE HANDLERS (delegated to ChartCardRange module)
        // ═══════════════════════════════════════════════════════════════
        const rangeHandlers = window.ChartCardRange.createRangeHandlers(ctx, { plot });

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
                onFit: rangeHandlers.handleFit,
                onRangeChange: rangeHandlers.handleRangeChange,
                onIntervalChange: rangeHandlers.handleIntervalChange
            },
            card: {
                onTitleChange: handleTitleChange,
                onAddChart: handleAddChart,
                onRemoveCard: handleRemoveCard,
                onExport: async () => {
                    if (!rt.chart) {
                        alert('No chart to export. Please plot a chart first.');
                        return;
                    }
                    console.log('[Export] Exporting chart for LinkedIn');
                    const title = titleInput ? titleInput.value : '';
                    try {
                        const result = await window.ChartExport.exportForLinkedIn(rt.chart, title, chartBox);
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
