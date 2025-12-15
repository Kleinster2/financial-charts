(() => {
  let nextChartId = 1;

  function createPriceScale() {
    return {
      applyOptions() {},
    };
  }

  function createSeries(seriesType, options) {
    let seriesData = [];
    const priceScale = createPriceScale();
    return {
      __type: seriesType,
      __options: { ...(options || {}) },
      applyOptions(next) {
        Object.assign(this.__options, next || {});
      },
      setData(data) {
        seriesData = Array.isArray(data) ? data : [];
      },
      data() {
        return seriesData;
      },
      priceScale() {
        return priceScale;
      },
    };
  }

  function createTimeScale() {
    let visibleRange = null;
    const subscribers = [];

    const notify = (range) => {
      subscribers.slice().forEach((cb) => {
        try {
          cb(range);
        } catch (e) {}
      });
    };

    return {
      __subscribers: subscribers,
      setVisibleRange(range) {
        visibleRange = range;
        notify(visibleRange);
      },
      getVisibleRange() {
        return visibleRange;
      },
      fitContent() {
        if (!visibleRange) visibleRange = { from: 0, to: 1 };
        notify(visibleRange);
      },
      subscribeVisibleTimeRangeChange(cb) {
        subscribers.push(cb);
      },
      unsubscribeVisibleTimeRangeChange(cb) {
        for (let i = subscribers.length - 1; i >= 0; i -= 1) {
          if (subscribers[i] === cb) subscribers.splice(i, 1);
        }
      },
    };
  }

  function createPane() {
    const seriesSet = new Set();

    return {
      __series: seriesSet,
      addSeries(seriesType, options) {
        const s = createSeries(seriesType, options);
        seriesSet.add(s);
        return s;
      },
      removeSeries(series) {
        seriesSet.delete(series);
      },
      setStretchFactor() {},
    };
  }

  function createChart(container) {
    const chartId = nextChartId++;
    const canvas = document.createElement('canvas');
    canvas.setAttribute('data-test-chart-id', String(chartId));
    canvas.width = container.clientWidth || 800;
    canvas.height = container.clientHeight || 500;
    container.appendChild(canvas);

    const timeScale = createTimeScale();
    const sharedPriceScale = createPriceScale();
    const panes = new Set();
    const seriesSet = new Set();
    const crosshairSubscribers = [];

    return {
      __testId: chartId,
      __container: container,
      __canvas: canvas,

      addSeries(seriesType, options) {
        const s = createSeries(seriesType, options);
        seriesSet.add(s);
        return s;
      },
      removeSeries(series) {
        seriesSet.delete(series);
      },

      addPane() {
        const pane = createPane();
        panes.add(pane);
        return pane;
      },
      removePane(pane) {
        panes.delete(pane);
      },

      applyOptions() {},
      resize(w, h) {
        canvas.width = Math.max(1, Math.floor(w));
        canvas.height = Math.max(1, Math.floor(h));
      },

      priceScale() {
        return sharedPriceScale;
      },
      timeScale() {
        return timeScale;
      },

      subscribeCrosshairMove(cb) {
        crosshairSubscribers.push(cb);
      },
      unsubscribeCrosshairMove(cb) {
        for (let i = crosshairSubscribers.length - 1; i >= 0; i -= 1) {
          if (crosshairSubscribers[i] === cb) crosshairSubscribers.splice(i, 1);
        }
      },

      remove() {
        try {
          canvas.remove();
        } catch (_) {}
      },
    };
  }

  window.LightweightCharts = {
    createChart,
    LineSeries: 'LineSeries',
    LineStyle: {
      Solid: 0,
      Dotted: 1,
      Dashed: 2,
      LargeDashed: 3,
      SparseDotted: 4,
    },
    PriceScaleMode: {
      Normal: 0,
      Logarithmic: 1,
      Percentage: 2,
      Index: 3,
    },
    CrosshairMode: {
      Normal: 0,
      Magnet: 1,
    },
  };
})();
