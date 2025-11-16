# 🎓 Communications Learning System - Subagent-First Architecture

> **Intelligent study system for Communications Systems exam preparation (UTN)**
> Uses Claude Code subagents for derivations, problem-solving, and progress tracking

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone [your-repo] communications-learning-system
cd communications-learning-system

# 2. Install minimal dependencies
pip install -r requirements.txt

# 3. Open in Claude Code
claude-code

# 4. Start studying!
# Just ask Claude:
#   "Can you derive Shannon-Hartley theorem?"
#   "Can you solve this noise problem?"
#   "Check my progress"
```

## 📚 What Is This?

An AI-powered learning system using **Claude Code subagents** to help you:

- 🎓 **Derive formulas** from first principles (any level: basic to rigorous)
- ✅ **Solve problems** step-by-step with validation
- 📊 **Track progress** with data-driven recommendations
- 🎯 **Prepare for exams** with focused study plans
- 🤝 **Collaborate** via Git-based state management

## 🤖 The Subagents

| Subagent | Color | Purpose | Model |
|----------|-------|---------|-------|
| 🎓 **formula-deriver** | 🟣 Purple | Adaptive formula derivations (all levels) | Opus |
| ✅ **exercise-solver** | 🟢 Green | Solve exam-style problems | Opus |
| 📊 **progress-analyzer** | 🟡 Amber | Progress tracking & recommendations | Sonnet |
| 🎯 **study-session-manager** | 🟠 Orange | Session coordination | Sonnet |

**Key Feature**: Subagents adapt automatically - no need to choose complexity level!

## 💻 How To Use

### In Claude Code (Primary Interface)

Simply ask Claude naturally:

```
"Can you derive Friis cascade formula?"
→ Invokes formula-deriver subagent
→ Saves to outputs/derivations/

"Can you solve this noise problem?"
→ Invokes exercise-solver subagent
→ Saves to outputs/solutions/

"Check my progress"
→ Invokes progress-analyzer subagent
→ Generates progress report
```

### Slash Commands (Alternative)

```
/derive Shannon-Hartley theorem
/solve docs/ejercicio_ruido.txt
/progress
/start-session rodrigo
/end-session
```

### Python CLI (Session Management)

```bash
# Start study session
python main.py start-session --user rodrigo

# Check progress
python main.py progress

# End session
python main.py end-session --summary "Studied Unit 7"

# Git workflow
git add .
git commit -m "Session: Derived Friis formula"
git push
```

## 🗂️ Project Structure

```
communications-learning-system/
├── .claude/
│   ├── agents/              # Subagent definitions (4 files)
│   ├── commands/            # Slash commands
│   └── SUBAGENT_REFERENCE.md  # Color scheme guide
├── agents/
│   └── coordinator.py       # State management (Python)
├── state/                   # Git-tracked state ⭐
│   ├── learning_state.json  # Global progress
│   └── session_history.jsonl
├── outputs/
│   ├── derivations/         # Formula derivations
│   └── solutions/           # Problem solutions
├── sessions/                # Session logs ⭐
│   └── YYYY-MM/
├── .doc/claude/             # Subagent working files
│   ├── tasks/
│   └── reports/
├── main.py                  # CLI for session management
├── requirements.txt         # Minimal dependencies
├── SYSTEM_ARCHITECTURE.md   # ⭐ Architecture details
└── README.md                # This file
```

## 💡 Key Features

### ✅ Subagent-First Architecture
- **All AI work done by specialized subagents**
- Automatic complexity adaptation
- No decision-making friction
- File-based output for persistence

### ✅ Git-Based Collaboration
- State lives in files, not conversation history
- Multiple users can collaborate
- Sessions are logged and shareable
- Full version control

### ✅ Token Efficiency
- Subagents save work to files
- 80-90% fewer tokens than conversation-based
- Context persists across sessions
- Enables long-term projects

### ✅ Adaptive Rigor
- Formula-deriver adjusts to topic complexity
- Session context influences approach
- Exam focus vs research depth
- Extra clarity when struggling

## 📖 Documentation

- **SYSTEM_ARCHITECTURE.md** - Complete architecture (read this!)
- **.claude/SUBAGENT_REFERENCE.md** - Subagent color scheme and usage
- **state/learning_state_schema.json** - State structure definition

## 🎯 Typical Workflow

### 1. Start Session
```bash
python main.py start-session --user rodrigo
```

### 2. Study in Claude Code
```
You: "Let's study Unit 7: Noise. Can you derive the Friis formula?"

Claude: I'll use the formula-deriver subagent...
[Creates outputs/derivations/friis_cascade_20251116.md]

You: "Now solve this noise problem"

