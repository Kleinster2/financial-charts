param(
    [string]$Destination = "$HOME\.agents\skill-parity"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Source = Split-Path -Parent $PSCommandPath
$ResolvedSource = (Resolve-Path -LiteralPath $Source).Path
$DestinationParent = Split-Path -Parent $Destination

if (-not $DestinationParent) {
    throw "Destination must include a parent directory: $Destination"
}

New-Item -ItemType Directory -Force -Path $Destination | Out-Null

$Files = @(
    "agent_skill_parity.py",
    "skill-parity.cmd",
    "registry.json",
    "README.md",
    "install.ps1"
)

foreach ($File in $Files) {
    $SourceFile = Join-Path $ResolvedSource $File
    if (-not (Test-Path -LiteralPath $SourceFile)) {
        throw "Missing source file: $SourceFile"
    }
    Copy-Item -LiteralPath $SourceFile -Destination (Join-Path $Destination $File) -Force
}

Write-Host "Installed skill parity runner to $Destination"
