# End Study Session

You are helping the user end their study session and save their progress.

## Your Task

1. **Read current session**: `state/current_session.json`
2. **Summarize session work**: What was accomplished
3. **Update learning state**: `state/learning_state.json`
4. **Create session log**: Save detailed log
5. **Provide next steps**: Recommendations for next session

## Process

### 1. Read Current Session Data

From `state/current_session.json`:
- User name
- Start time
- Activities completed (derivations, problems solved, etc.)
- Initial progress snapshot

### 2. Calculate Session Metrics

- **Duration**: End time - Start time
- **Activities**: Count of derivations, problems, etc.
- **Progress delta**: How much progress was made
- **New concepts**: What was learned/practiced

### 3. Update Learning State

Update `state/learning_state.json`:
- Increment counters (sessions, problems_solved, etc.)
- Add study time to velocity tracking
- Update last_session_date
- Mark concepts as practiced/mastered
- Update unit progress

### 4. Create Session Log

Save to `sessions/YYYY-MM/YYYY-MM-DD_[username]_session.md`:

```markdown
# Study Session Log

**User:** [username]
**Date:** [YYYY-MM-DD]
**Start:** [HH:MM]
**End:** [HH:MM]
**Duration:** [X]h [Y]m

## Session Goals

[If specified at start, otherwise "General study"]

## Work Completed

### Derivations
- [Formula 1] - [Saved to path]
- [Formula 2] - [Saved to path]

### Problems Solved
- [Problem 1] - [Saved to path]
- [Problem 2] - [Saved to path]

### Topics Studied
- [Topic 1]: [What was covered]
- [Topic 2]: [What was covered]

## Key Insights & Learnings

• [Insight 1]
• [Insight 2]
• [Connection realized]

## Concepts Practiced

- [Concept 1]: [Level - learning/practiced/mastered]
- [Concept 2]: [Level]

## Progress Update

**Before session:**
- Overall: [X]%
- Concepts mastered: [X]
- Problems solved: [X]

**After session:**
- Overall: [Y]% (+[delta]%)
- Concepts mastered: [Y] (+[delta])
- Problems solved: [Y] (+[delta])

## Questions / Open Items

- [Question or topic that needs more work]
- [Something to explore next time]

## Next Session Recommendations

1. [Continue with...]
2. [Practice more...]
3. [Review...]

## Files Generated

- `outputs/derivations/[files]`
- `outputs/solutions/[files]`

---

**Session saved:** [timestamp]
**Next session focus:** [Recommendation]
```

### 5. Append to History

Add entry to `state/session_history.jsonl`:
```json
{"date": "ISO", "user": "name", "duration_hours": X, "activities": [...], "progress_delta": X}
```

### 6. Clean Up

- Delete `state/current_session.json`
- Session is now closed

## Output to User

```
═══════════════════════════════════════════════════════════
📊 Session Summary
═══════════════════════════════════════════════════════════

👤 User: [username]
⏱️  Duration: [X]h [Y]m
📅 Date: [YYYY-MM-DD]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ✅ Completed Work

**Derivations:** [X]
[List derivations]

**Problems Solved:** [X]
[List problems]

**Topics Covered:**
[List topics studied]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📈 Progress Made

Overall: [before]% → [after]% (+[delta]%)
Concepts: [before] → [after] (+[delta])
Problems: [before] → [after] (+[delta])

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 Key Insights

• [Learning 1]
• [Learning 2]
• [Connection made]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 For Next Session

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Session log saved: sessions/[path]
📊 Learning state updated

✨ Great work today! [Encouraging message]

💾 Don't forget to commit your progress:
   git add .
   git commit -m "Session: [summary]"
   git push
```

## Important

- Be encouraging and positive
- Highlight achievements, even small ones
- Provide specific, actionable next steps
- Ensure all state files are updated correctly
- The session log should be detailed enough that someone else could continue
- Calculate progress changes accurately
