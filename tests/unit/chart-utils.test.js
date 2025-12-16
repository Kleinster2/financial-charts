/**
 * Unit tests for chart-utils.js
 *
 * Tests: ensureStyleTag() idempotency, mapToObject()
 */

const { describe, it, beforeEach } = require('node:test');
const assert = require('node:assert');
const { loadModule, createWindowStub } = require('./helpers/load-module');

describe('ChartUtils', () => {

  describe('ensureStyleTag()', () => {

    it('creates style element with id and content', () => {
      const window = createWindowStub();
      loadModule('charting_sandbox/chart-utils.js', window);

      window.ChartUtils.ensureStyleTag('test-styles', '.foo { color: red; }');

      const style = window._elements?.['test-styles'];
      assert.ok(style, 'Style element should exist');
      assert.strictEqual(style.id, 'test-styles');
      assert.strictEqual(style.textContent, '.foo { color: red; }');
    });

    it('is idempotent - second call does not duplicate', () => {
      const window = createWindowStub();
      loadModule('charting_sandbox/chart-utils.js', window);

      window.ChartUtils.ensureStyleTag('test-styles', '.foo { color: red; }');
      window.ChartUtils.ensureStyleTag('test-styles', '.bar { color: blue; }');

      // Should still have original content (not overwritten)
      const style = window._elements?.['test-styles'];
      assert.strictEqual(style.textContent, '.foo { color: red; }');
    });

    it('allows different ids', () => {
      const window = createWindowStub();
      loadModule('charting_sandbox/chart-utils.js', window);

      window.ChartUtils.ensureStyleTag('styles-a', '.a { }');
      window.ChartUtils.ensureStyleTag('styles-b', '.b { }');

      assert.ok(window._elements?.['styles-a']);
      assert.ok(window._elements?.['styles-b']);
      assert.strictEqual(window._elements['styles-a'].textContent, '.a { }');
      assert.strictEqual(window._elements['styles-b'].textContent, '.b { }');
    });

  });

  describe('mapToObject()', () => {

    it('converts Map to plain object', () => {
      const window = createWindowStub();
      loadModule('charting_sandbox/chart-utils.js', window);

      const map = new Map([['a', 1], ['b', 2]]);
      const obj = window.ChartUtils.mapToObject(map);

      assert.deepStrictEqual(obj, { a: 1, b: 2 });
    });

    it('returns empty object for empty Map', () => {
      const window = createWindowStub();
      loadModule('charting_sandbox/chart-utils.js', window);

      const obj = window.ChartUtils.mapToObject(new Map());
      assert.deepStrictEqual(obj, {});
    });

    it('returns empty object for null/undefined', () => {
      const window = createWindowStub();
      loadModule('charting_sandbox/chart-utils.js', window);

      assert.deepStrictEqual(window.ChartUtils.mapToObject(null), {});
      assert.deepStrictEqual(window.ChartUtils.mapToObject(undefined), {});
    });

  });

  describe('requests.fetchJSON()', () => {

    it('returns parsed JSON from fetch', async () => {
      const window = createWindowStub();
      // Mock fetch on window before loading module
      let fetchCalls = 0;
      window.fetch = async (url) => {
        fetchCalls++;
        return {
          ok: true,
          json: async () => ({ data: 'test', url })
        };
      };

      loadModule('charting_sandbox/chart-utils.js', window);

      const result = await window.ChartUtils.requests.fetchJSON('/api/test');
      assert.deepStrictEqual(result, { data: 'test', url: '/api/test' });
      assert.strictEqual(fetchCalls, 1);
    });

    it('deduplicates concurrent requests to same URL', async () => {
      const window = createWindowStub();
      let fetchCalls = 0;
      let resolvePromise;

      // Create a delayed fetch that we can control
      window.fetch = async (url) => {
        fetchCalls++;
        await new Promise(resolve => { resolvePromise = resolve; });
        return {
          ok: true,
          json: async () => ({ count: fetchCalls })
        };
      };

      loadModule('charting_sandbox/chart-utils.js', window);

      // Start two concurrent requests
      const promise1 = window.ChartUtils.requests.fetchJSON('/api/same');
      const promise2 = window.ChartUtils.requests.fetchJSON('/api/same');

      // Should be the same promise
      assert.strictEqual(promise1, promise2, 'Should return same promise');
      assert.strictEqual(fetchCalls, 1, 'Should only make one fetch call');

      // Resolve and check results
      resolvePromise();
      const [result1, result2] = await Promise.all([promise1, promise2]);
      assert.deepStrictEqual(result1, result2);
    });

    it('makes separate requests for different URLs', async () => {
      const window = createWindowStub();
      let fetchCalls = 0;
      window.fetch = async (url) => {
        fetchCalls++;
        return {
          ok: true,
          json: async () => ({ url })
        };
      };

      loadModule('charting_sandbox/chart-utils.js', window);

      await Promise.all([
        window.ChartUtils.requests.fetchJSON('/api/one'),
        window.ChartUtils.requests.fetchJSON('/api/two')
      ]);

      assert.strictEqual(fetchCalls, 2, 'Should make two fetch calls for different URLs');
    });

    it('skipDedupe forces new request', async () => {
      const window = createWindowStub();
      let fetchCalls = 0;
      let resolveFirst;

      window.fetch = async (url) => {
        fetchCalls++;
        if (fetchCalls === 1) {
          await new Promise(resolve => { resolveFirst = resolve; });
        }
        return {
          ok: true,
          json: async () => ({ call: fetchCalls })
        };
      };

      loadModule('charting_sandbox/chart-utils.js', window);

      // Start first request (will wait)
      const promise1 = window.ChartUtils.requests.fetchJSON('/api/test');

      // Second request with skipDedupe should not be deduplicated
      const promise2 = window.ChartUtils.requests.fetchJSON('/api/test', { skipDedupe: true });

      assert.strictEqual(fetchCalls, 2, 'skipDedupe should force new request');

      resolveFirst();
      await Promise.all([promise1, promise2]);
    });

    it('throws on non-ok response', async () => {
      const window = createWindowStub();
      window.fetch = async () => ({
        ok: false,
        status: 404
      });

      loadModule('charting_sandbox/chart-utils.js', window);

      await assert.rejects(
        window.ChartUtils.requests.fetchJSON('/api/notfound'),
        /HTTP 404/
      );
    });

    it('pending() returns count of in-flight requests', async () => {
      const window = createWindowStub();
      let resolvePromise;
      window.fetch = async () => {
        await new Promise(resolve => { resolvePromise = resolve; });
        return { ok: true, json: async () => ({}) };
      };

      loadModule('charting_sandbox/chart-utils.js', window);

      assert.strictEqual(window.ChartUtils.requests.pending(), 0);

      const promise = window.ChartUtils.requests.fetchJSON('/api/test');
      assert.strictEqual(window.ChartUtils.requests.pending(), 1);

      resolvePromise();
      await promise;
      assert.strictEqual(window.ChartUtils.requests.pending(), 0);
    });

    it('list() returns in-flight URLs', async () => {
      const window = createWindowStub();
      let resolvePromise;
      window.fetch = async () => {
        await new Promise(resolve => { resolvePromise = resolve; });
        return { ok: true, json: async () => ({}) };
      };

      loadModule('charting_sandbox/chart-utils.js', window);

      const promise = window.ChartUtils.requests.fetchJSON('/api/test');
      assert.deepStrictEqual(window.ChartUtils.requests.list(), ['/api/test']);

      resolvePromise();
      await promise;
      assert.deepStrictEqual(window.ChartUtils.requests.list(), []);
    });

  });

});
