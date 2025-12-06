# Ejercicio TP5_3: FM Receiver SNR Analysis - Complete Solution

**Date**: 2025-12-06
**Source**: Exercise TP5 #3 - FM Reception with Noise

---

## Problem Statement

Se tiene un receptor de FM con un filtro de FI con un ancho de banda de 200 kHz y un filtro de salida pasabajos ideal con f_c = 15 kHz que recibe una señal modulada por un tono con las siguientes características: f_m = 5 kHz y Δf = 75 kHz. La relación potencia media de señal a potencia media de ruido en la entrada del amplificador de FI es de 40 dB.

**Se pregunta:**
a) ¿Cuál es la S/N luego del filtro de salida si F_FI = 1?
b) ¿Cuál es la S/N luego del filtro de salida si Te_FI = 72.50 K?
c) ¿Cuál será el índice de modulación necesario para mejorar en 6 dB la S/N calculada en "a)"?

---

## Given Data

| Variable | Value | Unit | Converted (SI) | Notes |
|----------|-------|------|----------------|-------|
| B_FI | 200 | kHz | 200,000 Hz | IF filter bandwidth |
| f_c | 15 | kHz | 15,000 Hz | Output lowpass filter cutoff |
| f_m | 5 | kHz | 5,000 Hz | Modulating tone frequency |
| Δf | 75 | kHz | 75,000 Hz | Frequency deviation |
| (S/N)_in | 40 | dB | 10,000 (linear) | Input SNR at IF amplifier |
| F_FI (part a) | 1 | - | 1 | Noiseless amplifier |
| Te_FI (part b) | 72.50 | K | 72.50 K | Equivalent noise temperature |

**Constants:**
- T₀ = 290 K (Reference temperature for noise figure)
- k = 1.38 × 10⁻²³ J/K (Boltzmann constant - not needed for this problem)

---

## Problem Analysis

**Type:** FM Receiver - SNR Analysis with Noise Figure Effects

**Key Concepts Involved:**
- FM modulation index and its relationship to SNR improvement
- FM demodulation gain (processing gain)
- Noise figure and equivalent noise temperature relationship
- SNR degradation through noisy amplifiers

**Relevant Formulas:**

1. **FM Modulation Index:**
   $$\beta = \frac{\Delta f}{f_m}$$

2. **FM Output SNR (Single Tone Modulation):**
   $$\left(\frac{S}{N}\right)_{out} = \frac{3}{2} \beta^2 \left(\frac{B_{FI}}{f_m}\right) \left(\frac{S}{N}\right)_{in}$$

   This assumes the input SNR is measured at the IF stage BEFORE the noise figure degradation.

3. **Noise Figure from Equivalent Temperature:**
   $$F = 1 + \frac{T_e}{T_0}$$

4. **SNR Degradation Due to Noise Figure:**
   $$\left(\frac{S}{N}\right)_{in,effective} = \frac{1}{F} \left(\frac{S}{N}\right)_{in}$$

5. **dB to Linear Conversion:**
   $$X_{linear} = 10^{X_{dB}/10}$$

6. **Linear to dB Conversion:**
   $$X_{dB} = 10 \log_{10}(X_{linear})$$

---

## Solution

### Part (a): Output S/N with F_FI = 1

**What's being asked:** Calculate the output SNR when the IF amplifier is noiseless (F = 1).

**Approach:**
1. Calculate modulation index β
2. Convert input SNR from dB to linear
3. Apply FM SNR gain formula
4. Convert result back to dB

---

**Step 1: Calculate Modulation Index β**

Formula:
$$\beta = \frac{\Delta f}{f_m}$$

Substitution:
$$\beta = \frac{75,000 \text{ Hz}}{5,000 \text{ Hz}} = 15$$

Result:
$$\boxed{\beta = 15}$$

**Validation:**
- Dimensionless ratio ✓
- β = 15 indicates wideband FM (β > 1) ✓
- Sanity: Large deviation (75 kHz) vs small message frequency (5 kHz) gives large β ✓

**Explanation:** The modulation index of 15 is quite high, typical of commercial FM broadcasting. This high β will provide significant SNR improvement at the output.

---

**Step 2: Convert Input SNR from dB to Linear**

Formula:
$$\left(\frac{S}{N}\right)_{in,linear} = 10^{(S/N)_{in,dB}/10}$$

