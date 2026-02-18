# Codex Handoff

## Required Handoff Structure

Every handoff message should include these sections in order:

1. `Goal`
2. `Roles`
3. `Steps`
4. `Sync`
5. `Done`

For prompt content, include `{{PREAMBLE}}` and `{{REPORTBACK}}` in `### Instructions`.

## Broadcast-Safe Checklist

- [ ] Shared `thread_id` is stated.
- [ ] Doer is explicit.
- [ ] File surfaces are reserved and exclusive.
- [ ] Non-doers are read-only unless reassigned.
- [ ] No destructive git ops are requested.

## Engineering Checklist

- [ ] `make lint`
- [ ] `make build`
- [ ] Summarize changed files and test evidence.
- [ ] Note blockers and owner for next step.

## Manual NTM Verification

1. Run `ntm --help` and `ntm palette --help` to confirm local CLI usage.
2. Load the generated palette with:
   - `ntm palette load ./command_palette.md`
3. Verify expected entries are visible and executable in the UI.

## Suggested Handoff Template

```md
HANDOFF N — <Title>
Doer: Agent <X>. Others: read-only.

Goal:
- <Outcome>

Roles:
- Agent X: <owned surfaces>
- Agent Y: <owned surfaces>

Steps:
1) <step>
2) <step>

Sync:
- Run `make lint` and `make build` before Done.

Done:
- <explicit completion criteria>
```
