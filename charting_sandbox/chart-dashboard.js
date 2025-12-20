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
    conditionalFormatting: false, // Toggle for background shading on % columns
    // Multi-select state
    selectedTickers: new Set(), // Selected ticker symbols
    // Pagination state
    pageSize: 100,
    totalCount: 0,
    isLoading: false,
    hasMore: false,
    // Keyboard navigation state
    focusedRowIndex: -1,
    // Sparkline state (30D)
    sparklineCache: new Map(), // ticker -> { data: [...], pctChange: number }
    sparklineAbortController: null, // AbortController for in-flight requests
    sparklinePendingTickers: new Set(), // Tickers awaiting sparkline fetch
    // Sparkline state (1Y)
    sparkline1yCache: new Map(),
    sparkline1yAbortController: null,
    sparkline1yPendingTickers: new Set(),

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
        if (options.conditionalFormatting !== undefined) this.conditionalFormatting = options.conditionalFormatting;

        card.innerHTML = `
            <div class="dashboard-header">
                <h3>Data Dashboard</h3>
                <div class="dashboard-controls">
                    <input type="text" class="dashboard-filter" placeholder="Filter tickers..." />
                    <select class="dashboard-view-select">
                        <option value="flat">Flat View</option>
                        <option value="grouped">Grouped by Page</option>
                        <option value="grouped-chart">Grouped by Page & Chart</option>
                    </select>
                    <div class="dashboard-columns-dropdown">
                        <button class="dashboard-columns-btn">Columns ▼</button>
                        <div class="dashboard-columns-menu"></div>
                    </div>
                    <button class="dashboard-refresh-btn">Refresh</button>
                    <span class="dashboard-refresh-indicator" style="display:none;">Updating...</span>
                    <button class="dashboard-conditional-btn" title="Toggle background shading for % columns">Conditional</button>
                    <button class="dashboard-reset-btn">Reset Layout</button>
                    <button class="dashboard-export-btn">Export CSV</button>
                    <button class="dashboard-copy-btn" title="Copy as TSV (for Excel/Sheets)">Copy</button>
                    <button class="dashboard-export-all-btn" style="display:none;" title="Export all filtered rows to CSV">Export All</button>
                    <button class="dashboard-copy-all-btn" style="display:none;" title="Copy all filtered rows as TSV">Copy All</button>
                </div>
            </div>
            <div class="dashboard-stats"></div>
            <div class="dashboard-table-container">
                <table class="dashboard-table">
                    <thead></thead>
                    <tbody></tbody>
                </table>
            </div>
            <div class="dashboard-load-more-container" style="display:none; text-align:center; padding:12px;">
                <button class="dashboard-load-more-btn">Load More</button>
                <span class="dashboard-load-status"></span>
            </div>
            <div class="dashboard-action-bar" style="display:none;">
                <span class="action-bar-count">0 selected</span>
                <button class="action-bar-compare">Compare</button>
                <div class="action-bar-add-dropdown">
                    <button class="action-bar-add-btn">Add to Chart ▼</button>
                    <div class="action-bar-add-menu"></div>
                </div>
                <button class="action-bar-copy" title="Copy selected rows as TSV">Copy</button>
                <button class="action-bar-export" title="Export selected rows as CSV">Export</button>
                <button class="action-bar-clear">Clear</button>
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

        // Debounced server-side filter for better performance during typing
        const debouncedServerFilter = window.ChartUtils.debounce(() => {
            // Clear selection when filter changes
            this.clearSelection(card);
            // Reset to first page when filter changes, skip cache for fresh results
            this.loadData(card, false, true);
            if (window.saveCards) window.saveCards();
        }, 300);

        filterInput.addEventListener('input', (e) => {
            const raw = e.target.value;
            // Trailing space = exact ticker match
            this.filterExact = raw.endsWith(' ') && raw.trim().length > 0;
            this.filterText = raw.trim().toLowerCase();
            debouncedServerFilter();
        });

        viewSelect.addEventListener('change', (e) => {
            this.viewMode = e.target.value;
            this.renderTable(card);
            if (window.saveCards) window.saveCards();
        });

        refreshBtn.addEventListener('click', () => {
            // Skip cache on manual refresh
            this.loadData(card, false, true);
        });

        // Conditional formatting toggle
        const conditionalBtn = card.querySelector('.dashboard-conditional-btn');
        this._updateConditionalButton(conditionalBtn);
        conditionalBtn.addEventListener('click', () => {
            this.conditionalFormatting = !this.conditionalFormatting;
            this._updateConditionalButton(conditionalBtn);
            this.renderTable(card);
            if (window.saveCards) window.saveCards();
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

        // Copy to clipboard button
        const copyBtn = card.querySelector('.dashboard-copy-btn');
        copyBtn.addEventListener('click', () => {
            this.copyToClipboard();
        });

        // Export All button (server-side export)
        const exportAllBtn = card.querySelector('.dashboard-export-all-btn');
        exportAllBtn.addEventListener('click', () => {
            this.exportAll();
        });

        // Copy All button (server-side export to clipboard)
        const copyAllBtn = card.querySelector('.dashboard-copy-all-btn');
        copyAllBtn.addEventListener('click', () => {
            this.copyAll();
        });

        // Load More button (fallback for infinite scroll)
        const loadMoreBtn = card.querySelector('.dashboard-load-more-btn');
        loadMoreBtn.addEventListener('click', () => {
            this.loadMoreData(card);
        });

        // Infinite scroll - auto-load when near bottom
        const tableContainer = card.querySelector('.dashboard-table-container');
        this._setupInfiniteScroll(card, tableContainer);

        // Keyboard navigation
        this._setupKeyboardNavigation(card, tableContainer);

        // Columns dropdown
        const columnsBtn = card.querySelector('.dashboard-columns-btn');
        const columnsMenu = card.querySelector('.dashboard-columns-menu');
        this.initColumnsDropdown(card, columnsBtn, columnsMenu);

        // Action bar event handlers
        const actionBar = card.querySelector('.dashboard-action-bar');
        this._dashboardCard = card;  // Store reference for action bar updates

        const compareBtn = actionBar.querySelector('.action-bar-compare');
        compareBtn.addEventListener('click', () => this.compareTickers());

        const clearBtn = actionBar.querySelector('.action-bar-clear');
        clearBtn.addEventListener('click', () => this.clearSelection(card));

        const copySelectedBtn = actionBar.querySelector('.action-bar-copy');
        copySelectedBtn.addEventListener('click', () => this.copySelected());

        const exportSelectedBtn = actionBar.querySelector('.action-bar-export');
        exportSelectedBtn.addEventListener('click', () => this.exportSelected());

        const addDropdownBtn = actionBar.querySelector('.action-bar-add-btn');
        const addMenu = actionBar.querySelector('.action-bar-add-menu');
        addDropdownBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this._showAddToChartMenu(addMenu, addDropdownBtn);
        });

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
     * Update conditional formatting button appearance
     */
    _updateConditionalButton(btn) {
        if (!btn) return;
        if (this.conditionalFormatting) {
            btn.classList.add('active');
            btn.textContent = 'Conditional ✓';
        } else {
            btn.classList.remove('active');
            btn.textContent = 'Conditional';
        }
    },

    /**
     * Load dashboard data from API (with caching)
     * @param {HTMLElement} card - Dashboard card
     * @param {boolean} append - Whether to append to existing data
     * @param {boolean} skipCache - Force fresh fetch (e.g., on refresh button)
     */
    async loadData(card, append = false, skipCache = false) {
        console.log('[ChartDashboard] loadData called, append:', append, 'skipCache:', skipCache);
        const tbody = card.querySelector('.dashboard-table tbody');
        const loadMoreContainer = card.querySelector('.dashboard-load-more-container');
        const loadStatus = card.querySelector('.dashboard-load-status');
        const refreshIndicator = card.querySelector('.dashboard-refresh-indicator');

        const offset = append ? this.data.length : 0;
        // Build URL with filter parameter for server-side filtering
        let url = window.ChartUtils.apiUrl(`/api/dashboard?limit=${this.pageSize}&offset=${offset}`);
        if (this.filterText) {
            url += `&filter=${encodeURIComponent(this.filterText)}`;
        }
        const cacheKey = url;

        // Stale-While-Revalidate: show cached data immediately if available
        let cachedResult = null;
        if (!append && !skipCache && window.ChartUtils?.cache) {
            cachedResult = window.ChartUtils.cache.get(cacheKey);
            if (cachedResult) {
                console.log('[ChartDashboard] SWR: Showing cached data immediately');
                this._applyResult(card, cachedResult, append);
                // Show refresh indicator for background fetch
                if (refreshIndicator) refreshIndicator.style.display = 'inline';
            }
        }

        // Show skeleton only if no cached data
        if (!append && !cachedResult) {
            this.data = [];
            window.DashboardBase.renderSkeletonRows(tbody, 10, 12);
        }

        if (this.isLoading) return;
        this.isLoading = true;

        // Show loading status for infinite scroll
        if (append && loadStatus) {
            loadStatus.textContent = 'Loading more...';
        }

        try {
            console.log('[ChartDashboard] Fetching:', url);
            // Use deduplicated fetch to prevent duplicate requests on rapid clicks
            const result = await window.ChartUtils.requests.fetchJSON(url);

            // Cache the result (only for initial loads, not append)
            if (!append && window.ChartUtils?.cache) {
                window.ChartUtils.cache.set(cacheKey, result);
            }

            // Apply fresh data (even if we showed cached data first)
            this._applyResult(card, result, append);

            if (cachedResult) {
                console.log('[ChartDashboard] SWR: Updated with fresh data');
            }
        } catch (error) {
            console.error('[ChartDashboard] Dashboard load error:', error);
            // Only show error if we didn't have cached data
            if (!cachedResult) {
                window.DashboardBase.renderStatusRow(tbody, { colspan: 12, message: `Error loading data: ${error.message}` });
            }
        } finally {
            this.isLoading = false;
            if (refreshIndicator) refreshIndicator.style.display = 'none';
        }
    },

    /**
     * Apply fetched result to the dashboard (shared by initial load and SWR refresh)
     * @param {HTMLElement} card - Dashboard card
     * @param {Object} result - API response with data and total
     * @param {boolean} append - Whether to append to existing data
     */
    _applyResult(card, result, append) {
        const loadMoreContainer = card.querySelector('.dashboard-load-more-container');
        const loadStatus = card.querySelector('.dashboard-load-status');

        // Handle paginated response format
        const newData = result.data || result;
        this.totalCount = result.total || newData.length;

        if (append) {
            this.data = [...this.data, ...newData];
        } else {
            this.data = newData;
        }

        this.hasMore = this.data.length < this.totalCount;

        console.log('[ChartDashboard] Applied:', newData.length, 'tickers, total:', this.data.length, '/', this.totalCount);

        this.renderStats(card);
        this.renderTable(card);

        // Show/hide Load More button
        if (this.hasMore) {
            loadMoreContainer.style.display = 'block';
            loadStatus.textContent = `Showing ${this.data.length} of ${this.totalCount}`;
        } else {
            loadMoreContainer.style.display = 'none';
        }

        // Show/hide Export All / Copy All buttons when there's more data to export
        const exportAllBtn = card.querySelector('.dashboard-export-all-btn');
        const copyAllBtn = card.querySelector('.dashboard-copy-all-btn');
        if (this.hasMore) {
            exportAllBtn.style.display = 'inline-block';
            exportAllBtn.textContent = `Export All (${this.totalCount})`;
            copyAllBtn.style.display = 'inline-block';
            copyAllBtn.textContent = `Copy All (${this.totalCount})`;
        } else {
            exportAllBtn.style.display = 'none';
            copyAllBtn.style.display = 'none';
        }
    },

    /**
     * Load more data (pagination)
     */
    async loadMoreData(card) {
        if (this.isLoading || !this.hasMore) return;

        const loadMoreBtn = card.querySelector('.dashboard-load-more-btn');
        const originalText = loadMoreBtn.textContent;
        loadMoreBtn.textContent = 'Loading...';
        loadMoreBtn.disabled = true;

        try {
            await this.loadData(card, true);
        } finally {
            loadMoreBtn.textContent = originalText;
            loadMoreBtn.disabled = false;
        }
    },

    /**
     * Setup infinite scroll for auto-loading more data
     * @param {HTMLElement} card - Dashboard card element
     * @param {HTMLElement} container - Scroll container element
     */
    _setupInfiniteScroll(card, container) {
        if (!container) return;

        // Threshold: load more when within 200px of bottom
        const SCROLL_THRESHOLD = 200;

        // Debounce scroll checks to avoid excessive calls
        let scrollTimeout = null;

        const checkScroll = () => {
            if (this.isLoading || !this.hasMore) return;

            const { scrollTop, scrollHeight, clientHeight } = container;
            const distanceFromBottom = scrollHeight - scrollTop - clientHeight;

            if (distanceFromBottom < SCROLL_THRESHOLD) {
                console.log('[ChartDashboard] Infinite scroll triggered, distance:', distanceFromBottom);
                this.loadMoreData(card);
            }
        };

        container.addEventListener('scroll', () => {
            if (scrollTimeout) return;  // Throttle: one check per frame
            scrollTimeout = requestAnimationFrame(() => {
                scrollTimeout = null;
                checkScroll();
            });
        });

        // Store reference for potential cleanup
        container._infiniteScrollCheck = checkScroll;
    },

    /**
     * Setup keyboard navigation for dashboard rows
     * @param {HTMLElement} card - Dashboard card element
     * @param {HTMLElement} container - Table container element
     */
    _setupKeyboardNavigation(card, container) {
        if (!container) return;

        const tbody = card.querySelector('.dashboard-table tbody');

        // Make container focusable
        container.setAttribute('tabindex', '0');

        container.addEventListener('keydown', (e) => {
            // Only handle if we have data rows
            const rows = tbody.querySelectorAll('tr:not(.virtual-spacer-top):not(.virtual-spacer-bottom):not(.dashboard-group-header):not(.dashboard-loading)');
            if (rows.length === 0) return;

            switch (e.key) {
                case 'ArrowDown':
                    e.preventDefault();
                    this._moveFocus(card, container, 1, rows);
                    break;
                case 'ArrowUp':
                    e.preventDefault();
                    this._moveFocus(card, container, -1, rows);
                    break;
                case 'Enter':
                    e.preventDefault();
                    this._selectFocusedRow(card, rows);
                    break;
                case 'Home':
                    e.preventDefault();
                    this._setFocusedRow(card, container, 0, rows);
                    break;
                case 'End':
                    e.preventDefault();
                    this._setFocusedRow(card, container, rows.length - 1, rows);
                    break;
                case 'Escape':
                    this._clearFocus(card);
                    break;
            }
        });

        // Focus first row when clicking into table (if no row focused)
        container.addEventListener('focus', () => {
            if (this.focusedRowIndex === -1) {
                const rows = tbody.querySelectorAll('tr:not(.virtual-spacer-top):not(.virtual-spacer-bottom):not(.dashboard-group-header):not(.dashboard-loading)');
                if (rows.length > 0) {
                    this._setFocusedRow(card, container, 0, rows);
                }
            }
        });

        // Clear focus when clicking outside
        container.addEventListener('blur', () => {
            // Delay to allow click events to fire first
            setTimeout(() => {
                if (!container.contains(document.activeElement)) {
                    this._clearFocus(card);
                }
            }, 100);
        });
    },

    /**
     * Move focus by delta rows
     */
    _moveFocus(card, container, delta, rows) {
        let newIndex = this.focusedRowIndex + delta;

        // Wrap around or clamp
        if (newIndex < 0) newIndex = 0;
        if (newIndex >= rows.length) newIndex = rows.length - 1;

        this._setFocusedRow(card, container, newIndex, rows);
    },

    /**
     * Set focused row by index
     */
    _setFocusedRow(card, container, index, rows) {
        // Clear previous focus
        const prevFocused = card.querySelector('.dashboard-row-focused');
        if (prevFocused) prevFocused.classList.remove('dashboard-row-focused');

        // Set new focus
        this.focusedRowIndex = index;
        const row = rows[index];
        if (row) {
            row.classList.add('dashboard-row-focused');

            // Scroll into view if needed
            const containerRect = container.getBoundingClientRect();
            const rowRect = row.getBoundingClientRect();

            if (rowRect.top < containerRect.top + 40) {
                // Row is above visible area (account for sticky header)
                row.scrollIntoView({ block: 'start', behavior: 'smooth' });
            } else if (rowRect.bottom > containerRect.bottom) {
                // Row is below visible area
                row.scrollIntoView({ block: 'end', behavior: 'smooth' });
            }
        }
    },

    /**
     * Select the currently focused row (trigger ticker action)
     */
    _selectFocusedRow(card, rows) {
        if (this.focusedRowIndex < 0 || this.focusedRowIndex >= rows.length) return;

        const row = rows[this.focusedRowIndex];
        const ticker = row?.dataset?.ticker;
        if (ticker) {
            window.DashboardBase.setGlobalSearchTicker(ticker);
        }
    },

    /**
     * Clear row focus
     */
    _clearFocus(card) {
        const prevFocused = card.querySelector('.dashboard-row-focused');
        if (prevFocused) prevFocused.classList.remove('dashboard-row-focused');
        this.focusedRowIndex = -1;
    },

    /**
     * Render summary statistics
     */
    renderStats(card) {
        const statsEl = card.querySelector('.dashboard-stats');
        const data = this.data;

        const loadedTickers = data.length;
        const totalTickers = this.totalCount || loadedTickers;
        const tickersWithPages = data.filter(d => d.pages && d.pages.length > 0).length;
        const avgDailyChange = loadedTickers > 0
            ? data.reduce((sum, d) => sum + (d.daily_change || 0), 0) / loadedTickers
            : 0;
        const gainers = data.filter(d => d.daily_change > 0).length;
        const losers = data.filter(d => d.daily_change < 0).length;

        const tickerLabel = this.hasMore ? `Loaded / Total` : `Total Tickers`;
        const tickerValue = this.hasMore
            ? `${loadedTickers.toLocaleString()} / ${totalTickers.toLocaleString()}`
            : totalTickers.toLocaleString();

        statsEl.innerHTML = `
            <div class="dashboard-stat">
                <span class="dashboard-stat-label">${tickerLabel}</span>
                <span class="dashboard-stat-value">${tickerValue}</span>
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
            { key: 'select', label: '' },
            { key: 'actions', label: '' },
            { key: 'ticker', label: 'Ticker' },
            { key: 'sparkline', label: '30D', noSort: true },
            { key: 'sparkline1y', label: '1Y', noSort: true },
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

        // Initialize column order if not set (exclude select/actions - always first)
        if (!this.columnOrder) {
            this.columnOrder = defaultColumns.filter(c => c.key !== 'select' && c.key !== 'actions').map(c => c.key);
        } else {
            // Add any new columns that were added after the saved state
            const defaultKeys = defaultColumns.filter(c => c.key !== 'select' && c.key !== 'actions').map(c => c.key);
            for (const key of defaultKeys) {
                if (!this.columnOrder.includes(key)) {
                    // Insert new column at its default position
                    const defaultIndex = defaultKeys.indexOf(key);
                    const insertIndex = Math.min(defaultIndex, this.columnOrder.length);
                    this.columnOrder.splice(insertIndex, 0, key);
                }
            }
        }

        // Build columns array: select + actions first (fixed), then user-ordered columns
        const columnMap = {};
        defaultColumns.forEach(c => columnMap[c.key] = c);
        const selectCol = columnMap['select'];
        const actionsCol = columnMap['actions'];
        const orderedCols = this.columnOrder
            .filter(key => key !== 'select' && key !== 'actions')  // Ensure fixed cols not duplicated
            .map(key => columnMap[key])
            .filter(Boolean);
        const columns = [selectCol, actionsCol, ...orderedCols].filter(Boolean);

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
                // Select column: checkbox for select-all
                if (col.key === 'select') {
                    return `<th class="select-header" style="width:32px;min-width:32px;cursor:default;"><input type="checkbox" class="select-all-checkbox" title="Select all visible"></th>`;
                }
                // Actions column: non-sortable, non-draggable, fixed width (no data-column to prevent sorting)
                if (col.key === 'actions') {
                    return `<th class="actions-header" style="width:32px;min-width:32px;cursor:default;"></th>`;
                }
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
                // Clear selection when sort changes
                this.clearSelection(card);
                this.renderTable(card);
                if (window.saveCards) window.saveCards();
            }
        });

        // ChartDashboard-specific overrides: column resize + drag
        this.initColumnResize(card, thead);
        this.initColumnDrag(card, thead);

        // Setup select-all checkbox handler
        const selectAllCheckbox = thead.querySelector('.select-all-checkbox');
        if (selectAllCheckbox) {
            selectAllCheckbox.addEventListener('change', (e) => {
                this._handleSelectAll(e.target.checked, filteredData);
                this._updateActionBar();
            });
        }

        // Render body
        const container = tbody.closest('.dashboard-table-container');
        if (this.viewMode === 'grouped') {
            // Disable virtual scrolling for grouped view (complex nested structure)
            if (container) this._removeScrollHandler(container);
            this.renderGroupedBody(tbody, filteredData, columns);
        } else if (this.viewMode === 'grouped-chart') {
            // Disable virtual scrolling for grouped view
            if (container) this._removeScrollHandler(container);
            this.renderGroupedByChartBody(tbody, filteredData, columns);
        } else {
            this.renderFlatBody(tbody, filteredData, columns, card);
        }

        // Trigger sparkline fetch for visible rows
        this._triggerSparklineFetch(card);

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
                    const newWidth = Math.max(0, startWidth + (moveEvent.pageX - startX));
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
        // Default column definitions for building the menu (exclude actions - always visible)
        const defaultColumns = [
            { key: 'ticker', label: 'Ticker' },
            { key: 'sparkline', label: '30D' },
            { key: 'sparkline1y', label: '1Y' },
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
     * Render flat table body with optional virtual scrolling
     * @param {HTMLElement} tbody - Table body element
     * @param {Array} data - Filtered/sorted data array
     * @param {Array} columns - Column definitions
     * @param {HTMLElement} [card] - Card element (needed for scroll handler setup)
     */
    renderFlatBody(tbody, data, columns, card) {
        const container = tbody.closest('.dashboard-table-container');
        if (!container) {
            // Fallback: render all rows
            tbody.innerHTML = data.map(row => this.renderRow(row, columns)).join('');
            this.attachRowHandlers(tbody);
            return;
        }

        const containerHeight = container.clientHeight || 500;
        const scrollTop = container.scrollTop || 0;

        const range = window.DashboardBase.calcVisibleRange({
            scrollTop,
            containerHeight,
            totalRows: data.length
        });

        if (!range.shouldVirtualize) {
            // Small dataset - render all rows normally
            tbody.innerHTML = data.map(row => this.renderRow(row, columns)).join('');
            this.attachRowHandlers(tbody);
            this._removeScrollHandler(container);
            return;
        }

        // Virtual scrolling: render only visible rows with spacers
        const visibleData = data.slice(range.startIndex, range.endIndex);
        const rowHeight = window.DashboardBase.VIRTUAL_SCROLL.ROW_HEIGHT;

        // Build HTML with top/bottom spacer rows for scroll height
        let html = '';
        if (range.topPadding > 0) {
            html += `<tr class="virtual-spacer-top"><td colspan="${columns.length}" style="height:${range.topPadding}px;padding:0;border:none;"></td></tr>`;
        }
        html += visibleData.map(row => this.renderRow(row, columns)).join('');
        if (range.bottomPadding > 0) {
            html += `<tr class="virtual-spacer-bottom"><td colspan="${columns.length}" style="height:${range.bottomPadding}px;padding:0;border:none;"></td></tr>`;
        }

        tbody.innerHTML = html;
        this.attachRowHandlers(tbody);

        // Setup scroll handler if card provided and not already set
        if (card && !container._virtualScrollHandler) {
            this._setupScrollHandler(container, card, data, columns);
        }

        // Store current data reference for scroll handler
        container._virtualData = data;
        container._virtualColumns = columns;
    },

    /**
     * Setup scroll handler for virtual scrolling
     */
    _setupScrollHandler(container, card, data, columns) {
        const self = this;
        container._virtualScrollHandler = window.DashboardBase.createVirtualScrollHandler((scrollTop) => {
            // Use stored data/columns (may be updated on filter/sort)
            const currentData = container._virtualData || data;
            const currentColumns = container._virtualColumns || columns;

            const tbody = container.querySelector('tbody');
            if (!tbody) return;

            const containerHeight = container.clientHeight || 500;
            const range = window.DashboardBase.calcVisibleRange({
                scrollTop,
                containerHeight,
                totalRows: currentData.length
            });

            if (!range.shouldVirtualize) return;

            // Re-render visible rows
            const visibleData = currentData.slice(range.startIndex, range.endIndex);

            let html = '';
            if (range.topPadding > 0) {
                html += `<tr class="virtual-spacer-top"><td colspan="${currentColumns.length}" style="height:${range.topPadding}px;padding:0;border:none;"></td></tr>`;
            }
            html += visibleData.map(row => self.renderRow(row, currentColumns)).join('');
            if (range.bottomPadding > 0) {
                html += `<tr class="virtual-spacer-bottom"><td colspan="${currentColumns.length}" style="height:${range.bottomPadding}px;padding:0;border:none;"></td></tr>`;
            }

            tbody.innerHTML = html;
            self.attachRowHandlers(tbody);
        });

        container.addEventListener('scroll', container._virtualScrollHandler);
    },

    /**
     * Remove scroll handler when no longer needed
     */
    _removeScrollHandler(container) {
        if (container._virtualScrollHandler) {
            container.removeEventListener('scroll', container._virtualScrollHandler);
            container._virtualScrollHandler = null;
        }
        container._virtualData = null;
        container._virtualColumns = null;
    },

    /**
     * Render grouped table body
     */
    renderGroupedBody(tbody, data, columns) {
        // Group by first page
        const groups = {};
        const noPage = [];
        const colCount = columns.length;
        const escape = window.DashboardBase.escapeHtml;

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
            html += `<tr class="dashboard-group-header"><td colspan="${colCount}">${escape(groupName)} (${groups[groupName].length})</td></tr>`;
            html += groups[groupName].map(row => this.renderRow(row, columns)).join('');
        });

        if (noPage.length > 0) {
            html += `<tr class="dashboard-group-header"><td colspan="${colCount}">Not in Charts (${noPage.length})</td></tr>`;
            html += noPage.map(row => this.renderRow(row, columns)).join('');
        }

        tbody.innerHTML = html;
        this.attachRowHandlers(tbody);
    },

    /**
     * Render grouped table body by page and chart
     */
    renderGroupedByChartBody(tbody, data, columns) {
        // Group by page, then by chart within each page
        const pageGroups = {};  // pageName -> { chartName -> [rows] }
        const noPage = [];
        const colCount = columns.length;
        const escape = window.DashboardBase.escapeHtml;

        data.forEach(row => {
            if (row.pages && row.pages.length > 0) {
                // Use first page entry for grouping
                const pageEntry = row.pages[0];
                const pageName = pageEntry.page_name;
                const chartTitle = pageEntry.chart_title || 'Untitled Chart';

                if (!pageGroups[pageName]) pageGroups[pageName] = {};
                if (!pageGroups[pageName][chartTitle]) pageGroups[pageName][chartTitle] = [];
                pageGroups[pageName][chartTitle].push(row);
            } else {
                noPage.push(row);
            }
        });

        // Sort page names
        const sortedPages = Object.keys(pageGroups).sort();

        let html = '';
        sortedPages.forEach(pageName => {
            const charts = pageGroups[pageName];
            const pageTickerCount = Object.values(charts).reduce((sum, arr) => sum + arr.length, 0);

            // Page header
            html += `<tr class="dashboard-group-header dashboard-page-header"><td colspan="${colCount}">${escape(pageName)} (${pageTickerCount})</td></tr>`;

            // Sort chart names within page
            const sortedCharts = Object.keys(charts).sort();
            sortedCharts.forEach(chartTitle => {
                const rows = charts[chartTitle];
                // Chart sub-header
                html += `<tr class="dashboard-group-header dashboard-chart-header"><td colspan="${colCount}">&nbsp;&nbsp;${escape(chartTitle)} (${rows.length})</td></tr>`;
                html += rows.map(row => this.renderRow(row, columns)).join('');
            });
        });

        if (noPage.length > 0) {
            html += `<tr class="dashboard-group-header dashboard-page-header"><td colspan="${colCount}">Not in Charts (${noPage.length})</td></tr>`;
            html += noPage.map(row => this.renderRow(row, columns)).join('');
        }

        tbody.innerHTML = html;
        this.attachRowHandlers(tbody);
    },

    /**
     * Render a single row based on provided columns
     * @param {Object} row - Row data
     * @param {Array} columns - Column definitions array
     */
    renderRow(row, columns) {
        const conditional = this.conditionalFormatting;

        const formatChange = (val) => {
            if (val === null || val === undefined) return { html: '-', bgClass: '' };
            const isPositive = val >= 0;
            const textCls = isPositive ? 'change-positive' : 'change-negative';
            const sign = isPositive ? '+' : '';
            const arrow = conditional ? (isPositive ? '▲ ' : '▼ ') : '';
            const bgClass = conditional ? (isPositive ? 'cond-bg-positive' : 'cond-bg-negative') : '';
            return {
                html: `<span class="${textCls}">${arrow}${sign}${val.toFixed(2)}%</span>`,
                bgClass
            };
        };

        const formatPrice = (val) => {
            if (val === null || val === undefined) return '-';
            return val.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        };

        const pagesHtml = row.pages && row.pages.length > 0
            ? row.pages.map(p => `<a class="page-link" data-page="${p.page}">${window.DashboardBase.escapeHtml(p.page_name)}</a>`).join(', ')
            : '-';

        // Pre-compute change values for cell renderers
        const dailyChange = formatChange(row.daily_change);
        const weeklyChange = formatChange(row.weekly_change);
        const monthlyChange = formatChange(row.monthly_change);
        const yearlyChange = formatChange(row.yearly_change);

        // Check if this row is selected
        const isSelected = this.selectedTickers.has(row.ticker);

        // Sparkline renderer (30D)
        const renderSparkline = () => {
            const cached = this.sparklineCache.get(row.ticker);
            if (!cached) {
                // Mark for fetching and return placeholder
                this.sparklinePendingTickers.add(row.ticker);
                return `<td class="sparkline-cell" data-ticker="${row.ticker}"><span class="sparkline-loading">...</span></td>`;
            }
            // Render SVG sparkline
            const { data, pctChange } = cached;
            const svg = this._renderSparklineSVG(data, pctChange);
            const sign = pctChange >= 0 ? '+' : '';
            const colorClass = pctChange >= 0 ? 'sparkline-up' : 'sparkline-down';
            const title = `30D: ${sign}${pctChange.toFixed(1)}%`;
            return `<td class="sparkline-cell ${colorClass}" title="${title}" aria-label="${title}">${svg}</td>`;
        };

        // Sparkline renderer (1Y)
        const renderSparkline1y = () => {
            const cached = this.sparkline1yCache.get(row.ticker);
            if (!cached) {
                this.sparkline1yPendingTickers.add(row.ticker);
                return `<td class="sparkline-cell" data-ticker-1y="${row.ticker}"><span class="sparkline-loading">...</span></td>`;
            }
            const { data, pctChange } = cached;
            const svg = this._renderSparklineSVG(data, pctChange);
            const sign = pctChange >= 0 ? '+' : '';
            const colorClass = pctChange >= 0 ? 'sparkline-up' : 'sparkline-down';
            const title = `1Y: ${sign}${pctChange.toFixed(1)}%`;
            return `<td class="sparkline-cell ${colorClass}" title="${title}" aria-label="${title}">${svg}</td>`;
        };

        // Cell renderers for each column
        const cellRenderers = {
            select: () => `<td class="select-cell"><input type="checkbox" class="row-select-checkbox" data-ticker="${row.ticker}" ${isSelected ? 'checked' : ''}></td>`,
            actions: () => `<td class="actions-cell"><button class="quick-chart-btn" data-ticker="${row.ticker}" title="Add to chart">+</button></td>`,
            ticker: () => `<td class="ticker-cell">${window.DashboardBase.escapeHtml(row.ticker)}</td>`,
            sparkline: renderSparkline,
            sparkline1y: renderSparkline1y,
            name: () => `<td>${window.DashboardBase.escapeHtml(row.name) || '-'}</td>`,
            latest_price: () => `<td class="price-cell">${formatPrice(row.latest_price)}</td>`,
            daily_change: () => `<td class="price-cell ${dailyChange.bgClass}">${dailyChange.html}</td>`,
            weekly_change: () => `<td class="price-cell ${weeklyChange.bgClass}">${weeklyChange.html}</td>`,
            monthly_change: () => `<td class="price-cell ${monthlyChange.bgClass}">${monthlyChange.html}</td>`,
            yearly_change: () => `<td class="price-cell ${yearlyChange.bgClass}">${yearlyChange.html}</td>`,
            high_52w: () => `<td class="price-cell">${formatPrice(row.high_52w)}</td>`,
            low_52w: () => `<td class="price-cell">${formatPrice(row.low_52w)}</td>`,
            data_points: () => `<td class="price-cell">${row.data_points ? row.data_points.toLocaleString() : '-'}</td>`,
            pages: () => `<td>${pagesHtml}</td>`
        };

        // Render cells in column order from provided columns array
        const cells = columns.map(col => {
            const renderer = cellRenderers[col.key];
            return renderer ? renderer() : '<td>-</td>';
        }).join('');

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

            // Row checkbox click - toggle selection
            if (target.classList.contains('row-select-checkbox')) {
                const ticker = target.dataset.ticker;
                if (ticker) {
                    if (target.checked) {
                        this.selectedTickers.add(ticker);
                    } else {
                        this.selectedTickers.delete(ticker);
                    }
                    this._updateActionBar();
                    this._updateSelectAllCheckbox(tbody);
                }
                return;
            }

            // Quick chart button click - show dropdown
            const quickChartBtn = target.closest('.quick-chart-btn');
            if (quickChartBtn) {
                e.preventDefault();
                e.stopPropagation();
                const ticker = quickChartBtn.dataset.ticker;
                if (ticker) {
                    this.showQuickChartMenu(quickChartBtn, ticker);
                }
                return;
            }

            // Ticker cell click - put ticker in global search
            const tickerCell = target.closest('.ticker-cell');
            if (tickerCell) {
                const ticker = tickerCell.closest('tr')?.dataset.ticker;
                if (ticker) {
                    window.DashboardBase.setGlobalSearchTicker(ticker);
                }
                return;
            }

            // Page link click - open page in new tab
            const pageLink = target.closest('.page-link');
            if (pageLink) {
                e.preventDefault();
                const pageNum = parseInt(pageLink.dataset.page, 10);
                const url = new URL(window.location.href);
                url.searchParams.set('page', pageNum);
                window.open(url.toString(), '_blank');
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
     * Render SVG sparkline from data points
     * @param {Array} data - Array of {time, value} points (rebased to 100)
     * @param {number} pctChange - Percent change from start to end
     * @returns {string} SVG markup
     */
    _renderSparklineSVG(data, pctChange) {
        if (!data || data.length < 2) return '';

        const width = 60;
        const height = 20;
        const padding = 2;

        // Find min/max for scaling
        const values = data.map(d => d.value);
        const min = Math.min(...values);
        const max = Math.max(...values);
        const range = max - min || 1;

        // Generate path points
        const points = data.map((d, i) => {
            const x = padding + (i / (data.length - 1)) * (width - 2 * padding);
            const y = height - padding - ((d.value - min) / range) * (height - 2 * padding);
            return `${x.toFixed(1)},${y.toFixed(1)}`;
        });

        const pathData = 'M' + points.join(' L');
        const color = pctChange >= 0 ? '#22c55e' : '#ef4444'; // green/red

        return `<svg class="sparkline-svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
            <path d="${pathData}" fill="none" stroke="${color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>`;
    },

    /**
     * Fetch sparklines for pending tickers
     * @param {HTMLElement} card - Dashboard card element
     */
    async _fetchSparklines(card) {
        if (this.sparklinePendingTickers.size === 0) return;

        // Abort any in-flight request
        if (this.sparklineAbortController) {
            this.sparklineAbortController.abort();
        }
        this.sparklineAbortController = new AbortController();

        // Get tickers to fetch (limit to 50)
        const tickers = Array.from(this.sparklinePendingTickers).slice(0, 50);
        this.sparklinePendingTickers.clear();

        try {
            const url = `${window.API_BASE_URL || ''}/api/dashboard/sparklines?tickers=${encodeURIComponent(tickers.join(','))}&days=30`;
            const response = await fetch(url, { signal: this.sparklineAbortController.signal });

            if (!response.ok) {
                console.warn('[Dashboard] Sparkline fetch failed:', response.status);
                return;
            }

            const data = await response.json();

            // Cache results and update cells
            for (const [ticker, points] of Object.entries(data)) {
                if (points && points.length >= 2) {
                    const firstVal = points[0].value;
                    const lastVal = points[points.length - 1].value;
                    const pctChange = ((lastVal - firstVal) / firstVal) * 100;
                    this.sparklineCache.set(ticker, { data: points, pctChange });

                    // Update the cell in the DOM
                    const cell = card.querySelector(`.sparkline-cell[data-ticker="${ticker}"]`);
                    if (cell) {
                        const svg = this._renderSparklineSVG(points, pctChange);
                        const sign = pctChange >= 0 ? '+' : '';
                        const colorClass = pctChange >= 0 ? 'sparkline-up' : 'sparkline-down';
                        const title = `30D: ${sign}${pctChange.toFixed(1)}%`;
                        cell.className = `sparkline-cell ${colorClass}`;
                        cell.title = title;
                        cell.setAttribute('aria-label', title);
                        cell.innerHTML = svg;
                    }
                }
            }

            console.log(`[Dashboard] Fetched ${Object.keys(data).length} sparklines`);
        } catch (err) {
            if (err.name === 'AbortError') return; // Expected on abort
            console.error('[Dashboard] Sparkline fetch error:', err);
        }
    },

    /**
     * Trigger sparkline fetch after table render
     * @param {HTMLElement} card - Dashboard card element
     */
    _triggerSparklineFetch(card) {
        // Debounce to batch multiple render calls
        if (this._sparklineFetchTimeout) {
            clearTimeout(this._sparklineFetchTimeout);
        }
        this._sparklineFetchTimeout = setTimeout(() => {
            this._fetchSparklines(card);
            this._fetchSparklines1y(card);
        }, 100);
    },

    /**
     * Fetch 1Y sparklines for pending tickers
     * @param {HTMLElement} card - Dashboard card element
     */
    async _fetchSparklines1y(card) {
        if (this.sparkline1yPendingTickers.size === 0) return;

        // Abort any in-flight request
        if (this.sparkline1yAbortController) {
            this.sparkline1yAbortController.abort();
        }
        this.sparkline1yAbortController = new AbortController();

        // Get tickers to fetch (limit to 50)
        const tickers = Array.from(this.sparkline1yPendingTickers).slice(0, 50);
        this.sparkline1yPendingTickers.clear();

        try {
            const url = `${window.API_BASE_URL || ''}/api/dashboard/sparklines?tickers=${encodeURIComponent(tickers.join(','))}&days=365`;
            const response = await fetch(url, { signal: this.sparkline1yAbortController.signal });

            if (!response.ok) {
                console.warn('[Dashboard] 1Y Sparkline fetch failed:', response.status);
                return;
            }

            const data = await response.json();

            // Cache results and update cells
            for (const [ticker, points] of Object.entries(data)) {
                if (points && points.length >= 2) {
                    const firstVal = points[0].value;
                    const lastVal = points[points.length - 1].value;
                    const pctChange = ((lastVal - firstVal) / firstVal) * 100;
                    this.sparkline1yCache.set(ticker, { data: points, pctChange });

                    // Update the cell in the DOM
                    const cell = card.querySelector(`.sparkline-cell[data-ticker-1y="${ticker}"]`);
                    if (cell) {
                        const svg = this._renderSparklineSVG(points, pctChange);
                        const sign = pctChange >= 0 ? '+' : '';
                        const colorClass = pctChange >= 0 ? 'sparkline-up' : 'sparkline-down';
                        const title = `1Y: ${sign}${pctChange.toFixed(1)}%`;
                        cell.className = `sparkline-cell ${colorClass}`;
                        cell.title = title;
                        cell.setAttribute('aria-label', title);
                        cell.innerHTML = svg;
                    }
                }
            }

            console.log(`[Dashboard] Fetched ${Object.keys(data).length} 1Y sparklines`);
        } catch (err) {
            if (err.name === 'AbortError') return;
            console.error('[Dashboard] 1Y Sparkline fetch error:', err);
        }
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
     * Copy current filtered/sorted data to clipboard as TSV
     */
    copyToClipboard() {
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

        // Build TSV header - use visible columns only (same as CSV)
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

        // Build TSV content (tab-separated)
        const header = visibleColumns.map(c => c.label).join('\t');
        const rows = filteredData.map(row => {
            return visibleColumns.map(col => {
                let value = row[col.key];
                // Pages: use page names (more informative) instead of count
                if (col.key === 'pages') {
                    if (row.pages && Array.isArray(row.pages) && row.pages.length > 0) {
                        value = row.pages.map(p => p.page_name).join(', ');
                    } else {
                        value = '';
                    }
                }
                if (value === null || value === undefined) {
                    return '';
                }
                if (typeof value === 'number') {
                    return value.toFixed ? value.toFixed(2) : String(value);
                }
                // Replace tabs/newlines in string values to avoid breaking TSV
                return String(value).replace(/[\t\n\r]/g, ' ');
            }).join('\t');
        });

        const rowCount = filteredData.length;

        // Handle empty result
        if (rowCount === 0) {
            if (window.Toast?.info) {
                window.Toast.info('Nothing to copy');
            }
            return;
        }

        const tsv = [header, ...rows].join('\n');

        // Copy to clipboard
        this._writeToClipboard(tsv, rowCount);
    },

    /**
     * Write text to clipboard with fallback
     * @param {string} text - Text to copy
     * @param {number} rowCount - Number of rows (for toast message)
     */
    async _writeToClipboard(text, rowCount) {
        try {
            // Modern clipboard API (works on localhost and HTTPS)
            if (navigator.clipboard && navigator.clipboard.writeText) {
                await navigator.clipboard.writeText(text);
                if (window.Toast?.success) {
                    window.Toast.success(`Copied ${rowCount} rows to clipboard`);
                }
                return;
            }
        } catch (err) {
            console.warn('[ChartDashboard] Clipboard API failed, using fallback:', err);
        }

        // Fallback: textarea + execCommand
        try {
            const textarea = document.createElement('textarea');
            textarea.value = text;
            textarea.style.position = 'fixed';
            textarea.style.left = '-9999px';
            textarea.style.top = '0';
            document.body.appendChild(textarea);
            textarea.focus();
            textarea.select();
            const success = document.execCommand('copy');
            document.body.removeChild(textarea);

            if (success) {
                if (window.Toast?.success) {
                    window.Toast.success(`Copied ${rowCount} rows to clipboard`);
                }
            } else {
                throw new Error('execCommand copy failed');
            }
        } catch (err) {
            console.error('[ChartDashboard] Clipboard fallback failed:', err);
            if (window.Toast?.error) {
                window.Toast.error('Failed to copy to clipboard');
            }
        }
    },

    /**
     * Build export URL with current filter/sort parameters
     * @param {string} format - 'csv' or 'tsv'
     * @returns {string} URL for export endpoint
     */
    _buildExportUrl(format) {
        const params = new URLSearchParams();
        params.set('format', format);
        if (this.filterText) params.set('filter', this.filterText);
        if (this.sortColumn) params.set('sort', this.sortColumn);
        if (this.sortDirection) params.set('sortDir', this.sortDirection);
        return window.ChartUtils.apiUrl(`/api/dashboard/export?${params.toString()}`);
    },

    /**
     * Export all filtered rows to CSV (server-side export)
     * Uses anchor download for better popup-blocker compatibility
     */
    exportAll() {
        const url = this._buildExportUrl('csv');
        // Use anchor with download attribute for popup-blocker-proof download
        const anchor = document.createElement('a');
        anchor.href = url;
        anchor.download = '';  // Let server set filename via Content-Disposition
        anchor.style.display = 'none';
        document.body.appendChild(anchor);
        anchor.click();
        document.body.removeChild(anchor);

        if (window.Toast?.info) {
            window.Toast.info(`Exporting ${this.totalCount} rows...`);
        }
    },

    /**
     * Copy all filtered rows to clipboard (server-side fetch + clipboard)
     * Fetches TSV from server and copies to clipboard
     */
    async copyAll() {
        const card = this._dashboardCard;
        const copyAllBtn = card?.querySelector('.dashboard-copy-all-btn');
        const originalText = copyAllBtn?.textContent || '';

        // Disable button and show loading state
        if (copyAllBtn) {
            copyAllBtn.disabled = true;
            copyAllBtn.textContent = 'Copying...';
        }

        const url = this._buildExportUrl('tsv');

        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const tsv = await response.text();
            const lineCount = tsv.split('\n').length - 1; // Subtract header

            // Check if result was truncated
            const truncated = response.headers.get('X-Export-Truncated') === '1';
            const totalCount = response.headers.get('X-Export-Total');

            await this._writeToClipboard(tsv, lineCount);

            if (truncated && totalCount) {
                if (window.Toast?.warning) {
                    window.Toast.warning(`Copied ${lineCount} rows (capped from ${totalCount})`);
                }
            }
        } catch (error) {
            console.error('[ChartDashboard] Copy all failed:', error);
            if (window.Toast?.error) {
                window.Toast.error(`Failed to copy: ${error.message}`);
            }
        } finally {
            // Re-enable button
            if (copyAllBtn) {
                copyAllBtn.disabled = false;
                copyAllBtn.textContent = originalText;
            }
        }
    },

    /**
     * Show quick chart dropdown menu
     * @param {HTMLElement} btn - The button element clicked
     * @param {string} ticker - The ticker symbol
     */
    showQuickChartMenu(btn, ticker) {
        // Remove any existing menu
        const existing = document.querySelector('.quick-chart-menu');
        if (existing) existing.remove();

        // Get existing charts on the active page
        const activePage = window.PageManager?.getActivePage?.() || '1';
        const existingCharts = this.getChartsOnPage(activePage);
        const escape = window.DashboardBase.escapeHtml;

        // Build menu using DOM nodes (safer than innerHTML for user content)
        const menu = document.createElement('div');
        menu.className = 'quick-chart-menu';

        // "New chart" item
        const newItem = document.createElement('div');
        newItem.className = 'quick-chart-menu-item';
        newItem.dataset.action = 'new';
        newItem.dataset.ticker = ticker;
        newItem.textContent = 'New chart';
        menu.appendChild(newItem);

        if (existingCharts.length > 0) {
            const divider = document.createElement('div');
            divider.className = 'quick-chart-menu-divider';
            menu.appendChild(divider);

            existingCharts.forEach((chart, idx) => {
                const label = chart.title || chart.tickers?.slice(0, 3).join(', ') || `Chart ${idx + 1}`;
                const truncatedLabel = label.length > 25 ? label.slice(0, 22) + '...' : label;

                const item = document.createElement('div');
                item.className = 'quick-chart-menu-item';
                item.dataset.action = 'add';
                item.dataset.ticker = ticker;
                item.dataset.cardId = chart.id;
                item.textContent = `Add to: ${truncatedLabel}`;
                menu.appendChild(item);
            });
        }

        // Position menu below button
        const btnRect = btn.getBoundingClientRect();
        menu.style.position = 'fixed';
        menu.style.left = `${btnRect.left}px`;
        menu.style.top = `${btnRect.bottom + 2}px`;
        menu.style.zIndex = '10001';

        // Close on click outside
        let clickHandler, scrollHandler, resizeHandler;

        // Close menu helper - cleans up all event listeners
        const closeMenu = () => {
            if (menu.parentNode) {
                menu.remove();
            }
            document.removeEventListener('click', clickHandler);
            document.removeEventListener('scroll', scrollHandler, true);
            window.removeEventListener('resize', resizeHandler);
        };

        clickHandler = (e) => {
            if (!menu.contains(e.target) && e.target !== btn) {
                closeMenu();
            }
        };

        // Close on scroll (use capture to catch scroll on any element)
        scrollHandler = () => closeMenu();

        // Close on resize
        resizeHandler = () => closeMenu();

        // Add click handlers for menu items
        menu.addEventListener('click', (e) => {
            const item = e.target.closest('.quick-chart-menu-item');
            if (!item) return;

            const action = item.dataset.action;
            const tickerVal = item.dataset.ticker;

            if (action === 'new') {
                this.createNewChart(tickerVal);
            } else if (action === 'add') {
                const cardId = item.dataset.cardId;
                this.addToExistingChart(tickerVal, cardId);
            }

            closeMenu();
        });

        // Register close handlers after a tick (to avoid immediate close from the button click)
        setTimeout(() => {
            document.addEventListener('click', clickHandler);
            document.addEventListener('scroll', scrollHandler, true);
            window.addEventListener('resize', resizeHandler);
        }, 0);

        document.body.appendChild(menu);
    },

    /**
     * Get list of chart cards on a given page
     * @param {string} pageNum - Page number
     * @returns {Array} Array of {id, title, tickers}
     */
    getChartsOnPage(pageNum) {
        const pageEl = document.querySelector(`.page[data-page="${pageNum}"]`);
        if (!pageEl) return [];

        const charts = [];
        pageEl.querySelectorAll('.chart-card').forEach(card => {
            // Skip dashboard cards
            if (card._type === 'dashboard' || card._type === 'macro-dashboard') return;

            const ctx = card._ctx;
            charts.push({
                id: card.id,
                title: ctx?.title || card._title || '',
                tickers: ctx ? Array.from(ctx.selectedTickers || []) : Array.from(card._selectedTickers || [])
            });
        });

        return charts;
    },

    /**
     * Create a new chart with the given ticker
     * @param {string} ticker - Ticker symbol
     */
    createNewChart(ticker) {
        const activePage = window.PageManager?.getActivePage?.() || '1';

        // Get or create the page wrapper element
        const wrapper = window.PageManager?.ensurePage?.(activePage);
        if (!wrapper) {
            console.error('[ChartDashboard] Could not get page wrapper for page:', activePage);
            return;
        }

        // Switch to the page first (ensures it's visible for proper sizing)
        if (window.PageManager?.showPage) {
            window.PageManager.showPage(activePage);
        }

        // Create the chart card with explicit wrapper
        if (window.createChartCard) {
            window.createChartCard({ tickers: [ticker], wrapperEl: wrapper });

            // Save cards after creation
            if (window.saveCards) {
                window.saveCards();
            }

            // Show toast notification
            if (window.Toast?.success) {
                window.Toast.success(`Created new chart with ${ticker}`);
            }
        }
    },

    /**
     * Add ticker to an existing chart
     * @param {string} ticker - Ticker symbol
     * @param {string} cardId - Card element ID
     */
    addToExistingChart(ticker, cardId) {
        const card = document.getElementById(cardId);
        if (!card) {
            console.error('[ChartDashboard] Card not found:', cardId);
            return;
        }

        const ctx = card._ctx;
        if (!ctx) {
            console.error('[ChartDashboard] Card has no context:', cardId);
            return;
        }

        // Check if ticker already exists
        if (ctx.selectedTickers.has(ticker)) {
            if (window.Toast?.info) {
                window.Toast.info(`${ticker} is already in this chart`);
            }
            return;
        }

        // Check max tickers limit
        const maxTickers = window.ChartConfig?.UI?.MAX_TICKERS_PER_CHART || 30;
        if (ctx.selectedTickers.size >= maxTickers) {
            if (window.Toast?.warning) {
                window.Toast.warning(`Chart already has ${maxTickers} tickers (maximum)`);
            }
            return;
        }

        // Switch to the page containing the chart FIRST (ensures visible for proper width)
        const pageEl = card.closest('.page');
        if (pageEl && window.PageManager?.showPage) {
            window.PageManager.showPage(pageEl.dataset.page);
        }

        // Add the ticker
        ctx.selectedTickers.add(ticker);

        // Assign color
        if (!ctx.tickerColorMap.has(ticker)) {
            ctx.tickerColorMap.set(ticker, window.ChartConfig.getTickerColor(ticker));
        }

        // Re-render chips with proper handlers
        const selectedTickersDiv = ctx.elements?.selectedTickersDiv;
        if (selectedTickersDiv && window.ChartDomBuilder?.addTickerChips) {
            // Get handlers from ChartCardTickers if available
            const plotFn = () => window.ChartCardPlot?.plot?.(ctx);
            let handleChipRemove = null;
            let getAxis = null;
            let onAxisChange = null;

            if (window.ChartCardTickers?.createHandlers) {
                const handlers = window.ChartCardTickers.createHandlers(ctx, { plot: plotFn });
                handleChipRemove = handlers.handleChipRemove;
                getAxis = handlers.getAxis;
                onAxisChange = handlers.onAxisChange;
            }

            window.ChartDomBuilder.addTickerChips(
                selectedTickersDiv,
                ctx.selectedTickers,
                ctx.tickerColorMap,
                ctx.multiplierMap,
                ctx.hiddenTickers,
                handleChipRemove,
                getAxis,
                onAxisChange
            );

            // Re-bind chip interactions for click/multiplier handling
            if (window.CardEventBinder?.bindTickerInteractions) {
                window.CardEventBinder.bindTickerInteractions(
                    selectedTickersDiv,
                    ctx.hiddenTickers,
                    ctx.multiplierMap,
                    () => window.ChartCardContext?.syncToCard?.(ctx),
                    plotFn,
                    () => window.saveCards?.(),
                    () => ctx.useRaw
                );
            }
        }

        // Sync and save
        if (window.ChartCardContext?.syncToCard) {
            window.ChartCardContext.syncToCard(ctx);
        }
        if (window.saveCards) {
            window.saveCards();
        }

        // Trigger replot (direct call, not debounced)
        if (window.ChartCardPlot?.plot) {
            window.ChartCardPlot.plot(ctx);
        }

        // Show toast
        if (window.Toast?.success) {
            window.Toast.success(`Added ${ticker} to chart`);
        }
    },

    // ==================== Multi-Select Methods ====================

    /**
     * Update action bar visibility and count
     */
    _updateActionBar() {
        const card = this._dashboardCard;
        if (!card) return;

        const actionBar = card.querySelector('.dashboard-action-bar');
        if (!actionBar) return;

        const count = this.selectedTickers.size;
        const countEl = actionBar.querySelector('.action-bar-count');
        countEl.textContent = `${count} selected`;

        actionBar.style.display = count > 0 ? 'flex' : 'none';
    },

    /**
     * Update select-all checkbox state based on current selection
     */
    _updateSelectAllCheckbox(tbody) {
        const card = tbody.closest('.dashboard-card');
        if (!card) return;

        const selectAllCheckbox = card.querySelector('.select-all-checkbox');
        if (!selectAllCheckbox) return;

        // Get all visible row checkboxes
        const rowCheckboxes = tbody.querySelectorAll('.row-select-checkbox');
        const total = rowCheckboxes.length;
        const checked = Array.from(rowCheckboxes).filter(cb => cb.checked).length;

        if (checked === 0) {
            selectAllCheckbox.checked = false;
            selectAllCheckbox.indeterminate = false;
        } else if (checked === total) {
            selectAllCheckbox.checked = true;
            selectAllCheckbox.indeterminate = false;
        } else {
            selectAllCheckbox.checked = false;
            selectAllCheckbox.indeterminate = true;
        }
    },

    /**
     * Handle select-all checkbox toggle
     * @param {boolean} checked - New checked state
     * @param {Array} visibleData - Currently visible/filtered data
     */
    _handleSelectAll(checked, visibleData) {
        const card = this._dashboardCard;
        if (!card) return;

        if (checked) {
            // Add all visible tickers to selection
            visibleData.forEach(row => this.selectedTickers.add(row.ticker));
        } else {
            // Remove all visible tickers from selection
            visibleData.forEach(row => this.selectedTickers.delete(row.ticker));
        }

        // Update all visible checkboxes
        const tbody = card.querySelector('.dashboard-table tbody');
        tbody.querySelectorAll('.row-select-checkbox').forEach(cb => {
            cb.checked = checked;
        });
    },

    /**
     * Clear all selections
     * @param {HTMLElement} card - Dashboard card element
     */
    clearSelection(card) {
        this.selectedTickers.clear();

        // Update UI
        const tbody = card.querySelector('.dashboard-table tbody');
        tbody.querySelectorAll('.row-select-checkbox').forEach(cb => {
            cb.checked = false;
        });

        const selectAllCheckbox = card.querySelector('.select-all-checkbox');
        if (selectAllCheckbox) {
            selectAllCheckbox.checked = false;
            selectAllCheckbox.indeterminate = false;
        }

        this._updateActionBar();
    },

    /**
     * Create new chart with all selected tickers
     */
    compareTickers() {
        const tickers = Array.from(this.selectedTickers);
        if (tickers.length === 0) {
            if (window.Toast?.warning) {
                window.Toast.warning('No tickers selected');
            }
            return;
        }

        // Check max tickers limit
        const maxTickers = window.ChartConfig?.UI?.MAX_TICKERS_PER_CHART || 30;
        if (tickers.length > maxTickers) {
            if (window.Toast?.warning) {
                window.Toast.warning(`Can only compare up to ${maxTickers} tickers at once`);
            }
            return;
        }

        const activePage = window.PageManager?.getActivePage?.() || '1';
        const wrapper = window.PageManager?.ensurePage?.(activePage);
        if (!wrapper) {
            console.error('[ChartDashboard] Could not get page wrapper for page:', activePage);
            return;
        }

        if (window.PageManager?.showPage) {
            window.PageManager.showPage(activePage);
        }

        if (window.createChartCard) {
            window.createChartCard({ tickers, wrapperEl: wrapper });

            if (window.saveCards) {
                window.saveCards();
            }

            if (window.Toast?.success) {
                window.Toast.success(`Created chart with ${tickers.length} tickers`);
            }

            // Clear selection after creating chart
            this.clearSelection(this._dashboardCard);
        }
    },

    /**
     * Show "Add to Chart" dropdown menu
     * @param {HTMLElement} menu - Menu element to populate
     * @param {HTMLElement} btn - Button element for positioning
     */
    _showAddToChartMenu(menu, btn) {
        // Toggle menu visibility
        if (menu.classList.contains('show')) {
            menu.classList.remove('show');
            return;
        }

        const activePage = window.PageManager?.getActivePage?.() || '1';
        const existingCharts = this.getChartsOnPage(activePage);

        // Clear and rebuild menu
        menu.innerHTML = '';

        if (existingCharts.length === 0) {
            const emptyItem = document.createElement('div');
            emptyItem.className = 'action-bar-menu-item disabled';
            emptyItem.textContent = 'No charts on this page';
            menu.appendChild(emptyItem);
        } else {
            existingCharts.forEach((chart, idx) => {
                const label = chart.title || chart.tickers?.slice(0, 3).join(', ') || `Chart ${idx + 1}`;
                const truncatedLabel = label.length > 30 ? label.slice(0, 27) + '...' : label;

                const item = document.createElement('div');
                item.className = 'action-bar-menu-item';
                item.dataset.cardId = chart.id;
                item.textContent = truncatedLabel;
                item.addEventListener('click', () => {
                    this.addTickersToChart(chart.id);
                    menu.classList.remove('show');
                });
                menu.appendChild(item);
            });
        }

        menu.classList.add('show');

        // Close on click outside
        const closeHandler = (e) => {
            if (!menu.contains(e.target) && e.target !== btn) {
                menu.classList.remove('show');
                document.removeEventListener('click', closeHandler);
            }
        };
        setTimeout(() => document.addEventListener('click', closeHandler), 0);
    },

    /**
     * Add all selected tickers to an existing chart
     * @param {string} cardId - Card element ID
     */
    addTickersToChart(cardId) {
        const card = document.getElementById(cardId);
        if (!card) {
            console.error('[ChartDashboard] Card not found:', cardId);
            return;
        }

        const ctx = card._ctx;
        if (!ctx) {
            console.error('[ChartDashboard] Card has no context:', cardId);
            return;
        }

        const tickers = Array.from(this.selectedTickers);
        if (tickers.length === 0) {
            if (window.Toast?.warning) {
                window.Toast.warning('No tickers selected');
            }
            return;
        }

        // Check max tickers limit
        const maxTickers = window.ChartConfig?.UI?.MAX_TICKERS_PER_CHART || 30;
        const currentCount = ctx.selectedTickers.size;
        const available = maxTickers - currentCount;

        if (available <= 0) {
            if (window.Toast?.warning) {
                window.Toast.warning(`Chart already has ${maxTickers} tickers (maximum)`);
            }
            return;
        }

        // Filter out already-existing and limit to available slots
        const newTickers = tickers.filter(t => !ctx.selectedTickers.has(t)).slice(0, available);

        if (newTickers.length === 0) {
            if (window.Toast?.info) {
                window.Toast.info('All selected tickers are already in this chart');
            }
            return;
        }

        // Switch to the page containing the chart
        const pageEl = card.closest('.page');
        if (pageEl && window.PageManager?.showPage) {
            window.PageManager.showPage(pageEl.dataset.page);
        }

        // Add each ticker
        newTickers.forEach(ticker => {
            ctx.selectedTickers.add(ticker);
            if (!ctx.tickerColorMap.has(ticker)) {
                ctx.tickerColorMap.set(ticker, window.ChartConfig.getTickerColor(ticker));
            }
        });

        // Re-render chips
        const selectedTickersDiv = ctx.elements?.selectedTickersDiv;
        if (selectedTickersDiv && window.ChartDomBuilder?.addTickerChips) {
            const plotFn = () => window.ChartCardPlot?.plot?.(ctx);
            let handleChipRemove = null;
            let getAxis = null;
            let onAxisChange = null;

            if (window.ChartCardTickers?.createHandlers) {
                const handlers = window.ChartCardTickers.createHandlers(ctx, { plot: plotFn });
                handleChipRemove = handlers.handleChipRemove;
                getAxis = handlers.getAxis;
                onAxisChange = handlers.onAxisChange;
            }

            window.ChartDomBuilder.addTickerChips(
                selectedTickersDiv,
                ctx.selectedTickers,
                ctx.tickerColorMap,
                ctx.multiplierMap,
                ctx.hiddenTickers,
                handleChipRemove,
                getAxis,
                onAxisChange
            );

            if (window.CardEventBinder?.bindTickerInteractions) {
                window.CardEventBinder.bindTickerInteractions(
                    selectedTickersDiv,
                    ctx.hiddenTickers,
                    ctx.multiplierMap,
                    () => window.ChartCardContext?.syncToCard?.(ctx),
                    plotFn,
                    () => window.saveCards?.(),
                    () => ctx.useRaw
                );
            }
        }

        // Sync and save
        if (window.ChartCardContext?.syncToCard) {
            window.ChartCardContext.syncToCard(ctx);
        }
        if (window.saveCards) {
            window.saveCards();
        }

        // Replot
        if (window.ChartCardPlot?.plot) {
            window.ChartCardPlot.plot(ctx);
        }

        // Show toast with count
        const skipped = tickers.length - newTickers.length;
        let message = `Added ${newTickers.length} ticker${newTickers.length !== 1 ? 's' : ''} to chart`;
        if (skipped > 0) {
            message += ` (${skipped} already present)`;
        }
        if (window.Toast?.success) {
            window.Toast.success(message);
        }

        // Clear selection after adding
        this.clearSelection(this._dashboardCard);
    },

    /**
     * Get selected rows in current filtered+sorted order
     * @returns {Array} Array of row data objects in table display order
     */
    _getSelectedRowsData() {
        if (this.selectedTickers.size === 0) return [];

        // Apply same filter+sort logic as renderTable to get correct order
        const numericColumns = [
            'latest_price', 'daily_change', 'weekly_change', 'monthly_change',
            'yearly_change', 'high_52w', 'low_52w', 'data_points', 'pages'
        ];

        const filteredSortedData = window.DashboardBase.filterAndSortData({
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

        // Return only selected rows, preserving filtered+sorted order
        return filteredSortedData.filter(row => this.selectedTickers.has(row.ticker));
    },

    /**
     * Escape a cell value for CSV/TSV export
     * - Applies formula injection protection (prefix ' for cells starting with = + - @)
     * - Escapes quotes and handles special characters
     * @param {*} value - Cell value
     * @param {string} delimiter - '\t' for TSV or ',' for CSV
     * @returns {string} Escaped cell value
     */
    _escapeCsvField(value, delimiter) {
        if (value === null || value === undefined) return '';

        let strVal = String(value);

        // Formula injection protection: prefix with ' if starts with dangerous char
        if (strVal.length > 0 && '=+-@'.includes(strVal[0])) {
            strVal = "'" + strVal;
        }

        if (delimiter === ',') {
            // CSV: quote if contains comma, quote, or newline
            if (strVal.includes(',') || strVal.includes('"') || strVal.includes('\n') || strVal.includes('\r')) {
                return '"' + strVal.replace(/"/g, '""') + '"';
            }
            return strVal;
        } else {
            // TSV: replace tabs/newlines with spaces
            return strVal.replace(/[\t\n\r]/g, ' ');
        }
    },

    /**
     * Format rows for export
     * @param {Array} data - Row data array
     * @param {string} delimiter - '\t' for TSV or ',' for CSV
     * @returns {Object} { header: string, rows: string[] }
     */
    _formatRowsForExport(data, delimiter) {
        // Column definitions (excluding select and actions)
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

        // Use visible columns in order (exclude select/actions)
        const columnOrder = this.columnOrder || defaultColumns.map(c => c.key);
        const visibleColumns = columnOrder
            .filter(key => key !== 'select' && key !== 'actions')
            .filter(key => !this.hiddenColumns || !this.hiddenColumns.has(key))
            .map(key => defaultColumns.find(c => c.key === key))
            .filter(Boolean);

        // Build header
        const header = visibleColumns.map(c => this._escapeCsvField(c.label, delimiter)).join(delimiter);

        // Build rows
        const rows = data.map(row => {
            return visibleColumns.map(col => {
                let value = row[col.key];

                // Pages: use page names for readability
                if (col.key === 'pages') {
                    if (row.pages && Array.isArray(row.pages) && row.pages.length > 0) {
                        value = row.pages.map(p => p.page_name).join(', ');
                    } else {
                        value = '';
                    }
                }

                // Format numbers
                if (typeof value === 'number') {
                    value = value.toFixed ? value.toFixed(2) : String(value);
                }

                return this._escapeCsvField(value, delimiter);
            }).join(delimiter);
        });

        return { header, rows };
    },

    /**
     * Copy selected rows to clipboard as TSV
     */
    copySelected() {
        const selectedData = this._getSelectedRowsData();
        if (selectedData.length === 0) {
            if (window.Toast?.info) {
                window.Toast.info('No rows selected');
            }
            return;
        }

        const { header, rows } = this._formatRowsForExport(selectedData, '\t');
        const tsv = [header, ...rows].join('\n');

        this._writeToClipboard(tsv, selectedData.length);
    },

    /**
     * Export selected rows as CSV download
     */
    exportSelected() {
        const selectedData = this._getSelectedRowsData();
        if (selectedData.length === 0) {
            if (window.Toast?.info) {
                window.Toast.info('No rows selected');
            }
            return;
        }

        const { header, rows } = this._formatRowsForExport(selectedData, ',');
        const csv = [header, ...rows].join('\n');

        // Download
        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `selected_${selectedData.length}_rows_${new Date().toISOString().slice(0, 10)}.csv`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);

        if (window.Toast?.success) {
            window.Toast.success(`Exported ${selectedData.length} rows`);
        }
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
            columnWidths: this.columnWidths || {},
            conditionalFormatting: this.conditionalFormatting
        };
    }
};

console.log('[ChartDashboard] Module loaded');
