# Prompt Style Guide

This repo compiles prompts from `src/prompts/` and shared blocks from `src/blocks/` into `./command_palette.md`.

## Required Prompt Schema

Every prompt file must pass these linter requirements:

- File starts with YAML frontmatter containing:
  - `command_key`
  - `stage`
  - `include_in_palette`
  - `title`
- First non-empty line starts with `## `.
- Include section headings:
  - `### Goal`
  - `### Inputs`
  - `### Instructions`
  - `### Output`
- Include placeholders:
  - `{{PREAMBLE}}`
  - `{{REPORTBACK}}`
- Stay within size budget: `12000` bytes UTF-8 per prompt file.

## Minimal Template

```md
---
command_key: /plan/decompose
stage: plan
include_in_palette: true
title: "Prompt Title"
---

## Prompt Title

### Goal
Describe the intended outcome.

### Inputs
- Inputs required by the agent.

### Instructions
{{PREAMBLE}}

Task-specific instructions.

{{REPORTBACK}}

### Output
- Expected artifacts and status format.
```

## Command Key Contract

- Filename format: `NN_stage__slug.md`.
- `stage` is derived from filename stage token (`impl` normalizes to `implement`).
- `command_key` is deterministic from filename:
- `/<normalized-stage>/<slug-with-hyphens>`
- Example: `30_impl__claim_reserve_code_ubs_close.md` -> `/implement/claim-reserve-code-ubs-close`
- `include_in_palette: true` means the prompt must appear in generated command index.

## How Prompt Files Become Command Palette Entries

- Source of truth: prompt files in `src/prompts/`.
- Naming rule: `NN_stage__slug.md` keeps deterministic load order.
- Required metadata fields in frontmatter:
  - `command_key`
  - `stage`
  - `include_in_palette`
  - `title`
- Deterministic mapping:
  - stage: filename stage token, with `impl` normalized to `implement`
  - key: `/<stage>/<slug-with-hyphens>`
- To add a new prompt:
  - create `src/prompts/NN_stage__slug.md` with required frontmatter and schema headings
  - run `make build`
  - run `make validate`

## Build Contract

- `make lint` runs `scripts/lint_palette.py`.
- `make build` runs `scripts/build_palette.py`.
- `make validate` runs `scripts/validate_palette_alignment.py`.
- Prompt files are loaded in lexicographic filename order.
- Placeholders are expanded from:
  - `src/blocks/preamble.md`
  - `src/blocks/reportback.md`
- Palette output is prompt-file-only (no emitted legacy section).

## Author Checklist

- [ ] Prompt filename has a sortable prefix (for deterministic order).
- [ ] Frontmatter includes `command_key`, `stage`, `include_in_palette`, and `title`.
- [ ] Required headings and placeholders are present.
- [ ] Prompt is concise and under size budget.
- [ ] `make lint`, `make build`, and `make validate` pass locally.
