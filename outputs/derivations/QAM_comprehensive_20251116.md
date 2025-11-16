# Quadrature Amplitude Modulation (QAM) - Complete Derivation

**Date**: 2024-11-16
**Level**: Comprehensive (Undergraduate to Advanced)
**For**: Communications Systems Course

---

## 1. Introduction & Motivation

Quadrature Amplitude Modulation (QAM) is a fundamental modulation scheme that enables efficient transmission of digital data by modulating both amplitude and phase of a carrier signal. QAM forms the backbone of modern communication systems including:

- Digital television broadcasting (DVB)
- Cable modems (DOCSIS)
- WiFi standards (802.11)
- 4G/5G cellular networks
- Satellite communications

The key insight of QAM is that we can transmit two independent data streams on the same carrier frequency by exploiting orthogonality between sine and cosine components.

---

## 2. Prerequisites

**Mathematical background needed:**
- Fourier transform and its properties
- Complex number representation
- Orthogonality of functions
- Signal space concepts
- Basic probability theory

**Prior results assumed:**
- Euler's formula: $e^{j\theta} = \cos(\theta) + j\sin(\theta)$
- Orthogonality: $\int_{-\infty}^{\infty} \cos(\omega t)\sin(\omega t)dt = 0$
- Energy of sinusoids over integer periods
- Matched filter theory

---

## 3. Starting Definitions

### 3.1 Orthogonal Basis Functions

Define two orthonormal basis functions:

$$\phi_1(t) = \sqrt{\frac{2}{T_s}}\cos(2\pi f_c t) \quad \text{for } 0 \leq t \leq T_s \tag{1}$$

$$\phi_2(t) = -\sqrt{\frac{2}{T_s}}\sin(2\pi f_c t) \quad \text{for } 0 \leq t \leq T_s \tag{2}$$

**Where:**
- $f_c$ = carrier frequency [Hz]
- $T_s$ = symbol duration [seconds]
- The factor $\sqrt{2/T_s}$ normalizes energy to unity

**Physical meaning**: These functions form an orthonormal basis for the signal space, allowing independent modulation of two dimensions.

### 3.2 Orthogonality Verification

Verify orthogonality:

$$\int_0^{T_s} \phi_1(t)\phi_2(t)dt = -\frac{2}{T_s}\int_0^{T_s} \cos(2\pi f_c t)\sin(2\pi f_c t)dt \tag{3}$$

Using the identity $\sin(x)\cos(x) = \frac{1}{2}\sin(2x)$:

$$= -\frac{1}{T_s}\int_0^{T_s} \sin(4\pi f_c t)dt = -\frac{1}{T_s} \cdot \left[-\frac{1}{4\pi f_c}\cos(4\pi f_c t)\right]_0^{T_s} \tag{4}$$

For integer number of carrier cycles ($f_c T_s = n$, where $n$ is an integer):

$$= -\frac{1}{4\pi f_c T_s}[\cos(4\pi n) - \cos(0)] = 0 \tag{5}$$

### 3.3 Energy Normalization

Verify unit energy:

$$\int_0^{T_s} \phi_1^2(t)dt = \frac{2}{T_s}\int_0^{T_s} \cos^2(2\pi f_c t)dt \tag{6}$$

Using $\cos^2(x) = \frac{1}{2}[1 + \cos(2x)]$:

$$= \frac{2}{T_s} \cdot \frac{T_s}{2} = 1 \tag{7}$$

Similarly, $\int_0^{T_s} \phi_2^2(t)dt = 1$

---

## 4. Assumptions

We assume the following throughout this derivation:

1. **Carrier frequency assumption**: $f_c T_s = n$ (integer number of carrier cycles per symbol)
   - Ensures orthogonality between I and Q channels
   - Typically $f_c >> 1/T_s$ in practice

2. **Perfect synchronization**: Transmitter and receiver have perfect carrier and timing synchronization
   - Required for coherent demodulation
   - Practical systems use pilot signals or training sequences

