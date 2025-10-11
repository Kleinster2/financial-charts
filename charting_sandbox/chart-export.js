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
            addWatermark = false
        } = options;

        try {
            if (!chart || typeof chart.takeScreenshot !== 'function') {
                throw new Error('Chart instance not available or takeScreenshot not supported');
            }

            // Take screenshot using native API
            const canvas = chart.takeScreenshot();

            // If title is requested, create a composite canvas with title
            let finalCanvas = canvas;
            if (includeTitle && title) {
                finalCanvas = this._addTitleToCanvas(canvas, title);
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
     * @returns {Promise<Object>} Result object
     */
    async exportForLinkedIn(chart, title = '') {
        const timestamp = new Date().toISOString().split('T')[0];
        const safeTitle = title.replace(/[^a-z0-9]/gi, '_').toLowerCase() || 'chart';
        const filename = `${safeTitle}_${timestamp}.png`;

        return await this.exportToPNG(chart, {
            filename: filename,
            includeTitle: !!title,
            title: title,
            addWatermark: false
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
