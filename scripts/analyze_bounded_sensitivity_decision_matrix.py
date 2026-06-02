import csv
import statistics
from pathlib import Path


ROOT = Path(".")
PROCESSED = ROOT / "data/processed"
SENS_DIR = PROCESSED / "sensitivity"
CONTEXT_DIAG = PROCESSED / "retrieval_contexts" / "context_volume_diagnostics.csv"
PERTURB_DIAG = SENS_DIR / "retrieval_perturbation_diagnostics.csv"
CELL_OUT = SENS_DIR / "bounded_sensitivity_decision_matrix_by_cell.csv"
VARIANT_OUT = SENS_DIR / "bounded_sensitivity_variant_decisions.csv"
SUMMARY_OUT = SENS_DIR / "bounded_sensitivity_decision_summary.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def fmt(value: float) -> str:
    return f"{value:.3f}"


def mean(values: list[float]) -> float:
    return statistics.mean(values) if values else 0.0


def median(values: list[float]) -> float:
    return statistics.median(values) if values else 0.0


def decision_band(jaccard: float) -> str:
    if jaccard < 0.60:
        return "material_source_environment_change"
    if jaccard < 0.75:
        return "moderate_source_environment_change"
    return "bounded_source_environment_change"


def attention_band(imbalance_ratio: float, fact_only_jaccard: float, min_jaccard: float) -> str:
    if imbalance_ratio >= 1.50 or fact_only_jaccard < 0.60:
        return "high_separability_attention"
    if imbalance_ratio >= 1.25 or min_jaccard < 0.70:
        return "moderate_separability_attention"
    return "low_separability_attention"


