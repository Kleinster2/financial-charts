/**
 * Chart Card Registry Module
 *
 * Extensible registry for special card types (dashboard, dendrograms, etc.)
 * Extracted from card.js to separate app-wide type wiring from card orchestration.
 *
 * Exports: window.ChartCardRegistry
 */

window.ChartCardRegistry = (() => {
    const WRAPPER_ID = 'charts-wrapper';

    // ═══════════════════════════════════════════════════════════════════════
    // CARD TYPE REGISTRY
    // Extensible registry for special card types (dashboard, dendrograms, etc.)
    // ═══════════════════════════════════════════════════════════════════════
    const registry = {
        'dashboard': {
            module: () => window.ChartDashboard,
            create: (wrapper, opts) => window.ChartDashboard.createDashboardCard(wrapper),
            restore: (cardData, wrapper) => ({ type: 'dashboard', wrapperEl: wrapper })
        },
        'macro-dashboard': {
            module: () => window.ChartMacroDashboard,
            create: (wrapper, opts) => window.ChartMacroDashboard.createMacroDashboardCard(wrapper),
            restore: (cardData, wrapper) => ({ type: 'macro-dashboard', wrapperEl: wrapper })
        },
        'dendrograms': {
            module: () => window.ChartDendrograms,
            create: (wrapper, opts) => window.ChartDendrograms.createDendrogramCard(wrapper),
            restore: (cardData, wrapper) => ({ type: 'dendrograms', wrapperEl: wrapper })
        },
        'thesis-performance': {
            module: () => window.ChartThesisPerformance,
            create: (wrapper, opts) => window.ChartThesisPerformance.createThesisPerformanceCard(wrapper, { thesisId: opts.thesisId }),
            restore: (cardData, wrapper) => ({ type: 'thesis-performance', wrapperEl: wrapper, thesisId: cardData.thesisId })
        }
    };

    /**
     * Get a registered type handler
     * @param {string} type - Card type name
     * @returns {Object|null} Type handler or null if not registered
     */
    function getHandler(type) {
        return registry[type] || null;
    }

    /**
     * Check if a type is registered
     * @param {string} type - Card type name
     * @returns {boolean}
     */
    function hasType(type) {
        return type in registry;
    }

    /**
     * Dispatch card creation to a registered type handler
     * @param {string} type - Card type name
     * @param {HTMLElement} wrapper - Wrapper element
     * @param {Object} options - Creation options
     * @returns {HTMLElement|null} Created card element or null
     */
    function dispatchCreate(type, wrapper, options) {
        const handler = registry[type];
        if (!handler) return null;

        const module = handler.module();
        if (!wrapper || !module) {
            console.error(`${type} module not loaded`);
            return null;
        }

        console.log(`[ChartCardRegistry] Creating ${type} card`);
        return handler.create(wrapper, options);
    }

    /**
     * Restore a card from saved data
     * Uses createChartCard (must be available on window)
     * @param {Object} cardData - Saved card configuration
     */
    function restoreCard(cardData) {
        const wrapper = window.PageManager ? window.PageManager.ensurePage(cardData.page || '1') : null;

        // Check type registry for special card types
        const handler = registry[cardData.type];
        if (handler) {
            console.log(`[Restore] Creating ${cardData.type} card on page`, cardData.page);
            window.createChartCard(handler.restore(cardData, wrapper));
            return;
        }

        // Normal chart card: pass saved payload through directly
        // Schema owned by ChartCardContext.serialize/applyToCtx
        window.createChartCard({
            ...cardData,
            wrapperEl: wrapper,
            hydrateData: cardData
        });
    }

    /**
     * Register a new card type (for extensibility)
     * @param {string} type - Card type name
     * @param {Object} handler - Handler object with module, create, restore functions
     */
    function register(type, handler) {
        if (registry[type]) {
            console.warn(`[ChartCardRegistry] Overwriting existing type: ${type}`);
        }
        registry[type] = handler;
    }

    return {
        getHandler,
        hasType,
        dispatchCreate,
        restoreCard,
        register,
        WRAPPER_ID
    };

})();
