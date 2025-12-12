#!/usr/bin/env python3
"""
Add right-click context menu to ticker chips for axis selection.
"""

import re

print("Adding axis context menu to ticker chips...")

# ============================================================
# 1. Add context menu HTML and CSS to index.html
# ============================================================
with open('charting_sandbox/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS for context menu in the style section
context_menu_css = '''
    /* Context menu for ticker chips */
    .chip-context-menu {
        position: fixed;
        background: white;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        z-index: 10000;
        min-width: 150px;
        display: none;
    }
    .chip-context-menu.visible { display: block; }
    .chip-context-menu-item {
        padding: 8px 12px;
        cursor: pointer;
        font-size: 13px;
    }
    .chip-context-menu-item:hover { background: #f0f0f0; }
    .chip-context-menu-item.active { background: #e0e0e0; font-weight: bold; }
    .chip-context-menu-divider { border-top: 1px solid #eee; margin: 4px 0; }
    .chip-axis-indicator {
        font-size: 9px;
        margin-left: 3px;
        opacity: 0.8;
        vertical-align: super;
    }
    '''

# Find the style section and add our CSS
if '.chip-context-menu' not in html:
    # Add before closing </style> tag
    html = html.replace('</style>', context_menu_css + '\n</style>')
    print("  Added context menu CSS")

# Add context menu HTML before closing </body>
context_menu_html = '''
    <!-- Context menu for ticker chips -->
    <div id="chip-context-menu" class="chip-context-menu">
        <div class="chip-context-menu-item" data-action="axis-right">Move to Right Axis</div>
        <div class="chip-context-menu-item" data-action="axis-left">Move to Left Axis</div>
        <div class="chip-context-menu-divider"></div>
        <div class="chip-context-menu-item" data-action="hide">Hide/Show</div>
    </div>
'''

if 'chip-context-menu' not in html or 'id="chip-context-menu"' not in html:
    html = html.replace('</body>', context_menu_html + '\n</body>')
    print("  Added context menu HTML")

with open('charting_sandbox/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ============================================================
# 2. Update chart-dom-builder.js - add axis indicator and context menu handler
# ============================================================
with open('charting_sandbox/chart-dom-builder.js', 'r', encoding='utf-8') as f:
    dom_content = f.read()

# Modify createTickerChip to accept axis parameter and add indicator
old_func_sig = 'createTickerChip(ticker, color, multiplier = 1, isHidden = false, onRemove = null) {'
new_func_sig = 'createTickerChip(ticker, color, multiplier = 1, isHidden = false, onRemove = null, axis = "right", onAxisChange = null) {'

if old_func_sig in dom_content:
    dom_content = dom_content.replace(old_func_sig, new_func_sig)
    print("  Updated createTickerChip signature")

# Add axis indicator after the ticker span
old_ticker_span = '''        const tickerSpan = document.createElement('span');
        tickerSpan.textContent = ticker;
        tickerSpan.style.marginRight = '5px';
        chip.appendChild(tickerSpan);'''

new_ticker_span = '''        const tickerSpan = document.createElement('span');
        tickerSpan.textContent = ticker;
        tickerSpan.style.marginRight = '2px';
        chip.appendChild(tickerSpan);

        // Axis indicator (L for left, empty for right which is default)
        const axisIndicator = document.createElement('span');
        axisIndicator.className = 'chip-axis-indicator';
        axisIndicator.textContent = axis === 'left' ? 'L' : '';
        axisIndicator.style.marginRight = '3px';
        chip.appendChild(axisIndicator);
        chip._axisIndicator = axisIndicator;
        chip._currentAxis = axis;
        chip._onAxisChange = onAxisChange;'''

if old_ticker_span in dom_content:
    dom_content = dom_content.replace(old_ticker_span, new_ticker_span)
    print("  Added axis indicator to chip")

# Add right-click handler for context menu
old_return = '''        if (isHidden) {
            chip.classList.add('chip--hidden');
        }
        return chip;
    },'''

new_return = '''        if (isHidden) {
            chip.classList.add('chip--hidden');
        }

        // Right-click context menu
        chip.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const menu = document.getElementById('chip-context-menu');
            if (menu) {
                // Position menu at click location
                menu.style.left = e.clientX + 'px';
                menu.style.top = e.clientY + 'px';
                menu.classList.add('visible');
                menu._targetChip = chip;
                menu._targetTicker = ticker;

                // Update active state
                menu.querySelectorAll('.chip-context-menu-item').forEach(item => {
                    item.classList.remove('active');
                    if (item.dataset.action === 'axis-' + chip._currentAxis) {
                        item.classList.add('active');
                    }
                });
            }
        });

        return chip;
    },'''

if old_return in dom_content:
    dom_content = dom_content.replace(old_return, new_return)
    print("  Added right-click handler to chip")

with open('charting_sandbox/chart-dom-builder.js', 'w', encoding='utf-8') as f:
    f.write(dom_content)

# ============================================================
# 3. Add context menu click handler to card.js
# ============================================================
with open('charting_sandbox/card.js', 'r', encoding='utf-8') as f:
    card_content = f.read()

# Find a good location to add the global context menu handler
# Add it near the beginning of the IIFE, after the constants

context_menu_handler = '''
    // Global context menu handler for ticker chips
    document.addEventListener('click', () => {
        const menu = document.getElementById('chip-context-menu');
        if (menu) menu.classList.remove('visible');
    });

    document.addEventListener('DOMContentLoaded', () => {
        const menu = document.getElementById('chip-context-menu');
        if (menu) {
            menu.addEventListener('click', (e) => {
                const item = e.target.closest('.chip-context-menu-item');
                if (!item) return;

                const action = item.dataset.action;
                const chip = menu._targetChip;
                const ticker = menu._targetTicker;

                if (!chip || !ticker) return;

                if (action === 'axis-left' || action === 'axis-right') {
                    const newAxis = action === 'axis-left' ? 'left' : 'right';
                    chip._currentAxis = newAxis;
                    if (chip._axisIndicator) {
                        chip._axisIndicator.textContent = newAxis === 'left' ? 'L' : '';
                    }
                    if (typeof chip._onAxisChange === 'function') {
                        chip._onAxisChange(ticker, newAxis);
                    }
                } else if (action === 'hide') {
                    // Toggle hidden state via chip click
                    chip.click();
                }

                menu.classList.remove('visible');
            });
        }
    });

'''

# Add after the opening of the IIFE
old_iife_start = "(function() {\n    'use strict';"
if old_iife_start in card_content and 'Global context menu handler' not in card_content:
    card_content = card_content.replace(old_iife_start, old_iife_start + context_menu_handler)
    print("  Added global context menu handler")

with open('charting_sandbox/card.js', 'w', encoding='utf-8') as f:
    f.write(card_content)

# ============================================================
# 4. Update where chips are created to pass axis and callback
# ============================================================
with open('charting_sandbox/card.js', 'r', encoding='utf-8') as f:
    card_content = f.read()

# Find where createTickerChip is called and add axis parameters
# This is in the renderChips or similar function
old_chip_call = 'const chip = this.createTickerChip(ticker, color, multiplier, isHidden, onRemove);'
# We need to find where this is and add the axis parameter

# Let's search for the pattern
chip_creation_pattern = r"const chip = (window\.ChartDomBuilder\.createTickerChip|this\.createTickerChip)\(ticker, color, multiplier, isHidden, onRemove\);"

if re.search(chip_creation_pattern, card_content):
    # This is likely in chart-dom-builder.js, let's check there instead
    pass

# Check chart-dom-builder.js for the chip creation call
with open('charting_sandbox/chart-dom-builder.js', 'r', encoding='utf-8') as f:
    dom_content = f.read()

old_add_ticker = 'const chip = this.createTickerChip(ticker, color, multiplier, isHidden, onRemove);'
new_add_ticker = '''const axis = (typeof getAxis === 'function') ? getAxis(ticker) : 'right';
            const chip = this.createTickerChip(ticker, color, multiplier, isHidden, onRemove, axis, onAxisChange);'''

if old_add_ticker in dom_content:
    dom_content = dom_content.replace(old_add_ticker, new_add_ticker)
    print("  Updated chip creation to include axis")

# Update the addTickerChip function signature
old_add_sig = 'addTickerChip(container, ticker, color, multiplier, isHidden, onRemove) {'
new_add_sig = 'addTickerChip(container, ticker, color, multiplier, isHidden, onRemove, getAxis = null, onAxisChange = null) {'

if old_add_sig in dom_content:
    dom_content = dom_content.replace(old_add_sig, new_add_sig)
    print("  Updated addTickerChip signature")

with open('charting_sandbox/chart-dom-builder.js', 'w', encoding='utf-8') as f:
    f.write(dom_content)

# ============================================================
# 5. Update card.js where addTickerChip is called
# ============================================================
with open('charting_sandbox/card.js', 'r', encoding='utf-8') as f:
    card_content = f.read()

# Find where addTickerChip is called and add the axis callback
# Pattern: window.ChartDomBuilder.addTickerChip(selectedTickersDiv, ticker, color, mult, isHidden, removeCb)
old_add_call_pattern = r'window\.ChartDomBuilder\.addTickerChip\(\s*selectedTickersDiv,\s*ticker,\s*color,\s*mult,\s*isHidden,\s*removeCb\s*\)'

# Replace with version that includes axis getter and callback
new_add_call = '''window.ChartDomBuilder.addTickerChip(
                        selectedTickersDiv, ticker, color, mult, isHidden, removeCb,
                        (t) => priceScaleAssignmentMap.get(t) || 'right',
                        (t, newAxis) => {
                            priceScaleAssignmentMap.set(t, newAxis);
                            card._priceScaleAssignmentMap = priceScaleAssignmentMap;
                            saveCards();
                            plot();
                        }
                    )'''

card_content = re.sub(old_add_call_pattern, new_add_call, card_content)
print("  Updated addTickerChip call with axis callbacks")

with open('charting_sandbox/card.js', 'w', encoding='utf-8') as f:
    f.write(card_content)

# ============================================================
# 6. Update version numbers
# ============================================================
with open('charting_sandbox/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for script in ['card.js', 'chart-dom-builder.js']:
    match = re.search(rf'{script}\?v=(\d+)', html)
    if match:
        old_v = int(match.group(1))
        html = html.replace(f'{script}?v={old_v}', f'{script}?v={old_v + 1}')
        print(f"  Updated {script} version to v{old_v + 1}")

with open('charting_sandbox/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! Right-click context menu added for axis selection.")
print("\nHow to use:")
print("  1. Right-click on any ticker chip")
print("  2. Select 'Move to Left Axis' or 'Move to Right Axis'")
print("  3. Tickers on left axis show 'L' indicator")
