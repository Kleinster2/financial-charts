import { requestUrl, Vault } from "obsidian";

/**
 * Fetch a chart image from the API
 * Returns the image as an ArrayBuffer, or null if fetch failed
 */
export async function fetchChartImage(
  apiUrl: string
): Promise<ArrayBuffer | null> {
  try {
    const response = await requestUrl({
      url: apiUrl,
      method: "GET",
    });

    if (response.status !== 200) {
      console.log(`Chart API returned status ${response.status}`);
      return null;
    }

    return response.arrayBuffer;
  } catch (error) {
    // Fail silently - API might not be running
    console.log(`Chart fetch failed (API not running?): ${error}`);
    return null;
  }
}

/**
 * Write chart image to vault attachments folder
 */
export async function writeChartImage(
  vault: Vault,
  filename: string,
  data: ArrayBuffer,
  attachmentsFolder: string
): Promise<boolean> {
  try {
    const path = `${attachmentsFolder}/${filename}`;

    // Check if file exists
    const existing = vault.getAbstractFileByPath(path);

    if (existing) {
      // Modify existing file
      await vault.modifyBinary(existing as any, data);
    } else {
      // Create new file
      await vault.createBinary(path, data);
    }

    return true;
  } catch (error) {
    console.error(`Failed to write chart image: ${error}`);
    return false;
  }
}

/**
 * Check if API is reachable (quick health check)
 */
export async function isApiAvailable(baseUrl: string): Promise<boolean> {
  try {
    const response = await requestUrl({
      url: baseUrl,
      method: "GET",
      throw: false,
    });
    return response.status === 200;
  } catch {
    return false;
  }
}
