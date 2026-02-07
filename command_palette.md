# Fly-Prompts: NTM Command Palette

Battle-tested prompts for multi-agent coding workflows with the Flywheel stack.

---

## Planning

### Onboard & Orient
```
<instructions>
You are starting a new session. Complete these orientation steps before any coding.
</instructions>

<steps>
1. Read AGENTS.md and README.md in full — understand project conventions
2. Register with Agent Mail using your pane name (e.g., cc_1)
3. Check your inbox for messages from other agents or the overseer
4. Search project history: `cass search "<project name>" --days 7 --limit 5`
5. Run `bd ready` to see available work — do NOT claim yet
6. Send a brief intro message via Agent Mail announcing your presence
7. Review `bv` or `bd list --status=in_progress` to see what others are doing
</steps>

<cass_tips>
Use CASS to understand recent context:
- `cass search "error" --workspace .` — Recent errors in this project
- `cass search "refactor" --days 3` — Recent refactoring discussions
- `cass context src/main.ts` — Sessions that touched a key file
</cass_tips>

<constraints>
- Do NOT start coding until orientation is complete
- Do NOT claim beads during onboard — that comes after planning
- Do NOT skip reading AGENTS.md even if you have seen it before
- Do NOT skip CASS search — context from past sessions is valuable
</constraints>
```

### Create Initial Plan
```
<instructions>
Create a structured plan before implementation. Think deeply about architecture before writing code.
</instructions>

<context_gathering>
Before planning:
1. Search for prior art: `cass search "<feature or problem>" --limit 5`
2. Review existing architecture: read README, AGENTS.md, key source files
3. Identify constraints: performance, compatibility, dependencies
</context_gathering>

<architecture_thinking>
For non-trivial features, sketch the design:

1. **State Machine** (if stateful):
   - What states can the system be in?
   - What transitions are valid?
   - What triggers each transition?
   
2. **Data Flow**:
   - Where does data enter the system?
   - How is it transformed?
   - Where does it exit?

3. **Component Boundaries**:
   - What modules are involved?
   - What are the interfaces between them?
   - What can change independently?
</architecture_thinking>

<state_machine_format>
States: [list]
Transitions:
  <from> → <to>: <trigger>
  <from> → <to>: <trigger>
Initial: <state>
Terminal: [states]
</state_machine_format>

<example_state_machine>
Feature: OAuth login flow

States: [unauthenticated, redirecting, callback_pending, authenticated, error]
Transitions:
  unauthenticated → redirecting: user clicks "Login with Google"
  redirecting → callback_pending: redirect to OAuth provider
  callback_pending → authenticated: valid callback with token
  callback_pending → error: invalid callback or denied
  error → unauthenticated: user clicks "Try again"
  authenticated → unauthenticated: logout or token expiry
Initial: unauthenticated
Terminal: []
</example_state_machine>

<steps>
1. Identify the goal — from beads, Agent Mail, or overseer instructions
2. Gather context — search CASS, read existing code
3. Sketch architecture — state machines, data flow, components
4. Break work into discrete subtasks (3-7 steps ideal)
5. Identify risks and unknowns
6. Share your plan via Agent Mail — tag relevant agents
7. Wait for feedback before proceeding to bead creation
</steps>

<output_format>
## Plan: <feature or goal>

### Context
- Prior art: <CASS findings or "none found">
- Existing components affected: <list>

### Architecture
<state machine or data flow diagram if applicable>

### Tasks
1. <task>
2. <task>
...

### Risks & Unknowns
- <risk or question>

### Dependencies
- Blocked by: <list or "none">
- Blocks: <list or "none">
</output_format>

<constraints>
- Do NOT skip CASS search — prior art saves time
- Do NOT skip architecture for non-trivial features
- Do NOT start implementing during planning
- Do NOT create beads yet — that is a separate step after plan approval
</constraints>
```

