# Palette Improvement Plan

Granular task list to take `command_palette.md` (1466 lines, 667 entries, 30 sections) from "complete inventory" to "tight, purposeful, JSM-skill-aware."

Each item is sized to be one focused editing session. Mark `[x]` when done.

---

## Phase A — Structural Cleanup (highest ROI; do first)

### A1. Extract repeated coordination boilerplate
**Why:** the "Use one thread_id… coordinate via agent-mail… check beads first" block repeats ~28× across the palette (~400 lines of waste). Every prompt in Bootstrap/Plan/Implement/Review/Release contains it.
**Action:**
- [ ] Create `references/COORDINATION_BOILERPLATE.md` with the canonical text.
- [ ] Replace inline copies across all sections with a one-line pointer: `> See [Coordination Boilerplate](references/COORDINATION_BOILERPLATE.md).`
- [ ] Validate via `scripts/validate_palette_alignment.py`.

### A2. Merge Peer Review + Deep Diff Review
**Why:** lines 1037–1113 vs 1162–1205 — both run `bv --robot-triage` + `ubs --staged` + same severity table. Functional duplicate.
**Action:**
- [ ] Consolidate into single section "Review & Critique Changes" with two sub-modes: "tip-of-branch" (default) and "wider scope" (was Deep Diff).
- [ ] Delete the obsolete section.
- [ ] Update palette index.

### A3. Clarify Bug Hunt vs Incident Bug Hunt
**Why:** Fresh Eyes Bug Hunt (l.1486) and Incident Bug Hunt to Bead (l.1441) overlap confusingly. One is proactive, one reactive — but neither says so.
**Action:**
- [ ] Retitle: "Bug Hunt: Proactive Sweep" + "Bug Hunt: Incident Triage."
- [ ] Open both with one-line discriminator ("use this when X, NOT when Y").

### A4. Resolve Slop Audit self-duplication
**Why:** Codebase Slop Audit section appears twice (l.1584 and l.1699 both with "Slop Audit Results" output format).
**Action:**
- [ ] Determine if l.1699 is a continuation, a separate command, or accidental dup.
- [ ] Merge or delete.

---

## Phase B — Gap Fills: Add Prompts for New JSM Skills

Each new prompt should follow existing palette entry format: `## Title`, `### Goal`, `### Instructions`, `### Output`. Reference the relevant skill explicitly. Token budget per prompt: ~150 words.

### B1. Testing & Quality (no palette presence today)
- [ ] **Add `## Testing: Fuzz the Inputs`** — invoke `testing-fuzzing` skill, target binary/CLI surfaces.
- [ ] **Add `## Testing: Metamorphic Properties`** — invoke `testing-metamorphic`, define property pairs.
- [ ] **Add `## Testing: Golden Artifacts`** — invoke `testing-golden-artifacts`, snapshot expected outputs.
- [ ] **Add `## Testing: Real-Service E2E (No Mocks)`** — invoke `testing-real-service-e2e-no-mocks`.
- [ ] **Add `## Testing: Conformance Harness`** — invoke `testing-conformance-harnesses`.

### B2. Advanced Debugging
- [ ] **Add `## Debug: GDB Deep-Dive`** — invoke `gdb-for-debugging` for native crashes.
- [ ] **Add `## Debug: Deadlock Hunt`** — invoke `deadlock-finder-and-fixer` for concurrency hangs.
- [ ] **Add `## Debug: Mock-Code Sweep`** — invoke `mock-code-finder` to find dangerous test mocks bleeding into prod paths.
- [ ] **Add `## Debug: Multi-Pass Bug Hunt`** — invoke `multi-pass-bug-hunting` for systematic sweep.

### B3. Codebase Analytics (new lane)
- [ ] **Create new H1 section "Codebase Analytics."**
- [ ] **Add `## Codebase: Archaeology Pass`** — invoke `codebase-archaeology` on unfamiliar repo.
- [ ] **Add `## Codebase: Domain Audit`** — invoke `codebase-audit` (security/UX/perf/API/CLI variants).
- [ ] **Add `## Codebase: Architecture Report`** — invoke `codebase-report` after exploration.
- [ ] **Add `## Codebase: Pattern Extraction`** — invoke `codebase-pattern-extraction` across multiple repos.

### B4. Research & Synthesis (new lane)
- [ ] **Create new H1 section "Research."**
- [ ] **Add `## Research: Paper Hunt`** — invoke `paper-research` for academic angle.
- [ ] **Add `## Research: Product/Market Dossier`** — invoke `product-research` for feature scoping.
- [ ] **Add `## Research: Library/Tool Selection`** — invoke `research-software` before adopting deps.
- [ ] **Add `## Research: Multi-Repo Synthesis`** — invoke `franken-research`.
- [ ] **Add `## Research: Multi-Model Triangulation`** — invoke `multi-model-triangulation` for major decisions.

