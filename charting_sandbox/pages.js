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
  let pageNames = {};

  // Preload saved names before creating initial tab so Page 1 label is correct
  try {
    const rawInit = localStorage.getItem('sandbox_pages');
    if (rawInit) {
      const parsedInit = JSON.parse(rawInit);
      if (parsedInit && parsedInit.names && typeof parsedInit.names === 'object') {
        pageNames = parsedInit.names;
      }
    }
  } catch (e) { /* noop */ }

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
    
    // Update navigation link highlighting
    updateNavigationHighlighting(pageEl);
    
    // Save active page
    savePages();
  }

  // Update navigation link highlighting for visible charts
  function updateNavigationHighlighting(pageEl) {
    const chartNav = document.getElementById('chart-nav');
    if (!chartNav) return;
    
    // Remove active class from all navigation links
    Array.from(chartNav.children).forEach(link => link.classList.remove('active'));
    
    // Find all charts on the currently active page
    const wrapper = pageEl.querySelector('[id^="charts-wrapper"]');
    const charts = wrapper ? wrapper.querySelectorAll('.chart-card') : [];
    
    // Highlight navigation links for charts on the active page
    charts.forEach(card => {
      const cardId = card.id;
      if (cardId) {
        const navLink = chartNav.querySelector(`a[href="#${cardId}"]`);
        if (navLink) {
          navLink.classList.add('active');
        }
      }
    });
  }

  // create initial tab for page 1
  function createTab(num){
    const tab=document.createElement('div');
    tab.className='tab';
    tab.dataset.page=num;
    const name = pageNames[num] || `Page ${num}`;
    tab.textContent = name;
    tab.title = 'Double-click to rename';
    tab.addEventListener('click', ()=>{
      const target=pagesContainer.querySelector(`[data-page="${num}"]`);
      if(target) {
        switchTo(target);
        savePages();
      }
    });
    tab.addEventListener('dblclick', () => {
      const current = pageNames[num] || `Page ${num}`;
      const newName = prompt('Rename page', current);
      if (newName === null) return; // cancelled
      const trimmed = newName.trim();
      if (!trimmed) return;
      pageNames[num] = trimmed;
      tab.textContent = trimmed;
      savePages();
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
      localStorage.setItem('sandbox_pages', JSON.stringify({ pages, active: getActivePage(), names: pageNames }));
      // Also persist to backend (debounced) so changes sync across browsers
      try {
        const cardsKey = (window.StateManager && window.StateManager.STORAGE_KEYS && window.StateManager.STORAGE_KEYS.CARDS) || 'sandbox_cards';
        const raw = localStorage.getItem(cardsKey) || '[]';
        const cards = JSON.parse(raw);
        if (window.StateManager && typeof window.StateManager.saveToBackendDebounced === 'function') {
          window.StateManager.saveToBackendDebounced(Array.isArray(cards) ? cards : []);
        }
      } catch (e) {
        console.warn('[PageManager] Failed to trigger backend save after pages change', e);
      }
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
  function renamePage(num, newName){
    const trimmed = (newName || '').toString().trim();
    if (!trimmed) return false;
    pageNames[num] = trimmed;
    const tab = Array.from(tabBar.children).find(t => t.dataset.page === String(num));
    if (tab) tab.textContent = trimmed;
    savePages();
    return true;
  }
  window.PageManager = { ensurePage, showPage, renamePage };

  // Restore saved pages (so empty pages persist too)
  try {
    const raw = localStorage.getItem('sandbox_pages');
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed && Array.isArray(parsed.pages)) {
        // Restore names first so any newly created tabs use saved names
        if (parsed.names && typeof parsed.names === 'object') {
          pageNames = parsed.names;
          // Update any existing tabs (e.g., Page 1) to reflect saved name
          Array.from(tabBar.children).forEach(tab => {
            const num = tab.dataset.page;
            tab.textContent = pageNames[num] || `Page ${num}`;
            tab.title = 'Double-click to rename';
          });
        }
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
    showPage: showPage,
    renamePage: renamePage,
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
