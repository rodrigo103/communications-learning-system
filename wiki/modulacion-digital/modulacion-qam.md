---
tags:
  - wiki/modulacion-digital
source_file: explicaciones_anki/unidad_06/carta_29_qam.md
curso: Sistemas de Comunicaciones
unidad: 6
---

# QAM: Modulación de Amplitud en Cuadratura

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_06/carta_29_qam]]]

## Definición

QAM modula independientemente la amplitud de dos portadoras en cuadratura (desfasadas 90°), combinando efectivamente [[../modulacion-digital/ask-fsk-psk|ASK y PSK]] en un solo esquema. [source — [[../../explicaciones_anki/unidad_06/carta_29_qam]]]

### Señal QAM

$$\boxed{s_{QAM}(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)}$$

Donde $I(t)$ y $Q(t)$ toman valores discretos de un alfabeto de amplitudes. La envolvente compleja es:

$$\tilde{s}(t) = I(t) + jQ(t) = A(t)e^{j\phi(t)}$$

## Ortogonalidad I-Q

Las portadoras $\cos$ y $\sin$ son ortogonales:

$$\int_0^T \cos(2\pi f_c t) \cdot \sin(2\pi f_c t) \, dt = 0$$

Esto permite transmitir dos flujos independientes en el mismo ancho de banda. [source — [[../../explicaciones_anki/unidad_06/carta_29_qam]]]

## Eficiencia Espectral

Para M-QAM con velocidad de símbolo $R_s$:

$$R_b = R_s \cdot \log_2(M)$$

$$B_{min} = R_s \text{ (Nyquist)}$$

$$\boxed{\eta = \frac{R_b}{B} = \log_2(M) \text{ bits/s/Hz}}$$

Con filtrado raised-cosine (factor de roll-off $\alpha$):

$$\eta = \frac{2\log_2(M)}{1 + \alpha}$$

## Órdenes de QAM

| Orden | $M$ | bits/símbolo | $\eta$ ideal | SNR mínima |
|-------|-----|-------------|-------------|------------|
| 4-QAM (QPSK) | 4 | 2 | 2 | ~10 dB |
| 16-QAM | 16 | 4 | 4 | ~15 dB |
| 64-QAM | 64 | 6 | 6 | ~20 dB |
| 256-QAM | 256 | 8 | 8 | ~25 dB |
| 1024-QAM | 1024 | 10 | 10 | ~35 dB |

## Adaptación Dinámica

Sistemas como LTE y WiFi 6 ajustan el orden de QAM según la SNR del canal: [analysis]

- SNR > 25 dB → 256-QAM (máxima capacidad)
- SNR 15-25 dB → 64-QAM (balance)
- SNR 10-15 dB → 16-QAM (mayor robustez)
- SNR < 10 dB → QPSK (máxima robustez)

## Aplicaciones

- **WiFi 802.11ac/ax**: hasta 1024-QAM
- **Cable modems DOCSIS 3.1**: hasta 4096-QAM
- **5G NR**: hasta 256-QAM
- **DSL**: 16-256 QAM
- **TV digital (DVB)**: 16-256 QAM

## Ver también

- [[../modulacion-digital/constelaciones]] — Representación de constelaciones QAM rectangulares
- [[../modulacion-digital/ask-fsk-psk]] — Modulaciones básicas que QAM combina
- [[../derivaciones/modulacion-qam]] — Derivación matemática completa
- [[../modulacion-analogica/am-vs-dsb-sc]] — Antecedente analógico de modulación en cuadratura