Substitution:
$$\left(\frac{S}{N}\right)_{in,linear} = 10^{40/10} = 10^4$$

Result:
$$\boxed{\left(\frac{S}{N}\right)_{in,linear} = 10,000}$$

**Validation:**
- 40 dB = 10,000:1 ratio ✓
- This is a strong input signal ✓

---

**Step 3: Calculate Output SNR (Linear)**

Formula:
$$\left(\frac{S}{N}\right)_{out} = \frac{3}{2} \beta^2 \left(\frac{B_{FI}}{f_m}\right) \left(\frac{S}{N}\right)_{in}$$

Since F = 1, there's no noise figure degradation:
$$\left(\frac{S}{N}\right)_{in,effective} = \left(\frac{S}{N}\right)_{in} = 10,000$$

Substitution:
$$\left(\frac{S}{N}\right)_{out} = \frac{3}{2} \times (15)^2 \times \left(\frac{200,000}{5,000}\right) \times 10,000$$

Calculation breakdown:
$$\beta^2 = 15^2 = 225$$

$$\frac{B_{FI}}{f_m} = \frac{200,000}{5,000} = 40$$

$$\frac{3}{2} \times 225 = 337.5$$

$$\left(\frac{S}{N}\right)_{out} = 337.5 \times 40 \times 10,000$$

$$\left(\frac{S}{N}\right)_{out} = 13,500 \times 10,000 = 135,000,000$$

Result:
$$\boxed{\left(\frac{S}{N}\right)_{out,linear} = 1.35 \times 10^8}$$

---

**Step 4: Convert Output SNR to dB**

Formula:
$$\left(\frac{S}{N}\right)_{out,dB} = 10 \log_{10}\left(\frac{S}{N}\right)_{out,linear}$$

Substitution:
$$\left(\frac{S}{N}\right)_{out,dB} = 10 \log_{10}(1.35 \times 10^8)$$

Calculation:
$$\log_{10}(1.35 \times 10^8) = \log_{10}(1.35) + \log_{10}(10^8)$$

$$= 0.1303 + 8 = 8.1303$$

$$\left(\frac{S}{N}\right)_{out,dB} = 10 \times 8.1303 = 81.303 \text{ dB}$$

Result:
$$\boxed{\left(\frac{S}{N}\right)_{out} = 81.3 \text{ dB}}$$

**Validation:**
- Output SNR (81.3 dB) > Input SNR (40 dB) ✓
- SNR improvement = 81.3 - 40 = 41.3 dB ✓
- This improvement comes from FM processing gain ✓
- Dimensions: dB (dimensionless ratio) ✓

**Explanation:** The FM receiver provides a massive SNR improvement of 41.3 dB! This is the famous "FM quieting effect" where wideband FM trades bandwidth for improved SNR. The improvement factor of 13,500 comes from:
- β² factor: 225
- Bandwidth expansion factor (B_FI/f_m): 40
- FM constant factor: 3/2

---

### Part (b): Output S/N with Te_FI = 72.50 K

**What's being asked:** Calculate the output SNR when the IF amplifier has an equivalent noise temperature of 72.50 K.

**Approach:**
1. Calculate noise figure F from equivalent temperature Te
2. Calculate effective input SNR (degraded by F)
3. Apply FM SNR gain formula with degraded input
4. Convert to dB

---

**Step 1: Calculate Noise Figure from Equivalent Temperature**

Formula:
$$F = 1 + \frac{T_e}{T_0}$$

Substitution:
$$F = 1 + \frac{72.50 \text{ K}}{290 \text{ K}}$$

Calculation:
$$\frac{72.50}{290} = 0.25$$

$$F = 1 + 0.25 = 1.25$$

Result:
$$\boxed{F = 1.25 \text{ (linear)}}$$

Convert to dB:
$$F_{dB} = 10 \log_{10}(1.25) = 10 \times 0.0969 = 0.969 \text{ dB}$$

$$\boxed{F_{dB} \approx 0.97 \text{ dB}}$$

**Validation:**
- F ≥ 1 always ✓
- Low noise figure (< 1 dB) indicates good amplifier ✓
- Sanity: Te = 72.5 K is about 1/4 of T₀, so F should be 1.25 ✓

**Explanation:** A noise figure of 0.97 dB is quite good for an IF amplifier. This represents only a 25% increase in noise power over an ideal noiseless amplifier.

---

**Step 2: Calculate Effective Input SNR**

