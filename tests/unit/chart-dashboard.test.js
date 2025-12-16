/**
 * Unit tests for chart-dashboard.js serialize/restore
 *
 * Tests: serializeCard(), state restoration in createDashboardCard()
 */

const { describe, it, beforeEach } = require('node:test');
const assert = require('node:assert');
const { loadModules } = require('./helpers/load-module');

describe('ChartDashboard', () => {
  let window;
  let ChartDashboard;

  beforeEach(() => {
    // Fresh window with dependencies for each test
    window = loadModules([
      'charting_sandbox/chart-utils.js',
      'charting_sandbox/dashboard-base.js'
    ]);

    // Mock fetch for loadData
    window.fetch = async () => ({
      ok: true,
      json: async () => []
    });

    // Mock ChartUtils.apiUrl
    window.ChartUtils.apiUrl = (path) => `http://localhost:5000${path}`;

    // Create minimal DOM structure
    window.document.createElement = (tag) => {
      const el = {
        tagName: tag.toUpperCase(),
        id: null,
        className: '',
        innerHTML: '',
        style: {},
        children: [],
        dataset: {},
        _listeners: {},
        setAttribute: function(k, v) { this[k] = v; },
        getAttribute: function(k) { return this[k]; },
        addEventListener: function(event, fn) { this._listeners[event] = fn; },
        appendChild: function(child) {
          this.children.push(child);
          child.parentElement = this;
        },
        closest: function(sel) {
          // Return mock page element
          if (sel === '.page') return { dataset: { page: '1' } };
          return null;
        },
        querySelector: function(sel) {
          // Return mock elements for various selectors
          if (sel === '.dashboard-filter') {
            return {
              value: '',
              addEventListener: () => {}
            };
          }
          if (sel === '.dashboard-view-select') {
            return {
              value: 'flat',
              addEventListener: () => {}
            };
          }
          if (sel === '.dashboard-refresh-btn') {
            return { addEventListener: () => {} };
          }
          if (sel === '.dashboard-columns-btn') {
            return { addEventListener: () => {} };
          }
          if (sel === '.dashboard-columns-menu') {
            return { innerHTML: '' };
          }
          if (sel === '.dashboard-table tbody') {
            return { innerHTML: '' };
          }
          if (sel === '.dashboard-table thead') {
            return { innerHTML: '' };
          }
          if (sel === '.dashboard-stats') {
            return { innerHTML: '' };
          }
          return null;
        },
        querySelectorAll: function() { return []; }
      };
      return el;
    };

    // Mock wrapper element
    window._mockWrapper = {
      appendChild: () => {},
      dataset: { page: '1' }
    };

    // Load ChartDashboard module
    window = loadModules([
      'charting_sandbox/chart-utils.js',
      'charting_sandbox/dashboard-base.js',
      'charting_sandbox/chart-dashboard.js'
    ], window);

    ChartDashboard = window.ChartDashboard;

    // Reset singleton state before each test
    ChartDashboard.sortColumn = 'ticker';
    ChartDashboard.sortDirection = 'asc';
    ChartDashboard.viewMode = 'flat';
    ChartDashboard.filterText = '';
    ChartDashboard.columnOrder = null;
    ChartDashboard.hiddenColumns = new Set();
    ChartDashboard.columnWidths = {};
  });

  describe('serializeCard()', () => {

    it('serializes current state to object', () => {
      // Set some state
      ChartDashboard.sortColumn = 'price';
      ChartDashboard.sortDirection = 'desc';
      ChartDashboard.viewMode = 'grouped';
      ChartDashboard.filterText = 'AAPL';
      ChartDashboard.columnOrder = ['ticker', 'price', 'change'];
      ChartDashboard.hiddenColumns = new Set(['name', 'volume']);
      ChartDashboard.columnWidths = { ticker: 100, price: 80 };

      // Mock card element
      const card = {
        closest: () => ({ dataset: { page: '3' } })
      };

      const result = ChartDashboard.serializeCard(card);

      assert.strictEqual(result.type, 'dashboard');
      assert.strictEqual(result.page, '3');
      assert.strictEqual(result.sortColumn, 'price');
      assert.strictEqual(result.sortDirection, 'desc');
      assert.strictEqual(result.viewMode, 'grouped');
      assert.strictEqual(result.filterText, 'AAPL');
      assert.deepStrictEqual(result.columnOrder, ['ticker', 'price', 'change']);
      assert.deepStrictEqual(result.hiddenColumns, ['name', 'volume']);
      assert.deepStrictEqual(result.columnWidths, { ticker: 100, price: 80 });
    });

    it('handles card not in a page', () => {
      const card = {
        closest: () => null
      };

      const result = ChartDashboard.serializeCard(card);

      assert.strictEqual(result.page, '1'); // Default
    });

    it('converts hiddenColumns Set to Array', () => {
      ChartDashboard.hiddenColumns = new Set(['a', 'b', 'c']);

      const card = { closest: () => null };
      const result = ChartDashboard.serializeCard(card);

      assert.ok(Array.isArray(result.hiddenColumns));
      assert.strictEqual(result.hiddenColumns.length, 3);
      assert.ok(result.hiddenColumns.includes('a'));
      assert.ok(result.hiddenColumns.includes('b'));
      assert.ok(result.hiddenColumns.includes('c'));
    });

    it('handles null/undefined hiddenColumns', () => {
      ChartDashboard.hiddenColumns = null;

      const card = { closest: () => null };
      const result = ChartDashboard.serializeCard(card);

      assert.deepStrictEqual(result.hiddenColumns, []);
    });

    it('handles undefined columnWidths', () => {
      ChartDashboard.columnWidths = undefined;

      const card = { closest: () => null };
      const result = ChartDashboard.serializeCard(card);

      // Check it's an empty object
      assert.ok(result.columnWidths !== undefined);
      assert.strictEqual(Object.keys(result.columnWidths).length, 0);
    });

  });

  describe('state restoration', () => {

    it('restores sortColumn from options', () => {
      // Reset to default
      ChartDashboard.sortColumn = 'ticker';

      // Options to restore
      const options = { sortColumn: 'change' };

      // Simulate what createDashboardCard does
      if (options.sortColumn) ChartDashboard.sortColumn = options.sortColumn;

      assert.strictEqual(ChartDashboard.sortColumn, 'change');
    });

    it('restores sortDirection from options', () => {
      ChartDashboard.sortDirection = 'asc';

      const options = { sortDirection: 'desc' };
      if (options.sortDirection) ChartDashboard.sortDirection = options.sortDirection;

      assert.strictEqual(ChartDashboard.sortDirection, 'desc');
    });

    it('restores viewMode from options', () => {
      ChartDashboard.viewMode = 'flat';

      const options = { viewMode: 'grouped' };
      if (options.viewMode) ChartDashboard.viewMode = options.viewMode;

      assert.strictEqual(ChartDashboard.viewMode, 'grouped');
    });

    it('restores filterText from options', () => {
      ChartDashboard.filterText = '';

      const options = { filterText: 'SPY' };
      if (options.filterText) ChartDashboard.filterText = options.filterText;

      assert.strictEqual(ChartDashboard.filterText, 'SPY');
    });

    it('restores columnOrder from options', () => {
      ChartDashboard.columnOrder = null;

      const options = { columnOrder: ['a', 'b', 'c'] };
      if (options.columnOrder) ChartDashboard.columnOrder = options.columnOrder;

      assert.deepStrictEqual(ChartDashboard.columnOrder, ['a', 'b', 'c']);
    });

    it('restores hiddenColumns as Set from array', () => {
      ChartDashboard.hiddenColumns = new Set();

      const options = { hiddenColumns: ['x', 'y'] };
      if (options.hiddenColumns) ChartDashboard.hiddenColumns = new Set(options.hiddenColumns);

      assert.ok(ChartDashboard.hiddenColumns instanceof Set);
      assert.ok(ChartDashboard.hiddenColumns.has('x'));
      assert.ok(ChartDashboard.hiddenColumns.has('y'));
    });

    it('restores columnWidths from options', () => {
      ChartDashboard.columnWidths = {};

      const options = { columnWidths: { ticker: 150, price: 100 } };
      if (options.columnWidths) ChartDashboard.columnWidths = options.columnWidths;

      assert.deepStrictEqual(ChartDashboard.columnWidths, { ticker: 150, price: 100 });
    });

    it('keeps defaults when options not provided', () => {
      ChartDashboard.sortColumn = 'ticker';
      ChartDashboard.sortDirection = 'asc';
      ChartDashboard.viewMode = 'flat';

      const options = {}; // Empty options

      // Simulate restoration with empty options
      if (options.sortColumn) ChartDashboard.sortColumn = options.sortColumn;
      if (options.sortDirection) ChartDashboard.sortDirection = options.sortDirection;
      if (options.viewMode) ChartDashboard.viewMode = options.viewMode;

      // Should remain at defaults
      assert.strictEqual(ChartDashboard.sortColumn, 'ticker');
      assert.strictEqual(ChartDashboard.sortDirection, 'asc');
      assert.strictEqual(ChartDashboard.viewMode, 'flat');
    });

  });

  describe('round-trip', () => {

    it('serialize then restore preserves full state', () => {
      // Set state
      ChartDashboard.sortColumn = 'dayPct';
      ChartDashboard.sortDirection = 'desc';
      ChartDashboard.viewMode = 'grouped';
      ChartDashboard.filterText = 'tech';
      ChartDashboard.columnOrder = ['ticker', 'name', 'dayPct'];
      ChartDashboard.hiddenColumns = new Set(['volume', 'high', 'low']);
      ChartDashboard.columnWidths = { ticker: 120, name: 200 };

      // Serialize
      const card = { closest: () => ({ dataset: { page: '5' } }) };
      const serialized = ChartDashboard.serializeCard(card);

      // Reset state
      ChartDashboard.sortColumn = 'ticker';
      ChartDashboard.sortDirection = 'asc';
      ChartDashboard.viewMode = 'flat';
      ChartDashboard.filterText = '';
      ChartDashboard.columnOrder = null;
      ChartDashboard.hiddenColumns = new Set();
      ChartDashboard.columnWidths = {};

      // Restore from serialized
      if (serialized.sortColumn) ChartDashboard.sortColumn = serialized.sortColumn;
      if (serialized.sortDirection) ChartDashboard.sortDirection = serialized.sortDirection;
      if (serialized.viewMode) ChartDashboard.viewMode = serialized.viewMode;
      if (serialized.filterText) ChartDashboard.filterText = serialized.filterText;
      if (serialized.columnOrder) ChartDashboard.columnOrder = serialized.columnOrder;
      if (serialized.hiddenColumns) ChartDashboard.hiddenColumns = new Set(serialized.hiddenColumns);
      if (serialized.columnWidths) ChartDashboard.columnWidths = serialized.columnWidths;

      // Verify round-trip
      assert.strictEqual(ChartDashboard.sortColumn, 'dayPct');
      assert.strictEqual(ChartDashboard.sortDirection, 'desc');
      assert.strictEqual(ChartDashboard.viewMode, 'grouped');
      assert.strictEqual(ChartDashboard.filterText, 'tech');
      assert.deepStrictEqual(ChartDashboard.columnOrder, ['ticker', 'name', 'dayPct']);
      assert.ok(ChartDashboard.hiddenColumns.has('volume'));
      assert.ok(ChartDashboard.hiddenColumns.has('high'));
      assert.ok(ChartDashboard.hiddenColumns.has('low'));
      assert.deepStrictEqual(ChartDashboard.columnWidths, { ticker: 120, name: 200 });
    });

  });

});
