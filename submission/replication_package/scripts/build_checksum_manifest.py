import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(".")
OUTPUT_DIR = Path("data/processed/checksums")
OUTPUT_CSV = OUTPUT_DIR / "checksum_manifest.csv"
OUTPUT_MD = OUTPUT_DIR / "checksum_summary.md"

INCLUDED_ROOTS = [
    Path("config/filer_manifest.json"),
    Path("data/raw_sec"),
    Path("data/processed"),
    Path("scripts"),
    Path("README_REPLICATION.md"),
]

EXCLUDED_PARTS = {
    ".git",
    "__pycache__",
}

EXCLUDED_SUFFIXES = {
    ".pyc",
}


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & EXCLUDED_PARTS:
        return True
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    if path == OUTPUT_CSV or path == OUTPUT_MD:
        return True
    return False


def iter_files() -> list[Path]:
    files: list[Path] = []
    for root in INCLUDED_ROOTS:
        if not root.exists():
            continue
        if root.is_file():
            if not should_skip(root):
                files.append(root)
            continue
        for path in root.rglob("*"):
            if path.is_file() and not should_skip(path):
                files.append(path)
    return sorted({path for path in files}, key=lambda item: item.as_posix().lower())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def category(path: Path) -> str:
    text = path.as_posix()
    if text.startswith("data/raw_sec/"):
        return "raw_sec"
    if text.startswith("data/processed/"):
        return "processed"
    if text.startswith("scripts/"):
        return "script"
    if text.startswith("config/"):
        return "config"
    return "root"


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    generated_at = datetime.now(timezone.utc).isoformat()
    for path in iter_files():
        stat = path.stat()
        rows.append(
            {
                "relative_path": path.as_posix(),
                "category": category(path),
                "size_bytes": stat.st_size,
                "sha256": sha256(path),
                "generated_at_utc": generated_at,
            }
        )

    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["relative_path", "category", "size_bytes", "sha256", "generated_at_utc"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    counts = {}
    sizes = {}
    for row in rows:
        counts[row["category"]] = counts.get(row["category"], 0) + 1
        sizes[row["category"]] = sizes.get(row["category"], 0) + int(row["size_bytes"])

    lines = [
        "# Checksum Manifest Summary",
        "",
        f"- Generated at UTC: `{generated_at}`",
        f"- Manifest file: `{OUTPUT_CSV.as_posix()}`",
        f"- Hash algorithm: `SHA-256`",
        f"- Total files hashed: `{len(rows)}`",
        "",
        "## Counts By Category",
        "",
        "| Category | Files | Size Bytes |",
        "|---|---:|---:|",
    ]
    for name in sorted(counts):
        lines.append(f"| {name} | {counts[name]} | {sizes[name]} |")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "The manifest supports archival integrity checks for the replication package. It does not validate audit evidence, audit-valid coding, retrieval performance, or exact LLM output determinism.",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_CSV} with {len(rows)} rows.")
    print(f"Wrote {OUTPUT_MD}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
