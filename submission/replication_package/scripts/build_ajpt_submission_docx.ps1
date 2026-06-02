Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$Submission = Join-Path $Root "submission"

$wdFormatXMLDocument = 12
$wdStory = 6
$wdCollapseEnd = 0
$wdLineSpaceSingle = 0
$wdLineSpaceDouble = 2
$wdAlignLeft = 0
$wdAlignCenter = 1
$wdCellAlignVerticalCenter = 1
$wdAutoFitWindow = 2

function Clean-InlineText {
    param([string]$Text)
    if ($null -eq $Text) { return "" }
    $t = $Text -replace "^\s*>\s*", ""
    $t = $t -replace '`([^`]+)`', '$1'
    $t = $t -replace '\*\*([^*]+)\*\*', '$1'
    return $t
}

function Set-BaseSelection {
    param([object]$Selection, [int]$LineRule = $wdLineSpaceDouble)
    $Selection.Font.Name = "Times New Roman"
    $Selection.Font.Size = 12
    $Selection.Font.Bold = $false
    $Selection.Font.Italic = $false
    $Selection.ParagraphFormat.Alignment = $wdAlignLeft
    $Selection.ParagraphFormat.LineSpacingRule = $LineRule
    $Selection.ParagraphFormat.SpaceBefore = 0
    $Selection.ParagraphFormat.SpaceAfter = 0
    $Selection.ParagraphFormat.LeftIndent = 0
    $Selection.ParagraphFormat.RightIndent = 0
    $Selection.ParagraphFormat.FirstLineIndent = 0
}

function Write-Inline {
    param([object]$Selection, [string]$Text)
    $text = Clean-InlineText $Text
    $pattern = '\*([^*]+)\*'
    $pos = 0
    $matches = [regex]::Matches($text, $pattern)
    foreach ($m in $matches) {
        if ($m.Index -gt $pos) {
            $Selection.Font.Italic = $false
            $Selection.TypeText($text.Substring($pos, $m.Index - $pos))
        }
        $Selection.Font.Italic = $true
        $Selection.TypeText($m.Groups[1].Value)
        $Selection.Font.Italic = $false
        $pos = $m.Index + $m.Length
    }
    if ($pos -lt $text.Length) {
        $Selection.Font.Italic = $false
        $Selection.TypeText($text.Substring($pos))
    }
}

function Add-Para {
    param(
        [object]$Selection,
        [string]$Text,
        [string]$Kind = "Body",
        [int]$LineRule = $wdLineSpaceDouble
    )
    Set-BaseSelection $Selection $LineRule
    if ($Kind -eq "Title") {
        $Selection.ParagraphFormat.Alignment = $wdAlignCenter
        $Selection.Font.Bold = $true
    } elseif ($Kind -eq "Heading1") {
        $Selection.ParagraphFormat.Alignment = $wdAlignCenter
        $Selection.Font.Bold = $true
        $Text = $Text.ToUpperInvariant()
    } elseif ($Kind -eq "Heading2") {
        $Selection.Font.Bold = $true
    } elseif ($Kind -eq "BlockQuote") {
        $Selection.ParagraphFormat.LeftIndent = 36
        $Selection.ParagraphFormat.RightIndent = 36
        $Selection.Font.Italic = $true
    } elseif ($Kind -eq "Caption") {
        $Selection.Font.Bold = $false
        $Selection.Font.Size = 11
    }
    Write-Inline $Selection $Text
    $Selection.TypeParagraph()
}

function Add-Blank {
    param([object]$Selection)
    Set-BaseSelection $Selection
    $Selection.TypeParagraph()
}

function Set-PageSetup {
    param([object]$Document)
    $Document.PageSetup.TopMargin = 72
    $Document.PageSetup.BottomMargin = 72
    $Document.PageSetup.LeftMargin = 72
    $Document.PageSetup.RightMargin = 72
}

function Save-Doc {
    param([object]$Document, [string]$Path)
    if (Test-Path $Path) { Remove-Item -LiteralPath $Path -Force }
    $Document.SaveAs([ref]$Path, [ref]$wdFormatXMLDocument)
    $Document.Close()
}

function New-AjptDoc {
    param([object]$Word)
    $doc = $Word.Documents.Add()
    Set-PageSetup $doc
    $doc.Styles.Item("Normal").Font.Name = "Times New Roman"
    $doc.Styles.Item("Normal").Font.Size = 12
    $doc.Styles.Item("Normal").ParagraphFormat.LineSpacingRule = $wdLineSpaceDouble
    $doc.Styles.Item("Normal").ParagraphFormat.SpaceBefore = 0
    $doc.Styles.Item("Normal").ParagraphFormat.SpaceAfter = 0
    return $doc
}

