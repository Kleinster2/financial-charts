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

        const params = new URLSearchParams();
        params.set('tickers', tickers.join(','));
        const url = `${API_BASE_URL}/api/metadata?${params.toString()}`;
        return fetchWithRetry(url);
    },
    
    /**
     * Get historical price data
     */
    async getPriceData(tickers, fromDate = null, toDate = null) {
        if (!tickers || tickers.length === 0) return {};

        const params = new URLSearchParams();
        params.set('tickers', tickers.join(','));
        if (fromDate) params.set('from', Math.floor(fromDate));
        if (toDate) params.set('to', Math.floor(toDate));
        const url = `${API_BASE_URL}/api/data?${params.toString()}`;
        return fetchWithRetry(url);
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
    }
};

// Export for use in other modules
window.DataFetcher = DataFetcher;
