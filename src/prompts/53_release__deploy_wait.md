---
command_key: /release/deploy-wait
stage: release
include_in_palette: true
title: "Deploy & Wait"
---

## Deploy & Wait

### Goal
Execute the legacy "Deploy & Wait" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Push to remote: `git push`
- Create PR if needed: open or update the PR using your standard repo workflow
- Note the CI/deploy URL
- STOP and WAIT — do not proceed until CI completes
- If CI passes, report success via MCP Agent Mail (MCP tool)
- If CI fails, proceed to `debug-ci-failure` prompt
- Route through SLB: `slb run "<command>" --reason "<justification>"`
- Wait for approval before proceeding

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
