/**
 * Chart Navigation Toggle
 * Handles hiding/showing the chart navigation list
 */

(() => {
  const toggleBtn = document.getElementById('toggle-chart-nav-btn');
  const chartNav = document.getElementById('chart-nav');

  if (!toggleBtn || !chartNav) {
    console.warn('[ChartNavToggle] Required elements not found');
    return;
  }

  // Load saved state from localStorage
  const savedState = localStorage.getItem('chart_nav_visible');
  let isVisible = savedState !== 'false'; // Default to visible

  // Apply initial state
  if (!isVisible) {
    chartNav.classList.add('hidden');
    toggleBtn.textContent = 'Show Chart List';
  }

  // Toggle handler
  toggleBtn.addEventListener('click', () => {
    isVisible = !isVisible;

    if (isVisible) {
      chartNav.classList.remove('hidden');
      toggleBtn.textContent = 'Hide Chart List';
    } else {
      chartNav.classList.add('hidden');
      toggleBtn.textContent = 'Show Chart List';
    }

    // Save state
    localStorage.setItem('chart_nav_visible', isVisible ? 'true' : 'false');
  });

  console.log('[ChartNavToggle] Chart navigation toggle loaded');
})();