When the amplifier has noise figure F, it degrades the input SNR:

Formula:
$$\left(\frac{S}{N}\right)_{in,effective} = \frac{1}{F} \left(\frac{S}{N}\right)_{in}$$

Substitution:
$$\left(\frac{S}{N}\right)_{in,effective} = \frac{1}{1.25} \times 10,000$$

Calculation:
$$\left(\frac{S}{N}\right)_{in,effective} = 0.8 \times 10,000 = 8,000$$

Result:
$$\boxed{\left(\frac{S}{N}\right)_{in,effective,linear} = 8,000}$$

In dB:
$$\left(\frac{S}{N}\right)_{in,effective,dB} = 10 \log_{10}(8,000) = 10 \times 3.903 = 39.03 \text{ dB}$$

$$\boxed{\left(\frac{S}{N}\right)_{in,effective} = 39.0 \text{ dB}}$$

**Validation:**
- Degradation = 40 - 39.0 = 1.0 dB ≈ F_dB ✓
- Effective SNR < Original SNR ✓

**Explanation:** The noise figure causes a 1 dB reduction in input SNR, from 40 dB to 39 dB.

---

**Step 3: Calculate Output SNR with Degraded Input**

Formula:
$$\left(\frac{S}{N}\right)_{out} = \frac{3}{2} \beta^2 \left(\frac{B_{FI}}{f_m}\right) \left(\frac{S}{N}\right)_{in,effective}$$

Substitution (using same β and bandwidth ratio from part a):
$$\left(\frac{S}{N}\right)_{out} = \frac{3}{2} \times (15)^2 \times \left(\frac{200,000}{5,000}\right) \times 8,000$$

$$\left(\frac{S}{N}\right)_{out} = 337.5 \times 40 \times 8,000$$

$$\left(\frac{S}{N}\right)_{out} = 13,500 \times 8,000$$

Result:
$$\boxed{\left(\frac{S}{N}\right)_{out,linear} = 1.08 \times 10^8}$$

---

**Step 4: Convert to dB**

Formula:
$$\left(\frac{S}{N}\right)_{out,dB} = 10 \log_{10}(1.08 \times 10^8)$$

Calculation:
$$\log_{10}(1.08 \times 10^8) = \log_{10}(1.08) + 8$$

$$= 0.0334 + 8 = 8.0334$$

$$\left(\frac{S}{N}\right)_{out,dB} = 10 \times 8.0334 = 80.334 \text{ dB}$$

Result:
$$\boxed{\left(\frac{S}{N}\right)_{out} = 80.3 \text{ dB}}$$

**Validation:**
- Output SNR (80.3 dB) is 1 dB less than part (a) ✓
- Difference: 81.3 - 80.3 = 1.0 dB = F_dB ✓
- Still much better than input (39 dB) ✓

**Explanation:** The noise figure causes a 1 dB reduction in output SNR. The FM processing gain is still applied, but to a degraded input signal. The final output is 80.3 dB instead of 81.3 dB.

**Comparison:**
- Part (a) F=1: (S/N)_out = 81.3 dB
- Part (b) F=1.25: (S/N)_out = 80.3 dB
- Degradation = 1.0 dB = 10 log₁₀(1.25) ✓

---

### Part (c): New Modulation Index for 6 dB Improvement

**What's being asked:** Find the modulation index β needed to improve the SNR from part (a) by 6 dB.

**Approach:**
1. Determine target output SNR (81.3 dB + 6 dB)
2. Use FM SNR formula to solve for β²
3. Extract β
4. Calculate required new Δf (keeping f_m constant)

---

**Step 1: Determine Target Output SNR**

Starting from part (a): (S/N)_out,a = 81.3 dB

Target improvement: +6 dB

Formula:
$$\left(\frac{S}{N}\right)_{out,target,dB} = \left(\frac{S}{N}\right)_{out,a,dB} + 6$$

Result:
$$\boxed{\left(\frac{S}{N}\right)_{out,target} = 81.3 + 6 = 87.3 \text{ dB}}$$

Convert to linear:
$$\left(\frac{S}{N}\right)_{out,target,linear} = 10^{87.3/10} = 10^{8.73} = 5.37 \times 10^8$$

$$\boxed{\left(\frac{S}{N}\right)_{out,target,linear} = 5.37 \times 10^8}$$

