---
tags:
  - wiki/modulacion-pulsos
source_file: explicaciones_anki/unidad_05/carta_24_companding-pcm.md
curso: Sistemas de Comunicaciones
unidad: 5
---

# Companding: Compresión y Expansión

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_05/carta_24_companding-pcm]]]

## Definición

**Companding** = **Comp**ressing + **Exp**anding. Es una técnica de cuantificación no uniforme que mejora la SNR para señales débiles sin incrementar el número de bits en [[../modulacion-pulsos/pcm-cuantificacion]]. [source — [[../../explicaciones_anki/unidad_05/carta_24_companding-pcm]]]

### El Problema

En cuantificación uniforme, el error máximo $\pm\Delta/2$ es constante. Para señales débiles, el error relativo es grande, produciendo SNR pobre. Las señales fuertes "desperdician" resolución.

### La Solución

Usar pasos de cuantificación variables:
- **Pequeños** para señales débiles → mejor resolución donde se necesita
- **Grandes** para señales fuertes → suficiente calidad sin desperdiciar bits

## Leyes de Companding

### μ-law (Norteamérica, Japón)

$$\boxed{C_\mu(x) = \text{sgn}(x) \cdot \frac{\ln(1 + \mu|x/V_{max}|)}{\ln(1 + \mu)}}$$

con $\mu = 255$ (estándar). [source — [[../../explicaciones_anki/unidad_05/carta_24_companding-pcm]]]

### A-law (Europa, resto del mundo)

$$C_A(x) = \begin{cases}
\text{sgn}(x) \cdot \frac{A|x/V_{max}|}{1 + \ln(A)} & |x| \leq \frac{V_{max}}{A} \\[6pt]
\text{sgn}(x) \cdot \frac{1 + \ln(A|x/V_{max}|)}{1 + \ln(A)} & |x| > \frac{V_{max}}{A}
\end{cases}$$

con $A = 87.6$ (estándar). [source — [[../../explicaciones_anki/unidad_05/carta_24_companding-pcm]]]

**Importante:** μ-law y A-law **no son compatibles** entre sí. Mezclarlos causa distorsión severa. [analysis]

## Mejora en Rango Dinámico

La mejora aproximada en rango dinámico con μ-law:

$$\boxed{\Delta_{DR} \approx 20\log_{10}(\mu) \text{ dB}}$$

Para $\mu = 255$: mejora ≈ 48 dB. [source — [[../../explicaciones_anki/unidad_05/carta_24_companding-pcm]]]

## Proceso Completo

1. **Compresión** en transmisor: $y = C(x)$ (función no lineal)
2. **Cuantificación uniforme** de $y$
3. **Transmisión digital**
4. **Expansión** en receptor: $x' = C^{-1}(y')$

El companding **no reduce la tasa de bits**, redistribuye la resolución. [analysis]

## Ejemplo: Señal de Voz

Con 8 bits y rango dinámico de 40 dB:
- **Sin companding**: $SNR_{d\acute{e}bil} \approx 9.9$ dB (inaceptable)
- **Con μ-law**: $SNR_{d\acute{e}bil} \approx 30-35$ dB (calidad telefónica aceptable)

## Ver también

- [[../modulacion-pulsos/pcm-cuantificacion]] — PCM uniforme como base
- [[../modulacion-digital/ask-fsk-psk]] — Modulaciones digitales que transportan los bits
- [[../modulacion-pulsos/multiplex-tdm]] — Canales con companding en sistemas TDM
