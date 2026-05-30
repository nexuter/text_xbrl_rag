import csv
import re
import sys
from pathlib import Path


csv.field_size_limit(sys.maxsize)

PROCESSED = Path("data/processed")
REPORT_PATH = Path("plan/52_llm_results_validation_log.md")

RUNS = [
    {
        "label": "gemma4_31b_full",
        "role": "main_deep_case",
        "expected_outputs": 24,
        "coding_file": PROCESSED / "coding" / "claim_level_coding_gemma4_31b.csv",
    },
    {
        "label": "gemma4_31b_extension",
        "role": "bounded_extension",
        "expected_outputs": 18,
        "coding_file": PROCESSED / "coding" / "claim_level_coding_gemma4_31b_extension.csv",
    },
]


def read_csv(path: Path) -> list[dict]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def collect_ids(rows: list[dict], field: str) -> set[str]:
    return {row[field] for row in rows if row.get(field)}


def split_source_ids(value: str) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(";") if item.strip()]


def source_id_issues(rows: list[dict], valid_text: set[str], valid_xbrl: set[str]) -> list[dict]:
    issues = []
    for row in rows:
        for text_id in split_source_ids(row.get("text_source_ids", "")):
            if text_id.startswith("Text Chunk"):
                if not local_text_chunk_exists(row.get("context_file", ""), text_id):
                    issues.append(
                        {
                            "claim_id": row["claim_id"],
                            "ticker": row["ticker"],
                            "condition": row["condition"],
                            "source_type": "text_rank",
                            "source_id": text_id,
                            "issue": "Local Text Chunk rank not found in cited context file",
                        }
                    )
                continue
            if text_id not in valid_text:
                issues.append(
                    {
                        "claim_id": row["claim_id"],
                        "ticker": row["ticker"],
                        "condition": row["condition"],
                        "source_type": "text",
                        "source_id": text_id,
                        "issue": "Text source ID not found in text_chunks.csv",
                    }
                )
        for xbrl_id in split_source_ids(row.get("xbrl_source_ids", "")):
            if xbrl_id not in valid_xbrl:
                issues.append(
                    {
                        "claim_id": row["claim_id"],
                        "ticker": row["ticker"],
                        "condition": row["condition"],
                        "source_type": "xbrl",
                        "source_id": xbrl_id,
                        "issue": "XBRL source ID not found in fact/path tables",
                    }
                )
    return issues


def local_text_chunk_exists(context_file: str, text_chunk_ref: str) -> bool:
    if not context_file:
        return False
    path = Path(context_file)
    if not path.exists():
        return False
    context = path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"Text Chunk\s+(\d+)", text_chunk_ref)
    if not match:
        return False
    chunk_number = match.group(1)
    return f"[Text Chunk {chunk_number}]" in context


