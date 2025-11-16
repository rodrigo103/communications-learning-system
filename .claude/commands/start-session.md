# Start Study Session

**Architecture**: This command uses the **Python coordinator** for state management.

## What This Command Does

Starts a new study session by invoking the Python coordinator to handle state management and session initialization.

## Components Used

- **Python CLI**: `python main.py start-session --user [username]`
- **SessionCoordinator**: Handles session lifecycle and state persistence

## Your Task

1. **Check if user provided username** in the prompt
2. **Invoke Python CLI** to start the session
3. **Show the session context** returned by the coordinator
4. **Explain what the user can do now**

## Command Format

```
/start-session [username]
```

If username not provided, ask for it.

## Implementation

When user runs `/start-session [username]`:

```bash
# Execute Python CLI command
python main.py start-session --user [username]
```

The Python coordinator will:
- Load current learning state
- Create or load user profile
- Initialize session tracking
- Save session to state/current_session.json
- Return session context with recommendations

## After Session Starts

Show the user:
1. Session confirmation
2. Current progress summary (from coordinator output)
3. Days until exam
4. Top recommendations
5. Available commands for learning work

Then explain:
```
✨ Session started! Now you can:

**Learning Work** (using subagents):
- Ask me to derive formulas: "Can you derive Shannon-Hartley?"
- Ask me to solve problems: "Can you solve this exercise?"
- Use slash commands: /derive [formula] or /solve [file]

**Track Progress**:
- /progress - Check your learning progress
- /end-session - Finish and save your work

**How it works:**
- I'll use specialized subagents for derivations and problems
- All work is saved to files (outputs/ directory)
- Your progress is tracked in learning_state.json
- Sessions are logged for collaboration via git
```

## Example Usage

```
User: /start-session rodrigo

You: Starting your study session...

[Execute: python main.py start-session --user rodrigo]

[Show coordinator output]

✓ Session started for: rodrigo
⏰ Started at: 2025-11-16 10:30:00
📅 Exam in: 29 days

📊 Current Status:
• Overall progress: 8%
• Active unit: Unit 7 (Noise)
• Concepts mastered: 7/87
• Problems solved: 1

💡 Top Recommendations:
1. Complete Unit 7 (Noise Temperature, SNR)
2. Start Unit 9 (Shannon-Hartley - critical gap!)
3. Daily problem practice (need 3-5 problems/day)

✨ Ready to study! What would you like to work on?
- Derive a formula
- Solve a problem
- Check your progress
```

## If Session Already Active

If there's already an active session:

```
⚠️ Active session detected!

Current session:
- User: rodrigo
- Started: 2 hours ago
- Activities: 3 items

Would you like to:
1. Continue this session
2. End current and start new one
```

## Important Notes

- **Use Python CLI** - Don't manually manipulate state files
- The coordinator handles all state persistence
- Session data is saved to state/current_session.json
- This enables session continuity across CLI invocations
- The Python code is simple and reliable for state management

## Integration with Subagents

After starting a session:
- Use **formula-deriver** for derivations
- Use **exercise-solver** for problem solving
- Use **progress-analyzer** for progress checks
- Session activities are tracked automatically

## Error Handling

If the Python CLI fails:
```
❌ Error starting session: [error message]

This might be because:
- Python dependencies not installed (pip install -r requirements.txt)
- State directory doesn't exist
- Permission issues

Try running: python main.py info
```
