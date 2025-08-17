/**
 * data-fetcher.js - API communication module
 * Handles all backend API calls with error handling and retry logic
 */

// Base URL configuration (use same origin as the page/server)
const API_BASE_URL = window.location.origin;

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
        
        const url = `${API_BASE_URL}/api/metadata?tickers=${tickers.join(',')}`;
        return fetchWithRetry(url);
    },
    
    /**
     * Get historical price data
     */
    async getPriceData(tickers, fromDate = null, toDate = null, tf = '1d') {
        if (!tickers || (Array.isArray(tickers) && tickers.length === 0)) return {};
        const list = Array.isArray(tickers) ? tickers : [tickers];

        let url = `${API_BASE_URL}/api/data?tickers=${list.join(',')}`;

        // Convert unix seconds to YYYY-MM-DD for server params
        const tsToDate = (ts) => {
            const d = new Date(Math.floor(ts) * 1000);
            return d.toISOString().slice(0, 10);
        };

        if (fromDate) {
            url += `&start=${tsToDate(fromDate)}`;
        }
        if (toDate) {
            url += `&end=${tsToDate(toDate)}`;
        }
        if (tf) {
            url += `&tf=${encodeURIComponent(tf)}`;
        }

        return fetchWithRetry(url);
    },
    
    /**
     * Get volume data
     */
    async getVolumeData(tickers, fromDate = null, toDate = null, tf = '1d') {
        if (!tickers || (Array.isArray(tickers) && tickers.length === 0)) return {};
        const list = Array.isArray(tickers) ? tickers : [tickers];

        let url = `${API_BASE_URL}/api/volume?tickers=${list.join(',')}`;

        const tsToDate = (ts) => {
            const d = new Date(Math.floor(ts) * 1000);
            return d.toISOString().slice(0, 10);
        };

        if (fromDate) {
            url += `&start=${tsToDate(fromDate)}`;
        }
        if (toDate) {
            url += `&end=${tsToDate(toDate)}`;
        }
        if (tf) {
            url += `&tf=${encodeURIComponent(tf)}`;
        }

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
        return fetchWithRetry(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(cards)
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
        let url = `${API_BASE_URL}/api/commentary?ticker=${ticker}`;
        
        if (fromDate && toDate) {
            url += `&from=${Math.floor(fromDate)}&to=${Math.floor(toDate)}`;
        }
        
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
    }
};

// DataFetcher is attached to window above.
