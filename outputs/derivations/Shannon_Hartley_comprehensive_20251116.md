# Shannon-Hartley Theorem - Complete Derivation

**Date**: 2024-11-16
**Level**: Graduate/Advanced
**For**: Communications Systems - Information Theory

---

## 1. Introduction & Motivation

The Shannon-Hartley theorem establishes the fundamental limit on the rate at which information can be reliably transmitted over a communications channel in the presence of noise. This theorem, proved by Claude Shannon in 1948, forms the cornerstone of modern information theory and digital communications. It provides the theoretical maximum channel capacity, showing that reliable communication is possible at any rate below this capacity and impossible above it.

The theorem bridges information theory with physical communication systems, relating abstract concepts like entropy and mutual information to concrete parameters like bandwidth and signal-to-noise ratio. It reveals the fundamental tradeoff between bandwidth and power in achieving reliable communication.

## 2. Prerequisites

**Mathematical background needed:**
- Probability theory and random processes
- Differential entropy and mutual information
- Gaussian random variables and processes
- Fourier analysis and spectral representation
- Calculus of variations

**Prior results assumed:**
- Definition of entropy for continuous random variables
- Properties of Gaussian distributions
- Nyquist sampling theorem
- Power spectral density concepts
- Convolution and linear systems theory

## 3. Starting Definitions

### 3.1 Information-Theoretic Quantities

**Differential Entropy** for a continuous random variable $X$ with probability density function $f_X(x)$:

$$
h(X) = -\int_{-\infty}^{\infty} f_X(x) \log_2 f_X(x) \, dx \tag{1}
$$

**Mutual Information** between random variables $X$ and $Y$:

$$
I(X;Y) = h(Y) - h(Y|X) = h(X) - h(X|Y) \tag{2}
$$

For continuous variables:

$$
I(X;Y) = \int \int f_{XY}(x,y) \log_2 \frac{f_{XY}(x,y)}{f_X(x)f_Y(y)} \, dx \, dy \tag{3}
$$

### 3.2 Channel Model

Consider an **Additive White Gaussian Noise (AWGN) channel**:

$$
Y(t) = X(t) + N(t) \tag{4}
$$

**Where:**
- $X(t)$ = transmitted signal with average power constraint $P$ [watts]
- $N(t)$ = additive white Gaussian noise with power spectral density $N_0/2$ [W/Hz]
- $Y(t)$ = received signal
- $B$ = channel bandwidth [Hz]

**Physical meaning**: The channel adds random noise to the transmitted signal, limiting our ability to distinguish different transmitted symbols.

### 3.3 Power Constraints

The transmitted signal satisfies the average power constraint:

$$
\lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} E[X^2(t)] \, dt \leq P \tag{5}
$$

The noise power over bandwidth $B$ is:

$$
P_N = N_0 B \tag{6}
$$

The signal-to-noise ratio (SNR) is defined as:

$$
\text{SNR} = \frac{P}{N_0 B} \tag{7}
$$

## 4. Assumptions

We assume the following throughout this derivation:

1. **AWGN channel**: Noise is additive, white (flat spectrum), and Gaussian distributed
   - Valid for thermal noise in most communication systems
   - Represents worst-case noise for given variance (maximum entropy)

2. **Band-limited channel**: Bandwidth is limited to $B$ Hz
   - Physical channels have finite bandwidth
   - Signals are constrained to $[-B, B]$ in frequency domain

3. **Average power constraint**: Transmitted power averaged over time is limited to $P$
   - Realistic constraint for any physical transmitter
   - Peak power constraints not considered here

4. **Stationary processes**: Signal and noise statistics don't change with time
   - Valid for stable communication channels
   - Allows time-averaged analysis

5. **Memoryless channel**: Current output depends only on current input
   - No intersymbol interference
   - Simplification that can be relaxed in practice

## 5. Step-by-Step Derivation

### Step 1: Sampling and Discrete Representation

By the Nyquist-Shannon sampling theorem, any band-limited signal with bandwidth $B$ can be perfectly represented by $2B$ samples per second:

$$
X(t) = \sum_{n=-\infty}^{\infty} X[n] \cdot \text{sinc}(2Bt - n) \tag{8}
$$

where $X[n] = X(n/2B)$ are the sample values.

