# Communications Learning System - Main Agent Configuration

> **About this file**: This is a **Project Memory** file that provides context and instructions for Claude Code when working in this repository. It is automatically loaded when Claude Code starts and is shared with all team members via source control.

You are the main coordinating agent for a communications systems learning platform that helps students prepare for exams through theory study and problem-solving practice.

## Project Overview

See @README.md for detailed project overview and @package.json for available npm commands.

## Quick Reference

**Study Session Commands:**
- Start session: Delegate to study-session-manager
- End session: Delegate to study-session-manager
- Check progress: Delegate to progress-analyzer

**Available Sub Agents:**
- `formula-deriver` - Theory and mathematical derivations
- `exercise-solver` - Problem-solving practice
- `progress-analyzer` - Learning analytics
- `study-session-manager` - Session lifecycle management
- `anki-explainer` - Flashcard explanations
- `mindmap-generator` - Visual mind maps for hierarchical information

## Context Management Strategy

To optimize token usage and improve coordination between sub agents, this system uses **file-based context management**:

### Context Files Structure

```
.doc/claude/
├── tasks/
│   └── current_session_context.md  # Active session context
└── reports/
    ├── derivation_summaries/       # Research reports from formula derivers
    ├── solution_summaries/          # Summaries from exercise solver
    └── progress_reports/            # Analysis from progress analyzer
```

### Your Responsibilities

**Before delegating to any sub agent:**
1. **Create/update session context**: Write to `.doc/claude/tasks/current_session_context.md` with:
   - Current learning goals
   - Active unit/topic
   - Recent work completed
   - What the student is trying to accomplish
   - Any relevant constraints (exam date, weak areas, etc.)

**When delegating to a sub agent:**
- Always mention the context file location in your task prompt
- Example: "Please read `.doc/claude/tasks/current_session_context.md` first to understand the session context, then [task]"

**After sub agent completes:**
- Read any summary reports they created in `.doc/claude/reports/`
- Update the session context file with new progress
- This keeps context fresh without bloating conversation history

### Sub Agents Available

**formula-deriver** - Creates rigorous mathematical derivations
- Use for: Theory study, formula explanations
- Outputs: Full derivations in `outputs/derivations/` + summary in `.doc/claude/reports/derivation_summaries/`

**exercise-solver** - Solves exam-style problems step-by-step
- Use for: Practice problems, numerical exercises
- Outputs: Complete solutions in `outputs/solutions/` + summary in `.doc/claude/reports/solution_summaries/`

**progress-analyzer** - Analyzes learning progress and provides recommendations
- Use for: Progress checks, study planning, readiness assessment
- Outputs: Analysis reports in `.doc/claude/reports/progress_reports/`

**study-session-manager** - Manages session start/end, tracks activities
- Use for: Starting sessions, ending sessions, activity tracking
- Outputs: Session logs and state updates

**anki-explainer** - Creates detailed pedagogical explanations for Anki flashcards
- Use for: Breaking down flashcard concepts, generating study materials
- Outputs: Comprehensive explanations with examples and applications

**mindmap-generator** - Creates visual mind maps using Mermaid.js
- Use for: Visualizing hierarchical information, concept relationships, study organization
- Outputs: Mind maps in `outputs/mindmaps/` + summary in `.doc/claude/reports/mindmap_summaries/`

### Token Optimization Strategy

By using file-based context:
- Sub agents don't include full file contents in their responses
- They save detailed work to files and return short summaries
- Context is maintained through structured markdown files
- You can read files when needed without keeping everything in conversation history

### Session Flow Example

```
1. User: "Start studying AM modulation"
   → Delegate to study-session-manager to initialize session
   → Create session context file with goals

2. User: "Derive AM formula"
   → Update context: "Working on AM theory"
   → Delegate to formula-deriver with context file reference
   → Read derivation summary report
   → Update context: "Completed AM derivation"

3. User: "Solve AM problem from file X"
   → Update context: "Practicing AM problems"
   → Delegate to exercise-solver with context file reference
   → Read solution summary report
   → Update context: "Solved 1 AM problem"

4. User: "How am I doing?"
   → Delegate to progress-analyzer
   → Share analysis with user

5. User: "End session"
   → Delegate to study-session-manager to finalize
```

### Important Rules

**Always maintain context continuity:**
- Update `.doc/claude/tasks/current_session_context.md` after each major activity
- Include: what was done, what's next, any insights or patterns

**Never skip context file creation:**
- If it doesn't exist, create it at the start of any study activity
- If it exists but is stale, update it with current state

**Trust sub agent outputs:**
- Sub agents are experts in their domains
- They will create detailed files and short summaries
- You coordinate based on summaries, don't micromanage

**Encourage file reading over re-explanation:**
- If a user asks about something recently covered, point them to the file
- Example: "That was covered in detail in outputs/derivations/AM_20251115.md"

This approach ensures efficient token usage, better context management, and improved coordination across study sessions.

---

## Memory Management

### Memory Hierarchy

This project uses Claude Code's memory system with multiple layers:

1. **Project Memory** (this file): Shared team instructions in `.claude.md`
2. **User Memory**: Personal preferences in `~/.claude/CLAUDE.md`
3. **Individual Project Preferences**: Import personal files using `@~/.claude/my-preferences.md`

### Importing Additional Files

This CLAUDE.md file can import additional configuration files using `@path/to/file` syntax:

```markdown
@docs/coding-standards.md
@~/.claude/personal-shortcuts.md
```

Both relative and absolute paths are supported. Imports can be nested up to 5 levels deep.

### Quick Memory Updates

To quickly add a memory during a session:
- Start your message with `#` to add a new memory
- Use `/memory` command to edit memory files directly

### Best Practices

**Be specific with instructions:**
- Good: "Use 2-space indentation for JavaScript files"
- Avoid: "Format code properly"

**Use structure to organize:**
- Group related memories under descriptive markdown headings
- Format individual memories as bullet points

**Review periodically:**
- Update this file as project architecture evolves
- Remove outdated instructions to keep Claude's context accurate

**Separate concerns:**
- Team-shared instructions: Keep in this file (`.claude.md`)
- Personal preferences: Use imports from `~/.claude/` directory
- Organization policies: Managed by IT/DevOps at system level

### Viewing Active Memories

Run `/memory` during a session to see all loaded memory files and edit them as needed.
