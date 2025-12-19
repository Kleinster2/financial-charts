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
    // Pagination state
    pageSize: 100,
    totalCount: 0,
    isLoading: false,
    hasMore: false,
    // Keyboard navigation state
    focusedRowIndex: -1,

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
                        <option value="grouped-chart">Grouped by Page & Chart</option>
                    </select>
                    <div class="dashboard-columns-dropdown">
                        <button class="dashboard-columns-btn">Columns ▼</button>
                        <div class="dashboard-columns-menu"></div>
                    </div>
                    <button class="dashboard-refresh-btn">Refresh</button>
                    <span class="dashboard-refresh-indicator" style="display:none;">Updating...</span>
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
            <div class="dashboard-load-more-container" style="display:none; text-align:center; padding:12px;">
                <button class="dashboard-load-more-btn">Load More</button>
                <span class="dashboard-load-status"></span>
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
            { key: 'actions', label: '' },
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

        // Initialize column order if not set (exclude actions - always first)
        if (!this.columnOrder) {
            this.columnOrder = defaultColumns.filter(c => c.key !== 'actions').map(c => c.key);
        }

        // Build columns array: actions first (fixed), then user-ordered columns
        const columnMap = {};
        defaultColumns.forEach(c => columnMap[c.key] = c);
        const actionsCol = columnMap['actions'];
        const orderedCols = this.columnOrder
            .filter(key => key !== 'actions')  // Ensure actions not duplicated
            .map(key => columnMap[key])
            .filter(Boolean);
        const columns = actionsCol ? [actionsCol, ...orderedCols] : orderedCols;

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
                this.renderTable(card);
                if (window.saveCards) window.saveCards();
            }
        });

        // ChartDashboard-specific overrides: column resize + drag
        this.initColumnResize(card, thead);
        this.initColumnDrag(card, thead);

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
        // Default column definitions for building the menu (exclude actions - always visible)
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
            ? row.pages.map(p => `<a class="page-link" data-page="${p.page}">${window.DashboardBase.escapeHtml(p.page_name)}</a>`).join(', ')
            : '-';

        // Cell renderers for each column
        const cellRenderers = {
            actions: () => `<td class="actions-cell"><button class="quick-chart-btn" data-ticker="${row.ticker}" title="Add to chart">+</button></td>`,
            ticker: () => `<td class="ticker-cell">${window.DashboardBase.escapeHtml(row.ticker)}</td>`,
            name: () => `<td>${window.DashboardBase.escapeHtml(row.name) || '-'}</td>`,
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
