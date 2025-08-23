/**
 * Chart Legend Manager
 * Handles floating legend display and crosshair interactions
 */

window.ChartLegend = {
    /**
     * Create floating legend element
     */
    createLegendElement(chartBox) {
        chartBox.style.position = 'relative';
        const legendEl = document.createElement('div');
        legendEl.className = 'floating-legend';
        // Create a container for the legend that will handle overflow
        const legendContainer = document.createElement('div');
        Object.assign(legendContainer.style, {
            position: 'absolute',
            top: '0',
            left: '0',
            width: '100%',
            height: '100%',
            pointerEvents: 'none',
            overflow: 'visible',
            zIndex: '1000'
        });
        
        // Style the legend element
        Object.assign(legendEl.style, {
            position: 'absolute',
            pointerEvents: 'none',
            background: 'rgba(255,255,255,0.95)',
            border: '1px solid #ccc',
            borderRadius: '4px',
            padding: '2px 4px',
            fontSize: '12px',
            display: 'none',
            whiteSpace: 'nowrap',
            boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
            maxHeight: '90vh',
            overflowY: 'auto',
            zIndex: '1001',
            transform: 'translateZ(0)' // Force hardware acceleration
        });
        
        // Add legend to container, and container to chart box
        legendContainer.appendChild(legendEl);
        chartBox.appendChild(legendContainer);

        return legendEl;
    },

    /**
     * Format percentage value for display
     */
    formatPct(val) {
        const diff = val - 100;
        const sign = diff > 0 ? '+' : diff < 0 ? '-' : '';
        const dec = Math.abs(diff) >= 100 ? 0 : 1;
        return `${sign}${Math.abs(diff).toFixed(dec)}%`;
    },

    /**
     * Format price value for display
     */
    formatPrice(v) {
        if (v >= 1000) return v.toFixed(0);
        if (v >= 100) return v.toFixed(1);
        return v.toFixed(2);
    },

    /**
     * Subscribe to crosshair movement and update legend
     */
    subscribeToCrosshair(chart, legendEl, options) {
        const {
            useRaw,
            priceSeriesMap,
            hiddenTickers,
            tickerColorMap,
            selectedTickers,
            rawPriceMap,
            latestRebasedData,
            getName
        } = options;

        const formatter = useRaw ? this.formatPrice : this.formatPct;

        const handler = (param) => {
            if (!param || !param.point || param.time === undefined) {
                legendEl.style.display = 'none';
                return;
            }

            let html = '';
            const rows = []; // {t, price, color} objects to sort later
            const time = param.time !== undefined ? 
                (typeof param.time === 'string' ? Date.parse(param.time)/1000 : param.time) : null;
            
            const isMap = param.seriesPrices && typeof param.seriesPrices.forEach === 'function';
            const iterate = isMap
                ? (cb) => param.seriesPrices.forEach((v, s) => cb(s, v))
                : (cb) => { if(param.seriesPrices){ for (const key in param.seriesPrices) cb(key, param.seriesPrices[key]); } };
            
            iterate((series, val) => {
                // Determine ticker (t) and price series object (ps)
                let t;
                let ps;
                if (series && typeof series.priceScale === 'function') {
                    // Map form: series is Lightweight Chart series object
                    const entry = Array.from(priceSeriesMap.entries()).find(([, s]) => s === series);
                    if (!entry) return;
                    [t, ps] = entry;
                } else {
                    // Object form: key is ticker string, need to get series from map
                    t = series;
                    ps = priceSeriesMap.get(t);
                    if (!ps) return;
                }
                if (hiddenTickers.has(t)) return;
                let price = typeof val === 'object' ? (val.close ?? val.value ?? val.open ?? val.high ?? val.low) : val;
                if (price == null || isNaN(price)) return;
                const color = tickerColorMap.get(t) || '#000';
                rows.push({t, price, color});
            });

            if (!html && time != null) {
                // Fallback: look up rebased values directly from stored data arrays
                selectedTickers.forEach(t => {
                    if (hiddenTickers.has(t)) return;
                    const arr = useRaw ? rawPriceMap.get(t) : latestRebasedData[t];
                    if (!arr) return;
                    const idx = arr.findIndex(p => p.time === time);
                    if (idx === -1) return;
                    const price = arr[idx].value;
                    if (price == null || isNaN(price)) return;
                    const color = tickerColorMap.get(t) || '#000';
                    rows.push({t, price, color});
                });
            }

            // Build legend HTML sorted by price descending
            if (rows.length) {
                rows.sort((a, b) => b.price - a.price);
                html = rows.map(({t, price, color}) => {
                    const label = typeof getName === 'function' ? (getName(t) || t) : t;
                    return `<div><span style="color:${color};font-weight:bold">${label}</span>: ${formatter(price)}</div>`;
                }).join('');
            }

            if (!html) {
                legendEl.style.display = 'none';
                return;
            }

            legendEl.innerHTML = html;
            legendEl.style.display = 'block';
            
            // Position legend
            const container = legendEl.closest('.chart-box') || legendEl.parentElement;
            const rect = container.getBoundingClientRect();
            const x = param.point.x;
            const y = param.point.y;
            const legendWidth = 150;
            const legendHeight = rows.length * 20 + 10;
            
            let left = x + 10;
            let top = y - legendHeight / 2;
            
            // Constrain legend to stay within chart boundaries with a buffer
            const buffer = 20; // pixels from edges
            
            if (left + legendWidth > rect.width) {
                left = rect.width - legendWidth - buffer;
            }
            if (left < buffer) left = buffer;
            
            if (top < buffer) top = buffer;
            if (top + legendHeight > rect.height - buffer) {
                top = rect.height - legendHeight - buffer;
            }
            
            legendEl.style.left = `${left}px`;
            legendEl.style.top = `${top}px`;
        };
        // attach handler and expose for cleanup
        chart.subscribeCrosshairMove(handler);
        return handler;
    }
};