3. **Ideal channel**: Initially assume no noise or distortion
   - Will add AWGN analysis later
   - Real channels require equalization

4. **Band-limited signals**: Message signals are band-limited to $B < f_c$
   - Prevents aliasing
   - Enables narrowband approximation

---

## 5. Step-by-Step Derivation

### Step 1: Signal Space Representation

In M-ary QAM, we transmit one of M possible signal vectors. Each signal can be represented as:

$$s_i(t) = a_i \phi_1(t) + b_i \phi_2(t) \quad \text{for } i = 1, 2, ..., M \tag{8}$$

**Where:**
- $a_i$ = in-phase (I) component amplitude
- $b_i$ = quadrature (Q) component amplitude
- $(a_i, b_i)$ = constellation point coordinates

**Justification**: Any bandpass signal can be represented as a linear combination of orthonormal basis functions (signal space theorem).

### Step 2: Expansion to Standard Form

Substituting the basis functions:

$$s_i(t) = a_i\sqrt{\frac{2}{T_s}}\cos(2\pi f_c t) - b_i\sqrt{\frac{2}{T_s}}\sin(2\pi f_c t) \tag{9}$$

Factor out common terms:

$$s_i(t) = \sqrt{\frac{2}{T_s}}[a_i\cos(2\pi f_c t) - b_i\sin(2\pi f_c t)] \tag{10}$$

### Step 3: Complex Baseband Representation

Define the complex baseband signal:

$$\tilde{s}_i = a_i + jb_i \tag{11}$$

The modulated signal can be written using complex notation:

$$s_i(t) = \sqrt{\frac{2}{T_s}}\text{Re}[\tilde{s}_i e^{j2\pi f_c t}] \tag{12}$$

**Physical interpretation**: The complex baseband signal $\tilde{s}_i$ contains all information about the modulation, while $e^{j2\pi f_c t}$ performs the frequency translation to the carrier.

### Step 4: General QAM Signal

For a sequence of symbols, the QAM signal becomes:

$$s(t) = \sum_{n=-\infty}^{\infty} [I_n \cos(2\pi f_c t) - Q_n \sin(2\pi f_c t)]p(t - nT_s) \tag{13}$$

**Where:**
- $I_n$ = n-th in-phase symbol amplitude
- $Q_n$ = n-th quadrature symbol amplitude
- $p(t)$ = pulse shaping function (rectangular, raised cosine, etc.)

### Step 5: Alternative Amplitude-Phase Form

We can express QAM in polar form:

$$s_i(t) = A_i\cos(2\pi f_c t + \theta_i) \tag{14}$$

**Where:**
- $A_i = \sqrt{a_i^2 + b_i^2}$ = amplitude
- $\theta_i = \arctan(b_i/a_i)$ = phase

**Derivation**: Starting from equation (10):

$$s_i(t) = \sqrt{\frac{2}{T_s}}[a_i\cos(2\pi f_c t) - b_i\sin(2\pi f_c t)] \tag{15}$$

Define $A_i = \sqrt{a_i^2 + b_i^2}$ and factor:

$$s_i(t) = \sqrt{\frac{2}{T_s}}A_i\left[\frac{a_i}{A_i}\cos(2\pi f_c t) - \frac{b_i}{A_i}\sin(2\pi f_c t)\right] \tag{16}$$

Let $\cos(\theta_i) = a_i/A_i$ and $\sin(\theta_i) = b_i/A_i$:

$$s_i(t) = \sqrt{\frac{2}{T_s}}A_i[\cos(\theta_i)\cos(2\pi f_c t) - \sin(\theta_i)\sin(2\pi f_c t)] \tag{17}$$

Using the cosine addition formula:

$$s_i(t) = \sqrt{\frac{2}{T_s}}A_i\cos(2\pi f_c t + \theta_i) \tag{18}$$

