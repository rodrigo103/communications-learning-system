# Friis Cascade Noise Figure Formula - Derivation from First Principles

**Date:** November 15, 2025
**Topic:** Noise Figure Analysis in Cascaded Systems
**Level:** Advanced Communications Systems

---

## 1. Noise Figure Definition (SNR Approach)

### 1.1 Fundamental Definition

The **noise figure** (F) quantifies how much a component degrades the signal-to-noise ratio:

$$F = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}}$$

Where:
- $\text{SNR}_{\text{in}}$ = Input signal-to-noise ratio
- $\text{SNR}_{\text{out}}$ = Output signal-to-noise ratio

**Key Insight:** An ideal (noiseless) component has $F = 1$ (0 dB), meaning it preserves the SNR. Real components have $F > 1$, degrading the SNR.

### 1.2 Alternative Form Using Power

Since $\text{SNR} = \frac{P_{\text{signal}}}{P_{\text{noise}}}$, we can write:

$$F = \frac{P_{S,\text{in}}/P_{N,\text{in}}}{P_{S,\text{out}}/P_{N,\text{out}}} = \frac{P_{S,\text{in}} \cdot P_{N,\text{out}}}{P_{N,\text{in}} \cdot P_{S,\text{out}}}$$

For an amplifier with gain $G$:
- $P_{S,\text{out}} = G \cdot P_{S,\text{in}}$

Therefore:

$$F = \frac{P_{S,\text{in}} \cdot P_{N,\text{out}}}{P_{N,\text{in}} \cdot G \cdot P_{S,\text{in}}} = \frac{P_{N,\text{out}}}{G \cdot P_{N,\text{in}}}$$

### 1.3 Noise Figure in Terms of Added Noise

The output noise consists of:
1. **Amplified input noise:** $G \cdot P_{N,\text{in}}$
2. **Internally added noise:** $P_{N,\text{added}}$

Thus:
$$P_{N,\text{out}} = G \cdot P_{N,\text{in}} + P_{N,\text{added}}$$

Substituting into the noise figure formula:

$$F = \frac{G \cdot P_{N,\text{in}} + P_{N,\text{added}}}{G \cdot P_{N,\text{in}}} = 1 + \frac{P_{N,\text{added}}}{G \cdot P_{N,\text{in}}}$$

