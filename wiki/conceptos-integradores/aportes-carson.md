---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
unidad: 4
---

# John Renshaw Carson y sus Aportes a los Sistemas de Comunicaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

John Renshaw Carson (1886–1940) fue un ingeniero estadounidense que trabajo en los Laboratorios Bell. Sus contribuciones abarcan el analisis matematico de la modulacion FM, el desarrollo del modulador balanceado, y el estudio de la distorsion en sistemas de comunicaciones.

## Mapa de Aportes

### Unidad 4 — Regla de Carson para el Ancho de Banda de FM

El aporte mas celebre de Carson: una regla practica para estimar el ancho de banda de una señal FM, que captura aproximadamente el 98% de la potencia de la señal:

$$\boxed{B_T \approx 2(\Delta f + f_m) = 2 f_m (\beta + 1)}$$

Donde:
- $\Delta f = k_f \cdot \max|m(t)|$ = desviacion maxima de frecuencia
- $f_m$ = frecuencia maxima de la señal moduladora
- $\beta = \Delta f / f_m$ = indice de modulacion de FM

**Casos importantes:** [analysis]
- **NBFM ($\beta \ll 1$)**: $B_T \approx 2f_m$ (similar a AM)
- **WBFM ($\beta \gg 1$)**: $B_T \approx 2\Delta f$ (dominado por la desviacion)

La regla de Carson es esencial para el diseño y la asignacion de canales en radio FM comercial ($\Delta f = \pm 75$ kHz, $f_m = 15$ kHz, $\rightarrow B_T \approx 200$ kHz). [analysis]

→ [[../modulacion-analogica/ancho-banda-carson|Regla de Carson para FM]]

### Modulador Balanceado (con Ralph Hartley)

Carson y Hartley desarrollaron el **modulador balanceado**, que suprime la portadora y produce una señal **DSB-SC** (Doble Banda Lateral con Portadora Suprimida). En este circuito, dos señales moduladas en contrafase cancelan la portadora, dejando solo las bandas laterales:

$$\boxed{s_{DSB-SC}(t) = m(t) \cos(2\pi f_c t)}$$

Este diseño es el corazon de los sistemas DSB-SC, SSB (cuando se combina con filtrado), y moduladores I/Q modernos. [analysis]

→ [[../modulacion-analogica/am-vs-dsb-sc|AM vs DSB-SC]]

### Analisis de Distorsion y Pre-enfasis

Carson realizo estudios pioneros sobre distorsion en sistemas de comunicacion y propuso tecnicas de **pre-enfasis/de-enfasis** para reducir el ruido audible en FM, una idea que luego seria estandarizada en la radio FM comercial (constante de tiempo de 75 μs en America, 50 μs en Europa). [analysis]

→ [[../modulacion-analogica/preenfasis-deenfasis|Pre-enfasis y De-enfasis]]

## Ver Tambien

- [[../modulacion-analogica/ancho-banda-carson|Regla de Carson]]
- [[../modulacion-analogica/am-vs-dsb-sc|AM vs DSB-SC]]
- [[../modulacion-analogica/preenfasis-deenfasis|Pre-enfasis y De-enfasis]]
- [[../modulacion-analogica/fm-vs-pm|FM vs PM]]
- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]
- [[../conceptos-integradores/aportes-armstrong|Aportes de Armstrong]]
- [[../conceptos-integradores/pioneros-comunicaciones|Pioneros de las Comunicaciones]]