Claude: I'll use the exercise-solver subagent...
[Creates outputs/solutions/noise_problem_20251116.md]
```

### 3. Check Progress
```bash
python main.py progress
# or in Claude Code:
/progress
```

### 4. End Session & Save
```bash
python main.py end-session --summary "Completed Unit 7"
git add .
git commit -m "Session: Friis formula + noise problems"
git push
```

## 🔧 Setup

### Prerequisites
- Python 3.8+
- Git
- Claude Code CLI

### Installation

```bash
# Install dependencies (minimal!)
pip install -r requirements.txt

# Verify setup
python main.py info

# Initialize state (if needed)
python main.py start-session --user your-name
python main.py end-session
```

That's it! The subagents work through Claude Code automatically.

## 📊 Course Coverage

**10 Units / 87 Concepts**:
1. Introducción
2. Análisis de Señales (Fourier, Parseval)
3. Modulación Lineal (AM, DSB, SSB, VSB)
4. Modulación Exponencial (FM, PM, Carson's Rule)
5. Modulación de Pulsos (Sampling, PCM)
6. Modulación Digital (QAM, PSK, FSK)
7. Ruido (Noise Figure, Friis, SNR)
8. Intercomparación de Sistemas
9. Teoría de la Información (Shannon-Hartley, Entropy)
10. Temas Avanzados (OFDM, Spread Spectrum)

## 🎨 Subagent Colors

When you see colored indicators in outputs:
- 🎓 🟣 Purple = Formula derivation
- ✅ 🟢 Green = Problem solved
- 📊 🟡 Amber = Progress data
- 🎯 🟠 Orange = Session info

See `.claude/SUBAGENT_REFERENCE.md` for complete color guide.

## 🤝 Collaboration

Multiple users can work on the same repo:

```bash
# User A
python main.py start-session --user alice
# ... studies ...
python main.py end-session
git commit -m "Alice: Derived Parseval theorem"
git push

# User B
git pull
python main.py start-session --user bob
# ... continues from Alice's work ...
python main.py end-session
git commit -m "Bob: Solved practice problems"
git push
```

State in `learning_state.json` is shared automatically!

## 📈 Progress Tracking

The system tracks:
- Concepts mastered (87 total)
- Problems solved (150 target)
- Study hours and velocity
- Weak areas needing attention
- Days remaining to exam

Check anytime with `/progress` or `python main.py progress`

## 🆘 Troubleshooting

**"Subagent not found"**:
- Check `.claude/agents/` directory exists
- Verify subagent files are present

**"State file error"**:
- Run `python main.py start-session --user test` to initialize
- Check `state/learning_state.json` exists

**"Command not working"**:
- Use commands in Claude Code (recommended)
- Or use Python CLI: `python main.py <command>`

## 🎓 Example Session

```
$ python main.py start-session --user rodrigo

✓ Session started for: rodrigo
📊 Current Status:
  - Overall progress: 8%
  - Active unit: Unit 7 (Noise)
  - Days to exam: 29

💡 Recommendations:
  1. Complete Unit 7 (Noise Temperature, SNR)
  2. Start Unit 9 (Shannon-Hartley - critical!)
  3. Daily problem practice (3-5 problems)

[In Claude Code]
You: "Derive Friis cascade formula"
→ Creates outputs/derivations/friis_cascade_20251116.md

You: "Solve this noise problem: ..."
→ Creates outputs/solutions/noise_problem_20251116.md

$ python main.py end-session --summary "Friis + noise practice"
✓ Session ended
📁 Session log: sessions/2025-11/2025-11-16_rodrigo_session.md
```

## 🚀 What's Different About This System?

**Traditional approach**: Ask Claude questions, get answers in chat

**This system**:
1. ✅ Subagents create **complete files** you can review anytime
2. ✅ State **persists in Git** for collaboration
3. ✅ Progress is **tracked automatically**
4. ✅ Work is **organized and searchable**
5. ✅ **80-90% more token-efficient**

## 📚 Learning Philosophy

The system emphasizes:
- **First principles**: Derive everything from fundamentals
- **Validation**: Dimensional analysis, limiting cases
- **Physical intuition**: Understand WHY, not just WHAT
- **Exam preparation**: Focus on high-value topics
- **Consistent practice**: Track velocity and gaps

## 🎯 Exam Preparation Mode

When exam date approaches, the system:
- Prioritizes weak concepts
- Increases problem-solving focus
- Generates mock exams
- Provides realistic readiness assessment

Current exam date: **2025-12-15**

## 📝 License & Attribution

This system uses Claude Code's subagent architecture for educational purposes.

---

**Version**: 2.1.0
**Architecture**: Subagent-First with File-Based State
**Last Updated**: 2025-11-16

For detailed architecture information, see `SYSTEM_ARCHITECTURE.md`.
For subagent color scheme, see `.claude/SUBAGENT_REFERENCE.md`.

🎓 Happy studying! Good luck with your exam!