---

## 6. Constellation Diagrams

### 6.1 Square QAM Constellations

For M-ary QAM where $M = 2^{2k}$ (square constellations):

$$a_i, b_i \in \{-(2m-1)d, -(2m-3)d, ..., -d, d, ..., (2m-3)d, (2m-1)d\} \tag{19}$$

**Where:**
- $m = \sqrt{M}/2$
- $d$ = minimum distance between constellation points
- Total points: $\sqrt{M} \times \sqrt{M} = M$

### 6.2 Average Symbol Energy

For square M-QAM with unit minimum distance ($d = 1$):

$$E_s = \frac{1}{M}\sum_{i=1}^{M}(a_i^2 + b_i^2) \tag{20}$$

For equally probable symbols:

$$E_s = 2 \cdot \frac{1}{\sqrt{M}}\sum_{k=1}^{\sqrt{M}}(2k-1)^2 = \frac{2(M-1)}{3} \tag{21}$$

**Key results for common constellations:**
- 4-QAM (QPSK): $E_s = 2$
- 16-QAM: $E_s = 10$
- 64-QAM: $E_s = 42$
- 256-QAM: $E_s = 170$

### 6.3 Minimum Distance

The minimum Euclidean distance between constellation points:

$$d_{min} = 2d = 2\sqrt{\frac{3E_s}{2(M-1)}} \tag{22}$$

This determines the noise immunity of the modulation scheme.

---

## 7. Bandwidth Efficiency and Spectral Properties

### 7.1 Spectrum of QAM Signal

The power spectral density of the QAM signal:

$$S_{QAM}(f) = \frac{1}{T_s}|P(f)|^2[S_I(f-f_c) + S_Q(f-f_c)] \tag{23}$$

**Where:**
- $P(f)$ = Fourier transform of pulse shape $p(t)$
- $S_I(f)$, $S_Q(f)$ = power spectral densities of I and Q data streams

For rectangular pulses and random data:

$$S_{QAM}(f) = \frac{E_s}{T_s}\text{sinc}^2[(f-f_c)T_s] + \frac{E_s}{T_s}\text{sinc}^2[(f+f_c)T_s] \tag{24}$$

### 7.2 Bandwidth Requirements

**Null-to-null bandwidth** (rectangular pulses):
$$B_{null} = \frac{2}{T_s} = 2R_s \tag{25}$$

**Where:** $R_s = 1/T_s$ = symbol rate

**99% power bandwidth** (raised cosine pulses):
$$B_{99\%} = (1 + \alpha)R_s \tag{26}$$

**Where:** $\alpha$ = roll-off factor (0 ≤ α ≤ 1)

### 7.3 Spectral Efficiency

For M-ary QAM, each symbol carries $\log_2(M)$ bits:

$$\eta = \frac{R_b}{B} = \frac{\log_2(M) \cdot R_s}{B} \tag{27}$$

For ideal Nyquist pulses ($B = R_s$):

$$\eta_{max} = \log_2(M) \text{ bits/s/Hz} \tag{28}$$

**Examples:**
- 4-QAM: 2 bits/s/Hz
- 16-QAM: 4 bits/s/Hz
- 64-QAM: 6 bits/s/Hz
- 256-QAM: 8 bits/s/Hz

---

## 8. Power Distribution and Efficiency

### 8.1 Peak-to-Average Power Ratio (PAPR)

For M-QAM, the PAPR is:

$$\text{PAPR} = \frac{P_{peak}}{P_{avg}} = \frac{(\sqrt{M}-1)^2}{(M-1)/3} \tag{29}$$

Simplifying:

$$\text{PAPR} = \frac{3(\sqrt{M}-1)^2}{M-1} = \frac{3(\sqrt{M}-1)}{(\sqrt{M}+1)} \tag{30}$$

