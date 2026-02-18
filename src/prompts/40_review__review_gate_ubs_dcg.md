## Review: Quality Gate with UBS and DCG

### Goal
Run a focused review pass to catch regressions before release.

### Inputs
- Candidate diff/commit range.
- Acceptance criteria from plan/beads.
- Safety policies for destructive commands.

### Instructions
{{PREAMBLE}}

Goal:
- Approve only changes that satisfy behavior, safety, and ownership rules.

Roles:
- Reviewer inspects diff and checks.
- Doer addresses findings on owned surfaces.

Steps:
1. Review changed files for correctness and scope drift.
2. Re-run required checks and confirm outputs.
3. Run UBS on changed code areas and note findings.
4. Confirm DCG protections are respected for risky operations.
5. Request fixes or approve with explicit rationale.

Sync:
- Gate: no release handoff until blockers are resolved.
- Send findings in Agent Mail with `thread_id`, severity, owner.

{{REPORTBACK}}

Done:
- Review decision posted (approved or blocked) with concrete evidence.

### Output
- Findings list by severity.
- Final gate status and next owner.
