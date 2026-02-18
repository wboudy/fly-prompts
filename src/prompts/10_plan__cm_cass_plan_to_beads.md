## Plan: CASS Context to Beads

### Goal
Convert context into an execution plan with small, ordered beads.

### Inputs
- Current objective and constraints.
- Relevant history from CASS.
- Existing branch status and known risks.

### Instructions
{{PREAMBLE}}

Goal:
- Produce a minimal, testable implementation plan.

Roles:
- Planner drafts the sequence.
- Captain validates ownership and dependency order.

Steps:
1. Query CASS for prior decisions and failed attempts.
2. Draft milestones and acceptance checks.
3. Initialize tracking: `br init` (or `bd init` if alias).
4. Create beads with explicit owners, surfaces, and done criteria.
5. If flags/options are uncertain, run `br --help` before proceeding.

Sync:
- Gate: beads must map 1:1 to owned surfaces and validation commands.
- Broadcast the plan in Agent Mail using the shared `thread_id`.

{{REPORTBACK}}

Done:
- Bead list is ordered, owned, and ready for implementation.

### Output
- Plan summary with dependencies.
- Bead IDs + owners + acceptance checks.
