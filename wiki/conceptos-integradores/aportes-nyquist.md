---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
unidad: 2-7
---

# Harry Nyquist y sus Aportes a los Sistemas de Comunicaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

Harry Nyquist (1889–1976) fue un ingeniero sueco-estadounidense que trabajo en los Laboratorios Bell. Sus contribuciones abarcan tres pilares fundamentales de los sistemas de comunicaciones modernos: el teorema de muestreo, el criterio de transmision sin ISI, y el ruido termico (junto con Johnson).

## Mapa de Aportes

### Unidad 2 — Teorema de Muestreo de Nyquist-Shannon

Una señal limitada en banda $B$ puede reconstruirse **exactamente** a partir de sus muestras si:

$$\boxed{f_s \geq 2B}$$

Sin este teorema no existirian los conversores ADC/DAC, el audio digital, PCM, ni ninguna forma de procesamiento digital de señales. [analysis]

→ [[../herramientas-matematicas/teorema-muestreo|Teorema del Muestreo de Nyquist-Shannon]]

### Unidad 5–6 — Criterio de Nyquist para ISI Cero

En transmision digital por un canal de ancho de banda limitado, los pulsos transmitidos se ensanchan y se solapan, causando **interferencia entre simbolos (ISI)**. Nyquist establecio que la ISI puede eliminarse si los pulsos cumplen:

$$\boxed{p(kT_s) = \begin{cases} 1 & k = 0 \\ 0 & k \neq 0 \end{cases}}$$

Esto implica que el ancho de banda minimo para transmitir $R_s$ simbolos/segundo sin ISI es:

$$\boxed{B_{min} = \frac{R_s}{2}}$$

El **filtro de coseno realzado** (raised cosine) es la implementacion practica mas comun de este criterio. [analysis]

→ [[../modulacion-digital/constelaciones|Constelaciones y Filtro de Nyquist]]

### Unidad 7 — Ruido Termico Johnson-Nyquist

Junto con John B. Johnson, Nyquist explico teoricamente el ruido termico en conductores. La tension de ruido en una resistencia a temperatura $T$ es:

$$\boxed{v_n^2 = 4kTRB}$$

Donde $k = 1.38 \times 10^{-23}$ J/K (constante de Boltzmann), $T$ en Kelvin, $R$ en ohms, $B$ en Hz. Esta formula es la base para calcular la potencia de ruido en todo receptor:

$$\boxed{N = kTB}$$

[analysis]

→ [[../ruido/fuentes-ruido|Fuentes de Ruido]]
→ [[../ruido/temperatura-ruido|Temperatura Equivalente de Ruido]]

## Ver Tambien

- [[../herramientas-matematicas/teorema-muestreo|Teorema de Muestreo]]
- [[../modulacion-digital/constelaciones|Constelaciones]]
- [[../ruido/fuentes-ruido|Fuentes de Ruido]]
- [[../ruido/temperatura-ruido|Temperatura de Ruido]]
- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]
- [[../conceptos-integradores/aportes-armstrong|Aportes de Armstrong]]
- [[../conceptos-integradores/aportes-fourier|Aportes de Fourier]]