**Validation:**
- 6 dB improvement = factor of 10^0.6 ≈ 3.98 ≈ 4 ✓
- Check: (1.35 × 10⁸) × 4 = 5.4 × 10⁸ ✓

---

**Step 2: Set Up Equation to Solve for β_new**

The FM SNR formula is:
$$\left(\frac{S}{N}\right)_{out} = \frac{3}{2} \beta^2 \left(\frac{B_{FI}}{f_m}\right) \left(\frac{S}{N}\right)_{in}$$

We can write the ratio of target to original:
$$\frac{\left(\frac{S}{N}\right)_{out,target}}{\left(\frac{S}{N}\right)_{out,a}} = \frac{\beta_{new}^2}{\beta_a^2}$$

This is because all other factors remain constant (B_FI, f_m, (S/N)_in, F=1).

Formula:
$$\beta_{new}^2 = \beta_a^2 \times \frac{\left(\frac{S}{N}\right)_{out,target}}{\left(\frac{S}{N}\right)_{out,a}}$$

---

**Step 3: Calculate β_new²**

In dB, a 6 dB improvement means:
$$\left(\frac{S}{N}\right)_{out,target,dB} - \left(\frac{S}{N}\right)_{out,a,dB} = 6 \text{ dB}$$

In linear:
$$\frac{\left(\frac{S}{N}\right)_{out,target}}{\left(\frac{S}{N}\right)_{out,a}} = 10^{6/10} = 10^{0.6} = 3.981$$

$$\boxed{\text{Required improvement factor} = 3.981}$$

Now solve for β_new²:
$$\beta_{new}^2 = (15)^2 \times 3.981$$

$$\beta_{new}^2 = 225 \times 3.981 = 895.725$$

Result:
$$\boxed{\beta_{new}^2 = 895.7}$$

---

**Step 4: Calculate β_new**

Formula:
$$\beta_{new} = \sqrt{\beta_{new}^2}$$

Substitution:
$$\beta_{new} = \sqrt{895.7}$$

Calculation:
$$\beta_{new} = 29.928$$

Result:
$$\boxed{\beta_{new} = 29.93}$$

**Validation:**
- β_new > β_a (29.93 > 15) ✓
- Ratio: β_new/β_a = 29.93/15 = 1.995 ≈ 2 ✓
- Check: (β_new/β_a)² = (1.995)² = 3.98 ≈ 4 = 10^0.6 ✓
- Sanity: Need to double β to get 6 dB (≈4×) improvement ✓

**Explanation:** To achieve a 6 dB (≈4×) improvement in output SNR, we need to increase the modulation index by a factor of 2 (since SNR ∝ β²). The new modulation index is approximately 30.

---

**Step 5: Calculate Required New Δf**

The modulation index is defined as:
$$\beta = \frac{\Delta f}{f_m}$$

Assuming we keep f_m = 5 kHz constant:

Formula:
$$\Delta f_{new} = \beta_{new} \times f_m$$

Substitution:
$$\Delta f_{new} = 29.93 \times 5,000 \text{ Hz}$$

Result:
$$\boxed{\Delta f_{new} = 149,650 \text{ Hz} = 149.65 \text{ kHz}}$$

**Validation:**
- Δf_new > Δf_a (149.65 kHz > 75 kHz) ✓
- Ratio: 149.65/75 = 1.995 ≈ 2 ✓
- Dimensions: Hz ✓
- Sanity: Need to double frequency deviation to double β ✓

**Explanation:** To achieve the 6 dB improvement, the frequency deviation must be increased from 75 kHz to approximately 150 kHz. This would require:
1. More powerful transmitter (higher peak deviation)
2. Wider IF filter bandwidth at the receiver
3. Trade-off: More bandwidth consumption

---

**Alternative Interpretation (If B_FI Must Stay at 200 kHz):**

If the IF filter bandwidth is fixed at 200 kHz, then we need to check if the new signal fits:

Carson's Rule for FM bandwidth:
$$BW_{FM} = 2(\Delta f + f_m)$$

For β_new = 29.93:
$$BW_{FM,new} = 2(149.65 + 5) = 2(154.65) = 309.3 \text{ kHz}$$

This exceeds B_FI = 200 kHz! ⚠️

**Implication:** If the IF filter bandwidth is constrained to 200 kHz, achieving a 6 dB improvement by increasing β alone is **not feasible** without also widening the IF filter.

