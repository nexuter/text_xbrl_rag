Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$files = @(
    "submission/AJPT_Cover_Letter.docx",
    "submission/AJPT_Main_Manuscript.docx",
    "submission/AJPT_Online_Supplement.docx",
    "submission/AJPT_Response_to_Reviewers_Second_Revision.docx",
    "submission/AJPT_Title_Page.docx"
)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    foreach ($file in $files) {
        $path = (Resolve-Path $file).Path
        $doc = $word.Documents.Open($path, $false, $true)
        try {
            $pages = $doc.ComputeStatistics(2)
            $words = $doc.ComputeStatistics(0)
            $text = $doc.Content.Text
            $hasProtocol = $text.Contains("protocol-validation") -or $text.Contains("protocol validation")
            $hasTier2 = $text.Contains("Tier 2")
            $hasNineFiler = $text.Contains("nine-filer") -or $text.Contains("nine filer")
            $hasExtension48 = $text.Contains("48 extension outputs") -or $text.Contains("48 additional retrieval-conditioned outputs") -or $text.Contains("72 retrieval-conditioned outputs")
            $hasClaims281 = $text.Contains("281 preliminary coded claims") -or $text.Contains("281 coded claims")
            $tables = $doc.Tables.Count
            Write-Output ("{0}: pages={1}; words={2}; tables={3}; protocol={4}; tier2={5}; nine_filer={6}; extension48_or_72={7}; claims281={8}" -f (Split-Path $file -Leaf), $pages, $words, $tables, $hasProtocol, $hasTier2, $hasNineFiler, $hasExtension48, $hasClaims281)
        }
        finally {
            $doc.Close($false)
        }
    }
}
finally {
    $word.Quit()
}
