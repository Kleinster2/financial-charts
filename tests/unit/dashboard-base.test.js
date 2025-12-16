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

  describe('calcVisibleRange()', () => {

    it('returns shouldVirtualize=false for small datasets', () => {
      const result = DashboardBase.calcVisibleRange({
        scrollTop: 0,
        containerHeight: 500,
        totalRows: 50  // Below MIN_ROWS_TO_VIRTUALIZE (100)
      });
      assert.strictEqual(result.shouldVirtualize, false);
      assert.strictEqual(result.startIndex, 0);
      assert.strictEqual(result.endIndex, 50);
      assert.strictEqual(result.topPadding, 0);
      assert.strictEqual(result.bottomPadding, 0);
    });

    it('returns shouldVirtualize=true for large datasets', () => {
      const result = DashboardBase.calcVisibleRange({
        scrollTop: 0,
        containerHeight: 500,
        totalRows: 200  // Above MIN_ROWS_TO_VIRTUALIZE (100)
      });
      assert.strictEqual(result.shouldVirtualize, true);
    });

    it('calculates correct range at top of scroll', () => {
      const result = DashboardBase.calcVisibleRange({
        scrollTop: 0,
        containerHeight: 330,  // ~10 rows visible at 33px each
        totalRows: 200,
        rowHeight: 33,
        buffer: 5
      });
      // At top: startIndex should be 0 (max(0, 0 - 5))
      assert.strictEqual(result.startIndex, 0);
      // endIndex = min(200, 0 + 10 + 5) = 15
      assert.strictEqual(result.endIndex, 15);
      assert.strictEqual(result.topPadding, 0);
      // bottomPadding = (200 - 15) * 33 = 6105
      assert.strictEqual(result.bottomPadding, 185 * 33);
    });

    it('calculates correct range in middle of scroll', () => {
      const result = DashboardBase.calcVisibleRange({
        scrollTop: 1650,  // 50 rows down (50 * 33)
        containerHeight: 330,  // ~10 rows visible
        totalRows: 200,
        rowHeight: 33,
        buffer: 5
      });
      // firstVisible = floor(1650 / 33) = 50
      // startIndex = max(0, 50 - 5) = 45
      assert.strictEqual(result.startIndex, 45);
      // endIndex = min(200, 50 + 10 + 5) = 65
      assert.strictEqual(result.endIndex, 65);
      // topPadding = 45 * 33 = 1485
      assert.strictEqual(result.topPadding, 45 * 33);
      // bottomPadding = (200 - 65) * 33 = 4455
      assert.strictEqual(result.bottomPadding, 135 * 33);
    });

    it('calculates correct range at bottom of scroll', () => {
      const result = DashboardBase.calcVisibleRange({
        scrollTop: 6270,  // 190 rows down (190 * 33)
        containerHeight: 330,  // ~10 rows visible
        totalRows: 200,
        rowHeight: 33,
        buffer: 5
      });
      // firstVisible = floor(6270 / 33) = 190
      // startIndex = max(0, 190 - 5) = 185
      assert.strictEqual(result.startIndex, 185);
      // endIndex = min(200, 190 + 10 + 5) = 200
      assert.strictEqual(result.endIndex, 200);
      // topPadding = 185 * 33 = 6105
      assert.strictEqual(result.topPadding, 185 * 33);
      // bottomPadding = (200 - 200) * 33 = 0
      assert.strictEqual(result.bottomPadding, 0);
    });

    it('uses default values from VIRTUAL_SCROLL config', () => {
      const result = DashboardBase.calcVisibleRange({
        scrollTop: 0,
        containerHeight: 500,
        totalRows: 200
      });
      // Should use ROW_HEIGHT=33 and BUFFER_ROWS=10
      assert.strictEqual(result.shouldVirtualize, true);
      // With 500px / 33px = ~16 visible rows, buffer 10
      // endIndex = min(200, 0 + 16 + 10) = 26
      assert.ok(result.endIndex <= 30, 'endIndex should use default buffer');
    });

  });

  describe('createVirtualScrollHandler()', () => {

    it('returns a function', () => {
      const handler = DashboardBase.createVirtualScrollHandler(() => {});
      assert.strictEqual(typeof handler, 'function');
    });

    // Note: Testing the actual scroll behavior requires requestAnimationFrame
    // which is not available in Node.js. The handler itself works in browsers.
    // The calcVisibleRange logic is tested separately above.

  });

  describe('VIRTUAL_SCROLL config', () => {

    it('exports VIRTUAL_SCROLL constants', () => {
      assert.ok(DashboardBase.VIRTUAL_SCROLL);
      assert.strictEqual(typeof DashboardBase.VIRTUAL_SCROLL.ROW_HEIGHT, 'number');
      assert.strictEqual(typeof DashboardBase.VIRTUAL_SCROLL.BUFFER_ROWS, 'number');
      assert.strictEqual(typeof DashboardBase.VIRTUAL_SCROLL.MIN_ROWS_TO_VIRTUALIZE, 'number');
    });

    it('has sensible default values', () => {
      assert.ok(DashboardBase.VIRTUAL_SCROLL.ROW_HEIGHT > 20, 'Row height should be reasonable');
      assert.ok(DashboardBase.VIRTUAL_SCROLL.ROW_HEIGHT < 100, 'Row height should be reasonable');
      assert.ok(DashboardBase.VIRTUAL_SCROLL.BUFFER_ROWS >= 5, 'Buffer should be at least 5');
      assert.ok(DashboardBase.VIRTUAL_SCROLL.MIN_ROWS_TO_VIRTUALIZE >= 50, 'Threshold should be at least 50');
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
