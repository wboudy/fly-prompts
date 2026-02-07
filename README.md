# fly-prompts

Battle-tested prompts for multi-agent coding workflows with the [Flywheel](https://github.com/Dicklesworthstone/agentic_coding_flywheel_setup) stack.

## What is this?

A curated collection of NTM command palette prompts designed for orchestrating multiple AI coding agents (Claude Code, Codex CLI, Gemini CLI) working together on a codebase.

## Philosophy

### Workflow Phases

```
Planning → Implementing → Deploying → Utilities
```

1. **Planning** — Orient, plan, clarify, decompose into beads, review beads
2. **Implementing** — Claim beads, write code, review diffs, coordinate
3. **Deploying** — Commit, pre-deploy checks, push, debug CI
4. **Utilities** — Handoffs, status updates, session wrap-up

### Key Principles

- **Plan in bead-space, not code-space** — Fix bad plans before they become bad implementations
- **Clarify until zero ambiguity** — Ask questions, don't guess
- **Coordinate via Agent Mail** — Announce claims, share status, avoid conflicts
- **Use Flywheel tools** — CASS for history, BV for triage, UBS for scanning
- **Prefer hooks and daemons over agent busywork** — Let DCG catch dangerous commands automatically

## Flywheel Tools Referenced

| Tool | Purpose |
|------|---------|
| `bd` | Beads CLI — issue tracking |
| `bv` | Beads Viewer — TUI + analysis |
| `cass` | Cross-Agent Session Search — find past context |
| `ubs` | Ultimate Bug Scanner — static analysis |
| `dcg` | Destructive Command Guard — safety hook |
| `slb` | Simultaneous Launch Button — two-person auth |
| Agent Mail | Inter-agent messaging |

## Installation

### For NTM (Named Tmux Manager)

Copy `command_palette.md` to your NTM config directory:

```bash
cp command_palette.md ~/.config/ntm/command_palette.md
```

Then enable it in `~/.config/ntm/config.toml`:

```toml
palette_file = "~/.config/ntm/command_palette.md"
```

### Manual

Just copy the prompts you want from `command_palette.md`.

## Prompts

### Planning (7)
- **onboard** — Orient to project, register with Agent Mail, search CASS
- **plan** — Create initial plan with architecture thinking
- **brilliant_ideas** — Generate 100 ideas, filter to top 10
- **merge_plan** — Coordinate with other agents
- **clarify** — Ask questions until zero ambiguity
- **decompose** — Break plan into beads with BV validation
- **review_beads** — Verify beads before implementation

### Implementing (5)
- **swarm_beads** — Claim and work through beads
- **fresh_eyes** — Review recent changes
- **review_diffs** — Deep diff review
- **context_compact** — Summarize and prepare for continuation
- **check_mail** — Check Agent Mail inbox

### Deploying (4)
- **commit_grouped** — Commit changes in logical groups
- **pre_deploy** — Run tests and UBS before pushing
- **deploy_wait** — Push and wait for CI
- **debug_ci** — Diagnose CI failures

### Utilities (3)
- **handoff** — Prepare handoff for next agent
- **status** — Post brief status update
- **wrap_up** — End session cleanly

## Prompt Engineering Guidelines

These prompts follow these principles:

- **Be explicit, not implicit** — State exactly what you want
- **Use structured delimiters** — XML tags for sections
- **Front-load critical instructions** — Important stuff first
- **Give examples** — Show, don't just tell
- **Specify what NOT to do** — Negative constraints are effective
- **Control output format** — Define expected output structure

## Contributing

PRs welcome. Keep prompts:
- Professional and concise
- Integrated with Flywheel tools
- Following the engineering guidelines above

## License

MIT
