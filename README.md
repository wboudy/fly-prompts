# fly-prompts

Prompt source and build pipeline for a generated NTM command palette.

## Layout

- `src/prompts/`: editable prompt source files.
- `src/blocks/`: reusable macro blocks used by prompts.
- `src/legacy/command_palette.legacy.md`: preserved legacy palette content.
- `scripts/`: lint/build tooling.
- `docs/`: conventions and handoff docs.

## Edit Workflow

1. Edit prompt files in `src/prompts/` and shared blocks in `src/blocks/`.
2. Run `make lint` to validate prompt schema.
3. Run `make build` to generate `./command_palette.md`.

## Build and Lint

```bash
make lint
make build
```

- `make lint` enforces heading/section/placeholder/size rules.
- `make build` expands macros and appends legacy content.

## Load in NTM

NTM CLI behavior varies by version. Use the approach supported by your install:

- If your NTM supports file loading:
  - `ntm palette load command_palette.md`
- Otherwise:
  - Open the NTM palette TUI and select repo-root `./command_palette.md` (auto-discovery).
- If uncertain, run `ntm --help` and `ntm palette --help` first.

## Notes

- Build output path: `./command_palette.md`
- Legacy source path: `src/legacy/command_palette.legacy.md`
