---
command_key: /release/commit-grouped-changes
stage: release
include_in_palette: true
title: "Commit Grouped Changes"
---

## Commit Grouped Changes

### Goal
Execute the legacy "Commit Grouped Changes" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Run `git status` to see all changes
- Group related changes by feature, fix, or concern
- For each group:
- Stage only those files: `git add <files>`
- Write a detailed commit message (see format below)
- Commit: `git commit`
- Run `bd sync` to commit bead changes separately
- Review commit history: `git log --oneline -10`

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
