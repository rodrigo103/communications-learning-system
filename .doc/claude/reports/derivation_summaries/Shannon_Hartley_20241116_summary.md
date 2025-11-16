# Derivation Summary: Shannon-Hartley Theorem

**Completed**: 2024-11-16T10:00:00Z
**Full derivation**: /Users/rodrigovidela/DOCUMENTOS_MIOS/communications-learning-system/outputs/derivations/Shannon_Hartley_comprehensive_20251116.md
**Level**: Graduate/Advanced

## What Was Derived
The Shannon-Hartley theorem for channel capacity was derived from first principles of information theory, starting with entropy and mutual information definitions, through the AWGN channel model, to the final capacity formula. The derivation proves that Gaussian signaling is optimal and establishes the fundamental limit of reliable communication.

## Key Results
$$C = B \log_2(1 + \text{SNR}) \text{ bits/second}$$

$$C = B \log_2\left(1 + \frac{P}{N_0 B}\right) \text{ bits/second}$$

Where:
- $C$ = channel capacity [bits/s]
- $B$ = bandwidth [Hz]
- $P$ = signal power [W]
- $N_0$ = noise PSD [W/Hz]
- SNR = $P/(N_0 B)$

## Mathematical Techniques Used
- Differential entropy maximization
- Calculus of variations for optimal distributions
- Nyquist sampling theorem application
- Mutual information calculation
- Lagrangian optimization
- Properties of Gaussian distributions
- Information-theoretic inequalities

## Physical Insights
- Bandwidth-power tradeoff: linear growth with bandwidth, logarithmic with power
- Gaussian signaling achieves capacity for AWGN channels
- Capacity saturates at $P/(N_0 \ln 2)$ as bandwidth approaches infinity
- In low SNR regime, capacity is approximately linear in SNR
- Reliable communication possible at any rate below capacity
- Feedback doesn't increase AWGN channel capacity

## Concepts Reinforced
- Entropy and mutual information
- AWGN channel model
- Nyquist sampling rate (2B samples/second)
- Maximum entropy principle
- Signal-to-noise ratio
- Power spectral density
- Band-limited signals
- Information capacity vs data rate

## Prerequisites
- Probability theory and random processes
- Information theory basics (entropy, mutual information)
- Fourier analysis and sampling theorem
- Linear systems theory
- Gaussian distributions and their properties

## Validity Constraints
- Additive white Gaussian noise channel
- Band-limited signals (bandwidth B)
- Average power constraint
- Memoryless channel
- Stationary processes
- Time-invariant channel

## Suggested Next Steps
- Study channel coding theorem (achieving capacity)
- Explore MIMO capacity formulas
- Learn about practical capacity-approaching codes (Turbo, LDPC)
- Investigate capacity of fading channels
- Study rate-distortion theory (dual problem)
- Analyze finite blocklength effects
- Explore water-filling for frequency-selective channels