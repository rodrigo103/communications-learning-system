# Subagent Visual Reference Guide

**Quick identification guide for all Claude Code subagents in this system**

## Color Scheme Overview

Each subagent has a unique color and emoji for easy visual identification in logs, reports, and command outputs.

```
🎓 🟣 Purple → Formula derivations (Opus, adaptive rigor)
✅ 🟢 Green  → Problem solving (Opus, complete solutions)
📊 🟡 Amber  → Progress analysis (Sonnet, data-driven)
🎯 🟠 Orange → Session management (Sonnet, coordination)
```

---

## Detailed Subagent Profiles

### 🎓 Formula Deriver (🟣 Purple)

**File**: `.claude/agents/formula-deriver.md`
**Model**: Opus (most capable)
**Color**: 🟣 Purple
**Emoji**: 🎓

**Purpose**:
- Comprehensive formula derivations from first principles
- Adapts pedagogical level automatically (undergraduate to graduate)
- Rigorous mathematical treatment with clear explanations
- All communications systems topics

**Key Feature - Adaptive Rigor**:
The subagent intelligently adjusts its approach based on:
- Topic complexity (basic AM vs advanced Shannon-Hartley)
- Session context (exam prep vs research)
- Student indicators (struggling vs familiar)

**Use for**:
- ANY formula derivation request
- Basic topics: Gets clear pedagogical treatment
- Advanced topics: Gets rigorous mathematical depth
- Exam prep: Focuses on key steps and common mistakes

**Topics covered**:
- Modulation (AM, FM, PM, QAM, PSK, FSK)
- Noise analysis (F, Te, Friis, SNR)
- Information theory (Shannon-Hartley, entropy, capacity)
- Signal processing (Fourier, convolution, PSD)
- Probability (Gaussian processes, error probabilities)

**Quality guarantees**:
- Complete variable definitions
- Every step justified
- Physical interpretations
- Dimensional validation
- Limiting case analysis
- Applications and when to use

**Example output files**:
- Basic: `outputs/derivations/AM_spectrum_20251116.md` (10 pages, pedagogical)
- Advanced: `outputs/derivations/shannon_hartley_rigorous_20251116.md` (20+ pages, proof from axioms)

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
Invokes: 🎓 Purple (formula-deriver)
- Automatically adapts to topic complexity
- No need to choose basic vs advanced

### /solve [file]
Invokes: ✅ Green (exercise-solver)

### /progress
Invokes: 📊 Amber (progress-analyzer)

### /start-session
Uses: Python CLI (coordinator for state management)
Context for: 🎯 Orange

### /end-session
Uses: Python CLI (coordinator for state management)
Summary by: 🎯 Orange

---

## Color Legend in Reports

When you see these colors/emojis in outputs:

| Symbol | Meaning |
|--------|---------|
| 🎓 🟣 | Formula derivation work (any level) |
| ✅ 🟢 | Problem solved |
| 📊 🟡 | Progress/metrics data |
| 🎯 🟠 | Session information |

---

## Model Selection Guide

**Opus (advanced, thorough)**:
- 🎓 Formula derivations (adaptable complexity)
- ✅ Problem solving (exam-level rigor)

**Sonnet (faster, efficient)**:
- 📊 Progress analysis
- 🎯 Session management

---

## File Naming Conventions

Subagents save files with consistent naming:

**Derivations**:
- Purple: `outputs/derivations/[topic]_[date].md`
  - Filename reflects topic, not complexity
  - Subagent adapts content internally

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
| formula-deriver | 🟣 Purple | 🎓 | Opus | ANY derivation (adaptive) |
| exercise-solver | 🟢 Green | ✅ | Opus | Problem solving |
| progress-analyzer | 🟡 Amber | 📊 | Sonnet | Progress tracking |
| study-session-manager | 🟠 Orange | 🎯 | Sonnet | Session coordination |

---

## Integration with System Architecture

The color scheme reinforces the **subagent-first architecture**:

1. **AI Work** → Subagents (with colors)
   - 🎓 Derivations (all levels)
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
     ├─── 🎓 Purple → Any formula derivation
     ├─── ✅ Green → Problems
     ├─── 📊 Amber → Progress
     └─── 🎯 Orange → Sessions
```

All subagents save work to files → Git enables collaboration

---

## Why One Derivation Subagent?

**Previous**: Had two subagents (Blue/basic and Purple/advanced)
**Problem**: Overlap, confusion about which to use
**Solution**: Merged into one powerful subagent

**Benefits**:
✅ No decision-making friction ("Is this basic or advanced?")
✅ Opus model handles everything from simple to complex
✅ Automatic adaptation based on context
✅ Consistent quality across all derivations
✅ Simpler system architecture

**How it works**:
The Purple subagent reads session context and:
- Adjusts mathematical depth
- Balances rigor with pedagogy
- Emphasizes exam focus when needed
- Provides extra clarity for struggling students
- Moves to graduate-level when appropriate

**Example**:
- User: "Derive AM bandwidth" → Gets clear undergraduate treatment
- User: "Derive Shannon-Hartley from information theory axioms" → Gets rigorous proof
- Same subagent, different approach based on request!

---

**Version**: 2.1.0
**Last Updated**: 2025-11-16
**Major Change**: Merged derivation subagents into single adaptive Purple subagent
