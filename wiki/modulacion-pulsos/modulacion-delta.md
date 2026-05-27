---
tags:
  - wiki/modulacion-pulsos
source_file: explicaciones_anki/unidad_05/carta_25_pcm-vs-delta-modulation.md
curso: Sistemas de Comunicaciones
unidad: 5
---

# Modulación Delta y Delta Adaptativa

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_05/carta_25_pcm-vs-delta-modulation]]]

## Modulación Delta (DM)

A diferencia de [[../modulacion-pulsos/pcm-cuantificacion|PCM]], que transmite el valor absoluto de cada muestra con $n$ bits, la Modulación Delta transmite **solo 1 bit por muestra**: la dirección del cambio (incremento/decremento).

### Principio de Funcionamiento

1. **Predicción**: $\hat{x}[n] = \hat{x}[n-1] + \delta \cdot b[n-1]$
2. **Comparación**: si $x[n] > \hat{x}[n]$, $b[n] = +1$; si no, $b[n] = -1$
3. **Transmisión**: 1 bit por muestra → $R_{DM} = f_s$

El receptor reconstruye integrando:

$$\hat{x}[n] = \hat{x}[0] + \delta \sum_{i=1}^{n} b[i]$$

### Problemas Fundamentales

**Slope Overload** (sobrecarga de pendiente):
- Ocurre cuando $|\frac{dx}{dt}| > \delta \cdot f_s$
- La señal cambia más rápido de lo que DM puede seguir
- Condición para evitarlo: $\boxed{\delta \cdot f_s \geq \max|dx/dt|}$ [source — [[../../explicaciones_anki/unidad_05/carta_25_pcm-vs-delta-modulation]]]

**Granular Noise** (ruido granular):
- Ocurre en regiones planas de la señal
- El codificador oscila $\pm\delta$ alrededor del valor real

## Delta Adaptativa (ADM)

ADM varía el paso $\delta$ según el patrón de bits:

$$\delta[n] = \begin{cases}
\delta[n-1] \cdot K & \text{si } b[n] = b[n-1] \text{ (misma dirección)} \\
\delta[n-1] / K & \text{si } b[n] \neq b[n-1] \text{ (cambio dirección)}
\end{cases}$$

con $K > 1$ (típicamente 1.5). [source — [[../../explicaciones_anki/unidad_05/carta_25_pcm-vs-delta-modulation]]]

Esto permite:
- Pasos grandes para pendientes pronunciadas (evita slope overload)
- Pasos pequeños en regiones planas (reduce granular noise)

## Comparación PCM vs DM vs ADM

| Parámetro | PCM | DM | ADM |
|-----------|-----|----|----|
| Bits/muestra | 8-16 | 1 | 1 |
| Oversampling | 1× | 4-8× | 2-4× |
| SNR típico (voz) | 50 dB | 25 dB | 35 dB |
| Complejidad | Media | Muy baja | Baja |

**Regla clave:** DM usa 1 bit/muestra pero requiere $f_s$ de 4-8 veces mayor que PCM para tasas de bits equivalentes. [analysis]

## Aplicaciones

- **PCM**: Telefonía digital, audio CD, sistemas profesionales
- **DM**: Telemetría simple, sistemas militares antiguos
- **ADM**: Comunicaciones tácticas, codecs de voz de baja tasa
- **CVSD** (variante de ADM): Bluetooth clásico, radios militares

## Ver también

- [[../modulacion-pulsos/pcm-cuantificacion]] — Paradigma alternativo de digitalización
- [[../modulacion-pulsos/muestreo-ideal-natural]] — Oversampling requerido en DM
- [[../ruido/relacion-snr]] — SNR en sistemas de comunicaciones
