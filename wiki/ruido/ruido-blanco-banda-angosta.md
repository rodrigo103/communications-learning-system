---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_33_ruido-blanco.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Ruido Blanco y Ruido de Banda Angosta

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_07/carta_33_ruido-blanco]]]

## Ruido Blanco

El ruido blanco tiene [[../herramientas-matematicas/densidad-espectral-potencia|densidad espectral de potencia]] (DEP) constante para todas las frecuencias:

$$\boxed{S_n(f) = \frac{N_0}{2} \quad \text{(bilateral)}, \qquad N_0 = kT \quad \text{(unilateral)}}$$

**Propiedades:** [source — [[../../explicaciones_anki/unidad_07/carta_33_ruido-blanco]]]
- Autocorrelación: $R_n(\tau) = N_0 \delta(\tau)$ (decorrelación total)
- Proceso estacionario, gaussiano (AWGN)
- Potencia infinita en banda infinita → siempre se filtra en sistemas reales

En un sistema con ancho de banda $B$, la potencia de ruido es:

$$\boxed{N = N_0 B = kTB}$$

A $T = 290$ K: $N_0 = -174$ dBm/Hz.

## Ruido de Banda Angosta

Cuando el ruido blanco pasa por un filtro pasabanda centrado en $f_c$, con ancho de banda $B \ll f_c$, se obtiene ruido de banda angosta. Su representación matemática es fundamental para analizar el efecto del ruido en receptores. [source — [[../../explicaciones_anki/unidad_07/carta_33_ruido-blanco]]]

### Representación I-Q

$$\boxed{n(t) = x(t)\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)}$$

donde $x(t)$ e $y(t)$ son las componentes en fase y cuadratura, con propiedades:
- Procesos gaussianos de media cero
- Misma varianza: $\sigma_x^2 = \sigma_y^2 = \sigma_n^2$
- Independientes entre sí en cada instante

### Representación Envolvente-Fase

$$n(t) = R(t)\cos[2\pi f_c t + \phi(t)]$$

Donde:
- $R(t) = \sqrt{x^2(t) + y^2(t)}$ → distribución de **Rayleigh**
- $\phi(t) = \arctan(y/x)$ → distribución **uniforme** en $[0, 2\pi]$

**Distribución de Rayleigh:**

$$\boxed{p_R(r) = \frac{r}{\sigma^2}\exp\left(-\frac{r^2}{2\sigma^2}\right), \quad r \geq 0}$$

## Uso en Análisis de Receptores

Esta representación permite analizar:
- **Receptores AM**: el ruido afecta la envolvente detectada
- **Receptores FM**: el ruido produce fluctuaciones de fase/frecuencia
- **Efecto umbral**: cuando la envolvente del ruido supera a la portadora

Ver [[../ruido/snr-modulacion-lineal]] y [[../ruido/efecto-umbral]] para el análisis detallado. [analysis]

## Ver también

- [[../ruido/fuentes-ruido]] — Origen físico del ruido blanco
- [[../herramientas-matematicas/densidad-espectral-potencia]] — DEP como herramienta de análisis
- [[../ruido/factor-ruido-temperatura]] — Cuantificación del ruido agregado
- [[aclaracion-densidad-espectral-ruido]] — Aclaracion sobre densidad espectral de ruido