**Values for common constellations:**
- 4-QAM: PAPR = 1 (constant envelope)
- 16-QAM: PAPR = 1.8
- 64-QAM: PAPR = 2.33
- 256-QAM: PAPR = 2.6

### 8.2 Power Efficiency

The average transmitted power:

$$P_{avg} = \frac{E_s}{T_s} = \frac{2(M-1)d^2}{3T_s} \tag{31}$$

For a given bit error rate requirement, the required $E_b/N_0$:

$$\frac{E_b}{N_0} = \frac{E_s}{N_0 \log_2(M)} = \frac{(M-1)}{3\log_2(M)} \cdot \frac{d^2}{N_0/2} \tag{32}$$

---

## 9. Demodulation and Detection

### 9.1 Coherent Demodulation

The received signal in AWGN:

$$r(t) = s(t) + n(t) \tag{33}$$

Correlate with basis functions:

$$r_I = \int_0^{T_s} r(t)\phi_1(t)dt = a_i + n_I \tag{34}$$

$$r_Q = \int_0^{T_s} r(t)\phi_2(t)dt = b_i + n_Q \tag{35}$$

**Where:** $n_I$, $n_Q$ are independent Gaussian noise components with variance $\sigma^2 = N_0/2$

### 9.2 Maximum Likelihood Detection

The ML decision rule:

$$\hat{s}_i = \arg\min_{s_i} ||r - s_i||^2 = \arg\min_{s_i} [(r_I - a_i)^2 + (r_Q - b_i)^2] \tag{36}$$

This corresponds to choosing the nearest constellation point in Euclidean distance.

### 9.3 Symbol Error Probability

For high SNR, the symbol error probability:

$$P_s \approx 4\left(1 - \frac{1}{\sqrt{M}}\right)Q\left(\sqrt{\frac{3\log_2(M) \cdot E_b}{(M-1)N_0}}\right) \tag{37}$$

**Where:** $Q(x) = \frac{1}{\sqrt{2\pi}}\int_x^{\infty} e^{-t^2/2}dt$ is the Q-function

For Gray coding, the bit error probability:

$$P_b \approx \frac{P_s}{\log_2(M)} \tag{38}$$

---

## 10. Final Result

$$\boxed{s_{QAM}(t) = \sum_{n=-\infty}^{\infty} [I_n \cos(2\pi f_c t) - Q_n \sin(2\pi f_c t)]p(t - nT_s)}$$

**Where:**
- $I_n$ = in-phase component of n-th symbol ∈ $\{±d, ±3d, ..., ±(\sqrt{M}-1)d\}$
- $Q_n$ = quadrature component of n-th symbol ∈ $\{±d, ±3d, ..., ±(\sqrt{M}-1)d\}$
- $f_c$ = carrier frequency [Hz]
- $T_s$ = symbol duration [seconds]
- $p(t)$ = pulse shaping function
- $M$ = constellation size (number of symbols)
- $d$ = half the minimum distance between constellation points

**Valid when:**
- Carrier frequency satisfies: $f_c >> 1/T_s$ (narrowband condition)
- Integer carrier cycles per symbol: $f_c T_s = n$ (for perfect orthogonality)
- Channel bandwidth ≥ $(1+\alpha)/T_s$ Hz (for raised cosine pulses)
- Coherent demodulation with carrier/timing synchronization

---

## 11. Validation

### 11.1 Dimensional Analysis

Check units of modulated signal:
- $I_n$, $Q_n$: dimensionless (normalized amplitudes)
- $\cos(2\pi f_c t)$: dimensionless
- $p(t)$: has units of $1/\sqrt{\text{time}}$ for unit energy
- Result: $s(t)$ has units of $1/\sqrt{\text{time}}$ ✓

### 11.2 Limiting Cases

**Case 1: M = 4 (QPSK)**
- Constellation points: $(±1, ±1)$
- Constant envelope: $A_i = \sqrt{2}$ for all symbols
- Reduces to QPSK with phase shifts of ±45°, ±135° ✓

