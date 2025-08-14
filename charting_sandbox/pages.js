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
  function switchTo(pageEl){
    // hide all pages then show selected
    Array.from(pagesContainer.children).forEach(p=>p.style.display='none');
    pageEl.style.display='block';
    activateTab(pageEl.dataset.page);
  }


  // create initial tab for page 1
  function createTab(num){
    const tab=document.createElement('div');
    tab.className='tab';
    tab.dataset.page=num;
    tab.textContent=`Page ${num}`;
    tab.addEventListener('click', ()=>{
      const target=pagesContainer.querySelector(`[data-page="${num}"]`);
      if(target) switchTo(target);
    });
    tabBar.appendChild(tab);
    return tab;
  }
  createTab(1);

  // ensure first page visible only
  switchTo(pagesContainer.querySelector('[data-page="1"]'));

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
    } else {
      console.error('pages.js: createChartCard is not available yet.');
    }
  });
})();
