---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_08/carta_42_ganancia-procesamiento-pulsos.md
curso: Sistemas de Comunicaciones
unidad: 8
---

# Ganancia de Procesamiento en Modulacion de Pulsos

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_08/carta_42_ganancia-procesamiento-pulsos]]]

Los sistemas de modulacion de pulsos codificados (PCM) obtienen una mejora significativa de SNR gracias a la cuantificacion, regeneracion y codificacion. Esta mejora se cuantifica como ganancia de procesamiento.

## SNR de cuantificacion PCM

La relacion senal a ruido de cuantificacion para PCM con $n$ bits por muestra es:

$$\boxed{\text{SNR}_q\text{ (dB)} = 6.02n + 1.76}$$

Cada bit adicional agrega aproximadamente **6 dB** de SNR. [source — [[../../explicaciones_anki/unidad_08/carta_42_ganancia-procesamiento-pulsos]]]

## Componentes de la ganancia de procesamiento

$$\boxed{G_p = G_{\text{cuant}} \cdot G_{\text{regen}} \cdot G_{\text{cod}}}$$

Donde:

- **$G_{\text{cuant}}$:** Ganancia por cuantificacion. Depende del numero de bits $n$.
- **$G_{\text{regen}}$:** Ganancia por regeneracion. Los pulsos digitales se regeneran en cada repetidor, evitando la acumulacion de ruido (a diferencia de los sistemas analogicos).
- **$G_{\text{cod}}$:** Ganancia por codificacion de canal. Codigos correctores de errores agregan 3-5 dB tipicos.

[analysis]

## Costo en ancho de banda

La expansion de ancho de banda en PCM es:

$$BW_{\text{PCM}} \approx n \cdot f_m$$

Para $n = 8$ bits y $f_m = 4\text{ kHz}$ (voz): $BW \approx 32\text{ kHz}$, un factor de expansion de $8\times$ respecto a la senal analogica original.

Este es un ejemplo directo del **compromiso de Shannon**: se intercambia ancho de banda por SNR. [analysis]

## Regeneracion: la ventaja clave de lo digital

En sistemas analogicos, el ruido se acumula en cada etapa de amplificacion. En sistemas digitales, los pulsos pueden **regenerarse** completamente en cada repetidor: mientras el ruido no cause errores de bit, la senal se reconstruye sin degradacion.

Este es el principio detras de la calidad consistente de las comunicaciones digitales. [analysis]

## Ejemplo: telefonia digital

Sistema PCM telefonico tipico:
- $n = 8$ bits/muestra
- SNR de cuantificacion: $\text{SNR}_q = 6.02 \times 8 + 1.76 \approx 49.9\text{ dB}$
- Expansion de BW: $10\times$
- Con companding (ley A o ley $\mu$): SNR efectiva ~38 dB uniforme en todo el rango dinamico

## PCM vs modulacion analogica

| Aspecto | PCM | Analogica |
|---|---|---|
| SNR | Crece con $n$ (sin limite teorico) | Fija para un sistema dado |
| Ancho de banda | Crece con $n$ | Fijo |
| Regeneracion | Si (no acumula ruido) | No |
| Complejidad | Alta (ADC, sincronismo) | Baja |

## Modulacion Delta

La modulacion delta no tiene ganancia de codificacion inherente como PCM. Su ventaja es la simplicidad (1 bit por muestra), pero requiere **sobremuestreo** para mantener SNR aceptable. La relacion SNR en delta es inversamente proporcional a la frecuencia de muestreo. [analysis]

## Ver también

- [[../modulacion-pulsos/pcm-cuantificacion]] — PCM y cuantificacion
- [[../modulacion-pulsos/companding]] — Companding
- [[../ruido/relacion-snr]] — Relacion Senal a Ruido
- [[../ruido/intercomparacion-sistemas]] — Intercomparacion
- [[../teoria-informacion/teorema-shannon-hartley]] — Shannon-Hartley
- [[../modulacion-pulsos/cuantificacion]] — Cuantificacion
