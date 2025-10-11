/**
 * Chart Fixed Legend Manager
 * Handles fixed legend display with draggable positioning and dual mode behavior
 */

window.ChartFixedLegend = {
    /**
     * Create fixed legend element with draggable functionality
     */
    createFixedLegend(chartBox, options = {}) {
        const {
            initialX = 10,
            initialY = 10,
            minimized = false
        } = options;

        // Create fixed legend container
        const fixedLegend = document.createElement('div');
        fixedLegend.className = 'fixed-legend';

        Object.assign(fixedLegend.style, {
            position: 'absolute',
            left: `${initialX}px`,
            top: `${initialY}px`,
            background: 'rgba(255, 255, 255, 0.92)',
            border: '1px solid #999',
            borderRadius: '6px',
            padding: '8px',
            fontSize: '12px',
            fontFamily: 'monospace',
            boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
            zIndex: '2000',
            minWidth: '120px',
            maxWidth: '300px',
            cursor: 'move',
            userSelect: 'none',
            display: 'none'
        });

        // Create header with controls
        const header = document.createElement('div');
        header.className = 'fixed-legend-header';
        Object.assign(header.style, {
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: '6px',
            paddingBottom: '4px',
            borderBottom: '1px solid #ddd',
            cursor: 'move'
        });

        // Title
        const title = document.createElement('span');
        title.textContent = 'Legend';
        title.style.fontWeight = 'bold';
        title.style.fontSize = '11px';
        title.style.color = '#666';
        header.appendChild(title);

        // Controls container
        const controls = document.createElement('div');
        controls.style.display = 'flex';
        controls.style.gap = '4px';

        // Minimize/maximize button
        const minimizeBtn = document.createElement('button');
        minimizeBtn.className = 'legend-minimize-btn';
        minimizeBtn.textContent = minimized ? '+' : '−';
        Object.assign(minimizeBtn.style, {
            background: 'none',
            border: 'none',
            cursor: 'pointer',
            fontSize: '14px',
            padding: '0 4px',
            color: '#666',
            lineHeight: '1'
        });
        minimizeBtn.title = minimized ? 'Maximize' : 'Minimize';
        minimizeBtn.addEventListener('mouseenter', () => minimizeBtn.style.color = '#000');
        minimizeBtn.addEventListener('mouseleave', () => minimizeBtn.style.color = '#666');
        controls.appendChild(minimizeBtn);

        header.appendChild(controls);
        fixedLegend.appendChild(header);

        // Content area
        const content = document.createElement('div');
        content.className = 'fixed-legend-content';
        content.style.display = minimized ? 'none' : 'block';
        fixedLegend.appendChild(content);

        // Add to chart box
        chartBox.appendChild(fixedLegend);

        // Make draggable
        this.makeDraggable(fixedLegend, header, chartBox);

        // Handle minimize/maximize
        minimizeBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            const isMinimized = content.style.display === 'none';
            content.style.display = isMinimized ? 'block' : 'none';
            minimizeBtn.textContent = isMinimized ? '−' : '+';
            minimizeBtn.title = isMinimized ? 'Minimize' : 'Maximize';

            // Store state
            if (fixedLegend._onStateChange) {
                fixedLegend._onStateChange({ minimized: !isMinimized });
            }
        });

        // Store references
        fixedLegend._header = header;
        fixedLegend._content = content;
        fixedLegend._minimizeBtn = minimizeBtn;

        return fixedLegend;
    },

    /**
     * Make element draggable within container
     */
    makeDraggable(element, handle, container) {
        let isDragging = false;
        let startX, startY, initialLeft, initialTop;

        handle.addEventListener('mousedown', (e) => {
            if (e.target.tagName === 'BUTTON') return; // Don't drag when clicking buttons

            isDragging = true;
            startX = e.clientX;
            startY = e.clientY;

            const rect = element.getBoundingClientRect();
            const containerRect = container.getBoundingClientRect();
            initialLeft = rect.left - containerRect.left;
            initialTop = rect.top - containerRect.top;

            handle.style.cursor = 'grabbing';
            e.preventDefault();
        });

        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;

            const dx = e.clientX - startX;
            const dy = e.clientY - startY;

            let newLeft = initialLeft + dx;
            let newTop = initialTop + dy;

            // Constrain within container bounds
            const containerRect = container.getBoundingClientRect();
            const elementRect = element.getBoundingClientRect();

            newLeft = Math.max(0, Math.min(newLeft, containerRect.width - elementRect.width));
            newTop = Math.max(0, Math.min(newTop, containerRect.height - elementRect.height));

            element.style.left = `${newLeft}px`;
            element.style.top = `${newTop}px`;
        });

        document.addEventListener('mouseup', () => {
            if (isDragging) {
                isDragging = false;
                handle.style.cursor = 'move';

                // Store position
                if (element._onStateChange) {
                    element._onStateChange({
                        x: parseInt(element.style.left, 10),
                        y: parseInt(element.style.top, 10)
                    });
                }
            }
        });
    },

    /**
     * Update fixed legend content with latest values
     */
    updateContent(fixedLegend, data, options = {}) {
        const {
            useRaw = false,
            hiddenTickers = new Set(),
            tickerColorMap = new Map(),
            getName = (t) => t
        } = options;

        const content = fixedLegend._content;
        if (!content) return;

        const formatter = useRaw ? this.formatPrice : this.formatPct;

        // Build HTML
        let html = '';
        const rows = [];

        data.forEach(({ ticker, value, color }) => {
            if (hiddenTickers.has(ticker)) return;
            if (value == null || isNaN(value)) return;

            const displayColor = color || tickerColorMap.get(ticker) || '#000';
            const label = getName(ticker) || ticker;

            rows.push({ ticker, label, value, color: displayColor });
        });

        // Sort by value descending (matches visual order)
        rows.sort((a, b) => b.value - a.value);

        html = rows.map(({ label, value, color }) => {
            return `<div style="margin: 2px 0; white-space: nowrap;">
                <span style="color: ${color}; font-weight: bold;">${label}</span>:
                <span>${formatter(value)}</span>
            </div>`;
        }).join('');

        content.innerHTML = html || '<div style="color: #999; font-style: italic;">No data</div>';
    },

    /**
     * Format percentage value for display
     */
    formatPct(val) {
        const diff = val - 100;
        const sign = diff > 0 ? '+' : diff < 0 ? '−' : '';
        const dec = Math.abs(diff) >= 100 ? 0 : 1;
        return `${sign}${Math.abs(diff).toFixed(dec)}%`;
    },

    /**
     * Format price value for display
     */
    formatPrice(v) {
        if (v >= 1000) return v.toFixed(0);
        if (v >= 100) return v.toFixed(1);
        return v.toFixed(2);
    },

    /**
     * Show fixed legend
     */
    show(fixedLegend) {
        if (fixedLegend) {
            fixedLegend.style.display = 'block';
        }
    },

    /**
     * Hide fixed legend
     */
    hide(fixedLegend) {
        if (fixedLegend) {
            fixedLegend.style.display = 'none';
        }
    },

    /**
     * Set position
     */
    setPosition(fixedLegend, x, y) {
        if (fixedLegend) {
            fixedLegend.style.left = `${x}px`;
            fixedLegend.style.top = `${y}px`;
        }
    }
};
