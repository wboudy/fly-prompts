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

## Agent-Friendliness Principles

An **agent-friendly prompt** minimizes ambiguity and maximizes autonomous completion. Rate your prompt against these criteria:

### Core Principles

| Principle | Description | Example |
|-----------|-------------|---------|
| **Concrete commands** | Agents execute better than they infer | `bd ready` not "check tasks" |
| **Explicit structure** | XML tags/numbered steps parse cleanly | `<steps>1. 2. 3.</steps>` |
| **Scoped autonomy** | Clear "do this yourself" vs "escalate" boundaries | "Fix if <10 lines, else create bead" |
| **Failure recovery** | What to do when blocked, not just the happy path | "If no response in 15min, proceed" |
| **Measurable completion** | "Done when X" not "improve things" | "Done when test suite passes" |
| **Tool-aware** | References actual CLI tools in the environment | `cass`, `bd`, `rg`, `ubs` |
| **Output templates** | Exact format prevents drift | Markdown tables, not prose |
| **Constraint blocks** | "Do NOT" rules prevent common failure modes | 3-5 explicit constraints |

### What Makes Prompts Fail

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Vague quantities | "Generate many ideas" | "Generate 20-30 ideas minimum" |
| Abstract scoring | "Rate impact 1-10" | Provide anchors: "10 = production outage fix" |
| Missing commands | "Check for prior art" | `cass search "<keywords>" --limit 10` |
| No timeout protocol | "Wait for confirmation" | "If no response in 15min, proceed with note" |
| Prose output | "Describe what you found" | Provide table template |
| No failure path | Happy path only | "If blocked, create spike bead and continue" |

### Agent-Friendliness Checklist

Rate each criterion 0-2 (0=missing, 1=partial, 2=strong). Target score: 14+/18.

- [ ] **Discovery commands** — Concrete bash/CLI commands to gather context
- [ ] **Numbered steps** — Clear sequence, not prose paragraphs
- [ ] **Scoring anchors** — If rating anything, provide concrete anchor points
- [ ] **Output template** — Exact format (tables, structured markdown)
- [ ] **Timeout/fallback** — What to do when blocked or no response
- [ ] **Constraint block** — 3-5 explicit "Do NOT" rules
- [ ] **Tool references** — Uses actual tools: `bd`, `br`, `cass`, `rg`, `ubs`, `ntm`
- [ ] **Examples** — At least one concrete example (Agent Mail message, command output)
- [ ] **Completion criteria** — Explicit "done when" condition

### Example: Good vs Bad

**Bad (vague, no commands, no output format):**
```
Review the codebase for issues. Look for bugs and problems.
Report what you find.
```

**Good (concrete, structured, tool-aware):**
```
Discovery:
  git log --oneline --since="3 days ago" | head -20
  rg "TODO|FIXME" --type py -c | sort -t: -k2 -nr | head -10

Workflow:
1. Run discovery commands
2. For each file, check imports and trace execution
3. Classify issues by severity (P0-P3)
4. Fix P0/P1 immediately, create beads for P2/P3

Output:
| File:Line | Severity | Issue | Action |
|-----------|----------|-------|--------|

Constraints:
- Do NOT skip test files
- Do NOT rewrite working code for style
```

## Author Checklist

- [ ] Prompt filename has a sortable prefix (for deterministic order).
- [ ] Frontmatter includes `command_key`, `stage`, `include_in_palette`, and `title`.
- [ ] Required headings and placeholders are present.
- [ ] Prompt is concise and under size budget.
- [ ] `make lint`, `make build`, and `make validate` pass locally.
- [ ] Agent-friendliness score is 14+/18 (see checklist above).
