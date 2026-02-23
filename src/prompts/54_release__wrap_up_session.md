---
command_key: /release/wrap-up-session
stage: release
include_in_palette: true
title: "Wrap Up Session"
---

## Wrap Up Session

### Goal
Execute the legacy "Wrap Up Session" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Commit all pending changes with clear messages
- Run `bd sync` to commit bead changes
- Update in_progress beads — either close or add status comments
- Post final status to MCP Agent Mail (MCP tool)
- Push all commits: `git push`
- Run `bd list --status=in_progress` — ensure nothing is orphaned
- Sign off via MCP Agent Mail (MCP tool)
- Closed: bd-a1b2c3, bd-d4e5f6

Stage Tool Policy:
- Required: `ubs` and `ntm`
- Optional: `slb`, `bd`/`br`, `ru`
- Triggers:
  - Run `ubs --staged` (or `ubs .`) before release sign-off.
  - Gate risky commands through `slb run "<command>"`.
- Use installed-tool commands from `docs/TOOLS_QUICKREF.md` only.

Coordination Note:
- `agent-mail` / `mcp_agent_mail` are MCP server binaries, not shell workflow CLIs.
- Prefer MCP Agent Mail tools when available; otherwise use `ntm send` fallback.

{{REPORTBACK}}

### Output
- What was done, what is next, and who owns the next action.
- Key commands/checks executed and their outcomes.
- Any blockers and explicit handoff details.
