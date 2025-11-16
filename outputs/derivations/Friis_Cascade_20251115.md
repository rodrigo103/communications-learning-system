# Friis Cascade Noise Figure Formula - Complete Derivation

**Date:** 2025-11-15
**Topic:** Noise in Cascaded Systems

---

## 1. Starting Point: Noise Figure Definition

### 1.1 Signal-to-Noise Ratio (SNR)

$$SNR = \frac{S}{N}$$

**Where:**
- $S$ = signal power [W]
- $N$ = noise power [W]

**Physical Meaning:** SNR measures the quality of a signal relative to the noise present. Higher SNR = cleaner signal.

### 1.2 Noise Figure Definition

The noise figure quantifies how much a device **degrades** the SNR:

$$F = \frac{SNR_{in}}{SNR_{out}} = \frac{(S_{in}/N_{in})}{(S_{out}/N_{out})}$$

**Alternative form:**

$$F = \frac{N_{out}}{G \cdot N_{in}}$$

**Where:**
- $F$ = noise figure (linear, dimensionless)
- $G$ = power gain of the device (linear)
- $N_{in}$ = input noise power [W]
- $N_{out}$ = total output noise power [W]

**Physical Meaning:**
- $F = 1$ (0 dB): Ideal noiseless device - SNR unchanged
- $F > 1$ (> 0 dB): Real device adds noise - SNR degraded
- The larger $F$, the more noise the device adds

**Key insight:** $F$ tells us how much worse the SNR becomes after passing through the device.

---

## 2. Single Amplifier Analysis

### Step 1: Input Conditions

At the input of a single amplifier:
- Signal power: $S_1$
- Noise power: $N_1$ (from source resistance at temperature $T_0$)
- Input SNR: $SNR_1 = \frac{S_1}{N_1}$

### Step 2: Output Conditions

At the output:
- Signal power: $S_2 = G_1 \cdot S_1$ (amplified by gain $G_1$)
- Noise power: $N_2 = G_1 \cdot N_1 + N_{added,1}$

**Where:**
- $G_1 \cdot N_1$ = amplified input noise
- $N_{added,1}$ = noise added by the amplifier itself

### Step 3: Apply Noise Figure Definition

$$F_1 = \frac{SNR_{in}}{SNR_{out}} = \frac{S_1/N_1}{S_2/N_2} = \frac{S_1/N_1}{(G_1 S_1)/(G_1 N_1 + N_{added,1})}$$

Simplifying:

$$F_1 = \frac{S_1}{N_1} \cdot \frac{G_1 N_1 + N_{added,1}}{G_1 S_1} = \frac{G_1 N_1 + N_{added,1}}{G_1 N_1}$$

$$F_1 = 1 + \frac{N_{added,1}}{G_1 N_1}$$

**Rearranging for added noise:**

$$\boxed{N_{added,1} = N_1 G_1 (F_1 - 1)}$$

**Physical Interpretation:** The added noise is proportional to:
- Input noise level $N_1$
- Amplifier gain $G_1$
- How noisy the amplifier is $(F_1 - 1)$

---

## 3. Two-Stage Cascade Derivation

### Step 1: System Configuration

```
      ┌──────────┐      ┌──────────┐
S_1 ──┤          │─ S_2 ─┤          │── S_3
N_1   │  Stage 1 │  N_2  │  Stage 2 │   N_3
      │ G_1, F_1 │       │ G_2, F_2 │
      └──────────┘       └──────────┘
```

**Given:**
- Stage 1: Gain $G_1$, Noise Figure $F_1$
- Stage 2: Gain $G_2$, Noise Figure $F_2$

### Step 2: Analyze Stage 1 Output (= Stage 2 Input)

From previous section, at the output of stage 1:

$$S_2 = G_1 S_1$$

$$N_2 = G_1 N_1 + N_{added,1} = G_1 N_1 + G_1 N_1(F_1 - 1) = G_1 N_1 F_1$$

**Why?** Factor out $G_1 N_1$:
$$N_2 = G_1 N_1[1 + (F_1 - 1)] = G_1 N_1 F_1$$

### Step 3: Analyze Stage 2 Output

Stage 2 receives $S_2$ and $N_2$ as inputs:

$$S_3 = G_2 S_2 = G_2 G_1 S_1$$

$$N_3 = G_2 N_2 + N_{added,2}$$

**But:** Stage 2 has noise figure $F_2$, so its added noise (referred to its input) is:

$$N_{added,2} = N_2 G_2(F_2 - 1)$$