**Case 2: Q_n = 0 for all n**
- Reduces to: $s(t) = \sum_n I_n \cos(2\pi f_c t)p(t - nT_s)$
- This is Pulse Amplitude Modulation (PAM) on carrier ✓

**Case 3: Binary case (M = 2)**
- Only two points: typically $(±1, 0)$
- Reduces to BPSK ✓

### 11.3 Special Cases

**Square constellation verification:**
- 16-QAM: 4×4 grid with $I_n, Q_n \in \{±1, ±3\}$ ✓
- 64-QAM: 8×8 grid with $I_n, Q_n \in \{±1, ±3, ±5, ±7\}$ ✓

**Orthogonality preservation:**
$$\int_0^{T_s} \cos(2\pi f_c t)\sin(2\pi f_c t)dt = 0$$ ✓

### 11.4 Power Conservation

Total average power:
$$P_{avg} = \frac{1}{T_s}\int_0^{T_s} E[s^2(t)]dt = \frac{E[I_n^2] + E[Q_n^2]}{T_s} = \frac{E_s}{T_s}$$ ✓

---

## 12. Key Insights

• **Insight 1**: QAM exploits two orthogonal dimensions (I and Q) to transmit independent data streams on the same carrier frequency, doubling spectral efficiency compared to single-dimension modulation.

• **Insight 2**: The quadrature (90° phase shift) relationship between carriers ensures zero cross-talk between I and Q channels under ideal conditions.

• **Insight 3**: Higher-order QAM (larger M) increases spectral efficiency but requires higher SNR for the same error rate - a fundamental trade-off in digital communications.

• **Insight 4**: The constellation geometry directly impacts performance: square constellations are optimal for AWGN channels, while circular constellations may be better for peak-power-limited channels.

• **Insight 5**: Gray coding ensures adjacent constellation points differ by only one bit, minimizing bit errors when symbol errors occur.

• **Insight 6**: QAM can be viewed as simultaneous amplitude and phase modulation, combining benefits of both ASK and PSK.

---

## 13. Applications

**Where QAM is used:**

**Digital Cable (DOCSIS 3.1):**
- Up to 4096-QAM for downstream
- Adaptive modulation based on channel quality
- Spectral efficiency up to 12 bits/s/Hz

**WiFi Standards:**
- 802.11ac: up to 256-QAM
- 802.11ax (WiFi 6): up to 1024-QAM
- 802.11be (WiFi 7): up to 4096-QAM

**5G NR (New Radio):**
- Up to 256-QAM for sub-6 GHz
- 64-QAM for mmWave
- Adaptive based on channel conditions

**Digital TV (DVB-C2):**
- Up to 4096-QAM
- Variable constellation sizes per carrier
- LDPC coding for error correction

**Satellite Communications:**
- DVB-S2X: up to 256-APSK (variant of QAM)
- Adaptive coding and modulation (ACM)

**Design implications:**
- **Linearity requirements**: Higher-order QAM requires more linear amplifiers due to higher PAPR
- **Phase noise sensitivity**: Increases with constellation density
- **Equalization needs**: Dense constellations require better channel equalization
- **ADC/DAC resolution**: Typically need 2 extra bits per dimension increase

---

## 14. Extensions & Advanced Topics

### 14.1 Non-Square Constellations

**Cross-constellation** (32-QAM, 128-QAM):
- Optimized for certain channel conditions
- Better power efficiency than square constellations

**Hexagonal packing**:
- Theoretically optimal for 2D packing
- 0.66 dB gain over square lattice
- Complex implementation

### 14.2 Hierarchical QAM

Used in broadcasting for unequal error protection:
- High-priority bits mapped to MSBs
- Low-priority bits mapped to LSBs
- Different services with different robustness

### 14.3 APSK (Amplitude Phase Shift Keying)

