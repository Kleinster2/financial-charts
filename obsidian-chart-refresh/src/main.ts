import { MarkdownView, Notice, Plugin, TFile } from "obsidian";
import { parseChartFilename, buildApiUrl, parseRegistry, registryEntryToParams, RegistryEntry } from "./parser";
import { fetchChartImage, writeChartImage, isApiAvailable } from "./chart-fetcher";
import {
  ChartRefreshSettings,
  DEFAULT_SETTINGS,
  ChartRefreshSettingTab,
} from "./settings";

// Regex to match image embeds: ![[filename.png]]
const IMAGE_EMBED_REGEX = /!\[\[([^\]]+\.png)\]\]/gi;

// Registry file path — try both vault root and investing/ subfolder
const REGISTRY_PATHS = ["chart-registry.md", "investing/chart-registry.md"];

export default class ChartRefreshPlugin extends Plugin {
  settings: ChartRefreshSettings;
  private lastRefreshTimes: Map<string, number> = new Map();
  private apiAvailable: boolean | null = null;
  private registry: Map<string, RegistryEntry> = new Map();
  private isRefreshing = false;

  async onload() {
    await this.loadSettings();
    await this.loadRegistry();

    // Add settings tab
    this.addSettingTab(new ChartRefreshSettingTab(this.app, this));

    // Register file-open event
    this.registerEvent(
      this.app.workspace.on("file-open", async (file) => {
        if (file && this.settings.autoRefresh && !this.isRefreshing) {
          await this.refreshChartsInNote(file);
        }
      })
    );

    // Add command: manual refresh
    this.addCommand({
      id: "refresh-charts-current-note",
      name: "Refresh charts in current note",
      callback: async () => {
        const file = this.app.workspace.getActiveFile();
        if (file) {
          await this.refreshChartsInNote(file, true);
        }
      },
    });

    // Add command: reload registry
    this.addCommand({
      id: "reload-chart-registry",
      name: "Reload chart registry",
      callback: async () => {
        await this.loadRegistry();
        new Notice(`Loaded ${this.registry.size} chart(s) from registry`);
      },
    });

    // Refresh the already-open note (file-open fires before plugins load)
    this.app.workspace.onLayoutReady(() => {
      if (this.settings.autoRefresh) {
        const file = this.app.workspace.getActiveFile();
        if (file) {
          this.refreshChartsInNote(file);
        }
      }
    });

    console.log("Chart Refresh plugin loaded");
  }

  /**
   * Load chart registry from chart-registry.md
   */
  async loadRegistry() {
    for (const path of REGISTRY_PATHS) {
      try {
        const file = this.app.vault.getAbstractFileByPath(path);
        if (file && file instanceof TFile) {
          const content = await this.app.vault.read(file);
          this.registry = parseRegistry(content);
          console.log(`Loaded ${this.registry.size} chart(s) from registry (${path})`);
          return;
        }
      } catch (error) {
        console.log(`Could not load chart registry from ${path}: ${error}`);
      }
    }
  }

  onunload() {
    console.log("Chart Refresh plugin unloaded");
  }

  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }

  async saveSettings() {
    await this.saveData(this.settings);
  }

  /**
   * Find and refresh all chart images embedded in a note
   */
  async refreshChartsInNote(file: TFile, manual = false) {
    try {
      // Read note content
      const content = await this.app.vault.read(file);

      // Find all image embeds
      const matches = [...content.matchAll(IMAGE_EMBED_REGEX)];
      if (matches.length === 0) {
        if (manual) new Notice("No chart embeds found in this note");
        return;
      }

      // Extract unique filenames
      const filenames = [...new Set(matches.map((m) => m[1]))];

      // Filter to parseable chart images
      const chartsToRefresh: { filename: string; apiUrl: string }[] = [];

      for (const filename of filenames) {
        const result = parseChartFilename(filename);

        if (result.type === "skip") {
          continue;
        }

        if (result.type === "unknown") {
          // Check registry fallback
          const registryEntry = this.registry.get(filename);
          if (registryEntry) {
            if (registryEntry.skip) {
              continue;
            }
            const params = registryEntryToParams(registryEntry);
            if (params) {
              if (!manual && !this.shouldRefresh(filename)) {
                continue;
              }
              const apiUrl = buildApiUrl(this.settings.apiBaseUrl, params);
              chartsToRefresh.push({ filename, apiUrl });
            }
          }
          continue;
        }

        if (result.type === "parsed") {
          // Check cache TTL
          if (!manual && !this.shouldRefresh(filename)) {
            continue;
          }

          const apiUrl = buildApiUrl(this.settings.apiBaseUrl, result.params);
          chartsToRefresh.push({ filename, apiUrl });
        }
      }

      if (chartsToRefresh.length === 0) {
        if (manual) new Notice("No charts to refresh");
        return;
      }

      // Check if API is available
      if (this.apiAvailable === null || this.apiAvailable === false) {
        this.apiAvailable = await isApiAvailable(this.settings.apiBaseUrl);
      }

      if (!this.apiAvailable) {
        if (manual) new Notice("Chart API not available");
        return;
      }

      // Refresh each chart
      let refreshedCount = 0;
      for (const { filename, apiUrl } of chartsToRefresh) {
        const imageData = await fetchChartImage(apiUrl);

        if (imageData) {
          const success = await writeChartImage(
            this.app.vault,
            filename,
            imageData,
            this.settings.attachmentsFolder
          );

          if (success) {
            this.lastRefreshTimes.set(filename, Date.now());
            refreshedCount++;
          }
        }
      }

      // Reopen the file to force Obsidian to re-render all images
      if (refreshedCount > 0) {
        await new Promise(resolve => setTimeout(resolve, 200));
        const leaf = this.app.workspace.getLeaf(false);
        if (leaf) {
          this.isRefreshing = true;
          await leaf.openFile(file, { active: true });
          this.isRefreshing = false;
        }
      }

      if (manual) {
        new Notice(`Refreshed ${refreshedCount} chart(s)`);
      }
    } catch (error) {
      new Notice(`Chart Refresh error: ${error}`);
      console.error("Chart Refresh error:", error);
    }
  }

  /**
   * Check if a chart should be refreshed based on cache TTL
   */
  private shouldRefresh(filename: string): boolean {
    const lastRefresh = this.lastRefreshTimes.get(filename);
    if (!lastRefresh) return true;

    const ttlMs = this.settings.cacheTtlMinutes * 60 * 1000;
    return Date.now() - lastRefresh > ttlMs;
  }
}
