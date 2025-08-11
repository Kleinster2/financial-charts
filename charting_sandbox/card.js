// Lightweight Charts sandbox multi-card module
// Creates self-contained chart cards with independent state.
(() => {
  const WRAPPER_ID = 'charts-wrapper';
  const colors = [
    '#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf',
    '#393b79','#637939','#8c6d31','#843c39','#7b4173','#3182bd','#31a354','#756bb1','#636363','#e6550d',
    '#e31a1c','#6baed6','#9ecae1','#c6dbef','#fd8d3c','#fdd0a2','#fdae6b','#a1d99b','#74c476','#31a354',
    '#6baed6','#9e9ac8','#bcbddc','#dadaeb','#fcbba1','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d',
    '#084594','#4292c6','#6baed6','#9ecae1','#c6dbef','#d9f0a3','#addd8e','#78c679','#41ab5d','#238443',
    '#006837','#004529','#990099','#ff0099','#00bfff','#ffa500','#ff0000','#00ff00','#008FFB','#00E396',
    '#008FFB', '#00E396', '#FEB019', '#FF4560', '#775DD0', '#546E7A', '#26a69a', '#D10CE8',
    '#FF66C3', '#FF8633', '#2B908F', '#F0E442', '#3D85C6', '#A52A2A', '#FFD700', '#00BFFF',
    '#FF1493', '#00FA9A', '#9932CC', '#FF4500', '#4B0082'
  ];
  let globalCardCounter = 0;

  // --- Company name cache (ticker -> name) ---
  const nameCache = {};
  async function ensureNames(tickers){
    const missing = tickers.filter(t=>!(t in nameCache));
    if(!missing.length) return;
    
    try {
      const metadata = await window.DataFetcher.getMetadata(missing);
      Object.assign(nameCache, metadata);
      
      // refresh titles on existing chips
      document.querySelectorAll('.chip').forEach(ch=>{
        const t = ch.dataset.ticker;
        if(nameCache[t]) ch.title = nameCache[t];
      });
    } catch (error) {
      console.error('Failed to fetch metadata:', error);
    }
  }
  const VOL_WINDOW = 100; // rolling volatility window (days)

  // Save all chart states using StateManager
  function saveCards(){
    const cards = Array.from(document.querySelectorAll('.chart-card')).map(card=>({
      tickers: Array.from(card._selectedTickers||[]),
      showDiff: !!card._showDiff,
      showAvg: !!card._showAvg,
      showVol: !!card._showVol,
      multipliers: Object.fromEntries(card._multiplierMap ? Array.from(card._multiplierMap.entries()) : []),
      hidden: Array.from(card._hiddenTickers || []),
      range: card._visibleRange || null,
      useRaw: card._useRaw || false,
      title: card._title || ''
    }));
    
    // Use StateManager for persistence (includes debouncing)
    if (window.StateManager) {
      window.StateManager.saveCardsDebounced(cards);
    } else {
      // Fallback to direct localStorage
      localStorage.setItem('sandbox_cards', JSON.stringify(cards));
    }
  }

  function createChartCard(initialTickers = 'SPY', initialShowDiff = false, initialShowAvg = false, initialShowVol = true, initialUseRaw = false, initialMultipliers = {}, initialHidden = [], initialRange = null, initialTitle = '', wrapperEl = null) {
    const wrapper = wrapperEl || document.getElementById(WRAPPER_ID);
    if (!wrapper) { console.error('Missing charts wrapper'); return; }

    // ---------------- Build DOM ----------------
    const card = document.createElement('div');
  // Assign a unique id so navigation links can target this card
  globalCardCounter += 1;
  const cardId = `chart-${globalCardCounter}`;
  card.id = cardId;
    card.className = 'chart-card';

    card.innerHTML = `
      <div class="controls">
        <input type="text" class="ticker-input" list="ticker-list" placeholder="e.g. AAPL">
        <button class="add-ticker-btn">Add</button>
        <button class="plot-btn">Plot</button>
        <!-- Range dropdown -->
        <select class="range-select">
          <option value="" disabled selected>Range</option>
          <option value="ytd">YTD</option>
          <option value="2024">2024-</option>
          <option value="2023">2023-</option>
          <option value="2022">2022-</option>
          <option value="2021">2021-</option>
          <option value="2020">2020-</option>
        </select>
        <button class="toggle-diff-btn">Show Diff Pane</button>
        <button class="toggle-vol-btn">Hide Vol Pane</button>
        <button class="toggle-avg-btn">Show Avg</button>
        <button class="toggle-raw-btn">Show Raw</button>
        <button class="add-chart-btn">Add Chart</button>
        <button class="remove-card-btn">Remove</button>
        <input type="text" class="title-input" placeholder="Chart title..." style="margin-left:8px;width:140px;">
        <div class="ticker-chips"></div>
        
      </div>
      <div class="card-title" style="font-weight:bold;font-size:16px;margin:6px 0;">${initialTitle}</div>
      <div class="chart-box"></div>
    `;

    // ---------------- State ----------------
    let showDiff = initialShowDiff;
    let showAvg = initialShowAvg;
    let showVolPane = initialShowVol;
    let useRaw = initialUseRaw;
    const selectedTickers = new Set(initialTickers ? initialTickers.split(/[,\s]+/).filter(Boolean).map(t=>t.toUpperCase()) : []);

    // ---------- Navigation link ----------
    const nav = document.getElementById('chart-nav');
    let navLabel = initialTitle || (selectedTickers.size ? Array.from(selectedTickers)[0] : `Card ${globalCardCounter}`);
    let navLink = null;
    if(nav){
      navLink = document.createElement('a');
      navLink.href = `#${cardId}`;
      navLink.textContent = navLabel;
      nav.appendChild(navLink);
    }

    // Append the card to DOM
    wrapper.appendChild(card);

    // ---------------- More State ----------------
    const multiplierMap = new Map(); // ticker -> beta multiplier (default 1)
    // Apply initial multipliers if provided
    if(initialMultipliers && typeof initialMultipliers === 'object'){
      Object.entries(initialMultipliers).forEach(([t,v])=>{
        const num = parseFloat(v);
        if(!isNaN(num)) multiplierMap.set(t.toUpperCase(), num);
      });
    }
    const priceSeriesMap = new Map();
    const diffSeriesMap = new Map();
    const volSeriesMap = new Map();
    let avgSeries = null;
    let latestRebasedData = {};
    const rawPriceMap = new Map(); // ticker -> raw price array
    const hiddenTickers = new Set(initialHidden ? initialHidden.map(t=>t.toUpperCase()) : []);
    let savedRange = initialRange; // {from,to} epoch seconds
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
    card._multiplierMap = multiplierMap;
    card._visibleRange = savedRange;
    card._title = initialTitle || '';
    card._hiddenTickers = hiddenTickers;

    // Elements
    const inputEl = card.querySelector('.ticker-input');
    const addTickerBtn = card.querySelector('.add-ticker-btn');
    addTickerBtn.addEventListener('click', addTicker);
    inputEl.addEventListener('keyup', e=>{ if(e.key==='Enter') addTicker(); });
    const plotBtn = card.querySelector('.plot-btn');
    const titleInput = card.querySelector('.title-input');
    const titleDisplay = card.querySelector('.card-title');
    if(titleInput){
      titleInput.value = initialTitle || '';
      const updateTitle=()=>{ titleDisplay.textContent = titleInput.value; };
      updateTitle();
      titleInput.addEventListener('input',()=>{ 
        card._title = titleInput.value; 
        updateTitle(); 
        if(navLink){ navLink.textContent = titleInput.value || navLabel; }
        saveCards(); 
      });
    }
    const toggleDiffBtn = card.querySelector('.toggle-diff-btn');
    const toggleVolBtn = card.querySelector('.toggle-vol-btn');
    const toggleAvgBtn = card.querySelector('.toggle-avg-btn');
    const toggleRawBtn = card.querySelector('.toggle-raw-btn');
    const rangeSelect = card.querySelector('.range-select');
    toggleAvgBtn.textContent = showAvg ? 'Hide Avg':'Show Avg';
    toggleRawBtn.textContent = useRaw ? 'Show % Basis' : 'Show Raw';
    toggleDiffBtn.textContent = showDiff ? 'Hide Diff Pane' : 'Show Diff Pane';
    const removeBtn = card.querySelector('.remove-card-btn');
    const chipsContainer = card.querySelector('.ticker-chips');

    if(removeBtn){
      removeBtn.addEventListener('click', ()=>{
        if(navLink && navLink.parentElement){ navLink.parentElement.removeChild(navLink); }
        card.remove();
        saveCards();
      });
    }
    const chartBox = card.querySelector('.chart-box');

    // Create chart instance
    const chart = LightweightCharts.createChart(chartBox, {
      layout: { background: { type: 'solid', color: '#ffffff' }, textColor: '#333' },
      grid: { vertLines: { color: '#eee' }, horzLines: { color: '#eee' } },
      timeScale: { secondsVisible: false, rightOffset: 10, fixLeftEdge: true },
      rightPriceScale: { visible: true, scaleMargins: { top: 0.1, bottom: 0.1 } },
      // Disable horizontal crosshair and its Y-axis label while keeping vertical crosshair & X-axis label
      crosshair: {
        horzLine: {
          visible: false,
          labelVisible: false,
        },
        vertLine: {
          visible: true,
          labelVisible: true,
        },
      }
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
    const formatPrice = (v)=>{ if(v>=1000) return v.toFixed(0); if(v>=100) return v.toFixed(1); return v.toFixed(2); };
    chart.subscribeCrosshairMove(param => {
      const formatter = useRaw ? formatPrice : formatPct;
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
          const arr = useRaw ? rawPriceMap.get(t) : latestRebasedData[t];
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
        html = rows.map(({t,price,color})=>`<div><span style=\"color:${color};font-weight:bold\">${t}</span>: ${formatter(price)}</div>`).join('');
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
      if (volPane && !showVolPane) {
         chart.removePane(volPane);
         volPane = null;
         volSeriesMap.clear();
       }
       if (showVolPane) {
        if (!volPane) {
          volPane = chart.addPane({ height: 120 });
          volPaneIndex = volPane.paneIndex ? volPane.paneIndex() : (bottomPaneIndex != null ? bottomPaneIndex + 1 : 1);
        }
      }
    };

    // ---------------- Helpers ----------------
    function renderChips(tickers) {
      ensureNames(tickers);
      chipsContainer.innerHTML = '';
      tickers.forEach((t, idx) => {
        const chip = document.createElement('span');
         chip.dataset.ticker = t;
        chip.className = 'chip';
        chip.style.position='relative';
        if(hiddenTickers.has(t)){ chip.classList.add('off'); }
        const color = tickerColorMap.get(t) || colors[idx % colors.length];
        chip.style.backgroundColor = color;
        chip.style.color = '#fff';
         if(nameCache[t]) chip.title = nameCache[t];
         chip.style.cursor='help';
        const mult = multiplierMap.get(t) || 1;
        const updateLabel = ()=>{ chip.childNodes[0].textContent = `${t} × ${multiplierMap.get(t)?.toFixed(1)||'1.0'}`};
        const labelSpan=document.createElement('span');
        labelSpan.textContent=`${t} × ${mult.toFixed(1)}`;
        chip.appendChild(labelSpan);

        // multiplier slider
        const slider=document.createElement('input');
        slider.type='range';
        slider.min='0.1';
        slider.max='3';
        slider.step='0.1';
        slider.value=mult;
        slider.className='mult-slider';
        Object.assign(slider.style,{position:'absolute',left:'0',right:'0',bottom:'-18px',display:'none',width:'100px'});
        chip.appendChild(slider);
        chip.addEventListener('mouseenter',()=>{slider.style.display='block';});
        chip.addEventListener('mouseleave',()=>{slider.style.display='none';});
        slider.addEventListener('input',e=>{
          const val=parseFloat(e.target.value);
          multiplierMap.set(t,val);
          updateLabel();
        });
        slider.addEventListener('change',()=>{ // replot on commit
          plot();
          saveCards();
        });

        // Toggle visibility
        chip.addEventListener('click', () => {
           const currentlyOff = chip.classList.contains('off');
          const priceSeries = priceSeriesMap.get(t);
          if (!priceSeries) return;
          const off = chip.classList.toggle('off');
           if(off){ hiddenTickers.add(t); } else { hiddenTickers.delete(t); }
          card._hiddenTickers = hiddenTickers;
          saveCards();
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

    // Futures notional multipliers (price units × contract size)
    // Only include contracts with well-known specs; others default to 1.
    const FUTURES_MULTIPLIERS = Object.freeze({
      // Equity index
      'ES=F': 50,   // S&P 500 E-mini: $50 × index
      'NQ=F': 20,   // Nasdaq-100 E-mini: $20 × index
      'YM=F': 5,    // Dow mini: $5 × index
      'RTY=F': 50,  // Russell 2000: $50 × index
      // Energy
      'CL=F': 1000,   // Crude Oil: $/bbl × 1000 bbl
      'BZ=F': 1000,   // Brent: $/bbl × 1000 bbl
      'NG=F': 10000,  // Nat Gas: $/mmBtu × 10,000 mmBtu
      'RB=F': 42000,  // RBOB: $/gal × 42,000 gal
      // Metals
      'GC=F': 100,    // Gold: $/oz × 100 oz
      'SI=F': 5000,   // Silver: $/oz × 5,000 oz
      'HG=F': 25000,  // Copper: $/lb × 25,000 lb
      'PL=F': 50,     // Platinum: $/oz × 50 oz
      'PA=F': 100,    // Palladium: $/oz × 100 oz
      // Rates (price in points; notional ≈ price/100 × face)
      'ZB=F': 1000,   // 30Y Bond: $100k face ⇒ $1000 per point
      'ZN=F': 1000,   // 10Y Note: $1000 per point
      'ZF=F': 1000,   // 5Y Note: $1000 per point
      'ZT=F': 2000,   // 2Y Note: $2000 per point (face $200k)
      'FGBL=F': 1000, // Euro-Bund: €1000 per point (no FX adjustment)
      // Ags/Softs
      'ZC=F': 5000,   // Corn: $/bu × 5,000 bu
      'ZS=F': 5000,   // Soybeans
      'ZW=F': 5000,   // Wheat (Chicago)
      'KE=F': 5000,   // Wheat (KC)
      'SB=F': 112000, // Sugar No.11: $/lb × 112,000 lb
      'KC=F': 37500,  // Coffee: $/lb × 37,500 lb
      'CC=F': 10,     // Cocoa: $/metric ton × 10 t
      'CT=F': 50000,  // Cotton: $/lb × 50,000 lb
      'OJ=F': 15000,  // Orange Juice: $/lb solids × 15,000 lb
    });

    function getFuturesContractMultiplier(ticker){
      return FUTURES_MULTIPLIERS[ticker] || 1;
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
      // hiddenTickers.clear(); // keep hidden tickers for persistence
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
      
      // Split normal tickers and ETF metric tokens (e.g., ALLW_VALUE, ALLW_SHARES)
      const etfTokens = tickers.filter(t => /_VALUE$|_SHARES$/.test(t));
      const normalTickers = tickers.filter(t => !/_VALUE$|_SHARES$/.test(t));
      
      // Fetch data for normal tickers
      const rawData = {};
      if (normalTickers.length > 0) {
        try {
          const data = await DataFetcher.getPriceData(normalTickers);
          Object.assign(rawData, data);
        } catch (error) {
          console.error('Error fetching price data:', error);
          alert('Failed to fetch price data');
          return;
        }
      }
      
      // Fetch ETF metric data
      if (etfTokens.length > 0) {
        const group = new Map(); // etf -> Set(metrics)
        etfTokens.forEach(tok => {
          const m = tok.match(/^([A-Z]+)_(VALUE|SHARES)$/);
          if (!m) return;
          const etf = m[1];
          const metric = m[2].toLowerCase(); // 'value' | 'shares'
          if (!group.has(etf)) group.set(etf, new Set());
          group.get(etf).add(metric);
        });
        
        for (const [etf, metricsSet] of group.entries()) {
          try {
            const metrics = Array.from(metricsSet);
            const data = await DataFetcher.getETFSeries(etf, metrics);
            if (data.value) rawData[`${etf}_VALUE`] = data.value;
            if (data.shares) rawData[`${etf}_SHARES`] = data.shares;
          } catch (error) {
            console.error(`Error fetching ETF data for ${etf}:`, error);
          }
        }
      }

      // Normalize
      const rebasedData = {};
       latestRebasedData = rebasedData;
      tickers.forEach(ticker => {
        let data = (rawData[ticker] || []).filter(p => p.value != null);
         rawPriceMap.set(ticker, data);
        data = data.sort((a,b)=>a.time-b.time);
        if (!data.length) return;
        if (useRaw) {
          rebasedData[ticker] = data.map(p => ({ time: p.time, value: p.value }));
        } else {
          const base = data.find(p => p.value !== 0)?.value;
          if (!base) return;
          const mult = multiplierMap.get(ticker) || 1;
          rebasedData[ticker] = data.map(p => {
            const norm = p.value / base; // 1 at t0
            const scaled = 1 + (norm - 1) * mult;
            return { time: p.time, value: scaled * 100 };
          });
        }
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

      // Plot loops - using for...of to handle async operations
      const volumeData = {};
      for (const ticker of sortedTickers) {
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
        if(useRaw){ priceSeries.applyOptions({ priceFormat:{ type:'custom', minMove:0.01, formatter:formatPrice } }); }
        if(hiddenTickers.has(ticker)) priceSeries.applyOptions({visible:false});
        if(!useRaw && !zeroLineTop){ zeroLineTop = priceSeries.createPriceLine({ price:100,color:'#888',lineWidth:1,lineStyle:LightweightCharts.LineStyle.Dotted,axisLabelVisible:true,title:'0%' }); }
        priceSeriesMap.set(ticker, priceSeries);

        // Trading dollar volume (price * shares) line pane
        if (showVolPane) {
          // Fetch volume data if not already available
          if (!volumeData[ticker]) {
            try {
              const volData = await DataFetcher.getVolumeData([ticker]);
              volumeData[ticker] = volData[ticker] || [];
            } catch (error) {
              console.error(`Failed to fetch volume data for ${ticker}:`, error);
              volumeData[ticker] = [];
            }
          }
          const volSrcRaw = (volumeData[ticker] || []).filter(p => p.value != null).sort((a,b)=>a.time-b.time);
          // Join with raw price by timestamp to compute dollar volume
          const priceArr = rawPriceMap.get(ticker) || [];
          const priceByTime = new Map(priceArr.map(pt => [pt.time, pt.value]));
          const dollarVolRaw = volSrcRaw
            .map(p => {
              const price = priceByTime.get(p.time);
              if (price == null) return null;
              const contractMult = getFuturesContractMultiplier(ticker);
              return { time: p.time, value: p.value * price * contractMult };
            })
            .filter(x => x && isFinite(x.value));
          // Log scale cannot display non-positive values; clamp to 1 for zeros/negatives
          const volSrc = dollarVolRaw.map(p => ({ time: p.time, value: (p.value > 0 ? p.value : 1) }));
          const volSeries = chart.addSeries(
            LightweightCharts.LineSeries,
            {
              color,
              lineWidth: 1,
              priceLineVisible: false,
              priceFormat: {
                type: 'custom',
                minMove: 1,
                formatter: (v) => {
                  if (v == null) return '';
                  const abs = Math.abs(v);
                  if (abs >= 1e12) return `$${(v/1e12).toFixed(2)}T`;
                  if (abs >= 1e9)  return `$${(v/1e9).toFixed(2)}B`;
                  if (abs >= 1e6)  return `$${(v/1e6).toFixed(2)}M`;
                  if (abs >= 1e3)  return `$${(v/1e3).toFixed(0)}K`;
                  return `$${Math.round(v)}`;
                },
              },
            },
            volPaneIndex
          );
          // Set logarithmic scale for the volume pane via the series' price scale
          try {
            const volScale = typeof volSeries.priceScale === 'function' ? volSeries.priceScale() : null;
            if (volScale && typeof volScale.applyOptions === 'function') {
              volScale.applyOptions({ mode: LightweightCharts.PriceScaleMode.Logarithmic });
            }
          } catch (_) { /* noop */ }
          volSeries.setData(volSrc);
          if(hiddenTickers.has(ticker)) volSeries.applyOptions({visible:false});
          volSeriesMap.set(ticker, volSeries);
        }

        if(showDiff && bottomPane){
          const diffSeries = chart.addSeries(LightweightCharts.LineSeries,{ color,lineWidth:1,lineStyle:LightweightCharts.LineStyle.Dotted, priceLineVisible:false, priceFormat:{ type:'custom',minMove:0.1,formatter:(v)=>{const sign=v>0?'+':v<0?'-':'';const dec=Math.abs(v)>=100?0:1;return `${sign}${Math.abs(v).toFixed(dec)}%`;}} }, bottomPaneIndex);
          diffSeries.setData(diffData[ticker]);
          if(hiddenTickers.has(ticker)) diffSeries.applyOptions({visible:false});
          if(!zeroLineBottom){ zeroLineBottom = diffSeries.createPriceLine({ price:0,color:'#888',lineWidth:1,lineStyle:LightweightCharts.LineStyle.Dotted,axisLabelVisible:true,title:'0%' }); }
          diffSeriesMap.set(ticker,diffSeries);
        }
        originalNormalizedData[ticker] = rebasedData[ticker];

      }

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

      if(savedRange && savedRange.from && savedRange.to){ chart.timeScale().setVisibleRange(savedRange);} else { chart.timeScale().fitContent(); }
      chart.priceScale('right').applyOptions({ mode: LightweightCharts.PriceScaleMode.Logarithmic });

      if(!plot._rebasingAttached){
        // Create a debounced rebase function using ChartUtils
        const debouncedRebase = window.ChartUtils ? 
          window.ChartUtils.debounce(() => {
            if(useRaw) return;
            console.log('Rebasing data to visible range...', visible);
            // Rebase logic will be implemented here
            // For now, just save the range
            if(visible && visible.from){ 
              card._visibleRange = visible; 
              saveCards(); 
            }
          }, 500) : 
          // Fallback if ChartUtils not available
          ((fn, delay) => {
            let timeoutId;
            return (...args) => {
              clearTimeout(timeoutId);
              timeoutId = setTimeout(() => fn(...args), delay);
            };
          })(() => {
            if(visible && visible.from){ 
              card._visibleRange = visible; 
              saveCards(); 
            }
          }, 500);
        
        chart.timeScale().subscribeVisibleTimeRangeChange((visible)=>{
          if(useRaw) return;
          debouncedRebase(visible);
          if(!visible||!visible.from) return;
          const from = Math.round(visible.from);
          priceSeriesMap.forEach((series,ticker)=>{
            const raw = rawPriceMap.get(ticker);
            if(!raw?.length) return;
            
            const first = raw.find(p=>p.time>=from);
            if(!first||first.value===0) return;
            const base = first.value;
            const mult = multiplierMap.get(ticker) || 1;
            const rebased = raw.map(pt=>{
              const norm = pt.value / base;
              const scaled = 1 + (norm - 1) * mult;
              return {time: pt.time, value: scaled * 100};
            });
            series.setData(rebased);
            latestRebasedData[ticker] = rebased; // keep legend data aligned
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
      const newCard = createChartCard('', showDiff, showAvg, showVolPane, useRaw, Object.fromEntries(multiplierMap), Array.from(hiddenTickers), card._visibleRange, '', null);
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

    toggleRawBtn.addEventListener('click',()=>{
       useRaw = !useRaw;
       card._useRaw = useRaw;
       toggleRawBtn.textContent = useRaw ? 'Show % Basis' : 'Show Raw';
       saveCards();
       plot();
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
    if(rangeSelect){
      rangeSelect.addEventListener('change', () => {
        const val = rangeSelect.value;
        if(!val) return;
        let startYear;
        if(val === 'ytd'){
          startYear = new Date().getUTCFullYear();
        } else {
          startYear = parseInt(val, 10);
        }
        const from = Date.UTC(startYear, 0, 1) / 1000;
        const to = Math.floor(Date.now() / 1000);
        chart.timeScale().setVisibleRange({ from, to });
      });
    }
    card.querySelector('.remove-card-btn').addEventListener('click',()=>{ wrapper.removeChild(card);
     saveCards(); });

    // Add event listener to save multipliers
    card.querySelectorAll('.multiplier-input').forEach(input => {
      input.addEventListener('input', () => {
        const ticker = input.dataset.ticker;
        const value = parseFloat(input.value);
        multiplierMap.set(ticker, value);
        localStorage.setItem('multipliers', JSON.stringify(Object.fromEntries(multiplierMap)));
      });
    });

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
        if(dl){
          dl.innerHTML='';
          list.forEach(t=>{ const opt=document.createElement('option'); opt.value=t; dl.appendChild(opt);});
          // Add ETF metric series as regular options
          ['ALLW_VALUE','ALLW_SHARES'].forEach(x=>{ const opt=document.createElement('option'); opt.value=x; dl.appendChild(opt); });
        }
      })
      .catch(()=>{});

    // Decide whether to restore previous cards or start blank based on URL param
    const urlParams = new URLSearchParams(window.location.search);
    const startBlank = urlParams.has('blank');

    if(startBlank){
      createChartCard('');
    } else {
      // create first card automatically using any preset tickers in localStorage or default
      const stored = JSON.parse(localStorage.getItem('sandbox_cards')||'[]');
      if(stored.length){
        stored.forEach(c=>createChartCard(c.tickers.join(', '), c.showDiff, c.showAvg, c.showVol, c.useRaw||false, c.multipliers, c.hidden, c.range, c.title||''));
      }else{
        // attempt to restore from backend workspace file
        fetch('http://localhost:5000/api/workspace')
          .then(r=>r.json())
          .then(ws=>{
            if(Array.isArray(ws) && ws.length){
              ws.forEach(c=>createChartCard(c.tickers.join(', '), c.showDiff, c.showAvg, c.showVol, c.useRaw||false, c.multipliers, c.hidden, c.range, c.title||''));
              localStorage.setItem('sandbox_cards', JSON.stringify(ws));
            } else {
              createChartCard('SPY');
            }
          })
          .catch(()=>createChartCard('SPY'));
      }
    }
  });
  window.createChartCard = createChartCard;
})();
