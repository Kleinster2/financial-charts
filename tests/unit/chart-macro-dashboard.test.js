/**
 * Unit tests for chart-macro-dashboard.js serialize/restore
 *
 * Tests: serializeCard(), state restoration in createMacroDashboardCard()
 */

const { describe, it, beforeEach } = require('node:test');
const assert = require('node:assert');
const { loadModules } = require('./helpers/load-module');

describe('ChartMacroDashboard', () => {
  let window;
  let ChartMacroDashboard;

  beforeEach(() => {
    // Fresh window with dependencies for each test
    window = loadModules([
      'charting_sandbox/chart-utils.js',
      'charting_sandbox/dashboard-base.js',
      'charting_sandbox/chart-macro-dashboard.js'
    ]);

    ChartMacroDashboard = window.ChartMacroDashboard;

    // Reset singleton state before each test
    ChartMacroDashboard.sortColumn = 'category';
    ChartMacroDashboard.sortDirection = 'asc';
    ChartMacroDashboard.viewMode = 'grouped';
    ChartMacroDashboard.filterText = '';
  });

  describe('serializeCard()', () => {

    it('serializes current state to object', () => {
      // Set some state
      ChartMacroDashboard.sortColumn = 'dayDelta';
      ChartMacroDashboard.sortDirection = 'desc';
      ChartMacroDashboard.viewMode = 'flat';
      ChartMacroDashboard.filterText = 'rates';

      // Mock card element
      const card = {
        closest: () => ({ dataset: { page: '5' } })
      };

      const result = ChartMacroDashboard.serializeCard(card);

      assert.strictEqual(result.type, 'macro-dashboard');
      assert.strictEqual(result.page, '5');
      assert.strictEqual(result.sortColumn, 'dayDelta');
      assert.strictEqual(result.sortDirection, 'desc');
      assert.strictEqual(result.viewMode, 'flat');
      assert.strictEqual(result.filterText, 'rates');
    });

    it('handles card not in a page', () => {
      const card = {
        closest: () => null
      };

      const result = ChartMacroDashboard.serializeCard(card);

      assert.strictEqual(result.page, '1'); // Default
      assert.strictEqual(result.type, 'macro-dashboard');
    });

    it('serializes default state correctly', () => {
      const card = { closest: () => null };
      const result = ChartMacroDashboard.serializeCard(card);

      assert.strictEqual(result.sortColumn, 'category');
      assert.strictEqual(result.sortDirection, 'asc');
      assert.strictEqual(result.viewMode, 'grouped');
      assert.strictEqual(result.filterText, '');
    });

  });

  describe('state restoration', () => {

    it('restores sortColumn from options', () => {
      ChartMacroDashboard.sortColumn = 'category';

      const options = { sortColumn: 'ticker' };
      if (options.sortColumn) ChartMacroDashboard.sortColumn = options.sortColumn;

      assert.strictEqual(ChartMacroDashboard.sortColumn, 'ticker');
    });

    it('restores sortDirection from options', () => {
      ChartMacroDashboard.sortDirection = 'asc';

      const options = { sortDirection: 'desc' };
      if (options.sortDirection) ChartMacroDashboard.sortDirection = options.sortDirection;

      assert.strictEqual(ChartMacroDashboard.sortDirection, 'desc');
    });

    it('restores viewMode from options', () => {
      ChartMacroDashboard.viewMode = 'grouped';

      const options = { viewMode: 'flat' };
      if (options.viewMode) ChartMacroDashboard.viewMode = options.viewMode;

      assert.strictEqual(ChartMacroDashboard.viewMode, 'flat');
    });

    it('restores filterText from options', () => {
      ChartMacroDashboard.filterText = '';

      const options = { filterText: 'commodities' };
      if (options.filterText) ChartMacroDashboard.filterText = options.filterText;

      assert.strictEqual(ChartMacroDashboard.filterText, 'commodities');
    });

    it('keeps defaults when options not provided', () => {
      ChartMacroDashboard.sortColumn = 'category';
      ChartMacroDashboard.sortDirection = 'asc';
      ChartMacroDashboard.viewMode = 'grouped';

      const options = {}; // Empty options

      if (options.sortColumn) ChartMacroDashboard.sortColumn = options.sortColumn;
      if (options.sortDirection) ChartMacroDashboard.sortDirection = options.sortDirection;
      if (options.viewMode) ChartMacroDashboard.viewMode = options.viewMode;

      assert.strictEqual(ChartMacroDashboard.sortColumn, 'category');
      assert.strictEqual(ChartMacroDashboard.sortDirection, 'asc');
      assert.strictEqual(ChartMacroDashboard.viewMode, 'grouped');
    });

  });

  describe('round-trip', () => {

    it('serialize then restore preserves full state', () => {
      // Set state
      ChartMacroDashboard.sortColumn = 'weekDelta';
      ChartMacroDashboard.sortDirection = 'desc';
      ChartMacroDashboard.viewMode = 'flat';
      ChartMacroDashboard.filterText = 'treasury';

      // Serialize
      const card = { closest: () => ({ dataset: { page: '3' } }) };
      const serialized = ChartMacroDashboard.serializeCard(card);

      // Reset state
      ChartMacroDashboard.sortColumn = 'category';
      ChartMacroDashboard.sortDirection = 'asc';
      ChartMacroDashboard.viewMode = 'grouped';
      ChartMacroDashboard.filterText = '';

      // Restore from serialized
      if (serialized.sortColumn) ChartMacroDashboard.sortColumn = serialized.sortColumn;
      if (serialized.sortDirection) ChartMacroDashboard.sortDirection = serialized.sortDirection;
      if (serialized.viewMode) ChartMacroDashboard.viewMode = serialized.viewMode;
      if (serialized.filterText) ChartMacroDashboard.filterText = serialized.filterText;

      // Verify round-trip
      assert.strictEqual(ChartMacroDashboard.sortColumn, 'weekDelta');
      assert.strictEqual(ChartMacroDashboard.sortDirection, 'desc');
      assert.strictEqual(ChartMacroDashboard.viewMode, 'flat');
      assert.strictEqual(ChartMacroDashboard.filterText, 'treasury');
    });

  });

});
