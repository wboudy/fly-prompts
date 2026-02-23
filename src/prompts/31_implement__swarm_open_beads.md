---
command_key: /implement/swarm-open-beads
stage: implement
include_in_palette: true
title: "Swarm Open Beads"
---

## Swarm Open Beads

### Goal
Execute the legacy "Swarm Open Beads" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- Launch or attach a multi-agent session, then confirm health: `ntm doctor`, `ntm status <session>`.
- Prime all workers before coding:
  - `ntm send <session> "Read AGENTS.md and README.md carefully. Understand architecture, execution flows, and project purpose."`
- Run exploration + fix pass with fresh eyes:
  - `ntm send <session> "Randomly explore code files, trace imports/callers deeply, find obvious bugs/issues, and fix them while following AGENTS.md rules."`
- Run peer-agent review pass before handoff:
  - `ntm send <session> "Review code written by fellow agents, cast a wider net beyond latest commits, diagnose root causes, and patch issues."`
- Track assignments/findings in `br` (preferred) or `bd` to avoid overlap.
- For dangerous ops (force push, `rm -rf`), use `slb run "<command>"` for two-person auth.

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
