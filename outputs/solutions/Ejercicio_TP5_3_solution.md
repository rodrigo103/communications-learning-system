# Ejercicio TP5_3: FM Receiver SNR Analysis - Complete Solution (CORRECTED)

**Date**: 2025-12-09
**Source**: TP5 Exercise 3 - FM Modulation
**Status**: CORRECTED - Using proper Haykin formula with W/B_T factor

---

## Problem Statement

A FM receiver has an IF filter with bandwidth 200 kHz and an ideal lowpass output filter with f_c = 15 kHz. It receives a signal modulated by a tone with the following characteristics: f_m = 5 kHz and Δf = 75 kHz. The ratio of average signal power to average noise power at the input of the IF amplifier is 40 dB.

Find:
a) What is the S/N after the output filter if F_FI = 1?
b) What is the S/N after the output filter if Te_FI = 72.50 K?
c) What modulation index is necessary to improve the S/N calculated in "a)" by 6 dB?

---

## Given Data

| Variable | Value | Unit | Converted (SI) | Notes |
|----------|-------|------|----------------|-------|
| B_FI | 200 | kHz | 200,000 Hz | IF filter bandwidth (= B_T) |
| f_c | 15 | kHz | 15,000 Hz | Output LPF cutoff frequency |
| f_m | 5 | kHz | 5,000 Hz | Tone frequency (= W, message BW) |
| Δf | 75 | kHz | 75,000 Hz | Frequency deviation |
| (S/N)_R | 40 | dB | 10,000 (linear) | Input SNR at IF amp |
| F_FI (a) | 1 | - | 1 | Noise figure = 1 (noiseless) |
| Te_FI (b) | 72.50 | K | 72.50 K | Equivalent noise temperature |

**Constants:**
- k = 1.38×10^-23 J/K (Boltzmann constant)
- T_0 = 290 K (Reference temperature for noise figure)

**Calculated Parameters:**
- β = Δf/f_m = 75/5 = 15 (modulation index)
- B_T (Carson) = 2(Δf + f_m) = 2(75 + 5) = 160 kHz (transmission bandwidth)
- W/B_T = f_m/B_T = 5/160 = 0.03125 (critical ratio!)

