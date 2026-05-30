import argparse
import csv
import json
import re
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path


DEFAULT_ROLES = {"main_deep_case", "bounded_extension"}


def load_filers(manifest_path: Path, roles: set[str]) -> list[dict]:
    filers = json.loads(manifest_path.read_text(encoding="utf-8"))
    selected = [filer for filer in filers if filer.get("sample_role") in roles]
    for filer in selected:
        stem = Path(filer["primary_doc"]).stem
        filer["html"] = filer["primary_doc"]
        filer["instance"] = filer.get("instance") or f"{stem}_htm.xml"
        filer["pre"] = filer.get("pre") or f"{stem}_pre.xml"
        filer["cal"] = filer.get("cal") or f"{stem}_cal.xml"
        filer["def"] = filer.get("def") or f"{stem}_def.xml"
        filer["lab"] = filer.get("lab") or f"{stem}_lab.xml"
    return selected


TEXT_KEYWORDS = {
    "revenue": [
        "revenue",
        "sales",
        "contract liabilities",
        "deferred revenue",
        "gift card",
        "stored value",
        "loyalty",
        "returns",
        "refund",
        "customer incentives",
        "receivable",
    ],
    "inventory": [
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
}


XBRL_SEED_PATTERNS = [
    "Revenue",
    "SalesRevenue",
    "ContractWithCustomer",
    "DeferredRevenue",
    "RefundLiability",
    "Customer",
    "Receivable",
    "Inventory",
    "Inventories",
    "CostOfRevenue",
    "CostOfGoods",
    "CostOfSales",
    "GrossProfit",
    "GrossMargin",
    "Markdown",
    "Obsolescence",
    "Reserve",
    "Loyalty",
    "Gift",
    "StoredValue",
]


XBRL_NS = {
    "xlink": "http://www.w3.org/1999/xlink",
    "link": "http://www.xbrl.org/2003/linkbase",
    "xbrli": "http://www.xbrl.org/2003/instance",
}


def strip_html_to_blocks(html: str) -> list[str]:
    html = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", html)
    html = re.sub(r"(?is)<ix:header.*?</ix:header>", " ", html)
    html = re.sub(r"(?is)<ix:hidden.*?</ix:hidden>", " ", html)
    html = re.sub(r"(?is)<ix:resources.*?</ix:resources>", " ", html)
    html = re.sub(r'(?is)<[^>]+style="[^"]*display\s*:\s*none[^"]*"[^>]*>.*?</[^>]+>', " ", html)
    html = re.sub(r"(?i)</(p|div|tr|table|li|br|h[1-6])>", "\n", html)
    html = re.sub(r"(?is)<[^>]+>", " ", html)
    text = unescape(html)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.split("\n")]
    return [line for line in lines if len(line) >= 80 and not metadata_noise(line)]


def metadata_noise(line: str) -> bool:
    lower = line.lower()
    metadata_markers = [
        "http://fasb.org",
        "http://xbrl.sec.gov",
        "xbrli:",
        "us-gaap:",
        "iso4217:",
        "dei:",
    ]
    marker_hits = sum(1 for marker in metadata_markers if marker in lower)
    if marker_hits >= 2:
        return True
    if lower.count("http://") + lower.count("https://") >= 2:
        return True
    if lower.count(" us-gaap:") >= 3:
        return True
    return False


def classify_text(block: str) -> str:
    lower = block.lower()
    hits = []
    for construct, keywords in TEXT_KEYWORDS.items():
        if any(keyword in lower for keyword in keywords):
            hits.append(construct)
    if len(hits) == 2:
        return "revenue_inventory"
    if hits:
        return hits[0]
    return "other"


def extract_text_chunks(raw_dir: Path, filer: dict) -> list[dict]:
    path = raw_dir / filer["folder"] / filer["html"]
    blocks = strip_html_to_blocks(path.read_text(encoding="utf-8", errors="ignore"))
    rows = []
    counters = {"revenue": 0, "inventory": 0, "revenue_inventory": 0}
    previous = ""
    for block in blocks:
        construct = classify_text(block)
        if construct == "other":
            previous = block[:220]
            continue
        counters[construct] += 1
        chunk_id = f"T-{filer['ticker']}-{construct.upper()}-{counters[construct]:03d}"
        rows.append(
            {
                "chunk_id": chunk_id,
                "ticker": filer["ticker"],
                "company": filer["company"],
                "sample_role": filer.get("sample_role", ""),
                "construct": construct,
                "source_file": filer["html"],
                "preceding_context": previous,
                "text": block,
            }
        )
        previous = block[:220]
    return rows


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def namespace_uri(tag: str) -> str:
    if tag.startswith("{") and "}" in tag:
        return tag[1:].split("}", 1)[0]
    return ""


def concept_matches(name: str) -> bool:
    compact = name.replace("_", "")
    return any(pattern.lower() in compact.lower() for pattern in XBRL_SEED_PATTERNS)


