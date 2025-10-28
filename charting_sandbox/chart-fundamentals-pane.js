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
     * @returns {Promise<Object>} - Data for each ticker and metric
     */
    async function fetchFundamentalsChartData(tickers, metrics = ['revenue', 'netIncome', 'eps', 'fcf']) {
        try {
            const tickersParam = tickers.join(',');
            const metricsParam = metrics.join(',');
            const url = `http://localhost:5000/api/fundamentals/chart?tickers=${tickersParam}&metrics=${metricsParam}`;

            console.log(`[FundamentalsPane] Fetching chart data: ${url}`);

            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();
            console.log(`[FundamentalsPane] Received data for ${Object.keys(data).length} tickers`);
            return data;

        } catch (error) {
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
     */
    async function plotFundamentalsPane(pane, tickers, activeMetrics, seriesMap, hiddenTickers = {}) {
        console.log(`[FundamentalsPane] Plotting ${tickers.length} tickers, ${activeMetrics.length} metrics`);

        // Fetch data for all tickers and active metrics
        const data = await fetchFundamentalsChartData(tickers, activeMetrics);

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

    // Expose functions globally
    window.FundamentalsPane = {
        plot: plotFundamentalsPane,
        toggleMetric: toggleMetric,
        updateVisibility: updateSeriesVisibility,
        clear: clearPane,
        getDisplayName: getMetricDisplayName
    };

    console.log('[FundamentalsPane] Module loaded');

})();
