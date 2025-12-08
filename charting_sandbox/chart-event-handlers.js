/**
 * Chart Event Handlers Module
 * Centralizes event binding for chart cards
 */

window.ChartEventHandlers = {
    /**
     * Bind toggle button events using a handlers dictionary.
     * @param {Object} elements - DOM elements containing toggle buttons
     * @param {Object} handlers - Dictionary mapping handler names to callbacks:
     *   { diff, vol, volume, revenue, fundamentalsPane, raw, avg,
     *     lastLabel, lastTicker, zeroLine, fixedLegend, legendTickers, notes, reshuffleColors }
     */
    bindToggleButtons(elements, handlers) {
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
            reshuffleColorsBtn: 'reshuffleColors'
        };

        // Bind each button to its handler
        Object.entries(buttonMap).forEach(([btnKey, handlerKey]) => {
            const btn = elements[btnKey];
            const handler = handlers[handlerKey];
            if (btn && handler) {
                btn.addEventListener('click', handler);
            }
        });
    },

    /**
     * Bind metric toggle buttons (revenue, netincome, eps, fcf)
     * @param {Object} elements - DOM elements containing metric buttons
     * @param {Function} toggleMetric - Function that takes metric name and toggles it
     */
    bindMetricToggles(elements, toggleMetric) {
        const metricMap = {
            toggleRevenueMetricBtn: 'revenue',
            toggleNetIncomeMetricBtn: 'netincome',
            toggleEpsMetricBtn: 'eps',
            toggleFcfMetricBtn: 'fcf'
        };

        Object.entries(metricMap).forEach(([btnKey, metricName]) => {
            const btn = elements[btnKey];
            if (btn) {
                btn.addEventListener('click', () => toggleMetric(metricName));
            }
        });
    },

    /**
     * Bind height and font control events
     */
    bindSizeControls(card, elements, callbacks) {
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

        // Height controls
        if (heightUpBtn && onHeightUp) {
            heightUpBtn.addEventListener('click', onHeightUp);
        }
        if (heightDownBtn && onHeightDown) {
            heightDownBtn.addEventListener('click', onHeightDown);
        }

        // Volume pane height controls
        if (volPaneHeightUpBtn && onVolPaneHeightUp) {
            volPaneHeightUpBtn.addEventListener('click', onVolPaneHeightUp);
        }
        if (volPaneHeightDownBtn && onVolPaneHeightDown) {
            volPaneHeightDownBtn.addEventListener('click', onVolPaneHeightDown);
        }

        // Font size controls
        if (fontUpBtn && onFontUp) {
            fontUpBtn.addEventListener('click', onFontUp);
        }
        if (fontDownBtn && onFontDown) {
            fontDownBtn.addEventListener('click', onFontDown);
        }
    },

    /**
     * Bind ticker control events
     */
    bindTickerControls(card, elements, callbacks) {
        const { tickerInput, addBtn, plotBtn, fitBtn, rangeSelect } = elements;
        const { onAddTicker, onPlot, onFit, onRangeChange } = callbacks;

        // Add ticker
        if (addBtn && onAddTicker) {
            addBtn.addEventListener('click', onAddTicker);
        }
        if (tickerInput && onAddTicker) {
            tickerInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') onAddTicker();
            });
        }

        // Plot button
        if (plotBtn && onPlot) {
            plotBtn.addEventListener('click', onPlot);
        }

        // Fit button
        if (fitBtn && onFit) {
            fitBtn.addEventListener('click', onFit);
        }

        // Range selector
        if (rangeSelect && onRangeChange) {
            rangeSelect.addEventListener('change', onRangeChange);
        }
    },

    /**
     * Bind card management events
     */
    bindCardControls(card, elements, callbacks) {
        const { titleInput, addChartBtn, removeCardBtn } = elements;
        const { onTitleChange, onAddChart, onRemoveCard } = callbacks;

        // Title input
        if (titleInput && onTitleChange) {
            titleInput.addEventListener('input', onTitleChange);
        }

        // Add chart button
        if (addChartBtn && onAddChart) {
            addChartBtn.addEventListener('click', onAddChart);
        }

        // Remove card button
        if (removeCardBtn && onRemoveCard) {
            removeCardBtn.addEventListener('click', onRemoveCard);
        }
    },

    /**
     * Bind all events at once (legacy signature for backward compatibility)
     */
    bindAll(card, elements, callbacks) {
        // Convert old callback format to new handlers format if needed
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
        this.bindSizeControls(card, elements, callbacks);
        this.bindTickerControls(card, elements, callbacks);
        this.bindCardControls(card, elements, callbacks);
    }
};
