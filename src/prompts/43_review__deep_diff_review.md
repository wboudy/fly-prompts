---
command_key: /review/deep-diff-review
stage: review
include_in_palette: true
title: "Deep Diff Review"
---

## Deep Diff Review

### Goal
Execute the legacy "Deep Diff Review" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Start with `git status` and `git diff`, then widen scope beyond tip-of-branch changes.
- Review recent history and peer commits; do not restrict analysis to the latest commit set.
- For each changed file, trace upstream callers and downstream dependencies.
- Ask "what could go wrong?" at boundaries, error paths, and security-sensitive flows.
- Use first-principles root-cause analysis; avoid symptom-only fixes.
- Verify tests cover new and regressed paths, then record residual risks explicitly.

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