function Split-MarkdownTableLine {
    param([string]$Line)
    $trimmed = $Line.Trim()
    $trimmed = $trimmed.Trim("|")
    return @($trimmed -split "\|" | ForEach-Object { (Clean-InlineText $_.Trim()) })
}

function Add-WordTable {
    param(
        [object]$Document,
        [object]$Selection,
        [string[]]$Header,
        [object[]]$Rows,
        [int]$FontSize = 9
    )
    if ($Header.Count -eq 0) { return }
    $cols = $Header.Count
    $rowCount = $Rows.Count + 1
    $range = $Selection.Range
    $table = $Document.Tables.Add($range, $rowCount, $cols)
    $table.AutoFitBehavior($wdAutoFitWindow)
    $table.Range.Font.Name = "Times New Roman"
    $table.Range.Font.Size = $FontSize
    $table.Range.ParagraphFormat.LineSpacingRule = $wdLineSpaceSingle
    $table.Range.ParagraphFormat.SpaceBefore = 0
    $table.Range.ParagraphFormat.SpaceAfter = 0
    $table.Borders.Enable = $true
    for ($c = 1; $c -le $cols; $c++) {
        $table.Cell(1, $c).Range.Text = $Header[$c - 1]
        $table.Cell(1, $c).Range.Font.Bold = $true
        $table.Cell(1, $c).VerticalAlignment = $wdCellAlignVerticalCenter
    }
    for ($r = 0; $r -lt $Rows.Count; $r++) {
        $row = $Rows[$r]
        for ($c = 1; $c -le $cols; $c++) {
            $value = ""
            if (($c - 1) -lt $row.Count) { $value = $row[$c - 1] }
            $table.Cell($r + 2, $c).Range.Text = $value
            $table.Cell($r + 2, $c).VerticalAlignment = $wdCellAlignVerticalCenter
        }
    }
    $table.Rows.Item(1).HeadingFormat = $true
    $Selection.EndKey($wdStory) | Out-Null
    $Selection.TypeParagraph()
}

function Add-MdTableBlock {
    param([object]$Document, [object]$Selection, [string[]]$Lines, [int]$FontSize = 9)
    if ($Lines.Count -lt 2) { return }
    $header = Split-MarkdownTableLine $Lines[0]
    $rows = @()
    for ($i = 2; $i -lt $Lines.Count; $i++) {
        $rows += ,(Split-MarkdownTableLine $Lines[$i])
    }
    Add-WordTable $Document $Selection $header $rows $FontSize
}

function Extract-MainManuscriptBody {
    param([string[]]$Lines)
    $out = New-Object System.Collections.Generic.List[string]
    $skipNextTitleText = $false
    foreach ($line in $Lines) {
        if ($line -match "^## APPENDIX\s*$") { break }
        if ($line -match "^# Submission-Ready Manuscript") { continue }
        if ($line -match "^## Title\s*$") { $skipNextTitleText = $true; continue }
        if ($skipNextTitleText) {
            if ($line.Trim().Length -eq 0) { continue }
            $skipNextTitleText = $false
            continue
        }
        if ($line -match "^\[Insert (Table|Figure) [0-9A-Za-z]+ about here\]") { continue }
        $out.Add($line)
    }
    return $out.ToArray()
}

function Extract-AppendixSummary {
    param([string[]]$Lines)
    $out = New-Object System.Collections.Generic.List[string]
    $inAppendix = $false
    foreach ($line in $Lines) {
        if ($line -match "^## APPENDIX\s*$") { $inAppendix = $true }
        if ($inAppendix) { $out.Add($line) }
    }
    return $out.ToArray()
}

function Add-MarkdownContent {
    param(
        [object]$Document,
        [object]$Selection,
        [string[]]$Lines,
        [switch]$SkipTopH1,
        [int]$TableFontSize = 9
    )
    $i = 0
    while ($i -lt $Lines.Count) {
        $line = $Lines[$i]
        if ($line.Trim().Length -eq 0) { $i++; continue }
        if ($line -match "^#\s+(.+)$") {
            if (-not $SkipTopH1) { Add-Para $Selection $Matches[1] "Title" }
            $SkipTopH1 = $false
            $i++; continue
        }
        if ($line -match "^##\s+(.+)$") {
            Add-Para $Selection $Matches[1] "Heading1"
            $i++; continue
        }
        if ($line -match "^###\s+(.+)$") {
            Add-Para $Selection $Matches[1] "Heading2"
            $i++; continue
        }
        if ($line -match "^\|\s*.+\|\s*$") {
            $block = New-Object System.Collections.Generic.List[string]
            while ($i -lt $Lines.Count -and $Lines[$i] -match "^\|\s*.+\|\s*$") {
                $block.Add($Lines[$i])
                $i++
            }
            Add-MdTableBlock $Document $Selection $block.ToArray() $TableFontSize
            continue
        }
        if ($line -match "^\s*[-*]\s+(.+)$") {
            Add-Para $Selection ("- " + $Matches[1]) "Body"
            $i++; continue
        }
        if ($line -match "^\s*\d+\.\s+(.+)$") {
            Add-Para $Selection $line "Body"
            $i++; continue
        }
        if ($line -match "^\s*>\s*(.+)$") {
            Add-Para $Selection $Matches[1] "BlockQuote"
            $i++; continue
        }
        Add-Para $Selection $line "Body"
        $i++
    }
}

