# Frequency Modulation (FM) and Carson's Rule Derivation

**Date:** 2025-11-15
**Topic:** FM Theory and Bandwidth Estimation
**Course:** Communications Systems

---

## 1. Starting Point: Phase Modulation (PM)

### 1.1 General Form of an Angle-Modulated Signal

Any angle-modulated carrier can be expressed as:

$$
s(t) = A_c \cos[\omega_c t + \phi(t)]
$$

where:
- $A_c$ = carrier amplitude (constant)
- $\omega_c = 2\pi f_c$ = carrier angular frequency
- $\phi(t)$ = time-varying phase deviation

The **instantaneous phase** is:

$$
\theta_i(t) = \omega_c t + \phi(t)
$$

### 1.2 Phase Modulation Definition

In **Phase Modulation (PM)**, the phase deviation is directly proportional to the message signal:

$$
\phi(t) = k_p m(t)
$$

where:
- $k_p$ = phase sensitivity constant (rad/V)
- $m(t)$ = message (modulating) signal

Therefore, the PM signal is:

$$
s_{PM}(t) = A_c \cos[\omega_c t + k_p m(t)]
$$

---

## 2. Frequency Modulation Derived from Phase Modulation

### 2.1 Instantaneous Frequency Concept

The **instantaneous angular frequency** is defined as the time derivative of the instantaneous phase:

$$
\omega_i(t) = \frac{d\theta_i(t)}{dt} = \frac{d}{dt}[\omega_c t + \phi(t)]
$$

$$
\omega_i(t) = \omega_c + \frac{d\phi(t)}{dt}
$$

The **instantaneous frequency** (in Hz) is:

$$
f_i(t) = \frac{\omega_i(t)}{2\pi} = f_c + \frac{1}{2\pi}\frac{d\phi(t)}{dt}
$$

### 2.2 Frequency Modulation Definition

In **Frequency Modulation (FM)**, the instantaneous frequency deviation from the carrier is directly proportional to the message signal:

$$
f_i(t) - f_c = k_f m(t)
$$

where:
- $k_f$ = frequency sensitivity constant (Hz/V)
- $m(t)$ = message signal

Therefore:

$$
f_i(t) = f_c + k_f m(t)
$$

In angular frequency terms:

$$
\omega_i(t) = \omega_c + 2\pi k_f m(t)
$$

### 2.3 Deriving FM from PM

Since $\omega_i(t) = \omega_c + \frac{d\phi(t)}{dt}$, we can equate:

$$
\omega_c + \frac{d\phi(t)}{dt} = \omega_c + 2\pi k_f m(t)
$$

$$
\frac{d\phi(t)}{dt} = 2\pi k_f m(t)
$$

**Integrating both sides:**

$$
\phi(t) = 2\pi k_f \int_{-\infty}^{t} m(\tau) \, d\tau
$$

This is the **fundamental relationship**: FM is PM where the phase deviation is proportional to the **integral** of the message signal.

### 2.4 FM Signal Expression

The complete FM signal is:

$$
\boxed{s_{FM}(t) = A_c \cos\left[\omega_c t + 2\pi k_f \int_{-\infty}^{t} m(\tau) \, d\tau\right]}
$$

---

## 3. Instantaneous Frequency Analysis

### 3.1 Single-Tone Modulation

Consider a sinusoidal message signal:

$$
m(t) = A_m \cos(\omega_m t) = A_m \cos(2\pi f_m t)
$$

where:
- $A_m$ = message amplitude
- $f_m$ = message frequency (modulating frequency)

### 3.2 Frequency Deviation

The instantaneous frequency is:

$$
f_i(t) = f_c + k_f A_m \cos(2\pi f_m t)
$$

Define the **frequency deviation** as the maximum departure from the carrier frequency:

$$
\boxed{\Delta f = k_f A_m}
$$

This represents the peak frequency shift.

### 3.3 Modulation Index

The **modulation index** (or **frequency deviation ratio**) is defined as:

