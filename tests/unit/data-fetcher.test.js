/**
 * Unit tests for data-fetcher.js
 *
 * Tests: getVolumeData ticker normalization and abort signal handling
 */

const { describe, it, beforeEach } = require('node:test');
const assert = require('node:assert');
const { loadModule, createWindowStub } = require('./helpers/load-module');

describe('DataFetcher', () => {
  let window;
  let DataFetcher;

  beforeEach(() => {
    // Create a single window and load modules sequentially into it
    window = createWindowStub();

    // Load config first
    window = loadModule('charting_sandbox/config.js', window);

    // Load chart-utils
    window = loadModule('charting_sandbox/chart-utils.js', window);

    // Set up default fetch mock before loading data-fetcher
    window.fetch = async (url, options) => {
      if (options?.signal?.aborted) {
        const error = new Error('Aborted');
        error.name = 'AbortError';
        throw error;
      }
      return {
        ok: true,
        json: async () => ({ AAPL: [{ time: '2024-01-01', value: 1000000 }] })
      };
    };

    // Load data-fetcher
    window = loadModule('charting_sandbox/data-fetcher.js', window);

    DataFetcher = window.DataFetcher;
  });

  describe('getVolumeData()', () => {

    it('accepts single ticker string and normalizes to array', async () => {
      let capturedUrl = null;
      window.fetch = async (url) => {
        capturedUrl = url;
        return {
          ok: true,
          json: async () => ({ AAPL: [{ time: '2024-01-01', value: 1000000 }] })
        };
      };

      const result = await DataFetcher.getVolumeData('AAPL');

      assert.ok(capturedUrl, 'fetch should have been called');
      assert.ok(capturedUrl.includes('tickers=AAPL'), 'URL should contain ticker');
      assert.ok(result.AAPL, 'Result should have AAPL data');
    });

    it('accepts array of tickers', async () => {
      let capturedUrl = null;
      window.fetch = async (url) => {
        capturedUrl = url;
        return {
          ok: true,
          json: async () => ({
            AAPL: [{ time: '2024-01-01', value: 1000000 }],
            MSFT: [{ time: '2024-01-01', value: 2000000 }]
          })
        };
      };

      const result = await DataFetcher.getVolumeData(['AAPL', 'MSFT']);

      assert.ok(capturedUrl.includes('tickers=AAPL%2CMSFT') || capturedUrl.includes('tickers=AAPL,MSFT'),
        'URL should contain both tickers');
      assert.ok(result.AAPL, 'Result should have AAPL data');
      assert.ok(result.MSFT, 'Result should have MSFT data');
    });

    it('returns empty object when signal is already aborted', async () => {
      const controller = new AbortController();
      controller.abort();

      const result = await DataFetcher.getVolumeData('AAPL', null, null, { signal: controller.signal });

      // Use Object.keys comparison due to vm context isolation
      assert.strictEqual(Object.keys(result).length, 0, 'Should return empty object on pre-aborted signal');
    });

    it('returns empty object when signal aborts during fetch', async () => {
      const controller = new AbortController();

      window.fetch = async (url, options) => {
        // Simulate abort during fetch
        controller.abort();
        if (options?.signal?.aborted) {
          const error = new Error('Aborted');
          error.name = 'AbortError';
          throw error;
        }
        return { ok: true, json: async () => ({}) };
      };

      const result = await DataFetcher.getVolumeData('AAPL', null, null, { signal: controller.signal });

      // Use Object.keys comparison due to vm context isolation
      assert.strictEqual(Object.keys(result).length, 0, 'Should return empty object on abort during fetch');
    });

    it('returns empty object for empty/null tickers', async () => {
      const result1 = await DataFetcher.getVolumeData([]);
      const result2 = await DataFetcher.getVolumeData(null);

      // Use Object.keys comparison due to vm context isolation
      assert.strictEqual(Object.keys(result1).length, 0, 'Empty array should return empty object');
      assert.strictEqual(Object.keys(result2).length, 0, 'Null should return empty object');
    });

  });
});
