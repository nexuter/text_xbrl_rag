import argparse
import csv
import json
import re
import sys
from pathlib import Path


csv.field_size_limit(sys.maxsize)

DEFAULT_ROLES = {"main_deep_case", "bounded_extension"}


CONSTRUCTS = {
    "revenue": {
        "label": "revenue recognition risk cue identification",
        "text_keywords": [
            "revenue recognition",
            "revenue",
            "sales",
            "returns",
            "refund",
            "contract liabilities",
            "deferred revenue",
            "gift card",
            "stored value",
            "loyalty",
            "breakage",
            "customer incentives",
            "receivables",
            "wholesale",
            "licensed",
            "digital",
        ],
        "xbrl_keywords": [
            "Revenue",
            "SalesRevenue",
            "ContractWithCustomer",
            "DeferredRevenue",
            "RefundLiability",
            "Receivable",
            "Customer",
            "StoredValue",
            "Loyalty",
            "Gift",
        ],
    },
    "inventory": {
        "label": "inventory valuation assertion mapping",
        "text_keywords": [
            "inventory",
            "inventories",
            "cost of sales",
            "cost of goods",
            "gross margin",
            "gross profit",
            "markdown",
            "obsolescence",
            "lower of cost",
            "net realizable value",
            "reserve",
        ],
        "xbrl_keywords": [
            "Inventory",
            "Inventories",
            "CostOfRevenue",
            "CostOfGoods",
            "CostOfSales",
            "CostOfGoodsAndServicesSold",
            "GrossProfit",
            "GrossMargin",
            "Markdown",
            "Obsolescence",
            "LIFOReserve",
        ],
    },
}


CONDITIONS = ["text", "xbrl", "hybrid", "llm_only"]
EXTENSION_CONDITIONS = ["text", "xbrl", "hybrid"]


def load_filers(manifest_path: Path, roles: set[str]) -> dict[str, dict]:
    filers = json.loads(manifest_path.read_text(encoding="utf-8"))
    selected = {}
    for filer in filers:
        if filer.get("sample_role") not in roles:
            continue
        selected[filer["ticker"]] = {
            "company": filer["company"],
            "fiscal_year": filer.get("fiscal_year", ""),
            "period": filer["period"],
            "accession": filer["accession"],
            "sample_role": filer.get("sample_role", ""),
            "extension_primary_construct": filer.get("extension_primary_construct", ""),
        }
    return selected


def read_csv(path: Path) -> list[dict]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9%$.-]+", text)


def count_words(text: str) -> int:
    return len(words(text))


def truncate_words(text: str, limit: int) -> str:
    tokens = words(text)
    if len(tokens) <= limit:
        return text.strip()
    return " ".join(tokens[:limit]).strip() + " ..."


def keyword_score(text: str, keywords: list[str]) -> int:
    lower = text.lower()
    score = 0
    for keyword in keywords:
        count = lower.count(keyword.lower())
        if " " in keyword:
            score += count * 3
        else:
            score += count
    return score


def concept_score(row: dict, keywords: list[str]) -> int:
    text = " ".join(
        [
            row.get("concept", ""),
            row.get("source_concept", ""),
            row.get("target_concept", ""),
            row.get("source_label", ""),
            row.get("target_label", ""),
        ]
    )
    return keyword_score(text, keywords)


def select_text_rows(text_rows: list[dict], ticker: str, construct: str, limit: int) -> list[dict]:
    keywords = CONSTRUCTS[construct]["text_keywords"]
    candidates = []
    for row in text_rows:
        if row["ticker"] != ticker:
            continue
        row_construct = row["construct"]
        if construct not in row_construct:
            continue
        score = keyword_score(row["text"], keywords)
        if score <= 0:
            continue
        copy = dict(row)
        copy["score"] = score
        copy["word_count"] = count_words(row["text"])
        candidates.append(copy)
    candidates.sort(key=lambda item: (-int(item["score"]), item["chunk_id"]))
    return candidates[:limit]


def select_fact_rows(fact_rows: list[dict], ticker: str, construct: str, limit: int) -> list[dict]:
    keywords = CONSTRUCTS[construct]["xbrl_keywords"]
    candidates = []
    for row in fact_rows:
        if row["ticker"] != ticker:
            continue
        if construct == "inventory" and noisy_inventory_concept(row["concept"]):
            continue
        score = concept_score(row, keywords)
        if score <= 0:
            continue
        value = row.get("value", "")
        if "<" in value and ">" in value:
            continue
        copy = dict(row)
        copy["score"] = score
        copy["priority"] = fact_priority(construct, row["concept"])
        candidates.append(copy)
    candidates.sort(key=lambda item: (int(item["priority"]), item["concept"], item["period"]), reverse=False)

    selected = []
    concept_counts = {}
    for row in candidates:
        concept = row["concept"]
        if concept_counts.get(concept, 0) >= 3:
            continue
        selected.append(row)
        concept_counts[concept] = concept_counts.get(concept, 0) + 1
        if len(selected) >= limit:
            break
    return selected


