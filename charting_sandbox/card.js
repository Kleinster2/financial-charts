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

    // Font size controls (axis font only)
    const FONT_MIN = window.ChartConfig?.UI?.FONT_MIN || 8;
    const FONT_MAX = window.ChartConfig?.UI?.FONT_MAX || 24;

    /**
     * Restore a card from saved data
     * @param {Object} cardData - Saved card configuration
     */
    function restoreCard(cardData) {
        const wrapper = window.PageManager ? window.PageManager.ensurePage(cardData.page || '1') : null;

        // Handle dashboard card type
        if (cardData.type === 'dashboard') {
            createChartCard({ type: 'dashboard', wrapperEl: wrapper });
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
            settingsPanelOpen: !!cardData.settingsPanelOpen
        });
    }

    // Company name fetching
    // Fetch company names for tickers; optionally pass in chipNodes to avoid global DOM scan
    async function ensureNames(tickers, chipNodes = null) {
        const missing = tickers.filter(t => !(t in nameCache));
        if (!missing.length) return;

        try {
            const metadata = await window.DataFetcher.getMetadata(missing);
            Object.assign(nameCache, metadata);

            const chips = chipNodes ? Array.from(chipNodes) : document.querySelectorAll('.chip');
            chips.forEach(ch => {
                const t = ch.dataset.ticker;
                if (nameCache[t]) ch.title = nameCache[t];
            });
        } catch (error) {
            console.error('Failed to fetch metadata:', error);
        }
    }

    // Save all chart states
    function saveCards() {
        const cards = Array.from(document.querySelectorAll('.chart-card')).map(card => ({
            page: card.closest('.page')?.dataset.page || '1',
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
            settingsPanelOpen: !!card._state?.settingsPanelOpen
        }));

        window.ChartUtils.safeSetJSON(window.ChartConfig.STORAGE_KEYS.CARDS, cards);
        if (window.StateManager && typeof window.StateManager.saveCards === 'function') {
            window.StateManager.saveCards(cards);
        }
    }
    window.saveCards = saveCards;

    /**
     * Create a chart card with the given options
     * @param {Object|string} optionsOrTickers - Options object or legacy ticker string
     * @returns {HTMLElement} The created card element
     */
    function createChartCard(optionsOrTickers) {
        // Handle dashboard card type
        if (optionsOrTickers && optionsOrTickers.type === 'dashboard') {
            const wrapper = optionsOrTickers.wrapperEl || document.getElementById(WRAPPER_ID);
            if (wrapper && window.ChartDashboard) {
                return window.ChartDashboard.createDashboardCard(wrapper);
            }
            console.error('Dashboard module not loaded');
            return null;
        }

        // Handle backward compatibility: if first arg is string, convert to options
        let options = {};
        if (typeof optionsOrTickers === 'string') {
            // Legacy positional parameters
            options = {
                tickers: arguments[0] || 'SPY',
                showDiff: arguments[1] || false,
                showAvg: arguments[2] || false,
                showVol: arguments[3] || false,
                showVolume: arguments[4] || false,
                useRaw: arguments[5] || false,
                multipliers: arguments[6] || {},
                hidden: arguments[7] || [],
                range: arguments[8] || null,
                title: arguments[9] || '',
                lastLabelVisible: arguments[10] !== false,
                showZeroLine: arguments[11] || false,
                wrapperEl: arguments[12] || null,
                height: arguments[13] || (window.ChartConfig?.DIMENSIONS?.CHART_MIN_HEIGHT || 400),
                fontSize: arguments[14] || (window.ChartConfig?.UI?.FONT_DEFAULT || 12),
                showFixedLegend: arguments[15] || false,
                fixedLegendPos: arguments[16] || { x: 10, y: 10 },
                fixedLegendSize: arguments[17] || null
            };
        } else {
            options = optionsOrTickers || {};
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
            decimalPrecision: initialDecimalPrecision = 2
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
            toggleAvgBtn, toggleLastLabelBtn, toggleLastTickerBtn, reshuffleColorsBtn, toggleZeroLineBtn, toggleFixedLegendBtn, toggleLegendTickersBtn, toggleNotesBtn, heightSlider, heightValue, volPaneHeightSlider, volPaneHeightValue, fontSlider, fontValue, decimalsSlider, decimalsValue, exportBtn, rangeSelect, intervalSelect, selectedTickersDiv, chartBox, titleInput, removeCardBtn, addChartBtn, notesSection, notesTextarea } = elements;

        // Initialize state
        let showDiff = initialShowDiff;
        let showAvg = initialShowAvg;
        let showVolPane = initialShowVol;  // Volatility pane
        let showVolumePane = initialShowVolume;  // Trading volume pane
        let showRevenuePane = initialShowRevenue;  // Revenue pane
        let showFundamentalsPane = initialShowFundamentalsPane;  // Fundamentals pane
        let fundamentalsMetrics = initialFundamentalsMetrics;  // Active metrics
        let useRaw = initialUseRaw;
        let lastLabelVisible = initialLastLabelVisible;
        let lastTickerVisible = initialLastTickerVisible;
        let showZeroLine = initialShowZeroLine;
        let showFixedLegend = initialShowFixedLegend;
        let showLegendTickers = initialShowLegendTickers;
        let chart = null;
        let volPane = null;  // Volatility pane
        let volumePane = null;  // Trading volume pane
        let revenuePane = null;  // Revenue pane
        let fundamentalsPane = null;  // Fundamentals pane
        let avgSeries = null;
        let tickerLabelsContainer = null;  // Container for ticker labels on right side
        let zeroLineSeries = null;
        let fixedLegendEl = null;

        let crosshairHandler = null;
        let debouncedRebase = null;
        let diffChart = null;
        let rangeSaveHandler = null;
        let tickerLabelHandler = null;
        let skipRangeApplication = false;  // Flag to skip automatic range application
        const debouncedSaveCards = (window.ChartUtils && window.ChartUtils.debounce) ? window.ChartUtils.debounce(saveCards, 300) : saveCards;

        const selectedTickers = new Set();
        const hiddenTickers = new Set(initialHidden);
        const multiplierMap = new Map(Object.entries(initialMultipliers));
        const tickerColorMap = new Map(Object.entries(initialTickerColors));
        const priceScaleAssignmentMap = new Map(Object.entries(initialPriceScaleAssignments));
        const priceSeriesMap = new Map();
        const volSeriesMap = new Map();
        const volumeSeriesMap = new Map();
        const revenueSeriesMap = new Map();
        const fundamentalSeriesMap = new Map();
        const rawPriceMap = new Map();
        const latestRebasedData = {};

        // Store state on card element
        card._selectedTickers = selectedTickers;
        card._showDiff = showDiff;
        card._showAvg = showAvg;
        card._showVol = showVolPane;
        card._showVolume = showVolumePane;
        card._showRevenue = showRevenuePane;
        card._showFundamentalsPane = showFundamentalsPane;
        card._fundamentalsMetrics = fundamentalsMetrics;
        card._useRaw = useRaw;
        card._multiplierMap = multiplierMap;
        card._tickerColorMap = tickerColorMap;
        card._priceScaleAssignmentMap = priceScaleAssignmentMap;
        card._hiddenTickers = hiddenTickers;
        card._visibleRange = initialRange;
        card._title = initialTitle;
        card._lastLabelVisible = lastLabelVisible;
        card._lastTickerVisible = lastTickerVisible;
        card._showZeroLine = showZeroLine;
        card._showFixedLegend = showFixedLegend;
        card._showLegendTickers = showLegendTickers;
        card._fixedLegendPos = initialFixedLegendPos;
        card._fixedLegendSize = initialFixedLegendSize;
        card._height = initialHeight;
        card._fontSize = initialFontSize;
        card._volumePaneStretchFactor = 1.0;  // Default stretch factor for volume pane
        card._showNotes = initialShowNotes;
        card._notes = initialNotes;
        card._manualInterval = initialManualInterval;  // Manual interval override (null = auto)
        card._decimalPrecision = initialDecimalPrecision;  // Decimal precision for price display
        // Initialize notes UI
        if (notesSection && notesTextarea) {
            notesSection.style.display = initialShowNotes ? 'block' : 'none';
            notesTextarea.value = initialNotes;
        }

        // Helper to get current button states for updateButtonStates()
        function getButtonStates() {
            return {
                showDiff,
                showVol: showVolPane,
                showVolume: showVolumePane,
                showRevenue: showRevenuePane,
                showFundamentalsPane,
                useRaw,
                showAvg,
                lastLabelVisible,
                lastTickerVisible,
                showZeroLine,
                showFixedLegend,
                showLegendTickers
            };
        }

        // Get current font size with fallback
        function getCurrentFontSize() {
            return card._fontSize || window.ChartConfig.UI.FONT_DEFAULT || 12;
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
         * Save visible range, destroy chart, clear all panes/series, and replot.
         * Used by pane toggle handlers to ensure clean chart recreation.
         */
        function destroyChartAndReplot() {
            // Save current visible range
            if (chart && chart.timeScale) {
                try {
                    const visible = chart.timeScale().getVisibleRange();
                    if (visible && visible.from && visible.to) {
                        card._visibleRange = { from: Math.round(visible.from), to: Math.round(visible.to) };
                    }
                } catch (_) { }
            }

            // Destroy chart and clear all panes/series
            if (chart) {
                try {
                    if (crosshairHandler && chart.unsubscribeCrosshairMove) {
                        chart.unsubscribeCrosshairMove(crosshairHandler);
                    }
                } catch (_) { }
                try {
                    if (rangeSaveHandler && chart.timeScale && typeof chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                        chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                    }
                } catch (_) { }
                try {
                    chart.remove();
                } catch (_) { }
                chart = null;
                volPane = null;
                volumePane = null;
                revenuePane = null;
                fundamentalsPane = null;
                priceSeriesMap.clear();
                volSeriesMap.clear();
                volumeSeriesMap.clear();
                revenueSeriesMap.clear();
                fundamentalSeriesMap.clear();
            }

            // Skip automatic range application and replot
            skipRangeApplication = true;
            saveCards();
            plot();
        }

        function applyResize(newH) {
            if (!chartBox) return;
            chartBox.style.height = `${newH}px`;
            if (chart && typeof chart.resize === 'function') {
                const width = chartBox.clientWidth || chartBox.getBoundingClientRect().width || 800;
                console.log(`[Card:${cardId}] Resizing chart to ${width} x ${newH}`);
                try { chart.resize(width, newH); } catch (e) { console.warn(`[Card:${cardId}] chart.resize failed`, e); }
            }
        }

        function setHeight(newHeight) {
            const height = window.ChartUtils.clamp(parseInt(newHeight), HEIGHT_MIN, HEIGHT_MAX);
            console.log(`[Card:${cardId}] Height change to ${height}`);
            card._height = height;
            applyResize(height);
            // Update slider and display
            if (heightSlider) heightSlider.value = height;
            if (heightValue) heightValue.textContent = height;
            saveCards();
        }
        // Height slider event handler
        window.ChartUtils.bindSliderControl(heightSlider, heightValue, {
            initialValue: card._height || initialHeight,
            onInput: (v) => { card._height = v; applyResize(v); }
        });

        // Volume pane height adjustment
        function setVolumePaneHeight(newFactor) {
            const factor = window.ChartUtils.clamp(parseFloat(newFactor), 0.5, 3.0);
            console.log(`[Card:${cardId}] Volume pane stretch factor change to ${factor}`);
            card._volumePaneStretchFactor = factor;

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
            initialValue: card._volumePaneStretchFactor || 1.0,
            onInput: (v) => {
                card._volumePaneStretchFactor = v;
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
            card._fontSize = size;
            applyFont(size);
            // Update slider and display
            if (fontSlider) fontSlider.value = size;
            if (fontValue) fontValue.textContent = size;
            saveCards();
        }
        // Font slider event handler
        window.ChartUtils.bindSliderControl(fontSlider, fontValue, {
            initialValue: card._fontSize || (window.ChartConfig?.UI?.FONT_DEFAULT || 12),
            onInput: (v) => { card._fontSize = v; applyFont(v); }
        });

        // Decimals slider event handler
        function updatePriceFormat(precision) {
            if (chart && chart.priceScale) {
                const priceFormat = window.ChartUtils.createPriceFormatter(useRaw, precision);

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
            initialValue: card._decimalPrecision !== undefined ? card._decimalPrecision : 2,
            onInput: (v) => { card._decimalPrecision = v; updatePriceFormat(v); }
        });

        // Export button handler
        if (exportBtn) {
            exportBtn.addEventListener('click', async () => {
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
            });
        }

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
                if (showAvg && !useRaw) {
                    try {
                        avgSeries = window.ChartSeriesManager.updateAverageSeries(
                            chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, lastLabelVisible
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
            const rangeBefore = card._visibleRange;
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
            if (rangeBefore && !card._skipRangeRestoration) {
                try {
                    chart.timeScale().setVisibleRange(rangeBefore);
                    console.log(`[Plot] Final range restoration after ${paneName} operations`);
                } catch (_) { }
            } else if (card._skipRangeRestoration) {
                console.log(`[Plot] Skipping ${paneName} range restoration (manual range was set)`);
                if (paneName === 'fundamentals') {
                    card._skipRangeRestoration = false;  // Reset flag after last pane
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
            if (!chart) {
                // Set price format based on mode and decimal precision
                const precision = card._decimalPrecision !== undefined ? card._decimalPrecision : 2;
                const priceFormat = window.ChartUtils.createPriceFormatter(useRaw, precision);

                chart = LightweightCharts.createChart(chartBox, {
                    layout: { background: { type: 'solid', color: '#ffffff' }, textColor: '#333', fontSize: (card._fontSize || (window.ChartConfig?.UI?.FONT_DEFAULT || 12)) },
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
                applyResize(card._height || initialHeight);

                // Apply rightOffset dynamically (in case chart already exists)
                chart.applyOptions({
                    timeScale: { rightOffset: 3 }
                });

                // Add legend
                const legendEl = window.ChartLegend.createLegendElement(chartBox);
                crosshairHandler = window.ChartLegend.subscribeToCrosshair(chart, legendEl, {
                    useRaw,
                    priceSeriesMap,
                    hiddenTickers,
                    tickerColorMap,
                    selectedTickers,
                    rawPriceMap,
                    latestRebasedData,
                    getName: (t) => nameCache[t]
                });

                // Subscribe to crosshair for fixed legend dual mode
                let fixedLegendCrosshairHandler = null;
                if (chart) {
                    fixedLegendCrosshairHandler = (param) => {
                        if (!showFixedLegend || !fixedLegendEl) return;

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
                                const dataArray = useRaw ? rawPriceMap.get(ticker) : latestRebasedData[ticker];
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
                                    useRaw,
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
            if (!showVolPane && volPane) {
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
                if (card._manualInterval && card._manualInterval !== 'auto') {
                    interval = card._manualInterval;
                    console.log(`Using manual interval: ${interval}`);
                } else if (card._visibleRange) {
                    const rangeSeconds = card._visibleRange.to - card._visibleRange.from;
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
                const data = await window.DataFetcher.getData(tickerList, 5475, interval);

                if (!data || Object.keys(data).length === 0) {
                    console.warn('No data received');
                    // Don't show toast here - getData() already showed error if it was API failure
                    // Empty response could be legitimate (ticker not found in DB)
                    return;
                }

                // Process each ticker, skip hidden ones
                for (const ticker of tickerList) {
                    if (hiddenTickers.has(ticker)) continue;
                    const tickerData = data[ticker];
                    if (!tickerData) continue;

                    // API already returns objects with time (in seconds) and value properties
                    const rawData = tickerData.filter(d => d.value != null);
                    rawPriceMap.set(ticker, rawData);

                    const color = tickerColorMap.get(ticker);
                    const mult = multiplierMap.get(ticker) || 1;

                    const plotData = useRaw ? rawData :
                        window.ChartSeriesManager.rebaseData(rawData, mult);

                    if (!useRaw) {
                        latestRebasedData[ticker] = plotData;
                    }

                    const precision = card._decimalPrecision !== undefined ? card._decimalPrecision : 2;
                    const priceScaleId = priceScaleAssignmentMap.get(ticker) || 'right';
                    window.ChartSeriesManager.createOrUpdateSeries(
                        chart, ticker, plotData, color, priceSeriesMap, lastLabelVisible, !useRaw, precision, priceScaleId
                    );
                }

                // Volume pane
                if (showVolPane) {
                    await withRangePreservation('volume', async () => {
                        volPane = window.ChartVolumeManager.createVolumePaneIfNeeded(chart, volPane, card._visibleRange);

                        for (const ticker of tickerList) {
                            if (hiddenTickers.has(ticker)) continue;

                            const rawData = rawPriceMap.get(ticker);
                            if (!rawData || rawData.length < 2) {
                                console.warn(`[Plot] Insufficient data for volume calculation: ${ticker}`);
                                continue;
                            }

                            const volData = window.ChartVolumeManager.calculateVolume(rawData, VOL_WINDOW);
                            console.log(`[Plot] Calculated ${volData.length} volume points for ${ticker}`);

                            if (volData.length === 0) {
                                console.warn(`[Plot] No volume data calculated for ${ticker}`);
                                continue;
                            }

                            const color = tickerColorMap.get(ticker);

                            try {
                                window.ChartVolumeManager.addVolumeSeries(
                                    chart, volPane, ticker, volData, color, volSeriesMap, lastLabelVisible
                                );
                                console.log(`[Plot] Successfully added volume series for ${ticker}`);
                            } catch (e) {
                                console.error(`[Plot] Failed to add volume series for ${ticker}:`, e);
                            }
                        }
                    });
                }

                // Trading Volume pane
                if (showVolumePane) {
                    await withRangePreservation('trading volume', async () => {
                        // Create volume pane
                        if (!volumePane) {
                            const stretchFactor = card._volumePaneStretchFactor || 1.0;
                            console.log(`[VolumePane] Creating pane with stretch factor: ${stretchFactor}`);
                            volumePane = chart.addPane();

                            // Set stretch factor to make this pane taller (default is 1.0)
                            // Higher values = taller pane relative to other panes
                            if (typeof volumePane.setStretchFactor === 'function') {
                                volumePane.setStretchFactor(stretchFactor);
                                console.log(`[VolumePane] Set stretch factor to ${stretchFactor}`);
                            } else {
                                console.warn('[VolumePane] setStretchFactor not available');
                            }

                            // Restore range if provided
                            const rangeBeforeVolume = card._visibleRange;
                            if (rangeBeforeVolume && rangeBeforeVolume.from && rangeBeforeVolume.to) {
                                try {
                                    chart.timeScale().setVisibleRange(rangeBeforeVolume);
                                    console.log('[VolumePane] Restored range after pane creation: from ' + rangeBeforeVolume.from + ', to ' + rangeBeforeVolume.to);
                                } catch (e) {
                                    console.warn('[VolumePane] Could not restore range:', e);
                                }
                            }
                        }

                        // Fetch and plot trading volume data for each ticker
                        const volumePromises = tickerList
                            .filter(ticker => !hiddenTickers.has(ticker))
                            .map(async (ticker) => {
                                try {
                                    console.log(`[VolumePane] Fetching trading volume data for ${ticker}`);

                                    // Fetch volume data from API
                                    const volumeData = await window.DataFetcher.getVolumeData([ticker]);

                                    if (!volumeData || !volumeData[ticker]) {
                                        console.warn(`[VolumePane] No volume data received for ${ticker}`);
                                        return;
                                    }

                                    const tickerVolumeData = volumeData[ticker];

                                    // API returns array of {time, value} objects, similar to price data
                                    if (!Array.isArray(tickerVolumeData) || tickerVolumeData.length === 0) {
                                        console.warn(`[VolumePane] Invalid or empty volume data for ${ticker}`);
                                        return;
                                    }

                                    // Filter out null values
                                    const formattedData = tickerVolumeData.filter(d => d.value != null);

                                    const color = tickerColorMap.get(ticker) || '#000000';

                                    // Create or update volume series
                                    let volumeSeries = volumeSeriesMap.get(ticker);
                                    if (!volumeSeries) {
                                        console.log(`[VolumePane] Creating new volume series for ${ticker}`);
                                        if (volumePane && chart) {
                                            volumeSeries = volumePane.addSeries(LightweightCharts.LineSeries, {
                                                color: color,
                                                lineWidth: 1,
                                                priceLineVisible: false,
                                                lastValueVisible: lastLabelVisible,
                                                priceScaleId: 'right',
                                                priceFormat: {
                                                    type: 'volume'
                                                }
                                            });

                                            // Configure the price scale for logarithmic mode with better visibility
                                            volumeSeries.priceScale().applyOptions({
                                                mode: LightweightCharts.PriceScaleMode.Logarithmic,
                                                autoScale: true,
                                                scaleMargins: {
                                                    top: 0.1,
                                                    bottom: 0.1
                                                }
                                            });

                                            volumeSeriesMap.set(ticker, volumeSeries);
                                            console.log(`[VolumePane] Series created for ${ticker} with logarithmic scale`);
                                        } else {
                                            console.error(`[VolumePane] volumePane or chart is not available`);
                                            return;
                                        }
                                    } else {
                                        console.log(`[VolumePane] Updating existing volume series for ${ticker}`);
                                        volumeSeries.applyOptions({ color: color, lastValueVisible: lastLabelVisible });
                                    }

                                    volumeSeries.setData(formattedData);
                                    console.log(`[VolumePane] Data set successfully for ${ticker}, ${formattedData.length} points`);
                                } catch (error) {
                                    console.error(`[VolumePane] Failed to fetch/plot volume for ${ticker}:`, error);
                                }
                            });

                        // Wait for all volume data to be fetched and plotted
                        await Promise.all(volumePromises);
                    });
                }

                // Revenue pane
                if (showRevenuePane) {
                    await withRangePreservation('revenue', async () => {
                        // Create revenue pane
                        if (!revenuePane) {
                            const stretchFactor = card._revenuePaneStretchFactor || 1.0;
                            console.log(`[RevenuePane] Creating pane with stretch factor: ${stretchFactor}`);
                            revenuePane = chart.addPane();

                            // Set stretch factor to make this pane taller
                            if (typeof revenuePane.setStretchFactor === 'function') {
                                revenuePane.setStretchFactor(stretchFactor);
                                console.log(`[RevenuePane] Set stretch factor to ${stretchFactor}`);
                            } else {
                                console.warn('[RevenuePane] setStretchFactor not available');
                            }

                            // Restore range if provided
                            const rangeBeforeRevenue = card._visibleRange;
                            if (rangeBeforeRevenue && rangeBeforeRevenue.from && rangeBeforeRevenue.to) {
                                try {
                                    chart.timeScale().setVisibleRange(rangeBeforeRevenue);
                                    console.log('[RevenuePane] Restored range after pane creation: from ' + rangeBeforeRevenue.from + ', to ' + rangeBeforeRevenue.to);
                                } catch (e) {
                                    console.warn('[RevenuePane] Could not restore range:', e);
                                }
                            }
                        }

                        // Fetch and plot revenue data for each ticker
                        const revenuePromises = tickerList
                            .filter(ticker => !hiddenTickers.has(ticker))
                            .map(async (ticker) => {
                                try {
                                    console.log(`[RevenuePane] Fetching revenue data for ${ticker}`);

                                    // Fetch revenue data from API
                                    const response = await fetch(`/api/revenue?tickers=${ticker}`);
                                    if (!response.ok) {
                                        console.warn(`[RevenuePane] Failed to fetch revenue for ${ticker}: ${response.status}`);
                                        return;
                                    }

                                    const revenueData = await response.json();
                                    if (!revenueData || !revenueData[ticker]) {
                                        console.warn(`[RevenuePane] No revenue data received for ${ticker}`);
                                        return;
                                    }

                                    const tickerRevenueData = revenueData[ticker];

                                    // API returns array of {time, value} objects
                                    if (!Array.isArray(tickerRevenueData) || tickerRevenueData.length === 0) {
                                        console.warn(`[RevenuePane] Invalid or empty revenue data for ${ticker}`);
                                        return;
                                    }

                                    // Filter out null values
                                    const formattedData = tickerRevenueData.filter(d => d.value != null);

                                    const color = tickerColorMap.get(ticker) || '#000000';

                                    // Create or update revenue series
                                    let revenueSeries = revenueSeriesMap.get(ticker);
                                    if (!revenueSeries) {
                                        console.log(`[RevenuePane] Creating new revenue series for ${ticker}`);
                                        if (revenuePane && chart) {
                                            revenueSeries = revenuePane.addSeries(LightweightCharts.LineSeries, {
                                                color: color,
                                                lineWidth: 2,
                                                priceLineVisible: false,
                                                lastValueVisible: lastLabelVisible,
                                                priceScaleId: 'right',
                                                priceFormat: {
                                                    type: 'volume'
                                                }
                                            });

                                            // Configure the price scale for logarithmic mode
                                            revenueSeries.priceScale().applyOptions({
                                                mode: LightweightCharts.PriceScaleMode.Logarithmic,
                                                autoScale: true,
                                                scaleMargins: {
                                                    top: 0.1,
                                                    bottom: 0.1
                                                }
                                            });

                                            revenueSeriesMap.set(ticker, revenueSeries);
                                            console.log(`[RevenuePane] Series created for ${ticker} with logarithmic scale`);
                                        } else {
                                            console.error(`[RevenuePane] revenuePane or chart is not available`);
                                            return;
                                        }
                                    } else {
                                        console.log(`[RevenuePane] Updating existing revenue series for ${ticker}`);
                                        revenueSeries.applyOptions({ color: color, lastValueVisible: lastLabelVisible });
                                    }

                                    revenueSeries.setData(formattedData);
                                    console.log(`[RevenuePane] Data set successfully for ${ticker}, ${formattedData.length} quarters`);
                                } catch (error) {
                                    console.error(`[RevenuePane] Failed to fetch/plot revenue for ${ticker}:`, error);
                                }
                            });

                        // Wait for all revenue data to be fetched and plotted
                        await Promise.all(revenuePromises);
                    });
                }

                // Fundamentals pane
                if (showFundamentalsPane && window.FundamentalsPane) {
                    await withRangePreservation('fundamentals', async () => {
                        // Create fundamentals pane
                        if (!fundamentalsPane) {
                            const stretchFactor = card._fundamentalsPaneStretchFactor || 1.0;
                            console.log(`[FundamentalsPane] Creating pane with stretch factor: ${stretchFactor}`);
                            fundamentalsPane = chart.addPane();

                            // Set stretch factor to make this pane taller
                            if (typeof fundamentalsPane.setStretchFactor === 'function') {
                                fundamentalsPane.setStretchFactor(stretchFactor);
                                console.log(`[FundamentalsPane] Set stretch factor to ${stretchFactor}`);
                            } else {
                                console.warn('[FundamentalsPane] setStretchFactor not available');
                            }

                            // Restore range if provided
                            const rangeBeforeFundamentals = card._visibleRange;
                            if (rangeBeforeFundamentals && rangeBeforeFundamentals.from && rangeBeforeFundamentals.to) {
                                try {
                                    chart.timeScale().setVisibleRange(rangeBeforeFundamentals);
                                    console.log('[FundamentalsPane] Restored range after pane creation');
                                } catch (e) {
                                    console.warn('[FundamentalsPane] Could not restore range:', e);
                                }
                            }
                        }

                        // Plot fundamentals using the FundamentalsPane module
                        try {
                            const hiddenTickersMap = {};
                            hiddenTickers.forEach(ticker => { hiddenTickersMap[ticker] = true; });

                            await window.FundamentalsPane.plot(
                                fundamentalsPane,
                                tickerList,
                                fundamentalsMetrics,
                                fundamentalSeriesMap,
                                hiddenTickersMap
                            );
                            console.log(`[FundamentalsPane] Plotted ${tickerList.length} tickers with ${fundamentalsMetrics.length} metrics`);
                        } catch (error) {
                            console.error('[FundamentalsPane] Error plotting fundamentals:', error);
                        }
                    });
                }

                // Average series
                if (showAvg && !useRaw) {
                    avgSeries = window.ChartSeriesManager.updateAverageSeries(
                        chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, lastLabelVisible
                    );
                }

                // Update ticker labels
                if (tickerLabelsContainer) {
                    const currentFontSize = getCurrentFontSize();
                    const tickerData = useRaw ? rawPriceMap : latestRebasedData;

                    // Initial update (only for raw mode or if rebased data exists)
                    if (useRaw || Object.keys(latestRebasedData).length > 0) {
                        window.ChartTickerLabels.updateAllLabels(
                            tickerLabelsContainer, priceSeriesMap, tickerColorMap, hiddenTickers,
                            tickerData, chart, lastTickerVisible, currentFontSize
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
                        if (useRaw && tickerLabelsContainer && chart) {
                            // Raw mode: just update positions with same data
                            setTimeout(() => {
                                const currentFontSize = getCurrentFontSize();
                                window.ChartTickerLabels.updateAllLabels(
                                    tickerLabelsContainer, priceSeriesMap, tickerColorMap, hiddenTickers,
                                    rawPriceMap, chart, lastTickerVisible, currentFontSize
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
                        card._visibleRange = { from, to };
                        console.log(`[RangeSave:${cardId}] Visible time range changed => from ${from}, to ${to}`);
                        debouncedSaveCards();
                        // Update fixed legend when range changes
                        if (showFixedLegend) {
                            updateFixedLegend();
                        }
                    }
                };
                chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);

                // Setup range-based rebasing
                if (!useRaw) {
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
                        showAvg,
                        updateAverageSeries: () => {
                            if (showAvg) {
                                avgSeries = window.ChartSeriesManager.updateAverageSeries(
                                    chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, lastLabelVisible
                                );
                            }
                        },
                        onRebaseComplete: () => {
                            // Update ticker labels after rebasing completes
                            if (tickerLabelsContainer) {
                                const currentFontSize = getCurrentFontSize();
                                window.ChartTickerLabels.updateAllLabels(
                                    tickerLabelsContainer, priceSeriesMap, tickerColorMap, hiddenTickers,
                                    latestRebasedData, chart, lastTickerVisible, currentFontSize
                                );
                            }
                        },
                        useRaw: () => useRaw  // Pass as function to get current value
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
                    const saved = card._visibleRange || initialRange;
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
                            card._visibleRange = dataRange;
                            saveCards();
                        } else {
                            applyRange(saved, 'saved');
                        }
                    } else if (dataRange) {
                        applyRange(dataRange, 'data');
                        card._visibleRange = dataRange;
                        saveCards();
                    } else {
                        chart.timeScale().fitContent();
                    }
                } else {
                    // Manual range application when skipping automatic logic
                    console.log(`[RangeApply:${cardId}] Skipping automatic range application`);
                    const saved = card._visibleRange;
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
                    if (showFixedLegend && !fixedLegendEl) {
                        console.log(`[Card:${cardId}] Restoring fixed legend after plot`);
                        fixedLegendEl = window.ChartFixedLegend.createFixedLegend(chartBox, {
                            initialX: card._fixedLegendPos?.x || 10,
                            initialY: card._fixedLegendPos?.y || 10,
                            initialWidth: card._fixedLegendSize?.width || null,
                            initialHeight: card._fixedLegendSize?.height || null
                        });

                        // Setup state change handler
                        fixedLegendEl._onStateChange = (changes) => {
                            if (changes.x !== undefined || changes.y !== undefined) {
                                card._fixedLegendPos = {
                                    x: changes.x !== undefined ? changes.x : card._fixedLegendPos?.x || 10,
                                    y: changes.y !== undefined ? changes.y : card._fixedLegendPos?.y || 10
                                };
                            }
                            if (changes.width !== undefined || changes.height !== undefined) {
                                card._fixedLegendSize = {
                                    width: changes.width !== undefined ? changes.width : card._fixedLegendSize?.width || null,
                                    height: changes.height !== undefined ? changes.height : card._fixedLegendSize?.height || null
                                };
                            }
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

        // Event handlers
        addBtn.addEventListener('click', addTicker);
        tickerInput.addEventListener('keypress', e => {
            if (e.key === 'Enter') addTicker();
        });

        plotBtn.addEventListener('click', plot);

        // Manual fit button: fit chart to full data range and persist
        if (fitBtn) {
            fitBtn.addEventListener('click', () => {
                if (!chart) return;
                const dataRange = getCurrentDataRange();
                if (dataRange) {
                    try {
                        chart.timeScale().setVisibleRange(dataRange);
                        card._visibleRange = dataRange;
                        saveCards();
                    } catch (e) {
                        chart.timeScale().fitContent();
                    }
                } else {
                    chart.timeScale().fitContent();
                }
            });
        }

        toggleDiffBtn.addEventListener('click', () => {
            showDiff = !showDiff;
            card._showDiff = showDiff;
            toggleDiffBtn.textContent = showDiff ? 'Hide Diff Pane' : 'Show Diff Pane';
            saveCards();
            // Diff pane implementation would go here
        });

        toggleVolBtn.addEventListener('click', () => {
            showVolPane = !showVolPane;
            card._showVol = showVolPane;
            toggleVolBtn.textContent = showVolPane ? 'Hide Vol (σ) Pane' : 'Show Vol (σ) Pane';
            destroyChartAndReplot();
        });

        toggleVolumeBtn.addEventListener('click', () => {
            showVolumePane = !showVolumePane;
            card._showVolume = showVolumePane;
            toggleVolumeBtn.textContent = showVolumePane ? 'Hide Volume Pane' : 'Show Volume Pane';
            destroyChartAndReplot();
        });

        toggleRevenueBtn.addEventListener('click', () => {
            showRevenuePane = !showRevenuePane;
            card._showRevenue = showRevenuePane;
            toggleRevenueBtn.textContent = showRevenuePane ? 'Hide Revenue Pane' : 'Show Revenue Pane';
            destroyChartAndReplot();
        });

        // Toggle Fundamentals Pane button
        toggleFundamentalsPaneBtn.addEventListener('click', () => {
            showFundamentalsPane = !showFundamentalsPane;
            card._showFundamentalsPane = showFundamentalsPane;
            toggleFundamentalsPaneBtn.textContent = showFundamentalsPane ? 'Hide Fundamentals Pane' : 'Show Fundamentals Pane';

            // Show/hide metric buttons based on pane state
            const metricButtonsDisplay = showFundamentalsPane ? 'inline-block' : 'none';
            if (toggleRevenueMetricBtn) toggleRevenueMetricBtn.style.display = metricButtonsDisplay;
            if (toggleNetIncomeMetricBtn) toggleNetIncomeMetricBtn.style.display = metricButtonsDisplay;
            if (toggleEpsMetricBtn) toggleEpsMetricBtn.style.display = metricButtonsDisplay;
            if (toggleFcfMetricBtn) toggleFcfMetricBtn.style.display = metricButtonsDisplay;

            destroyChartAndReplot();
        });

        // Helper function to update metric button states
        function updateMetricButtonStates() {
            if (toggleRevenueMetricBtn) {
                toggleRevenueMetricBtn.style.fontWeight = fundamentalsMetrics.includes('revenue') ? 'bold' : 'normal';
                toggleRevenueMetricBtn.style.opacity = fundamentalsMetrics.includes('revenue') ? '1' : '0.5';
            }
            if (toggleNetIncomeMetricBtn) {
                toggleNetIncomeMetricBtn.style.fontWeight = fundamentalsMetrics.includes('netincome') ? 'bold' : 'normal';
                toggleNetIncomeMetricBtn.style.opacity = fundamentalsMetrics.includes('netincome') ? '1' : '0.5';
            }
            if (toggleEpsMetricBtn) {
                toggleEpsMetricBtn.style.fontWeight = fundamentalsMetrics.includes('eps') ? 'bold' : 'normal';
                toggleEpsMetricBtn.style.opacity = fundamentalsMetrics.includes('eps') ? '1' : '0.5';
            }
            if (toggleFcfMetricBtn) {
                toggleFcfMetricBtn.style.fontWeight = fundamentalsMetrics.includes('fcf') ? 'bold' : 'normal';
                toggleFcfMetricBtn.style.opacity = fundamentalsMetrics.includes('fcf') ? '1' : '0.5';
            }
        }

        // Initialize metric button visibility and states
        if (showFundamentalsPane) {
            if (toggleRevenueMetricBtn) toggleRevenueMetricBtn.style.display = 'inline-block';
            if (toggleNetIncomeMetricBtn) toggleNetIncomeMetricBtn.style.display = 'inline-block';
            if (toggleEpsMetricBtn) toggleEpsMetricBtn.style.display = 'inline-block';
            if (toggleFcfMetricBtn) toggleFcfMetricBtn.style.display = 'inline-block';
        }
        updateMetricButtonStates();

        // Metric toggle helper
        function toggleMetric(metricName) {
            const index = fundamentalsMetrics.indexOf(metricName);
            if (index > -1) {
                fundamentalsMetrics.splice(index, 1);
            } else {
                fundamentalsMetrics.push(metricName);
            }
            card._fundamentalsMetrics = fundamentalsMetrics;
            updateMetricButtonStates();
            saveCards();
            if (showFundamentalsPane) plot();
        }

        // Metric toggle buttons
        if (toggleRevenueMetricBtn) toggleRevenueMetricBtn.addEventListener('click', () => toggleMetric('revenue'));
        if (toggleNetIncomeMetricBtn) toggleNetIncomeMetricBtn.addEventListener('click', () => toggleMetric('netincome'));
        if (toggleEpsMetricBtn) toggleEpsMetricBtn.addEventListener('click', () => toggleMetric('eps'));
        if (toggleFcfMetricBtn) toggleFcfMetricBtn.addEventListener('click', () => toggleMetric('fcf'));

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

        toggleRawBtn.addEventListener('click', () => {
            useRaw = !useRaw;
            card._useRaw = useRaw;
            toggleRawBtn.textContent = useRaw ? 'Show % Basis' : 'Show Raw';

            // Update price scale format immediately
            if (chart && chart.priceScale) {
                const precision = card._decimalPrecision !== undefined ? card._decimalPrecision : 2;
                const priceFormat = useRaw
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

            saveCards();
            plot();
            // Update zero line after mode change
            setTimeout(() => updateZeroLine(), 100);
        });

        // Toggle last value label visibility
        if (toggleLastLabelBtn) {
            toggleLastLabelBtn.addEventListener('click', () => {
                lastLabelVisible = !lastLabelVisible;
                card._lastLabelVisible = lastLabelVisible;
                console.log(`[Card:${cardId}] Last value label ${lastLabelVisible ? 'enabled' : 'disabled'}`);
                window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());
                // Apply to all existing series
                priceSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: lastLabelVisible }));
                if (avgSeries) avgSeries.applyOptions({ lastValueVisible: lastLabelVisible });
                if (volPane && volSeriesMap) {
                    volSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: lastLabelVisible }));
                }
                // Apply to volume pane series (trading volume)
                if (volumePane && volumeSeriesMap) {
                    volumeSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: lastLabelVisible }));
                }
                // Apply to revenue pane series
                if (revenuePane && revenueSeriesMap) {
                    revenueSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: lastLabelVisible }));
                }
                saveCards();
            });
        }

        // Toggle last ticker label visibility
        if (toggleLastTickerBtn) {
            toggleLastTickerBtn.addEventListener('click', () => {
                lastTickerVisible = !lastTickerVisible;
                card._lastTickerVisible = lastTickerVisible;
                console.log(`[Card:${cardId}] Last ticker label ${lastTickerVisible ? 'enabled' : 'disabled'}`);
                window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());
                // Update ticker labels visibility
                if (tickerLabelsContainer) {
                    window.ChartTickerLabels.setLabelsVisibility(tickerLabelsContainer, lastTickerVisible);
                }
                saveCards();
            });
        }

        // Reshuffle colors button
        if (reshuffleColorsBtn) {
            reshuffleColorsBtn.addEventListener('click', () => {
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
                        useRaw ? rawPriceMap : latestRebasedData, chart, lastTickerVisible,
                        getCurrentFontSize()
                    );
                }

                saveCards();
            });
        }

        // Toggle zero line visibility
        if (toggleZeroLineBtn) {
            toggleZeroLineBtn.addEventListener('click', () => {
                showZeroLine = !showZeroLine;
                card._showZeroLine = showZeroLine;
                console.log(`[Card:${cardId}] Zero line ${showZeroLine ? 'enabled' : 'disabled'}`);

                updateZeroLine();

                window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());
                saveCards();
            });
        }

        // Function to update zero line visibility and data
        function updateZeroLine() {
            if (!chart) return;

            if (showZeroLine) {
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
                const zeroValue = useRaw ? 0 : 100; // 0 for raw prices, 100 for percentage (rebased to 100)

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

        toggleAvgBtn.addEventListener('click', () => {
            showAvg = !showAvg;
            card._showAvg = showAvg;
            toggleAvgBtn.textContent = showAvg ? 'Hide Avg' : 'Show Avg';
            saveCards();
            if (showAvg && !useRaw) {
                avgSeries = window.ChartSeriesManager.updateAverageSeries(
                    chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, lastLabelVisible
                );
            } else if (avgSeries) {
                chart.removeSeries(avgSeries);
                avgSeries = null;
            }
        });

        // Toggle fixed legend visibility
        if (toggleFixedLegendBtn) {
            toggleFixedLegendBtn.addEventListener('click', () => {
                showFixedLegend = !showFixedLegend;
                card._showFixedLegend = showFixedLegend;
                console.log(`[Card:${cardId}] Fixed legend ${showFixedLegend ? 'enabled' : 'disabled'}`);

                if (showFixedLegend) {
                    // Create fixed legend if it doesn't exist
                    if (!fixedLegendEl) {
                        fixedLegendEl = window.ChartFixedLegend.createFixedLegend(chartBox, {
                            initialX: card._fixedLegendPos?.x || 10,
                            initialY: card._fixedLegendPos?.y || 10,
                            initialWidth: card._fixedLegendSize?.width || null,
                            initialHeight: card._fixedLegendSize?.height || null
                        });

                        // Setup state change handler
                        fixedLegendEl._onStateChange = (changes) => {
                            if (changes.x !== undefined || changes.y !== undefined) {
                                card._fixedLegendPos = {
                                    x: changes.x !== undefined ? changes.x : card._fixedLegendPos?.x || 10,
                                    y: changes.y !== undefined ? changes.y : card._fixedLegendPos?.y || 10
                                };
                            }
                            if (changes.width !== undefined || changes.height !== undefined) {
                                card._fixedLegendSize = {
                                    width: changes.width !== undefined ? changes.width : card._fixedLegendSize?.width || null,
                                    height: changes.height !== undefined ? changes.height : card._fixedLegendSize?.height || null
                                };
                            }
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
                saveCards();
            });
        }

        // Toggle Legend Tickers
        if (toggleLegendTickersBtn) {
            toggleLegendTickersBtn.addEventListener('click', () => {
                showLegendTickers = !showLegendTickers;
                card._showLegendTickers = showLegendTickers;
                console.log(`[Card:${cardId}] Legend tickers ${showLegendTickers ? 'enabled' : 'disabled'}`);

                // Update fixed legend to reflect new setting
                if (showFixedLegend && fixedLegendEl) {
                    updateFixedLegend();
                }

                window.ChartDomBuilder.updateButtonStates(elements, getButtonStates());
                saveCards();
            });
        }

        // Toggle Notes Button
        if (toggleNotesBtn) {
            toggleNotesBtn.addEventListener('click', () => {
                const showNotes = notesSection.style.display !== 'none';
                notesSection.style.display = showNotes ? 'none' : 'block';
                card._showNotes = !showNotes;
                card._notes = notesTextarea.value;

                window.ChartDomBuilder.updateButtonStates(elements, { ...getButtonStates(), showNotes: !showNotes });
                saveCards();
            });

            // Auto-save notes on input
            notesTextarea.addEventListener('input', () => {
                card._notes = notesTextarea.value;
                saveCards();
            });
        }

        // Function to update fixed legend with latest values
        function updateFixedLegend() {
            if (!showFixedLegend || !fixedLegendEl) return;

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
                const dataArray = useRaw ? rawPriceMap.get(ticker) : latestRebasedData[ticker];
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
                useRaw,
                hiddenTickers,
                tickerColorMap,
                getName: (t) => nameCache[t],
                showTickers: showLegendTickers
            });
        }

        if (intervalSelect) {
            // Set initial value if manual interval is set
            if (card._manualInterval) {
                intervalSelect.value = card._manualInterval;
            }

            intervalSelect.addEventListener('change', () => {
                const val = intervalSelect.value;
                card._manualInterval = val === 'auto' ? null : val;
                console.log(`Interval changed to: ${val}`);
                debouncedSaveCards();
                // Replot to fetch data with new interval
                if (selectedTickers.size > 0) {
                    plot();
                }
            });
        }

        if (rangeSelect) {
            rangeSelect.addEventListener('change', () => {
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
                            if (showFundamentalsPane && !earliestTime) {
                                // Use 1996 as earliest for fundamentals (AAPL data goes back to 1996-04-01)
                                earliestTime = Date.UTC(1996, 0, 1) / 1000;
                            }
                        } catch (e) { /* ignore */ }
                    });

                    // If we have fundamental data showing, use 1996 as earliest
                    if (showFundamentalsPane && fundamentalSeriesMap.size > 0) {
                        earliestTime = Date.UTC(1996, 0, 1) / 1000;
                    }

                    // Default to price data earliest if no fundamentals
                    if (!earliestTime) {
                        chart.timeScale().fitContent();
                        const timeScale = chart.timeScale();
                        const visibleRange = timeScale.getVisibleRange();
                        if (visibleRange) {
                            card._visibleRange = { from: visibleRange.from, to: visibleRange.to };
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

                    // Set flag to skip range restoration in plot functions
                    card._skipRangeRestoration = true;

                    // For fundamentals, we know the earliest data is 2005-06-30
                    // Set explicit range to show all fundamental data
                    const fundamentalsEarliest = Date.UTC(2005, 5, 30) / 1000;  // June 30, 2005
                    const from = fundamentalsEarliest;
                    const to = Math.floor(Date.now() / 1000);

                    console.log(`[RangeSelect] Setting explicit range from ${new Date(from * 1000).toISOString()} to ${new Date(to * 1000).toISOString()}`);

                    // Update card state
                    card._visibleRange = { from, to };

                    // Set the range
                    chart.timeScale().setVisibleRange({ from, to });

                    // Verify what range was actually set
                    setTimeout(() => {
                        const actualRange = chart.timeScale().getVisibleRange();
                        if (actualRange) {
                            console.log(`[RangeSelect] Actual visible range after setting: from ${new Date(actualRange.from * 1000).toISOString()} to ${new Date(actualRange.to * 1000).toISOString()}`);
                            // Update with actual range if different
                            card._visibleRange = { from: actualRange.from, to: actualRange.to };
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

                // Update card state FIRST
                card._visibleRange = { from, to };

                // Then set the visual range
                chart.timeScale().setVisibleRange({ from, to });

                saveCards();

                // Resubscribe to range changes
                if (rangeSaveHandler) {
                    try {
                        chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);
                    } catch (_) { }
                }
            });
        }

        if (addChartBtn) {
            addChartBtn.addEventListener('click', () => {
                // Get the current active page wrapper
                let targetWrapper = null;
                if (window.PageManager && window.PageManager.getActivePage) {
                    const activePage = window.PageManager.getActivePage();
                    targetWrapper = window.PageManager.ensurePage(activePage);
                }
                // Create new chart on the active page with default settings (all panes off)
                const newCard = createChartCard('', false, false, false, false, false,
                    {}, [],
                    null, '', true, false, targetWrapper, 500, (window.ChartConfig?.UI?.FONT_DEFAULT || 12));
                saveCards();
                // Insert new card after the current card (within the same page)
                if (card.nextSibling) {
                    (targetWrapper || wrapper).insertBefore(newCard, card.nextSibling);
                }
            });
        }
        if (removeCardBtn) {
            removeCardBtn.addEventListener('click', () => {
                try {
                    // Cleanup global keydown listener for settings panel
                    if (card._escapeHandler) {
                        document.removeEventListener('keydown', card._escapeHandler);
                    }

                    // Remove nav link
                    if (navLink && navLink.parentElement) {
                        navLink.parentElement.removeChild(navLink);
                    }
                    // Unsubscribe handlers and clear series
                    if (chart) {
                        try {
                            if (crosshairHandler && typeof chart.unsubscribeCrosshairMove === 'function') {
                                chart.unsubscribeCrosshairMove(crosshairHandler);
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
                        try { window.ChartSeriesManager.clearAllSeries(chart, priceSeriesMap, volSeriesMap, avgSeries); } catch (_) { }
                        try {
                            if (volPane && chart && typeof chart.removePane === 'function') {
                                chart.removePane(volPane);
                            }
                        } catch (_) { }
                    }
                } catch (e) {
                    console.warn('Cleanup on remove failed:', e);
                }
                // Remove card from DOM and persist
                if (card && card.parentElement) {
                    card.parentElement.removeChild(card);
                }
                saveCards();
            });
        }

        if (titleInput) {
            titleInput.addEventListener('input', () => {
                card._title = titleInput.value;
                if (navLink) {
                    navLink.textContent = titleInput.value || (selectedTickers.size ? Array.from(selectedTickers)[0] : cardId);
                }
                saveCards();
            });
        }

        // Bind chip toggle & multiplier events via helper
        window.CardEventBinder.bindTickerInteractions(
            selectedTickersDiv,
            hiddenTickers,
            multiplierMap,
            () => { card._hiddenTickers = hiddenTickers; },
            () => plot(),
            saveCards,
            () => useRaw
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
                    fetch('http://localhost:5000/api/tickers'),
                    fetch('http://localhost:5000/api/metadata?tickers=ALL')
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
                const resp = await fetch('http://localhost:5000/api/workspace');
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
