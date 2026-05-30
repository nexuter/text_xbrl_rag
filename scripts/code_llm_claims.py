import csv
import argparse
import re
from pathlib import Path


CONTEXT_MANIFEST = Path("data/processed/retrieval_contexts/context_manifest.csv")
OUTPUT_ROOT = Path("data/processed/coding")


def read_csv(path: Path) -> list[dict]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def stem(row: dict) -> str:
    return f"{row['ticker'].lower()}_{row['construct']}_{row['condition']}"


def split_filter(value: str) -> set[str]:
    if not value:
        return set()
    return {item.strip() for item in value.split(",") if item.strip()}


def filter_manifest_rows(rows: list[dict], args: argparse.Namespace) -> list[dict]:
    filters = {
        "sample_role": split_filter(args.roles),
        "ticker": split_filter(args.tickers),
        "construct": split_filter(args.constructs),
        "condition": split_filter(args.conditions),
    }
    selected = []
    for row in rows:
        keep = True
        for field, allowed in filters.items():
            if allowed and row.get(field, "") not in allowed:
                keep = False
                break
        if keep:
            selected.append(row)
    return selected


def parse_claim_blocks(text: str) -> list[dict]:
    stripped = text.strip()
    if not stripped:
        return []

    if "- Claim:" not in stripped and not re.search(r"(?im)^\s*claim\s*:", stripped):
        return [
            {
                "claim_text": stripped,
                "claim_type": "insufficient-context statement",
                "support_used": "",
                "inferential_bridge": "",
                "limitation": stripped,
                "raw_block": stripped,
            }
        ]

    starts = [match.start() for match in re.finditer(r"(?im)^\s*-\s*Claim\s*:", stripped)]
    if not starts:
        starts = [match.start() for match in re.finditer(r"(?im)^\s*Claim\s*:", stripped)]
    starts.append(len(stripped))

    blocks = []
    for index in range(len(starts) - 1):
        block = stripped[starts[index] : starts[index + 1]].strip()
        if block:
            blocks.append(parse_claim_block(block))
    return blocks


def parse_claim_block(block: str) -> dict:
    lines = [line.rstrip() for line in block.splitlines() if line.strip()]
    claim_lines = []
    fields = {
        "claim_type": "",
        "support_used": "",
        "inferential_bridge": "",
        "limitation": "",
    }
    current_field = "claim_text"

    for line in lines:
        normalized = line.strip()
        normalized = re.sub(r"^\s*[-*]\s*", "", normalized)
        lower = normalized.lower()

        if lower.startswith("claim:"):
            value = normalized.split(":", 1)[1].strip()
            if value:
                claim_lines.append(value)
            current_field = "claim_text"
        elif lower.startswith("claim type:"):
            fields["claim_type"] = normalized.split(":", 1)[1].strip()
            current_field = "claim_type"
        elif lower.startswith("support used:"):
            fields["support_used"] = normalized.split(":", 1)[1].strip()
            current_field = "support_used"
        elif lower.startswith("inferential bridge:"):
            fields["inferential_bridge"] = normalized.split(":", 1)[1].strip()
            current_field = "inferential_bridge"
        elif lower.startswith("limitation:"):
            fields["limitation"] = normalized.split(":", 1)[1].strip()
            current_field = "limitation"
        else:
            if current_field == "claim_text":
                claim_lines.append(normalized)
            elif current_field in fields:
                fields[current_field] = " ".join([fields[current_field], normalized]).strip()

    return {
        "claim_text": " ".join(claim_lines).strip(),
        "claim_type": fields["claim_type"],
        "support_used": fields["support_used"],
        "inferential_bridge": fields["inferential_bridge"],
        "limitation": fields["limitation"],
        "raw_block": block,
    }


