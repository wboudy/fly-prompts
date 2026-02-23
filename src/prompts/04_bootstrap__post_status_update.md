---
command_key: /bootstrap/post-status-update
stage: bootstrap
include_in_palette: true
title: "Post Status Update"
---

## Post Status Update

### Goal
Execute the legacy "Post Status Update" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Working on: [current bead or task]
- Progress: [percentage or milestone]
- Blockers: [none, or list]
- ETA: [estimate if known]
- Need: [nothing, or specific request]
- Working on: bd-x7y8z9 (rate limiting middleware)
- Progress: 60% — core logic done, writing tests
- Blockers: none

Stage Tool Policy:
- Required: `ntm`
- Optional: `cass`, `cm`, `bd`/`br`, `bv`
- Triggers:
  - If selecting work, run `bd ready` or `br ready`.
  - If MCP Agent Mail tools are unavailable, coordinate via `ntm send <session> --all "<message>"`.
- Use installed-tool commands from `docs/TOOLS_QUICKREF.md` only.

Coordination Note:
- `agent-mail` / `mcp_agent_mail` are MCP server binaries, not shell workflow CLIs.
- Prefer MCP Agent Mail tools when available; otherwise use `ntm send` fallback.

{{REPORTBACK}}

### Output
- What was done, what is next, and who owns the next action.
- Key commands/checks executed and their outcomes.
- Any blockers and explicit handoff details.
