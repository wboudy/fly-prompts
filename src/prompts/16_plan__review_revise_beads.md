---
command_key: /plan/review-revise-beads
stage: plan
include_in_palette: true
title: "Review & Revise Beads"
---

## Review & Revise Beads

### Goal
Iteratively improve issue quality in plan space before implementation begins.

### Inputs
- Current issue set (`br` preferred / `bd` compatible).
- Approved plan markdown and acceptance criteria.
- Quality and risk constraints.

### Instructions
{{PREAMBLE}}

Revision workflow:
- `bv --robot-triage` — Full analysis: recommendations, quick wins, blockers
- `bv --robot-insights` — Graph metrics: cycles, bottlenecks, PageRank
- `bv --robot-plan` — Execution plan with parallel tracks
- `bv --robot-priority` — Priority recommendations with reasoning
- Iterate in plan space until issues are stable and implementation-ready.

Bead Revision Loop (copy/paste template; no outdated reasoning tags):
```text
Reread AGENTS.md so it's fresh in your mind. Then review every issue carefully. Are you sure each one is optimal? Could anything make the system work better for users? If so, revise the issues now while we're still in plan space.

Do NOT oversimplify. Do NOT lose features or functionality. Ensure every issue embeds the required plan context so implementers never need to refer back to the plan file. Ensure each issue includes comprehensive unit tests, end-to-end tests, and detailed logging requirements.
```
- Prefer `br` terminology in new issue edits; keep `bd` compatibility where needed.

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
- Revised issue set with rationale for major changes.
- Explicit confirmation: no feature loss during revision loop.
- Remaining blockers before implementation handoff.
