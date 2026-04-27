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
  $today = Get-Date -Format "yyyy-MM-dd"
  $projectDir = $env:CLAUDE_PROJECT_DIR
  if ([string]::IsNullOrWhiteSpace($projectDir)) {
    $projectDir = (Get-Location).Path
  }

  $dailyNote = Join-Path $projectDir ("investing/Daily/{0}.md" -f $today)
  if (-not (Test-Path -LiteralPath $dailyNote)) { exit 0 }

  $text = (Get-Content -LiteralPath $dailyNote -Raw -Encoding UTF8).Normalize("FormC")
  $editLogSection = Get-MarkdownSection -Text $text -Heading "## Edit log"
  if ([string]::IsNullOrWhiteSpace($editLogSection)) { exit 0 }

  # Parse edit log entries with timestamps, only check recent ones (within 2 hours)
  # to avoid false positives from concurrent/previous sessions whose summary lines
  # may not yet be written. Format: "- HH:MM - edited [[Entity]] (Category)"
  $now = Get-Date
  $cutoffMinutes = 120
  $recentEntities = @()
  foreach ($line in $editLogSection -split '\r?\n') {
    $tsMatch = [regex]::Match($line, '^\s*-\s+(\d{1,2}):(\d{2})\s+-\s+edited\s+\[\[([^\]|]+)')
    if ($tsMatch.Success) {
      $h = [int]$tsMatch.Groups[1].Value
      $m = [int]$tsMatch.Groups[2].Value
      $entryTime = (Get-Date -Hour $h -Minute $m -Second 0)
      # Handle midnight wraparound: if entry time is in the future, it was yesterday
      if ($entryTime -gt $now.AddMinutes(5)) {
        $entryTime = $entryTime.AddDays(-1)
      }
      $diffMinutes = ($now - $entryTime).TotalMinutes
      if ($diffMinutes -ge 0 -and $diffMinutes -le $cutoffMinutes) {
        $recentEntities += $tsMatch.Groups[3].Value.Normalize("FormC")
      }
    }
  }
  $entities = $recentEntities | Sort-Object -Unique

  if ($entities.Count -eq 0) { exit 0 }

  # Collect summary text from today's note
  $summarySection = Get-MarkdownSection -Text $text -Heading "## Notes created/expanded"

  # Before 6am, also check yesterday's daily note (common: working past midnight)
  $hour = (Get-Date).Hour
  if ($hour -lt 6) {
    $yesterday = (Get-Date).AddDays(-1).ToString("yyyy-MM-dd")
    $yesterdayNote = Join-Path $projectDir ("investing/Daily/{0}.md" -f $yesterday)
    if (Test-Path -LiteralPath $yesterdayNote) {
      $yesterdayText = (Get-Content -LiteralPath $yesterdayNote -Raw -Encoding UTF8).Normalize("FormC")
      $yesterdaySummary = Get-MarkdownSection -Text $yesterdayText -Heading "## Notes created/expanded"
      if (-not [string]::IsNullOrWhiteSpace($yesterdaySummary)) {
        $summarySection = $summarySection + "`n" + $yesterdaySummary
      }
    }
  }

  $noteFilename = Split-Path $dailyNote -Leaf
  if ([string]::IsNullOrWhiteSpace($summarySection)) {
    $entityList = ($entities -join ", ")
    [Console]::Error.WriteLine(
      "DAILY NOTE GATE ($noteFilename): Edit log has entries ($entityList) but no '## Notes created/expanded' section. " +
      "Update the daily note with a summary of what was created/changed before finishing."
    )
    exit 2
  }

  # Fix double-encoded UTF-8: é stored as Ã© (bytes C3 A9 read as Latin-1 then re-encoded)
  # Reverse: take Latin-1 bytes → reinterpret as UTF-8
  function Repair-DoubleUtf8 {
    param([string]$s)
    try {
      $latin1 = [System.Text.Encoding]::GetEncoding("iso-8859-1")
      $utf8 = [System.Text.Encoding]::UTF8
      $bytes = $latin1.GetBytes($s)
      return $utf8.GetString($bytes).Normalize("FormC")
    } catch { return $s }
  }

  $missing = @()
  foreach ($entity in $entities) {
    $escaped = [regex]::Escape($entity)
    $found = [regex]::IsMatch($summarySection, $escaped, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
    if (-not $found) {
      # Try repairing double-encoded UTF-8 and matching the repaired name
      $repaired = Repair-DoubleUtf8 $entity
      if ($repaired -ne $entity) {
        $found = [regex]::IsMatch($summarySection, [regex]::Escape($repaired), [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
      }
    }
    if (-not $found) {
      $displayName = Repair-DoubleUtf8 $entity
      $missing += "[[$displayName]]"
    }
  }

  if ($missing.Count -gt 0) {
    [Console]::Error.WriteLine(
      "DAILY NOTE GATE ($noteFilename): These entities were edited but not mentioned in '## Notes created/expanded': " +
      ($missing -join " ") +
      ". Add a summary line for each before finishing."
    )
    exit 2
  }

  exit 0
} catch {
  [Console]::Error.WriteLine("Stop hook failed: $($_.Exception.Message)")
  exit 1
}