### Generate Brilliant Ideas
```
<instructions>
Diverge then converge. Generate many ideas, then ruthlessly filter to the best.
</instructions>

<phase_1_diverge>
Generate 100 ideas for improving the codebase, feature, or problem at hand.
- Include wild ideas, safe ideas, and everything between
- Do not self-censor during generation
- Aim for quantity over quality in this phase
</phase_1_diverge>

<phase_2_evaluate>
Score each idea on two axes (1-10):
- Impact: How much value does this deliver?
- Effort: How hard is this to implement? (10 = easy, 1 = hard)
</phase_2_evaluate>

<phase_3_converge>
Select the top 10 ideas by impact/effort ratio.
Create beads for the winners: `bd create --title="..." --priority=N`
Share your recommendations via Agent Mail.
</phase_3_converge>

<constraints>
- Do NOT stop at 20 ideas — push to 100
- Do NOT implement during ideation — this is planning only
- Do NOT skip the scoring step
</constraints>
```

### Coordinate Plans
```
<instructions>
Multiple agents are active. Align plans to avoid conflicts and duplicate work.
</instructions>

<steps>
1. Check Agent Mail for other agents' announced plans
2. Run `bd list --status=in_progress` to see claimed work
3. Identify overlaps — same files, same features, same beads
4. Message conflicting agents directly with a coordination proposal
5. Agree on division: who owns what files/beads
6. Update beads to reflect the agreed split
</steps>

<output_format>
After coordination, post to Agent Mail:
- Agents involved: [names]
- Division agreed: [who does what]
- Beads reassigned: [if any]
</output_format>

<constraints>
- Do NOT start work until conflicts are resolved
- Do NOT assume silence is agreement — get explicit confirmation
- Do NOT claim beads another agent is already working on
</constraints>
```

### Clarify Requirements
```
<instructions>
The plan may be underspecified. Ask questions until there is zero ambiguity.
</instructions>

<process>
1. Review the current goal, beads, or instructions
2. Identify every assumption you are making
3. List every ambiguous point — scope, format, edge cases, priorities
4. Formulate specific questions for each ambiguity
5. Send questions to the overseer via Agent Mail or direct message
6. WAIT for answers before proceeding
7. Repeat until no ambiguities remain
</process>

<question_format>
For each ambiguity, ask:
- Context: [what you are trying to decide]
- Options: [the choices you see]
- Recommendation: [what you would pick and why]
- Question: [what you need answered]
</question_format>

<example>
Context: User auth flow for the new signup feature
Options: (A) Email/password only (B) OAuth + email (C) OAuth only
Recommendation: B — flexibility without forcing OAuth
Question: Which auth approach should I implement?
</example>

<constraints>
- Do NOT guess on ambiguous requirements — ask
- Do NOT ask vague questions — be specific with options
- Do NOT proceed until you receive explicit answers
- Do NOT batch more than 5 questions at once — prioritize blockers
</constraints>
```

### Decompose Plan Into Beads
```
<instructions>
Convert an approved plan into atomic, trackable beads. Each bead should be a single logical unit of work that can be completed and verified independently.
</instructions>

<pre_check>
Before creating beads:
- Confirm the plan has been reviewed and approved
- Confirm all ambiguities have been resolved via `clarify`
- Search past work: `cass search "<project or feature>" --limit 5`
</pre_check>

<decomposition_rules>
1. Each bead = one logical unit of work (single feature, fix, or change)
2. Beads should be independently testable where possible
3. Prefer smaller beads — they parallelize better across agents
4. Set dependencies explicitly: if B requires A, link them
5. Use clear, action-oriented titles: "Implement X" not "X stuff"
6. Include acceptance criteria in the bead description
</decomposition_rules>

<steps>
1. List all tasks from the approved plan
2. For each task, assess scope — split if it touches multiple components
3. Identify dependencies between tasks
4. Create beads with proper metadata:
   `bd create --title="<action>: <target>" --type=<task|bug|feature> --priority=<0-4>`
5. Add dependencies: `bd dep add <child-id> <parent-id>`
6. Add descriptions with acceptance criteria: `bd update <id> --description="..."`
7. Validate with BV: `bv --robot-insights` — check for cycles or issues
8. Post summary to Agent Mail: "Created N beads for <plan>: <list of IDs>"
</steps>

<bead_format>
Title: <verb> <object> — e.g., "Implement OAuth callback handler"
Type: task | bug | feature | docs | test
Priority: 0 (critical) to 4 (backlog)
Description: |
  ## Goal
  <what this achieves>
  
  ## Acceptance Criteria
  - [ ] <measurable outcome>
  - [ ] <measurable outcome>
  
  ## Notes
  <any context or gotchas>
</bead_format>

<example>
Plan: "Add user authentication with OAuth"

Beads created:
1. bd-a1b2c3: "Implement OAuth provider configuration" (priority 1)
2. bd-d4e5f6: "Implement OAuth callback handler" (priority 1, depends on bd-a1b2c3)
3. bd-g7h8i9: "Add session management middleware" (priority 1, depends on bd-d4e5f6)
4. bd-j0k1l2: "Write OAuth integration tests" (priority 2, depends on bd-g7h8i9)
5. bd-m3n4o5: "Update README with auth setup" (priority 3, depends on bd-g7h8i9)

Validation: `bv --robot-insights` shows no cycles, clear critical path through auth chain.

Agent Mail: "Created 5 beads for OAuth implementation: bd-a1b2c3 → bd-d4e5f6 → bd-g7h8i9 → bd-j0k1l2, bd-m3n4o5. Ready for review."
</example>

<constraints>
- Do NOT create beads for unresolved or ambiguous requirements
- Do NOT create beads that touch multiple unrelated components — split them
- Do NOT forget to set dependencies — orphan beads cause chaos
- Do NOT skip acceptance criteria — vague beads lead to vague implementations
- Do NOT skip `bv --robot-insights` validation — catch cycles early
</constraints>
```

