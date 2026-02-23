# Installed Tools (Machine Truth)

Validated on the local machine for this repo alignment pass.

## Installed CLIs

| Tool | Version (observed) | Notes |
|---|---|---|
| `ntm` | `1.7.0` | Session orchestration; command palette and messaging fallback (`ntm send`). |
| `apr` | `1.2.2` | Automated Plan Reviser workflow CLI. |
| `bd` | `0.46.0` | Beads issue tracker. |
| `br` | `0.1.13` | beads_rust issue tracker. |
| `bv` | `0.12.1` | Robot triage/planning flags (`--robot-*`). |
| `cass` | `0.1.64` | Session/context search. |
| `cm` | `0.2.3` | Procedural memory CLI. |
| `ubs` | help verified | Version command is flaky in this environment; `--help` and scanner usage work. |
| `dcg` | `0.3.0` | Hook-style guard binary; see `dcg --help`. |
| `slb` | `0.2.0` | Two-person safety gate for dangerous commands. |
| `caam` | `0.1.10` | Account/profile manager for coding CLIs. |
| `ru` | `1.2.1` | Repo updater workflow CLI. |

## Present But Not Shell Workflow CLIs

- `agent-mail`
- `mcp_agent_mail`

These binaries explicitly report they are MCP server entrypoints, not shell workflow CLIs.
Use MCP Agent Mail tools directly when available. For shell fallback coordination, use `ntm send`.

## Not Installed As CLIs

- `beads`
- `cm-cass`
- `am`
