document.addEventListener('DOMContentLoaded', () => {
    const workspaceContainer = document.getElementById('workspace-container');
    // Top-level "Add New Chart" button may be absent
    const addChartBtn = document.getElementById('add-chart-btn');
    let chartCards = []; // Global list of chart card instances
    let availableTickers = [];

    // --- Main Setup ---
    async function initializeWorkspace() {
        await fetchAvailableTickers();
        loadWorkspace();
        if (addChartBtn) {
            addChartBtn.addEventListener('click', () => createNewChart());
        }
    }

    async function fetchAvailableTickers() {
        try {
            const response = await fetch('/api/tickers');
            availableTickers = await response.json();
            // Populate the global datalist for ticker autocomplete
            const datalist = document.getElementById('ticker-list');
            if (datalist) {
                datalist.innerHTML = '';
                availableTickers.forEach(ticker => {
                    const opt = document.createElement('option');
                    opt.value = ticker;
                    datalist.appendChild(opt);
                });
            }
        } catch (error) {
            console.error('Failed to fetch tickers:', error);
            alert('Could not load ticker list.');
        }
    }

    // --- ChartCard Class ---
    const BASE_HEIGHT = 400; // px
const EXTRA_PER_TICKER = 25; // px per ticker beyond threshold
const HEIGHT_THRESHOLD = 6;  // start enlarging at 7th ticker

class ChartCard {
        constructor(container, id, tickers = []) {
            this.container = container;
            this.id = id;
            this.tickers = new Set(tickers);
            this.raw_data = {};
            // Color palette for distinct series lines
            this.colorPalette = [
                '#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd',
                '#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf',
                '#393b79','#637939','#8c6d31','#843c39','#7b4173',
                '#3182bd','#f33f48','#ffbb78','#98df8a','#ff9896',
                '#c5b0d5','#c49c94','#f7b6d2','#c7c7c7','#dbdb8d',
                '#9edae5','#5254a3','#8ca252','#bd9e39','#ad494a'
            ];
            this.colorIndex = 0;
            this.diffChartSeries = {};
            this.chartSeries = {};
            // Remove diff chart series
            for (const t in this.diffChartSeries) { this.diffChart.removeSeries(this.diffChartSeries[t]); }
            this.diffChartSeries = {};
            if (this.averageSeries) {
                this.chart.removeSeries(this.averageSeries);
            }
            this.averageSeries = null;

            this.element = document.getElementById('chart-card-template').content.cloneNode(true).firstElementChild;
            this.element.dataset.id = this.id;
            this.container.appendChild(this.element);

            // Create crosshair legend overlay
            this.legendDiv = document.createElement('div');
            this.legendDiv.className = 'crosshair-legend';
            this.legendDiv.style.display = 'none';
            this.element.appendChild(this.legendDiv);

            this.chartContainer = this.element.querySelector('.chart-container');
            this.chart = LightweightCharts.createChart(this.chartContainer, {
                width: this.chartContainer.clientWidth,
            
                layout: { background: { type: 'solid', color: '#ffffff' }, textColor: 'rgba(0, 0, 0, 0.9)' },
                grid: { vertLines: { color: 'rgba(197, 203, 206, 0.5)' }, horzLines: { color: 'rgba(197, 203, 206, 0.5)' } },
                crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
                timeScale: { borderColor: 'rgba(197, 203, 206, 0.8)', timeVisible: true, secondsVisible: false },
                rightPriceScale: { 
                    mode: LightweightCharts.PriceScaleMode.Logarithmic,
                    borderColor: 'rgba(197, 203, 206, 0.8)',
                    entireTextOnly: true,
                    alignLabels: false, // This is the key to hiding the labels
                    formatter: (price) => {
                        const diff = price - 100;
                        const sign = diff > 0 ? '+' : diff < 0 ? '-' : '';
                        const decimals = Math.abs(diff) >= 100 ? 0 : 1;
                        return `${sign}${Math.abs(diff).toFixed(decimals)}%`;
                    }
                },
            });

            // Create diff chart for deviations from average
            this.diffChartContainer = this.element.querySelector('.diff-chart-container');
            // --- Diff Chart ---
            this.diffChart = LightweightCharts.createChart(this.diffChartContainer, {
                width: this.diffChartContainer.clientWidth,
            
                layout: { background: { type: 'solid', color: '#ffffff' }, textColor: 'rgba(0, 0, 0, 0.8)' },
                grid: { vertLines: { color: 'rgba(197, 203, 206, 0.2)' }, horzLines: { color: 'rgba(197, 203, 206, 0.2)' } },
                crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
                timeScale: { borderColor: 'rgba(197, 203, 206, 0.8)' },
            });
            // Configure right price scale for diffChart
            this.diffChart.priceScale('right').applyOptions({
                entireTextOnly: true,
                tickMarkFormatter: (v) => {
                    const sign = v > 0 ? '+' : v < 0 ? '-' : '';
                    const decimals = Math.abs(v) >= 100 ? 0 : 1;
                    return `${sign}${Math.abs(v).toFixed(decimals)}%`;
                }
            });

            // Mirror left price scale for diffChart using transparent series
            this.diffMirrorSeries = this.diffChart.addLineSeries({
                priceScaleId: 'left',
                color: 'rgba(0,0,0,0)',
                lineWidth: 1,
                lastValueVisible: false,
                priceLineVisible: false,
                priceFormat: {
                    type: 'custom',
                    minMove: 0.1,
                    formatter: (v) => {
                        const sign = v > 0 ? '+' : v < 0 ? '-' : '';
                        const decimals = Math.abs(v) >= 100 ? 0 : 1;
                        return `${sign}${Math.abs(v).toFixed(decimals)}%`;
                    },
                },
            });
            this.diffChart.applyOptions({
                leftPriceScale: {
                    visible: true,
                    borderColor: 'rgba(197, 203, 206, 0.8)',
                    alignLabels: true,
                    entireTextOnly: true,
                }
            });
            this.diffChart.priceScale('left').applyOptions({
                tickMarkFormatter: (v) => {
                    const sign = v > 0 ? '+' : v < 0 ? '-' : '';
                    const decimals = Math.abs(v) >= 100 ? 0 : 1;
                    return `${sign}${Math.abs(v).toFixed(decimals)}%`;
                }
            });

            // Keep sub-chart horizontally in sync with main chart
            // --- Synchronize time scales between main and diff charts (both directions) ---
            const syncLogicalRange = (source, target) => (range) => {
                if (!range || this._syncingRangeUpdate) return;
                this._syncingRangeUpdate = true;
                target.timeScale().setVisibleLogicalRange(range);
                this._syncingRangeUpdate = false;
            };
            this.chart.timeScale().subscribeVisibleLogicalRangeChange(syncLogicalRange(this.chart, this.diffChart));
            this.diffChart.timeScale().subscribeVisibleLogicalRangeChange(syncLogicalRange(this.diffChart, this.chart));



            // Mirror left price scale so grid labels also appear on the left
            // Add transparent mirror series to keep left scale in sync with right
            this.mirrorSeries = this.chart.addLineSeries({
                priceScaleId: 'left',
                color: 'rgba(0,0,0,0)',
                lineWidth: 1,
                lastValueVisible: false,
                priceLineVisible: false,
                priceFormat: {
                    type: 'custom',
                    minMove: 0.1,
                    formatter: (price) => {
                        const diff = price - 100;
                        const sign = diff > 0 ? '+' : diff < 0 ? '-' : '';
                        const decimals = Math.abs(diff) >= 100 ? 0 : 1;
                        return `${sign}${Math.abs(diff).toFixed(decimals)}%`;
                    },
                },
            });
            // Add 0% baseline horizontal line at value 100 (represents 0% change)
            this.mirrorSeries.createPriceLine({
                price: 100,
                color: 'rgba(0, 0, 0, 0.5)',
                lineWidth: 1,
                lineStyle: LightweightCharts.LineStyle.Dashed,
                priceLabelVisible: false,
                axisLabelVisible: true,
            });

            this.chart.applyOptions({
                leftPriceScale: {
                    visible: true,
                    mode: LightweightCharts.PriceScaleMode.Logarithmic,
                    borderColor: 'rgba(197, 203, 206, 0.8)',
                    entireTextOnly: true,
                    alignLabels: false,

                }

            });

                        // Format left price scale labels as ± percentages to mirror right scale
            this.chart.priceScale('left').applyOptions({
                tickMarkFormatter: (price) => {
                    const diff = price - 100;
                    const sign = diff > 0 ? '+' : diff < 0 ? '-' : '';
                    const decimals = Math.abs(diff) >= 100 ? 0 : 1;
                    return `${sign}${Math.abs(diff).toFixed(decimals)}%`;
                }
            });

            this.chart.timeScale().subscribeVisibleLogicalRangeChange(() => this.rebaseAndSetData());

            // Subscribe to crosshair movement to update legend
            this.chart.subscribeCrosshairMove(param => {
                if (!param || param.time === undefined) {
                    this.legendDiv.style.display = 'none';
                    return;
                }
                let entries = [];
                // Include each series' value at crosshair
                for (const ticker in this.chartSeries) {
                    const series = this.chartSeries[ticker];
                    const point = param.seriesData.get(series);
                    const val = point && typeof point === 'object' ? point.value : point;
                    if (val !== undefined && val !== null) {
                        entries.push({ticker, val, color: series.options().color});
                    }
                }
                // AVG series
                if (this.averageSeries) {
                    const pointAvg = param.seriesData.get(this.averageSeries);
                    const valAvg = pointAvg && typeof pointAvg === 'object' ? pointAvg.value : pointAvg;
                    if (valAvg !== undefined && valAvg !== null && !isNaN(valAvg)) {
                        entries.push({ticker: 'AVG', val: valAvg, color: this.averageSeries.options().color});
                    }
                }
                                entries.sort((a, b) => b.val - a.val);
                const html = entries.map(e => `<div style=\"color:${e.color}\">${e.ticker}: ${this.formatPercent(e.val)}</div>`).join('');

                if (html) {
                    this.legendDiv.innerHTML = html;
                    this.legendDiv.style.display = 'block';
                } else {
                    this.legendDiv.style.display = 'none';
                }
            });

            this.selectedTickersElement = this.element.querySelector('.selected-tickers');
            this.tickerInputElement = this.element.querySelector('.ticker-input');
            this.addButton = this.element.querySelector('.add-btn');
            this.plotButton = this.element.querySelector('.plot-btn');
            this.clearButton = this.element.querySelector('.clear-btn');
            this.ytdButton = this.element.querySelector('.ytd-btn');
            this.removeButton = this.element.querySelector('.remove-chart-btn');
            this.addBelowButton = this.element.querySelector('.add-below-chart-btn');

            this.addButton.addEventListener('click', () => this.addTicker(this.tickerInputElement.value));
            this.plotButton.addEventListener('click', () => this.plotData());
            this.clearButton.addEventListener('click', () => this.clearChart());
            this.ytdButton.addEventListener('click', () => this.setYTDView());
            this.removeButton.addEventListener('click', () => this.destroy());
            // Insert a new empty chart card directly below this one
            this.addBelowButton.addEventListener('click', () => {
                const newCard = createNewChart();
                // Move DOM node just after current card
                this.container.insertBefore(newCard.element, this.element.nextSibling);
                // Reorder internal array so workspace save order matches visual order
                const currentIdx = chartCards.findIndex(c => c.id === this.id);
                if (currentIdx > -1) {
                    // Remove from end where it was pushed and insert after current index
                    chartCards.splice(chartCards.length - 1, 1);
                    chartCards.splice(currentIdx + 1, 0, newCard);
                }
                saveWorkspace();
            });

            this.updateSelectedTickersUI();
            if (this.tickers.size > 0) {
                this.plotData();
            }
        }

        addTicker(ticker) {
            ticker = ticker.trim().toUpperCase();
            if (ticker && !this.tickers.has(ticker)) {
                this.tickers.add(ticker);
                this.tickerInputElement.value = '';
                this.updateSelectedTickersUI();
                this.adjustHeight();
                saveWorkspace();
            }
        }

        updateSelectedTickersUI() {
            this.selectedTickersElement.innerHTML = '';
            if (this.tickers.size === 0) {
                this.selectedTickersElement.textContent = 'Selected: (none)';
                return;
            }
        
            const label = document.createElement('span');
            label.textContent = 'Selected: ';
            this.selectedTickersElement.appendChild(label);
        
            this.tickers.forEach(ticker => {
                const chip = document.createElement('span');
                chip.className = 'ticker-chip';
                chip.textContent = ticker;
        
                // Color the chip to match its series color
                if (this.chartSeries[ticker]) {
                    const seriesColor = this.chartSeries[ticker].options().color;
                    chip.style.backgroundColor = seriesColor;
                    chip.style.color = 'white'; // Set text color for contrast
                    chip.style.padding = '2px 8px';
                    chip.style.borderRadius = '12px';
                    chip.style.margin = '0 4px';
                    chip.style.display = 'inline-flex';
                    chip.style.alignItems = 'center';
                }
        
                const btn = document.createElement('button');
                btn.className = 'delete-ticker-btn';
                btn.textContent = '×';
                btn.title = 'Remove';
                btn.style.marginLeft = '5px';
                btn.style.border = 'none';
                btn.style.background = 'none';
                btn.style.color = 'white';
                btn.style.cursor = 'pointer';
                btn.addEventListener('click', (e) => {
                    e.stopPropagation(); // Prevent other click events
                    this.removeTicker(ticker);
                });
        
                chip.appendChild(btn);
                this.selectedTickersElement.appendChild(chip);
            });
        }

        removeTicker(ticker) {
            ticker = ticker.trim().toUpperCase();
            if (!this.tickers.has(ticker)) return;
            this.tickers.delete(ticker);

            if (this.chartSeries[ticker]) {
                this.chart.removeSeries(this.chartSeries[ticker]);
                delete this.chartSeries[ticker];
            }
            if (this.diffChartSeries && this.diffChartSeries[ticker]) {
                this.diffChart.removeSeries(this.diffChartSeries[ticker]);
                delete this.diffChartSeries[ticker];
            }
            delete this.raw_data[ticker];

            this.adjustHeight();
            this.rebaseAndSetData();
            this.updateSelectedTickersUI();
            saveWorkspace();
        }

        async plotData() {
            console.log('Starting plotData for tickers:', [...this.tickers]);
            this.clearSeries();
            const fetchPromises = [...this.tickers].map(ticker =>
                fetch(`/api/data?tickers=${ticker}`)
                    .then(response => {
                        console.log(`API response status for ${ticker}:`, response.status);
                        return response.json();
                    })
                    .then(data => {
                        console.log(`API data for ${ticker}:`, data);
                        return { ticker, data: data[ticker] || [] };
                    })
                    .catch(error => {
                        console.error(`Error fetching data for ${ticker}:`, error);
                        return { ticker, data: [] };
                    })
            );

            try {
                const results = await Promise.all(fetchPromises);
                console.log('All API results:', results);

                results.forEach(({ ticker, data }) => {
                    console.log(`Processing ${ticker}, data points:`, data.length);
                    this.raw_data[ticker] = data;
                    const color = this.colorPalette[this.colorIndex % this.colorPalette.length];
                this.chartSeries[ticker] = this.chart.addLineSeries({
                        color: color,
                        lastValueVisible: false,
                        axisLabelVisible: false,
                        priceLineVisible: false,
                        priceFormat: {
                            type: 'custom',
                            minMove: 0.1,
                            formatter: (price) => {
                                const diff = price - 100;
                                const sign = diff > 0 ? '+' : diff < 0 ? '-' : '';
                                const decimals = Math.abs(diff) >= 100 ? 0 : 1;
                                return `${sign}${Math.abs(diff).toFixed(decimals)}%`;
                            },
                        },
                    });
                this.colorIndex++;
                    console.log(`Series created for ${ticker}:`, this.chartSeries[ticker]);
                });

                this.rebaseAndSetData();
                this.updateSelectedTickersUI(); // Update UI to color the new ticker chips

                // Fit the time scale so the full series is visible by default
                this.chart.timeScale().fitContent();

                this.rebaseAndSetData();
                this.adjustHeight();
                saveWorkspace();
            } catch (error) {
                console.error('Error in plotData:', error);
            }
        }

        clearChart() {
            this.tickers.clear();
            this.adjustHeight();
            this.clearSeries();
            this.updateSelectedTickersUI();
            saveWorkspace();
        }

        setYTDView() {
            if (!this.chart || Object.keys(this.raw_data).length === 0) return;

            const timeScale = this.chart.timeScale();

            // The target start date for YTD view, as a UTC timestamp in seconds.
            const ytdStartTimestamp = Date.UTC(2024, 11, 31) / 1000;

            let firstDataTimestamp = null;

            // Find the earliest data point across all series that is on or after the YTD start date.
            // `point.time` is already a UTC timestamp in seconds.
            for (const ticker in this.raw_data) {
                const seriesData = this.raw_data[ticker];
                for (const point of seriesData) {
                    if (point.time >= ytdStartTimestamp) {
                        if (firstDataTimestamp === null || point.time < firstDataTimestamp) {
                            firstDataTimestamp = point.time;
                        }
                    }
                }
            }

            if (firstDataTimestamp === null) {
                console.warn('No data found on or after the YTD start date.');
                return;
            }

            // Find the latest time across all plotted series to set the 'to' range.
            let latestTimestamp = 0;
            for (const ticker in this.raw_data) {
                const data = this.raw_data[ticker];
                if (data.length > 0) {
                    const lastDataPoint = data[data.length - 1];
                    if (lastDataPoint.time > latestTimestamp) {
                        latestTimestamp = lastDataPoint.time;
                    }
                }
            }

            if (latestTimestamp === 0) return; // No data to determine the end range.

            // Use setVisibleRange with the timestamps directly.
            timeScale.setVisibleRange({
                from: firstDataTimestamp,
                to: latestTimestamp,
            });
        }

        clearSeries() {
            for (const ticker in this.chartSeries) {
                this.chart.removeSeries(this.chartSeries[ticker]);
            }
            this.chartSeries = {};
            // Remove diff chart series
            for (const t in this.diffChartSeries) { this.diffChart.removeSeries(this.diffChartSeries[t]); }
            this.diffChartSeries = {};
            if (this.averageSeries) {
                this.chart.removeSeries(this.averageSeries);
            }
            this.averageSeries = null;
            this.raw_data = {};
            this.colorIndex = 0;
            this.diffChartSeries = {};
        }

        formatPercent(price) {
            const diff = price - 100;
            const sign = diff > 0 ? '+' : diff < 0 ? '-' : '';
            const decimals = Math.abs(diff) >= 100 ? 0 : 1;
            return `${sign}${Math.abs(diff).toFixed(decimals)}%`;
        }

        adjustHeight() {
            const n = this.tickers.size;
            const extra = n > HEIGHT_THRESHOLD ? (n - HEIGHT_THRESHOLD) * EXTRA_PER_TICKER : 0;
            const newH = BASE_HEIGHT + extra;
            this.chartContainer.style.height = `${newH}px`;
            this.chart.resize(this.chartContainer.clientWidth, newH);
        }

        rebaseAndSetData() {
            const logicalRange = this.chart.timeScale().getVisibleLogicalRange();
            const firstVisibleIndex = logicalRange ? Math.max(0, Math.floor(logicalRange.from)) : 0;
            const allRebasedData = {};

            for (const ticker in this.chartSeries) {
                const tickerData = this.raw_data[ticker];
                if (!tickerData || tickerData.length === 0) {
                    allRebasedData[ticker] = [];
                    continue;
                }

                let baseValue = null;
                for (let i = firstVisibleIndex; i < tickerData.length; i++) {
                    if (tickerData[i] && tickerData[i].value !== null && tickerData[i].value > 0) {
                        baseValue = tickerData[i].value;
                        break;
                    }
                }

                if (baseValue === null) {
                    allRebasedData[ticker] = [];
                    continue;
                }

                allRebasedData[ticker] = tickerData.reduce((acc, point) => {
                    if (point && point.value !== null && point.value > 0) {
                        acc.push({ time: point.time, value: (point.value / baseValue) * 100 });
                    }
                    return acc;
                }, []);
            }

            for (const ticker in this.chartSeries) {
                this.chartSeries[ticker].setData(allRebasedData[ticker] || []);
            }

            // --- Compute and set average series ---
            const timeMap = new Map();
            Object.values(allRebasedData).forEach(seriesArr => {
                seriesArr.forEach(pt => {
                    if (!timeMap.has(pt.time)) {
                        timeMap.set(pt.time, { sum: 0, count: 0 });
                    }
                    const obj = timeMap.get(pt.time);
                    obj.sum += pt.value;
                    obj.count += 1;
                });
            });
            const avgData = Array.from(timeMap.entries()).map(([time, { sum, count }]) => ({ time, value: sum / count }));
            avgData.sort((a, b) => a.time - b.time);

            if (!this.averageSeries) {
                // Attach average series to left price scale so it drives left labels

                this.averageSeries = this.chart.addLineSeries({
                    color: '#000000',
                    lastValueVisible: false,
                    axisLabelVisible: false,
                    priceLineVisible: false,
                    priceFormat: {
                        type: 'custom',
                        minMove: 0.1,
                        formatter: (price) => {
                            const diff = price - 100;
                            const sign = diff > 0 ? '+' : diff < 0 ? '-' : '';
                            const decimals = Math.abs(diff) >= 100 ? 0 : 1;
                            return `${sign}${Math.abs(diff).toFixed(decimals)}%`;
                        },
                    },
                });
            }
            this.averageSeries.setData(avgData);
            // Update mirror series to cover full visible value range so left/right scales match
            // Determine min/max only for the portion of data currently visible
            const vis = this.chart.timeScale().getVisibleRange();
            let globalMin = Infinity, globalMax = -Infinity;
            let firstT = null, lastT = null;
            Object.values(allRebasedData).forEach(arr => {
                if (!arr || arr.length === 0) return;
                // Filter points to visible range if available
                const filtered = vis ? arr.filter(p => p.time >= vis.from && p.time <= vis.to) : arr;
                if (filtered.length === 0) return;
                if (firstT === null) firstT = filtered[0].time;
                lastT = filtered[filtered.length - 1].time;
                filtered.forEach(pt => {
                    if (pt.value < globalMin) globalMin = pt.value;
                    if (pt.value > globalMax) globalMax = pt.value;
                });
            });
            if (Number.isFinite(globalMin) && Number.isFinite(globalMax)) {
                let forcedMin = Math.min(globalMin, 100);
                let forcedMax = Math.max(globalMax, 100);
                // If baseline 100 coincides with min or max, expand the range by a small epsilon
                if (forcedMin === forcedMax) {
                    forcedMin -= 0.1;
                    forcedMax += 0.1;
                } else {
                    if (forcedMin === 100) forcedMin -= 0.1;
                    if (forcedMax === 100) forcedMax += 0.1;
                }
                this.mirrorSeries.setData([
                    { time: firstT, value: forcedMin },
                    { time: lastT || firstT, value: forcedMax }
                ]);
            }

            // --- Compute and plot per-ticker deviations from average ---
            const avgLookup = new Map(avgData.map(d => [d.time, d.value]));
            // Prepare variables for diff mirror series alignment
            let diffGlobalMin = Infinity, diffGlobalMax = -Infinity;
            let diffFirstT = null, diffLastT = null;
            for (const ticker in this.chartSeries) {
                const baseArr = allRebasedData[ticker] || [];
                const diffArr = baseArr.map(pt => {
                    const avgVal = avgLookup.get(pt.time);
                    if (avgVal && avgVal !== 0) {
                        // deviation = (1+rebased)/(1+avg) - 1  => (rebased/avg) -1, then *100 for pct points
                        return { time: pt.time, value: ((pt.value / avgVal) - 1) * 100 };
                    }
                    return { time: pt.time, value: 0 };
                });
                if (!this.diffChartSeries[ticker]) {
                    this.diffChartSeries[ticker] = this.diffChart.addLineSeries({
                        color: this.chartSeries[ticker].options().color,
                        lastValueVisible: false,
                        axisLabelVisible: false,
                        priceLineVisible: false,
                        priceFormat: {
                            type: 'custom',
                            minMove: 0.1,
                            formatter: (v) => {
                                const sign = v > 0 ? '+' : v < 0 ? '-' : '';
                                const decimals = Math.abs(v) >= 100 ? 0 : 1;
                                return `${sign}${Math.abs(v).toFixed(decimals)}%`;
                            },
                        },
                    });
                }
                // Ensure ticker label is set but last value box is hidden even if series already existed
                this.diffChartSeries[ticker].applyOptions({ lastValueVisible: false, priceLineVisible: false });
                this.diffChartSeries[ticker].setData(diffArr);
                // Track global min/max for diff mirror series within visible range
                const vis = this.chart.timeScale().getVisibleRange();
                const filtered = vis ? diffArr.filter(p => p.time >= vis.from && p.time <= vis.to) : diffArr;
                filtered.forEach(pt => {
                    if (pt.value < diffGlobalMin) diffGlobalMin = pt.value;
                    if (pt.value > diffGlobalMax) diffGlobalMax = pt.value;
                });
                if (filtered.length) {
                    if (diffFirstT === null) diffFirstT = filtered[0].time;
                    diffLastT = filtered[filtered.length - 1].time;
                }
            }
            // Push data to diffChart mirror series so left y-axis can show labels
            if (Number.isFinite(diffGlobalMin) && Number.isFinite(diffGlobalMax)) {
                const forcedMin = Math.min(diffGlobalMin, 0);
                const forcedMax = Math.max(diffGlobalMax, 0);
                this.diffMirrorSeries.setData([
                    { time: diffFirstT, value: forcedMin },
                    { time: diffLastT || diffFirstT, value: forcedMax }
                ]);
                // Resize diff chart height based on current ticker count
                this.updateDiffChartHeight();
            }
        }



        // Dynamically adjust diff chart height based on ticker count
        updateDiffChartHeight() {
            const count = Object.keys(this.chartSeries).length;
            // Base 120px, add 20px per ticker beyond 5
            const newHeight = Math.max(120, 20 * count + 20);
            const current = parseInt(this.diffChartContainer.style.height || 0, 10);
            if (current !== newHeight) {
                this.diffChartContainer.style.height = `${newHeight}px`;
                this.diffChart.resize(this.diffChartContainer.clientWidth, newHeight);
            }
        }

        destroy() {
            this.chart.remove();
            this.element.remove();
            const index = chartCards.findIndex(c => c.id === this.id);
            if (index > -1) chartCards.splice(index, 1);
            saveWorkspace();
        }

        getState() {
            return { id: this.id, tickers: [...this.tickers] };
        }
    }

    // --- Workspace Management ---
    function createNewChart(tickers = []) {
        const id = `chart-${Date.now()}`;
        const chartCard = new ChartCard(workspaceContainer, id, tickers);
        chartCards.push(chartCard);
        saveWorkspace();
        return chartCard;
    }

    async function saveWorkspace() {
        const state = chartCards.map(c => c.getState());
        // Always save to localStorage for quick restore on same origin
        localStorage.setItem('financialChartWorkspace', JSON.stringify(state));
        // Also persist to backend so state is shared across origins/ports
        try {
            await fetch('/api/workspace', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(state)
            });
        } catch (err) {
            console.warn('Workspace POST failed:', err);
        }
    }

    async function loadWorkspace() {
        // First try backend
        try {
            const resp = await fetch('/api/workspace');
            if (resp.ok) {
                const chartData = await resp.json();
                if (chartData && chartData.length) {
                    chartData.forEach(d => createNewChart(d.tickers));
                    return;
                }
            }
        } catch (err) {
            console.warn('Workspace GET failed:', err);
        }
        // Fallback to localStorage
        const savedState = localStorage.getItem('financialChartWorkspace');
        if (savedState) {
            const chartData = JSON.parse(savedState);
            if (chartData.length > 0) {
                chartData.forEach(data => createNewChart(data.tickers));
                return;
            }
        }
        // Final fallback: default chart
        createNewChart(['SPY', 'RSP']);
    }

    initializeWorkspace();
});