### Review & Revise Beads
```
<instructions>
Review newly created beads before implementation begins. Use BV analysis to catch structural issues. It is far cheaper to fix a bad plan than a bad implementation.
</instructions>

<bv_analysis>
Run these BV commands to understand the bead graph:
- `bv --robot-triage` — Full analysis: recommendations, quick wins, blockers
- `bv --robot-insights` — Graph metrics: cycles, bottlenecks, PageRank
- `bv --robot-plan` — Execution plan with parallel tracks
- `bv --robot-priority` — Priority recommendations with reasoning
</bv_analysis>

<review_checklist>
For each bead, verify:
- [ ] Title is clear and action-oriented
- [ ] Scope is a single logical unit (not multiple unrelated changes)
- [ ] Acceptance criteria are specific and testable
- [ ] Dependencies are correctly set (no missing links)
- [ ] Priority reflects actual importance
- [ ] No duplicate or overlapping beads

From BV analysis, check:
- [ ] No dependency cycles (`bv --robot-insights` → cycles array)
- [ ] Bottlenecks are appropriately prioritized
- [ ] Critical path makes sense
- [ ] Parallel tracks are identified for multi-agent work
</review_checklist>

<steps>
1. Run `bv --robot-triage` for full analysis
2. Check insights for cycles — these MUST be fixed
3. Review priority recommendations — adjust if BV suggests changes
4. Review execution plan — verify parallel tracks make sense
5. For each bead, apply the review checklist
6. Revise problematic beads:
   - Split large beads: create new ones, close original with note
   - Clarify vague beads: `bd update <id> --description="..."`
   - Fix dependencies: `bd dep add/remove`
   - Fix cycles: remove or reverse problematic dependencies
7. Re-run `bv --robot-insights` to confirm fixes
8. Post review summary to Agent Mail
</steps>

<output_format>
Bead Review Summary:
- Reviewed: <count> beads
- BV Analysis:
  - Cycles: <none | list>
  - Bottlenecks: <list of high-PageRank beads>
  - Parallel tracks: <count>
- Approved as-is: <list>
- Revised: <list with changes>
- Split: <original> → <new beads>
- Flagged for discussion: <list with questions>
</output_format>

<example>
Bead Review Summary:
- Reviewed: 5 beads
- BV Analysis:
  - Cycles: none
  - Bottlenecks: bd-d4e5f6 (OAuth callback) — high PageRank, blocks 3 beads
  - Parallel tracks: 2 (auth chain + docs)
- Approved as-is: bd-a1b2c3, bd-d4e5f6, bd-g7h8i9
- Revised:
  - bd-j0k1l2: Added missing acceptance criteria for test coverage %
- Split: none
- Flagged for discussion: none

All beads ready for implementation. Recommend 2 agents: one on auth chain, one on docs.
</example>

<constraints>
- Do NOT approve beads with dependency cycles — fix them first
- Do NOT ignore BV priority recommendations without justification
- Do NOT approve vague beads — push back for clarity
- Do NOT rubber-stamp — actually read each bead
- Do NOT implement during review — this is planning only
</constraints>
```

