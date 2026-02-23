---
command_key: /plan/clarify-requirements
stage: plan
include_in_palette: true
title: "Clarify Requirements"
---

## Clarify Requirements

### Goal
Execute the legacy "Clarify Requirements" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Review the current goal, beads, or instructions
- Identify every assumption you are making
- List every ambiguous point — scope, format, edge cases, priorities
- Formulate specific questions for each ambiguity
- Send questions to the overseer via MCP Agent Mail (MCP tool) or direct message
- WAIT for answers before proceeding
- Repeat until no ambiguities remain
- Context: [what you are trying to decide]

Stage Tool Policy:
- Required: `cass` and one issue tracker (`bd` or `br`)
- Optional: `cm`, `bv`, `apr`
- Triggers:
  - If planning dependencies, run `bv --robot-plan` and `bv --robot-insights`.
  - If creating tasks, use either `bd create ...` or `br create ...` consistently for the repo.
- Use installed-tool commands from `docs/TOOLS_QUICKREF.md` only.

Coordination Note:
- `agent-mail` / `mcp_agent_mail` are MCP server binaries, not shell workflow CLIs.
- Prefer MCP Agent Mail tools when available; otherwise use `ntm send` fallback.

{{REPORTBACK}}

### Output
- What was done, what is next, and who owns the next action.
- Key commands/checks executed and their outcomes.
- Any blockers and explicit handoff details.
