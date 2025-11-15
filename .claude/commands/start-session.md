# Start Study Session

You are helping the user start a new study session for their Communications Systems course.

## Your Task

1. **Read the current learning state**: `state/learning_state.json`
2. **Check for active session**: `state/current_session.json`
3. **Ask for username** if not provided in the prompt
4. **Create session file** with:
   - Username
   - Start timestamp
   - Current context from learning_state

5. **Show session summary**:
   - Overall progress %
   - Current focus unit/topic
   - Days until exam (2025-12-15)
   - Top 3 recommendations

6. **Save session state** to `state/current_session.json`:
   ```json
   {
     "user": "username",
     "start_time": "ISO timestamp",
     "initial_progress": {...},
     "activities": []
   }
   ```

## Output Format

Present a clean summary:
```
✓ Session started for: [username]
⏰ Started at: [time]
📅 Exam in: [X] days

📊 Current Status:
• Overall progress: X%
• Active unit: Unit Y - [Name]
• Concepts mastered: X/87
• Problems solved: X

💡 Recommendations:
1. [Recommendation based on progress]
2. [Focus area]
3. [Suggested next topic]

✨ Ready! Use these commands:
• /derive [formula] - Get step-by-step derivation
• /solve [file] - Solve an exercise
• /progress - Check your progress
• /end-session - Finish and save
```

## Important

- Update `state/current_session.json` with session data
- This file will be used by other commands to track activities
- Be encouraging and supportive in your tone
