/**
 * Chart Card Toggles Module
 *
 * Extracted from card.js - handles all toggle button handlers.
 * Uses ctx and ctx.runtime for state access.
 *
 * Exports: window.ChartCardToggles
 */

window.ChartCardToggles = (() => {

    /**
     * Create toggle handlers for a card
     * @param {Object} ctx - Card context with runtime initialized
     * @param {Object} callbacks - Callback functions from card.js
     * @param {Function} callbacks.plot - Plot function
     * @param {Function} callbacks.destroyChartAndReplot - Destroy and replot function
     * @param {Function} callbacks.persistState - Persist state helper
     * @returns {Object} Toggle handlers dictionary
     */
    function createToggleHandlers(ctx, callbacks) {
        const { plot, destroyChartAndReplot, persistState } = callbacks;
        const elements = ctx.elements;
        const rt = ctx.runtime;

        return {
            diff: () => {
                persistState({ showDiff: !ctx.showDiff });
                elements.toggleDiffBtn.textContent = ctx.showDiff ? 'Hide Diff Pane' : 'Show Diff Pane';
            },

            vol: () => {
                ctx.showVolPane = !ctx.showVolPane;
                window.ChartCardContext.syncToCard(ctx);
                elements.toggleVolBtn.textContent = ctx.showVolPane ? 'Hide Vol (σ) Pane' : 'Show Vol (σ) Pane';
                destroyChartAndReplot();
            },

            volume: () => {
                ctx.showVolumePane = !ctx.showVolumePane;
                window.ChartCardContext.syncToCard(ctx);
                elements.toggleVolumeBtn.textContent = ctx.showVolumePane ? 'Hide Volume Pane' : 'Show Volume Pane';
                destroyChartAndReplot();
            },

            revenue: () => {
                ctx.showRevenuePane = !ctx.showRevenuePane;
                window.ChartCardContext.syncToCard(ctx);
                elements.toggleRevenueBtn.textContent = ctx.showRevenuePane ? 'Hide Revenue Pane' : 'Show Revenue Pane';
                destroyChartAndReplot();
            },

            fundamentalsPane: () => {
                ctx.showFundamentalsPane = !ctx.showFundamentalsPane;
                window.ChartCardContext.syncToCard(ctx);
                elements.toggleFundamentalsPaneBtn.textContent = ctx.showFundamentalsPane ? 'Hide Fundamentals Pane' : 'Show Fundamentals Pane';

                // Show/hide metric buttons based on pane state
                const metricButtonsDisplay = ctx.showFundamentalsPane ? 'inline-block' : 'none';
                if (elements.toggleRevenueMetricBtn) elements.toggleRevenueMetricBtn.style.display = metricButtonsDisplay;
                if (elements.toggleNetIncomeMetricBtn) elements.toggleNetIncomeMetricBtn.style.display = metricButtonsDisplay;
                if (elements.toggleEpsMetricBtn) elements.toggleEpsMetricBtn.style.display = metricButtonsDisplay;
                if (elements.toggleFcfMetricBtn) elements.toggleFcfMetricBtn.style.display = metricButtonsDisplay;

                destroyChartAndReplot();
            },

            raw: () => {
                ctx.useRaw = !ctx.useRaw;
                elements.toggleRawBtn.textContent = ctx.useRaw ? 'Show % Basis' : 'Show Raw';

                // Update price scale format immediately
                if (rt.chart && rt.chart.priceScale) {
                    const precision = ctx.decimalPrecision !== undefined ? ctx.decimalPrecision : 2;
                    const priceFormat = ctx.useRaw
                        ? {
                            type: 'custom', minMove: 0.01, formatter: (price) => {
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
                                const magDecimals = Math.abs(diff) >= 100 ? 0 : Math.abs(diff) >= 10 ? 1 : 2;
                                const dec = Math.min(magDecimals, precision);
                                return `${sign}${Math.abs(diff).toFixed(dec)}%`;
                            }
                        };

                    try {
                        rt.chart.priceScale('right').applyOptions({ priceFormat });
                    } catch (e) {
                        console.warn('[Card] Could not update price scale format:', e);
                    }
                }

                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
                plot();
                // Update zero line after mode change
                setTimeout(() => window.ChartCardPlot.updateZeroLine(ctx), 100);
            },

            logScale: () => {
                ctx.useLogScale = !ctx.useLogScale;
                elements.toggleLogScaleBtn.textContent = ctx.useLogScale ? 'Linear Scale' : 'Log Scale';

                // Apply log scale to chart
                if (rt.chart && rt.chart.priceScale) {
                    rt.chart.priceScale('right').applyOptions({
                        mode: ctx.useLogScale ? 1 : 0  // 0=Normal, 1=Logarithmic
                    });
                }

                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
            },

            lastLabel: () => {
                ctx.lastLabelVisible = !ctx.lastLabelVisible;
                console.log(`[Card:${ctx.cardId}] Last value label ${ctx.lastLabelVisible ? 'enabled' : 'disabled'}`);
                window.ChartDomBuilder.updateButtonStates(elements, window.ChartCardContext.getButtonStates(ctx));

                // Apply to all existing series
                rt.priceSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: ctx.lastLabelVisible }));
                if (rt.avgSeries) rt.avgSeries.applyOptions({ lastValueVisible: ctx.lastLabelVisible });
                if (rt.volPane && rt.volSeriesMap) {
                    rt.volSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: ctx.lastLabelVisible }));
                }
                if (rt.volumePane && rt.volumeSeriesMap) {
                    rt.volumeSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: ctx.lastLabelVisible }));
                }
                if (rt.revenuePane && rt.revenueSeriesMap) {
                    rt.revenueSeriesMap.forEach(s => s.applyOptions({ lastValueVisible: ctx.lastLabelVisible }));
                }

                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
            },

            lastTicker: () => {
                ctx.lastTickerVisible = !ctx.lastTickerVisible;
                console.log(`[Card:${ctx.cardId}] Last ticker label ${ctx.lastTickerVisible ? 'enabled' : 'disabled'}`);
                window.ChartDomBuilder.updateButtonStates(elements, window.ChartCardContext.getButtonStates(ctx));

                // Update ticker labels visibility
                if (rt.tickerLabelsContainer) {
                    window.ChartTickerLabels.setLabelsVisibility(rt.tickerLabelsContainer, ctx.lastTickerVisible);
                }

                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
            },

            zeroLine: () => {
                ctx.showZeroLine = !ctx.showZeroLine;
                console.log(`[Card:${ctx.cardId}] Zero line ${ctx.showZeroLine ? 'enabled' : 'disabled'}`);

                window.ChartCardPlot.updateZeroLine(ctx);

                window.ChartDomBuilder.updateButtonStates(elements, window.ChartCardContext.getButtonStates(ctx));
                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
            },

            reshuffleColors: () => {
                console.log(`[Card:${ctx.cardId}] Reshuffling colors`);

                // Create shuffled copy of colors array
                const shuffledColors = [...window.ChartConfig.COLORS].sort(() => Math.random() - 0.5);

                // Reassign random colors to all tickers
                const tickersArray = Array.from(ctx.selectedTickers);
                tickersArray.forEach((ticker, index) => {
                    ctx.tickerColorMap.set(ticker, shuffledColors[index % shuffledColors.length]);
                });

                // Update UI
                window.ChartDomBuilder.addTickerChips(
                    elements.selectedTickersDiv, ctx.selectedTickers, ctx.tickerColorMap, ctx.multiplierMap, ctx.hiddenTickers,
                    (ticker, chipEl) => {
                        // This callback needs to be provided by card.js
                        if (callbacks.handleChipRemove) {
                            callbacks.handleChipRemove(ticker, chipEl);
                        }
                    }
                );

                // Update chart series colors
                rt.priceSeriesMap.forEach((series, ticker) => {
                    const newColor = ctx.tickerColorMap.get(ticker);
                    if (newColor) {
                        series.applyOptions({
                            color: newColor,
                            lineColor: newColor
                        });
                    }
                });

                // Update ticker labels colors
                if (rt.tickerLabelsContainer) {
                    const currentFontSize = window.ChartCardContext.getCurrentFontSize(ctx);
                    window.ChartTickerLabels.updateAllLabels(
                        rt.tickerLabelsContainer, rt.priceSeriesMap, ctx.tickerColorMap, ctx.hiddenTickers,
                        ctx.useRaw ? rt.rawPriceMap : rt.latestRebasedData, rt.chart, ctx.lastTickerVisible,
                        currentFontSize
                    );
                }

                ctx.saveCards();
            },

            avg: () => {
                ctx.showAvg = !ctx.showAvg;
                elements.toggleAvgBtn.textContent = ctx.showAvg ? 'Hide Avg' : 'Show Avg';
                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();

                if (ctx.showAvg && !ctx.useRaw) {
                    rt.avgSeries = window.ChartSeriesManager.updateAverageSeries(
                        rt.chart, rt.avgSeries, rt.priceSeriesMap, ctx.hiddenTickers, undefined, ctx.lastLabelVisible
                    );
                } else if (rt.avgSeries) {
                    rt.chart.removeSeries(rt.avgSeries);
                    rt.avgSeries = null;
                }
            },

            fixedLegend: () => {
                ctx.showFixedLegend = !ctx.showFixedLegend;
                console.log(`[Card:${ctx.cardId}] Fixed legend ${ctx.showFixedLegend ? 'enabled' : 'disabled'}`);

                if (ctx.showFixedLegend) {
                    // Create fixed legend if it doesn't exist
                    if (!rt.fixedLegendEl) {
                        rt.fixedLegendEl = window.ChartFixedLegend.createFixedLegend(ctx.chartBox, {
                            initialX: ctx.fixedLegendPos?.x || 10,
                            initialY: ctx.fixedLegendPos?.y || 10,
                            initialWidth: ctx.fixedLegendSize?.width || null,
                            initialHeight: ctx.fixedLegendSize?.height || null
                        });

                        // Setup state change handler
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
                    }

                    // Show legend and update with latest values
                    window.ChartFixedLegend.show(rt.fixedLegendEl);
                    window.ChartCardPlot.updateFixedLegend(ctx);
                } else {
                    // Hide legend
                    if (rt.fixedLegendEl) {
                        window.ChartFixedLegend.hide(rt.fixedLegendEl);
                    }
                }

                window.ChartDomBuilder.updateButtonStates(elements, window.ChartCardContext.getButtonStates(ctx));
                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
            },

            legendTickers: () => {
                ctx.showLegendTickers = !ctx.showLegendTickers;
                console.log(`[Card:${ctx.cardId}] Legend tickers ${ctx.showLegendTickers ? 'enabled' : 'disabled'}`);

                // Update fixed legend to reflect new setting
                if (ctx.showFixedLegend && rt.fixedLegendEl) {
                    window.ChartCardPlot.updateFixedLegend(ctx);
                }

                window.ChartDomBuilder.updateButtonStates(elements, window.ChartCardContext.getButtonStates(ctx));
                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
            },

            notes: () => {
                const notesSection = elements.notesSection;
                const notesTextarea = elements.notesTextarea;

                const showNotes = notesSection.style.display !== 'none';
                notesSection.style.display = showNotes ? 'none' : 'block';
                ctx.showNotes = !showNotes;
                ctx.notes = notesTextarea.value;
                window.ChartCardContext.syncToCard(ctx);

                window.ChartDomBuilder.updateButtonStates(elements, { ...window.ChartCardContext.getButtonStates(ctx), showNotes: !showNotes });
                ctx.saveCards();
            }
        };
    }

    /**
     * Update metric button visual states
     * @param {Object} ctx - Card context
     */
    function updateMetricButtonStates(ctx) {
        const elements = ctx.elements;

        if (elements.toggleRevenueMetricBtn) {
            elements.toggleRevenueMetricBtn.style.fontWeight = ctx.fundamentalsMetrics.includes('revenue') ? 'bold' : 'normal';
            elements.toggleRevenueMetricBtn.style.opacity = ctx.fundamentalsMetrics.includes('revenue') ? '1' : '0.5';
        }
        if (elements.toggleNetIncomeMetricBtn) {
            elements.toggleNetIncomeMetricBtn.style.fontWeight = ctx.fundamentalsMetrics.includes('netincome') ? 'bold' : 'normal';
            elements.toggleNetIncomeMetricBtn.style.opacity = ctx.fundamentalsMetrics.includes('netincome') ? '1' : '0.5';
        }
        if (elements.toggleEpsMetricBtn) {
            elements.toggleEpsMetricBtn.style.fontWeight = ctx.fundamentalsMetrics.includes('eps') ? 'bold' : 'normal';
            elements.toggleEpsMetricBtn.style.opacity = ctx.fundamentalsMetrics.includes('eps') ? '1' : '0.5';
        }
        if (elements.toggleFcfMetricBtn) {
            elements.toggleFcfMetricBtn.style.fontWeight = ctx.fundamentalsMetrics.includes('fcf') ? 'bold' : 'normal';
            elements.toggleFcfMetricBtn.style.opacity = ctx.fundamentalsMetrics.includes('fcf') ? '1' : '0.5';
        }
    }

    /**
     * Create metric toggle function
     * @param {Object} ctx - Card context
     * @param {Function} plot - Plot function
     * @returns {Function} Toggle metric function
     */
    function createToggleMetric(ctx, plot) {
        return function toggleMetric(metricName) {
            const index = ctx.fundamentalsMetrics.indexOf(metricName);
            if (index > -1) {
                ctx.fundamentalsMetrics.splice(index, 1);
            } else {
                ctx.fundamentalsMetrics.push(metricName);
            }
            window.ChartCardContext.syncToCard(ctx);
            updateMetricButtonStates(ctx);
            ctx.saveCards();
            if (ctx.showFundamentalsPane) plot();
        };
    }

    /**
     * Initialize metric button visibility and states
     * @param {Object} ctx - Card context
     */
    function initMetricButtons(ctx) {
        const elements = ctx.elements;

        if (ctx.showFundamentalsPane) {
            if (elements.toggleRevenueMetricBtn) elements.toggleRevenueMetricBtn.style.display = 'inline-block';
            if (elements.toggleNetIncomeMetricBtn) elements.toggleNetIncomeMetricBtn.style.display = 'inline-block';
            if (elements.toggleEpsMetricBtn) elements.toggleEpsMetricBtn.style.display = 'inline-block';
            if (elements.toggleFcfMetricBtn) elements.toggleFcfMetricBtn.style.display = 'inline-block';
        }
        updateMetricButtonStates(ctx);
    }

    // Public API
    return {
        createToggleHandlers,
        createToggleMetric,
        updateMetricButtonStates,
        initMetricButtons
    };
})();
