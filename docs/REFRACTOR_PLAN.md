# Refactor Plan

## Delivery Strategy

Ship in small, reviewable PRs with deterministic checks.

1. Scaffold
- Add `scripts/build_palette.py`, `scripts/lint_palette.py`, `Makefile`.
- Move root palette to `src/legacy/command_palette.legacy.md`.
- Acceptance: `make lint`, `make build`.

2. Docs
- Add style guide, taxonomy, state machine, handoff, and plan docs.
- Update `README.md` with build/load workflow.
- Acceptance: docs align with linter/build contract.

3. Prompt Migration
- Add/normalize prompts under `src/prompts/`.
- Keep macro use consistent with block files.
- Acceptance: linter passes for all prompt files.

4. Release Validation
- Rebuild palette and inspect generated diff.
- Run quick operator verification in NTM.
- Acceptance: build artifact loads and command list is intact.

## Acceptance Checks Per PR

- Run `make lint`.
- Run `make build`.
- Confirm `./command_palette.md` regeneration is intentional.
- Confirm legacy content remains in `src/legacy/command_palette.legacy.md`.

## NTM Quick Test

Use your local NTM command help to confirm exact subcommands:

- `ntm --help`
- `ntm palette --help`

NTM CLI behavior varies by version. Load the generated palette with whichever path your install supports:

- If your NTM supports file loading: `ntm palette load command_palette.md`
- Otherwise: open the NTM palette TUI and select repo-root `./command_palette.md` (auto-discovery).