function Get-FigureCaptions {
    param([string[]]$Lines)
    $items = @()
    for ($i = 0; $i -lt $Lines.Count; $i++) {
        if ($Lines[$i] -match "^## Figure ([0-9A-Za-z]+)\.\s*(.+)$") {
            $num = $Matches[1]
            $title = $Matches[2]
            $caption = ""
            $alt = ""
            for ($j = $i + 1; $j -lt $Lines.Count; $j++) {
                if ($Lines[$j] -match "^## ") { break }
                if ($Lines[$j] -match "^Caption:\s*$" -and ($j + 2) -lt $Lines.Count) {
                    $caption = $Lines[$j + 2]
                }
                if ($Lines[$j] -match "^Alt text:\s*$" -and ($j + 2) -lt $Lines.Count) {
                    $alt = $Lines[$j + 2]
                }
            }
            $items += [pscustomobject]@{ Num = $num; Title = $title; Caption = $caption; Alt = $alt }
        }
    }
    return $items
}

function Get-TableBlocks {
    param([string[]]$Lines)
    $items = @()
    for ($i = 0; $i -lt $Lines.Count; $i++) {
        if ($Lines[$i] -match "^## Table (\d+)\.\s*(.+)$") {
            $num = $Matches[1]
            $title = $Matches[2]
            $tableLines = New-Object System.Collections.Generic.List[string]
            $note = New-Object System.Collections.Generic.List[string]
            for ($j = $i + 1; $j -lt $Lines.Count; $j++) {
                if ($Lines[$j] -match "^## ") { break }
                if ($Lines[$j] -match "^\|\s*.+\|\s*$") {
                    while ($j -lt $Lines.Count -and $Lines[$j] -match "^\|\s*.+\|\s*$") {
                        $tableLines.Add($Lines[$j])
                        $j++
                    }
                }
                if ($Lines[$j] -match "^Note:\s*$") {
                    for ($k = $j + 1; $k -lt $Lines.Count; $k++) {
                        if ($Lines[$k] -match "^## " -or $Lines[$k] -match "^### ") { break }
                        if ($Lines[$k].Trim().Length -gt 0) { $note.Add($Lines[$k]) }
                    }
                }
            }
            $items += [pscustomobject]@{ Num = $num; Title = $title; Lines = $tableLines.ToArray(); Note = $note.ToArray() }
        }
    }
    return $items
}

function Build-TitlePage {
    param([object]$Word)
    $doc = New-AjptDoc $Word
    $doc.Activate()
    $sel = $Word.Selection
    Add-Para $sel "Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL Relational Retrieval" "Title"
    Add-Blank $sel
    Add-Para $sel "[Author 1 Name]" "Body"
    Add-Para $sel "[Affiliation]" "Body"
    Add-Para $sel "[Email]" "Body"
    Add-Blank $sel
    Add-Para $sel "[Author 2 Name]" "Body"
    Add-Para $sel "[Affiliation]" "Body"
    Add-Para $sel "[Email]" "Body"
    Add-Blank $sel
    Add-Para $sel "Corresponding Author: [Corresponding author name, affiliation, mailing address if required, email, phone if required]" "Body"
    Add-Blank $sel
    Add-Para $sel "Acknowledgments: [Insert acknowledgments or state that the authors have no acknowledgments to report.]" "Body"
    Add-Para $sel "Funding: [Insert funding statement or state that the authors received no specific funding for this work.]" "Body"
    Add-Para $sel "Conflicts of Interest: [Insert conflict-of-interest statement.]" "Body"
    Add-Blank $sel
    Add-Para $sel "Data Availability" "Heading2"
    Add-Para $sel "Replication materials include the filer manifest, extraction and retrieval scripts, processed text and XBRL retrieval artifacts, rendered prompts, raw LLM outputs, claim-level coding files, model metadata, and checksum files. Raw SEC filings are publicly available from the SEC EDGAR system. The final data availability statement should be adjusted to match the journal's repository and file-size requirements." "Body"
    Add-Blank $sel
    Add-Para $sel "Generative AI and AI-Assisted Technology Disclosure" "Heading2"
    Add-Para $sel "The authors used generative AI and AI-assisted tools to support manuscript drafting, editing, code development, and organization of reproducibility materials. The authors reviewed, revised, and are responsible for all manuscript content, analyses, source interpretations, and conclusions. The use of LLMs as part of the methodological demonstration is described in the manuscript and online supplement." "Body"
    Add-Blank $sel
    Add-Para $sel "Keywords: Audit methodology; large language models; retrieval-augmented generation; XBRL; research design; construct validity; audit analytics." "Body"
    Save-Doc $doc (Join-Path $Submission "AJPT_Title_Page.docx")
}

