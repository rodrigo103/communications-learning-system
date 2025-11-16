# Context Management System for Sub Agents

This directory contains the infrastructure for efficient context management across all sub agents in the communications learning system.

## 📁 Directory Structure

```
.doc/claude/
├── README.md                          # This file
├── SUBAGENT_IMPROVEMENTS.md          # Detailed explanation of improvements
├── QUICK_REFERENCE.md                # Quick reference for using the system
├── tasks/
│   └── current_session_context.md    # Active session context (created at session start)
└── reports/
    ├── derivation_summaries/         # Summaries from formula derivation agents
    ├── solution_summaries/           # Summaries from exercise solver
    ├── progress_reports/             # Reports from progress analyzer
    └── session_contexts/             # Archived session contexts
```

## 🎯 Purpose

This system implements **file-based context management** to:

1. **Reduce token usage by 80-90%** - Detailed work stays in files, only summaries in conversation
2. **Maintain context across sessions** - Context survives conversation compacts and session boundaries
3. **Improve agent coordination** - All agents read/write shared context files
4. **Create learning history** - Archived contexts and summaries show progression over time

## 🚀 Quick Start

### For Users

Just use the system normally! The improvements are transparent:

```bash
# Start studying
/start-session

# Study theory
/derive AM formula

# Practice problems
/solve exercises/unit3/problems.md

# Check progress
/progress

# End session
/end-session
```

**What's different:**
- Responses are more concise (point to files instead of full content)
- Context persists across days
- Much lower token usage = lower cost

### For Developers/Curious Users

**Read these in order:**

1. **SUBAGENT_IMPROVEMENTS.md** - Comprehensive explanation of all changes
2. **QUICK_REFERENCE.md** - Practical guide for using the system
3. **.claude.md** (project root) - Main agent configuration

## 📊 Key Benefits

### Token Efficiency
- **Before**: Full derivation in chat (~5,000 tokens)
- **After**: Summary in chat (~300 tokens)
- **Savings**: ~94% reduction per derivation

### Better Study Experience
- Detailed work preserved in organized files
- Quick summaries for reference
- Context-aware recommendations
- Historical tracking of learning

### Improved Coordination
- Session manager creates context at start
- Formula derivers read context to tailor work
- Exercise solver sees what's being studied
- Progress analyzer understands recent activities
- All agents update shared context

## 🔧 How It Works

### The Flow

```
1. Session Start
   └─→ study-session-manager creates current_session_context.md

2. User Request (e.g., "derive AM formula")
   └─→ Main agent updates context: "Working on AM theory"
   └─→ Main agent invokes formula-deriver with context reference
   └─→ formula-deriver reads context
   └─→ formula-deriver creates full derivation in outputs/derivations/
   └─→ formula-deriver creates summary in .doc/claude/reports/derivation_summaries/
   └─→ formula-deriver returns brief message with file locations
   └─→ Main agent reads summary
   └─→ Main agent updates context: "Completed AM derivation"
   └─→ User sees brief message + file locations

3. Session End
   └─→ study-session-manager archives current_session_context.md
   └─→ Context preserved for next session
```

### Context File

**Location**: `.doc/claude/tasks/current_session_context.md`

**Purpose**: Shared state that all agents can read and update

**Contains**:
- Current study focus
- Recent activities
- Work completed this session
- Key insights
- Next steps
- Weak areas to address

### Summary Reports

**Purpose**: Brief reports that capture essence without full detail

**Types**:
- **Derivation summaries**: Key formulas, insights, next steps
- **Solution summaries**: Problem type, answers, skills reinforced
- **Progress summaries**: Quick stats, priorities, goals

**Location**: `.doc/claude/reports/[category]/`

## 📚 Documentation

### For Understanding the System
- **SUBAGENT_IMPROVEMENTS.md**: Complete explanation with examples
- **how-sub-agents-work.md** (project root): Original best practices guide

