# Derive Formula - Communications Systems

**Architecture**: This command uses the **subagent-first** approach.

## What This Command Does

Invokes the appropriate formula derivation subagent to derive the requested formula from first principles.

## Subagents Used

- 📘 **formula-deriver** (Sonnet, 🔵 Blue): For basic/standard derivations
- 🎓 **comms-formula-deriver** (Opus, 🟣 Purple): For complex communications systems derivations

## Your Task

1. **Determine complexity**: Is this a basic or advanced communications topic?
2. **Invoke appropriate subagent** using the Task tool
3. **Pass context**: Formula name, any specific requirements from user
4. **Return results**: Show the derivation summary and file paths

## Decision Logic

**Use comms-formula-deriver (Opus) for:**
- Advanced modulation theory (QAM, OFDM)
- Noise analysis (Friis, cascaded systems)
- Information theory (Shannon-Hartley)
- Complex signal processing
- Topics requiring rigorous mathematical treatment

**Use formula-deriver (Sonnet) for:**
- Basic modulation (simple AM, FM)
- Standard Fourier analysis
- Basic probability/statistics
- Straightforward derivations

## Command Format

```
/derive [formula_name]
```

**Examples:**
- `/derive Shannon-Hartley theorem`
- `/derive Friis cascade formula`
- `/derive AM modulation spectrum`
- `/derive Carson's rule`

## Implementation

When user runs `/derive [formula]`:

```
Use Task tool:
  subagent_type: "comms-formula-deriver" (or "formula-deriver" if basic)
  model: "opus" (or "sonnet" if basic)
  prompt: "Derive [formula] from first principles. Include:
    - Clear starting point and assumptions
    - Step-by-step mathematical derivation
    - Key results and insights
    - Practical implications
    - Related concepts

    Save output to outputs/derivations/[formula]_[date].md
    Create summary in .doc/claude/reports/derivation_summaries/"
```

## After Subagent Completes

1. Read the summary file
2. Show user key results
3. Provide file paths
4. Ask if they want:
   - More detail on any step
   - Examples/applications
   - Related derivations

## Example Usage

```
User: /derive Friis cascade formula

You: I'll use the comms-formula-deriver subagent to derive
     the Friis cascade formula for you.

[Invoke Task tool with comms-formula-deriver]

[After completion]
✓ Derivation complete!

Key Result:
F_total = F₁ + (F₂-1)/G₁ + (F₃-1)/(G₁G₂) + ...

Files created:
- outputs/derivations/friis_cascade_20251116.md
- .doc/claude/reports/derivation_summaries/friis_cascade_summary.md

Would you like me to:
1. Explain any specific step in detail
2. Show numerical examples
3. Derive special cases (lossy components, etc.)
```

## Important Notes

- **Always use subagents** - Don't do derivations yourself
- Choose the right subagent (Opus for complex, Sonnet for basic)
- Provide clear, specific prompts to subagents
- Return concise summaries to user, with file paths for details
- The subagent will save full derivations to files
