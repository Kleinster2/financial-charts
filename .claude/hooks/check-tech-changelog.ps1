#!/usr/bin/env pwsh

$ErrorActionPreference = "Stop"

try {
  $techVault = "C:/Users/klein/obsidian/technologies"
  if (-not (Test-Path -LiteralPath $techVault)) { exit 0 }

  # Check git status for uncommitted changes (excluding changelog.md itself)
  $status = git -C $techVault status --porcelain 2>$null
  if ([string]::IsNullOrWhiteSpace($status)) { exit 0 }

  # Filter to only .md files that aren't changelog.md
  $changedNotes = $status -split '\r?\n' | Where-Object {
    $_ -match '\.md$' -and $_ -notmatch 'changelog\.md$'
  }
  if ($changedNotes.Count -eq 0) { exit 0 }

  # Extract filenames for the message
  $names = $changedNotes | ForEach-Object {
    ($_ -replace '^\s*\S+\s+', '') -replace '.*/', '' -replace '\.md$', ''
  }

  # Resolve full paths so we can read mtimes
  $changedPaths = $changedNotes | ForEach-Object {
    $rel = (($_ -replace '^\s*\S+\s+', '') -replace '^"', '') -replace '"$', ''
    Join-Path $techVault $rel
  } | Where-Object { Test-Path -LiteralPath $_ }

  $changelog = Join-Path $techVault "changelog.md"
  if (-not (Test-Path -LiteralPath $changelog)) {
    [Console]::Error.WriteLine(
      "TECH VAULT GATE: Notes changed in technologies vault ($($names -join ', ')) but changelog.md is missing."
    )
    exit 2
  }

  $text = Get-Content -LiteralPath $changelog -Raw -Encoding UTF8

  # Each unique mtime-date among changed files must have a changelog entry.
  # This avoids date-rollover false positives: yesterday's edits still uncommitted
  # are covered by yesterday's changelog entry, not today's.
  $changedDates = $changedPaths | ForEach-Object {
    (Get-Item -LiteralPath $_).LastWriteTime.ToString("yyyy-MM-dd")
  } | Sort-Object -Unique

  $missingDates = @()
  foreach ($d in $changedDates) {
    if ($text -notmatch [regex]::Escape($d)) {
      $missingDates += $d
    }
  }

  if ($missingDates.Count -eq 0) { exit 0 }

  [Console]::Error.WriteLine(
    "TECH VAULT GATE: Notes changed in technologies vault ($($names -join ', ')) but changelog.md has no entry for $($missingDates -join ', '). " +
    "Add a changelog section before finishing."
  )
  exit 2
} catch {
  [Console]::Error.WriteLine("Tech changelog hook failed: $($_.Exception.Message)")
  exit 1
}
