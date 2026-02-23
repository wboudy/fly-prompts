# Legacy Conversion Log

- Date: 2026-02-23
- Policy: no runnable legacy section; every command is backed by `src/prompts/*.md`.
- Behavioral updates: removed non-installed CLI references (`beads`, `cm-cass`, `am`) from runnable instructions; standardized MCP note for Agent Mail binaries.

| legacy_command_key | new_prompt_file | likely_stage | tools_referenced_in_legacy | legacy_text_location |
|---|---|---|---|---|
| `/bootstrap/onboard-orient` | `src/prompts/01_bootstrap__onboard_orient.md` | `bootstrap` | `bd, beads, bv, cass` | `legacy line 9` |
| `/bootstrap/check-agent-mail` | `src/prompts/02_bootstrap__check_agent_mail.md` | `bootstrap` | `beads` | `legacy line 686` |
| `/bootstrap/prepare-handoff` | `src/prompts/03_bootstrap__prepare_handoff.md` | `bootstrap` | `bd, beads` | `legacy line 898` |
| `/bootstrap/post-status-update` | `src/prompts/04_bootstrap__post_status_update.md` | `bootstrap` | `bd` | `legacy line 954` |
| `/plan/create-initial-plan` | `src/prompts/11_plan__create_initial_plan.md` | `plan` | `beads, cass` | `legacy line 40` |
| `/plan/generate-brilliant-ideas` | `src/prompts/12_plan__generate_brilliant_ideas.md` | `plan` | `bd, beads` | `legacy line 137` |
| `/plan/coordinate-plans` | `src/prompts/13_plan__coordinate_plans.md` | `plan` | `bd, beads` | `legacy line 169` |
| `/plan/clarify-requirements` | `src/prompts/14_plan__clarify_requirements.md` | `plan` | `beads` | `legacy line 198` |
| `/plan/decompose-plan-into-beads` | `src/prompts/15_plan__decompose_plan_into_beads.md` | `plan` | `bd, beads, bv, cass` | `legacy line 237` |
| `/plan/review-revise-beads` | `src/prompts/16_plan__review_revise_beads.md` | `plan` | `bd, beads, bv` | `legacy line 311` |
| `/implement/swarm-open-beads` | `src/prompts/31_implement__swarm_open_beads.md` | `implement` | `bd, beads, ntm, slb` | `legacy line 399` |
| `/implement/compact-context` | `src/prompts/32_implement__compact_context.md` | `implement` | `bd` | `legacy line 652` |
| `/review/fresh-eyes-peer-review` | `src/prompts/41_review__fresh_eyes_peer_review.md` | `review` | `beads` | `legacy line 503` |
| `/review/fresh-eyes-ux-polish` | `src/prompts/42_review__fresh_eyes_ux_polish.md` | `review` | `beads` | `legacy line 554` |
| `/review/deep-diff-review` | `src/prompts/43_review__deep_diff_review.md` | `review` | `none` | `legacy line 620` |
| `/release/commit-grouped-changes` | `src/prompts/51_release__commit_grouped_changes.md` | `release` | `bd, beads` | `legacy line 714` |
| `/release/pre-deploy-checks` | `src/prompts/52_release__pre_deploy_checks.md` | `release` | `bd, beads, slb, ubs` | `legacy line 759` |
| `/release/deploy-wait` | `src/prompts/53_release__deploy_wait.md` | `release` | `beads, ntm, slb` | `legacy line 810` |
| `/release/wrap-up-session` | `src/prompts/54_release__wrap_up_session.md` | `release` | `bd, beads` | `legacy line 985` |
| `/incident/fresh-eyes-bug-hunt` | `src/prompts/91_incident__fresh_eyes_bug_hunt.md` | `incident` | `none` | `legacy line 448` |
| `/incident/debug-ci-failure` | `src/prompts/92_incident__debug_ci_failure.md` | `incident` | `bd, ubs` | `legacy line 852` |