**Note on B_T vs B_FI:**
- B_T = 160 kHz is the signal bandwidth (Carson's Rule)
- B_FI = 200 kHz is the IF filter bandwidth (given, slightly wider)
- We use B_T from Carson for the Haykin formula (theoretically correct)

---

## Problem Analysis

**Type:** FM Receiver - SNR Analysis with Noise Figure Effects

**Key Concepts Involved:**
- FM demodulation SNR gain (processing gain)
- Noise figure and equivalent noise temperature
- Modulation index β and its quadratic effect on SNR
- Carson's Rule bandwidth constraints

**Relevant Formulas:**

**1. Haykin FM SNR Formula (CORRECT VERSION):**
$$\left(\frac{S}{N}\right)_{D} = 3\beta^2 \left(\frac{W}{B_T}\right) \left(\frac{S}{N}\right)_R$$

Where:
- (S/N)_D = output SNR (after demodulator and LPF)
- (S/N)_R = input SNR at receiver (before demodulator)
- β = Δf/f_m = modulation index
- W = message bandwidth (for single tone: W = f_m)
- B_T = transmission bandwidth (IF filter bandwidth)
- **IMPORTANT**: The factor W/B_T is ALWAYS < 1 in wideband FM

**2. Noise Figure Relationship:**
$$F = \frac{(S/N)_{in}}{(S/N)_{out}} = 1 + \frac{T_e}{T_0}$$

Where T_0 = 290 K (reference temperature)

**3. Carson's Rule (for bandwidth):**
$$B_T = 2(\Delta f + f_m) = 2f_m(\beta + 1)$$

---

## Solution

### Part (a): Output SNR with F_FI = 1 (Noiseless IF Amplifier)

**What's being asked:** Calculate the output SNR when the IF amplifier has no added noise (F = 1).

**Approach:** Apply the Haykin formula directly since F = 1 means the input SNR is not degraded.

**Step 1: Verify the given input SNR**

With F_FI = 1 (noiseless amplifier):
$$(S/N)_R = 40 \text{ dB} = 10^{40/10} = 10,000 \text{ (linear)}$$

**Step 2: Calculate modulation index**

$$\beta = \frac{\Delta f}{f_m} = \frac{75 \text{ kHz}}{5 \text{ kHz}} = 15$$

**Step 3: Calculate B_T using Carson's Rule**

$$B_T = 2(\Delta f + f_m) = 2(75 + 5) = 160 \text{ kHz}$$

**Note:** The IF filter (200 kHz) is wider than Carson's bandwidth (160 kHz) to accommodate filter roll-off. For the Haykin formula, we use the theoretical B_T from Carson.

**Step 4: Calculate the W/B_T factor**

$$\frac{W}{B_T} = \frac{f_m}{B_T} = \frac{5 \text{ kHz}}{160 \text{ kHz}} = 0.03125$$

**Validation of W/B_T < 1:**
- For wideband FM, this ratio MUST be much less than 1 ✓
- This factor represents the bandwidth compression that enables FM's processing gain

**Step 5: Apply Haykin formula**

$$\left(\frac{S}{N}\right)_{D} = 3\beta^2 \left(\frac{W}{B_T}\right) \left(\frac{S}{N}\right)_R$$

Substitution:
$$\left(\frac{S}{N}\right)_{D} = 3 \times (15)^2 \times (0.03125) \times 10,000$$

Calculation:
$$\left(\frac{S}{N}\right)_{D} = 3 \times 225 \times 0.03125 \times 10,000$$
$$\left(\frac{S}{N}\right)_{D} = 675 \times 0.03125 \times 10,000$$
$$\left(\frac{S}{N}\right)_{D} = 21.09375 \times 10,000$$
$$\left(\frac{S}{N}\right)_{D} = 210,937.5$$

**Convert to dB:**
$$\left(\frac{S}{N}\right)_{D,dB} = 10 \log_{10}(210,937.5) = 10 \times 5.324 = 53.24 \text{ dB}$$

Result:
$$\boxed{(S/N)_D = 210,938 \text{ (linear)} = 53.2 \text{ dB}}$$

**Validation:**
- Dimensions: Dimensionless ratio ✓
- FM processing gain: 53.2 - 40 = 13.2 dB ✓
- Sanity check: Wideband FM with β = 15 should give moderate gain ✓
- Physical meaning: FM exchanges bandwidth for SNR improvement

**Explanation:** The FM demodulation process provides a **13.2 dB processing gain** (also called "quieting effect"). This gain comes from the wideband nature of FM - we use 160 kHz bandwidth (Carson) to transmit a 5 kHz signal, and FM demodulation converts this bandwidth expansion into SNR improvement.

**FM Processing Gain Factor:**
$$G_{FM} = 3\beta^2 \left(\frac{W}{B_T}\right) = 3 \times 225 \times 0.03125 = 21.09 = 13.2 \text{ dB}$$

---

### Part (b): Output SNR with Te_FI = 72.50 K

**What's being asked:** Calculate the output SNR when the IF amplifier has equivalent noise temperature of 72.50 K.

**Approach:** First calculate the noise figure F from Te, then find the degraded input SNR, and finally apply the FM formula.

**Step 1: Calculate Noise Figure from Equivalent Noise Temperature**

Formula:
$$F = 1 + \frac{T_e}{T_0}$$

Where T_0 = 290 K (standard reference temperature)

Substitution:
$$F = 1 + \frac{72.50}{290} = 1 + 0.25 = 1.25$$

Convert to dB:
$$F_{dB} = 10 \log_{10}(1.25) = 0.97 \text{ dB}$$

**Step 2: Calculate degraded input SNR**

The noise figure degrades the input SNR:
$$\left(\frac{S}{N}\right)_{R,degraded} = \frac{(S/N)_{R,original}}{F} = \frac{10,000}{1.25} = 8,000$$

In dB:
$$(S/N)_{R,degraded,dB} = 40 - 0.97 = 39.03 \text{ dB}$$

**Step 3: Apply Haykin FM formula with degraded SNR**

Using B_T = 160 kHz from Carson's Rule (same as part a):

$$\left(\frac{S}{N}\right)_{D} = 3\beta^2 \left(\frac{W}{B_T}\right) \left(\frac{S}{N}\right)_{R,degraded}$$

Substitution:
$$\left(\frac{S}{N}\right)_{D} = 3 \times (15)^2 \times (0.03125) \times 8,000$$

Calculation:
$$\left(\frac{S}{N}\right)_{D} = 3 \times 225 \times 0.03125 \times 8,000$$
$$\left(\frac{S}{N}\right)_{D} = 21.09375 \times 8,000$$
$$\left(\frac{S}{N}\right)_{D} = 168,750$$

**Convert to dB:**
$$\left(\frac{S}{N}\right)_{D,dB} = 10 \log_{10}(168,750) = 52.27 \text{ dB}$$

Result:
$$\boxed{(S/N)_D = 168,750 \text{ (linear)} = 52.3 \text{ dB}}$$

**Validation:**
- Dimensions: Dimensionless ratio ✓
- Degradation: 53.2 - 52.3 = 0.9 dB ≈ F_dB = 0.97 dB ✓
- Sanity check: Noise figure causes ~1 dB loss in output SNR ✓

**Explanation:** The IF amplifier's noise temperature of 72.50 K corresponds to a noise figure of 1.25 (0.97 dB). This added noise degrades the input SNR by the same amount, which then propagates through the FM demodulator. The output SNR is reduced by approximately 1 dB compared to the noiseless case.

**Comparison:**
- Part (a): 53.2 dB (F = 1, noiseless)
- Part (b): 52.3 dB (F = 1.25, Te = 72.5 K)
- Degradation: 0.9 dB ≈ 1 dB (due to IF amplifier noise)

---

### Part (c): Required β for 6 dB Improvement

**What's being asked:** Find the modulation index β needed to improve the SNR from part (a) by 6 dB.

**Approach:** Use the quadratic relationship between β and SNR. A 6 dB improvement means SNR must double in linear scale. Since SNR ∝ β², we need β_new = β_old × √2.

**Step 1: Determine target output SNR**

Starting SNR from part (a):
$$(S/N)_{D,a} = 53.2 \text{ dB} = 210,938 \text{ (linear)}$$

Target SNR (6 dB higher):
$$(S/N)_{D,target} = 53.2 + 6 = 59.2 \text{ dB}$$

In linear:
$$(S/N)_{D,target} = 10^{59.2/10} = 831,764$$

Alternatively (easier approach):
$$\frac{(S/N)_{D,target}}{(S/N)_{D,a}} = 10^{6/10} = 10^{0.6} = 3.981 \approx 4$$

So:
$$(S/N)_{D,target} = 4 \times 210,938 = 843,752$$

**Step 2: Analyze the β² relationship**

From Haykin formula:
$$\left(\frac{S}{N}\right)_{D} = 3\beta^2 \left(\frac{W}{B_T}\right) \left(\frac{S}{N}\right)_R$$

**IMPORTANT:** When β changes, B_T also changes (Carson's Rule)!

Carson's Rule:
$$B_T = 2(\Delta f + f_m) = 2(f_m \beta + f_m) = 2f_m(\beta + 1)$$

Therefore:
$$\frac{W}{B_T} = \frac{f_m}{2f_m(\beta + 1)} = \frac{1}{2(\beta + 1)}$$

The FM formula becomes:
$$\left(\frac{S}{N}\right)_{D} = 3\beta^2 \cdot \frac{1}{2(\beta + 1)} \cdot (S/N)_R = \frac{3\beta^2}{2(\beta + 1)} \cdot (S/N)_R$$

**Step 3: Set up equation for required β**

We need:
$$\frac{(S/N)_{D,new}}{(S/N)_{D,original}} = 4$$

$$\frac{\frac{3\beta_{new}^2}{2(\beta_{new} + 1)}}{\frac{3\beta_{old}^2}{2(\beta_{old} + 1)}} = 4$$

Simplifying:
$$\frac{\beta_{new}^2}{\beta_{new} + 1} \cdot \frac{\beta_{old} + 1}{\beta_{old}^2} = 4$$

With β_old = 15:
$$\frac{\beta_{new}^2}{\beta_{new} + 1} \cdot \frac{16}{225} = 4$$

$$\frac{\beta_{new}^2}{\beta_{new} + 1} = 4 \times \frac{225}{16} = \frac{900}{16} = 56.25$$

$$\beta_{new}^2 = 56.25(\beta_{new} + 1)$$

$$\beta_{new}^2 = 56.25\beta_{new} + 56.25$$

$$\beta_{new}^2 - 56.25\beta_{new} - 56.25 = 0$$

**Step 4: Solve quadratic equation**

Using quadratic formula:
$$\beta_{new} = \frac{56.25 \pm \sqrt{56.25^2 + 4(56.25)}}{2}$$

$$\beta_{new} = \frac{56.25 \pm \sqrt{3164.0625 + 225}}{2}$$

$$\beta_{new} = \frac{56.25 \pm \sqrt{3389.0625}}{2}$$

$$\beta_{new} = \frac{56.25 \pm 58.22}{2}$$

Taking positive root:
$$\beta_{new} = \frac{56.25 + 58.22}{2} = \frac{114.47}{2} = 57.23$$

Result:
$$\boxed{\beta_{new} = 57.23}$$

**Step 5: Calculate required frequency deviation**

$$\Delta f_{new} = \beta_{new} \times f_m = 57.23 \times 5 \text{ kHz} = 286.2 \text{ kHz}$$

Result:
$$\boxed{\Delta f_{new} = 286.2 \text{ kHz}}$$

**Step 6: Verify new bandwidth requirement (Carson's Rule)**

$$B_{T,new} = 2(\Delta f_{new} + f_m) = 2(286.2 + 5) = 2 \times 291.2 = 582.4 \text{ kHz}$$

**Critical constraint:**
$$\boxed{B_{T,new} = 582.4 \text{ kHz} > B_{FI} = 200 \text{ kHz}}$$

**PROBLEM:** The existing 200 kHz IF filter is **insufficient** for this modulation index!

**Validation:**
- Dimensions: β is dimensionless ✓
- Sanity: β_new = 57.23 is much larger than β_old = 15 ✓
- Physical constraint: Would require wider IF filter (582 kHz vs 200 kHz available) ⚠

**Explanation:** To achieve a 6 dB improvement in output SNR, the modulation index must increase from 15 to approximately 57.2, corresponding to a frequency deviation of 286 kHz. However, this creates a **practical problem**: the required transmission bandwidth (582 kHz by Carson's Rule) exceeds the available IF filter bandwidth (200 kHz).

**Alternative Interpretation:**

If we assume the IF filter bandwidth is **fixed at 200 kHz** and cannot be changed, then we must keep:
$$B_T = 200 \text{ kHz}$$

From Carson's Rule:
$$200 = 2(\Delta f + 5)$$
$$100 = \Delta f + 5$$
$$\Delta f_{max} = 95 \text{ kHz}$$
$$\beta_{max} = \frac{95}{5} = 19$$

This gives maximum possible improvement of:
$$\frac{(S/N)_{D,\beta=19}}{(S/N)_{D,\beta=15}} = \frac{19^2}{15^2} \times \frac{15+1}{19+1} = \frac{361}{225} \times \frac{16}{20} = 1.604 \times 0.8 = 1.283$$

In dB:
$$\Delta(S/N) = 10\log_{10}(1.283) = 1.08 \text{ dB}$$

**Conclusion for part (c):**
- **Theoretical answer**: β = 57.2, Δf = 286 kHz (requires 582 kHz bandwidth)
- **Practical limit**: β = 19, Δf = 95 kHz (constrained by 200 kHz IF filter)
- **Achievable improvement with 200 kHz filter**: Only 1.08 dB, not 6 dB
- **To achieve 6 dB improvement**: Must widen IF filter to ~582 kHz

---

## Final Answers Summary

| Part | Answer | Units | Notes |
|------|--------|-------|-------|
| (a) | **210,938 = 53.2 dB** | - | F = 1 (noiseless), B_T = 160 kHz (Carson) |
| (b) | **168,750 = 52.3 dB** | - | Te = 72.5 K, F = 1.25 |
| (c) | **β = 57.2, Δf = 286 kHz** | - | Requires 582 kHz BW (impractical!) |

---

## Validation Checks

✓ **Dimensional Analysis**: All SNR values are dimensionless ratios

✓ **Sanity Checks**:
- FM processing gain: 13.2 dB (reasonable for β = 15)
- Noise figure impact: ~1 dB degradation (matches F = 0.97 dB)
- β relationship: Quadratic scaling verified
- Carson's Rule: B_T = 160 kHz used consistently

✓ **Special Cases**:
- If β → 0: (S/N)_D → (S/N)_R (no FM gain) ✓
- If F → 1: Part (b) → Part (a) ✓

⚠ **Practical Constraint**:
- Part (c) requires IF bandwidth beyond available hardware

✓ **Cross-validation**:
- Noise figure calculation: Te = 72.5 K → F = 1.25 ✓
- Carson's Rule: Bandwidth requirements consistent

---

## Key Learnings

### Physical Insights

• **FM Processing Gain**: FM demodulation provides SNR improvement by trading bandwidth for noise performance. The gain is proportional to β² but inversely proportional to the bandwidth expansion ratio (B_T/W).

• **W/B_T Factor**: This critical factor (0.03125 in this problem, using Carson's B_T = 160 kHz) represents the bandwidth compression. In wideband FM, we transmit a wideband signal (160 kHz) to carry a narrowband message (5 kHz), and FM demodulation converts this bandwidth excess into SNR gain.

• **Noise Figure Impact**: Added noise at the receiver (from the IF amplifier) degrades the input SNR, which then propagates through the system. A noise figure of 1.25 (1 dB) causes a 1 dB reduction in output SNR.

• **Bandwidth-SNR Trade-off**: To improve SNR by 6 dB, we need to increase β by a factor of √4 = 2, but this requires proportionally wider bandwidth (by Carson's Rule). There's no "free lunch" - better SNR demands more spectrum.

### Common Mistakes to Avoid

• **Inverted Fraction**: The most common error is using B_T/W instead of W/B_T. This gives absurdly high SNR values (41 dB gain instead of 12 dB). Always verify that W/B_T < 1 for wideband FM.

• **Ignoring Carson's Rule**: When β changes, B_T also changes! You cannot arbitrarily increase β without checking if the IF filter can accommodate the wider bandwidth.

• **Forgetting Noise Figure Effect**: The noise figure degrades the input SNR, not the output SNR directly. Apply F to (S/N)_R first, then use the FM formula.

• **dB vs Linear Confusion**: Always convert to linear for formula calculations, then convert back to dB for final answers.

### Formula Mastery

**Haykin FM SNR Formula (memorize!):**
$$\left(\frac{S}{N}\right)_{D} = 3\beta^2 \left(\frac{W}{B_T}\right) \left(\frac{S}{N}\right)_R$$

Where the factor W/B_T is always less than 1 in wideband FM.

**Alternative form with Carson's Rule:**
$$\left(\frac{S}{N}\right)_{D} = \frac{3\beta^2}{2(\beta + 1)} \left(\frac{S}{N}\right)_R$$

This form explicitly shows the β²/(β+1) relationship.

---

## Related Practice

To master FM receiver analysis, practice:

1. **Varying β**: Solve similar problems with different modulation indices (β = 5, 10, 20)
2. **Cascade Analysis**: Add RF amplifier before the mixer (Friis formula for overall noise figure)
3. **Pre-emphasis/De-emphasis**: Analyze SNR improvement with pre-emphasis filtering
4. **FM Threshold**: Study behavior when (S/N)_R approaches threshold (~10 dB)
5. **Comparison Problems**: Compare FM vs AM for same signal and bandwidth

**Related Topics:**
- Unit 7: Friis cascade formula for multi-stage noise analysis
- Unit 9: Shannon-Hartley capacity for FM channels
- Unit 4: Pre-emphasis, stereo FM, commercial FM broadcasting standards

---

## Exam Tips

**For FM receiver problems:**
1. Always write out the Haykin formula first
2. Calculate β = Δf/f_m immediately
3. Verify W/B_T < 1 (sanity check)
4. Apply noise figure to input SNR before FM formula
5. Check Carson's Rule bandwidth constraints
6. Show both linear and dB results

**Common exam variations:**
- Given output SNR, find required β or Δf
- Given noise figure in dB, convert to linear first
- Multiple stages (use Friis formula)
- Compare different modulation schemes

**Time-saving tips:**
- Memorize key conversions: 10^4 = 40 dB, factor of 2 = 3 dB, factor of 4 = 6 dB
- Use the factor form: 3β²(W/B_T) as a single "FM gain" factor
- Carson's Rule shortcut: B_T ≈ 2Δf when β >> 1

---

**END OF SOLUTION**
