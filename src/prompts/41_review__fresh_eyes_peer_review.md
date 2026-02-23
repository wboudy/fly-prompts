---
command_key: /review/fresh-eyes-peer-review
stage: review
include_in_palette: true
title: "Fresh Eyes: Peer Review"
---

## Fresh Eyes: Peer Review

### Goal
Execute the legacy "Fresh Eyes: Peer Review" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Review fellow-agent changes across a recent window (for example, last 7 days), not just the latest commit.
- For each peer change, inspect touched files and neighboring/import-linked files.
- Follow the ripple: verify assumptions still hold across dependent modules.
- Use first-principles analysis; diagnose root causes before proposing fixes.
- Check for bugs, inefficiencies, security issues, and reliability gaps in peer-written code.

Peer-Agent Review Template (copy/paste):
```text
Turn your attention to reviewing the code written by your fellow agents. Check for issues, bugs, inefficiencies, security or reliability problems. Do not restrict yourself to the latest commits; cast a wider net and go deep. Diagnose root causes and fix or revise where needed.
```

Stage Tool Policy:
- Required: `bv` robot modes and `ntm`
- Optional: `cass`, `ubs`, `dcg`
- Triggers:
  - Use `bv --robot-triage` for prioritization and `bv --robot-insights` for dependency risk.
  - If reviewing changed files, run `ubs --staged` before approval.
- Use installed-tool commands from `docs/TOOLS_QUICKREF.md` only.

Coordination Note:
- `agent-mail` / `mcp_agent_mail` are MCP server binaries, not shell workflow CLIs.
- Prefer MCP Agent Mail tools when available; otherwise use `ntm send` fallback.

{{REPORTBACK}}

### Output
- What was done, what is next, and who owns the next action.
- Key commands/checks executed and their outcomes.
- Any blockers and explicit handoff details.
