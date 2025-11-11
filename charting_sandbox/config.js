/**
 * Global Configuration File
 * Centralizes all magic numbers, constants, and configuration values
 */

window.ChartConfig = {
    // Trading/Market Constants
    TRADING_DAYS_PER_YEAR: 252,
    
    // Chart Visual Settings - Professional Color Palette
    // Balanced palette: Tableau10 + ColorBrewer Set1 + Dark2 (tested, perceptually distinct)
    COLORS: [
        // Tableau10 (10 colors) - Industry standard, colorblind-friendly
        '#4E79A7', '#B8860B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1', '#C71585', '#9C755F', '#BAB0AC',
        // ColorBrewer Set1 (9 colors) - High contrast, distinct
        '#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#FFFF33', '#A65628', '#C2185B', '#999999',
        // ColorBrewer Dark2 (8 colors) - Darker tones, good separation
        '#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E', '#E6AB02', '#A6761D', '#666666',
        // Additional distinct colors (6 colors)
        '#8B4513', '#2F4F4F', '#FF6347', '#4682B4', '#DAA520', '#20B2AA'
    ],
    
    // Analysis Settings
    VOLUME_WINDOW: 100,  // Number of bars for volume SMA calculation
    
    // Timing/Delays (in milliseconds)
    DEBOUNCE_MS: {
        REBASE: 500,      // Delay for rebasing on range change
        SAVE: 2000,       // Delay for auto-saving to backend
        PLOT: 100,        // Delay before initial plot
        SEARCH: 300       // Delay for search/filter operations
    },
    
    // Chart Dimensions
    DIMENSIONS: {
        VOLUME_PANE_HEIGHT: 100,  // Base height of volume pane in pixels
        VOLUME_PANE_STRETCH_FACTOR: 1.0,  // Default stretch factor for volume pane (1.0 = equal height to main chart)
        CHART_DEFAULT_HEIGHT: 500,  // Default total chart height
        CHART_MIN_HEIGHT: 400,    // Minimum chart height
        CHART_MAX_HEIGHT: 800     // Maximum chart height
    },
    
    // API Settings
    API: {
        BASE_URL: 'http://localhost:5000',
        RETRY_COUNT: 2,
        RETRY_DELAY_BASE: 1000  // Base delay for exponential backoff
    },
    
    // Storage Keys
    STORAGE_KEYS: {
        CARDS: 'sandbox_cards',
        MULTIPLIERS: 'multipliers',
        PREFERENCES: 'chart_preferences',
        WORKSPACE: 'workspace'
    },
    
    // Chart Series Settings
    SERIES: {
        LINE_WIDTH: {
            PRICE: 2,
            AVERAGE: 3,
            VOLUME: 1
        },
        PRICE_FORMAT: {
            PRECISION: 2,
            MIN_MOVE: 0.01
        }
    },
    
    // UI Settings
    UI: {
        MAX_TICKERS_PER_CHART: 30,
        DEFAULT_TICKER: 'SPY',
        NOTIFICATION_DURATION: 3000,  // How long to show notifications
        // Chart font controls
        FONT_DEFAULT: 12,
        FONT_MIN: 8,
        FONT_MAX: 24,
        FONT_STEP: 1
    },

    // Range behavior
    RANGE: {
        // If a saved visible range covers less than this fraction of the data width
        // on initial plot, auto-fit to full data and persist the new range.
        // Set to 0 to always honor saved ranges, or very low (0.01) for minimal override
        FIT_MIN_COVERAGE: 0.01
    }
};

/**
 * Convert hex color to RGB
 */
window.ChartConfig._hexToRgb = function(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
};

/**
 * Calculate perceptual color distance (CIE76 approximation)
 * Returns a value where higher = more different
 */
window.ChartConfig._colorDistance = function(color1, color2) {
    const rgb1 = this._hexToRgb(color1);
    const rgb2 = this._hexToRgb(color2);

    if (!rgb1 || !rgb2) return 0;

    // Weighted Euclidean distance (approximates human perception)
    const rMean = (rgb1.r + rgb2.r) / 2;
    const dr = rgb1.r - rgb2.r;
    const dg = rgb1.g - rgb2.g;
    const db = rgb1.b - rgb2.b;

    return Math.sqrt(
        (2 + rMean/256) * dr * dr +
        4 * dg * dg +
        (2 + (255-rMean)/256) * db * db
    );
};

