---
command_key: /plan/create-initial-plan
stage: plan
include_in_palette: true
title: "Create Initial Plan"
---

## Create Initial Plan

### Goal
Draft a strong initial plan, then improve it with one explicit pre-implementation review loop.

### Inputs
- Existing markdown plan (or draft plan).
- Constraints, acceptance criteria, and architecture context.
- Ownership boundaries and tracker choice (`br` preferred / `bd` compatible).

### Instructions
{{PREAMBLE}}

Plan-space workflow:
- Search for prior art: `cass search "<feature or problem>" --limit 5`
- Review existing architecture: read README, AGENTS.md, key source files
- Identify constraints: performance, compatibility, dependencies
- Sketch state transitions, data flow, and component boundaries.

Plan Review Loop (pre-implementation, copy/paste template):
```text
Carefully review this entire plan for me and come up with your best revisions in terms of better architecture, new features, changed features, etc. to make it better, more robust/reliable, more performant, more compelling/useful, etc.

For each proposed change, give me your detailed analysis and rationale/justification for why it would make the project better along with the git-diff style changes relative to the original markdown plan shown below:

<PASTE YOUR EXISTING COMPLETE PLAN HERE>
```
- Run this once in an external frontier model review pass before implementation.
- Apply accepted changes in-place to the same plan file.
- Keep unresolved questions explicit as TODO bullets in the plan.

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
- Revised plan (or plan diff) and rationale for major changes.
- Explicit open risks/questions before bead decomposition.
- Next owner and next plan-space action.
