import csv
from collections import Counter, defaultdict
from pathlib import Path


INPUT_FILES = [
    Path("data/processed/coding/claim_level_coding_gemma4_31b.csv"),
    Path("data/processed/coding/claim_level_coding_gemma4_31b_extension.csv"),
]
OUT_DIR = Path("data/processed/coding")


def read_rows() -> list[dict]:
    rows = []
    for path in INPUT_FILES:
        with path.open("r", newline="", encoding="utf-8") as handle:
            rows.extend(csv.DictReader(handle))
    return rows


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def mechanism(row: dict) -> tuple[str, str]:
    has_text = row.get("has_text_source") == "1"
    has_xbrl = row.get("has_xbrl_source") == "1"
    integrated = row.get("integrated_prelim") == "1"
    if integrated and has_text and has_xbrl:
        return (
            "integrated_text_xbrl_bridge",
            "Claim uses both text and XBRL evidence with an inferential bridge.",
        )
    if has_text and not has_xbrl:
        return (
            "text_only_within_hybrid",
            "Hybrid prompt was available, but the claim used narrative text only.",
        )
    if has_xbrl and not has_text:
        return (
            "xbrl_only_within_hybrid",
            "Hybrid prompt was available, but the claim used XBRL facts or paths only.",
        )
    if has_text and has_xbrl:
        return (
            "juxtaposed_without_bridge",
            "Claim cited both evidence types but did not connect them in one inferential bridge.",
        )
    return (
        "no_retrieved_source_used",
        "Claim did not use a traceable retrieved source despite hybrid context availability.",
    )


def pct(part: int, total: int) -> str:
    return f"{part / total * 100:.1f}%" if total else "0.0%"


def main() -> None:
    rows = [row for row in read_rows() if row.get("condition") == "hybrid"]
    detail_rows = []
    for row in rows:
        code, definition = mechanism(row)
        detail_rows.append(
            {
                "claim_id": row["claim_id"],
                "ticker": row["ticker"],
                "company": row["company"],
                "sample_role": row["sample_role"],
                "construct": row["construct"],
                "claim_kind": row["claim_kind"],
                "mechanism": code,
                "mechanism_definition": definition,
                "has_text_source": row["has_text_source"],
                "has_xbrl_source": row["has_xbrl_source"],
                "integrated_prelim": row["integrated_prelim"],
                "text_source_ids": row["text_source_ids"],
                "xbrl_source_ids": row["xbrl_source_ids"],
                "claim_text": row["claim_text"],
            }
        )

    mechanism_counts = Counter(row["mechanism"] for row in detail_rows)
    summary_rows = []
    for code, count in sorted(mechanism_counts.items()):
        definition = next(row["mechanism_definition"] for row in detail_rows if row["mechanism"] == code)
        summary_rows.append(
            {
                "mechanism": code,
                "definition": definition,
                "claims": count,
                "share_of_hybrid_claims": pct(count, len(detail_rows)),
            }
        )

    construct_counts = defaultdict(Counter)
    for row in detail_rows:
        construct_counts[row["construct"]][row["mechanism"]] += 1
    construct_rows = []
    mechanisms = sorted(mechanism_counts)
    for construct, counts in sorted(construct_counts.items()):
        total = sum(counts.values())
        out = {"construct": construct, "hybrid_claims": total}
        for code in mechanisms:
            out[code] = counts.get(code, 0)
        construct_rows.append(out)

    write_csv(
        OUT_DIR / "hybrid_integration_mechanisms.csv",
        detail_rows,
        [
            "claim_id",
            "ticker",
            "company",
            "sample_role",
            "construct",
            "claim_kind",
            "mechanism",
            "mechanism_definition",
            "has_text_source",
            "has_xbrl_source",
            "integrated_prelim",
            "text_source_ids",
            "xbrl_source_ids",
            "claim_text",
        ],
    )
    write_csv(
        OUT_DIR / "hybrid_integration_mechanism_summary.csv",
        summary_rows,
        ["mechanism", "definition", "claims", "share_of_hybrid_claims"],
    )
    write_csv(
        OUT_DIR / "hybrid_integration_mechanism_by_construct.csv",
        construct_rows,
        ["construct", "hybrid_claims", *mechanisms],
    )

    lines = [
        "# Hybrid Integration Mechanism Summary",
        "",
        "This diagnostic decomposes hybrid-condition claims by the evidence type actually used in each claim.",
        "It is a mechanism diagnostic for the paper's integration-failure argument, not a model-performance result.",
        "",
        f"Hybrid claims analyzed: {len(detail_rows)}",
        "",
        "| Mechanism | Claims | Share | Interpretation |",
        "|---|---:|---:|---|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['mechanism']} | {row['claims']} | {row['share_of_hybrid_claims']} | {row['definition']} |"
        )
    lines.extend(
        [
            "",
            "The mechanism table shows that hybrid non-integration is not a single phenomenon.",
            "In this sample, non-integrated hybrid claims primarily arise because the model uses either the narrative layer or the XBRL layer, rather than because it cites both layers but fails to connect them.",
        ]
    )
    (OUT_DIR / "hybrid_integration_mechanism_summary.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote hybrid integration mechanism diagnostics for {len(detail_rows)} hybrid claims.")


if __name__ == "__main__":
    main()
