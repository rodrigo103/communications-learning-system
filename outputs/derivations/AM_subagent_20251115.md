# Amplitude Modulation (AM) - First Principles Derivation

**Date**: 2025-11-15
**Topic**: Amplitude Modulation Formula Derivation
**Level**: Fundamental Communication Systems

---

## 1. Starting Definitions

### 1.1 Message Signal (Baseband Signal)
The information-bearing signal we want to transmit:

$$m(t) = A_m \cos(2\pi f_m t)$$

Where:
- $m(t)$ = message signal (information to be transmitted)
- $A_m$ = amplitude of the message signal
- $f_m$ = frequency of the message signal (baseband frequency)
- $t$ = time variable

**Physical Meaning**: This represents the audio, data, or any low-frequency signal we wish to transmit. Typical frequencies: 20 Hz - 20 kHz for audio.

### 1.2 Carrier Signal (High-Frequency Sinusoid)
The high-frequency wave that will "carry" our message:

$$c(t) = A_c \cos(2\pi f_c t)$$

Where:
- $c(t)$ = carrier signal
- $A_c$ = amplitude of the carrier signal
- $f_c$ = carrier frequency (much higher than $f_m$)
- Typically: $f_c \gg f_m$ (carrier frequency much greater than message frequency)

**Physical Meaning**: This high-frequency wave can propagate efficiently through space as an electromagnetic wave. Typical frequencies: kHz to GHz range.

### 1.3 Amplitude Modulation Concept
**Key Idea**: We vary (modulate) the amplitude of the carrier signal in proportion to the instantaneous value of the message signal, while keeping the carrier frequency constant.

---

## 2. Mathematical Derivation Steps

### Step 1: Express the Modulation Principle
The fundamental idea of AM is to make the carrier amplitude vary with the message signal. Instead of a constant amplitude $A_c$, we want a time-varying amplitude:

$$A(t) = A_c + m(t)$$

**Why this step?** We're creating a variable amplitude that has two components:
1. A DC component ($A_c$) - the unmodulated carrier level
2. An AC component ($m(t)$) - the information signal

This ensures the carrier amplitude increases and decreases according to the message signal.

---

### Step 2: Substitute the Message Signal
Now we substitute the explicit form of $m(t)$:

$$A(t) = A_c + A_m \cos(2\pi f_m t)$$

**Why this step?** We're making the derivation concrete by using the sinusoidal message signal. This gives us an explicit mathematical expression for how the amplitude varies with time.

**Physical Interpretation**: When $\cos(2\pi f_m t) = +1$ (maximum), the amplitude is $A_c + A_m$. When $\cos(2\pi f_m t) = -1$ (minimum), the amplitude is $A_c - A_m$.

---

### Step 3: Form the Modulated Signal
The AM signal is created by multiplying this time-varying amplitude by the carrier:

$$s_{AM}(t) = A(t) \cdot \cos(2\pi f_c t)$$

$$s_{AM}(t) = [A_c + A_m \cos(2\pi f_m t)] \cos(2\pi f_c t)$$

**Why this step?** This is the mathematical implementation of "varying the carrier amplitude." We multiply the carrier by our time-varying amplitude function. This is called **linear modulation**.

---

### Step 4: Expand Using Distributive Property
Distribute the carrier cosine term:

$$s_{AM}(t) = A_c \cos(2\pi f_c t) + A_m \cos(2\pi f_m t) \cos(2\pi f_c t)$$

**Why this step?** We're separating the expression into two distinct components that have different physical meanings:
- **First term**: The unmodulated carrier
- **Second term**: The product of message and carrier (the actual modulation term)

---

### Step 5: Apply Trigonometric Product-to-Sum Identity
Use the identity: $\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$

For our second term where $A = 2\pi f_m t$ and $B = 2\pi f_c t$:

$$\cos(2\pi f_m t) \cos(2\pi f_c t) = \frac{1}{2}[\cos(2\pi(f_c - f_m)t) + \cos(2\pi(f_c + f_m)t)]$$

**Why this step?** This trigonometric identity reveals the **frequency translation** property of modulation. The multiplication of two sinusoids creates new frequencies that are the sum and difference of the original frequencies.

---

### Step 6: Substitute Back into the AM Signal
$$s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{A_m}{2}\cos(2\pi(f_c - f_m)t) + \frac{A_m}{2}\cos(2\pi(f_c + f_m)t)$$

**Why this step?** This is the **spectral representation** of the AM signal. It shows explicitly that our signal now contains three distinct frequency components:
1. **Carrier**: at frequency $f_c$ with amplitude $A_c$
2. **Lower Sideband (LSB)**: at frequency $(f_c - f_m)$ with amplitude $\frac{A_m}{2}$
3. **Upper Sideband (USB)**: at frequency $(f_c + f_m)$ with amplitude $\frac{A_m}{2}$

---

### Step 7: Introduce the Modulation Index
Define the **modulation index** (or modulation depth):

$$\mu = \frac{A_m}{A_c}$$

