/**
 * Chart Event Handlers Module
 * Centralizes event binding for chart cards with cleanup support
 */

window.ChartEventHandlers = {
    /**
     * Create a listener tracker for cleanup
     * @returns {Object} { add, unbindAll }
     */
    createListenerTracker() {
        const listeners = [];
        return {
            add(el, type, fn, opts = false) {
                if (!el) return;
                el.addEventListener(type, fn, opts);
                listeners.push({ el, type, fn, opts });
            },
            unbindAll() {
                listeners.forEach(({ el, type, fn, opts }) => {
                    try { el.removeEventListener(type, fn, opts); } catch (_) {}
                });
                listeners.length = 0;
            },
            getCount() {
                return listeners.length;
            }
        };
    },

    /**
     * Bind toggle button events using a handlers dictionary.
     * @param {Object} elements - DOM elements containing toggle buttons
     * @param {Object} handlers - Dictionary mapping handler names to callbacks
     * @param {Object} [tracker] - Optional listener tracker from createListenerTracker()
     */
    bindToggleButtons(elements, handlers, tracker = null) {
        const add = tracker ? tracker.add.bind(tracker) : (el, type, fn) => el?.addEventListener(type, fn);

        // Map of button element keys to handler keys
        const buttonMap = {
            toggleDiffBtn: 'diff',
            toggleVolBtn: 'vol',
            toggleVolumeBtn: 'volume',
            toggleRevenueBtn: 'revenue',
            toggleFundamentalsPaneBtn: 'fundamentalsPane',
            toggleRawBtn: 'raw',
            toggleAvgBtn: 'avg',
            toggleLastLabelBtn: 'lastLabel',
            toggleLastTickerBtn: 'lastTicker',
            toggleZeroLineBtn: 'zeroLine',
            toggleFixedLegendBtn: 'fixedLegend',
            toggleLegendTickersBtn: 'legendTickers',
            toggleNotesBtn: 'notes',
            reshuffleColorsBtn: 'reshuffleColors',
            toggleLogScaleBtn: 'logScale'
        };

        // Bind each button to its handler
        Object.entries(buttonMap).forEach(([btnKey, handlerKey]) => {
            const btn = elements[btnKey];
            const handler = handlers[handlerKey];
            if (btn && handler) {
                add(btn, 'click', handler);
            }
        });
    },

    /**
     * Bind metric toggle buttons (revenue, netincome, eps, fcf)
     * @param {Object} elements - DOM elements containing metric buttons
     * @param {Function} toggleMetric - Function that takes metric name and toggles it
     * @param {Object} [tracker] - Optional listener tracker
     */
    bindMetricToggles(elements, toggleMetric, tracker = null) {
        const add = tracker ? tracker.add.bind(tracker) : (el, type, fn) => el?.addEventListener(type, fn);

        const metricMap = {
            toggleRevenueMetricBtn: 'revenue',
            toggleNetIncomeMetricBtn: 'netincome',
            toggleEpsMetricBtn: 'eps',
            toggleFcfMetricBtn: 'fcf'
        };

        Object.entries(metricMap).forEach(([btnKey, metricName]) => {
            const btn = elements[btnKey];
            if (btn) {
                add(btn, 'click', () => toggleMetric(metricName));
            }
        });
    },

    /**
     * Bind height and font control events
     * @param {Object} elements - DOM elements
     * @param {Object} callbacks - Handler callbacks
     * @param {Object} [tracker] - Optional listener tracker
     */
    bindSizeControls(elements, callbacks, tracker = null) {
        const add = tracker ? tracker.add.bind(tracker) : (el, type, fn) => el?.addEventListener(type, fn);

        const {
            heightUpBtn, heightDownBtn,
            volPaneHeightUpBtn, volPaneHeightDownBtn,
            fontUpBtn, fontDownBtn
        } = elements;

        const {
            onHeightUp, onHeightDown,
            onVolPaneHeightUp, onVolPaneHeightDown,
            onFontUp, onFontDown
        } = callbacks;

        if (heightUpBtn && onHeightUp) add(heightUpBtn, 'click', onHeightUp);
        if (heightDownBtn && onHeightDown) add(heightDownBtn, 'click', onHeightDown);
        if (volPaneHeightUpBtn && onVolPaneHeightUp) add(volPaneHeightUpBtn, 'click', onVolPaneHeightUp);
        if (volPaneHeightDownBtn && onVolPaneHeightDown) add(volPaneHeightDownBtn, 'click', onVolPaneHeightDown);
        if (fontUpBtn && onFontUp) add(fontUpBtn, 'click', onFontUp);
        if (fontDownBtn && onFontDown) add(fontDownBtn, 'click', onFontDown);
    },

    /**
     * Bind ticker control events
     * @param {Object} elements - DOM elements
     * @param {Object} callbacks - Handler callbacks
     * @param {Object} [tracker] - Optional listener tracker
     */
    bindTickerControls(elements, callbacks, tracker = null) {
        const add = tracker ? tracker.add.bind(tracker) : (el, type, fn) => el?.addEventListener(type, fn);

        const { tickerInput, addBtn, plotBtn, fitBtn, rangeSelect, intervalSelect } = elements;
        const { onAddTicker, onPlot, onFit, onRangeChange, onIntervalChange } = callbacks;

        if (addBtn && onAddTicker) add(addBtn, 'click', onAddTicker);
        if (tickerInput && onAddTicker) {
            add(tickerInput, 'keypress', (e) => { if (e.key === 'Enter') onAddTicker(); });
        }
        if (plotBtn && onPlot) add(plotBtn, 'click', onPlot);
        if (fitBtn && onFit) add(fitBtn, 'click', onFit);
        if (rangeSelect && onRangeChange) add(rangeSelect, 'change', onRangeChange);
        if (intervalSelect && onIntervalChange) add(intervalSelect, 'change', onIntervalChange);
    },

    /**
     * Bind card management events
     * @param {Object} elements - DOM elements
     * @param {Object} callbacks - Handler callbacks
     * @param {Object} [tracker] - Optional listener tracker
     */
    bindCardControls(elements, callbacks, tracker = null) {
        const add = tracker ? tracker.add.bind(tracker) : (el, type, fn) => el?.addEventListener(type, fn);

        const { titleInput, addChartBtn, removeCardBtn, starBtn, notesTextarea, exportBtn } = elements;
        const { onTitleChange, onAddChart, onRemoveCard, onToggleStar, onNotesInput, onExport } = callbacks;

        if (titleInput && onTitleChange) add(titleInput, 'input', onTitleChange);
        if (addChartBtn && onAddChart) add(addChartBtn, 'click', onAddChart);
        if (removeCardBtn && onRemoveCard) add(removeCardBtn, 'click', onRemoveCard);
        if (starBtn && onToggleStar) add(starBtn, 'click', onToggleStar);
        if (notesTextarea && onNotesInput) add(notesTextarea, 'input', onNotesInput);
        if (exportBtn && onExport) add(exportBtn, 'click', onExport);
    },

    /**
     * Bind show fundamentals modal button
     * @param {HTMLElement} card - Card element
     * @param {Function} handler - Click handler
     * @param {Object} [tracker] - Optional listener tracker
     */
    bindShowFundamentals(card, handler, tracker = null) {
        const add = tracker ? tracker.add.bind(tracker) : (el, type, fn) => el?.addEventListener(type, fn);
        const btn = card.querySelector('.show-fundamentals-btn');
        if (btn && handler) add(btn, 'click', handler);
    },

    /**
     * Bind all card events with cleanup support
     * @param {HTMLElement} card - Card element
     * @param {Object} elements - DOM elements from ChartDomBuilder
     * @param {Object} handlers - All handler callbacks organized by category
     * @returns {Function} unbind - Call to remove all listeners
     */
    bindAllWithCleanup(card, elements, handlers) {
        const tracker = this.createListenerTracker();

        // Toggle buttons (diff, vol, volume, revenue, raw, avg, etc.)
        if (handlers.toggles) {
            this.bindToggleButtons(elements, handlers.toggles, tracker);
        }

        // Metric toggles (revenue, netincome, eps, fcf)
        if (handlers.toggleMetric) {
            this.bindMetricToggles(elements, handlers.toggleMetric, tracker);
        }

        // Size controls (height, font)
        if (handlers.size) {
            this.bindSizeControls(elements, handlers.size, tracker);
        }

        // Ticker controls (add, plot, fit, range, interval)
        if (handlers.ticker) {
            this.bindTickerControls(elements, handlers.ticker, tracker);
        }

        // Card controls (title, add/remove, star, notes, export)
        if (handlers.card) {
            this.bindCardControls(elements, handlers.card, tracker);
        }

        // Show fundamentals modal
        if (handlers.showFundamentals) {
            this.bindShowFundamentals(card, handlers.showFundamentals, tracker);
        }

        console.log(`[EventHandlers] Bound ${tracker.getCount()} listeners`);

        return tracker.unbindAll.bind(tracker);
    },

    /**
     * Bind all events at once (legacy signature for backward compatibility)
     */
    bindAll(card, elements, callbacks) {
        const handlers = callbacks.toggleHandlers || {
            diff: callbacks.onToggleDiff,
            vol: callbacks.onToggleVol,
            volume: callbacks.onToggleVolume,
            raw: callbacks.onToggleRaw,
            avg: callbacks.onToggleAvg,
            lastLabel: callbacks.onToggleLastLabel,
            zeroLine: callbacks.onToggleZeroLine,
            fixedLegend: callbacks.onToggleFixedLegend
        };
        this.bindToggleButtons(elements, handlers);
        this.bindSizeControls(elements, callbacks);
        this.bindTickerControls(elements, callbacks);
        this.bindCardControls(elements, callbacks);
    }
};
