# Prompt Style Guide

This repo compiles prompts from `src/prompts/` and shared blocks from `src/blocks/` into `./command_palette.md`.

## Required Prompt Schema

Every prompt file must pass these linter requirements:

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

## Build Contract

- `make lint` runs `scripts/lint_palette.py`.
- `make build` runs `scripts/build_palette.py`.
- Prompt files are loaded in lexicographic filename order.
- Placeholders are expanded from:
  - `src/blocks/preamble.md`
  - `src/blocks/reportback.md`
- Legacy content is appended from `src/legacy/command_palette.legacy.md`.

## Author Checklist

- [ ] Prompt filename has a sortable prefix (for deterministic order).
- [ ] Required headings and placeholders are present.
- [ ] Prompt is concise and under size budget.
- [ ] `make lint` and `make build` pass locally.
