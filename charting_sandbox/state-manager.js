/**
 * state-manager.js - State persistence and management module
 * Handles localStorage, workspace sync, and card state
 */

// Debounce utility
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Export the StateManager
window.StateManager = {
    // Constants
    STORAGE_KEYS: window.ChartConfig ? window.ChartConfig.STORAGE_KEYS : {
        CARDS: 'sandbox_cards',
        MULTIPLIERS: 'multipliers',
        PREFERENCES: 'chart_preferences'
    },
    
    // internal timer for backend saves
    _saveTimeout: null,
    
    /**
     * Save cards to localStorage only (immediate)
     */
    saveCardsLocal(cards) {
        try {
            localStorage.setItem(this.STORAGE_KEYS.CARDS, JSON.stringify(cards));
        } catch (e) {
            console.error('[StateManager] Failed to write localStorage', e);
        }
    },
    
    /**
     * Debounced backend save
     */
    saveToBackendDebounced: debounce(cards => StateManager.saveToBackend(cards), window.ChartConfig ? window.ChartConfig.DEBOUNCE_MS.SAVE : 2000),
    
    async saveToBackend(cards) {
        try {
            // Read page metadata (names, active, pages) from localStorage to persist cross-browser
            let pagesMeta = null;
            try {
                const raw = localStorage.getItem('sandbox_pages');
                if (raw) {
                    const parsed = JSON.parse(raw);
                    if (parsed && typeof parsed === 'object') pagesMeta = parsed;
                }
            } catch (e) {
                console.warn('[StateManager] Could not read sandbox_pages for workspace save:', e);
            }

            const payload = { cards, pages: pagesMeta };

            const response = await fetch('http://localhost:5000/api/workspace', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            
            if (response.ok) {
                const info = await response.json().catch(() => ({}));
                const cardCount = Array.isArray(cards) ? cards.length : 0;
                const nameCount = pagesMeta && pagesMeta.names ? Object.keys(pagesMeta.names).length : 0;
                console.log(`[StateManager] ✓ Workspace saved to backend (cards=${cardCount}, pageNames=${nameCount})`, info);
                // Show subtle notification (optional)
                this.showSaveNotification('Saved to server');
            } else {
                console.error('[StateManager] Failed to save to backend:', response.status);
            }
        } catch (error) {
            console.error('[StateManager] Backend save error:', error);
            // Silently fail - don't interrupt user experience
        }
    },

    /**
     * Public save: local immediately, backend debounced
     */
    saveCards(cards) {
        this.saveCardsLocal(cards);
        this.saveToBackendDebounced(cards);
    },
    
    /**
     * Show a subtle save notification
     */
    showSaveNotification(message) {
        // Check if notification already exists
        let notification = document.getElementById('save-notification');
        
        if (!notification) {
            // Create notification element
            notification = document.createElement('div');
            notification.id = 'save-notification';
            notification.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 20px;
                background: #28a745;
                color: white;
                padding: 10px 15px;
                border-radius: 4px;
                font-size: 14px;
                z-index: 10000;
                opacity: 0;
                transition: opacity 0.3s;
                pointer-events: none;
            `;
            document.body.appendChild(notification);
        }
        
        // Update message and show
        notification.textContent = message;
        notification.style.opacity = '1';
        
        // Hide after 2 seconds
        clearTimeout(this._notificationTimeout);
        this._notificationTimeout = setTimeout(() => {
            notification.style.opacity = '0';
        }, 2000);
    },
    
    /**
     * Load cards from localStorage or backend
     */
    async loadCards() {
        try {
            // Backend-first restore for cross-browser persistence
            if (window.DataFetcher) {
                const remoteData = await window.DataFetcher.loadWorkspace();
                if (remoteData) {
                    // Two schema possibilities: legacy array or new object {cards, pages}
                    if (Array.isArray(remoteData)) {
                        if (remoteData.length > 0) {
                            localStorage.setItem(this.STORAGE_KEYS.CARDS, JSON.stringify(remoteData));
                            console.log('[StateManager] Loaded legacy workspace (array) from backend');
                            return remoteData;
                        }
                    } else if (typeof remoteData === 'object') {
                        const cards = Array.isArray(remoteData.cards) ? remoteData.cards : [];
                        // Restore pages metadata for PageManager
                        if (remoteData.pages && typeof remoteData.pages === 'object') {
                            try {
                                localStorage.setItem('sandbox_pages', JSON.stringify(remoteData.pages));
                                const nameCount = remoteData.pages.names ? Object.keys(remoteData.pages.names).length : 0;
                                console.log(`[StateManager] Restored page metadata from backend (pageNames=${nameCount})`);
                            } catch (e) {
                                console.warn('[StateManager] Failed to cache sandbox_pages from backend:', e);
                            }
                        }
                        localStorage.setItem(this.STORAGE_KEYS.CARDS, JSON.stringify(cards));
                        console.log('[StateManager] Loaded workspace (object) from backend, cards=', cards.length);
                        if (cards.length > 0) return cards;
                    }
                }
            }

            // Fallback: localStorage
            const localData = localStorage.getItem(this.STORAGE_KEYS.CARDS);
            if (localData) {
                const parsed = JSON.parse(localData);
                console.log('[StateManager] Loaded workspace from localStorage (fallback)');

                // Show info toast that backend failed but localStorage worked
                if (window.Toast && remoteData === null) {
                    window.Toast.info('Loaded workspace from local storage (server unavailable)', 3000);
                }

                return parsed;
            }

            // Both backend and localStorage failed - show warning
            if (window.Toast) {
                window.Toast.warning('Could not load saved workspace. Starting with empty workspace.');
            }

            return [];
        } catch (error) {
            console.error('Failed to load cards:', error);

            // Show error toast for unexpected failures
            if (window.Toast) {
                window.Toast.error('Error loading workspace. Please refresh the page.');
            }

            return [];
        }
    },
    
    /**
     * Save multipliers configuration
     */
    saveMultipliers(multipliers) {
        try {
            const data = multipliers instanceof Map 
                ? Object.fromEntries(multipliers) 
                : multipliers;
            localStorage.setItem(this.STORAGE_KEYS.MULTIPLIERS, JSON.stringify(data));
        } catch (error) {
            console.error('Failed to save multipliers:', error);
        }
    },
    
    /**
     * Load multipliers configuration
     */
    loadMultipliers() {
        try {
            const data = localStorage.getItem(this.STORAGE_KEYS.MULTIPLIERS);
            if (data) {
                const obj = JSON.parse(data);
                return new Map(Object.entries(obj));
            }
        } catch (error) {
            console.error('Failed to load multipliers:', error);
        }
        return new Map();
    },
    
    /**
     * Save chart preferences
     */
    savePreferences(prefs) {
        try {
            localStorage.setItem(this.STORAGE_KEYS.PREFERENCES, JSON.stringify(prefs));
        } catch (error) {
            console.error('Failed to save preferences:', error);
        }
    },
    
    /**
     * Load chart preferences
     */
    loadPreferences() {
        try {
            const data = localStorage.getItem(this.STORAGE_KEYS.PREFERENCES);
            if (data) {
                return JSON.parse(data);
            }
        } catch (error) {
            console.error('Failed to load preferences:', error);
        }
        return {
            defaultShowDiff: false,
            defaultShowAvg: false,
            defaultShowVol: true,
            defaultUseRaw: false
        };
    },
    
    /**
     * Clear all saved state
     */
    clearAll() {
        try {
            Object.values(this.STORAGE_KEYS).forEach(key => {
                localStorage.removeItem(key);
            });
            console.log('Cleared all saved state');
        } catch (error) {
            console.error('Failed to clear state:', error);
        }
    },
    
    /**
     * Export current state as JSON
     */
    exportState() {
        const state = {
            cards: this.loadCards(),
            multipliers: Object.fromEntries(this.loadMultipliers()),
            preferences: this.loadPreferences(),
            timestamp: new Date().toISOString()
        };
        return JSON.stringify(state, null, 2);
    },
    
    /**
     * Import state from JSON
     */
    importState(jsonString) {
        try {
            const state = JSON.parse(jsonString);
            
            if (state.cards) {
                this.saveCards(state.cards);
            }
            if (state.multipliers) {
                this.saveMultipliers(state.multipliers);
            }
            if (state.preferences) {
                this.savePreferences(state.preferences);
            }
            
            console.log('State imported successfully');
            return true;
        } catch (error) {
            console.error('Failed to import state:', error);
            return false;
        }
    }
};

// No-op footer: StateManager is already exposed as window.StateManager above.
