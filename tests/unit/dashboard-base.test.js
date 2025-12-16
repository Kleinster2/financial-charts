/**
 * Unit tests for dashboard-base.js
 *
 * Tests: filterAndSortData(), escapeHtml(), renderStatusRow()
 */

const { describe, it } = require('node:test');
const assert = require('node:assert');
const { loadModules } = require('./helpers/load-module');

// Load dependencies in order (ChartUtils first, then DashboardBase)
const window = loadModules([
  'charting_sandbox/chart-utils.js',
  'charting_sandbox/dashboard-base.js'
]);
const DashboardBase = window.DashboardBase;

describe('DashboardBase', () => {

  describe('filterAndSortData()', () => {

    const testData = [
      { ticker: 'AAPL', name: 'Apple Inc', price: 150, change: 2.5 },
      { ticker: 'MSFT', name: 'Microsoft', price: 380, change: -1.2 },
      { ticker: 'GOOGL', name: 'Alphabet', price: 140, change: 0.8 },
      { ticker: 'AMZN', name: 'Amazon', price: 175, change: null },
      { ticker: 'META', name: null, price: 500, change: 3.1 }
    ];

    it('returns all data when no filter', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        sortColumn: 'ticker',
        sortDirection: 'asc'
      });
      assert.strictEqual(result.length, 5);
    });

    it('filters data with filterFn', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        filterText: 'apple',
        filterFn: (d, text) => d.name && d.name.toLowerCase().includes(text),
        sortColumn: 'ticker',
        sortDirection: 'asc'
      });
      assert.strictEqual(result.length, 1);
      assert.strictEqual(result[0].ticker, 'AAPL');
    });

    it('filters by ticker', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        filterText: 'ms',
        filterFn: (d, text) => d.ticker.toLowerCase().includes(text),
        sortColumn: 'ticker',
        sortDirection: 'asc'
      });
      assert.strictEqual(result.length, 1);
      assert.strictEqual(result[0].ticker, 'MSFT');
    });

    it('sorts strings ascending', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        sortColumn: 'ticker',
        sortDirection: 'asc'
      });
      assert.strictEqual(result[0].ticker, 'AAPL');
      assert.strictEqual(result[4].ticker, 'MSFT');
    });

    it('sorts strings descending', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        sortColumn: 'ticker',
        sortDirection: 'desc'
      });
      assert.strictEqual(result[0].ticker, 'MSFT');
      assert.strictEqual(result[4].ticker, 'AAPL');
    });

    it('sorts numeric columns ascending', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        sortColumn: 'price',
        sortDirection: 'asc',
        numericColumns: ['price', 'change']
      });
      assert.strictEqual(result[0].ticker, 'GOOGL'); // 140
      assert.strictEqual(result[4].ticker, 'META');  // 500
    });

    it('sorts numeric columns descending', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        sortColumn: 'price',
        sortDirection: 'desc',
        numericColumns: ['price', 'change']
      });
      assert.strictEqual(result[0].ticker, 'META');  // 500
      assert.strictEqual(result[4].ticker, 'GOOGL'); // 140
    });

    it('handles null values - sorts to end', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        sortColumn: 'change',
        sortDirection: 'asc',
        numericColumns: ['price', 'change']
      });
      // Null should be at end regardless of direction
      assert.strictEqual(result[4].ticker, 'AMZN');
    });

    it('handles null values - sorts to end descending too', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        sortColumn: 'change',
        sortDirection: 'desc',
        numericColumns: ['price', 'change']
      });
      // Null should still be at end
      assert.strictEqual(result[4].ticker, 'AMZN');
    });

    it('uses getSortValue when provided', () => {
      const dataWithPages = [
        { ticker: 'A', pages: [1, 2, 3] },
        { ticker: 'B', pages: [1] },
        { ticker: 'C', pages: [1, 2] }
      ];
      const result = DashboardBase.filterAndSortData({
        data: dataWithPages,
        sortColumn: 'pages',
        sortDirection: 'desc',
        numericColumns: ['pages'],
        getSortValue: (d, col) => col === 'pages' ? d.pages.length : d[col]
      });
      assert.strictEqual(result[0].ticker, 'A'); // 3 pages
      assert.strictEqual(result[2].ticker, 'B'); // 1 page
    });

    it('handles empty data array', () => {
      const result = DashboardBase.filterAndSortData({
        data: [],
        sortColumn: 'ticker',
        sortDirection: 'asc'
      });
      assert.strictEqual(result.length, 0);
    });

    it('handles undefined data', () => {
      const result = DashboardBase.filterAndSortData({
        sortColumn: 'ticker',
        sortDirection: 'asc'
      });
      assert.strictEqual(result.length, 0);
    });

    it('normalizes filter text (trim + lowercase)', () => {
      const result = DashboardBase.filterAndSortData({
        data: testData,
        filterText: '  AAPL  ',
        filterFn: (d, text) => d.ticker.toLowerCase() === text,
        sortColumn: 'ticker',
        sortDirection: 'asc'
      });
      assert.strictEqual(result.length, 1);
      assert.strictEqual(result[0].ticker, 'AAPL');
    });

  });

  describe('escapeHtml()', () => {

    it('escapes < and >', () => {
      const result = DashboardBase.escapeHtml('<script>alert("xss")</script>');
      assert.ok(!result.includes('<'));
      assert.ok(!result.includes('>'));
      assert.ok(result.includes('&lt;'));
      assert.ok(result.includes('&gt;'));
    });

    it('escapes & and quotes', () => {
      const result = DashboardBase.escapeHtml('A & B "quoted" \'apostrophe\'');
      assert.ok(result.includes('&amp;'));
      assert.ok(result.includes('&quot;'));
      assert.ok(result.includes('&#39;'));
    });

    it('handles null/undefined', () => {
      assert.strictEqual(DashboardBase.escapeHtml(null), '');
      assert.strictEqual(DashboardBase.escapeHtml(undefined), '');
    });

    it('converts numbers to string', () => {
      assert.strictEqual(DashboardBase.escapeHtml(123), '123');
    });

  });

});
