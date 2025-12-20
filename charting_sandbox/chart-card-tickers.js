/**
 * Chart Card Tickers Module
 *
 * Handles ticker/chip management: add, remove, axis assignment, context menu.
 * Extracted from card.js to keep orchestration separate from ticker logic.
 *
 * Exports: window.ChartCardTickers
 */

window.ChartCardTickers = (() => {
    let globalMenuInitialized = false;

    /**
     * Initialize global chip context menu (idempotent - only binds once)
     * Handles right-click on chips to show axis/hide options
     */
    function initGlobalChipContextMenu() {
        if (globalMenuInitialized) return;
        globalMenuInitialized = true;

        // Hide menu on any click
        document.addEventListener('click', () => {
            const menu = document.getElementById('chip-context-menu');
            if (menu) menu.classList.remove('visible');
        });

        // Menu item click handler
        const setupMenuHandler = () => {
            const menu = document.getElementById('chip-context-menu');
            if (!menu) return;

            menu.addEventListener('click', (e) => {
                const item = e.target.closest('.chip-context-menu-item');
                if (!item) return;

                const action = item.dataset.action;
                const chip = menu._targetChip;
                const ticker = menu._targetTicker;

                if (!chip || !ticker) return;

                if (action === 'axis-left' || action === 'axis-right') {
                    const newAxis = action === 'axis-left' ? 'left' : 'right';
                    chip._currentAxis = newAxis;
                    if (chip._axisIndicator) {
                        chip._axisIndicator.textContent = newAxis === 'left' ? 'L' : '';
                    }
                    if (typeof chip._onAxisChange === 'function') {
                        chip._onAxisChange(ticker, newAxis);
                    }
                } else if (action === 'hide') {
                    // Toggle hidden state via chip click
                    chip.click();
                }

                menu.classList.remove('visible');
            });
        };

        // Set up handler when DOM is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', setupMenuHandler);
        } else {
            setupMenuHandler();
        }
    }

    /**
     * Create ticker management handlers for a card
     * @param {Object} ctx - Card context
     * @param {Object} callbacks - Callback functions
     * @param {Function} callbacks.plot - Plot function
     * @returns {Object} Ticker handler functions
     */
    function createHandlers(ctx, callbacks) {
        const { plot } = callbacks;
        const rt = ctx.runtime;

        /**
         * Get the axis assignment for a ticker
         * @param {string} ticker
         * @returns {string} 'left' or 'right'
         */
        function getAxis(ticker) {
            return ctx.priceScaleAssignmentMap.get(ticker) || 'right';
        }

        /**
         * Handle axis change for a ticker
         * @param {string} ticker
         * @param {string} axis - 'left' or 'right'
         */
        function onAxisChange(ticker, axis) {
            ctx.priceScaleAssignmentMap.set(ticker, axis);
            window.ChartCardContext.syncToCard(ctx);
            ctx.saveCards();

            // Update existing series if chart exists
            if (rt.chart && rt.priceSeriesMap.has(ticker)) {
                const series = rt.priceSeriesMap.get(ticker);
                try {
                    series.applyOptions({ priceScaleId: axis });
                } catch (e) {
                    console.warn('[Tickers] Could not update series axis, replotting:', e);
                    plot();
                }
            }
        }

        /**
         * Remove a ticker and clean up all associated series/state
         * @param {string} ticker
         * @param {HTMLElement} chipEl - The chip element to remove
         */
        function handleChipRemove(ticker, chipEl) {
            const { selectedTickers, hiddenTickers, multiplierMap, tickerColorMap } = ctx;
            const { priceSeriesMap, rawPriceMap, latestRebasedData, volSeriesMap } = rt;

            try {
                if (!selectedTickers.has(ticker)) {
                    if (chipEl && chipEl.parentElement) chipEl.parentElement.removeChild(chipEl);
                    return;
                }

                // Remove from all state collections
                selectedTickers.delete(ticker);
                hiddenTickers.delete(ticker);
                multiplierMap.delete(ticker);
                tickerColorMap.delete(ticker);
                rawPriceMap.delete(ticker);
                try { delete latestRebasedData[ticker]; } catch (_) { }

                // Remove price series
                const s = priceSeriesMap.get(ticker);
                if (s && rt.chart) {
                    try { rt.chart.removeSeries(s); } catch (_) { }
                }
                priceSeriesMap.delete(ticker);

                // Remove volume series (if present)
                if (volSeriesMap && rt.chart) {
                    const vs = volSeriesMap.get(ticker);
                    if (vs) {
                        try { rt.chart.removeSeries(vs); } catch (_) { }
                        volSeriesMap.delete(ticker);
                    }
                    // If no volume series remain, remove the pane
                    if (rt.volPane && volSeriesMap.size === 0) {
                        try {
                            rt.volPane = window.ChartVolumeManager.clearVolumeSeries(rt.chart, rt.volPane, volSeriesMap);
                        } catch (_) { }
                    }
                }

                // Update average series
                if (ctx.showAvg && !ctx.useRaw) {
                    try {
                        rt.avgSeries = window.ChartSeriesManager.updateAverageSeries(
                            rt.chart, rt.avgSeries, priceSeriesMap, hiddenTickers, undefined, ctx.lastLabelVisible
                        );
                    } catch (_) { }
                }

                // Remove ticker label
                if (rt.tickerLabelsContainer) {
                    window.ChartTickerLabels.removeLabel(rt.tickerLabelsContainer, ticker);
                }

                // Remove chip element
                if (chipEl && chipEl.parentElement) chipEl.parentElement.removeChild(chipEl);

                // Update nav label if title empty
                const { titleInput } = ctx.elements;
                const title = titleInput ? titleInput.value : '';
                window.ChartCardNav.updateNavLabel(ctx.card?._navLink, title, selectedTickers, ctx.cardId);

                ctx.saveCards();
            } catch (e) {
                console.warn('[ChartCardTickers] handleChipRemove failed:', e);
            }
        }

        /**
         * Add ticker(s) from input field
         * Supports comma/space separated lists: "AAPL, MSFT, GOOG" or "AAPL MSFT GOOG"
         */
        function addTickerFromInput() {
            const { tickerInput } = ctx.elements;
            const tickers = window.ChartDomBuilder.parseTickerInput(tickerInput.value);
            if (!tickers.length) return;

            // Filter out already-selected tickers
            let newTickers = tickers.filter(t => !ctx.selectedTickers.has(t));
            if (!newTickers.length) {
                tickerInput.value = '';
                return;
            }

            // Enforce max tickers per chart
            const maxTickers = window.ChartConfig?.UI?.MAX_TICKERS_PER_CHART || 30;
            const currentCount = ctx.selectedTickers.size;
            const availableSlots = maxTickers - currentCount;

            if (availableSlots <= 0) {
                if (window.Toast?.warning) {
                    window.Toast.warning(`Chart already has maximum ${maxTickers} tickers`);
                }
                tickerInput.value = '';
                return;
            }

            if (newTickers.length > availableSlots) {
                const skipped = newTickers.length - availableSlots;
                newTickers = newTickers.slice(0, availableSlots);
                if (window.Toast?.warning) {
                    window.Toast.warning(`Added ${availableSlots} tickers, skipped ${skipped} (max ${maxTickers})`);
                }
            }

            // Batch add all new tickers
            newTickers.forEach(ticker => {
                ctx.selectedTickers.add(ticker);
                if (!ctx.tickerColorMap.has(ticker)) {
                    ctx.tickerColorMap.set(ticker, window.ChartConfig.getTickerColor(ticker));
                }
            });

            renderChips();
            tickerInput.value = '';
            ctx.saveCards(); // Single save after all tickers added
        }

        /**
         * Initialize tickers from initial string/array
         * @param {string|Array} initialTickers
         */
        function initializeTickers(initialTickers) {
            if (!initialTickers) return;

            const tickers = window.ChartDomBuilder.parseTickerInput(initialTickers);
            tickers.forEach(t => ctx.selectedTickers.add(t));

            // Assign consistent hash-based colors
            ctx.selectedTickers.forEach(ticker => {
                if (!ctx.tickerColorMap.has(ticker)) {
                    ctx.tickerColorMap.set(ticker, window.ChartConfig.getTickerColor(ticker));
                }
            });

            renderChips();
        }

        /**
         * Render all ticker chips with current state
         */
        function renderChips() {
            const { selectedTickersDiv } = ctx.elements;
            if (!selectedTickersDiv) return;

            window.ChartDomBuilder.addTickerChips(
                selectedTickersDiv,
                ctx.selectedTickers,
                ctx.tickerColorMap,
                ctx.multiplierMap,
                ctx.hiddenTickers,
                handleChipRemove,
                getAxis,
                onAxisChange
            );
        }

        /**
         * Bind chip toggle and multiplier interactions
         * Wraps CardEventBinder.bindTickerInteractions with ctx
         */
        function bindChipInteractions() {
            const { selectedTickersDiv } = ctx.elements;
            if (!selectedTickersDiv) return;

            window.CardEventBinder.bindTickerInteractions(
                selectedTickersDiv,
                ctx.hiddenTickers,
                ctx.multiplierMap,
                () => window.ChartCardContext.syncToCard(ctx),
                plot,
                ctx.saveCards,
                () => ctx.useRaw
            );
        }

        return {
            getAxis,
            onAxisChange,
            handleChipRemove,
            addTickerFromInput,
            initializeTickers,
            renderChips,
            bindChipInteractions
        };
    }

    return {
        initGlobalChipContextMenu,
        createHandlers
    };

})();
