## Release: Sync Gate, SLB, Deploy

### Goal
Ship validated changes with explicit sync gates and operator checks.

### Inputs
- Approved commit set.
- Required release checklist.
- CI and deployment context.

### Instructions
{{PREAMBLE}}

Goal:
- Perform a controlled release with documented verification.

Roles:
- Release owner runs checks and deploy commands.
- Observer verifies commands and outcomes.

Steps:
1. Run release gate checks (`make lint`, `make build`, tests as required).
2. Confirm no unresolved review blockers.
3. Use SLB workflow where two-person authorization is required.
4. Deploy using project-approved commands.
5. If command details are unclear, run `br --help` and tool `--help` first.

Sync:
- Gate: deploy starts only after gate checks + approvals are posted.
- Post release status in Agent Mail (`thread_id`, version/commit, outcome).

{{REPORTBACK}}

Done:
- Deployment result and rollback posture are documented.

### Output
- Release checklist results.
- Deploy outcome, follow-ups, and owner.
- Legacy prompts append check confirmed.
