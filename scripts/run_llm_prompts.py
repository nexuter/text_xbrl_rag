import argparse
import csv
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import requests


DEFAULT_OPENAI_BASE_URL = "https://api.openai.com/v1"
DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"


def read_csv(path: Path) -> list[dict]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def prompt_stem(row: dict) -> str:
    return f"{row['ticker'].lower()}_{row['construct']}_{row['condition']}"


def split_filter(value: str) -> set[str]:
    if not value:
        return set()
    return {item.strip() for item in value.split(",") if item.strip()}


def filter_rows(rows: list[dict], args: argparse.Namespace) -> list[dict]:
    filters = {
        "sample_role": split_filter(args.roles),
        "ticker": split_filter(args.tickers),
        "construct": split_filter(args.constructs),
        "condition": split_filter(args.conditions),
    }
    selected = []
    for row in rows:
        keep = True
        for field, allowed in filters.items():
            if allowed and row.get(field, "") not in allowed:
                keep = False
                break
        if keep:
            selected.append(row)
    return selected


def extract_output_text(payload: dict) -> str:
    if isinstance(payload.get("response"), str):
        return payload["response"].strip()

    if isinstance(payload.get("output_text"), str):
        return payload["output_text"].strip()

    texts = []
    for item in payload.get("output", []) or []:
        for content in item.get("content", []) or []:
            if content.get("type") in {"output_text", "text"} and content.get("text"):
                texts.append(content["text"])
    if texts:
        return "\n".join(texts).strip()

    choices = payload.get("choices", [])
    if choices:
        message = choices[0].get("message", {})
        if message.get("content"):
            return str(message["content"]).strip()

    return ""


def call_responses_api(base_url: str, api_key: str, model: str, prompt: str, temperature: float) -> dict:
    url = f"{base_url.rstrip('/')}/responses"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    body = {
        "model": model,
        "input": prompt,
        "temperature": temperature,
    }
    response = requests.post(url, headers=headers, json=body, timeout=180)
    response.raise_for_status()
    return response.json()


def call_ollama_api(base_url: str, model: str, prompt: str, temperature: float) -> dict:
    url = f"{base_url.rstrip('/')}/api/generate"
    body = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature},
    }
    response = requests.post(url, json=body, timeout=600)
    response.raise_for_status()
    return response.json()


