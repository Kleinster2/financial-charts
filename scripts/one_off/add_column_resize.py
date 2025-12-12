#!/usr/bin/env python3
"""
Add column resizing to dashboard table.
"""

import re

print("Adding column resize functionality to dashboard...")

with open('charting_sandbox/chart-dashboard.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update header rendering to include resize handles
old_header_render = '''thead.innerHTML = `<tr>${columns.map(col => {
            const sortClass = this.sortColumn === col.key
                ? (this.sortDirection === 'asc' ? 'sorted-asc' : 'sorted-desc')
                : '';
            return `<th class="${sortClass}" data-column="${col.key}">${col.label}</th>`;
        }).join('')}</tr>`;'''

new_header_render = '''// Get saved column widths
        const savedWidths = this.columnWidths || {};

        thead.innerHTML = `<tr>${columns.map(col => {
            const sortClass = this.sortColumn === col.key
                ? (this.sortDirection === 'asc' ? 'sorted-asc' : 'sorted-desc')
                : '';
            const widthStyle = savedWidths[col.key] ? `style="width: ${savedWidths[col.key]}px; min-width: ${savedWidths[col.key]}px;"` : '';
            return `<th class="${sortClass}" data-column="${col.key}" ${widthStyle}>${col.label}<span class="resize-handle"></span></th>`;
        }).join('')}</tr>`;'''

if 'resize-handle' not in content or 'savedWidths' not in content:
    content = content.replace(old_header_render, new_header_render)
    print("  Updated header rendering with resize handles")

# 2. Add resize event handlers after sort handlers
old_sort_handlers = '''        // Add sort handlers
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
        });'''

new_sort_handlers = '''        // Add sort handlers
        thead.querySelectorAll('th').forEach(th => {
            th.addEventListener('click', (e) => {
                // Don't sort if clicking on resize handle
                if (e.target.classList.contains('resize-handle')) return;

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

        // Add resize handlers
        this.initColumnResize(card, thead);'''

if 'initColumnResize' not in content:
    content = content.replace(old_sort_handlers, new_sort_handlers)
    print("  Updated sort handlers and added resize initialization")

# 3. Add initColumnResize method after renderTable
# Find the end of renderTable method
render_table_end = '''        // Render body
        if (this.viewMode === 'grouped') {
            this.renderGroupedBody(tbody, filteredData, columns);
        } else {
            this.renderFlatBody(tbody, filteredData, columns);
        }
    },'''

init_column_resize = '''        // Render body
        if (this.viewMode === 'grouped') {
            this.renderGroupedBody(tbody, filteredData, columns);
        } else {
            this.renderFlatBody(tbody, filteredData, columns);
        }
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
                };

                document.addEventListener('mousemove', onMouseMove);
                document.addEventListener('mouseup', onMouseUp);
            });
        });
    },'''

if 'initColumnResize(card, thead)' not in content:
    content = content.replace(render_table_end, init_column_resize)
    print("  Added initColumnResize method")

# 4. Update version number in index.html
with open('charting_sandbox/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'chart-dashboard\.js\?v=(\d+)', html)
if match:
    old_v = int(match.group(1))
    html = html.replace(f'chart-dashboard.js?v={old_v}', f'chart-dashboard.js?v={old_v + 1}')
    with open('charting_sandbox/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Updated chart-dashboard.js version to v{old_v + 1}")

with open('charting_sandbox/chart-dashboard.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone! Column widths are now adjustable.")
print("\nHow to use:")
print("  1. Hover over the right edge of any column header")
print("  2. When cursor changes to resize cursor, drag left/right")
print("  3. Column widths are remembered during the session")
