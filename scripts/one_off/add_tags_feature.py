#!/usr/bin/env python3
"""
Add tag system for chart cards.
"""

import re

print("Adding tag system to chart cards...")

# ============================================================
# 1. Add CSS for tags in index.html
# ============================================================
with open('charting_sandbox/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

tags_css = '''
    /* Tag system styles */
    .tag-container { display: flex; flex-wrap: wrap; gap: 3px; margin-left: 8px; align-items: center; }
    .tag { display: inline-flex; align-items: center; background: #e0e0e0; border-radius: 12px; padding: 2px 8px; font-size: 0.75rem; color: #333; }
    .tag .tag-remove { margin-left: 4px; cursor: pointer; font-weight: bold; opacity: 0.6; }
    .tag .tag-remove:hover { opacity: 1; }
    .tag-add-btn { background: none; border: 1px dashed #999; border-radius: 12px; padding: 2px 8px; font-size: 0.75rem; color: #666; cursor: pointer; }
    .tag-add-btn:hover { border-color: #007bff; color: #007bff; }
    .tag-input-container { position: relative; display: inline-block; }
    .tag-input { padding: 2px 6px; font-size: 0.75rem; border: 1px solid #007bff; border-radius: 12px; width: 80px; outline: none; }
    .tag-suggestions { position: absolute; top: 100%; left: 0; background: #fff; border: 1px solid #ddd; border-radius: 4px; max-height: 150px; overflow-y: auto; z-index: 1000; min-width: 120px; display: none; }
    .tag-suggestions.show { display: block; }
    .tag-suggestion { padding: 4px 8px; cursor: pointer; font-size: 0.8rem; }
    .tag-suggestion:hover { background: #f0f0f0; }
    /* Tag filter in top controls */
    #tag-filter-container { display: flex; align-items: center; gap: 4px; margin-left: 8px; }
    #tag-filter-container label { font-size: 0.85rem; color: #666; }
    #tag-filter-select { padding: 4px 8px; font-size: 0.85rem; border: 1px solid #999; border-radius: 4px; }
'''

if '.tag-container' not in html:
    html = html.replace('</style>', tags_css + '\n</style>')
    print("  Added tags CSS")

# Add tag filter dropdown in top controls (after highlights button)
tag_filter_html = '''<div id="tag-filter-container">
      <label for="tag-filter-select">Tag:</label>
      <select id="tag-filter-select">
        <option value="">All</option>
      </select>
    </div>'''

if 'tag-filter-container' not in html:
    html = html.replace(
        '<button id="new-page-btn">New Page</button>',
        tag_filter_html + '\n    <button id="new-page-btn">New Page</button>'
    )
    print("  Added tag filter dropdown to top controls")

with open('charting_sandbox/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ============================================================
# 2. Update chart-dom-builder.js - add tag container and elements
# ============================================================
with open('charting_sandbox/chart-dom-builder.js', 'r', encoding='utf-8') as f:
    dom_content = f.read()

# Add tag container after star button
old_star_line = '<button class="star-btn" title="Add to Highlights">☆</button>'
new_star_line = '''<button class="star-btn" title="Add to Highlights">☆</button>
                <div class="tag-container"></div>'''

if 'tag-container' not in dom_content:
    dom_content = dom_content.replace(old_star_line, new_star_line)
    print("  Added tag container to card template")

# Add tagContainer to getCardElements
old_star_element = "starBtn: card.querySelector('.star-btn'),"
new_star_element = """starBtn: card.querySelector('.star-btn'),
            tagContainer: card.querySelector('.tag-container'),"""

if 'tagContainer' not in dom_content:
    dom_content = dom_content.replace(old_star_element, new_star_element)
    print("  Added tagContainer to getCardElements")

with open('charting_sandbox/chart-dom-builder.js', 'w', encoding='utf-8') as f:
    f.write(dom_content)

# ============================================================
# 3. Update card.js - add tags state, rendering, and filter
# ============================================================
with open('charting_sandbox/card.js', 'r', encoding='utf-8') as f:
    card_content = f.read()

# Add tags to saveCards
old_starred_save = 'starred: !!card._starred'
new_starred_save = '''starred: !!card._starred,
            tags: card._tags || []'''

if "tags: card._tags" not in card_content:
    card_content = card_content.replace(old_starred_save, new_starred_save)
    print("  Added tags to saveCards")

# Add global tag management functions after the context menu handler
tag_management_code = '''
    // Global tag management
    window._allTags = new Set();

    function getAllTags() {
        const tags = new Set();
        document.querySelectorAll('.chart-card').forEach(card => {
            (card._tags || []).forEach(tag => tags.add(tag));
        });
        window._allTags = tags;
        return Array.from(tags).sort();
    }

    function updateTagFilterDropdown() {
        const select = document.getElementById('tag-filter-select');
        if (!select) return;
        const currentValue = select.value;
        const tags = getAllTags();
        select.innerHTML = '<option value="">All</option>' +
            tags.map(t => `<option value="${t}"${t === currentValue ? ' selected' : ''}>${t}</option>`).join('');
    }

    function applyTagFilter() {
        const select = document.getElementById('tag-filter-select');
        if (!select) return;
        const filterTag = select.value;
        const highlightsMode = window.highlightsMode || false;

        document.querySelectorAll('.chart-card').forEach(card => {
            const page = card.closest('.page');
            const isActivePage = page && page.classList.contains('active');
            const hasTag = !filterTag || (card._tags || []).includes(filterTag);
            const isStarred = !highlightsMode || card._starred;

            if (isActivePage && hasTag && isStarred) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Initialize tag filter
    document.addEventListener('DOMContentLoaded', () => {
        const select = document.getElementById('tag-filter-select');
        if (select) {
            select.addEventListener('change', applyTagFilter);
        }
    });

    window.updateTagFilterDropdown = updateTagFilterDropdown;
    window.applyTagFilter = applyTagFilter;
    window.getAllTags = getAllTags;

'''

# Insert after the context menu handler
if 'window._allTags' not in card_content:
    # Find the end of the DOMContentLoaded block for context menu
    insert_marker = "window.saveCards = saveCards;"
    if insert_marker in card_content:
        card_content = card_content.replace(insert_marker, insert_marker + tag_management_code)
        print("  Added global tag management functions")

# Add renderTags function and tag event handlers
# Find the star button handler and add tag handling after it
star_handler_end = '''            starBtn.addEventListener('click', () => {
                card._starred = !card._starred;
                starBtn.textContent = card._starred ? '★' : '☆';
                starBtn.style.color = card._starred ? '#f5a623' : '#666';
                saveCards();
            });
        });'''

tag_handler_code = '''            starBtn.addEventListener('click', () => {
                card._starred = !card._starred;
                starBtn.textContent = card._starred ? '★' : '☆';
                starBtn.style.color = card._starred ? '#f5a623' : '#666';
                saveCards();
            });
        }

        // Tag management
        const { tagContainer } = elements;
        if (tagContainer) {
            card._tags = card._tags || [];

            function renderTags() {
                tagContainer.innerHTML = '';
                card._tags.forEach(tag => {
                    const tagEl = document.createElement('span');
                    tagEl.className = 'tag';
                    tagEl.innerHTML = `${tag}<span class="tag-remove" data-tag="${tag}">&times;</span>`;
                    tagContainer.appendChild(tagEl);
                });

                // Add "+" button
                const addBtn = document.createElement('button');
                addBtn.className = 'tag-add-btn';
                addBtn.textContent = '+';
                addBtn.title = 'Add tag';
                addBtn.addEventListener('click', showTagInput);
                tagContainer.appendChild(addBtn);

                // Remove tag handler
                tagContainer.querySelectorAll('.tag-remove').forEach(btn => {
                    btn.addEventListener('click', (e) => {
                        const tagToRemove = e.target.dataset.tag;
                        card._tags = card._tags.filter(t => t !== tagToRemove);
                        renderTags();
                        saveCards();
                        if (window.updateTagFilterDropdown) window.updateTagFilterDropdown();
                    });
                });
            }

            function showTagInput() {
                const inputContainer = document.createElement('div');
                inputContainer.className = 'tag-input-container';

                const input = document.createElement('input');
                input.type = 'text';
                input.className = 'tag-input';
                input.placeholder = 'Tag...';

                const suggestions = document.createElement('div');
                suggestions.className = 'tag-suggestions';

                inputContainer.appendChild(input);
                inputContainer.appendChild(suggestions);

                // Replace add button with input
                const addBtn = tagContainer.querySelector('.tag-add-btn');
                if (addBtn) addBtn.style.display = 'none';
                tagContainer.appendChild(inputContainer);
                input.focus();

                function updateSuggestions() {
                    const val = input.value.toLowerCase().trim();
                    const allTags = window.getAllTags ? window.getAllTags() : [];
                    const matches = allTags.filter(t =>
                        t.toLowerCase().includes(val) && !card._tags.includes(t)
                    );

                    if (matches.length > 0 && val) {
                        suggestions.innerHTML = matches.map(t =>
                            `<div class="tag-suggestion" data-tag="${t}">${t}</div>`
                        ).join('');
                        suggestions.classList.add('show');

                        suggestions.querySelectorAll('.tag-suggestion').forEach(el => {
                            el.addEventListener('click', () => {
                                addTag(el.dataset.tag);
                            });
                        });
                    } else {
                        suggestions.classList.remove('show');
                    }
                }

                function addTag(tag) {
                    tag = tag.trim();
                    if (tag && !card._tags.includes(tag)) {
                        card._tags.push(tag);
                        renderTags();
                        saveCards();
                        if (window.updateTagFilterDropdown) window.updateTagFilterDropdown();
                    } else {
                        inputContainer.remove();
                        if (addBtn) addBtn.style.display = '';
                    }
                }

                input.addEventListener('input', updateSuggestions);

                input.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        addTag(input.value);
                    } else if (e.key === 'Escape') {
                        inputContainer.remove();
                        if (addBtn) addBtn.style.display = '';
                    }
                });

                input.addEventListener('blur', () => {
                    setTimeout(() => {
                        if (document.activeElement !== input) {
                            inputContainer.remove();
                            if (addBtn) addBtn.style.display = '';
                        }
                    }, 200);
                });
            }

            renderTags();
        }'''

if 'renderTags' not in card_content:
    # Need to handle the malformed code around star handler
    # First check if the problematic pattern exists
    if star_handler_end in card_content:
        card_content = card_content.replace(star_handler_end, tag_handler_code)
        print("  Added tag rendering and event handlers")
    else:
        # Try alternate pattern
        alt_pattern = '''starBtn.addEventListener('click', () => {
                card._starred = !card._starred;
                starBtn.textContent = card._starred ? '★' : '☆';
                starBtn.style.color = card._starred ? '#f5a623' : '#666';
                saveCards();
            });
        }'''
        if alt_pattern in card_content:
            card_content = card_content.replace(alt_pattern, tag_handler_code)
            print("  Added tag rendering and event handlers (alt pattern)")
        else:
            print("  WARNING: Could not find star handler pattern to add tag handlers")

with open('charting_sandbox/card.js', 'w', encoding='utf-8') as f:
    f.write(card_content)

# ============================================================
# 4. Update pages.js to integrate tag filter with highlights
# ============================================================
with open('charting_sandbox/pages.js', 'r', encoding='utf-8') as f:
    pages_content = f.read()

# Update applyHighlightsFilter to work with tags
old_highlights_filter = '''function applyHighlightsFilter() {
        const cards = document.querySelectorAll('.chart-card');
        cards.forEach(card => {
            if (highlightsMode) {
                card.style.display = card._starred ? '' : 'none';
            } else {
                const page = card.closest('.page');
                if (page && page.classList.contains('active')) {
                    card.style.display = '';
                }
            }
        });
    }'''

new_highlights_filter = '''function applyHighlightsFilter() {
        // Use the unified tag filter if available
        if (window.applyTagFilter) {
            window.applyTagFilter();
            return;
        }

        const cards = document.querySelectorAll('.chart-card');
        cards.forEach(card => {
            if (highlightsMode) {
                card.style.display = card._starred ? '' : 'none';
            } else {
                const page = card.closest('.page');
                if (page && page.classList.contains('active')) {
                    card.style.display = '';
                }
            }
        });
    }'''

if 'window.applyTagFilter' not in pages_content:
    pages_content = pages_content.replace(old_highlights_filter, new_highlights_filter)
    print("  Updated applyHighlightsFilter to integrate with tag filter")

# Export highlightsMode for tag filter
if 'window.highlightsMode' not in pages_content:
    pages_content = pages_content.replace(
        'let highlightsMode = false;',
        'let highlightsMode = false;\n    window.highlightsMode = false;'
    )
    pages_content = pages_content.replace(
        'highlightsMode = !highlightsMode;',
        'highlightsMode = !highlightsMode;\n        window.highlightsMode = highlightsMode;'
    )
    print("  Exported highlightsMode to window")

with open('charting_sandbox/pages.js', 'w', encoding='utf-8') as f:
    f.write(pages_content)

# ============================================================
# 5. Update version numbers
# ============================================================
with open('charting_sandbox/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for script in ['card.js', 'chart-dom-builder.js', 'pages.js']:
    match = re.search(rf'{script}\?v=(\d+)', html)
    if match:
        old_v = int(match.group(1))
        html = html.replace(f'{script}?v={old_v}', f'{script}?v={old_v + 1}')
        print(f"  Updated {script} version to v{old_v + 1}")

with open('charting_sandbox/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! Tag system added.")
print("\nHow to use:")
print("  1. Click the '+' button next to the star on any chart card")
print("  2. Type a tag name and press Enter (or select from suggestions)")
print("  3. Click the 'x' on a tag to remove it")
print("  4. Use the 'Tag:' dropdown in top controls to filter by tag")
print("  5. Tags work together with the Highlights filter")
