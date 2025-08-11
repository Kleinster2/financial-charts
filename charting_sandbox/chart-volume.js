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
    createVolumePaneIfNeeded(chart, volPane) {
        if (!volPane) {
            volPane = chart.addPane({
                height: 100,
                horzGridLines: { visible: true },
                vertGridLines: { visible: true }
            });
        }
        return volPane;
    },

    /**
     * Add volume series to the pane
     */
    addVolumeSeries(chart, volPane, ticker, volData, color, volSeriesMap) {
        console.log(`[VolumeManager] Adding volume series for ${ticker}`);
        
        let volSeries = volSeriesMap.get(ticker);
        if (!volSeries) {
            volSeries = chart.addSeries(LightweightCharts.LineSeries, {
                color: color,
                lineWidth: 1,
                pane: volPane,
                priceScaleId: 'volume',
                priceFormat: { type: 'price', precision: 1 }
            });
            volSeriesMap.set(ticker, volSeries);
        } else {
            volSeries.applyOptions({ color: color });
        }
        
        volSeries.setData(volData);
        return volSeries;
    },

    /**
     * Clear all volume series
     */
    clearVolumeSeries(chart, volPane, volSeriesMap) {
        if (volSeriesMap) {
            volSeriesMap.forEach(series => {
                chart.removeSeries(series);
            });
            volSeriesMap.clear();
        }
        
        if (volPane) {
            chart.removePane(volPane);
        }
        
        return null; // Return null for volPane
    },

    /**
     * Update all volume series with new data
     */
    updateAllVolumeSeries(chart, volPane, selectedTickers, rawPriceMap, tickerColorMap, volSeriesMap, hiddenTickers) {
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
            
            this.addVolumeSeries(chart, volPane, ticker, volData, color, volSeriesMap);
        });
    },

    /**
     * Handle volume data fetching from API
     */
    async fetchAndPlotVolume(ticker, color, chart, volPane, volSeriesMap) {
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

            this.addVolumeSeries(chart, volPane, ticker, formattedData, color, volSeriesMap);
        } catch (error) {
            console.error(`[VolumeManager] Failed to fetch volume for ${ticker}:`, error);
        }
    }
};
