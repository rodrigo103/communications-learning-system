---
tags:
  - wiki/modulacion-pulsos
source_file: explicaciones_anki/unidad_05/carta_23_pcm-etapas.md
curso: Sistemas de Comunicaciones
unidad: 5
---

# PCM: Muestreo, Cuantificación y Codificación

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_05/carta_23_pcm-etapas]]]

## Etapas del PCM

**Pulse Code Modulation (PCM)** digitaliza señales analógicas en tres etapas fundamentales. [source — [[../../explicaciones_anki/unidad_05/carta_23_pcm-etapas]]]

### 1. Muestreo

La señal continua $x(t)$ se muestrea a frecuencia $f_s \geq 2f_{max}$ (Nyquist):

$$x_s(t) = \sum_{n=-\infty}^{\infty} x(nT_s) \, \delta(t - nT_s)$$

En frecuencia, el espectro se replica cada $f_s$ Hz. Si $f_s$ es insuficiente, se produce [[../herramientas-matematicas/teorema-muestreo|aliasing]]. [source — [[../../explicaciones_anki/unidad_05/carta_23_pcm-etapas]]]

### 2. Cuantificación

La amplitud se discretiza en $L = 2^n$ niveles. Para rango $[-V_{max}, +V_{max}]$:

$$\Delta = \frac{2V_{max}}{L} = \frac{2V_{max}}{2^n}$$

El error de cuantificación está acotado: $-\Delta/2 \leq e_q \leq \Delta/2$. [source — [[../../explicaciones_anki/unidad_05/carta_23_pcm-etapas]]]

### 3. Codificación

Cada nivel recibe un código binario de $n$ bits. La tasa de bits resultante es:

$$\boxed{R_b = n \cdot f_s \text{ bits/s}}$$

Para telefonía: $n = 8$, $f_s = 8$ kHz → 64 kbps por canal. [source — [[../../explicaciones_anki/unidad_05/carta_23_pcm-etapas]]]

## Ruido de Cuantificación y SNR

Modelando el error como ruido uniforme, la potencia del error es:

$$\sigma_q^2 = \int_{-\Delta/2}^{\Delta/2} e^2 \cdot \frac{1}{\Delta} de = \frac{\Delta^2}{12}$$

Para señal senoidal de amplitud completa, la SNR de cuantificación es:

$$\boxed{SNR_q = 6.02n + 1.76 \text{ dB}}$$

Esta es la **regla de 6 dB/bit**: cada bit adicional duplica los niveles de cuantificación y mejora la SNR en aproximadamente 6 dB. [source — [[../../explicaciones_anki/unidad_05/carta_23_pcm-etapas]]]

## Ancho de Banda PCM

Para transmisión en banda base:

$$BW_{PCM} \approx \frac{R_b}{2} = \frac{n \cdot f_s}{2}$$

Comparado con la señal analógica original:

$$\frac{BW_{PCM}}{BW_{analog}} \geq n$$

PCM intercambia ancho de banda por inmunidad al ruido. [analysis]

## Valores de Referencia

| Aplicación | $f_s$ | $n$ | $R_b$ |
|------------|-------|-----|-------|
| Telefonía G.711 | 8 kHz | 8 | 64 kbps |
| CD Audio | 44.1 kHz | 16 | 1.411 Mbps |
| Audio profesional | 192 kHz | 24 | 4.6 Mbps |

## Ver también

- [[../modulacion-pulsos/muestreo-ideal-natural]] — Muestreo ideal, natural y PAM
- [[../modulacion-pulsos/companding]] — Cuantificación no uniforme para mejorar SNR
- [[../modulacion-pulsos/modulacion-delta]] — Alternativa a PCM con 1 bit/muestra
- [[../ruido/relacion-snr]] — Relación señal-ruido en sistemas de comunicación
