/**
 * Chart Grid Layout Module
 *
 * Provides TradingView-style multi-chart grid layouts (2x1, 2x2, 3x2, etc.)
 * with crosshair sync across all visible charts.
 *
 * Exports: window.GridLayout
 */

window.GridLayout = (() => {
    // Available layouts: [cols, rows, label]
    const LAYOUTS = [
        { id: '1x1', cols: 1, rows: null, label: '1\u00d71' },
        { id: '2x1', cols: 2, rows: 1,    label: '2\u00d71' },
        { id: '1x2', cols: 1, rows: 2,    label: '1\u00d72' },
        { id: '2x2', cols: 2, rows: 2,    label: '2\u00d72' },
        { id: '3x2', cols: 3, rows: 2,    label: '3\u00d72' },
        { id: '2x3', cols: 2, rows: 3,    label: '2\u00d73' },
        { id: '3x3', cols: 3, rows: 3,    label: '3\u00d73' },
        { id: '4x3', cols: 4, rows: 3,    label: '4\u00d73' },
    ];

    let currentLayout = '1x1';
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

        if (layout.id === '1x1') {
            // Default stacked layout
            wrapper.style.display = '';
            wrapper.style.gridTemplateColumns = '';
            wrapper.style.gridTemplateRows = '';
            wrapper.style.gap = '';
            wrapper.classList.remove('grid-layout');

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
            wrapper.style.gap = '8px';
            wrapper.classList.add('grid-layout');

            // Let rows auto-size based on content
            if (layout.rows) {
                wrapper.style.gridTemplateRows = `repeat(${layout.rows}, 1fr)`;
            } else {
                wrapper.style.gridTemplateRows = '';
            }

            // Compact mode for all cards in grid
            wrapper.querySelectorAll('.chart-card').forEach(card => {
                card.classList.add('grid-compact');
            });
        }

        // Setup ResizeObserver for auto-resize in grid mode
        setupResizeObserver(wrapper, layout.id !== '1x1');

        // Resize all charts to fit their new containers
        // Double rAF ensures the grid layout has been computed
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                resizeAllCharts(wrapper);
                // Setup crosshair sync for grid layouts
                if (layout.id !== '1x1' && crosshairSyncEnabled) {
                    setupCrosshairSync(wrapper);
                } else {
                    teardownCrosshairSync(wrapper);
                }
            });
        });

        // Persist
        saveLayoutForPage(pageNum || getActivePage());
        updateLayoutSelector();
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
        return layouts[pageNum] || '1x1';
    }

    // ─── UI ───────────────────────────────────────────────────────────

    function createLayoutSelector() {
        const container = document.createElement('div');
        container.id = 'grid-layout-selector';
        container.style.cssText = 'display:flex;align-items:center;gap:4px;margin-left:8px;';

        const label = document.createElement('span');
        label.textContent = 'Layout:';
        label.style.cssText = 'font-size:0.85rem;color:#666;';
        container.appendChild(label);

        const btnGroup = document.createElement('div');
        btnGroup.id = 'grid-layout-buttons';
        btnGroup.style.cssText = 'display:flex;gap:2px;';

        LAYOUTS.forEach(layout => {
            const btn = document.createElement('button');
            btn.dataset.layout = layout.id;
            btn.textContent = layout.label;
            btn.title = `${layout.cols} columns \u00d7 ${layout.rows || 'auto'} rows`;
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
        syncBtn.style.cssText = 'padding:3px 7px;font-size:0.8rem;border:1px solid #007bff;border-radius:3px;background:#007bff;color:#fff;cursor:pointer;margin-left:4px;';
        syncBtn.addEventListener('click', () => {
            crosshairSyncEnabled = !crosshairSyncEnabled;
            syncBtn.style.background = crosshairSyncEnabled ? '#007bff' : '#eee';
            syncBtn.style.color = crosshairSyncEnabled ? '#fff' : '#666';
            syncBtn.style.borderColor = crosshairSyncEnabled ? '#007bff' : '#999';

            const wrapper = getActiveWrapper();
            if (wrapper) {
                if (crosshairSyncEnabled && currentLayout !== '1x1') {
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
            btn.style.background = isActive ? '#666' : '#eee';
            btn.style.color = isActive ? '#fff' : '#333';
            btn.style.borderColor = isActive ? '#666' : '#999';
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
