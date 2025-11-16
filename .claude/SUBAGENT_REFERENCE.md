# Subagent Visual Reference Guide

**Quick identification guide for all Claude Code subagents in this system**

## Color Scheme Overview

Each subagent has a unique color and emoji for easy visual identification in logs, reports, and command outputs.

```
📘 🔵 Blue   → Basic derivations (Sonnet, fast)
🎓 🟣 Purple → Advanced derivations (Opus, rigorous)
✅ 🟢 Green  → Problem solving (Opus, complete solutions)
📊 🟡 Amber  → Progress analysis (Sonnet, data-driven)
🎯 🟠 Orange → Session management (Sonnet, coordination)
```

---

## Detailed Subagent Profiles

### 📘 Formula Deriver (🔵 Blue)

**File**: `.claude/agents/formula-deriver.md`
**Model**: Sonnet (fast, cost-effective)
**Color**: 🔵 Blue
**Emoji**: 📘

**Purpose**:
- Basic formula derivations
- Standard topics (simple AM/FM, Fourier basics)
- Teaching-focused explanations
- Fundamental concepts

**Use when**:
- Deriving straightforward formulas
- Student needs clear pedagogical approach
- Topic is well-established and standard
- Speed and cost-efficiency matter

**Example output file**: `outputs/derivations/AM_basic_20251116.md`

---

### 🎓 Advanced Formula Deriver (🟣 Purple)

**File**: `.claude/agents/comms-formula-deriver.md`
**Model**: Opus (advanced, thorough)
**Color**: 🟣 Purple
**Emoji**: 🎓

**Purpose**:
- Complex communications systems derivations
- Rigorous mathematical treatment
- Advanced topics (QAM, OFDM, Shannon-Hartley)
- Expert-level analysis

**Use when**:
- Deriving complex formulas from first principles
- Need rigorous mathematical justification
- Advanced modulation theory
- Noise analysis (Friis, cascaded systems)
- Information theory proofs

**Example output file**: `outputs/derivations/shannon_hartley_comprehensive_20251116.md`

---

### ✅ Exercise Solver (🟢 Green)

**File**: `.claude/agents/exercise-solver.md`
**Model**: Opus (problem-solving focus)
**Color**: 🟢 Green
**Emoji**: ✅

**Purpose**:
- Solve exam-style problems step-by-step
- Complete solutions with validation
- Dimensional analysis and sanity checks
- Problem-solving practice

**Use when**:
- Student has a specific problem to solve
- Need complete solution with all steps
- Preparing for exams
- Want validation and insights

**Example output file**: `outputs/solutions/noise_problem_20251116.md`

**Problem types**:
- Noise calculations (F, Te, SNR)
- Modulation analysis (bandwidth, power)
- Digital modulation (BER, constellations)
- Information theory (capacity, data rate)
- System design (link budgets)

---

### 📊 Progress Analyzer (🟡 Amber)

**File**: `.claude/agents/progress-analyzer.md`
**Model**: Sonnet (analytical)
**Color**: 🟡 Amber
**Emoji**: 📊

**Purpose**:
- Analyze learning progress
- Identify weak areas
- Provide data-driven recommendations
- Track study velocity

**Use when**:
- Student wants to check progress
- Need honest assessment of readiness
- Planning study schedule
- Identifying gaps before exam

**Example output file**: `.doc/claude/reports/progress_reports/progress_20251116.md`

**Analysis includes**:
- Overall completion percentage
- Learning velocity (concepts/week)
- Time remaining vs. work needed
- Weak area identification
- Personalized study recommendations

---

### 🎯 Study Session Manager (🟠 Orange)

**File**: `.claude/agents/study-session-manager.md`
**Model**: Sonnet (orchestration)
**Color**: 🟠 Orange
**Emoji**: 🎯

**Purpose**:
- Coordinate study sessions
- Load and save session state
- Track activities during sessions
- Generate session summaries

**Use when**:
- Starting a new study session
- Ending a session (need summary)
- Need handoff for collaborators
- Tracking session activities

**Example output file**: `sessions/2025-11/2025-11-16_rodrigo_session.md`

**Session management**:
- Load current learning state
- Create session context
- Track activities (derivations, problems)
- Calculate session metrics
- Update progress
- Generate handoff notes

---

## Usage in Commands

### /derive [formula]
Invokes: 📘 Blue (basic) or 🎓 Purple (advanced)

### /solve [file]
Invokes: ✅ Green

### /progress
Invokes: 📊 Amber

### /start-session
Uses: Python CLI (state management)
Context for: 🎯 Orange

### /end-session
Uses: Python CLI (state management)
Summary by: 🎯 Orange

---

## Color Legend in Reports

When you see these colors/emojis in outputs:

| Symbol | Meaning |
|--------|---------|
| 📘 🔵 | Basic derivation work |
| 🎓 🟣 | Advanced derivation work |
| ✅ 🟢 | Problem solved |
| 📊 🟡 | Progress/metrics data |
| 🎯 🟠 | Session information |

---

## Model Selection Guide

**When to use Sonnet (faster, cheaper)**:
- 📘 Basic derivations
- 📊 Progress analysis
- 🎯 Session management

**When to use Opus (more capable, thorough)**:
- 🎓 Complex derivations
- ✅ Problem solving (exam-level)

---

## File Naming Conventions

Subagents save files with consistent naming:

**Derivations**:
- Blue: `outputs/derivations/[topic]_basic_[date].md`
- Purple: `outputs/derivations/[topic]_comprehensive_[date].md`

**Solutions**:
- Green: `outputs/solutions/[problem]_solution_[date].md`

**Progress**:
- Amber: `.doc/claude/reports/progress_reports/progress_[date].md`

**Sessions**:
- Orange: `sessions/[YYYY-MM]/[date]_[user]_session.md`

---

## Quick Reference Table

| Subagent | Color | Emoji | Model | Use Case |
|----------|-------|-------|-------|----------|
| formula-deriver | 🔵 Blue | 📘 | Sonnet | Basic derivations |
| comms-formula-deriver | 🟣 Purple | 🎓 | Opus | Advanced derivations |
| exercise-solver | 🟢 Green | ✅ | Opus | Problem solving |
| progress-analyzer | 🟡 Amber | 📊 | Sonnet | Progress tracking |
| study-session-manager | 🟠 Orange | 🎯 | Sonnet | Session coordination |

---

## Integration with System Architecture

The color scheme reinforces the **subagent-first architecture**:

1. **AI Work** → Subagents (with colors)
   - 📘🎓 Derivations
   - ✅ Problem solving
   - 📊 Analysis

2. **State Management** → Python CLI (no subagent)
   - Session start/end
   - State persistence
   - Progress tracking

3. **File-Based Context** → All subagents read/write files
   - Input: `state/`, `.doc/claude/tasks/`
   - Output: `outputs/`, `.doc/claude/reports/`

---

## Visual Workflow

```
User Request
     │
     ▼
Commands dispatch to:
     │
     ├─── 📘 Blue → Basic formulas
     ├─── 🎓 Purple → Advanced theory
     ├─── ✅ Green → Problems
     ├─── 📊 Amber → Progress
     └─── 🎯 Orange → Sessions
```

All subagents save work to files → Git enables collaboration

---

**Version**: 2.0.1
**Last Updated**: 2025-11-16
**Color Scheme Rationale**: Each color reflects the subagent's function and cognitive style
