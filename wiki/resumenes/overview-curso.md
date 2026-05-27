---
tags:
  - wiki/resumen
source_file: outputs/mindmaps/communications_systems_course_overview_20251116.md
curso: Sistemas de Comunicaciones
unidad: null
---

# Visión General del Curso: Sistemas de Comunicaciones

> **Last verified:** 2025-11-16 | **Verified by:** source

## Estructura del curso

El curso se organiza en 10 unidades que progresan desde fundamentos hasta temas avanzados, siguiendo el flujo pedagógico:

## Bloque 1: Fundamentos (Unidades 1–2)

### Unidad 1: Introducción
Conceptos básicos: elementos de un sistema de comunicaciones (transmisor, canal, receptor), clasificación de señales (analógicas vs digitales, determinísticas vs aleatorias), espectro electromagnético y uso racional, organismos de normalización.
- [[../introduccion/elementos-sistema]]
- [[../introduccion/espectro-electromagnetico]]

### Unidad 2: Análisis de Señales
Herramientas matemáticas esenciales: [[../herramientas-matematicas/serie-fourier|Serie de Fourier]], [[../herramientas-matematicas/transformada-fourier|Transformada de Fourier]], [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]], convolución, [[../herramientas-matematicas/densidad-espectral-potencia|densidad espectral de potencia]], [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]], correlación y autocorrelación.
- [[../herramientas-matematicas/senales-energia-potencia]]

## Bloque 2: Modulación Analógica (Unidades 3–4)

### Unidad 3: Modulación Lineal
Familia AM: [[../modulacion-analogica/am-vs-dsb-sc|AM estándar]], DSB-SC, SSB (BLU), VSB. Moduladores balanceados, detectores sincrónicos, receptor superheterodino, FDM. Anchos de banda: $BW_{AM} = 2f_m$, $BW_{SSB} = f_m$.
- [[../modulacion-analogica/indice-modulacion-am]]
- [[../modulacion-analogica/receptor-superheterodino]]
- [[../derivaciones/modulacion-am]]

### Unidad 4: Modulación Exponencial
FM y PM: desviación de frecuencia $\Delta f = k_f A_m$, índice de modulación $\beta = \Delta f/f_m$, [[../modulacion-analogica/ancho-banda-carson|Regla de Carson]] ($BW \approx 2(\Delta f + f_m)$), funciones de Bessel, NBFM vs WBFM, pre-énfasis/de-énfasis, FM estéreo.
- [[../modulacion-analogica/fm-vs-pm]]
- [[../modulacion-analogica/fm-banda-angosta]]
- [[../derivaciones/modulacion-fm-carson]]
- [[../derivaciones/modulacion-fm-banda-angosta]]

## Bloque 3: Evolución Digital (Unidades 5–6)

### Unidad 5: Modulación de Pulsos
[[../herramientas-matematicas/teorema-muestreo|Teorema de muestreo]] ($f_s \geq 2f_{max}$), PAM, PWM, PPM, [[../modulacion-pulsos/pcm|PCM]] (muestreo + cuantificación + codificación), SQNR $\approx 6n + 1.76$ dB, companding (Ley A, Ley $\mu$), modulación Delta.
- [[../modulacion-pulsos/cuantificacion]]
- [[../modulacion-pulsos/tdm]]

### Unidad 6: Modulación Digital
[[../modulacion-digital/ask-fsk-psk|ASK, FSK, PSK]] y [[../modulacion-digital/modulacion-qam|QAM]]. [[../modulacion-digital/constelaciones|Constelaciones de señales]], tasa de símbolos vs bits ($R_b = R_s \log_2 M$), [[../modulacion-digital/probabilidad-error|BER vs $E_b/N_0$]], eficiencia espectral $\eta = R_b/B$, filtrado de pulsos (coseno realzado).
- [[../modulacion-digital/comparacion-digital-analogica]]
- [[../modulacion-digital/codificacion-linea]]
- [[../derivaciones/modulacion-qam]]

## Bloque 4: Análisis de Sistemas (Unidades 7–8)

### Unidad 7: Ruido
[[../ruido/fuentes-ruido|Fuentes de ruido]] (térmico, shot, flicker), temperatura de ruido, [[../ruido/factor-ruido-temperatura|figura de ruido]] ($F = SNR_{in}/SNR_{out}$), [[../ruido/formula-friis|Fórmula de Friis]] para cascada, $E_b/N_0$, ruido de banda angosta.
- [[../ruido/relacion-snr]]
- [[../ruido/ruido-termico]]
- [[../derivaciones/ecuacion-friis]]

### Unidad 8: Intercomparación
Criterios: ancho de banda, eficiencia espectral, eficiencia de potencia, complejidad. SNR en modulación lineal (AM, DSB, SSB), SNR en FM/PM, [[../ruido/efecto-umbral-fm|efecto umbral]], comparación analógica vs digital.
- [[../ruido/intercomparacion-sistemas]]
- [[../ruido/snr-modulacion-lineal]]

## Bloque 5: Teoría y Avanzados (Unidades 9–10)

### Unidad 9: Teoría de la Información
[[../teoria-informacion/entropia|Entropía]] ($H = -\sum p_i \log_2 p_i$), [[../teoria-informacion/teorema-shannon-hartley|Shannon-Hartley]] ($C = B \log_2(1+SNR)$), codificación de fuente (Huffman), codificación de canal (Hamming, convolucionales, Turbo, LDPC), límite de Shannon.
- [[../teoria-informacion/capacidad-canal-shannon]]
- [[../teoria-informacion/codificacion-canal]]
- [[../derivaciones/teorema-shannon-hartley]]

### Unidad 10: Temas Avanzados
[[../espectro-expandido/cdma|CDMA]], [[../espectro-expandido/dsss|DSSS]], [[../espectro-expandido/fhss|FHSS]], [[../espectro-expandido/ofdm|OFDM]] (IFFT/FFT + prefijo cíclico), multiplexación (FDM, TDM, CDM, OFDMA), sistemas MIMO, modulación adaptativa.
- [[../conceptos-integradores/evolucion-sistemas]]

## Relaciones clave entre unidades

- **Fourier (U2)** → análisis espectral de todas las modulaciones (U3–U6)
- **Parseval (U2)** → cálculos de potencia y energía en todo el curso
- **Ruido (U7)** → afecta el desempeño de todos los sistemas
- **Shannon (U9)** → límite teórico para todos los sistemas comparados en U8
- **Friis (U7)** → diseño de receptores para todas las modulaciones

## Fórmulas críticas para examen

| Concepto | Fórmula |
|----------|---------|
| AM | $s(t) = A_c[1 + \mu m_n(t)]\cos(2\pi f_c t)$ |
| Carson | $BW = 2(\Delta f + f_m)$ |
| Shannon | $C = B\log_2(1 + SNR)$ |
| Friis | $F_{total} = F_1 + \frac{F_2-1}{G_1} + \cdots$ |
| QAM | $s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$ |
| Parseval | $\int |x(t)|^2 dt = \int |X(f)|^2 df$ |

## Ver también

- [[../planificacion/programa-oficial]]
- [[../planificacion/mazo-anki]]
- [[../planificacion/progreso-actual]]
- [[../resumenes/modulacion-digital-unidad6]]
- [[../conceptos-integradores/trade-off-bw-potencia]]
