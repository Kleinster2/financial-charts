/**
 * chart-fundamentals-pane.js
 * Module for displaying fundamental metrics (Revenue, Net Income, EPS, FCF) in a chart pane
 */

(function() {
    'use strict';

    /**
     * Fetch fundamental chart data for tickers
     * @param {Array<string>} tickers - Array of ticker symbols
     * @param {Array<string>} metrics - Array of metric names (revenue, netIncome, eps, fcf)
     * @param {AbortSignal} signal - Optional abort signal for cancellation
     * @returns {Promise<Object>} - Data for each ticker and metric
     */
    async function fetchFundamentalsChartData(tickers, metrics = ['revenue', 'netIncome', 'eps', 'fcf'], signal = null) {
        try {
            const tickersParam = tickers.join(',');
            const metricsParam = metrics.join(',');
            const url = window.ChartUtils.apiUrl(`/api/fundamentals/chart?tickers=${tickersParam}&metrics=${metricsParam}`);

            console.log(`[FundamentalsPane] Fetching chart data: ${url}`);

            const response = await fetch(url, signal ? { signal } : {});
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();
            console.log(`[FundamentalsPane] Received data for ${Object.keys(data).length} tickers`);
            return data;

        } catch (error) {
            if (error.name === 'AbortError') {
                console.log('[FundamentalsPane] Fetch aborted');
                return {};
            }
            console.error('[FundamentalsPane] Error fetching data:', error);
            return {};
        }
    }

    /**
     * Create or update fundamental metrics series on a chart pane
     * @param {Object} pane - LightweightCharts pane instance
     * @param {string} ticker - Ticker symbol
     * @param {string} metric - Metric name (revenue, netIncome, etc.)
     * @param {Array} data - Array of {time, value} objects
     * @param {string} color - Line color
     * @param {Map} seriesMap - Map to store series references
     * @param {boolean} visible - Whether series should be visible
     * @returns {Object} - The created/updated series
     */
    function createOrUpdateSeries(pane, ticker, metric, data, color, seriesMap, visible = true) {
        const seriesKey = `${ticker}_${metric}`;
        let series = seriesMap.get(seriesKey);

        if (!series) {
            // Create new line series using LightweightCharts v5 API
            series = pane.addSeries(LightweightCharts.LineSeries, {
                color: color,
                lineWidth: 2,
                title: `${ticker} ${metric}`,
                priceFormat: {
                    type: 'volume',  // Use volume format for large numbers (adds K, M, B suffixes)
                },
                visible: visible,
                lastValueVisible: true,
                priceLineVisible: false,
                priceScaleId: 'right'
            });

            // Configure logarithmic scale for better visualization of large numbers
            series.priceScale().applyOptions({
                mode: LightweightCharts.PriceScaleMode.Logarithmic,
                autoScale: true,
                scaleMargins: {
                    top: 0.1,
                    bottom: 0.1
                }
            });

            seriesMap.set(seriesKey, series);
            console.log(`[FundamentalsPane] Created series: ${seriesKey}`);
        } else {
            // Update existing series
            series.applyOptions({
                color: color,
                visible: visible
            });
        }

        // Set data
        if (data && data.length > 0) {
            series.setData(data);
            console.log(`[FundamentalsPane] Set ${data.length} data points for ${seriesKey}`);
        }

        return series;
    }

    /**
     * Get color for a metric/ticker combination
     */
    function getMetricColor(ticker, metric, tickerIndex, metricIndex) {
        // Color palettes for each metric
        const colorPalettes = {
            revenue: ['#2962FF', '#1E88E5', '#1976D2', '#1565C0'],      // Blues
            netincome: ['#00C853', '#00E676', '#69F0AE', '#B9F6CA'],    // Greens
            eps: ['#FF6D00', '#FF9100', '#FFB74D', '#FFCC80'],          // Oranges
            fcf: ['#AA00FF', '#D500F9', '#E040FB', '#EA80FC']           // Purples
        };

        const palette = colorPalettes[metric.toLowerCase()] || ['#666', '#888', '#AAA', '#CCC'];
        return palette[tickerIndex % palette.length];
    }

    /**
     * Create metric display name
     */
    function getMetricDisplayName(metric) {
        const displayNames = {
            revenue: 'Revenue',
            netincome: 'Net Income',
            eps: 'EPS',
            fcf: 'Free Cash Flow',
            operatingincome: 'Operating Income',
            ebitda: 'EBITDA',
            grossprofit: 'Gross Profit',
            operatingcashflow: 'Operating CF'
        };
        return displayNames[metric.toLowerCase()] || metric;
    }

    /**
     * Plot fundamentals on a pane
     * @param {Object} pane - LightweightCharts pane
     * @param {Array<string>} tickers - Tickers to plot
     * @param {Array<string>} activeMetrics - Metrics to display
     * @param {Map} seriesMap - Map to store series
     * @param {Object} hiddenTickers - Map of hidden tickers
     * @param {AbortSignal} signal - Optional abort signal for cancellation
     */
    async function plotFundamentalsPane(pane, tickers, activeMetrics, seriesMap, hiddenTickers = {}, signal = null) {
        console.log(`[FundamentalsPane] Plotting ${tickers.length} tickers, ${activeMetrics.length} metrics`);

        // Fetch data for all tickers and active metrics
        const data = await fetchFundamentalsChartData(tickers, activeMetrics, signal);

        // Check if aborted after fetch
        if (signal?.aborted) {
            console.log('[FundamentalsPane] Plot aborted after fetch');
            return;
        }

        // Plot each ticker's metrics
        tickers.forEach((ticker, tickerIndex) => {
            const tickerData = data[ticker];
            if (!tickerData) {
                console.warn(`[FundamentalsPane] No data for ${ticker}`);
                return;
            }

            const isHidden = hiddenTickers[ticker] === true;

            activeMetrics.forEach((metric, metricIndex) => {
                const metricData = tickerData[metric.toLowerCase()];
                if (!metricData || metricData.length === 0) {
                    console.warn(`[FundamentalsPane] No ${metric} data for ${ticker}`);
                    return;
                }

                const color = getMetricColor(ticker, metric, tickerIndex, metricIndex);
                const visible = !isHidden;

                createOrUpdateSeries(
                    pane,
                    ticker,
                    metric,
                    metricData,
                    color,
                    seriesMap,
                    visible
                );
            });
        });

        console.log(`[FundamentalsPane] Plotted ${seriesMap.size} series`);
    }

    /**
     * Toggle metric visibility
     */
    function toggleMetric(metric, seriesMap, tickers, isActive) {
        tickers.forEach(ticker => {
            const seriesKey = `${ticker}_${metric}`;
            const series = seriesMap.get(seriesKey);
            if (series) {
                series.applyOptions({ visible: isActive });
                console.log(`[FundamentalsPane] ${isActive ? 'Showing' : 'Hiding'} ${seriesKey}`);
            }
        });
    }

    /**
     * Update series visibility based on hidden tickers
     */
    function updateSeriesVisibility(seriesMap, hiddenTickers) {
        seriesMap.forEach((series, seriesKey) => {
            const ticker = seriesKey.split('_')[0];
            const isHidden = hiddenTickers[ticker] === true;
            series.applyOptions({ visible: !isHidden });
        });
    }

    /**
     * Clear all series from pane
     */
    function clearPane(pane, seriesMap) {
        seriesMap.forEach((series, key) => {
            try {
                pane.removeSeries(series);
            } catch (e) {
                console.warn(`[FundamentalsPane] Error removing series ${key}:`, e);
            }
        });
        seriesMap.clear();
        console.log('[FundamentalsPane] Cleared all series');
    }

    /**
     * Setup revenue pane with all series for given tickers
     * High-level helper that orchestrates pane creation and series plotting
     *
     * @param {Object} chart - LightweightCharts instance
     * @param {Array} tickerList - Tickers to plot
     * @param {Object} revenuePane - Existing pane or null
     * @param {Map} revenueSeriesMap - Series map (mutated in place)
     * @param {Object} dataRefs - { tickerColorMap, hiddenTickers, visibleRange, lastLabelVisible, stretchFactor, signal }
     * @param {Function} withRangePreservation - Wrapper to preserve time range
     * @returns {Promise<Object>} { revenuePane }
     */
    async function setupRevenuePane(chart, tickerList, revenuePane, revenueSeriesMap, dataRefs, withRangePreservation) {
        const { tickerColorMap, hiddenTickers, visibleRange, lastLabelVisible, stretchFactor, signal } = dataRefs;

        await withRangePreservation('revenue', async () => {
            revenuePane = window.ChartUtils.createPaneIfNeeded(chart, revenuePane, {
                name: 'RevenuePane',
                stretchFactor: stretchFactor ?? 1.0,
                visibleRange
            });

            // Filter to visible tickers only
            const visibleTickers = tickerList.filter(ticker => !hiddenTickers.has(ticker));
            if (visibleTickers.length === 0) return;

            // Check if aborted before fetching
            if (signal?.aborted) return;

            // Batch fetch all tickers in single request
            console.log(`[RevenuePane] Fetching revenue data for ${visibleTickers.length} tickers: ${visibleTickers.join(', ')}`);
            const url = window.ChartUtils.apiUrl(`/api/revenue?tickers=${visibleTickers.join(',')}`);

            let revenueData;
            try {
                const response = await fetch(url, signal ? { signal } : {});
                if (!response.ok) {
                    console.warn(`[RevenuePane] Failed to fetch revenue: ${response.status}`);
                    return;
                }
                revenueData = await response.json();
            } catch (error) {
                if (error.name === 'AbortError') {
                    console.log('[RevenuePane] Fetch aborted');
                    return;
                }
                console.error('[RevenuePane] Failed to fetch revenue:', error);
                return;
            }

            // Check if aborted after fetch
            if (signal?.aborted) return;

            // Plot each ticker's data
            for (const ticker of visibleTickers) {
                const tickerRevenueData = revenueData[ticker];
                if (!Array.isArray(tickerRevenueData) || tickerRevenueData.length === 0) {
                    console.warn(`[RevenuePane] No revenue data for ${ticker}`);
                    continue;
                }

                // Filter out null values
                const formattedData = tickerRevenueData.filter(d => d.value != null);
                const color = tickerColorMap.get(ticker) || '#000000';

                // Create or update revenue series
                let revenueSeries = revenueSeriesMap.get(ticker);
                if (!revenueSeries) {
                    if (revenuePane && chart) {
                        revenueSeries = revenuePane.addSeries(LightweightCharts.LineSeries, {
                            color: color,
                            lineWidth: 2,
                            priceLineVisible: false,
                            lastValueVisible: lastLabelVisible,
                            priceScaleId: 'right',
                            priceFormat: { type: 'volume' }
                        });

                        revenueSeries.priceScale().applyOptions({
                            mode: LightweightCharts.PriceScaleMode.Logarithmic,
                            autoScale: true,
                            scaleMargins: { top: 0.1, bottom: 0.1 }
                        });

                        revenueSeriesMap.set(ticker, revenueSeries);
                        console.log(`[RevenuePane] Created series for ${ticker}`);
                    } else {
                        console.error('[RevenuePane] revenuePane or chart is not available');
                        continue;
                    }
                } else {
                    revenueSeries.applyOptions({ color: color, lastValueVisible: lastLabelVisible });
                }

                revenueSeries.setData(formattedData);
                console.log(`[RevenuePane] Set ${formattedData.length} quarters for ${ticker}`);
            }

            console.log(`[RevenuePane] Plotted ${visibleTickers.length} tickers`);
        });

        return { revenuePane };
    }

    /**
     * Setup fundamentals pane with all series for given tickers
     * High-level helper that orchestrates pane creation and series plotting
     *
     * @param {Object} chart - LightweightCharts instance
     * @param {Array} tickerList - Tickers to plot
     * @param {Object} fundamentalsPane - Existing pane or null
     * @param {Map} fundamentalSeriesMap - Series map (mutated in place)
     * @param {Object} dataRefs - { hiddenTickers, visibleRange, stretchFactor, activeMetrics, signal }
     * @param {Function} withRangePreservation - Wrapper to preserve time range
     * @returns {Promise<Object>} { fundamentalsPane }
     */
    async function setupFundamentalsPane(chart, tickerList, fundamentalsPane, fundamentalSeriesMap, dataRefs, withRangePreservation) {
        const { hiddenTickers, visibleRange, stretchFactor, activeMetrics, signal } = dataRefs;

        await withRangePreservation('fundamentals', async () => {
            fundamentalsPane = window.ChartUtils.createPaneIfNeeded(chart, fundamentalsPane, {
                name: 'FundamentalsPane',
                stretchFactor: stretchFactor ?? 1.0,
                visibleRange
            });

            // Build hiddenTickersMap (plot() expects object, not Set)
            const hiddenTickersMap = {};
            hiddenTickers.forEach(ticker => { hiddenTickersMap[ticker] = true; });

            // Plot fundamentals
            try {
                await plotFundamentalsPane(
                    fundamentalsPane,
                    tickerList,
                    activeMetrics,
                    fundamentalSeriesMap,
                    hiddenTickersMap,
                    signal
                );
                console.log(`[FundamentalsPane] Plotted ${tickerList.length} tickers with ${activeMetrics.length} metrics`);
            } catch (error) {
                if (error.name === 'AbortError') {
                    console.log('[FundamentalsPane] Plot aborted');
                    return;
                }
                console.error('[FundamentalsPane] Error plotting fundamentals:', error);
            }
        });

        return { fundamentalsPane };
    }

    // Expose functions globally
    window.FundamentalsPane = {
        plot: plotFundamentalsPane,
        toggleMetric: toggleMetric,
        updateVisibility: updateSeriesVisibility,
        clear: clearPane,
        getDisplayName: getMetricDisplayName,
        setupRevenuePane: setupRevenuePane,
        setupFundamentalsPane: setupFundamentalsPane
    };

    console.log('[FundamentalsPane] Module loaded');

})();