**Standard Reference:** Typically, $P_{N,\text{in}} = kT_0B$ where:
- $k = 1.38 \times 10^{-23}$ J/K (Boltzmann's constant)
- $T_0 = 290$ K (reference temperature)
- $B$ = bandwidth

---

## 2. Single Amplifier Analysis

### 2.1 Amplifier Noise Model

Consider an amplifier with:
- **Gain:** $G$
- **Noise Figure:** $F$
- **Input noise power:** $N_{\text{in}} = kT_0B$

The amplifier adds noise power:

$$N_{\text{added}} = (F - 1) \cdot G \cdot kT_0B$$

**Output noise power:**

$$N_{\text{out}} = G \cdot N_{\text{in}} + N_{\text{added}} = G \cdot kT_0B + (F-1) \cdot G \cdot kT_0B$$

$$N_{\text{out}} = F \cdot G \cdot kT_0B$$

### 2.2 Verification

Check the noise figure:

$$F = \frac{N_{\text{out}}}{G \cdot N_{\text{in}}} = \frac{F \cdot G \cdot kT_0B}{G \cdot kT_0B} = F \quad \checkmark$$

### 2.3 Key Insight for Cascade Analysis

The noise added by an amplifier, **referred to its input**, is:

$$N_{\text{added, input-referred}} = \frac{N_{\text{added}}}{G} = (F-1) \cdot kT_0B$$

This concept is crucial for cascade analysis.

---

## 3. Two-Stage Cascade Derivation (Detailed Steps)

### 3.1 System Configuration

Consider two amplifiers in cascade:
- **Stage 1:** Gain $G_1$, Noise Figure $F_1$
- **Stage 2:** Gain $G_2$, Noise Figure $F_2$

```
Input → [Stage 1: G₁, F₁] → [Stage 2: G₂, F₂] → Output
```

**Overall gain:** $G_{\text{total}} = G_1 \cdot G_2$

### 3.2 Noise Analysis - Step by Step

**Input to Stage 1:**
- Signal power: $S_{\text{in}}$
- Noise power: $N_{\text{in}} = kT_0B$

**Output of Stage 1 (= Input to Stage 2):**
- Signal power: $S_1 = G_1 \cdot S_{\text{in}}$
- Noise power: $N_1 = F_1 \cdot G_1 \cdot kT_0B$

Breaking down $N_1$:
$$N_1 = G_1 \cdot kT_0B + (F_1 - 1) \cdot G_1 \cdot kT_0B$$
- First term: amplified input noise
- Second term: noise added by Stage 1

**Stage 2 operates on its input:**

Stage 2 amplifies everything at its input and adds its own noise:
- **Amplified signal:** $S_{\text{out}} = G_2 \cdot S_1 = G_2 \cdot G_1 \cdot S_{\text{in}}$
- **Amplified noise from Stage 1:** $G_2 \cdot N_1 = G_2 \cdot F_1 \cdot G_1 \cdot kT_0B$
- **Noise added by Stage 2:** $(F_2 - 1) \cdot G_2 \cdot N_{\text{in,stage2}}$

**Critical Point:** What is the "input noise" for Stage 2?

The noise figure $F_2$ is defined with respect to the **reference noise** $kT_0B$, not the actual noise entering Stage 2. Therefore:

$$N_{\text{added,2}} = (F_2 - 1) \cdot G_2 \cdot kT_0B$$

**Total output noise:**

$$N_{\text{out}} = G_2 \cdot N_1 + N_{\text{added,2}}$$

$$N_{\text{out}} = G_2 \cdot F_1 \cdot G_1 \cdot kT_0B + (F_2 - 1) \cdot G_2 \cdot kT_0B$$

Factor out $G_2 \cdot kT_0B$:

$$N_{\text{out}} = G_2 \cdot kT_0B \left[ F_1 \cdot G_1 + (F_2 - 1) \right]$$

$$N_{\text{out}} = G_1 \cdot G_2 \cdot kT_0B \left[ F_1 + \frac{F_2 - 1}{G_1} \right]$$

### 3.3 Overall Noise Figure Calculation

The overall noise figure is:

$$F_{\text{total}} = \frac{N_{\text{out}}}{G_{\text{total}} \cdot N_{\text{in}}} = \frac{G_1 \cdot G_2 \cdot kT_0B \left[ F_1 + \frac{F_2 - 1}{G_1} \right]}{G_1 \cdot G_2 \cdot kT_0B}$$

**Simplify:**

$$\boxed{F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1}}$$

This is the **Friis formula for two stages**.

### 3.4 Physical Interpretation

The formula reveals:
1. **$F_1$** - First stage noise figure appears directly (not reduced)
2. **$\frac{F_2 - 1}{G_1}$** - Second stage contribution is reduced by the gain of the first stage

**Key Insight:** High gain in the first stage ($G_1 \gg 1$) makes the second stage contribution negligible!

---

## 4. General N-Stage Cascade Formula

### 4.1 Three-Stage Extension

For three stages, we treat the first two as a single block with noise figure $F_{12} = F_1 + \frac{F_2-1}{G_1}$, then cascade with stage 3:

$$F_{123} = F_{12} + \frac{F_3 - 1}{G_{12}}$$

where $G_{12} = G_1 \cdot G_2$

**Expanding:**

$$F_{123} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 \cdot G_2}$$

### 4.2 General N-Stage Formula

For $N$ stages in cascade, each with gain $G_i$ and noise figure $F_i$:

$$\boxed{F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \frac{F_4 - 1}{G_1 G_2 G_3} + \cdots + \frac{F_N - 1}{\prod_{i=1}^{N-1} G_i}}$$

**Compact notation:**

$$F_{\text{total}} = F_1 + \sum_{i=2}^{N} \frac{F_i - 1}{\prod_{j=1}^{i-1} G_j}$$

### 4.3 Mathematical Derivation by Induction

**Base case:** Single stage, $F_{\text{total}} = F_1$ ✓

**Inductive step:** Assume formula holds for $n$ stages. For $n+1$ stages:

$$F_{n+1} = F_n + \frac{F_{n+1} - 1}{\prod_{j=1}^{n} G_j}$$

where $F_n = F_1 + \sum_{i=2}^{n} \frac{F_i - 1}{\prod_{j=1}^{i-1} G_j}$

Substituting:

$$F_{n+1} = F_1 + \sum_{i=2}^{n} \frac{F_i - 1}{\prod_{j=1}^{i-1} G_j} + \frac{F_{n+1} - 1}{\prod_{j=1}^{n} G_j}$$

