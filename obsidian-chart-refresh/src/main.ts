import { Notice, Plugin, TFile } from "obsidian";
import { parseChartFilename, buildApiUrl } from "./parser";
import { fetchChartImage, writeChartImage, isApiAvailable } from "./chart-fetcher";
import {
  ChartRefreshSettings,
  DEFAULT_SETTINGS,
  ChartRefreshSettingTab,
} from "./settings";

// Regex to match image embeds: ![[filename.png]]
const IMAGE_EMBED_REGEX = /!\[\[([^\]]+\.png)\]\]/gi;

export default class ChartRefreshPlugin extends Plugin {
  settings: ChartRefreshSettings;
  private lastRefreshTimes: Map<string, number> = new Map();
  private apiAvailable: boolean | null = null;

  async onload() {
    await this.loadSettings();

    // Add settings tab
    this.addSettingTab(new ChartRefreshSettingTab(this.app, this));

    // Register file-open event
    this.registerEvent(
      this.app.workspace.on("file-open", async (file) => {
        if (file && this.settings.autoRefresh) {
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

    console.log("Chart Refresh plugin loaded");
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
    // Read note content
    const content = await this.app.vault.read(file);

    // Find all image embeds
    const matches = [...content.matchAll(IMAGE_EMBED_REGEX)];
    if (matches.length === 0) return;

    // Extract unique filenames
    const filenames = [...new Set(matches.map((m) => m[1]))];

    // Filter to parseable chart images
    const chartsToRefresh: { filename: string; apiUrl: string }[] = [];

    for (const filename of filenames) {
      const result = parseChartFilename(filename);

      if (result.type === "skip") {
        // Fundamentals chart - skip
        continue;
      }

      if (result.type === "unknown") {
        // TODO: check registry fallback
        console.log(`Unknown chart pattern: ${filename}`);
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

    if (chartsToRefresh.length === 0) return;

    // Check if API is available (only once per session until it succeeds)
    if (this.apiAvailable === null || this.apiAvailable === false) {
      this.apiAvailable = await isApiAvailable(this.settings.apiBaseUrl);
    }

    if (!this.apiAvailable) {
      if (manual) {
        new Notice("Chart API not available");
      }
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

    if (manual && refreshedCount > 0) {
      new Notice(`Refreshed ${refreshedCount} chart(s)`);
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
