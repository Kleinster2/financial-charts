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

});
