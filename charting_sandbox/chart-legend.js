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
        Object.assign(legendEl.style, {
            position: 'absolute',
            pointerEvents: 'none',
            background: 'rgba(255,255,255,0.85)',
            border: '1px solid #ccc',
            borderRadius: '4px',
            padding: '2px 4px',
            fontSize: '12px',
            display: 'none',
            zIndex: 1000,
            whiteSpace: 'nowrap',
        });
        chartBox.appendChild(legendEl);
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
            latestRebasedData
        } = options;

        const formatter = useRaw ? this.formatPrice : this.formatPct;

        chart.subscribeCrosshairMove(param => {
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
                html = rows.map(({t, price, color}) => 
                    `<div><span style="color:${color};font-weight:bold">${t}</span>: ${formatter(price)}</div>`
                ).join('');
            }

            if (!html) {
                legendEl.style.display = 'none';
                return;
            }

            legendEl.innerHTML = html;
            legendEl.style.display = 'block';
            
            // Position legend
            const rect = chartBox.getBoundingClientRect();
            const x = param.point.x;
            const y = param.point.y;
            const legendWidth = 150;
            const legendHeight = rows.length * 20 + 10;
            
            let left = x + 10;
            let top = y - legendHeight / 2;
            
            if (left + legendWidth > rect.width) {
                left = x - legendWidth - 10;
            }
            if (top < 0) top = 10;
            if (top + legendHeight > rect.height) {
                top = rect.height - legendHeight - 10;
            }
            
            legendEl.style.left = `${left}px`;
            legendEl.style.top = `${top}px`;
        });
    }
};
