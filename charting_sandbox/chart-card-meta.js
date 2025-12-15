/**
 * Chart Card Meta Module
 *
 * Extracted from card.js - handles star, tags, and notes UI.
 * Uses ctx for state access.
 *
 * Exports: window.ChartCardMeta
 */

window.ChartCardMeta = (() => {

    /**
     * Initialize star button functionality
     * @param {Object} ctx - Card context
     */
    function initStarButton(ctx) {
        const starBtn = ctx.elements.starBtn;
        if (!starBtn) return;

        // Set initial star state
        starBtn.textContent = ctx.starred ? '★' : '☆';
        starBtn.style.color = ctx.starred ? '#f5a623' : '#666';

        starBtn.addEventListener('click', () => {
            ctx.starred = !ctx.starred;
            window.ChartCardContext.syncToCard(ctx);
            starBtn.textContent = ctx.starred ? '★' : '☆';
            starBtn.style.color = ctx.starred ? '#f5a623' : '#666';
            ctx.saveCards();
        });
    }

    /**
     * Initialize tag management functionality
     * @param {Object} ctx - Card context
     */
    function initTagManagement(ctx) {
        const tagContainer = ctx.elements.tagContainer;
        if (!tagContainer) return;

        if (!ctx.tags) ctx.tags = [];

        function renderTags() {
            tagContainer.innerHTML = '';
            ctx.tags.forEach(tag => {
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
                    ctx.tags = ctx.tags.filter(t => t !== tagToRemove);
                    window.ChartCardContext.syncToCard(ctx);
                    renderTags();
                    ctx.saveCards();
                    if (window.updateTagFilterDropdown) window.updateTagFilterDropdown();
                    if (window.applyFilters) window.applyFilters();
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
                    t.toLowerCase().includes(val) && !ctx.tags.includes(t)
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
                if (tag && !ctx.tags.includes(tag)) {
                    ctx.tags.push(tag);
                    window.ChartCardContext.syncToCard(ctx);
                    renderTags();
                    ctx.saveCards();
                    if (window.updateTagFilterDropdown) window.updateTagFilterDropdown();
                    if (window.applyFilters) window.applyFilters();
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
    }

    /**
     * Initialize notes section functionality
     * @param {Object} ctx - Card context
     */
    function initNotesSection(ctx) {
        const { notesSection, notesTextarea } = ctx.elements;

        // Initialize notes UI visibility
        if (notesSection && notesTextarea) {
            notesSection.style.display = ctx.showNotes ? 'block' : 'none';
            notesTextarea.value = ctx.notes || '';
        }

        // Auto-save notes on input
        if (notesTextarea) {
            notesTextarea.addEventListener('input', () => {
                ctx.notes = notesTextarea.value;
                window.ChartCardContext.syncToCard(ctx);
                ctx.saveCards();
            });
        }
    }

    /**
     * Initialize all meta UI components (star, tags, notes)
     * @param {Object} ctx - Card context
     */
    function initAll(ctx) {
        initStarButton(ctx);
        initTagManagement(ctx);
        initNotesSection(ctx);
    }

    return {
        initStarButton,
        initTagManagement,
        initNotesSection,
        initAll
    };

})();