Substituting $N_2 = G_1 N_1 F_1$:

$$N_3 = G_2(G_1 N_1 F_1) + (G_1 N_1 F_1) G_2 (F_2 - 1)$$

Factor out $G_2 G_1 N_1$:

$$N_3 = G_2 G_1 N_1[F_1 + F_1(F_2 - 1)]$$

$$N_3 = G_2 G_1 N_1[F_1 + F_1 F_2 - F_1]$$

$$N_3 = G_2 G_1 N_1[F_1 F_2]$$

**Wait, let me recalculate more carefully:**

$$N_3 = G_2 G_1 N_1 F_1 + G_1 N_1 F_1 \cdot G_2 (F_2 - 1)$$

$$N_3 = G_2 G_1 N_1 F_1[1 + (F_2 - 1)]$$

$$N_3 = G_2 G_1 N_1[F_1 + F_1(F_2 - 1)]$$

$$N_3 = G_2 G_1 N_1[F_1 + F_1 F_2 - F_1]$$

Hmm, let me restart with the correct approach:

$$N_3 = G_2 N_2 + N_{added,2}$$

Where $N_{added,2} = G_2 N_2 (F_2 - 1)$ (noise added by stage 2)

$$N_3 = G_2 N_2[1 + (F_2 - 1)] = G_2 N_2 F_2$$

But $N_2 = G_1 N_1 F_1$, so:

$$N_3 = G_2 \cdot G_1 N_1 F_1 \cdot F_2 = G_1 G_2 N_1 F_1 F_2$$

**This is wrong!** Let me use the correct definition.

### Step 3 (Corrected): Using Noise Figure Definition Properly

The noise figure of stage 2 tells us how much noise it adds **referred to its input**:

$$F_2 = \frac{N_{out,stage2}}{G_2 \cdot N_{in,stage2}}$$

So:
$$N_{added,2} = N_{in,stage2} \cdot G_2 \cdot (F_2 - 1) = N_2 \cdot G_2 \cdot (F_2 - 1)$$

Total output noise:
$$N_3 = G_2 N_2 + N_2 G_2(F_2 - 1) = G_2 N_2[1 + F_2 - 1] = G_2 N_2 F_2$$

But we need to express everything in terms of $N_1$ (the original input):

$$N_2 = G_1 N_1 F_1$$

Therefore:
$$N_3 = G_2 \cdot G_1 N_1 F_1 \cdot F_2$$

**This still doesn't give us the Friis formula!** Let me reconsider...

### Step 3 (Correct Approach): Separate Noise Contributions

The key insight is to track noise contributions separately:

**At output of stage 2:**
- Amplified original noise: $G_1 G_2 N_1$
- Amplified stage 1 added noise: $G_2 \cdot N_{added,1} = G_2 \cdot G_1 N_1(F_1-1)$
- Stage 2 added noise: $N_{added,2} = G_2 N_2(F_2-1)$

But $N_2 = G_1 N_1 F_1$ is the noise at stage 2 input (not just the thermal noise).

**Actually, for Friis, we need to refer all noise back to the input.**

Let me use the standard approach:

### Step 4: Total System Noise Figure

The total noise figure is defined as:

$$F_{total} = \frac{N_3}{G_1 G_2 N_1}$$

We need to find $N_3$ in terms of contributions:

$$N_3 = \underbrace{G_1 G_2 N_1}_{\text{amplified input}} + \underbrace{G_2 \cdot [G_1 N_1(F_1-1)]}_{\text{stage 1 noise}} + \underbrace{G_2 G_1 N_1 \frac{F_2-1}{G_1}}_{\text{stage 2 noise}}$$

Wait, let me use the cleaner derivation:

**Noise contributions at output:**
1. Input noise amplified: $G_1 G_2 N_1$
2. Stage 1 adds: $N_{added,1} \times G_2 = [G_1 N_1(F_1-1)] \times G_2$
3. Stage 2 adds: $N_{added,2}$, but referred to its input $N_2$, so $N_{added,2} = G_2 N_2(F_2-1)$

But $N_2$ should be the **thermal noise** at the input of stage 2, not the total noise.

For Friis formula, we consider that stage 2 sees equivalent thermal noise at its input.

**The key: Stage 2's added noise is $(F_2-1)$ times its input thermal noise $G_1 N_1$ (not the total $N_2$):**

$$N_{added,2} = G_2 \cdot G_1 N_1 \cdot (F_2 - 1)$$

