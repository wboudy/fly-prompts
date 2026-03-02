---
command_key: /plan/coordinate-plans
stage: plan
include_in_palette: true
title: "Coordinate Plans"
---

## Coordinate Plans

### Goal
Coordinate multiple planning streams and produce one aligned execution plan.

### Inputs
- Current objective and active plan variants.
- Collaboration context (NTM session + ownership boundaries).
- Tracker state (`br` preferred / `bd` compatible).

### Instructions
{{PREAMBLE}}

Coordination workflow:
1. Identify active agents and their claims:
   ```bash
   ntm activity forecasting --json 2>/dev/null || ntm activity
   bd list --status=in_progress
   ```
2. Collect active plan proposals and identify overlap/conflict
3. Align ownership and sequencing before implementation starts
4. Keep one merged plan as source and track rejected alternatives explicitly

Agent Mail Coordination Examples:
```
Subject: [COORD] TealPeak + CopperHawk file overlap on src/auth/*

Body:
I'm claiming src/auth/login.py and src/auth/session.py for bd-XXXX.
You mentioned working on auth — which files do you need?
Reply within 10 min or I'll proceed with my claim.
```

```
Subject: [COORD-ACK] Confirmed split

Body:
Agreed. I'll take middleware.py, you take login.py + session.py.
Proceeding.
```

Timeout Protocol:
- If no response in 15 minutes, check agent activity: `ntm activity <session>`
- If agent idle >10min, proceed with your claim and note "unconfirmed split"
- If agent active, ping directly: `ntm send <session> --pane=X "Waiting on coord ack for <files>"`

Multi-Model Hybridization (copy/paste template):
```text
I asked 3 competing LLMs to do the exact same thing and they came up with pretty different plans which you can read below. I want you to REALLY carefully analyze their plans with an open mind and be intellectually honest about what they did that's better than your plan. Then I want you to come up with the best possible revisions to your plan (you should simply update your existing document for your original plan with the revisions) that artfully and skillfully blends the "best of all worlds" to create a true, ultimate, superior hybrid version of the plan that best achieves our stated goals and will work the best in real-world practice to solve the problems we are facing and our overarching goals while ensuring the extreme success of the enterprise as best as possible; you should provide me with a complete series of git-diff style changes to your original plan to turn it into the new, enhanced, much longer and detailed plan that integrates the best of all the plans with every good idea included (you don't need to mention which ideas came from which models in the final revised enhanced plan):
```
- Require git-diff style plan changes as output.
- Use `ntm send <session> --all "<summary>"` fallback if MCP Agent Mail tools are unavailable.

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
- Merged plan decision and rejected alternatives summary.
- Ownership split, dependency order, and next planning owner.
- Any blockers requiring escalation.
