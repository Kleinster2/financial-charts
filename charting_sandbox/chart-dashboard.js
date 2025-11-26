/**
 * chart-dashboard.js - Data Dashboard Component
 * Displays a spreadsheet-like view of all tickers with prices, changes, and metadata
 */

window.ChartDashboard = {
    data: [],
    sortColumn: 'ticker',
    sortDirection: 'asc',
    viewMode: 'flat', // 'flat' or 'grouped'
    filterText: '',

    /**
     * Create a dashboard card
     */
    createDashboardCard(wrapperEl) {
        console.log('[ChartDashboard] createDashboardCard called, wrapper:', wrapperEl);
        const card = document.createElement('div');
        card.className = 'chart-card dashboard-card';
        card.id = `dashboard-${Date.now()}`;

        card.innerHTML = `
            <div class="dashboard-header">
                <h3>Data Dashboard</h3>
                <div class="dashboard-controls">
                    <input type="text" class="dashboard-filter" placeholder="Filter tickers..." />
                    <select class="dashboard-view-select">
                        <option value="flat">Flat View</option>
                        <option value="grouped">Grouped by Page</option>
                    </select>
                    <button class="dashboard-refresh-btn">Refresh</button>
                </div>
            </div>
            <div class="dashboard-stats"></div>
            <div class="dashboard-table-container">
                <table class="dashboard-table">
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

        filterInput.addEventListener('input', (e) => {
            this.filterText = e.target.value.toLowerCase();
            this.renderTable(card);
        });

        viewSelect.addEventListener('change', (e) => {
            this.viewMode = e.target.value;
            this.renderTable(card);
        });

        refreshBtn.addEventListener('click', () => {
            this.loadData(card);
        });

        // Mark as dashboard type for saveCards
        card._type = 'dashboard';

        wrapperEl.appendChild(card);

        // Load data
        this.loadData(card);

        return card;
    },

    /**
     * Add dashboard-specific styles
     */
    addStyles() {
        if (document.getElementById('dashboard-styles')) return;

        const style = document.createElement('style');
        style.id = 'dashboard-styles';
        style.textContent = `
            .dashboard-card {
                background: #fff;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 16px;
                min-height: 400px;
            }
            .dashboard-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 16px;
                flex-wrap: wrap;
                gap: 12px;
            }
            .dashboard-header h3 {
                margin: 0;
                color: #333;
            }
            .dashboard-controls {
                display: flex;
                gap: 8px;
                align-items: center;
                flex-wrap: wrap;
            }
            .dashboard-filter {
                padding: 6px 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                width: 200px;
            }
            .dashboard-view-select {
                padding: 6px 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            .dashboard-refresh-btn {
                padding: 6px 12px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .dashboard-refresh-btn:hover {
                background: #0056b3;
            }
            .dashboard-stats {
                display: flex;
                gap: 24px;
                margin-bottom: 16px;
                padding: 12px;
                background: #f8f9fa;
                border-radius: 4px;
                flex-wrap: wrap;
            }
            .dashboard-stat {
                display: flex;
                flex-direction: column;
            }
            .dashboard-stat-label {
                font-size: 0.8rem;
                color: #666;
            }
            .dashboard-stat-value {
                font-size: 1.2rem;
                font-weight: bold;
                color: #333;
            }
            .dashboard-table-container {
                max-height: 70vh;
                overflow: auto;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            .dashboard-table {
                width: 100%;
                border-collapse: collapse;
                font-size: 0.85rem;
            }
            .dashboard-table th {
                position: sticky;
                top: 0;
                background: #f1f3f4;
                padding: 10px 8px;
                text-align: left;
                border-bottom: 2px solid #ddd;
                cursor: pointer;
                white-space: nowrap;
                user-select: none;
            }
            .dashboard-table th:hover {
                background: #e2e6ea;
            }
            .dashboard-table th.sorted-asc::after {
                content: ' \\25B2';
                font-size: 0.7rem;
            }
            .dashboard-table th.sorted-desc::after {
                content: ' \\25BC';
                font-size: 0.7rem;
            }
            .dashboard-table td {
                padding: 8px;
                border-bottom: 1px solid #eee;
            }
            .dashboard-table tr:hover {
                background: #f8f9fa;
            }
            .dashboard-table .ticker-cell {
                font-weight: bold;
                color: #007bff;
                cursor: pointer;
            }
            .dashboard-table .ticker-cell:hover {
                text-decoration: underline;
            }
            .dashboard-table .price-cell {
                text-align: right;
                font-family: monospace;
            }
            .dashboard-table .change-positive {
                color: #28a745;
            }
            .dashboard-table .change-negative {
                color: #dc3545;
            }
            .dashboard-table .page-link {
                color: #007bff;
                cursor: pointer;
                text-decoration: none;
            }
            .dashboard-table .page-link:hover {
                text-decoration: underline;
            }
            .dashboard-group-header {
                background: #e9ecef !important;
                font-weight: bold;
            }
            .dashboard-group-header td {
                padding: 12px 8px;
                border-bottom: 2px solid #dee2e6;
            }
            .dashboard-loading {
                text-align: center;
                padding: 40px;
                color: #666;
            }
        `;
        document.head.appendChild(style);
    },

    /**
     * Load dashboard data from API
     */
    async loadData(card) {
        console.log('[ChartDashboard] loadData called');
        const tbody = card.querySelector('.dashboard-table tbody');
        console.log('[ChartDashboard] tbody:', tbody);
        tbody.innerHTML = '<tr><td colspan="12" class="dashboard-loading">Loading data...</td></tr>';

        try {
            console.log('[ChartDashboard] Fetching from API...');
            const response = await fetch('http://localhost:5000/api/dashboard');
            console.log('[ChartDashboard] Response status:', response.status);
            if (!response.ok) throw new Error('Failed to load dashboard data');

            this.data = await response.json();
            console.log('[ChartDashboard] Data loaded:', this.data.length, 'tickers');
            console.log('[ChartDashboard] Calling renderStats...');
            this.renderStats(card);
            console.log('[ChartDashboard] Calling renderTable...');
            this.renderTable(card);
            console.log('[ChartDashboard] Render complete');
        } catch (error) {
            console.error('[ChartDashboard] Dashboard load error:', error);
            tbody.innerHTML = `<tr><td colspan="12" class="dashboard-loading">Error loading data: ${error.message}</td></tr>`;
        }
    },

    /**
     * Render summary statistics
     */
    renderStats(card) {
        const statsEl = card.querySelector('.dashboard-stats');
        const data = this.data;

        const totalTickers = data.length;
        const tickersWithPages = data.filter(d => d.pages && d.pages.length > 0).length;
        const avgDailyChange = data.reduce((sum, d) => sum + (d.daily_change || 0), 0) / data.length;
        const gainers = data.filter(d => d.daily_change > 0).length;
        const losers = data.filter(d => d.daily_change < 0).length;

        statsEl.innerHTML = `
            <div class="dashboard-stat">
                <span class="dashboard-stat-label">Total Tickers</span>
                <span class="dashboard-stat-value">${totalTickers.toLocaleString()}</span>
            </div>
            <div class="dashboard-stat">
                <span class="dashboard-stat-label">In Charts</span>
                <span class="dashboard-stat-value">${tickersWithPages.toLocaleString()}</span>
            </div>
            <div class="dashboard-stat">
                <span class="dashboard-stat-label">Avg Daily Change</span>
                <span class="dashboard-stat-value ${avgDailyChange >= 0 ? 'change-positive' : 'change-negative'}">${avgDailyChange.toFixed(2)}%</span>
            </div>
            <div class="dashboard-stat">
                <span class="dashboard-stat-label">Gainers</span>
                <span class="dashboard-stat-value change-positive">${gainers}</span>
            </div>
            <div class="dashboard-stat">
                <span class="dashboard-stat-label">Losers</span>
                <span class="dashboard-stat-value change-negative">${losers}</span>
            </div>
        `;
    },

    /**
     * Render the data table
     */
    renderTable(card) {
        const thead = card.querySelector('.dashboard-table thead');
        const tbody = card.querySelector('.dashboard-table tbody');

        // Filter data
        let filteredData = this.data;
        if (this.filterText) {
            filteredData = this.data.filter(d =>
                d.ticker.toLowerCase().includes(this.filterText) ||
                (d.name && d.name.toLowerCase().includes(this.filterText)) ||
                (d.pages && d.pages.some(p => p.page_name.toLowerCase().includes(this.filterText)))
            );
        }

        // Sort data
        const numericColumns = ['latest_price', 'daily_change', 'weekly_change', 'monthly_change', 'yearly_change', 'high_52w', 'low_52w', 'data_points'];
        const isNumeric = numericColumns.includes(this.sortColumn);

        filteredData = [...filteredData].sort((a, b) => {
            let aVal = a[this.sortColumn];
            let bVal = b[this.sortColumn];

            // Special handling for pages column - sort by count
            if (this.sortColumn === 'pages') {
                aVal = (aVal && Array.isArray(aVal)) ? aVal.length : 0;
                bVal = (bVal && Array.isArray(bVal)) ? bVal.length : 0;
            }

            // Handle nulls - put them at the end regardless of sort direction
            const aNull = aVal === null || aVal === undefined;
            const bNull = bVal === null || bVal === undefined;
            if (aNull && bNull) return 0;
            if (aNull) return 1;
            if (bNull) return -1;

            // Numeric comparison
            if (isNumeric || this.sortColumn === 'pages') {
                aVal = Number(aVal) || 0;
                bVal = Number(bVal) || 0;
            } else if (typeof aVal === 'string') {
                // String comparison
                aVal = aVal.toLowerCase();
                bVal = (bVal || '').toLowerCase();
            }

            if (aVal < bVal) return this.sortDirection === 'asc' ? -1 : 1;
            if (aVal > bVal) return this.sortDirection === 'asc' ? 1 : -1;
            return 0;
        });

        // Render header
        const columns = [
            { key: 'ticker', label: 'Ticker' },
            { key: 'name', label: 'Name' },
            { key: 'latest_price', label: 'Price' },
            { key: 'daily_change', label: 'Day %' },
            { key: 'weekly_change', label: 'Week %' },
            { key: 'monthly_change', label: 'Month %' },
            { key: 'yearly_change', label: 'Year %' },
            { key: 'high_52w', label: '52w High' },
            { key: 'low_52w', label: '52w Low' },
            { key: 'data_points', label: 'Data Pts' },
            { key: 'pages', label: 'Pages' }
        ];

        thead.innerHTML = `<tr>${columns.map(col => {
            const sortClass = this.sortColumn === col.key
                ? (this.sortDirection === 'asc' ? 'sorted-asc' : 'sorted-desc')
                : '';
            return `<th class="${sortClass}" data-column="${col.key}">${col.label}</th>`;
        }).join('')}</tr>`;

        // Add sort handlers
        thead.querySelectorAll('th').forEach(th => {
            th.addEventListener('click', () => {
                const col = th.dataset.column;
                if (this.sortColumn === col) {
                    this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
                } else {
                    this.sortColumn = col;
                    this.sortDirection = 'asc';
                }
                this.renderTable(card);
            });
        });

        // Render body
        if (this.viewMode === 'grouped') {
            this.renderGroupedBody(tbody, filteredData, columns);
        } else {
            this.renderFlatBody(tbody, filteredData, columns);
        }
    },

    /**
     * Render flat table body
     */
    renderFlatBody(tbody, data, columns) {
        tbody.innerHTML = data.map(row => this.renderRow(row)).join('');
        this.attachRowHandlers(tbody);
    },

    /**
     * Render grouped table body
     */
    renderGroupedBody(tbody, data, columns) {
        // Group by first page
        const groups = {};
        const noPage = [];

        data.forEach(row => {
            if (row.pages && row.pages.length > 0) {
                const pageName = row.pages[0].page_name;
                if (!groups[pageName]) groups[pageName] = [];
                groups[pageName].push(row);
            } else {
                noPage.push(row);
            }
        });

        // Sort group names
        const sortedGroups = Object.keys(groups).sort();

        let html = '';
        sortedGroups.forEach(groupName => {
            html += `<tr class="dashboard-group-header"><td colspan="11">${groupName} (${groups[groupName].length})</td></tr>`;
            html += groups[groupName].map(row => this.renderRow(row)).join('');
        });

        if (noPage.length > 0) {
            html += `<tr class="dashboard-group-header"><td colspan="11">Not in Charts (${noPage.length})</td></tr>`;
            html += noPage.map(row => this.renderRow(row)).join('');
        }

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
            return `<span class="${cls}">${sign}${val.toFixed(2)}%</span>`;
        };

        const formatPrice = (val) => {
            if (val === null || val === undefined) return '-';
            return val.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        };

        const pagesHtml = row.pages && row.pages.length > 0
            ? row.pages.map(p => `<a class="page-link" data-page="${p.page}">${p.page_name}</a>`).join(', ')
            : '-';

        return `
            <tr data-ticker="${row.ticker}">
                <td class="ticker-cell">${row.ticker}</td>
                <td>${row.name || '-'}</td>
                <td class="price-cell">${formatPrice(row.latest_price)}</td>
                <td class="price-cell">${formatChange(row.daily_change)}</td>
                <td class="price-cell">${formatChange(row.weekly_change)}</td>
                <td class="price-cell">${formatChange(row.monthly_change)}</td>
                <td class="price-cell">${formatChange(row.yearly_change)}</td>
                <td class="price-cell">${formatPrice(row.high_52w)}</td>
                <td class="price-cell">${formatPrice(row.low_52w)}</td>
                <td class="price-cell">${row.data_points ? row.data_points.toLocaleString() : '-'}</td>
                <td>${pagesHtml}</td>
            </tr>
        `;
    },

    /**
     * Attach click handlers to rows
     */
    attachRowHandlers(tbody) {
        // Ticker click - could add to search or show details
        tbody.querySelectorAll('.ticker-cell').forEach(cell => {
            cell.addEventListener('click', () => {
                const ticker = cell.closest('tr').dataset.ticker;
                // Put ticker in global search
                const searchInput = document.getElementById('global-search-input');
                if (searchInput) {
                    searchInput.value = ticker;
                    searchInput.dispatchEvent(new Event('input'));
                }
            });
        });

        // Page link click - navigate to page
        tbody.querySelectorAll('.page-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const pageNum = parseInt(link.dataset.page, 10);
                if (window.PageManager && typeof window.PageManager.showPage === 'function') {
                    window.PageManager.showPage(pageNum);
                }
            });
        });
    }
};

console.log('[ChartDashboard] Module loaded');
