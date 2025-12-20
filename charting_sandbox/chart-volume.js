/**
 * Chart Volume Manager
 * Handles volume pane creation and volume calculations
 */

window.ChartVolumeManager = {
    /**
     * Calculate volume data from price changes
     */
    calculateVolume(data, window = 100) {
        if (!data || data.length < 2) return [];
        
        const volData = [];
        for (let i = 1; i < data.length; i++) {
            const endIdx = i;
            const startIdx = Math.max(0, i - window);
            
            let sumSqReturns = 0;
            let count = 0;
            
            for (let j = startIdx + 1; j <= endIdx; j++) {
                const prevPrice = data[j - 1].value;
                const currPrice = data[j].value;
                if (prevPrice > 0) {
                    const dayReturn = Math.log(currPrice / prevPrice);
                    sumSqReturns += dayReturn * dayReturn;
                    count++;
                }
            }
            
            const variance = count > 0 ? sumSqReturns / count : 0;
            const annualizedVol = Math.sqrt(variance * 252) * 100;
            
            volData.push({
                time: data[i].time,
                value: annualizedVol
            });
        }
        
        return volData;
    },

    /**
     * Create or update volume pane
     */
    createVolumePaneIfNeeded(chart, volPane, preserveRange = null) {
        if (!volPane) {
            volPane = chart.addPane({
                height: 100,
                horzGridLines: { visible: true },
                vertGridLines: { visible: true }
            });

            // Restore range if provided
            if (preserveRange && preserveRange.from && preserveRange.to) {
                try {
                    chart.timeScale().setVisibleRange(preserveRange);
                    console.log('[VolumeManager] Restored range after pane creation: from ' + preserveRange.from + ', to ' + preserveRange.to);
                } catch (e) {
                    console.warn('[VolumeManager] Could not restore range:', e);
                }
            }
        }
        return volPane;
    },

    /**
     * Add volume series to the pane
     */
    addVolumeSeries(chart, volPane, ticker, volData, color, volSeriesMap, lastLabelVisible = true) {
        console.log(`[VolumeManager] Adding volume series for ${ticker}, data points: ${volData.length}`);

        let volSeries = volSeriesMap.get(ticker);
        if (!volSeries) {
            console.log(`[VolumeManager] Creating new volume series for ${ticker}`);
            try {
                // Create series on the volume pane directly using pane.addSeries()
                if (volPane && typeof volPane.addSeries === 'function') {
                    volSeries = volPane.addSeries(LightweightCharts.LineSeries, {
                        color: color,
                        lineWidth: 1,
                        priceLineVisible: false,
                        lastValueVisible: lastLabelVisible,
                        priceFormat: { type: 'price', precision: 1 }
                    });
                    console.log(`[VolumeManager] Series created on pane for ${ticker}`);
                } else {
                    console.error(`[VolumeManager] volPane does not have addSeries method`);
                    throw new Error('Invalid volPane object');
                }
                volSeriesMap.set(ticker, volSeries);
            } catch (e) {
                console.error(`[VolumeManager] Failed to create series for ${ticker}:`, e);
                throw e;
            }
        } else {
            console.log(`[VolumeManager] Updating existing volume series for ${ticker}`);
            volSeries.applyOptions({ color: color, lastValueVisible: lastLabelVisible });
        }

        try {
            volSeries.setData(volData);
            console.log(`[VolumeManager] Data set successfully for ${ticker}`);
        } catch (e) {
            console.error(`[VolumeManager] Failed to set data for ${ticker}:`, e);
            throw e;
        }

        return volSeries;
    },

    /**
     * Clear all volume series
     */
    clearVolumeSeries(chart, volPane, volSeriesMap) {
        // Remove pane first - this automatically removes all series on it
        if (volPane) {
            try {
                chart.removePane(volPane);
                console.log('[VolumeManager] Volume pane removed');
            } catch (e) {
                console.warn('[VolumeManager] Could not remove pane (may already be removed):', e);
            }
        }

        // Clear the map regardless
        if (volSeriesMap) {
            volSeriesMap.clear();
        }

        return null; // Return null for volPane
    },

    /**
     * Update all volume series with new data
     */
    updateAllVolumeSeries(chart, volPane, selectedTickers, rawPriceMap, tickerColorMap, volSeriesMap, hiddenTickers, lastLabelVisible = true) {
        if (!volPane) {
            console.warn('[VolumeManager] No volume pane to update');
            return;
        }

        selectedTickers.forEach(ticker => {
            if (hiddenTickers.has(ticker)) return;
            
            const rawData = rawPriceMap.get(ticker);
            if (!rawData || rawData.length < 2) return;
            
            const volData = this.calculateVolume(rawData);
            const color = tickerColorMap.get(ticker) || '#000000';
            
            this.addVolumeSeries(chart, volPane, ticker, volData, color, volSeriesMap, lastLabelVisible);
        });
    },

    /**
     * Setup volatility (σ) pane with all series for given tickers
     * High-level helper that orchestrates pane creation and series plotting
     *
     * @param {Object} chart - LightweightCharts instance
     * @param {Array} tickerList - Tickers to plot
     * @param {Object} volPane - Existing pane or null
     * @param {Map} volSeriesMap - Series map (mutated in place)
     * @param {Object} dataRefs - { rawPriceMap, tickerColorMap, hiddenTickers, visibleRange, lastLabelVisible }
     * @param {Function} withRangePreservation - Wrapper to preserve time range
     * @param {number} volWindow - Rolling window for volatility calculation
     * @returns {Promise<Object>} { volPane }
     */
    async setupVolatilityPane(chart, tickerList, volPane, volSeriesMap, dataRefs, withRangePreservation, volWindow = 100) {
        const { rawPriceMap, tickerColorMap, hiddenTickers, visibleRange, lastLabelVisible } = dataRefs;

        await withRangePreservation('volatility', async () => {
            volPane = window.ChartUtils.createPaneIfNeeded(chart, volPane, {
                name: 'VolatilityPane',
                createPane: () => chart.addPane({ height: 100, horzGridLines: { visible: true }, vertGridLines: { visible: true } }),
                visibleRange
            });

            for (const ticker of tickerList) {
                if (hiddenTickers.has(ticker)) continue;

                const rawData = rawPriceMap.get(ticker);
                if (!rawData || rawData.length < 2) {
                    console.warn(`[VolumeManager] Insufficient data for volatility calculation: ${ticker}`);
                    continue;
                }

                const volData = this.calculateVolume(rawData, volWindow);
                console.log(`[VolumeManager] Calculated ${volData.length} volatility points for ${ticker}`);

                if (volData.length === 0) {
                    console.warn(`[VolumeManager] No volatility data calculated for ${ticker}`);
                    continue;
                }

                const color = tickerColorMap.get(ticker);

                try {
                    this.addVolumeSeries(chart, volPane, ticker, volData, color, volSeriesMap, lastLabelVisible);
                    console.log(`[VolumeManager] Successfully added volatility series for ${ticker}`);
                } catch (e) {
                    console.error(`[VolumeManager] Failed to add volatility series for ${ticker}:`, e);
                }
            }
        });

        return { volPane };
    },

    /**
     * Handle volume data fetching from API
     */
    async fetchAndPlotVolume(ticker, color, chart, volPane, volSeriesMap, lastLabelVisible = true) {
        try {
            console.log(`[VolumeManager] Fetching volume data for ${ticker}`);
            const volData = await window.DataFetcher.getVolumeData(ticker);

            if (!volData || !volData.time || !volData.value) {
                console.warn(`[VolumeManager] No volume data received for ${ticker}`);
                return;
            }

            const formattedData = volData.time.map((t, i) => ({
                time: t,
                value: volData.value[i]
            }));

            this.addVolumeSeries(chart, volPane, ticker, formattedData, color, volSeriesMap, lastLabelVisible);
        } catch (error) {
            console.error(`[VolumeManager] Failed to fetch volume for ${ticker}:`, error);
        }
    },

    /**
     * Setup trading volume pane with all series for given tickers
     * High-level helper that orchestrates pane creation and series plotting
     *
     * @param {Object} chart - LightweightCharts instance
     * @param {Array} tickerList - Tickers to plot
     * @param {Object} volumePane - Existing pane or null
     * @param {Map} volumeSeriesMap - Series map (mutated in place)
     * @param {Object} dataRefs - { tickerColorMap, hiddenTickers, visibleRange, lastLabelVisible, stretchFactor, signal }
     * @param {Function} withRangePreservation - Wrapper to preserve time range
     * @returns {Promise<Object>} { volumePane }
     */
    async setupTradingVolumePane(chart, tickerList, volumePane, volumeSeriesMap, dataRefs, withRangePreservation) {
        const { tickerColorMap, hiddenTickers, visibleRange, lastLabelVisible, stretchFactor, signal } = dataRefs;

        // Early exit if already aborted
        if (signal?.aborted) return { volumePane };

        await withRangePreservation('trading volume', async () => {
            volumePane = window.ChartUtils.createPaneIfNeeded(chart, volumePane, {
                name: 'TradingVolumePane',
                stretchFactor: stretchFactor ?? 1.0,
                visibleRange
            });

            // Check abort after pane creation
            if (signal?.aborted) return;

            // Fetch and plot trading volume data for each ticker
            const volumePromises = tickerList
                .filter(ticker => !hiddenTickers.has(ticker))
                .map(async (ticker) => {
                    // Check abort before each fetch
                    if (signal?.aborted) return;

                    try {
                        console.log(`[TradingVolumePane] Fetching volume data for ${ticker}`);

                        const volumeData = await window.DataFetcher.getVolumeData([ticker], null, null, { signal });

                        // Check abort after fetch - skip series writes if aborted
                        if (signal?.aborted) return;

                        if (!volumeData || !volumeData[ticker]) {
                            console.warn(`[TradingVolumePane] No volume data received for ${ticker}`);
                            return;
                        }

                        const tickerVolumeData = volumeData[ticker];

                        if (!Array.isArray(tickerVolumeData) || tickerVolumeData.length === 0) {
                            console.warn(`[TradingVolumePane] Invalid or empty volume data for ${ticker}`);
                            return;
                        }

                        // Filter out null values
                        const formattedData = tickerVolumeData.filter(d => d.value != null);
                        const color = tickerColorMap.get(ticker) || '#000000';

                        // Create or update volume series
                        let volumeSeries = volumeSeriesMap.get(ticker);
                        if (!volumeSeries) {
                            console.log(`[TradingVolumePane] Creating new volume series for ${ticker}`);
                            if (volumePane && chart) {
                                volumeSeries = volumePane.addSeries(LightweightCharts.LineSeries, {
                                    color: color,
                                    lineWidth: 1,
                                    priceLineVisible: false,
                                    lastValueVisible: lastLabelVisible,
                                    priceScaleId: 'right',
                                    priceFormat: { type: 'volume' }
                                });

                                volumeSeries.priceScale().applyOptions({
                                    mode: LightweightCharts.PriceScaleMode.Logarithmic,
                                    autoScale: true,
                                    scaleMargins: { top: 0.1, bottom: 0.1 }
                                });

                                volumeSeriesMap.set(ticker, volumeSeries);
                                console.log(`[TradingVolumePane] Series created for ${ticker} with logarithmic scale`);
                            } else {
                                console.error(`[TradingVolumePane] volumePane or chart is not available`);
                                return;
                            }
                        } else {
                            console.log(`[TradingVolumePane] Updating existing volume series for ${ticker}`);
                            volumeSeries.applyOptions({ color: color, lastValueVisible: lastLabelVisible });
                        }

                        volumeSeries.setData(formattedData);
                        console.log(`[TradingVolumePane] Data set for ${ticker}, ${formattedData.length} points`);
                    } catch (error) {
                        // Silently ignore AbortError
                        if (error.name === 'AbortError') return;
                        console.error(`[TradingVolumePane] Failed to fetch/plot volume for ${ticker}:`, error);
                    }
                });

            await Promise.all(volumePromises);
        });

        return { volumePane };
    }
};
