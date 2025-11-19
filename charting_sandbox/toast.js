/**
 * toast.js - Lightweight toast notification system
 * Provides user-visible error/warning/info messages
 */

(function() {
    // Toast container
    let container = null;

    // Recent toasts to prevent duplicates
    const recentToasts = new Map();
    const DUPLICATE_WINDOW = 10000; // 10 seconds

    // Toast types with styling
    const TYPES = {
        error: { icon: '✗', color: '#ef4444', bg: '#fee2e2' },
        warning: { icon: '⚠', color: '#f59e0b', bg: '#fef3c7' },
        info: { icon: 'ℹ', color: '#3b82f6', bg: '#dbeafe' },
        success: { icon: '✓', color: '#10b981', bg: '#d1fae5' }
    };

    /**
     * Initialize toast container
     */
    function init() {
        if (container) return;

        container = document.createElement('div');
        container.id = 'toast-container';
        container.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 10000;
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-width: 400px;
        `;
        document.body.appendChild(container);
    }

    /**
     * Show a toast notification
     * @param {string} message - Message to display
     * @param {string} type - Type: 'error', 'warning', 'info', 'success'
     * @param {number} duration - Auto-dismiss duration in ms (0 = no auto-dismiss)
     */
    function show(message, type = 'info', duration = 5000) {
        init();

        // Prevent duplicate toasts
        const key = `${type}:${message}`;
        const lastShown = recentToasts.get(key);
        if (lastShown && Date.now() - lastShown < DUPLICATE_WINDOW) {
            console.log('[Toast] Skipping duplicate:', message);
            return;
        }
        recentToasts.set(key, Date.now());

        // Clean up old entries
        for (const [k, time] of recentToasts.entries()) {
            if (Date.now() - time > DUPLICATE_WINDOW) {
                recentToasts.delete(k);
            }
        }

        const config = TYPES[type] || TYPES.info;

        // Create toast element
        const toast = document.createElement('div');
        toast.style.cssText = `
            background: ${config.bg};
            border-left: 4px solid ${config.color};
            padding: 12px 16px;
            border-radius: 4px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            display: flex;
            align-items: start;
            gap: 12px;
            min-width: 300px;
            animation: slideIn 0.3s ease-out;
        `;

        // Icon
        const icon = document.createElement('span');
        icon.textContent = config.icon;
        icon.style.cssText = `
            font-size: 18px;
            color: ${config.color};
            flex-shrink: 0;
        `;

        // Message
        const msg = document.createElement('div');
        msg.textContent = message;
        msg.style.cssText = `
            flex: 1;
            font-size: 14px;
            color: #1f2937;
            line-height: 1.5;
        `;

        // Close button
        const closeBtn = document.createElement('button');
        closeBtn.textContent = '×';
        closeBtn.style.cssText = `
            background: none;
            border: none;
            font-size: 20px;
            color: #6b7280;
            cursor: pointer;
            padding: 0;
            width: 20px;
            height: 20px;
            flex-shrink: 0;
        `;
        closeBtn.onclick = () => remove(toast);

        toast.appendChild(icon);
        toast.appendChild(msg);
        toast.appendChild(closeBtn);
        container.appendChild(toast);

        // Auto-dismiss
        if (duration > 0) {
            setTimeout(() => remove(toast), duration);
        }
    }

    /**
     * Remove a toast
     */
    function remove(toast) {
        if (!toast || !toast.parentNode) return;

        toast.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => {
            if (toast.parentNode) {
                toast.parentNode.removeChild(toast);
            }
        }, 300);
    }

    /**
     * Convenience methods
     */
    const Toast = {
        show,
        error: (msg, duration) => show(msg, 'error', duration),
        warning: (msg, duration) => show(msg, 'warning', duration),
        info: (msg, duration) => show(msg, 'info', duration),
        success: (msg, duration) => show(msg, 'success', duration)
    };

    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from {
                transform: translateX(400px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }

        @keyframes slideOut {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(400px);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);

    // Export globally
    window.Toast = Toast;
})();
