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
                <button class="settings-toggle-btn" title="Toggle Settings Panel">⚙️</button>
                <button class="export-btn" title="Export chart as PNG for LinkedIn">📸 Export</button>
                <button class="add-chart-btn">Add Chart</button>
                <button class="remove-card-btn">Remove</button>
                <input type="text" class="title-input" placeholder="Chart Title" value="${initialTitle}" style="margin-left: 10px; padding: 4px; border: 1px solid #ccc; border-radius: 3px;">
                <button class="toggle-notes-btn">Show Notes</button>
            </div>
            <div class="settings-panel" style="padding: 12px; background: #f5f5f5; border: 1px solid #ddd; border-radius: 4px; margin: 5px 0;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px;">
                    <!-- Column 1: Panes -->
                    <div style="display: flex; flex-direction: column; gap: 6px;">
                        <strong style="font-size: 0.8rem; color: #666; text-transform: uppercase;">Panes</strong>
                        <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                            <button class="toggle-diff-btn">Show Diff Pane</button>
                            <button class="toggle-vol-btn">Hide Vol (σ) Pane</button>
                            <button class="toggle-volume-btn">Show Volume Pane</button>
                            <button class="toggle-revenue-btn">Show Revenue Pane</button>
                            <button class="toggle-fundamentals-pane-btn">Show Fundamentals Pane</button>
                        </div>
                        <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                            <button class="toggle-revenue-metric-btn" style="display:none;">Revenue</button>
                            <button class="toggle-netincome-metric-btn" style="display:none;">Net Income</button>
                            <button class="toggle-eps-metric-btn" style="display:none;">EPS</button>
                            <button class="toggle-fcf-metric-btn" style="display:none;">FCF</button>
                        </div>
                        <button class="show-fundamentals-btn">Show Fundamentals</button>
                    </div>
                    <!-- Column 2: Data & Display -->
                    <div style="display: flex; flex-direction: column; gap: 6px;">
                        <strong style="font-size: 0.8rem; color: #666; text-transform: uppercase;">Data & Display</strong>
                        <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                            <button class="toggle-raw-btn">Show Raw</button>
                            <button class="toggle-logscale-btn">Log Scale</button>
                            <button class="toggle-avg-btn">Show Avg</button>
                            <button class="toggle-zeroline-btn">Show 0% Line</button>
                        </div>
                        <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                            <button class="toggle-lastlabel-btn">Hide Last Label</button>
                            <button class="toggle-lastticker-btn">Show Last Ticker</button>
                        </div>
                        <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                            <button class="reshuffle-colors-btn">Reshuffle Colors</button>
                            <button class="toggle-fixedlegend-btn">Show Fixed Legend</button>
                            <button class="toggle-legend-tickers-btn">Show Legend Tickers</button>
                        </div>
                    </div>
                    <!-- Column 3: Appearance -->
                    <div style="display: flex; flex-direction: column; gap: 6px;">
                        <strong style="font-size: 0.8rem; color: #666; text-transform: uppercase;">Appearance</strong>
                        <div style="display: grid; grid-template-columns: 55px 1fr 32px; align-items: center; gap: 6px; font-size: 0.85rem;">
                            <span>Height</span>
                            <input type="range" class="height-slider" min="400" max="800" value="500" step="50">
                            <span class="height-value" style="font-weight: bold;">500</span>
                            <span>Vol H</span>
                            <input type="range" class="volpane-height-slider" min="0.5" max="3.0" value="1.0" step="0.1">
                            <span class="volpane-height-value" style="font-weight: bold;">1.0</span>
                            <span>Font</span>
                            <input type="range" class="font-slider" min="8" max="24" value="12" step="1">
                            <span class="font-value" style="font-weight: bold;">12</span>
                            <span>Decimals</span>
                            <input type="range" class="decimals-slider" min="0" max="6" value="2" step="1">
                            <span class="decimals-value" style="font-weight: bold;">2</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="selected-tickers"></div>
            <div class="chart-box" style="height: ${initialHeight}px;"></div>
            <div class="notes-section" style="display: none; margin-top: 10px;">
                <textarea class="notes-textarea" placeholder="Add notes about this chart..." style="width: 100%; min-height: 80px; padding: 8px; border: 1px solid #ccc; border-radius: 4px; font-family: inherit; font-size: 12px; resize: vertical;"></textarea>
            </div>
        `;

        // Set up settings panel toggle
        const settingsToggleBtn = card.querySelector('.settings-toggle-btn');
        const settingsPanel = card.querySelector('.settings-panel');

        // Initialize state object if not present (ensures persistence works immediately)
        if (!card._state) {
            card._state = {};
        }

        if (settingsToggleBtn && settingsPanel) {
            // Helper to persist state
            const persistState = (isOpen) => {
                card._state.settingsPanelOpen = isOpen;
                if (typeof window.saveCards === 'function') window.saveCards();
            };

            settingsToggleBtn.addEventListener('click', () => {
                const isOpen = settingsPanel.classList.toggle('settings-panel--open');
                settingsToggleBtn.classList.toggle('active', isOpen);
                persistState(isOpen);
            });

            // Close on Escape key - scoped to this card only
            const escapeHandler = (e) => {
                if (e.key === 'Escape' && settingsPanel.classList.contains('settings-panel--open')) {
                    // Only handle if focus is within this card or no specific element is focused
                    const activeEl = document.activeElement;
                    if (!activeEl || activeEl === document.body || card.contains(activeEl)) {
                        settingsPanel.classList.remove('settings-panel--open');
                        settingsToggleBtn.classList.remove('active');
                        persistState(false);
                    }
                }
            };

            // Store handler for cleanup later
            card._escapeHandler = escapeHandler;
            document.addEventListener('keydown', escapeHandler);
        }

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
            settingsToggleBtn: card.querySelector('.settings-toggle-btn'),
            settingsPanel: card.querySelector('.settings-panel'),
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
            toggleLogScaleBtn: card.querySelector('.toggle-logscale-btn'),
            toggleAvgBtn: card.querySelector('.toggle-avg-btn'),
            toggleLastLabelBtn: card.querySelector('.toggle-lastlabel-btn'),
            toggleLastTickerBtn: card.querySelector('.toggle-lastticker-btn'),
            reshuffleColorsBtn: card.querySelector('.reshuffle-colors-btn'),
            toggleZeroLineBtn: card.querySelector('.toggle-zeroline-btn'),
            toggleFixedLegendBtn: card.querySelector('.toggle-fixedlegend-btn'),
            toggleLegendTickersBtn: card.querySelector('.toggle-legend-tickers-btn'),
            toggleNotesBtn: card.querySelector('.toggle-notes-btn'),
            heightSlider: card.querySelector('.height-slider'),
            heightValue: card.querySelector('.height-value'),
            volPaneHeightSlider: card.querySelector('.volpane-height-slider'),
            volPaneHeightValue: card.querySelector('.volpane-height-value'),
            fontSlider: card.querySelector('.font-slider'),
            fontValue: card.querySelector('.font-value'),
            decimalsSlider: card.querySelector('.decimals-slider'),
            decimalsValue: card.querySelector('.decimals-value'),
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
        const { toggleDiffBtn, toggleVolBtn, toggleVolumeBtn, toggleRevenueBtn, toggleFundamentalsPaneBtn, toggleRawBtn, toggleLogScaleBtn, toggleAvgBtn, toggleLastLabelBtn, toggleLastTickerBtn, toggleZeroLineBtn, toggleFixedLegendBtn, toggleLegendTickersBtn, toggleNotesBtn } = elements;
        const { showDiff, showVol, showVolume, showRevenue, showFundamentalsPane, useRaw, useLogScale, showAvg, lastLabelVisible, lastTickerVisible, showZeroLine, showFixedLegend, showLegendTickers, showNotes } = states;

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
        if (toggleLogScaleBtn) {
            toggleLogScaleBtn.textContent = useLogScale ? 'Linear Scale' : 'Log Scale';
        }
        if (toggleAvgBtn) {
            toggleAvgBtn.textContent = showAvg ? 'Hide Avg' : 'Show Avg';
        }
        if (toggleLastLabelBtn) {
            toggleLastLabelBtn.textContent = lastLabelVisible ? 'Hide Last Label' : 'Show Last Label';
        }
        if (toggleLastTickerBtn) {
            toggleLastTickerBtn.textContent = lastTickerVisible ? 'Hide Last Ticker' : 'Show Last Ticker';
        }
        if (toggleZeroLineBtn) {
            toggleZeroLineBtn.textContent = showZeroLine ? 'Hide 0% Line' : 'Show 0% Line';
        }
        if (toggleFixedLegendBtn) {
            toggleFixedLegendBtn.textContent = showFixedLegend ? 'Hide Fixed Legend' : 'Show Fixed Legend';
        }
        if (toggleLegendTickersBtn) {
            toggleLegendTickersBtn.textContent = showLegendTickers ? 'Hide Legend Tickers' : 'Show Legend Tickers';
        }
        if (toggleNotesBtn) {
            toggleNotesBtn.textContent = showNotes ? 'Hide Notes' : 'Show Notes';
        }
    },

    /**
     * Add ticker chips to the selected tickers div
     */
    normalizeTicker(t){
        // Extract ticker from "TICKER - Company Name" format
        const trimmed = t.trim();
        const dashIndex = trimmed.indexOf(' - ');
        if (dashIndex > 0) {
            return trimmed.substring(0, dashIndex).trim().toUpperCase();
        }
        return trimmed.toUpperCase();
    },

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
