---
command_key: /review/fresh-eyes-peer-review
stage: review
include_in_palette: true
title: "Fresh Eyes: Peer Review"
---

## Fresh Eyes: Peer Review

### Goal
Execute the legacy "Fresh Eyes: Peer Review" workflow as a prompt-backed, stage-scoped command.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Review Scope Discovery:
```bash
# Find commits from other agents (not you)
git log --all --oneline --since="7 days ago" | head -30

# See which files changed recently
git diff --stat HEAD~20..HEAD | tail -20

# Focus on files touched by others
git log --name-only --pretty=format: --since="3 days ago" | sort -u | head -30
```

Workflow:
1. Identify peer changes using commands above
2. For each peer change, inspect touched files AND neighboring/import-linked files
3. Follow the ripple: verify assumptions still hold across dependent modules
4. Use first-principles analysis; diagnose root causes before proposing fixes
5. Check for bugs, inefficiencies, security issues, and reliability gaps

Severity Classification:
```
P0 (block merge): Security holes, data loss, crashes
P1 (fix before ship): Logic bugs, race conditions, missing validation
P2 (should fix): Perf issues, error handling gaps, test coverage
P3 (nice to have): Style, naming, minor refactors
```

Peer-Agent Review Template (copy/paste):
```text
Turn your attention to reviewing the code written by your fellow agents. Check for issues, bugs, inefficiencies, security or reliability problems. Do not restrict yourself to the latest commits; cast a wider net and go deep. Diagnose root causes and fix or revise where needed.
```

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
Format findings as:

| File:Line | Severity | Issue | Suggested Fix |
|-----------|----------|-------|---------------|
| auth.py:42 | P1 | SQL injection via f-string | Use parameterized query |
| utils.py:88 | P2 | Unbounded list growth | Add max size check |

Then report:
- Files reviewed (count)
- Issues found by severity (P0/P1/P2/P3 counts)
- Fixes applied vs beads created vs escalated
- Clean files (no issues found)