def run(args: argparse.Namespace) -> int:
    processed = Path("data/processed")
    manifest_path = processed / "retrieval_contexts" / "context_manifest.csv"
    rows = read_csv(manifest_path)
    rows = filter_rows(rows, args)

    if args.limit:
        rows = rows[: args.limit]

    provider = args.provider
    api_key = os.environ.get("OPENAI_API_KEY", "")
    model = args.model or os.environ.get("LLM_MODEL", "")
    if provider == "openai":
        model = model or os.environ.get("OPENAI_MODEL", "")
        base_url = args.base_url or os.environ.get("OPENAI_BASE_URL", DEFAULT_OPENAI_BASE_URL)
    else:
        model = model or os.environ.get("OLLAMA_MODEL", "")
        base_url = args.base_url or os.environ.get("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL)
    temperature = args.temperature
    access_time = datetime.now(timezone.utc).isoformat()

    output_root = processed / "llm_outputs"
    if args.run_label:
        output_root = output_root / args.run_label
    raw_root = output_root / "raw_json"
    text_root = output_root / "text"
    manifest_rows = []

    if not args.dry_run and provider == "openai" and not api_key:
        raise SystemExit("OPENAI_API_KEY is missing. Set it before running without --dry-run.")
    if not args.dry_run and not model:
        raise SystemExit("Model is missing. Set LLM_MODEL, OPENAI_MODEL/OLLAMA_MODEL, or pass --model before running without --dry-run.")

    for index, row in enumerate(rows, start=1):
        stem = prompt_stem(row)
        prompt_path = Path(row["prompt_file"])
        prompt = prompt_path.read_text(encoding="utf-8")
        text_path = text_root / f"{stem}_output.txt"
        raw_path = raw_root / f"{stem}_raw.json"

        status = "pending"
        error = ""
        output_chars = 0

        if args.dry_run:
            status = "dry_run"
        elif text_path.exists() and raw_path.exists() and not args.force:
            status = "skipped_existing"
            output_chars = len(text_path.read_text(encoding="utf-8"))
        else:
            try:
                if provider == "openai":
                    payload = call_responses_api(base_url, api_key, model, prompt, temperature)
                else:
                    payload = call_ollama_api(base_url, model, prompt, temperature)
                output_text = extract_output_text(payload)
                write_json(raw_path, payload)
                write_text(text_path, output_text)
                output_chars = len(output_text)
                status = "completed"
                time.sleep(args.sleep)
            except Exception as exc:
                status = "error"
                error = repr(exc)

        manifest_rows.append(
            {
                "run_id": f"RUN-{index:03d}",
                "ticker": row["ticker"],
                "company": row["company"],
                "sample_role": row.get("sample_role", ""),
                "construct": row["construct"],
                "condition": row["condition"],
                "condition_label": row["condition_label"],
                "prompt_file": row["prompt_file"],
                "context_file": row["context_file"],
                "context_word_count": row["context_word_count"],
                "output_text_file": str(text_path).replace("\\", "/"),
                "raw_json_file": str(raw_path).replace("\\", "/"),
                "status": status,
                "provider": provider,
                "model": model or "missing",
                "base_url": base_url,
                "temperature": temperature,
                "access_time_utc": access_time,
                "output_chars": output_chars,
                "error": error,
            }
        )
        print(f"{index:02d}/{len(rows)} {stem}: {status}")

    manifest_name = "run_manifest_dry_run.csv" if args.dry_run else "run_manifest.csv"
    write_csv(
        output_root / manifest_name,
        manifest_rows,
        [
            "run_id",
            "ticker",
            "company",
            "sample_role",
            "construct",
            "condition",
            "condition_label",
            "prompt_file",
            "context_file",
            "context_word_count",
            "output_text_file",
            "raw_json_file",
            "status",
            "provider",
            "model",
            "base_url",
            "temperature",
            "access_time_utc",
            "output_chars",
            "error",
        ],
    )

    summary = ["# Phase 6 LLM Output Run Summary", ""]
    summary.append(f"- Dry run: `{args.dry_run}`")
    summary.append(f"- Provider: `{provider}`")
    summary.append(f"- Rows: {len(manifest_rows)}")
    summary.append(f"- Model: `{model or 'missing'}`")
    summary.append(f"- Base URL: `{base_url}`")
    summary.append(f"- Temperature: `{temperature}`")
    summary.append(f"- Access time UTC: `{access_time}`")
    summary.append("")
    summary.append("## Status Counts")
    summary.append("")
    counts = {}
    for row in manifest_rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    for status, count in sorted(counts.items()):
        summary.append(f"- {status}: {count}")
    write_text(output_root / ("run_summary_dry_run.md" if args.dry_run else "run_summary.md"), "\n".join(summary))

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Phase 6 prompt files through an OpenAI-compatible or local Ollama model.")
    parser.add_argument("--provider", choices=["openai", "ollama"], default=os.environ.get("LLM_PROVIDER", "openai"))
    parser.add_argument("--dry-run", action="store_true", help="Validate inputs and write a dry-run manifest without API calls.")
    parser.add_argument("--model", default="", help="Model identifier. Defaults to LLM_MODEL, then provider-specific environment variables.")
    parser.add_argument("--base-url", default="", help="Provider base URL. Defaults to OPENAI_BASE_URL or OLLAMA_BASE_URL.")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--limit", type=int, default=0, help="Optional number of prompts to run from the manifest.")
    parser.add_argument("--roles", default="", help="Comma-separated sample_role filter, e.g. bounded_extension.")
    parser.add_argument("--tickers", default="", help="Comma-separated ticker filter.")
    parser.add_argument("--constructs", default="", help="Comma-separated construct filter.")
    parser.add_argument("--conditions", default="", help="Comma-separated condition filter.")
    parser.add_argument("--run-label", default="", help="Optional subdirectory under data/processed/llm_outputs for this run.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Seconds to sleep between API calls.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(run(parse_args()))
