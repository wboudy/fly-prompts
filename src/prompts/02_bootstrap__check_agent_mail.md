---
command_key: /bootstrap/check-agent-mail
stage: bootstrap
include_in_palette: true
title: "Check Agent Mail"
---

## Check Agent Mail

### Goal
Execute the legacy "Check Agent Mail" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Check your MCP Agent Mail (MCP tool) inbox
- Read all unread messages
- For each message requiring action:
- Acknowledge receipt
- Take requested action or explain why you cannot
- Update relevant beads if needed
- For coordination requests, respond with your availability and plan
- Mark messages as read once handled

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