$$F_{n+1} = F_1 + \sum_{i=2}^{n+1} \frac{F_i - 1}{\prod_{j=1}^{i-1} G_j} \quad \text{QED}$$

---

## 5. Physical Interpretation - Why First Stage Dominates

### 5.1 Successive Reduction

Each term in the Friis formula is reduced by the cumulative gain of preceding stages:

$$F_{\text{total}} = \underbrace{F_1}_{\text{full impact}} + \underbrace{\frac{F_2-1}{G_1}}_{\text{reduced by } G_1} + \underbrace{\frac{F_3-1}{G_1 G_2}}_{\text{reduced by } G_1 G_2} + \cdots$$

**Example with typical values:**
- $F_1 = 2$ (3 dB), $F_2 = 4$ (6 dB), $F_3 = 4$ (6 dB)
- $G_1 = 100$ (20 dB), $G_2 = 100$ (20 dB)

$$F_{\text{total}} = 2 + \frac{4-1}{100} + \frac{4-1}{100 \times 100}$$

$$F_{\text{total}} = 2 + 0.03 + 0.0003 = 2.0303$$

**Contribution analysis:**
- Stage 1: 98.5% of total noise figure
- Stage 2: 1.48%
- Stage 3: 0.015%

### 5.2 Physical Reasoning

**Why does this happen?**

1. **Signal Amplification:** The first stage amplifies the signal by $G_1$
2. **Noise Addition:** Each stage adds noise proportional to $kT_0B$
3. **Relative Impact:** Noise added by later stages, when referred back to the input, is divided by the large cumulative gain

**Analogy:** Imagine shouting in a noisy room:
- Stage 1: Your voice (signal) and room noise are both picked up
- If Stage 1 amplifies strongly, your voice is now much louder than any new noise added by Stage 2
- Stage 2's noise is relatively insignificant compared to the already-amplified signal

### 5.3 Mathematical Threshold

When is a stage's contribution negligible?

$$\frac{F_i - 1}{\prod_{j=1}^{i-1} G_j} \ll F_1$$

**Rule of thumb:** If the cumulative gain before stage $i$ satisfies:

$$\prod_{j=1}^{i-1} G_j > 10(F_i - 1)$$

then stage $i$ contributes less than 10% to the total noise figure.

For $F_i \approx 3$ (typical), we need:
$$\prod_{j=1}^{i-1} G_j > 20 \quad (13 \text{ dB})$$

**Design Implication:** A first stage with 15-20 dB gain effectively isolates the system from subsequent stage noise.

---

## 6. Numerical Example - Three-Stage Receiver

### 6.1 Problem Setup

Design a receiver front-end with three stages:

| Stage | Component | Gain (dB) | Gain (Linear) | Noise Figure (dB) | Noise Figure (Linear) |
|-------|-----------|-----------|---------------|-------------------|-----------------------|
| 1 | LNA | 20 dB | 100 | 1.5 dB | 1.41 |
| 2 | Mixer | -6 dB | 0.25 | 8 dB | 6.31 |
| 3 | IF Amp | 30 dB | 1000 | 3 dB | 2.00 |

**Note:** Mixers typically have conversion *loss* (gain < 1)

### 6.2 Cascade Calculation

Apply Friis formula:

$$F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2}$$

**Substitute values:**

$$F_{\text{total}} = 1.41 + \frac{6.31 - 1}{100} + \frac{2.00 - 1}{100 \times 0.25}$$

$$F_{\text{total}} = 1.41 + \frac{5.31}{100} + \frac{1.00}{25}$$

$$F_{\text{total}} = 1.41 + 0.0531 + 0.04$$

$$F_{\text{total}} = 1.5031 \text{ (linear)}$$

**Convert to dB:**

$$F_{\text{total}} = 10 \log_{10}(1.5031) = 1.77 \text{ dB}$$

### 6.3 Contribution Analysis

Calculate each stage's contribution:

| Stage | Term | Value (Linear) | Contribution |
|-------|------|----------------|--------------|
| 1 | $F_1$ | 1.4100 | 93.8% |
| 2 | $\frac{F_2-1}{G_1}$ | 0.0531 | 3.5% |
| 3 | $\frac{F_3-1}{G_1 G_2}$ | 0.0400 | 2.7% |
| **Total** | | **1.5031** | **100%** |

**Key Observations:**

1. **LNA dominates:** Despite the mixer having poor noise figure (8 dB), its contribution is only 3.5%
2. **High gain mitigates poor stages:** The 20 dB LNA gain reduces the mixer's impact by 20 dB
3. **Final amplifier negligible:** Third stage contributes < 3% despite 3 dB noise figure

