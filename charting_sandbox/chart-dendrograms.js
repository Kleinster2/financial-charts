/**
 * Dendrogram viewer component
 * Displays hierarchical clustering dendrograms
 * Supports multiple time periods: Full History, 2024, 2025
 */

(() => {
    // Time periods available
    const TIME_PERIODS = [
        { suffix: '', label: 'Full History', description: '2+ years of data', group: 'main' },
        { suffix: '_2024', label: '2024', description: 'Jan 2024 - Dec 2024', group: 'main' },
        { suffix: '_2025', label: '2025', description: 'Jan 2025 - Present', group: 'main' },
        // Quarters
        { suffix: '_2024_Q1', label: 'Q1 2024', description: 'Jan - Mar 2024', group: 'q2024' },
        { suffix: '_2024_Q2', label: 'Q2 2024', description: 'Apr - Jun 2024', group: 'q2024' },
        { suffix: '_2024_Q3', label: 'Q3 2024', description: 'Jul - Sep 2024', group: 'q2024' },
        { suffix: '_2024_Q4', label: 'Q4 2024', description: 'Oct - Dec 2024', group: 'q2024' },
        { suffix: '_2025_Q1', label: 'Q1 2025', description: 'Jan - Mar 2025', group: 'q2025' },
        { suffix: '_2025_Q2', label: 'Q2 2025', description: 'Apr - Jun 2025', group: 'q2025' },
        { suffix: '_2025_Q3', label: 'Q3 2025', description: 'Jul - Sep 2025', group: 'q2025' },
        // 2024 Months
        { suffix: '_2024_01', label: 'Jan', description: 'January 2024', group: 'm2024' },
        { suffix: '_2024_02', label: 'Feb', description: 'February 2024', group: 'm2024' },
        { suffix: '_2024_03', label: 'Mar', description: 'March 2024', group: 'm2024' },
        { suffix: '_2024_04', label: 'Apr', description: 'April 2024', group: 'm2024' },
        { suffix: '_2024_05', label: 'May', description: 'May 2024', group: 'm2024' },
        { suffix: '_2024_06', label: 'Jun', description: 'June 2024', group: 'm2024' },
        { suffix: '_2024_07', label: 'Jul', description: 'July 2024', group: 'm2024' },
        { suffix: '_2024_08', label: 'Aug', description: 'August 2024', group: 'm2024' },
        { suffix: '_2024_09', label: 'Sep', description: 'September 2024', group: 'm2024' },
        { suffix: '_2024_10', label: 'Oct', description: 'October 2024', group: 'm2024' },
        { suffix: '_2024_11', label: 'Nov', description: 'November 2024', group: 'm2024' },
        { suffix: '_2024_12', label: 'Dec', description: 'December 2024', group: 'm2024' },
        // 2025 Months
        { suffix: '_2025_01', label: 'Jan', description: 'January 2025', group: 'm2025' },
        { suffix: '_2025_02', label: 'Feb', description: 'February 2025', group: 'm2025' },
        { suffix: '_2025_03', label: 'Mar', description: 'March 2025', group: 'm2025' },
        { suffix: '_2025_04', label: 'Apr', description: 'April 2025', group: 'm2025' },
        { suffix: '_2025_05', label: 'May', description: 'May 2025', group: 'm2025' },
        { suffix: '_2025_06', label: 'Jun', description: 'June 2025', group: 'm2025' },
        { suffix: '_2025_07', label: 'Jul', description: 'July 2025', group: 'm2025' },
        { suffix: '_2025_08', label: 'Aug', description: 'August 2025', group: 'm2025' },
        { suffix: '_2025_09', label: 'Sep', description: 'September 2025', group: 'm2025' },
        { suffix: '_2025_10', label: 'Oct', description: 'October 2025', group: 'm2025' },
        { suffix: '_2025_11', label: 'Nov', description: 'November 2025', group: 'm2025' }
    ];

    // Dendrograms organized by category
    const DENDROGRAM_CATEGORIES = {
        'US Sectors': [
            { file: 'dendrogram_tech', title: 'Technology', description: 'Tech companies hierarchical clustering' },
            { file: 'dendrogram_financials', title: 'Financials', description: 'Financial services clustering' },
            { file: 'dendrogram_energy', title: 'Energy', description: 'Oil, gas, and energy companies' },
            { file: 'dendrogram_consumer', title: 'Consumer', description: 'Consumer discretionary and staples' },
            { file: 'dendrogram_reits', title: 'REITs', description: 'Real Estate Investment Trusts' },
        ],
        'US Themes': [
            { file: 'dendrogram_ai', title: 'AI & Data Centers', description: 'AI infrastructure and data center companies' },
            { file: 'dendrogram_crypto', title: 'Crypto & Mining', description: 'Cryptocurrency and mining stocks' },
            { file: 'dendrogram_defense', title: 'Defense & Aerospace', description: 'Defense contractors, space, and aerospace' },
        ],
        'China': [
            { file: 'dendrogram_china', title: 'All', description: 'All China A-shares (Shanghai & Shenzhen)' },
            { file: 'dendrogram_china_tech', title: 'Tech', description: 'Tech, semiconductors, AI chips' },
            { file: 'dendrogram_china_semis', title: 'Semis/AI', description: 'Cambricon, SMIC, Hygon, etc.' },
            { file: 'dendrogram_china_ev', title: 'EV/Battery', description: 'CATL, BYD, lithium miners' },
            { file: 'dendrogram_china_financials', title: 'Financials', description: 'Chinese banks & insurance' },
            { file: 'dendrogram_china_consumer', title: 'Consumer', description: 'Baijiu & consumer goods' },
            { file: 'dendrogram_china_healthcare', title: 'Healthcare', description: 'Pharma & biotech' },
            { file: 'dendrogram_china_energy', title: 'Energy', description: 'Oil, coal, mining' },
            { file: 'dendrogram_china_industrials', title: 'Industrials', description: 'Manufacturing & appliances' },
            { file: 'dendrogram_china_realestate', title: 'Real Estate', description: 'Property developers' },
        ],
        'Korea': [
            { file: 'dendrogram_korea', title: 'All', description: 'All Korean stocks (KRX exchange)' },
            { file: 'dendrogram_korea_tech', title: 'Tech', description: 'Samsung, SK Hynix, NAVER, Kakao' },
            { file: 'dendrogram_korea_battery', title: 'Battery/EV', description: 'Samsung SDI, LG Chem, Hyundai' },
            { file: 'dendrogram_korea_financials', title: 'Financials', description: 'KB, Shinhan, Hana, Woori' },
            { file: 'dendrogram_korea_biotech', title: 'Biotech', description: 'Celltrion, Samsung Biologics' },
            { file: 'dendrogram_korea_industrial', title: 'Industrial', description: 'POSCO, shipbuilding, telecom' },
        ],
        'Brazil': [
            { file: 'dendrogram_brazil', title: 'All', description: 'All Brazilian stocks (B3 exchange)' },
            { file: 'dendrogram_brazil_financials', title: 'Financials', description: 'Itaú, Bradesco, B3, BTG Pactual' },
            { file: 'dendrogram_brazil_energy', title: 'Oil & Gas', description: 'Petrobras, PetroRio, Ultrapar' },
            { file: 'dendrogram_brazil_mining', title: 'Mining & Steel', description: 'Vale, Gerdau, CSN, Usiminas' },
            { file: 'dendrogram_brazil_utilities', title: 'Utilities', description: 'Eletrobras, Equatorial, Engie' },
            { file: 'dendrogram_brazil_consumer', title: 'Consumer', description: 'Ambev, Renner, Magazine Luiza' },
            { file: 'dendrogram_brazil_industrial', title: 'Industrial', description: 'WEG, Embraer, Rumo, Localiza' },
        ],
        'International': [
            { file: 'dendrogram_countries', title: 'Country ETFs', description: 'iShares country ETFs (EWJ, EWZ, FXI)' },
        ],
        'Overview': [
            { file: 'dendrogram_truncated', title: 'All (Truncated)', description: 'Overview with truncated branches' },
            { file: 'dendrogram_detailed', title: 'All (Detailed)', description: 'Full dendrogram of top 100 stocks' },
        ],
    };

    // Clustermaps organized by category
    const CLUSTERMAP_CATEGORIES = {
        'US Sectors': [
            { file: 'clustermap_tech', title: 'Technology', description: 'Tech sector correlation heatmap' },
            { file: 'clustermap_financials', title: 'Financials', description: 'Financial services correlation' },
            { file: 'clustermap_energy', title: 'Energy', description: 'Energy sector correlation' },
            { file: 'clustermap_consumer', title: 'Consumer', description: 'Consumer sector correlation' },
            { file: 'clustermap_reits', title: 'REITs', description: 'REITs correlation heatmap' },
        ],
        'US Themes': [
            { file: 'clustermap_ai', title: 'AI & Data Centers', description: 'AI/DC stocks correlation' },
            { file: 'clustermap_crypto', title: 'Crypto & Mining', description: 'Crypto stocks correlation' },
            { file: 'clustermap_defense', title: 'Defense & Aerospace', description: 'Defense stocks correlation' },
        ],
        'China': [
            { file: 'clustermap_china', title: 'All', description: 'All China A-shares correlation' },
            { file: 'clustermap_china_tech', title: 'Tech', description: 'Tech, semiconductors, AI chips' },
            { file: 'clustermap_china_semis', title: 'Semis/AI', description: 'Cambricon, SMIC, Hygon' },
            { file: 'clustermap_china_ev', title: 'EV/Battery', description: 'EV & battery stocks' },
            { file: 'clustermap_china_financials', title: 'Financials', description: 'Chinese banks & insurance' },
            { file: 'clustermap_china_consumer', title: 'Consumer', description: 'Baijiu & consumer goods' },
            { file: 'clustermap_china_healthcare', title: 'Healthcare', description: 'Pharma & biotech' },
            { file: 'clustermap_china_energy', title: 'Energy', description: 'Oil, coal, mining' },
            { file: 'clustermap_china_industrials', title: 'Industrials', description: 'Manufacturing' },
            { file: 'clustermap_china_realestate', title: 'Real Estate', description: 'Property developers' },
        ],
        'Korea': [
            { file: 'clustermap_korea', title: 'All', description: 'All Korean stocks correlation' },
            { file: 'clustermap_korea_tech', title: 'Tech', description: 'Samsung, SK Hynix, NAVER' },
            { file: 'clustermap_korea_battery', title: 'Battery/EV', description: 'Battery & auto stocks' },
            { file: 'clustermap_korea_financials', title: 'Financials', description: 'Korean banks' },
            { file: 'clustermap_korea_biotech', title: 'Biotech', description: 'Biotech stocks' },
            { file: 'clustermap_korea_industrial', title: 'Industrial', description: 'Industrial stocks' },
        ],
        'Brazil': [
            { file: 'clustermap_brazil', title: 'All', description: 'All Brazilian stocks correlation' },
            { file: 'clustermap_brazil_financials', title: 'Financials', description: 'Itaú, Bradesco, B3 correlations' },
            { file: 'clustermap_brazil_energy', title: 'Oil & Gas', description: 'Petrobras, PetroRio correlations' },
            { file: 'clustermap_brazil_mining', title: 'Mining & Steel', description: 'Vale, Gerdau correlations' },
            { file: 'clustermap_brazil_utilities', title: 'Utilities', description: 'Electric utilities correlations' },
            { file: 'clustermap_brazil_consumer', title: 'Consumer', description: 'Consumer stocks correlations' },
            { file: 'clustermap_brazil_industrial', title: 'Industrial', description: 'Industrial stocks correlations' },
        ],
        'International': [
            { file: 'clustermap_countries', title: 'Country ETFs', description: 'iShares country ETFs' },
        ],
        'Overview': [
            { file: 'clustermap_top50', title: 'Top 50 Connected', description: 'Most correlated stocks' },
        ],
    };

    // Helper to build dropdown options from categories
    function buildCategoryOptions(categories) {
        let html = '';
        for (const [category, items] of Object.entries(categories)) {
            html += `<optgroup label="${category}">`;
            items.forEach(item => {
                html += `<option value="${item.file}" data-description="${item.description}">${item.title}</option>`;
            });
            html += '</optgroup>';
        }
        return html;
    }

    /**
     * Create dendrogram viewer card
     */
    function createDendrogramCard(wrapperEl) {
        const wrapper = wrapperEl || document.getElementById('charts-wrapper');
        if (!wrapper) {
            console.error('[Dendrograms] No wrapper element found');
            return null;
        }

        console.log('[Dendrograms] Creating dendrogram viewer');

        const card = document.createElement('div');
        card.className = 'chart-card dendrogram-card';
        card.id = `dendrogram-viewer-${Date.now()}`;
        card._type = 'dendrograms';

        // Build the card HTML with dropdowns
        card.innerHTML = `
            <div class="controls" style="margin-bottom: 12px; display: flex; align-items: center; flex-wrap: wrap; gap: 12px;">
                <strong style="font-size: 1.1rem;">Hierarchical Clustering</strong>
                <div class="view-type-selector" style="display: flex; gap: 4px;">
                    <button class="view-type-btn active" data-type="dendrogram">Dendrograms</button>
                    <button class="view-type-btn" data-type="clustermap">Clustermaps</button>
                </div>
                <select class="chart-select dendrogram-select" style="padding: 8px 12px; font-size: 0.95rem; border: 2px solid #007bff; border-radius: 4px; min-width: 200px;">
                    ${buildCategoryOptions(DENDROGRAM_CATEGORIES)}
                </select>
                <select class="chart-select clustermap-select" style="display: none; padding: 8px 12px; font-size: 0.95rem; border: 2px solid #007bff; border-radius: 4px; min-width: 200px;">
                    ${buildCategoryOptions(CLUSTERMAP_CATEGORIES)}
                </select>
                <span style="color: #666; font-size: 0.85rem;">Ward's Method | Distance = 1 - Correlation</span>
            </div>
            <div class="period-row" style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px; flex-wrap: wrap;">
                <span style="font-weight: bold;">Period:</span>
                ${TIME_PERIODS.filter(p => p.group === 'main').map((p, i) => `
                    <button class="period-btn${i === 0 ? ' active' : ''}" data-suffix="${p.suffix}" title="${p.description}">
                        ${p.label}
                    </button>
                `).join('')}
                <span style="color: #999; margin: 0 4px;">|</span>
                <select class="period-select-quarter" style="padding: 4px 8px; font-size: 0.85rem; border: 1px solid #28a745; border-radius: 4px;">
                    <option value="">Quarters...</option>
                    <optgroup label="2024">
                        ${TIME_PERIODS.filter(p => p.group === 'q2024').map(p => `
                            <option value="${p.suffix}">${p.label}</option>
                        `).join('')}
                    </optgroup>
                    <optgroup label="2025">
                        ${TIME_PERIODS.filter(p => p.group === 'q2025').map(p => `
                            <option value="${p.suffix}">${p.label}</option>
                        `).join('')}
                    </optgroup>
                </select>
                <select class="period-select-month" style="padding: 4px 8px; font-size: 0.85rem; border: 1px solid #28a745; border-radius: 4px;">
                    <option value="">Months...</option>
                    <optgroup label="2024">
                        ${TIME_PERIODS.filter(p => p.group === 'm2024').map(p => `
                            <option value="${p.suffix}">${p.label}</option>
                        `).join('')}
                    </optgroup>
                    <optgroup label="2025">
                        ${TIME_PERIODS.filter(p => p.group === 'm2025').map(p => `
                            <option value="${p.suffix}">${p.label}</option>
                        `).join('')}
                    </optgroup>
                </select>
            </div>
            <div class="dendrogram-container" style="background: #fff; border: 1px solid #ddd; border-radius: 4px; padding: 16px; min-height: 400px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div>
                        <div class="dendrogram-title" style="font-weight: bold; color: #333;"></div>
                        <div class="dendrogram-description" style="color: #666; font-size: 0.9rem;"></div>
                    </div>
                    <div class="zoom-controls" style="display: flex; gap: 8px; align-items: center;">
                        <button class="zoom-out-btn" title="Zoom Out" style="padding: 4px 12px; font-size: 1.2rem; cursor: pointer;">-</button>
                        <span class="zoom-level" style="min-width: 50px; text-align: center; font-size: 0.9rem;">100%</span>
                        <button class="zoom-in-btn" title="Zoom In" style="padding: 4px 12px; font-size: 1.2rem; cursor: pointer;">+</button>
                        <button class="zoom-reset-btn" title="Reset Zoom" style="padding: 4px 8px; font-size: 0.9rem; cursor: pointer;">Reset</button>
                    </div>
                </div>
                <div class="dendrogram-image-wrapper" style="text-align: center; overflow: auto; max-height: 700px; border: 1px solid #eee;">
                    <img class="dendrogram-image" src="" alt="Dendrogram" style="height: auto; cursor: grab; transform-origin: top left;" />
                </div>
            </div>
        `;

        // Add styles for buttons
        const style = document.createElement('style');
        style.textContent = `
            .period-btn {
                padding: 5px 12px;
                border: 2px solid #28a745;
                border-radius: 4px;
                background: #fff;
                color: #28a745;
                cursor: pointer;
                font-size: 0.85rem;
                font-weight: bold;
                transition: all 0.2s;
            }
            .period-btn:hover {
                background: #e8f5e9;
            }
            .period-btn.active {
                background: #28a745;
                color: #fff;
            }
            .view-type-btn {
                padding: 6px 14px;
                border: 2px solid #333;
                border-radius: 4px;
                background: #fff;
                color: #333;
                cursor: pointer;
                font-size: 0.85rem;
                font-weight: bold;
                transition: all 0.2s;
            }
            .view-type-btn:hover {
                background: #f0f0f0;
            }
            .view-type-btn.active {
                background: #333;
                color: #fff;
            }
            .chart-select {
                cursor: pointer;
            }
            .chart-select:focus {
                outline: none;
                box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
            }
            .dendrogram-image.zoomed {
                max-width: none;
                cursor: zoom-out;
            }
        `;
        if (!document.querySelector('style[data-dendrograms]')) {
            style.setAttribute('data-dendrograms', 'true');
            document.head.appendChild(style);
        }

        // Get references
        const periodButtons = card.querySelectorAll('.period-btn');
        const quarterSelect = card.querySelector('.period-select-quarter');
        const monthSelect = card.querySelector('.period-select-month');
        const viewTypeButtons = card.querySelectorAll('.view-type-btn');
        const dendrogramSelect = card.querySelector('.dendrogram-select');
        const clustermapSelect = card.querySelector('.clustermap-select');
        const titleEl = card.querySelector('.dendrogram-title');
        const descEl = card.querySelector('.dendrogram-description');
        const imgEl = card.querySelector('.dendrogram-image');
        const zoomInBtn = card.querySelector('.zoom-in-btn');
        const zoomOutBtn = card.querySelector('.zoom-out-btn');
        const zoomResetBtn = card.querySelector('.zoom-reset-btn');
        const zoomLevelEl = card.querySelector('.zoom-level');

        // State
        let currentZoom = 100;
        let currentViewType = 'dendrogram';
        let currentPeriodSuffix = '';
        let currentFile = 'dendrogram_tech';
        const ZOOM_STEP = 25;
        const ZOOM_MIN = 50;
        const ZOOM_MAX = 300;

        function updateZoom() {
            imgEl.style.width = `${currentZoom}%`;
            zoomLevelEl.textContent = `${currentZoom}%`;
        }

        // Get file path with period suffix
        function getFilePath(baseFile, suffix) {
            return `dendrograms/${baseFile}${suffix}.png`;
        }

        // Load image from file and description
        function loadImage(file, suffix) {
            const activeSelect = currentViewType === 'dendrogram' ? dendrogramSelect : clustermapSelect;
            const selectedOption = activeSelect.querySelector(`option[value="${file}"]`);
            const title = selectedOption ? selectedOption.textContent : file;
            const description = selectedOption ? selectedOption.dataset.description : '';
            const category = selectedOption && selectedOption.parentElement.label ? selectedOption.parentElement.label : '';

            const periodLabel = TIME_PERIODS.find(p => p.suffix === suffix)?.label || 'Full History';
            titleEl.textContent = `${category ? category + ' - ' : ''}${title} - ${periodLabel}`;
            descEl.textContent = description;
            imgEl.src = getFilePath(file, suffix);
            imgEl.alt = title;
            // Reset zoom when changing images
            currentZoom = 100;
            updateZoom();
        }

        // Reload current view
        function reloadCurrentView() {
            loadImage(currentFile, currentPeriodSuffix);
        }

        // Clear period selections and set suffix
        function setPeriod(suffix, source) {
            currentPeriodSuffix = suffix;

            // Update main period buttons
            periodButtons.forEach(b => b.classList.toggle('active', b.dataset.suffix === suffix));

            // Reset dropdowns if not the source
            if (source !== 'quarter') quarterSelect.value = '';
            if (source !== 'month') monthSelect.value = '';

            // If using dropdown, deactivate main buttons
            if (source === 'quarter' || source === 'month') {
                periodButtons.forEach(b => b.classList.remove('active'));
            }

            reloadCurrentView();
        }

        // Period button click handlers
        periodButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                setPeriod(btn.dataset.suffix, 'main');
            });
        });

        // Quarter dropdown
        quarterSelect.addEventListener('change', () => {
            if (quarterSelect.value) {
                setPeriod(quarterSelect.value, 'quarter');
            }
        });

        // Month dropdown
        monthSelect.addEventListener('change', () => {
            if (monthSelect.value) {
                setPeriod(monthSelect.value, 'month');
            }
        });

        // View type switching
        viewTypeButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const type = btn.dataset.type;
                currentViewType = type;

                // Update view type button states
                viewTypeButtons.forEach(b => b.classList.toggle('active', b.dataset.type === type));

                // Show/hide selectors
                dendrogramSelect.style.display = type === 'dendrogram' ? 'inline-block' : 'none';
                clustermapSelect.style.display = type === 'clustermap' ? 'inline-block' : 'none';

                // Set current file from the appropriate dropdown
                const activeSelect = type === 'dendrogram' ? dendrogramSelect : clustermapSelect;
                currentFile = activeSelect.value;
                reloadCurrentView();
            });
        });

        // Dendrogram dropdown change
        dendrogramSelect.addEventListener('change', () => {
            currentFile = dendrogramSelect.value;
            reloadCurrentView();
        });

        // Clustermap dropdown change
        clustermapSelect.addEventListener('change', () => {
            currentFile = clustermapSelect.value;
            reloadCurrentView();
        });

        // Zoom controls
        zoomInBtn.addEventListener('click', () => {
            if (currentZoom < ZOOM_MAX) {
                currentZoom += ZOOM_STEP;
                updateZoom();
            }
        });

        zoomOutBtn.addEventListener('click', () => {
            if (currentZoom > ZOOM_MIN) {
                currentZoom -= ZOOM_STEP;
                updateZoom();
            }
        });

        zoomResetBtn.addEventListener('click', () => {
            currentZoom = 100;
            updateZoom();
        });

        // Mouse wheel zoom
        const imageWrapper = card.querySelector('.dendrogram-image-wrapper');
        imageWrapper.addEventListener('wheel', (e) => {
            if (e.ctrlKey) {
                e.preventDefault();
                if (e.deltaY < 0 && currentZoom < ZOOM_MAX) {
                    currentZoom += ZOOM_STEP;
                } else if (e.deltaY > 0 && currentZoom > ZOOM_MIN) {
                    currentZoom -= ZOOM_STEP;
                }
                updateZoom();
            }
        });

        // Load initial view
        currentFile = dendrogramSelect.value;
        reloadCurrentView();

        wrapper.appendChild(card);
        console.log('[Dendrograms] Dendrogram viewer created');

        return card;
    }

    // Export
    window.ChartDendrograms = {
        createDendrogramCard
    };

    console.log('[ChartDendrograms] Module loaded');
})();
