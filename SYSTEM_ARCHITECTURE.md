# System Architecture: Subagent-First Design

**Version**: 2.0.0
**Last Updated**: 2025-11-15
**Architecture**: Subagent-First with File-Based State

---

## Overview

This learning system uses a **subagent-first architecture** where Claude Code subagents handle all AI-intensive work (derivations, problem solving, analysis), while a minimal Python layer manages state persistence and session tracking.

## Design Philosophy

### Core Principles

1. **Subagents Do the Work**: All AI tasks are handled by specialized Claude Code subagents
2. **Files Are the API**: State and context are shared through files, not in-memory
3. **Git-Based Collaboration**: Multiple users can collaborate via git commits
4. **Minimal Python**: Python code is limited to state management and CLI
5. **Token Efficiency**: File-based context uses 80-90% fewer tokens than conversation history

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        User Layer                           │
├─────────────────────────────────────────────────────────────┤
│  • Claude Code Interface (Primary)                          │
│  • Python CLI (Optional, for session management)            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    Claude Code Subagents                    │
├─────────────────────────────────────────────────────────────┤
│  🎓 formula-deriver        - Adaptive derivations (all)     │
│  ✅ exercise-solver        - Problem solving                │
│  📊 progress-analyzer      - Progress analysis              │
│  🎯 study-session-manager  - Session orchestration          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   File-Based State Layer                    │
├─────────────────────────────────────────────────────────────┤
│  state/                                                     │
│  ├── learning_state.json     - Global learning state        │
│  ├── user_profiles.json      - User profiles                │
│  ├── session_history.jsonl   - Session history              │
│  ├── current_focus.json      - Current focus area           │
│  └── current_session.json    - Active session data          │
│                                                             │
│  .doc/claude/                                               │
│  ├── tasks/                  - Task context                 │
│  ├── reports/                - Subagent reports             │
│  └── session_states/         - Session states               │
│                                                             │
│  outputs/                                                   │
│  ├── derivations/            - Generated derivations        │
│  └── solutions/              - Problem solutions            │
│                                                             │
│  sessions/                                                  │
│  └── YYYY-MM/                - Monthly session logs         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                  Python State Manager                       │
├─────────────────────────────────────────────────────────────┤
│  agents/coordinator.py                                      │
│  • Load/save learning state                                 │
│  • Manage user sessions                                     │
│  • Track progress                                           │
│  • Generate session logs                                    │
│                                                             │
│  main.py                                                    │
│  • Thin CLI wrapper                                         │
│  • Session commands                                         │
│  • Progress display                                         │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Claude Code Subagents

Located in `.claude/agents/`, these are markdown files that define specialized AI agents. Each has a unique color/emoji for visual identification:

#### 🎓 **formula-deriver** (🟣 Purple)
- Model: Opus (most capable)
- Purpose: **Adaptive formula derivations** - handles everything from basic to advanced
- Key Feature: Automatically adjusts pedagogical level based on topic and context
- Output: Comprehensive derivations with appropriate rigor
- Example: `outputs/derivations/AM_spectrum.md` (pedagogical) or `shannon_hartley_rigorous.md` (advanced proof)

#### ✅ **exercise-solver** (🟢 Green)
- Model: Opus (problem-solving focus)
- Purpose: Solve exam-style problems
- Output: Complete solutions with validation
- Example: `outputs/solutions/noise_problem_20251115.md`

#### 📊 **progress-analyzer** (🟡 Amber)
- Model: Sonnet (analytical)
- Purpose: Analyze learning progress and identify weak areas
- Output: Progress reports and recommendations

#### 🎯 **study-session-manager** (🟠 Orange)
- Model: Sonnet (orchestration)
- Purpose: Manage study sessions, load context, generate handoffs
- Output: Session state updates

**Color Legend**: 🎓🟣 Derivations (adaptive) | ✅🟢 Solving | 📊🟡 Analysis | 🎯🟠 Coordination

**Note**: Previously had separate basic/advanced derivation subagents - now merged into one intelligent Purple subagent that adapts automatically. See `.claude/SUBAGENT_REFERENCE.md` for details.

### 2. File-Based State System

All state is persisted to files for:
- **Collaboration**: Multiple users share state via git
- **Persistence**: Sessions survive across CLI invocations
- **Transparency**: All state is human-readable JSON/Markdown
- **Version Control**: Git tracks all changes

#### Key State Files

```json
// state/learning_state.json
{
  "metadata": { "created_at": "...", "exam_date": "2025-04-24" },
  "progress_summary": { "overall_completion": 15.5 },
  "current_context": { "active_unit": 3 },
  "units": { "1": {...}, "2": {...} },
  "learning_velocity": { "last_7_days": {...} },
  "recommendations": { "next_topics": [...] }
}
```

### 3. Python State Manager

Minimal Python code for state management:

**agents/coordinator.py** (~750 lines)
- Session lifecycle (start/end)
- State loading/saving
- User profiles
- Session logging

