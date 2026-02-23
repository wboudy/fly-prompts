---
command_key: /review/fresh-eyes-ux-polish
stage: review
include_in_palette: true
title: "Fresh Eyes: UX Polish"
---

## Fresh Eyes: UX Polish

### Goal
Execute the legacy "Fresh Eyes: UX Polish" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Workflow (condensed from legacy command):
- **Workflows:** Walk through every user-facing flow end-to-end. Where does it feel clunky?
- **UI polish:** Spacing, alignment, typography, color consistency, loading states
- **Error states:** What happens when things go wrong? Are error messages helpful or cryptic?
- **Edge cases:** Empty states, long strings, slow connections, rapid clicks
- **Micro-interactions:** Hover states, transitions, feedback on actions
- **Copy:** Is the text clear, concise, and consistent? Any jargon leaking through?
- **Performance feel:** Does anything feel sluggish? Unnecessary spinners?
- **Accessibility:** Keyboard navigation, screen reader compatibility, contrast ratios

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