def detect_sources(text: str) -> tuple[str, str, str, str]:
    text_refs = sorted(set(re.findall(r"(?:Text Chunk\s+\d+|T-[A-Z]+-[A-Z_]+-\d+)", text)))
    fact_refs = sorted(set(re.findall(r"(?<![A-Z0-9_-])F-[A-Z]+-\d+", text)))
    path_refs = sorted(set(re.findall(r"(?<![A-Z0-9_-])X-[A-Z]+-\d+", text)))
    xbrl_refs = sorted(set(fact_refs + path_refs))
    has_text = "1" if text_refs else "0"
    has_xbrl = "1" if xbrl_refs else "0"
    return has_text, has_xbrl, "; ".join(text_refs), "; ".join(xbrl_refs)


def normalize_claim_type(claim_type: str, claim_text: str) -> str:
    compact = f"{claim_type} {claim_text}".lower()
    if "insufficient" in compact:
        return "insufficient_context"
    if "factual" in compact:
        return "factual"
    if "risk" in compact or "assertion" in compact or "mapping" in compact:
        return "risk_or_assertion_mapping"
    return "other"


def unsupported_conclusion(text: str) -> bool:
    compact = text.lower()
    red_flags = [
        "misstatement exists",
        "is misstated",
        "material misstatement exists",
        "proves",
        "confirms no misstatement",
        "sufficient audit evidence",
    ]
    return any(flag in compact for flag in red_flags)


def code_text_supported(condition: str, claim_kind: str, has_text: str, support: str) -> tuple[str, str]:
    if condition == "llm_only":
        return "NA", "No retrieved text context in diagnostic baseline."
    if condition == "xbrl":
        return "NA", "Text support is not assessable in XBRL-only condition."
    if has_text == "1":
        score = "1" if claim_kind == "factual" else "0.5"
        rationale = "Claim cites retrieved text; inferential claims receive partial text-support because audit implication is not directly stated."
        return score, rationale
    if support:
        return "0", "Support statement does not cite retrieved text."
    return "NA", "No specific text support stated."


def code_graph_valid(condition: str, claim_kind: str, has_xbrl: str, support: str) -> tuple[str, str]:
    if condition == "llm_only":
        return "NA", "No retrieved XBRL context in diagnostic baseline."
    if condition == "text":
        return "NA", "Graph validity is not assessable in text-only condition."
    if has_xbrl == "1":
        score = "1" if claim_kind == "factual" else "0.5"
        rationale = "Claim cites retrieved XBRL facts or relation paths; inferential audit implications are not fully graph-valid by themselves."
        return score, rationale
    if condition == "hybrid":
        return "NA", "This hybrid claim does not cite an XBRL fact or path; graph validity is not separately assessed for this claim."
    if support:
        return "0", "Support statement does not cite retrieved XBRL fact or path identifiers."
    return "NA", "No specific XBRL support stated."


def code_audit_valid(claim_kind: str, claim_text: str, bridge: str, limitation: str) -> tuple[str, str]:
    if claim_kind == "insufficient_context":
        return "1", "Appropriately states that context is insufficient."
    if unsupported_conclusion(claim_text):
        return "0", "Claim appears to convert a risk cue into an unsupported audit conclusion."
    if claim_kind == "factual":
        return "1", "Factual claim is bounded by source or period limitations."
    if claim_kind == "risk_or_assertion_mapping":
        if bridge and limitation:
            return "1", "Risk or assertion-mapping claim is qualified and states an inferential bridge."
        if limitation:
            return "0.5", "Risk or assertion-mapping claim is qualified but lacks an explicit inferential bridge."
        return "0.5", "Risk or assertion-mapping claim is plausible but under-qualified."
    return "0.5", "Other audit-relevant claim requires manual review."


def code_integrated(condition: str, has_text: str, has_xbrl: str, audit_score: str) -> tuple[str, str]:
    if condition != "hybrid":
        return "NA", "Integrated correctness is primarily assessed for hybrid retrieval in this demonstration."
    if has_text == "1" and has_xbrl == "1" and audit_score == "1":
        return "1", "Claim integrates text, XBRL, and qualified audit reasoning."
    if (has_text == "1" or has_xbrl == "1") and audit_score in {"1", "0.5"}:
        return "0.5", "Hybrid context is available, but this claim uses only one evidence layer or only partially reconciles layers."
    return "0", "Hybrid claim lacks traceable evidence-layer integration."


