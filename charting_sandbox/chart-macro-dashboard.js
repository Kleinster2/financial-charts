/**
 * chart-macro-dashboard.js - Macro/FRED Dashboard Component
 * Displays a spreadsheet-like view of FRED economic indicators
 */

window.ChartMacroDashboard = {
    data: [],
    sortColumn: 'category',
    sortDirection: 'asc',
    viewMode: 'grouped', // 'flat' or 'grouped'
    filterText: '',

    /**
     * Create a macro dashboard card
     * @param {HTMLElement} wrapperEl - Parent element to append card to
     * @param {Object} options - Optional saved state to restore
     */
    createMacroDashboardCard(wrapperEl, options = {}) {
        console.log('[ChartMacroDashboard] createMacroDashboardCard called');
        const card = document.createElement('div');
        card.className = 'chart-card macro-dashboard-card';
        card.id = `macro-dashboard-${Date.now()}`;

        // Restore saved state if provided
        if (options.sortColumn) this.sortColumn = options.sortColumn;
        if (options.sortDirection) this.sortDirection = options.sortDirection;
        if (options.viewMode) this.viewMode = options.viewMode;
        if (options.filterText) this.filterText = options.filterText;

        card.innerHTML = `
            <div class="dashboard-header">
                <h3>Macro Dashboard (FRED)</h3>
                <div class="dashboard-controls">
                    <input type="text" class="dashboard-filter" placeholder="Filter indicators..." />
                    <select class="dashboard-view-select">
                        <option value="grouped" selected>Grouped by Category</option>
                        <option value="flat">Flat View</option>
                    </select>
                    <button class="dashboard-refresh-btn">Refresh</button>
                </div>
            </div>
            <div class="macro-dashboard-stats"></div>
            <div class="dashboard-table-container">
                <table class="dashboard-table macro-table">
                    <thead></thead>
                    <tbody></tbody>
                </table>
            </div>
        `;

        // Add styles
        this.addStyles();

        // Setup event handlers
        const filterInput = card.querySelector('.dashboard-filter');
        const viewSelect = card.querySelector('.dashboard-view-select');
        const refreshBtn = card.querySelector('.dashboard-refresh-btn');

        // Apply saved filter/viewMode to UI
        if (this.filterText) filterInput.value = this.filterText;
        if (this.viewMode) viewSelect.value = this.viewMode;

        filterInput.addEventListener('input', (e) => {
            this.filterText = e.target.value.toLowerCase();
            this.renderTable(card);
            if (window.saveCards) window.saveCards();
        });

        viewSelect.addEventListener('change', (e) => {
            this.viewMode = e.target.value;
            this.renderTable(card);
            if (window.saveCards) window.saveCards();
        });

        refreshBtn.addEventListener('click', () => {
            this.loadData(card);
        });

        // Mark as macro-dashboard type for saveCards
        card._type = 'macro-dashboard';

        wrapperEl.appendChild(card);

        // Load data
        this.loadData(card);

        return card;
    },

    /**
     * Add macro dashboard-specific styles
     */
    addStyles() {
        // Ensure base dashboard styles are loaded first
        if (!window.DashboardBase || typeof window.DashboardBase.ensureStyles !== 'function') {
            console.error('[ChartMacroDashboard] DashboardBase not loaded; check index.html script order');
        } else {
            window.DashboardBase.ensureStyles();
        }

        window.ChartUtils.ensureStyleTag('macro-dashboard-styles', `
            .macro-dashboard-card {
                background: #fff;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 16px;
                min-height: 400px;
            }
            .macro-dashboard-stats {
                display: flex;
                gap: 16px;
                margin-bottom: 16px;
                padding: 12px;
                background: linear-gradient(135deg, #1a365d 0%, #2c5282 100%);
                border-radius: 4px;
                flex-wrap: wrap;
            }
            .macro-stat {
                display: flex;
                flex-direction: column;
                color: white;
            }
            .macro-stat-label {
                font-size: 0.75rem;
                opacity: 0.8;
            }
            .macro-stat-value {
                font-size: 1.1rem;
                font-weight: bold;
            }
            .macro-stat-change {
                font-size: 0.8rem;
            }
            .macro-stat-change.positive { color: #68d391; }
            .macro-stat-change.negative { color: #fc8181; }
            .macro-table .category-cell {
                font-size: 0.75rem;
                color: #666;
                text-transform: uppercase;
            }
            .macro-table .indicator-cell {
                font-weight: bold;
                color: #2c5282;
            }
            .macro-table .value-cell {
                text-align: right;
                font-family: monospace;
                font-size: 0.9rem;
            }
            .macro-table .change-cell {
                text-align: right;
                font-family: monospace;
                font-size: 0.85rem;
            }
            .macro-table .change-positive { color: #28a745; }
            .macro-table .change-negative { color: #dc3545; }
            .macro-category-header {
                background: #2c5282 !important;
                color: white !important;
            }
            .macro-category-header td {
                padding: 10px 8px !important;
                font-weight: bold;
                font-size: 0.9rem;
            }
        `);
    },

    /**
     * Load macro dashboard data from API
     */
    async loadData(card) {
        console.log('[ChartMacroDashboard] loadData called');
        const tbody = card.querySelector('.dashboard-table tbody');
        window.DashboardBase.renderStatusRow(tbody, { colspan: 10, message: 'Loading FRED data...' });

        try {
            const response = await fetch(window.ChartUtils.apiUrl('/api/macro-dashboard'));
            if (!response.ok) throw new Error('Failed to load macro dashboard data');

            this.data = await response.json();
            console.log('[ChartMacroDashboard] Data loaded:', this.data.length, 'indicators');
            this.renderStats(card);
            this.renderTable(card);
        } catch (error) {
            console.error('[ChartMacroDashboard] Load error:', error);
            window.DashboardBase.renderStatusRow(tbody, { colspan: 10, message: `Error loading data: ${error.message}` });
        }
    },

    /**
     * Render summary statistics
     */
    renderStats(card) {
        const statsEl = card.querySelector('.macro-dashboard-stats');
        const data = this.data;

        // Find key indicators
        const fedFunds = data.find(d => d.ticker === 'FEDFUNDS');
        const dgs10 = data.find(d => d.ticker === 'DGS10');
        const cpi = data.find(d => d.ticker === 'CPIAUCSL');
        const unrate = data.find(d => d.ticker === 'UNRATE');
        const gdp = data.find(d => d.ticker === 'GDP');

        const formatValue = (val, decimals = 2) => val !== null ? val.toFixed(decimals) : '-';
        const formatChange = (val) => {
            if (val === null || val === undefined) return '';
            const sign = val >= 0 ? '+' : '';
            const cls = val >= 0 ? 'positive' : 'negative';
            return `<span class="macro-stat-change ${cls}">${sign}${val.toFixed(2)}</span>`;
        };

        statsEl.innerHTML = `
            <div class="macro-stat">
                <span class="macro-stat-label">Fed Funds Rate</span>
                <span class="macro-stat-value">${fedFunds ? formatValue(fedFunds.latest_value) + '%' : '-'}</span>
                ${fedFunds ? formatChange(fedFunds.yearly_change) : ''}
            </div>
            <div class="macro-stat">
                <span class="macro-stat-label">10Y Treasury</span>
                <span class="macro-stat-value">${dgs10 ? formatValue(dgs10.latest_value) + '%' : '-'}</span>
                ${dgs10 ? formatChange(dgs10.yearly_change) : ''}
            </div>
            <div class="macro-stat">
                <span class="macro-stat-label">CPI (YoY)</span>
                <span class="macro-stat-value">${cpi ? formatValue(cpi.latest_value) : '-'}</span>
                ${cpi ? formatChange(cpi.yearly_change) : ''}
            </div>
            <div class="macro-stat">
                <span class="macro-stat-label">Unemployment</span>
                <span class="macro-stat-value">${unrate ? formatValue(unrate.latest_value) + '%' : '-'}</span>
                ${unrate ? formatChange(unrate.yearly_change) : ''}
            </div>
            <div class="macro-stat">
                <span class="macro-stat-label">GDP (B)</span>
                <span class="macro-stat-value">${gdp ? formatValue(gdp.latest_value / 1000, 1) + 'T' : '-'}</span>
                ${gdp ? formatChange(gdp.yearly_change) : ''}
            </div>
            <div class="macro-stat">
                <span class="macro-stat-label">Total Indicators</span>
                <span class="macro-stat-value">${data.length}</span>
            </div>
        `;
    },

    /**
     * Render the data table
     */
    renderTable(card) {
        const endTiming = window.ChartUtils?.perf?.start('macroDashboardRender');

        const thead = card.querySelector('.dashboard-table thead');
        const tbody = card.querySelector('.dashboard-table tbody');

        const columns = [
            { key: 'ticker', label: 'Indicator' },
            { key: 'name', label: 'Description' },
            { key: 'category', label: 'Category' },
            { key: 'latest_value', label: 'Value' },
            { key: 'daily_change', label: 'Day \u0394' },
            { key: 'weekly_change', label: 'Week \u0394' },
            { key: 'monthly_change', label: 'Month \u0394' },
            { key: 'yearly_change', label: 'Year \u0394' },
            { key: 'high_52w', label: '52w High' },
            { key: 'low_52w', label: '52w Low' }
        ];

        const filteredData = window.DashboardBase.filterAndSortData({
            data: this.data,
            filterText: this.filterText,
            filterFn: (d, filterText) =>
                d.ticker.toLowerCase().includes(filterText) ||
                (d.name && d.name.toLowerCase().includes(filterText)) ||
                (d.category && d.category.toLowerCase().includes(filterText)),
            sortColumn: this.sortColumn,
            sortDirection: this.sortDirection,
            numericColumns: ['latest_value', 'daily_change', 'weekly_change', 'monthly_change', 'yearly_change', 'high_52w', 'low_52w']
        });

        window.DashboardBase.renderSortableHeader({
            thead,
            columns,
            sortColumn: this.sortColumn,
            sortDirection: this.sortDirection,
            onSortChange: (col, direction) => {
                this.sortColumn = col;
                this.sortDirection = direction;
                this.renderTable(card);
                if (window.saveCards) window.saveCards();
            }
        });

        // Render body
        if (this.viewMode === 'grouped') {
            this.renderGroupedBody(tbody, filteredData);
        } else {
            this.renderFlatBody(tbody, filteredData);
        }

        if (endTiming) endTiming();
    },

    /**
     * Render flat table body
     */
    renderFlatBody(tbody, data) {
        tbody.innerHTML = data.map(row => this.renderRow(row)).join('');
        this.attachRowHandlers(tbody);
    },

    /**
     * Render grouped table body
     */
    renderGroupedBody(tbody, data) {
        const groups = {};

        data.forEach(row => {
            const category = row.category || 'Other';
            if (!groups[category]) groups[category] = [];
            groups[category].push(row);
        });

        // Order categories
        const categoryOrder = [
            'Interest Rates', 'Inflation', 'Labor Market', 'Economic Activity',
            'Money Supply', 'Credit Spreads', 'Currencies', 'Energy', 'Other'
        ];

        let html = '';
        categoryOrder.forEach(category => {
            if (groups[category] && groups[category].length > 0) {
                html += `<tr class="macro-category-header"><td colspan="10">${category} (${groups[category].length})</td></tr>`;
                html += groups[category].map(row => this.renderRow(row)).join('');
            }
        });

        tbody.innerHTML = html;
        this.attachRowHandlers(tbody);
    },

    /**
     * Render a single row
     */
    renderRow(row) {
        const formatChange = (val) => {
            if (val === null || val === undefined) return '-';
            const cls = val >= 0 ? 'change-positive' : 'change-negative';
            const sign = val >= 0 ? '+' : '';
            return `<span class="${cls}">${sign}${val.toFixed(4)}</span>`;
        };

        const formatValue = (val) => {
            if (val === null || val === undefined) return '-';
            return val.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 4 });
        };

        return `
            <tr data-ticker="${row.ticker}">
                <td class="indicator-cell">${row.ticker}</td>
                <td>${row.name || '-'}</td>
                <td class="category-cell">${row.category || '-'}</td>
                <td class="value-cell">${formatValue(row.latest_value)}</td>
                <td class="change-cell">${formatChange(row.daily_change)}</td>
                <td class="change-cell">${formatChange(row.weekly_change)}</td>
                <td class="change-cell">${formatChange(row.monthly_change)}</td>
                <td class="change-cell">${formatChange(row.yearly_change)}</td>
                <td class="value-cell">${formatValue(row.high_52w)}</td>
                <td class="value-cell">${formatValue(row.low_52w)}</td>
            </tr>
        `;
    },

    /**
     * Attach click handlers to rows
     */
    attachRowHandlers(tbody) {
        tbody.querySelectorAll('.indicator-cell').forEach(cell => {
            cell.style.cursor = 'pointer';
            cell.addEventListener('click', () => {
                const ticker = cell.closest('tr').dataset.ticker;
                window.DashboardBase.setGlobalSearchTicker(ticker);
            });
        });
    },

    /**
     * Serialize macro dashboard state for workspace save
     * @param {HTMLElement} card - The dashboard card element
     * @returns {Object} Serialized state
     */
    serializeCard(card) {
        return {
            type: 'macro-dashboard',
            page: card.closest('.page')?.dataset.page || '1',
            sortColumn: this.sortColumn,
            sortDirection: this.sortDirection,
            viewMode: this.viewMode,
            filterText: this.filterText
        };
    }
};

console.log('[ChartMacroDashboard] Module loaded');
