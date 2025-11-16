# Derive Formula - Communications Systems

**Architecture**: This command uses the **subagent-first** approach.

## What This Command Does

Invokes the **formula-deriver subagent** to derive the requested formula from first principles. The subagent automatically adapts its pedagogical level based on the complexity of the topic and session context.

## Subagent Used

- 🎓 **formula-deriver** (Opus, 🟣 Purple): Comprehensive formula derivations at any level

## Your Task

1. **Invoke formula-deriver subagent** using the Task tool
2. **Pass the formula name** and any specific requirements from user
3. **Return results**: Show the derivation summary and file paths

## Key Feature: Adaptive Rigor

The formula-deriver automatically adjusts its approach:
- **Basic topics** (e.g., simple AM): Clear pedagogical treatment
- **Advanced topics** (e.g., Shannon-Hartley): Rigorous mathematical derivation
- **Session context**: Checks student's level and exam focus

You don't need to choose complexity level - the subagent does this intelligently.

## Command Format

```
/derive [formula_name]
```

**Examples:**
- `/derive Shannon-Hartley theorem`
- `/derive Friis cascade formula`
- `/derive AM modulation spectrum`
- `/derive Carson's rule`
- `/derive Parseval's theorem`

## Implementation

When user runs `/derive [formula]`:

```
Use Task tool:
  subagent_type: "formula-deriver"
  model: "opus"
  prompt: "Derive [formula] from first principles.

    Please provide a comprehensive derivation including:
    - Clear starting point and assumptions
    - Step-by-step mathematical derivation with justification
    - Physical interpretation at each stage
    - Key results and insights
    - Validation (dimensional analysis, limiting cases)
    - Practical implications and applications
    - Related concepts to study next

    Adapt the mathematical rigor based on topic complexity and session context.

    Save outputs to:
    - Full derivation: outputs/derivations/[topic]_[date].md
    - Summary: .doc/claude/reports/derivation_summaries/[topic]_[date]_summary.md"
```

## After Subagent Completes

1. Read the summary file
2. Show user:
   - Key result formula
   - Level of treatment used
   - File paths for full derivation
3. Ask if they want:
   - More detail on any specific step
   - Examples or applications
   - Related derivations
   - Numerical examples

## Example Usage

```
User: /derive Friis cascade formula

You: I'll use the formula-deriver subagent to derive the Friis cascade formula.

[Invoke Task tool with formula-deriver]

[After completion]
✓ Derivation complete!

📐 Friis Cascade Formula Derivation

Level: Undergraduate (exam-focused)

Key Result:
F_total = F₁ + (F₂-1)/G₁ + (F₃-1)/(G₁G₂) + ...

Physical Insight:
- First stage noise figure dominates (if G₁ >> 1)
- High gain first stage minimizes overall noise figure
- Critical for low-noise amplifier (LNA) design

Files created:
- Full: outputs/derivations/friis_cascade_20251116.md
- Summary: .doc/claude/reports/derivation_summaries/friis_cascade_20251116_summary.md

The derivation includes:
✓ Starting from basic noise definitions
✓ Cascaded system analysis
✓ Step-by-step proof with 12 equations
✓ Dimensional validation
✓ Design guidelines

Would you like me to:
1. Explain any specific step in more detail
2. Show numerical examples
3. Derive related cases (lossy components, impedance mismatches)
4. Solve practice problems using this formula
```

## Topics Covered

The formula-deriver can handle any communications systems formula:

**Modulation:**
- AM, DSB-SC, SSB, VSB (envelope, spectrum, power)
- FM, PM (instantaneous frequency, Bessel analysis, Carson's rule)
- QAM, PSK, FSK, ASK (constellation, spectrum, bandwidth)

**Noise:**
- Noise figure, noise temperature
- Friis cascade formula
- SNR in various modulation schemes
- Noise bandwidth

**Information Theory:**
- Shannon-Hartley theorem
- Channel capacity
- Entropy, mutual information
- Source and channel coding theorems

**Signal Processing:**
- Fourier transform properties
- Convolution, correlation
- Power spectral density
- Hilbert transform
- Sampling theorem

## Automatic Adaptations

The subagent automatically:
- Checks session context for student's focus
- Adjusts mathematical depth appropriately
- Emphasizes exam-relevant aspects when needed
- Provides extra clarity for struggling students
- Moves faster for familiar topics
- Includes validation and sanity checks
- Suggests related practice problems

## Important Notes

- **Single powerful subagent** - No need to choose complexity level
- Uses Opus model (most capable) for all derivations
- Automatically balances rigor with pedagogy
- Always validates results (dimensions, limits, special cases)
- Provides both mathematical depth and physical intuition
- Saves comprehensive files for review and study

## Quality Guarantee

Every derivation includes:
✓ Complete variable definitions
✓ Clear statement of assumptions
✓ Justification for each step
✓ Physical interpretation
✓ Dimensional analysis
✓ At least one limiting case check
✓ Applications and when to use
✓ Related concepts for further study

## Example Invocations

**Basic request:**
```
User: Derive AM bandwidth
You: [Invokes formula-deriver with "AM bandwidth derivation"]
Result: Clear undergraduate treatment with spectrum analysis
```

**Advanced request:**
```
User: Derive Shannon-Hartley from information theory fundamentals
You: [Invokes formula-deriver with "Shannon-Hartley theorem from first principles"]
Result: Rigorous graduate-level treatment with entropy, channel coding concepts
```

**Exam prep:**
```
User: I have an exam on noise - derive Friis formula
You: [Invokes formula-deriver, which sees "exam" in session context]
Result: Focused on key steps, common mistakes, verification techniques
```

The subagent intelligently adapts to all these scenarios without you having to specify the level!