def assign_failure_mode(condition: str, claim_kind: str, has_text: str, has_xbrl: str, audit_score: str, graph_score: str) -> str:
    if claim_kind == "insufficient_context":
        return "none"
    if audit_score == "0":
        return "source overreach"
    if graph_score == "0":
        return "relation hallucination"
    if condition == "hybrid" and not (has_text == "1" and has_xbrl == "1"):
        return "integration failure"
    if has_text == "0" and has_xbrl == "0":
        return "attribution failure"
    if audit_score == "0.5":
        return "source overreach"
    return "none"


def build_claim_rows(args: argparse.Namespace) -> list[dict]:
    manifest_rows = filter_manifest_rows(read_csv(CONTEXT_MANIFEST), args)
    run_root = Path("data/processed/llm_outputs") / args.run_label
    rows = []
    claim_counter = 1

    for manifest_row in manifest_rows:
        output_path = run_root / "text" / f"{stem(manifest_row)}_output.txt"
        if not output_path.exists():
            continue
        output_text = output_path.read_text(encoding="utf-8")
        claims = parse_claim_blocks(output_text)

        for local_index, claim in enumerate(claims, start=1):
            combined_sources = " ".join([claim["support_used"], claim["claim_text"], claim["raw_block"]])
            has_text, has_xbrl, text_ids, xbrl_ids = detect_sources(combined_sources)
            claim_kind = normalize_claim_type(claim["claim_type"], claim["claim_text"])
            text_score, text_rationale = code_text_supported(
                manifest_row["condition"], claim_kind, has_text, claim["support_used"]
            )
            graph_score, graph_rationale = code_graph_valid(
                manifest_row["condition"], claim_kind, has_xbrl, claim["support_used"]
            )
            audit_score, audit_rationale = code_audit_valid(
                claim_kind, claim["claim_text"], claim["inferential_bridge"], claim["limitation"]
            )
            integrated_score, integrated_rationale = code_integrated(
                manifest_row["condition"], has_text, has_xbrl, audit_score
            )
            failure_mode = assign_failure_mode(
                manifest_row["condition"], claim_kind, has_text, has_xbrl, audit_score, graph_score
            )

            rows.append(
                {
                    "claim_id": f"C{claim_counter:03d}",
                    "local_claim_index": local_index,
                    "ticker": manifest_row["ticker"],
                    "company": manifest_row["company"],
                    "sample_role": manifest_row.get("sample_role", ""),
                    "construct": manifest_row["construct"],
                    "condition": manifest_row["condition"],
                    "condition_label": manifest_row["condition_label"],
                    "model": "gemma4:31b",
                    "run_label": args.run_label,
                    "output_file": str(output_path).replace("\\", "/"),
                    "context_file": manifest_row["context_file"],
                    "prompt_file": manifest_row["prompt_file"],
                    "claim_text": claim["claim_text"],
                    "claim_type_raw": claim["claim_type"],
                    "claim_kind": claim_kind,
                    "support_used": claim["support_used"],
                    "inferential_bridge": claim["inferential_bridge"],
                    "limitation": claim["limitation"],
                    "has_text_source": has_text,
                    "has_xbrl_source": has_xbrl,
                    "text_source_ids": text_ids,
                    "xbrl_source_ids": xbrl_ids,
                    "text_supported_prelim": text_score,
                    "text_supported_rationale": text_rationale,
                    "graph_valid_prelim": graph_score,
                    "graph_valid_rationale": graph_rationale,
                    "audit_valid_prelim": audit_score,
                    "audit_valid_rationale": audit_rationale,
                    "integrated_prelim": integrated_score,
                    "integrated_rationale": integrated_rationale,
                    "failure_mode_prelim": failure_mode,
                    "manual_review_required": "1",
                    "coding_status": "preliminary_author_code",
                    "raw_claim_block": claim["raw_block"],
                }
            )
            claim_counter += 1
    return rows


