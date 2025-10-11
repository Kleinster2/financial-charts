/**
 * Chart Event Handlers Module
 * Centralizes event binding for chart cards
 */

window.ChartEventHandlers = {
    /**
     * Bind all toggle button events
     */
    bindToggleButtons(card, elements, state, callbacks) {
        const {
            toggleDiffBtn, toggleVolBtn, toggleVolumeBtn, toggleRawBtn,
            toggleAvgBtn, toggleLastLabelBtn, toggleZeroLineBtn, toggleFixedLegendBtn
        } = elements;

        const {
            onToggleDiff, onToggleVol, onToggleVolume, onToggleRaw,
            onToggleAvg, onToggleLastLabel, onToggleZeroLine, onToggleFixedLegend
        } = callbacks;

        // Toggle Diff Pane
        if (toggleDiffBtn && onToggleDiff) {
            toggleDiffBtn.addEventListener('click', onToggleDiff);
        }

        // Toggle Volatility Pane
        if (toggleVolBtn && onToggleVol) {
            toggleVolBtn.addEventListener('click', onToggleVol);
        }

        // Toggle Volume Pane
        if (toggleVolumeBtn && onToggleVolume) {
            toggleVolumeBtn.addEventListener('click', onToggleVolume);
        }

        // Toggle Raw/Percentage Mode
        if (toggleRawBtn && onToggleRaw) {
            toggleRawBtn.addEventListener('click', onToggleRaw);
        }

        // Toggle Average Series
        if (toggleAvgBtn && onToggleAvg) {
            toggleAvgBtn.addEventListener('click', onToggleAvg);
        }

        // Toggle Last Label Visibility
        if (toggleLastLabelBtn && onToggleLastLabel) {
            toggleLastLabelBtn.addEventListener('click', onToggleLastLabel);
        }

        // Toggle Zero Line
        if (toggleZeroLineBtn && onToggleZeroLine) {
            toggleZeroLineBtn.addEventListener('click', onToggleZeroLine);
        }

        // Toggle Fixed Legend
        if (toggleFixedLegendBtn && onToggleFixedLegend) {
            toggleFixedLegendBtn.addEventListener('click', onToggleFixedLegend);
        }
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
     * Bind all events at once
     */
    bindAll(card, elements, callbacks) {
        this.bindToggleButtons(card, elements, null, callbacks);
        this.bindSizeControls(card, elements, callbacks);
        this.bindTickerControls(card, elements, callbacks);
        this.bindCardControls(card, elements, callbacks);
    }
};
