# Taxonomy

## Directory Map

- `src/prompts/`: source prompt files compiled into the palette.
- `src/blocks/`: reusable macro blocks referenced by prompts.
- `src/legacy/`: preserved historical palette source.
- `scripts/`: build and lint tooling.
- `docs/`: conventions, process, and handoff docs.

## Prompt Naming

Use lexicographic naming so execution order is stable.

- Pattern: `NN_topic__action.md`
- Examples:
  - `00_bootstrap__register_roles.md`
  - `10_plan__decompose.md`
  - `20_impl__review.md`

## Prompt Intent Classes

- `bootstrap`: role election, thread registration, ownership setup.
- `plan`: scope, sequencing, risk controls, acceptance criteria.
- `implement`: execution handoffs for owned file surfaces.
- `review`: validation, regressions, final convergence.
- `release`: push/PR/checklist and operational verification.

## Required Markers

All prompts must include:

- Heading starting with `## `
- `### Goal`, `### Inputs`, `### Instructions`, `### Output`
- `{{PREAMBLE}}` and `{{REPORTBACK}}`
