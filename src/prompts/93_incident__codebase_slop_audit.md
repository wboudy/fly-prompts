---
command_key: /incident/codebase-slop-audit
stage: incident
include_in_palette: true
title: "Codebase Slop Audit"
---

## Codebase Slop Audit

### Goal
Hunt for AI-generated bloat: unnecessary files, redundant modules, one-shot scripts, and overlapping logic. The goal is net file and complexity reduction.

### Inputs
- Current objective, constraints, and relevant files.
- Active branch, changed files, and validation commands.
- Collaboration context (NTM session + issue tracker state).

### Instructions
{{PREAMBLE}}

Slop Taxonomy (ordered by severity):

1. **Duplicate files** - Same logic in multiple locations, often with slight naming variations
   - `utils.py` and `helpers.py` with overlapping functions
   - `config.py` and `settings.py` doing the same thing
   - Test files duplicated across directories

2. **One-shot scripts** - Scripts created for a single task that are now dead weight
   - Migration scripts that already ran
   - Debug/investigation scripts left behind
   - Scaffold generators that won't run again

3. **Orphan modules** - Files no longer imported or called anywhere
   - Use: `rg -l "from <module>" . && rg -l "import <module>" .`
   - Check `__init__.py` exports vs actual usage

4. **Overlapping abstractions** - Multiple ways to do the same thing
   - Two HTTP clients, two logging setups, two config loaders
   - Wrapper modules that add no value over the wrapped library

5. **Verbose scaffolding** - Over-engineered structure for simple needs
   - Empty `__init__.py` files in non-package directories
   - Abstract base classes with only one implementation
   - Interfaces/protocols with single implementers

6. **Dead documentation** - Docs describing removed features or wrong paths
   - READMEs referencing deleted files
   - Comments explaining code that no longer exists

Discovery Commands:
```bash
# Find potential duplicates by similar names
find . -name "*.py" | xargs -I{} basename {} | sort | uniq -d

# Find files not imported anywhere (potential orphans)
for f in $(find . -name "*.py" -not -path "./venv/*"); do
  base=$(basename "$f" .py)
  if ! rg -q "import.*$base|from.*$base" --type py .; then
    echo "ORPHAN?: $f"
  fi
done

# Find one-shot scripts (high standalone logic, low imports)
rg -c "^(def |class )" --type py | sort -t: -k2 -nr | head -20

# Find empty or near-empty files
find . -name "*.py" -size -100c

# List files by last modification (old = suspicious)
find . -name "*.py" -mtime +30 -not -path "./venv/*"
```

Workflow:
1. Run discovery commands to build candidate list
2. For each candidate, verify it's actually unused:
   - Check imports: `rg "from X import|import X" --type py`
   - Check runtime calls: `rg "X\." --type py`
   - Check test coverage: does a test file exist and import it?
3. Categorize findings by slop taxonomy type
4. For clear deletions (orphans, one-shots): delete and note in output
5. For consolidation candidates (duplicates, overlapping): create bead with merge plan
6. For uncertain cases: create spike bead to investigate
7. Run test suite after each deletion batch to catch breakage
8. Commit deletions in logical groups with clear messages

Deletion Safety:
- Confirm zero imports: `rg "import.*<filename>|from.*<filename>" .`
- Confirm zero references: `rg "<filename>" . --type-not py` (catches configs, docs)
- Check git log: `git log --oneline -5 -- <file>` (recent = caution)
- If tests exist for the file, delete tests too or they'll fail on missing imports

Stage Tool Policy:
- Required: `cass`, `ubs`, and one issue tracker (`bd` or `br`)
- Optional: `ntm`, `cm`, `bv`
- Triggers:
  - Use `ubs <path>` for targeted scans before deletion.
  - Record consolidation work in `bd` or `br` and broadcast status via `ntm send` when needed.
- Use installed-tool commands from `docs/TOOLS_QUICKREF.md` only.

Coordination Note:
- `agent-mail` / `mcp_agent_mail` are MCP server binaries, not shell workflow CLIs.
- Prefer MCP Agent Mail tools when available; otherwise use `ntm send` fallback.

Constraints:
- Do NOT delete files with imports until imports are removed
- Do NOT delete files modified in last 7 days without creating a bead first
- Do NOT consolidate across package boundaries without a plan
- Do NOT skip the test suite run after deletions
- Do NOT delete `__init__.py` files without checking if package is used
- Comply with AGENTS.md deletion governance (allowlist/blocklist)

{{REPORTBACK}}

### Output
Report in this format:

```markdown
## Slop Audit Results

### Deleted (net reduction: X files, ~Y lines)
| File | Type | Reason | Verification |
|------|------|--------|--------------|
| path/to/file.py | orphan | zero imports | `rg` returned empty |

### Consolidated (beads created)
| Bead ID | Files Merged | Target | Est. Line Reduction |
|---------|--------------|--------|---------------------|
| bd-XXXX | a.py, b.py | a.py | ~50 lines |

### Flagged for Review (uncertain)
| File | Concern | Recommended Action |
|------|---------|-------------------|
| path/to/suspicious.py | low usage but recent commits | spike bead |

### Clean (audited, no action needed)
- list of files verified as necessary
```