def numeric_score(value: str) -> float | None:
    if value == "NA" or value == "":
        return None
    return float(value)


def summarize(rows: list[dict]) -> list[dict]:
    grouped = {}
    layers = [
        "text_supported_prelim",
        "graph_valid_prelim",
        "audit_valid_prelim",
        "integrated_prelim",
    ]
    for row in rows:
        key = (row["condition"], row["construct"])
        grouped.setdefault(key, []).append(row)

    summary_rows = []
    for (condition, construct), group in sorted(grouped.items()):
        summary = {
            "condition": condition,
            "construct": construct,
            "claims": len(group),
            "factual_claims": sum(1 for row in group if row["claim_kind"] == "factual"),
            "risk_or_assertion_claims": sum(1 for row in group if row["claim_kind"] == "risk_or_assertion_mapping"),
            "insufficient_context_claims": sum(1 for row in group if row["claim_kind"] == "insufficient_context"),
        }
        for layer in layers:
            values = [numeric_score(row[layer]) for row in group]
            values = [value for value in values if value is not None]
            summary[f"{layer}_mean"] = f"{sum(values) / len(values):.2f}" if values else "NA"
            summary[f"{layer}_n"] = len(values)
        summary_rows.append(summary)
    return summary_rows


def build_inference_shift(rows: list[dict]) -> list[dict]:
    patterns = []
    for ticker in sorted(set(row["ticker"] for row in rows)):
        for construct in sorted(set(row["construct"] for row in rows if row["ticker"] == ticker)):
            group = [row for row in rows if row["ticker"] == ticker and row["construct"] == construct]
            by_condition = {}
            for condition in ["llm_only", "text", "xbrl", "hybrid"]:
                subset = [row for row in group if row["condition"] == condition]
                by_condition[condition] = {
                    "claims": len(subset),
                    "text_refs": sum(1 for row in subset if row["has_text_source"] == "1"),
                    "xbrl_refs": sum(1 for row in subset if row["has_xbrl_source"] == "1"),
                    "audit_valid_1": sum(1 for row in subset if row["audit_valid_prelim"] == "1"),
                    "integrated_1": sum(1 for row in subset if row["integrated_prelim"] == "1"),
                    "failure_modes": sorted(set(row["failure_mode_prelim"] for row in subset if row["failure_mode_prelim"] != "none")),
                }

            patterns.append(
                {
                    "ticker": ticker,
                    "construct": construct,
                    "naive_reading_risk": "A reader might compare conditions by output fluency or number of plausible audit claims.",
                    "protocol_based_inference": (
                        f"LLM-only produced {by_condition['llm_only']['claims']} context-limited claim(s); "
                        f"text retrieval generated {by_condition['text']['text_refs']} text-traceable claim(s); "
                        f"XBRL retrieval generated {by_condition['xbrl']['xbrl_refs']} XBRL-traceable claim(s); "
                        f"hybrid retrieval generated {by_condition['hybrid']['integrated_1']} preliminarily integrated claim(s)."
                    ),
                    "main_failure_modes_observed": "; ".join(
                        sorted(
                            set(
                                mode
                                for condition in by_condition.values()
                                for mode in condition["failure_modes"]
                            )
                        )
                    )
                    or "none",
                    "reviewer_note": "Preliminary coding; audit-valid and integrated scores require expert review before manuscript claims.",
                }
            )
    return patterns