**Justification**: A signal band-limited to $B$ Hz has no frequency components above $B$ Hz, so sampling at rate $2B$ captures all information (Nyquist rate).

**Physical interpretation**: We can analyze the continuous channel as a sequence of parallel discrete channels, one per sample.

### Step 2: Channel Capacity Definition

For a discrete memoryless channel over $n$ uses, the channel capacity per channel use is:

$$
C = \max_{f_X(x)} I(X;Y) \text{ bits per channel use} \tag{9}
$$

Since we have $2B$ samples per second, the capacity in bits per second is:

$$
C = 2B \cdot \max_{f_X(x)} I(X;Y) \text{ bits per second} \tag{10}
$$

**Justification**: Channel capacity is the maximum mutual information achievable by optimizing the input distribution.

### Step 3: Mutual Information for Gaussian Channel

For the AWGN channel with $Y = X + N$ where $N \sim \mathcal{N}(0, \sigma_N^2)$:

$$
I(X;Y) = h(Y) - h(Y|X) \tag{11}
$$

Since $Y|X = X + N$ and $N$ is independent of $X$:

$$
h(Y|X) = h(X + N|X) = h(N) \tag{12}
$$

**Justification**: Given $X$, the randomness in $Y$ comes only from $N$, and conditioning doesn't affect the entropy of independent noise.

Therefore:

$$
I(X;Y) = h(Y) - h(N) \tag{13}
$$

### Step 4: Entropy of Gaussian Noise

For a Gaussian random variable $N \sim \mathcal{N}(0, \sigma_N^2)$:

$$
h(N) = \frac{1}{2} \log_2(2\pi e \sigma_N^2) \text{ bits} \tag{14}
$$

**Derivation of (14)**:

$$
\begin{align}
h(N) &= -\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\sigma_N^2}} e^{-n^2/2\sigma_N^2} \log_2\left(\frac{1}{\sqrt{2\pi\sigma_N^2}} e^{-n^2/2\sigma_N^2}\right) dn \\
&= \frac{1}{2}\log_2(2\pi\sigma_N^2) + \frac{1}{2\sigma_N^2 \ln 2} \int_{-\infty}^{\infty} n^2 \cdot \frac{1}{\sqrt{2\pi\sigma_N^2}} e^{-n^2/2\sigma_N^2} dn \\
&= \frac{1}{2}\log_2(2\pi\sigma_N^2) + \frac{1}{2\ln 2} \\
&= \frac{1}{2}\log_2(2\pi e \sigma_N^2)
\end{align}
$$

### Step 5: Maximum Entropy Theorem

**Theorem**: Among all continuous distributions with a given variance $\sigma^2$, the Gaussian distribution has maximum differential entropy.

**Proof sketch**: Using calculus of variations with the constraints:
- $\int f(x)dx = 1$ (normalization)
- $\int x^2 f(x)dx = \sigma^2$ (variance constraint)

The Lagrangian method yields $f(x) \propto e^{-x^2/2\sigma^2}$, which is Gaussian.

**Implication**: For fixed power (variance) $P + \sigma_N^2$, $h(Y)$ is maximized when $Y$ is Gaussian.

### Step 6: Optimal Input Distribution

Given that $Y = X + N$ with $N \sim \mathcal{N}(0, \sigma_N^2)$:
- $Y$ is Gaussian if and only if $X$ is Gaussian (sum of Gaussians is Gaussian)
- To maximize $h(Y)$ with constraint $E[Y^2] = P + \sigma_N^2$, we need $Y$ Gaussian
- Therefore, optimal $X \sim \mathcal{N}(0, P)$

With this choice:

$$
Y \sim \mathcal{N}(0, P + \sigma_N^2) \tag{15}
$$

### Step 7: Computing Maximum Mutual Information

With optimal Gaussian input:

$$
\begin{align}
I(X;Y) &= h(Y) - h(N) \\
&= \frac{1}{2}\log_2(2\pi e (P + \sigma_N^2)) - \frac{1}{2}\log_2(2\pi e \sigma_N^2) \\
&= \frac{1}{2}\log_2\left(\frac{P + \sigma_N^2}{\sigma_N^2}\right) \\
&= \frac{1}{2}\log_2\left(1 + \frac{P}{\sigma_N^2}\right) \tag{16}
\end{align}
$$

### Step 8: Relating to Physical Parameters