def empty_or_short_outputs(run_label: str) -> list[dict]:
    text_root = PROCESSED / "llm_outputs" / run_label / "text"
    rows = []
    for path in sorted(text_root.glob("*_output.txt")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        word_count = len(re.findall(r"\S+", text))
        if word_count < 25:
            rows.append({"file": str(path).replace("\\", "/"), "word_count": word_count})
    return rows


def run_manifest_status(run_label: str) -> dict[str, int]:
    path = PROCESSED / "llm_outputs" / run_label / "run_manifest.csv"
    if not path.exists():
        return {"missing_manifest": 1}
    counts = {}
    for row in read_csv(path):
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    return counts


def output_count(run_label: str) -> int:
    return len(list((PROCESSED / "llm_outputs" / run_label / "text").glob("*_output.txt")))


def raw_count(run_label: str) -> int:
    return len(list((PROCESSED / "llm_outputs" / run_label / "raw_json").glob("*_raw.json")))


def group_counts(rows: list[dict], fields: list[str]) -> dict[tuple[str, ...], int]:
    counts = {}
    for row in rows:
        key = tuple(row.get(field, "") for field in fields)
        counts[key] = counts.get(key, 0) + 1
    return counts


def markdown_table(headers: list[str], rows: list[list[str]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |"]
    lines.append("|" + "|".join("---" for _ in headers) + "|")
    for row in rows:
        lines.append("| " + " | ".join(str(item) for item in row) + " |")
    return lines


def main() -> int:
    context_rows = read_csv(PROCESSED / "retrieval_contexts" / "context_manifest.csv")
    text_rows = read_csv(PROCESSED / "text_chunks" / "text_chunks.csv")
    fact_rows = read_csv(PROCESSED / "xbrl_facts" / "xbrl_facts.csv")
    path_rows = read_csv(PROCESSED / "xbrl_paths" / "xbrl_paths.csv")

    valid_text = collect_ids(text_rows, "chunk_id")
    valid_xbrl = collect_ids(fact_rows, "fact_id") | collect_ids(path_rows, "path_id")

    lines = ["# LLM Results Validation Log", ""]
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This log validates completeness, parseability, source traceability, and coding separation for the main deep-case and bounded-extension LLM results."
    )
    lines.append("")

    role_counts = group_counts(context_rows, ["sample_role", "condition"])
    lines.append("## Retrieval Context Manifest Check")
    lines.append("")
    lines.extend(
        markdown_table(
            ["Sample Role", "Condition", "Prompt/Context Count"],
            [[role, condition, count] for (role, condition), count in sorted(role_counts.items())],
        )
    )
    lines.append("")

    all_issue_rows = []
    for run in RUNS:
        run_label = run["label"]
        coding_path = run["coding_file"]
        coding_rows = read_csv(coding_path)
        issue_rows = source_id_issues(coding_rows, valid_text, valid_xbrl)
        all_issue_rows.extend({"run_label": run_label, **issue} for issue in issue_rows)
        short_outputs = empty_or_short_outputs(run_label)
        status_counts = run_manifest_status(run_label)

        lines.append(f"## Run Check: `{run_label}`")
        lines.append("")
        lines.extend(
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Expected output files", run["expected_outputs"]],
                    ["Text output files", output_count(run_label)],
                    ["Raw JSON files", raw_count(run_label)],
                    ["Parsed/coded claims", len(coding_rows)],
                    ["Short output files under 25 words", len(short_outputs)],
                    ["Invalid source references", len(issue_rows)],
                    ["Manual-review-required claims", sum(1 for row in coding_rows if row.get("manual_review_required") == "1")],
                ],
            )
        )
        lines.append("")
        lines.append("### Run Manifest Status Counts")
        lines.append("")
        lines.extend(markdown_table(["Status", "Count"], [[status, count] for status, count in sorted(status_counts.items())]))
        lines.append("")

        condition_counts = group_counts(coding_rows, ["ticker", "condition"])
        lines.append("### Claim Counts by Filer and Condition")
        lines.append("")
        lines.extend(
            markdown_table(
                ["Ticker", "Condition", "Claims"],
                [[ticker, condition, count] for (ticker, condition), count in sorted(condition_counts.items())],
            )
        )
        lines.append("")

    lines.append("## Source Reference Validation")
    lines.append("")
    if all_issue_rows:
        lines.append("Invalid source references were found and require manual review.")
        lines.append("")
        lines.extend(
            markdown_table(
                ["Run", "Claim ID", "Ticker", "Condition", "Source Type", "Source ID", "Issue"],
                [
                    [
                        row["run_label"],
                        row["claim_id"],
                        row["ticker"],
                        row["condition"],
                        row["source_type"],
                        row["source_id"],
                        row["issue"],
                    ]
                    for row in all_issue_rows[:50]
                ],
            )
        )
    else:
        lines.append("No invalid global source IDs or local text-chunk rank references were detected in coded source references.")
    lines.append("")

    lines.append("## Validation Verdict")
    lines.append("")
    if all_issue_rows:
        lines.append("Conditional pass with source-reference issues requiring review.")
    else:
        lines.append("Pass for completeness, parseability, run separation, global source-ID traceability, and local text-chunk rank traceability.")
    lines.append("")
    lines.append("## Important Limitation")
    lines.append("")
    lines.append(
        "This validation checks data integrity and traceability. It does not validate audit-valid or integrated correctness as expert audit judgments. Those scores remain preliminary author coding until audit-domain review is completed."
    )

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
