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

Context Gathering (run before planning):
```bash
cass search "<feature keywords>" --limit 10                    # prior art
rg "class.*<RelatedConcept>" --type py -l | head -10          # existing patterns
bd list --status=closed --limit=20 | grep -i "<area>"         # past work in area
```

Plan-space workflow:
1. Search for prior art using commands above
2. Review existing architecture: read README, AGENTS.md, key source files
3. Identify constraints: performance, compatibility, dependencies
4. Sketch state transitions, data flow, and component boundaries

When to Sketch Architecture:
- **Use state machine** when: >2 user-facing states (auth flows, wizards, async jobs)
- **Use data flow** when: data transforms across >2 services
- **Use component diagram** when: failure modes matter (payments, data sync)
- **Skip diagrams** for: pure refactors, bug fixes, config/cosmetic changes

State Machine Format (when applicable):
```
States: [list]
Transitions:
  <from> → <to>: <trigger>
Initial: <state>
Terminal: [states]
```

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