For bandwidth $B$ and noise PSD $N_0/2$:
- Noise power in bandwidth $B$: $\sigma_N^2 = N_0 B$
- SNR = $P/(N_0 B)$

Substituting into equation (16):

$$
I(X;Y) = \frac{1}{2}\log_2\left(1 + \frac{P}{N_0 B}\right) = \frac{1}{2}\log_2(1 + \text{SNR}) \tag{17}
$$

### Step 9: Channel Capacity Formula

Since we have $2B$ independent samples per second (from Step 1), the channel capacity is:

$$
C = 2B \cdot \frac{1}{2}\log_2(1 + \text{SNR}) \tag{18}
$$

### Step 10: Final Form

$$
\boxed{C = B \log_2(1 + \text{SNR}) \text{ bits per second}} \tag{19}
$$

Or equivalently:

$$
\boxed{C = B \log_2\left(1 + \frac{P}{N_0 B}\right) \text{ bits per second}} \tag{20}
$$

## 6. Final Result

$$
\boxed{C = B \log_2\left(1 + \frac{P}{N_0 B}\right) \text{ bits per second}}
$$

**Where:**
- $C$ = channel capacity [bits/second]
- $B$ = channel bandwidth [Hz]
- $P$ = average signal power [watts]
- $N_0$ = noise power spectral density [watts/Hz]
- $\text{SNR} = P/(N_0 B)$ = signal-to-noise ratio [dimensionless]

**Valid when:**
- Channel is AWGN (additive white Gaussian noise)
- Signal is band-limited to $B$ Hz
- Average power constraint $P$ is satisfied
- Channel is memoryless and time-invariant

## 7. Validation

### 7.1 Dimensional Analysis

$$
[C] = [B] \cdot \log_2\left(1 + \frac{[P]}{[N_0][B]}\right) = \text{Hz} \cdot \text{dimensionless} = \text{s}^{-1}
$$

Bits per second has dimensions of inverse time ✓

### 7.2 Limiting Cases

**Case 1**: When SNR → 0 (very noisy channel):

$$
C \approx B \log_2(1 + \text{SNR}) \approx B \cdot \frac{\text{SNR}}{\ln 2} \approx 1.44 B \cdot \text{SNR}
$$

Capacity linear in SNR for weak signals (power-limited regime).

**Case 2**: When SNR → ∞ (noiseless channel):

$$
C \approx B \log_2(\text{SNR}) = B \log_2\left(\frac{P}{N_0 B}\right)
$$

Capacity grows logarithmically with power (bandwidth-limited regime).

**Case 3**: When $B$ → 0:

$$
\lim_{B \to 0} B \log_2\left(1 + \frac{P}{N_0 B}\right) = \lim_{B \to 0} \frac{P}{N_0 \ln 2} = \frac{P}{N_0 \ln 2}
$$

Finite capacity even with zero bandwidth (using infinite SNR).

**Case 4**: When $B$ → ∞:

$$
\lim_{B \to \infty} B \log_2\left(1 + \frac{P}{N_0 B}\right) = \lim_{B \to \infty} \frac{P}{N_0 \ln 2} = \frac{P}{N_0 \ln 2} = 1.44 \frac{P}{N_0}
$$

Capacity saturates at finite value despite infinite bandwidth.

### 7.3 Special Cases

**Binary Symmetric Channel (BSC)**: For binary signaling with error probability $p$:

$$
C_{BSC} = 1 - H(p) = 1 + p\log_2(p) + (1-p)\log_2(1-p)
$$

This is a special case of the general capacity formula.

**Noiseless channel** ($N_0 = 0$): Capacity becomes infinite, but Nyquist's result shows we can transmit at most $2B$ independent symbols per second.

### 7.4 Sanity Check

- Capacity increases with bandwidth ✓
- Capacity increases with power ✓
- Capacity decreases with noise ✓
- Cannot achieve infinite capacity with finite resources ✓
- Matches known results for specific channels ✓

## 8. Key Insights

• **Insight 1**: **Fundamental Tradeoff** - We can trade bandwidth for power. Doubling bandwidth doubles capacity, while doubling power gives diminishing returns (logarithmic growth).

• **Insight 2**: **Gaussian Optimality** - Gaussian input distributions achieve capacity for AWGN channels. This is why Gaussian signaling appears so frequently in communications.

