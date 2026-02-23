---
command_key: /bootstrap/prepare-handoff
stage: bootstrap
include_in_palette: true
title: "Prepare Handoff"
---

## Prepare Handoff

### Goal
Execute the legacy "Prepare Handoff" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Commit all code changes with clear messages
- Run `bd sync` to save bead state
- Update any in_progress beads with status comments
- Write a handoff document (see format below)
- Post handoff to MCP Agent Mail (MCP tool)
- Tag the next agent if known
- OAuth2 login flow (bd-a1b2c3)
- Token refresh middleware

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