$$
\boxed{\beta = \frac{\Delta f}{f_m}}
$$

The modulation index $\beta$ is the key parameter that determines:
- The bandwidth of the FM signal
- Whether the FM is narrowband or wideband

### 3.4 Phase Deviation for Single-Tone FM

Substituting $m(t) = A_m \cos(\omega_m t)$ into the phase equation:

$$
\phi(t) = 2\pi k_f \int_{-\infty}^{t} A_m \cos(2\pi f_m \tau) \, d\tau
$$

$$
\phi(t) = 2\pi k_f A_m \cdot \frac{\sin(2\pi f_m t)}{2\pi f_m}
$$

$$
\phi(t) = \frac{k_f A_m}{f_m} \sin(2\pi f_m t) = \frac{\Delta f}{f_m} \sin(2\pi f_m t)
$$

$$
\boxed{\phi(t) = \beta \sin(2\pi f_m t)}
$$

Therefore, the single-tone FM signal becomes:

$$
s_{FM}(t) = A_c \cos[\omega_c t + \beta \sin(\omega_m t)]
$$

---

## 4. Spectrum Analysis Using Bessel Functions

### 4.1 Expansion Using Bessel Functions

The FM signal with single-tone modulation:

$$
s_{FM}(t) = A_c \cos[\omega_c t + \beta \sin(\omega_m t)]
$$

can be expanded using the **Jacobi-Anger identity**:

$$
\cos(\alpha + \beta \sin \theta) = \sum_{n=-\infty}^{\infty} J_n(\beta) \cos(\alpha + n\theta)
$$

where $J_n(\beta)$ is the **Bessel function of the first kind of order $n$**.

### 4.2 FM Spectrum

Applying this identity:

$$
s_{FM}(t) = A_c \sum_{n=-\infty}^{\infty} J_n(\beta) \cos[(\omega_c + n\omega_m)t]
$$

Using the property $J_{-n}(\beta) = (-1)^n J_n(\beta)$, we can rewrite:

$$
\boxed{s_{FM}(t) = A_c J_0(\beta) \cos(\omega_c t) + A_c \sum_{n=1}^{\infty} J_n(\beta) \left[\cos((\omega_c + n\omega_m)t) + (-1)^n \cos((\omega_c - n\omega_m)t)\right]}
$$

### 4.3 Spectral Components

The FM spectrum consists of:

1. **Carrier component** at $f_c$ with amplitude $A_c J_0(\beta)$
2. **Infinite sidebands** at $f_c \pm n f_m$ (where $n = 1, 2, 3, ...$) with amplitudes $A_c J_n(\beta)$

**Key observations:**

- Unlike AM, which has only 2 sidebands, FM has theoretically **infinite sidebands**
- The amplitudes are determined by Bessel function coefficients $J_n(\beta)$
- The carrier amplitude $J_0(\beta)$ can be zero for certain values of $\beta$ (carrier suppression)
- As $n$ increases, $J_n(\beta)$ decreases, making distant sidebands negligible

### 4.4 Bessel Function Properties

Important properties of $J_n(\beta)$:

1. $J_0(0) = 1$, $J_n(0) = 0$ for $n \neq 0$
2. $\sum_{n=-\infty}^{\infty} J_n^2(\beta) = 1$ (power conservation)
3. For small $\beta$: $J_0(\beta) \approx 1$, $J_1(\beta) \approx \beta/2$, $J_n(\beta) \approx 0$ for $n > 1$
4. Significant sidebands: approximately $\beta + 1$ pairs have $|J_n(\beta)| > 0.01$

### 4.5 Practical Bandwidth Consideration

Since Bessel functions decay for large $n$, we typically consider only sidebands where $|J_n(\beta)| > 0.01$ (1% of carrier amplitude).

**Rule of thumb:** Significant sidebands exist for:

$$
n \leq \beta + 1
$$

Therefore, the **approximate bandwidth** is:

