// Lightweight Charts sandbox multi-card module
// Creates self-contained chart cards with independent state.
(() => {
  const WRAPPER_ID = 'charts-wrapper';
  const colors = ['#008FFB','#00E396','#FEB019','#FF4560','#775DD0','#546E7A','#26a69a','#D10CE8'];
  let globalCardCounter = 0;

  function createChartCard(initialTickers = 'SPY') {
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
        <button class="toggle-diff-btn">Show Diff Pane</button>
        <button class="add-chart-btn">Add Chart</button>
        <button class="remove-card-btn">Remove</button>
        <div class="ticker-chips"></div>
        
      </div>
      <div class="chart-box"></div>
    `;

    wrapper.appendChild(card);

    // ---------------- State ----------------
    let showDiff = false;
    const selectedTickers = new Set(initialTickers ? initialTickers.split(/[,\s]+/).filter(Boolean).map(t=>t.toUpperCase()) : []);
    const priceSeriesMap = new Map();
    const diffSeriesMap = new Map();
    const tickerColorMap = new Map();
    let bottomPane = null;
    let bottomPaneIndex = null;
    let zeroLineTop = null;
    let zeroLineBottom = null;
    const originalNormalizedData = {};
    let colorIndex = 0;

    // Elements
    const inputEl = card.querySelector('.ticker-input');
    const addTickerBtn = card.querySelector('.add-ticker-btn');
    addTickerBtn.addEventListener('click', addTicker);
    inputEl.addEventListener('keyup', e=>{ if(e.key==='Enter') addTicker(); });
    const plotBtn = card.querySelector('.plot-btn');
    const toggleDiffBtn = card.querySelector('.toggle-diff-btn');
    const chipsContainer = card.querySelector('.ticker-chips');
    const chartBox = card.querySelector('.chart-box');

    // Create chart instance
    const chart = LightweightCharts.createChart(chartBox, {
      layout: { background: { type: 'solid', color: '#ffffff' }, textColor: '#333' },
      grid: { vertLines: { color: '#eee' }, horzLines: { color: '#eee' } },
      timeScale: { secondsVisible: false, rightOffset: 10, fixLeftEdge: true },
      rightPriceScale: { visible: true, scaleMargins: { top: 0.1, bottom: 0.1 } },
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
          const priceSeries = priceSeriesMap.get(t);
          if (!priceSeries) return;
          const off = chip.classList.toggle('off');
          priceSeries.applyOptions({ visible: !off });
          const diffSeries = diffSeriesMap.get(t);
          if (diffSeries) diffSeries.applyOptions({ visible: !off });
        });

        // Remove ticker
        const close = document.createElement('span');
        close.className = 'close';
        close.textContent = '×';
        close.addEventListener('click', (e) => {
          e.stopPropagation();
          selectedTickers.delete(t);
          renderChips(Array.from(selectedTickers));
          plot();
        });
        chip.appendChild(close);
        chipsContainer.appendChild(chip);
      });
    }

    // add ticker helper
    function addTicker(){
      const raw = inputEl.value.trim();
      if(!raw) return;
      raw.split(/[\s,]+/).forEach(tok=>{
        const t = tok.toUpperCase();
        if(t) selectedTickers.add(t);
      });
      inputEl.value='';
      renderChips(Array.from(selectedTickers));
    }

    // ---------------- Plot Logic ----------------
    async function plot() {
      // Clear existing series
      for (const s of priceSeriesMap.values()) chart.removeSeries(s);
      for (const s of diffSeriesMap.values()) chart.removeSeries(s);
      priceSeriesMap.clear();
      diffSeriesMap.clear();
      tickerColorMap.clear();
      zeroLineTop = zeroLineBottom = null;
      colorIndex = 0;
      ensureBottomPane();

      const tickers = Array.from(selectedTickers);
      if (!tickers.length) return;
      const resp = await fetch(`http://localhost:5000/api/data?tickers=${tickers.join(',')}`);
      if (!resp.ok) { alert('API error'); return; }
      const rawData = await resp.json();

      // Normalize
      const rebasedData = {};
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
        const color = colors[colorIndex % colors.length];
        tickerColorMap.set(ticker, color);
        const priceSeries = chart.addSeries(LightweightCharts.LineSeries,{ color,
          priceFormat:{ type:'custom', minMove:0.1, formatter:(v)=>{
            const diff=v-100; const sign=diff>0?'+':diff<0?'-':''; const dec=Math.abs(diff)>=100?0:1; return `${sign}${Math.abs(diff).toFixed(dec)}%`; } } });
        priceSeries.setData(rebasedData[ticker]);
        if(!zeroLineTop){ zeroLineTop = priceSeries.createPriceLine({ price:100,color:'#888',lineWidth:1,lineStyle:LightweightCharts.LineStyle.Dotted,axisLabelVisible:true,title:'0%' }); }
        priceSeriesMap.set(ticker, priceSeries);

        if(showDiff && bottomPane){
          const diffSeries = chart.addSeries(LightweightCharts.LineSeries,{ color,lineWidth:1,lineStyle:LightweightCharts.LineStyle.Dotted, priceFormat:{ type:'custom',minMove:0.1,formatter:(v)=>{const sign=v>0?'+':v<0?'-':'';const dec=Math.abs(v)>=100?0:1;return `${sign}${Math.abs(v).toFixed(dec)}%`;}} }, bottomPaneIndex);
          diffSeries.setData(diffData[ticker]);
          if(!zeroLineBottom){ zeroLineBottom = diffSeries.createPriceLine({ price:0,color:'#888',lineWidth:1,lineStyle:LightweightCharts.LineStyle.Dotted,axisLabelVisible:true,title:'0%' }); }
          diffSeriesMap.set(ticker,diffSeries);
        }
        originalNormalizedData[ticker] = rebasedData[ticker];
        colorIndex++;
      });

      // now chips with correct colors
      renderChips(sortedTickers);

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
        });
        plot._rebasingAttached=true;
      }
    }

    // ---------------- Event Wiring ----------------
    plotBtn.addEventListener('click', plot);
    const addChartBtn = card.querySelector('.add-chart-btn');
    addChartBtn.addEventListener('click', () => {
      const newCard = createChartCard('');
      if(card.nextSibling){
        wrapper.insertBefore(newCard, card.nextSibling);
      }
    });
    
    toggleDiffBtn.addEventListener('click',()=>{ showDiff=!showDiff; toggleDiffBtn.textContent = showDiff?'Hide Diff Pane':'Show Diff Pane'; plot(); });
    card.querySelector('.remove-card-btn').addEventListener('click',()=>{ wrapper.removeChild(card); });

    // initial plot
    plot();
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
    createChartCard(localStorage.getItem('sandbox_tickers') || 'SPY');
  });
})();
