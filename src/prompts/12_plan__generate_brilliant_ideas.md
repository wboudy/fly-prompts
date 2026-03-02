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

Discovery Phase (run these first):
```bash
rg "TODO|FIXME|HACK" --type py -c | sort -t: -k2 -nr | head -10  # existing pain points
cass search "slow|bug|error|crash" --days 14 --limit 10          # recent complaints
bd list --status=closed --limit=20 | head -20                     # patterns in past work
```

Idea Generation (20-30 minimum):
- Cover all categories: performance, reliability, UX, DX, security, maintainability
- Include wild ideas, safe ideas, and everything between
- Do not self-censor during generation
- Stop when you've addressed each category at least twice

Scoring Anchors:
```
Impact (1-10):
  10: Fixes production outage or security hole
   7: Measurable perf/UX improvement for most users
   4: Developer experience improvement
   1: Cosmetic or hypothetical benefit

Effort (1-10, inverted - 10=easy):
  10: One-line fix, no tests needed
   7: Single file, <50 lines, tests exist
   4: Multi-file, new tests required
   1: Architectural change, multi-day work
```

Select top candidates by Impact/Effort ratio (higher = better).

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
Format your idea ranking as:

| Idea | Impact | Effort | Ratio | Action |
|------|--------|--------|-------|--------|
| Fix N+1 query in /users | 8 | 9 | 0.89 | `bd create --priority=2` |
| Add retry logic to API | 6 | 7 | 0.86 | `bd create --priority=3` |
| Rewrite auth from scratch | 9 | 2 | 0.22 | Rejected: too costly |

Then report:
- Top 5 ideas converted to beads (with IDs)
- Rejected ideas and one-line rationale each
- Categories not covered (if any)
