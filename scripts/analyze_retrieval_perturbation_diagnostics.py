import csv
import statistics
import sys
from pathlib import Path

from build_retrieval_contexts import read_csv, select_fact_rows, select_path_rows, select_text_rows


csv.field_size_limit(sys.maxsize)

PROCESSED = Path("data/processed")
OUT_DIR = PROCESSED / "sensitivity"


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def unique_cells(context_rows: list[dict]) -> list[dict]:
    seen = {}
    for row in context_rows:
        key = (row["ticker"], row["construct"])
        if key not in seen:
            seen[key] = {
                "ticker": row["ticker"],
                "company": row["company"],
                "sample_role": row["sample_role"],
                "construct": row["construct"],
            }
    return list(seen.values())


def ids(rows: list[dict], field: str) -> list[str]:
    return [row[field] for row in rows]


def set_metrics(baseline_ids: list[str], variant_ids: list[str]) -> dict:
    baseline = set(baseline_ids)
    variant = set(variant_ids)
    union = baseline | variant
    intersection = baseline & variant
    return {
        "baseline_count": len(baseline),
        "variant_count": len(variant),
        "retained_count": len(intersection),
        "added_count": len(variant - baseline),
        "removed_count": len(baseline - variant),
        "jaccard": len(intersection) / len(union) if union else 1.0,
        "retained_share": len(intersection) / len(baseline) if baseline else 1.0,
    }


def format_float(value: float) -> str:
    return f"{value:.3f}"


def add_row(rows: list[dict], cell: dict, variant_group: str, variant: str, baseline_ids: list[str], variant_ids: list[str], note: str) -> None:
    metrics = set_metrics(baseline_ids, variant_ids)
    rows.append(
        {
            **cell,
            "variant_group": variant_group,
            "variant": variant,
            "baseline_count": metrics["baseline_count"],
            "variant_count": metrics["variant_count"],
            "retained_count": metrics["retained_count"],
            "added_count": metrics["added_count"],
            "removed_count": metrics["removed_count"],
            "jaccard": format_float(metrics["jaccard"]),
            "retained_share": format_float(metrics["retained_share"]),
            "note": note,
        }
    )


def mean(values: list[float]) -> float:
    return statistics.mean(values) if values else 0.0


def median(values: list[float]) -> float:
    return statistics.median(values) if values else 0.0


def summarize(rows: list[dict]) -> list[dict]:
    grouped = {}
    for row in rows:
        key = (row["variant_group"], row["variant"])
        grouped.setdefault(key, []).append(row)

    summary = []
    for (variant_group, variant), group_rows in sorted(grouped.items()):
        jaccards = [float(row["jaccard"]) for row in group_rows]
        retained = [float(row["retained_share"]) for row in group_rows]
        summary.append(
            {
                "variant_group": variant_group,
                "variant": variant,
                "n_cells": len(group_rows),
                "mean_jaccard": format_float(mean(jaccards)),
                "median_jaccard": format_float(median(jaccards)),
                "mean_retained_share": format_float(mean(retained)),
                "mean_baseline_count": format_float(mean([float(row["baseline_count"]) for row in group_rows])),
                "mean_variant_count": format_float(mean([float(row["variant_count"]) for row in group_rows])),
                "mean_added_count": format_float(mean([float(row["added_count"]) for row in group_rows])),
                "mean_removed_count": format_float(mean([float(row["removed_count"]) for row in group_rows])),
            }
        )
    return summary


