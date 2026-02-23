---
command_key: /plan/decompose-plan-into-beads
stage: plan
include_in_palette: true
title: "Decompose Plan Into Beads"
---

## Decompose Plan Into Beads

### Goal
Convert an approved plan into implementation-ready issues with complete context.

### Inputs
- Final approved plan markdown.
- Constraints, test strategy, and logging requirements.
- Tracker choice (`br` preferred / `bd` compatible).

### Instructions
{{PREAMBLE}}

Decomposition workflow:
- Confirm all plan ambiguities are resolved before creating issues.
- Break work into small, testable, dependency-aware issues.
- Prefer `br` commands; use `bd` only for compatibility with existing repos.

Required acceptance criteria for each issue:
- Issue includes enough context to implement without reopening the plan file.
- Issue preserves full feature scope; no silent feature/functionality loss.
- Issue includes explicit unit-test requirements.
- Issue includes explicit end-to-end (e2e) test requirements.
- Issue includes detailed logging/observability expectations for verification.
- Dependency links are explicit and validated with `bv --robot-insights` when graph complexity is high.

Stage Tool Policy:
- Required: `cass` and one issue tracker (`bd` or `br`)
- Optional: `cm`, `bv`, `apr`
- Triggers:
  - If planning dependencies, run `bv --robot-plan` and `bv --robot-insights`.
  - If creating tasks, use either `bd create ...` or `br create ...` consistently for the repo.
- Use installed-tool commands from `docs/TOOLS_QUICKREF.md` only.

Coordination Note:
- `agent-mail` / `mcp_agent_mail` are MCP server binaries, not shell workflow CLIs.
- Prefer MCP Agent Mail tools when available; otherwise use `ntm send` fallback.

{{REPORTBACK}}

### Output
- Issue list with ownership, dependencies, and acceptance criteria.
- Confirmation that each issue is self-contained relative to the plan.
- Gaps that still require plan updates before implementation.