• **Insight 3**: **Bandwidth Efficiency** - Maximum spectral efficiency is $C/B = \log_2(1 + \text{SNR})$ bits/s/Hz. High SNR allows more bits per Hz.

• **Insight 4**: **Power Efficiency** - In low SNR regime, capacity is approximately $1.44 B \cdot \text{SNR}$. Each 3 dB increase in power doubles capacity.

• **Insight 5**: **Asymptotic Limits** - As $B \to \infty$, capacity saturates at $P/(N_0 \ln 2)$. Infinite bandwidth cannot give infinite capacity.

• **Insight 6**: **Reliable Communication** - For rates $R < C$, error probability can be made arbitrarily small with appropriate coding. For $R > C$, errors are inevitable.

• **Insight 7**: **Connection to Sampling** - The factor $2B$ connects information theory to signal processing via the Nyquist rate.

## 9. Applications

**Where this formula is used:**
- **Digital Communications Design** - Determining achievable data rates
- **Link Budget Analysis** - Calculating required power for desired capacity
- **Spectrum Allocation** - Optimizing bandwidth usage
- **Coding Theory** - Setting benchmarks for error-correcting codes
- **Satellite Communications** - Power-limited channel design
- **Wireless Systems** - Bandwidth-limited channel optimization
- **Optical Communications** - High SNR regime analysis
- **Information Storage** - Channel capacity of storage media

**Design implications:**
- **Power vs Bandwidth Tradeoff** - In power-limited scenarios (satellite), use more bandwidth. In bandwidth-limited scenarios (urban wireless), use higher power/modulation.
- **Coding Gain** - Practical systems operate 3-10 dB from Shannon limit
- **Adaptive Systems** - Adjust rate based on channel conditions to approach capacity
- **MIMO Benefits** - Multiple antennas provide additional spatial dimensions, multiplying capacity

## 10. Extensions & Related Results

### 10.1 Capacity with Feedback

For AWGN channels, feedback doesn't increase capacity (surprising result):

$$
C_{feedback} = C_{no-feedback} = B \log_2(1 + \text{SNR})
$$

### 10.2 MIMO Capacity

For $M$ transmit and $N$ receive antennas with channel matrix $\mathbf{H}$:

$$
C_{MIMO} = \log_2 \det\left(\mathbf{I}_N + \frac{\text{SNR}}{M}\mathbf{H}\mathbf{H}^H\right) \text{ bits/s/Hz}
$$

### 10.3 Fading Channels

For ergodic fading with channel gain $h$:

$$
C_{fading} = E_h\left[B \log_2(1 + |h|^2 \text{SNR})\right]
$$

### 10.4 Water-Filling Solution

For frequency-selective channels, optimal power allocation follows water-filling:

$$
P(f) = \max\left(0, \lambda - N_0(f)\right)
$$

where $\lambda$ is chosen to satisfy the power constraint.

### 10.5 Sphere Packing Interpretation

Shannon capacity relates to the number of distinguishable signal points in $n$-dimensional space:

$$
M \approx \frac{\text{Volume of signal sphere}}{\text{Volume of noise sphere}} = \left(1 + \text{SNR}\right)^{n/2}
$$

Leading to $C = \frac{1}{n}\log_2 M = \frac{1}{2}\log_2(1 + \text{SNR})$ per dimension.

## 11. Summary for Exam Preparation

**Must remember:**
- **The Formula**: $C = B \log_2(1 + \text{SNR})$ bits/second
- **Key Insight**: Logarithmic relationship with SNR, linear with bandwidth
- **Assumptions**: AWGN channel, optimal Gaussian signaling
- **Units**: Check that SNR is power ratio (not dB!)