### 6.4 Design Comparison - Poor LNA

What if we used a cheaper LNA with higher noise figure?

**Scenario:** LNA with 3 dB noise figure, same gain

$$F_{\text{total}} = 2.00 + \frac{5.31}{100} + \frac{1.00}{25}$$

$$F_{\text{total}} = 2.00 + 0.0531 + 0.04 = 2.093 \text{ (linear)} = 3.21 \text{ dB}$$

**Degradation:** System noise figure increased by $3.21 - 1.77 = 1.44$ dB

**Sensitivity loss:** Receiver sensitivity degrades by 1.44 dB (≈28% reduction in range for a radar)

### 6.5 Impact of Reduced LNA Gain

**Scenario:** Original LNA (1.5 dB NF) but only 10 dB gain

$$G_1 = 10 \text{ (linear)}$$

$$F_{\text{total}} = 1.41 + \frac{5.31}{10} + \frac{1.00}{10 \times 0.25}$$

$$F_{\text{total}} = 1.41 + 0.531 + 0.4 = 2.341 \text{ (linear)} = 3.69 \text{ dB}$$

**Result:** Even with excellent LNA noise figure, insufficient gain (10 dB) allows the mixer's poor noise figure to dominate.

**Lesson:** Both low noise figure AND high gain are needed in the first stage!

---

## 7. Design Implications for Receiver Systems

### 7.1 First Stage (LNA) Requirements

The Friis formula dictates that the Low-Noise Amplifier (LNA) is the most critical component:

**Primary Requirements:**
1. **Minimum Noise Figure:** Typically 0.5-2 dB for sensitive receivers
2. **Sufficient Gain:** 15-25 dB to suppress following stage noise
3. **Impedance Matching:** Critical for noise figure (affects $F_1$)
4. **Linearity:** Must not create distortion (separate from noise considerations)

**Technology Choices:**
- **High-frequency:** GaAs or GaN HEMTs (Low noise, high frequency capability)
- **Lower frequency:** SiGe HBTs or CMOS LNAs (Integration, cost)
- **Cryogenic systems:** Cooled amplifiers (F approaching 0 dB)

### 7.2 System-Level Trade-offs

**Trade-off 1: Cost vs. Performance**
- Premium LNA: $50-200, enables cheaper subsequent stages
- Poor LNA: Requires expensive low-noise mixer and filters

**Trade-off 2: Power Consumption**
- High-gain LNA: Higher DC power, but allows lower-power IF stages
- Overall system power may actually decrease with better LNA

**Trade-off 3: Bandwidth**
- Wideband LNAs: Higher noise figure (more bandwidth = more thermal noise)
- Narrowband: Better noise figure, but limited application

### 7.3 Practical Design Guidelines

#### Guideline 1: The "20 dB Rule"

**Statement:** First stage gain should be ≥20 dB to make system noise figure ≈ LNA noise figure

**Proof:**
If $G_1 = 100$ (20 dB) and $F_2 = 6$ (typical mixer):

$$\frac{F_2-1}{G_1} = \frac{5}{100} = 0.05$$

This adds only 0.22 dB to the system noise figure.

#### Guideline 2: Mixer Placement

**Before or after LNA?**

**Option A:** Antenna → Mixer → LNA
$$F_{\text{total}} = F_{\text{mixer}} + \frac{F_{\text{LNA}}-1}{G_{\text{mixer}}}$$

With $F_{\text{mixer}} = 6$, $G_{\text{mixer}} = 0.25$:
$$F_{\text{total}} = 6 + \frac{1.41-1}{0.25} = 6 + 1.64 = 7.64 \text{ (8.8 dB)} \quad \text{BAD!}$$

**Option B:** Antenna → LNA → Mixer
$$F_{\text{total}} = 1.41 + \frac{6-1}{100} = 1.46 \text{ (1.6 dB)} \quad \text{GOOD!}$$

**Conclusion:** ALWAYS place LNA first!

#### Guideline 3: Filter Insertion Loss

Band-pass filters have insertion loss (effective gain < 1), degrading noise figure:

**Filter as first stage:**
$$F_{\text{filter}} = \frac{1}{G_{\text{filter}}} = L_{\text{insertion}}$$

Example: 1 dB insertion loss → 1 dB noise figure

