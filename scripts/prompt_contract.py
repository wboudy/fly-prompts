#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

PROMPT_FILENAME_RE = re.compile(
    r"^(?P<order>\d{2})_(?P<topic>[a-z0-9]+)__(?P<slug>[a-z0-9_]+)\.md$"
)
COMMAND_KEY_RE = re.compile(
    r"^/(?P<stage>[a-z0-9][a-z0-9-]*)/(?P<slug>[a-z0-9][a-z0-9-]*)$"
)
STAGE_ALIASES = {
    "impl": "implement",
}

REQUIRED_PLACEHOLDERS = ("{{PREAMBLE}}", "{{REPORTBACK}}")
REQUIRED_SECTIONS = ("### Goal", "### Inputs", "### Instructions", "### Output")
MAX_PROMPT_BYTES = 12_000


@dataclass(frozen=True)
class PromptRecord:
    path: Path
    rel_path: str
    order: int
    file_topic: str
    file_slug: str
    command_key: str
    stage: str
    include_in_palette: bool
    metadata_title: str
    title: str
    body: str


def first_non_empty_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line
    return ""


def _parse_frontmatter(text: str, path: Path) -> tuple[dict[str, object], str, list[str]]:
    errors: list[str] = []

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{path}: missing frontmatter block starting with '---'")
        return {}, text, errors

    closing_index: int | None = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            closing_index = idx
            break

    if closing_index is None:
        errors.append(f"{path}: frontmatter block is not closed with '---'")
        return {}, text, errors

    metadata_lines = lines[1:closing_index]
    body = "\n".join(lines[closing_index + 1 :])

    metadata: dict[str, object] = {}
    for idx, raw_line in enumerate(metadata_lines, start=2):
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            errors.append(f"{path}:{idx}: invalid frontmatter line (expected key: value)")
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not key:
            errors.append(f"{path}:{idx}: missing frontmatter key")
            continue

        lowered = value.lower()
        if lowered in {"true", "false"}:
            parsed_value: object = lowered == "true"
        else:
            parsed_value = value.strip("\"'")

        metadata[key] = parsed_value

    return metadata, body, errors


def _parse_prompt(path: Path, root: Path) -> tuple[PromptRecord | None, list[str]]:
    errors: list[str] = []

    filename_match = PROMPT_FILENAME_RE.match(path.name)
    if not filename_match:
        errors.append(
            f"{path}: filename must match NN_topic__slug.md "
            "(example: 10_plan__create_beads.md)"
        )
        return None, errors

    text = path.read_text(encoding="utf-8")
    metadata, body, metadata_errors = _parse_frontmatter(text, path)
    errors.extend(metadata_errors)

    command_key_raw = metadata.get("command_key")
    stage_raw = metadata.get("stage")
    include_raw = metadata.get("include_in_palette")
    metadata_title_raw = metadata.get("title")

    if not isinstance(command_key_raw, str) or not command_key_raw:
        errors.append(f"{path}: frontmatter requires non-empty string 'command_key'")

    if not isinstance(stage_raw, str) or not stage_raw:
        errors.append(f"{path}: frontmatter requires non-empty string 'stage'")

    if not isinstance(include_raw, bool):
        errors.append(f"{path}: frontmatter requires boolean 'include_in_palette' (true/false)")
    if not isinstance(metadata_title_raw, str) or not metadata_title_raw:
        errors.append(f"{path}: frontmatter requires non-empty string 'title'")

    command_key = command_key_raw if isinstance(command_key_raw, str) else ""
    stage = stage_raw if isinstance(stage_raw, str) else ""
    include_in_palette = include_raw if isinstance(include_raw, bool) else False
    metadata_title = metadata_title_raw if isinstance(metadata_title_raw, str) else ""

    file_topic = filename_match.group("topic")
    normalized_file_stage = STAGE_ALIASES.get(file_topic, file_topic)
    if stage and stage != normalized_file_stage:
        errors.append(
            f"{path}: stage '{stage}' must match filename stage '{normalized_file_stage}'"
        )

    command_match = COMMAND_KEY_RE.match(command_key)
    if command_key and not command_match:
        errors.append(
            f"{path}: command_key must match '/stage/slug' using lowercase letters, numbers, and hyphens"
        )

    if command_match and stage and command_match.group("stage") != stage:
        errors.append(
            f"{path}: stage '{stage}' must match command_key stage '{command_match.group('stage')}'"
        )

    file_slug = filename_match.group("slug")
    expected_key_slug = file_slug.replace("_", "-")
    expected_key = f"/{normalized_file_stage}/{expected_key_slug}"
    if command_key and command_key != expected_key:
        errors.append(f"{path}: command_key must be '{expected_key}'")

    if command_match and command_match.group("slug") != expected_key_slug:
        errors.append(
            f"{path}: command_key slug '{command_match.group('slug')}' must match filename slug '{expected_key_slug}'"
        )

    first_line = first_non_empty_line(body)
    if not first_line.startswith("## "):
        errors.append(f"{path}: first non-empty line after frontmatter must start with '## '")
    heading_title = first_line[3:].strip() if first_line.startswith("## ") else ""
    if metadata_title and heading_title and metadata_title != heading_title:
        errors.append(
            f"{path}: frontmatter title '{metadata_title}' must match heading title '{heading_title}'"
        )

    if errors:
        return None, errors

    rel_path = path.relative_to(root).as_posix()
    title = first_line[3:].strip()

    return (
        PromptRecord(
            path=path,
            rel_path=rel_path,
            order=int(filename_match.group("order")),
            file_topic=file_topic,
            file_slug=file_slug,
            command_key=command_key,
            stage=stage,
            include_in_palette=include_in_palette,
            metadata_title=metadata_title,
            title=title,
            body=body,
        ),
        [],
    )


def collect_prompts(prompts_dir: Path, root: Path) -> tuple[list[PromptRecord], list[str]]:
    records: list[PromptRecord] = []
    errors: list[str] = []

    for path in sorted(p for p in prompts_dir.glob("*.md") if p.is_file()):
        record, parse_errors = _parse_prompt(path, root)
        errors.extend(parse_errors)
        if record is not None:
            records.append(record)

    records.sort(key=lambda record: (record.order, record.rel_path))
    return records, errors
