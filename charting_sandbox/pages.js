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
  let pageNames = {};  // page number -> name mapping
  let hasRestored = false; // delay saving until after restore
  let saveDebounceTimer = null;
  function debounceSave(){
    if (saveDebounceTimer) clearTimeout(saveDebounceTimer);
    saveDebounceTimer = setTimeout(() => { try { savePages(); } catch(_){} }, 300);
  }

  function removePage(num){
    if (num === 1) {
      console.warn('pages.js: Page 1 cannot be removed');
      return;
    }
    const pageEl = pagesContainer.querySelector(`[data-page="${num}"]`);
    const tabEl = tabBar.querySelector(`.tab[data-page="${num}"]`);
    if (!pageEl && !tabEl) return;

    // Remove any chart nav links for cards on this page
    try {
      if (pageEl) {
        const cards = pageEl.querySelectorAll('.chart-card');
        cards.forEach(card => {
          const navLink = card && card._navLink;
          if (navLink && navLink.parentElement) {
            navLink.parentElement.removeChild(navLink);
          }
        });
      }
    } catch (e) { console.warn('pages.js: failed cleaning nav links for page', num, e); }

    const wasActive = (tabBar.querySelector('.tab.active')?.dataset?.page === String(num));

    if (pageEl) pageEl.remove();
    if (tabEl) tabEl.remove();
    try { delete pageNames[num]; } catch(_) {}

    // Determine next page to activate if needed
    const remaining = Array.from(pagesContainer.children)
      .map(p => parseInt(p.dataset.page, 10))
      .sort((a,b)=>a-b);
    if (wasActive && remaining.length) {
      const next = remaining.find(n => n > num) || remaining[remaining.length - 1];
      const nextEl = pagesContainer.querySelector(`[data-page="${next}"]`);
      if (nextEl) switchTo(nextEl);
    }

    if (window.saveCards) window.saveCards();
    savePages();
  }

  function activateTab(pageNum){
    Array.from(tabBar.children).forEach(t=>t.classList.toggle('active', t.dataset.page==pageNum+''));
  }

  function renamePage(num, newName){
    const name = (newName || '').trim() || `Page ${num}`;
    pageNames[num] = name;
    const tab = tabBar.querySelector(`.tab[data-page="${num}"]`);
    if (tab) {
      const labelEl = tab.querySelector('.tab-label');
      if (labelEl) labelEl.textContent = name;
      tab.title = name;
    }
    savePages();
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
    
    // Save active page (only after initial restore to avoid clobbering)
    if (hasRestored) savePages();
  }

  // create initial tab for page 1
  function createTab(num){
    const tab=document.createElement('div');
    tab.className='tab';
    tab.dataset.page=num;
    const label = document.createElement('span');
    label.className = 'tab-label';
    label.textContent = pageNames[num] || `Page ${num}`;
    label.title = 'Double-click to rename';
    label.addEventListener('dblclick', (e) => {
      e.stopPropagation();
      label.contentEditable = 'true';
      label.focus();
      // select all text (fallback safe)
      try {
        const range = document.createRange();
        range.selectNodeContents(label);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
      } catch(_) {}
    });
    label.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') { e.preventDefault(); label.blur(); }
      if (e.key === 'Escape') { e.preventDefault(); label.textContent = pageNames[num] || `Page ${num}`; label.blur(); }
      e.stopPropagation();
    });
    // Update live as user types so persistence works even without blur
    label.addEventListener('input', () => {
      pageNames[num] = label.textContent.trim();
      debounceSave();
    });
    label.addEventListener('blur', () => {
      label.contentEditable = 'false';
      renamePage(num, label.textContent);
    });
    tab.appendChild(label);
    const closer = document.createElement('span');
    closer.className = 'tab-close';
    closer.textContent = '×';
    closer.style.cssText = 'margin-left:6px;cursor:pointer;font-weight:bold;';
    closer.addEventListener('click', (e) => {
      e.stopPropagation();
      removePage(num);
    });
    tab.appendChild(closer);
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
    const active = getActivePage();
    const names = {};
    // Harvest names from DOM to catch un-blurred edits
    pages.forEach(n => {
      const labelEl = tabBar.querySelector(`.tab[data-page="${n}"] .tab-label`);
      const text = labelEl ? labelEl.textContent.trim() : (pageNames[n] || `Page ${n}`);
      names[n] = text || `Page ${n}`;
      pageNames[n] = names[n];
    });
    try {
      localStorage.setItem('sandbox_pages', JSON.stringify({ pages, active, names }));
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

  // Restore saved pages (so empty pages persist too) and names
  try {
    const raw = localStorage.getItem('sandbox_pages');
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed && Array.isArray(parsed.pages)) {
        if (parsed.names && typeof parsed.names === 'object') {
          pageNames = parsed.names;
        } else {
          // initialize default names
          parsed.pages.forEach(n => { pageNames[n] = `Page ${n}`; });
        }
        parsed.pages.filter(n => n !== 1).forEach(n => ensurePage(n));
        // Update tab labels to saved names
        Object.entries(pageNames).forEach(([num, name]) => {
          const tab = tabBar.querySelector(`.tab[data-page="${num}"]`);
          if (tab) {
            const lbl = tab.querySelector('.tab-label');
            if (lbl) lbl.textContent = name;
            tab.title = name;
          }
        });
        if (parsed.active && parsed.active !== 1) {
          const target = pagesContainer.querySelector(`[data-page="${parsed.active}"]`);
          if (target) switchTo(target);
        }
      }
    }
    // Mark restore complete and persist final state now
    hasRestored = true;
    savePages();
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
    // default page name
    pageNames[pageCounter] = `Page ${pageCounter}`;
    createTab(pageCounter);
    switchTo(pageEl);

    // create a blank chart card inside this wrapper
    if (typeof createChartCard === 'function') {
      createChartCard('', false, false, true, false, {}, [], null, '', false, null, wrapper);
      if(window.saveCards) window.saveCards();
      savePages();
    } else {
      console.error('pages.js: createChartCard is not available yet.');
    }
  });
  // Expose PageManager functions to window for cross-module access
  window.PageManager = {
    getActivePage: getActivePage,
    renamePage: renamePage,
    removePage: removePage,
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