**Practical consideration:** The maximum β achievable with B_FI = 200 kHz and f_m = 5 kHz is:
$$BW_{FM} = 200 \text{ kHz} = 2(\Delta f_{max} + 5 \text{ kHz})$$
$$\Delta f_{max} = 95 \text{ kHz}$$
$$\beta_{max} = 95/5 = 19$$

This would give an improvement of:
$$\text{Improvement factor} = \left(\frac{19}{15}\right)^2 = 1.604$$
$$\text{Improvement (dB)} = 10 \log_{10}(1.604) = 2.05 \text{ dB}$$

**Conclusion for part (c):** The theoretical answer is β_new ≈ 30, but practical implementation would require widening the IF filter to at least 310 kHz.

---

## Final Answers Summary

| Part | Answer | Units | Notes |
|------|--------|-------|-------|
| (a) | 81.3 | dB | With noiseless amplifier (F=1) |
| (b) | 80.3 | dB | With Te_FI = 72.50 K (F=1.25) |
| (c) | β = 29.93 | - | Requires Δf ≈ 150 kHz |
| (c) | Δf = 149.65 | kHz | New frequency deviation needed |

**Key Result:**
- FM provides 41.3 dB of SNR improvement (part a)
- Noise figure causes 1 dB degradation (part b)
- Doubling β improves SNR by 6 dB (part c)

---

## Validation Checks

✓ **Dimensional Analysis**:
- All SNR values are dimensionless (expressed in dB) ✓
- β is dimensionless ✓
- Frequency deviations in Hz ✓

✓ **Sanity Checks**:
- Output SNR > Input SNR (FM processing gain) ✓
- Higher β gives higher output SNR ✓
- Noise figure degrades SNR ✓
- 6 dB improvement requires ~2× increase in β ✓

✓ **Special Cases**:
- When F = 1, no degradation occurs ✓
- When β increases, SNR increases quadratically ✓

✓ **Cross-validation**:
- Part (b) is 1 dB worse than part (a), matching F_dB ✓
- Part (c): (β_new/β_a)² = 3.98 ≈ 10^0.6 ✓

✓ **Numerical Consistency**:
- Linear to dB conversions verified ✓
- All intermediate calculations checked ✓

---

## Key Learnings

### 1. FM Processing Gain (FM Quieting Effect)

**Physical Insight:** FM receivers provide significant SNR improvement through the demodulation process. The output SNR is improved by a factor of (3/2)β²(B_FI/f_m) compared to the input. This is why FM radio sounds so clean even with moderate signal strengths.

**Formula:**
$$\text{FM Gain} = \frac{3}{2} \beta^2 \left(\frac{B_{FI}}{f_m}\right)$$

In this problem: Gain = 13,500 = 41.3 dB

This gain comes from:
- **β² term (225)**: Larger frequency deviation spreads the signal power across more bandwidth
- **B_FI/f_m term (40)**: Wider IF bandwidth captures more of the FM signal
- **3/2 constant**: Intrinsic to FM demodulation mathematics

### 2. Noise Figure Impact

**Physical Insight:** Any real amplifier adds noise, characterized by noise figure F or equivalent temperature Te. This degrades the input SNR before FM processing gain is applied.

**Key Relationship:**
$$F = 1 + \frac{T_e}{T_0}$$

where T₀ = 290 K is the standard reference temperature.

**Important:** The noise figure degrades SNR at the input, but the FM processing gain is still applied. So a 1 dB noise figure causes 1 dB loss at both input AND output.

### 3. Modulation Index and SNR Relationship

**Physical Insight:** Since (S/N)_out ∝ β², the output SNR is quadratically related to modulation index.

**Practical Implications:**
- To double output SNR (+3 dB), increase β by √2 = 1.41
- To quadruple output SNR (+6 dB), increase β by 2
- To get 10× SNR (+10 dB), increase β by √10 = 3.16

