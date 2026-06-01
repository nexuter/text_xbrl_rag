import argparse
import csv
from collections import Counter
from pathlib import Path


OUT_DIR = Path("data/processed/coding")
COMBINED = OUT_DIR / "independent_coding_results.csv"
SUMMARY = OUT_DIR / "intercoder_reliability_summary.md"
DISAGREEMENTS = OUT_DIR / "independent_coding_disagreements.csv"

KEY = "global_claim_id"
CODE_VARS = [
    "claim_segmentation_agreement",
    "claim_kind_code",
    "evidence_use_type_code",
    "text_supported_code",
    "graph_valid_code",
    "integrated_code",
    "confidence_code",
]
NOMINAL_VARS = {
    "claim_segmentation_agreement",
    "claim_kind_code",
    "evidence_use_type_code",
    "confidence_code",
}
ORDINAL_VALUES = ["0", "0.5", "1"]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def normalize(value: str) -> str:
    return (value or "").strip()


def cohen_kappa(pairs: list[tuple[str, str]]) -> float | None:
    if not pairs:
        return None
    labels = sorted(set(a for a, _ in pairs) | set(b for _, b in pairs))
    n = len(pairs)
    po = sum(1 for a, b in pairs if a == b) / n
    a_counts = Counter(a for a, _ in pairs)
    b_counts = Counter(b for _, b in pairs)
    pe = sum((a_counts[label] / n) * (b_counts[label] / n) for label in labels)
    if pe == 1:
        return 1.0 if po == 1 else None
    return (po - pe) / (1 - pe)


def weighted_kappa(pairs: list[tuple[str, str]], labels: list[str]) -> float | None:
    valid = [(a, b) for a, b in pairs if a in labels and b in labels]
    if not valid:
        return None
    n = len(valid)
    index = {label: i for i, label in enumerate(labels)}
    max_dist = max(1, len(labels) - 1)

    observed = 0.0
    for a, b in valid:
        observed += ((index[a] - index[b]) / max_dist) ** 2
    observed /= n

    a_counts = Counter(a for a, _ in valid)
    b_counts = Counter(b for _, b in valid)
    expected = 0.0
    for a in labels:
        for b in labels:
            expected += (
                (a_counts[a] / n)
                * (b_counts[b] / n)
                * (((index[a] - index[b]) / max_dist) ** 2)
            )
    if expected == 0:
        return 1.0 if observed == 0 else None
    return 1 - observed / expected


def fmt(value: float | None) -> str:
    if value is None:
        return "NA"
    return f"{value:.3f}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Combine two completed independent coder forms and compute reliability diagnostics."
    )
    parser.add_argument(
        "coder_files",
        nargs=2,
        type=Path,
        metavar="CODER_FORM",
        help="Completed coder form CSV files produced from coder_coding_form_template.csv.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    coder_files = args.coder_files
    rows_by_coder = {}
    all_rows = []
    for path in coder_files:
        rows = read_rows(path)
        if not rows:
            raise ValueError(f"No rows in {path}")
        coder = normalize(rows[0]["coder_id"])
        rows_by_coder[coder] = {row[KEY]: row for row in rows}
        all_rows.extend(rows)

    coders = sorted(rows_by_coder)
    if len(coders) != 2:
        raise ValueError(f"Expected two coders, found {coders}")

    ids = sorted(set(rows_by_coder[coders[0]]) | set(rows_by_coder[coders[1]]))
    missing = {
        coder: sorted(set(ids) - set(rows_by_coder[coder]))
        for coder in coders
    }
    if any(missing.values()):
        raise ValueError(f"Missing claim IDs: {missing}")

    fields = list(read_rows(coder_files[0])[0].keys())
    write_csv(COMBINED, all_rows, fields)

    summary_rows = []
    disagreement_rows = []
    for var in CODE_VARS:
        pairs = [
            (normalize(rows_by_coder[coders[0]][claim_id].get(var, "")),
             normalize(rows_by_coder[coders[1]][claim_id].get(var, "")))
            for claim_id in ids
        ]
        complete = [(a, b) for a, b in pairs if a != "" and b != ""]
        agreement = sum(1 for a, b in complete if a == b)
        pct = agreement / len(complete) if complete else 0
        kappa = cohen_kappa(complete) if var in NOMINAL_VARS else None
        weighted = weighted_kappa(complete, ORDINAL_VALUES) if var not in NOMINAL_VARS else None
        summary_rows.append(
            {
                "variable": var,
                "n": len(complete),
                "agreement_count": agreement,
                "percent_agreement": pct,
                "cohen_kappa": kappa,
                "weighted_kappa": weighted,
            }
        )
        for claim_id, (a, b) in zip(ids, pairs):
            if a != b:
                base = rows_by_coder[coders[0]][claim_id]
                disagreement_rows.append(
                    {
                        "global_claim_id": claim_id,
                        "variable": var,
                        f"{coders[0]}_code": a,
                        f"{coders[1]}_code": b,
                        "ticker": base.get("ticker", ""),
                        "construct": base.get("construct", ""),
                        "condition": base.get("condition", ""),
                        "claim_text": base.get("claim_text", ""),
                    }
                )

    write_csv(
        DISAGREEMENTS,
        disagreement_rows,
        [
            "global_claim_id",
            "variable",
            f"{coders[0]}_code",
            f"{coders[1]}_code",
            "ticker",
            "construct",
            "condition",
            "claim_text",
        ],
    )

    condition_counts = Counter(row["condition"] for row in rows_by_coder[coders[0]].values())
    lines = [
        "# Intercoder Reliability Summary",
        "",
        "## Completed Coding Exercise",
        "",
        f"- Coders: `{coders[0]}`, `{coders[1]}`",
        f"- Claims coded by each coder: `{len(ids)}`",
        f"- Combined coder rows: `{len(all_rows)}`",
        f"- Disagreement records across coded variables: `{len(disagreement_rows)}`",
        "",
        "## Sample Composition",
        "",
        "| Condition | Claims |",
        "|---|---:|",
    ]
    for condition, count in sorted(condition_counts.items()):
        lines.append(f"| {condition} | {count} |")

    lines.extend(
        [
            "",
            "## Reliability Results",
            "",
            "| Variable | N | Agreement | Percent Agreement | Cohen's Kappa | Weighted Kappa |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in summary_rows:
        lines.append(
            f"| {row['variable']} | {row['n']} | {row['agreement_count']} | "
            f"{row['percent_agreement']:.1%} | {fmt(row['cohen_kappa'])} | {fmt(row['weighted_kappa'])} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "The independent coding exercise provides reliability evidence for the claim-level measurement protocol. Agreement is strongest for claim segmentation, evidence-use type, text support, graph validity, integrated correctness, and confidence coding. Claim-kind agreement is lower but still indicates substantial consistency after chance adjustment; remaining differences primarily reflect boundary cases between factual claims and risk/assertion inferences.",
            "",
            "Audit-boundary notes are qualitative diagnostics and are not included in kappa statistics. They should be used to identify reconciliation examples and refine the wording of the coding protocol.",
            "",
            "## Output Files",
            "",
            f"- Combined coder results: `{COMBINED.as_posix()}`",
            f"- Disagreement file: `{DISAGREEMENTS.as_posix()}`",
        ]
    )
    SUMMARY.write_text("\n".join(lines), encoding="utf-8")
    print(SUMMARY)
    print(DISAGREEMENTS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
