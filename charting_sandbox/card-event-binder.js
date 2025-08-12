(function(){
  /**
   * CardEventBinder: handles ticker chip toggle & multiplier input events.
   * Keeps logic separate from the large card.js orchestrator.
   */
  function bindTickerInteractions(selectedTickersDiv, hiddenTickers, multiplierMap, syncHiddenCb, plotFn, saveFn, isRawFn){
    // Toggle chip visibility
    selectedTickersDiv.addEventListener('click', e => {
      const chip = e.target.closest('.chip');
      if (!chip) return;
      const ticker = chip.dataset.ticker;
      if (hiddenTickers.has(ticker)) {
        hiddenTickers.delete(ticker);
        chip.style.opacity = '1';
        chip.style.textDecoration = 'none';
      } else {
        hiddenTickers.add(ticker);
        chip.style.opacity = '0.4';
        chip.style.textDecoration = 'line-through';
      }
      // let the parent card store updated set
      if (typeof syncHiddenCb === 'function') syncHiddenCb();
      if (typeof saveFn === 'function') saveFn();
      if (typeof plotFn === 'function') plotFn();
    });

    // Multiplier input changes
    selectedTickersDiv.addEventListener('input', e => {
      const el = e.target;
      if (!el.classList.contains('multiplier-input')) return;
      const ticker = el.dataset.ticker;
      const value = parseFloat(el.value);
      if (!isNaN(value) && value > 0) {
        multiplierMap.set(ticker, value);
        if (typeof saveFn === 'function') saveFn();
        if (!isRawFn || !isRawFn()) {
          if (typeof plotFn === 'function') plotFn();
        }
      }
    });
  }

  window.CardEventBinder = {
    bindTickerInteractions
  };
})();
