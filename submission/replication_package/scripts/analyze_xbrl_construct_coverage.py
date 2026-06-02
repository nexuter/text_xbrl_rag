import csv
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(".")
RETRIEVAL_LOG = ROOT / "data/processed/retrieval_logs/retrieval_log.csv"
XBRL_FACTS = ROOT / "data/processed/xbrl_facts/xbrl_facts.csv"
XBRL_PATHS = ROOT / "data/processed/xbrl_paths/xbrl_paths.csv"
OUT_DIR = ROOT / "data/processed/xbrl_coverage"
FILER_CSV = OUT_DIR / "construct_coverage_by_filer.csv"
FAMILY_CSV = OUT_DIR / "construct_coverage_by_family.csv"
SUMMARY_MD = OUT_DIR / "xbrl_construct_coverage_summary.md"

csv.field_size_limit(sys.maxsize)


CONSTRUCT_FAMILIES = {
    "revenue": {
        "revenue_or_sales_amount": [
            r"revenue",
            r"salesrevenue",
            r"\bsales\b",
            r"net sales",
        ],
        "contract_liability_or_deferred_revenue": [
            r"contractwithcustomerliability",
            r"deferredrevenue",
            r"unearnedrevenue",
            r"customeradvances",
            r"storedvalue",
            r"gift",
            r"loyalty",
            r"breakage",
        ],
        "refunds_returns_or_variable_consideration": [
            r"refund",
            r"returns?",
            r"variableconsideration",
            r"rebate",
            r"incentive",
        ],
        "receivables_or_collectibility": [
            r"accountsreceivable",
            r"receivable",
            r"allowancefordoubtful",
            r"creditloss",
        ],
        "disaggregation_or_customer_dimension": [
            r"disaggregation",
            r"externalcustomers",
            r"customer",
            r"segment",
            r"geograph",
            r"product",
            r"channel",
        ],
    },
    "inventory": {
        "inventory_balance": [
            r"inventory",
            r"inventories",
            r"merchandiseinventor",
        ],
        "inventory_components": [
            r"rawmaterials",
            r"workinprocess",
            r"finishedgoods",
            r"materials",
            r"parts",
            r"supplies",
        ],
        "valuation_reserve_or_obsolescence": [
            r"reserve",
            r"valuation",
            r"writedown",
            r"write.?down",
            r"obsolete",
            r"obsolescence",
            r"lowerofcost",
            r"netrealizable",
            r"nrv",
            r"shrink",
        ],
        "cost_flow_or_cogs": [
            r"costofgoods",
            r"costofrevenue",
            r"lifo",
            r"fifo",
            r"averagecost",
            r"grossprofit",
        ],
        "inventory_movements": [
            r"increasedecreaseininventor",
            r"change.?in.?inventor",
            r"purchases",
            r"turnover",
        ],
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower())


def family_hits(construct: str, text: str) -> set[str]:
    normalized = normalize(text)
    compact = normalized.replace(" ", "")
    hits = set()
    for family, patterns in CONSTRUCT_FAMILIES[construct].items():
        for pattern in patterns:
            if re.search(pattern, normalized) or re.search(pattern, compact):
                hits.add(family)
                break
    return hits


def source_maps() -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    facts = {row["fact_id"]: row for row in read_csv(XBRL_FACTS)}
    paths = {row["path_id"]: row for row in read_csv(XBRL_PATHS)}
    return facts, paths


def row_text_for_fact(row: dict[str, str]) -> str:
    return " ".join(
        [
            row.get("concept", ""),
            row.get("namespace", ""),
            row.get("period", ""),
            row.get("dimensions", ""),
        ]
    )


def row_text_for_path(row: dict[str, str]) -> str:
    return " ".join(
        [
            row.get("source_concept", ""),
            row.get("source_label", ""),
            row.get("target_concept", ""),
            row.get("target_label", ""),
            row.get("relation_type", ""),
            row.get("role", ""),
        ]
    )


def main() -> int:
    facts, paths = source_maps()
    retrieval = read_csv(RETRIEVAL_LOG)

    selected: dict[tuple[str, str, str, str], set[str]] = defaultdict(set)
    metadata: dict[tuple[str, str], dict[str, str]] = {}

    for row in retrieval:
        construct = row["construct"]
        if construct not in CONSTRUCT_FAMILIES:
            continue
        component = row["condition_component"]
        if component not in {"xbrl_fact", "xbrl_relation_path", "xbrl_path"}:
            continue

        ticker = row["ticker"]
        metadata[(ticker, construct)] = {
            "ticker": ticker,
            "company": row["company"],
            "sample_role": row["sample_role"],
            "construct": construct,
        }

        source_id = row["source_id"]
        if component == "xbrl_fact":
            source_row = facts.get(source_id)
            source_text = row_text_for_fact(source_row) if source_row else row.get("notes", "")
            source_kind = "fact"
        else:
            source_row = paths.get(source_id)
            source_text = row_text_for_path(source_row) if source_row else row.get("notes", "")
            source_kind = "path"

        for family in family_hits(construct, source_text):
            selected[(ticker, construct, family, source_kind)].add(source_id)

    filer_rows = []
    family_rows = []
    for (ticker, construct), meta in sorted(metadata.items()):
        expected = set(CONSTRUCT_FAMILIES[construct])
        fact_families = {
            family
            for family in expected
            if selected.get((ticker, construct, family, "fact"), set())
        }
        path_families = {
            family
            for family in expected
            if selected.get((ticker, construct, family, "path"), set())
        }
        covered = sorted(fact_families | path_families)
        missing = sorted(expected - set(covered))
        status = "complete_family_coverage" if len(covered) == len(expected) else "partial_family_coverage"
        if not covered:
            status = "no_family_coverage"
        filer_rows.append(
            {
                **meta,
                "expected_family_count": len(expected),
                "covered_family_count": len(covered),
                "fact_family_count": len(fact_families),
                "path_family_count": len(path_families),
                "covered_families": "; ".join(covered),
                "missing_families": "; ".join(missing),
                "coverage_status": status,
                "diagnostic_boundary": "Coverage indicates whether retrieved XBRL facts/paths instantiate the ex ante construct family; absence is a retrieval-design diagnostic, not evidence that the assertion is misstated.",
            }
        )

    for construct, families in CONSTRUCT_FAMILIES.items():
        tickers = sorted({ticker for (ticker, c), _meta in metadata.items() if c == construct})
        for family in families:
            fact_hit_tickers = [
                ticker for ticker in tickers if selected.get((ticker, construct, family, "fact"), set())
            ]
            path_hit_tickers = [
                ticker for ticker in tickers if selected.get((ticker, construct, family, "path"), set())
            ]
            family_rows.append(
                {
                    "construct": construct,
                    "concept_family": family,
                    "filers_in_construct": len(tickers),
                    "filers_with_fact_hit": len(fact_hit_tickers),
                    "filers_with_path_hit": len(path_hit_tickers),
                    "filers_with_any_hit": len(set(fact_hit_tickers) | set(path_hit_tickers)),
                    "fact_hit_filers": "; ".join(fact_hit_tickers),
                    "path_hit_filers": "; ".join(path_hit_tickers),
                    "diagnostic_boundary": "Family-level counts describe retrieval coverage of reported XBRL concepts and relation paths, not model accuracy or audit evidence sufficiency.",
                }
            )

    write_csv(
        FILER_CSV,
        filer_rows,
        [
            "ticker",
            "company",
            "sample_role",
            "construct",
            "expected_family_count",
            "covered_family_count",
            "fact_family_count",
            "path_family_count",
            "covered_families",
            "missing_families",
            "coverage_status",
            "diagnostic_boundary",
        ],
    )
    write_csv(
        FAMILY_CSV,
        family_rows,
        [
            "construct",
            "concept_family",
            "filers_in_construct",
            "filers_with_fact_hit",
            "filers_with_path_hit",
            "filers_with_any_hit",
            "fact_hit_filers",
            "path_hit_filers",
            "diagnostic_boundary",
        ],
    )

    complete = sum(1 for row in filer_rows if row["coverage_status"] == "complete_family_coverage")
    partial = sum(1 for row in filer_rows if row["coverage_status"] == "partial_family_coverage")
    lines = [
        "# XBRL Construct Coverage Diagnostics",
        "",
        "## Purpose",
        "",
        "This diagnostic links the ex ante revenue and inventory construct protocols to the XBRL facts and relation paths actually supplied in the retrieval environment. It is a retrieval-environment validity diagnostic, not a model-performance or final audit-judgment test.",
        "",
        "## Output Files",
        "",
        f"- Filer-level coverage: `{FILER_CSV.as_posix()}`",
        f"- Concept-family coverage: `{FAMILY_CSV.as_posix()}`",
        "",
        "## Filer-Level Summary",
        "",
        f"- Construct-filer cells reviewed: `{len(filer_rows)}`",
        f"- Complete expected-family coverage cells: `{complete}`",
        f"- Partial expected-family coverage cells: `{partial}`",
        "",
        "| Ticker | Construct | Covered Families | Missing Families | Status |",
        "|---|---|---:|---|---|",
    ]
    for row in filer_rows:
        lines.append(
            f"| {row['ticker']} | {row['construct']} | {row['covered_family_count']}/{row['expected_family_count']} | "
            f"{row['missing_families'] or 'None'} | {row['coverage_status']} |"
        )
    lines.extend(
        [
            "",
            "## Family-Level Summary",
            "",
            "| Construct | Concept Family | Filers With Any Hit | Fact-Hit Filers | Path-Hit Filers |",
            "|---|---|---:|---|---|",
        ]
    )
    for row in family_rows:
        lines.append(
            f"| {row['construct']} | {row['concept_family']} | {row['filers_with_any_hit']}/{row['filers_in_construct']} | "
            f"{row['fact_hit_filers'] or 'None'} | {row['path_hit_filers'] or 'None'} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation Boundary",
            "",
            "These counts show whether the retrieval protocol surfaced expected XBRL concept families before LLM outputs are interpreted. They do not show that the LLM made correct audit judgments, that a reported balance has sufficient appropriate audit evidence, or that unobserved concept families are absent from the filing. Future Tier 2 model-validation studies should combine this diagnostic with expert coding, retrieval sensitivity tests, and model-output performance analysis.",
            "",
        ]
    )
    SUMMARY_MD.write_text("\n".join(lines), encoding="utf-8")

    print(FILER_CSV)
    print(FAMILY_CSV)
    print(SUMMARY_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