This represents the extent of modulation. Substituting $A_m = \mu A_c$:

$$s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{\mu A_c}{2}\cos(2\pi(f_c - f_m)t) + \frac{\mu A_c}{2}\cos(2\pi(f_c + f_m)t)$$

Factor out $A_c$:

$$s_{AM}(t) = A_c \left[\cos(2\pi f_c t) + \frac{\mu}{2}\cos(2\pi(f_c - f_m)t) + \frac{\mu}{2}\cos(2\pi(f_c + f_m)t)\right]$$

**Why this step?** The modulation index $\mu$ is a **normalized measure** of how much the carrier amplitude varies relative to its unmodulated value. This makes it easier to analyze system performance and ensure we don't over-modulate.

---

### Step 8: Alternative Compact Form
We can also write the AM signal in its most common compact form:

$$s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)]\cos(2\pi f_c t)$$

**Why this step?** This form clearly shows the amplitude modulation structure:
- The term $[1 + \mu \cos(2\pi f_m t)]$ is the **envelope** of the carrier
- The envelope varies between $(1-\mu)$ and $(1+\mu)$
- This form is most useful for understanding envelope detection

---

## 3. Final Formula with Variable Definitions

### Standard AM Signal (Time Domain)

#### Compact Form:
$$\boxed{s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)]\cos(2\pi f_c t)}$$

#### Expanded Form:
$$\boxed{s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{\mu A_c}{2}\cos(2\pi(f_c - f_m)t) + \frac{\mu A_c}{2}\cos(2\pi(f_c + f_m)t)}$$

### Variable Definitions

| Symbol | Description | Units | Typical Range |
|--------|-------------|-------|---------------|
| $s_{AM}(t)$ | Amplitude-modulated signal | Volts | - |
| $A_c$ | Carrier amplitude | Volts | > 0 |
| $A_m$ | Message signal amplitude | Volts | > 0 |
| $\mu$ | Modulation index ($= A_m/A_c$) | Dimensionless | 0 to 1 |
| $f_c$ | Carrier frequency | Hz | kHz to GHz |
| $f_m$ | Message frequency | Hz | Hz to kHz |
| $t$ | Time | seconds | - |

### Modulation Index Constraints

$$0 \leq \mu \leq 1$$

- **$\mu = 0$**: No modulation (pure carrier)
- **$0 < \mu < 1$**: Under-modulation (safe, no distortion)
- **$\mu = 1$**: 100% modulation (maximum efficient modulation)
- **$\mu > 1$**: Over-modulation (causes distortion and splatter)

When $\mu = 1$, the envelope reaches zero at its minimum, and the signal varies from 0 to $2A_c$.

---

## 4. Key Insights About Bandwidth and Power

### 4.1 Bandwidth Analysis

**Occupied Bandwidth**:
$$B_{AM} = 2f_m$$

For a complex message signal with maximum frequency $f_{m,max}$:
$$B_{AM} = 2f_{m,max}$$

**Insight**: The AM signal occupies twice the bandwidth of the message signal. This is because we have two sidebands (USB and LSB), each spanning the same frequency range as the message.

**Frequency Spectrum**:
```
           LSB      Carrier      USB
            |          |          |
     -------•----------•----------•-------
            |          |          |
       fc - fm       fc       fc + fm

  Amplitude: Am/2     Ac        Am/2
```

**Key Point**: Both sidebands contain the complete message information (they are mirror images). This redundancy is inefficient but simplifies receiver design.

---

### 4.2 Power Analysis

#### Carrier Power:
$$P_c = \frac{A_c^2}{2R}$$

Where $R$ is the load resistance (often normalized to 1Ω).

#### Each Sideband Power:
$$P_{USB} = P_{LSB} = \frac{(\mu A_c/2)^2}{2R} = \frac{\mu^2 A_c^2}{8R}$$

#### Total Sideband Power:
$$P_{sidebands} = P_{USB} + P_{LSB} = \frac{\mu^2 A_c^2}{4R} = \frac{\mu^2}{2} \cdot P_c$$

#### Total AM Signal Power:
$$P_{total} = P_c + P_{sidebands} = \frac{A_c^2}{2R}\left(1 + \frac{\mu^2}{2}\right)$$

$$\boxed{P_{total} = P_c\left(1 + \frac{\mu^2}{2}\right)}$$

---

### 4.3 Efficiency Analysis

**Power Efficiency** is the ratio of power in sidebands (information) to total power:

$$\eta = \frac{P_{sidebands}}{P_{total}} = \frac{\mu^2/2}{1 + \mu^2/2} = \frac{\mu^2}{2 + \mu^2}$$

**For maximum modulation** ($\mu = 1$):
$$\eta_{max} = \frac{1}{3} = 33.33\%$$

**Critical Insight**: Even at 100% modulation, only 33.33% of the transmitted power carries information! The remaining 66.67% is in the carrier, which carries no information but is necessary for simple envelope detection at the receiver.

