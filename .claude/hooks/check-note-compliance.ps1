#!/usr/bin/env pwsh
# PostToolUse hook: runs note compliance on edited actor files.
# Only fires for investing/Actors/*.md edits. Non-blocking (warnings only).
# Exits 0 always — this is advisory, not a gate.

$ErrorActionPreference = "Stop"

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

  # Only run on investing/Actors/*.md files
  if ($filePath -notmatch "investing/Actors/[^/]+\.md$") { exit 0 }

  $projectDir = $env:CLAUDE_PROJECT_DIR
  if ([string]::IsNullOrWhiteSpace($projectDir)) {
    $projectDir = (Get-Location).Path
  }

  # Resolve to absolute path for the compliance script
  $absPath = $filePath
  if (-not [System.IO.Path]::IsPathRooted($filePath)) {
    $absPath = Join-Path $projectDir $filePath
  }

  if (-not (Test-Path -LiteralPath $absPath)) { exit 0 }

  $scriptPath = Join-Path $projectDir "scripts/check_note_compliance.py"
  if (-not (Test-Path -LiteralPath $scriptPath)) { exit 0 }

  # Run compliance check, capture output
  $result = & python $scriptPath $absPath 2>&1
  $exitCode = $LASTEXITCODE

  # Only report if there are errors (exit code 1)
  if ($exitCode -ne 0) {
    # Filter to ERROR lines only — warnings are noise during editing
    $errors = $result | Where-Object { $_ -match "^\s*ERROR" }
    if ($errors) {
      $noteName = [System.IO.Path]::GetFileNameWithoutExtension($filePath)
      $errorList = ($errors | ForEach-Object { $_.ToString().Trim() }) -join "`n  "
      [Console]::Error.WriteLine("COMPLIANCE ($noteName.md):`n  $errorList")
    }
  }

  # Always exit 0 — advisory only, never blocks
  exit 0
} catch {
  # Fail silently — never block edits due to hook errors
  exit 0
}
