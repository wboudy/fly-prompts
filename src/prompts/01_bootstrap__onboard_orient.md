---
command_key: /bootstrap/onboard-orient
stage: bootstrap
include_in_palette: true
title: "Onboard & Orient"
---

## Onboard & Orient

### Goal
Execute the legacy "Onboard & Orient" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Read AGENTS.md and README.md in full — understand project conventions
- Register with MCP Agent Mail (MCP tool) using your pane name (e.g., cc_1)
- Check your inbox for messages from other agents or the overseer
- Search project history: `cass search "<project name>" --days 7 --limit 5`
- Run `bd ready` to see available work — do NOT claim yet
- Send a brief intro message via MCP Agent Mail (MCP tool) announcing your presence
- Review `bv` or `bd list --status=in_progress` to see what others are doing
- `cass search "error" --workspace .` — Recent errors in this project

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