---

## Implementing

### Swarm Open Beads
```
<instructions>
Claim and work through available beads systematically. Coordinate via Agent Mail.
</instructions>

<pre_check>
Before claiming work, confirm you understand project conventions:
- If this is your first bead this session, re-skim AGENTS.md
- If context was recently compacted, refresh on README.md
- If unsure about workflow, check AGENTS.md before proceeding
</pre_check>

<steps>
1. Run `bd ready` to see beads with no blockers
2. Check Agent Mail for any claimed work or active discussions
3. Pick a bead matching your skills — prefer highest priority
4. Claim it: `bd update <id> --status=in_progress`
5. Announce via Agent Mail: "Claiming <bead-id>: <title>"
6. Implement the task fully
7. Close when done: `bd close <id> --reason="Completed"`
8. Repeat from step 1
</steps>

<constraints>
- Do NOT claim more than one bead at a time
- Do NOT work on beads marked in_progress by others
- Do NOT forget to announce claims via Agent Mail
- Do NOT leave beads in_progress when context is exhausted — hand off or pause
</constraints>
```

### Fresh Eyes Review
```
<instructions>
Review recent changes as if seeing the code for the first time. Catch what the author missed.
</instructions>

<steps>
1. Run `git diff HEAD~5` or check recent commits
2. For each changed file, read the diff carefully
3. Look for: typos, logic errors, missing edge cases, unclear naming
4. Check: does this match the stated intent in the bead or commit message?
5. If issues found, either fix directly or create a bead
6. Post findings via Agent Mail if other agents are affected
</steps>

<checklist>
- [ ] Variable names are clear and consistent
- [ ] Error handling covers failure cases
- [ ] No hardcoded values that should be config
- [ ] No commented-out dead code
- [ ] Tests cover the new behavior
</checklist>

<constraints>
- Do NOT rubber-stamp — actually read the code
- Do NOT rewrite working code for style preferences alone
- Do NOT skip files because they look fine at a glance
</constraints>
```

### Deep Diff Review
```
<instructions>
Perform a thorough review of uncommitted or recent changes. Think like a skeptical reviewer.
</instructions>

<steps>
1. Run `git status` and `git diff` to see all changes
2. For each file, ask: "What could go wrong here?"
3. Trace data flow — where does input come from, where does output go?
4. Check boundary conditions and error paths
5. Look for security issues: injection, auth bypass, data exposure
6. Verify tests exist and cover new code paths
</steps>

<output_format>
Report findings as:
- File: [path]
- Line: [number]
- Issue: [description]
- Severity: [critical/high/medium/low]
- Suggested fix: [brief recommendation]
</output_format>

<constraints>
- Do NOT approve without thorough review
- Do NOT skip "boring" files like configs or tests
- Do NOT assume the author tested edge cases
</constraints>
```

### Compact Context
```
<instructions>
Your context window is filling up. Summarize progress and prepare for continuation.
</instructions>

<steps>
1. List what you have completed this session
2. List what remains to be done
3. Note any blockers, open questions, or partial work
4. Write a handoff summary to Agent Mail or a bead comment
5. Run `bd sync` to commit bead changes
6. Commit any code changes with clear messages
</steps>

<output_format>
Write a context summary:
---
Session Summary for [agent name]:
Completed: [list]
In Progress: [current bead, current file]
Remaining: [list]
Blockers: [any questions or dependencies]
Next agent should: [specific instruction]
---
</output_format>

<constraints>
- Do NOT lose work — commit and sync before compacting
- Do NOT leave ambiguous state — be explicit about what is done vs pending
- Do NOT skip the Agent Mail update if other agents are active
</constraints>
```

