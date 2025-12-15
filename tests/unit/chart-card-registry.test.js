/**
 * Unit tests for chart-card-registry.js
 *
 * Tests: hasType(), register(), dispatchCreate(), getHandler()
 */

const { describe, it, beforeEach } = require('node:test');
const assert = require('node:assert');
const { loadModule, createWindowStub } = require('./helpers/load-module');

describe('ChartCardRegistry', () => {

  let window;
  let ChartCardRegistry;

  beforeEach(() => {
    // Fresh load for each test to reset registry state
    window = loadModule('charting_sandbox/chart-card-registry.js');
    ChartCardRegistry = window.ChartCardRegistry;
  });

  describe('hasType()', () => {

    it('returns true for registered types', () => {
      assert.strictEqual(ChartCardRegistry.hasType('dashboard'), true);
      assert.strictEqual(ChartCardRegistry.hasType('macro-dashboard'), true);
      assert.strictEqual(ChartCardRegistry.hasType('dendrograms'), true);
      assert.strictEqual(ChartCardRegistry.hasType('thesis-performance'), true);
    });

    it('returns false for unregistered types', () => {
      assert.strictEqual(ChartCardRegistry.hasType('unknown'), false);
      assert.strictEqual(ChartCardRegistry.hasType(''), false);
      assert.strictEqual(ChartCardRegistry.hasType(null), false);
    });

  });

  describe('getHandler()', () => {

    it('returns handler for registered types', () => {
      const handler = ChartCardRegistry.getHandler('dashboard');

      assert.ok(handler);
      assert.strictEqual(typeof handler.module, 'function');
      assert.strictEqual(typeof handler.create, 'function');
      assert.strictEqual(typeof handler.restore, 'function');
    });

    it('returns null for unregistered types', () => {
      assert.strictEqual(ChartCardRegistry.getHandler('unknown'), null);
      assert.strictEqual(ChartCardRegistry.getHandler(''), null);
    });

  });

  describe('register()', () => {

    it('registers a new type', () => {
      const customHandler = {
        module: () => ({ custom: true }),
        create: (wrapper, opts) => ({ created: true }),
        restore: (data, wrapper) => ({ restored: true })
      };

      ChartCardRegistry.register('custom-type', customHandler);

      assert.strictEqual(ChartCardRegistry.hasType('custom-type'), true);
      assert.strictEqual(ChartCardRegistry.getHandler('custom-type'), customHandler);
    });

    it('overwrites existing type (with warning)', () => {
      const originalHandler = ChartCardRegistry.getHandler('dashboard');

      const newHandler = {
        module: () => ({ replaced: true }),
        create: () => null,
        restore: () => null
      };

      ChartCardRegistry.register('dashboard', newHandler);

      assert.strictEqual(ChartCardRegistry.getHandler('dashboard'), newHandler);
      assert.notStrictEqual(ChartCardRegistry.getHandler('dashboard'), originalHandler);
    });

  });

  describe('dispatchCreate()', () => {

    it('returns null for unregistered types', () => {
      const result = ChartCardRegistry.dispatchCreate('unknown', {}, {});
      assert.strictEqual(result, null);
    });

    it('returns null when module is not loaded', () => {
      // Dashboard module is not actually loaded in test environment
      const wrapper = {};
      const result = ChartCardRegistry.dispatchCreate('dashboard', wrapper, {});

      // Should return null because window.ChartDashboard is undefined
      assert.strictEqual(result, null);
    });

    it('calls create when module is available', () => {
      // Register a type with a mock module
      let createCalled = false;
      let passedWrapper = null;
      let passedOpts = null;

      const mockHandler = {
        module: () => ({ available: true }),
        create: (wrapper, opts) => {
          createCalled = true;
          passedWrapper = wrapper;
          passedOpts = opts;
          return { type: 'mock-card' };
        },
        restore: () => ({})
      };

      ChartCardRegistry.register('mock-type', mockHandler);

      const wrapper = { id: 'test-wrapper' };
      const opts = { option1: 'value1' };
      const result = ChartCardRegistry.dispatchCreate('mock-type', wrapper, opts);

      assert.strictEqual(createCalled, true);
      assert.strictEqual(passedWrapper, wrapper);
      assert.strictEqual(passedOpts, opts);
      assert.deepStrictEqual(result, { type: 'mock-card' });
    });

    it('returns null when wrapper is missing', () => {
      const mockHandler = {
        module: () => ({ available: true }),
        create: () => ({}),
        restore: () => ({})
      };

      ChartCardRegistry.register('mock-type', mockHandler);

      const result = ChartCardRegistry.dispatchCreate('mock-type', null, {});
      assert.strictEqual(result, null);
    });

  });

  describe('restoreCard()', () => {

    it('calls createChartCard for normal cards', () => {
      let createChartCardCalled = false;
      let passedOptions = null;

      window.createChartCard = (opts) => {
        createChartCardCalled = true;
        passedOptions = opts;
      };

      ChartCardRegistry.restoreCard({
        page: '1',
        tickers: ['SPY'],
        title: 'Test'
      });

      assert.strictEqual(createChartCardCalled, true);
      assert.ok(passedOptions.hydrateData);
      assert.deepStrictEqual(passedOptions.tickers, ['SPY']);
    });

    it('uses handler.restore for registered types', () => {
      let createChartCardCalled = false;
      let passedOptions = null;

      window.createChartCard = (opts) => {
        createChartCardCalled = true;
        passedOptions = opts;
      };

      ChartCardRegistry.restoreCard({
        type: 'dashboard',
        page: '2'
      });

      assert.strictEqual(createChartCardCalled, true);
      assert.strictEqual(passedOptions.type, 'dashboard');
    });

  });

  describe('WRAPPER_ID', () => {

    it('exports WRAPPER_ID constant', () => {
      assert.strictEqual(ChartCardRegistry.WRAPPER_ID, 'charts-wrapper');
    });

  });

});