**Impact on system:**
If filter precedes LNA:
$$F_{\text{total}} = L_{\text{filter}} + \frac{F_{\text{LNA}}-1}{G_{\text{filter}}}$$

With $L = 1.26$ (1 dB), $F_{\text{LNA}} = 1.41$:
$$F_{\text{total}} = 1.26 + \frac{0.41}{0.79} = 1.26 + 0.52 = 1.78 \text{ (2.5 dB)}$$

**Design Choice:**
- **If filter needed:** Place after LNA when possible (image rejection often requires pre-LNA filtering)
- **Minimize loss:** Use high-Q filters, superconducting filters for extreme applications

### 7.4 Advanced Techniques

#### Technique 1: Cryogenic Cooling

For radio astronomy and deep-space communications:
- Cool LNA to 20 K using cryogenic refrigerators
- Noise figure: 0.1-0.3 dB (factors of 10 improvement)
- **Cost:** $10,000-100,000 for cooling system
- **Application:** Very Large Array (VLA), Deep Space Network (DSN)

#### Technique 2: Balanced Amplifiers

Use quadrature hybrids with two LNAs:
- Advantage: Improved input match, reduced reflections
- Noise figure: Essentially same as single LNA (both contribute equally)
- Gain: 3 dB less than single LNA (power split)

#### Technique 3: Distributed Amplification

For ultra-wideband applications:
- Multiple gain stages with transmission-line interconnects
- Achieves decade+ bandwidth with moderate noise figure
- Example: 2-20 GHz with 4 dB noise figure

### 7.5 Real-World Example: GPS Receiver

**GPS L1 Band (1.575 GHz) Receiver Front-End:**

| Component | Gain | Noise Figure |
|-----------|------|--------------|
| Antenna + Cable | -1 dB | 1 dB |
| SAW Filter | -2 dB | 2 dB |
| LNA | 15 dB | 0.8 dB |
| Image-Reject Mixer | -8 dB | 8 dB |
| IF Amplifier | 20 dB | 3 dB |

**Calculate system noise figure:**

$$F_{\text{total}} = L_{\text{cable}} + \frac{L_{\text{filter}}-1}{G_{\text{cable}}} + \frac{F_{\text{LNA}}-1}{G_{\text{cable}} G_{\text{filter}}} + \cdots$$

**Simplified calculation (stages 1-4):**

$$F_{\text{total}} = 1.26 + \frac{0.58}{0.79} + \frac{0.2}{0.79 \times 0.63} + \frac{7}{0.79 \times 0.63 \times 31.6}$$

$$F_{\text{total}} = 1.26 + 0.73 + 0.40 + 0.44 = 2.83 \text{ (4.5 dB)}$$

**Observations:**
1. Antenna system and filter dominate (2 dB combined)
2. Excellent LNA is "wasted" due to preceding losses
3. Typical GPS receiver: 4-5 dB system noise figure

**Improvement Strategy:**
- Use active antenna (LNA at antenna, before cable)
- Reduces system NF to ≈1.5 dB (typical commercial GPS active antenna)

---

## 8. Related Concepts - Noise Temperature

### 8.1 Noise Temperature Definition

An alternative to noise figure is **noise temperature** ($T_e$):

$$T_e = (F - 1) \cdot T_0$$

where $T_0 = 290$ K (reference temperature)

**Relationship:**
$$F = 1 + \frac{T_e}{T_0}$$

**Why use temperature?**
- More intuitive for cryogenic systems
- Additive for cascaded stages (in certain formulations)
- Standard in radio astronomy

### 8.2 Cascade Formula in Terms of Temperature

For two stages:

$$F_{\text{total}} = F_1 + \frac{F_2-1}{G_1}$$

Converting to temperature:

$$1 + \frac{T_{e,\text{total}}}{T_0} = 1 + \frac{T_{e,1}}{T_0} + \frac{T_{e,2}}{G_1 T_0}$$

**Simplifies to:**

$$\boxed{T_{e,\text{total}} = T_{e,1} + \frac{T_{e,2}}{G_1}}$$

**N-stage formula:**

$$T_{e,\text{total}} = T_{e,1} + \frac{T_{e,2}}{G_1} + \frac{T_{e,3}}{G_1 G_2} + \cdots$$

### 8.3 Numerical Example

Convert our 3-stage example to noise temperatures:

| Stage | $F$ | $T_e = (F-1) \times 290$ K |
|-------|-----|----------------------------|
| LNA | 1.41 | 119 K |
| Mixer | 6.31 | 1540 K |
| IF Amp | 2.00 | 290 K |

