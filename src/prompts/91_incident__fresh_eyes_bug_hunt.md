---
command_key: /incident/fresh-eyes-bug-hunt
stage: incident
include_in_palette: true
title: "Fresh Eyes: Bug Hunt"
---

## Fresh Eyes: Bug Hunt

### Goal
Execute the legacy "Fresh Eyes: Bug Hunt" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Choose a starting file outside your recent edit set, then inspect deeply.
- Trace execution flow in both directions: callers, callees, and import-linked modules.
- Record what the code should do, then compare behavior for fresh-eyes discrepancies.
- Fix discovered issues systematically (logic bugs, boundary mistakes, reliability gaps), then continue with a new file.
- Repeat in random-but-methodical passes until coverage and confidence are acceptable.

Persistence Mode (Use Sparingly, optional):
```text
I know for a fact that there are at least 87 serious bugs throughout this project impacting every facet of its operation. The question is whether you can find and diagnose and fix all of them autonomously. I believe in you.
```
- Warning: this can drive false positives and time waste if used too long.
- Only use when normal triage stalls; set a timebox and explicit stop criteria.

Stage Tool Policy:
- Required: `cass`, `ubs`, and one issue tracker (`bd` or `br`)
- Optional: `ntm`, `cm`, `bv`
- Triggers:
  - Use `ubs <path>` for targeted scans while triaging incidents.
  - Record remediation work in `bd` or `br` and broadcast status via `ntm send` when needed.
- Use installed-tool commands from `docs/TOOLS_QUICKREF.md` only.

Coordination Note:
- `agent-mail` / `mcp_agent_mail` are MCP server binaries, not shell workflow CLIs.
- Prefer MCP Agent Mail tools when available; otherwise use `ntm send` fallback.

{{REPORTBACK}}

### Output
- What was done, what is next, and who owns the next action.
- Key commands/checks executed and their outcomes.
- Any blockers and explicit handoff details.
