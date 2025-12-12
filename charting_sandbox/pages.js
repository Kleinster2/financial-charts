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
  let pageCategories = {}; // { categoryName: [pageNum, ...] }
  let currentActivePage = 1; // Track active page directly
  let isInitializing = true; // Prevent saves during initial load
  let highlightsMode = false;
    window.highlightsMode = false; // Show only starred charts

  // Toggle highlights mode - show only starred charts across ALL pages
  function toggleHighlightsMode() {
    highlightsMode = !highlightsMode;
    window.highlightsMode = highlightsMode;
    const btn = document.querySelector('.highlights-toggle-btn');
    if (btn) {
      btn.textContent = highlightsMode ? String.fromCharCode(9733) + ' Highlights ON' : String.fromCharCode(9734) + ' Highlights';
      btn.style.background = highlightsMode ? '#f5a623' : '';
      btn.style.color = highlightsMode ? '#fff' : '';
    }

    // Update page title
    const pageTitle = document.getElementById('page-title');
    if (pageTitle) {
      if (highlightsMode) {
        pageTitle.dataset.originalTitle = pageTitle.textContent;
        pageTitle.textContent = '★ All Starred Charts';
        pageTitle.style.color = '#f5a623';
      } else {
        pageTitle.textContent = pageTitle.dataset.originalTitle || pageNames[currentActivePage] || `Page ${currentActivePage}`;
        pageTitle.style.color = '';
      }
    }

    applyHighlightsFilter();

    // Save highlights mode state
    savePages();
  }

  // Apply highlights filter - show starred charts from ALL pages, hide others
  function applyHighlightsFilter() {
    const allPages = pagesContainer.querySelectorAll('.page');

    if (highlightsMode) {
      // HIGHLIGHTS MODE: Show all pages, but only starred charts
      let starredCount = 0;

      allPages.forEach(page => {
        // Show the page container
        page.style.display = 'block';

        // Filter cards within this page
        const cards = page.querySelectorAll('.chart-card');
        cards.forEach(card => {
          if (card._starred) {
            card.style.display = '';
            starredCount++;

            // Auto-plot if not yet rendered
            const chartBox = card.querySelector('.chart-box');
            const hasCanvas = chartBox && chartBox.querySelector('canvas');
            const hasTickers = card._selectedTickers && card._selectedTickers.size > 0;
            if (hasTickers && chartBox && !hasCanvas) {
              const plotBtn = card.querySelector('.plot-btn');
              if (plotBtn) {
                setTimeout(() => plotBtn.click(), 100);
              }
            }
          } else {
            card.style.display = 'none';
          }
        });
      });

      console.log(`[Highlights] Showing ${starredCount} starred charts across all pages`);

      // Update chart navigation to show all starred charts
      updateHighlightsNavigation();

    } else {
      // NORMAL MODE: Show only active page with all its cards
      allPages.forEach(page => {
        const pageNum = parseInt(page.dataset.page, 10);
        if (pageNum === currentActivePage) {
          page.style.display = 'block';
          // Show all cards on active page
          page.querySelectorAll('.chart-card').forEach(card => {
            card.style.display = '';
          });
        } else {
          page.style.display = 'none';
        }
      });

      // Restore normal navigation
      const pageEl = pagesContainer.querySelector(`[data-page="${currentActivePage}"]`);
      if (pageEl) {
        updateNavigationHighlighting(pageEl);
      }
    }
  }

  // Update navigation to show all starred charts across pages
  function updateHighlightsNavigation() {
    const chartNav = document.getElementById('chart-nav');
    if (!chartNav) return;

    // Show all links for starred charts, hide others
    Array.from(chartNav.children).forEach(link => {
      link.classList.remove('active');
      const cardId = link.getAttribute('href')?.replace('#', '');
      if (cardId) {
        const card = document.getElementById(cardId);
        if (card && card._starred) {
          link.style.display = '';
          link.classList.add('active');
        } else {
          link.style.display = 'none';
        }
      }
    });
  }

  window.toggleHighlightsMode = toggleHighlightsMode;
  window.applyHighlightsFilter = applyHighlightsFilter;

  // Preload saved names before creating initial tab so Page 1 label is correct
  try {
    const rawInit = localStorage.getItem('sandbox_pages');
    if (rawInit) {
      const parsedInit = JSON.parse(rawInit);
      if (parsedInit && parsedInit.names && typeof parsedInit.names === 'object') {
        pageNames = parsedInit.names;
      }
      if (parsedInit && parsedInit.categories && typeof parsedInit.categories === 'object') {
        pageCategories = parsedInit.categories;
      }
    }
  } catch (e) { /* noop */ }

  // Clean up deleted pages from localStorage (one-time cleanup)
  const deletedPages = [10, 16, 18, 23, 24, 26];
  deletedPages.forEach(pageNum => {
    delete pageNames[pageNum];
    // Remove from all categories
    Object.keys(pageCategories).forEach(cat => {
      if (Array.isArray(pageCategories[cat])) {
        pageCategories[cat] = pageCategories[cat].filter(p => p !== pageNum);
      }
    });
  });
  // Save cleaned data back to localStorage
  try {
    const existingRaw = localStorage.getItem('sandbox_pages');
    if (existingRaw) {
      const existing = JSON.parse(existingRaw);
      if (existing.pages) {
        existing.pages = existing.pages.filter(p => !deletedPages.includes(p));
      }
      existing.names = pageNames;
      existing.categories = pageCategories;
      localStorage.setItem('sandbox_pages', JSON.stringify(existing));
    }
  } catch (e) { /* noop */ }

  function activateTab(pageNum){
    // Update dropdown button active states
    tabBar.querySelectorAll('.category-dropdown').forEach(dropdown => {
      const hasActivePage = dropdown.querySelector(`.dropdown-item[data-page="${pageNum}"]`);
      dropdown.querySelector('.category-btn').classList.toggle('active', !!hasActivePage);
    });
    // Update individual tab active states (for uncategorized)
    tabBar.querySelectorAll('.tab').forEach(t => {
      t.classList.toggle('active', t.dataset.page == pageNum + '');
    });
  }

  // Create category dropdown
  function createCategoryDropdown(categoryName, pageNums) {
    const dropdown = document.createElement('div');
    dropdown.className = 'category-dropdown';
    dropdown.style.cssText = 'position: relative; display: inline-block;';

    const btn = document.createElement('button');
    btn.className = 'category-btn';
    btn.textContent = categoryName + ' ▼';
    btn.style.cssText = 'padding: 4px 10px; font-size: 0.9rem; cursor: pointer; border: 1px solid #666; border-radius: 4px; background: #eee;';

    const menu = document.createElement('div');
    menu.className = 'dropdown-menu';
    menu.style.cssText = 'display: none; position: absolute; top: 100%; left: 0; background: #ffffff; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); z-index: 1000; min-width: 180px; max-height: 400px; overflow-y: auto;';

    // Sort pages alphabetically by name
    const sortedPages = pageNums
      .map(num => ({ num, name: pageNames[num] || `Page ${num}` }))
      .sort((a, b) => a.name.localeCompare(b.name));

    sortedPages.forEach(({ num, name }) => {
      const item = document.createElement('div');
      item.className = 'dropdown-item';
      item.dataset.page = num;
      item.textContent = name;
      item.style.cssText = 'padding: 8px 12px; cursor: pointer; white-space: nowrap; background: #ffffff;';
      item.addEventListener('mouseenter', () => item.style.background = '#e8e8e8');
      item.addEventListener('mouseleave', () => item.style.background = '#ffffff');
      item.addEventListener('click', (e) => {
        e.stopPropagation();
        const target = pagesContainer.querySelector(`[data-page="${num}"]`);
        if (target) {
          switchTo(target);
          savePages();
        }
        menu.style.display = 'none';
      });
      menu.appendChild(item);
    });

    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      // Close other dropdowns
      tabBar.querySelectorAll('.dropdown-menu').forEach(m => {
        if (m !== menu) m.style.display = 'none';
      });
      menu.style.display = menu.style.display === 'none' ? 'block' : 'none';
    });

    dropdown.appendChild(btn);
    dropdown.appendChild(menu);
    return dropdown;
  }

  // Close dropdowns when clicking outside
  document.addEventListener('click', () => {
    tabBar.querySelectorAll('.dropdown-menu').forEach(m => m.style.display = 'none');
  });

  // Build the tab bar with category dropdowns
  function buildTabBar() {
    tabBar.innerHTML = '';

    // If we have categories, use dropdown mode
    if (Object.keys(pageCategories).length > 0) {
      const knownCategories = ['Portfolios', 'Sectors', 'Countries', 'Macro', 'Assets'];
      // Include any additional categories from pageCategories
      const categoryOrder = [...new Set([...knownCategories, ...Object.keys(pageCategories)])];
      const categorizedPages = new Set();

      categoryOrder.forEach(cat => {
        if (pageCategories[cat] && pageCategories[cat].length > 0) {
          const dropdown = createCategoryDropdown(cat, pageCategories[cat]);
          tabBar.appendChild(dropdown);
          pageCategories[cat].forEach(p => categorizedPages.add(p));
        }
      });

      // Add any uncategorized pages as individual tabs
      const allPages = Array.from(pagesContainer.children).map(p => parseInt(p.dataset.page, 10)).filter(p => !isNaN(p));
      const uncategorized = allPages.filter(p => !categorizedPages.has(p));
      uncategorized.forEach(num => {
        const tab = createTab(num);
        tabBar.appendChild(tab);
      });
    } else {
      // Fallback: show all pages as individual tabs
      const allPages = Array.from(pagesContainer.children).map(p => parseInt(p.dataset.page, 10)).filter(p => !isNaN(p));
      allPages.sort((a, b) => a - b).forEach(num => {
        const tab = createTab(num);
        tabBar.appendChild(tab);
      });
    }
  }
  function switchTo(pageEl) {
    if (!pageEl) return;

    // Exit highlights mode when switching pages
    if (highlightsMode) {
      highlightsMode = false;
      window.highlightsMode = false;
      const btn = document.querySelector('.highlights-toggle-btn');
      if (btn) {
        btn.textContent = String.fromCharCode(9734) + ' Highlights';
        btn.style.background = '';
        btn.style.color = '';
      }
      const pageTitle = document.getElementById('page-title');
      if (pageTitle) {
        pageTitle.style.color = '';
      }
    }

    // Hide all pages
    Array.from(pagesContainer.children).forEach(p => {
      p.style.display = 'none';
    });

    // Show the target page
    pageEl.style.display = 'block';

    // Track the active page
    const pageNum = parseInt(pageEl.dataset.page, 10);
    currentActivePage = pageNum;

    // Update page title
    const pageTitle = document.getElementById("page-title");
    if (pageTitle) {
      pageTitle.textContent = pageNames[pageNum] || `Page ${pageNum}`;
    }
    activateTab(pageNum);
    
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

    const currentPageNum = pageEl.dataset.page;

    // Show/hide navigation links based on current page
    Array.from(chartNav.children).forEach(link => {
      link.classList.remove('active');

      // Hide links not on current page, show links on current page
      if (link.dataset.page === currentPageNum) {
        link.style.display = '';
      } else {
        link.style.display = 'none';
      }
    });

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

  // create individual tab (for uncategorized pages)
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
    return tab;
  }

  // Load categories from backend workspace.json
  async function loadCategoriesFromBackend() {
    try {
      const resp = await fetch('/api/workspace');
      if (resp.ok) {
        const data = await resp.json();
        if (data.pages && data.pages.names) {
          // Merge backend names with local (backend takes precedence)
          Object.assign(pageNames, data.pages.names);
        }
        if (data.pages && data.pages.categories) {
          pageCategories = data.pages.categories;
        }
      }
    } catch (e) {
      console.warn('[PageManager] Failed to load categories from backend', e);
    }
  }

  // Initialize: load from backend then build UI
  async function initialize() {
    await loadCategoriesFromBackend();

    // Restore saved pages from localStorage FIRST (so page elements exist)
    let savedActivePage = 1;
    let savedHighlightsMode = false;
    try {
      const raw = localStorage.getItem('sandbox_pages');
      if (raw) {
        const parsed = JSON.parse(raw);
        if (parsed && parsed.active) {
          savedActivePage = parsed.active;
        }
        if (parsed && parsed.highlightsMode) {
          savedHighlightsMode = true;
        }
        // Restore names so tabs get correct labels
        if (parsed.names && typeof parsed.names === 'object') {
          Object.assign(pageNames, parsed.names);
        }
        // Restore categories if backend didn't provide any
        if (parsed.categories && typeof parsed.categories === 'object') {
          if (Object.keys(pageCategories).length === 0) {
            pageCategories = parsed.categories;
          }
        }
        // Create page elements for all saved pages
        if (Array.isArray(parsed.pages)) {
          parsed.pages.filter(n => n !== 1).forEach(n => ensurePage(n));
        }
      }
    } catch (e) { /* use default */ }

    buildTabBar();

    // Switch to saved active page (or page 1 if not found)
    const targetPage = pagesContainer.querySelector(`[data-page="${savedActivePage}"]`)
                    || pagesContainer.querySelector('[data-page="1"]');
    if (targetPage) {
      switchTo(targetPage);
    }

    // Restore highlights mode if it was active (after a short delay to let cards load)
    if (savedHighlightsMode) {
      setTimeout(() => {
        console.log('[PageManager] Restoring highlights mode from saved state');
        toggleHighlightsMode();
      }, 500);
    }
  }

  initialize();

  function getActivePage(){
    return currentActivePage;
  }

  function savePages(){
    // Don't save during initialization to avoid overwriting saved active page
    if (isInitializing) {
      console.log('[PageManager] savePages() skipped - still initializing');
      return;
    }
    const pages = Array.from(pagesContainer.children).map(p => parseInt(p.dataset.page, 10)).filter(p => !isNaN(p));
    const activePage = getActivePage();
    console.log(`[PageManager] savePages() - active page: ${activePage}, highlightsMode: ${highlightsMode}`);
    try {
      localStorage.setItem('sandbox_pages', JSON.stringify({ pages, active: activePage, names: pageNames, categories: pageCategories, highlightsMode: highlightsMode }));
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
    // Skip if already on this page to avoid race conditions
    if (currentActivePage === num) {
      console.log(`[PageManager] showPage(${num}) skipped - already on this page`);
      return;
    }
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

        // add tab and switch focus - rebuild tab bar to include new page
    buildTabBar();
    switchTo(pageEl);

    // create a blank chart card inside this wrapper
    if (typeof window.createChartCard === 'function') {
      // Create an empty chart with default ticker (SPY)
      window.createChartCard({
        tickers: 'SPY',
        wrapperEl: wrapper,
        title: ''
      });
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
    },
    // Called by StateManager after workspace is fully loaded
    finishInitialization: function() {
      isInitializing = false;
      console.log('[PageManager] Initialization complete, saves now enabled');
    },
    // Refresh navigation filtering for current page (call after cards are loaded)
    refreshNavigation: function() {
      const pageEl = pagesContainer.querySelector(`[data-page="${currentActivePage}"]`);
      if (pageEl) {
        updateNavigationHighlighting(pageEl);
      }
    }
  };

  // Signal readiness for listeners that depend on PageManager
  try { document.dispatchEvent(new Event('PageManagerReady')); } catch(e) {}
})();
