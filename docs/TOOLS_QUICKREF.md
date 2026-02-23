# Tools Quick Reference

Copy/paste-safe commands for installed tools only.

## Session + Coordination

```bash
ntm doctor
ntm palette
ntm send <session> --all "<message>"
```

## Planning + Context

```bash
cass search "<topic>" --limit 5
cass context <path>
cm context "<task>" --json
```

## Issue Tracking

Choose one tracker per repo workflow and stay consistent.

```bash
bd ready
bd create --title "<title>"
bd list --status=in_progress
bd update <id> --status=in_progress
bd close <id>
bd sync
```

```bash
br ready
br create --title "<title>"
br list
br update <id> --status in_progress
br close <id> --reason "Completed"
br sync --flush-only
```

## Triage + Review

```bash
bv --robot-triage
bv --robot-plan
bv --robot-insights
```

## Safety + Validation

```bash
ubs --staged
ubs .
ubs doctor
dcg --help
slb check "<command>"
slb run "<command>"
```

## Optional Workflow Utilities

```bash
apr status
apr run 1
apr diff 1 2
apr integrate <round>
```

```bash
ru status
ru sync
ru list
ru doctor
```

```bash
caam status
caam activate <tool> <profile>
caam run <tool> -- "<command>"
```

## Notes

- Do not use `beads`, `cm-cass`, or `am` as shell commands; they are not installed CLIs.
- `agent-mail` and `mcp_agent_mail` are MCP server binaries, not shell workflow CLIs.
