# Amplitude Modulation (AM) - Complete Derivation from First Principles

**Date**: November 15, 2025
**Topic**: Amplitude Modulation Theory and Analysis
**Level**: Advanced Undergraduate/Graduate

---

## Starting Definitions

### Carrier Signal
The carrier signal is a high-frequency sinusoidal wave that serves as the "vehicle" for transmitting information:

$$c(t) = A_c \cos(2\pi f_c t)$$

Where:
- $A_c$ = Amplitude of the carrier signal (volts)
- $f_c$ = Carrier frequency (Hz), typically in RF range (kHz to GHz)
- $t$ = Time (seconds)

### Message Signal
The message signal contains the information to be transmitted:

$$m(t) = A_m \cos(2\pi f_m t)$$

Where:
- $A_m$ = Amplitude of the message signal (volts)
- $f_m$ = Message frequency (Hz), typically audio range (20 Hz - 20 kHz)
- Constraint: $f_m \ll f_c$ (message frequency must be much less than carrier frequency)

### Modulation Index
The modulation index quantifies the depth of modulation:

$$\mu = \frac{A_m}{A_c}$$

Where:
- $\mu$ = Modulation index (dimensionless)
- Valid range: $0 \leq \mu \leq 1$ for undistorted transmission
- $\mu = 1$ represents 100% modulation (maximum without distortion)
- $\mu > 1$ causes overmodulation and signal distortion

---

## Step-by-Step Derivation

### Step 1: Amplitude Variation Concept
**WHY**: In amplitude modulation, we want the message signal to control the amplitude of the carrier.

The instantaneous amplitude of the carrier must vary according to the message signal:

$$A(t) = A_c + m(t)$$

This ensures the carrier amplitude increases and decreases following the message signal.

Substituting the message signal:

$$A(t) = A_c + A_m \cos(2\pi f_m t)$$

$$A(t) = A_c[1 + \frac{A_m}{A_c} \cos(2\pi f_m t)]$$

$$A(t) = A_c[1 + \mu \cos(2\pi f_m t)]$$

**Physical Interpretation**: The carrier amplitude varies between $A_c(1-\mu)$ and $A_c(1+\mu)$.

---

### Step 2: Forming the AM Signal
**WHY**: We multiply the time-varying amplitude by the carrier oscillation to create the modulated signal.

The AM signal is the product of the time-varying amplitude and the carrier frequency:

$$s_{AM}(t) = A(t) \cdot \cos(2\pi f_c t)$$

Substituting our expression for $A(t)$:

$$s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)$$

**This is the standard form of the AM signal equation.**

---

### Step 3: Expanding Using Trigonometric Identity
**WHY**: To reveal the frequency components (carrier and sidebands) that make up the AM signal.

Expand the product:

$$s_{AM}(t) = A_c \cos(2\pi f_c t) + A_c \mu \cos(2\pi f_m t) \cos(2\pi f_c t)$$

Apply the product-to-sum trigonometric identity:

$$\cos(A) \cos(B) = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$$

With $A = 2\pi f_c t$ and $B = 2\pi f_m t$:

$$\cos(2\pi f_c t) \cos(2\pi f_m t) = \frac{1}{2}[\cos(2\pi(f_c - f_m)t) + \cos(2\pi(f_c + f_m)t)]$$

---

### Step 4: Complete Time-Domain Expression
**WHY**: To express the AM signal as a sum of three distinct frequency components.

Substituting the identity back:

$$s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2} \cos(2\pi(f_c - f_m)t) + \frac{A_c \mu}{2} \cos(2\pi(f_c + f_m)t)$$

**Final Time-Domain Formula**:

$$\boxed{s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2} \cos(2\pi(f_c - f_m)t) + \frac{A_c \mu}{2} \cos(2\pi(f_c + f_m)t)}$$

**Components**:
1. **Carrier**: $A_c \cos(2\pi f_c t)$ at frequency $f_c$
2. **Lower Sideband (LSB)**: $\frac{A_c \mu}{2} \cos(2\pi(f_c - f_m)t)$ at frequency $f_c - f_m$
3. **Upper Sideband (USB)**: $\frac{A_c \mu}{2} \cos(2\pi(f_c + f_m)t)$ at frequency $f_c + f_m$

---

### Step 5: Frequency-Domain Analysis Using Fourier Transform
**WHY**: To visualize the spectral content and understand bandwidth requirements.

Taking the Fourier Transform of each component:

$$\mathcal{F}\{A \cos(2\pi f_0 t)\} = \frac{A}{2}[\delta(f - f_0) + \delta(f + f_0)]$$

For the AM signal:

$$S_{AM}(f) = \frac{A_c}{2}[\delta(f - f_c) + \delta(f + f_c)]$$
$$+ \frac{A_c \mu}{4}[\delta(f - (f_c - f_m)) + \delta(f + (f_c - f_m))]$$
$$+ \frac{A_c \mu}{4}[\delta(f - (f_c + f_m)) + \delta(f + (f_c + f_m))]$$