def fact_priority(construct: str, concept: str) -> int:
    compact = concept.lower()
    if construct == "revenue":
        priorities = [
            ["revenuefromcontract", "revenues", "salesrevenue"],
            ["deferredrevenue", "contractwithcustomerliability"],
            ["refundliability", "storedvalue", "loyalty", "gift"],
            ["accountsreceivable", "receivable"],
            ["customer"],
        ]
    else:
        priorities = [
            ["inventorynet", "inventoryfinished", "inventorylifo", "inventory"],
            ["obsolescence", "markdown"],
            ["grossprofit", "grossmargin"],
            ["costofgoods", "costofsales", "costofrevenue"],
        ]
    for index, group in enumerate(priorities):
        if any(token in compact for token in group):
            return index
    return 99


def noisy_inventory_concept(concept: str) -> bool:
    compact = concept.lower()
    noisy_tokens = [
        "deferredtax",
        "selfinsurance",
        "accruedliabilities",
    ]
    return any(token in compact for token in noisy_tokens)


def select_path_rows(path_rows: list[dict], ticker: str, construct: str, limit: int) -> list[dict]:
    keywords = CONSTRUCTS[construct]["xbrl_keywords"]
    candidates = []
    for row in path_rows:
        if row["ticker"] != ticker:
            continue
        score = concept_score(row, keywords)
        if score <= 0:
            continue
        copy = dict(row)
        copy["score"] = score
        candidates.append(copy)
    candidates.sort(
        key=lambda item: (
            -int(item["score"]),
            item["relation_type"],
            item["source_concept"],
            item["target_concept"],
        )
    )
    return candidates[:limit]


def render_text_context(rows: list[dict], word_limit_per_chunk: int = 220) -> str:
    lines = ["TEXT RETRIEVAL CONTEXT", ""]
    for rank, row in enumerate(rows, start=1):
        text = truncate_words(row["text"], word_limit_per_chunk)
        lines.extend(
            [
                f"[Text Chunk {rank}]",
                f"chunk_id: {row['chunk_id']}",
                f"source_file: {row['source_file']}",
                f"construct_tag: {row['construct']}",
                f"ranking_score: {row['score']}",
                f"text: {text}",
                "",
            ]
        )
    return "\n".join(lines).strip()


def render_xbrl_context(facts: list[dict], paths: list[dict]) -> str:
    lines = ["XBRL RELATIONAL RETRIEVAL CONTEXT", ""]
    lines.append("Facts:")
    if facts:
        for rank, row in enumerate(facts, start=1):
            lines.append(
                f"{rank}. fact_id={row['fact_id']} concept={row['concept']} value={row['value']} "
                f"unit={row['unit']} period={row['period']} dimensions={row['dimensions'] or 'none'}"
            )
    else:
        lines.append("No selected XBRL facts.")
    lines.append("")
    lines.append("Relation paths:")
    if paths:
        for rank, row in enumerate(paths, start=1):
            source_label = row["source_label"] or "label unavailable"
            target_label = row["target_label"] or "label unavailable"
            lines.append(
                f"{rank}. path_id={row['path_id']} relation_type={row['relation_type']} "
                f"source={row['source_concept']} ({source_label}) -> "
                f"target={row['target_concept']} ({target_label}) "
                f"arcrole={row['arcrole']} role={row['role']}"
            )
    else:
        lines.append("No selected XBRL relation paths.")
    return "\n".join(lines).strip()


def render_prompt(ticker: str, filer: dict, construct: str, condition: str, context: str) -> str:
    construct_label = CONSTRUCTS[construct]["label"]
    if condition == "llm_only":
        context = "No retrieved filing context is provided in this diagnostic baseline."
    return f"""You are assisting with an auditing research task. Use only the information provided in the context.

Task:
Identify audit-relevant risk cues or assertion-mapping considerations for {construct_label} for {filer['company']}, fiscal year {filer['fiscal_year']}, period ended {filer['period']}, accession {filer['accession']}, based on the provided context.

Instructions:
1. Provide no more than five audit-relevant claims.
2. Distinguish factual claims from risk-cue or assertion-mapping claims.
3. Do not conclude that a misstatement exists.
4. State when the provided context is insufficient.
5. Avoid treating reported XBRL relationships as independent audit evidence.
6. Do not use general company knowledge outside the provided context.
7. For each risk-cue or assertion-mapping claim, state the inferential bridge from the source evidence to the audit consideration.
8. Do not write "Limitation: None" for risk-cue or assertion-mapping claims; identify at least one missing audit evidence item, missing control detail, or source-bound limitation.
9. For factual claims, state any period, source, or measurement limitation rather than treating the claim as unrestricted.

Context:
{context}

Output format:
- Claim:
  - Claim type:
  - Support used:
  - Limitation:
""".strip()


