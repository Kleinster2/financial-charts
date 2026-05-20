/**
 * global-search.js
 * Global ticker and company name search functionality
 */

(function() {
    'use strict';

    let tickerMetadata = {};
    let availableTickers = [];
    let searchIndex = [];
    let pageIndex = []; // { pageNum, pageName }

    /**
     * Initialize global search
     */
    async function initGlobalSearch() {
        const searchInput = document.getElementById('global-search-input');
        const searchResults = document.getElementById('search-results');

        if (!searchInput || !searchResults) {
            console.warn('[GlobalSearch] Search elements not found');
            return;
        }

        console.log('[GlobalSearch] Starting initialization...');

        // Load ticker universe + metadata
        await Promise.all([loadTickerMetadata(), loadAvailableTickers()]);

        // Build search index (async)
        await buildSearchIndex();

        // Setup event listeners
        setupSearchListeners(searchInput, searchResults);

        console.log('[GlobalSearch] Initialized with', searchIndex.length, 'unique tickers');
    }

    /**
     * Load ticker metadata from API
     */
    async function loadTickerMetadata() {
        try {
            const response = await fetch(window.ChartUtils.apiUrl('/api/metadata?tickers=ALL'));
            if (response.ok) {
                tickerMetadata = await response.json();
                console.log('[GlobalSearch] Loaded metadata for', Object.keys(tickerMetadata).length, 'tickers');
            } else {
                console.warn('[GlobalSearch] API returned non-OK status:', response.status);
            }
        } catch (error) {
            console.warn('[GlobalSearch] Failed to load metadata:', error);
            // Continue with empty metadata
        }
    }

    /**
     * Load available tickers from API so search can find symbols not yet in cards
     */
    async function loadAvailableTickers() {
        try {
            const response = await fetch(window.ChartUtils.apiUrl('/api/tickers'));
            if (response.ok) {
                availableTickers = await response.json();
                console.log('[GlobalSearch] Loaded ticker universe:', availableTickers.length);
            } else {
                console.warn('[GlobalSearch] /api/tickers returned non-OK status:', response.status);
            }
        } catch (error) {
            console.warn('[GlobalSearch] Failed to load ticker universe:', error);
            availableTickers = [];
        }
    }

    /**
     * Build search index from workspace
     */
    async function buildSearchIndex() {
        searchIndex = [];

        // Check if StateManager exists
        if (!window.StateManager || typeof window.StateManager.loadCards !== 'function') {
            console.warn('[GlobalSearch] StateManager not available yet, will retry');
            return;
        }

        // Get all cards from workspace (async)
        let workspace;
        try {
            workspace = await window.StateManager.loadCards();
        } catch (error) {
            console.warn('[GlobalSearch] Failed to load workspace:', error);
            return;
        }

        if (!workspace || !Array.isArray(workspace)) {
            console.warn('[GlobalSearch] Invalid workspace structure:', workspace);
            return;
        }

        // Build index of ticker -> [locations]
        const tickerLocations = new Map();
        const pageCardCounts = new Map();

        workspace.forEach((card, cardIndex) => {
            const page = card.page || '1';
            const title = card.title || `Chart ${cardIndex + 1}`;
            const tickers = card.tickers || [];
            const pageCardIndex = pageCardCounts.get(page) || 0;
            pageCardCounts.set(page, pageCardIndex + 1);

            tickers.forEach(ticker => {
                if (!tickerLocations.has(ticker)) {
                    tickerLocations.set(ticker, []);
                }
                tickerLocations.get(ticker).push({
                    page,
                    title,
                    cardIndex,
                    pageCardIndex,
                    card
                });
            });
        });

        // Convert to search index array. Include DB tickers even if they are not
        // currently present in a saved chart card.
        const allTickers = new Set([...availableTickers, ...tickerLocations.keys()]);
        allTickers.forEach((ticker) => {
            const name = tickerMetadata[ticker] || '';

            searchIndex.push({
                ticker,
                name,
                locations: tickerLocations.get(ticker) || []
            });
        });

        // Sort by ticker
        searchIndex.sort((a, b) => a.ticker.localeCompare(b.ticker));

        // Build page index
        buildPageIndex();

        console.log('[GlobalSearch] Index built with', searchIndex.length, 'unique tickers and', pageIndex.length, 'pages');
    }

    /**
     * Build page index from localStorage
     */
    function buildPageIndex() {
        pageIndex = [];
        try {
            const pagesData = JSON.parse(localStorage.getItem('sandbox_pages') || '{}');
            if (pagesData.names) {
                Object.entries(pagesData.names).forEach(([pageNum, pageName]) => {
                    pageIndex.push({
                        pageNum,
                        pageName,
                        type: 'page'
                    });
                });
            }
        } catch (e) {
            console.warn('[GlobalSearch] Failed to build page index:', e);
        }
    }

    /**
     * Setup search event listeners
     */
    function setupSearchListeners(searchInput, searchResults) {
        let searchTimeout = null;

        // Search on input
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            const rawValue = e.target.value;
            const query = rawValue.trim();
            // Trailing space = exact ticker match
            const exactMatch = rawValue.endsWith(' ') && query.length > 0;

            if (query.length === 0) {
                hideSearchResults(searchResults);
                return;
            }

            // Debounce search
            searchTimeout = setTimeout(() => {
                performSearch(query, searchResults, exactMatch);
            }, 200);
        });

        // Hide results when clicking outside
        document.addEventListener('click', (e) => {
            if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
                hideSearchResults(searchResults);
            }
        });

        // Show results when focusing on input with value
        searchInput.addEventListener('focus', (e) => {
            const rawValue = e.target.value;
            const query = rawValue.trim();
            const exactMatch = rawValue.endsWith(' ') && query.length > 0;
            if (query.length > 0) {
                performSearch(query, searchResults, exactMatch);
            }
        });

        // Handle keyboard navigation
        searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                hideSearchResults(searchResults);
                searchInput.blur();
            }
        });
    }

    /**
     * Perform search and display results
     */
    function performSearch(query, searchResults, exactMatch = false) {
        query = query.trim();
        const queryUpper = query.toUpperCase();
        const queryLower = query.toLowerCase();

        // Search pages (not affected by exact match)
        const pageResults = exactMatch ? [] : pageIndex.filter(item => {
            return item.pageName.toLowerCase().includes(queryLower);
        }).slice(0, 10);

        // Search ticker and name
        let tickerResults;
        if (exactMatch) {
            // Trailing space = exact ticker match only
            tickerResults = searchIndex.filter(item =>
                item.ticker.toUpperCase() === queryUpper
            );
        } else {
            // Normal contains match
            tickerResults = searchIndex.filter(item => {
                const tickerMatch = item.ticker.toUpperCase().includes(queryUpper);
                const nameMatch = item.name.toLowerCase().includes(queryLower);
                return tickerMatch || nameMatch;
            });
        }

        tickerResults.sort((a, b) => {
            const aTicker = a.ticker.toUpperCase();
            const bTicker = b.ticker.toUpperCase();
            const score = (item, ticker) => {
                if (ticker === queryUpper) return 0;
                if (ticker.startsWith(queryUpper)) return 1;
                if (item.locations.length > 0) return 2;
                return 3;
            };
            const aScore = score(a, aTicker);
            const bScore = score(b, bTicker);
            if (aScore !== bScore) return aScore - bScore;
            return a.ticker.localeCompare(b.ticker);
        });

        // Limit to top 40 ticker results (leave room for pages)
        const limitedTickerResults = tickerResults.slice(0, 40);

        displaySearchResults(pageResults, limitedTickerResults, searchResults);
    }

    /**
     * Display search results
     */
    function displaySearchResults(pageResults, tickerResults, searchResults) {
        searchResults.innerHTML = '';

        if (pageResults.length === 0 && tickerResults.length === 0) {
            searchResults.innerHTML = '<div class="search-no-results">No results found</div>';
            searchResults.classList.add('show');
            return;
        }

        // Display page results first
        if (pageResults.length > 0) {
            const pageHeader = document.createElement('div');
            pageHeader.style.cssText = 'padding: 6px 12px; font-size: 0.75rem; color: #888; text-transform: uppercase; background: #1e222d; border-bottom: 1px solid #2a2e39;';
            pageHeader.textContent = 'Pages';
            searchResults.appendChild(pageHeader);

            pageResults.forEach(item => {
                const resultItem = document.createElement('div');
                resultItem.className = 'search-result-item';

                const pageIcon = document.createElement('span');
                pageIcon.textContent = '📄 ';
                pageIcon.style.marginRight = '4px';

                const nameSpan = document.createElement('span');
                nameSpan.className = 'search-result-ticker';
                nameSpan.textContent = item.pageName;

                resultItem.appendChild(pageIcon);
                resultItem.appendChild(nameSpan);

                // Click handler - navigate to page
                resultItem.addEventListener('click', () => {
                    if (window.PageManager && typeof window.PageManager.showPage === 'function') {
                        window.PageManager.showPage(parseInt(item.pageNum, 10));
                    }
                    hideSearchResults(searchResults);
                    document.getElementById('global-search-input').value = '';
                });

                searchResults.appendChild(resultItem);
            });
        }

        // Display ticker results
        if (tickerResults.length > 0) {
            const tickerHeader = document.createElement('div');
            tickerHeader.style.cssText = 'padding: 6px 12px; font-size: 0.75rem; color: #888; text-transform: uppercase; background: #1e222d; border-bottom: 1px solid #2a2e39;';
            tickerHeader.textContent = 'Tickers';
            searchResults.appendChild(tickerHeader);

            tickerResults.forEach(item => {
                const locations = item.locations.length ? item.locations : [null];
                locations.forEach(location => {
                    const resultItem = document.createElement('div');
                    resultItem.className = 'search-result-item';

                    const tickerSpan = document.createElement('span');
                    tickerSpan.className = 'search-result-ticker';
                    tickerSpan.textContent = item.ticker;

                    const nameSpan = document.createElement('span');
                    nameSpan.className = 'search-result-name';
                    nameSpan.textContent = item.name;

                    const locationSpan = document.createElement('span');
                    locationSpan.className = 'search-result-location';

                    if (location) {
                        // Get page name from localStorage
                        let pageName = `Page ${location.page}`;
                        try {
                            const pagesData = JSON.parse(localStorage.getItem('sandbox_pages') || '{}');
                            pageName = pagesData?.names?.[location.page] || `Page ${location.page}`;
                        } catch (e) {
                            // Fallback to Page N
                        }
                        locationSpan.textContent = `${pageName}: ${location.title}`;
                    } else {
                        locationSpan.textContent = 'Add to active chart';
                    }

                    resultItem.appendChild(tickerSpan);
                    if (item.name) {
                        resultItem.appendChild(nameSpan);
                    }
                    resultItem.appendChild(locationSpan);

                    // Click handler - navigate to chart
                    resultItem.addEventListener('click', () => {
                        if (location) {
                            navigateToChart(location.page, location.pageCardIndex, location.cardIndex);
                        } else {
                            addTickerToActiveChart(item.ticker);
                        }
                        hideSearchResults(searchResults);
                        document.getElementById('global-search-input').value = '';
                    });

                    searchResults.appendChild(resultItem);
                });
            });
        }

        searchResults.classList.add('show');
    }

    /**
     * Hide search results
     */
    function hideSearchResults(searchResults) {
        searchResults.classList.remove('show');
    }

    /**
     * Navigate to specific chart
     */
    function navigateToChart(page, pageCardIndex, fallbackCardIndex) {
        console.log('[GlobalSearch] Navigating to page', page, 'card', pageCardIndex);

        // Switch to the page
        if (window.PageManager && typeof window.PageManager.showPage === 'function') {
            window.PageManager.showPage(parseInt(page, 10));
        } else if (window.PageManager && typeof window.PageManager.switchToPage === 'function') {
            window.PageManager.switchToPage(page);
        }

        // Wait for page to render, then scroll to chart
        setTimeout(() => {
            const pageEl = document.querySelector(`.page[data-page="${page}"]`);
            const pageCards = pageEl ? pageEl.querySelectorAll('.chart-card') : [];
            const allCards = document.querySelectorAll('.chart-card');
            const card = pageCards[pageCardIndex] || allCards[fallbackCardIndex];

            if (card) {
                card.scrollIntoView({ behavior: 'smooth', block: 'start' });
                // Briefly highlight the card
                card.style.boxShadow = '0 0 0 3px #007bff';
                setTimeout(() => {
                    card.style.boxShadow = '';
                }, 2000);
            }
        }, 300);
    }

    /**
     * Add an available ticker to the first visible chart, creating one if needed.
     */
    function addTickerToActiveChart(ticker) {
        let card = Array.from(document.querySelectorAll('.chart-card'))
            .find(candidate => {
                const page = candidate.closest('.page');
                return !page || page.style.display !== 'none';
            });

        if (!card && typeof window.createChartCard === 'function') {
            let wrapperEl = null;
            if (window.PageManager && typeof window.PageManager.getActivePage === 'function' &&
                typeof window.PageManager.ensurePage === 'function') {
                wrapperEl = window.PageManager.ensurePage(window.PageManager.getActivePage());
            }
            card = window.createChartCard({ tickers: ticker, wrapperEl });
        } else if (card) {
            const input = card.querySelector('.ticker-input');
            const addBtn = card.querySelector('.add-ticker-btn');
            if (input && addBtn) {
                input.value = ticker;
                addBtn.click();
            }
        }

        if (card) {
            const plotBtn = card.querySelector('.plot-btn');
            if (plotBtn) plotBtn.click();
            card.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    // Expose functions globally
    window.GlobalSearch = {
        init: initGlobalSearch,
        rebuild: buildSearchIndex
    };

    // Initialize when DOM is ready - but wait a bit for workspace to load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            setTimeout(initGlobalSearch, 1000);
        });
    } else {
        setTimeout(initGlobalSearch, 1000);
    }

    // Re-build index when workspace changes
    window.addEventListener('workspace-updated', () => {
        buildSearchIndex();
    });

})();
