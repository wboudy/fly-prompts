---
command_key: /implement/compact-context
stage: implement
include_in_palette: true
title: "Compact Context"
---

## Compact Context

### Goal
Execute the legacy "Compact Context" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- List what you have completed this session
- List what remains to be done
- Note any blockers, open questions, or partial work
- Write a handoff summary to MCP Agent Mail (MCP tool) or a bead comment
- Run `bd sync` to commit bead changes
- Commit any code changes with clear messages
- Do NOT lose work — commit and sync before compacting
- Do NOT leave ambiguous state — be explicit about what is done vs pending

Stage Tool Policy:
- Required: one issue tracker (`bd` or `br`) and `ntm`
- Optional: `cass`, `cm`, `ubs`, `dcg`
- Triggers:
  - Before commit readiness checks, run `ubs --staged` (or `ubs .` for full scan).
  - For dangerous operations, use `slb run "<command>"`.
- Use installed-tool commands from `docs/TOOLS_QUICKREF.md` only.

Coordination Note:
- `agent-mail` / `mcp_agent_mail` are MCP server binaries, not shell workflow CLIs.
- Prefer MCP Agent Mail tools when available; otherwise use `ntm send` fallback.

{{REPORTBACK}}

### Output
- What was done, what is next, and who owns the next action.
- Key commands/checks executed and their outcomes.
- Any blockers and explicit handoff details.
