/**
 * Chart Updaters Module
 * Helper functions for updating chart elements (zero line, fixed legend, etc.)
 */

window.ChartUpdaters = {
    /**
     * Update zero line visibility and position
     */
    updateZeroLine(chart, zeroLineSeries, showZeroLine, useRaw) {
        if (!chart) return zeroLineSeries;

        if (showZeroLine) {
            if (!zeroLineSeries) {
                zeroLineSeries = chart.addSeries(window.LightweightCharts.LineSeries, {
                    color: '#666666',
                    lineWidth: 1,
                    lineStyle: window.LightweightCharts.LineStyle.Dashed,
                    lastValueVisible: false,
                    priceLineVisible: false,
                    crosshairMarkerVisible: false,
                    title: ''
                });
            }

            // Update zero line data based on current mode
            const zeroValue = useRaw ? 0 : 100; // 0 for raw prices, 100 for percentage

            // Get visible time range
            const timeScale = chart.timeScale();
            const visibleRange = timeScale.getVisibleRange();

            if (visibleRange) {
                // Create horizontal line across visible range
                const lineData = [
                    { time: visibleRange.from, value: zeroValue },
                    { time: visibleRange.to, value: zeroValue }
                ];
                zeroLineSeries.setData(lineData);
            } else {
                // Fallback: use wide time range
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

        return zeroLineSeries;
    },

    /**
     * Update fixed legend with latest values
     */
    updateFixedLegend(fixedLegendEl, showFixedLegend, options) {
        if (!showFixedLegend || !fixedLegendEl) return;

        const {
            selectedTickers,
            hiddenTickers,
            useRaw,
            rawPriceMap,
            latestRebasedData,
            tickerColorMap,
            getName
        } = options;

        const legendData = [];
        selectedTickers.forEach(ticker => {
            if (hiddenTickers.has(ticker)) return;

            // Get latest value
            const dataArray = useRaw ? rawPriceMap.get(ticker) : latestRebasedData[ticker];
            if (!dataArray || dataArray.length === 0) return;

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
            getName
        });
    },

    /**
     * Create crosshair handler for fixed legend dual mode
     */
    createFixedLegendCrosshairHandler(fixedLegendEl, showFixedLegend, updateFixedLegendFn, options) {
        const {
            selectedTickers,
            hiddenTickers,
            useRaw,
            rawPriceMap,
            latestRebasedData,
            tickerColorMap,
            getName
        } = options;

        return (param) => {
            if (!showFixedLegend || !fixedLegendEl) return;

            // If hovering, show crosshair values; otherwise show latest
            if (param && param.point && param.time !== undefined) {
                const legendData = [];
                const time = param.time !== undefined ?
                    (typeof param.time === 'string' ? Date.parse(param.time) / 1000 : param.time) : null;

                selectedTickers.forEach(ticker => {
                    if (hiddenTickers.has(ticker)) return;

                    // Get value at crosshair time
                    const dataArray = useRaw ? rawPriceMap.get(ticker) : latestRebasedData[ticker];
                    if (!dataArray) return;

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
                        getName
                    });
                }
            } else {
                // Not hovering, show latest values
                updateFixedLegendFn();
            }
        };
    }
};