$$
BW \approx 2(\beta + 1)f_m = 2\left(\frac{\Delta f}{f_m} + 1\right)f_m
$$

$$
\boxed{BW \approx 2(\Delta f + f_m)}
$$

This is **Carson's Rule**.

---

## 5. Carson's Rule Derivation

### 5.1 Power-Based Approach

The total power in an FM signal must equal the carrier power (constant envelope):

$$
P_{total} = \frac{A_c^2}{2}
$$

Using Bessel function orthogonality:

$$
P_{total} = \frac{A_c^2}{2} \sum_{n=-\infty}^{\infty} J_n^2(\beta) = \frac{A_c^2}{2}
$$

This confirms power conservation. However, in practice, we want to capture **98% of the signal power**.

### 5.2 98% Power Criterion

Carson's Rule states that the bandwidth required to capture approximately **98% of the FM signal power** is:

$$
\boxed{BW_{Carson} = 2(\Delta f + f_m)}
$$

where:
- $\Delta f$ = maximum frequency deviation
- $f_m$ = maximum modulating frequency

### 5.3 Alternative Form Using Modulation Index

Since $\beta = \Delta f / f_m$:

$$
BW_{Carson} = 2f_m(\beta + 1)
$$

### 5.4 Generalization for Complex Signals

For a general message signal with bandwidth $B$ (not just a single tone at $f_m$):

$$
\boxed{BW_{Carson} = 2(\Delta f + B)}
$$

where:
- $\Delta f$ = maximum frequency deviation
- $B$ = bandwidth of the message signal

### 5.5 Comparison with Exact Bandwidth

The **exact** FM bandwidth (using Bessel function cutoff at 1% amplitude):

$$
BW_{exact} = 2(n_{max} \cdot f_m)
$$

where $n_{max}$ is determined by $|J_n(\beta)| > 0.01$.

Carson's Rule provides a **simpler approximation**:

$$
\frac{BW_{Carson}}{BW_{exact}} \approx 1 \pm 10\%
$$

for most practical values of $\beta$.

---

## 6. Narrowband FM vs Wideband FM

### 6.1 Classification Criteria

The classification depends on the **modulation index** $\beta$:

| Type | Condition | Characteristics |
|------|-----------|----------------|
| **Narrowband FM (NBFM)** | $\beta < 0.3$ | Small frequency deviation, similar to AM |
| **Transition** | $0.3 \leq \beta \leq 1$ | Intermediate behavior |
| **Wideband FM (WBFM)** | $\beta > 1$ | Large frequency deviation, superior performance |

### 6.2 Narrowband FM (NBFM)

For $\beta \ll 1$:

**Bessel function approximations:**
- $J_0(\beta) \approx 1$
- $J_1(\beta) \approx \beta/2$
- $J_n(\beta) \approx 0$ for $n \geq 2$

**Spectrum:** Only carrier and first sideband pair are significant.

**Bandwidth:**

$$
BW_{NBFM} \approx 2f_m
$$

This is **identical to AM bandwidth**!

**Signal approximation:**

Using $\cos(\alpha + \epsilon) \approx \cos \alpha - \epsilon \sin \alpha$ for small $\epsilon$:

$$
s_{NBFM}(t) \approx A_c \cos(\omega_c t) - A_c \beta \sin(\omega_m t) \sin(\omega_c t)
$$

For $m(t) = A_m \cos(\omega_m t)$:

$$
s_{NBFM}(t) \approx A_c \cos(\omega_c t) - \frac{A_c \beta}{2}[\cos((\omega_c - \omega_m)t) - \cos((\omega_c + \omega_m)t)]
$$

This looks similar to **AM with suppressed carrier**, but with 90° phase shift in sidebands.

### 6.3 Wideband FM (WBFM)

For $\beta \gg 1$:

**Spectrum:** Many significant sideband pairs.

**Bandwidth:**

$$
BW_{WBFM} \approx 2\Delta f
$$

