/**
 * Dendrogram viewer component
 * Displays hierarchical clustering dendrograms
 */

(() => {
    const DENDROGRAMS = [
        { file: 'dendrogram_tech.png', title: 'Technology Sector', description: 'Tech companies hierarchical clustering' },
        { file: 'dendrogram_financials.png', title: 'Financials Sector', description: 'Financial services clustering' },
        { file: 'dendrogram_energy.png', title: 'Energy Sector', description: 'Oil, gas, and energy companies' },
        { file: 'dendrogram_consumer.png', title: 'Consumer Sector', description: 'Consumer discretionary and staples' },
        { file: 'dendrogram_crypto.png', title: 'Crypto & Mining', description: 'Cryptocurrency and mining stocks' },
        { file: 'dendrogram_ai.png', title: 'AI & Data Centers', description: 'AI infrastructure and data center companies' },
        { file: 'dendrogram_truncated.png', title: 'All Tickers (Truncated)', description: 'Overview of all tickers with truncated branches' },
        { file: 'dendrogram_detailed.png', title: 'All Tickers (Detailed)', description: 'Full dendrogram of all tickers' }
    ];

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

        // Build the card HTML
        card.innerHTML = `
            <div class="controls" style="margin-bottom: 12px;">
                <strong style="font-size: 1.1rem;">Hierarchical Clustering Dendrograms</strong>
                <span style="margin-left: auto; color: #666; font-size: 0.9rem;">Ward's Method | Distance = 1 - Correlation | Period: Nov 2023 - Nov 2025 (2 years)</span>
            </div>
            <div class="dendrogram-selector" style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;">
                ${DENDROGRAMS.map((d, i) => `
                    <button class="dendrogram-btn${i === 0 ? ' active' : ''}" data-index="${i}" title="${d.description}">
                        ${d.title}
                    </button>
                `).join('')}
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
            .dendrogram-btn {
                padding: 8px 16px;
                border: 1px solid #007bff;
                border-radius: 4px;
                background: #fff;
                color: #007bff;
                cursor: pointer;
                font-size: 0.9rem;
                transition: all 0.2s;
            }
            .dendrogram-btn:hover {
                background: #e7f1ff;
            }
            .dendrogram-btn.active {
                background: #007bff;
                color: #fff;
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
        const buttons = card.querySelectorAll('.dendrogram-btn');
        const titleEl = card.querySelector('.dendrogram-title');
        const descEl = card.querySelector('.dendrogram-description');
        const imgEl = card.querySelector('.dendrogram-image');
        const zoomInBtn = card.querySelector('.zoom-in-btn');
        const zoomOutBtn = card.querySelector('.zoom-out-btn');
        const zoomResetBtn = card.querySelector('.zoom-reset-btn');
        const zoomLevelEl = card.querySelector('.zoom-level');

        // Zoom state
        let currentZoom = 100;
        const ZOOM_STEP = 25;
        const ZOOM_MIN = 50;
        const ZOOM_MAX = 300;

        function updateZoom() {
            imgEl.style.width = `${currentZoom}%`;
            zoomLevelEl.textContent = `${currentZoom}%`;
        }

        // Load dendrogram function
        function loadDendrogram(index) {
            const d = DENDROGRAMS[index];
            titleEl.textContent = d.title;
            descEl.textContent = d.description;
            imgEl.src = `dendrograms/${d.file}`;
            imgEl.alt = d.title;
            // Reset zoom when changing images
            currentZoom = 100;
            updateZoom();

            // Update active button
            buttons.forEach((btn, i) => {
                btn.classList.toggle('active', i === index);
            });
        }

        // Button click handlers
        buttons.forEach((btn, i) => {
            btn.addEventListener('click', () => loadDendrogram(i));
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

        // Load first dendrogram
        loadDendrogram(0);

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