**Frequency Spectrum** (positive frequencies only):
- Carrier at $f_c$ with amplitude $\frac{A_c}{2}$
- LSB at $f_c - f_m$ with amplitude $\frac{A_c \mu}{4}$
- USB at $f_c + f_m$ with amplitude $\frac{A_c \mu}{4}$

---

### Step 6: Bandwidth Calculation
**WHY**: To determine the frequency range occupied by the AM signal for spectrum allocation.

The bandwidth is the difference between the highest and lowest frequency components:

$$BW = (f_c + f_m) - (f_c - f_m)$$

$$\boxed{BW = 2f_m}$$

**For complex message signals** with bandwidth $B$:

$$\boxed{BW_{AM} = 2B}$$

**Key Insight**: AM doubles the bandwidth of the original message signal. This is inefficient but simple to implement.

---

## Frequency Spectrum Analysis

### Spectral Representation

```
Amplitude
    ^
    |
A_c/2|     *                      (Carrier)
    |
    |
A_cμ/4|  *     *                   (Sidebands)
    |
    |______|______|________________> Frequency
         fc-fm   fc   fc+fm
         LSB         USB

    |<---BW = 2fm--->|
```

### Spectral Components Table

| Component | Frequency | Amplitude | Information Content |
|-----------|-----------|-----------|---------------------|
| Carrier | $f_c$ | $\frac{A_c}{2}$ | None (constant) |
| LSB | $f_c - f_m$ | $\frac{A_c \mu}{4}$ | Complete message |
| USB | $f_c + f_m$ | $\frac{A_c \mu}{4}$ | Complete message (redundant) |

**Critical Observation**: Both sidebands contain identical information. The carrier contains no information but carries most of the power.

---

## Power and Efficiency Analysis

### Step 7: Power Distribution
**WHY**: To understand energy efficiency and optimize transmission.

For sinusoidal signals, average power over a resistive load $R$ is:

$$P = \frac{A_{rms}^2}{R} = \frac{A^2}{2R}$$

#### Carrier Power

$$P_c = \frac{A_c^2}{2R}$$

#### Lower Sideband Power

$$P_{LSB} = \frac{(\frac{A_c \mu}{2})^2}{2R} = \frac{A_c^2 \mu^2}{8R}$$

#### Upper Sideband Power

$$P_{USB} = \frac{(\frac{A_c \mu}{2})^2}{2R} = \frac{A_c^2 \mu^2}{8R}$$

#### Total Sideband Power

$$P_{sidebands} = P_{LSB} + P_{USB} = \frac{A_c^2 \mu^2}{4R}$$

#### Total Transmitted Power

$$P_{total} = P_c + P_{sidebands}$$

$$P_{total} = \frac{A_c^2}{2R} + \frac{A_c^2 \mu^2}{4R}$$

$$P_{total} = \frac{A_c^2}{2R}\left(1 + \frac{\mu^2}{2}\right)$$

$$\boxed{P_{total} = P_c\left(1 + \frac{\mu^2}{2}\right)}$$

---

### Step 8: Transmission Efficiency
**WHY**: Efficiency determines how much transmitted power actually carries information.

Efficiency is the ratio of useful power (sidebands) to total power:

$$\eta = \frac{P_{sidebands}}{P_{total}} \times 100\%$$

$$\eta = \frac{\frac{A_c^2 \mu^2}{4R}}{\frac{A_c^2}{2R}\left(1 + \frac{\mu^2}{2}\right)} \times 100\%$$

$$\eta = \frac{\mu^2/4}{1 + \mu^2/2} \times 100\%$$

$$\eta = \frac{\mu^2}{2 + \mu^2} \times 100\%$$

$$\boxed{\eta = \frac{\mu^2}{2 + \mu^2} \times 100\%}$$

#### Maximum Efficiency (at μ = 1)

$$\eta_{max} = \frac{1^2}{2 + 1^2} \times 100\% = \frac{1}{3} \times 100\%$$

$$\boxed{\eta_{max} = 33.33\%}$$

**Critical Finding**: Even at 100% modulation, only one-third of the transmitted power carries information. The remaining two-thirds is in the carrier, which is necessary for simple demodulation but carries no information.

---

### Efficiency vs. Modulation Index

| μ | η (%) | Power Distribution |
|---|-------|-------------------|
| 0.1 | 0.50% | Negligible sidebands |
| 0.3 | 4.29% | Low efficiency |
| 0.5 | 11.11% | Moderate efficiency |
| 0.7 | 19.60% | Good efficiency |
| 1.0 | 33.33% | Maximum efficiency |

**Practical Insight**: Higher modulation index improves efficiency, but overmodulation (μ > 1) causes distortion.

---

## Final Formulas Summary

### Compact Form
$$\boxed{s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)] \cos(2\pi f_c t)}$$

### Expanded Form (Three Components)
$$\boxed{s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2} \cos(2\pi(f_c - f_m)t) + \frac{A_c \mu}{2} \cos(2\pi(f_c + f_m)t)}$$

### Bandwidth
$$\boxed{BW = 2f_m \text{ or } BW = 2B \text{ (for complex signals)}}$$

### Total Power
$$\boxed{P_{total} = P_c\left(1 + \frac{\mu^2}{2}\right)}$$

