Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$FigureDir = Join-Path $Root "submission\figures"
$Edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

if (-not (Test-Path $Edge)) {
    throw "Microsoft Edge was not found at $Edge"
}

$figures = @(
    @{
        Svg = "Figure_1_Retrieval_Environment_Validity.svg"
        Stem = "Figure_1_Retrieval_Environment_Validity"
        Width = 3600
        Height = 2940
    },
    @{
        Svg = "Figure_1A_Claim_Correctness_Layers.svg"
        Stem = "Figure_1A_Claim_Correctness_Layers"
        Width = 3600
        Height = 2400
    },
    @{
        Svg = "Figure_2_Methodological_Demonstration_Pipeline.svg"
        Stem = "Figure_2_Methodological_Demonstration_Pipeline"
        Width = 4200
        Height = 3300
    }
)

foreach ($fig in $figures) {
    $svgPath = Join-Path $FigureDir $fig.Svg
    if (-not (Test-Path $svgPath)) {
        throw "Missing SVG input: $svgPath"
    }

    $htmlPath = Join-Path $FigureDir ($fig.Stem + ".html")
    $pngPath = Join-Path $FigureDir ($fig.Stem + ".png")
    $pdfPath = Join-Path $FigureDir ($fig.Stem + ".pdf")
    $svgUri = ([System.Uri](Resolve-Path $svgPath).Path).AbsoluteUri

    $html = @"
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>$($fig.Stem)</title>
<style>
  html, body {
    margin: 0;
    padding: 0;
    width: $($fig.Width)px;
    height: $($fig.Height)px;
    background: #ffffff;
  }
  .canvas {
    width: $($fig.Width)px;
    height: $($fig.Height)px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #ffffff;
  }
  img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
  }
</style>
</head>
<body>
<div class="canvas">
  <img src="$svgUri" alt="$($fig.Stem)">
</div>
</body>
</html>
"@
    Set-Content -LiteralPath $htmlPath -Value $html -Encoding UTF8
    $htmlUri = ([System.Uri](Resolve-Path $htmlPath).Path).AbsoluteUri

    if (Test-Path $pngPath) { Remove-Item -LiteralPath $pngPath -Force }
    if (Test-Path $pdfPath) { Remove-Item -LiteralPath $pdfPath -Force }

    & $Edge --headless --disable-gpu --hide-scrollbars --window-size="$($fig.Width),$($fig.Height)" --screenshot="$pngPath" $htmlUri | Out-Null
    & $Edge --headless --disable-gpu --print-to-pdf="$pdfPath" --print-to-pdf-no-header $htmlUri | Out-Null

    if (-not (Test-Path $pngPath)) {
        throw "PNG export failed for $($fig.Stem)"
    }
    if (-not (Test-Path $pdfPath)) {
        throw "PDF export failed for $($fig.Stem)"
    }
}

Write-Output "Exported PNG and PDF figure files to $FigureDir"