def write_markdown(summary_rows: list[dict], diagnostic_rows: list[dict]) -> None:
    lines = [
        "# Retrieval Perturbation Diagnostic Summary",
        "",
        "This diagnostic varies deterministic retrieval-source selection without re-running the LLM.",
        "It evaluates whether source environments are reconstructable and how much they change under bounded source-selection perturbations.",
        "The results support protocol transparency and stability assessment at the retrieval stage; they are not model-performance sensitivity results.",
        "",
        f"Diagnostic cells: {len({(row['ticker'], row['construct']) for row in diagnostic_rows})}",
        f"Diagnostic rows: {len(diagnostic_rows)}",
        "",
        "| Variant Group | Variant | Cells | Mean Jaccard | Median Jaccard | Mean Retained Share | Mean Baseline Sources | Mean Variant Sources | Mean Added | Mean Removed |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['variant_group']} | {row['variant']} | {row['n_cells']} | "
            f"{row['mean_jaccard']} | {row['median_jaccard']} | {row['mean_retained_share']} | "
            f"{row['mean_baseline_count']} | {row['mean_variant_count']} | "
            f"{row['mean_added_count']} | {row['mean_removed_count']} |"
        )
    lines.extend(
        [
            "",
            "Interpretation:",
            "",
            "- `text_top3` and `text_top8` vary the text-retrieval source budget around the implemented top-5 rule.",
            "- `xbrl_fact_only` removes relation-path evidence and therefore measures how much of the XBRL source environment depends on linkbase relations rather than instance facts alone.",
            "- `xbrl_expanded_paths` keeps the implemented fact budget and expands relation paths from 10 to 15 when available.",
            "- Because no LLM outputs are regenerated, these diagnostics should be reported as source-environment perturbation evidence rather than output-level robustness evidence.",
        ]
    )
    (OUT_DIR / "retrieval_perturbation_summary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    context_rows = read_csv(PROCESSED / "retrieval_contexts" / "context_manifest.csv")
    text_rows = read_csv(PROCESSED / "text_chunks" / "text_chunks.csv")
    fact_rows = read_csv(PROCESSED / "xbrl_facts" / "xbrl_facts.csv")
    path_rows = read_csv(PROCESSED / "xbrl_paths" / "xbrl_paths.csv")

    rows = []
    for cell in unique_cells(context_rows):
        ticker = cell["ticker"]
        construct = cell["construct"]

        text_current = ids(select_text_rows(text_rows, ticker, construct, limit=5), "chunk_id")
        text_top3 = ids(select_text_rows(text_rows, ticker, construct, limit=3), "chunk_id")
        text_top8 = ids(select_text_rows(text_rows, ticker, construct, limit=8), "chunk_id")

        facts_current = ids(select_fact_rows(fact_rows, ticker, construct, limit=12), "fact_id")
        facts_top8 = ids(select_fact_rows(fact_rows, ticker, construct, limit=8), "fact_id")
        facts_top16 = ids(select_fact_rows(fact_rows, ticker, construct, limit=16), "fact_id")
        paths_current = ids(select_path_rows(path_rows, ticker, construct, limit=10), "path_id")
        paths_top15 = ids(select_path_rows(path_rows, ticker, construct, limit=15), "path_id")

        xbrl_current = facts_current + paths_current
        xbrl_fact_only = facts_current
        xbrl_fact_top8_paths_current = facts_top8 + paths_current
        xbrl_expanded = facts_top16 + paths_top15

        add_row(rows, cell, "text", "text_top3", text_current, text_top3, "Implemented text top-5 varied to top-3.")
        add_row(rows, cell, "text", "text_top8", text_current, text_top8, "Implemented text top-5 varied to top-8.")
        add_row(rows, cell, "xbrl", "xbrl_fact_only", xbrl_current, xbrl_fact_only, "Relation paths removed; fact budget unchanged.")
        add_row(
            rows,
            cell,
            "xbrl",
            "xbrl_fact_top8_paths_current",
            xbrl_current,
            xbrl_fact_top8_paths_current,
            "Fact budget reduced from 12 to 8; relation-path budget unchanged.",
        )
        add_row(
            rows,
            cell,
            "xbrl",
            "xbrl_expanded_fact16_path15",
            xbrl_current,
            xbrl_expanded,
            "Fact budget expanded to 16 and relation-path budget expanded to 15 when available.",
        )

    fieldnames = [
        "ticker",
        "company",
        "sample_role",
        "construct",
        "variant_group",
        "variant",
        "baseline_count",
        "variant_count",
        "retained_count",
        "added_count",
        "removed_count",
        "jaccard",
        "retained_share",
        "note",
    ]
    summary_rows = summarize(rows)
    summary_fieldnames = [
        "variant_group",
        "variant",
        "n_cells",
        "mean_jaccard",
        "median_jaccard",
        "mean_retained_share",
        "mean_baseline_count",
        "mean_variant_count",
        "mean_added_count",
        "mean_removed_count",
    ]

    write_csv(OUT_DIR / "retrieval_perturbation_diagnostics.csv", rows, fieldnames)
    write_csv(OUT_DIR / "retrieval_perturbation_summary_by_variant.csv", summary_rows, summary_fieldnames)
    write_markdown(summary_rows, rows)

    print(f"Wrote {len(rows)} perturbation diagnostic rows to {OUT_DIR}")


if __name__ == "__main__":
    main()
