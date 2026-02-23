# fly-prompts

Prompt source and build pipeline for a generated NTM command palette.

## Layout

- `src/prompts/`: editable prompt source files.
- `src/blocks/`: reusable macro blocks used by prompts.
- `docs/legacy/`: non-runnable archive/reference from legacy conversion.
- `scripts/`: lint/build tooling.
- `docs/`: conventions and handoff docs.

## Edit Workflow

1. Edit prompt files in `src/prompts/` and shared blocks in `src/blocks/`.
2. Run `make lint` to validate prompt schema.
3. Run `make build` to generate `./command_palette.md`.
4. Run `make validate` to verify palette/prompt alignment.

## Build and Lint

```bash
make lint
make build
make validate
```

- `make lint` enforces metadata + heading/section/placeholder/size rules.
- `make build` expands macros and writes a generated command index.
- `make validate` checks prompt metadata against the generated command index in `command_palette.md`.

## Palette Contract

- Source of truth: `src/prompts/*.md` frontmatter.
- Required prompt metadata:
  - `command_key`
  - `stage`
  - `include_in_palette`
  - `title`
- Filename rule: `NN_stage__slug.md`.
- Deterministic key rule: `command_key` must equal `/<normalized-stage>/<slug-kebab>`.
  - Stage normalization currently maps `impl` -> `implement`.
- Prompts with `include_in_palette: true` must appear in `command_palette.md` generated index.
- No legacy runnable commands: palette output is prompt-file-only.

## Load in NTM

NTM CLI behavior varies by version. Use the approach supported by your install:

- If your NTM supports file loading:
  - `ntm palette load command_palette.md`
- Otherwise:
  - Open the NTM palette TUI and select repo-root `./command_palette.md` (auto-discovery).
- If uncertain, run `ntm --help` and `ntm palette --help` first.

## Notes

- Build output path: `./command_palette.md`
- Installed tool inventory: `docs/INSTALLED_TOOLS.md`
- Copy/paste quick reference: `docs/TOOLS_QUICKREF.md`
- Stage tool policy: `docs/WORKFLOW_TOOL_POLICY.md`
