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

    // Initialize global chip context menu (delegated to ChartCardTickers)
    window.ChartCardTickers.initGlobalChipContextMenu();

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
        // Check type registry for special card types (delegated to ChartCardRegistry)
        if (options.type && window.ChartCardRegistry && window.ChartCardRegistry.hasType(options.type)) {
            const wrapper = options.wrapperEl || document.getElementById(WRAPPER_ID);
            return window.ChartCardRegistry.dispatchCreate(options.type, wrapper, options);
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
        // Create nav link via ChartCardNav module
        const navLink = window.ChartCardNav.createNavLink(cardId, initialTitle, initialTickers, targetPage);
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

        // ═══════════════════════════════════════════════════════════════
        // PLOT FUNCTION (delegated to ChartCardPlot module)
        // ═══════════════════════════════════════════════════════════════
        async function plot() {
            return window.ChartCardPlot.plot(ctx, { initialHeight, initialRange });
        }

        // NOTE: Legacy plot_legacy() removed - now delegated to ChartCardPlot.plot(ctx)
        // See chart-card-plot.js for implementation

        // ═══════════════════════════════════════════════════════════════
        // TICKER HANDLERS (delegated to ChartCardTickers module)
        // ═══════════════════════════════════════════════════════════════
        const tickerHandlers = window.ChartCardTickers.createHandlers(ctx, { plot });

        // Initialize tickers and render chips
        tickerHandlers.initializeTickers(initialTickers);
        tickerHandlers.bindChipInteractions();

        // Alias for event binding
        const addTicker = tickerHandlers.addTickerFromInput;
        const handleChipRemove = tickerHandlers.handleChipRemove;

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
            window.ChartCardNav.updateNavLabel(navLink, titleInput.value, selectedTickers, cardId);
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
                window.ChartCardNav.removeNavLink(navLink);

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

        // NOTE: Chip toggle & multiplier events now bound via tickerHandlers.bindChipInteractions() above

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

    // Export createChartCard globally
    // Note: Sandbox-specific initialization (autocomplete, workspace restore) is in sandbox-init.js
    window.createChartCard = createChartCard;
})();
