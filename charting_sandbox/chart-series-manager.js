/**
 * Chart Series Manager
 * Manages chart series creation, updates, and rebasing
 */

window.ChartSeriesManager = {
    /**
     * Create or update a price series for a ticker
     */
    createOrUpdateSeries(chart, ticker, data, color, priceSeriesMap) {
        console.log(`[SeriesManager] Creating/updating series for ${ticker}`);
        
        let series = priceSeriesMap.get(ticker);
        if (!series) {
            series = chart.addSeries(LightweightCharts.LineSeries, {
                color: color,
                lineWidth: 2,
                priceScaleId: 'right',
                priceFormat: { type: 'price', precision: 2, minMove: 0.01 }
            });
            priceSeriesMap.set(ticker, series);
        } else {
            series.applyOptions({ color: color });
        }
        
        series.setData(data);
        return series;
    },

    /**
     * Rebase price data to percentage basis
     */
    rebaseData(rawData, multiplier = 1, baseValue = null) {
        if (!rawData || rawData.length === 0) return [];
        
        const base = baseValue !== null ? baseValue : rawData[0].value;
        if (base === 0) return rawData;
        
        return rawData.map(pt => {
            const norm = pt.value / base;
            const scaled = 1 + (norm - 1) * multiplier;
            return { time: pt.time, value: scaled * 100 };
        });
    },

    /**
     * Update average series from multiple tickers
     */
    updateAverageSeries(chart, avgSeries, priceSeriesMap, hiddenTickers, visibleRange) {
        const visibleSeries = Array.from(priceSeriesMap.entries())
            .filter(([t]) => !hiddenTickers.has(t));
        
        if (visibleSeries.length === 0) {
            if (avgSeries) {
                chart.removeSeries(avgSeries);
            }
            return null;
        }

        // Collect all data points
        const dataByTime = new Map();
        visibleSeries.forEach(([ticker, series]) => {
            try {
                // Get data from series (this is a placeholder - actual implementation depends on chart library)
                const data = series.data ? series.data() : [];
                data.forEach(pt => {
                    if (!dataByTime.has(pt.time)) {
                        dataByTime.set(pt.time, []);
                    }
                    dataByTime.get(pt.time).push(pt.value);
                });
            } catch (e) {
                console.warn(`[SeriesManager] Could not get data for ${ticker}:`, e);
            }
        });

        // Calculate averages
        const avgData = Array.from(dataByTime.entries())
            .map(([time, values]) => ({
                time,
                value: values.reduce((a, b) => a + b, 0) / values.length
            }))
            .sort((a, b) => a.time - b.time);

        // Create or update average series
        if (!avgSeries) {
            avgSeries = chart.addSeries(LightweightCharts.LineSeries, {
                color: '#000000',
                lineWidth: 3,
                priceScaleId: 'right',
                title: 'Average',
                lineStyle: 2 // Dashed line
            });
        }
        
        avgSeries.setData(avgData);
        return avgSeries;
    },

    /**
     * Handle visible range change for rebasing
     */
    setupRangeBasedRebasing(chart, options) {
        const {
            priceSeriesMap,
            rawPriceMap,
            multiplierMap,
            latestRebasedData,
            showAvg,
            updateAverageSeries,
            useRaw
        } = options;

        const debouncedRebase = this.debounce((visible) => {
            if (useRaw || !visible || !visible.from) return;

            const from = Math.round(visible.from);
            priceSeriesMap.forEach((series, ticker) => {
                const raw = rawPriceMap.get(ticker);
                if (!raw?.length) return;
                
                const first = raw.find(p => p.time >= from);
                if (!first || first.value === 0) return;
                
                const multiplier = multiplierMap.get(ticker) || 1;
                const rebased = this.rebaseData(raw, multiplier, first.value);
                series.setData(rebased);
                latestRebasedData[ticker] = rebased;
            });

            if (showAvg) {
                updateAverageSeries(visible);
            }
        }, 500);

        chart.timeScale().subscribeVisibleTimeRangeChange(debouncedRebase);
        return debouncedRebase;
    },

    /**
     * Debounce helper
     */
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    /**
     * Clear all series from chart
     */
    clearAllSeries(chart, priceSeriesMap, volSeriesMap = null, avgSeries = null) {
        priceSeriesMap.forEach(series => {
            chart.removeSeries(series);
        });
        priceSeriesMap.clear();

        if (volSeriesMap) {
            volSeriesMap.forEach(series => {
                chart.removeSeries(series);
            });
            volSeriesMap.clear();
        }

        if (avgSeries) {
            chart.removeSeries(avgSeries);
        }
    }
};
