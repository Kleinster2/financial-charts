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
                background: #1e222d;
                border: 1px solid #2a2e39;
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
                color: #d1d4dc;
            }
            .dashboard-controls {
                display: flex;
                gap: 8px;
                align-items: center;
                flex-wrap: wrap;
            }
            .dashboard-filter {
                padding: 6px 10px;
                border: 1px solid #444;
                border-radius: 4px;
                width: 200px;
                background: #2a2e39;
                color: #d1d4dc;
            }
            .dashboard-view-select {
                padding: 6px 10px;
                border: 1px solid #444;
                border-radius: 4px;
                background: #2a2e39;
                color: #d1d4dc;
            }
            .dashboard-refresh-btn {
                padding: 6px 12px;
                background: #2962ff;
                color: #d1d4dc;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .dashboard-refresh-btn:hover {
                background: #1e50d2;
            }
            .dashboard-reset-btn,
            .dashboard-export-btn,
            .dashboard-copy-btn,
            .dashboard-conditional-btn,
            .dashboard-export-all-btn,
            .dashboard-copy-all-btn {
                padding: 6px 12px;
                background: #3a3e4a;
                color: #d1d4dc;
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
                background: #2e323c;
            }
            /* Highlight Export All / Copy All buttons when visible */
            .dashboard-export-all-btn,
            .dashboard-copy-all-btn {
                background: #0d8da0;
            }
            .dashboard-export-all-btn:hover,
            .dashboard-copy-all-btn:hover {
                background: #0a7585;
            }
            .dashboard-copy-all-btn:disabled {
                background: #3a3e4a;
                cursor: wait;
                opacity: 0.7;
            }
            .dashboard-conditional-btn.active {
                background: #26a69a;
            }
            .dashboard-conditional-btn.active:hover {
                background: #1e8e83;
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
                color: #787b86;
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
                background: #3a3e4a;
                color: #d1d4dc;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .dashboard-columns-btn:hover {
                background: #2e323c;
            }
            .dashboard-columns-menu {
                display: none;
                position: absolute;
                top: 100%;
                left: 0;
                background: #1e222d;
                border: 1px solid #2a2e39;
                border-radius: 4px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.4);
                z-index: 1000;
                min-width: 180px;
                max-height: 300px;
                overflow-y: auto;
                color: #d1d4dc;
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
                background: #363a45;
            }
            .dashboard-columns-menu input[type="checkbox"] {
                margin-right: 8px;
            }
            .dashboard-stats {
                display: flex;
                gap: 24px;
                margin-bottom: 16px;
                padding: 12px;
                background: #1a1e2b;
                border-radius: 4px;
                flex-wrap: wrap;
            }
            .dashboard-stat {
                display: flex;
                flex-direction: column;
            }
            .dashboard-stat-label {
                font-size: 0.8rem;
                color: #787b86;
            }
            .dashboard-stat-value {
                font-size: 1.2rem;
                font-weight: bold;
                color: #d1d4dc;
            }
            .dashboard-table-container {
                max-height: 70vh;
                overflow: auto;
                border: 1px solid #2a2e39;
                border-radius: 4px;
            }
            .dashboard-table {
                width: 100%;
                min-width: 1200px;
                border-collapse: collapse;
                font-size: 0.85rem;
                table-layout: fixed;
                color: #d1d4dc;
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
                background: #2a2e39;
                padding: 10px 8px;
                text-align: left;
                border-bottom: 2px solid #2a2e39;
                cursor: pointer;
                user-select: none;
                position: relative;
                color: #d1d4dc;
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
                background: #2962ff;
            }
            .dashboard-table.resizing {
                cursor: col-resize;
                user-select: none;
            }
            .dashboard-table th.dragging {
                opacity: 0.5;
                background: #2962ff;
                color: #d1d4dc;
            }
            .dashboard-table th.drag-over {
                border-left: 3px solid #2962ff;
            }
            .dashboard-table th[draggable="true"] {
                cursor: grab;
            }
            .dashboard-table th[draggable="true"]:active {
                cursor: grabbing;
            }
            .dashboard-table th:hover {
                background: #363a45;
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
                border-bottom: 1px solid #2a2e39;
            }
            .dashboard-table tr:hover {
                background: #1a1e2b;
            }
            .dashboard-table .ticker-cell {
                font-weight: bold;
                color: #2962ff;
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
                background: #1a1e2b;
            }
            .dashboard-card .dashboard-table th:nth-child(2),
            .dashboard-card .dashboard-table td:nth-child(2) {
                position: sticky;
                left: 32px;
                z-index: 1;
                background: #1a1e2b;
            }
            .dashboard-card .dashboard-table th:first-child,
            .dashboard-card .dashboard-table th:nth-child(2) {
                z-index: 3;
                background: #2a2e39;
            }
            .dashboard-card .dashboard-table td:first-child,
            .dashboard-card .dashboard-table td:nth-child(2) {
                background: #1e222d;
            }
            .dashboard-card .dashboard-table tr:hover td:first-child,
            .dashboard-card .dashboard-table tr:hover td:nth-child(2) {
                background: #1a1e2b;
            }
            .dashboard-card .dashboard-row-focused td:first-child,
            .dashboard-card .dashboard-row-focused td:nth-child(2) {
                background: rgba(41,98,255,0.15) !important;
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
                background: linear-gradient(to right, rgba(0,0,0,0.25), transparent);
                pointer-events: none;
            }
            .dashboard-table .price-cell {
                text-align: right;
                font-family: monospace;
            }
            .dashboard-table .change-positive {
                color: #26a69a;
            }
            .dashboard-table .change-negative {
                color: #ef5350;
            }
            .dashboard-table .page-link {
                color: #2962ff;
                cursor: pointer;
                text-decoration: none;
            }
            .dashboard-table .page-link:hover {
                text-decoration: underline;
            }
            .dashboard-group-header {
                background: #2a2e39 !important;
                font-weight: bold;
            }
            .dashboard-group-header td {
                padding: 12px 8px;
                border-bottom: 2px solid #2a2e39;
            }
            .dashboard-chart-header {
                background: #1a1e2b !important;
                font-weight: 600;
            }
            .dashboard-chart-header td {
                padding: 8px 8px 8px 24px;
                border-bottom: 1px solid #2a2e39;
                font-size: 0.95em;
                color: #787b86;
            }
            .dashboard-loading {
                text-align: center;
                padding: 40px;
                color: #787b86;
            }
            .dashboard-load-more-container {
                border-top: 1px solid #2a2e39;
                background: #1a1e2b;
            }
            .dashboard-load-more-btn {
                padding: 8px 24px;
                background: #2962ff;
                color: #d1d4dc;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 0.9rem;
            }
            .dashboard-load-more-btn:hover {
                background: #1e50d2;
            }
            .dashboard-load-more-btn:disabled {
                background: #3a3e4a;
                cursor: not-allowed;
            }
            .dashboard-load-status {
                margin-left: 12px;
                color: #787b86;
                font-size: 0.85rem;
            }
            /* Keyboard navigation focus styles */
            .dashboard-table-container:focus {
                outline: 2px solid #2962ff;
                outline-offset: -2px;
            }
            .dashboard-row-focused {
                background-color: rgba(41,98,255,0.15) !important;
                outline: 2px solid #2962ff;
                outline-offset: -2px;
            }
            .dashboard-row-focused td {
                background-color: rgba(41,98,255,0.15) !important;
            }
            /* Loading skeleton styles */
            .dashboard-skeleton-row td {
                padding: 8px;
            }
            .dashboard-skeleton {
                background: linear-gradient(90deg, #2a2e39 25%, #363a45 50%, #2a2e39 75%);
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
                background: #26a69a;
                color: #d1d4dc;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                transition: background 0.15s;
            }
            .quick-chart-btn:hover {
                background: #1e8e83;
            }
            .quick-chart-btn:active {
                background: #17756c;
            }
            .quick-chart-menu {
                background: #1e222d;
                border: 1px solid #2a2e39;
                border-radius: 6px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.4);
                min-width: 180px;
                max-width: 280px;
                overflow: hidden;
            }
            .quick-chart-menu-item {
                padding: 10px 14px;
                cursor: pointer;
                font-size: 0.9rem;
                color: #d1d4dc;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }
            .quick-chart-menu-item:hover {
                background: #363a45;
            }
            .quick-chart-menu-item:first-child {
                font-weight: 600;
                color: #26a69a;
            }
            .quick-chart-menu-divider {
                height: 1px;
                background: #2a2e39;
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
                accent-color: #2962ff;
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
                background: #1a1e2b;
                color: #d1d4dc;
                border-radius: 0 0 4px 4px;
                box-shadow: 0 -2px 8px rgba(0,0,0,0.4);
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
                background: #26a69a;
                color: #d1d4dc;
            }
            .action-bar-compare:hover {
                background: #1e8e83;
            }
            .action-bar-copy,
            .action-bar-export {
                background: #0d8da0;
                color: #d1d4dc;
            }
            .action-bar-copy:hover,
            .action-bar-export:hover {
                background: #0a7585;
            }
            .action-bar-clear {
                background: #3a3e4a;
                color: #d1d4dc;
            }
            .action-bar-clear:hover {
                background: #2e323c;
            }
            /* Action bar dropdown */
            .action-bar-add-dropdown {
                position: relative;
            }
            .action-bar-add-btn {
                padding: 6px 14px;
                background: #2962ff;
                color: #d1d4dc;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 0.9rem;
                font-weight: 500;
                transition: background 0.15s;
            }
            .action-bar-add-btn:hover {
                background: #1e50d2;
            }
            .action-bar-add-menu {
                display: none;
                position: absolute;
                bottom: 100%;
                left: 0;
                margin-bottom: 4px;
                background: #1e222d;
                border: 1px solid #2a2e39;
                border-radius: 6px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.4);
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
                color: #d1d4dc;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }
            .action-bar-menu-item:hover {
                background: #363a45;
            }
            .action-bar-menu-item.disabled {
                color: #555;
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
                background: #1a1e2b;
            }
            .dashboard-card .dashboard-table th:nth-child(3) {
                z-index: 3;
                background: #2a2e39;
            }
            .dashboard-card .dashboard-table td:nth-child(3) {
                background: #1e222d;
            }
            .dashboard-card .dashboard-table tr:hover td:nth-child(3) {
                background: #1a1e2b;
            }
            .dashboard-card .dashboard-row-focused td:nth-child(3) {
                background: rgba(41,98,255,0.15) !important;
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
                background: linear-gradient(to right, rgba(0,0,0,0.25), transparent);
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
                text-align: center;
            }
            .sparkline-svg {
                display: block;
                margin: 0 auto;
            }
            .sparkline-loading {
                color: #555;
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
            /* 52w range bar */
            .range-52w-cell {
                padding: 8px 6px !important;
                min-width: 80px;
            }
            .range-52w-bar {
                width: 100%;
                height: 8px;
                background: #2a2e39;
                border-radius: 4px;
                overflow: hidden;
            }
            .range-52w-fill {
                height: 100%;
                border-radius: 4px;
            }
            /* Column filter row */
            .dashboard-filter-row th {
                position: sticky;
                top: 37px;
                background: #1e222d;
                padding: 4px 4px;
                border-bottom: 1px solid #2a2e39;
                z-index: 2;
                cursor: default;
            }
            .filter-cell {
                padding: 2px 4px !important;
            }
            .column-filter-input {
                width: 100%;
                padding: 3px 5px;
                font-size: 0.75rem;
                background: #2a2e39;
                color: #d1d4dc;
                border: 1px solid #363a45;
                border-radius: 3px;
                outline: none;
                box-sizing: border-box;
            }
            .column-filter-input:focus {
                border-color: #2962ff;
                box-shadow: 0 0 0 1px rgba(41,98,255,0.3);
            }
            .column-filter-input::placeholder {
                color: #555;
                font-size: 0.7rem;
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