### Check Agent Mail
```
<instructions>
Check for messages from other agents or the overseer. Respond promptly.
</instructions>

<steps>
1. Check your Agent Mail inbox
2. Read all unread messages
3. For each message requiring action:
   - Acknowledge receipt
   - Take requested action or explain why you cannot
   - Update relevant beads if needed
4. For coordination requests, respond with your availability and plan
5. Mark messages as read once handled
</steps>

<constraints>
- Do NOT ignore messages — acknowledge even if you cannot act immediately
- Do NOT let inbox pile up — check regularly during long sessions
- Do NOT forget to update beads when mail changes your plan
</constraints>
```

---

## Deploying

### Commit Grouped Changes
```
<instructions>
Commit changes in logical groups with detailed messages. Quality commits make history useful.
</instructions>

<steps>
1. Run `git status` to see all changes
2. Group related changes by feature, fix, or concern
3. For each group:
   - Stage only those files: `git add <files>`
   - Write a detailed commit message (see format below)
   - Commit: `git commit`
4. Run `bd sync` to commit bead changes separately
5. Review commit history: `git log --oneline -10`
</steps>

<commit_format>
<type>(<scope>): <summary>

<body - what and why, not how>

<footer - bead refs, breaking changes>

Types: feat, fix, docs, refactor, test, chore
</commit_format>

<example>
feat(auth): add OAuth2 login flow

Implements Google OAuth2 as an alternative to email/password login.
Users can now click "Sign in with Google" on the login page.
Token refresh is handled automatically via middleware.

Closes: bd-a1b2c3
</example>

<constraints>
- Do NOT make one giant commit with unrelated changes
- Do NOT write vague messages like "fix stuff" or "updates"
- Do NOT commit generated files, secrets, or .env files
- Do NOT forget to sync beads after code commits
</constraints>
```

### Pre-Deploy Checks
```
<instructions>
Prepare for deployment. Catch issues before CI does.
</instructions>

<steps>
1. Run the full test suite — fix any failures
2. Run UBS (Ultimate Bug Scanner): `ubs scan .`
3. Review UBS findings — fix critical and high severity issues
4. Create beads for issues you cannot fix now: `bd create --title="..." --type=bug`
5. Run linter and formatter — commit any fixes
6. Check for uncommitted changes: `git status`
7. Ensure all beads are synced: `bd sync`
</steps>

<example_ubs_output>
$ ubs scan .
[CRITICAL] src/auth.ts:42 - SQL injection via unsanitized input
[HIGH] src/api.ts:118 - Missing rate limit on public endpoint
[MEDIUM] src/utils.ts:55 - Unused variable 'temp'

Action: Fix CRITICAL and HIGH before deploy. Create beads for MEDIUM.
</example_ubs_output>

<checklist>
- [ ] All tests passing
- [ ] No critical UBS findings
- [ ] No uncommitted changes
- [ ] Beads synced
- [ ] README updated if needed
</checklist>

<constraints>
- Do NOT skip UBS scan
- Do NOT deploy with failing tests
- Do NOT ignore critical security findings
</constraints>
```

### Deploy & Wait
```
<instructions>
Push code and wait for CI. Do not spin or guess at failures.
</instructions>

<steps>
1. Push to remote: `git push`
2. Create PR if needed: `gh pr create`
3. Note the CI/deploy URL
4. STOP and WAIT — do not proceed until CI completes
5. If CI passes, report success via Agent Mail
6. If CI fails, proceed to debug_ci prompt
</steps>

<example_success>
Agent Mail message after CI passes:
"Deploy complete. PR #142 merged. Vercel preview: https://app-git-feature-xyz.vercel.app"
</example_success>

<while_waiting>
Do NOT watch CI obsessively. Instead:
- Check Agent Mail for other tasks
- Review beads for low-priority work
- Document what you just shipped
- Or simply wait — idle time is acceptable
</while_waiting>

<constraints>
- Do NOT push again hoping it fixes CI
- Do NOT guess at CI failures — wait for logs
- Do NOT start new features while deploy is pending
</constraints>
```

