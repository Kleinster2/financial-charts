// Lightweight Charts sandbox multi-card module
// Creates self-contained chart cards with independent state.
(() => {
  const WRAPPER_ID = 'charts-wrapper';
  const colors = [
    '#008FFB', '#00E396', '#FEB019', '#FF4560', '#775DD0', '#546E7A', '#26a69a', '#D10CE8',
    '#FF66C3', '#FF8633', '#2B908F', '#F0E442', '#3D85C6', '#A52A2A', '#FFD700', '#00BFFF',
    '#FF1493', '#00FA9A', '#9932CC', '#FF4500', '#4B0082'
  ];
  let globalCardCounter = 0;
  const VOL_WINDOW = 100; // rolling volatility window (days)

  // Save all chart states to localStorage
  function saveCards(){
    const cards = Array.from(document.querySelectorAll('.chart-card')).map(card=>({
      tickers: Array.from(card._selectedTickers||[]),
      showDiff: !!card._showDiff,
      showAvg: !!card._showAvg,
      showVol: !!card._showVol
    }));
    localStorage.setItem('sandbox_cards', JSON.stringify(cards));
  }

  function createChartCard(initialTickers = 'SPY', initialShowDiff = false, initialShowAvg = false, initialShowVol = true) {
    const wrapper = document.getElementById(WRAPPER_ID);
    if (!wrapper) { console.error('Missing charts wrapper'); return; }

    // ---------------- Build DOM ----------------
    const card = document.createElement('div');
    card.className = 'chart-card';

    card.innerHTML = `
      <div class="controls">
        <input type="text" class="ticker-input" list="ticker-list" placeholder="e.g. AAPL">
        <button class="add-ticker-btn">Add</button>
        <button class="plot-btn">Plot</button>
        <!-- Quick range buttons -->
        <button class="range-btn" data-range="ytd">YTD</button>
        <button class="range-btn" data-range="2024">2024-</button>
        <button class="range-btn" data-range="2023">2023-</button>
        <button class="range-btn" data-range="2022">2022-</button>
        <button class="range-btn" data-range="2021">2021-</button>
        <button class="range-btn" data-range="2020">2020-</button>
        <button class="toggle-diff-btn">Show Diff Pane</button>
        <button class="toggle-vol-btn">Hide Vol Pane</button>
        <button class="toggle-avg-btn">Show Avg</button>
        <button class="add-chart-btn">Add Chart</button>
        <button class="remove-card-btn">Remove</button>
        <div class="ticker-chips"></div>
        
      </div>
      <div class="chart-box"></div>
    `;

    wrapper.appendChild(card);

    // ---------------- State ----------------
    let showDiff = initialShowDiff;
    let showAvg = initialShowAvg;
    let showVolPane = initialShowVol;
    const selectedTickers = new Set(initialTickers ? initialTickers.split(/[,\s]+/).filter(Boolean).map(t=>t.toUpperCase()) : []);
    const priceSeriesMap = new Map();
    const diffSeriesMap = new Map();
    const volSeriesMap = new Map();
    let avgSeries = null;
    let latestRebasedData = {};
    const hiddenTickers = new Set();
    const tickerColorMap = new Map();
    let bottomPane = null;
    let volPane = null;
    let bottomPaneIndex = null;
    let volPaneIndex = null;
    let zeroLineTop = null;
    let zeroLineBottom = null;
    const originalNormalizedData = {};
    let colorIndex = 0;

    // Persist initial card state for localStorage
    card._selectedTickers = new Set(selectedTickers);
    card._showDiff = showDiff;
    card._showAvg = showAvg;
    card._showVol = showVolPane;

    // Elements
    const inputEl = card.querySelector('.ticker-input');
    const addTickerBtn = card.querySelector('.add-ticker-btn');
    addTickerBtn.addEventListener('click', addTicker);
    inputEl.addEventListener('keyup', e=>{ if(e.key==='Enter') addTicker(); });
    const plotBtn = card.querySelector('.plot-btn');
    const toggleDiffBtn = card.querySelector('.toggle-diff-btn');
    const toggleVolBtn = card.querySelector('.toggle-vol-btn');
    const toggleAvgBtn = card.querySelector('.toggle-avg-btn');
    const rangeBtns = card.querySelectorAll('.range-btn');
    toggleAvgBtn.textContent = showAvg ? 'Hide Avg':'Show Avg';
    toggleDiffBtn.textContent = showDiff ? 'Hide Diff Pane' : 'Show Diff Pane';
    const chipsContainer = card.querySelector('.ticker-chips');
    const chartBox = card.querySelector('.chart-box');

    // Create chart instance
    const chart = LightweightCharts.createChart(chartBox, {
      layout: { background: { type: 'solid', color: '#ffffff' }, textColor: '#333' },
      grid: { vertLines: { color: '#eee' }, horzLines: { color: '#eee' } },
      timeScale: { secondsVisible: false, rightOffset: 10, fixLeftEdge: true },
      rightPriceScale: { visible: true, scaleMargins: { top: 0.1, bottom: 0.1 } },
    });

    // Floating legend element for cursor values
    chartBox.style.position = 'relative';
    const legendEl = document.createElement('div');
    legendEl.className = 'floating-legend';
    Object.assign(legendEl.style, {
      position: 'absolute',
      pointerEvents: 'none',
      background: 'rgba(255,255,255,0.85)',
      border: '1px solid #ccc',
      borderRadius: '4px',
      padding: '2px 4px',
      fontSize: '12px',
      display: 'none',
      zIndex: 1000,
      whiteSpace: 'nowrap',
    });
    chartBox.appendChild(legendEl);

    const formatPct = (val)=>{ const diff=val-100; const sign=diff>0?'+':diff<0?'-':''; const dec=Math.abs(diff)>=100?0:1; return `${sign}${Math.abs(diff).toFixed(dec)}%`; };
    chart.subscribeCrosshairMove(param => {
      // DEBUG: log param once per move (can remove later)
      // console.debug('crosshair', param);

      if (!param || !param.point || param.time === undefined) {
        legendEl.style.display = 'none';
        return;
      }
      let html = '';
      const rows = []; // {t, price, color} objects to sort later
      const time = param.time !== undefined ? (typeof param.time === 'string' ? Date.parse(param.time)/1000 : param.time) : null;
      const isMap = param.seriesPrices && typeof param.seriesPrices.forEach === 'function';
      const iterate = isMap
        ? (cb) => param.seriesPrices.forEach((v, s) => cb(s, v))
        : (cb) => { if(param.seriesPrices){ for (const key in param.seriesPrices) cb(key, param.seriesPrices[key]); } };
      iterate((series, val) => {
        // Determine ticker (t) and price series object (ps)
        let t;
        let ps;
        if (series && typeof series.priceScale === 'function') {
          // Map form: series is Lightweight Chart series object
          const entry = Array.from(priceSeriesMap.entries()).find(([, s]) => s === series);
          if (!entry) return;
          [t, ps] = entry;
        } else {
          // Object form: key is ticker string, need to get series from map
          t = series;
          ps = priceSeriesMap.get(t);
          if (!ps) return;
        }
        if (hiddenTickers.has(t)) return;
        let price = typeof val === 'object' ? (val.close ?? val.value ?? val.open ?? val.high ?? val.low) : val;
        if (price == null || isNaN(price)) return;
        const color = tickerColorMap.get(t) || '#000';
        rows.push({t, price, color});
      });
      if (!html && time!=null) {
        // Fallback: look up rebased values directly from stored data arrays (so legend matches chart scale)
        selectedTickers.forEach(t=>{
          if (hiddenTickers.has(t)) return;
          const arr = latestRebasedData[t];
          if(!arr) return;
          // find nearest point equal to time
          const idx = arr.findIndex(p=>p.time===time);
          if(idx===-1) return;
          const price = arr[idx].value;
          if(price==null||isNaN(price)) return;
          const color = tickerColorMap.get(t) || '#000';
          const ps = priceSeriesMap.get(t);
          rows.push({t, price, color});
        });
      }
      // Build legend HTML sorted by price descending
      if(rows.length){
        rows.sort((a,b)=>b.price - a.price);
        html = rows.map(({t,price,color})=>`<div><span style=\"color:${color};font-weight:bold\">${t}</span>: ${formatPct(price)}</div>`).join('');
      }
      if (!html) {
        legendEl.style.display = 'none';
        return;
      }
      legendEl.innerHTML = html;
      legendEl.style.display = 'block';
      const offset = 10;
      let x = param.point.x + offset;
      let y = param.point.y + offset;
      const boxW = chartBox.clientWidth;
      const boxH = chartBox.clientHeight;
      const legendW = legendEl.offsetWidth;
      const legendH = legendEl.offsetHeight;
      if (x + legendW > boxW) x = param.point.x - legendW - offset;
      if (y + legendH > boxH) y = param.point.y - legendH - offset;
      legendEl.style.left = x + 'px';
      legendEl.style.top = y + 'px';
    });

    // Initialize bottom diff pane (optional)
    const ensureBottomPane = () => {
      if (showDiff && !bottomPane) {
        bottomPane = chart.addPane({ height: 120 });
        bottomPaneIndex = bottomPane.paneIndex ? bottomPane.paneIndex() : 1;
      }
      if (!showDiff && bottomPane) {
        chart.removePane(bottomPane);
        bottomPane = null;
        bottomPaneIndex = null;
      }
    };

    // Initialize volatility pane (always present once any ticker plotted)
    const ensureVolPane = () => {
      if (showVolPane) {
        if (!volPane) {
          volPane = chart.addPane({ height: 120 });
          volPaneIndex = volPane.paneIndex ? volPane.paneIndex() : (bottomPaneIndex != null ? bottomPaneIndex + 1 : 1);
        }
      } else {
        if (volPane) {
          chart.removePane(volPane);
          volPane = null;
          volSeriesMap.clear();
        }
      }
    };

    // ---------------- Helpers ----------------
    function renderChips(tickers) {
      chipsContainer.innerHTML = '';
      tickers.forEach((t, idx) => {
        const chip = document.createElement('span');
        chip.className = 'chip';
        const color = tickerColorMap.get(t) || colors[idx % colors.length];
        chip.style.backgroundColor = color;
        chip.style.color = '#fff';
        chip.textContent = t;

        // Toggle visibility
        chip.addEventListener('click', () => {
           const currentlyOff = chip.classList.contains('off');
          const priceSeries = priceSeriesMap.get(t);
          if (!priceSeries) return;
          const off = chip.classList.toggle('off');
           if(off){ hiddenTickers.add(t); } else { hiddenTickers.delete(t); }
           priceSeries.applyOptions({ visible: !off });
          const diffSeries = diffSeriesMap.get(t);
          if (diffSeries) diffSeries.applyOptions({ visible: !off });
          const volSeries = volSeriesMap.get(t);
          if (volSeries) volSeries.applyOptions({ visible: !off });
           if(showAvg) updateAverageSeries();
        });

        // Remove ticker
        const close = document.createElement('span');
        close.className = 'close';
        close.textContent = '×';
        close.addEventListener('click', (e) => {
          e.stopPropagation();
          selectedTickers.delete(t);
           hiddenTickers.delete(t);
          renderChips(Array.from(selectedTickers));
          card._selectedTickers = new Set(selectedTickers);
          saveCards();
          plot();
        });
        chip.appendChild(close);
        chipsContainer.appendChild(chip);
      });
    }

    // add ticker helper
    function drawAverage(sortedTickers, timeRange=null){
      const active = sortedTickers.filter(t=>!hiddenTickers.has(t));
      if(active.length===0){ if(avgSeries){ chart.removeSeries(avgSeries); avgSeries=null; } return; }
      const timeMap = new Map();
      active.forEach(t=>{
        const series = latestRebasedData[t] || [];
        if(series.length===0) return;
        // determine rebasing factor based on first point within visible range (or 1 if no range)
        let factor = 1;
        if(timeRange){
          const firstVisible = series.find(pt=>pt.time>=timeRange.from && pt.time<=timeRange.to);
          if(!firstVisible) return; // no data in range
          factor = 100/firstVisible.value;
        }
        series.forEach(pt=>{
          if(timeRange && (pt.time<timeRange.from || pt.time>timeRange.to)) return;
          const val = pt.value * factor;
          if(!timeMap.has(pt.time)) timeMap.set(pt.time,{sum:0,count:0});
          const e=timeMap.get(pt.time);
          e.sum += val; e.count++;
        });
      });
      const avgData = Array.from(timeMap.entries()).map(([time,{sum,count}])=>({time,value:sum/count}));
      if(!avgSeries){ avgSeries = chart.addSeries(LightweightCharts.LineSeries,{ color:'#000', lineWidth:2 }); }
      avgSeries.setData(avgData);
    }

    function updateAverageSeries(visibleRange=null){
      if(!showAvg) return;
      const sortedTickersList = Array.from(selectedTickers).sort();
      const range = visibleRange || chart.timeScale().getVisibleRange();
      drawAverage(sortedTickersList, range);
    }

    function addTicker(){
      const raw = inputEl.value.trim().replace(/['"]/g, '');
      if(!raw) return;
      raw.split(/[\s,]+/).forEach(tok=>{
        const t = tok.toUpperCase();
        if(t) selectedTickers.add(t);
      });
      inputEl.value='';
      renderChips(Array.from(selectedTickers));
            card._selectedTickers = new Set(selectedTickers);
      saveCards();
    }

    // ---------------- Plot Logic ----------------
    async function plot() {
      // Clear existing series
      for (const s of priceSeriesMap.values()) chart.removeSeries(s);
      for (const s of diffSeriesMap.values()) chart.removeSeries(s);
      for (const s of volSeriesMap.values()) chart.removeSeries(s);
      priceSeriesMap.clear();
      diffSeriesMap.clear();
      volSeriesMap.clear();
      if(avgSeries){ chart.removeSeries(avgSeries); avgSeries=null; }
      hiddenTickers.clear();
      // keep existing color mapping so colors stay stable
// tickerColorMap is not cleared anymore to preserve assigned colors
      zeroLineTop = zeroLineBottom = null;
      ensureBottomPane();

      // --- Volatility Pane ---
      if (volPane && !showVolPane) {
         chart.removePane(volPane);
         volPane = null;
         volSeriesMap.clear();
       }
       ensureVolPane();

      const tickers = Array.from(selectedTickers);
      if (!tickers.length) return;
      const resp = await fetch(`http://localhost:5000/api/data?tickers=${tickers.join(',')}`);
      if (!resp.ok) { alert('API error'); return; }
      const rawData = await resp.json();

      // Normalize
      const rebasedData = {};
       latestRebasedData = rebasedData;
      tickers.forEach(ticker => {
        let data = (rawData[ticker] || []).filter(p => p.value != null);
        data = data.sort((a,b)=>a.time-b.time);
        if (!data.length) return;
        const base = data.find(p=>p.value!==0)?.value;
        if (!base) return;
        rebasedData[ticker] = data.map(p=>({time:p.time, value:(p.value/base)*100}));
      });

      // Sort by latest
      const sortedTickers = [...tickers].sort((a,b)=>{
        const aval = rebasedData[a]?.slice(-1)[0]?.value ?? 0;
        const bval = rebasedData[b]?.slice(-1)[0]?.value ?? 0;
        return bval - aval;
      });
      renderChips(Array.from(selectedTickers));

      // Average + diff
      const timeMap = new Map();
      Object.values(rebasedData).forEach(series=>{
        series.forEach(pt=>{
          if(!timeMap.has(pt.time)) timeMap.set(pt.time,{sum:0,count:0});
          const e = timeMap.get(pt.time); e.sum+=pt.value; e.count++;
        });
      });
      const avgLookup = new Map(Array.from(timeMap.entries()).map(([time,{sum,count}])=>[time,sum/count]));

      const diffData = {};
      sortedTickers.forEach(t=>{
        diffData[t] = (rebasedData[t]||[]).map(p=>({time:p.time, value:(p.value - (avgLookup.get(p.time)??0))}));
      });

      // Plot loops
      sortedTickers.forEach(ticker=>{
        let color = tickerColorMap.get(ticker);
        if(!color){
          color = colors[colorIndex % colors.length];
           tickerColorMap.set(ticker, color);
           colorIndex++; // advance only when assigning a new color
         }
        const priceSeries = chart.addSeries(LightweightCharts.LineSeries,{ color, priceLineVisible:false,
          priceFormat:{ type:'custom', minMove:0.1, formatter:(v)=>{
            const diff=v-100; const sign=diff>0?'+':diff<0?'-':''; const dec=Math.abs(diff)>=100?0:1; return `${sign}${Math.abs(diff).toFixed(dec)}%`; } } });
        priceSeries.setData(rebasedData[ticker]);
        if(!zeroLineTop){ zeroLineTop = priceSeries.createPriceLine({ price:100,color:'#888',lineWidth:1,lineStyle:LightweightCharts.LineStyle.Dotted,axisLabelVisible:true,title:'0%' }); }
        priceSeriesMap.set(ticker, priceSeries);

        // rolling volatility (100-day standard deviation of daily % returns)
          if (showVolPane) {
          const originalSrc = (rawData[ticker] || []).filter(p => p.value != null).sort((a,b)=>a.time-b.time);
          const volData = [];
          const returns = [];
          for (let i = 1; i < originalSrc.length; i++) {
            const pct = (originalSrc[i].value / originalSrc[i-1].value) - 1;
            returns.push(pct);
            if (returns.length >= VOL_WINDOW) {
              const window = returns.slice(-VOL_WINDOW);
              const mean = window.reduce((a, b) => a + b, 0) / VOL_WINDOW;
              const variance = window.reduce((s, r) => s + Math.pow(r - mean, 2), 0) / (VOL_WINDOW - 1); // Sample variance
              const dailyStdDev = Math.sqrt(variance);
              const annualizedVol = dailyStdDev * Math.sqrt(252) * 100; // annualize and convert to %
              volData.push({ time: originalSrc[i].time, value: annualizedVol });
            }
          }
          const volSeries = chart.addSeries(
            LightweightCharts.LineSeries,
            {
              color,
              lineWidth: 1,
              priceLineVisible: false,
              priceFormat: {
                type: 'custom',
                minMove: 0.1,
                formatter: (v) => v.toFixed(2) + '%',
              },
            },
            volPaneIndex
          );
          volSeries.setData(volData);
          volSeriesMap.set(ticker, volSeries);
          }

        if(showDiff && bottomPane){
          const diffSeries = chart.addSeries(LightweightCharts.LineSeries,{ color,lineWidth:1,lineStyle:LightweightCharts.LineStyle.Dotted, priceLineVisible:false, priceFormat:{ type:'custom',minMove:0.1,formatter:(v)=>{const sign=v>0?'+':v<0?'-':'';const dec=Math.abs(v)>=100?0:1;return `${sign}${Math.abs(v).toFixed(dec)}%`;}} }, bottomPaneIndex);
          diffSeries.setData(diffData[ticker]);
          if(!zeroLineBottom){ zeroLineBottom = diffSeries.createPriceLine({ price:0,color:'#888',lineWidth:1,lineStyle:LightweightCharts.LineStyle.Dotted,axisLabelVisible:true,title:'0%' }); }
          diffSeriesMap.set(ticker,diffSeries);
        }
        originalNormalizedData[ticker] = rebasedData[ticker];

      });

      if(showAvg){
        drawAverage(sortedTickers);
      }
      // now chips with correct colors
      renderChips(sortedTickers);
      // persist state
      card._selectedTickers = new Set(selectedTickers);
      card._showDiff = showDiff;
      card._showAvg = showAvg;
      card._showVol = showVolPane;
      saveCards();

      chart.timeScale().fitContent();
      chart.priceScale('right').applyOptions({ mode: LightweightCharts.PriceScaleMode.Logarithmic });

      if(!plot._rebasingAttached){
        chart.timeScale().subscribeVisibleTimeRangeChange((visible)=>{
          if(!visible||!visible.from) return;
          const from = Math.round(visible.from);
          priceSeriesMap.forEach((series,ticker)=>{
            const data = originalNormalizedData[ticker];
            if(!data?.length) return;
            const first = data.find(p=>p.time>=from);
            if(!first||first.value===0) return;
            const factor = 100/first.value;
            series.setData(data.map(pt=>({time:pt.time,value:pt.value*factor})));
          });
          if(showAvg) updateAverageSeries(visible);
        });
        plot._rebasingAttached=true;
      }
    }

    // ---------------- Event Wiring ----------------
    plotBtn.addEventListener('click', plot);

    const addChartBtn = card.querySelector('.add-chart-btn');
    addChartBtn.addEventListener('click', () => {
      const newCard = createChartCard('', showDiff, showAvg, showVolPane);
      saveCards();
      if(card.nextSibling){
        wrapper.insertBefore(newCard, card.nextSibling);
      }
    }); 
    
    toggleDiffBtn.addEventListener('click',()=>{
      showDiff = !showDiff;
      card._showDiff = showDiff;
      toggleDiffBtn.textContent = showDiff ? 'Hide Diff Pane' : 'Show Diff Pane';
      saveCards();
      plot();
    });
    toggleVolBtn.addEventListener('click',()=>{
      showVolPane = !showVolPane;
      card._showVol = showVolPane;
      toggleVolBtn.textContent = showVolPane ? 'Hide Vol Pane' : 'Show Vol Pane';
      saveCards();
      if (showVolPane) { plot(); } else { if (volPane){ chart.removePane(volPane); volPane=null; volSeriesMap.clear(); } }
    });

    toggleAvgBtn.addEventListener('click',()=>{
      showAvg=!showAvg;
      toggleAvgBtn.textContent = showAvg?'Hide Avg':'Show Avg';
      card._showAvg = showAvg;
      saveCards();
      if(showAvg){
        updateAverageSeries();
      } else {
        if(avgSeries){ chart.removeSeries(avgSeries); avgSeries=null; }
      }
    });
    rangeBtns.forEach(btn=>{
      btn.addEventListener('click',()=>{
        let startYear;
        if(btn.dataset.range==='ytd'){
          startYear = new Date().getUTCFullYear();
        } else {
          startYear = parseInt(btn.dataset.range,10);
        }
        const from = Date.UTC(startYear,0,1)/1000;
        const to = Math.floor(Date.now()/1000);
        chart.timeScale().setVisibleRange({from,to});
      });
    });
    card.querySelector('.remove-card-btn').addEventListener('click',()=>{ wrapper.removeChild(card);
     saveCards(); });

    // initial plot
    plot();

    // return DOM element for callers (e.g., Add Chart button)
    return card;
  }

  document.addEventListener('DOMContentLoaded', () => {
    // move existing Add Chart button from inline page
    const addBtn = document.getElementById('add-chart-btn');
    if(addBtn){
      addBtn.addEventListener('click', () => createChartCard(''));
    }
    // populate autocomplete list
    fetch('http://localhost:5000/api/tickers')
      .then(r=>r.json())
      .then(list=>{
        const dl=document.getElementById('ticker-list');
        if(dl){ dl.innerHTML=''; list.forEach(t=>{ const opt=document.createElement('option'); opt.value=t; dl.appendChild(opt);}); }
      })
      .catch(()=>{});

    // create first card automatically using any preset tickers in localStorage or default
    const stored = JSON.parse(localStorage.getItem('sandbox_cards')||'[]');
     if(stored.length){
       stored.forEach(c=>createChartCard(c.tickers.join(', '), c.showDiff, c.showAvg, c.showVol));
     }else{
       createChartCard('SPY');
     }
  });
})();