**main.py** (~200 lines)
- CLI interface
- Commands: start-session, end-session, progress, info
- Thin wrapper around coordinator

### 4. Command System

Located in `.claude/commands/`:
- `derive.md` - Trigger formula derivation
- `solve.md` - Trigger problem solving
- `progress.md` - Check learning progress
- `start-session.md` / `end-session.md` - Session management

## Workflows

### Typical Learning Session

```bash
# 1. Start session
python main.py start-session --user rodrigo

# 2. Work in Claude Code
# Ask: "Can you derive Shannon-Hartley theorem?"
# Subagent creates: outputs/derivations/shannon_hartley.md

# 3. Solve problems
# Ask: "Can you solve this noise calculation problem?"
# Subagent creates: outputs/solutions/noise_problem_123.md

# 4. Check progress
python main.py progress

# 5. End session
python main.py end-session --summary "Studied Unit 3: Noise"

# 6. Commit work
git add .
git commit -m "Session: Unit 3 noise calculations"
git push
```

### Collaboration Workflow

```bash
# User A works
python main.py start-session --user alice
# ... does work ...
python main.py end-session
git commit -m "Alice: Derived Friis formula"
git push

# User B continues
git pull
python main.py start-session --user bob
# Loads Alice's work from state files
# ... continues work ...
python main.py end-session
git commit -m "Bob: Solved transmission problems"
git push
```

## Why This Architecture?

### ✅ Advantages

1. **Flexibility**: Subagents adapt to any problem, no hardcoded logic
2. **Token Efficiency**: File-based context uses 80-90% fewer tokens
3. **Collaboration**: Git-based state enables multi-user workflows
4. **Maintainability**: Less code to maintain (~1000 lines vs ~5400)
5. **Powerful AI**: Leverages Claude's full capabilities
6. **Transparency**: All work is saved as readable files
7. **Composability**: Subagents can call other subagents

### ⚠️ Trade-offs

1. **Requires Claude Code**: Can't use standalone
2. **Less Predictable**: Subagent behavior varies slightly
3. **File Management**: More files to track in git
4. **Speed**: Each subagent invocation takes time

## Migration from v1.0

**What Changed**:
- ❌ Removed: `agents/derivation_engine.py` (839 lines)
- ❌ Removed: `agents/problem_solver.py` (787 lines)
- ✅ Simplified: `agents/coordinator.py` (807 → 750 lines)
- ✅ Simplified: `main.py` (510 → 202 lines)
- ✅ Reduced: `requirements.txt` (32 → 11 dependencies)

**What Stayed**:
- ✅ State management in coordinator.py
- ✅ Session lifecycle management
- ✅ Progress tracking
- ✅ File-based architecture

**What Improved**:
- 🚀 Subagents handle derivations dynamically
- 🚀 No hardcoded derivation logic
- 🚀 Better collaboration via git
- 🚀 44% less code to maintain

## File Organization

```
communications-learning-system/
├── .claude/
│   ├── agents/           # Subagent definitions (5 files)
│   ├── commands/         # Slash commands (5 files)
│   └── settings.local.json
├── agents/
│   ├── __init__.py
│   └── coordinator.py    # State management only
├── state/
│   ├── learning_state.json
│   ├── user_profiles.json
│   └── session_history.jsonl
├── outputs/
│   ├── derivations/      # Subagent-generated derivations
│   └── solutions/        # Subagent-generated solutions
├── sessions/
│   └── YYYY-MM/          # Monthly session logs
├── .doc/claude/          # Subagent working files
│   ├── tasks/
│   ├── reports/
│   └── session_states/
├── main.py               # Thin CLI wrapper
├── requirements.txt      # Minimal dependencies
└── README.md
```

## Development

### Adding a New Subagent

1. Create `.claude/agents/new-agent.md`
2. Define prompt, model, and output format
3. Add command in `.claude/commands/`
4. Document in README

### Modifying State Schema

1. Update `learning_state_schema.json`
2. Add migration logic in `coordinator.py`
3. Update documentation

### Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Test coordinator
python -m pytest tests/

# Test session lifecycle
python main.py start-session --user test
python main.py progress
python main.py end-session
```

## Future Enhancements

Potential additions without compromising the simple architecture:

1. **Anki Integration**: Simple script to convert outputs to Anki cards
2. **Web Dashboard**: Read-only progress visualization
3. **Analytics**: Session analytics and velocity tracking
4. **Export**: Generate comprehensive study guides from outputs

## Summary

This architecture prioritizes:
- **Simplicity**: Minimal Python, maximum AI
- **Flexibility**: Subagents adapt to new requirements
- **Collaboration**: Git-based multi-user workflows
- **Maintainability**: Less code, clear separation of concerns

The result: A powerful, flexible learning system that leverages Claude's full capabilities while maintaining a simple, maintainable codebase.
