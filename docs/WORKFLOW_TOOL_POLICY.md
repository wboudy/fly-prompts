# Workflow Tool Policy

Stage-scoped tool usage policy for prompt commands.

## Bootstrap

- Required: `ntm`
- Optional: `cass`, `cm`, `bd`/`br`, `bv`
- Triggers:
  - If selecting work, run `bd ready` or `br ready`.
  - If MCP Agent Mail tools are unavailable, use `ntm send` for coordination updates.

## Plan

- Required: `cass` and one issue tracker (`bd` or `br`)
- Optional: `cm`, `bv`, `apr`
- Triggers:
  - If dependency complexity grows, run `bv --robot-plan` and `bv --robot-insights`.
  - If creating tasks, use `bd create ...` or `br create ...` consistently for the repo.

## Implement

- Required: one issue tracker (`bd` or `br`) and `ntm`
- Optional: `cass`, `cm`, `ubs`, `dcg`
- Triggers:
  - Before commit readiness checks, run `ubs --staged` (or `ubs .` for full scan).
  - For dangerous operations, gate via `slb run "<command>"`.

## Review

- Required: `bv` robot modes and `ntm`
- Optional: `cass`, `ubs`, `dcg`
- Triggers:
  - Use `bv --robot-triage` for ranking/prioritization.
  - Use `bv --robot-insights` for dependency/cycle checks.
  - Run `ubs --staged` for changed-file scan before approval.

## Release

- Required: `ubs` and `ntm`
- Optional: `slb`, `bd`/`br`, `ru`
- Triggers:
  - Run `ubs --staged` (or `ubs .`) before release sign-off.
  - For risky commands, require `slb run "<command>"`.

## Incident

- Required: `cass`, `ubs`, and one issue tracker (`bd` or `br`)
- Optional: `ntm`, `cm`, `bv`
- Triggers:
  - Use `ubs <path>` for targeted triage scans.
  - Track remediation in `bd` or `br` and broadcast status via `ntm send`.

## MCP Note

- `agent-mail` / `mcp_agent_mail` binaries are MCP server entrypoints, not shell workflow CLIs.
- Prefer MCP Agent Mail tool calls when available; use `ntm send` as shell fallback.
