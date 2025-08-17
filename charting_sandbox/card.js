/**
 * Lightweight Charts Card Module (Refactored)
 * Main orchestrator that uses modular components for chart functionality
 */
(() => {
    const WRAPPER_ID = 'charts-wrapper';
    const SETTINGS = {
        COLORS: [
        '#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf',
        '#393b79','#637939','#8c6d31','#843c39','#7b4173','#3182bd','#31a354','#756bb1','#636363','#e6550d',
        '#e31a1c','#6baed6','#9ecae1','#c6dbef','#fd8d3c','#fdd0a2','#fdae6b','#a1d99b','#74c476','#31a354',
        '#6baed6','#9e9ac8','#bcbddc','#dadaeb','#fcbba1','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d',
        '#084594','#4292c6','#6baed6','#9ecae1','#c6dbef','#d9f0a3','#addd8e','#78c679','#41ab5d','#238443',
        '#006837','#004529','#990099','#ff0099','#00bfff','#ffa500','#ff0000','#00ff00','#008FFB','#00E396',
        '#008FFB', '#00E396', '#FEB019', '#FF4560', '#775DD0', '#546E7A', '#26a69a', '#D10CE8',
        '#FF66C3', '#FF8633', '#2B908F', '#F0E442', '#3D85C6', '#A52A2A', '#FFD700', '#00BFFF',
        '#FF1493', '#00FA9A', '#9932CC', '#FF4500', '#4B0082'],
        VOL_WINDOW: 100,          // bars for volume SMA
        PLOT_DEFER_MS: 100        // delay before initial plot
    };
    // convenient local aliases
    const colors = SETTINGS.COLORS;
    const { VOL_WINDOW, PLOT_DEFER_MS } = SETTINGS;
    
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
            multipliers: Object.fromEntries(card._multiplierMap ? Array.from(card._multiplierMap.entries()) : []),
            hidden: Array.from(card._hiddenTickers || []),
            range: card._visibleRange || null,
            useRaw: card._useRaw || false,
            title: card._title || '',
            lastLabelVisible: card._lastLabelVisible === true,
            height: (typeof card._height === 'number' ? card._height : (function(){
                const box = card.querySelector('.chart-box');
                const h = box ? parseInt(box.style.height || '0', 10) : 0;
                return isNaN(h) || h <= 0 ? null : h;
            })())
        }));
        
        localStorage.setItem('sandbox_cards', JSON.stringify(cards));
        if (window.StateManager && typeof window.StateManager.saveCards === 'function') {
            window.StateManager.saveCards(cards);
        }
    }
    window.saveCards = saveCards;

    function createChartCard(
        initialTickers = 'SPY',
        initialShowDiff = false,
        initialShowAvg = false,
        initialShowVol = true,
        initialUseRaw = false,
        initialMultipliers = {},
        initialHidden = [],
        initialRange = null,
        initialTitle = '',
        initialLastLabelVisible = false,
        initialHeight = null,
        wrapperEl = null
    ) {
        const wrapper = wrapperEl || document.getElementById(WRAPPER_ID);
        if (!wrapper) {
            console.error('Missing charts wrapper');
            return;
        }

        // Create card DOM
        globalCardCounter += 1;
        const cardId = `chart-${globalCardCounter}`;
        const card = window.ChartDomBuilder.createChartCard(cardId, initialTitle);
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
            nav.appendChild(navLink);
        }
        card._navLink = navLink;

        // Get DOM elements
        const elements = window.ChartDomBuilder.getCardElements(card);
        const { tickerInput, addBtn, plotBtn, toggleDiffBtn, toggleVolBtn, toggleRawBtn, 
                toggleAvgBtn, toggleLastLabelBtn, rangeSelect, selectedTickersDiv, chartBox, titleInput, removeCardBtn, addChartBtn, heightIncBtn, heightDecBtn } = elements;

        // Initialize state
        let showDiff = initialShowDiff;
        let showAvg = initialShowAvg;
        let showVolPane = initialShowVol;
        let useRaw = initialUseRaw;
        let lastLabelVisible = initialLastLabelVisible;
        let chart = null;
        let volPane = null;
        let avgSeries = null;
        
        let crosshairHandler = null;
        let debouncedRebase = null;
        let diffChart = null;
        let rangeSaveHandler = null;
        let rangeFetchHandler = null;
        let debouncedFetch = null;
        
        const debouncedSaveCards = (window.ChartUtils && window.ChartUtils.debounce) ? window.ChartUtils.debounce(saveCards, 300) : saveCards;

        const selectedTickers = new Set();
        const hiddenTickers = new Set(initialHidden);
        const multiplierMap = new Map(Object.entries(initialMultipliers));
        const tickerColorMap = new Map();
        const priceSeriesMap = new Map();
        const volSeriesMap = new Map();
        const rawPriceMap = new Map();
        const latestRebasedData = {};
        let colorIndex = 0;

        // Store state on card element
        card._selectedTickers = selectedTickers;
        card._showDiff = showDiff;
        card._showAvg = showAvg;
        card._showVol = showVolPane;
        card._useRaw = useRaw;
        card._multiplierMap = multiplierMap;
        card._hiddenTickers = hiddenTickers;
        card._visibleRange = initialRange;
        card._title = initialTitle;
        card._lastLabelVisible = lastLabelVisible;

        // Update button states
        window.ChartDomBuilder.updateButtonStates(elements, {
            showDiff, showVol: showVolPane, useRaw, showAvg, lastLabelVisible
        });

        // Initialize height
        const HEIGHT_MIN = 200;
        const HEIGHT_MAX = 1400;
        const HEIGHT_STEP = 100;
        let currentHeight = parseInt(initialHeight || chartBox.style.height || '400', 10);
        if (isNaN(currentHeight) || currentHeight < HEIGHT_MIN) currentHeight = 400;
        chartBox.style.height = currentHeight + 'px';
        card._height = currentHeight;

        // Initialize tickers
        if (initialTickers) {
            const tickers = window.ChartDomBuilder.parseTickerInput(initialTickers);
            tickers.forEach(t => {
                selectedTickers.add(t);
                tickerColorMap.set(t, colors[colorIndex++ % colors.length]);
            });
            window.ChartDomBuilder.addTickerChips(
                selectedTickersDiv, selectedTickers, tickerColorMap, multiplierMap, hiddenTickers
            );
        }

        // Add ticker function
        const addTicker = () => {
            const input = window.ChartDomBuilder.normalizeTicker(tickerInput.value);
            if (!input || selectedTickers.has(input)) return;
            
            selectedTickers.add(input);
            tickerColorMap.set(input, colors[colorIndex++ % colors.length]);
            
            window.ChartDomBuilder.addTickerChips(
                selectedTickersDiv, selectedTickers, tickerColorMap, multiplierMap, hiddenTickers
            );
            
            tickerInput.value = '';
            saveCards();
        };

        // Main plot function
        async function plot() {
            if (!chart) {
                chart = LightweightCharts.createChart(chartBox, {
                    layout: { background: { type: 'solid', color: '#ffffff' }, textColor: '#333' },
                    grid: { vertLines: { color: '#eee' }, horzLines: { color: '#eee' } },
                    timeScale: { secondsVisible: false, rightOffset: 10, fixLeftEdge: true },
                    rightPriceScale: { visible: true, mode: LightweightCharts.PriceScaleMode.Logarithmic, scaleMargins: { top: 0.1, bottom: 0.1 } },
                    crosshair: {
                        horzLine: { visible: false, labelVisible: false },
                        vertLine: { visible: true, labelVisible: true }
                    }
                });
                // Ensure chart matches container size
                try {
                    const w = chartBox.clientWidth;
                    const h = card._height || chartBox.clientHeight;
                    if (w && h) chart.resize(w, h);
                } catch(e) { console.warn(`[Card:${cardId}] initial resize skipped`, e); }

                // Add legend
                const legendEl = window.ChartLegend.createLegendElement(chartBox);
                crosshairHandler = window.ChartLegend.subscribeToCrosshair(chart, legendEl, {
                    useRaw,
                    priceSeriesMap,
                    hiddenTickers,
                    tickerColorMap,
                    selectedTickers,
                    rawPriceMap,
                    latestRebasedData
                });
            }

            if (selectedTickers.size === 0) return;

            // Clear existing series
            window.ChartSeriesManager.clearAllSeries(chart, priceSeriesMap, volSeriesMap, avgSeries);
            avgSeries = null;

            // Ensure company names
            // Pass chip nodes to avoid global DOM scan
            ensureNames(Array.from(selectedTickers), selectedTickersDiv.querySelectorAll('.chip'));

            // Fetch price data (range-aware)
            try {
                const tickerList = Array.from(selectedTickers);
                // Determine fetch range: saved -> initial -> default 1Y
                const savedRange = card._visibleRange || initialRange;
                const presets = window.ChartUtils && typeof window.ChartUtils.getPresetRanges === 'function'
                    ? window.ChartUtils.getPresetRanges() : null;
                const defaultRange = presets ? presets['1Y'] : null;
                const fetchRange = savedRange || defaultRange;

                const from = fetchRange && fetchRange.from ? Math.floor(fetchRange.from) : null;
                const to = fetchRange && fetchRange.to ? Math.floor(fetchRange.to) : null;

                const data = await window.DataFetcher.getPriceData(tickerList, from, to, '1d');
                
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
                    volPane = window.ChartVolumeManager.createVolumePaneIfNeeded(chart, volPane);
                    try {
                        const volResp = await window.DataFetcher.getVolumeData(tickerList, from, to, '1d');
                        for (const ticker of tickerList) {
                            if (hiddenTickers.has(ticker)) continue;
                            const color = tickerColorMap.get(ticker);
                            const apiArr = Array.isArray(volResp?.[ticker]) ? volResp[ticker].filter(d => d && d.value != null) : [];
                            let volData;
                            if (apiArr.length) {
                                volData = apiArr;
                            } else {
                                const rawData = rawPriceMap.get(ticker);
                                volData = window.ChartVolumeManager.calculateVolume(rawData, VOL_WINDOW);
                            }
                            window.ChartVolumeManager.addVolumeSeries(
                                chart, volPane, ticker, volData, color, volSeriesMap, lastLabelVisible
                            );
                        }
                    } catch (e) {
                        console.warn('[Volume] API fetch failed, falling back to derived:', e);
                        for (const ticker of tickerList) {
                            if (hiddenTickers.has(ticker)) continue;
                            const rawData = rawPriceMap.get(ticker);
                            const volData = window.ChartVolumeManager.calculateVolume(rawData, VOL_WINDOW);
                            const color = tickerColorMap.get(ticker);
                            window.ChartVolumeManager.addVolumeSeries(
                                chart, volPane, ticker, volData, color, volSeriesMap, lastLabelVisible
                            );
                        }
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
                    }
                };
                chart.timeScale().subscribeVisibleTimeRangeChange(rangeSaveHandler);

                // Subscribe to fetch data on visible range change (debounced)
                if (rangeFetchHandler) {
                    chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeFetchHandler);
                }
                const fetchDebounce = (window.ChartUtils && typeof window.ChartUtils.debounce === 'function')
                    ? window.ChartUtils.debounce : (fn) => fn;
                debouncedFetch = fetchDebounce(async (visible) => {
                    try {
                        if (!visible || !visible.from || !visible.to) return;
                        const fromTs = Math.round(visible.from);
                        const toTs = Math.round(visible.to);
                        const list = Array.from(selectedTickers);
                        console.log(`[RangeFetch:${cardId}] Fetching range ${fromTs} -> ${toTs} for ${list.join(',')}`);
                        const fresh = await window.DataFetcher.getPriceData(list, fromTs, toTs, '1d');

                        for (const t of list) {
                            const tData = fresh[t] || [];
                            const clean = Array.isArray(tData) ? tData.filter(d => d.value != null) : [];
                            rawPriceMap.set(t, clean);
                            const color = tickerColorMap.get(t);
                            const mult = multiplierMap.get(t) || 1;
                            const plotData = useRaw ? clean : window.ChartSeriesManager.rebaseData(clean, mult);
                            if (!useRaw) {
                                latestRebasedData[t] = plotData;
                            }
                            const series = window.ChartSeriesManager.createOrUpdateSeries(
                                chart, t, plotData, color, priceSeriesMap, lastLabelVisible, !useRaw
                            );
                        }

                        // Update avg if enabled
                        if (showAvg && !useRaw) {
                            avgSeries = window.ChartSeriesManager.updateAverageSeries(
                                chart, avgSeries, priceSeriesMap, hiddenTickers, undefined, lastLabelVisible
                            );
                        }

                        // Update volume pane if enabled (API preferred)
                        if (showVolPane && volPane) {
                            try {
                                const volResp = await window.DataFetcher.getVolumeData(list, fromTs, toTs, '1d');
                                for (const t of list) {
                                    if (hiddenTickers.has(t)) continue;
                                    const color = tickerColorMap.get(t) || '#000000';
                                    const apiArr = Array.isArray(volResp?.[t]) ? volResp[t].filter(d => d && d.value != null) : [];
                                    const volData = apiArr.length ? apiArr : window.ChartVolumeManager.calculateVolume(rawPriceMap.get(t), VOL_WINDOW);
                                    window.ChartVolumeManager.addVolumeSeries(
                                        chart, volPane, t, volData, color, volSeriesMap, lastLabelVisible
                                    );
                                }
                            } catch (e) {
                                console.warn(`[RangeFetch:${cardId}] Volume API fetch failed; fallback to derived`, e);
                                window.ChartVolumeManager.updateAllVolumeSeries(
                                    chart, volPane, selectedTickers, rawPriceMap, tickerColorMap, volSeriesMap, hiddenTickers, lastLabelVisible
                                );
                            }
                        }
                    } catch (err) {
                        console.warn(`[RangeFetch:${cardId}] Error during fetch:`, err);
                    }
                }, 500);
                rangeFetchHandler = (visible) => {
                    if (visible && visible.from && visible.to) {
                        debouncedFetch(visible);
                    }
                };
                chart.timeScale().subscribeVisibleTimeRangeChange(rangeFetchHandler);

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
                        useRaw
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

                // Apply saved or default visible range
                const saved = card._visibleRange || initialRange || (defaultRange || null);
                if (saved && saved.from && saved.to) {
                    try {
                        chart.timeScale().setVisibleRange(saved);
                        console.log(`[RangeApply:${cardId}] Applied saved time range => from ${saved.from}, to ${saved.to}`);
                    } catch (e) {
                        chart.timeScale().fitContent();
                    }
                } else {
                    chart.timeScale().fitContent();
                }

            } catch (error) {
                console.error('Plot error:', error);
            }
        }

        // Event handlers
        addBtn.addEventListener('click', addTicker);
        tickerInput.addEventListener('keypress', e => {
            if (e.key === 'Enter') addTicker();
        });
        
        plotBtn.addEventListener('click', plot);

        // Height controls
        function applyHeight(newH){
            const clamped = Math.max(HEIGHT_MIN, Math.min(HEIGHT_MAX, newH|0));
            card._height = clamped;
            chartBox.style.height = clamped + 'px';
            try {
                if (chart) {
                    const w = chartBox.clientWidth || (chartBox.parentElement ? chartBox.parentElement.clientWidth : undefined);
                    chart.resize(w || 0, clamped);
                }
            } catch(e) { console.warn(`[Card:${cardId}] resize error`, e); }
            saveCards();
            console.log(`[Card:${cardId}] Height set to ${clamped}px`);
        }
        if (heightIncBtn) {
            heightIncBtn.addEventListener('click', () => applyHeight((card._height||chartBox.clientHeight||400) + HEIGHT_STEP));
        }
        if (heightDecBtn) {
            heightDecBtn.addEventListener('click', () => applyHeight((card._height||chartBox.clientHeight||400) - HEIGHT_STEP));
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
            toggleVolBtn.textContent = showVolPane ? 'Hide Vol Pane' : 'Show Vol Pane';
            saveCards();
            if (showVolPane) {
                plot();
            } else if (volPane) {
                window.ChartVolumeManager.clearVolumeSeries(chart, volPane, volSeriesMap);
                volPane = null;
            }
        });

        toggleRawBtn.addEventListener('click', () => {
            useRaw = !useRaw;
            card._useRaw = useRaw;
            toggleRawBtn.textContent = useRaw ? 'Show % Basis' : 'Show Raw';
            saveCards();
            plot();
        });

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

        if (toggleLastLabelBtn) {
            toggleLastLabelBtn.addEventListener('click', () => {
                lastLabelVisible = !lastLabelVisible;
                card._lastLabelVisible = lastLabelVisible;
                console.log(`[Card:${cardId}] Last value label ${lastLabelVisible ? 'enabled' : 'disabled'}`);
                window.ChartDomBuilder.updateButtonStates(elements, {
                    showDiff, showVol: showVolPane, useRaw, showAvg, lastLabelVisible
                });
                // Apply to all existing series
                priceSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: lastLabelVisible }));
                if (avgSeries) avgSeries.applyOptions({ lastValueVisible: lastLabelVisible });
                if (volPane && volSeriesMap) {
                    volSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: lastLabelVisible }));
                }
                saveCards();
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
                // Create new chart on the active page (or default wrapper if no pages)
                const newCard = createChartCard('', showDiff, showAvg, showVolPane, useRaw, 
                    Object.fromEntries(multiplierMap), Array.from(hiddenTickers), 
                    card._visibleRange, '', lastLabelVisible, card._height ?? null, targetWrapper);
                saveCards();
                // Insert new card after the current card (within the same page)
                if (card.nextSibling) {
                    (targetWrapper || wrapper).insertBefore(newCard, card.nextSibling);
                }
            });
        }

        // Remove card handler
        if (removeCardBtn) {
            removeCardBtn.addEventListener('click', () => {
                console.log(`[Card:${cardId}] Removing card`);
                try {
                    if (chart) {
                        // Unsubscribe range listeners
                        try {
                            if (rangeSaveHandler) {
                                chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeSaveHandler);
                                rangeSaveHandler = null;
                            }
                            if (rangeFetchHandler) {
                                chart.timeScale().unsubscribeVisibleTimeRangeChange(rangeFetchHandler);
                                rangeFetchHandler = null;
                            }
                            if (debouncedRebase) {
                                chart.timeScale().unsubscribeVisibleTimeRangeChange(debouncedRebase);
                                if (typeof debouncedRebase.cancel === 'function') debouncedRebase.cancel();
                                debouncedRebase = null;
                            }
                        } catch (subErr) {
                            console.warn(`[Card:${cardId}] Unsubscribe error:`, subErr);
                        }

                        // Clear volume pane & series first
                        try {
                            if (volPane) {
                                volPane = window.ChartVolumeManager.clearVolumeSeries(chart, volPane, volSeriesMap);
                            }
                        } catch (vErr) {
                            console.warn(`[Card:${cardId}] Volume clear error:`, vErr);
                        }

                        // Clear price and avg series
                        try {
                            window.ChartSeriesManager.clearAllSeries(chart, priceSeriesMap, null, avgSeries);
                            avgSeries = null;
                        } catch (pErr) {
                            console.warn(`[Card:${cardId}] Series clear error:`, pErr);
                        }

                        // Dispose chart instance
                        try {
                            if (typeof chart.remove === 'function') {
                                chart.remove();
                            }
                            chart = null;
                        } catch (rmErr) {
                            console.warn(`[Card:${cardId}] Chart dispose error:`, rmErr);
                        }
                    }
                } catch (err) {
                    console.warn(`[Card:${cardId}] Error during cleanup:`, err);
                }

                // Remove nav link
                try {
                    if (navLink && navLink.parentElement) {
                        navLink.parentElement.removeChild(navLink);
                    }
                } catch (navErr) {
                    console.warn(`[Card:${cardId}] Nav removal error:`, navErr);
                }

                // Remove card from DOM
                const parent = card.parentElement;
                if (parent) parent.removeChild(card);
                
                // Persist updated state
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
        window.DataFetcher.getTickers()
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
            .catch((e) => { console.warn('Ticker list load failed:', e); });

        // Restore or create cards
        const urlParams = new URLSearchParams(window.location.search);
        const startBlank = urlParams.has('blank');

        if (startBlank) {
            createChartCard('');
        } else {
            const stored = JSON.parse(localStorage.getItem('sandbox_cards') || '[]');
            if (stored.length) {
                stored.forEach(c => {
                    const wrapper = window.PageManager ? window.PageManager.ensurePage(c.page || '1') : null;
                    createChartCard(
                        c.tickers.join(', '), c.showDiff, c.showAvg, c.showVol, 
                        c.useRaw || false, c.multipliers, c.hidden, c.range, c.title || '', c.lastLabelVisible ?? false, c.height ?? null, wrapper
                    );
                });
            } else {
                // Try to restore from backend
                window.DataFetcher.loadWorkspace()
                    .then(ws => {
                        if (Array.isArray(ws) && ws.length) {
                            ws.forEach(c => {
                                const wrapper = window.PageManager ? window.PageManager.ensurePage(c.page || '1') : null;
                                createChartCard(
                                    c.tickers.join(', '), c.showDiff, c.showAvg, c.showVol,
                                    c.useRaw || false, c.multipliers, c.hidden, c.range, c.title || '', c.lastLabelVisible ?? false, c.height ?? null, wrapper
                                );
                            });
                            localStorage.setItem('sandbox_cards', JSON.stringify(ws));
                        } else {
                            createChartCard('SPY');
                        }
                    })
                    .catch(() => createChartCard('SPY'));
            }
        }
    });

    window.createChartCard = createChartCard;
})();