For large $\beta$, the $f_m$ term becomes negligible:

$$
BW_{WBFM} \approx 2\Delta f = 2\beta f_m
$$

**Advantages:**
- Better noise immunity
- Improved SNR
- Constant envelope (efficient amplification)

**Disadvantages:**
- Requires much wider bandwidth
- More complex receivers

### 6.4 Comparison Table

| Parameter | NBFM ($\beta < 0.3$) | WBFM ($\beta > 1$) |
|-----------|---------------------|-------------------|
| Bandwidth | $\approx 2f_m$ | $\approx 2\Delta f$ |
| Sidebands | 1 pair dominant | Many pairs significant |
| SNR improvement | Minimal | Proportional to $\beta^2$ |
| Complexity | Low | High |
| Applications | Mobile communications | FM radio, TV audio |

### 6.5 SNR Advantage in Wideband FM

The SNR improvement in WBFM compared to AM is:

$$
\left(\frac{SNR_{FM}}{SNR_{AM}}\right) = \frac{3\beta^2(\beta + 1)}{2}
$$

For large $\beta$:

$$
\frac{SNR_{FM}}{SNR_{AM}} \approx \frac{3\beta^3}{2}
$$

This is the **FM advantage**: trading bandwidth for SNR.

---

## 7. Comparison with AM Bandwidth

### 7.1 AM Bandwidth

For amplitude modulation with message bandwidth $B$:

$$
BW_{AM} = 2B
$$

This is the **minimum possible bandwidth** for transmitting a signal with bandwidth $B$ (Nyquist criterion).

### 7.2 FM Bandwidth

For frequency modulation with message bandwidth $B$ and maximum deviation $\Delta f$:

$$
BW_{FM} = 2(\Delta f + B)
$$

### 7.3 Bandwidth Efficiency Comparison

The **bandwidth expansion factor** for FM is:

$$
\frac{BW_{FM}}{BW_{AM}} = \frac{2(\Delta f + B)}{2B} = \frac{\Delta f}{B} + 1 = \beta + 1
$$

**Examples:**

| Application | $\beta$ | $BW_{FM}/BW_{AM}$ | Comment |
|-------------|---------|-------------------|---------|
| NBFM | 0.2 | 1.2 | Only 20% more bandwidth |
| FM Radio | 5 | 6 | 6× more bandwidth |
| TV Audio | 2.5 | 3.5 | 3.5× more bandwidth |

### 7.4 SNR vs Bandwidth Trade-off

**AM:** No SNR improvement with bandwidth increase.

**FM:** SNR improves with bandwidth (through $\beta$):

$$
SNR_{FM} \propto \beta^2 \propto \left(\frac{BW_{FM}}{BW_{AM}}\right)^2
$$

This is an example of the **bandwidth-SNR trade-off** in communications.

---

## 8. Applications

### 8.1 FM Radio Broadcasting

**Standards:**
- Carrier frequency: 88-108 MHz
- Maximum frequency deviation: $\Delta f = 75$ kHz
- Audio bandwidth: $B = 15$ kHz
- Modulation index: $\beta = 75/15 = 5$