**Common mistakes to avoid:**
- Using SNR in dB directly (must convert to linear)
- Forgetting the bandwidth factor $B$
- Confusing bits/s with bits/s/Hz
- Assuming capacity equals actual data rate (it's the theoretical limit)

**Practice problems:**
- Calculate capacity given $P$, $N_0$, and $B$
- Find required SNR for target capacity and bandwidth
- Compare capacity in power-limited vs bandwidth-limited regimes
- Analyze capacity vs bandwidth curves for fixed power

**Quick checks:**
- More bandwidth → more capacity (linear)
- More power → more capacity (logarithmic)
- Capacity has units of bits/second
- Realistic systems operate below capacity

## 12. Related Concepts to Study Next

- **Channel Coding Theorem** - How to achieve capacity with arbitrarily low error
- **Rate-Distortion Theory** - Dual problem of source compression
- **Turbo and LDPC Codes** - Practical codes approaching Shannon limit
- **MIMO Systems** - Spatial multiplexing for increased capacity
- **Network Information Theory** - Multi-user channels and interference
- **Quantum Information Theory** - Capacity of quantum channels
- **Differential Entropy** - Information theory for continuous variables
- **Kolmogorov Complexity** - Algorithmic information theory

## 13. Historical Context and Significance

### 13.1 Historical Development

Claude Shannon proved this theorem in his landmark 1948 paper "A Mathematical Theory of Communication," which founded the field of information theory. The theorem unified disparate communication problems into a single mathematical framework and showed that reliable communication was possible even in noisy channels - a revolutionary insight at the time.

### 13.2 Practical Impact

The Shannon-Hartley theorem has guided the design of every modern communication system:
- **Modems**: V.34 and V.90 approach Shannon capacity for telephone lines
- **Wireless**: 4G and 5G use adaptive modulation to track capacity
- **Satellite**: Deep space communications optimize power efficiency
- **Storage**: Hard drives and SSDs use capacity-approaching codes

### 13.3 Modern Relevance

Current research focuses on:
- **Massive MIMO**: Exploiting spatial dimensions
- **mmWave Communications**: Ultra-wide bandwidth at high frequencies
- **Non-orthogonal Multiple Access**: Approaching multi-user capacity
- **Machine Learning**: Learning optimal codes and modulation

## 14. Deeper Mathematical Connections

### 14.1 Connection to Thermodynamics

Shannon entropy has deep connections to thermodynamic entropy:

$$
S = k_B \ln \Omega \leftrightarrow H = \log_2 M
$$

Where $k_B$ is Boltzmann's constant and $\Omega$ is the number of microstates. This reveals information as a physical quantity.

### 14.2 Connection to Statistical Mechanics

The maximum entropy principle used in deriving capacity relates to:
- **Jaynes' Principle**: Maximum entropy inference
- **Partition Functions**: Optimal distributions minimize free energy
- **Phase Transitions**: Capacity exhibits threshold behavior

### 14.3 Connection to Estimation Theory

The capacity formula relates to the Cramér-Rao bound:

$$
\text{Var}(\hat{\theta}) \geq \frac{1}{I(\theta)}
$$

where $I(\theta)$ is Fisher information, connecting estimation precision to channel capacity.

## 15. Practical Implementation Considerations

### 15.1 Approaching Capacity

Modern codes achieving near-Shannon performance:
- **Turbo Codes** (1993): Within 0.5 dB of Shannon limit
- **LDPC Codes**: Used in 5G, WiFi 6, approaching capacity
- **Polar Codes**: Provably capacity-achieving for binary channels

### 15.2 Finite Blocklength Effects

For finite blocklength $n$, capacity is reduced:

$$
R \approx C - \sqrt{\frac{V}{n}}Q^{-1}(\epsilon)
$$

where $V$ is channel dispersion and $\epsilon$ is error probability.

### 15.3 Implementation Complexity

Approaching capacity requires:
- Longer codewords (higher latency)
- More complex encoding/decoding (higher power consumption)
- Precise channel state information

Trade-offs must balance theoretical optimality with practical constraints.

## 16. Final Remarks

The Shannon-Hartley theorem represents one of the most profound results in engineering and applied mathematics. It provides an absolute benchmark for communication system performance and reveals the fundamental nature of information transmission. While the theorem gives us the ultimate limit, approaching this limit in practical systems remains an active area of research and engineering innovation.

The beauty of the theorem lies not just in its mathematical elegance but in its universality - it applies equally to radio communications, optical fibers, storage systems, and even biological communication channels. It shows us that noise doesn't prevent communication; it only limits its rate. With proper coding, we can communicate as reliably as desired, as long as we respect the capacity limit.

This derivation has shown how the theorem emerges naturally from information-theoretic principles, connecting abstract mathematical concepts to concrete engineering parameters. The journey from entropy to capacity reveals the deep structure underlying all communication systems and provides the foundation for the digital age.

---

*"The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point."* - Claude Shannon, 1948