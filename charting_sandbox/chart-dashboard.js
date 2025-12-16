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
    filterExact: false, // true when trailing space = exact ticker match
    columnOrder: null, // Will be initialized with default order
    hiddenColumns: new Set(), // Columns to hide

    /**
     * Create a dashboard card
     * @param {HTMLElement} wrapperEl - Parent element to append card to
     * @param {Object} options - Optional saved state to restore
     */
    createDashboardCard(wrapperEl, options = {}) {
        console.log('[ChartDashboard] createDashboardCard called, wrapper:', wrapperEl);
        const card = document.createElement('div');
        card.className = 'chart-card dashboard-card';
        card.id = `dashboard-${Date.now()}`;

        // Restore saved state if provided
        if (options.sortColumn) this.sortColumn = options.sortColumn;
        if (options.sortDirection) this.sortDirection = options.sortDirection;
        if (options.viewMode) this.viewMode = options.viewMode;
        if (options.filterText) this.filterText = options.filterText;
        if (options.columnOrder) this.columnOrder = options.columnOrder;
        if (options.hiddenColumns) this.hiddenColumns = new Set(options.hiddenColumns);
        if (options.columnWidths) this.columnWidths = options.columnWidths;

        card.innerHTML = `
            <div class="dashboard-header">
                <h3>Data Dashboard</h3>
                <div class="dashboard-controls">
                    <input type="text" class="dashboard-filter" placeholder="Filter tickers..." />
                    <select class="dashboard-view-select">
                        <option value="flat">Flat View</option>
                        <option value="grouped">Grouped by Page</option>
                    </select>
                    <div class="dashboard-columns-dropdown">
                        <button class="dashboard-columns-btn">Columns ▼</button>
                        <div class="dashboard-columns-menu"></div>
                    </div>
                    <button class="dashboard-refresh-btn">Refresh</button>
                    <button class="dashboard-reset-btn">Reset Layout</button>
                    <button class="dashboard-export-btn">Export CSV</button>
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

        // Apply saved filter/viewMode to UI
        if (this.filterText) filterInput.value = this.filterText;
        if (this.viewMode) viewSelect.value = this.viewMode;

        // Debounced filter render for better performance during typing
        const debouncedFilterRender = window.ChartUtils.debounce(() => {
            this.renderTable(card);
            if (window.saveCards) window.saveCards();
        }, 150);

        filterInput.addEventListener('input', (e) => {
            const raw = e.target.value;
            // Trailing space = exact ticker match
            this.filterExact = raw.endsWith(' ') && raw.trim().length > 0;
            this.filterText = raw.trim().toLowerCase();
            debouncedFilterRender();
        });

        viewSelect.addEventListener('change', (e) => {
            this.viewMode = e.target.value;
            this.renderTable(card);
            if (window.saveCards) window.saveCards();
        });

        refreshBtn.addEventListener('click', () => {
            this.loadData(card);
        });

        // Reset Layout button
        const resetBtn = card.querySelector('.dashboard-reset-btn');
        resetBtn.addEventListener('click', () => {
            this.resetLayout(card, filterInput, viewSelect);
        });

        // Export CSV button
        const exportBtn = card.querySelector('.dashboard-export-btn');
        exportBtn.addEventListener('click', () => {
            this.exportCSV();
        });

        // Columns dropdown
        const columnsBtn = card.querySelector('.dashboard-columns-btn');
        const columnsMenu = card.querySelector('.dashboard-columns-menu');
        this.initColumnsDropdown(card, columnsBtn, columnsMenu);

        // Mark as dashboard type for saveCards
        card._type = 'dashboard';

        wrapperEl.appendChild(card);

        // Load data
        this.loadData(card);

        return card;
    },

    /**
     * Add dashboard-specific styles (delegates to DashboardBase)
     */
    addStyles() {
        if (!window.DashboardBase || typeof window.DashboardBase.ensureStyles !== 'function') {
            console.error('[ChartDashboard] DashboardBase not loaded; check index.html script order');
            return;
        }
        window.DashboardBase.ensureStyles();
    },

    /**
     * Load dashboard data from API
     */
    async loadData(card) {
        console.log('[ChartDashboard] loadData called');
        const tbody = card.querySelector('.dashboard-table tbody');
        console.log('[ChartDashboard] tbody:', tbody);
        window.DashboardBase.renderStatusRow(tbody, { colspan: 12, message: 'Loading data...' });

        try {
            console.log('[ChartDashboard] Fetching from API...');
            const response = await fetch(window.ChartUtils.apiUrl('/api/dashboard'));
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
            window.DashboardBase.renderStatusRow(tbody, { colspan: 12, message: `Error loading data: ${error.message}` });
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
        const endTiming = window.ChartUtils?.perf?.start('dashboardRender');

        const thead = card.querySelector('.dashboard-table thead');
        const tbody = card.querySelector('.dashboard-table tbody');

        // Default column definitions
        const defaultColumns = [
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

        // Initialize column order if not set
        if (!this.columnOrder) {
            this.columnOrder = defaultColumns.map(c => c.key);
        }

        // Build columns array in current order
        const columnMap = {};
        defaultColumns.forEach(c => columnMap[c.key] = c);
        const columns = this.columnOrder.map(key => columnMap[key]).filter(Boolean);

        // Filter + sort data
        const numericColumns = [
            'latest_price', 'daily_change', 'weekly_change', 'monthly_change',
            'yearly_change', 'high_52w', 'low_52w', 'data_points', 'pages'
        ];

        const filteredData = window.DashboardBase.filterAndSortData({
            data: this.data,
            filterText: this.filterText,
            filterFn: (d, filterText) => {
                if (this.filterExact) {
                    return d.ticker.toLowerCase() === filterText;
                }
                return d.ticker.toLowerCase().includes(filterText) ||
                    (d.name && d.name.toLowerCase().includes(filterText)) ||
                    (d.pages && d.pages.some(p => p.page_name.toLowerCase().includes(filterText)));
            },
            sortColumn: this.sortColumn,
            sortDirection: this.sortDirection,
            numericColumns,
            getSortValue: (d, sortColumn) => {
                if (sortColumn === 'pages') {
                    return (d.pages && Array.isArray(d.pages)) ? d.pages.length : 0;
                }
                return d[sortColumn];
            }
        });

        // Get saved column widths
        const savedWidths = this.columnWidths || {};

        // Render header with sortable click handling
        window.DashboardBase.renderSortableHeader({
            thead,
            columns,
            sortColumn: this.sortColumn,
            sortDirection: this.sortDirection,
            thRenderer: (col, sortClass) => {
                const widthStyle = savedWidths[col.key]
                    ? `style="width: ${savedWidths[col.key]}px; min-width: ${savedWidths[col.key]}px;"`
                    : '';
                const label = window.DashboardBase.escapeHtml(col.label);
                return `<th class="${sortClass}" data-column="${col.key}" draggable="true" ${widthStyle}>${label}<span class="resize-handle"></span></th>`;
            },
            shouldIgnoreSortClick: (e) => e.target.classList.contains('resize-handle'),
            onSortChange: (col, direction) => {
                this.sortColumn = col;
                this.sortDirection = direction;
                this.renderTable(card);
                if (window.saveCards) window.saveCards();
            }
        });

        // ChartDashboard-specific overrides: column resize + drag
        this.initColumnResize(card, thead);
        this.initColumnDrag(card, thead);

        // Render body
        if (this.viewMode === 'grouped') {
            this.renderGroupedBody(tbody, filteredData, columns);
        } else {
            this.renderFlatBody(tbody, filteredData, columns);
        }

        if (endTiming) endTiming();
    },

    /**
     * Initialize column resize functionality
     */
    initColumnResize(card, thead) {
        const table = card.querySelector('.dashboard-table');
        const handles = thead.querySelectorAll('.resize-handle');

        handles.forEach(handle => {
            handle.addEventListener('mousedown', (e) => {
                e.preventDefault();
                e.stopPropagation();

                const th = handle.parentElement;
                const startX = e.pageX;
                const startWidth = th.offsetWidth;
                const colKey = th.dataset.column;

                handle.classList.add('resizing');
                table.classList.add('resizing');

                const onMouseMove = (moveEvent) => {
                    const newWidth = Math.max(50, startWidth + (moveEvent.pageX - startX));
                    th.style.width = newWidth + 'px';
                    th.style.minWidth = newWidth + 'px';

                    // Save width
                    if (!this.columnWidths) this.columnWidths = {};
                    this.columnWidths[colKey] = newWidth;
                };

                const onMouseUp = () => {
                    handle.classList.remove('resizing');
                    table.classList.remove('resizing');
                    document.removeEventListener('mousemove', onMouseMove);
                    document.removeEventListener('mouseup', onMouseUp);
                    if (window.saveCards) window.saveCards();
                };

                document.addEventListener('mousemove', onMouseMove);
                document.addEventListener('mouseup', onMouseUp);
            });
        });
    },

    /**
     * Initialize columns dropdown for showing/hiding columns
     */
    initColumnsDropdown(card, btn, menu) {
        // Default column definitions for building the menu
        const defaultColumns = [
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

        // Build checkboxes for each column
        menu.innerHTML = defaultColumns.map(col => `
            <label>
                <input type="checkbox" data-column="${col.key}" ${!this.hiddenColumns.has(col.key) ? 'checked' : ''}>
                ${col.label}
            </label>
        `).join('');

        // Toggle menu visibility
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            menu.classList.toggle('show');
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!menu.contains(e.target) && e.target !== btn) {
                menu.classList.remove('show');
            }
        });

        // Handle checkbox changes
        menu.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', (e) => {
                const colKey = e.target.dataset.column;
                if (e.target.checked) {
                    this.hiddenColumns.delete(colKey);
                    // Add back to column order if not present
                    if (!this.columnOrder.includes(colKey)) {
                        this.columnOrder.push(colKey);
                    }
                } else {
                    this.hiddenColumns.add(colKey);
                    // Remove from column order
                    const idx = this.columnOrder.indexOf(colKey);
                    if (idx !== -1) {
                        this.columnOrder.splice(idx, 1);
                    }
                }
                this.renderTable(card);
                if (window.saveCards) window.saveCards();
            });
        });
    },

    /**
     * Initialize column drag-and-drop reordering
     */
    initColumnDrag(card, thead) {
        let draggedColumn = null;

        thead.querySelectorAll('th').forEach(th => {
            th.addEventListener('dragstart', (e) => {
                // Don't start drag from resize handle
                if (e.target.classList.contains('resize-handle')) {
                    e.preventDefault();
                    return;
                }
                draggedColumn = th.dataset.column;
                th.classList.add('dragging');
                e.dataTransfer.effectAllowed = 'move';
                e.dataTransfer.setData('text/plain', draggedColumn);
            });

            th.addEventListener('dragend', () => {
                th.classList.remove('dragging');
                thead.querySelectorAll('th').forEach(h => h.classList.remove('drag-over'));
                draggedColumn = null;
            });

            th.addEventListener('dragover', (e) => {
                e.preventDefault();
                e.dataTransfer.dropEffect = 'move';
                if (th.dataset.column !== draggedColumn) {
                    th.classList.add('drag-over');
                }
            });

            th.addEventListener('dragleave', () => {
                th.classList.remove('drag-over');
            });

            th.addEventListener('drop', (e) => {
                e.preventDefault();
                th.classList.remove('drag-over');

                const targetColumn = th.dataset.column;
                if (draggedColumn && draggedColumn !== targetColumn) {
                    // Reorder columns
                    const fromIndex = this.columnOrder.indexOf(draggedColumn);
                    const toIndex = this.columnOrder.indexOf(targetColumn);

                    if (fromIndex !== -1 && toIndex !== -1) {
                        // Remove from old position and insert at new
                        this.columnOrder.splice(fromIndex, 1);
                        this.columnOrder.splice(toIndex, 0, draggedColumn);

                        // Re-render table
                        this.renderTable(card);
                        if (window.saveCards) window.saveCards();
                    }
                }
            });
        });
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
     * Render a single row based on current column order
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

        // Cell renderers for each column
        const cellRenderers = {
            ticker: () => `<td class="ticker-cell">${row.ticker}</td>`,
            name: () => `<td>${row.name || '-'}</td>`,
            latest_price: () => `<td class="price-cell">${formatPrice(row.latest_price)}</td>`,
            daily_change: () => `<td class="price-cell">${formatChange(row.daily_change)}</td>`,
            weekly_change: () => `<td class="price-cell">${formatChange(row.weekly_change)}</td>`,
            monthly_change: () => `<td class="price-cell">${formatChange(row.monthly_change)}</td>`,
            yearly_change: () => `<td class="price-cell">${formatChange(row.yearly_change)}</td>`,
            high_52w: () => `<td class="price-cell">${formatPrice(row.high_52w)}</td>`,
            low_52w: () => `<td class="price-cell">${formatPrice(row.low_52w)}</td>`,
            data_points: () => `<td class="price-cell">${row.data_points ? row.data_points.toLocaleString() : '-'}</td>`,
            pages: () => `<td>${pagesHtml}</td>`
        };

        // Render cells in column order
        const cells = this.columnOrder.map(key => cellRenderers[key]()).join('');

        return `<tr data-ticker="${row.ticker}">${cells}</tr>`;
    },

    /**
     * Attach click handlers to tbody using event delegation
     * Single handler for all rows instead of per-row handlers
     */
    attachRowHandlers(tbody) {
        // Remove any existing delegated handler
        if (tbody._delegatedHandler) {
            tbody.removeEventListener('click', tbody._delegatedHandler);
        }

        // Single delegated click handler for all tbody interactions
        tbody._delegatedHandler = (e) => {
            const target = e.target;

            // Ticker cell click - put ticker in global search
            const tickerCell = target.closest('.ticker-cell');
            if (tickerCell) {
                const ticker = tickerCell.closest('tr')?.dataset.ticker;
                if (ticker) {
                    window.DashboardBase.setGlobalSearchTicker(ticker);
                }
                return;
            }

            // Page link click - navigate to page
            const pageLink = target.closest('.page-link');
            if (pageLink) {
                e.preventDefault();
                const pageNum = parseInt(pageLink.dataset.page, 10);
                if (window.PageManager && typeof window.PageManager.showPage === 'function') {
                    window.PageManager.showPage(pageNum);
                }
                return;
            }
        };

        tbody.addEventListener('click', tbody._delegatedHandler);
    },

    /**
     * Reset layout to defaults
     * @param {HTMLElement} card - The dashboard card element
     * @param {HTMLInputElement} filterInput - Filter input element
     * @param {HTMLSelectElement} viewSelect - View mode select element
     */
    resetLayout(card, filterInput, viewSelect) {
        // Reset all state to defaults
        this.sortColumn = 'ticker';
        this.sortDirection = 'asc';
        this.viewMode = 'flat';
        this.filterText = '';
        this.filterExact = false;
        this.columnOrder = null;  // Will be re-initialized on render
        this.hiddenColumns = new Set();
        this.columnWidths = {};

        // Update UI
        filterInput.value = '';
        viewSelect.value = 'flat';

        // Re-render
        this.renderTable(card);
        this.initColumnsDropdown(card, card.querySelector('.dashboard-columns-btn'), card.querySelector('.dashboard-columns-menu'));

        // Save
        if (window.saveCards) window.saveCards();
    },

    /**
     * Export current filtered/sorted data to CSV
     */
    exportCSV() {
        // Get current filtered/sorted data using same logic as renderTable
        const numericColumns = [
            'latest_price', 'daily_change', 'weekly_change', 'monthly_change',
            'yearly_change', 'high_52w', 'low_52w', 'data_points', 'pages'
        ];

        const filteredData = window.DashboardBase.filterAndSortData({
            data: this.data,
            filterText: this.filterText,
            filterFn: (d, filterText) => {
                if (this.filterExact) {
                    return d.ticker.toLowerCase() === filterText;
                }
                return d.ticker.toLowerCase().includes(filterText) ||
                    (d.name && d.name.toLowerCase().includes(filterText)) ||
                    (d.pages && d.pages.some(p => p.page_name.toLowerCase().includes(filterText)));
            },
            sortColumn: this.sortColumn,
            sortDirection: this.sortDirection,
            numericColumns,
            getSortValue: (d, sortColumn) => {
                if (sortColumn === 'pages') {
                    return (d.pages && Array.isArray(d.pages)) ? d.pages.length : 0;
                }
                return d[sortColumn];
            }
        });

        // Build CSV header - use visible columns only
        const defaultColumns = [
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

        // Get visible columns in order
        const columnOrder = this.columnOrder || defaultColumns.map(c => c.key);
        const visibleColumns = columnOrder
            .filter(key => !this.hiddenColumns || !this.hiddenColumns.has(key))
            .map(key => defaultColumns.find(c => c.key === key))
            .filter(Boolean);

        // Build CSV content
        const header = visibleColumns.map(c => `"${c.label}"`).join(',');
        const rows = filteredData.map(row => {
            return visibleColumns.map(col => {
                let value = row[col.key];
                if (col.key === 'pages') {
                    value = row.pages && Array.isArray(row.pages) ? row.pages.length : 0;
                }
                if (value === null || value === undefined) {
                    return '';
                }
                if (typeof value === 'string') {
                    return `"${value.replace(/"/g, '""')}"`;
                }
                if (typeof value === 'number') {
                    return value.toFixed ? value.toFixed(2) : value;
                }
                return value;
            }).join(',');
        });

        const csv = [header, ...rows].join('\n');

        // Download
        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `dashboard_export_${new Date().toISOString().slice(0, 10)}.csv`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    },

    /**
     * Serialize dashboard state for workspace save
     * @param {HTMLElement} card - The dashboard card element
     * @returns {Object} Serialized state
     */
    serializeCard(card) {
        return {
            type: 'dashboard',
            page: card.closest('.page')?.dataset.page || '1',
            sortColumn: this.sortColumn,
            sortDirection: this.sortDirection,
            viewMode: this.viewMode,
            filterText: this.filterText,
            columnOrder: this.columnOrder,
            hiddenColumns: Array.from(this.hiddenColumns || []),
            columnWidths: this.columnWidths || {}
        };
    }
};

console.log('[ChartDashboard] Module loaded');