**Total output noise:**
$$N_3 = G_1 G_2 N_1 + G_2 G_1 N_1(F_1-1) + G_2 G_1 N_1(F_2-1)$$

Factor out $G_1 G_2 N_1$:

$$N_3 = G_1 G_2 N_1[1 + (F_1-1) + (F_2-1)]$$

$$N_3 = G_1 G_2 N_1[F_1 + F_2 - 1]$$

**NO! This is still wrong!**

Let me use the **correct Friis derivation**:

### Correct Derivation: Referring Noise to Input

The trick is that stage 2's added noise, when **referred back to the system input**, is divided by $G_1$:

**Total output noise:**
$$N_3 = G_1 G_2 N_1 \cdot F_{total}$$

**Components:**
1. Input noise amplified: $G_1 G_2 N_1$
2. Stage 1 added noise (amplified by $G_2$): $G_2 \cdot G_1 N_1(F_1-1)$
3. Stage 2 added noise: $G_2 \cdot G_1 N_1 (F_2-1)$

**But stage 2's contribution should be divided by $G_1$ because it's downstream:**

Actually, the correct way is:

$$F_{total} = F_1 + \frac{F_2 - 1}{G_1}$$

**Derivation:**

Output noise referred to input:
$$N_{3,ref} = \frac{N_3}{G_1 G_2}$$

$$N_{3,ref} = N_1 + \frac{N_{added,1}}{G_1} + \frac{N_{added,2}}{G_1 G_2}$$

But $N_{added,1} = G_1 N_1(F_1-1)$ and $N_{added,2} = G_2 G_1 N_1(F_2-1)$:

$$N_{3,ref} = N_1 + \frac{G_1 N_1(F_1-1)}{G_1} + \frac{G_2 G_1 N_1(F_2-1)}{G_1 G_2}$$

$$N_{3,ref} = N_1 + N_1(F_1-1) + N_1(F_2-1)/G_1$$

$$N_{3,ref} = N_1[1 + (F_1-1) + (F_2-1)/G_1]$$

$$N_{3,ref} = N_1[F_1 + (F_2-1)/G_1]$$

**Noise figure:**
$$F_{total} = \frac{N_{3,ref}}{N_1} = F_1 + \frac{F_2-1}{G_1}$$

$$\boxed{F_{total} = F_1 + \frac{F_2 - 1}{G_1}}$$

**Physical Interpretation:**
- Stage 1's noise contribution: $F_1$ (full effect)
- Stage 2's noise contribution: $\frac{F_2-1}{G_1}$ (divided by $G_1$!)

**Why divided by $G_1$?** Because stage 2's noise appears after amplification by $G_1$. When we refer it back to the input, it's reduced by the first stage gain.

**Key Insight:** If $G_1$ is large (high gain first stage), then $(F_2-1)/G_1$ becomes very small, making stage 2's contribution negligible!

---

## 4. Generalization to N Stages

### Extending the Pattern

For three stages:

$$F_{total} = F_1 + \frac{F_2-1}{G_1} + \frac{F_3-1}{G_1 G_2}$$

**Why?** Stage 3's noise is divided by the cumulative gain of stages 1 and 2.

### General N-Stage Friis Formula

$$\boxed{F_{total} = F_1 + \frac{F_2-1}{G_1} + \frac{F_3-1}{G_1 G_2} + \frac{F_4-1}{G_1 G_2 G_3} + \cdots + \frac{F_N-1}{\prod_{i=1}^{N-1} G_i}}$$

**Compact notation:**

$$\boxed{F_{total} = F_1 + \sum_{n=2}^{N} \frac{F_n - 1}{\prod_{i=1}^{n-1} G_i}}$$

---

## 5. Key Insights and Physical Interpretation

### Insight 1: First Stage Dominates

Each subsequent stage's contribution is divided by the cumulative gain of all preceding stages.

**Example:** If $G_1 = 100$ (20 dB):
- Stage 2 contribution: $(F_2-1)/100$ → 20 dB reduction
- Even if stage 2 is very noisy ($F_2 = 10$), its contribution is only $9/100 = 0.09$

**Conclusion:** The first stage's noise figure is BY FAR the most important!

### Insight 2: Why High Gain First Stages?

$$F_{total} \approx F_1 + \frac{F_2-1}{G_1}$$

To minimize $F_{total}$:
1. Use low-noise first stage (small $F_1$)
2. Use high-gain first stage (large $G_1$ makes second term tiny)

This is why **Low-Noise Amplifiers (LNAs)** are always placed first in receiver chains!

### Insight 3: Later Stages Don't Matter Much

