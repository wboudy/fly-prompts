---
command_key: /bootstrap/register-roles
stage: bootstrap
include_in_palette: true
title: "Bootstrap: Register Roles and Thread"
---

## Bootstrap: Register Roles and Thread

### Goal
Establish one broadcast-safe coordination thread before any edits.

### Inputs
- Team roster and intended role split.
- Proposed `thread_id`.
- Initial file-surface ownership map.

### Instructions
{{PREAMBLE}}

Goal:
- Confirm one `thread_id` and shared mission statement.

Roles:
- Elect a Captain and assign Doer roles.
- Post exclusive file surfaces per role.

Steps:
1. Post `thread_id` and role table in Agent Mail.
2. Each agent ACKs with role + owned surfaces.
3. Captain confirms no overlapping reservations.

Sync:
- Gate: no implementation begins until all ACKs are posted.
- Any ownership change requires a new handoff message.

{{REPORTBACK}}

Done:
- All agents ACKed and ownership boundaries are conflict-free.

### Output
- One ACK per agent with role and reserved paths.
- Explicit "ready for next handoff" line.
