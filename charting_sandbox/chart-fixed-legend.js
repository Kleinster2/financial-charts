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
            initialWidth = null,
            initialHeight = null
        } = options;

        // Create fixed legend container
        const fixedLegend = document.createElement('div');
        fixedLegend.className = 'fixed-legend';

        Object.assign(fixedLegend.style, {
            position: 'absolute',
            left: `${initialX}px`,
            top: `${initialY}px`,
            background: 'transparent',
            borderRadius: '4px',
            padding: '2px 4px',
            fontSize: '12px',
            boxShadow: 'none',
            zIndex: '2000',
            cursor: 'move',
            userSelect: 'none',
            display: 'none',
            whiteSpace: 'nowrap',
            resize: 'both',
            overflow: 'auto',
            minWidth: '100px',
            minHeight: '20px',
            width: (initialWidth != null && initialWidth > 0) ? `${initialWidth}px` : 'auto',
            height: (initialHeight != null && initialHeight > 0) ? `${initialHeight}px` : 'auto'
        });

        // Add to chart box
        chartBox.appendChild(fixedLegend);

        // Make draggable
        this.makeDraggable(fixedLegend, fixedLegend, chartBox);

        // Function to adjust font size to prevent scrollbars
        const adjustFontSize = () => {
            const width = fixedLegend.offsetWidth;
            const height = fixedLegend.offsetHeight;

            // Account for padding (2px top + 2px bottom = 4px, 4px left + 4px right = 8px)
            const effectiveWidth = width - 8;
            const effectiveHeight = height - 4;

            // Estimate lines of content
            const estimatedLines = Math.max(1, fixedLegend.children.length || 3);

            // Calculate max font size that fits the height
            const lineHeight = 1.2;
            const maxFontFromHeight = effectiveHeight / (estimatedLines * lineHeight);

            // Start with height-based sizing
            const minSize = 8;
            const maxSize = 24;
            let fontSize = Math.max(minSize, Math.min(maxSize, maxFontFromHeight));

            // Apply initial font size
            fixedLegend.style.fontSize = `${Math.round(fontSize)}px`;

            // Check if content overflows horizontally and reduce font if needed
            let iterations = 0;
            while (fixedLegend.scrollWidth > fixedLegend.clientWidth && fontSize > minSize && iterations < 20) {
                fontSize -= 0.5;
                fixedLegend.style.fontSize = `${Math.round(fontSize)}px`;
                iterations++;
            }

            // Check if content overflows vertically and reduce font if needed
            iterations = 0;
            while (fixedLegend.scrollHeight > fixedLegend.clientHeight && fontSize > minSize && iterations < 20) {
                fontSize -= 0.5;
                fixedLegend.style.fontSize = `${Math.round(fontSize)}px`;
                iterations++;
            }
        };

        // Add ResizeObserver to trigger font size adjustment AND save size
        const resizeObserver = new ResizeObserver(() => {
            // Use requestAnimationFrame to ensure DOM has updated
            requestAnimationFrame(() => {
                adjustFontSize();

                // Save size when manually resized (but ignore if hidden/zero size)
                if (fixedLegend._onStateChange) {
                    const width = fixedLegend.offsetWidth;
                    const height = fixedLegend.offsetHeight;
                    // Only save if element is visible and has actual size
                    if (width > 0 && height > 0 && fixedLegend.style.display !== 'none') {
                        fixedLegend._onStateChange({
                            width,
                            height
                        });
                    }
                }
            });
        });

        resizeObserver.observe(fixedLegend);
        fixedLegend._resizeObserver = resizeObserver;
        fixedLegend._adjustFontSize = adjustFontSize;

        // Attach cleanup method (document listeners added by makeDraggable)
        fixedLegend._cleanup = () => {
            if (fixedLegend._resizeObserver) {
                fixedLegend._resizeObserver.disconnect();
                fixedLegend._resizeObserver = null;
            }
            if (fixedLegend._docMouseMove) {
                document.removeEventListener('mousemove', fixedLegend._docMouseMove);
                fixedLegend._docMouseMove = null;
            }
            if (fixedLegend._docMouseUp) {
                document.removeEventListener('mouseup', fixedLegend._docMouseUp);
                fixedLegend._docMouseUp = null;
            }
        };

        return fixedLegend;
    },

    /**
     * Make element draggable within container
     * Stores document listener refs on element for cleanup
     */
    makeDraggable(element, handle, container) {
        let isDragging = false;
        let startX, startY, initialLeft, initialTop;

        handle.addEventListener('mousedown', (e) => {
            if (e.target.tagName === 'BUTTON') return; // Don't drag when clicking buttons

            // Check if clicking near the resize corner (bottom-right 15px area)
            const rect = element.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const clickY = e.clientY - rect.top;
            const resizeZone = 15; // pixels from bottom-right corner

            if (clickX > rect.width - resizeZone && clickY > rect.height - resizeZone) {
                // In resize zone, don't start dragging
                return;
            }

            isDragging = true;
            startX = e.clientX;
            startY = e.clientY;

            const containerRect = container.getBoundingClientRect();
            initialLeft = rect.left - containerRect.left;
            initialTop = rect.top - containerRect.top;

            handle.style.cursor = 'grabbing';
            e.preventDefault();
        });

        const onMouseMove = (e) => {
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
        };

        const onMouseUp = () => {
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
        };

        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);

        // Store refs for cleanup
        element._docMouseMove = onMouseMove;
        element._docMouseUp = onMouseUp;
    },

    /**
     * Check if name is similar enough to ticker to show only name
     */
    _isSimilarToTicker(ticker, name) {
        if (!name || !ticker) return false;

        const tickerUpper = ticker.toUpperCase();
        const nameUpper = name.toUpperCase();

        // Exact match (case-insensitive)
        if (tickerUpper === nameUpper) return true;

        // Name is just the ticker with common suffixes
        const suffixes = [' INC', ' CORP', ' LTD', ' PLC', ' AG', ' SE', ' NV'];
        for (const suffix of suffixes) {
            if (nameUpper === tickerUpper + suffix) return true;
        }

        // Ticker is an acronym of the name (e.g., "IBM" for "IBM")
        // or name starts with ticker (e.g., "AAPL" for "Apple")
        if (nameUpper.startsWith(tickerUpper)) return true;

        // Check if name contains ticker as whole word
        const words = nameUpper.split(/\s+/);
        if (words.some(w => w === tickerUpper)) return true;

        return false;
    },

    /**
     * Update fixed legend content with latest values
     */
    updateContent(fixedLegend, data, options = {}) {
        const {
            useRaw = false,
            hiddenTickers = new Set(),
            tickerColorMap = new Map(),
            getName = (t) => t,
            showTickers = false
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
            const name = getName(ticker);

            // Smart label logic
            let label;
            if (showTickers) {
                // If name is same or similar to ticker, show only name
                if (this._isSimilarToTicker(ticker, name)) {
                    label = name || ticker;
                } else {
                    // Show both: "Name (TICKER)"
                    label = name && name !== ticker ? `${name} (${ticker})` : ticker;
                }
            } else {
                // Original behavior: just show name (or ticker if no name)
                label = name || ticker;
            }

            rows.push({ ticker, label, value, color: displayColor });
        });

        // Sort by value descending (matches visual order)
        rows.sort((a, b) => b.value - a.value);

        html = rows.map(({ label, value, color }) => {
            return `<div><span style="color: ${color}; font-weight: bold;">${label}</span>: ${formatter(value)}</div>`;
        }).join('');

        fixedLegend.innerHTML = html || '<div style="color: #999; font-style: italic;">No data</div>';

        // Adjust font size after content update
        if (fixedLegend._adjustFontSize) {
            requestAnimationFrame(fixedLegend._adjustFontSize);
        }
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
