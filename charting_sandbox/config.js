/**
 * Global Configuration File
 * Centralizes all magic numbers, constants, and configuration values
 */

window.ChartConfig = {
    // Trading/Market Constants
    TRADING_DAYS_PER_YEAR: 252,
    
    // Chart Visual Settings
    COLORS: [
        '#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf',
        '#393b79','#637939','#8c6d31','#843c39','#7b4173','#3182bd','#31a354','#756bb1','#636363','#e6550d',
        '#e31a1c','#6baed6','#9ecae1','#c6dbef','#fd8d3c','#fdd0a2','#fdae6b','#a1d99b','#74c476','#31a354',
        '#6baed6','#9e9ac8','#bcbddc','#dadaeb','#fcbba1','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d',
        '#084594','#4292c6','#6baed6','#9ecae1','#c6dbef','#d9f0a3','#addd8e','#78c679','#41ab5d','#238443',
        '#006837','#004529','#990099','#ff0099','#00bfff','#ffa500','#ff0000','#00ff00','#008FFB','#00E396',
        '#008FFB', '#00E396', '#FEB019', '#FF4560', '#775DD0', '#546E7A', '#26a69a', '#D10CE8',
        '#FF66C3', '#FF8633', '#2B908F', '#F0E442', '#3D85C6', '#A52A2A', '#FFD700', '#00BFFF',
        '#FF1493', '#00FA9A', '#9932CC', '#FF4500', '#4B0082'
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
