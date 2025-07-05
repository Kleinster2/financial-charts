document.addEventListener('DOMContentLoaded', () => {
    const workspaceContainer = document.getElementById('workspace-container');
    const addChartBtn = document.getElementById('add-chart-btn');
    let chartCards = []; // Global list of chart card instances
    let availableTickers = [];

    // --- Main Setup ---
    async function initializeWorkspace() {
        await fetchAvailableTickers();
        loadWorkspace();
        addChartBtn.addEventListener('click', () => createNewChart());
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
    class ChartCard {
        constructor(container, id, tickers = []) {
            this.container = container;
            this.id = id;
            this.tickers = new Set(tickers);
            this.raw_data = {};
            // Color palette for distinct series lines
            this.colorPalette = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf'];
            this.colorIndex = 0;
            this.chartSeries = {};

            this.element = document.getElementById('chart-card-template').content.cloneNode(true).firstElementChild;
            this.element.dataset.id = this.id;
            this.container.appendChild(this.element);

            this.chartContainer = this.element.querySelector('.chart-container');
            this.chart = LightweightCharts.createChart(this.chartContainer, {
                width: this.chartContainer.clientWidth,
                height: 300,
                layout: { background: { type: 'solid', color: '#ffffff' }, textColor: 'rgba(0, 0, 0, 0.9)' },
                grid: { vertLines: { color: 'rgba(197, 203, 206, 0.5)' }, horzLines: { color: 'rgba(197, 203, 206, 0.5)' } },
                crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
                timeScale: { borderColor: 'rgba(197, 203, 206, 0.8)', timeVisible: true, secondsVisible: false },
                rightPriceScale: { 
                 mode: LightweightCharts.PriceScaleMode.Logarithmic,
                 borderColor: 'rgba(197, 203, 206, 0.8)',
                 formatter: (price) => `${(price - 100).toFixed(0)}%` 
             },
            });

            // Ensure right price scale is logarithmic
            this.chart.priceScale('right').applyOptions({ mode: LightweightCharts.PriceScaleMode.Logarithmic });

            this.chart.timeScale().subscribeVisibleLogicalRangeChange(() => this.rebaseAndSetData());

            this.selectedTickersElement = this.element.querySelector('.selected-tickers');
            this.tickerInputElement = this.element.querySelector('.ticker-input');
            this.addButton = this.element.querySelector('.add-btn');
            this.plotButton = this.element.querySelector('.plot-btn');
            this.clearButton = this.element.querySelector('.clear-btn');
            this.removeButton = this.element.querySelector('.remove-chart-btn');

            this.addButton.addEventListener('click', () => this.addTicker(this.tickerInputElement.value));
            this.plotButton.addEventListener('click', () => this.plotData());
            this.clearButton.addEventListener('click', () => this.clearChart());
            this.removeButton.addEventListener('click', () => this.destroy());

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
                saveWorkspace();
            }
        }

        updateSelectedTickersUI() {
            this.selectedTickersElement.textContent = `Selected: ${[...this.tickers].join(', ')}`;
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
                this.chartSeries[ticker] = this.chart.addLineSeries({ title: ticker, color, lastValueVisible: true, priceLineVisible: false });
                this.colorIndex++;
                    console.log(`Series created for ${ticker}:`, this.chartSeries[ticker]);
                });

                // Fit the time scale so the full series is visible by default
                this.chart.timeScale().fitContent();

                this.rebaseAndSetData();
                saveWorkspace();
            } catch (error) {
                console.error('Error in plotData:', error);
            }
        }

        clearChart() {
            this.tickers.clear();
            this.clearSeries();
            this.updateSelectedTickersUI();
            saveWorkspace();
        }

        clearSeries() {
            for (const ticker in this.chartSeries) {
                this.chart.removeSeries(this.chartSeries[ticker]);
            }
            this.chartSeries = {};
            this.raw_data = {};
            this.colorIndex = 0;
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

    function saveWorkspace() {
        const state = chartCards.map(c => c.getState());
        localStorage.setItem('financialChartWorkspace', JSON.stringify(state));
    }

    function loadWorkspace() {
        const savedState = localStorage.getItem('financialChartWorkspace');
        if (savedState) {
            const chartData = JSON.parse(savedState);
            if (chartData.length > 0) {
                chartData.forEach(data => createNewChart(data.tickers));
            } else {
                createNewChart(['SPY', 'RSP']); // Default chart if workspace is empty
            }
        } else {
            createNewChart(['SPY', 'RSP']); // Default for first-time users
        }
    }

    initializeWorkspace();
});