### Efficiency
$$\boxed{\eta = \frac{\mu^2}{2 + \mu^2} \times 100\% \quad \text{(max = 33.33\% at } \mu = 1\text{)}}$$

---

## Key Insights

### 1. Frequency Translation
AM shifts the baseband message signal to a high-frequency carrier band through multiplication. This enables wireless transmission and frequency division multiplexing.

### 2. Bandwidth Inefficiency
AM doubles the bandwidth requirement compared to the original message. This is a fundamental trade-off for simple implementation.

### 3. Power Inefficiency
Maximum power efficiency is only 33.33%, with most power wasted in the carrier. This led to the development of:
- **SSB (Single Sideband)**: Removes carrier and one sideband → η up to 100%
- **DSB-SC (Double Sideband Suppressed Carrier)**: Removes carrier → η up to 50%

### 4. Redundancy
Both sidebands carry identical information. Removing one sideband (SSB) saves bandwidth and power without information loss.

### 5. Envelope Detection
The AM signal envelope equals $A_c[1 + \mu \cos(2\pi f_m t)]$, which directly represents the message. This allows simple, low-cost demodulation using a diode detector.

### 6. Overmodulation
When $\mu > 1$, the envelope crosses zero, causing phase reversal and severe distortion. This must be avoided through:
- Automatic Gain Control (AGC)
- Peak limiters
- Proper transmitter design

### 7. Spectrum Conservation
The 2:1 bandwidth expansion makes AM inefficient for spectrum-limited applications, explaining its decline in modern digital communications.

---

## Applications

### Historical Applications
1. **AM Radio Broadcasting** (535-1605 kHz)
   - Standard amplitude modulation
   - Simple receiver design
   - Long-range propagation
   - Being phased out in favor of FM and digital

2. **Aviation Communications** (118-137 MHz)
   - AM still used for reliability
   - Simple equipment
   - Robust in interference

3. **Citizens Band (CB) Radio** (26.965-27.405 MHz)
   - AM and SSB modes
   - Short-range communication

### Modern Applications
1. **Two-way Radio Systems**
   - Public safety
   - Military communications
   - Marine radio

2. **Amplitude Shift Keying (ASK)**
   - Digital variant of AM
   - Used in RFID systems
   - Optical fiber communications

3. **Quadrature Amplitude Modulation (QAM)**
   - Modern evolution combining AM and PM
   - Used in:
     - WiFi (802.11ac/ax)
     - Cable modems
     - Digital television
     - 4G/5G cellular networks

4. **Software Defined Radio (SDR)**
   - AM demodulation in digital domain
   - Educational tool
   - Research applications

### Why AM Persists
Despite inefficiency:
- **Simplicity**: Easy to generate and demodulate
- **Robustness**: Works in high-noise environments
- **Legacy Systems**: Massive installed base
- **Cost**: Inexpensive receivers
- **Regulatory**: Established frequency allocations

---

## Mathematical Derivation Summary

```
Starting Point:
  Carrier: c(t) = Ac·cos(2πfc·t)
  Message: m(t) = Am·cos(2πfm·t)

Step 1: Amplitude Variation
  A(t) = Ac[1 + μ·cos(2πfm·t)]

Step 2: Form AM Signal
  sAM(t) = A(t)·cos(2πfc·t)

Step 3: Expand Product
  sAM(t) = Ac·cos(2πfc·t) + Ac·μ·cos(2πfm·t)·cos(2πfc·t)

Step 4: Apply Trig Identity
  cos(A)·cos(B) = ½[cos(A-B) + cos(A+B)]

Step 5: Final Time-Domain
  sAM(t) = Ac·cos(2πfc·t) + (Ac·μ/2)·cos(2π(fc-fm)t) + (Ac·μ/2)·cos(2π(fc+fm)t)
           [Carrier]          [LSB]                      [USB]

Step 6: Frequency Domain
  Fourier Transform → Three spectral lines

Step 7: Bandwidth
  BW = (fc + fm) - (fc - fm) = 2fm

Step 8: Power Analysis
  Ptotal = Pc(1 + μ²/2)

Step 9: Efficiency
  η = μ²/(2 + μ²) × 100%
  ηmax = 33.33% at μ = 1
```

---

## Conclusion

Amplitude Modulation represents the foundation of analog communications theory. While inefficient in bandwidth and power, its mathematical elegance and implementation simplicity made it the cornerstone of early radio systems. Understanding AM is essential for:

- Grasping more advanced modulation techniques (SSB, QAM, OFDM)
- Appreciating spectrum management challenges
- Designing efficient communication systems
- Analyzing trade-offs between complexity and performance

The derivation demonstrates fundamental principles:
- **Frequency translation** through multiplication
- **Spectral analysis** using Fourier transforms
- **Power budgeting** in communication systems
- **Trade-offs** between simplicity and efficiency

Modern communications have largely moved beyond AM, but its principles remain relevant in understanding how information is encoded, transmitted, and recovered in all modulation schemes.

---

**End of Derivation**

*Generated by Communications Learning System*
*Date: November 15, 2025*