def condition_label(condition: str) -> str:
    return {
        "text": "Text-based contextual retrieval",
        "xbrl": "XBRL-based relational retrieval",
        "hybrid": "Hybrid retrieval",
        "llm_only": "LLM-only diagnostic baseline",
    }[condition]


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def selected_constructs(filer: dict, extension_all_constructs: bool) -> list[str]:
    if filer.get("sample_role") == "bounded_extension" and not extension_all_constructs:
        return [filer.get("extension_primary_construct") or "inventory"]
    return list(CONSTRUCTS)


def selected_conditions(filer: dict, include_extension_baseline: bool) -> list[str]:
    if filer.get("sample_role") == "bounded_extension" and not include_extension_baseline:
        return EXTENSION_CONDITIONS
    return CONDITIONS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build prompt-ready text, XBRL, and hybrid retrieval contexts.")
    parser.add_argument("--manifest", default="config/filer_manifest.json")
    parser.add_argument("--roles", nargs="+", default=sorted(DEFAULT_ROLES))
    parser.add_argument("--include-extension-baseline", action="store_true")
    parser.add_argument(
        "--extension-all-constructs",
        action="store_true",
        help="Generate both revenue and inventory constructs for bounded-extension filers.",
    )
    return parser.parse_args()


def build() -> None:
    args = parse_args()
    filers = load_filers(Path(args.manifest), set(args.roles))
    processed = Path("data/processed")
    text_rows = read_csv(processed / "text_chunks" / "text_chunks.csv")
    fact_rows = read_csv(processed / "xbrl_facts" / "xbrl_facts.csv")
    path_rows = read_csv(processed / "xbrl_paths" / "xbrl_paths.csv")

    context_root = processed / "retrieval_contexts"
    prompt_root = processed / "prompts"
    log_rows = []
    manifest_rows = []

    for ticker, filer in filers.items():
        for construct in selected_constructs(filer, args.extension_all_constructs):
            selected_text = select_text_rows(text_rows, ticker, construct, limit=5)
            selected_facts = select_fact_rows(fact_rows, ticker, construct, limit=12)
            selected_paths = select_path_rows(path_rows, ticker, construct, limit=10)

            text_context = render_text_context(selected_text)
            xbrl_context = render_xbrl_context(selected_facts, selected_paths)
            hybrid_context = "\n\n".join(
                [
                    render_text_context(selected_text[:3], word_limit_per_chunk=160),
                    render_xbrl_context(selected_facts[:8], selected_paths[:6]),
                ]
            )

            contexts = {
                "text": text_context,
                "xbrl": xbrl_context,
                "hybrid": hybrid_context,
                "llm_only": "No retrieved filing context is provided in this diagnostic baseline.",
            }

            for condition in selected_conditions(filer, args.include_extension_baseline):
                context = contexts[condition]
                stem = f"{ticker.lower()}_{construct}_{condition}"
                context_file = context_root / f"{stem}_context.txt"
                prompt_file = prompt_root / f"{stem}_prompt.txt"
                write_text(context_file, context)
                write_text(prompt_file, render_prompt(ticker, filer, construct, condition, context))
                manifest_rows.append(
                    {
                        "ticker": ticker,
                        "company": filer["company"],
                        "sample_role": filer.get("sample_role", ""),
                        "construct": construct,
                        "condition": condition,
                        "condition_label": condition_label(condition),
                        "context_file": str(context_file).replace("\\", "/"),
                        "prompt_file": str(prompt_file).replace("\\", "/"),
                        "context_word_count": count_words(context),
                    }
                )

            for rank, row in enumerate(selected_text, start=1):
                log_rows.append(
                    {
                        "retrieval_id": f"T-{ticker}-{construct.upper()}-{rank:02d}",
                        "ticker": ticker,
                        "company": filer["company"],
                        "sample_role": filer.get("sample_role", ""),
                        "construct": construct,
                        "condition_component": "text",
                        "source_id": row["chunk_id"],
                        "source_file": row["source_file"],
                        "retrieval_operator": "keyword-ranked text retrieval over extracted 10-K chunks",
                        "query_or_seed": "; ".join(CONSTRUCTS[construct]["text_keywords"]),
                        "rank_or_path_depth": rank,
                        "score": row["score"],
                        "included_in_conditions": "text; hybrid",
                        "context_word_count": row["word_count"],
                        "notes": "Prompt rendering may truncate long text chunks.",
                    }
                )

            for rank, row in enumerate(selected_facts, start=1):
                log_rows.append(
                    {
                        "retrieval_id": f"F-{ticker}-{construct.upper()}-{rank:02d}",
                        "ticker": ticker,
                        "company": filer["company"],
                        "sample_role": filer.get("sample_role", ""),
                        "construct": construct,
                        "condition_component": "xbrl_fact",
                        "source_id": row["fact_id"],
                        "source_file": row["source_file"],
                        "retrieval_operator": "seed-pattern concept selection from extracted XBRL instance",
                        "query_or_seed": "; ".join(CONSTRUCTS[construct]["xbrl_keywords"]),
                        "rank_or_path_depth": rank,
                        "score": row["score"],
                        "included_in_conditions": "xbrl; hybrid",
                        "context_word_count": count_words(" ".join(str(value) for value in row.values())),
                        "notes": f"concept={row['concept']} period={row['period']}",
                    }
                )

            for rank, row in enumerate(selected_paths, start=1):
                log_rows.append(
                    {
                        "retrieval_id": f"X-{ticker}-{construct.upper()}-{rank:02d}",
                        "ticker": ticker,
                        "company": filer["company"],
                        "sample_role": filer.get("sample_role", ""),
                        "construct": construct,
                        "condition_component": "xbrl_relation_path",
                        "source_id": row["path_id"],
                        "source_file": row["source_file"],
                        "retrieval_operator": "seed-pattern relation selection from XBRL linkbases",
                        "query_or_seed": "; ".join(CONSTRUCTS[construct]["xbrl_keywords"]),
                        "rank_or_path_depth": "direct_arc",
                        "score": row["score"],
                        "included_in_conditions": "xbrl; hybrid",
                        "context_word_count": count_words(" ".join(str(value) for value in row.values())),
                        "notes": f"{row['relation_type']}: {row['source_concept']} -> {row['target_concept']}",
                    }
                )

    write_csv(
        processed / "retrieval_logs" / "retrieval_log.csv",
        log_rows,
        [
            "retrieval_id",
            "ticker",
            "company",
            "sample_role",
            "construct",
            "condition_component",
            "source_id",
            "source_file",
            "retrieval_operator",
            "query_or_seed",
            "rank_or_path_depth",
            "score",
            "included_in_conditions",
            "context_word_count",
            "notes",
        ],
    )
    write_csv(
        processed / "retrieval_contexts" / "context_manifest.csv",
        manifest_rows,
        [
            "ticker",
            "company",
            "sample_role",
            "construct",
            "condition",
            "condition_label",
            "context_file",
            "prompt_file",
            "context_word_count",
        ],
    )

    summary = {}
    for row in manifest_rows:
        key = (row["ticker"], row["construct"])
        summary.setdefault(key, []).append(row)

    lines = ["# Phase 6 Retrieval Context Build Summary", ""]
    lines.append("Generated prompt-ready contexts from the shared filer manifest.")
    lines.append("")
    lines.append("| Filer | Role | Construct | Text Words | XBRL Words | Hybrid Words | Baseline Words |")
    lines.append("|---|---|---|---:|---:|---:|---:|")
    for (ticker, construct), rows in summary.items():
        by_condition = {row["condition"]: row for row in rows}
        baseline_words = by_condition.get("llm_only", {}).get("context_word_count", "NA")
        lines.append(
            f"| {ticker} | {rows[0]['sample_role']} | {construct} | "
            f"{by_condition['text']['context_word_count']} | "
            f"{by_condition['xbrl']['context_word_count']} | "
            f"{by_condition['hybrid']['context_word_count']} | "
            f"{baseline_words} |"
        )
    lines.append("")
    lines.append("## Output Files")
    lines.append("")
    lines.append("- `data/processed/retrieval_contexts/context_manifest.csv`")
    lines.append("- `data/processed/retrieval_logs/retrieval_log.csv`")
    lines.append("- `data/processed/retrieval_contexts/*_context.txt`")
    lines.append("- `data/processed/prompts/*_prompt.txt`")
    write_text(processed / "retrieval_contexts" / "retrieval_context_summary.md", "\n".join(lines))

    write_text(
        processed / "retrieval_contexts" / "retrieval_context_manifest.json",
        json.dumps(manifest_rows, indent=2),
    )


if __name__ == "__main__":
    build()
