/**
 * Sandbox Initialization Module
 *
 * Index-specific bootstrapping: autocomplete population, workspace restore,
 * default card creation. Extracted from card.js so other pages can reuse
 * createChartCard without pulling in this bootstrap logic.
 *
 * Exports: window.SandboxInit
 */

window.SandboxInit = (() => {

    /**
     * Populate ticker autocomplete datalist
     */
    async function populateAutocomplete() {
        try {
            const [tickersResp, metadataResp] = await Promise.all([
                fetch(window.ChartUtils.apiUrl('/api/tickers')),
                fetch(window.ChartUtils.apiUrl('/api/metadata?tickers=ALL'))
            ]);

            const tickers = await tickersResp.json();
            const metadata = await metadataResp.json();

            const dl = document.getElementById('ticker-list');
            if (dl) {
                dl.innerHTML = '';

                // Add ticker options with company names
                tickers.forEach(t => {
                    const opt = document.createElement('option');

                    // If we have metadata, create option as "TICKER - Company Name"
                    // This allows searching by either ticker or company name
                    if (metadata[t] && metadata[t] !== t) {
                        opt.value = `${t} - ${metadata[t]}`;
                    } else {
                        opt.value = t;
                    }

                    dl.appendChild(opt);
                });

                // Add special tickers
                ['ALLW_VALUE', 'ALLW_SHARES'].forEach(x => {
                    const opt = document.createElement('option');
                    opt.value = x;
                    dl.appendChild(opt);
                });
            }
        } catch (e) {
            console.warn('Failed to populate autocomplete:', e);
        }
    }

    /**
     * Restore workspace from server or localStorage
     */
    async function restoreWorkspace() {
        // Check for ?blank URL param - start with empty card
        const urlParams = new URLSearchParams(window.location.search);
        const startBlank = urlParams.has('blank');

        // Helper to navigate to page from URL param
        const navigateToUrlPage = () => {
            const pageParam = urlParams.get('page');
            if (pageParam && window.PageManager) {
                const pageNum = parseInt(pageParam, 10);
                if (!isNaN(pageNum)) {
                    setTimeout(() => {
                        window.PageManager.showPage(pageNum);
                        console.log(`[Restore] Navigated to page ${pageNum} from URL param`);
                    }, 100);
                }
            }
        };

        if (startBlank) {
            window.createChartCard('');
            return;
        }

        try {
            const resp = await fetch(window.ChartUtils.apiUrl('/api/workspace'));
            const ws = await resp.json();

            if (Array.isArray(ws) && ws.length) {
                // Legacy workspace format (array of cards)
                console.log('[Restore] Loaded legacy workspace (array) from server');
                ws.forEach(c => window.ChartCardRegistry.restoreCard(c));
                window.ChartUtils.safeSetJSON(window.ChartConfig.STORAGE_KEYS.CARDS, ws);
                return;
            } else if (ws && typeof ws === 'object') {
                // New workspace format with pages metadata
                const cards = Array.isArray(ws.cards) ? ws.cards : [];
                const pagesMeta = (ws.pages && typeof ws.pages === 'object') ? ws.pages : null;

                if (pagesMeta) {
                    window.ChartUtils.safeSetJSON('sandbox_pages', pagesMeta);
                    const nameCount = pagesMeta.names ? Object.keys(pagesMeta.names).length : 0;
                    console.log(`[Restore] Loaded workspace (object) from server; pages meta present (pageNames=${nameCount})`);

                    if (window.PageManager) {
                        // Create additional pages
                        if (Array.isArray(pagesMeta.pages)) {
                            pagesMeta.pages.filter(n => n !== 1).forEach(n => window.PageManager.ensurePage(n));
                        }
                        // Restore page names
                        if (pagesMeta.names && typeof pagesMeta.names === 'object') {
                            Object.entries(pagesMeta.names).forEach(([num, name]) => {
                                window.PageManager.renamePage(Number(num), String(name));
                            });
                        }
                        // Restore active page
                        if (pagesMeta.active) {
                            window.PageManager.showPage(pagesMeta.active);
                        }
                    }
                } else {
                    console.log('[Restore] Workspace object has no pages meta');
                }

                // Restore cards
                cards.forEach(c => window.ChartCardRegistry.restoreCard(c));
                window.ChartUtils.safeSetJSON(window.ChartConfig.STORAGE_KEYS.CARDS, cards);

                // Refresh navigation filtering after cards are loaded
                if (window.PageManager && typeof window.PageManager.refreshNavigation === 'function') {
                    window.PageManager.refreshNavigation();
                }

                if (cards.length > 0) {
                    navigateToUrlPage();
                    return;
                }
                console.log('[Restore] Workspace object had no cards; checking localStorage');
            } else {
                console.log('[Restore] Server returned empty workspace; checking localStorage');
            }
        } catch (e) {
            console.warn('[Restore] Server load failed, falling back to localStorage', e);
        }

        // Fallback to localStorage
        const stored = window.ChartUtils.safeGetJSON(window.ChartConfig.STORAGE_KEYS.CARDS, []);
        if (Array.isArray(stored) && stored.length) {
            console.log('[Restore] Loaded workspace from localStorage fallback');
            stored.forEach(c => window.ChartCardRegistry.restoreCard(c));

            // Refresh navigation filtering after cards are loaded
            if (window.PageManager && typeof window.PageManager.refreshNavigation === 'function') {
                window.PageManager.refreshNavigation();
            }

            // Push local state to server to sync
            if (window.StateManager && typeof window.StateManager.saveCards === 'function') {
                window.StateManager.saveCards(stored);
            }
        } else {
            console.log('[Restore] No stored workspace found; creating default card');
            window.createChartCard('SPY');
        }

        navigateToUrlPage();
    }

    /**
     * Initialize the sandbox (called on DOMContentLoaded)
     */
    function initialize() {
        // Bind add chart button
        const addBtn = document.getElementById('add-chart-btn');
        if (addBtn) {
            addBtn.addEventListener('click', () => window.createChartCard(''));
        }

        // Populate autocomplete (async, non-blocking)
        populateAutocomplete();

        // Restore workspace (async)
        restoreWorkspace();
    }

    // Auto-initialize on DOMContentLoaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initialize);
    } else {
        // DOM already loaded
        initialize();
    }

    return {
        populateAutocomplete,
        restoreWorkspace,
        initialize
    };

})();
