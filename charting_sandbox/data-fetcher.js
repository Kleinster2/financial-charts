/**
 * data-fetcher.js - API communication module
 * Handles all backend API calls with error handling and retry logic
 */

// Base URL configuration
const API_BASE_URL = 'http://localhost:5000';

// Utility function for fetch with retry
async function fetchWithRetry(url, options = {}, retries = 2) {
    for (let i = 0; i <= retries; i++) {
        try {
            console.log(`Fetching: ${url}${i > 0 ? ` (retry ${i})` : ''}`);
            const resp = await fetch(url, options);
            
            if (!resp.ok) {
                throw new Error(`HTTP ${resp.status}: ${resp.statusText}`);
            }
            
            return await resp.json();
        } catch (error) {
            console.error(`Fetch error: ${error.message}`);
            
            if (i === retries) {
                throw error;
            }
            
            // Wait before retry (exponential backoff)
            await new Promise(resolve => setTimeout(resolve, 1000 * Math.pow(2, i)));
        }
    }
}

// API methods
window.DataFetcher = {
    /**
     * Get ticker metadata
     */
    async getMetadata(tickers) {
        if (!tickers || tickers.length === 0) return {};

        // Separate portfolio tickers from regular tickers
        const portfolioTickers = tickers.filter(t => t.startsWith('PORTFOLIO_'));
        const regularTickers = tickers.filter(t => !t.startsWith('PORTFOLIO_'));

        const results = {};

        // Fetch regular ticker metadata
        if (regularTickers.length > 0) {
            const params = new URLSearchParams();
            params.set('tickers', regularTickers.join(','));
            const url = `${API_BASE_URL}/api/metadata?${params.toString()}`;
            const regularMetadata = await fetchWithRetry(url);
            Object.assign(results, regularMetadata);
        }

        // Add portfolio metadata
        for (const portfolioTicker of portfolioTickers) {
            const portfolioId = portfolioTicker.replace('PORTFOLIO_', '');
            try {
                const url = `${API_BASE_URL}/api/portfolio/list`;
                const portfolios = await fetchWithRetry(url);
                const portfolio = portfolios.find(p => p.portfolio_id === parseInt(portfolioId));
                if (portfolio) {
                    results[portfolioTicker] = portfolio.name || `Portfolio ${portfolioId}`;
                }
            } catch (error) {
                results[portfolioTicker] = `Portfolio ${portfolioId}`;
            }
        }

        return results;
    },

    /**
     * UNIFIED DATA GETTER - ALL tickers from single source
     * No routing needed - all tickers (prices and IV) come from same API
     * Returns uniform format: {ticker: [{time, value}, ...]}
     *
     * @param {Array<string>} tickers - Array of ANY ticker symbols (AAPL, ^VXAPL, ^VIX, MSFT, etc.)
     * @param {number} days - Number of days of history (default: 5475 for 15 years)
     * @param {string} interval - Data interval: 'daily', 'weekly', or 'monthly' (default: 'daily')
     * @returns {Object} Unified data: {ticker: [{time, value}]}
     */
    async getData(tickers, days = 5475, interval = 'daily') {
        if (!tickers || tickers.length === 0) return {};

        console.log(`[Unified] Fetching ${tickers.length} tickers: ${tickers.join(', ')} (interval: ${interval})`);

        // ALL tickers go to same endpoint - /api/data handles everything
        // Backend automatically finds ticker in stock_prices_daily (which now includes IV columns)
        const results = {};

        try {
            const priceData = await this.getPriceData(tickers, null, null, interval);

            // Normalize: extract just {time, value} from data
            for (const [ticker, data] of Object.entries(priceData)) {
                results[ticker] = data.map(d => ({
                    time: d.time,
                    value: d.close || d.value || d.price
                }));
            }

            console.log(`  ✓ Fetched ${Object.keys(results).length} tickers`);
        } catch (err) {
            console.error(`  ✗ Data fetch failed:`, err);
        }

        console.log(`[Unified] Returning ${Object.keys(results).length} tickers`);
        return results;
    },

    /**
     * Get historical price data
     * @param {Array<string>} tickers - Array of ticker symbols
     * @param {number|null} fromDate - Start date (unix timestamp)
     * @param {number|null} toDate - End date (unix timestamp)
     * @param {string} interval - Data interval: 'daily', 'weekly', or 'monthly' (default: 'daily')
     */
    async getPriceData(tickers, fromDate = null, toDate = null, interval = 'daily') {
        if (!tickers || tickers.length === 0) return {};

        // Check for portfolio tickers (format: PORTFOLIO_1, PORTFOLIO_2, etc.)
        const portfolioTickers = tickers.filter(t => t.startsWith('PORTFOLIO_'));
        const regularTickers = tickers.filter(t => !t.startsWith('PORTFOLIO_'));

        const results = {};

        // Fetch regular tickers
        if (regularTickers.length > 0) {
            const params = new URLSearchParams();
            params.set('tickers', regularTickers.join(','));
            if (fromDate) params.set('from', Math.floor(fromDate));
            if (toDate) params.set('to', Math.floor(toDate));
            if (interval && interval !== 'daily') params.set('interval', interval);
            const url = `${API_BASE_URL}/api/data?${params.toString()}`;
            const regularData = await fetchWithRetry(url);
            Object.assign(results, regularData);
        }

        // Fetch portfolio data
        for (const portfolioTicker of portfolioTickers) {
            const portfolioId = portfolioTicker.replace('PORTFOLIO_', '');
            const url = `${API_BASE_URL}/api/portfolio/${portfolioId}/valuations`;
            try {
                const portfolioData = await fetchWithRetry(url);
                // Store in same format as regular tickers
                results[portfolioTicker] = portfolioData;
            } catch (error) {
                console.warn(`Failed to fetch portfolio ${portfolioId}:`, error);
            }
        }

        return results;
    },
    
    /**
     * Get volume data
     */
    async getVolumeData(tickers, fromDate = null, toDate = null) {
        if (!tickers || tickers.length === 0) return {};

        const params = new URLSearchParams();
        params.set('tickers', tickers.join(','));
        if (fromDate) params.set('from', Math.floor(fromDate));
        if (toDate) params.set('to', Math.floor(toDate));
        const url = `${API_BASE_URL}/api/volume?${params.toString()}`;
        try {
            return await fetchWithRetry(url);
        } catch (error) {
            console.warn('Volume data fetch failed, returning empty:', error);
            return {};
        }
    },
    
    /**
     * Get ETF series data
     */
    async getETFSeries(etf, metrics = ['value', 'shares']) {
        const url = `${API_BASE_URL}/api/etf/series?etf=${etf}&metrics=${metrics.join(',')}`;
        return fetchWithRetry(url);
    },
    
    /**
     * Get all available tickers
     */
    async getTickers() {
        const url = `${API_BASE_URL}/api/tickers`;
        return fetchWithRetry(url);
    },
    
    /**
     * Save workspace
     */
    async saveWorkspace(cards) {
        const url = `${API_BASE_URL}/api/workspace`;
        // Include page metadata so renames persist cross-browser
        let pagesMeta = null;
        try {
            const raw = localStorage.getItem('sandbox_pages');
            if (raw) {
                const parsed = JSON.parse(raw);
                if (parsed && typeof parsed === 'object') pagesMeta = parsed;
            }
        } catch (e) {
            console.warn('[DataFetcher] Could not read sandbox_pages for workspace save:', e);
        }
        const payload = { cards, pages: pagesMeta };
        console.log(`[DataFetcher] Saving workspace to backend (cards=${Array.isArray(cards) ? cards.length : 0}, pageNames=${pagesMeta && pagesMeta.names ? Object.keys(pagesMeta.names).length : 0})`);
        return fetchWithRetry(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        }, 0); // No retry for saves
    },
    
    /**
     * Load workspace
     */
    async loadWorkspace() {
        const url = `${API_BASE_URL}/api/workspace`;
        try {
            return await fetchWithRetry(url, {}, 1);
        } catch (error) {
            console.warn('Failed to load workspace from server:', error);
            return null;
        }
    },
    
    /**
     * Get commentary for a ticker
     */
    async getCommentary(ticker, fromDate = null, toDate = null) {
        const params = new URLSearchParams();
        params.set('ticker', ticker);
        if (fromDate && toDate) {
            params.set('from', Math.floor(fromDate));
            params.set('to', Math.floor(toDate));
        }
        const url = `${API_BASE_URL}/api/commentary?${params.toString()}`;
        return fetchWithRetry(url);
    },
    
    /**
     * Health check
     */
    async healthCheck() {
        const url = `${API_BASE_URL}/api/health`;
        try {
            const result = await fetchWithRetry(url, {}, 0);
            console.log('Health check:', result);
            return result;
        } catch (error) {
            console.error('Health check failed:', error);
            return { status: 'error', error: error.message };
        }
    },

    /**
     * Get implied volatility data for stocks
     * @param {Array<string>} tickers - Array of ticker symbols
     * @param {number} days - Number of days of history (default: 365)
     * @param {string} metric - Which IV metric to use: 'average_iv', 'call_iv', or 'put_iv' (default: 'average_iv')
     * @returns {Object} Map of ticker to array of {time, value} objects
     */
    async getImpliedVolatility(tickers, days = 365, metric = 'average_iv') {
        if (!tickers || tickers.length === 0) return {};

        const params = new URLSearchParams();
        params.set('tickers', tickers.join(','));
        params.set('days', days);
        const url = `${API_BASE_URL}/api/iv/stock?${params.toString()}`;

        try {
            const data = await fetchWithRetry(url);

            // Convert IV data to chart format
            const result = {};
            for (const [ticker, ivArray] of Object.entries(data)) {
                if (!Array.isArray(ivArray)) continue;

                result[ticker] = ivArray.map(d => ({
                    time: d.time,
                    value: (d[metric] || 0) * 100  // Convert to percentage (0.30 -> 30%)
                }));
            }

            console.log(`Fetched IV data for ${Object.keys(result).length} tickers (metric: ${metric})`);
            return result;
        } catch (error) {
            console.warn('IV data fetch failed, returning empty:', error);
            return {};
        }
    },

    /**
     * Get CBOE volatility indices (VIX, VXN, VXD)
     * @param {Array<string>} symbols - Array of CBOE symbols (e.g., ['^VIX', '^VXN'])
     * @param {number} days - Number of days of history (default: 365)
     * @returns {Object} Map of symbol to array of {time, value} objects
     */
    async getCBOEIndices(symbols, days = 365) {
        if (!symbols || symbols.length === 0) return {};

        const params = new URLSearchParams();
        params.set('symbols', symbols.join(','));
        params.set('days', days);
        const url = `${API_BASE_URL}/api/iv/cboe?${params.toString()}`;

        try {
            const data = await fetchWithRetry(url);

            // Convert to chart format
            const result = {};
            for (const [symbol, dataArray] of Object.entries(data)) {
                if (!Array.isArray(dataArray)) continue;

                result[symbol] = dataArray.map(d => ({
                    time: d.time,
                    value: d.value  // CBOE indices are already in percentage-like scale
                }));
            }

            console.log(`Fetched CBOE indices for ${Object.keys(result).length} symbols`);
            return result;
        } catch (error) {
            console.warn('CBOE indices fetch failed, returning empty:', error);
            return {};
        }
    },

    /**
     * Get latest implied volatility values
     * @param {Array<string>} tickers - Array of ticker symbols
     * @returns {Object} Map of ticker to latest IV data
     */
    async getLatestIV(tickers) {
        if (!tickers || tickers.length === 0) return {};

        const params = new URLSearchParams();
        params.set('tickers', tickers.join(','));
        const url = `${API_BASE_URL}/api/iv/latest?${params.toString()}`;

        try {
            return await fetchWithRetry(url);
        } catch (error) {
            console.warn('Latest IV fetch failed, returning empty:', error);
            return {};
        }
    }
};

// Export for use in other modules
window.DataFetcher = DataFetcher;
