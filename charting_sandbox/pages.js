// Page manager for sandbox: supports creating new pages each with its own charts wrapper.
(() => {
  const pagesContainer = document.getElementById('pages-container');
  const tabBar = document.getElementById('tab-bar');
  const newPageBtn = document.getElementById('new-page-btn');
  if (!pagesContainer || !newPageBtn) {
    console.error('pages.js: required DOM elements not found');
    return;
  }

  let pageCounter = 1; // page 1 exists

  function activateTab(pageNum){
    Array.from(tabBar.children).forEach(t=>t.classList.toggle('active', t.dataset.page==pageNum+''));
  }
  function switchTo(pageEl) {
    if (!pageEl) return;
    
    // Hide all pages
    Array.from(pagesContainer.children).forEach(p => {
      p.style.display = 'none';
    });
    
    // Show the target page
    pageEl.style.display = 'block';
    activateTab(pageEl.dataset.page);
    
    // Trigger plot for all charts on the newly visible page if they haven't been plotted
    // Use a small delay to ensure cards are fully initialized
    setTimeout(() => {
      // Charts are inside the wrapper div, not directly under the page
      const wrapper = pageEl.querySelector('[id^="charts-wrapper"]');
      const charts = wrapper ? wrapper.querySelectorAll('.chart-card') : [];
      console.log(`[PageManager] Switching to page ${pageEl.dataset.page}, found ${charts.length} charts`);
      
      charts.forEach((card, idx) => {
        const hasTickers = card._selectedTickers && card._selectedTickers.size > 0;
        const chartBox = card.querySelector('.chart-box');
        const hasCanvas = chartBox && chartBox.querySelector('canvas');
        
        console.log(`[PageManager] Chart ${idx + 1} on page ${pageEl.dataset.page}: hasTickers=${hasTickers}, hasCanvas=${hasCanvas}`);
        
        // Check if card has tickers but no chart (not plotted yet)
        if (hasTickers && chartBox && !hasCanvas) {
          // Chart hasn't been rendered yet, trigger plot
          const plotBtn = card.querySelector('.plot-btn');
          if (plotBtn) {
            console.log(`[PageManager] Auto-plotting uninitialized chart ${idx + 1} on page ${pageEl.dataset.page}`);
            plotBtn.click();
          } else {
            console.error(`[PageManager] Plot button not found for chart ${idx + 1} on page ${pageEl.dataset.page}`);
          }
        }
      });
    }, 100); // Small delay to ensure cards are initialized
    
    // Save active page
    savePages();
  }

  // create initial tab for page 1
  function createTab(num){
    const tab=document.createElement('div');
    tab.className='tab';
    tab.dataset.page=num;
    tab.textContent=`Page ${num}`;
    tab.addEventListener('click', ()=>{
      const target=pagesContainer.querySelector(`[data-page="${num}"]`);
      if(target) {
        switchTo(target);
        savePages();
      }
    });
    tabBar.appendChild(tab);
    return tab;
  }
  createTab(1);

  // ensure first page visible only
  switchTo(pagesContainer.querySelector('[data-page="1"]'));

  function getActivePage(){
    const activeTab = tabBar.querySelector('.tab.active');
    return activeTab ? parseInt(activeTab.dataset.page, 10) : 1;
  }

  function savePages(){
    const pages = Array.from(pagesContainer.children).map(p => parseInt(p.dataset.page, 10));
    try {
      localStorage.setItem('sandbox_pages', JSON.stringify({ pages, active: getActivePage() }));
    } catch(e) { console.warn('pages.js: failed to save pages', e); }
  }

  function ensurePage(num){
    let pageEl = pagesContainer.querySelector(`[data-page="${num}"]`);
    if(!pageEl){
      pageCounter = Math.max(pageCounter, num);
      // create page and wrapper
      pageEl = document.createElement('div');
      pageEl.className='page';
      pageEl.dataset.page=num;
      const wrapper=document.createElement('div');
      wrapper.id = num === 1 ? 'charts-wrapper' : `charts-wrapper-${num}`;
      pageEl.appendChild(wrapper);
      pagesContainer.appendChild(pageEl);
      createTab(num);
      savePages();
    }
    return pageEl.querySelector('[id^="charts-wrapper"]');
  }
  function showPage(num){
    const el = pagesContainer.querySelector(`[data-page="${num}"]`);
    if (el) switchTo(el);
  }
  window.PageManager = { ensurePage, showPage };

  // Restore saved pages (so empty pages persist too)
  try {
    const raw = localStorage.getItem('sandbox_pages');
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed && Array.isArray(parsed.pages)) {
        parsed.pages.filter(n => n !== 1).forEach(n => ensurePage(n));
        if (parsed.active && parsed.active !== 1) {
          const target = pagesContainer.querySelector(`[data-page="${parsed.active}"]`);
          if (target) switchTo(target);
        }
      }
    }
  } catch(e) { console.warn('pages.js: failed to restore pages', e); }

  window.addEventListener('beforeunload', () => {
    if(window.saveCards) window.saveCards();
    savePages();
  });

  newPageBtn.addEventListener('click', () => {
    pageCounter += 1;
    // create page container
    const pageEl = document.createElement('div');
    pageEl.className = 'page';
    pageEl.dataset.page = pageCounter;

    const wrapper = document.createElement('div');
    wrapper.id = `charts-wrapper-${pageCounter}`;
    pageEl.appendChild(wrapper);
    pagesContainer.appendChild(pageEl);

        // add tab and switch focus
    createTab(pageCounter);
    switchTo(pageEl);

    // create a blank chart card inside this wrapper
    if (typeof createChartCard === 'function') {
      createChartCard('', false, false, true, false, {}, [], null, '', true, wrapper);
      if(window.saveCards) window.saveCards();
      savePages();
    } else {
      console.error('pages.js: createChartCard is not available yet.');
    }
  });
  // Expose PageManager functions to window for cross-module access
  window.PageManager = {
    getActivePage: getActivePage,
    ensurePage: function(pageNum) {
      ensurePage(pageNum);
      // Return the wrapper element for the page
      const pageEl = pagesContainer.querySelector(`[data-page="${pageNum}"]`);
      if (pageEl) {
        return pageEl.querySelector('[id^="charts-wrapper"]');
      }
      return document.getElementById('charts-wrapper');
    }
  };

  // Signal readiness for listeners that depend on PageManager
  try { document.dispatchEvent(new Event('PageManagerReady')); } catch(e) {}
})();