function Build-CoverLetter {
    param([object]$Word)
    $doc = New-AjptDoc $Word
    $doc.Activate()
    $sel = $Word.Selection
    $lines = Get-Content (Join-Path $Submission "Cover_Letter.md")
    Add-MarkdownContent $doc $sel $lines -SkipTopH1 -TableFontSize 10
    Save-Doc $doc (Join-Path $Submission "AJPT_Cover_Letter.docx")
}

function Build-MainManuscript {
    param([object]$Word)
    $doc = New-AjptDoc $Word
    $doc.Activate()
    $sel = $Word.Selection
    $sourceManuscriptLines = Get-Content (Join-Path $Submission "Manuscript_Retrieval_as_Research_Design.md")
    $manuscriptLines = Extract-MainManuscriptBody $sourceManuscriptLines
    $appendixLines = Extract-AppendixSummary $sourceManuscriptLines
    $tableLines = Get-Content (Join-Path $Submission "Tables_and_Figures.md")
    Add-Para $sel "Retrieval as Research Design in LLM-Based Audit Research: Retrieval-Environment Validity and XBRL Relational Retrieval" "Title"
    Add-MarkdownContent $doc $sel $manuscriptLines -SkipTopH1 -TableFontSize 9
    Add-Para $sel "FIGURE CAPTIONS" "Heading1"
    foreach ($fig in (Get-FigureCaptions $tableLines)) {
        Add-Para $sel ("Figure " + $fig.Num + ". " + $fig.Title) "Heading2"
        if ($fig.Caption.Trim().Length -gt 0) { Add-Para $sel ("Caption: " + $fig.Caption) "Caption" }
        if ($fig.Alt.Trim().Length -gt 0) { Add-Para $sel ("Alt text: " + $fig.Alt) "Caption" }
    }
    Add-Para $sel "TABLES" "Heading1"
    foreach ($tbl in (Get-TableBlocks $tableLines)) {
        Add-Para $sel ("Table " + $tbl.Num + ". " + $tbl.Title) "Heading2"
        $fontSize = 9
        if ($tbl.Lines.Count -gt 0) {
            $colCount = (Split-MarkdownTableLine $tbl.Lines[0]).Count
            if ($colCount -gt 8) { $fontSize = 7 }
            elseif ($colCount -gt 5) { $fontSize = 8 }
            Add-MdTableBlock $doc $sel $tbl.Lines $fontSize
        }
        foreach ($noteLine in $tbl.Note) {
            Add-Para $sel ("Note: " + $noteLine) "Caption" $wdLineSpaceSingle
        }
        Add-Blank $sel
    }
    if ($appendixLines.Count -gt 0) {
        Add-MarkdownContent $doc $sel $appendixLines -SkipTopH1 -TableFontSize 9
    }
    Save-Doc $doc (Join-Path $Submission "AJPT_Main_Manuscript.docx")
}

function Build-OnlineSupplement {
    param([object]$Word)
    $doc = New-AjptDoc $Word
    $doc.Activate()
    $sel = $Word.Selection
    $lines = Get-Content (Join-Path $Submission "Online_Supplement_Appendix.md")
    Add-MarkdownContent $doc $sel $lines -SkipTopH1 -TableFontSize 8
    Save-Doc $doc (Join-Path $Submission "AJPT_Online_Supplement.docx")
}

function Build-ResponseToReviewers {
    param([object]$Word)
    $doc = New-AjptDoc $Word
    $doc.Activate()
    $sel = $Word.Selection
    $lines = Get-Content (Join-Path $Submission "Response_to_Reviewers_Second_Revision.md")
    Add-MarkdownContent $doc $sel $lines -TableFontSize 9
    Save-Doc $doc (Join-Path $Submission "AJPT_Response_to_Reviewers_Second_Revision.docx")
}

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
    Build-TitlePage $word
    Build-CoverLetter $word
    Build-MainManuscript $word
    Build-OnlineSupplement $word
    Build-ResponseToReviewers $word
}
finally {
    $word.Quit()
}

Write-Output "Created AJPT DOCX files in $Submission"
