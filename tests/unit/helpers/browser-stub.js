/**
 * Minimal window/document stub for loading browser modules in Node.
 * Only stubs what's actually used by the modules under test.
 */

function createWindowStub() {
  const window = {
    // ChartConfig stub - minimal config for tests
    ChartConfig: {
      DIMENSIONS: {
        CHART_MIN_HEIGHT: 400,
        CHART_MAX_HEIGHT: 800,
        PANE_HEIGHT: 100
      },
      UI: {
        FONT_MIN: 8,
        FONT_MAX: 24,
        FONT_DEFAULT: 12
      },
      STORAGE_KEYS: {
        CARDS: 'sandbox_cards'
      }
    },

    // ChartUtils stub - minimal utilities
    ChartUtils: {
      mapToObject(map) {
        if (!map || typeof map.entries !== 'function') return {};
        const obj = {};
        for (const [k, v] of map.entries()) {
          obj[k] = v;
        }
        return obj;
      },
      debounce(fn, ms) {
        return fn; // No actual debouncing in tests
      }
    },

    // ChartDomBuilder stub - for parseTickerInput
    ChartDomBuilder: {
      parseTickerInput(input) {
        if (!input || typeof input !== 'string') return [];
        // Split by comma first, then extract ticker from "TICKER - Name" format
        return input
          .split(',')
          .map(part => {
            const trimmed = part.trim();
            // Handle "TICKER - Company Name" format
            const dashIdx = trimmed.indexOf(' - ');
            const ticker = dashIdx > 0 ? trimmed.substring(0, dashIdx) : trimmed;
            return ticker.trim().toUpperCase();
          })
          .filter(Boolean);
      }
    },

    // PageManager stub
    PageManager: {
      ensurePage(page) {
        return null; // Return null wrapper in tests
      }
    },

    // Console passthrough
    console
  };

  // Document stub with style element support
  window.document = {
    addEventListener: () => {},
    getElementById: (id) => window._elements?.[id] || null,
    querySelector: () => null,
    querySelectorAll: () => [],
    createElement: (tag) => {
      const el = {
        tagName: tag.toUpperCase(),
        id: null,
        textContent: '',
        style: {},
        setAttribute: function(k, v) { this[k] = v; },
        getAttribute: function(k) { return this[k]; }
      };
      return el;
    },
    head: {
      appendChild: (el) => {
        if (!window._elements) window._elements = {};
        if (el.id) window._elements[el.id] = el;
      }
    }
  };

  return window;
}

module.exports = { createWindowStub };