def build_markdown_summary(rows: list[dict], summary_rows: list[dict], run_label: str, output_prefix: str) -> str:
    lines = ["# Phase 6 Claim-Level Preliminary Coding Summary", ""]
    lines.append("## Scope")
    lines.append("")
    lines.append(f"- Run label: `{run_label}`")
    lines.append("- Model: `gemma4:31b`")
    lines.append(f"- Segmented claims: `{len(rows)}`")
    lines.append("- Coding status: `preliminary_author_code`")
    lines.append("")
    lines.append("## Important Limitation")
    lines.append("")
    lines.append(
        "The scores are preliminary author codes generated from the structured LLM outputs. "
        "Audit-valid and integrated correctness require expert review before being treated as manuscript evidence."
    )
    lines.append("")
    lines.append("## Summary by Condition and Construct")
    lines.append("")
    lines.append("| Condition | Construct | Claims | Factual | Risk/Assertion | Insufficient Context | Text Mean | Graph Mean | Audit Mean | Integrated Mean |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for row in summary_rows:
        lines.append(
            f"| {row['condition']} | {row['construct']} | {row['claims']} | "
            f"{row['factual_claims']} | {row['risk_or_assertion_claims']} | {row['insufficient_context_claims']} | "
            f"{row['text_supported_prelim_mean']} | {row['graph_valid_prelim_mean']} | "
            f"{row['audit_valid_prelim_mean']} | {row['integrated_prelim_mean']} |"
        )
    lines.append("")
    lines.append("## Output Files")
    lines.append("")
    lines.append(f"- `data/processed/coding/claim_level_coding_{output_prefix}.csv`")
    lines.append(f"- `data/processed/coding/coding_summary_by_condition_{output_prefix}.csv`")
    lines.append(f"- `data/processed/coding/inference_shift_table_prelim_{output_prefix}.csv`")
    lines.append(f"- `data/processed/coding/failure_mode_examples_prelim_{output_prefix}.csv`")
    return "\n".join(lines)


def build_failure_examples(rows: list[dict]) -> list[dict]:
    examples = []
    for row in rows:
        if row["failure_mode_prelim"] == "none":
            continue
        examples.append(
            {
                "failure_mode": row["failure_mode_prelim"],
                "claim_id": row["claim_id"],
                "ticker": row["ticker"],
                "construct": row["construct"],
                "condition": row["condition"],
                "claim_text": row["claim_text"],
                "support_used": row["support_used"],
                "text_source_ids": row["text_source_ids"],
                "xbrl_source_ids": row["xbrl_source_ids"],
                "preliminary_interpretation": (
                    "Hybrid output uses only one evidence layer for this claim, so it may be useful but does not "
                    "demonstrate narrative-XBRL integration."
                    if row["failure_mode_prelim"] == "integration failure"
                    else "Claim requires manual failure-mode review."
                ),
                "manual_review_required": "1",
            }
        )
    return examples


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse and preliminarily code LLM output claims.")
    parser.add_argument("--run-label", default="gemma4_31b_full")
    parser.add_argument("--output-prefix", default="gemma4_31b")
    parser.add_argument("--roles", default="", help="Comma-separated sample_role filter.")
    parser.add_argument("--tickers", default="", help="Comma-separated ticker filter.")
    parser.add_argument("--constructs", default="", help="Comma-separated construct filter.")
    parser.add_argument("--conditions", default="", help="Comma-separated condition filter.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rows = build_claim_rows(args)
    if not rows:
        raise SystemExit("No claims were parsed. Check the run label and output files.")

    fieldnames = list(rows[0].keys())
    write_csv(OUTPUT_ROOT / f"claim_level_coding_{args.output_prefix}.csv", rows, fieldnames)

    summary_rows = summarize(rows)
    write_csv(OUTPUT_ROOT / f"coding_summary_by_condition_{args.output_prefix}.csv", summary_rows, list(summary_rows[0].keys()))

    inference_rows = build_inference_shift(rows)
    write_csv(OUTPUT_ROOT / f"inference_shift_table_prelim_{args.output_prefix}.csv", inference_rows, list(inference_rows[0].keys()))

    failure_examples = build_failure_examples(rows)
    if failure_examples:
        write_csv(
            OUTPUT_ROOT / f"failure_mode_examples_prelim_{args.output_prefix}.csv",
            failure_examples,
            list(failure_examples[0].keys()),
        )

    write_text(
        OUTPUT_ROOT / f"claim_coding_summary_{args.output_prefix}.md",
        build_markdown_summary(rows, summary_rows, args.run_label, args.output_prefix),
    )
    print(f"Parsed and preliminarily coded {len(rows)} claims.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
