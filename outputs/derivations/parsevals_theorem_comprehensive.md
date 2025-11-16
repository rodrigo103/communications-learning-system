# Parseval's Theorem: A Comprehensive Mathematical Treatment

## 1. Introduction and Motivation

Parseval's theorem is one of the most profound results in signal analysis, establishing that the total energy of a signal is preserved under the Fourier transform. This principle has deep implications for communications systems, where we often analyze signals in both time and frequency domains.

## 2. Statement of the Theorem

### 2.1 Continuous-Time Parseval's Theorem

For a signal x(t) with Fourier transform X(f), Parseval's theorem states:

$$\boxed{\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df}$$

**Alternative form using angular frequency ω = 2πf:**

$$\int_{-\infty}^{\infty} |x(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} |X(\omega)|^2 d\omega$$

### 2.2 Discrete-Time Parseval's Theorem

For a discrete sequence x[n] with Discrete-Time Fourier Transform (DTFT) X(e^(jω)):

$$\boxed{\sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega}$$

### 2.3 Generalized Form (Plancherel's Theorem)

For two signals x(t) and y(t) with Fourier transforms X(f) and Y(f):

$$\int_{-\infty}^{\infty} x(t)y^*(t) dt = \int_{-\infty}^{\infty} X(f)Y^*(f) df$$

where * denotes complex conjugation.

## 3. Physical Interpretation

### 3.1 Energy Conservation Principle

Parseval's theorem states that **the total energy of a signal is the same whether computed in the time domain or the frequency domain**. This is a manifestation of energy conservation under linear transformations.

- **Left side**: ∫|x(t)|²dt represents the total energy in the time domain
- **Right side**: ∫|X(f)|²df represents the total energy in the frequency domain
- |X(f)|² is called the **energy spectral density** (ESD)

### 3.2 Power Distribution Insight

The theorem tells us that |X(f)|²df represents the energy contained in the frequency band [f, f+df]. This allows us to:
- Determine which frequencies carry the most energy
- Design filters to preserve or remove specific energy components
- Analyze bandwidth-energy tradeoffs in communications

### 3.3 Communications Significance

In communications systems, Parseval's theorem enables:
1. **SNR Analysis**: Computing signal and noise power in either domain
2. **Bandwidth Determination**: Finding the frequency range containing most signal energy
3. **Filter Design**: Predicting energy loss from filtering operations
4. **Modulation Analysis**: Understanding energy distribution in modulated signals

## 4. Rigorous Derivation from First Principles

### 4.1 Prerequisites and Definitions

**Fourier Transform Pair:**
$$X(f) = \int_{-\infty}^{\infty} x(t)e^{-j2\pi ft} dt \quad \text{(Forward Transform)}$$

$$x(t) = \int_{-\infty}^{\infty} X(f)e^{j2\pi ft} df \quad \text{(Inverse Transform)}$$

**Energy of a signal:**
$$E = \int_{-\infty}^{\infty} |x(t)|^2 dt$$

### 4.2 Step-by-Step Derivation

**Step 1: Start with the energy integral**

$$E = \int_{-\infty}^{\infty} |x(t)|^2 dt$$

For complex signals, |x(t)|² = x(t)x*(t), so:

$$E = \int_{-\infty}^{\infty} x(t)x^*(t) dt$$

**Step 2: Express x*(t) using the inverse Fourier transform**

Since x(t) = ∫X(f)e^(j2πft)df, we have:

$$x^*(t) = \left[\int_{-\infty}^{\infty} X(f)e^{j2\pi ft} df\right]^*$$

Using the property that [∫f(x)dx]* = ∫f*(x)dx for real integration variables:

$$x^*(t) = \int_{-\infty}^{\infty} X^*(f)e^{-j2\pi ft} df$$

**Step 3: Substitute into the energy integral**

$$E = \int_{-\infty}^{\infty} x(t)\left[\int_{-\infty}^{\infty} X^*(f)e^{-j2\pi ft} df\right] dt$$

**Step 4: Exchange order of integration**

Assuming absolute integrability (Fubini's theorem applies):

$$E = \int_{-\infty}^{\infty} X^*(f)\left[\int_{-\infty}^{\infty} x(t)e^{-j2\pi ft} dt\right] df$$

**Step 5: Recognize the inner integral as X(f)**

The inner integral is exactly the Fourier transform of x(t):

$$E = \int_{-\infty}^{\infty} X^*(f)X(f) df$$

**Step 6: Simplify using |X(f)|² = X(f)X*(f)**

$$E = \int_{-\infty}^{\infty} |X(f)|^2 df$$

**Therefore:**

$$\boxed{\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df}$$

### 4.3 Verification of Mathematical Validity

**Conditions for validity:**
1. x(t) must be square-integrable: ∫|x(t)|²dt < ∞
2. X(f) exists and is square-integrable
3. The interchange of integration order must be valid (satisfied for L² functions)

**Dimensional Analysis:**
- Left side: [signal²][time] = [energy]
- Right side: [transform²][frequency] = [signal²·time²][1/time] = [energy]
✓ Dimensions match

## 5. Discrete-Time Derivation

### 5.1 DTFT Definition

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}$$

$$x[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi} X(e^{j\omega})e^{j\omega n} d\omega$$

### 5.2 Derivation

**Step 1: Start with discrete energy**

$$E = \sum_{n=-\infty}^{\infty} |x[n]|^2 = \sum_{n=-\infty}^{\infty} x[n]x^*[n]$$

**Step 2: Express x*[n] using inverse DTFT**

$$x^*[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi} X^*(e^{j\omega})e^{-j\omega n} d\omega$$

