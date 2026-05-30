import argparse
import json
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


USER_AGENT = "xbrl-ontology-audit-research/0.1 contact: jk2347@rutgers.com"
BASE = "https://www.sec.gov/Archives/edgar/data"


DEFAULT_ROLES = {"main_deep_case", "bounded_extension"}


def load_filers(manifest_path: Path, roles: set[str]) -> list[dict]:
    filers = json.loads(manifest_path.read_text(encoding="utf-8"))
    return [filer for filer in filers if filer.get("sample_role") in roles]


def fetch_bytes(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "identity"})
    with urlopen(req, timeout=60) as response:
        return response.read()


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def fetch_or_reuse(path: Path, url: str) -> tuple[bytes, bool]:
    if path.exists() and path.stat().st_size > 0:
        return path.read_bytes(), True
    data = fetch_bytes(url)
    write_bytes(path, data)
    return data, False


def accession_nodash(accession: str) -> str:
    return accession.replace("-", "")


def filing_base_url(filer: dict) -> str:
    return f"{BASE}/{int(filer['cik'])}/{accession_nodash(filer['accession'])}"


def wanted_file(name: str, accession: str) -> bool:
    lower = name.lower()
    accession_txt = f"{accession}.txt"
    return (
        lower.endswith(".xsd")
        or lower.endswith("_cal.xml")
        or lower.endswith("_def.xml")
        or lower.endswith("_lab.xml")
        or lower.endswith("_pre.xml")
        or lower.endswith("_htm.xml")
        or lower.endswith(".htm")
        or lower == accession_txt
    )


def download_filer(filer: dict, raw_root: Path) -> dict:
    base_url = filing_base_url(filer)
    out_dir = raw_root / filer["folder"]
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "ticker": filer["ticker"],
        "company": filer["company"],
        "cik": filer["cik"],
        "accession": filer["accession"],
        "period": filer["period"],
        "fiscal_year": filer.get("fiscal_year", ""),
        "sample_role": filer.get("sample_role", ""),
        "primary_doc": filer.get("primary_doc", ""),
        "base_url": base_url,
        "downloaded": [],
        "skipped": [],
    }

    index_url = f"{base_url}/index.json"
    index_data, reused = fetch_or_reuse(out_dir / "index.json", index_url)
    if reused:
        manifest["downloaded"].append("index.json (reused)")
    else:
        manifest["downloaded"].append("index.json")
    index = json.loads(index_data.decode("utf-8"))

    html_index_url = f"{base_url}/{filer['accession']}-index.htm"
    try:
        _, reused = fetch_or_reuse(out_dir / f"{filer['accession']}-index.htm", html_index_url)
        suffix = " (reused)" if reused else ""
        manifest["downloaded"].append(f"{filer['accession']}-index.htm{suffix}")
    except (HTTPError, URLError) as exc:
        manifest["skipped"].append({"name": f"{filer['accession']}-index.htm", "reason": str(exc)})

    for item in index.get("directory", {}).get("item", []):
        name = item.get("name", "")
        if not wanted_file(name, filer["accession"]):
            continue
        url = f"{base_url}/{name}"
        try:
            _, reused = fetch_or_reuse(out_dir / name, url)
            suffix = " (reused)" if reused else ""
            manifest["downloaded"].append(f"{name}{suffix}")
            if not reused:
                time.sleep(0.15)
        except (HTTPError, URLError) as exc:
            manifest["skipped"].append({"name": name, "reason": str(exc)})

    write_bytes(out_dir / "download_manifest.json", json.dumps(manifest, indent=2).encode("utf-8"))
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download SEC filing files for the XBRL retrieval demonstration.")
    parser.add_argument("--manifest", default="config/filer_manifest.json")
    parser.add_argument("--roles", nargs="+", default=sorted(DEFAULT_ROLES))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    filers = load_filers(Path(args.manifest), set(args.roles))
    raw_root = Path("data/raw_sec")
    manifests = []
    for filer in filers:
        print(f"Downloading {filer['ticker']} {filer['accession']}...")
        manifests.append(download_filer(filer, raw_root))
        time.sleep(0.25)

    processed = Path("data/processed")
    processed.mkdir(parents=True, exist_ok=True)
    write_bytes(processed / "download_manifest.json", json.dumps(manifests, indent=2).encode("utf-8"))

    lines = ["# SEC Download Manifest", ""]
    for manifest in manifests:
        lines.append(f"## {manifest['ticker']} - {manifest['company']}")
        lines.append("")
        lines.append(f"- CIK: `{manifest['cik']}`")
        lines.append(f"- Accession: `{manifest['accession']}`")
        lines.append(f"- Sample role: `{manifest['sample_role']}`")
        lines.append(f"- Period: `{manifest['period']}`")
        lines.append(f"- Base URL: {manifest['base_url']}")
        lines.append("- Downloaded files:")
        for name in manifest["downloaded"]:
            lines.append(f"  - `{name}`")
        if manifest["skipped"]:
            lines.append("- Skipped files:")
            for item in manifest["skipped"]:
                lines.append(f"  - `{item['name']}`: {item['reason']}")
        lines.append("")
    (processed / "download_manifest.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
