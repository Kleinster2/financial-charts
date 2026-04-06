/**
 * chart-tic-dashboard.js - TIC (Treasury International Capital) Dashboard Component
 * Displays net foreign flows and holdings charts using Lightweight Charts
 */

window.ChartTicDashboard = {
    /**
     * Create a TIC dashboard card with two charts:
     * 1. Net foreign flows by asset class (rolling 12-month sum)
     * 2. Top foreign holders of US Treasuries (time series)
     */
    createTicDashboardCard(wrapperEl, options = {}) {
        const card = document.createElement('div');
        card.className = 'chart-card tic-dashboard-card';
        card.id = `tic-dashboard-${Date.now()}`;

        card.innerHTML = `
            <div class="dashboard-header">
                <h3>TIC — Foreign Capital Flows</h3>
                <div class="dashboard-controls">
                    <select class="tic-rolling-select">
                        <option value="3">3-Month Rolling</option>
                        <option value="6">6-Month Rolling</option>
                        <option value="12" selected>12-Month Rolling</option>
                        <option value="24">24-Month Rolling</option>
                    </select>
                    <button class="dashboard-refresh-btn">Refresh</button>
                </div>
            </div>
            <div class="tic-charts-container">
                <div class="tic-chart-section">
                    <h4>Net Foreign Purchases of US Long-Term Securities ($B)</h4>
                    <div class="tic-flows-chart" style="height: 350px;"></div>
                    <div class="tic-flows-legend"></div>
                </div>
                <div class="tic-chart-section">
                    <h4>Top Foreign Holders of US Treasuries ($B)</h4>
                    <div class="tic-holdings-chart" style="height: 350px;"></div>
                    <div class="tic-holdings-legend"></div>
                </div>
            </div>
        `;

        this.addStyles();

        // Event handlers
        const rollingSelect = card.querySelector('.tic-rolling-select');
        const refreshBtn = card.querySelector('.dashboard-refresh-btn');

        if (options.rolling) rollingSelect.value = options.rolling;

        rollingSelect.addEventListener('change', () => {
            this.loadFlows(card, parseInt(rollingSelect.value));
            if (window.saveCards) window.saveCards();
        });

        refreshBtn.addEventListener('click', () => {
            this.loadAll(card, parseInt(rollingSelect.value));
        });

        card._type = 'tic-dashboard';
        card._fullWidth = true;
        card._ticState = { rolling: parseInt(rollingSelect.value) };

        wrapperEl.appendChild(card);
        this.loadAll(card, parseInt(rollingSelect.value));

        return card;
    },

    async loadAll(card, rolling = 12) {
        await Promise.all([
            this.loadFlows(card, rolling),
            this.loadHoldings(card)
        ]);
    },

    async loadFlows(card, rolling = 12) {
        const container = card.querySelector('.tic-flows-chart');
        const legendEl = card.querySelector('.tic-flows-legend');
        if (!container) return;

        try {
            const baseUrl = window.API_BASE_URL || '';
            const resp = await fetch(`${baseUrl}/api/tic/flows?rolling=${rolling}`);
            const data = await resp.json();

            if (data.error) {
                container.innerHTML = `<div style="padding:20px;color:#999">${data.error}</div>`;
                return;
            }

            // Clear previous chart
            container.innerHTML = '';

            const chart = LightweightCharts.createChart(container, {
                width: container.clientWidth,
                height: 350,
                layout: { background: { type: 'solid', color: '#000000' }, textColor: '#d1d4dc' },
                grid: { vertLines: { visible: false }, horzLines: { color: '#1e222d' } },
                rightPriceScale: { borderColor: '#2a2e39' },
                timeScale: { borderColor: '#2a2e39', timeVisible: false },
                crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
            });

            const colors = {
                'Treasury': '#d32f2f',
                'Agency': '#ff9800',
                'Corporate': '#1976d2',
                'Equity': '#7b1fa2',
            };

            const seriesMap = {};
            for (const [name, color] of Object.entries(colors)) {
                if (data[name] && data[name].length > 0) {
                    const series = chart.addSeries(LightweightCharts.LineSeries, {
                        color: color,
                        lineWidth: 2,
                        title: name,
                        priceFormat: { type: 'custom', formatter: v => `$${v.toFixed(0)}B` },
                        lastValueVisible: false,
                        priceLineVisible: false,
                    });
                    series.setData(data[name]);
                    seriesMap[name] = { series, color };
                }
            }

            // Zero line
            const baseline = chart.addSeries(LightweightCharts.LineSeries, {
                color: '#999',
                lineWidth: 1,
                lineStyle: LightweightCharts.LineStyle.Dashed,
                priceLineVisible: false,
                lastValueVisible: false,
            });
            if (data['Treasury'] && data['Treasury'].length > 0) {
                baseline.setData(data['Treasury'].map(d => ({ time: d.time, value: 0 })));
            }

            chart.timeScale().fitContent();

            // Build legend
            legendEl.innerHTML = Object.entries(colors).map(([name, color]) => {
                const latest = data[name]?.[data[name].length - 1]?.value;
                const val = latest != null ? `$${latest.toFixed(0)}B` : '';
                return `<span class="tic-legend-item" style="color:${color}">● ${name} ${val}</span>`;
            }).join('');

            // Responsive — also refit on first real resize (hidden page init)
            let flowsFitted = container.clientWidth > 0;
            const resizeObserver = new ResizeObserver(() => {
                const w = container.clientWidth;
                if (w > 0) {
                    chart.applyOptions({ width: w });
                    if (!flowsFitted) { chart.timeScale().fitContent(); flowsFitted = true; }
                }
            });
            resizeObserver.observe(container);
            card._flowsChart = chart;
            card._flowsResize = resizeObserver;

            card._ticState = { ...card._ticState, rolling };

        } catch (err) {
            console.error('[TIC] Flows load error:', err);
            container.innerHTML = `<div style="padding:20px;color:#c00">Failed to load TIC flows data</div>`;
        }
    },

    async loadHoldings(card) {
        const container = card.querySelector('.tic-holdings-chart');
        const legendEl = card.querySelector('.tic-holdings-legend');
        if (!container) return;

        try {
            const baseUrl = window.API_BASE_URL || '';
            const resp = await fetch(`${baseUrl}/api/tic/holdings?limit=6`);
            const data = await resp.json();

            if (data.error) {
                container.innerHTML = `<div style="padding:20px;color:#999">${data.error}</div>`;
                return;
            }

            container.innerHTML = '';

            const chart = LightweightCharts.createChart(container, {
                width: container.clientWidth,
                height: 350,
                layout: { background: { type: 'solid', color: '#000000' }, textColor: '#d1d4dc' },
                grid: { vertLines: { visible: false }, horzLines: { color: '#1e222d' } },
                rightPriceScale: { borderColor: '#2a2e39' },
                timeScale: { borderColor: '#2a2e39', timeVisible: false },
                crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
            });

            const palette = ['#1976d2', '#d32f2f', '#ff9800', '#4caf50', '#7b1fa2', '#00bcd4'];
            const legendParts = [];
            let colorIdx = 0;

            for (const [country, points] of Object.entries(data)) {
                if (country === 'meta' || !Array.isArray(points) || points.length === 0) continue;

                const color = palette[colorIdx % palette.length];
                const series = chart.addSeries(LightweightCharts.LineSeries, {
                    color: color,
                    lineWidth: 2,
                    title: country,
                    priceFormat: { type: 'custom', formatter: v => `$${v.toFixed(0)}B` },
                    lastValueVisible: false,
                    priceLineVisible: false,
                });
                series.setData(points);

                const latest = points[points.length - 1]?.value;
                legendParts.push(`<span class="tic-legend-item" style="color:${color}">● ${country} $${latest?.toFixed(0) || '?'}B</span>`);
                colorIdx++;
            }

            chart.timeScale().fitContent();
            legendEl.innerHTML = legendParts.join('');

            let holdingsFitted = container.clientWidth > 0;
            const resizeObserver = new ResizeObserver(() => {
                const w = container.clientWidth;
                if (w > 0) {
                    chart.applyOptions({ width: w });
                    if (!holdingsFitted) { chart.timeScale().fitContent(); holdingsFitted = true; }
                }
            });
            resizeObserver.observe(container);
            card._holdingsChart = chart;
            card._holdingsResize = resizeObserver;

        } catch (err) {
            console.error('[TIC] Holdings load error:', err);
            container.innerHTML = `<div style="padding:20px;color:#c00">Failed to load TIC holdings data</div>`;
        }
    },

    addStyles() {
        if (document.getElementById('tic-dashboard-styles')) return;
        const style = document.createElement('style');
        style.id = 'tic-dashboard-styles';
        style.textContent = `
            .tic-dashboard-card {
                background: #000;
                border: 1px solid #2a2e39;
                border-radius: 4px;
                padding: 16px;
                color: #d1d4dc;
            }
            .tic-dashboard-card .dashboard-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 16px;
            }
            .tic-dashboard-card .dashboard-header h3 {
                margin: 0;
                font-size: 16px;
            }
            .tic-dashboard-card .dashboard-controls {
                display: flex;
                gap: 8px;
                align-items: center;
            }
            .tic-charts-container {
                display: flex;
                flex-direction: row;
                gap: 16px;
            }
            .tic-chart-section {
                flex: 1;
                min-width: 0;
            }
            .tic-chart-section h4 {
                margin: 0 0 8px 0;
                font-size: 13px;
                color: #888;
                font-weight: 500;
            }
            .tic-flows-legend, .tic-holdings-legend {
                display: flex;
                gap: 16px;
                flex-wrap: wrap;
                margin-top: 8px;
                font-size: 12px;
            }
            .tic-legend-item {
                font-weight: 500;
            }
            .tic-rolling-select {
                padding: 4px 8px;
                border: 1px solid #2a2e39;
                border-radius: 4px;
                font-size: 13px;
                background: #1e222d;
                color: #d1d4dc;
            }
        `;
        document.head.appendChild(style);
    },

    /**
     * Get save state for workspace persistence
     */
    getSaveState(card) {
        return {
            type: 'tic-dashboard',
            rolling: card._ticState?.rolling || 12,
        };
    },
};
