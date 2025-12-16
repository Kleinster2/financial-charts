/**
 * Thesis Performance Card Module
 * Displays P&L performance chart for investment theses with weighted ticker tracking
 */

window.ChartThesisPerformance = {
    /**
     * Create a thesis performance card
     */
    createThesisPerformanceCard(wrapperEl, options = {}) {
        const card = document.createElement('div');
        card.className = 'chart-card thesis-performance-card';
        card.id = `thesis-perf-${Date.now()}`;
        card._type = 'thesis-performance';
        card._thesisId = options.thesisId || null;

        card.innerHTML = `
            <div class="thesis-perf-header">
                <div class="thesis-perf-title-row">
                    <select class="thesis-selector">
                        <option value="">Select a thesis...</option>
                    </select>
                    <span class="thesis-perf-title"></span>
                    <span class="thesis-perf-pnl"></span>
                </div>
                <div class="thesis-perf-weights"></div>
            </div>
            <div class="thesis-perf-chart-container"></div>
            <div class="thesis-perf-legend"></div>
        `;

        this.addStyles();
        wrapperEl.appendChild(card);

        // Load thesis list and initialize
        this.loadThesisList(card).then(() => {
            if (options.thesisId) {
                card.querySelector('.thesis-selector').value = options.thesisId;
                this.loadThesisPerformance(card, options.thesisId);
            }
        });

        // Event listener for thesis selection
        card.querySelector('.thesis-selector').addEventListener('change', (e) => {
            const thesisId = e.target.value;
            card._thesisId = thesisId || null;
            if (thesisId) {
                this.loadThesisPerformance(card, thesisId);
            } else {
                this.clearChart(card);
            }
        });

        return card;
    },

    addStyles() {
        window.ChartUtils.ensureStyleTag('thesis-perf-styles', `
            .thesis-performance-card {
                background: #1e1e1e;
                border-radius: 8px;
                padding: 16px;
                margin-bottom: 16px;
            }
            .thesis-perf-header {
                margin-bottom: 12px;
            }
            .thesis-perf-title-row {
                display: flex;
                align-items: center;
                gap: 12px;
                margin-bottom: 8px;
            }
            .thesis-selector {
                background: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #444;
                border-radius: 4px;
                padding: 6px 10px;
                font-size: 13px;
                min-width: 200px;
            }
            .thesis-perf-title {
                font-size: 16px;
                font-weight: 600;
                color: #e0e0e0;
            }
            .thesis-perf-pnl {
                font-size: 18px;
                font-weight: 700;
                padding: 4px 10px;
                border-radius: 4px;
            }
            .thesis-perf-pnl.positive {
                background: rgba(76, 175, 80, 0.2);
                color: #4caf50;
            }
            .thesis-perf-pnl.negative {
                background: rgba(244, 67, 54, 0.2);
                color: #f44336;
            }
            .thesis-perf-weights {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                font-size: 12px;
            }
            .thesis-weight-badge {
                background: #2d2d2d;
                padding: 4px 8px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
            }
            .thesis-weight-badge .ticker {
                font-weight: 600;
                color: #e0e0e0;
            }
            .thesis-weight-badge .weight {
                color: #888;
            }
            .thesis-weight-badge .pnl {
                font-weight: 500;
            }
            .thesis-weight-badge .pnl.positive { color: #4caf50; }
            .thesis-weight-badge .pnl.negative { color: #f44336; }
            .thesis-perf-chart-container {
                height: 300px;
                background: #1a1a1a;
                border-radius: 4px;
            }
            .thesis-perf-legend {
                margin-top: 8px;
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                font-size: 11px;
                color: #888;
            }
            .thesis-legend-item {
                display: flex;
                align-items: center;
                gap: 4px;
            }
            .thesis-legend-color {
                width: 12px;
                height: 3px;
                border-radius: 1px;
            }
        `);
    },

    async loadThesisList(card) {
        try {
            const response = await fetch(window.ChartUtils.apiUrl('/api/theses'));
            const theses = await response.json();
            const selector = card.querySelector('.thesis-selector');

            theses.forEach(thesis => {
                const option = document.createElement('option');
                option.value = thesis.id;
                option.textContent = `${thesis.title} (${thesis.status})`;
                selector.appendChild(option);
            });
        } catch (err) {
            console.error('Failed to load theses:', err);
        }
    },

    async loadThesisPerformance(card, thesisId) {
        try {
            const response = await fetch(window.ChartUtils.apiUrl(`/api/theses/${thesisId}/performance`));
            if (!response.ok) {
                const err = await response.json();
                console.error('Performance API error:', err);
                return;
            }
            const data = await response.json();
            this.renderPerformance(card, data);
        } catch (err) {
            console.error('Failed to load thesis performance:', err);
        }
    },

    renderPerformance(card, data) {
        // Update title
        card.querySelector('.thesis-perf-title').textContent = data.title;

        // Get latest P&L
        const latestPerf = data.performance[data.performance.length - 1];
        const pnlEl = card.querySelector('.thesis-perf-pnl');
        if (latestPerf) {
            const pnl = latestPerf.weighted_pnl_percent;
            pnlEl.textContent = `${pnl >= 0 ? '+' : ''}${pnl.toFixed(2)}%`;
            pnlEl.className = `thesis-perf-pnl ${pnl >= 0 ? 'positive' : 'negative'}`;
        }

        // Render weight badges with individual P&L
        const weightsEl = card.querySelector('.thesis-perf-weights');
        weightsEl.innerHTML = '';
        if (latestPerf && latestPerf.tickers) {
            latestPerf.tickers.forEach(t => {
                const badge = document.createElement('div');
                badge.className = 'thesis-weight-badge';
                badge.innerHTML = `
                    <span class="ticker">${t.ticker}</span>
                    <span class="weight">${t.weight}%</span>
                    <span class="pnl ${t.pnl_percent >= 0 ? 'positive' : 'negative'}">
                        ${t.pnl_percent >= 0 ? '+' : ''}${t.pnl_percent.toFixed(1)}%
                    </span>
                `;
                weightsEl.appendChild(badge);
            });
        }

        // Render chart
        this.renderChart(card, data);
    },

    renderChart(card, data) {
        const container = card.querySelector('.thesis-perf-chart-container');
        container.innerHTML = '';

        if (!window.LightweightCharts) {
            console.error('LightweightCharts not loaded');
            return;
        }

        const chart = LightweightCharts.createChart(container, {
            width: container.clientWidth,
            height: 300,
            layout: {
                background: { color: '#1a1a1a' },
                textColor: '#888'
            },
            grid: {
                vertLines: { color: '#2d2d2d' },
                horzLines: { color: '#2d2d2d' }
            },
            crosshair: {
                mode: LightweightCharts.CrosshairMode.Normal
            },
            rightPriceScale: {
                borderColor: '#2d2d2d'
            },
            timeScale: {
                borderColor: '#2d2d2d',
                timeVisible: true
            }
        });

        // Store chart reference for cleanup
        card._chart = chart;

        // Main weighted P&L line
        const mainSeries = chart.addLineSeries({
            color: '#2196f3',
            lineWidth: 2,
            title: 'Weighted P&L'
        });

        // Convert data to chart format
        const mainData = data.performance.map(p => ({
            time: p.date.split(' ')[0], // Extract date part
            value: p.weighted_pnl_percent
        }));
        mainSeries.setData(mainData);

        // Add zero line
        const zeroLine = chart.addLineSeries({
            color: '#666',
            lineWidth: 1,
            lineStyle: 2, // Dashed
            priceLineVisible: false,
            lastValueVisible: false
        });
        zeroLine.setData(mainData.map(d => ({ time: d.time, value: 0 })));

        // Individual ticker lines (lighter, thinner)
        const tickerColors = ['#ff9800', '#4caf50', '#e91e63', '#9c27b0', '#00bcd4'];
        const legendEl = card.querySelector('.thesis-perf-legend');
        legendEl.innerHTML = `
            <div class="thesis-legend-item">
                <div class="thesis-legend-color" style="background: #2196f3"></div>
                <span>Weighted P&L</span>
            </div>
        `;

        // Get unique tickers from first data point
        if (data.performance.length > 0 && data.performance[0].tickers) {
            const tickers = data.performance[0].tickers.map(t => t.ticker);
            const tickerSeries = []; // Store series references for legend toggle

            tickers.forEach((ticker, i) => {
                const color = tickerColors[i % tickerColors.length];
                const series = chart.addLineSeries({
                    color: color,
                    lineWidth: 1,
                    title: ticker,
                    visible: false // Hidden by default
                });
                tickerSeries.push(series);

                // Build ticker-specific data
                const tickerData = data.performance.map(p => {
                    const tickerInfo = p.tickers.find(t => t.ticker === ticker);
                    return {
                        time: p.date.split(' ')[0],
                        value: tickerInfo ? tickerInfo.pnl_percent : null
                    };
                }).filter(d => d.value !== null);

                series.setData(tickerData);

                // Add to legend
                legendEl.innerHTML += `
                    <div class="thesis-legend-item" data-ticker="${ticker}" style="cursor: pointer; opacity: 0.5">
                        <div class="thesis-legend-color" style="background: ${color}"></div>
                        <span>${ticker}</span>
                    </div>
                `;
            });

            // Toggle ticker visibility on legend click
            legendEl.querySelectorAll('.thesis-legend-item[data-ticker]').forEach((item, i) => {
                item.addEventListener('click', () => {
                    const series = tickerSeries[i];
                    if (series) {
                        const visible = item.style.opacity === '1';
                        item.style.opacity = visible ? '0.5' : '1';
                        series.applyOptions({ visible: !visible });
                    }
                });
            });
        }

        // Fit content
        chart.timeScale().fitContent();

        // Handle resize
        const resizeObserver = new ResizeObserver(() => {
            chart.applyOptions({ width: container.clientWidth });
        });
        resizeObserver.observe(container);
        card._resizeObserver = resizeObserver;
    },

    clearChart(card) {
        if (card._chart) {
            card._chart.remove();
            card._chart = null;
        }
        if (card._resizeObserver) {
            card._resizeObserver.disconnect();
            card._resizeObserver = null;
        }
        card.querySelector('.thesis-perf-title').textContent = '';
        card.querySelector('.thesis-perf-pnl').textContent = '';
        card.querySelector('.thesis-perf-pnl').className = 'thesis-perf-pnl';
        card.querySelector('.thesis-perf-weights').innerHTML = '';
        card.querySelector('.thesis-perf-legend').innerHTML = '';
    }
};
