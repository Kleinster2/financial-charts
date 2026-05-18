$ErrorActionPreference = "Stop"
$base = "http://localhost:5000/api/chart/lw"
$out  = Join-Path $PSScriptRoot "..\investing\attachments" | Resolve-Path | Select-Object -ExpandProperty Path

$jobs = @(
    @{name="dxyz-price-chart.png"; url="$base`?tickers=DXYZ&normalize=false"},
    @{name="bptrx-price-chart.png"; url="$base`?tickers=BPTRX&normalize=false"},
    @{name="barax-price-chart.png"; url="$base`?tickers=BARAX&normalize=false"},
    @{name="bptrx-vs-bfgix-price-chart.png"; url="$base`?tickers=BPTRX,BFGIX&normalize=true&sort_by_last=true"},
    @{name="bptrx-vs-barax-vs-bscfx-price-chart.png"; url="$base`?tickers=BPTRX,BARAX,BSCFX&normalize=true&sort_by_last=true"},
    @{name="bptrx-vs-barax-vs-qqq-vs-spy-price-chart.png"; url="$base`?tickers=BPTRX,BARAX,QQQ,SPY&normalize=true&sort_by_last=true"},
    @{name="baron-core-funds-price-chart.png"; url="$base`?tickers=BPTRX,BFGIX,BFGFX,BGRIX,BIGFX,BREIX&normalize=true&start=2011-01-01&sort_by_last=true"},
    @{name="baron-all-funds-price-chart.png"; url="$base`?tickers=BPTRX,BARAX,BSCFX,BFGFX,BGRIX,BFTHX,BIGFX,BREIX,BGAIX,BDAFX,BFGIX,BTECX,BRIFX&normalize=true&start=2020-01-01&sort_by_last=true"}
)

foreach ($j in $jobs) {
    $path = Join-Path $out $j.name
    try {
        Invoke-WebRequest -Uri $j.url -OutFile $path -UseBasicParsing -TimeoutSec 60
        $size = [math]::Round((Get-Item $path).Length / 1KB, 1)
        Write-Host "OK  $($j.name) ($size KB)"
    } catch {
        Write-Host "FAIL $($j.name): $($_.Exception.Message)"
    }
}
