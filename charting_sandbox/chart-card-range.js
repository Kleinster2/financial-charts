/**
 * Chart Card Range Module
 *
 * Extracted from card.js - handles range/interval/fit functionality.
 * Uses ctx and ctx.runtime for state access.
 *
 * Exports: window.ChartCardRange
 */

window.ChartCardRange = (() => {

    /**
     * Handle fit button click - fit chart to full data range
     * @param {Object} ctx - Card context with runtime initialized
     */
    function handleFit(ctx) {
        const rt = ctx.runtime;
        if (!rt.chart) return;

        const dataRange = window.ChartCardPlot.getCurrentDataRange(ctx);
        if (dataRange) {
            try {
                rt.chart.timeScale().setVisibleRange(dataRange);
                ctx.visibleRange = dataRange;
                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
            } catch (e) {
                rt.chart.timeScale().fitContent();
            }
        } else {
            rt.chart.timeScale().fitContent();
        }
    }

    /**
     * Handle interval select change
     * @param {Object} ctx - Card context with runtime initialized
     * @param {Function} plot - Plot function to replot with new interval
     */
    function handleIntervalChange(ctx, plot) {
        const intervalSelect = ctx.elements.intervalSelect;
        if (!intervalSelect) return;

        const val = intervalSelect.value;
        ctx.manualInterval = val === 'auto' ? null : val;
        window.ChartCardContext.syncToCard(ctx);
        console.log(`Interval changed to: ${val}`);
        ctx.debouncedSaveCards();

        // Replot to fetch data with new interval
        if (ctx.selectedTickers.size > 0) {
            plot();
        }
    }

    /**
     * Handle range select change
     * @param {Object} ctx - Card context with runtime initialized
     */
    function handleRangeChange(ctx) {
        const rt = ctx.runtime;
        const rangeSelect = ctx.elements.rangeSelect;
        if (!rangeSelect) return;

        const val = rangeSelect.value;
        if (!val) return;

        // Temporarily unsubscribe from range changes to prevent interference
        if (rt.rangeSaveHandler && rt.chart && rt.chart.timeScale) {
            try {
                rt.chart.timeScale().unsubscribeVisibleTimeRangeChange(rt.rangeSaveHandler);
                console.log('[RangeSelect] Unsubscribed from range changes');
            } catch (_) { }
        }

        // Special case: if selecting 1995 (or any year before 2000), find earliest data across all series
        if (val === '1995' || (val !== 'ytd' && parseInt(val, 10) < 2000)) {
            handleEarlyYearRange(ctx, val);
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

        // Update ctx state FIRST
        ctx.visibleRange = { from, to };
        window.ChartCardContext.syncToCard(ctx);

        // Then set the visual range
        rt.chart.timeScale().setVisibleRange({ from, to });

        ctx.saveCards();

        // Resubscribe to range changes
        resubscribeRangeHandler(ctx);
    }

    /**
     * Handle early year range selection (before 2000) with fundamentals support
     * @param {Object} ctx - Card context
     * @param {string} val - Selected value
     */
    function handleEarlyYearRange(ctx, val) {
        const rt = ctx.runtime;

        // Find earliest timestamp across all series (price + fundamentals)
        let earliestTime = null;

        // Check price series
        rt.priceSeriesMap.forEach((series, ticker) => {
            try {
                const data = rt.rawPriceMap.get(ticker);
                if (data && data.length > 0 && data[0].time) {
                    const firstTime = data[0].time;
                    if (!earliestTime || firstTime < earliestTime) {
                        earliestTime = firstTime;
                    }
                }
            } catch (e) { /* ignore */ }
        });

        // Check fundamental series
        rt.fundamentalSeriesMap.forEach((series, seriesKey) => {
            try {
                if (ctx.showFundamentalsPane && !earliestTime) {
                    // Use 1996 as earliest for fundamentals (AAPL data goes back to 1996-04-01)
                    earliestTime = Date.UTC(1996, 0, 1) / 1000;
                }
            } catch (e) { /* ignore */ }
        });

        // If we have fundamental data showing, use 1996 as earliest
        if (ctx.showFundamentalsPane && rt.fundamentalSeriesMap.size > 0) {
            earliestTime = Date.UTC(1996, 0, 1) / 1000;
        }

        // Default to price data earliest if no fundamentals
        if (!earliestTime) {
            rt.chart.timeScale().fitContent();
            const timeScale = rt.chart.timeScale();
            const visibleRange = timeScale.getVisibleRange();
            if (visibleRange) {
                ctx.visibleRange = { from: visibleRange.from, to: visibleRange.to };
                window.ChartCardContext.syncToCard(ctx);
            }
            ctx.saveCards();
            resubscribeRangeHandler(ctx);
            return;
        }

        // Set flag to skip range restoration in pane operations
        ctx.skipRangeRestoration = true;

        // For fundamentals, we know the earliest data is 2005-06-30
        // Set explicit range to show all fundamental data
        const fundamentalsEarliest = Date.UTC(2005, 5, 30) / 1000;  // June 30, 2005
        const from = fundamentalsEarliest;
        const to = Math.floor(Date.now() / 1000);

        console.log(`[RangeSelect] Setting explicit range from ${new Date(from * 1000).toISOString()} to ${new Date(to * 1000).toISOString()}`);

        // Update ctx state
        ctx.visibleRange = { from, to };
        window.ChartCardContext.syncToCard(ctx);

        // Set the range
        rt.chart.timeScale().setVisibleRange({ from, to });

        // Verify what range was actually set
        setTimeout(() => {
            const actualRange = rt.chart.timeScale().getVisibleRange();
            if (actualRange) {
                console.log(`[RangeSelect] Actual visible range after setting: from ${new Date(actualRange.from * 1000).toISOString()} to ${new Date(actualRange.to * 1000).toISOString()}`);
                // Update with actual range if different
                ctx.visibleRange = { from: actualRange.from, to: actualRange.to };
                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
            }
        }, 100);

        // Resubscribe to range changes AFTER a delay
        setTimeout(() => {
            resubscribeRangeHandler(ctx);
            console.log('[RangeSelect] Resubscribed to range changes');
        }, 500);
    }

    /**
     * Resubscribe to range change handler
     * @param {Object} ctx - Card context
     */
    function resubscribeRangeHandler(ctx) {
        const rt = ctx.runtime;
        if (rt.rangeSaveHandler && rt.chart && rt.chart.timeScale) {
            try {
                rt.chart.timeScale().subscribeVisibleTimeRangeChange(rt.rangeSaveHandler);
            } catch (_) { }
        }
    }

    /**
     * Create range handlers bound to a specific card context
     * @param {Object} ctx - Card context with runtime initialized
     * @param {Object} callbacks - Callback functions
     * @param {Function} callbacks.plot - Plot function
     * @returns {Object} Range handler functions
     */
    function createRangeHandlers(ctx, callbacks) {
        const { plot } = callbacks;

        return {
            handleFit: () => handleFit(ctx),
            handleIntervalChange: () => handleIntervalChange(ctx, plot),
            handleRangeChange: () => handleRangeChange(ctx)
        };
    }

    return {
        handleFit,
        handleIntervalChange,
        handleRangeChange,
        createRangeHandlers
    };

})();