**Efficiency Values**:
| $\mu$ | Efficiency $\eta$ | Information Power |
|-------|-------------------|-------------------|
| 0.5   | 11.1%            | Very inefficient  |
| 0.7   | 17.0%            | Typical speech    |
| 1.0   | 33.3%            | Maximum possible  |

**This inefficiency motivated the development of**:
- **DSB-SC** (Double Sideband Suppressed Carrier): Remove the carrier
- **SSB** (Single Sideband): Transmit only one sideband
- **VSB** (Vestigial Sideband): Transmit one sideband plus a trace of the other

---

## 5. Physical Interpretation

### 5.1 Time Domain Interpretation

**Envelope Behavior**:
- The **envelope** of the AM signal is $A_c[1 + \mu \cos(2\pi f_m t)]$
- This envelope varies at the message frequency $f_m$
- The carrier oscillates rapidly at $f_c$ within this envelope

**Visual Analogy**: Imagine a high-frequency rope wave (carrier) whose amplitude slowly increases and decreases (message). The "outline" of the peaks follows the message signal.

**Envelope Detection**: A simple diode-capacitor circuit can extract the envelope directly, recovering the message signal. This is why AM radio receivers can be very simple (crystal radio).

---

### 5.2 Frequency Domain Interpretation

**Spectrum Components**:

1. **Carrier at $f_c$**:
   - Always present regardless of message content
   - Acts as a reference for demodulation
   - Contains no information itself

2. **Lower Sideband (LSB) at $f_c - f_m$**:
   - Contains the complete message information
   - Frequency components are inverted (mirrored)

3. **Upper Sideband (USB) at $f_c + f_m$**:
   - Contains the complete message information
   - Frequency components are in normal order
   - Identical information to LSB (redundant)

**Why Two Sidebands?** This is a fundamental property of multiplying two real sinusoids. The product creates both sum and difference frequencies (heterodyning principle).

---

### 5.3 Practical Interpretation

**Generation**:
- AM can be generated by a nonlinear device (e.g., transistor in active region) or by a **multiplier circuit**
- Simple to implement with analog circuits
- Can use high-level modulation (modulate the final amplifier)

**Detection**:
- **Envelope Detector**: Simple diode + capacitor + load resistor
- No frequency/phase synchronization needed (unlike DSB-SC)
- Trade-off: Simplicity vs. power efficiency

**Applications**:
- **AM Broadcasting**: 535-1605 kHz (medium wave)
- **Aviation Communication**: 118-137 MHz
- **Citizens Band (CB) Radio**: 27 MHz
- **Historical**: First practical radio system (still used today)

**Advantages**:
- Simple, inexpensive receivers
- Robust to frequency drift
- Well-established technology

**Disadvantages**:
- Poor power efficiency (max 33.3%)
- Susceptible to noise and interference
- Wastes bandwidth (transmits redundant information)
- Fading affects carrier and sidebands differently

---

## 6. Mathematical Summary

### Key Equations

1. **Time Domain (Compact)**:
   $$s_{AM}(t) = A_c[1 + \mu \cos(2\pi f_m t)]\cos(2\pi f_c t)$$

2. **Time Domain (Expanded)**:
   $$s_{AM}(t) = A_c \cos(2\pi f_c t) + \frac{\mu A_c}{2}\cos(2\pi(f_c - f_m)t) + \frac{\mu A_c}{2}\cos(2\pi(f_c + f_m)t)$$

3. **Modulation Index**:
   $$\mu = \frac{A_m}{A_c}, \quad 0 \leq \mu \leq 1$$

4. **Bandwidth**:
   $$B_{AM} = 2f_m$$

5. **Total Power**:
   $$P_{total} = P_c\left(1 + \frac{\mu^2}{2}\right)$$

6. **Efficiency**:
   $$\eta = \frac{\mu^2}{2 + \mu^2}, \quad \eta_{max} = \frac{1}{3} \text{ at } \mu = 1$$

---

## 7. Connection to Fourier Analysis

The AM derivation illustrates the **frequency translation property** of modulation:

$$m(t) \cos(2\pi f_c t) \xrightarrow{\mathcal{F}} \frac{1}{2}[M(f - f_c) + M(f + f_c)]$$

Where $M(f)$ is the Fourier transform of $m(t)$.

**Interpretation**: Multiplication by a cosine in the time domain corresponds to shifting and scaling the spectrum in the frequency domain. This is the fundamental principle behind **heterodyning** and all frequency translation operations in communications.

---

## Conclusion

Amplitude Modulation represents the most straightforward implementation of analog modulation. While inefficient in terms of power and bandwidth, its simplicity in both generation and detection made it the foundation of early radio communication and it continues to be used in specific applications where receiver simplicity is paramount.

The mathematical derivation shows how a simple product of two sinusoids creates a frequency translation mechanism, which is the basis for all modern communication systems.

---

**Derivation completed on**: 2025-11-15
**Mathematical rigor**: First principles
**Pedagogical level**: Undergraduate Communications Systems
