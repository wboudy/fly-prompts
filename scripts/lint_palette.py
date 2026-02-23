#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from prompt_contract import (
    MAX_PROMPT_BYTES,
    REQUIRED_PLACEHOLDERS,
    REQUIRED_SECTIONS,
    collect_prompts,
    first_non_empty_line,
)

ROOT = Path(__file__).resolve().parent.parent
BLOCKS_DIR = ROOT / "src" / "blocks"
PROMPTS_DIR = ROOT / "src" / "prompts"

REQUIRED_BLOCK_FILES = (
    BLOCKS_DIR / "preamble.md",
    BLOCKS_DIR / "reportback.md",
)


def lint() -> list[str]:
    errors: list[str] = []

    for block_file in REQUIRED_BLOCK_FILES:
        if not block_file.exists():
            errors.append(f"Missing required block file: {block_file}")

    prompt_records, prompt_errors = collect_prompts(PROMPTS_DIR, ROOT)
    errors.extend(prompt_errors)

    if not prompt_records:
        errors.append(f"No prompt files found in {PROMPTS_DIR}")
        return errors

    included_keys: dict[str, str] = {}
    included_count = 0

    for record in prompt_records:
        text = record.body
        first_line = first_non_empty_line(text)

        if not first_line.startswith("## "):
            errors.append(
                f"{record.path}: first non-empty line must be a prompt heading starting with '## '"
            )

        for placeholder in REQUIRED_PLACEHOLDERS:
            if placeholder not in text:
                errors.append(f"{record.path}: missing placeholder {placeholder}")

        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{record.path}: missing required section heading {section}")

        size = len(text.encode("utf-8"))
        if size > MAX_PROMPT_BYTES:
            errors.append(
                f"{record.path}: exceeds size budget ({size} bytes > {MAX_PROMPT_BYTES} bytes)"
            )

        if record.include_in_palette:
            included_count += 1
            if record.command_key in included_keys:
                errors.append(
                    f"{record.path}: duplicate command_key '{record.command_key}' also used by {included_keys[record.command_key]}"
                )
            else:
                included_keys[record.command_key] = record.rel_path

    if included_count == 0:
        errors.append("No prompts are marked include_in_palette: true.")

    return errors


def main() -> int:
    errors = lint()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    prompt_count = len([p for p in PROMPTS_DIR.glob("*.md") if p.is_file()])
    print(f"Lint passed for {prompt_count} prompt file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
