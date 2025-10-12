/**
 * Chart Export Manager
 * Handles exporting charts as images using LightweightCharts v5 takeScreenshot API
 */

window.ChartExport = {
    /**
     * Export chart to PNG using native takeScreenshot API
     * @param {Object} chart - LightweightCharts chart instance
     * @param {Object} options - Export options
     * @returns {Promise<Object>} Result object with success status
     */
    async exportToPNG(chart, options = {}) {
        const {
            filename = 'chart-export.png',
            includeTitle = false,
            title = '',
            addWatermark = false,
            chartBox = null
        } = options;

        try {
            if (!chart || typeof chart.takeScreenshot !== 'function') {
                throw new Error('Chart instance not available or takeScreenshot not supported');
            }

            // Take screenshot using native API
            const canvas = chart.takeScreenshot();

            // Composite legend onto canvas if available
            let finalCanvas = canvas;
            if (chartBox) {
                finalCanvas = await this._compositeLegend(canvas, chartBox);
            }

            // If title is requested, create a composite canvas with title
            if (includeTitle && title) {
                finalCanvas = this._addTitleToCanvas(finalCanvas, title);
            }

            // Add watermark if requested
            if (addWatermark) {
                finalCanvas = this._addWatermark(finalCanvas);
            }

            // Download the image
            finalCanvas.toBlob((blob) => {
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = filename;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            }, 'image/png');

            return { success: true, message: 'Chart exported successfully' };

        } catch (error) {
            console.error('[ChartExport] Export error:', error);
            return { success: false, message: error.message };
        }
    },

    /**
     * Export chart optimized for LinkedIn
     * @param {Object} chart - LightweightCharts chart instance
     * @param {string} title - Chart title
     * @param {HTMLElement} chartBox - Chart container element for legend capture
     * @returns {Promise<Object>} Result object
     */
    async exportForLinkedIn(chart, title = '', chartBox = null) {
        const timestamp = new Date().toISOString().split('T')[0];
        const safeTitle = title.replace(/[^a-z0-9]/gi, '_').toLowerCase() || 'chart';
        const filename = `${safeTitle}_${timestamp}.png`;

        return await this.exportToPNG(chart, {
            filename: filename,
            includeTitle: !!title,
            title: title,
            addWatermark: false,
            chartBox: chartBox
        });
    },

    /**
     * Copy chart to clipboard for quick sharing
     * @param {Object} chart - LightweightCharts chart instance
     * @returns {Promise<Object>} Result object
     */
    async copyToClipboard(chart) {
        try {
            if (!chart || typeof chart.takeScreenshot !== 'function') {
                throw new Error('Chart instance not available');
            }

            const canvas = chart.takeScreenshot();

            // Convert to blob and copy to clipboard
            canvas.toBlob(async (blob) => {
                try {
                    await navigator.clipboard.write([
                        new ClipboardItem({ 'image/png': blob })
                    ]);
                    console.log('[ChartExport] Chart copied to clipboard');
                } catch (err) {
                    console.error('[ChartExport] Clipboard error:', err);
                    alert('Failed to copy to clipboard. Your browser may not support this feature.');
                }
            }, 'image/png');

            return { success: true, message: 'Chart copied to clipboard' };

        } catch (error) {
            console.error('[ChartExport] Copy error:', error);
            return { success: false, message: error.message };
        }
    },

    /**
     * Composite legend elements onto canvas
     * @private
     */
    async _compositeLegend(sourceCanvas, chartBox) {
        // Create new canvas matching source
        const newCanvas = document.createElement('canvas');
        newCanvas.width = sourceCanvas.width;
        newCanvas.height = sourceCanvas.height;

        const ctx = newCanvas.getContext('2d');

        // Draw original chart
        ctx.drawImage(sourceCanvas, 0, 0);

        // Find visible legend elements (both floating and fixed)
        const legends = [
            chartBox.querySelector('.floating-legend'),
            chartBox.querySelector('.fixed-legend')
        ].filter(el => el && el.style.display !== 'none' && el.offsetParent !== null);

        for (const legend of legends) {
            try {
                // Get legend position and size
                const legendRect = legend.getBoundingClientRect();
                const chartRect = chartBox.getBoundingClientRect();

                // Calculate position relative to chart
                const x = legendRect.left - chartRect.left;
                const y = legendRect.top - chartRect.top;

                // Get computed styles
                const styles = window.getComputedStyle(legend);
                const bgColor = styles.backgroundColor;
                const borderColor = styles.borderColor;
                const borderWidth = parseInt(styles.borderWidth) || 1;
                const borderRadius = parseInt(styles.borderRadius) || 0;
                const padding = parseInt(styles.padding) || 8;

                // Draw legend background with rounded corners
                ctx.fillStyle = bgColor;
                ctx.strokeStyle = borderColor;
                ctx.lineWidth = borderWidth;

                if (borderRadius > 0) {
                    this._roundRect(ctx, x, y, legendRect.width, legendRect.height, borderRadius);
                    ctx.fill();
                    ctx.stroke();
                } else {
                    ctx.fillRect(x, y, legendRect.width, legendRect.height);
                    ctx.strokeRect(x, y, legendRect.width, legendRect.height);
                }

                // Draw legend content with proper styling
                const contentElement = legend.classList.contains('fixed-legend')
                    ? legend.querySelector('.fixed-legend-content')
                    : legend;

                if (contentElement) {
                    this._drawLegendContent(ctx, contentElement, x, y, padding, styles);
                }

            } catch (err) {
                console.warn('[ChartExport] Failed to composite legend:', err);
            }
        }

        return newCanvas;
    },

    /**
     * Draw legend content with styled text (colors, bold, etc.)
     * @private
     */
    _drawLegendContent(ctx, contentElement, baseX, baseY, padding, legendStyles) {
        const fontSize = parseInt(legendStyles.fontSize) || 12;
        const fontFamily = legendStyles.fontFamily || 'monospace';
        const lineHeight = fontSize * 1.4;

        let textY = baseY + padding;

        // Process each child div element
        const divs = contentElement.querySelectorAll('div');

        divs.forEach(div => {
            if (div.textContent.trim() === '') return;

            let textX = baseX + padding;
            ctx.textBaseline = 'top';

            // Process each child node (text and spans)
            const processNode = (node) => {
                if (node.nodeType === Node.TEXT_NODE) {
                    // Plain text
                    const text = node.textContent;
                    if (text.trim()) {
                        ctx.font = `${fontSize}px ${fontFamily}`;
                        ctx.fillStyle = legendStyles.color || '#333';
                        ctx.fillText(text, textX, textY);
                        textX += ctx.measureText(text).width;
                    }
                } else if (node.nodeType === Node.ELEMENT_NODE && node.tagName === 'SPAN') {
                    // Styled span (ticker names, etc.)
                    const spanStyles = window.getComputedStyle(node);
                    const text = node.textContent;

                    if (text.trim()) {
                        // Apply span styles
                        const isBold = spanStyles.fontWeight === 'bold' || parseInt(spanStyles.fontWeight) >= 600;
                        const fontWeight = isBold ? 'bold' : 'normal';
                        ctx.font = `${fontWeight} ${fontSize}px ${fontFamily}`;
                        ctx.fillStyle = spanStyles.color || legendStyles.color || '#333';

                        ctx.fillText(text, textX, textY);
                        textX += ctx.measureText(text).width;
                    }
                }
            };

            // Process all child nodes in order
            Array.from(div.childNodes).forEach(processNode);

            textY += lineHeight;
        });
    },

    /**
     * Helper to draw rounded rectangle
     * @private
     */
    _roundRect(ctx, x, y, width, height, radius) {
        ctx.beginPath();
        ctx.moveTo(x + radius, y);
        ctx.lineTo(x + width - radius, y);
        ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
        ctx.lineTo(x + width, y + height - radius);
        ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
        ctx.lineTo(x + radius, y + height);
        ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
        ctx.lineTo(x, y + radius);
        ctx.quadraticCurveTo(x, y, x + radius, y);
        ctx.closePath();
    },

    /**
     * Add title to canvas (creates new canvas with title above chart)
     * @private
     */
    _addTitleToCanvas(sourceCanvas, title) {
        const titleHeight = 60;
        const padding = 20;

        // Create new canvas with space for title
        const newCanvas = document.createElement('canvas');
        newCanvas.width = sourceCanvas.width;
        newCanvas.height = sourceCanvas.height + titleHeight;

        const ctx = newCanvas.getContext('2d');

        // Fill background
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, newCanvas.width, newCanvas.height);

        // Draw title
        ctx.fillStyle = '#333333';
        ctx.font = 'bold 24px Arial, sans-serif';
        ctx.textBaseline = 'middle';
        ctx.fillText(title, padding, titleHeight / 2);

        // Draw chart below title
        ctx.drawImage(sourceCanvas, 0, titleHeight);

        return newCanvas;
    },

    /**
     * Add subtle watermark to canvas
     * @private
     */
    _addWatermark(sourceCanvas) {
        const newCanvas = document.createElement('canvas');
        newCanvas.width = sourceCanvas.width;
        newCanvas.height = sourceCanvas.height;

        const ctx = newCanvas.getContext('2d');

        // Draw original chart
        ctx.drawImage(sourceCanvas, 0, 0);

        // Add watermark in bottom right
        const watermarkText = 'Financial Charts';
        ctx.fillStyle = 'rgba(0, 0, 0, 0.3)';
        ctx.font = '12px Arial, sans-serif';
        ctx.textAlign = 'right';
        ctx.textBaseline = 'bottom';
        ctx.fillText(watermarkText, newCanvas.width - 10, newCanvas.height - 10);

        return newCanvas;
    }
};
