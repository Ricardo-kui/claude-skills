param(
    [Parameter(Mandatory = $true, ParameterSetName = 'Inspection')]
    [string]$Inspection,
    [Parameter(Mandatory = $true, ParameterSetName = 'Data')]
    [string]$Data,
    [Parameter(ParameterSetName = 'Data')]
    [string]$SheetName,
    [Parameter(ParameterSetName = 'Data')]
    [int]$PreviewRows = 5,
    [Parameter(ParameterSetName = 'Data')]
    [int]$SampleValues = 5,
    [Parameter(ParameterSetName = 'Data')]
    [int]$MaxColumns = 200,
    [ValidateSet('auto', 'ols', 'fe', 'iv', 'did', 'event-study', 'psm', 'ipw', 'aipw', 'ipwra', 'rdd', 'fuzzy-rdd')]
    [string]$Model = 'auto',
    [string]$Query,
    [string]$Outcome,
    [string]$Treatment,
    [string[]]$Controls,
    [string]$EntityId,
    [string]$TimeId,
    [string]$Instrument,
    [string]$Weights,
    [string]$Cluster,
    [string]$CovType,
    [string]$TreatGroup,
    [string]$Post,
    [string]$RunningVariable,
    [string]$Cutoff,
    [string]$Bandwidth,
    [string]$Kernel,
    [string]$RddMode,
    [string]$PolyOrder,
    [string]$Estimand,
    [string]$LeadWindow,
    [string]$LagWindow,
    [ValidateSet('powershell', 'json')]
    [string]$Format = 'powershell'
)

$pythonVenv = 'C:\Users\admin\Econometrics-Agent\.venv\Scripts\python.exe'
$pythonFallback = Get-Command py -ErrorAction SilentlyContinue
$scriptPath = Join-Path $PSScriptRoot 'draft_run_command.py'

$argsList = @(
    $scriptPath,
    '--model', $Model,
    '--format', $Format
)

if ($PSCmdlet.ParameterSetName -eq 'Inspection') {
    $argsList += @('--inspection', $Inspection)
} else {
    $argsList += @(
        '--data', $Data,
        '--preview-rows', $PreviewRows,
        '--sample-values', $SampleValues,
        '--max-columns', $MaxColumns
    )
    if ($SheetName) {
        $argsList += @('--sheet-name', $SheetName)
    }
}

foreach ($pair in @(
    @{ Name = 'Query'; Flag = '--query' },
    @{ Name = 'Outcome'; Flag = '--outcome' },
    @{ Name = 'Treatment'; Flag = '--treatment' },
    @{ Name = 'EntityId'; Flag = '--entity-id' },
    @{ Name = 'TimeId'; Flag = '--time-id' },
    @{ Name = 'Instrument'; Flag = '--instrument' },
    @{ Name = 'Weights'; Flag = '--weights' },
    @{ Name = 'Cluster'; Flag = '--cluster' },
    @{ Name = 'CovType'; Flag = '--cov-type' },
    @{ Name = 'TreatGroup'; Flag = '--treat-group' },
    @{ Name = 'Post'; Flag = '--post' },
    @{ Name = 'RunningVariable'; Flag = '--running-variable' },
    @{ Name = 'Cutoff'; Flag = '--cutoff' },
    @{ Name = 'Bandwidth'; Flag = '--bandwidth' },
    @{ Name = 'Kernel'; Flag = '--kernel' },
    @{ Name = 'RddMode'; Flag = '--rdd-mode' },
    @{ Name = 'PolyOrder'; Flag = '--poly-order' },
    @{ Name = 'Estimand'; Flag = '--estimand' },
    @{ Name = 'LeadWindow'; Flag = '--lead-window' },
    @{ Name = 'LagWindow'; Flag = '--lag-window' }
)) {
    $value = Get-Variable -Name $pair.Name -ValueOnly
    if ($null -ne $value -and $value -ne '') {
        $argsList += @($pair.Flag, $value)
    }
}

if ($Controls) {
    $argsList += '--controls'
    $argsList += $Controls
}

if (Test-Path $pythonVenv) {
    & $pythonVenv @argsList
    exit $LASTEXITCODE
}

if ($pythonFallback) {
    & py -3 @argsList
    exit $LASTEXITCODE
}

throw 'No usable Python interpreter was found for draft_run_command.ps1.'
