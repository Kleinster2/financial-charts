/**
 * chart-fundamentals.js
 * Display fundamental data (earnings, financials) for chart tickers
 */

(function() {
    'use strict';

    /**
     * Format large numbers with abbreviations (K, M, B, T)
     */
    function formatNumber(value) {
        if (value === null || value === undefined || value === 0) return 'N/A';

        const absValue = Math.abs(value);
        if (absValue >= 1e12) return (value / 1e12).toFixed(2) + 'T';
        if (absValue >= 1e9) return (value / 1e9).toFixed(2) + 'B';
        if (absValue >= 1e6) return (value / 1e6).toFixed(2) + 'M';
        if (absValue >= 1e3) return (value / 1e3).toFixed(2) + 'K';
        return value.toFixed(2);
    }

    /**
     * Format percentage
     */
    function formatPercent(value) {
        if (value === null || value === undefined || value === 0) return 'N/A';
        return (value * 100).toFixed(2) + '%';
    }

    /**
     * Format ratio
     */
    function formatRatio(value) {
        if (value === null || value === undefined || value === 0) return 'N/A';
        return value.toFixed(2);
    }

    /**
     * Format date from YYYY-MM-DD
     */
    function formatDate(dateStr) {
        if (!dateStr) return 'N/A';
        const date = new Date(dateStr);
        return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
    }

    /**
     * Fetch fundamental overview for a ticker
     */
    async function fetchOverview(ticker) {
        try {
            const response = await fetch(window.ChartUtils.apiUrl(`/api/fundamentals/overview?tickers=${ticker}`));
            if (!response.ok) throw new Error('Failed to fetch overview');
            const data = await response.json();
            return data[ticker];
        } catch (error) {
            console.error(`[Fundamentals] Error fetching overview for ${ticker}:`, error);
            return null;
        }
    }

    /**
     * Fetch earnings data for a ticker
     */
    async function fetchEarnings(ticker, period = 'quarterly') {
        try {
            const response = await fetch(window.ChartUtils.apiUrl(`/api/fundamentals/earnings?tickers=${ticker}&period=${period}`));
            if (!response.ok) throw new Error('Failed to fetch earnings');
            const data = await response.json();
            return data[ticker] || [];
        } catch (error) {
            console.error(`[Fundamentals] Error fetching earnings for ${ticker}:`, error);
            return [];
        }
    }

    /**
     * Create overview metrics section
     */
    function createOverviewSection(overview) {
        if (!overview) return '';

        return `
            <div class="fundamentals-section">
                <div class="fundamentals-section-title">Key Metrics</div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">Market Cap</span>
                    <span class="fundamentals-metric-value">${formatNumber(overview.market_cap)}</span>
                </div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">P/E Ratio</span>
                    <span class="fundamentals-metric-value">${formatRatio(overview.pe_ratio)}</span>
                </div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">EPS (TTM)</span>
                    <span class="fundamentals-metric-value">$${formatRatio(overview.eps)}</span>
                </div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">Dividend Yield</span>
                    <span class="fundamentals-metric-value">${formatPercent(overview.dividend_yield)}</span>
                </div>
            </div>
            <div class="fundamentals-section">
                <div class="fundamentals-section-title">Profitability</div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">Revenue (TTM)</span>
                    <span class="fundamentals-metric-value">${formatNumber(overview.revenue)}</span>
                </div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">Profit Margin</span>
                    <span class="fundamentals-metric-value">${formatPercent(overview.profit_margin)}</span>
                </div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">ROE</span>
                    <span class="fundamentals-metric-value">${formatPercent(overview.return_on_equity)}</span>
                </div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">ROA</span>
                    <span class="fundamentals-metric-value">${formatPercent(overview.return_on_assets)}</span>
                </div>
            </div>
            <div class="fundamentals-section">
                <div class="fundamentals-section-title">Valuation</div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">Forward P/E</span>
                    <span class="fundamentals-metric-value">${formatRatio(overview.forward_pe)}</span>
                </div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">PEG Ratio</span>
                    <span class="fundamentals-metric-value">${formatRatio(overview.peg_ratio)}</span>
                </div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">Price/Sales</span>
                    <span class="fundamentals-metric-value">${formatRatio(overview.price_to_sales)}</span>
                </div>
                <div class="fundamentals-metric">
                    <span class="fundamentals-metric-label">Price/Book</span>
                    <span class="fundamentals-metric-value">${formatRatio(overview.price_to_book)}</span>
                </div>
            </div>
        `;
    }

    /**
     * Create earnings table
     */
    function createEarningsTable(earnings) {
        if (!earnings || earnings.length === 0) {
            return '<div class="fundamentals-error">No earnings data available</div>';
        }

        // Show last 4 quarters
        const recent = earnings.slice(0, 4);

        let rows = '';
        recent.forEach(earning => {
            const surprise = earning.surprise || 0;
            const surpriseClass = surprise >= 0 ? 'positive' : 'negative';
            const surpriseSign = surprise >= 0 ? '+' : '';

            rows += `
                <tr>
                    <td>${formatDate(earning.fiscal_date_ending)}</td>
                    <td>$${formatRatio(earning.reported_eps)}</td>
                    <td>$${formatRatio(earning.estimated_eps)}</td>
                    <td class="${surpriseClass}">${surpriseSign}$${formatRatio(surprise)}</td>
                    <td class="${surpriseClass}">${surpriseSign}${formatPercent(earning.surprise_percentage / 100)}</td>
                </tr>
            `;
        });

        return `
            <table class="fundamentals-earnings-table">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Reported EPS</th>
                        <th>Estimated EPS</th>
                        <th>Surprise ($)</th>
                        <th>Surprise (%)</th>
                    </tr>
                </thead>
                <tbody>
                    ${rows}
                </tbody>
            </table>
        `;
    }

    /**
     * Show fundamentals panel for a chart
     */
    async function showFundamentals(chartCard) {
        // Get first ticker from the chart
        const tickerChips = chartCard.querySelectorAll('.chip');
        if (!tickerChips || tickerChips.length === 0) {
            alert('No tickers found in this chart');
            return;
        }

        const ticker = tickerChips[0].textContent.replace('×', '').trim();
        console.log(`[Fundamentals] Loading data for ${ticker}`);

        // Check if panel already exists
        let panel = chartCard.querySelector('.fundamentals-panel');
        if (!panel) {
            // Create panel
            panel = document.createElement('div');
            panel.className = 'fundamentals-panel';
            chartCard.appendChild(panel);
        }

        // Show loading state
        panel.innerHTML = `
            <div class="fundamentals-header">
                <div class="fundamentals-title">Fundamentals: ${ticker}</div>
                <span class="fundamentals-close">×</span>
            </div>
            <div class="fundamentals-loading">Loading fundamental data...</div>
        `;
        panel.classList.add('show');

        // Setup close button
        panel.querySelector('.fundamentals-close').addEventListener('click', () => {
            panel.classList.remove('show');
        });

        // Fetch data in parallel
        const [overview, earnings] = await Promise.all([
            fetchOverview(ticker),
            fetchEarnings(ticker, 'quarterly')
        ]);

        // Check if we got data
        if (!overview && (!earnings || earnings.length === 0)) {
            panel.innerHTML = `
                <div class="fundamentals-header">
                    <div class="fundamentals-title">Fundamentals: ${ticker}</div>
                    <span class="fundamentals-close">×</span>
                </div>
                <div class="fundamentals-error">
                    No fundamental data available for ${ticker}.<br>
                    Run: <code>python fetch_fundamentals.py ${ticker}</code>
                </div>
            `;
            // Re-setup close button
            panel.querySelector('.fundamentals-close').addEventListener('click', () => {
                panel.classList.remove('show');
            });
            return;
        }

        // Build panel content
        let content = `
            <div class="fundamentals-header">
                <div class="fundamentals-title">Fundamentals: ${ticker}</div>
                <span class="fundamentals-close">×</span>
            </div>
        `;

        // Add overview metrics
        if (overview) {
            content += `<div class="fundamentals-grid">${createOverviewSection(overview)}</div>`;
        }

        // Add earnings table
        if (earnings && earnings.length > 0) {
            content += `
                <div class="fundamentals-earnings">
                    <div class="fundamentals-earnings-title">Recent Quarterly Earnings</div>
                    ${createEarningsTable(earnings)}
                </div>
            `;
        }

        panel.innerHTML = content;

        // Re-setup close button
        panel.querySelector('.fundamentals-close').addEventListener('click', () => {
            panel.classList.remove('show');
        });

        console.log(`[Fundamentals] Data loaded for ${ticker}`);
    }

    /**
     * Hide fundamentals panel for a chart
     */
    function hideFundamentals(chartCard) {
        const panel = chartCard.querySelector('.fundamentals-panel');
        if (panel) {
            panel.classList.remove('show');
        }
    }

    /**
     * Toggle fundamentals panel
     */
    function toggleFundamentals(chartCard) {
        const panel = chartCard.querySelector('.fundamentals-panel');
        if (panel && panel.classList.contains('show')) {
            hideFundamentals(chartCard);
        } else {
            showFundamentals(chartCard);
        }
    }

    // Expose functions globally
    window.ChartFundamentals = {
        show: showFundamentals,
        hide: hideFundamentals,
        toggle: toggleFundamentals
    };

    console.log('[ChartFundamentals] Module loaded');

})();
