/**
 * Ticker Label Manager
 * Creates custom HTML labels showing ticker symbols on the right side of the chart
 * at the last price level for each series.
 */

window.ChartTickerLabels = {
    /**
     * Create ticker labels container
     * @param {HTMLElement} chartContainer - The chart container element
     * @returns {HTMLElement} The labels container
     */
    createLabelsContainer(chartContainer) {
        // Find the actual chart element (canvas container) within chartContainer
        // LightweightCharts creates a div inside our container
        const container = document.createElement('div');
        container.className = 'ticker-labels-container';
        container.style.position = 'absolute';
        container.style.top = '0';
        container.style.left = '0';
        container.style.right = '0';
        container.style.bottom = '0';
        container.style.pointerEvents = 'none';
        container.style.zIndex = '10';
        chartContainer.style.position = 'relative';
        chartContainer.appendChild(container);
        return container;
    },

    /**
     * Create or update ticker label
     * @param {HTMLElement} container - Labels container
     * @param {string} ticker - Ticker symbol
     * @param {number} price - Last price value
     * @param {string} color - Ticker color
     * @param {Object} series - Series object for this ticker
     * @param {boolean} visible - Whether label should be visible
     * @param {number} fontSize - Font size in pixels
     * @returns {HTMLElement} The label element
     */
    createOrUpdateLabel(container, ticker, price, color, series, visible, fontSize = 12) {
        let label = container.querySelector(`[data-ticker="${ticker}"]`);

        if (!label) {
            label = document.createElement('div');
            label.className = 'ticker-label';
            label.setAttribute('data-ticker', ticker);
            label.style.position = 'absolute';
            label.style.right = '10px'; // Position near right edge in price scale area
            label.style.padding = '2px 6px';
            label.style.borderRadius = '3px';
            label.style.fontWeight = 'bold';
            label.style.fontSize = `${fontSize}px`;
            label.style.fontFamily = 'Trebuchet MS, sans-serif';
            label.style.whiteSpace = 'nowrap';
            label.style.transition = 'top 0.2s ease-out';
            label.textContent = ticker;
            container.appendChild(label);
        }

        // Update styling
        label.style.backgroundColor = color;
        label.style.color = this._getContrastColor(color);
        label.style.display = visible ? 'block' : 'none';
        label.style.fontSize = `${fontSize}px`;

        // Calculate vertical position using series coordinate conversion
        try {
            if (series && typeof series.priceToCoordinate === 'function') {
                const coordinate = series.priceToCoordinate(price);
                if (coordinate !== null && coordinate !== undefined) {
                    label.style.top = `${coordinate - (fontSize / 2)}px`;
                }
            }
        } catch (e) {
            console.warn(`[TickerLabels] Could not position label for ${ticker}:`, e);
        }

        return label;
    },

    /**
     * Update all ticker labels positions
     * @param {HTMLElement} container - Labels container
     * @param {Map} priceSeriesMap - Map of ticker to series
     * @param {Map} tickerColorMap - Map of ticker to color
     * @param {Set} hiddenTickers - Set of hidden tickers
     * @param {Object|Map} tickerDataSource - Latest data for each ticker (Object or Map)
     * @param {Object} chart - LightweightCharts instance
     * @param {boolean} labelsVisible - Whether labels should be shown
     * @param {number} fontSize - Font size in pixels
     */
    updateAllLabels(container, priceSeriesMap, tickerColorMap, hiddenTickers, tickerDataSource, chart, labelsVisible, fontSize = 12) {
        if (!container || !chart) return;

        const existingLabels = new Set();

        // Helper to get data from either Map or Object
        const getData = (ticker) => {
            if (tickerDataSource instanceof Map) {
                return tickerDataSource.get(ticker);
            } else {
                return tickerDataSource[ticker];
            }
        };

        // Get visible time range to find the last visible point
        let visibleTimeRange = null;
        try {
            if (chart && chart.timeScale) {
                visibleTimeRange = chart.timeScale().getVisibleRange();
            }
        } catch (e) {
            console.warn('[TickerLabels] Could not get visible range:', e);
        }

        // Update or create labels for each visible series
        priceSeriesMap.forEach((series, ticker) => {
            if (hiddenTickers.has(ticker)) return;

            const data = getData(ticker);
            if (!data || data.length === 0) return;

            // Find the last visible data point
            let lastPoint = data[data.length - 1];

            // If we have visible time range, find the rightmost visible point
            if (visibleTimeRange && visibleTimeRange.to) {
                const visibleData = data.filter(point => {
                    return point.time <= visibleTimeRange.to;
                });
                if (visibleData.length > 0) {
                    lastPoint = visibleData[visibleData.length - 1];
                }
            }

            const price = lastPoint.value;
            const color = tickerColorMap.get(ticker) || '#666';
            const visible = labelsVisible && !hiddenTickers.has(ticker);

            this.createOrUpdateLabel(container, ticker, price, color, series, visible, fontSize);
            existingLabels.add(ticker);
        });

        // Remove labels for tickers no longer in the chart
        const allLabels = container.querySelectorAll('.ticker-label');
        allLabels.forEach(label => {
            const ticker = label.getAttribute('data-ticker');
            if (!existingLabels.has(ticker)) {
                label.remove();
            }
        });
    },

    /**
     * Remove a specific ticker label
     * @param {HTMLElement} container - Labels container
     * @param {string} ticker - Ticker symbol to remove
     */
    removeLabel(container, ticker) {
        if (!container) return;
        const label = container.querySelector(`[data-ticker="${ticker}"]`);
        if (label) {
            label.remove();
        }
    },

    /**
     * Clear all ticker labels
     * @param {HTMLElement} container - Labels container
     */
    clearAllLabels(container) {
        if (!container) return;
        container.innerHTML = '';
    },

    /**
     * Show or hide all labels
     * @param {HTMLElement} container - Labels container
     * @param {boolean} visible - Whether labels should be visible
     */
    setLabelsVisibility(container, visible) {
        if (!container) return;
        const labels = container.querySelectorAll('.ticker-label');
        labels.forEach(label => {
            label.style.display = visible ? 'block' : 'none';
        });
    },

    /**
     * Update font size for all labels
     * @param {HTMLElement} container - Labels container
     * @param {number} fontSize - Font size in pixels
     */
    updateFontSize(container, fontSize) {
        if (!container) return;
        const labels = container.querySelectorAll('.ticker-label');
        labels.forEach(label => {
            label.style.fontSize = `${fontSize}px`;
        });
    },

    /**
     * Get contrasting text color (black or white) for a background color
     * @param {string} hexColor - Hex color string
     * @returns {string} '#000000' or '#FFFFFF'
     */
    _getContrastColor(hexColor) {
        // Convert hex to RGB
        const rgb = window.ChartConfig._hexToRgb(hexColor);
        if (!rgb) return '#FFFFFF';

        // Calculate relative luminance
        const luminance = (0.299 * rgb.r + 0.587 * rgb.g + 0.114 * rgb.b) / 255;

        // Return black for light backgrounds, white for dark
        return luminance > 0.5 ? '#000000' : '#FFFFFF';
    }
};

console.log('[ChartTickerLabels] Ticker labels module loaded');
