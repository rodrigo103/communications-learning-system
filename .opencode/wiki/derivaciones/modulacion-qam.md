---
tags:
  - wiki/derivaciones
  - wiki/modulacion-digital
source_file: outputs/derivations/QAM_comprehensive_20251116.md
curso: Sistemas de Comunicaciones
unidad: 6
---

# Derivación Completa de Modulación QAM

> **Last verified:** 2025-11-16 | **Verified by:** source

## Fundamento

**Quadrature Amplitude Modulation (QAM)** transmite dos flujos de datos independientes en la misma frecuencia portadora explotando la ortogonalidad entre las componentes seno y coseno.

## Bases ortonormales

$$\phi_1(t) = \sqrt{\frac{2}{T_s}}\cos(2\pi f_c t), \quad \phi_2(t) = -\sqrt{\frac{2}{T_s}}\sin(2\pi f_c t)$$

Estas funciones son ortonormales: $\int_0^{T_s} \phi_i(t)\phi_j(t)dt = \delta_{ij}$ [source].

## Señal QAM

En el espacio de señales, cada símbolo se representa como:

$$s_i(t) = a_i \phi_1(t) + b_i \phi_2(t)$$

Sustituyendo las bases:

$$s_i(t) = \sqrt{\frac{2}{T_s}}[a_i\cos(2\pi f_c t) - b_i\sin(2\pi f_c t)]$$

Para una secuencia de símbolos con pulsos de forma $p(t)$:

$$\boxed{s_{QAM}(t) = \sum_{n=-\infty}^{\infty} [I_n \cos(2\pi f_c t) - Q_n \sin(2\pi f_c t)]p(t - nT_s)}$$

donde $I_n$ y $Q_n$ son las amplitudes de los componentes en fase y cuadratura [source].

## Forma amplitud-fase

Alternativamente, en coordenadas polares:

$$s_i(t) = \sqrt{\frac{2}{T_s}} A_i \cos(2\pi f_c t + \theta_i)$$

con $A_i = \sqrt{a_i^2 + b_i^2}$ y $\theta_i = \arctan(b_i/a_i)$.

## Constelaciones

### QAM cuadrada (M-ary con $M = 2^{2k}$)

$$I_n, Q_n \in \{ \pm d, \pm 3d, \dots, \pm(\sqrt{M}-1)d \}$$

Energía promedio por símbolo para constelación cuadrada:

$$E_s = \frac{2(M-1)}{3}d^2$$

### Ejemplos

| Constelación | Grid | bits/símbolo |
|---|---|---|
| 4-QAM (QPSK) | 2×2 | 2 |
| 16-QAM | 4×4 | 4 |
| 64-QAM | 8×8 | 6 |
| 256-QAM | 16×16 | 8 |

## Ancho de banda y eficiencia espectral

Ancho de banda nulo a nulo (pulsos rectangulares):

$$B_{null} = \frac{2}{T_s} = 2R_s$$

Con pulsos de coseno realzado (roll-off $\alpha$):

$$B = (1 + \alpha)R_s$$

Eficiencia espectral:

$$\boxed{\eta = \frac{R_b}{B} = \log_2(M) \text{ bits/s/Hz}}$$

para pulsos Nyquist ideales ($B = R_s$) [source].

| M-QAM | $\eta$ (bits/s/Hz) |
|---|---|
| 4-QAM | 2 |
| 16-QAM | 4 |
| 64-QAM | 6 |
| 256-QAM | 8 |

## Probabilidad de error

Para QAM cuadrada con detección coherente en AWGN:

$$\boxed{P_s \approx 4\left(1 - \frac{1}{\sqrt{M}}\right) Q\left(\sqrt{\frac{3\log_2(M) \cdot E_b}{(M-1)N_0}}\right)}$$

Con codificación Gray: $P_b \approx P_s / \log_2(M)$ [source].

## PAPR (Peak-to-Average Power Ratio)

$$\text{PAPR} = \frac{3(\sqrt{M} - 1)}{\sqrt{M} + 1}$$

- 4-QAM: PAPR = 1 (envolvente constante)
- 64-QAM: PAPR = 2.33
- 256-QAM: PAPR = 2.6

Mayor orden → mayor PAPR → amplificadores más lineales requeridos [analysis].

## Aplicaciones

- WiFi (802.11ac: hasta 256-QAM, WiFi 6: 1024-QAM)
- 4G LTE / 5G NR: hasta 256-QAM
- Cable módems (DOCSIS 3.1): hasta 4096-QAM
- TV digital (DVB-C): hasta 4096-QAM
- Comunicaciones satelitales (DVB-S2X)

## Ver también

- [[modulacion-digital/modulacion-qam]]
- [[modulacion-digital/constelaciones]]
- [[modulacion-digital/ask-fsk-psk]]
- [[modulacion-digital/probabilidad-error]]
- [[modulacion-digital/eficiencia-espectral]]
- [[espectro-expandido/ofdm]]
