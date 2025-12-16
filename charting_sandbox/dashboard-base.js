/**
 * Dashboard Base Module
 *
 * Shared utilities for dashboard-style cards (ChartDashboard, ChartMacroDashboard).
 *
 * Exports: window.DashboardBase
 */
window.DashboardBase = (() => {
    const STYLE_ID = 'dashboard-styles';

    function ensureStyles() {
        if (document.getElementById(STYLE_ID)) return;

        const style = document.createElement('style');
        style.id = STYLE_ID;
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
                width: 100%;
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

    return {
        ensureStyles,
        escapeHtml,
        renderStatusRow,
        setGlobalSearchTicker,
        filterAndSortData,
        renderSortableHeader
    };
})();

console.log('[DashboardBase] Module loaded');