### B5. Performance Lane
- [ ] **Create new H1 section "Performance."**
- [ ] **Add `## Perf: Extreme Optimization Pass`** — invoke `extreme-software-optimization`.
- [ ] **Add `## Perf: System Remediation`** — invoke `system-performance-remediation` for runtime issues.
- [ ] **Add `## Perf: GPU Workload Spin-up`** — invoke `vast-gpu` for transient compute needs.

### B6. New Workflow Skills (from latest pull)
- [ ] **Add `## Plan: Auto-Apply Jobs`** — invoke `auto-apply-jobs` for job-application automation.
- [ ] **Add `## Plan: Bead Creation Details`** — invoke `bead-creation-details` for richer bead specs.
- [ ] **Add `## Maintenance: Repo Hygiene Pass`** — invoke `repo-hygiene`.
- [ ] **Add `## Bootstrap: Mac Doctor`** — invoke `mac-doctor` in Onboard & Orient.

### B7. Release/Security
- [ ] **Add `## Release: SaaS Security Audit`** — invoke `security-audit-for-saas` as pre-deploy gate.

---

## Phase C — Quality Rewrites of Existing Prompts (~20 sub-tasks)

Each is a focused 5-min edit on one prompt. Source line numbers reference current `command_palette.md`.

- [ ] **C1. Bootstrap: Register Roles (l.186)** — strip 28× boilerplate; reference COORDINATION_BOILERPLATE.md
- [ ] **C2. Onboard & Orient (l.227)** — add explicit skill invocations (agent-mail, cass, br); replace "execute legacy workflow" with what it actually does
- [ ] **C3. Check Agent Mail (l.274)** — dedupe Instructions block from C2; reference shared
- [ ] **C4. Plan: CASS to Beads (l.415)** — add 1-line decision tree (CASS when context exists; raw plan when greenfield)
- [ ] **C5. Create Initial Plan (l.460)** — sharpen Goal: "Generate architectural + implementation roadmap (scope, milestones, risks)"
- [ ] **C6. Generate Brilliant Ideas (l.537)** — trim 280 lines; move templates to `references/IDEA_TEMPLATES.md`
- [ ] **C7. Coordinate Plans (l.620)** — extract numbered checklist; push boilerplate to footer
- [ ] **C8. Clarify Requirements (l.697)** — add "use before planning if ambiguity exists; skip if requirements locked"
- [ ] **C9. Decompose Plan Into Beads (l.744)** — link to AGENTS.md or inline required bead fields (title/acceptance/tests/deps)
- [ ] **C10. Review & Revise Beads (l.800)** — define `bv --robot-*` outputs in 1 line each
- [ ] **C11. Implement: Claim/Reserve/Code (l.852)** — explain UBS in 1 line ("safety check; run before close")
- [ ] **C12. Swarm Open Beads (l.897)** — extract boilerplate; workflow section ≤20 lines
- [ ] **C13. Compact Context (l.945)** — specify required handoff fields (status/blockers/next owner/committed+pending)
- [ ] **C14. Quality Gate (l.992)** — promote Goal: "Security + Quality Review Before Release"
- [ ] **C15. Fresh Eyes: UX Polish (l.1115)** — extract coordinate boilerplate; keep checklist
- [ ] **C16. Release: Sync Gate (l.1207)** — add concrete deploy stub (`vercel deploy --prod` / `gcloud app deploy`)
- [ ] **C17. Deploy & Wait (~l.1280)** — define wait predicate (URL probe / CI green / smoke test)
- [ ] **C18. Wrap Up Session (~l.1340)** — required outputs (changelog snippet, open beads, mail summary)
- [ ] **C19. Incident Bug Hunt (l.1441)** — specify `br init` (preferred) vs `bd init` (legacy) + bead fields
- [ ] **C20. Debug CI Failure (~l.1535)** — link to actual CI provider docs/log fetcher commands

---

## Phase D — Category Restructuring

Run AFTER B and C so we know the final inventory.

- [ ] **D1. Bootstrap consolidation** — 5 entries → 2 ("Initialize Thread & Roles" + "Coordinate & Health Check").
- [ ] **D2. Review consolidation** — 4 entries → 2 (after A2 merge + UX Polish standalone).
- [ ] **D3. Release consolidation** — 3 entries → 1 ("Release & Handoff").
- [ ] **D4. New section ordering** — Bootstrap → Plan → Implement → Codebase Analytics → Research → Performance → Review → Release → Incident → Maintenance.

---

## Phase E — Validation & Sync

- [ ] **E1.** Re-run `scripts/validate_palette_alignment.py` and `scripts/lint_palette.py`.
- [ ] **E2.** Regenerate `~/Desktop/palette-cheatsheet.pdf` via the palette-cheatsheet skill.
- [ ] **E3.** Commit fly-prompts; bump submodule pointer in orchestration-kit; push.

---

## Tracking

- Total items: ~50 (4 structural + 25 gap-fills + 20 quality + 4 restructure + 3 validation)
- Suggested batches: A → B1+B6+B7 → B2+B3 → B4+B5 → C (split into 4 sessions of 5) → D → E
