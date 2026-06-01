import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(".")
CONTEXT_MANIFEST = ROOT / "data/processed/retrieval_contexts/context_manifest.csv"
RETRIEVAL_LOG = ROOT / "data/processed/retrieval_logs/retrieval_log.csv"
OUT_DIR = ROOT / "data/processed/retrieval_contexts"
DETAIL_CSV = OUT_DIR / "context_volume_diagnostics.csv"
SUMMARY_CSV = OUT_DIR / "context_volume_summary_by_condition.csv"
SUMMARY_MD = OUT_DIR / "context_volume_diagnostics_summary.md"


WORD_RE = re.compile(r"\b[\w$%.-]+\b")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def word_count(path_text: str) -> int:
    if not path_text:
        return 0
    path = ROOT / path_text
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="ignore")
    return len(WORD_RE.findall(text))


def in_condition(included: str, condition: str) -> bool:
    parts = {part.strip() for part in (included or "").split(";") if part.strip()}
    return condition in parts


def pct(values: list[int], q: float) -> float:
    if not values:
        return 0.0
    xs = sorted(values)
    pos = (len(xs) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(xs) - 1)
    frac = pos - lo
    return xs[lo] * (1 - frac) + xs[hi] * frac


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["condition"])].append(row)

    out = []
    for condition, items in sorted(grouped.items()):
        context_words = [int(row["actual_context_word_count"]) for row in items]
        prompt_words = [int(row["prompt_word_count"]) for row in items]
        text_chunks = [int(row["text_chunk_count"]) for row in items]
        xbrl_facts = [int(row["xbrl_fact_count"]) for row in items]
        xbrl_paths = [int(row["xbrl_path_count"]) for row in items]
        out.append(
            {
                "condition": condition,
                "n_contexts": len(items),
                "context_words_mean": round(mean(context_words), 1),
                "context_words_median": round(pct(context_words, 0.5), 1),
                "context_words_min": min(context_words) if context_words else 0,
                "context_words_max": max(context_words) if context_words else 0,
                "prompt_words_mean": round(mean(prompt_words), 1),
                "text_chunks_mean": round(mean(text_chunks), 1),
                "xbrl_facts_mean": round(mean(xbrl_facts), 1),
                "xbrl_paths_mean": round(mean(xbrl_paths), 1),
            }
        )
    return out