**Step 3: Substitute and rearrange**

$$E = \sum_{n=-\infty}^{\infty} x[n]\left[\frac{1}{2\pi}\int_{-\pi}^{\pi} X^*(e^{j\omega})e^{-j\omega n} d\omega\right]$$

$$E = \frac{1}{2\pi}\int_{-\pi}^{\pi} X^*(e^{j\omega})\left[\sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}\right] d\omega$$

**Step 4: Recognize the sum as X(e^(jω))**

$$E = \frac{1}{2\pi}\int_{-\pi}^{\pi} X^*(e^{j\omega})X(e^{j\omega}) d\omega$$

$$\boxed{E = \frac{1}{2\pi}\int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega}$$

## 6. Practical Applications in Communications

### 6.1 Application 1: Bandwidth Calculation

**Problem:** Find the 95% energy bandwidth of a signal.

**Solution using Parseval:**
1. Compute total energy: E_total = ∫|X(f)|²df
2. Find bandwidth B such that: ∫_{-B}^{B}|X(f)|²df = 0.95·E_total

### 6.2 Application 2: SNR in Matched Filtering

For a signal s(t) in white noise with PSD N₀/2:

**Signal Energy:**
$$E_s = \int_{-\infty}^{\infty} |s(t)|^2 dt = \int_{-\infty}^{\infty} |S(f)|^2 df$$

**Matched filter output SNR:**
$$\text{SNR} = \frac{2E_s}{N_0}$$

Parseval's theorem allows us to compute E_s in whichever domain is more convenient.

### 6.3 Application 3: Power Spectral Density for Random Processes

For a wide-sense stationary random process with autocorrelation R_x(τ):

**Wiener-Khinchin Theorem (uses Parseval):**
$$S_x(f) = \mathcal{F}\{R_x(\tau)\}$$

**Average Power:**
$$P = R_x(0) = \int_{-\infty}^{\infty} S_x(f) df$$

This is Parseval's theorem applied to random processes.

### 6.4 Application 4: Amplitude Modulation Analysis

For AM signal x(t) = m(t)cos(2πf_c t):

**Time domain energy:**
$$E_{time} = \int_{-\infty}^{\infty} |m(t)|^2\cos^2(2\pi f_c t) dt$$

**Frequency domain (using Parseval):**
$$E_{freq} = \frac{1}{4}\int_{-\infty}^{\infty} |M(f-f_c)|^2 + |M(f+f_c)|^2 df$$

Both give the same result, but frequency domain often simplifies calculation.

## 7. Numerical Example

### Example: Rectangular Pulse

Consider a rectangular pulse:
$$x(t) = \begin{cases}
A & |t| \leq T/2 \\
0 & |t| > T/2
\end{cases}$$

**Time Domain Energy:**
$$E_{time} = \int_{-T/2}^{T/2} A^2 dt = A^2T$$

**Fourier Transform:**
$$X(f) = AT\text{sinc}(fT) = AT\frac{\sin(\pi fT)}{\pi fT}$$

**Frequency Domain Energy:**
$$E_{freq} = \int_{-\infty}^{\infty} |AT\text{sinc}(fT)|^2 df$$

Using the property ∫sinc²(x)dx = 1:
$$E_{freq} = A^2T^2 \cdot \frac{1}{T} = A^2T$$

**Verification:** E_time = E_freq = A²T ✓

## 8. Extensions and Related Results

### 8.1 Parseval for Fourier Series

For periodic signal with period T₀ and Fourier coefficients c_n:

$$\frac{1}{T_0}\int_{0}^{T_0} |x(t)|^2 dt = \sum_{n=-\infty}^{\infty} |c_n|^2$$

### 8.2 Parseval for Discrete Fourier Transform (DFT)

For N-point DFT:

$$\sum_{n=0}^{N-1} |x[n]|^2 = \frac{1}{N}\sum_{k=0}^{N-1} |X[k]|^2$$

### 8.3 Uncertainty Principle Connection

Parseval's theorem is related to the time-frequency uncertainty principle:

$$\Delta t \cdot \Delta f \geq \frac{1}{4\pi}$$

Both stem from the fundamental properties of the Fourier transform.

## 9. Common Pitfalls and Clarifications

### 9.1 Power vs. Energy Signals

- **Energy signals:** Parseval applies directly (finite energy)
- **Power signals:** Use Parseval on windowed segments, then average

### 9.2 Normalization Constants

Different Fourier transform conventions affect the constant:
- Using ω: factor of 1/(2π)
- Using f: no additional factor
- Always verify your convention!

### 9.3 Real vs. Complex Signals

For real signals x(t):
- X(f) has Hermitian symmetry: X(-f) = X*(f)
- Energy integral can be simplified: E = 2∫₀^∞|X(f)|²df

## 10. Summary and Key Insights

**Parseval's theorem establishes that:**

1. **Energy is conserved** under the Fourier transform
2. **Time and frequency domains** provide equivalent energy information
3. **Signal processing operations** can be analyzed in either domain
4. **Bandwidth-time tradeoffs** are fundamentally constrained

**Physical Significance:**
- No information is lost in the Fourier transform
- Energy cannot be created or destroyed by linear filtering
- Spectral analysis provides complete signal characterization

**Mathematical Beauty:**
- Connects L² norm preservation to unitary transformations
- Generalizes to other orthogonal transforms (wavelets, etc.)
- Forms basis for spectral methods in PDEs and quantum mechanics

This theorem is not just a mathematical curiosity but a fundamental principle that underlies much of modern signal processing and communications theory.