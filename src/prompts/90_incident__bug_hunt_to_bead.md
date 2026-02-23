---
command_key: /incident/bug-hunt-to-bead
stage: incident
include_in_palette: true
title: "Incident: Bug Hunt to Bead"
---

## Incident: Bug Hunt to Bead

### Goal
Triage an incident and convert it into an owned, testable bead.

### Inputs
- Incident symptom, logs, and reproduction hints.
- Current branch/commit and recent changes.
- Severity and business impact.

### Instructions
{{PREAMBLE}}

Goal:
- Reproduce, contain, and route the fix with clear ownership.

Roles:
- Incident lead coordinates triage.
- Fix owner implements and validates remediation.

Steps:
1. Capture minimal repro and blast radius.
2. Search CASS for related incidents and prior fixes.
3. Create/assign a bead for remediation (`br init` or `bd init` if alias).
4. Implement fix on reserved surfaces and add/adjust tests.
5. Run UBS on changed code and attach relevant results.

Sync:
- Gate: incident is not closed until repro is resolved and checks pass.
- Post timeline updates in Agent Mail with `thread_id` and next checkpoint.

{{REPORTBACK}}

Done:
- Incident status, fix bead, and verification evidence are recorded.

### Output
- Triage summary and root-cause hypothesis.
- Bead assignment, fix evidence, and closure recommendation.
