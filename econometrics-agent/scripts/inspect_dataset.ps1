param(
    [Parameter(Mandatory = $true)]
    [string]$Data,
    [string]$SheetName,
    [int]$PreviewRows = 5,
    [int]$SampleValues = 5,
    [int]$MaxColumns = 200,
    [string]$OutFile
)

$pythonVenv = 'C:\Users\admin\Econometrics-Agent\.venv\Scripts\python.exe'
$pythonFallback = Get-Command py -ErrorAction SilentlyContinue
$scriptPath = Join-Path $PSScriptRoot 'inspect_dataset.py'

$argsList = @(
    $scriptPath,
    '--data', $Data,
    '--preview-rows', $PreviewRows,
    '--sample-values', $SampleValues,
    '--max-columns', $MaxColumns
)

if ($SheetName) {
    $argsList += @('--sheet-name', $SheetName)
}

if (Test-Path $pythonVenv) {
    $output = & $pythonVenv @argsList
    $exitCode = $LASTEXITCODE
    if ($OutFile) {
        Set-Content -LiteralPath $OutFile -Value ($output -join [Environment]::NewLine) -Encoding utf8
    }
    $output
    exit $exitCode
}

if ($pythonFallback) {
    $output = & py -3 @argsList
    $exitCode = $LASTEXITCODE
    if ($OutFile) {
        Set-Content -LiteralPath $OutFile -Value ($output -join [Environment]::NewLine) -Encoding utf8
    }
    $output
    exit $exitCode
}

throw 'No usable Python interpreter was found for inspect_dataset.ps1.'
