import { App, PluginSettingTab, Setting } from "obsidian";
import type ChartRefreshPlugin from "./main";

export interface ChartRefreshSettings {
  apiBaseUrl: string;
  attachmentsFolder: string;
  autoRefresh: boolean;
  cacheTtlMinutes: number;
}

export const DEFAULT_SETTINGS: ChartRefreshSettings = {
  apiBaseUrl: "http://localhost:5000",
  attachmentsFolder: "investing/attachments",
  autoRefresh: true,
  cacheTtlMinutes: 5,
};

export class ChartRefreshSettingTab extends PluginSettingTab {
  plugin: ChartRefreshPlugin;

  constructor(app: App, plugin: ChartRefreshPlugin) {
    super(app, plugin);
    this.plugin = plugin;
  }

  display(): void {
    const { containerEl } = this;
    containerEl.empty();

    containerEl.createEl("h2", { text: "Chart Refresh Settings" });

    new Setting(containerEl)
      .setName("Auto-refresh on note open")
      .setDesc("Automatically refresh price charts when a note is opened")
      .addToggle((toggle) =>
        toggle.setValue(this.plugin.settings.autoRefresh).onChange(async (value) => {
          this.plugin.settings.autoRefresh = value;
          await this.plugin.saveSettings();
        })
      );

    new Setting(containerEl)
      .setName("API base URL")
      .setDesc("Base URL for the chart API (default: http://localhost:5000)")
      .addText((text) =>
        text
          .setPlaceholder("http://localhost:5000")
          .setValue(this.plugin.settings.apiBaseUrl)
          .onChange(async (value) => {
            this.plugin.settings.apiBaseUrl = value;
            await this.plugin.saveSettings();
          })
      );

    new Setting(containerEl)
      .setName("Attachments folder")
      .setDesc("Folder path where chart images are stored")
      .addText((text) =>
        text
          .setPlaceholder("investing/attachments")
          .setValue(this.plugin.settings.attachmentsFolder)
          .onChange(async (value) => {
            this.plugin.settings.attachmentsFolder = value;
            await this.plugin.saveSettings();
          })
      );

    new Setting(containerEl)
      .setName("Cache TTL (minutes)")
      .setDesc("Skip refresh if image was updated less than this many minutes ago")
      .addText((text) =>
        text
          .setPlaceholder("5")
          .setValue(String(this.plugin.settings.cacheTtlMinutes))
          .onChange(async (value) => {
            const num = parseInt(value, 10);
            if (!isNaN(num) && num >= 0) {
              this.plugin.settings.cacheTtlMinutes = num;
              await this.plugin.saveSettings();
            }
          })
      );
  }
}