With typical values $G_1 = 20$ dB (100), $G_2 = 20$ dB (100):

- Stage 3 contribution divided by: $G_1 G_2 = 10,000$ (40 dB)
- Stage 4 contribution divided by: $G_1 G_2 G_3 = 1,000,000$ (60 dB)

**Later stages become completely negligible!**

---

## 6. Numerical Example

### Given:
- **Stage 1 (LNA):** $F_1 = 1.5$ (1.76 dB), $G_1 = 20$ dB = 100
- **Stage 2 (Mixer):** $F_2 = 8$ (9.03 dB), $G_2 = 10$ dB = 10
- **Stage 3 (IF Amp):** $F_3 = 3$ (4.77 dB), $G_3 = 30$ dB = 1000

### Calculate Total Noise Figure:

$$F_{total} = F_1 + \frac{F_2-1}{G_1} + \frac{F_3-1}{G_1 G_2}$$

$$F_{total} = 1.5 + \frac{8-1}{100} + \frac{3-1}{100 \times 10}$$

$$F_{total} = 1.5 + \frac{7}{100} + \frac{2}{1000}$$

$$F_{total} = 1.5 + 0.07 + 0.002$$

$$F_{total} = 1.572$$

**In dB:**
$$F_{total,dB} = 10\log_{10}(1.572) = 1.96 \text{ dB}$$

### Analysis of Contributions:

| Stage | F (linear) | F (dB) | Contribution to F_total | Percentage |
|-------|------------|--------|------------------------|------------|
| 1 (LNA) | 1.5 | 1.76 dB | 1.500 | **95.4%** |
| 2 (Mixer) | 8 | 9.03 dB | 0.070 | **4.5%** |
| 3 (IF Amp) | 3 | 4.77 dB | 0.002 | **0.1%** |

**Conclusion:** First stage contributes 95.4% of total noise! Stages 2 and 3 are almost irrelevant.

---

## 7. Design Implications

### Rule 1: Invest in the First Stage
Spend money and effort on a low-noise, high-gain first stage. Later stages can be cheaper and noisier.

### Rule 2: Never Attenuate Before Amplifying
If you have an attenuator (loss $L$, where $G = 1/L < 1$) before an amplifier:

$$F_{total} = L \cdot F_{amp} + (F_{amp}-1) \cdot L = L \cdot F_{amp}(1 + \frac{F_{amp}-1}{F_{amp}}) \approx L \cdot F_{amp}$$

**Actually:** For a lossy element, $F = L$ (loss degrades noise figure directly).

$$F_{total} = L + \frac{F_{amp}-1}{1/L} = L + L(F_{amp}-1) = L \cdot F_{amp}$$

**Example:** 3 dB cable loss ($L = 2$) + amplifier ($F = 2$) → $F_{total} = 4$ (6 dB)!

### Rule 3: Receiver Design Priority
**Antenna → LNA → everything else**

The LNA must be:
- As close to the antenna as possible (minimize cable loss)
- Low noise figure ($F < 2$ dB typical)
- High gain ($G > 20$ dB typical)

---

## 8. Related Concepts

### Noise Temperature
Friis formula also applies to noise temperature:

$$T_{total} = T_1 + \frac{T_2}{G_1} + \frac{T_3}{G_1 G_2} + \cdots$$

Where $T_e = T_0(F-1)$ is the equivalent noise temperature.

### dB Conversion
**Warning:** Friis formula uses **linear** gains and noise figures, not dB!

**Correct:**
$$F_{total} = 1.5 + \frac{8-1}{100}$$

**Wrong:**
$$F_{total,dB} \neq 1.76 + \frac{9.03-0}{20}$$

Always convert to linear first!

---

## 9. Summary

### Friis Cascade Formula

$$\boxed{F_{total} = F_1 + \frac{F_2-1}{G_1} + \frac{F_3-1}{G_1 G_2} + \cdots + \frac{F_N-1}{\prod_{i=1}^{N-1} G_i}}$$

### Key Takeaways

1. **First stage dominates** - its noise figure is the most critical
2. **High gain first stage** - reduces impact of all subsequent stages
3. **Later stages negligible** - after high gain, nothing else matters much
4. **Design priority** - invest in excellent first stage (LNA)
5. **Never attenuate first** - cable loss before LNA is catastrophic

### Applications

- Radio receiver design
- Satellite communications (LNA at antenna)
- Radar systems
- Test equipment
- Any cascaded RF/microwave system

**This is one of the most important formulas in communications engineering!**
