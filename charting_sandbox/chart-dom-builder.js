/**
 * Chart DOM Builder
 * Handles creation of chart card DOM elements and controls
 */

window.ChartDomBuilder = {
    /**
     * Create the main chart card element with all controls
     */
    createChartCard(cardId, initialTitle = '', initialHeight = 500) {
        const card = document.createElement('div');
        card.id = cardId;
        card.className = 'chart-card';

        card.innerHTML = `
            <div class="controls">
                <input type="text" class="ticker-input" list="ticker-list" placeholder="e.g. AAPL">
                <button class="add-ticker-btn">Add</button>
                <button class="plot-btn">Plot</button>
                <!-- Range dropdown -->
                <select class="range-select">
                    <option value="">Range</option>
                    <option value="ytd">YTD</option>
                    <option value="2024">2024</option>
                    <option value="2023">2023</option>
                    <option value="2022">2022</option>
                    <option value="2021">2021</option>
                    <option value="2020">2020</option>
                    <option value="2019">2019</option>
                    <option value="2018">2018</option>
                    <option value="2015">2015</option>
                    <option value="2010">2010</option>
                    <option value="2005">2005</option>
                    <option value="2000">2000</option>
                    <option value="1995">All Data (Fit)</option>
                </select>
                <!-- Interval dropdown -->
                <select class="interval-select">
                    <option value="auto">Auto Interval</option>
                    <option value="daily">Daily</option>
                    <option value="weekly">Weekly</option>
                    <option value="monthly">Monthly</option>
                </select>
                <button class="fit-btn">Fit</button>
                <button class="toggle-diff-btn">Show Diff Pane</button>
                <button class="toggle-vol-btn">Hide Vol (σ) Pane</button>
                <button class="toggle-volume-btn">Show Volume Pane</button>
                <button class="toggle-revenue-btn">Show Revenue Pane</button>
                <button class="toggle-fundamentals-pane-btn">Show Fundamentals Pane</button>
                <button class="toggle-revenue-metric-btn" style="display:none;">Revenue</button>
                <button class="toggle-netincome-metric-btn" style="display:none;">Net Income</button>
                <button class="toggle-eps-metric-btn" style="display:none;">EPS</button>
                <button class="toggle-fcf-metric-btn" style="display:none;">FCF</button>
                <button class="show-fundamentals-btn">Show Fundamentals</button>
                <button class="toggle-raw-btn">Show Raw</button>
                <button class="toggle-avg-btn">Show Avg</button>
                <button class="toggle-lastlabel-btn">Hide Last Label</button>
                <button class="toggle-zeroline-btn">Show 0% Line</button>
                <button class="toggle-fixedlegend-btn">Show Fixed Legend</button>
                <button class="height-decrease-btn">Height -</button>
                <button class="height-increase-btn">Height +</button>
                <button class="volpane-height-decrease-btn">Vol Height -</button>
                <button class="volpane-height-increase-btn">Vol Height +</button>
                <label style="display: inline-flex; align-items: center; gap: 6px; margin-left: 8px;">
                    <span style="font-size: 0.9rem;">Font:</span>
                    <input type="range" class="font-slider" min="8" max="24" value="12" step="1" style="width: 80px; vertical-align: middle;">
                    <span class="font-value" style="display: inline-block; min-width: 28px; font-size: 0.9rem; font-weight: bold;">12</span>
                </label>
                <button class="export-btn" title="Export chart as PNG for LinkedIn">📸 Export</button>
                <button class="add-chart-btn">Add Chart</button>
                <button class="remove-card-btn">Remove</button>
                <input type="text" class="title-input" placeholder="Chart Title" value="${initialTitle}" style="margin-left: 10px; padding: 4px; border: 1px solid #ccc; border-radius: 3px;">
                <button class="toggle-notes-btn">Show Notes</button>
            </div>
            <div class="selected-tickers"></div>
            <div class="chart-box" style="height: ${initialHeight}px;"></div>
            <div class="notes-section" style="display: none; margin-top: 10px;">
                <textarea class="notes-textarea" placeholder="Add notes about this chart..." style="width: 100%; min-height: 80px; padding: 8px; border: 1px solid #ccc; border-radius: 4px; font-family: inherit; font-size: 12px; resize: vertical;"></textarea>
            </div>
        `;

        return card;
    },

    /**
     * Create a ticker chip element
     */
    createTickerChip(ticker, color, multiplier = 1, isHidden = false, onRemove = null) {
        const chip = document.createElement('span');
        chip.className = 'chip';
        chip.dataset.ticker = ticker;
        chip.style.cssText = `
            display: inline-flex;
            align-items: center;
            margin: 3px;
            padding: 4px 8px;
            background: ${color};
            color: white;
            border-radius: 4px;
            font-size: 12px;
            cursor: pointer;
        `;

        // Create chip content
        const tickerSpan = document.createElement('span');
        tickerSpan.textContent = ticker;
        tickerSpan.style.marginRight = '5px';
        chip.appendChild(tickerSpan);

        // Add multiplier input
        const multInput = document.createElement('input');
        multInput.type = 'number';
        multInput.className = 'multiplier-input';
        multInput.dataset.ticker = ticker;
        multInput.value = multiplier;
        multInput.step = '0.1';
        multInput.min = '0.1';
        multInput.max = '10';
        multInput.style.cssText = `
            width: 40px;
            margin: 0 2px;
            padding: 1px 2px;
            border: 1px solid rgba(255,255,255,0.5);
            background: rgba(255,255,255,0.2);
            color: white;
            border-radius: 2px;
            font-size: 11px;
        `;
        multInput.onclick = (e) => e.stopPropagation();
        chip.appendChild(multInput);

        // Add remove button
        const removeBtn = document.createElement('span');
        removeBtn.className = 'close';
        removeBtn.innerHTML = '×';
        removeBtn.style.cssText = `
            margin-left: 5px;
            cursor: pointer;
            font-weight: bold;
            font-size: 16px;
            line-height: 1;
        `;
        removeBtn.onclick = (e) => {
            e.stopPropagation();
            if (typeof onRemove === 'function') {
                try { onRemove(ticker, chip); } catch (_) { /* noop */ }
            } else {
                chip.remove();
            }
        };
        chip.appendChild(removeBtn);

                if (isHidden) {
            chip.classList.add('chip--hidden');
        }
        return chip;
    },

    /**
     * Get all DOM elements from a card
     */
    getCardElements(card) {
        return {
            tickerInput: card.querySelector('.ticker-input'),
            addBtn: card.querySelector('.add-ticker-btn'),
            plotBtn: card.querySelector('.plot-btn'),
            fitBtn: card.querySelector('.fit-btn'),
            toggleDiffBtn: card.querySelector('.toggle-diff-btn'),
            toggleVolBtn: card.querySelector('.toggle-vol-btn'),
            toggleVolumeBtn: card.querySelector('.toggle-volume-btn'),
            toggleRevenueBtn: card.querySelector('.toggle-revenue-btn'),
            toggleFundamentalsPaneBtn: card.querySelector('.toggle-fundamentals-pane-btn'),
            toggleRevenueMetricBtn: card.querySelector('.toggle-revenue-metric-btn'),
            toggleNetIncomeMetricBtn: card.querySelector('.toggle-netincome-metric-btn'),
            toggleEpsMetricBtn: card.querySelector('.toggle-eps-metric-btn'),
            toggleFcfMetricBtn: card.querySelector('.toggle-fcf-metric-btn'),
            toggleRawBtn: card.querySelector('.toggle-raw-btn'),
            toggleAvgBtn: card.querySelector('.toggle-avg-btn'),
            toggleLastLabelBtn: card.querySelector('.toggle-lastlabel-btn'),
            toggleZeroLineBtn: card.querySelector('.toggle-zeroline-btn'),
            toggleFixedLegendBtn: card.querySelector('.toggle-fixedlegend-btn'),
            toggleNotesBtn: card.querySelector('.toggle-notes-btn'),
            heightDownBtn: card.querySelector('.height-decrease-btn'),
            heightUpBtn: card.querySelector('.height-increase-btn'),
            volPaneHeightDownBtn: card.querySelector('.volpane-height-decrease-btn'),
            volPaneHeightUpBtn: card.querySelector('.volpane-height-increase-btn'),
            fontSlider: card.querySelector('.font-slider'),
            fontValue: card.querySelector('.font-value'),
            exportBtn: card.querySelector('.export-btn'),
            rangeSelect: card.querySelector('.range-select'),
            intervalSelect: card.querySelector('.interval-select'),
            selectedTickersDiv: card.querySelector('.selected-tickers'),
            chartBox: card.querySelector('.chart-box'),
            titleInput: card.querySelector('.title-input'),
            removeCardBtn: card.querySelector('.remove-card-btn'),
            addChartBtn: card.querySelector('.add-chart-btn'),
            notesSection: card.querySelector('.notes-section'),
            notesTextarea: card.querySelector('.notes-textarea')
        };
    },

    /**
     * Update button text based on state
     */
    updateButtonStates(elements, states) {
        const { toggleDiffBtn, toggleVolBtn, toggleVolumeBtn, toggleRevenueBtn, toggleFundamentalsPaneBtn, toggleRawBtn, toggleAvgBtn, toggleLastLabelBtn, toggleZeroLineBtn, toggleFixedLegendBtn, toggleNotesBtn } = elements;
        const { showDiff, showVol, showVolume, showRevenue, showFundamentalsPane, useRaw, showAvg, lastLabelVisible, showZeroLine, showFixedLegend, showNotes } = states;

        if (toggleDiffBtn) {
            toggleDiffBtn.textContent = showDiff ? 'Hide Diff Pane' : 'Show Diff Pane';
        }
        if (toggleVolBtn) {
            toggleVolBtn.textContent = showVol ? 'Hide Vol (σ) Pane' : 'Show Vol (σ) Pane';
        }
        if (toggleVolumeBtn) {
            toggleVolumeBtn.textContent = showVolume ? 'Hide Volume Pane' : 'Show Volume Pane';
        }
        if (toggleRevenueBtn) {
            toggleRevenueBtn.textContent = showRevenue ? 'Hide Revenue Pane' : 'Show Revenue Pane';
        }
        if (toggleFundamentalsPaneBtn) {
            toggleFundamentalsPaneBtn.textContent = showFundamentalsPane ? 'Hide Fundamentals Pane' : 'Show Fundamentals Pane';
        }
        if (toggleRawBtn) {
            toggleRawBtn.textContent = useRaw ? 'Show % Basis' : 'Show Raw';
        }
        if (toggleAvgBtn) {
            toggleAvgBtn.textContent = showAvg ? 'Hide Avg' : 'Show Avg';
        }
        if (toggleLastLabelBtn) {
            toggleLastLabelBtn.textContent = lastLabelVisible ? 'Hide Last Label' : 'Show Last Label';
        }
        if (toggleZeroLineBtn) {
            toggleZeroLineBtn.textContent = showZeroLine ? 'Hide 0% Line' : 'Show 0% Line';
        }
        if (toggleFixedLegendBtn) {
            toggleFixedLegendBtn.textContent = showFixedLegend ? 'Hide Fixed Legend' : 'Show Fixed Legend';
        }
        if (toggleNotesBtn) {
            toggleNotesBtn.textContent = showNotes ? 'Hide Notes' : 'Show Notes';
        }
    },

    /**
     * Add ticker chips to the selected tickers div
     */
    normalizeTicker(t){ return t.trim().toUpperCase(); },

    addTickerChips(selectedTickersDiv, tickers, colorMap, multiplierMap, hiddenTickers, onRemove = null) {
        selectedTickersDiv.innerHTML = '';
        tickers.forEach(ticker => {
            const color = colorMap.get(ticker) || '#000000';
            const multiplier = multiplierMap.get(ticker) || 1;
            const isHidden = hiddenTickers.has(ticker);
            const chip = this.createTickerChip(ticker, color, multiplier, isHidden, onRemove);
            selectedTickersDiv.appendChild(chip);
        });
    },

    /**
     * Parse ticker input string
     */
    parseTickerInput(input) {
        if (!input) return [];
        
        // Split by comma or space, trim, uppercase, and filter empty
        return input.split(/[,\s]+/)
            .map(t => this.normalizeTicker(t))
            .filter(t => t.length > 0);
    }
};
