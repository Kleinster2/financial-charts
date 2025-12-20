/**
 * Dashboard Base Module
 *
 * Shared utilities for dashboard-style cards (ChartDashboard, ChartMacroDashboard).
 *
 * Exports: window.DashboardBase
 */
window.DashboardBase = (() => {
    const STYLE_ID = 'dashboard-styles';
    const DASHBOARD_CSS = `
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
            .dashboard-reset-btn,
            .dashboard-export-btn,
            .dashboard-copy-btn,
            .dashboard-conditional-btn,
            .dashboard-export-all-btn,
            .dashboard-copy-all-btn {
                padding: 6px 12px;
                background: #6c757d;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .dashboard-reset-btn:hover,
            .dashboard-export-btn:hover,
            .dashboard-copy-btn:hover,
            .dashboard-conditional-btn:hover,
            .dashboard-export-all-btn:hover,
            .dashboard-copy-all-btn:hover {
                background: #5a6268;
            }
            /* Highlight Export All / Copy All buttons when visible */
            .dashboard-export-all-btn,
            .dashboard-copy-all-btn {
                background: #17a2b8;
            }
            .dashboard-export-all-btn:hover,
            .dashboard-copy-all-btn:hover {
                background: #138496;
            }
            .dashboard-copy-all-btn:disabled {
                background: #6c757d;
                cursor: wait;
                opacity: 0.7;
            }
            .dashboard-conditional-btn.active {
                background: #28a745;
            }
            .dashboard-conditional-btn.active:hover {
                background: #218838;
            }
            /* Conditional formatting background colors */
            .cond-bg-positive {
                background-color: rgba(40, 167, 69, 0.15) !important;
            }
            .cond-bg-negative {
                background-color: rgba(220, 53, 69, 0.15) !important;
            }
            .dashboard-refresh-indicator {
                font-size: 12px;
                color: #6c757d;
                font-style: italic;
                animation: dashboard-pulse 1.5s ease-in-out infinite;
            }
            @keyframes dashboard-pulse {
                0%, 100% { opacity: 0.5; }
                50% { opacity: 1; }
            }
            .dashboard-columns-dropdown {
                position: relative;
                display: inline-block;
            }
            .dashboard-columns-btn {
                padding: 6px 12px;
                background: #6c757d;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .dashboard-columns-btn:hover {
                background: #5a6268;
            }
            .dashboard-columns-menu {
                display: none;
                position: absolute;
                top: 100%;
                left: 0;
                background: white;
                border: 1px solid #ddd;
                border-radius: 4px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
                z-index: 1000;
                min-width: 180px;
                max-height: 300px;
                overflow-y: auto;
            }
            .dashboard-columns-menu.show {
                display: block;
            }
            .dashboard-columns-menu label {
                display: flex;
                align-items: center;
                padding: 8px 12px;
                cursor: pointer;
                font-size: 0.9rem;
            }
            .dashboard-columns-menu label:hover {
                background: #f0f0f0;
            }
            .dashboard-columns-menu input[type="checkbox"] {
                margin-right: 8px;
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
                min-width: 1200px;
                border-collapse: collapse;
                font-size: 0.85rem;
                table-layout: fixed;
            }
            .dashboard-table th,
            .dashboard-table td {
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }
            .dashboard-table th {
                position: sticky;
                top: 0;
                background: #f1f3f4;
                padding: 10px 8px;
                text-align: left;
                border-bottom: 2px solid #ddd;
                cursor: pointer;
                user-select: none;
                position: relative;
            }
            .dashboard-table th .resize-handle {
                position: absolute;
                right: 0;
                top: 0;
                bottom: 0;
                width: 5px;
                cursor: col-resize;
                background: transparent;
            }
            .dashboard-table th .resize-handle:hover,
            .dashboard-table th .resize-handle.resizing {
                background: #007bff;
            }
            .dashboard-table.resizing {
                cursor: col-resize;
                user-select: none;
            }
            .dashboard-table th.dragging {
                opacity: 0.5;
                background: #007bff;
                color: white;
            }
            .dashboard-table th.drag-over {
                border-left: 3px solid #007bff;
            }
            .dashboard-table th[draggable="true"] {
                cursor: grab;
            }
            .dashboard-table th[draggable="true"]:active {
                cursor: grabbing;
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
            /* Pinned/frozen first two columns (actions + ticker) - scoped to .dashboard-card only */
            .dashboard-card .dashboard-table th:first-child,
            .dashboard-card .dashboard-table td:first-child {
                position: sticky;
                left: 0;
                z-index: 1;
                background: #f8f9fa;
            }
            .dashboard-card .dashboard-table th:nth-child(2),
            .dashboard-card .dashboard-table td:nth-child(2) {
                position: sticky;
                left: 32px;
                z-index: 1;
                background: #f8f9fa;
            }
            .dashboard-card .dashboard-table th:first-child,
            .dashboard-card .dashboard-table th:nth-child(2) {
                z-index: 3;
                background: #e9ecef;
            }
            .dashboard-card .dashboard-table td:first-child,
            .dashboard-card .dashboard-table td:nth-child(2) {
                background: #fff;
            }
            .dashboard-card .dashboard-table tr:hover td:first-child,
            .dashboard-card .dashboard-table tr:hover td:nth-child(2) {
                background: #f8f9fa;
            }
            .dashboard-card .dashboard-row-focused td:first-child,
            .dashboard-card .dashboard-row-focused td:nth-child(2) {
                background: #e3f2fd !important;
            }
            /* Shadow to indicate frozen column edge */
            .dashboard-card .dashboard-table th:nth-child(2)::after,
            .dashboard-card .dashboard-table td:nth-child(2)::after {
                content: '';
                position: absolute;
                right: 0;
                top: 0;
                bottom: 0;
                width: 4px;
                background: linear-gradient(to right, rgba(0,0,0,0.08), transparent);
                pointer-events: none;
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
            .dashboard-chart-header {
                background: #f4f6f8 !important;
                font-weight: 600;
            }
            .dashboard-chart-header td {
                padding: 8px 8px 8px 24px;
                border-bottom: 1px solid #dee2e6;
                font-size: 0.95em;
                color: #495057;
            }
            .dashboard-loading {
                text-align: center;
                padding: 40px;
                color: #666;
            }
            .dashboard-load-more-container {
                border-top: 1px solid #ddd;
                background: #f8f9fa;
            }
            .dashboard-load-more-btn {
                padding: 8px 24px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 0.9rem;
            }
            .dashboard-load-more-btn:hover {
                background: #0056b3;
            }
            .dashboard-load-more-btn:disabled {
                background: #6c757d;
                cursor: not-allowed;
            }
            .dashboard-load-status {
                margin-left: 12px;
                color: #666;
                font-size: 0.85rem;
            }
            /* Keyboard navigation focus styles */
            .dashboard-table-container:focus {
                outline: 2px solid #007bff;
                outline-offset: -2px;
            }
            .dashboard-row-focused {
                background-color: #e3f2fd !important;
                outline: 2px solid #2196f3;
                outline-offset: -2px;
            }
            .dashboard-row-focused td {
                background-color: #e3f2fd !important;
            }
            /* Loading skeleton styles */
            .dashboard-skeleton-row td {
                padding: 8px;
            }
            .dashboard-skeleton {
                background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
                background-size: 200% 100%;
                animation: skeleton-shimmer 1.5s infinite;
                border-radius: 4px;
                height: 16px;
            }
            .dashboard-skeleton.skeleton-ticker {
                width: 60px;
            }
            .dashboard-skeleton.skeleton-name {
                width: 120px;
            }
            .dashboard-skeleton.skeleton-price {
                width: 70px;
                margin-left: auto;
            }
            .dashboard-skeleton.skeleton-change {
                width: 50px;
                margin-left: auto;
            }
            .dashboard-skeleton.skeleton-short {
                width: 40px;
            }
            @keyframes skeleton-shimmer {
                0% { background-position: 200% 0; }
                100% { background-position: -200% 0; }
            }
            /* Quick Chart button and menu */
            .actions-cell {
                width: 32px;
                min-width: 32px;
                max-width: 32px;
                text-align: center;
                padding: 4px !important;
            }
            .quick-chart-btn {
                width: 24px;
                height: 24px;
                padding: 0;
                font-size: 16px;
                font-weight: bold;
                line-height: 22px;
                background: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                transition: background 0.15s;
            }
            .quick-chart-btn:hover {
                background: #218838;
            }
            .quick-chart-btn:active {
                background: #1e7e34;
            }
            .quick-chart-menu {
                background: white;
                border: 1px solid #ddd;
                border-radius: 6px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                min-width: 180px;
                max-width: 280px;
                overflow: hidden;
            }
            .quick-chart-menu-item {
                padding: 10px 14px;
                cursor: pointer;
                font-size: 0.9rem;
                color: #333;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }
            .quick-chart-menu-item:hover {
                background: #f0f0f0;
            }
            .quick-chart-menu-item:first-child {
                font-weight: 600;
                color: #28a745;
            }
            .quick-chart-menu-divider {
                height: 1px;
                background: #eee;
                margin: 4px 0;
            }
            /* Multi-select checkbox column */
            .select-cell {
                width: 32px;
                min-width: 32px;
                max-width: 32px;
                text-align: center;
                padding: 4px !important;
            }
            .select-header {
                width: 32px;
                min-width: 32px;
                max-width: 32px;
                text-align: center;
                cursor: default !important;
            }
            .row-select-checkbox,
            .select-all-checkbox {
                width: 16px;
                height: 16px;
                cursor: pointer;
                accent-color: #007bff;
            }
            /* Floating action bar */
            .dashboard-action-bar {
                position: sticky;
                bottom: 0;
                left: 0;
                right: 0;
                display: flex;
                align-items: center;
                gap: 12px;
                padding: 12px 16px;
                background: #2c3e50;
                color: white;
                border-radius: 0 0 4px 4px;
                box-shadow: 0 -2px 8px rgba(0,0,0,0.15);
                z-index: 100;
            }
            .action-bar-count {
                font-weight: 600;
                font-size: 0.95rem;
                padding-right: 8px;
                border-right: 1px solid rgba(255,255,255,0.3);
            }
            .action-bar-compare,
            .action-bar-copy,
            .action-bar-export,
            .action-bar-clear {
                padding: 6px 14px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 0.9rem;
                font-weight: 500;
                transition: background 0.15s;
            }
            .action-bar-compare {
                background: #28a745;
                color: white;
            }
            .action-bar-compare:hover {
                background: #218838;
            }
            .action-bar-copy,
            .action-bar-export {
                background: #17a2b8;
                color: white;
            }
            .action-bar-copy:hover,
            .action-bar-export:hover {
                background: #138496;
            }
            .action-bar-clear {
                background: #6c757d;
                color: white;
            }
            .action-bar-clear:hover {
                background: #5a6268;
            }
            /* Action bar dropdown */
            .action-bar-add-dropdown {
                position: relative;
            }
            .action-bar-add-btn {
                padding: 6px 14px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 0.9rem;
                font-weight: 500;
                transition: background 0.15s;
            }
            .action-bar-add-btn:hover {
                background: #0056b3;
            }
            .action-bar-add-menu {
                display: none;
                position: absolute;
                bottom: 100%;
                left: 0;
                margin-bottom: 4px;
                background: white;
                border: 1px solid #ddd;
                border-radius: 6px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                min-width: 200px;
                max-width: 300px;
                max-height: 250px;
                overflow-y: auto;
                z-index: 101;
            }
            .action-bar-add-menu.show {
                display: block;
            }
            .action-bar-menu-item {
                padding: 10px 14px;
                cursor: pointer;
                font-size: 0.9rem;
                color: #333;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }
            .action-bar-menu-item:hover {
                background: #f0f0f0;
            }
            .action-bar-menu-item.disabled {
                color: #999;
                cursor: not-allowed;
            }
            .action-bar-menu-item.disabled:hover {
                background: transparent;
            }
            /* Update pinned columns for select + actions + ticker */
            .dashboard-card .dashboard-table th:nth-child(3),
            .dashboard-card .dashboard-table td:nth-child(3) {
                position: sticky;
                left: 64px;
                z-index: 1;
                background: #f8f9fa;
            }
            .dashboard-card .dashboard-table th:nth-child(3) {
                z-index: 3;
                background: #e9ecef;
            }
            .dashboard-card .dashboard-table td:nth-child(3) {
                background: #fff;
            }
            .dashboard-card .dashboard-table tr:hover td:nth-child(3) {
                background: #f8f9fa;
            }
            .dashboard-card .dashboard-row-focused td:nth-child(3) {
                background: #e3f2fd !important;
            }
            /* Shadow after third column (ticker) */
            .dashboard-card .dashboard-table th:nth-child(3)::after,
            .dashboard-card .dashboard-table td:nth-child(3)::after {
                content: '';
                position: absolute;
                right: 0;
                top: 0;
                bottom: 0;
                width: 4px;
                background: linear-gradient(to right, rgba(0,0,0,0.08), transparent);
                pointer-events: none;
            }
            /* Remove shadow from second column now that third is pinned */
            .dashboard-card .dashboard-table th:nth-child(2)::after,
            .dashboard-card .dashboard-table td:nth-child(2)::after {
                display: none;
            }
            /* Sparkline column styles */
            .sparkline-cell {
                padding: 4px 6px !important;
                width: 70px;
                min-width: 70px;
                text-align: center;
            }
            .sparkline-svg {
                display: block;
                margin: 0 auto;
            }
            .sparkline-loading {
                color: #999;
                font-size: 11px;
            }
            .sparkline-up .sparkline-svg path {
                stroke: #22c55e;
            }
            .sparkline-down .sparkline-svg path {
                stroke: #ef4444;
            }
            .sparkline-cell[title] {
                cursor: help;
            }
    `;

    function ensureStyles() {
        window.ChartUtils.ensureStyleTag(STYLE_ID, DASHBOARD_CSS);
    }

    function escapeHtml(value) {
        const str = String(value ?? '');
        return str
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function renderStatusRow(tbody, { colspan, message }) {
        if (!tbody) return;
        const safeColspan = Number(colspan) > 0 ? Number(colspan) : 1;
        tbody.innerHTML = `<tr><td colspan="${safeColspan}" class="dashboard-loading">${escapeHtml(message)}</td></tr>`;
    }

    /**
     * Render skeleton loading rows
     * @param {HTMLElement} tbody - Table body element
     * @param {number} rowCount - Number of skeleton rows to render
     * @param {number} colCount - Number of columns
     */
    function renderSkeletonRows(tbody, rowCount = 10, colCount = 12) {
        if (!tbody) return;

        const skeletonTypes = [
            'skeleton-ticker',  // Ticker
            'skeleton-name',    // Name
            'skeleton-short',   // Pages
            'skeleton-price',   // Price
            'skeleton-change',  // Daily
            'skeleton-change',  // Weekly
            'skeleton-change',  // Monthly
            'skeleton-change',  // Yearly
            'skeleton-price',   // 52w High
            'skeleton-price',   // 52w Low
            'skeleton-short',   // First Date
            'skeleton-short'    // Last Date
        ];

        let html = '';
        for (let i = 0; i < rowCount; i++) {
            html += '<tr class="dashboard-skeleton-row">';
            for (let j = 0; j < colCount; j++) {
                const type = skeletonTypes[j] || 'skeleton-short';
                html += `<td><div class="dashboard-skeleton ${type}"></div></td>`;
            }
            html += '</tr>';
        }
        tbody.innerHTML = html;
    }

    function setGlobalSearchTicker(ticker) {
        const searchInput = document.getElementById('global-search-input');
        if (!searchInput) return;
        searchInput.value = ticker;
        searchInput.dispatchEvent(new Event('input'));
    }

    function filterAndSortData({
        data,
        filterText = '',
        filterFn = null,
        sortColumn,
        sortDirection = 'asc',
        numericColumns = [],
        getSortValue = null
    } = {}) {
        const rows = Array.isArray(data) ? data : [];
        const normalizedFilterText = String(filterText ?? '').trim().toLowerCase();

        let filteredRows = rows;
        if (normalizedFilterText && typeof filterFn === 'function') {
            filteredRows = rows.filter(row => filterFn(row, normalizedFilterText));
        }

        return [...filteredRows].sort((a, b) => {
            const rawA = typeof getSortValue === 'function' ? getSortValue(a, sortColumn) : a?.[sortColumn];
            const rawB = typeof getSortValue === 'function' ? getSortValue(b, sortColumn) : b?.[sortColumn];

            const aNull = rawA === null || rawA === undefined;
            const bNull = rawB === null || rawB === undefined;
            if (aNull && bNull) return 0;
            if (aNull) return 1;
            if (bNull) return -1;

            const isNumeric = numericColumns.includes(sortColumn);
            let aVal = rawA;
            let bVal = rawB;

            if (isNumeric) {
                aVal = Number(aVal) || 0;
                bVal = Number(bVal) || 0;
            } else if (typeof aVal === 'string') {
                aVal = aVal.toLowerCase();
                bVal = (bVal || '').toString().toLowerCase();
            }

            if (aVal < bVal) return sortDirection === 'asc' ? -1 : 1;
            if (aVal > bVal) return sortDirection === 'asc' ? 1 : -1;
            return 0;
        });
    }

    function renderSortableHeader({
        thead,
        columns,
        sortColumn,
        sortDirection,
        thRenderer,
        onSortChange,
        shouldIgnoreSortClick
    } = {}) {
        if (!thead) return;
        const cols = Array.isArray(columns) ? columns : [];

        thead.innerHTML = `<tr>${cols.map(col => {
            const sortClass = sortColumn === col.key
                ? (sortDirection === 'asc' ? 'sorted-asc' : 'sorted-desc')
                : '';
            if (typeof thRenderer === 'function') return thRenderer(col, sortClass);
            return `<th class="${sortClass}" data-column="${col.key}">${escapeHtml(col.label)}</th>`;
        }).join('')}</tr>`;

        thead.querySelectorAll('th').forEach(th => {
            th.addEventListener('click', (e) => {
                if (typeof shouldIgnoreSortClick === 'function' && shouldIgnoreSortClick(e)) return;

                const col = th.dataset.column;
                if (!col) return;

                const nextDirection = sortColumn === col
                    ? (sortDirection === 'asc' ? 'desc' : 'asc')
                    : 'asc';

                if (typeof onSortChange === 'function') onSortChange(col, nextDirection);
            });
        });
    }

    // Virtual scroll configuration
    const VIRTUAL_SCROLL = {
        ROW_HEIGHT: 33,       // Estimated row height in px (8px padding * 2 + ~17px content)
        BUFFER_ROWS: 10,      // Extra rows above/below viewport
        MIN_ROWS_TO_VIRTUALIZE: 100  // Only virtualize when row count exceeds this
    };

    /**
     * Calculate visible row range for virtual scrolling
     * @param {Object} options - Configuration
     * @param {number} options.scrollTop - Current scroll position
     * @param {number} options.containerHeight - Height of scroll container
     * @param {number} options.totalRows - Total number of rows
     * @param {number} [options.rowHeight] - Row height in px (default: VIRTUAL_SCROLL.ROW_HEIGHT)
     * @param {number} [options.buffer] - Buffer rows above/below (default: VIRTUAL_SCROLL.BUFFER_ROWS)
     * @returns {Object} { startIndex, endIndex, topPadding, bottomPadding, shouldVirtualize }
     */
    function calcVisibleRange({
        scrollTop,
        containerHeight,
        totalRows,
        rowHeight = VIRTUAL_SCROLL.ROW_HEIGHT,
        buffer = VIRTUAL_SCROLL.BUFFER_ROWS
    } = {}) {
        // Don't virtualize small datasets
        if (totalRows < VIRTUAL_SCROLL.MIN_ROWS_TO_VIRTUALIZE) {
            return {
                startIndex: 0,
                endIndex: totalRows,
                topPadding: 0,
                bottomPadding: 0,
                shouldVirtualize: false
            };
        }

        const visibleRows = Math.ceil(containerHeight / rowHeight);
        const firstVisible = Math.floor(scrollTop / rowHeight);

        const startIndex = Math.max(0, firstVisible - buffer);
        const endIndex = Math.min(totalRows, firstVisible + visibleRows + buffer);

        const topPadding = startIndex * rowHeight;
        const bottomPadding = (totalRows - endIndex) * rowHeight;

        return {
            startIndex,
            endIndex,
            topPadding,
            bottomPadding,
            shouldVirtualize: true
        };
    }

    /**
     * Create a debounced scroll handler for virtual scrolling
     * @param {Function} renderFn - Function to call on scroll (receives scrollTop)
     * @param {number} [delay=16] - Debounce delay in ms (~60fps)
     * @returns {Function} Scroll event handler
     */
    function createVirtualScrollHandler(renderFn, delay = 16) {
        let rafId = null;
        let lastScrollTop = -1;

        return function onScroll(e) {
            const scrollTop = e.target.scrollTop;

            // Skip if scroll position hasn't changed meaningfully
            if (Math.abs(scrollTop - lastScrollTop) < 5) return;
            lastScrollTop = scrollTop;

            // Use requestAnimationFrame for smooth updates
            if (rafId) cancelAnimationFrame(rafId);
            rafId = requestAnimationFrame(() => {
                renderFn(scrollTop);
                rafId = null;
            });
        };
    }

    return {
        ensureStyles,
        escapeHtml,
        renderStatusRow,
        renderSkeletonRows,
        setGlobalSearchTicker,
        filterAndSortData,
        renderSortableHeader,
        // Virtual scroll exports
        VIRTUAL_SCROLL,
        calcVisibleRange,
        createVirtualScrollHandler
    };
})();

console.log('[DashboardBase] Module loaded');
