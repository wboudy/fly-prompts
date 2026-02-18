#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCKS_DIR = ROOT / "src" / "blocks"
PROMPTS_DIR = ROOT / "src" / "prompts"

REQUIRED_BLOCK_FILES = (
    BLOCKS_DIR / "preamble.md",
    BLOCKS_DIR / "reportback.md",
)
REQUIRED_PLACEHOLDERS = ("{{PREAMBLE}}", "{{REPORTBACK}}")
REQUIRED_SECTIONS = ("### Goal", "### Inputs", "### Instructions", "### Output")
MAX_PROMPT_BYTES = 12_000


def _prompt_files() -> list[Path]:
    return sorted(p for p in PROMPTS_DIR.glob("*.md") if p.is_file())


def _first_non_empty_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line
    return ""


def lint() -> list[str]:
    errors: list[str] = []

    for block_file in REQUIRED_BLOCK_FILES:
        if not block_file.exists():
            errors.append(f"Missing required block file: {block_file}")

    prompt_files = _prompt_files()
    if not prompt_files:
        errors.append(f"No prompt files found in {PROMPTS_DIR}")
        return errors

    for prompt_file in prompt_files:
        text = prompt_file.read_text(encoding="utf-8")
        first_line = _first_non_empty_line(text)

        if not first_line.startswith("## "):
            errors.append(
                f"{prompt_file}: first non-empty line must be a prompt heading starting with '## '"
            )

        for placeholder in REQUIRED_PLACEHOLDERS:
            if placeholder not in text:
                errors.append(f"{prompt_file}: missing placeholder {placeholder}")

        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{prompt_file}: missing required section heading {section}")

        size = len(text.encode("utf-8"))
        if size > MAX_PROMPT_BYTES:
            errors.append(
                f"{prompt_file}: exceeds size budget ({size} bytes > {MAX_PROMPT_BYTES} bytes)"
            )

    return errors


def main() -> int:
    errors = lint()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    prompt_count = len(_prompt_files())
    print(f"Lint passed for {prompt_count} prompt file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
