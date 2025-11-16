# Solve Exercise - Communications Systems

**Architecture**: This command uses the **subagent-first** approach.

## What This Command Does

Invokes the **exercise-solver subagent** to solve a communications systems problem step-by-step.

## Subagent Used

- ✅ **exercise-solver** (Opus, 🟢 Green): Expert problem solver for communications systems exercises

## Your Task

1. **Locate the exercise file** (or help user describe the problem)
2. **Invoke exercise-solver subagent** using the Task tool
3. **Pass the problem**: Either file path or problem description
4. **Return results**: Show solution summary and file paths

## Command Format

```
/solve [exercise_file]
```

**Examples:**
- `/solve docs/ejercicio_ruido.txt`
- `/solve exercises/unit7_problem3.md`
- `/solve` (then describe problem interactively)

## Implementation

When user runs `/solve [file]`:

```
Use Task tool:
  subagent_type: "exercise-solver"
  model: "opus"
  prompt: "Solve the communications systems problem in [file].

    The problem should be solved with:
    - Clear identification of given data and what's asked
    - Step-by-step solution with justification
    - All calculations showing units
    - Dimensional validation
    - Final answer summary
    - Key insights and learnings

    Save output to:
    - outputs/solutions/[problem_name]_[date].md
    - .doc/claude/reports/solution_summaries/[problem_name]_summary.md

    Update learning state to reflect:
    - Problem solved
    - Concepts practiced
    - Session activity"
```

## If No File Provided

If user just types `/solve` without a file:

```
You: What problem would you like to solve? You can either:
1. Provide a file path to an exercise
2. Describe the problem directly
3. Tell me the unit and topic (I'll suggest relevant problems)

Example problems available:
- docs/ejercicio_ruido.txt (Unit 7: Noise figure and temperature)
- [List other available problems if any]
```

## After Subagent Completes

1. Read the summary file
2. Show user:
   - Problem type identified
   - Key steps taken
   - Final answers
   - File paths
3. Ask if they want:
   - Clarification on any step
   - Alternative solution method
   - Similar problems to practice
   - Explanation of related concepts

## Example Usage

```
User: /solve docs/ejercicio_ruido.txt

You: I'll use the exercise-solver subagent to solve this problem.

[Invoke Task tool with exercise-solver]

[After completion]
✓ Problem solved!

Type: Noise figure and temperature calculations
Unit: 7 (Noise)

Key Results:
a) Noise figure F = 3 (4.77 dB)
b) Noise temperature Te = 580 K
c) Output SNR = 30 dB
d) F remains 3 (independent of input noise density)
e) For thermal noise: η_in = 1.16×10^-20 W/Hz

Files created:
- outputs/solutions/ejercicio_ruido_20251116.md
- .doc/claude/reports/solution_summaries/ejercicio_ruido_summary.md

Would you like me to:
1. Explain any calculation step in detail
2. Show you similar problems to practice
3. Generate Anki cards from this problem
```

## Problem Types Handled

The exercise-solver subagent can handle:

**Noise Problems:**
- Noise figure calculations
- Noise temperature conversions
- Friis cascade formula
- SNR computations
- Cascaded system analysis

**Modulation Problems:**
- AM/FM/PM analysis
- Bandwidth calculations
- Power efficiency
- Modulation index
- Spectrum analysis

**Digital Modulation:**
- QAM, PSK, FSK, ASK
- Bit error rate (BER)
- Constellation diagrams
- Symbol vs bit rate

**Information Theory:**
- Shannon-Hartley theorem
- Channel capacity
- Data rate limits
- Coding gain

**System Design:**
- Link budget analysis
- System comparisons
- Trade-off analysis

## Important Notes

- **Always use the subagent** - Don't solve problems yourself
- The subagent will show ALL calculation steps with units
- Solutions are validated dimensionally
- Subagent saves complete solutions to files
- Learning state should be updated after solving

## Validation Features

The exercise-solver subagent automatically:
- ✓ Checks dimensional consistency
- ✓ Validates units throughout
- ✓ Verifies answers make physical sense
- ✓ Identifies common mistakes
- ✓ Provides key insights and learnings
