# Derivation Summary: Quadrature Amplitude Modulation (QAM)

**Completed**: 2024-11-16T00:00:00Z
**Full derivation**: /Users/rodrigovidela/DOCUMENTOS_MIOS/communications-learning-system/outputs/derivations/QAM_comprehensive_20251116.md
**Level**: Comprehensive (Undergraduate to Advanced)

## What Was Derived
Complete derivation of QAM from orthogonal basis functions, showing how two independent data streams can be transmitted on the same carrier frequency using in-phase and quadrature components. Includes constellation mapping, spectral analysis, power calculations, and error probability formulas.

## Key Results
$$s_{QAM}(t) = \sum_{n=-\infty}^{\infty} [I_n \cos(2\pi f_c t) - Q_n \sin(2\pi f_c t)]p(t - nT_s)$$

$$E_s = \frac{2(M-1)}{3} \cdot d^2 \quad \text{(square M-QAM)}$$

$$\eta_{max} = \log_2(M) \text{ bits/s/Hz}$$

$$P_s \approx 4\left(1 - \frac{1}{\sqrt{M}}\right)Q\left(\sqrt{\frac{3\log_2(M) \cdot E_b}{(M-1)N_0}}\right)$$

## Mathematical Techniques Used
- Orthogonal function expansion
- Signal space representation
- Complex baseband notation
- Fourier transform for spectral analysis
- Euclidean distance metrics
- Probability theory for error analysis
- Energy and power calculations

## Physical Insights
- QAM exploits orthogonality between sine and cosine to double spectral efficiency
- Higher-order constellations trade power efficiency for spectral efficiency
- Square constellations are optimal for AWGN channels
- PAPR increases with constellation size, requiring linear amplifiers
- Gray coding minimizes bit errors when symbol errors occur

## Concepts Reinforced
- Orthogonality and basis functions
- Signal space and constellation diagrams
- Spectral efficiency vs power efficiency trade-offs
- Coherent demodulation
- Maximum likelihood detection
- Symbol and bit error probabilities
- Bandwidth requirements

## Prerequisites
- Fourier transform
- Complex numbers
- Basic probability
- Signal orthogonality
- Matched filter theory

## Validity Constraints
- Requires f_c >> 1/T_s (narrowband assumption)
- Integer carrier cycles per symbol for perfect orthogonality
- Assumes perfect carrier and timing synchronization
- AWGN channel model for error probability formulas
- Linear channel (no nonlinear distortion)

## Suggested Next Steps
- Study OFDM (QAM on multiple subcarriers)
- Explore adaptive modulation techniques
- Learn about practical impairments (I/Q imbalance, phase noise)
- Implement QAM modulator/demodulator in software
- Study error correction coding with QAM
- Investigate non-square constellations and probabilistic shaping