def main() -> int:
    context_rows = read_csv(CONTEXT_DIAG)
    perturb_rows = read_csv(PERTURB_DIAG)

    hybrid_ratios: dict[tuple[str, str], float] = {}
    for row in context_rows:
        if row["condition"] != "hybrid":
            continue
        ratio = row.get("hybrid_text_xbrl_word_imbalance_ratio", "")
        hybrid_ratios[(row["ticker"], row["construct"])] = float(ratio) if ratio else 0.0

    by_cell: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in perturb_rows:
        by_cell.setdefault((row["ticker"], row["construct"]), []).append(row)

    cell_rows: list[dict[str, object]] = []
    for (ticker, construct), rows in sorted(by_cell.items()):
        jaccards = [float(row["jaccard"]) for row in rows]
        fact_only_rows = [row for row in rows if row["variant"] == "xbrl_fact_only"]
        fact_only_jaccard = float(fact_only_rows[0]["jaccard"]) if fact_only_rows else 1.0
        ratio = hybrid_ratios.get((ticker, construct), 0.0)
        min_jaccard = min(jaccards) if jaccards else 1.0
        cell_rows.append(
            {
                "ticker": ticker,
                "company": rows[0]["company"],
                "sample_role": rows[0]["sample_role"],
                "construct": construct,
                "hybrid_text_xbrl_word_imbalance_ratio": fmt(ratio),
                "minimum_source_set_jaccard": fmt(min_jaccard),
                "fact_only_jaccard": fmt(fact_only_jaccard),
                "n_variants_reviewed": len(rows),
                "separability_attention_band": attention_band(ratio, fact_only_jaccard, min_jaccard),
                "interpretive_boundary": (
                    "Retrieval-stage sensitivity diagnostic only; not output-level robustness or model-performance evidence."
                ),
            }
        )

    by_variant: dict[str, list[dict[str, str]]] = {}
    for row in perturb_rows:
        by_variant.setdefault(row["variant"], []).append(row)

    variant_rows: list[dict[str, object]] = []
    for variant, rows in sorted(by_variant.items()):
        jaccards = [float(row["jaccard"]) for row in rows]
        retained = [float(row["retained_share"]) for row in rows]
        low_cells = [row for row in rows if float(row["jaccard"]) < 0.60]
        variant_rows.append(
            {
                "variant": variant,
                "variant_group": rows[0]["variant_group"],
                "n_cells": len(rows),
                "mean_jaccard": fmt(mean(jaccards)),
                "median_jaccard": fmt(median(jaccards)),
                "minimum_jaccard": fmt(min(jaccards)),
                "mean_retained_share": fmt(mean(retained)),
                "cells_below_0_60": len(low_cells),
                "decision_band": decision_band(mean(jaccards)),
                "reviewer_use": (
                    "Use to evaluate source-environment sensitivity before interpreting LLM outputs."
                ),
            }
        )

    write_csv(
        CELL_OUT,
        cell_rows,
        [
            "ticker",
            "company",
            "sample_role",
            "construct",
            "hybrid_text_xbrl_word_imbalance_ratio",
            "minimum_source_set_jaccard",
            "fact_only_jaccard",
            "n_variants_reviewed",
            "separability_attention_band",
            "interpretive_boundary",
        ],
    )
    write_csv(
        VARIANT_OUT,
        variant_rows,
        [
            "variant",
            "variant_group",
            "n_cells",
            "mean_jaccard",
            "median_jaccard",
            "minimum_jaccard",
            "mean_retained_share",
            "cells_below_0_60",
            "decision_band",
            "reviewer_use",
        ],
    )

    attention_counts = {}
    for row in cell_rows:
        attention_counts[str(row["separability_attention_band"])] = attention_counts.get(str(row["separability_attention_band"]), 0) + 1

    lines = [
        "# Bounded Sensitivity Decision Summary",
        "",
        "## Purpose",
        "",
        "This diagnostic converts the context-volume and source-environment perturbation outputs into a reviewer-facing decision matrix.",
        "It evaluates retrieval-stage separability and source-composition sensitivity; it does not re-run the LLM and should not be interpreted as model-output robustness evidence.",
        "",
        "## Scope",
        "",
        f"- Filer-construct cells reviewed: `{len(cell_rows)}`",
        f"- Perturbation rows reviewed: `{len(perturb_rows)}`",
        "- Variants reviewed: text top-3, text top-8, XBRL fact-only, XBRL reduced fact budget, and XBRL expanded fact/path budget.",
        "",
        "## Variant Decision Bands",
        "",
        "| Variant | Cells | Mean Jaccard | Minimum Jaccard | Cells Below 0.60 | Decision Band |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in variant_rows:
        lines.append(
            f"| {row['variant']} | {row['n_cells']} | {row['mean_jaccard']} | "
            f"{row['minimum_jaccard']} | {row['cells_below_0_60']} | {row['decision_band']} |"
        )

    lines.extend(
        [
            "",
            "## Cell-Level Separability Attention",
            "",
            "| Attention Band | Cells |",
            "|---|---:|",
        ]
    )
    for band, count in sorted(attention_counts.items()):
        lines.append(f"| {band} | {count} |")

    high_cells = [row for row in cell_rows if row["separability_attention_band"] == "high_separability_attention"]
    lines.extend(
        [
            "",
            "## High-Attention Cells",
            "",
            "| Ticker | Construct | Hybrid Imbalance | Minimum Jaccard | Fact-Only Jaccard |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for row in high_cells:
        lines.append(
            f"| {row['ticker']} | {row['construct']} | "
            f"{row['hybrid_text_xbrl_word_imbalance_ratio']} | {row['minimum_source_set_jaccard']} | "
            f"{row['fact_only_jaccard']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- The diagnostic shows that relational XBRL evidence is methodologically separable from fact-only XBRL retrieval: removing relation paths creates a material source-environment change in most filer-construct cells.",
            "- High-attention cells identify where future Tier 2 model-validation studies should add matched-budget, source-order, prompt-sensitivity, and output-level rerun checks before making performance claims.",
            "- The current paper uses these results to validate protocol transparency and source-environment inspectability, not retrieval superiority.",
            "",
        ]
    )
    SUMMARY_OUT.write_text("\n".join(lines), encoding="utf-8")

    print(CELL_OUT)
    print(VARIANT_OUT)
    print(SUMMARY_OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
