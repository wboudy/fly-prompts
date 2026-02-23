---
command_key: /release/pre-deploy-checks
stage: release
include_in_palette: true
title: "Pre-Deploy Checks"
---

## Pre-Deploy Checks

### Goal
Execute the legacy "Pre-Deploy Checks" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Run the full test suite — fix any failures
- Run UBS (Ultimate Bug Scanner): `ubs .`
- Review UBS findings — fix critical and high severity issues
- Create beads for issues you cannot fix now: `bd create --title="..." --type=bug`
- Run linter and formatter — commit any fixes
- Check for uncommitted changes: `git status`
- Ensure all beads are synced: `bd sync`
- For any dangerous commands, route through SLB: `slb run "<command>"`

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