def extract_contexts(root: ET.Element) -> dict:
    contexts = {}
    for context in root.findall(".//xbrli:context", XBRL_NS):
        context_id = context.attrib.get("id", "")
        period = context.find("xbrli:period", XBRL_NS)
        period_text = ""
        if period is not None:
            instant = period.find("xbrli:instant", XBRL_NS)
            start = period.find("xbrli:startDate", XBRL_NS)
            end = period.find("xbrli:endDate", XBRL_NS)
            if instant is not None:
                period_text = f"instant:{instant.text}"
            elif start is not None and end is not None:
                period_text = f"duration:{start.text}/{end.text}"
        dims = []
        for member in context.iter():
            lname = local_name(member.tag)
            if lname in {"explicitMember", "typedMember"}:
                dims.append(f"{member.attrib.get('dimension', '')}={''.join(member.itertext()).strip()}")
        contexts[context_id] = {"period": period_text, "dimensions": "; ".join(dims)}
    return contexts


def extract_units(root: ET.Element) -> dict:
    units = {}
    for unit in root.findall(".//xbrli:unit", XBRL_NS):
        unit_id = unit.attrib.get("id", "")
        measures = [m.text or "" for m in unit.findall(".//xbrli:measure", XBRL_NS)]
        units[unit_id] = " / ".join(measures)
    return units


def extract_facts(raw_dir: Path, filer: dict) -> list[dict]:
    path = raw_dir / filer["folder"] / filer["instance"]
    root = ET.parse(path).getroot()
    contexts = extract_contexts(root)
    units = extract_units(root)
    rows = []
    for elem in root.iter():
        context_ref = elem.attrib.get("contextRef")
        if not context_ref:
            continue
        concept = local_name(elem.tag)
        if not concept_matches(concept):
            continue
        value = "".join(elem.itertext()).strip()
        if not value:
            continue
        context = contexts.get(context_ref, {})
        rows.append(
            {
                "fact_id": f"F-{filer['ticker']}-{len(rows)+1:04d}",
                "ticker": filer["ticker"],
                "company": filer["company"],
                "sample_role": filer.get("sample_role", ""),
                "concept": concept,
                "namespace": namespace_uri(elem.tag),
                "value": value,
                "unit": units.get(elem.attrib.get("unitRef", ""), elem.attrib.get("unitRef", "")),
                "decimals": elem.attrib.get("decimals", ""),
                "context_ref": context_ref,
                "period": context.get("period", ""),
                "dimensions": context.get("dimensions", ""),
                "source_file": filer["instance"],
            }
        )
    return rows


def loc_concept(href: str) -> str:
    if "#" not in href:
        return href
    value = href.split("#", 1)[1]
    return value.replace("_", ":", 1) if "_" in value else value


def extract_labels(raw_dir: Path, filer: dict) -> dict:
    path = raw_dir / filer["folder"] / filer["lab"]
    if not path.exists():
        return {}
    root = ET.parse(path).getroot()
    locs = {}
    for loc in root.findall(".//link:loc", XBRL_NS):
        label = loc.attrib.get(f"{{{XBRL_NS['xlink']}}}label", "")
        href = loc.attrib.get(f"{{{XBRL_NS['xlink']}}}href", "")
        locs[label] = loc_concept(href)

    resources = {}
    for label in root.findall(".//link:label", XBRL_NS):
        label_id = label.attrib.get(f"{{{XBRL_NS['xlink']}}}label", "")
        role = label.attrib.get(f"{{{XBRL_NS['xlink']}}}role", "")
        text = "".join(label.itertext()).strip()
        resources[label_id] = {"role": role, "text": text}

    concept_labels = {}
    for arc in root.findall(".//link:labelArc", XBRL_NS):
        from_label = arc.attrib.get(f"{{{XBRL_NS['xlink']}}}from", "")
        to_label = arc.attrib.get(f"{{{XBRL_NS['xlink']}}}to", "")
        concept = locs.get(from_label)
        resource = resources.get(to_label)
        if concept and resource and "label" in resource["role"].lower():
            concept_labels.setdefault(concept, resource["text"])
    return concept_labels


