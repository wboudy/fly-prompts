---
command_key: /implement/claim-reserve-code-ubs-close
stage: implement
include_in_palette: true
title: "Implement: Claim, Reserve, Code, UBS, Close"
---

## Implement: Claim, Reserve, Code, UBS, Close

### Goal
Execute assigned beads with explicit reservations and safe sync points.

### Inputs
- Assigned bead IDs and acceptance criteria.
- Reserved file surfaces.
- Current branch and test/lint commands.

### Instructions
{{PREAMBLE}}

Goal:
- Land code changes for assigned beads without ownership conflicts.

Roles:
- Doer edits only reserved surfaces.
- Review partner stays read-only until handoff.

Steps:
1. Claim bead in Agent Mail (`thread_id`, bead ID, reserved paths).
2. Implement only on reserved files.
3. Run local checks required by bead.
4. Run UBS for touched code paths before closing bead.
5. Update bead status and close when acceptance checks pass.

Sync:
- Gate: no bead closure without check outputs + UBS mention.
- Post reservation release or transfer in Agent Mail.

{{REPORTBACK}}

Done:
- Bead closed with evidence, and reservations updated.

### Output
- Change summary by file.
- Validation list (lint/build/tests/UBS) and bead closure note.
