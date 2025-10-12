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
            initialY = 10
        } = options;

        // Create fixed legend container
        const fixedLegend = document.createElement('div');
        fixedLegend.className = 'fixed-legend';

        Object.assign(fixedLegend.style, {
            position: 'absolute',
            left: `${initialX}px`,
            top: `${initialY}px`,
            background: 'rgba(255, 255, 255, 0.85)',
            border: '1px solid #ccc',
            borderRadius: '4px',
            padding: '2px 4px',
            fontSize: '12px',
            boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
            zIndex: '2000',
            cursor: 'move',
            userSelect: 'none',
            display: 'none',
            whiteSpace: 'nowrap'
        });

        // Add to chart box
        chartBox.appendChild(fixedLegend);

        // Make draggable
        this.makeDraggable(fixedLegend, fixedLegend, chartBox);

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

        if (!fixedLegend) return;

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
            return `<div><span style="color: ${color}; font-weight: bold;">${label}</span>: ${formatter(value)}</div>`;
        }).join('');

        fixedLegend.innerHTML = html || '<div style="color: #999; font-style: italic;">No data</div>';
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
