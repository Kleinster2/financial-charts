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
    STORAGE_KEYS: {
        CARDS: 'sandbox_cards',
        MULTIPLIERS: 'multipliers',
        PREFERENCES: 'chart_preferences'
    },
    
    // internal timer for backend saves
    _saveTimeout: null,
    
    /**
     * Save cards to localStorage and backend
     */
    async saveCards(cards) {
        // Save to localStorage immediately
        try {
            localStorage.setItem(this.STORAGE_KEYS.CARDS, JSON.stringify(cards));
        } catch (e) {
            console.error('[StateManager] Failed to write localStorage', e);
        }

        // Debounce saving to backend
        clearTimeout(this._saveTimeout);
        this._saveTimeout = setTimeout(() => {
            try {
                console.log('[StateManager] Auto-saving to backend...');
                this.saveToBackend(cards);
            } catch (e) {
                console.error('[StateManager] Backend save scheduling failed', e);
            }
        }, 2000);
    },
    
    /**
     * Save charts to backend workspace
     */
    async saveToBackend(cards) {
        try {
            const response = await fetch('http://localhost:5000/api/workspace', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(cards)
            });
            
            if (response.ok) {
                console.log('[StateManager] ✓ Charts auto-saved to backend');
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
            // Try localStorage first
            const localData = localStorage.getItem(this.STORAGE_KEYS.CARDS);
            if (localData) {
                return JSON.parse(localData);
            }
            
            // Try backend if no local data
            if (window.DataFetcher) {
                const remoteData = await window.DataFetcher.loadWorkspace();
                if (remoteData) {
                    // Cache locally
                    localStorage.setItem(this.STORAGE_KEYS.CARDS, JSON.stringify(remoteData));
                    return remoteData;
                }
            }
            
            return [];
        } catch (error) {
            console.error('Failed to load cards:', error);
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
