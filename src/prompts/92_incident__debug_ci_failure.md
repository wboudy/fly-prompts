---
command_key: /incident/debug-ci-failure
stage: incident
include_in_palette: true
title: "Debug CI Failure"
---

## Debug CI Failure

### Goal
Execute the legacy "Debug CI Failure" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Get the CI logs: your CI log viewer or CI URL
- Identify the failing step and error message
- Reproduce locally if possible
- Run UBS on affected files: `ubs <path>`
- Create a bead for the fix: `bd create --title="Fix CI: <issue>" --type=bug --priority=1`
- Fix the issue
- Run pre_deploy checks again before pushing
- Test failure: Run the specific test locally, check for flaky tests

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
