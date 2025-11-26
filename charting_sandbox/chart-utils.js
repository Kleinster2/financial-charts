/**
 * chart-utils.js - Chart utilities and helpers
 * Common chart operations, calculations, and formatting
 */

window.ChartUtils = {
    /**
     * Format price value for display
     */
    formatPrice(value) {
        if (value === null || value === undefined) return '';
        
        if (Math.abs(value) >= 1e9) {
            return (value / 1e9).toFixed(2) + 'B';
        } else if (Math.abs(value) >= 1e6) {
            return (value / 1e6).toFixed(2) + 'M';
        } else if (Math.abs(value) >= 1e3) {
            return (value / 1e3).toFixed(2) + 'K';
        } else if (Math.abs(value) >= 100) {
            return value.toFixed(0);
        } else if (Math.abs(value) >= 10) {
            return value.toFixed(1);
        } else if (Math.abs(value) >= 1) {
            return value.toFixed(2);
        } else {
            return value.toFixed(4);
        }
    },
    
    /**
     * Format volume value for display
     */
    formatVolume(value) {
        if (value === null || value === undefined) return '';
        
        if (value >= 1e9) {
            return (value / 1e9).toFixed(1) + 'B';
        } else if (value >= 1e6) {
            return (value / 1e6).toFixed(1) + 'M';
        } else if (value >= 1e3) {
            return (value / 1e3).toFixed(1) + 'K';
        } else {
            return value.toFixed(0);
        }
    },
    
    /**
     * Calculate rebased series (all start at 100)
     */
    rebaseSeries(data, baseDate = null) {
        if (!data || data.length === 0) return data;
        
        // Find base value (first non-null value or value at baseDate)
        let baseValue = null;
        let baseIndex = 0;
        
        if (baseDate) {
            // Find value at or near baseDate
            for (let i = 0; i < data.length; i++) {
                if (data[i].time >= baseDate) {
                    if (data[i].value !== null) {
                        baseValue = data[i].value;
                        baseIndex = i;
                    }
                    break;
                }
            }
        }
        
        // If no base found, use first non-null value
        if (baseValue === null) {
            for (let i = 0; i < data.length; i++) {
                if (data[i].value !== null) {
                    baseValue = data[i].value;
                    baseIndex = i;
                    break;
                }
            }
        }
        
        if (baseValue === null || baseValue === 0) return data;
        
        // Rebase all values
        return data.map((point, i) => ({
            time: point.time,
            value: point.value !== null ? (point.value / baseValue) * 100 : null
        }));
    },
    
    /**
     * Calculate difference series (subtract first series from all others)
     */
    calculateDifference(baseSeries, compareSeries) {
        if (!baseSeries || !compareSeries) return compareSeries;
        
        // Create a map for quick lookup
        const baseMap = new Map(baseSeries.map(p => [p.time, p.value]));
        
        return compareSeries.map(point => {
            const baseValue = baseMap.get(point.time);
            return {
                time: point.time,
                value: (point.value !== null && baseValue !== null) 
                    ? point.value - baseValue 
                    : null
            };
        });
    },
    
    /**
     * Calculate moving average
     */
    calculateMovingAverage(data, period = 20) {
        if (!data || data.length < period) return [];
        
        const result = [];
        for (let i = period - 1; i < data.length; i++) {
            let sum = 0;
            let count = 0;
            
            for (let j = 0; j < period; j++) {
                const value = data[i - j].value;
                if (value !== null) {
                    sum += value;
                    count++;
                }
            }
            
            result.push({
                time: data[i].time,
                value: count > 0 ? sum / count : null
            });
        }
        
        return result;
    },
    
    /**
     * Calculate volatility (rolling standard deviation)
     */
    calculateVolatility(data, period = 20) {
        if (!data || data.length < period) return [];
        
        const result = [];
        
        for (let i = period - 1; i < data.length; i++) {
            const values = [];
            
            for (let j = 0; j < period; j++) {
                const value = data[i - j].value;
                if (value !== null) {
                    values.push(value);
                }
            }
            
            if (values.length > 1) {
                const mean = values.reduce((a, b) => a + b, 0) / values.length;
                const variance = values.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / values.length;
                result.push({
                    time: data[i].time,
                    value: Math.sqrt(variance)
                });
            } else {
                result.push({
                    time: data[i].time,
                    value: null
                });
            }
        }
        
        return result;
    },
    
    /**
     * Get date range from series data
     */
    getDateRange(seriesData) {
        let minTime = Infinity;
        let maxTime = -Infinity;
        
        Object.values(seriesData).forEach(data => {
            if (Array.isArray(data) && data.length > 0) {
                minTime = Math.min(minTime, data[0].time);
                maxTime = Math.max(maxTime, data[data.length - 1].time);
            }
        });
        
        return {
            from: minTime === Infinity ? null : minTime,
            to: maxTime === -Infinity ? null : maxTime
        };
    },
    
    /**
     * Merge multiple series by time
     */
    mergeSeries(seriesMap) {
        const timeSet = new Set();
        
        // Collect all unique times
        Object.values(seriesMap).forEach(data => {
            if (Array.isArray(data)) {
                data.forEach(point => timeSet.add(point.time));
            }
        });
        
        // Sort times
        const times = Array.from(timeSet).sort((a, b) => a - b);
        
        // Create merged data
        const merged = times.map(time => {
            const point = { time };
            
            Object.entries(seriesMap).forEach(([key, data]) => {
                if (Array.isArray(data)) {
                    const found = data.find(p => p.time === time);
                    point[key] = found ? found.value : null;
                }
            });
            
            return point;
        });
        
        return merged;
    },
    
    /**
     * Get visible range for chart (with padding)
     */
    calculateVisibleRange(data, paddingPercent = 0.02) {
        const range = this.getDateRange(data);
        
        if (!range.from || !range.to) return null;
        
        const span = range.to - range.from;
        const padding = span * paddingPercent;
        
        return {
            from: range.from - padding,
            to: range.to + padding
        };
    },
    
    /**
     * Convert date to Unix timestamp
     */
    dateToTimestamp(date) {
        if (typeof date === 'number') return date;
        if (date instanceof Date) return Math.floor(date.getTime() / 1000);
        if (typeof date === 'string') return Math.floor(new Date(date).getTime() / 1000);
        return null;
    },
    
    /**
     * Convert Unix timestamp to date string
     */
    timestampToDate(timestamp) {
        return new Date(timestamp * 1000).toISOString().split('T')[0];
    },
    
    /**
     * Get predefined date ranges
     */
    getPresetRanges() {
        const now = Date.now() / 1000;
        const day = 86400;
        
        return {
            '1D': { from: now - day, to: now },
            '1W': { from: now - (7 * day), to: now },
            '1M': { from: now - (30 * day), to: now },
            '3M': { from: now - (90 * day), to: now },
            '6M': { from: now - (180 * day), to: now },
            'YTD': { 
                from: this.dateToTimestamp(new Date(new Date().getFullYear(), 0, 1)), 
                to: now 
            },
            '1Y': { from: now - (365 * day), to: now },
            '2Y': { from: now - (730 * day), to: now },
            '5Y': { from: now - (1825 * day), to: now },
            '10Y': { from: now - (3650 * day), to: now },
            'ALL': null // Will be calculated from data
        };
    },
    
    /**
     * Debounce function
     */
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    /**
     * Throttle function
     */
    throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },

    /**
     * Bind a slider control with live preview and save-on-release
     * @param {HTMLInputElement} slider - The slider input element
     * @param {HTMLElement} displayEl - Element to show current value (optional)
     * @param {Object} options - Configuration options
     * @param {Function} options.onInput - Called during drag with current value
     * @param {Function} options.onCommit - Called on release (default: window.saveCards)
     * @param {number} options.initialValue - Initial slider value
     * @param {Function} options.formatDisplay - Format value for display (default: String)
     */
    bindSliderControl(slider, displayEl, options) {
        if (!slider) return;

        const {
            onInput,
            onCommit = () => { if (window.saveCards) window.saveCards(); },
            initialValue,
            formatDisplay = String
        } = options;

        slider.addEventListener('input', (e) => {
            const value = parseFloat(e.target.value);
            if (onInput) onInput(value);
            if (displayEl) displayEl.textContent = formatDisplay(value);
        });

        slider.addEventListener('change', onCommit);

        // Initialize
        slider.value = initialValue;
        if (displayEl) displayEl.textContent = formatDisplay(initialValue);
    },

    /**
     * Create a price formatter based on mode and precision
     * @param {boolean} useRaw - Whether to use raw prices or percentage
     * @param {number} precision - Number of decimal places
     * @returns {Object} LightweightCharts price format object
     */
    createPriceFormatter(useRaw, precision) {
        if (useRaw) {
            return {
                type: 'custom',
                minMove: 0.01,
                formatter: (price) => {
                    // Magnitude-based decimals for raw prices, capped by slider maximum
                    const absPrice = Math.abs(price);
                    const magDecimals = absPrice >= 1000 ? 0 : absPrice >= 100 ? 1 : absPrice >= 1 ? 2 : absPrice >= 0.01 ? 4 : 6;
                    const dec = Math.min(magDecimals, precision);
                    return price.toFixed(dec);
                }
            };
        } else {
            return {
                type: 'custom',
                minMove: 0.1,
                formatter: (v) => {
                    const diff = v - 100;
                    const sign = diff > 0 ? '+' : diff < 0 ? '-' : '';
                    // Magnitude-based decimals, capped by slider maximum
                    const magDecimals = Math.abs(diff) >= 100 ? 0 : Math.abs(diff) >= 10 ? 1 : 2;
                    const dec = Math.min(magDecimals, precision);
                    return `${sign}${Math.abs(diff).toFixed(dec)}%`;
                }
            };
        }
    }
};

// Export for use in other modules
try { console.log('[ChartUtils] Loaded'); } catch(e) {}
