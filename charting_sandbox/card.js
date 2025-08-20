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
            multipliers: Object.fromEntries(card._multiplierMap ? Array.from(card._multiplierMap.entries()) : []),
            hidden: Array.from(card._hiddenTickers || []),
            range: card._visibleRange || null,
            useRaw: card._useRaw || false,
            title: card._title || '',
            lastLabelVisible: card._lastLabelVisible !== false,
            height: card._height || (() => { try { const el = card.querySelector('.chart-box'); return el ? parseInt(getComputedStyle(el).height, 10) : undefined; } catch(_) { return undefined; } })(),
            fontSize: card._fontSize || ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12)
        }));
        
        localStorage.setItem(window.ChartConfig.STORAGE_KEYS.CARDS, JSON.stringify(cards));
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
        initialLastLabelVisible = true,
        wrapperEl = null,
        initialHeight = ((window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MIN_HEIGHT) || 400),
        initialFontSize = ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12)
    ) {
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
            nav.appendChild(navLink);
        }
        card._navLink = navLink;

        // Get DOM elements
        const elements = window.ChartDomBuilder.getCardElements(card);
        const { tickerInput, addBtn, plotBtn, toggleDiffBtn, toggleVolBtn, toggleRawBtn, 
                toggleAvgBtn, toggleLastLabelBtn, heightDownBtn, heightUpBtn, fontDownBtn, fontUpBtn, rangeSelect, selectedTickersDiv, chartBox, titleInput, removeCardBtn, addChartBtn } = elements;

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
        card._height = initialHeight;
        card._fontSize = initialFontSize;

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

        // Update button states
        window.ChartDomBuilder.updateButtonStates(elements, {
            showDiff, showVol: showVolPane, useRaw, showAvg, lastLabelVisible
        });

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
                    layout: { background: { type: 'solid', color: '#ffffff' }, textColor: '#333', fontSize: (card._fontSize || (UI.FONT_DEFAULT || 12)) },
                    grid: { vertLines: { color: '#eee' }, horzLines: { color: '#eee' } },
                    timeScale: { secondsVisible: false, rightOffset: 10, fixLeftEdge: true },
                    rightPriceScale: { visible: true, mode: LightweightCharts.PriceScaleMode.Logarithmic, scaleMargins: { top: 0.1, bottom: 0.1 } },
                    crosshair: {
                        horzLine: { visible: false, labelVisible: false },
                        vertLine: { visible: true, labelVisible: true }
                    }
                });

                // Ensure initial size reflects stored height
                applyResize(card._height || initialHeight);

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
                    volPane = window.ChartVolumeManager.createVolumePaneIfNeeded(chart, volPane);
                    
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
                const saved = card._visibleRange || initialRange;
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

        // Toggle last value label visibility
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
                    card._visibleRange, '', lastLabelVisible, targetWrapper, card._height || initialHeight, card._fontSize || (UI.FONT_DEFAULT || 12));
                saveCards();
                // Insert new card after the current card (within the same page)
                if (card.nextSibling) {
                    (targetWrapper || wrapper).insertBefore(newCard, card.nextSibling);
                }
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
                    console.log('[Restore] Loaded workspace from server');
                    ws.forEach(c => {
                        const wrapper = window.PageManager ? window.PageManager.ensurePage(c.page || '1') : null;
                        createChartCard(
                            Array.isArray(c.tickers) ? c.tickers.join(', ') : (c.tickers || ''),
                            !!c.showDiff, !!c.showAvg, !!c.showVol,
                            c.useRaw || false, c.multipliers || {}, c.hidden || [], c.range || null,
                            c.title || '', c.lastLabelVisible ?? true, wrapper,
                            c.height || ((window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MIN_HEIGHT) || 400),
                            c.fontSize || ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12)
                        );
                    });
                    try { localStorage.setItem(window.ChartConfig.STORAGE_KEYS.CARDS, JSON.stringify(ws)); } catch (_) {}
                    return;
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
                        !!c.showDiff, !!c.showAvg, !!c.showVol,
                        c.useRaw || false, c.multipliers || {}, c.hidden || [], c.range || null,
                        c.title || '', c.lastLabelVisible ?? true, wrapper,
                        c.height || ((window.ChartConfig && window.ChartConfig.DIMENSIONS && window.ChartConfig.DIMENSIONS.CHART_MIN_HEIGHT) || 400),
                        c.fontSize || ((window.ChartConfig && window.ChartConfig.UI && window.ChartConfig.UI.FONT_DEFAULT) || 12)
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
