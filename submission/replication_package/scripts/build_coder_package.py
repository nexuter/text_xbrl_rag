import csv
import shutil
from pathlib import Path


ROOT = Path(".")
CODING_DIR = ROOT / "data" / "processed" / "coding"
CODER_DIR = ROOT / "coder"

SAMPLE = CODING_DIR / "independent_coding_sample.csv"
PROTOCOL = CODING_DIR / "independent_coding_protocol.md"
RELIABILITY_TEMPLATE = CODING_DIR / "intercoder_reliability_summary.md"

FORM_CODE_COLUMNS = [
    "coder_id",
    "claim_segmentation_agreement",
    "claim_kind_code",
    "evidence_use_type_code",
    "text_supported_code",
    "graph_valid_code",
    "integrated_code",
    "audit_boundary_note",
    "confidence_code",
    "coder_notes",
]

CODER_SAMPLE_COLUMNS = [
    "global_claim_id",
    "source_archive",
    "claim_id",
    "ticker",
    "company",
    "sample_role",
    "construct",
    "condition",
    "condition_label",
    "claim_text",
    "claim_kind",
    "has_text_source",
    "has_xbrl_source",
    "text_source_ids",
    "xbrl_source_ids",
    "text_supported_prelim",
    "graph_valid_prelim",
    "audit_valid_prelim",
    "integrated_prelim",
    "failure_mode_prelim",
    "manual_review_required",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def safe_read(path_text: str) -> str:
    if not path_text:
        return ""
    path = ROOT / path_text
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def make_evidence_packet(sample_rows: list[dict[str, str]]) -> None:
    fields = [
        "global_claim_id",
        "ticker",
        "company",
        "sample_role",
        "construct",
        "condition",
        "claim_text",
        "text_source_ids",
        "xbrl_source_ids",
        "retrieval_context_text",
        "llm_output_text",
    ]
    rows = []
    for row in sample_rows:
        rows.append(
            {
                "global_claim_id": row["global_claim_id"],
                "ticker": row["ticker"],
                "company": row["company"],
                "sample_role": row["sample_role"],
                "construct": row["construct"],
                "condition": row["condition"],
                "claim_text": row["claim_text"],
                "text_source_ids": row["text_source_ids"],
                "xbrl_source_ids": row["xbrl_source_ids"],
                "retrieval_context_text": safe_read(row["context_file"]),
                "llm_output_text": safe_read(row["output_file"]),
            }
        )
    write_csv(CODER_DIR / "claim_evidence_packet.csv", rows, fields)


def make_empty_template(sample_rows: list[dict[str, str]]) -> None:
    fields = [
        "global_claim_id",
        "ticker",
        "company",
        "sample_role",
        "construct",
        "condition",
        "claim_text",
        "text_source_ids",
        "xbrl_source_ids",
    ] + FORM_CODE_COLUMNS
    rows = []
    for row in sample_rows:
        out = {field: row.get(field, "") for field in fields}
        for field in FORM_CODE_COLUMNS:
            out[field] = ""
        rows.append(out)
    write_csv(CODER_DIR / "coder_coding_form_template.csv", rows, fields)


def make_results_template() -> None:
    fields = [
        "global_claim_id",
        "ticker",
        "company",
        "sample_role",
        "construct",
        "condition",
        "claim_text",
        "text_source_ids",
        "xbrl_source_ids",
    ] + FORM_CODE_COLUMNS + ["reconciled_code", "reconciliation_notes"]
    write_csv(CODER_DIR / "independent_coding_results_template.csv", [], fields)


def main() -> int:
    CODER_DIR.mkdir(exist_ok=True)

    sample_rows = read_csv(SAMPLE)

    shutil.copy2(PROTOCOL, CODER_DIR / "CODING_PROTOCOL.md")
    shutil.copy2(RELIABILITY_TEMPLATE, CODER_DIR / "intercoder_reliability_summary_template.md")

    write_csv(
        CODER_DIR / "independent_coding_sample.csv",
        [{field: row.get(field, "") for field in CODER_SAMPLE_COLUMNS} for row in sample_rows],
        CODER_SAMPLE_COLUMNS,
    )
    make_evidence_packet(sample_rows)
    make_empty_template(sample_rows)
    make_results_template()

    print(f"Built coder package at {CODER_DIR.resolve()}")
    print(f"Claims included: {len(sample_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
