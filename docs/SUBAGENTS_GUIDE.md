# 🤖 Subagents Guide - Communications Learning System

> **Specialized AI experts that automatically help you study**

---

## 🎯 What Are These Subagents?

These are **persistent, specialized AI assistants** stored in `.claude/agents/` that are automatically invoked when you need them. Each is an expert in a specific aspect of learning communications systems.

---

## 🤖 Your Subagents

### 1. `formula-deriver` 📐
**Expert in:** Deriving formulas from first principles
**Invoked when:** You ask to derive any formula or understand mathematical foundations

**Specialties:**
- AM, FM, DSB, SSB, VSB modulation
- Noise theory (F, Te, Friis formula)
- Information theory (Shannon-Hartley, capacity)
- Digital modulation (QAM, PSK, FSK)
- Signal analysis (Fourier, convolution)

**Output:** Complete derivations saved to `outputs/derivations/`

**Example requests:**
```
"Derive AM from first principles"
"Show me how to get Friis cascade formula"
"Explain Shannon-Hartley theorem derivation"
"Derive Carson's rule step by step"
```

---

### 2. `exercise-solver` 📝
**Expert in:** Solving exam-type problems step-by-step
**Invoked when:** You need help solving exercises or problems

**Specialties:**
- Noise calculations (F, Te, cascades, SNR)
- Modulation problems (bandwidth, power, efficiency)
- Information theory (capacity, data rate)
- Signal processing (sampling, filtering)
- System design (link budgets)

**Output:** Complete solutions saved to `outputs/solutions/`

**Example requests:**
```
"Solve docs/ejercicio_ruido.txt"
"Help me with this noise problem"
"Solve the AM bandwidth exercise"
"Calculate the SNR for this system"
```

---

### 3. `progress-analyzer` 📊
**Expert in:** Analyzing your learning progress and providing recommendations
**Invoked when:** You want to check progress or get study advice

**Analyzes:**
- Overall progress percentage
- Concepts mastered vs remaining
- Study velocity and trends
- Weak areas needing attention
- Time management and pacing
- Exam readiness

**Output:** Detailed progress reports with recommendations

**Example requests:**
```
"Show my progress"
"How am I doing?"
"What should I focus on?"
"Am I ready for the exam?"
"Analyze my weak areas"
```

---

### 4. `study-session-manager` 🗂️
**Expert in:** Managing study sessions and tracking activities
**Invoked when:** You start/end sessions or need session tracking

**Handles:**
- Starting sessions (loads state, shows context)
- Tracking activities during sessions
- Ending sessions (calculates metrics, updates progress)
- Creating session logs
- Updating learning state

**Output:** Session logs in `sessions/` and updated state files

**Example requests:**
```
"Start a study session"
"End my session"
"What have I done this session?"
"Save my progress"
```

---

## 🚀 How to Use Them

### Automatic Invocation (Recommended)

Just describe what you want naturally:

```
"Derive Friis formula"
→ formula-deriver automatically invoked

"Solve this noise problem"
→ exercise-solver automatically invoked

"How's my progress?"
→ progress-analyzer automatically invoked
```

**I (Claude Code main) will:**
1. Analyze your request
2. Match it to the appropriate subagent
3. Invoke that specialist
4. Present the results to you

---

### Explicit Invocation

You can request a specific subagent:

```
"Use the formula-deriver subagent to derive Shannon-Hartley"
"Ask the exercise-solver to help with this problem"
"Use progress-analyzer to check my status"
```

---

## 🎓 Complete Study Workflow

### Starting Your Study Session

```
You: "Start a study session for rodrigo"
    ↓
study-session-manager invoked
    ↓
Creates session, loads your state
    ↓
Shows: progress, days to exam, recommendations
```

### Studying Theory

```
You: "Derive AM and FM"
    ↓
formula-deriver invoked (can do both)
    ↓
Creates complete derivations
    ↓
Saves to outputs/derivations/
```

### Practicing Problems

```
You: "Solve ejercicio_ruido.txt and ejercicio_AM.txt"
    ↓
exercise-solver invoked for each
    ↓
Step-by-step solutions created
    ↓
Saves to outputs/solutions/
```