def extract_relations(raw_dir: Path, filer: dict, labels: dict) -> list[dict]:
    linkbases = [
        ("presentation", filer["pre"], "presentationArc"),
        ("calculation", filer["cal"], "calculationArc"),
        ("definition", filer["def"], "definitionArc"),
    ]
    rows = []
    for relation_type, filename, arc_name in linkbases:
        path = raw_dir / filer["folder"] / filename
        if not path.exists():
            continue
        root = ET.parse(path).getroot()
        for link in root:
            if not local_name(link.tag).endswith("Link"):
                continue
            role = link.attrib.get(f"{{{XBRL_NS['xlink']}}}role", "")
            locs = {}
            for loc in link.findall("link:loc", XBRL_NS):
                label = loc.attrib.get(f"{{{XBRL_NS['xlink']}}}label", "")
                href = loc.attrib.get(f"{{{XBRL_NS['xlink']}}}href", "")
                locs[label] = loc_concept(href)
            for arc in link.findall(f"link:{arc_name}", XBRL_NS):
                source = locs.get(arc.attrib.get(f"{{{XBRL_NS['xlink']}}}from", ""), "")
                target = locs.get(arc.attrib.get(f"{{{XBRL_NS['xlink']}}}to", ""), "")
                if not source or not target:
                    continue
                if not (concept_matches(source) or concept_matches(target)):
                    continue
                rows.append(
                    {
                        "path_id": f"X-{filer['ticker']}-{len(rows)+1:04d}",
                        "ticker": filer["ticker"],
                        "company": filer["company"],
                        "sample_role": filer.get("sample_role", ""),
                        "relation_type": relation_type,
                        "source_concept": source,
                        "source_label": labels.get(source, ""),
                        "target_concept": target,
                        "target_label": labels.get(target, ""),
                        "arcrole": arc.attrib.get(f"{{{XBRL_NS['xlink']}}}arcrole", ""),
                        "order": arc.attrib.get("order", ""),
                        "weight": arc.attrib.get("weight", ""),
                        "preferred_label": arc.attrib.get("preferredLabel", ""),
                        "role": role,
                        "source_file": filename,
                    }
                )
    return rows


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract text chunks and XBRL relation data for the demonstration.")
    parser.add_argument("--manifest", default="config/filer_manifest.json")
    parser.add_argument("--roles", nargs="+", default=sorted(DEFAULT_ROLES))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    filers = load_filers(Path(args.manifest), set(args.roles))
    raw_dir = Path("data/raw_sec")
    processed = Path("data/processed")

    all_text_rows = []
    all_fact_rows = []
    all_relation_rows = []
    summary = []

    for filer in filers:
        text_rows = extract_text_chunks(raw_dir, filer)
        fact_rows = extract_facts(raw_dir, filer)
        labels = extract_labels(raw_dir, filer)
        relation_rows = extract_relations(raw_dir, filer, labels)

        all_text_rows.extend(text_rows)
        all_fact_rows.extend(fact_rows)
        all_relation_rows.extend(relation_rows)

        summary.append(
            {
                "ticker": filer["ticker"],
                "company": filer["company"],
                "sample_role": filer.get("sample_role", ""),
                "text_chunks": len(text_rows),
                "xbrl_facts": len(fact_rows),
                "xbrl_relations": len(relation_rows),
            }
        )

        write_json(processed / "text_chunks" / f"{filer['ticker'].lower()}_text_chunks.json", text_rows)
        write_json(processed / "xbrl_facts" / f"{filer['ticker'].lower()}_xbrl_facts.json", fact_rows)
        write_json(processed / "xbrl_paths" / f"{filer['ticker'].lower()}_xbrl_paths.json", relation_rows)

    write_csv(
        processed / "text_chunks" / "text_chunks.csv",
        all_text_rows,
        ["chunk_id", "ticker", "company", "sample_role", "construct", "source_file", "preceding_context", "text"],
    )
    write_csv(
        processed / "xbrl_facts" / "xbrl_facts.csv",
        all_fact_rows,
        [
            "fact_id",
            "ticker",
            "company",
            "sample_role",
            "concept",
            "namespace",
            "value",
            "unit",
            "decimals",
            "context_ref",
            "period",
            "dimensions",
            "source_file",
        ],
    )
    write_csv(
        processed / "xbrl_paths" / "xbrl_paths.csv",
        all_relation_rows,
        [
            "path_id",
            "ticker",
            "company",
            "sample_role",
            "relation_type",
            "source_concept",
            "source_label",
            "target_concept",
            "target_label",
            "arcrole",
            "order",
            "weight",
            "preferred_label",
            "role",
            "source_file",
        ],
    )
    write_json(processed / "extraction_summary.json", summary)

    lines = ["# Phase 6 Extraction Summary", ""]
    for item in summary:
        lines.append(f"## {item['ticker']} - {item['company']}")
        lines.append("")
        lines.append(f"- Sample role: `{item['sample_role']}`")
        lines.append(f"- Text chunks: {item['text_chunks']}")
        lines.append(f"- XBRL facts: {item['xbrl_facts']}")
        lines.append(f"- XBRL relation paths: {item['xbrl_relations']}")
        lines.append("")
    lines.append("## Output Files")
    lines.append("")
    lines.append("- `data/processed/text_chunks/text_chunks.csv`")
    lines.append("- `data/processed/xbrl_facts/xbrl_facts.csv`")
    lines.append("- `data/processed/xbrl_paths/xbrl_paths.csv`")
    lines.append("- per-filer JSON files in the same processed subdirectories")
    (processed / "extraction_summary.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