def main() -> int:
    manifest = read_csv(CONTEXT_MANIFEST)
    retrieval_rows = read_csv(RETRIEVAL_LOG)

    source_counts: dict[tuple[str, str, str, str], Counter] = defaultdict(Counter)
    source_words: dict[tuple[str, str, str, str], Counter] = defaultdict(Counter)
    for row in retrieval_rows:
        base = (
            row["ticker"],
            row["sample_role"],
            row["construct"],
        )
        component = row["condition_component"]
        source_type = "xbrl_path" if component in {"xbrl_path", "xbrl_relation_path"} else (
            "xbrl_fact" if component == "xbrl_fact" else "text"
        )
        for condition in ("text", "xbrl", "hybrid"):
            if in_condition(row.get("included_in_conditions", ""), condition):
                key = (*base, condition)
                source_counts[key][source_type] += 1
                try:
                    source_words[key][source_type] += int(float(row.get("context_word_count", "0") or 0))
                except ValueError:
                    source_words[key][source_type] += 0

    detail_rows = []
    for row in manifest:
        key = (row["ticker"], row["sample_role"], row["construct"], row["condition"])
        counts = source_counts[key]
        words = source_words[key]
        actual_context_words = word_count(row["context_file"])
        prompt_words = word_count(row["prompt_file"])
        text_words = words["text"]
        xbrl_words = words["xbrl_fact"] + words["xbrl_path"]
        imbalance_ratio = ""
        if row["condition"] == "hybrid" and min(text_words, xbrl_words) > 0:
            imbalance_ratio = round(max(text_words, xbrl_words) / min(text_words, xbrl_words), 2)
        detail_rows.append(
            {
                "ticker": row["ticker"],
                "company": row["company"],
                "sample_role": row["sample_role"],
                "construct": row["construct"],
                "condition": row["condition"],
                "condition_label": row["condition_label"],
                "manifest_context_word_count": row["context_word_count"],
                "actual_context_word_count": actual_context_words,
                "prompt_word_count": prompt_words,
                "text_chunk_count": counts["text"],
                "xbrl_fact_count": counts["xbrl_fact"],
                "xbrl_path_count": counts["xbrl_path"],
                "text_context_words_from_log": text_words,
                "xbrl_context_words_from_log": xbrl_words,
                "hybrid_text_xbrl_word_imbalance_ratio": imbalance_ratio,
                "context_file": row["context_file"],
                "prompt_file": row["prompt_file"],
            }
        )

    fields = [
        "ticker",
        "company",
        "sample_role",
        "construct",
        "condition",
        "condition_label",
        "manifest_context_word_count",
        "actual_context_word_count",
        "prompt_word_count",
        "text_chunk_count",
        "xbrl_fact_count",
        "xbrl_path_count",
        "text_context_words_from_log",
        "xbrl_context_words_from_log",
        "hybrid_text_xbrl_word_imbalance_ratio",
        "context_file",
        "prompt_file",
    ]
    write_csv(DETAIL_CSV, detail_rows, fields)

    summary_rows = summarize(detail_rows)
    write_csv(
        SUMMARY_CSV,
        summary_rows,
        [
            "condition",
            "n_contexts",
            "context_words_mean",
            "context_words_median",
            "context_words_min",
            "context_words_max",
            "prompt_words_mean",
            "text_chunks_mean",
            "xbrl_facts_mean",
            "xbrl_paths_mean",
        ],
    )

    hybrid = [row for row in detail_rows if row["condition"] == "hybrid"]
    ratios = [
        float(row["hybrid_text_xbrl_word_imbalance_ratio"])
        for row in hybrid
        if row["hybrid_text_xbrl_word_imbalance_ratio"] != ""
    ]
    lines = [
        "# Context Volume Diagnostics",
        "",
        "## Purpose",
        "",
        "This diagnostic addresses separability concerns by documenting the information volume supplied under each retrieval condition. It is a Tier 1 transparency diagnostic, not a completed model-performance sensitivity test.",
        "",
        "## Files",
        "",
        f"- Detail diagnostics: `{DETAIL_CSV.as_posix()}`",
        f"- Condition summary: `{SUMMARY_CSV.as_posix()}`",
        "",
        "## Summary By Condition",
        "",
        "| Condition | Contexts | Mean Context Words | Median | Min | Max | Mean Prompt Words | Mean Text Chunks | Mean XBRL Facts | Mean XBRL Paths |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['condition']} | {row['n_contexts']} | {row['context_words_mean']} | "
            f"{row['context_words_median']} | {row['context_words_min']} | {row['context_words_max']} | "
            f"{row['prompt_words_mean']} | {row['text_chunks_mean']} | {row['xbrl_facts_mean']} | {row['xbrl_paths_mean']} |"
        )
    lines.extend(
        [
            "",
            "## Hybrid Separability Diagnostic",
            "",
            f"- Hybrid contexts reviewed: `{len(hybrid)}`",
            f"- Hybrid text/XBRL word-imbalance ratio mean: `{round(mean(ratios), 2) if ratios else 0}`",
            f"- Hybrid text/XBRL word-imbalance ratio median: `{round(pct([int(r * 100) for r in ratios], 0.5) / 100, 2) if ratios else 0}`",
            f"- Hybrid text/XBRL word-imbalance ratio maximum: `{round(max(ratios), 2) if ratios else 0}`",
            "",
            "Interpretation: hybrid retrieval supplies more total information than text-only or XBRL-only retrieval because it combines narrative chunks and structured facts/paths. This supports the manuscript boundary that hybrid outputs should not be interpreted as model-performance evidence unless future studies add token-budget equalization, evidence-order sensitivity, and prompt sensitivity checks.",
            "",
            "## Reviewer-Facing Use",
            "",
            "These diagnostics strengthen the separability discussion by making context-volume differences observable. They do not eliminate separability concerns; instead, they document why the current paper remains a protocol-validation demonstration and why Tier 2 studies should add matched-budget and retrieval-variation sensitivity tests.",
            "",
        ]
    )
    SUMMARY_MD.write_text("\n".join(lines), encoding="utf-8")
    print(DETAIL_CSV)
    print(SUMMARY_CSV)
    print(SUMMARY_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
