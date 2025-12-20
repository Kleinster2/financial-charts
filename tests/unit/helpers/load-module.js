/**
 * Load a browser-style module (assigns to window.X) in Node via vm.
 * Returns the exports from window after running the module code.
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { createWindowStub } = require('./browser-stub');

/**
 * Load a browser module and return the window object with its exports
 * @param {string} modulePath - Path to the .js file (relative to project root or absolute)
 * @param {Object} [existingWindow] - Optional existing window to extend
 * @returns {Object} The window object with module exports
 */
function loadModule(modulePath, existingWindow = null) {
  const window = existingWindow || createWindowStub();

  // Resolve path relative to project root if not absolute
  const projectRoot = path.join(__dirname, '..', '..', '..');
  const fullPath = path.isAbsolute(modulePath)
    ? modulePath
    : path.join(projectRoot, modulePath);

  const code = fs.readFileSync(fullPath, 'utf8');

  // Create context with window as global
  // Use getter for fetch so it picks up mocks set on window
  const context = vm.createContext({
    window,
    console,
    // Use window.document so modules can use document directly
    document: window.document,
    setTimeout,
    clearTimeout,
    Date,
    Array,
    Object,
    Map,
    Set,
    Number,
    String,
    Boolean,
    JSON,
    Math,
    Promise,
    Error,
    URLSearchParams,
    DOMException,
    AbortController,
    performance,
    get fetch() { return window.fetch; }
  });

  // Run the module code
  vm.runInContext(code, context, { filename: fullPath });

  return window;
}

/**
 * Load multiple modules in order, sharing the same window
 * @param {string[]} modulePaths - Array of paths to load in order
 * @returns {Object} The window object with all module exports
 */
function loadModules(modulePaths) {
  let window = createWindowStub();
  for (const modulePath of modulePaths) {
    window = loadModule(modulePath, window);
  }
  return window;
}

module.exports = { loadModule, loadModules, createWindowStub };
