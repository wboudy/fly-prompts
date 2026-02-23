---
command_key: /plan/generate-brilliant-ideas
stage: plan
include_in_palette: true
title: "Generate Brilliant Ideas"
---

## Generate Brilliant Ideas

### Goal
Expand option space, then converge on high-value plan improvements.

### Inputs
- Current plan (or project state if already implemented).
- Constraints, risks, and success criteria.
- Tracker state for capturing selected ideas (`br` preferred / `bd` compatible).

### Instructions
{{PREAMBLE}}

Idea workflow:
- Include wild ideas, safe ideas, and everything between
- Do not self-censor during generation
- Aim for quantity over quality in this phase
- Impact: How much value does this deliver?
- Effort: How hard is this to implement? (10 = easy, 1 = hard)
- Select top candidates by value-to-effort ratio.

Radical Innovation Nudge (copy/paste template):
```text
What's the single smartest and most radically innovative and accretive and useful and compelling addition you could make to the plan at this point?
```
- If development has already started, replace the word `plan` with `project`.
- Add accepted ideas into the plan (or convert directly into `br`/`bd` issues).

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
- Ranked idea shortlist with rationale.
- Chosen ideas integrated into plan/issue tracker.
- Explicitly rejected ideas and why.
