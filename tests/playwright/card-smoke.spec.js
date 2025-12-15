const fs = require('fs');
const path = require('path');
const { test, expect } = require('@playwright/test');
const { startStaticServer } = require('./helpers/static-server');

const FIXED_NOW_MS = Date.UTC(2024, 5, 1, 12, 0, 0);
const PRICE_BASE_TIME_S = Math.floor(Date.UTC(2024, 0, 1) / 1000);
const PRICE_POINTS = 30;

function buildSeries({ startTimeS, points, stepS, startValue, stepValue }) {
  return Array.from({ length: points }, (_, i) => ({
    time: startTimeS + i * stepS,
    value: startValue + i * stepValue,
  }));
}

function json(route, payload, status = 200) {
  return route.fulfill({
    status,
    contentType: 'application/json; charset=utf-8',
    body: JSON.stringify(payload),
    headers: { 'Cache-Control': 'no-store' },
  });
}

test.describe('Chart card smoke', () => {
  /** @type {{server: import('http').Server, baseURL: string} | null} */
  let serverInfo = null;

  test.beforeAll(async () => {
    const sandboxRoot = path.join(__dirname, '..', '..', 'charting_sandbox');
    serverInfo = await startStaticServer(sandboxRoot);
  });

  test.afterAll(async () => {
    if (!serverInfo) return;
    await new Promise((resolve) => serverInfo.server.close(resolve));
  });

  test('initial plot, Fit, range dropdown, and pane toggles', async ({ page }) => {
    if (!serverInfo) throw new Error('Static server not started');

    const lwcStubPath = path.join(__dirname, 'stubs', 'lightweight-charts-stub.js');
    const lwcStub = fs.readFileSync(lwcStubPath, 'utf8');

    const consoleErrors = [];
    page.on('pageerror', (err) => consoleErrors.push(`pageerror: ${err.message}`));
    page.on('console', (msg) => {
      if (msg.type() === 'error') consoleErrors.push(`console.error: ${msg.text()}`);
    });

    await page.addInitScript(({ fixedNowMs }) => {
      const OriginalDate = Date;
      // eslint-disable-next-line no-global-assign
      Date = class MockDate extends OriginalDate {
        constructor(...args) {
          if (args.length === 0) return new OriginalDate(fixedNowMs);
          return new OriginalDate(...args);
        }
        static now() {
          return fixedNowMs;
        }
      };
    }, { fixedNowMs: FIXED_NOW_MS });

    await page.route('**/lightweight-charts.standalone.development.js', (route) => {
      return route.fulfill({
        status: 200,
        contentType: 'application/javascript; charset=utf-8',
        body: lwcStub,
        headers: { 'Cache-Control': 'no-store' },
      });
    });

    await page.route('**/api/**', (route) => {
      const request = route.request();
      const url = new URL(request.url());

      if (url.pathname === '/api/workspace' && request.method() === 'GET') {
        return json(route, { cards: [] });
      }
      if (url.pathname === '/api/workspace' && request.method() === 'POST') {
        return json(route, { ok: true });
      }

      if (url.pathname === '/api/ticker-aliases') return json(route, {});
      if (url.pathname === '/api/tickers') return json(route, ['SPY']);

      if (url.pathname === '/api/metadata') {
        const raw = url.searchParams.get('tickers') || '';
        if (raw === 'ALL') return json(route, { SPY: 'SPDR S&P 500 ETF Trust' });

        const tickers = raw.split(',').map((t) => t.trim()).filter(Boolean);
        const out = {};
        tickers.forEach((t) => { out[t] = t; });
        return json(route, out);
      }

      if (url.pathname === '/api/data') {
        const tickers = (url.searchParams.get('tickers') || '')
          .split(',')
          .map((t) => t.trim())
          .filter(Boolean);

        const series = buildSeries({
          startTimeS: PRICE_BASE_TIME_S,
          points: PRICE_POINTS,
          stepS: 86400,
          startValue: 100,
          stepValue: 1,
        });

        const out = {};
        tickers.forEach((t) => { out[t] = series; });
        return json(route, out);
      }

      if (url.pathname === '/api/volume') {
        const tickers = (url.searchParams.get('tickers') || '')
          .split(',')
          .map((t) => t.trim())
          .filter(Boolean);

        const series = buildSeries({
          startTimeS: PRICE_BASE_TIME_S,
          points: PRICE_POINTS,
          stepS: 86400,
          startValue: 1_000_000,
          stepValue: 10_000,
        });

        const out = {};
        tickers.forEach((t) => { out[t] = series; });
        return json(route, out);
      }

      if (url.pathname === '/api/revenue') {
        const tickers = (url.searchParams.get('tickers') || '')
          .split(',')
          .map((t) => t.trim())
          .filter(Boolean);

        const series = buildSeries({
          startTimeS: Math.floor(Date.UTC(2018, 0, 1) / 1000),
          points: 12,
          stepS: 90 * 86400,
          startValue: 10_000_000_000,
          stepValue: 100_000_000,
        });

        const out = {};
        tickers.forEach((t) => { out[t] = series; });
        return json(route, out);
      }

      if (url.pathname === '/api/fundamentals/chart') {
        const tickers = (url.searchParams.get('tickers') || '')
          .split(',')
          .map((t) => t.trim())
          .filter(Boolean);
        const metrics = (url.searchParams.get('metrics') || '')
          .split(',')
          .map((m) => m.trim().toLowerCase())
          .filter(Boolean);

        const out = {};
        tickers.forEach((t) => {
          out[t] = {};
          metrics.forEach((metric) => {
            out[t][metric] = buildSeries({
              startTimeS: Math.floor(Date.UTC(2018, 0, 1) / 1000),
              points: 12,
              stepS: 90 * 86400,
              startValue: 1_000,
              stepValue: 10,
            });
          });
        });
        return json(route, out);
      }

      return json(route, {});
    });

    await page.goto(`${serverInfo.baseURL}/index.html`, { waitUntil: 'domcontentloaded' });

    // 1) initial plot on load
    await page.waitForSelector('.chart-card');
    await page.waitForFunction(() => {
      const card = document.querySelector('.chart-card');
      const ctx = card && card._ctx;
      return !!(ctx && ctx.runtime && ctx.runtime.chart && ctx.runtime.priceSeriesMap && ctx.runtime.priceSeriesMap.size > 0);
    });

    await page.waitForFunction(() => {
      const ctx = document.querySelector('.chart-card')._ctx;
      const ts = ctx.runtime.chart.timeScale();
      return typeof ctx.runtime.rangeSaveHandler === 'function'
        && Array.isArray(ts.__subscribers)
        && ts.__subscribers.includes(ctx.runtime.rangeSaveHandler);
    });

    // 2) Fit button
    await page.click('.chart-card .fit-btn');
    const expectedFitFrom = PRICE_BASE_TIME_S;
    const expectedFitTo = PRICE_BASE_TIME_S + (PRICE_POINTS - 1) * 86400;
    await page.waitForFunction(([fromS, toS]) => {
      const ctx = document.querySelector('.chart-card')._ctx;
      return ctx.visibleRange && ctx.visibleRange.from === fromS && ctx.visibleRange.to === toS;
    }, [expectedFitFrom, expectedFitTo]);

    // 3) Range dropdown
    await page.selectOption('.chart-card .range-select', '2020');
    const expectedFrom2020 = Math.floor(Date.UTC(2020, 0, 1) / 1000);
    const expectedToFixed = Math.floor(FIXED_NOW_MS / 1000);
    await page.waitForFunction(([fromS, toS]) => {
      const ctx = document.querySelector('.chart-card')._ctx;
      return ctx.visibleRange && ctx.visibleRange.from === fromS && ctx.visibleRange.to === toS;
    }, [expectedFrom2020, expectedToFixed]);

    await page.waitForFunction(() => {
      const ctx = document.querySelector('.chart-card')._ctx;
      const ts = ctx.runtime.chart.timeScale();
      const subs = Array.isArray(ts.__subscribers) ? ts.__subscribers : [];
      const handler = ctx.runtime.rangeSaveHandler;
      const occurrences = subs.filter((cb) => cb === handler).length;
      return occurrences === 1;
    });

    // 4) Pane toggles
    await page.click('.chart-card .settings-toggle-btn');

    const toggleSteps = [
      { selector: '.toggle-vol-btn', key: 'showVolPane' },
      { selector: '.toggle-volume-btn', key: 'showVolumePane' },
      { selector: '.toggle-revenue-btn', key: 'showRevenuePane' },
      { selector: '.toggle-fundamentals-pane-btn', key: 'showFundamentalsPane' },
    ];

    for (const { selector, key } of toggleSteps) {
      const before = await page.evaluate(() => document.querySelector('.chart-card')._ctx.runtime.chart.__testId);
      await page.click(`.chart-card ${selector}`);

      await page.waitForFunction(([prevId, stateKey]) => {
        const ctx = document.querySelector('.chart-card')._ctx;
        return ctx.runtime.chart && ctx.runtime.chart.__testId !== prevId && ctx[stateKey] === true;
      }, [before, key]);

      await page.waitForFunction(() => {
        const ctx = document.querySelector('.chart-card')._ctx;
        const ts = ctx.runtime.chart.timeScale();
        return typeof ctx.runtime.rangeSaveHandler === 'function'
          && Array.isArray(ts.__subscribers)
          && ts.__subscribers.includes(ctx.runtime.rangeSaveHandler);
      });
    }

    expect(consoleErrors).toEqual([]);
  });
});
