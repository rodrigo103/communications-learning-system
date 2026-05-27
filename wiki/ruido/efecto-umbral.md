---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_39_efecto_umbral_fm.md
curso: Sistemas de Comunicaciones
unidad: 8
---

# Efecto Umbral en FM y AM

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Definición

El **efecto umbral** es una degradación súbita y no lineal del desempeño cuando la SNR de entrada cae por debajo de un valor crítico. Es característico de los demoduladores no lineales (envolvente en AM, discriminador en FM). [source]

## Umbral en FM

### Mecanismo

Cuando la portadora FM se suma con ruido de banda angosta, la fase resultante es:

$$\phi_{total}(t) = \phi_m(t) + \tan^{-1}\left(\frac{-n_q(t)}{A_c + n_i(t)}\right)$$

**Sobre el umbral** ($A_c \gg n$): la fase extra es pequeña y lineal, ruido aditivo.

**Bajo el umbral** ($A_c < n$): el denominador $A_c + n_i(t)$ cruza cero, produciendo **saltos de fase de $2\pi$** (clicks). El discriminador de frecuencia detecta estos saltos como pulsos impulsivos intensos. [source]

### Umbral Típico

$$\boxed{SNR_{umbral} \approx 10 \text{ dB}}$$

La tasa de clicks es:

$$\lambda_{clicks} \approx \frac{B}{\pi}\exp(-SNR_{in})$$

- Sobre el umbral (SNR > 10 dB): $\lambda \approx 0$
- En el umbral (SNR ≈ 10 dB): clicks esporádicos audibles
- Bajo el umbral: colapso total [source]

### Reducción del Umbral

| Demodulador | Umbral típico |
|-------------|---------------|
| Discriminador convencional | ~10 dB |
| PLL (Phase-Locked Loop) | ~7 dB |
| FMFB (FM Feedback) | ~4-5 dB |

## Umbral en AM

En AM con detección de envolvente, el umbral también ocurre cerca de 10 dB. La diferencia con FM: [analysis]

- **AM**: degradación más gradual, el ruido se suma a la señal
- **FM**: colapso súbito y dramático, los clicks dominan completamente

**Paradoja:** FM es muy superior a AM sobre el umbral, pero peor bajo el umbral.

## Implicaciones de Diseño

1. **Operar siempre sobre el umbral**: diseñar margen de 2-3 dB mínimo
2. **Mayor $\beta$ empeora el umbral**: más ancho de banda → más ruido → umbral más cercano
3. **PLL para extender alcance**: ganancia de ~3 dB en sensibilidad
4. **Sistemas digitales**: no tienen umbral tan marcado como FM

## Ver también

- [[ruido/snr-modulacion-lineal]] — Umbral en AM: comportamiento comparado
- [[ruido/snr-modulacion-exponencial]] — Ventaja de FM sobre el umbral
- [[modulacion-analogica/fm-vs-pm]] — Ambos sufren efecto umbral
- [[ruido/intercomparacion-sistemas]] — Umbral como factor de comparación
