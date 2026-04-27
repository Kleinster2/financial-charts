#!/usr/bin/env pwsh

$ErrorActionPreference = "Stop"

function Get-MarkdownSection {
  param(
    [string]$Text,
    [string]$Heading
  )
  $escaped = [regex]::Escape($Heading)
  $pattern = "(?ms)^$escaped\s*$\r?\n?(.*?)(?=^##\s|\z)"
  $match = [regex]::Match($Text, $pattern)
  if ($match.Success) {
    return $match.Groups[1].Value.Trim()
  }
  return ""
}

try {
  $inputText = [Console]::In.ReadToEnd()
  $filePath = ""

  if (-not [string]::IsNullOrWhiteSpace($inputText)) {
    try {
      $payload = $inputText | ConvertFrom-Json -Depth 20
      if ($null -ne $payload.tool_input -and $null -ne $payload.tool_input.file_path) {
        $filePath = [string]$payload.tool_input.file_path
      }
    } catch {
      $filePath = ""
    }
  }

  if ([string]::IsNullOrWhiteSpace($filePath)) { exit 0 }

  $filePath = $filePath -replace "\\", "/"
  if ($filePath -notmatch "investing/") { exit 0 }
  if ($filePath -notmatch "\.md$") { exit 0 }

  $today = Get-Date -Format "yyyy-MM-dd"
  if ($filePath -match ("investing/Daily/" + [regex]::Escape($today) + "\.md$")) { exit 0 }

  $projectDir = $env:CLAUDE_PROJECT_DIR
  if ([string]::IsNullOrWhiteSpace($projectDir)) {
    $projectDir = (Get-Location).Path
  }

  $dailyDir = Join-Path $projectDir "investing/Daily"
  if (-not (Test-Path -LiteralPath $dailyDir)) {
    New-Item -ItemType Directory -Path $dailyDir -Force | Out-Null
  }

  $dailyNote = Join-Path $dailyDir "$today.md"
  if (-not (Test-Path -LiteralPath $dailyNote)) {
    Set-Content -LiteralPath $dailyNote -Value "#daily`n`n" -Encoding utf8
  }

  $content = Get-Content -LiteralPath $dailyNote -Raw
  if ($content -notmatch "(?m)^## Edit log\s*$") {
    if ($content.Length -gt 0 -and -not $content.EndsWith("`n")) {
      $content += "`n"
    }
    $content += "`n## Edit log`n`n"
    Set-Content -LiteralPath $dailyNote -Value $content -Encoding utf8
    $content = Get-Content -LiteralPath $dailyNote -Raw
  }

  $noteName = [System.IO.Path]::GetFileNameWithoutExtension($filePath)
  $editLogSection = Get-MarkdownSection -Text $content -Heading "## Edit log"
  $entityToken = "[[$noteName]]"
  if ($editLogSection -match [regex]::Escape($entityToken)) {
    exit 0
  }

  $subfolderMatch = [regex]::Match($filePath, "investing/([^/]+)/")
  $subfolder = if ($subfolderMatch.Success) { $subfolderMatch.Groups[1].Value } else { "Unknown" }

  $timestamp = Get-Date -Format "HH:mm"
  Add-Content -LiteralPath $dailyNote -Value ("- {0} - edited [[{1}]] ({2})" -f $timestamp, $noteName, $subfolder)
  Write-Output ("Logged edit to [[{0}]] in daily note. Remember to expand the edit log into a proper summary section before finishing." -f $noteName)
  exit 0
} catch {
  [Console]::Error.WriteLine("PostToolUse hook failed: $($_.Exception.Message)")
  exit 1
}
