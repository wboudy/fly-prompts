# State Machine

This defines broadcast-safe coordination for multi-agent prompt execution.

## States

1. `BOOTSTRAP`
- Set `thread_id`.
- Elect roles and assign exclusive file surfaces.
- Done when every agent posts ACK with role + owned surfaces.

2. `PLAN`
- Define small PR sequence and acceptance checks.
- Reserve file ownership per PR.
- Done when scope, owners, and checks are explicit.

3. `EXECUTE`
- Doer edits only owned surfaces.
- Other agents are read-only unless reassigned.
- Done when required files are updated and local checks pass.

4. `CONVERGE`
- Summarize diffs and resolve cross-surface dependencies.
- Reconfirm no ownership conflicts.
- Done when branch is stable and ready for release checks.

5. `RELEASE`
- Final lint/build and operator verification steps.
- Push branch and open PR when authorized.
- Done when PR and test evidence are posted.

## Transition Rules

- `BOOTSTRAP -> PLAN`: all ACKs present.
- `PLAN -> EXECUTE`: handoff includes Goal/Roles/Steps/Sync/Done.
- `EXECUTE -> CONVERGE`: required checks pass for changed surfaces.
- `CONVERGE -> RELEASE`: no unresolved conflicts or blockers.

## Broadcast-Safe Patterns

- Use one shared `thread_id` in every handoff.
- Reserve file surfaces before edits.
- Use explicit Doer line (`Doer: Agent X`).
- Use converge checkpoints before release.
- Avoid destructive git operations.