**Bandwidth (Carson's Rule):**

$$
BW = 2(\Delta f + B) = 2(75 + 15) = 180 \text{ kHz}
$$

**Allocated bandwidth:** 200 kHz (with guard bands)

**Advantages:**
- Excellent audio quality
- Good noise immunity
- Resistant to atmospheric interference

### 8.2 Television Audio

**Standards (NTSC):**
- Maximum deviation: $\Delta f = 25$ kHz
- Audio bandwidth: $B = 10$ kHz
- Modulation index: $\beta = 2.5$

**Bandwidth:**

$$
BW = 2(25 + 10) = 70 \text{ kHz}
$$

### 8.3 Mobile Communications

**Narrowband FM (NBFM):**
- Used in two-way radio, police, emergency services
- Typical $\beta = 0.2$ to $0.5$
- Channel bandwidth: 12.5 kHz or 25 kHz
- Bandwidth efficient but lower quality

**Example (12.5 kHz channel):**
- Audio bandwidth: $B = 3$ kHz
- Carson's Rule: $BW = 2(\Delta f + 3)$
- Solving: $12.5 = 2(\Delta f + 3) \Rightarrow \Delta f = 3.25$ kHz
- Modulation index: $\beta = 3.25/3 \approx 1.08$

### 8.4 Satellite Communications

- FM used for analog satellite TV (legacy systems)
- Higher deviation ratios for better SNR
- Trade bandwidth for signal quality in noisy space environment

### 8.5 Radar Systems

- FM used in **FMCW (Frequency Modulated Continuous Wave)** radar
- Frequency linearly swept over time
- Used for measuring range and velocity
- Applications: automotive radar, altimeters

### 8.6 FM vs PM in Practice

| Application | Modulation | Reason |
|-------------|------------|--------|
| FM Radio | FM | Direct frequency control |
| Indirect FM (Armstrong) | PM + integration | Easier to generate stable FM |
| Digital FM (FSK) | FM | Simple binary frequency switching |
| Phase-locked loops | Both | FM detection and synthesis |

---

## 9. Key Takeaways and Summary

### 9.1 Fundamental Relationships

1. **FM is the derivative of PM:**
   $$
   \phi_{FM}(t) = 2\pi k_f \int m(t) \, dt
   $$

2. **Modulation index determines behavior:**
   $$
   \beta = \frac{\Delta f}{f_m}
   $$

3. **Carson's Rule for bandwidth:**
   $$
   \boxed{BW = 2(\Delta f + f_m)}
   $$

### 9.2 FM vs AM Decision Criteria

**Use FM when:**
- Noise immunity is critical
- Audio quality is important
- Bandwidth is available
- Constant envelope is advantageous (efficient power amplification)
- Examples: Broadcasting, high-quality audio

**Use AM when:**
- Bandwidth is limited
- Simple, low-cost receivers needed
- Many channels in limited spectrum
- Examples: AM radio, aircraft communications

### 9.3 Bandwidth-Performance Trade-off

$$
\text{Quality (SNR)} \propto \beta^2 \propto BW^2
$$

FM allows **exchanging bandwidth for SNR**, which AM cannot do.

### 9.4 Spectral Efficiency

**Narrowband FM:**
- Similar bandwidth to AM
- Slight improvement in noise performance
- Compromise between FM and AM

**Wideband FM:**
- Much larger bandwidth
- Significant SNR improvement
- Used when spectrum is available

---

## 10. Mathematical Summary

### Complete FM Signal Equations

1. **Time-domain (general):**
   $$
   s_{FM}(t) = A_c \cos\left[\omega_c t + 2\pi k_f \int_{-\infty}^{t} m(\tau) \, d\tau\right]
   $$

2. **Time-domain (single tone):**
   $$
   s_{FM}(t) = A_c \cos[\omega_c t + \beta \sin(\omega_m t)]
   $$

3. **Frequency-domain (Bessel expansion):**
   $$
   s_{FM}(t) = A_c \sum_{n=-\infty}^{\infty} J_n(\beta) \cos[(\omega_c + n\omega_m)t]
   $$

4. **Carson's Rule:**
   $$
   BW = 2(\Delta f + f_m) = 2f_m(\beta + 1)
   $$

5. **Modulation index:**
   $$
   \beta = \frac{\Delta f}{f_m} = \frac{k_f A_m}{f_m}
   $$

---

## References

1. Haykin, S., "Communication Systems," 5th Edition
2. Proakis, J. G., & Salehi, M., "Communication Systems Engineering"
3. Carlson, A. B., "Communication Systems"
4. Couch, L. W., "Digital and Analog Communication Systems"

---

**End of Derivation**

*This document provides a complete theoretical foundation for understanding Frequency Modulation and applying Carson's Rule in communications system design.*