**Trade-off:** Higher β requires:
- Wider bandwidth (Carson's Rule: BW = 2(Δf + f_m))
- More transmitter power for larger deviation
- Better linearity in transmitter

### 4. Bandwidth-SNR Trade-off in FM

**Physical Insight:** FM trades bandwidth for SNR improvement. By using more bandwidth than necessary (wideband FM, β > 1), we can achieve superior noise performance.

**Comparison with AM:**
- AM: BW = 2f_m, no SNR improvement
- FM: BW = 2(Δf + f_m), SNR improvement ∝ β²

For this problem:
- Message bandwidth: 5 kHz (single tone)
- IF bandwidth needed: 200 kHz
- Bandwidth expansion: 40×
- SNR improvement: 13,500× (41.3 dB)

This is the fundamental reason FM broadcasting (88-108 MHz) uses 200 kHz channel spacing for 15 kHz audio - the bandwidth expansion provides excellent noise immunity.

### 5. Common Pitfalls to Avoid

**Pitfall 1:** Forgetting to convert dB to linear before calculations
- Always work in linear for multiplications
- Convert back to dB for final answer

**Pitfall 2:** Applying noise figure incorrectly
- F degrades the INPUT SNR: (S/N)_effective = (S/N)_in / F
- Then apply FM gain to the degraded input
- NOT: Apply FM gain first, then divide by F

**Pitfall 3:** Confusing β with Δf
- β is dimensionless: β = Δf/f_m
- β is what matters for SNR calculations
- Δf alone doesn't determine performance

**Pitfall 4:** Not checking bandwidth constraints
- Increasing β requires wider bandwidth
- Carson's Rule: BW = 2(Δf + f_m) = 2f_m(β + 1)
- Receiver IF filter must accommodate the FM bandwidth

### 6. Physical Meaning of Results

**Part (a) - 81.3 dB:**
This is an excellent SNR, corresponding to a power ratio of 135 million to 1. In audio terms, this would be crystal-clear reception with imperceptible noise.

**Part (b) - 80.3 dB:**
The 1 dB degradation is barely noticeable in practice. A noise figure of ~1 dB is typical of good RF amplifiers (LNA, IF amplifiers).

**Part (c) - β = 30:**
This is an extremely high modulation index, approaching the limits of commercial FM systems. For reference:
- FM broadcasting: β ≈ 5 (Δf = 75 kHz, f_m = 15 kHz)
- NBFM (narrowband): β < 1
- Wideband FM: β > 1

Achieving β = 30 would require Δf = 150 kHz, which is twice the standard FM broadcast deviation.

---

## Related Practice

To master FM receiver analysis, try:

1. **Vary the parameters**: What if f_m = 10 kHz instead? How does this affect β and output SNR?

2. **Different noise figures**: Calculate output SNR for F = 3 dB (typical), F = 10 dB (poor amplifier)

3. **Threshold effect**: Research FM threshold - what happens when input SNR drops below ~10 dB?

4. **Narrowband FM**: Solve the same problem with Δf = 5 kHz (β = 1). Compare SNR improvement.

5. **Cascade analysis**: What if there are multiple amplifiers with different noise figures? (Use Friis formula for cascaded F)

6. **Pre-emphasis/de-emphasis**: How do these techniques further improve SNR in FM systems?

7. **Carson's Rule verification**: Calculate exact FM bandwidth using Bessel functions and compare to Carson's approximation

8. **Power allocation**: If total transmitted power is fixed, how should you allocate between carrier and sidebands?

---

## Additional Notes

### FM System Design Considerations

This problem illustrates the key FM system design trade-offs:

**Advantage of high β (wideband FM):**
- Excellent noise immunity (41 dB improvement in this case)
- Superior audio quality
- Threshold extension (FM quieting)

**Disadvantage of high β:**
- Large bandwidth requirement (200 kHz vs 10 kHz for AM)
- More complex transmitter (frequency modulator)
- More complex receiver (discriminator, PLL)
- Spectrum efficiency reduced

**When to use FM:**
- Applications where SNR/quality is paramount
- Sufficient bandwidth available (VHF/UHF)
- Fixed installations (broadcasting, point-to-point links)

**When not to use FM:**
- Bandwidth-limited scenarios
- Long-distance HF communication
- Power-limited systems (space communications)

### Historical Context

The spectacular SNR improvement of FM (discovered by Edwin Armstrong in 1933) revolutionized radio broadcasting. Before FM:
- AM radio: noisy, interference-prone
- Required high transmitter power for quality

After FM:
- Clear, noise-free audio with moderate power
- Static immunity (lightning, ignition noise)
- Enabled high-fidelity music broadcasting

This problem's 41.3 dB improvement is exactly why FM radio sounds so much better than AM!

---

**END OF SOLUTION**

*Generated by: Exercise Solver (Green Subagent)*
*Date: 2025-12-06*
*Model: Claude Opus 4.5*