### For Using the System
- **QUICK_REFERENCE.md**: Fast lookup for common tasks
- **.claude.md** (project root): Main agent configuration

### For Sub Agents
Each agent file in `.claude/agents/` now has "Context Management" section:
- formula-deriver.md
- exercise-solver.md
- progress-analyzer.md
- comms-formula-deriver.md
- study-session-manager.md

## 🧪 Testing

To verify the system works:

```bash
# 1. Start a session
/start-session

# Check: Should create .doc/claude/tasks/current_session_context.md

# 2. Do a derivation
/derive [some formula]

# Check: Should create:
# - outputs/derivations/[formula]_[date].md
# - .doc/claude/reports/derivation_summaries/[formula]_[date]_summary.md
# Response should be brief (~10 lines) not full derivation

# 3. End session
/end-session

# Check: Should archive context to:
# - .doc/claude/reports/session_contexts/context_[date].md
```

## 🔍 Finding Past Work

### Recent Work
```bash
# Derivation summaries
ls .doc/claude/reports/derivation_summaries/

# Solution summaries
ls .doc/claude/reports/solution_summaries/

# Progress reports
ls .doc/claude/reports/progress_reports/
```

### Full Details
```bash
# Full derivations
ls outputs/derivations/

# Full solutions
ls outputs/solutions/

# Session logs
ls sessions/YYYY-MM/
```

### Historical Context
```bash
# Archived session contexts
ls .doc/claude/reports/session_contexts/
```

## 💡 Tips

### For Efficient Token Usage
- Trust the system - don't ask for full content if summary is sufficient
- Use file references: "as shown in [file]"
- Point to files when reviewing: "check [file] for details"

### For Better Learning
- Read summaries for quick review
- Read full files for deep understanding
- Check archived contexts to see progression
- Use summaries to identify knowledge gaps

### For Maintenance
- Archive context periodically if it grows large
- Old summaries can be archived/deleted after exam
- Session contexts provide study timeline

## 🐛 Troubleshooting

**Q: Agent didn't create summary?**
A: Older agents might not have new instructions. Check agent file has "Context Management" section.

**Q: Context file missing?**
A: Start a session with `/start-session` to create it, or main agent should create it before first study activity.

**Q: Token usage still high?**
A: Ensure agents are returning brief messages, not full content. Check if they're creating summaries properly.

**Q: Want to see full derivation?**
A: Read the file at `outputs/derivations/[filename].md` - full details are there!

## 📈 Expected Results

### Token Usage Reduction
- Typical study session: ~50,000 tokens → ~10,000 tokens
- Long derivations: ~8,000 tokens → ~400 tokens
- Problem solutions: ~4,000 tokens → ~300 tokens

### Improved Experience
- Faster responses (less token processing)
- Better context continuity
- Organized learning materials
- Clear study timeline

### Cost Savings
- 80-90% reduction in API costs
- Can afford more sophisticated derivations
- Can study longer sessions

## 🎓 Philosophy

**Principle**: "Sub agents work best when they're just looking for information and providing a small amount of summary back to the main conversation thread." - Adam Wolf, Claude Code team

**Adaptation for Education**: While the original best practice says sub agents should only do research/planning, we adapted it for educational use:
- Agents still produce the actual work (derivations/solutions) since those ARE the deliverables
- But they save detailed work to files
- And return only brief summaries to conversation
- Context is managed through file system, not conversation history

**Result**: Best of both worlds - complete detailed work + token efficiency

## 🔄 Version History

- **2025-11-15**: Initial implementation
  - Created directory structure
  - Updated all 5 sub agents with context management
  - Created main agent configuration (.claude.md)
  - Created documentation (this file, improvements, quick reference)

---

**Questions?** Check QUICK_REFERENCE.md for common scenarios or SUBAGENT_IMPROVEMENTS.md for detailed explanation.

**Ready to study?** Just use `/start-session` and the system handles the rest! 🚀