### Debug CI Failure
```
<instructions>
CI failed. Diagnose systematically using available tools.
</instructions>

<steps>
1. Get the CI logs: `gh run view --log-failed` or check the CI URL
2. Identify the failing step and error message
3. Reproduce locally if possible
4. Run UBS on affected files: `ubs scan <path>`
5. Create a bead for the fix: `bd create --title="Fix CI: <issue>" --type=bug --priority=1`
6. Fix the issue
7. Run pre_deploy checks again before pushing
</steps>

<example>
CI log shows:
  FAIL src/auth.test.ts
  ✕ should reject expired tokens (42ms)
    Expected: 401
    Received: 200

Diagnosis: Token expiry check is missing.
Fix: Add expiry validation in validateToken().
Bead: `bd create --title="Fix CI: token expiry not validated" --type=bug --priority=1`
</example>

<common_failures>
- Test failure: Run the specific test locally, check for flaky tests
- Lint failure: Run linter locally, auto-fix if possible
- Build failure: Check dependencies, lock files, build config
- Timeout: Check for infinite loops, missing mocks, slow tests
</common_failures>

<constraints>
- Do NOT push blind fixes hoping they work
- Do NOT skip local reproduction
- Do NOT ignore flaky tests — fix or quarantine them
</constraints>
```

---

## Utilities

### Prepare Handoff
```
<instructions>
Prepare a complete handoff for the next agent or session.
</instructions>

<steps>
1. Commit all code changes with clear messages
2. Run `bd sync` to save bead state
3. Update any in_progress beads with status comments
4. Write a handoff document (see format below)
5. Post handoff to Agent Mail
6. Tag the next agent if known
</steps>

<handoff_format>
Handoff from [agent] at [timestamp]
Completed: [list]
In Progress: [bead ID + status]
Open Questions: [list]
Files Modified: [list]
Next Steps: [numbered actions]
Warnings: [gotchas]
</handoff_format>

<example>
Handoff from cc_1 at 2026-02-07 14:30

Completed:
- OAuth2 login flow (bd-a1b2c3)
- Token refresh middleware

In Progress:
- bd-d4e5f6: Logout endpoint — 80% done, needs tests

Open Questions:
- Should logout invalidate all sessions or just current?

Files Modified:
- src/auth/oauth.ts, src/middleware/refresh.ts

Next Steps:
1. Finish logout endpoint tests
2. Add session invalidation (pending answer)

Warnings:
- Google OAuth sandbox expires Feb 15 — need prod creds before then
</example>

<constraints>
- Do NOT leave work uncommitted
- Do NOT write vague handoffs — be specific
- Do NOT skip Agent Mail update
</constraints>
```

### Post Status Update
```
<instructions>
Send a brief status update via Agent Mail. Keep it under 100 words.
</instructions>

<format>
Status from [agent]:
- Working on: [current bead or task]
- Progress: [percentage or milestone]
- Blockers: [none, or list]
- ETA: [estimate if known]
- Need: [nothing, or specific request]
</format>

<example>
Status from cc_2:
- Working on: bd-x7y8z9 (rate limiting middleware)
- Progress: 60% — core logic done, writing tests
- Blockers: none
- ETA: ~30 minutes
- Need: nothing right now
</example>

<constraints>
- Do NOT write essays — keep it under 100 words
- Do NOT skip blockers — flag them early
- Do NOT forget to check mail after posting
</constraints>
```

### Wrap Up Session
```
<instructions>
End your session cleanly. Leave the codebase better than you found it.
</instructions>

<steps>
1. Commit all pending changes with clear messages
2. Run `bd sync` to commit bead changes
3. Update in_progress beads — either close or add status comments
4. Post final status to Agent Mail
5. Push all commits: `git push`
6. Run `bd list --status=in_progress` — ensure nothing is orphaned
7. Sign off via Agent Mail
</steps>

<example_signoff>
cc_1 signing off at 2026-02-07 18:00

Session summary:
- Closed: bd-a1b2c3, bd-d4e5f6
- Left in progress: bd-g7h8i9 (blocked on API decision)
- Commits pushed: 4
- Tests passing: yes

Next agent: pick up bd-g7h8i9 once API format is confirmed.
</example_signoff>

<final_checklist>
- [ ] All changes committed
- [ ] Beads synced
- [ ] No orphaned in_progress beads
- [ ] Agent Mail updated
- [ ] Pushed to remote
</final_checklist>

<constraints>
- Do NOT leave uncommitted work
- Do NOT leave beads in limbo
- Do NOT vanish without a signoff message
</constraints>
```