### Checking Progress

```
You: "Show my progress"
    ↓
progress-analyzer invoked
    ↓
Analyzes your data
    ↓
Provides recommendations
```

### Ending Session

```
You: "End session"
    ↓
study-session-manager invoked
    ↓
Calculates metrics, updates state
    ↓
Creates session log
```

---

## 💡 Key Benefits

### ✅ Specialized Expertise
Each subagent is an expert in their domain with custom prompts

### ✅ Automatic Selection
You don't need to think about which to use - it happens automatically

### ✅ Persistent & Customizable
Stored in files, can be modified to fit your learning style

### ✅ Consistent Quality
Each subagent follows their specific methodology every time

### ✅ Separate Context
Each has its own context, keeping focused on their specialty

---

## 🛠️ Customizing Subagents

You can edit the JSON files in `.claude/agents/` to customize:

```json
{
  "name": "formula-deriver",
  "description": "What triggers this subagent",
  "systemPrompt": "Detailed instructions for how it behaves",
  "tools": ["Which tools it can use"]
}
```

**To modify:**
1. Open `.claude/agents/[subagent-name].json`
2. Edit the `systemPrompt` or `description`
3. Save the file
4. Changes take effect immediately

---

## 📊 When Each Subagent Is Used

| Your Request | Subagent Invoked | Why |
|--------------|------------------|-----|
| "Derive AM" | formula-deriver | Matches "deriving formulas" |
| "Solve problem X" | exercise-solver | Matches "solving problems" |
| "Show progress" | progress-analyzer | Matches "analyzing progress" |
| "Start session" | study-session-manager | Matches "managing sessions" |
| "Explain noise figure" | formula-deriver | Involves formula understanding |
| "How to calculate SNR?" | exercise-solver | Problem-solving oriented |
| "Am I ready for exam?" | progress-analyzer | Progress assessment |

---

## 🎯 Best Practices

### 1. Be Specific
```
Good: "Derive Friis cascade formula with detailed steps"
Better: "Use formula-deriver to derive Friis cascade, include numerical example"
```

### 2. One Task at a Time
```
Good: "Derive AM"
Less optimal: "Derive AM, FM, solve 3 exercises, check my progress"
   → Better to do separately so each subagent can focus
```

### 3. Trust Automatic Selection
```
You: "Derive Shannon-Hartley"
(Don't need to say "use formula-deriver")
→ It will be selected automatically
```

### 4. Review Session Logs
Check `sessions/` directory to see what you've accomplished

---

## 🔄 Complete Example Session

```
You: "Start session"
→ study-session-manager creates session, shows context

You: "Derive AM from first principles"
→ formula-deriver creates full derivation

You: "Now derive Friis cascade formula"
→ formula-deriver creates another derivation

You: "Solve docs/ejercicio_ruido.txt"
→ exercise-solver solves the 5-part problem

You: "How's my progress?"
→ progress-analyzer shows you've made progress on:
  - 2 derivations completed
  - 1 exercise solved
  - Unit 3 and 7 concepts practiced

You: "End session"
→ study-session-manager saves everything, creates log
```

---

## 📁 Output Locations

All subagent work is saved:

```
outputs/
├── derivations/        ← formula-deriver saves here
│   ├── AM_20251115.md
│   └── Friis_20251115.md
│
└── solutions/          ← exercise-solver saves here
    └── ejercicio_ruido_20251115.md

sessions/               ← study-session-manager saves logs here
└── 2025-11/
    └── 2025-11-15_rodrigo_session.md

state/                  ← Updated by session-manager
├── learning_state.json      ← Your progress
└── current_session.json     ← Active session
```

---

## 🎓 This Is The System You Wanted!

✅ Specialized subagents (not generic Task tool)
✅ Automatically invoked when needed
✅ Persistent across sessions
✅ Customizable to your needs
✅ Each an expert in their domain

**Just talk naturally about what you want to learn, and the right expert will help you!** 🚀

---

**Created:** 2025-11-15
**Subagents:** 4 specialized experts ready to help you ace your exam
