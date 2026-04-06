/**
 * Chart Grid Layout Module
 *
 * Provides TradingView-style multi-chart grid layouts (2x1, 2x2, 3x2, etc.)
 * with crosshair sync across all visible charts.
 *
 * Exports: window.GridLayout
 */

window.GridLayout = (() => {
    // Layouts = column counts. Rows are auto (scroll for more).
    const LAYOUTS = [
        { id: '1', cols: 1, label: '1' },
        { id: '2', cols: 2, label: '2' },
        { id: '3', cols: 3, label: '3' },
        { id: '4', cols: 4, label: '4' },
    ];

    let currentLayout = '1';
    let crosshairSyncEnabled = true;
    let isSyncing = false; // guard against infinite loops
    let resizeObserver = null;

    // ─── Layout application ───────────────────────────────────────────

    function getLayout(id) {
        return LAYOUTS.find(l => l.id === id) || LAYOUTS[0];
    }

    function applyLayout(layoutId, pageNum) {
        const layout = getLayout(layoutId);
        currentLayout = layout.id;

        const wrapper = getActiveWrapper();
        if (!wrapper) return;

        // Toggle page-level chrome (title, nav) for grid mode
        const pageTitle = document.getElementById('page-title');
        const chartNav = document.getElementById('chart-nav');

        if (layout.id === '1x1') {
            // Default stacked layout
            wrapper.style.display = '';
            wrapper.style.gridTemplateColumns = '';
            wrapper.style.gridTemplateRows = '';
            wrapper.style.gridAutoRows = '';
            wrapper.style.gap = '';
            wrapper.style.overflow = '';
            wrapper.classList.remove('grid-layout');
            if (pageTitle) pageTitle.style.display = '';
            if (chartNav) chartNav.style.display = '';

            // Restore individual card heights
            wrapper.querySelectorAll('.chart-card').forEach(card => {
                card.classList.remove('grid-compact');
                const chartBox = card.querySelector('.chart-box');
                if (chartBox && card._ctx) {
                    chartBox.style.height = `${card._ctx.height || 500}px`;
                }
            });
        } else {
            // Grid layout
            wrapper.style.display = 'grid';
            wrapper.style.gridTemplateColumns = `repeat(${layout.cols}, 1fr)`;
            wrapper.style.gap = '4px';
            wrapper.style.overflow = '';
            wrapper.classList.add('grid-layout');

            // Row height: fit ~cols rows in viewport (square-ish cells), scroll for more
            const visibleRows = layout.cols; // e.g. 2 cols → 2 rows visible
            const rowHeight = Math.floor(window.innerHeight / visibleRows);
            wrapper.style.gridTemplateRows = '';
            wrapper.style.gridAutoRows = `${rowHeight}px`;

            // Hide page chrome in grid mode
            if (pageTitle) pageTitle.style.display = 'none';
            if (chartNav) chartNav.style.display = 'none';

            // Compact mode for all cards in grid
            wrapper.querySelectorAll('.chart-card').forEach(card => {
                card.classList.add('grid-compact');
            });
        }

        const isGrid = layout.cols > 1;

        // Reset maximize state
        maximizedCard = null;
        wrapper.querySelectorAll('.chart-card').forEach(c => {
            c.style.display = '';
            c.classList.remove('grid-maximized');
        });

        // Setup ResizeObserver for auto-resize in grid mode
        setupResizeObserver(wrapper, isGrid);

        // Resize all charts to fit their new containers
        // Double rAF ensures the grid layout has been computed
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                applyThemeToCharts(wrapper, isGrid);
                resizeAllCharts(wrapper);
                // Scale ticker labels for grid mode
                wrapper.querySelectorAll('.ticker-label').forEach(lbl => {
                    lbl.style.fontSize = isGrid ? '8px' : '';
                    lbl.style.padding = isGrid ? '1px 3px' : '';
                });
                // Setup crosshair sync for grid layouts
                if (isGrid && crosshairSyncEnabled) {
                    setupCrosshairSync(wrapper);
                } else {
                    teardownCrosshairSync(wrapper);
                }
                if (isGrid) setupMaximize(wrapper);
            });
        });

        // Persist
        saveLayoutForPage(pageNum || getActivePage());
        updateLayoutSelector();
    }

    const DARK_THEME = {
        layout: { background: { type: 'solid', color: '#000000' }, textColor: '#d1d4dc' },
        grid: { vertLines: { color: '#1e222d' }, horzLines: { color: '#1e222d' } },
        crosshair: {
            horzLine: { color: '#758696', labelBackgroundColor: '#2a2e39' },
            vertLine: { color: '#758696', labelBackgroundColor: '#2a2e39' }
        },
        rightPriceScale: { borderColor: '#2a2e39' },
        leftPriceScale: { borderColor: '#2a2e39' },
        timeScale: { borderColor: '#2a2e39' }
    };

    const LIGHT_THEME = {
        layout: { background: { type: 'solid', color: '#000000' }, textColor: '#d1d4dc' },
        grid: { vertLines: { color: '#1e222d' }, horzLines: { color: '#1e222d' } },
        crosshair: {
            horzLine: { color: undefined, labelBackgroundColor: undefined },
            vertLine: { color: undefined, labelBackgroundColor: undefined }
        },
        rightPriceScale: { borderColor: '#2a2e39' },
        leftPriceScale: { borderColor: undefined },
        timeScale: { borderColor: undefined }
    };

    function applyThemeToCharts(wrapper, dark) {
        if (!wrapper) return;
        const theme = dark ? DARK_THEME : LIGHT_THEME;
        wrapper.querySelectorAll('.chart-card').forEach(card => {
            const rt = card._ctx?.runtime;
            if (!rt?.chart) return;
            try { rt.chart.applyOptions(theme); } catch (_) {}
        });
    }

    function resizeAllCharts(wrapper) {
        if (!wrapper) return;
        wrapper.querySelectorAll('.chart-card').forEach(card => {
            const ctx = card._ctx;
            if (!ctx || !ctx.runtime || !ctx.runtime.chart) return;

            const chartBox = card.querySelector('.chart-box');
            if (!chartBox) return;

            const rt = ctx.runtime;
            const width = chartBox.clientWidth || chartBox.getBoundingClientRect().width || 400;
            const height = chartBox.clientHeight || chartBox.getBoundingClientRect().height || 300;

            try {
                rt.chart.resize(width, height);
                rt.chart.timeScale().fitContent();
            } catch (e) {
                console.warn(`[GridLayout] Resize failed for ${ctx.cardId}`, e);
            }
        });
    }

    // ─── ResizeObserver for chart boxes ──────────────────────────────

    function setupResizeObserver(wrapper, enable) {
        if (resizeObserver) {
            resizeObserver.disconnect();
            resizeObserver = null;
        }
        if (!enable || !wrapper) return;

        let resizeRafId = null;
        resizeObserver = new ResizeObserver((entries) => {
            if (resizeRafId) cancelAnimationFrame(resizeRafId);
            resizeRafId = requestAnimationFrame(() => {
                entries.forEach(entry => {
                    const chartBox = entry.target;
                    const card = chartBox.closest('.chart-card');
                    if (!card?._ctx?.runtime?.chart) return;

                    const rt = card._ctx.runtime;
                    const w = chartBox.clientWidth;
                    const h = chartBox.clientHeight;
                    if (w > 0 && h > 0) {
                        try { rt.chart.resize(w, h); } catch (_) {}
                    }
                });
            });
        });

        wrapper.querySelectorAll('.chart-box').forEach(box => {
            resizeObserver.observe(box);
        });
    }

    // ─── Crosshair sync ───────────────────────────────────────────────

    function setupCrosshairSync(wrapper) {
        teardownCrosshairSync(wrapper); // clean up previous

        const cards = Array.from(wrapper.querySelectorAll('.chart-card')).filter(
            c => c._ctx && c._ctx.runtime && c._ctx.runtime.chart && c.style.display !== 'none'
        );

        if (cards.length < 2) return;

        cards.forEach(card => {
            const chart = card._ctx.runtime.chart;
            const handler = (param) => {
                if (isSyncing) return;
                isSyncing = true;

                cards.forEach(otherCard => {
                    if (otherCard === card) return;
                    const otherChart = otherCard._ctx?.runtime?.chart;
                    if (!otherChart) return;

                    try {
                        if (param.time) {
                            otherChart.setCrosshairPosition(undefined, param.time, otherChart.panes()[0]?.series()[0]);
                        } else {
                            otherChart.clearCrosshairPosition();
                        }
                    } catch (_) {
                        // series might not exist yet
                    }
                });

                isSyncing = false;
            };

            chart.subscribeCrosshairMove(handler);
            card._gridCrosshairHandler = handler;
        });

        console.log(`[GridLayout] Crosshair sync active for ${cards.length} charts`);
    }

    function teardownCrosshairSync(wrapper) {
        if (!wrapper) return;
        wrapper.querySelectorAll('.chart-card').forEach(card => {
            if (card._gridCrosshairHandler && card._ctx?.runtime?.chart) {
                try {
                    card._ctx.runtime.chart.unsubscribeCrosshairMove(card._gridCrosshairHandler);
                } catch (_) {}
                card._gridCrosshairHandler = null;
            }
        });
    }

    // ─── Time range sync ──────────────────────────────────────────────

    function syncTimeRanges(wrapper) {
        const cards = Array.from(wrapper.querySelectorAll('.chart-card')).filter(
            c => c._ctx?.runtime?.chart && c.style.display !== 'none'
        );
        if (cards.length < 2) return;

        // Get the visible range from the first card with data
        const sourceChart = cards[0]._ctx.runtime.chart;
        const range = sourceChart.timeScale().getVisibleRange();
        if (!range) return;

        cards.slice(1).forEach(card => {
            try {
                card._ctx.runtime.chart.timeScale().setVisibleRange(range);
            } catch (_) {}
        });
    }

    // ─── Maximize (double-click to expand a single chart) ─────────────

    let maximizedCard = null;

    function setupMaximize(wrapper) {
        if (!wrapper) return;
        wrapper.querySelectorAll('.chart-card').forEach(card => {
            if (card._gridDblHandler) return; // already bound
            const handler = (e) => {
                // Ignore double-clicks on inputs/buttons
                if (e.target.closest('input, button, select, .chip')) return;
                if (currentLayout === '1x1') return;
                toggleMaximize(card, wrapper);
            };
            card.addEventListener('dblclick', handler);
            card._gridDblHandler = handler;
        });
    }

    function toggleMaximize(card, wrapper) {
        if (maximizedCard === card) {
            // Restore grid
            maximizedCard = null;
            wrapper.querySelectorAll('.chart-card').forEach(c => {
                c.style.display = '';
                c.classList.remove('grid-maximized');
            });
            const layout = getLayout(currentLayout);
            wrapper.style.gridTemplateColumns = `repeat(${layout.cols}, 1fr)`;
            wrapper.style.height = '';
            const visibleRows = layout.cols;
            const rowHeight = Math.floor(window.innerHeight / visibleRows);
            wrapper.style.gridTemplateRows = '';
            wrapper.style.gridAutoRows = `${rowHeight}px`;
            requestAnimationFrame(() => resizeAllCharts(wrapper));
        } else {
            // Maximize this card
            maximizedCard = card;
            wrapper.querySelectorAll('.chart-card').forEach(c => {
                if (c === card) {
                    c.style.display = '';
                    c.classList.add('grid-maximized');
                } else {
                    c.style.display = 'none';
                }
            });
            wrapper.style.gridTemplateColumns = '1fr';
            wrapper.style.gridTemplateRows = '1fr';
            wrapper.style.gridAutoRows = '';
            wrapper.style.height = 'calc(100vh - 190px)';
            requestAnimationFrame(() => {
                const chartBox = card.querySelector('.chart-box');
                const rt = card._ctx?.runtime;
                if (chartBox && rt?.chart) {
                    const w = chartBox.clientWidth;
                    const h = chartBox.clientHeight;
                    if (w > 0 && h > 0) {
                        try {
                            rt.chart.resize(w, h);
                            rt.chart.timeScale().fitContent();
                        } catch (_) {}
                    }
                }
            });
        }
    }

    // ─── Persistence ──────────────────────────────────────────────────

    function getActivePage() {
        if (window.PageManager && typeof window.PageManager.getActivePage === 'function') {
            return window.PageManager.getActivePage();
        }
        return 1;
    }

    function getActiveWrapper() {
        const page = document.querySelector(`.page[data-page="${getActivePage()}"]`);
        return page ? page.querySelector('#charts-wrapper, [id^="charts-wrapper"]') : document.getElementById('charts-wrapper');
    }

    function getPageLayouts() {
        try {
            const raw = localStorage.getItem('grid_layouts');
            return raw ? JSON.parse(raw) : {};
        } catch (_) {
            return {};
        }
    }

    function saveLayoutForPage(pageNum) {
        const layouts = getPageLayouts();
        layouts[pageNum] = currentLayout;
        localStorage.setItem('grid_layouts', JSON.stringify(layouts));
    }

    function loadLayoutForPage(pageNum) {
        const layouts = getPageLayouts();
        let id = layouts[pageNum] || '1';
        // Migrate old NxM format to column-only
        if (id.includes('x')) {
            id = id.split('x')[0];
        }
        // Ensure valid
        if (!LAYOUTS.find(l => l.id === id)) id = '1';
        return id;
    }

    // ─── UI ───────────────────────────────────────────────────────────

    function createLayoutSelector() {
        const container = document.createElement('div');
        container.id = 'grid-layout-selector';
        container.style.cssText = 'display:flex;align-items:center;gap:4px;margin-left:8px;';

        const label = document.createElement('span');
        label.textContent = 'Columns:';
        label.style.cssText = 'font-size:0.85rem;color:#888;';
        container.appendChild(label);

        const btnGroup = document.createElement('div');
        btnGroup.id = 'grid-layout-buttons';
        btnGroup.style.cssText = 'display:flex;gap:2px;';

        LAYOUTS.forEach(layout => {
            const btn = document.createElement('button');
            btn.dataset.layout = layout.id;
            btn.textContent = layout.label;
            btn.title = `${layout.cols} column${layout.cols > 1 ? 's' : ''}`;
            btn.style.cssText = 'padding:3px 7px;font-size:0.8rem;border:1px solid #999;border-radius:3px;background:#eee;cursor:pointer;min-width:36px;';
            btn.addEventListener('click', () => {
                applyLayout(layout.id);
            });
            btnGroup.appendChild(btn);
        });

        container.appendChild(btnGroup);

        // Sync toggle
        const syncBtn = document.createElement('button');
        syncBtn.id = 'grid-sync-btn';
        syncBtn.textContent = '\u21c4 Sync';
        syncBtn.title = 'Toggle crosshair sync across charts';
        syncBtn.style.cssText = 'padding:3px 7px;font-size:0.8rem;border:1px solid #2962ff;border-radius:3px;background:#2962ff;color:#fff;cursor:pointer;margin-left:4px;';
        syncBtn.addEventListener('click', () => {
            crosshairSyncEnabled = !crosshairSyncEnabled;
            syncBtn.style.background = crosshairSyncEnabled ? '#2962ff' : '#2a2e39';
            syncBtn.style.color = crosshairSyncEnabled ? '#fff' : '#888';
            syncBtn.style.borderColor = crosshairSyncEnabled ? '#2962ff' : '#444';

            const wrapper = getActiveWrapper();
            if (wrapper) {
                if (crosshairSyncEnabled && getLayout(currentLayout).cols > 1) {
                    setupCrosshairSync(wrapper);
                } else {
                    teardownCrosshairSync(wrapper);
                }
            }
        });
        container.appendChild(syncBtn);

        return container;
    }

    function updateLayoutSelector() {
        const buttons = document.querySelectorAll('#grid-layout-buttons button');
        buttons.forEach(btn => {
            const isActive = btn.dataset.layout === currentLayout;
            btn.style.background = isActive ? '#2962ff' : '#2a2e39';
            btn.style.color = isActive ? '#fff' : '#d1d4dc';
            btn.style.borderColor = isActive ? '#2962ff' : '#444';
        });
    }

    // ─── Init ─────────────────────────────────────────────────────────

    function initialize() {
        // Insert layout selector into top controls
        const topControls = document.getElementById('top-controls');
        if (topControls) {
            const selector = createLayoutSelector();
            // Insert before the "New Page" button
            const newPageBtn = document.getElementById('new-page-btn');
            if (newPageBtn) {
                topControls.insertBefore(selector, newPageBtn);
            } else {
                topControls.appendChild(selector);
            }
        }

        // Load saved layout for current page
        const savedLayout = loadLayoutForPage(getActivePage());
        if (savedLayout && savedLayout !== '1x1') {
            // Delay to let cards render first
            setTimeout(() => applyLayout(savedLayout), 500);
        }
        updateLayoutSelector();

        // Re-apply layout when page changes
        if (window.PageManager) {
            const origShowPage = window.PageManager.showPage;
            if (origShowPage) {
                window.PageManager.showPage = function(pageNum) {
                    origShowPage.call(this, pageNum);
                    const layout = loadLayoutForPage(pageNum);
                    currentLayout = layout;
                    setTimeout(() => applyLayout(layout, pageNum), 200);
                };
            }
        }

        // Resize charts on window resize
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => {
                if (currentLayout !== '1x1') {
                    const wrapper = getActiveWrapper();
                    if (wrapper) resizeAllCharts(wrapper);
                }
            }, 250);
        });

        console.log('[GridLayout] Initialized');
    }

    // Auto-initialize
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initialize);
    } else {
        initialize();
    }

    return {
        applyLayout,
        getCurrentLayout: () => currentLayout,
        getLayouts: () => LAYOUTS,
        resizeAllCharts,
        syncTimeRanges,
        setupCrosshairSync,
        teardownCrosshairSync,
        initialize
    };
})();
