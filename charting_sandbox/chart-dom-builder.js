/**
 * Chart DOM Builder
 * Handles creation of chart card DOM elements and controls
 */

window.ChartDomBuilder = {
    /**
     * Create the main chart card element with all controls
     */
    createChartCard(cardId, initialTitle = '') {
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
                </select>
                <button class="toggle-diff-btn">Show Diff Pane</button>
                <button class="toggle-vol-btn">Hide Vol Pane</button>
                <button class="toggle-raw-btn">Show Raw</button>
                <button class="toggle-avg-btn">Show Avg</button>
                <button class="toggle-lastlabel-btn">Hide Last Label</button>
                <button class="add-chart-btn">Add Chart</button>
                <button class="remove-card-btn">Remove</button>
                <input type="text" class="title-input" placeholder="Chart Title" value="${initialTitle}" style="margin-left: 10px; padding: 4px; border: 1px solid #ccc; border-radius: 3px;">
            </div>
            <div class="selected-tickers"></div>
            <div class="chart-box" style="height: 400px;"></div>
        `;

        return card;
    },

    /**
     * Create a ticker chip element
     */
    createTickerChip(ticker, color, multiplier = 1, isHidden = false) {
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
            chip.remove();
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
            toggleDiffBtn: card.querySelector('.toggle-diff-btn'),
            toggleVolBtn: card.querySelector('.toggle-vol-btn'),
            toggleRawBtn: card.querySelector('.toggle-raw-btn'),
            toggleAvgBtn: card.querySelector('.toggle-avg-btn'),
            toggleLastLabelBtn: card.querySelector('.toggle-lastlabel-btn'),
            rangeSelect: card.querySelector('.range-select'),
            selectedTickersDiv: card.querySelector('.selected-tickers'),
            chartBox: card.querySelector('.chart-box'),
            titleInput: card.querySelector('.title-input'),
            removeCardBtn: card.querySelector('.remove-card-btn'),
            addChartBtn: card.querySelector('.add-chart-btn')
        };
    },

    /**
     * Update button text based on state
     */
    updateButtonStates(elements, states) {
        const { toggleDiffBtn, toggleVolBtn, toggleRawBtn, toggleAvgBtn, toggleLastLabelBtn } = elements;
        const { showDiff, showVol, useRaw, showAvg, lastLabelVisible } = states;

        if (toggleDiffBtn) {
            toggleDiffBtn.textContent = showDiff ? 'Hide Diff Pane' : 'Show Diff Pane';
        }
        if (toggleVolBtn) {
            toggleVolBtn.textContent = showVol ? 'Hide Vol Pane' : 'Show Vol Pane';
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
    },

    /**
     * Add ticker chips to the selected tickers div
     */
    addTickerChips(selectedTickersDiv, tickers, colorMap, multiplierMap, hiddenTickers) {
        selectedTickersDiv.innerHTML = '';
        tickers.forEach(ticker => {
            const color = colorMap.get(ticker) || '#000000';
            const multiplier = multiplierMap.get(ticker) || 1;
            const isHidden = hiddenTickers.has(ticker);
            const chip = this.createTickerChip(ticker, color, multiplier, isHidden);
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
            .map(t => t.trim().toUpperCase())
            .filter(t => t.length > 0);
    }
};
