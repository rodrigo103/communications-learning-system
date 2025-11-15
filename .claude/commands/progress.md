# Show Learning Progress

You are helping the user review their learning progress for the Communications Systems course.

## Your Task

1. **Read learning state**: `state/learning_state.json`
2. **Calculate metrics**: Progress percentages, velocity, etc.
3. **Analyze trends**: What's going well, what needs attention
4. **Provide recommendations**: Based on data and exam date

## Output Format

```
📊 Learning Progress Report
═══════════════════════════════════════════════════════════

📅 Exam: 2025-12-15 ([X] days remaining)
⏱️  Study time (last 7 days): [X] hours
📈 Overall progress: [X]%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📚 Units Progress

✅ Unit 1: Introducción (100%) ━━━━━━━━━━ Complete
📚 Unit 2: Análisis de Señales (75%) ━━━━━━━━░░ In Progress
⏳ Unit 3: Modulación Lineal (0%) ░░░░░░░░░░ Not Started
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Concepts & Skills

**Mastered:** [X]/87 concepts
- [List top mastered concepts]

**In Progress:** [X] concepts
- [List concepts being learned]

**Not Started:** [X] concepts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📝 Practice Stats

**Problems solved:** [X]
**Derivations completed:** [X]

**By type:**
- Noise: [X] problems
- Modulation: [X] problems
- Information Theory: [X] problems

**Difficulty distribution:**
- Easy: [X]
- Medium: [X]
- Hard: [X]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📈 Learning Velocity

**Recent activity:**
- Sessions this week: [X]
- Avg session length: [X] hours
- Concepts mastered/week: [X]

**Trend:** [↗️ Increasing / ↘️ Decreasing / → Stable]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ⚠️ Areas Needing Attention

[Identify weak areas based on data]
• [Area 1]: [Why it needs attention]
• [Area 2]: [Why it needs attention]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 Personalized Recommendations

Given your progress and [X] days until exam:

1️⃣ **Immediate priority:** [Specific action]
   → Use: `/derive [topic]` or `/solve [file]`

2️⃣ **This week focus:** [Topic/unit]
   → Aim for: [specific goal]

3️⃣ **Practice needed:** [Type of problems]
   → Try: [specific exercises]

4️⃣ **Review:** [Topics that need reinforcement]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎓 Exam Readiness Assessment

**Current readiness:** [X]%

**To reach 100%:**
- [X] more units to complete
- [X] more concepts to master
- ~[X] study hours needed
- Recommended: [X] hours/day until exam

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💪 Keep going! [Encouraging message based on progress]
```

## Analysis Guidelines

**Calculate Overall Progress:**
```
overall = (
    0.4 * (concepts_mastered / total_concepts) +
    0.3 * (units_completed / total_units) +
    0.3 * (problems_solved / target_problems)
)
```

**Identify Weak Areas:**
- Units with <20% progress and close to exam
- Concepts marked as "struggling"
- Problem types with low success rate

**Smart Recommendations:**
- If <30 days to exam: Focus on weak areas first
- If >60 days: Systematic unit-by-unit approach
- If falling behind: Suggest more intensive schedule
- If ahead: Suggest advanced topics or practice

## Session Context

- If in active session: Include session duration so far
- Show activities completed this session
- Provide mid-session encouragement

## Important

- Be honest but encouraging about progress
- Provide actionable recommendations
- Use the actual data from state files
- Calculate realistic estimates for exam readiness
- Adjust tone based on progress (struggling vs. ahead)
