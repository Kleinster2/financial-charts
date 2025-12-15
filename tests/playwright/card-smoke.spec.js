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

/**
 * Shared page setup for smoke tests - configures mocks and routes.
 * @param {import('@playwright/test').Page} page
 * @param {Object} options
 * @param {Array} options.consoleErrors - Array to collect console errors
 * @param {Object} [options.workspace] - Optional workspace data to return from /api/workspace
 */
async function setupPage(page, { consoleErrors, workspace }) {
  const lwcStubPath = path.join(__dirname, 'stubs', 'lightweight-charts-stub.js');
  const lwcStub = fs.readFileSync(lwcStubPath, 'utf8');

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
      return json(route, workspace || { cards: [] });
    }
    if (url.pathname === '/api/workspace' && request.method() === 'POST') {
      return json(route, { ok: true });
    }

    if (url.pathname === '/api/ticker-aliases') return json(route, {});
    if (url.pathname === '/api/tickers') return json(route, ['SPY', 'QQQ', 'AAPL', 'MSFT']);

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

  test('workspace restore with saved card state', async ({ page }) => {
    if (!serverInfo) throw new Error('Static server not started');

    const consoleErrors = [];
    const savedWorkspace = {
      cards: [
        {
          id: 'chart-restored-1',
          page: 1,
          tickers: ['AAPL', 'MSFT'],
          title: 'Tech Giants',
          showVolPane: true,
          useRaw: true,
        },
      ],
      pages: {
        pages: [1],
        active: 1,
        names: { 1: 'Test Page' },
        categories: {},
      },
    };

    await setupPage(page, { workspace: savedWorkspace, consoleErrors });
    await page.goto(`${serverInfo.baseURL}/index.html`, { waitUntil: 'domcontentloaded' });

    // Wait for card to be created and plotted
    await page.waitForSelector('.chart-card');
    await page.waitForFunction(() => {
      const card = document.querySelector('.chart-card');
      const ctx = card && card._ctx;
      return !!(ctx && ctx.runtime && ctx.runtime.chart && ctx.runtime.priceSeriesMap && ctx.runtime.priceSeriesMap.size > 0);
    });

    // Verify restored state
    const restoredState = await page.evaluate(() => {
      const card = document.querySelector('.chart-card');
      const ctx = card._ctx;
      return {
        tickerCount: ctx.runtime.priceSeriesMap.size,
        showVolPane: ctx.showVolPane,
        useRaw: ctx.useRaw,
        title: card.querySelector('.title-input')?.value || '',
        ctxTitle: ctx.title || '',
      };
    });

    expect(restoredState.tickerCount).toBe(2);
    expect(restoredState.showVolPane).toBe(true);
    expect(restoredState.useRaw).toBe(true);
    // Title is passed to DOM via initialTitle in createChartCard
    expect(restoredState.title).toBe('Tech Giants');

    expect(consoleErrors).toEqual([]);
  });

  test('page switching hides/shows correct pages', async ({ page }) => {
    if (!serverInfo) throw new Error('Static server not started');

    const consoleErrors = [];
    const multiPageWorkspace = {
      cards: [
        { id: 'chart-page1', page: 1, tickers: ['SPY'], title: 'Page 1 Chart' },
        { id: 'chart-page2', page: 2, tickers: ['QQQ'], title: 'Page 2 Chart' },
      ],
      pages: {
        pages: [1, 2],
        active: 1,
        names: { 1: 'First Page', 2: 'Second Page' },
        categories: {},
      },
    };

    // Inject localStorage BEFORE page load so pages.js creates page 2
    const pagesData = JSON.stringify(multiPageWorkspace.pages);
    await page.addInitScript((data) => {
      localStorage.setItem('sandbox_pages', data);
    }, pagesData);

    await setupPage(page, { workspace: multiPageWorkspace, consoleErrors });
    await page.goto(`${serverInfo.baseURL}/index.html`, { waitUntil: 'domcontentloaded' });

    // Wait for initial page load, page 2 to be created, and PageManager initialization
    await page.waitForSelector('.chart-card');
    await page.waitForFunction(() => {
      const card = document.querySelector('.chart-card');
      const ctx = card && card._ctx;
      // Use .page selector to avoid matching tab elements
      const page2Exists = !!document.querySelector('.page[data-page="2"]');
      const pmReady = window.PageManager && typeof window.PageManager.getActivePage === 'function';
      return !!(ctx && ctx.runtime && ctx.runtime.chart && page2Exists && pmReady);
    });

    // Wait for async initialization to settle (pages.js initialize is async)
    await page.waitForFunction(() => {
      // Check that PageManager has finished initialization by verifying page visibility is set
      const page1 = document.querySelector('.page[data-page="1"]');
      return page1 && page1.style.display !== '';
    }, { timeout: 5000 });

    // Verify page 2 exists
    const page2Exists = await page.evaluate(() => !!document.querySelector('.page[data-page="2"]'));
    expect(page2Exists).toBe(true);

    // Get initial active page (should be 1 based on localStorage)
    const initialActivePage = await page.evaluate(() => window.PageManager?.getActivePage?.());
    expect(initialActivePage).toBe(1);

    // Switch to page 2 via PageManager
    await page.evaluate(() => {
      window.PageManager.showPage(2);
    });

    // Wait for page switch to complete and DOM to update
    await page.waitForFunction(() => {
      const activePage = window.PageManager?.getActivePage?.();
      const page1 = document.querySelector('.page[data-page="1"]');
      const page2 = document.querySelector('.page[data-page="2"]');
      return activePage === 2 && page1?.style.display === 'none' && page2?.style.display === 'block';
    });

    // Verify page 2 is now visible, page 1 is hidden
    // Use .page selector to avoid matching tab elements which also have data-page
    const afterSwitchTo2 = await page.evaluate(() => {
      const page1 = document.querySelector('.page[data-page="1"]');
      const page2 = document.querySelector('.page[data-page="2"]');
      return {
        page1Visible: page1 ? page1.style.display !== 'none' : false,
        page2Visible: page2 ? page2.style.display !== 'none' : false,
        activePage: window.PageManager?.getActivePage?.() || null,
      };
    });

    expect(afterSwitchTo2.page1Visible).toBe(false);
    expect(afterSwitchTo2.page2Visible).toBe(true);
    expect(afterSwitchTo2.activePage).toBe(2);

    // Switch back to page 1
    await page.evaluate(() => {
      window.PageManager.showPage(1);
    });

    // Wait for page switch to complete and DOM to update
    await page.waitForFunction(() => {
      const activePage = window.PageManager?.getActivePage?.();
      const page1 = document.querySelector('.page[data-page="1"]');
      const page2 = document.querySelector('.page[data-page="2"]');
      return activePage === 1 && page1?.style.display === 'block' && page2?.style.display === 'none';
    });

    // Verify page 1 is now visible, page 2 is hidden
    const afterSwitchTo1 = await page.evaluate(() => {
      const page1 = document.querySelector('.page[data-page="1"]');
      const page2 = document.querySelector('.page[data-page="2"]');
      return {
        page1Visible: page1 ? page1.style.display !== 'none' : false,
        page2Visible: page2 ? page2.style.display !== 'none' : false,
        activePage: window.PageManager?.getActivePage?.() || null,
      };
    });

    expect(afterSwitchTo1.page1Visible).toBe(true);
    expect(afterSwitchTo1.page2Visible).toBe(false);
    expect(afterSwitchTo1.activePage).toBe(1);

    expect(consoleErrors).toEqual([]);
  });

  test('tag filtering works in normal and highlights mode', async ({ page }) => {
    if (!serverInfo) throw new Error('Static server not started');

    const consoleErrors = [];
    const taggedWorkspace = {
      cards: [
        { id: 'chart-tagged-1', page: 1, tickers: ['SPY'], title: 'Card A', tags: ['tech'], starred: true },
        { id: 'chart-tagged-2', page: 1, tickers: ['QQQ'], title: 'Card B', tags: ['finance'], starred: false },
        { id: 'chart-tagged-3', page: 1, tickers: ['AAPL'], title: 'Card C', tags: ['tech'], starred: true },
        { id: 'chart-tagged-4', page: 2, tickers: ['MSFT'], title: 'Card D', tags: ['tech'], starred: true },
      ],
      pages: {
        pages: [1, 2],
        active: 1,
        names: { 1: 'Page 1', 2: 'Page 2' },
        categories: {},
      },
    };

    const pagesData = JSON.stringify(taggedWorkspace.pages);
    await page.addInitScript((data) => {
      localStorage.setItem('sandbox_pages', data);
    }, pagesData);

    await setupPage(page, { workspace: taggedWorkspace, consoleErrors });
    await page.goto(`${serverInfo.baseURL}/index.html`, { waitUntil: 'domcontentloaded' });

    // Wait for all 4 cards to load (need page 2's card for highlights tests)
    await page.waitForSelector('.chart-card');
    await page.waitForFunction(() => {
      const cards = document.querySelectorAll('.chart-card');
      return cards.length >= 4;
    });

    // Wait for tag dropdown to populate
    await page.waitForFunction(() => {
      const select = document.getElementById('tag-filter-select');
      return select && select.options.length > 1;
    });

    // 1) Test normal mode: filter by 'tech' tag
    await page.selectOption('#tag-filter-select', 'tech');
    await page.waitForFunction(() => {
      const cards = Array.from(document.querySelectorAll('.page[data-page="1"] .chart-card'));
      return cards.filter(c => c.style.display !== 'none').length === 2;
    });

    const afterTechFilter = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.page[data-page="1"] .chart-card'));
      return {
        visibleCount: cards.filter(c => c.style.display !== 'none').length,
        visibleTitles: cards.filter(c => c.style.display !== 'none')
          .map(c => c.querySelector('.title-input')?.value || '').sort(),
      };
    });

    expect(afterTechFilter.visibleCount).toBe(2); // Card A and Card C have 'tech' tag
    expect(afterTechFilter.visibleTitles).toEqual(['Card A', 'Card C']);

    // 2) Clear filter, all cards should be visible
    await page.selectOption('#tag-filter-select', '');
    await page.waitForFunction(() => {
      const cards = Array.from(document.querySelectorAll('.page[data-page="1"] .chart-card'));
      return cards.filter(c => c.style.display !== 'none').length === 3;
    });

    const afterClearFilter = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.page[data-page="1"] .chart-card'));
      return cards.filter(c => c.style.display !== 'none').length;
    });

    expect(afterClearFilter).toBe(3); // All 3 cards on page 1

    // 3) Test highlights mode with tag filter
    await page.evaluate(() => {
      window.toggleHighlightsMode();
    });
    await page.waitForFunction(() => {
      if (!window.highlightsMode) return false;
      const allCards = Array.from(document.querySelectorAll('.chart-card'));
      return allCards.filter(c => c.style.display !== 'none').length === 3;
    });

    // In highlights mode without tag filter, should show all starred (3 cards across pages)
    const highlightsNoTag = await page.evaluate(() => {
      const allCards = Array.from(document.querySelectorAll('.chart-card'));
      return allCards.filter(c => c.style.display !== 'none').length;
    });

    expect(highlightsNoTag).toBe(3); // Card A, Card C (page 1), Card D (page 2) are starred

    // 4) Apply 'tech' filter in highlights mode
    await page.selectOption('#tag-filter-select', 'tech');
    await page.waitForFunction(() => {
      const allCards = Array.from(document.querySelectorAll('.chart-card'));
      return allCards.filter(c => c.style.display !== 'none').length === 3;
    });

    const highlightsWithTech = await page.evaluate(() => {
      const allCards = Array.from(document.querySelectorAll('.chart-card'));
      const visible = allCards.filter(c => c.style.display !== 'none');
      return {
        visibleCount: visible.length,
        visibleTitles: visible.map(c => c.querySelector('.title-input')?.value || '').sort(),
      };
    });

    // Should show starred cards with 'tech' tag: Card A, Card C, Card D
    expect(highlightsWithTech.visibleCount).toBe(3);
    expect(highlightsWithTech.visibleTitles).toEqual(['Card A', 'Card C', 'Card D']);

    // 5) Filter by 'finance' in highlights mode - Card B has 'finance' but is not starred
    await page.selectOption('#tag-filter-select', 'finance');
    await page.waitForFunction(() => {
      const allCards = Array.from(document.querySelectorAll('.chart-card'));
      return allCards.filter(c => c.style.display !== 'none').length === 0;
    });

    const highlightsWithFinance = await page.evaluate(() => {
      const allCards = Array.from(document.querySelectorAll('.chart-card'));
      return allCards.filter(c => c.style.display !== 'none').length;
    });

    expect(highlightsWithFinance).toBe(0); // No starred cards have 'finance' tag

    expect(consoleErrors).toEqual([]);
  });
});
