---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_39_efecto_umbral_fm.md
curso: Sistemas de Comunicaciones
unidad: 8
---

# SNR en Modulaciones Exponenciales (FM y PM)

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Ganancia de SNR en FM

Sobre el umbral, FM ofrece una ganancia de SNR proporcional al cuadrado del índice de modulación:

$$\boxed{\left(\frac{S}{N}\right)_{out}^{FM} = 3\beta^2(\beta + 1) \cdot \left(\frac{S}{N}\right)_{in}}$$

Para un tono modulante simple: $SNR_{out} = 3\beta^2 \cdot SNR_{in}$. [source]

### Ejemplo: FM Broadcast

Con $\beta = 5$ (desviación 75 kHz, audio 15 kHz):
- Factor de mejora: $3 \times 25 \times 6 = 450$ (26.5 dB)
- Si $SNR_{in} = 20$ dB → $SNR_{out} \approx 46.5$ dB

## El Ruido en FM: Forma Triangular

El ruido a la salida del demodulador FM tiene DEP que aumenta con $f^2$:

$$\boxed{S_{n,out}(f) = \frac{2N_0 f^2}{A_c^2} \quad \text{para } |f| < f_m}$$

Esto significa que las frecuencias altas de la señal son más vulnerables al ruido. [source]

## Pre-énfasis y De-énfasis

Para compensar la forma triangular del ruido, se aplica:

1. **Pre-énfasis** en el transmisor: amplifica altas frecuencias del audio antes de modular
2. **De-énfasis** en el receptor: atenúa altas frecuencias después de demodular

La mejora típica en SNR es de:

$$\boxed{\text{Mejora por \'{e}nfasis} \approx 10-13 \text{ dB}}$$

Constantes de tiempo estándar: $\tau = 75$ μs (USA/Japón), $\tau = 50$ μs (Europa). [source]

### SNR Total con Énfasis

Para FM broadcast ($\beta = 5$, con énfasis):

$$SNR_{total} = 3\beta^2 \cdot SNR_{in} + \text{Mejora}_{enfasis} \approx 38.8 + 12 = 50.8 \text{ dB}$$

Comparado con AM: ventaja de ~31 dB (factor > 1000). [analysis]

## Ver también

- [[ruido/relacion-snr]] — Definiciones y métricas fundamentales
- [[modulacion-analogica/fm-vs-pm]] — Comparación entre FM y PM
- [[modulacion-analogica/preenfasis-deenfasis]] — Red de énfasis en detalle
- [[ruido/efecto-umbral]] — Límite donde colapsa la ventaja de FM
- [[ruido/intercomparacion-sistemas]] — Comparación global de todos los sistemas
