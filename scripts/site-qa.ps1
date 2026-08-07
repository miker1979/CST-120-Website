param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'

Write-Host "Ghostline website QA" -ForegroundColor Cyan
Write-Host "Root: $Root"
Write-Host ""

$htmlFiles = Get-ChildItem -Path $Root -Filter *.html -File -Recurse |
    Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' }

$problems = New-Object System.Collections.Generic.List[string]

$mojibakePatterns = @(
    'â€”',
    'â€“',
    'â€™',
    'â€œ',
    'â€',
    'Ã',
    'Â',
    [char]0xFFFD
)

foreach ($file in $htmlFiles) {
    $text = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)

    foreach ($pattern in $mojibakePatterns) {
        if ($text.Contains([string]$pattern)) {
            $problems.Add("ENCODING  $($file.FullName)  contains '$pattern'")
        }
    }

    $attributeMatches = [regex]::Matches(
        $text,
        '(?i)(?:href|src)\s*=\s*["'']([^"''#?]+)["'']'
    )

    foreach ($match in $attributeMatches) {
        $target = $match.Groups[1].Value.Trim()

        if (
            [string]::IsNullOrWhiteSpace($target) -or
            $target -match '^(?:https?:|mailto:|tel:|javascript:|data:|//)'
        ) {
            continue
        }

        $decodedTarget = [System.Net.WebUtility]::HtmlDecode($target)
        $localPath = Join-Path $file.DirectoryName $decodedTarget

        if (-not (Test-Path -LiteralPath $localPath)) {
            $problems.Add("MISSING   $($file.FullName)  -> $target")
        }
    }
}

if ($problems.Count -eq 0) {
    Write-Host "PASS: No encoding artifacts or missing local href/src targets found." -ForegroundColor Green
    exit 0
}

Write-Host "Found $($problems.Count) issue(s):" -ForegroundColor Yellow
Write-Host ""
$problems | Sort-Object -Unique | ForEach-Object { Write-Host $_ }
exit 1