**System noise temperature:**

$$T_{e,\text{sys}} = 119 + \frac{1540}{100} + \frac{290}{100 \times 0.25}$$

$$T_{e,\text{sys}} = 119 + 15.4 + 11.6 = 146 \text{ K}$$

**Verify:**
$$F_{\text{sys}} = 1 + \frac{146}{290} = 1.503 \quad \checkmark$$

### 8.4 Cryogenic System Example

**Radio telescope LNA at 20 K physical temperature:**
- LNA noise temperature: $T_{e,1} = 5$ K (excellent!)
- Mixer at 290 K: $T_{e,2} = 1500$ K
- LNA gain: $G_1 = 40$ dB = 10,000

$$T_{e,\text{sys}} = 5 + \frac{1500}{10000} = 5.15 \text{ K}$$

**Noise figure:**
$$F_{\text{sys}} = 1 + \frac{5.15}{290} = 1.018 \text{ (0.08 dB)}$$

**Contrast with room-temperature LNA:**
If $T_{e,1} = 100$ K (room-temp LNA):
$$T_{e,\text{sys}} = 100 + 0.15 = 100.15 \text{ K} \quad (F = 1.35, \text{ 1.3 dB})$$

Cooling provides **16× improvement** in noise temperature!

---

## 9. Summary and Key Formulas

### 9.1 Friis Cascade Noise Figure Formula

**Two-stage:**
$$\boxed{F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1}}$$

**N-stage:**
$$\boxed{F_{\text{total}} = F_1 + \sum_{i=2}^{N} \frac{F_i - 1}{\prod_{j=1}^{i-1} G_j}}$$

**Equivalent (expanded):**
$$F_{\text{total}} = F_1 + \frac{F_2-1}{G_1} + \frac{F_3-1}{G_1 G_2} + \frac{F_4-1}{G_1 G_2 G_3} + \cdots$$

### 9.2 Noise Temperature Form

$$\boxed{T_{e,\text{total}} = T_{e,1} + \frac{T_{e,2}}{G_1} + \frac{T_{e,3}}{G_1 G_2} + \cdots}$$

### 9.3 Key Insights

1. **First stage dominates:** The noise figure of the first stage appears directly and undiminished
2. **Gain suppresses later stages:** Each subsequent stage's contribution is reduced by the cumulative gain of all preceding stages
3. **Design implication:** Invest in an excellent first stage (low $F_1$, high $G_1$)
4. **20 dB rule:** First stage gain ≥20 dB makes subsequent stages nearly irrelevant
5. **Losses hurt:** Any loss before the LNA (cables, filters) directly adds to system noise figure

### 9.4 Design Principles

✓ **Maximize first-stage gain** (15-25 dB typical)
✓ **Minimize first-stage noise figure** (state-of-art: 0.3-1.5 dB)
✓ **Minimize losses before LNA** (use short, low-loss cables)
✓ **Place LNA as close to antenna as possible**
✓ **Later stages can have higher noise figure** (save cost/power)
✗ **Never place lossy component before LNA** (if avoidable)
✗ **Don't skimp on LNA to save cost** (system penalty is severe)

---

## 10. Historical Note

The Friis formula is named after **Harald T. Friis** (1893-1976), a Danish-American radio engineer who worked at Bell Labs. He published this formula in 1944 in the paper:

> Friis, H. T. (1944). "Noise figures of radio receivers." *Proceedings of the IRE*, 32(7), 419-422.

This work laid the foundation for modern receiver design and remains one of the most important results in communications engineering.

Friis also developed the Friis transmission equation for antenna link budgets, making him doubly influential in RF engineering!

---

## 11. Further Reading

1. **Textbooks:**
   - Pozar, D. M. *Microwave Engineering* (Chapter 10: Noise)
   - Razavi, B. *RF Microelectronics* (Chapter 2: Receiver Architectures)
   - Richards, M. A. *Fundamentals of Radar Signal Processing* (Appendix: Noise Analysis)

2. **Application Notes:**
   - Agilent AN 57-1: "Fundamentals of RF and Microwave Noise Figure Measurements"
   - Analog Devices MT-010: "The Importance of Noise Figure in Receivers"

3. **Standards:**
   - IEEE Standard 1139-2008: "Standard Definitions of Physical Quantities for Fundamental Frequency and Time Metrology"

---

**End of Derivation**

*Generated for Communications Systems Learning - November 15, 2025*
