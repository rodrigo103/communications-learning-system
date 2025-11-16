# Show Learning Progress

**Architecture**: This command uses the **subagent-first** approach.

## What This Command Does

Invokes the **progress-analyzer subagent** to analyze learning progress and provide personalized recommendations.

## Subagent Used

- 📊 **progress-analyzer** (Sonnet, 🟡 Amber): Expert in analyzing learning progress, identifying weak areas, and providing study recommendations

## Your Task

1. **Invoke progress-analyzer subagent** using the Task tool
2. **Pass context**: Current date, exam date, any specific focus areas user mentioned
3. **Return results**: Show progress summary and key recommendations

## Command Format

```
/progress
```

## Implementation

When user runs `/progress`:

```
Use Task tool:
  subagent_type: "progress-analyzer"
  model: "sonnet"
  prompt: "Analyze the current learning progress for the Communications Systems course.

    Context:
    - Exam date: 2025-12-15
    - Current date: [today]
    - Course: 10 units, 87 concepts total
    - User: [primary user from state]

    Files to analyze:
    - state/learning_state.json - Tracked progress
    - outputs/derivations/ - Generated derivation files
    - outputs/solutions/ - Generated solution files
    - sessions/ - Session logs
    - .doc/claude/reports/ - Previous reports

    Provide:
    - Honest assessment of current vs. tracked progress
    - Reconciliation between state and actual work
    - Time remaining vs. work needed analysis
    - Personalized recommendations
    - Concrete action plan
    - Priority areas to focus on

    Save reports to:
    - .doc/claude/reports/progress_reports/progress_[date].md (detailed)
    - .doc/claude/reports/progress_reports/progress_[date]_summary.md (concise)

    Format: Comprehensive markdown report with clear sections, metrics, and actionable recommendations."
```

## After Subagent Completes

1. Read the summary file
2. Show user:
   - Overall progress percentage
   - Key statistics (concepts mastered, problems solved, study hours)
   - Days remaining to exam
   - Critical gaps or concerns
   - Top 3-5 priority recommendations
3. Provide file path to detailed report
4. Ask if they want deeper analysis of specific areas

## Example Usage

```
User: /progress

You: I'll analyze your learning progress using the progress-analyzer subagent.

[Invoke Task tool with progress-analyzer]

[After completion]
📊 Progress Analysis Complete

Overall: 8% actual (7/87 concepts)
Tracked: 0% (state needs updating!)
Days to exam: 29

Critical Findings:
• Tracking system broken - work not recorded in state
• Only 1 active study day in last week
• Problem practice severely neglected (1/150)
• Need 3 concepts + 5 problems DAILY to pass

Top Priorities:
1. Fix tracking: Update learning_state.json TODAY
2. Shannon-Hartley derivation (critical gap in Unit 9)
3. Daily problem practice (60% of study time)

This Week Target:
- Complete 13 concepts + 20 problems by Nov 23
- Focus: Unit 7 (Noise), Unit 9 (Info Theory)

Status: SEVERELY BEHIND - Need 5-7 hours daily

Full reports:
- Summary: .doc/claude/reports/progress_reports/progress_2025-11-16_summary.md
- Detailed: .doc/claude/reports/progress_reports/progress_2025-11-16.md

Would you like me to:
1. Help update your learning state with completed work
2. Create a detailed study schedule for next week
3. Identify specific weak areas to focus on
```

## What the Subagent Analyzes

The progress-analyzer subagent examines:

**State Files:**
- learning_state.json - Official tracked progress
- session_history.jsonl - Session patterns
- user_profiles.json - Study preferences

**Output Files:**
- outputs/derivations/ - What's been derived
- outputs/solutions/ - Problems solved
- Sessions logs - Study session details

**Calculations:**
- Overall completion percentage
- Learning velocity (concepts/week, problems/week)
- Time remaining vs. work needed
- Study frequency and consistency
- Gap between tracked and actual progress

**Recommendations:**
- Priority topics based on exam coverage
- Study schedule suggestions
- Weak area identification
- Time management advice
- Realistic exam readiness assessment

## Important Notes

- **Always use the subagent** - Don't do progress analysis yourself
- The subagent provides honest, data-driven assessments
- Reports are saved to files for later reference
- Subagent reconciles state tracking vs. actual work done
- Recommendations are personalized based on time remaining

## Honest Assessment Philosophy

The progress-analyzer subagent:
- ✓ Provides honest assessments (even if difficult to hear)
- ✓ Uses actual data, not optimistic estimates
- ✓ Identifies critical gaps and time pressures
- ✓ Gives actionable, specific recommendations
- ✓ Calculates realistic paths to exam readiness
- ✓ Encourages but doesn't sugarcoat the situation
