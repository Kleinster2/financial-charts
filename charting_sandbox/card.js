        /**
 * Lightweight Charts Card Module (Refactored)
 * Main orchestrator that uses modular components for chart functionality
 */
(() => {
    const WRAPPER_ID = 'charts-wrapper';
    // Use global config
    const config = window.ChartConfig;
    const colors = config.COLORS;
    const VOL_WINDOW = config.VOLUME_WINDOW;
    const PLOT_DEFER_MS = config.DEBOUNCE_MS.PLOT;
    
    let globalCardCounter = 0;
    const nameCache = {};
    

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
            multipliers: Object.fromEntries(card._multiplierMap ? Array.from(card._multiplierMap.entries()) : []),
            hidden: Array.from(card._hiddenTickers || []),
            range: card._visibleRange || null,
            useRaw: card._useRaw || false,
            title: card._title || '',
            lastLabelVisible: card._lastLabelVisible !== false,
            showZeroLine: !!card._showZeroLine,
            showFixedLegend: !!card._showFixedLegend,
            fixedLegendPos: card._fixedLegendPos || { x: 10, y: 10 },
            height: card._height || (() => { try { const el = card.querySelector('.chart-box'); return el ? parseInt(getComputedStyle(el).height, 10) : undefined; } catch(_) { return undefined; } })(),
            fontSize: card._fontSize || ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12)
        }));

        localStorage.setItem(window.ChartConfig.STORAGE_KEYS.CARDS, JSON.stringify(cards));
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
                height: arguments[13] || ((window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MIN_HEIGHT) || 400),
                fontSize: arguments[14] || ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12),
                showFixedLegend: arguments[15] || false,
                fixedLegendPos: arguments[16] || { x: 10, y: 10 }
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
            useRaw: initialUseRaw = false,
            multipliers: initialMultipliers = {},
            hidden: initialHidden = [],
            range: initialRange = null,
            title: initialTitle = '',
            lastLabelVisible: initialLastLabelVisible = true,
            showZeroLine: initialShowZeroLine = false,
            wrapperEl = null,
            height: initialHeight = ((window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MIN_HEIGHT) || 400),
            fontSize: initialFontSize = ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12),
            showFixedLegend: initialShowFixedLegend = false,
            fixedLegendPos: initialFixedLegendPos = { x: 10, y: 10 }
        } = options;
        const wrapper = wrapperEl || document.getElementById(WRAPPER_ID);
        if (!wrapper) {
            console.error('Missing charts wrapper');
            return;
        }

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
        const { tickerInput, addBtn, plotBtn, fitBtn, toggleDiffBtn, toggleVolBtn, toggleVolumeBtn, toggleRawBtn,
                toggleAvgBtn, toggleLastLabelBtn, toggleZeroLineBtn, toggleFixedLegendBtn, heightDownBtn, heightUpBtn, volPaneHeightDownBtn, volPaneHeightUpBtn, fontDownBtn, fontUpBtn, exportBtn, rangeSelect, selectedTickersDiv, chartBox, titleInput, removeCardBtn, addChartBtn } = elements;

        // Initialize state
        let showDiff = initialShowDiff;
        let showAvg = initialShowAvg;
        let showVolPane = initialShowVol;  // Volatility pane
        let showVolumePane = initialShowVolume;  // Trading volume pane
        let useRaw = initialUseRaw;
        let lastLabelVisible = initialLastLabelVisible;
        let showZeroLine = initialShowZeroLine;
        let showFixedLegend = initialShowFixedLegend;
        let chart = null;
        let volPane = null;  // Volatility pane
        let volumePane = null;  // Trading volume pane
        let avgSeries = null;
        let zeroLineSeries = null;
        let fixedLegendEl = null;
        
        let crosshairHandler = null;
        let debouncedRebase = null;
        let diffChart = null;
        let rangeSaveHandler = null;
        let skipRangeApplication = false;  // Flag to skip automatic range application
        const debouncedSaveCards = (window.ChartUtils && window.ChartUtils.debounce) ? window.ChartUtils.debounce(saveCards, 300) : saveCards;

        const selectedTickers = new Set();
        const hiddenTickers = new Set(initialHidden);
        const multiplierMap = new Map(Object.entries(initialMultipliers));
        const tickerColorMap = new Map();
        const priceSeriesMap = new Map();
        const volSeriesMap = new Map();
        const volumeSeriesMap = new Map();
        const rawPriceMap = new Map();
        const latestRebasedData = {};
        let colorIndex = 0;

        // Store state on card element
        card._selectedTickers = selectedTickers;
        card._showDiff = showDiff;
        card._showAvg = showAvg;
        card._showVol = showVolPane;
        card._showVolume = showVolumePane;
        card._useRaw = useRaw;
        card._multiplierMap = multiplierMap;
        card._hiddenTickers = hiddenTickers;
        card._visibleRange = initialRange;
        card._title = initialTitle;
        card._lastLabelVisible = lastLabelVisible;
        card._showZeroLine = showZeroLine;
        card._showFixedLegend = showFixedLegend;
        card._fixedLegendPos = initialFixedLegendPos;
        card._height = initialHeight;
        card._fontSize = initialFontSize;
        card._volumePaneStretchFactor = 1.0;  // Default stretch factor for volume pane

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

        // Height adjust helpers (scoped per card)
        const HEIGHT_MIN = (window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MIN_HEIGHT) || 400;
        const HEIGHT_MAX = (window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MAX_HEIGHT) || 800;
        const HEIGHT_STEP = 50;

        // Font size controls (axis font only)
        const UI = (window.ChartConfig && window.ChartConfig.UI) || {};
        const FONT_MIN = UI.FONT_MIN || 8;
        const FONT_MAX = UI.FONT_MAX || 24;
        const FONT_STEP = UI.FONT_STEP || 1;

        function applyResize(newH) {
            if (!chartBox) return;
            chartBox.style.height = `${newH}px`;
            if (chart && typeof chart.resize === 'function') {
                const width = chartBox.clientWidth || chartBox.getBoundingClientRect().width || 800;
                console.log(`[Card:${cardId}] Resizing chart to ${width} x ${newH}`);
                try { chart.resize(width, newH); } catch (e) { console.warn(`[Card:${cardId}] chart.resize failed`, e); }
            }
        }

        function adjustHeight(delta) {
            const current = card._height || parseInt(getComputedStyle(chartBox).height, 10) || HEIGHT_MIN;
            const next = Math.max(HEIGHT_MIN, Math.min(HEIGHT_MAX, current + delta));
            console.log(`[Card:${cardId}] Height change: ${current} -> ${next} (delta ${delta})`);
            card._height = next;
            applyResize(next);
            saveCards();
        }

        if (heightUpBtn) heightUpBtn.addEventListener('click', () => adjustHeight(+HEIGHT_STEP));
        if (heightDownBtn) heightDownBtn.addEventListener('click', () => adjustHeight(-HEIGHT_STEP));

        // Volume pane height adjustment
        function adjustVolumePaneHeight(delta) {
            const current = card._volumePaneStretchFactor || 1.0;
            const next = Math.max(1.0, Math.min(10.0, current + delta));
            console.log(`[Card:${cardId}] Volume pane stretch factor change: ${current} -> ${next} (delta ${delta})`);
            card._volumePaneStretchFactor = next;

            // Apply to existing volume pane if it exists
            if (volumePane && typeof volumePane.setStretchFactor === 'function') {
                volumePane.setStretchFactor(next);
                console.log(`[Card:${cardId}] Applied stretch factor ${next} to volume pane`);
            }

            saveCards();
        }
        if (volPaneHeightUpBtn) volPaneHeightUpBtn.addEventListener('click', () => adjustVolumePaneHeight(+0.5));
        if (volPaneHeightDownBtn) volPaneHeightDownBtn.addEventListener('click', () => adjustVolumePaneHeight(-0.5));

        function applyFont(newSize) {
            if (chart && typeof chart.applyOptions === 'function') {
                console.log(`[Card:${cardId}] Applying axis font size ${newSize}`);
                try { chart.applyOptions({ layout: { fontSize: newSize } }); } catch (e) { console.warn(`[Card:${cardId}] chart.applyOptions(layout.fontSize) failed`, e); }
            }
        }
        function adjustFont(delta) {
            const current = card._fontSize || (UI.FONT_DEFAULT || 12);
            const next = Math.max(FONT_MIN, Math.min(FONT_MAX, current + delta));
            console.log(`[Card:${cardId}] Font size change: ${current} -> ${next} (delta ${delta})`);
            card._fontSize = next;
            applyFont(next);
            // Disable/enable controls at bounds
            if (fontDownBtn) fontDownBtn.disabled = (next <= FONT_MIN);
            if (fontUpBtn) fontUpBtn.disabled = (next >= FONT_MAX);
            saveCards();
        }
        if (fontUpBtn) fontUpBtn.addEventListener('click', () => adjustFont(+FONT_STEP));
        if (fontDownBtn) fontDownBtn.addEventListener('click', () => adjustFont(-FONT_STEP));
        // Initialize font button disabled state
        if (fontDownBtn) fontDownBtn.disabled = ((card._fontSize || (UI.FONT_DEFAULT || 12)) <= FONT_MIN);
        if (fontUpBtn) fontUpBtn.disabled = ((card._fontSize || (UI.FONT_DEFAULT || 12)) >= FONT_MAX);

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
        window.ChartDomBuilder.updateButtonStates(elements, {
            showDiff, showVol: showVolPane, showVolume: showVolumePane, useRaw, showAvg, lastLabelVisible, showZeroLine, showFixedLegend
        });

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
                try { delete latestRebasedData[ticker]; } catch (_) {}

                // Remove price series
                const s = priceSeriesMap.get(ticker);
                if (s && chart) {
                    try { chart.removeSeries(s); } catch (_) {}
                }
                priceSeriesMap.delete(ticker);

                // Remove volume series (if present)
                if (volSeriesMap && chart) {
                    const vs = volSeriesMap.get(ticker);
                    if (vs) {
                        try { chart.removeSeries(vs); } catch (_) {}
                        volSeriesMap.delete(ticker);
                    }
                    // If no volume series remain, remove the pane
                    if (volPane && volSeriesMap.size === 0) {
                        try { volPane = window.ChartVolumeManager.clearVolumeSeries(chart, volPane, volSeriesMap); } catch (_) {}
                    }
                }

                // Update average series
                if (showAvg && !useRaw) {
                    try {
                        avgSeries = window.ChartSeriesManager.updateAverageSeries(
                            chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, lastLabelVisible
                        );
                    } catch (_) {}
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
                tickerColorMap.set(t, colors[colorIndex++ % colors.length]);
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
            tickerColorMap.set(input, colors[colorIndex++ % colors.length]);
            
            window.ChartDomBuilder.addTickerChips(
                selectedTickersDiv, selectedTickers, tickerColorMap, multiplierMap, hiddenTickers, handleChipRemove
            );
            
            tickerInput.value = '';
            saveCards();
        };

        // Main plot function
        async function plot() {
            if (!chart) {
                chart = LightweightCharts.createChart(chartBox, {
                    layout: { background: { type: 'solid', color: '#ffffff' }, textColor: '#333', fontSize: (card._fontSize || (UI.FONT_DEFAULT || 12)) },
                    grid: { vertLines: { color: '#eee' }, horzLines: { color: '#eee' } },
                    timeScale: { secondsVisible: false, rightOffset: 3, fixLeftEdge: true },
                    rightPriceScale: { visible: true, mode: LightweightCharts.PriceScaleMode.Logarithmic, scaleMargins: { top: 0.1, bottom: 0.1 } },
                    crosshair: {
                        horzLine: { visible: false, labelVisible: false },
                        vertLine: { visible: true, labelVisible: true }
                    }
                });

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
                                (typeof param.time === 'string' ? Date.parse(param.time)/1000 : param.time) : null;

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

            // Fetch price data
            try {
                const tickerList = Array.from(selectedTickers);
                const data = await window.DataFetcher.getPriceData(tickerList);
                
                if (!data || Object.keys(data).length === 0) {
                    console.warn('No price data received');
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

                    window.ChartSeriesManager.createOrUpdateSeries(
                        chart, ticker, plotData, color, priceSeriesMap, lastLabelVisible, !useRaw
                    );
                }

                // Volume pane
                if (showVolPane) {
                    // Use saved range from card._visibleRange (already saved before chart recreation)
                    let rangeBeforeVol = card._visibleRange;
                    if (rangeBeforeVol) {
                        console.log(`[Plot] Using saved range for volume ops: from ${rangeBeforeVol.from}, to ${rangeBeforeVol.to}`);
                    }

                    // Temporarily unsubscribe from range changes during volume operations
                    if (rangeSaveHandler) {
                        try {
                            chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                        } catch (_) {}
                    }

                    volPane = window.ChartVolumeManager.createVolumePaneIfNeeded(chart, volPane, rangeBeforeVol);

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

                    // Final range restoration after all volume operations
                    if (rangeBeforeVol) {
                        try {
                            chart.timeScale().setVisibleRange(rangeBeforeVol);
                            console.log('[Plot] Final range restoration after volume pane operations: from ' + rangeBeforeVol.from + ', to ' + rangeBeforeVol.to);
                        } catch (_) {}
                    }

                    // Resubscribe to range changes
                    if (rangeSaveHandler) {
                        try {
                            chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);
                        } catch (_) {}
                    }
                }

                // Trading Volume pane
                if (showVolumePane) {
                    // Use saved range from card._visibleRange (already saved before chart recreation)
                    let rangeBeforeVolume = card._visibleRange;
                    if (rangeBeforeVolume) {
                        console.log(`[Plot] Using saved range for trading volume ops: from ${rangeBeforeVolume.from}, to ${rangeBeforeVolume.to}`);
                    }

                    // Temporarily unsubscribe from range changes during volume operations
                    if (rangeSaveHandler) {
                        try {
                            chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                        } catch (_) {}
                    }

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
                                    if (volumePane && typeof volumePane.addSeries === 'function') {
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
                                        console.error(`[VolumePane] volumePane does not have addSeries method`);
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

                    // Final range restoration after all volume operations
                    if (rangeBeforeVolume) {
                        try {
                            chart.timeScale().setVisibleRange(rangeBeforeVolume);
                            console.log('[Plot] Final range restoration after volume pane operations: from ' + rangeBeforeVolume.from + ', to ' + rangeBeforeVolume.to);
                        } catch (_) {}
                    }

                    // Resubscribe to range changes
                    if (rangeSaveHandler) {
                        try {
                            chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);
                        } catch (_) {}
                    }
                }

                // Average series
                if (showAvg && !useRaw) {
                    avgSeries = window.ChartSeriesManager.updateAverageSeries(
                        chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, lastLabelVisible
                    );
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
                // Update fixed legend if it's enabled
                setTimeout(() => updateFixedLegend(), 100);
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

            // Save current visible range before destroying chart
            let savedRange = null;
            if (chart && chart.timeScale) {
                try {
                    const visible = chart.timeScale().getVisibleRange();
                    if (visible && visible.from && visible.to) {
                        savedRange = { from: Math.round(visible.from), to: Math.round(visible.to) };
                        card._visibleRange = savedRange;
                        console.log(`[VolToggle] Saving range before recreate: from ${savedRange.from}, to ${savedRange.to}`);
                    }
                } catch (_) {}
            }

            // Keep the same total height - stretch factor will allocate space between panes

            saveCards();

            // Destroy and recreate chart to properly remove volume pane
            if (chart) {
                try {
                    if (crosshairHandler && chart.unsubscribeCrosshairMove) {
                        chart.unsubscribeCrosshairMove(crosshairHandler);
                    }
                } catch (_) {}
                try {
                    if (rangeSaveHandler && chart.timeScale && typeof chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                        chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                    }
                } catch (_) {}
                try {
                    chart.remove();
                } catch (_) {}
                chart = null;
                volPane = null;
                volumePane = null;
                priceSeriesMap.clear();
                volSeriesMap.clear();
                volumeSeriesMap.clear();
            }

            // Skip automatic range application since we're preserving the range manually
            skipRangeApplication = true;

            plot();
        });

        toggleVolumeBtn.addEventListener('click', () => {
            showVolumePane = !showVolumePane;
            card._showVolume = showVolumePane;
            toggleVolumeBtn.textContent = showVolumePane ? 'Hide Volume Pane' : 'Show Volume Pane';

            // Save current visible range
            let savedRange = null;
            if (chart && chart.timeScale) {
                const visible = chart.timeScale().getVisibleRange();
                if (visible && visible.from && visible.to) {
                    savedRange = { from: Math.round(visible.from), to: Math.round(visible.to) };
                    card._visibleRange = savedRange;
                }
            }

            // Keep the same total height - stretch factor will allocate space between panes

            // Destroy and recreate chart (panes are automatically destroyed with the chart)
            if (chart) {
                chart.remove();
                chart = null;
                volumePane = null;
                volPane = null;
                priceSeriesMap.clear();
                volSeriesMap.clear();
                volumeSeriesMap.clear();
            }

            skipRangeApplication = true;
            saveCards();
            plot();
        });

        toggleRawBtn.addEventListener('click', () => {
            useRaw = !useRaw;
            card._useRaw = useRaw;
            toggleRawBtn.textContent = useRaw ? 'Show % Basis' : 'Show Raw';
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
                window.ChartDomBuilder.updateButtonStates(elements, {
                    showDiff, showVol: showVolPane, showVolume: showVolumePane, useRaw, showAvg, lastLabelVisible
                });
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

                window.ChartDomBuilder.updateButtonStates(elements, {
                    showDiff, showVol: showVolPane, showVolume: showVolumePane, useRaw, showAvg, lastLabelVisible, showZeroLine
                });
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
                            initialY: card._fixedLegendPos?.y || 10
                        });

                        // Setup state change handler
                        fixedLegendEl._onStateChange = (changes) => {
                            if (changes.x !== undefined || changes.y !== undefined) {
                                card._fixedLegendPos = {
                                    x: changes.x !== undefined ? changes.x : card._fixedLegendPos?.x || 10,
                                    y: changes.y !== undefined ? changes.y : card._fixedLegendPos?.y || 10
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

                window.ChartDomBuilder.updateButtonStates(elements, {
                    showDiff, showVol: showVolPane, showVolume: showVolumePane, useRaw, showAvg, lastLabelVisible, showZeroLine, showFixedLegend
                });
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
                getName: (t) => nameCache[t]
            });
        }

        if (rangeSelect) {
            rangeSelect.addEventListener('change', () => {
                const val = rangeSelect.value;
                if (!val) return;
                let startYear;
                if (val === 'ytd') {
                    startYear = new Date().getUTCFullYear();
                } else {
                    startYear = parseInt(val, 10);
                }
                const from = Date.UTC(startYear, 0, 1) / 1000;
                const to = Math.floor(Date.now() / 1000);
                chart.timeScale().setVisibleRange({ from, to });
                // persist selection
                card._visibleRange = { from, to };
                saveCards();
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
                    null, '', true, false, targetWrapper, 500, (UI.FONT_DEFAULT || 12));
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
                        } catch (_) {}
                        try {
                            if (debouncedRebase && chart.timeScale && typeof chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                                chart.timeScale().unsubscribeVisibleTimeRangeChange(debouncedRebase);
                                if (typeof debouncedRebase.cancel === 'function') debouncedRebase.cancel();
                            }
                        } catch (_) {}
                        try {
                            if (rangeSaveHandler && chart.timeScale && typeof chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                                chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                            }
                        } catch (_) {}
                        try { window.ChartSeriesManager.clearAllSeries(chart, priceSeriesMap, volSeriesMap, avgSeries); } catch (_) {}
                        try {
                            if (volPane && chart && typeof chart.removePane === 'function') {
                                chart.removePane(volPane);
                            }
                        } catch (_) {}
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

        // Populate autocomplete
        fetch('http://localhost:5000/api/tickers')
            .then(r => r.json())
            .then(list => {
                const dl = document.getElementById('ticker-list');
                if (dl) {
                    dl.innerHTML = '';
                    list.forEach(t => {
                        const opt = document.createElement('option');
                        opt.value = t;
                        dl.appendChild(opt);
                    });
                    ['ALLW_VALUE', 'ALLW_SHARES'].forEach(x => {
                        const opt = document.createElement('option');
                        opt.value = x;
                        dl.appendChild(opt);
                    });
                }
            })
            .catch(() => {});

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
                    ws.forEach(c => {
                        const wrapper = window.PageManager ? window.PageManager.ensurePage(c.page || '1') : null;
                        createChartCard(
                            Array.isArray(c.tickers) ? c.tickers.join(', ') : (c.tickers || ''),
                            !!c.showDiff, !!c.showAvg, !!c.showVol, !!c.showVolume,
                            c.useRaw || false, c.multipliers || {}, c.hidden || [], c.range || null,
                            c.title || '', c.lastLabelVisible ?? true, c.showZeroLine || false, wrapper,
                            c.height || ((window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MIN_HEIGHT) || 400),
                            c.fontSize || ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12),
                            !!c.showFixedLegend,
                            c.fixedLegendPos || { x: 10, y: 10 }
                        );
                    });
                    try { localStorage.setItem(window.ChartConfig.STORAGE_KEYS.CARDS, JSON.stringify(ws)); } catch (_) {}
                    return;
                } else if (ws && typeof ws === 'object') {
                    const cards = Array.isArray(ws.cards) ? ws.cards : [];
                    const pagesMeta = (ws.pages && typeof ws.pages === 'object') ? ws.pages : null;
                    if (pagesMeta) {
                        try { localStorage.setItem('sandbox_pages', JSON.stringify(pagesMeta)); } catch (_) {}
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
                    cards.forEach(c => {
                        const wrapper = window.PageManager ? window.PageManager.ensurePage(c.page || '1') : null;
                        createChartCard(
                            Array.isArray(c.tickers) ? c.tickers.join(', ') : (c.tickers || ''),
                            !!c.showDiff, !!c.showAvg, !!c.showVol, !!c.showVolume,
                            c.useRaw || false, c.multipliers || {}, c.hidden || [], c.range || null,
                            c.title || '', c.lastLabelVisible ?? true, c.showZeroLine || false, wrapper,
                            c.height || ((window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MIN_HEIGHT) || 400),
                            c.fontSize || ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12),
                            !!c.showFixedLegend,
                            c.fixedLegendPos || { x: 10, y: 10 }
                        );
                    });
                    try { localStorage.setItem(window.ChartConfig.STORAGE_KEYS.CARDS, JSON.stringify(cards)); } catch (_) {}
                    if (cards.length > 0) return;
                    console.log('[Restore] Workspace object had no cards; checking localStorage');
                } else {
                    console.log('[Restore] Server returned empty workspace; checking localStorage');
                }
            } catch (e) {
                console.warn('[Restore] Server load failed, falling back to localStorage', e);
            }
            const stored = JSON.parse(localStorage.getItem(window.ChartConfig.STORAGE_KEYS.CARDS) || '[]');
            if (Array.isArray(stored) && stored.length) {
                console.log('[Restore] Loaded workspace from localStorage fallback');
                stored.forEach(c => {
                    const wrapper = window.PageManager ? window.PageManager.ensurePage(c.page || '1') : null;
                    createChartCard(
                        Array.isArray(c.tickers) ? c.tickers.join(', ') : (c.tickers || ''),
                        !!c.showDiff, !!c.showAvg, !!c.showVol, !!c.showVolume,
                        c.useRaw || false, c.multipliers || {}, c.hidden || [], c.range || null,
                        c.title || '', c.lastLabelVisible ?? true, c.showZeroLine || false, wrapper,
                        c.height || ((window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MIN_HEIGHT) || 400),
                        c.fontSize || ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12),
                        !!c.showFixedLegend,
                        c.fixedLegendPos || { x: 10, y: 10 },
                        !!c.fixedLegendMinimized
                    );
                });
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
