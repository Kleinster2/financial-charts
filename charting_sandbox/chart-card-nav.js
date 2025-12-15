/**
 * Chart Card Nav - Navigation link management for chart cards
 *
 * Handles creation, update, and removal of navigation links in the chart-nav sidebar.
 */
window.ChartCardNav = {
    /**
     * Compute nav label from title, tickers, or cardId fallback
     * @param {string} title - Card title
     * @param {string|Array|Set} tickers - Ticker string, Array, or Set
     * @param {string} cardId - Card ID fallback
     * @returns {string} - Label to display
     */
    computeLabel(title, tickers, cardId) {
        const trimmedTitle = (title ?? '').toString().trim();
        if (trimmedTitle) return trimmedTitle;

        // Get first ticker
        let firstTicker = '';
        if (tickers instanceof Set) {
            firstTicker = tickers.size ? tickers.values().next().value : '';
        } else if (Array.isArray(tickers)) {
            firstTicker = tickers.find(t => (t ?? '').toString().trim()) || '';
        } else if (typeof tickers === 'string') {
            firstTicker = tickers.split(/[,\s]+/).filter(Boolean)[0] || '';
        }

        firstTicker = (firstTicker ?? '').toString().trim();

        return firstTicker || cardId;
    },

    /**
     * Create a navigation link for a card
     * @param {string} cardId - Card DOM ID
     * @param {string} initialTitle - Initial title (may be empty)
     * @param {string} initialTickers - Initial tickers string
     * @param {string|number} targetPage - Page number for data attribute
     * @returns {HTMLAnchorElement|null} - Created nav link or null if nav container not found
     */
    createNavLink(cardId, initialTitle, initialTickers, targetPage) {
        const nav = document.getElementById('chart-nav');
        if (!nav) return null;

        const label = this.computeLabel(initialTitle, initialTickers, cardId);

        const navLink = document.createElement('a');
        navLink.href = `#${cardId}`;
        navLink.textContent = label;
        navLink.dataset.page = targetPage;

        // Add click handler to switch pages and scroll to chart
        navLink.addEventListener('click', (e) => {
            e.preventDefault();

            const targetCard = document.getElementById(cardId);
            if (!targetCard) {
                console.warn(`[ChartCardNav] Card ${cardId} not found`);
                return;
            }

            const pageEl = targetCard.closest('.page');
            if (!pageEl) {
                console.warn(`[ChartCardNav] No page found for card ${cardId}`);
                return;
            }

            const pageNum = pageEl.dataset.page;

            if (window.PageManager && window.PageManager.showPage) {
                window.PageManager.showPage(parseInt(pageNum, 10));
            }

            setTimeout(() => {
                targetCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        });

        nav.appendChild(navLink);
        return navLink;
    },

    /**
     * Update nav link text based on title/tickers/cardId
     * @param {HTMLAnchorElement} navLink - Nav link element
     * @param {string} title - Current title
     * @param {string|Set} tickers - Current tickers
     * @param {string} cardId - Card ID fallback
     */
    updateNavLabel(navLink, title, tickers, cardId) {
        if (!navLink) return;
        navLink.textContent = this.computeLabel(title, tickers, cardId);
    },

    /**
     * Remove nav link from DOM
     * @param {HTMLAnchorElement} navLink - Nav link to remove
     */
    removeNavLink(navLink) {
        if (navLink && navLink.parentElement) {
            navLink.parentElement.removeChild(navLink);
        }
    }
};

console.log('[ChartCardNav] Nav link module loaded');