/**
 * Get a consistent color for a ticker symbol
 * Uses a simple hash function to ensure the same ticker always gets the same color
 */
window.ChartConfig.getTickerColor = function(ticker) {
    if (!ticker) return this.COLORS[0];

    // Simple hash function for string
    let hash = 0;
    for (let i = 0; i < ticker.length; i++) {
        hash = ((hash << 5) - hash) + ticker.charCodeAt(i);
        hash = hash & hash; // Convert to 32-bit integer
    }

    // Use absolute value and modulo to get color index
    const index = Math.abs(hash) % this.COLORS.length;
    return this.COLORS[index];
};

/**
 * Optimize color assignment for a list of tickers within a chart
 * Maintains cross-chart consistency while maximizing within-chart contrast
 *
 * @param {Array<string>} tickers - List of ticker symbols
 * @returns {Map<string, string>} Map of ticker to optimized color
 */
window.ChartConfig.optimizeChartColors = function(tickers) {
    if (!tickers || tickers.length === 0) return new Map();

    const colorMap = new Map();

    // Step 1: Hash each ticker to get its "preferred" color indices
    // We'll create a list of candidate colors for each ticker (primary + alternatives)
    const tickerCandidates = tickers.map(ticker => {
        const primaryIndex = Math.abs(this._hashString(ticker)) % this.COLORS.length;

        // Generate alternative indices by rotating through palette
        const candidates = [];
        for (let offset = 0; offset < this.COLORS.length; offset++) {
            const index = (primaryIndex + offset) % this.COLORS.length;
            candidates.push({
                ticker,
                color: this.COLORS[index],
                index,
                isPrimary: offset === 0,
                offset
            });
        }
        return candidates;
    });

    // Step 2: Greedy assignment - assign colors to maximize minimum distance
    const usedColors = new Set();
    const assignments = [];

    for (let i = 0; i < tickers.length; i++) {
        let bestCandidate = null;
        let bestScore = -Infinity;

        for (const candidate of tickerCandidates[i]) {
            // Skip if color already used
            if (usedColors.has(candidate.color)) continue;

            // Calculate score: prefer primary color, but maximize distance to already assigned
            let minDistance = Infinity;
            for (const assigned of assignments) {
                const distance = this._colorDistance(candidate.color, assigned.color);
                minDistance = Math.min(minDistance, distance);
            }

            // Score favors: (1) minimum distance to existing colors, (2) primary color preference
            const score = (assignments.length === 0 ? 1000 : minDistance) - (candidate.offset * 10);

            if (score > bestScore) {
                bestScore = score;
                bestCandidate = candidate;
            }
        }

        if (bestCandidate) {
            usedColors.add(bestCandidate.color);
            assignments.push(bestCandidate);
            colorMap.set(bestCandidate.ticker, bestCandidate.color);
        } else {
            // Fallback: use hash-based color even if duplicate
            colorMap.set(tickers[i], this.getTickerColor(tickers[i]));
        }
    }

    return colorMap;
};

/**
 * Helper: Hash a string to an integer
 */
window.ChartConfig._hashString = function(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
        hash = ((hash << 5) - hash) + str.charCodeAt(i);
        hash = hash & hash;
    }
    return hash;
};

// Freeze the config to prevent accidental modifications
Object.freeze(window.ChartConfig);
Object.freeze(window.ChartConfig.COLORS);
Object.freeze(window.ChartConfig.DEBOUNCE_MS);
Object.freeze(window.ChartConfig.DIMENSIONS);
Object.freeze(window.ChartConfig.API);
Object.freeze(window.ChartConfig.STORAGE_KEYS);
Object.freeze(window.ChartConfig.SERIES);
Object.freeze(window.ChartConfig.SERIES.LINE_WIDTH);
Object.freeze(window.ChartConfig.SERIES.PRICE_FORMAT);
Object.freeze(window.ChartConfig.UI);
Object.freeze(window.ChartConfig.RANGE);

console.log('[Config] Global configuration loaded');