Circular constellation variants:
- Better PAPR properties
- Used in satellite communications
- Optimal for nonlinear channels

### 14.4 Probabilistic Shaping

Non-uniform constellation usage:
- Gaussian-like distribution of symbols
- Approaches Shannon capacity
- Up to 1.53 dB shaping gain

### 14.5 Geometric Shaping

Optimize constellation point positions:
- Non-uniform spacing
- Adapted to channel characteristics
- Machine learning optimization

---

## 15. Implementation Considerations

### 15.1 Carrier Recovery

**Phase-locked loop (PLL)**:
$$\theta_{error} = \arg\left(\sum_{n} r_n s_n^*\right) \tag{39}$$

**Costas loop**: Performs simultaneous demodulation and carrier recovery

### 15.2 Timing Recovery

**Gardner algorithm**:
$$e_n = (r_{n-1/2} - r_{n+1/2})(r_n^* - r_n^{**}) \tag{40}$$

**Mueller-Müller**: Decision-directed timing recovery

### 15.3 Equalization

**Linear equalizer**:
$$H_{eq}(f) = \frac{H^*(f)}{|H(f)|^2 + N_0/E_s} \tag{41}$$

**Decision feedback equalizer (DFE)**: Removes ISI using past decisions

### 15.4 Practical Impairments

**I/Q imbalance**:
- Gain imbalance: $g = g_I/g_Q ≠ 1$
- Phase imbalance: $\phi ≠ 90°$
- Causes constellation distortion

**Phase noise**:
- Random phase variations: $\phi(t)$
- Increases error floor
- Limits achievable constellation size

**Nonlinear distortion**:
- Amplifier compression
- Constellation warping
- Spectral regrowth

---

## 16. Summary for Exam Preparation

**Must remember:**

1. **Basic QAM formula**:
   $$s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$

2. **Orthogonality condition**:
   $$\int_0^{T_s} \cos(2\pi f_c t)\sin(2\pi f_c t)dt = 0$$

3. **Constellation size relationship**:
   - M-QAM carries $\log_2(M)$ bits per symbol
   - Spectral efficiency: $\eta = \log_2(M)$ bits/s/Hz (ideal)

4. **Energy per symbol** (square QAM):
   $$E_s = \frac{2(M-1)}{3} \cdot d^2$$

5. **Symbol error rate approximation**:
   $$P_s \approx 4Q\left(\sqrt{\frac{3E_s}{2(M-1)N_0}}\right)$$

**Common mistakes to avoid:**
- Forgetting the negative sign in Q channel
- Confusing symbol rate with bit rate
- Using wrong normalization for constellation energy
- Missing factor of 2 in bandwidth calculations
- Confusing peak vs average power

**Practice problems:**
- Draw constellation diagrams for 16-QAM, 64-QAM
- Calculate spectral efficiency for given QAM order
- Find minimum $E_b/N_0$ for target BER
- Compare QAM with PSK for same bit rate
- Analyze effect of phase error on constellation

---

## 17. Related Concepts to Study Next

- **OFDM**: Orthogonal Frequency Division Multiplexing - uses QAM on multiple subcarriers
- **MIMO**: Multiple-Input Multiple-Output - spatial multiplexing with QAM
- **Trellis Coded Modulation**: Combining QAM with convolutional coding
- **Adaptive Modulation**: Dynamic QAM order selection based on channel conditions
- **Predistortion**: Linearization techniques for QAM transmitters
- **Soft Decision Decoding**: Using QAM soft outputs for error correction codes

---

## References

1. Proakis & Salehi, "Digital Communications," 5th Edition
2. Goldsmith, "Wireless Communications," Cambridge University Press
3. Barry, Lee & Messerschmitt, "Digital Communication," 3rd Edition
4. Benedetto & Biglieri, "Principles of Digital Transmission"
5. ITU-T Recommendations for QAM systems

---

*End of QAM Derivation*