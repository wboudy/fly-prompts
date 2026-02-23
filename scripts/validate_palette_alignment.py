#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

from prompt_contract import collect_prompts

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "src" / "prompts"
PALETTE_PATH = ROOT / "command_palette.md"

INDEX_BEGIN = "<!-- BEGIN GENERATED COMMAND INDEX -->"
INDEX_END = "<!-- END GENERATED COMMAND INDEX -->"


def _parse_palette_index(text: str) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    pattern = re.compile(
        rf"{re.escape(INDEX_BEGIN)}\s*```json\s*(?P<payload>\[.*?\])\s*```\s*{re.escape(INDEX_END)}",
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        errors.append(
            "F) command_palette.md is missing the generated command index block; source-of-truth is ambiguous."
        )
        return [], errors

    payload = match.group("payload")
    try:
        parsed = json.loads(payload)
    except json.JSONDecodeError as error:
        errors.append(f"F) generated command index JSON is invalid: {error}")
        return [], errors

    if not isinstance(parsed, list):
        errors.append("F) generated command index must be a JSON array.")
        return [], errors

    entries: list[dict[str, str]] = []
    for idx, item in enumerate(parsed, start=1):
        if not isinstance(item, dict):
            errors.append(f"F) index entry {idx} must be an object.")
            continue
        entry_errors = False
        for field in ("command_key", "stage", "title", "source"):
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"F) index entry {idx} missing string field '{field}'.")
                entry_errors = True
        if entry_errors:
            continue
        entries.append(
            {
                "command_key": item["command_key"],
                "stage": item["stage"],
                "title": item["title"],
                "source": item["source"],
            }
        )
    return entries, errors


def validate() -> tuple[list[str], list[dict[str, str]]]:
    errors: list[str] = []
    records, prompt_errors = collect_prompts(PROMPTS_DIR, ROOT)
    errors.extend(f"E) {error}" for error in prompt_errors)

    expected_entries = [
        {
            "command_key": record.command_key,
            "stage": record.stage,
            "title": record.title,
            "source": record.rel_path,
        }
        for record in records
        if record.include_in_palette
    ]

    prompt_key_to_source: dict[str, str] = {}
    for entry in expected_entries:
        key = entry["command_key"]
        if key in prompt_key_to_source:
            errors.append(
                f"D) duplicate command_key '{key}' in prompts: {prompt_key_to_source[key]} and {entry['source']}."
            )
        else:
            prompt_key_to_source[key] = entry["source"]

    if not PALETTE_PATH.exists():
        errors.append("F) command_palette.md does not exist. Run make build.")
        return errors, expected_entries

    palette_text = PALETTE_PATH.read_text(encoding="utf-8")
    if "## Legacy Palette" in palette_text:
        errors.append(
            "F) command_palette.md still contains a 'Legacy Palette' section; "
            "palette must be generated strictly from prompt files."
        )
    palette_entries, palette_errors = _parse_palette_index(palette_text)
    errors.extend(palette_errors)
    if palette_errors:
        return errors, expected_entries

    palette_key_to_source: dict[str, str] = {}
    for entry in palette_entries:
        key = entry["command_key"]
        source = entry["source"]
        if key in palette_key_to_source:
            errors.append(
                f"D) duplicate command_key '{key}' in palette index: {palette_key_to_source[key]} and {source}."
            )
        else:
            palette_key_to_source[key] = source

    expected_by_source = {entry["source"]: entry for entry in expected_entries}
    palette_by_source = {entry["source"]: entry for entry in palette_entries}

    for source, palette_entry in palette_by_source.items():
        source_path = ROOT / source
        if not source_path.exists():
            errors.append(
                f"A) palette references missing prompt file '{source}' via {palette_entry['command_key']}."
            )
        elif source not in expected_by_source:
            errors.append(
                f"A) palette references prompt '{source}' that is not marked include_in_palette=true."
            )

    for source, expected_entry in expected_by_source.items():
        if source not in palette_by_source:
            errors.append(
                f"B) prompt '{source}' ({expected_entry['command_key']}) is not referenced by palette index."
            )

    for source in sorted(set(expected_by_source) & set(palette_by_source)):
        expected_entry = expected_by_source[source]
        palette_entry = palette_by_source[source]
        if expected_entry["command_key"] != palette_entry["command_key"]:
            errors.append(
                f"C) key mismatch for '{source}': prompt={expected_entry['command_key']} palette={palette_entry['command_key']}."
            )

    return errors, expected_entries


def main() -> int:
    errors, expected_entries = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Alignment OK: {len(expected_entries)} command(s) in sync.")
    for entry in expected_entries:
        print(f"OK: {entry['command_key']} -> {entry['source']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
