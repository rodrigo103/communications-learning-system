# Sub Agent System - Quick Reference Guide

## For the Main Agent (You!)

### Starting Any Study Activity

**Always do this first:**
```
1. Check if .doc/claude/tasks/current_session_context.md exists
2. If not, create it with current state
3. If yes, read it to understand current context
```

### Delegating to Sub Agents

**Template for delegation:**
```
Please read .doc/claude/tasks/current_session_context.md first to understand the session context, then [task description]
```

**Examples:**
```
"Read .doc/claude/tasks/current_session_context.md, then derive the AM formula focusing on the aspects relevant to the exam."

"Check .doc/claude/tasks/current_session_context.md to see current progress, then solve the problems in exercises/unit3/noise_problems.md"

"Read .doc/claude/tasks/current_session_context.md for recent activity, then analyze learning progress"
```

### After Sub Agent Completes

**Do these steps:**
```
1. Read the summary report from .doc/claude/reports/[category]/
2. Update .doc/claude/tasks/current_session_context.md with:
   - What was completed
   - Key insights/results
   - What should come next
3. Present brief summary to user (not full details - point to files)
```

### Context File Updates

**What to include in current_session_context.md:**
```markdown
# Current Session Context

**Last Updated**: [timestamp]

## Current Focus
[What topic/unit is being studied]

## Recent Activities
- [Activity 1 with timestamp]
- [Activity 2 with timestamp]

## Work Completed Today
- Derivations: [list with file links]
- Problems solved: [list with file links]

## Key Insights
[Any important learnings or patterns noticed]

## Next Steps
[What should be studied/practiced next]

## Weak Areas
[Topics that need more attention]
```

---

## For Sub Agents

### Your Workflow (All Agents)

**1. BEFORE starting:**
```
Check if .doc/claude/tasks/current_session_context.md exists
If yes: Read it to understand context
If no: Proceed anyway (parent agent might not have created it yet)
```

**2. DO your work:**
```
Create detailed output in standard location:
- Derivations → outputs/derivations/
- Solutions → outputs/solutions/
- Reports → appropriate location
```

**3. AFTER completing:**
```
Create summary report in:
.doc/claude/reports/[your_category]/[TOPIC]_[DATE]_summary.md

Return brief message:
✓ [Task] complete: [Topic]
📄 Full [work]: [file_path]
📋 Summary: [summary_path]

[One-line key result]

Please read the full [work] for details.
```

### Summary Report Template

**For derivations (formula-deriver):**
```markdown
# [Advanced] Derivation Summary: [Topic]

**Completed**: [ISO timestamp]
**Full derivation**: outputs/derivations/[file].md

## What Was Derived
[1-3 sentence description]

## Key Formulas
- Formula 1: $...$
- Formula 2: $...$

## Key Insights
[2-3 takeaways for student]

## Concepts Covered
[List]

## Suggested Next Steps
[What to study next]
```

**For problems (exercise-solver):**
```markdown
# Solution Summary: [Problem]

**Completed**: [ISO timestamp]
**Full solution**: outputs/solutions/[file].md

## Problem Type
[Category]

## Concepts Tested
[List]

## Key Formulas Used
[List]

## Final Answers
| Part | Answer | Units |
|------|--------|-------|
| (a)  | ...    | ...   |

## Skills Reinforced
[What this problem helps master]

## Related Practice
[Similar problems to try]
```

**For progress (progress-analyzer):**
```markdown
# Progress Summary

**Date**: [ISO date]
**Days to Exam**: [X]

## Quick Stats
- Overall: [X]%
- Concepts: [X]/87
- Problems: [X]/150
- Status: [Behind/On-track/Ahead]

## Top 3 Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

## This Week Goal
[Specific measurable goal]
```

---

## Common Scenarios

### Scenario: User starts studying

**Main agent:**
```
1. Invoke study-session-manager to start session
2. Wait for confirmation and context file creation
3. Present recommendations to user
```

### Scenario: User asks to derive a formula

**Main agent:**
```
1. Read/update current_session_context.md
2. Add: "Working on [topic] theory"
3. Invoke formula-deriver
4. Wait for completion message
5. Read summary from .doc/claude/reports/derivation_summaries/
6. Update context: "Completed [topic] derivation"
7. Tell user: "Derivation saved to [file], see [summary] for quick reference"
```

### Scenario: User asks to solve problems

**Main agent:**
```
1. Read/update current_session_context.md
2. Add: "Practicing [topic] problems"
3. Invoke exercise-solver
4. Wait for completion message
5. Read summary from .doc/claude/reports/solution_summaries/
6. Update context: "Solved X problems on [topic]"
7. Tell user results with file locations
```

### Scenario: User asks for progress check

**Main agent:**
```
1. Read current_session_context.md for recent activity
2. Invoke progress-analyzer
3. Wait for completion
4. Read summary from .doc/claude/reports/progress_reports/
5. Present key findings to user
6. Update context with any action items identified
```

### Scenario: User ends session

**Main agent:**
```
1. Invoke study-session-manager to end session
2. Wait for completion and context archival
3. Confirm to user that progress was saved
```

---

## File Locations Cheat Sheet

| Content Type | Full Detail | Summary |
|--------------|-------------|---------|
| Derivations | `outputs/derivations/` | `.doc/claude/reports/derivation_summaries/` |
| Solutions | `outputs/solutions/` | `.doc/claude/reports/solution_summaries/` |
| Progress | `.doc/claude/reports/progress_reports/` | Same file + `_summary.md` |
| Sessions | `sessions/YYYY-MM/` | `.doc/claude/reports/session_contexts/` |
| Active Context | `.doc/claude/tasks/current_session_context.md` | N/A |

---

## Token Optimization Tips

### DO:
✅ Point users to files instead of repeating content
✅ Read summaries instead of full documents when possible
✅ Update context incrementally (small changes, not full rewrites)
✅ Use file references in conversation ("as shown in [file]")

### DON'T:
❌ Include full derivations/solutions in conversation
❌ Re-read full files unnecessarily
❌ Duplicate information already in files
❌ Let context file grow unbounded (archive and start fresh when needed)

---

## Troubleshooting

**Q: Sub agent didn't create summary?**
- Check if it followed the new instructions
- If not, gently remind it in next invocation
- May need to re-read agent configuration

**Q: Context file getting too large?**
- Archive current context to `.doc/claude/reports/session_contexts/context_[DATE].md`
- Create fresh context file with just recent essentials
- Reference archived context if needed: "See archived context at [file] for earlier work"

**Q: User wants to see full derivation?**
- Point them to the file: `outputs/derivations/[file].md`
- Can optionally read key sections if they ask specific questions

**Q: Lost track of what was done?**
- Check `.doc/claude/tasks/current_session_context.md`
- Check recent summaries in `.doc/claude/reports/`
- Check session logs in `sessions/YYYY-MM/`

---

## Key Principles

1. **Files are truth**: Detailed work lives in files, conversation has summaries
2. **Context is shared**: All agents read/write same context file
3. **Summaries save tokens**: Brief reports instead of full content in conversation
4. **Archive regularly**: Don't let active context grow unbounded
5. **Reference, don't repeat**: Point to files instead of duplicating content

---

**Remember**: The goal is to save 80-90% of tokens while maintaining full detail in accessible files!
