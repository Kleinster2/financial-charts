/**
 * Chart Card Plot Module
 *
 * Extracted from card.js - handles chart plotting, destruction, and related helpers.
 * Uses ctx.runtime for all chart instance state.
 *
 * Exports: window.ChartCardPlot
 */

window.ChartCardPlot = (() => {
    // Constants from ChartConfig
    const getConfig = () => ({
        VOL_WINDOW: window.ChartConfig?.VOLUME_WINDOW || 100,
        PANE_HEIGHT: window.ChartConfig?.DIMENSIONS?.PANE_HEIGHT || 100,
        HEIGHT_MIN: window.ChartConfig?.DIMENSIONS?.CHART_MIN_HEIGHT || 400,
        HEIGHT_MAX: window.ChartConfig?.DIMENSIONS?.CHART_MAX_HEIGHT || 800
    });

    // Name cache shared across cards
    const nameCache = {};

    /**
     * Ensure company names are loaded for tickers
     * @param {string[]} tickers - Tickers to fetch names for
     * @param {NodeList|null} chipNodes - Optional chip nodes to update tooltips
     */
    async function ensureNames(tickers, chipNodes = null) {
        const missing = tickers.filter(t => !(t in nameCache));
        const aliasPromise = window.ChartUtils.getAliases();

        if (missing.length) {
            try {
                const metadata = await window.DataFetcher.getMetadata(missing);
                Object.assign(nameCache, metadata);
            } catch (error) {
                console.error('Failed to fetch metadata:', error);
            }
        }

        const aliases = await aliasPromise;

        const chips = chipNodes ? Array.from(chipNodes) : document.querySelectorAll('.chip');
        chips.forEach(ch => {
            const t = ch.dataset.ticker;
            let tooltip = nameCache[t] || '';
            if (aliases[t]) {
                const hint = `${t} → ${aliases[t]} (fundamentals)`;
                tooltip = tooltip ? `${tooltip}\n${hint}` : hint;
            }
            if (tooltip) ch.title = tooltip;
        });
    }

    /**
     * Get name from cache
     * @param {string} ticker
     * @returns {string|undefined}
     */
    function getName(ticker) {
        return nameCache[ticker];
    }

    /**
     * Compute min/max time across currently visible tickers
     * @param {Object} ctx - Card context
     * @returns {Object|null} { from, to } or null
     */
    function getCurrentDataRange(ctx) {
        const rt = ctx.runtime;
        if (!rt) return null;

        let minT = Infinity;
        let maxT = -Infinity;
        let has = false;

        ctx.selectedTickers.forEach(t => {
            if (ctx.hiddenTickers.has(t)) return;
            const arr = rt.rawPriceMap.get(t);
            if (!arr || !arr.length) return;
            has = true;
            minT = Math.min(minT, arr[0].time);
            maxT = Math.max(maxT, arr[arr.length - 1].time);
        });

        return has ? { from: minT, to: maxT } : null;
    }

    /**
     * Destroy chart instance and cleanup all subscriptions/series/panes
     * @param {Object} ctx - Card context
     */
    function destroyChart(ctx) {
        const rt = ctx.runtime;
        if (!rt) return;

        // Abort any in-flight fetches
        if (rt.plotAbortController) {
            rt.plotAbortController.abort();
            rt.plotAbortController = null;
        }

        if (!rt.chart) return;

        // Unsubscribe all handlers
        try {
            if (rt.crosshairHandler && rt.chart.unsubscribeCrosshairMove) {
                rt.chart.unsubscribeCrosshairMove(rt.crosshairHandler);
            }
        } catch (_) { }
        try {
            if (rt.fixedLegendCrosshairHandler && rt.chart.unsubscribeCrosshairMove) {
                rt.chart.unsubscribeCrosshairMove(rt.fixedLegendCrosshairHandler);
            }
        } catch (_) { }
        try {
            if (rt.debouncedRebase && rt.chart.timeScale && typeof rt.chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                rt.chart.timeScale().unsubscribeVisibleTimeRangeChange(rt.debouncedRebase);
                if (typeof rt.debouncedRebase.cancel === 'function') rt.debouncedRebase.cancel();
            }
        } catch (_) { }
        try {
            if (rt.rangeSaveHandler && rt.chart.timeScale && typeof rt.chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                rt.chart.timeScale().unsubscribeVisibleTimeRangeChange(rt.rangeSaveHandler);
            }
        } catch (_) { }
        try {
            if (rt.tickerLabelHandler && rt.chart.timeScale && typeof rt.chart.timeScale().unsubscribeVisibleTimeRangeChange === 'function') {
                rt.chart.timeScale().unsubscribeVisibleTimeRangeChange(rt.tickerLabelHandler);
            }
        } catch (_) { }

        // Remove chart instance
        try {
            rt.chart.remove();
        } catch (_) { }

        // Clear references
        rt.chart = null;
        rt.volPane = null;
        rt.volumePane = null;
        rt.revenuePane = null;
        rt.fundamentalsPane = null;
        rt.fixedLegendCrosshairHandler = null;
        rt.avgSeries = null;
        rt.zeroLineSeries = null;

        // Clear series maps
        rt.priceSeriesMap.clear();
        rt.volSeriesMap.clear();
        rt.volumeSeriesMap.clear();
        rt.revenueSeriesMap.clear();
        rt.fundamentalSeriesMap.clear();

        // Cleanup fixed legend
        if (rt.fixedLegendEl) {
            if (typeof rt.fixedLegendEl._cleanup === 'function') {
                rt.fixedLegendEl._cleanup();
            }
            rt.fixedLegendEl.remove();
            rt.fixedLegendEl = null;
        }

        // Remove overlay DOM elements
        const chartBox = ctx.chartBox;
        if (chartBox) {
            const tickerLabels = chartBox.querySelector('.ticker-labels-container');
            if (tickerLabels) tickerLabels.remove();
            const floatingLegend = chartBox.querySelector('.floating-legend');
            if (floatingLegend) floatingLegend.remove();
        }
    }

    /**
     * Save visible range, destroy chart, and replot
     * @param {Object} ctx - Card context
     * @param {Function} plotFn - The plot function to call after destroy
     */
    function destroyChartAndReplot(ctx, plotFn) {
        const rt = ctx.runtime;
        if (!rt) return;

        // Save current visible range
        if (rt.chart && rt.chart.timeScale) {
            try {
                const visible = rt.chart.timeScale().getVisibleRange();
                if (visible && visible.from && visible.to) {
                    ctx.visibleRange = { from: Math.round(visible.from), to: Math.round(visible.to) };
                    window.ChartCardContext.syncToCard(ctx);
                }
            } catch (_) { }
        }

        destroyChart(ctx);

        // Skip automatic range application and replot
        rt.skipRangeApplication = true;
        ctx.saveCards();
        plotFn();
    }

    /**
     * Apply resize to chart box based on height and active panes
     * @param {Object} ctx - Card context
     * @param {number} baseH - Base height
     */
    function applyResize(ctx, baseH) {
        const rt = ctx.runtime;
        const chartBox = ctx.chartBox;
        const config = getConfig();

        if (!chartBox) return;

        let paneCount = 0;
        if (ctx.showVolumePane) paneCount++;
        if (ctx.showRevenuePane) paneCount++;
        if (ctx.showFundamentalsPane) paneCount++;
        if (ctx.showVolPane) paneCount++;

        const totalH = baseH + (paneCount * config.PANE_HEIGHT);
        chartBox.style.height = `${totalH}px`;

        if (rt?.chart && typeof rt.chart.resize === 'function') {
            const width = chartBox.clientWidth || chartBox.getBoundingClientRect().width || 800;
            console.log(`[Card:${ctx.cardId}] Resizing chart to ${width} x ${totalH} (base: ${baseH}, panes: ${paneCount})`);
            try { rt.chart.resize(width, totalH); } catch (e) { console.warn(`[Card:${ctx.cardId}] chart.resize failed`, e); }
        }
    }

    /**
     * Update zero line visibility and data
     * @param {Object} ctx - Card context
     */
    function updateZeroLine(ctx) {
        const rt = ctx.runtime;
        if (!rt?.chart) return;

        if (ctx.showZeroLine) {
            if (!rt.zeroLineSeries) {
                rt.zeroLineSeries = rt.chart.addSeries(LightweightCharts.LineSeries, {
                    color: '#666666',
                    lineWidth: 1,
                    lineStyle: LightweightCharts.LineStyle.Dashed,
                    lastValueVisible: false,
                    priceLineVisible: false,
                    crosshairMarkerVisible: false,
                    title: ''
                });
            }

            const zeroValue = ctx.useRaw ? 0 : 100;
            const timeScale = rt.chart.timeScale();
            const visibleRange = timeScale.getVisibleRange();

            if (visibleRange) {
                const lineData = [
                    { time: visibleRange.from, value: zeroValue },
                    { time: visibleRange.to, value: zeroValue }
                ];
                rt.zeroLineSeries.setData(lineData);
            } else {
                const now = Math.floor(Date.now() / 1000);
                const tenYearsAgo = now - (10 * 365 * 24 * 60 * 60);
                const lineData = [
                    { time: tenYearsAgo, value: zeroValue },
                    { time: now, value: zeroValue }
                ];
                rt.zeroLineSeries.setData(lineData);
            }
        } else {
            if (rt.zeroLineSeries) {
                rt.chart.removeSeries(rt.zeroLineSeries);
                rt.zeroLineSeries = null;
            }
        }
    }

    /**
     * Update fixed legend with latest values
     * @param {Object} ctx - Card context
     */
    function updateFixedLegend(ctx) {
        const rt = ctx.runtime;
        if (!ctx.showFixedLegend || !rt?.fixedLegendEl) return;

        let visibleRange = null;
        if (rt.chart && rt.chart.timeScale) {
            try {
                visibleRange = rt.chart.timeScale().getVisibleRange();
            } catch (e) {
                console.warn('[FixedLegend] Could not get visible range:', e);
            }
        }

        const legendData = [];
        ctx.selectedTickers.forEach(ticker => {
            if (ctx.hiddenTickers.has(ticker)) return;

            const dataArray = ctx.useRaw ? rt.rawPriceMap.get(ticker) : rt.latestRebasedData[ticker];
            if (!dataArray || dataArray.length === 0) return;

            if (visibleRange && visibleRange.from && visibleRange.to) {
                const hasVisibleData = dataArray.some(point =>
                    point.time >= visibleRange.from && point.time <= visibleRange.to
                );
                if (!hasVisibleData) return;
            }

            const latestPoint = dataArray[dataArray.length - 1];
            if (latestPoint && latestPoint.value != null) {
                legendData.push({
                    ticker,
                    value: latestPoint.value,
                    color: ctx.tickerColorMap.get(ticker)
                });
            }
        });

        window.ChartFixedLegend.updateContent(rt.fixedLegendEl, legendData, {
            useRaw: ctx.useRaw,
            hiddenTickers: ctx.hiddenTickers,
            tickerColorMap: ctx.tickerColorMap,
            getName: (t) => nameCache[t],
            showTickers: ctx.showLegendTickers
        });
    }

    /**
     * Execute pane operations while preserving visible range
     * @param {Object} ctx - Card context
     * @param {string} paneName - Name for logging
     * @param {Function} operation - Async function to execute
     */
    async function withRangePreservation(ctx, paneName, operation) {
        const rt = ctx.runtime;
        if (!rt?.chart) return;

        const rangeBefore = ctx.visibleRange;
        if (rangeBefore) {
            console.log(`[Plot] Using saved range for ${paneName} ops: from ${rangeBefore.from}, to ${rangeBefore.to}`);
        }

        // Temporarily unsubscribe from range changes
        if (rt.rangeSaveHandler) {
            try {
                rt.chart.timeScale().unsubscribeVisibleTimeRangeChange(rt.rangeSaveHandler);
            } catch (_) { }
        }

        await operation();

        // Final range restoration
        if (rangeBefore && !ctx.skipRangeRestoration) {
            try {
                rt.chart.timeScale().setVisibleRange(rangeBefore);
                console.log(`[Plot] Final range restoration after ${paneName} operations`);
            } catch (_) { }
        } else if (ctx.skipRangeRestoration) {
            console.log(`[Plot] Skipping ${paneName} range restoration (manual range was set)`);
            if (paneName === 'fundamentals') {
                ctx.skipRangeRestoration = false;
            }
        }

        // Resubscribe to range changes
        if (rt.rangeSaveHandler) {
            try {
                rt.chart.timeScale().subscribeVisibleTimeRangeChange(rt.rangeSaveHandler);
            } catch (_) { }
        }
    }

    /**
     * Main plot function
     * @param {Object} ctx - Card context
     * @param {Object} options - Additional options (initialHeight, initialRange)
     */
    async function plot(ctx, options = {}) {
        const endTiming = window.ChartUtils?.perf?.start('chartPlot');

        const rt = window.ChartCardContext.getRuntime(ctx);
        const config = getConfig();
        const { initialHeight, initialRange } = options;

        // Cancel any in-flight fetches from previous plot
        if (rt.plotAbortController) {
            rt.plotAbortController.abort();
        }
        rt.plotAbortController = new AbortController();
        const plotSignal = rt.plotAbortController.signal;

        const chartBox = ctx.chartBox;

        if (!rt.chart) {
            // Set price format based on mode and decimal precision
            const precision = ctx.decimalPrecision !== undefined ? ctx.decimalPrecision : 2;
            const priceFormat = window.ChartUtils.createPriceFormatter(ctx.useRaw, precision);

            rt.chart = LightweightCharts.createChart(chartBox, {
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
            rt.tickerLabelsContainer = window.ChartTickerLabels.createLabelsContainer(chartBox);

            // Ensure initial size reflects stored height
            applyResize(ctx, ctx.height || initialHeight);

            // Apply rightOffset dynamically
            rt.chart.applyOptions({
                timeScale: { rightOffset: 3 }
            });

            // Add legend
            const legendEl = window.ChartLegend.createLegendElement(chartBox);
            rt.crosshairHandler = window.ChartLegend.subscribeToCrosshair(rt.chart, legendEl, {
                useRaw: ctx.useRaw,
                priceSeriesMap: rt.priceSeriesMap,
                hiddenTickers: ctx.hiddenTickers,
                tickerColorMap: ctx.tickerColorMap,
                selectedTickers: ctx.selectedTickers,
                rawPriceMap: rt.rawPriceMap,
                latestRebasedData: rt.latestRebasedData,
                getName: (t) => nameCache[t]
            });

            // Subscribe to crosshair for fixed legend dual mode
            rt.fixedLegendCrosshairHandler = (param) => {
                if (!ctx.showFixedLegend || !rt.fixedLegendEl) return;

                if (param && param.point && param.time !== undefined) {
                    let visibleRange = null;
                    try {
                        visibleRange = rt.chart.timeScale().getVisibleRange();
                    } catch (e) {
                        console.warn('[FixedLegend] Could not get visible range:', e);
                    }

                    const legendData = [];
                    const time = param.time !== undefined ?
                        (typeof param.time === 'string' ? Date.parse(param.time) / 1000 : param.time) : null;

                    ctx.selectedTickers.forEach(ticker => {
                        if (ctx.hiddenTickers.has(ticker)) return;

                        const dataArray = ctx.useRaw ? rt.rawPriceMap.get(ticker) : rt.latestRebasedData[ticker];
                        if (!dataArray) return;

                        if (visibleRange && visibleRange.from && visibleRange.to) {
                            const hasVisibleData = dataArray.some(point =>
                                point.time >= visibleRange.from && point.time <= visibleRange.to
                            );
                            if (!hasVisibleData) return;
                        }

                        const point = dataArray.find(p => p.time === time);
                        if (point && point.value != null) {
                            legendData.push({
                                ticker,
                                value: point.value,
                                color: ctx.tickerColorMap.get(ticker)
                            });
                        }
                    });

                    if (legendData.length > 0) {
                        window.ChartFixedLegend.updateContent(rt.fixedLegendEl, legendData, {
                            useRaw: ctx.useRaw,
                            hiddenTickers: ctx.hiddenTickers,
                            tickerColorMap: ctx.tickerColorMap,
                            getName: (t) => nameCache[t]
                        });
                    }
                } else {
                    updateFixedLegend(ctx);
                }
            };
            rt.chart.subscribeCrosshairMove(rt.fixedLegendCrosshairHandler);
        }

        if (ctx.selectedTickers.size === 0) return;

        // Clear existing series first
        window.ChartSeriesManager.clearAllSeries(rt.chart, rt.priceSeriesMap, rt.volSeriesMap, rt.avgSeries);
        rt.avgSeries = null;

        // Remove volume pane if hiding it
        if (!ctx.showVolPane && rt.volPane) {
            try {
                console.log('[Plot] Attempting to remove volume pane');
                rt.chart.removePane(rt.volPane);
                console.log('[Plot] Volume pane removed successfully');
            } catch (e) {
                console.warn('[Plot] Could not remove volume pane:', e);
            }
            rt.volPane = null;
            rt.volSeriesMap.clear();
        }

        // Ensure company names
        const selectedTickersDiv = ctx.elements?.selectedTickersDiv;
        ensureNames(Array.from(ctx.selectedTickers), selectedTickersDiv?.querySelectorAll('.chip'));

        // Fetch price data with auto-interval selection
        try {
            const tickerList = Array.from(ctx.selectedTickers);

            // Determine optimal interval
            let interval = 'daily';
            if (ctx.manualInterval && ctx.manualInterval !== 'auto') {
                interval = ctx.manualInterval;
                console.log(`Using manual interval: ${interval}`);
            } else if (ctx.visibleRange) {
                const rangeSeconds = ctx.visibleRange.to - ctx.visibleRange.from;
                const rangeDays = rangeSeconds / (24 * 3600);

                if (rangeDays > 3650) {
                    interval = 'monthly';
                    console.log(`Auto-selected monthly interval for ${Math.floor(rangeDays / 365)} year range`);
                } else if (rangeDays > 1825) {
                    interval = 'weekly';
                    console.log(`Auto-selected weekly interval for ${Math.floor(rangeDays / 365)} year range`);
                }
            }

            console.log(`Fetching data for ${tickerList.length} tickers: ${tickerList.join(', ')} (interval: ${interval})`);
            const data = await window.DataFetcher.getData(tickerList, 5475, interval, { signal: plotSignal });

            if (plotSignal.aborted) {
                console.log('[plot] Aborted during data fetch');
                return;
            }

            if (!data || Object.keys(data).length === 0) {
                console.warn('No data received');
                return;
            }

            // Process each ticker
            window.ChartSeriesManager.setupPriceSeries(
                rt.chart, tickerList, data, rt.priceSeriesMap, rt.rawPriceMap, rt.latestRebasedData,
                {
                    hiddenTickers: ctx.hiddenTickers,
                    tickerColorMap: ctx.tickerColorMap,
                    multiplierMap: ctx.multiplierMap,
                    priceScaleAssignmentMap: ctx.priceScaleAssignmentMap,
                    useRaw: ctx.useRaw,
                    lastLabelVisible: ctx.lastLabelVisible,
                    decimalPrecision: ctx.decimalPrecision
                }
            );

            // Volatility (σ) pane
            if (ctx.showVolPane) {
                if (plotSignal.aborted) return; // Early exit if cancelled
                const result = await window.ChartVolumeManager.setupVolatilityPane(
                    rt.chart, tickerList, rt.volPane, rt.volSeriesMap,
                    {
                        rawPriceMap: rt.rawPriceMap,
                        tickerColorMap: ctx.tickerColorMap,
                        hiddenTickers: ctx.hiddenTickers,
                        visibleRange: ctx.visibleRange,
                        lastLabelVisible: ctx.lastLabelVisible
                    },
                    (paneName, op) => withRangePreservation(ctx, paneName, op),
                    config.VOL_WINDOW
                );
                rt.volPane = result.volPane;
            }

            // Trading Volume pane
            if (ctx.showVolumePane) {
                if (plotSignal.aborted) return; // Early exit if cancelled
                const result = await window.ChartVolumeManager.setupTradingVolumePane(
                    rt.chart, tickerList, rt.volumePane, rt.volumeSeriesMap,
                    {
                        tickerColorMap: ctx.tickerColorMap,
                        hiddenTickers: ctx.hiddenTickers,
                        visibleRange: ctx.visibleRange,
                        lastLabelVisible: ctx.lastLabelVisible,
                        stretchFactor: ctx.volumePaneStretchFactor
                    },
                    (paneName, op) => withRangePreservation(ctx, paneName, op)
                );
                rt.volumePane = result.volumePane;
            }

            // Revenue pane
            if (ctx.showRevenuePane && window.FundamentalsPane) {
                if (plotSignal.aborted) return; // Early exit if cancelled
                const result = await window.FundamentalsPane.setupRevenuePane(
                    rt.chart, tickerList, rt.revenuePane, rt.revenueSeriesMap,
                    {
                        tickerColorMap: ctx.tickerColorMap,
                        hiddenTickers: ctx.hiddenTickers,
                        visibleRange: ctx.visibleRange,
                        lastLabelVisible: ctx.lastLabelVisible,
                        stretchFactor: ctx.revenuePaneStretchFactor,
                        signal: plotSignal
                    },
                    (paneName, op) => withRangePreservation(ctx, paneName, op)
                );
                rt.revenuePane = result.revenuePane;
            }

            // Fundamentals pane
            if (ctx.showFundamentalsPane && window.FundamentalsPane) {
                if (plotSignal.aborted) return; // Early exit if cancelled
                const result = await window.FundamentalsPane.setupFundamentalsPane(
                    rt.chart, tickerList, rt.fundamentalsPane, rt.fundamentalSeriesMap,
                    {
                        hiddenTickers: ctx.hiddenTickers,
                        visibleRange: ctx.visibleRange,
                        stretchFactor: ctx.fundamentalsPaneStretchFactor,
                        activeMetrics: ctx.fundamentalsMetrics,
                        signal: plotSignal
                    },
                    (paneName, op) => withRangePreservation(ctx, paneName, op)
                );
                rt.fundamentalsPane = result.fundamentalsPane;
            }

            // Average series
            if (ctx.showAvg && !ctx.useRaw) {
                rt.avgSeries = window.ChartSeriesManager.updateAverageSeries(
                    rt.chart, rt.avgSeries, rt.priceSeriesMap, ctx.hiddenTickers, undefined, ctx.lastLabelVisible
                );
            }

            // Update ticker labels
            if (rt.tickerLabelsContainer) {
                const currentFontSize = window.ChartCardContext.getCurrentFontSize(ctx);
                const tickerData = ctx.useRaw ? rt.rawPriceMap : rt.latestRebasedData;

                if (ctx.useRaw || Object.keys(rt.latestRebasedData).length > 0) {
                    window.ChartTickerLabels.updateAllLabels(
                        rt.tickerLabelsContainer, rt.priceSeriesMap, ctx.tickerColorMap, ctx.hiddenTickers,
                        tickerData, rt.chart, ctx.lastTickerVisible, currentFontSize
                    );
                }

                // Subscribe to range changes for label updates
                if (rt.tickerLabelHandler) {
                    rt.chart.timeScale().unsubscribeVisibleTimeRangeChange(rt.tickerLabelHandler);
                }

                rt.tickerLabelHandler = () => {
                    if (ctx.useRaw && rt.tickerLabelsContainer && rt.chart) {
                        setTimeout(() => {
                            const fontSize = window.ChartCardContext.getCurrentFontSize(ctx);
                            window.ChartTickerLabels.updateAllLabels(
                                rt.tickerLabelsContainer, rt.priceSeriesMap, ctx.tickerColorMap, ctx.hiddenTickers,
                                rt.rawPriceMap, rt.chart, ctx.lastTickerVisible, fontSize
                            );
                        }, 50);
                    }
                };
                rt.chart.timeScale().subscribeVisibleTimeRangeChange(rt.tickerLabelHandler);
            }

            // Subscribe to save visible range changes
            if (rt.rangeSaveHandler) {
                rt.chart.timeScale().unsubscribeVisibleTimeRangeChange(rt.rangeSaveHandler);
            }
            rt.rangeSaveHandler = (visible) => {
                if (visible && visible.from && visible.to) {
                    const from = Math.round(visible.from);
                    const to = Math.round(visible.to);
                    ctx.visibleRange = { from, to };
                    window.ChartCardContext.syncToCard(ctx);
                    console.log(`[RangeSave:${ctx.cardId}] Visible time range changed => from ${from}, to ${to}`);
                    ctx.debouncedSaveCards();
                    if (ctx.showFixedLegend) {
                        updateFixedLegend(ctx);
                    }
                }
            };
            rt.chart.timeScale().subscribeVisibleTimeRangeChange(rt.rangeSaveHandler);

            // Setup range-based rebasing
            if (!ctx.useRaw) {
                const card = ctx.card;
                const pageNum = card.closest('[data-page]')?.dataset?.page || '1';
                const isVisible = card.closest('.page')?.classList?.contains('visible');
                console.log(`[Rebasing Setup] Chart on page ${pageNum}, visible: ${isVisible}, tickers: ${Array.from(ctx.selectedTickers).join(',')}`);

                if (rt.debouncedRebase) {
                    rt.chart.timeScale().unsubscribeVisibleTimeRangeChange(rt.debouncedRebase);
                    if (typeof rt.debouncedRebase.cancel === 'function') rt.debouncedRebase.cancel();
                }

                rt.debouncedRebase = window.ChartSeriesManager.setupRangeBasedRebasing(rt.chart, {
                    priceSeriesMap: rt.priceSeriesMap,
                    rawPriceMap: rt.rawPriceMap,
                    multiplierMap: ctx.multiplierMap,
                    latestRebasedData: rt.latestRebasedData,
                    showAvg: ctx.showAvg,
                    updateAverageSeries: () => {
                        if (ctx.showAvg) {
                            rt.avgSeries = window.ChartSeriesManager.updateAverageSeries(
                                rt.chart, rt.avgSeries, rt.priceSeriesMap, ctx.hiddenTickers, undefined, ctx.lastLabelVisible
                            );
                        }
                    },
                    onRebaseComplete: () => {
                        if (rt.tickerLabelsContainer) {
                            const fontSize = window.ChartCardContext.getCurrentFontSize(ctx);
                            window.ChartTickerLabels.updateAllLabels(
                                rt.tickerLabelsContainer, rt.priceSeriesMap, ctx.tickerColorMap, ctx.hiddenTickers,
                                rt.latestRebasedData, rt.chart, ctx.lastTickerVisible, fontSize
                            );
                        }
                    },
                    useRaw: () => ctx.useRaw
                });

                if (!isVisible) {
                    setTimeout(() => {
                        const visible = rt.chart.timeScale().getVisibleRange();
                        if (visible && rt.debouncedRebase) {
                            console.log(`[Rebasing] Forcing initial rebase for hidden chart on page ${pageNum}`);
                            rt.debouncedRebase(visible);
                        }
                    }, 100);
                }
            }

            // Apply saved or smart default visible range
            if (!rt.skipRangeApplication) {
                const saved = ctx.visibleRange || initialRange;
                const dataRange = getCurrentDataRange(ctx);
                const minCoverage = window.ChartConfig?.RANGE?.FIT_MIN_COVERAGE || 0;

                const applyRange = (rng, reason = 'saved') => {
                    try {
                        rt.chart.timeScale().setVisibleRange(rng);
                        console.log(`[RangeApply:${ctx.cardId}] Applied ${reason} range => from ${rng.from}, to ${rng.to}`);
                    } catch (e) {
                        rt.chart.timeScale().fitContent();
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
                        ctx.saveCards();
                    } else {
                        applyRange(saved, 'saved');
                    }
                } else if (dataRange) {
                    applyRange(dataRange, 'data');
                    ctx.visibleRange = dataRange;
                    window.ChartCardContext.syncToCard(ctx);
                    ctx.saveCards();
                } else {
                    rt.chart.timeScale().fitContent();
                }
            } else {
                console.log(`[RangeApply:${ctx.cardId}] Skipping automatic range application`);
                const saved = ctx.visibleRange;
                if (saved && saved.from && saved.to) {
                    try {
                        rt.chart.timeScale().setVisibleRange(saved);
                        console.log(`[RangeApply:${ctx.cardId}] Manually applied saved range => from ${saved.from}, to ${saved.to}`);
                    } catch (e) {
                        console.warn(`[RangeApply:${ctx.cardId}] Could not apply saved range:`, e);
                        rt.chart.timeScale().fitContent();
                    }
                }
                rt.skipRangeApplication = false;
            }

            // Ensure rightOffset is applied
            if (rt.chart && rt.chart.applyOptions) {
                rt.chart.applyOptions({
                    timeScale: { rightOffset: 3 }
                });
            }

        } catch (error) {
            console.error('Plot error:', error);
        } finally {
            // Update zero line if enabled
            setTimeout(() => updateZeroLine(ctx), 100);

            // Restore/create fixed legend if enabled
            setTimeout(() => {
                if (ctx.showFixedLegend && !rt.fixedLegendEl) {
                    console.log(`[Card:${ctx.cardId}] Restoring fixed legend after plot`);
                    rt.fixedLegendEl = window.ChartFixedLegend.createFixedLegend(chartBox, {
                        initialX: ctx.fixedLegendPos?.x || 10,
                        initialY: ctx.fixedLegendPos?.y || 10,
                        initialWidth: ctx.fixedLegendSize?.width || null,
                        initialHeight: ctx.fixedLegendSize?.height || null
                    });

                    rt.fixedLegendEl._onStateChange = (changes) => {
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
                        ctx.debouncedSaveCards();
                    };

                    window.ChartFixedLegend.show(rt.fixedLegendEl);
                }

                updateFixedLegend(ctx);
            }, 100);
        }

        if (endTiming) endTiming();
    }

    // Public API
    return {
        plot,
        destroyChart,
        destroyChartAndReplot,
        applyResize,
        updateZeroLine,
        updateFixedLegend,
        getCurrentDataRange,
        ensureNames,
        getName,
        withRangePreservation,
        nameCache  // Expose for card.js to access
    };
})();
