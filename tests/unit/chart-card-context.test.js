/**
 * Unit tests for chart-card-context.js
 *
 * Tests: create(), serialize(), applyToCtx() round-trip, defaults, legacy aliases
 */

const { describe, it } = require('node:test');
const assert = require('node:assert');
const { loadModule } = require('./helpers/load-module');

// Load the module
const window = loadModule('charting_sandbox/chart-card-context.js');
const ChartCardContext = window.ChartCardContext;

describe('ChartCardContext', () => {

  describe('create()', () => {

    it('creates context with default values', () => {
      const card = { closest: () => null };
      const elements = { chartBox: {} };
      const ctx = ChartCardContext.create(card, elements, {});

      assert.strictEqual(ctx.showDiff, false);
      assert.strictEqual(ctx.showAvg, false);
      assert.strictEqual(ctx.showVolPane, false);
      assert.strictEqual(ctx.useRaw, false);
      assert.strictEqual(ctx.height, 400);
      assert.strictEqual(ctx.fontSize, 12);
      assert.strictEqual(ctx.decimalPrecision, 2);
      assert.strictEqual(ctx.starred, false);
      assert.strictEqual(ctx.tags.length, 0);
      assert.strictEqual(ctx.selectedTickers.size, 0);
    });

    it('creates context with provided options', () => {
      const card = { closest: () => null };
      const elements = { chartBox: {} };
      const ctx = ChartCardContext.create(card, elements, {
        initialShowDiff: true,
        initialUseRaw: true,
        initialHeight: 600,
        initialStarred: true,
        initialTags: ['tech', 'growth']
      });

      assert.strictEqual(ctx.showDiff, true);
      assert.strictEqual(ctx.useRaw, true);
      assert.strictEqual(ctx.height, 600);
      assert.strictEqual(ctx.starred, true);
      assert.strictEqual(ctx.tags.length, 2);
      assert.strictEqual(ctx.tags[0], 'tech');
      assert.strictEqual(ctx.tags[1], 'growth');
    });

    it('initializes empty ticker collections', () => {
      const ctx = ChartCardContext.create({ closest: () => null }, { chartBox: {} }, {});

      assert.ok(ctx.selectedTickers instanceof Set);
      assert.ok(ctx.hiddenTickers instanceof Set);
      assert.ok(ctx.multiplierMap instanceof Map);
      assert.ok(ctx.tickerColorMap instanceof Map);
    });

  });

  describe('serialize()', () => {

    it('serializes context to plain object', () => {
      const card = { closest: () => ({ dataset: { page: '2' } }) };
      const elements = { chartBox: {} };
      const ctx = ChartCardContext.create(card, elements, {
        initialShowDiff: true,
        initialTitle: 'Test Chart',
        initialStarred: true
      });
      ctx.selectedTickers.add('AAPL');
      ctx.selectedTickers.add('MSFT');

      const data = ChartCardContext.serialize(ctx);

      assert.strictEqual(data.page, '2');
      assert.strictEqual(data.showDiff, true);
      assert.strictEqual(data.title, 'Test Chart');
      assert.strictEqual(data.starred, true);
      assert.deepStrictEqual(data.tickers, ['AAPL', 'MSFT']);
    });

    it('serializes maps to objects', () => {
      const card = { closest: () => null };
      const ctx = ChartCardContext.create(card, { chartBox: {} }, {
        initialMultipliers: { AAPL: 2, MSFT: 0.5 },
        initialTickerColors: { AAPL: '#ff0000' }
      });

      const data = ChartCardContext.serialize(ctx);

      assert.strictEqual(data.multipliers.AAPL, 2);
      assert.strictEqual(data.multipliers.MSFT, 0.5);
      assert.strictEqual(data.tickerColors.AAPL, '#ff0000');
    });

    it('handles missing card gracefully', () => {
      const ctx = { selectedTickers: new Set(), hiddenTickers: new Set() };
      const data = ChartCardContext.serialize(ctx);

      assert.strictEqual(data.page, '1'); // Default page
      assert.strictEqual(data.type, null);
    });

  });

  describe('applyToCtx()', () => {

    it('applies saved data to context', () => {
      const card = { closest: () => null };
      const elements = { chartBox: {} };
      const ctx = ChartCardContext.create(card, elements, {});

      ChartCardContext.applyToCtx(ctx, {
        tickers: ['AAPL', 'MSFT'],
        showDiff: true,
        title: 'Restored Chart',
        height: 550,
        starred: true,
        tags: ['value']
      });

      assert.ok(ctx.selectedTickers.has('AAPL'));
      assert.ok(ctx.selectedTickers.has('MSFT'));
      assert.strictEqual(ctx.showDiff, true);
      assert.strictEqual(ctx.title, 'Restored Chart');
      assert.strictEqual(ctx.height, 550);
      assert.strictEqual(ctx.starred, true);
      assert.strictEqual(ctx.tags[0], 'value');
    });

    it('handles legacy ticker alias', () => {
      const ctx = ChartCardContext.create({ closest: () => null }, { chartBox: {} }, {});

      // Legacy format used 'ticker' (singular)
      ChartCardContext.applyToCtx(ctx, {
        ticker: 'SPY'
      });

      assert.ok(ctx.selectedTickers.has('SPY'));
    });

    it('handles legacy showVol alias', () => {
      const ctx = ChartCardContext.create({ closest: () => null }, { chartBox: {} }, {});

      // Legacy used 'showVol', new uses 'showVolPane'
      ChartCardContext.applyToCtx(ctx, {
        showVol: true
      });

      assert.strictEqual(ctx.showVolPane, true);
    });

    it('handles legacy range alias', () => {
      const ctx = ChartCardContext.create({ closest: () => null }, { chartBox: {} }, {});
      const range = { from: 1000, to: 2000 };

      ChartCardContext.applyToCtx(ctx, {
        range: range
      });

      assert.strictEqual(ctx.visibleRange.from, 1000);
      assert.strictEqual(ctx.visibleRange.to, 2000);
    });

    it('normalizes ticker input with "TICKER - Name" format (string input)', () => {
      const ctx = ChartCardContext.create({ closest: () => null }, { chartBox: {} }, {});

      // When tickers is a string, parseTickerInput extracts just the ticker symbols
      ChartCardContext.applyToCtx(ctx, {
        tickers: 'AAPL - Apple Inc, msft - Microsoft'
      });

      // Should extract just the ticker symbols, uppercased
      assert.ok(ctx.selectedTickers.has('AAPL'));
      assert.ok(ctx.selectedTickers.has('MSFT'));
      assert.strictEqual(ctx.selectedTickers.size, 2);
    });

    it('defaults lastLabelVisible to true when not specified', () => {
      const ctx = ChartCardContext.create({ closest: () => null }, { chartBox: {} }, {});

      ChartCardContext.applyToCtx(ctx, {});

      assert.strictEqual(ctx.lastLabelVisible, true);
    });

    it('restores maps from objects', () => {
      const ctx = ChartCardContext.create({ closest: () => null }, { chartBox: {} }, {});

      ChartCardContext.applyToCtx(ctx, {
        multipliers: { AAPL: 2 },
        tickerColors: { AAPL: '#ff0000' },
        priceScaleAssignments: { AAPL: 'left' }
      });

      assert.strictEqual(ctx.multiplierMap.get('AAPL'), 2);
      assert.strictEqual(ctx.tickerColorMap.get('AAPL'), '#ff0000');
      assert.strictEqual(ctx.priceScaleAssignmentMap.get('AAPL'), 'left');
    });

  });

  describe('round-trip', () => {

    it('serialize then applyToCtx preserves state', () => {
      const card = { closest: () => null };
      const elements = { chartBox: {} };

      // Create and modify context
      const ctx1 = ChartCardContext.create(card, elements, {});
      ctx1.selectedTickers.add('AAPL');
      ctx1.selectedTickers.add('MSFT');
      ctx1.hiddenTickers.add('MSFT');
      ctx1.showDiff = true;
      ctx1.useRaw = true;
      ctx1.height = 600;
      ctx1.title = 'Round Trip Test';
      ctx1.starred = true;
      ctx1.tags = ['test', 'unit'];
      ctx1.multiplierMap.set('AAPL', 2);
      ctx1.visibleRange = { from: 1000, to: 2000 };

      // Serialize
      const data = ChartCardContext.serialize(ctx1);

      // Create new context and apply
      const ctx2 = ChartCardContext.create({ closest: () => null }, { chartBox: {} }, {});
      ChartCardContext.applyToCtx(ctx2, data);

      // Verify state preserved
      assert.ok(ctx2.selectedTickers.has('AAPL'));
      assert.ok(ctx2.selectedTickers.has('MSFT'));
      assert.ok(ctx2.hiddenTickers.has('MSFT'));
      assert.strictEqual(ctx2.showDiff, true);
      assert.strictEqual(ctx2.useRaw, true);
      assert.strictEqual(ctx2.height, 600);
      assert.strictEqual(ctx2.title, 'Round Trip Test');
      assert.strictEqual(ctx2.starred, true);
      assert.strictEqual(ctx2.tags[0], 'test');
      assert.strictEqual(ctx2.tags[1], 'unit');
      assert.strictEqual(ctx2.multiplierMap.get('AAPL'), 2);
      assert.strictEqual(ctx2.visibleRange.from, 1000);
      assert.strictEqual(ctx2.visibleRange.to, 2000);
    });

  });

  describe('initRuntime()', () => {

    it('initializes runtime state', () => {
      const ctx = ChartCardContext.create({ closest: () => null }, { chartBox: {} }, {});
      const rt = ChartCardContext.initRuntime(ctx);

      assert.ok(rt.priceSeriesMap instanceof Map);
      assert.ok(rt.rawPriceMap instanceof Map);
      assert.strictEqual(rt.chart, null);
      assert.strictEqual(ctx.runtime, rt);
    });

  });

});
