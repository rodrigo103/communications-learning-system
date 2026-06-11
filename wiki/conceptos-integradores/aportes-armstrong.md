---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
unidad: 3-4
---

# Edwin Howard Armstrong y sus Aportes a los Sistemas de Comunicaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

Edwin Howard Armstrong (1890–1954) fue un ingeniero e inventor estadounidense, considerado uno de los mas prolificos en la historia de las radiocomunicaciones. Sus tres grandes invenciones —el receptor superheterodino, el circuito regenerativo, y la modulacion FM— transformaron la radio para siempre.

## Mapa de Aportes

### Unidad 3 — Receptor Superheterodino (1918)

Armstrong invento el receptor superheterodino, la arquitectura de receptor mas utilizada hasta hoy. La idea central es convertir cualquier frecuencia recibida a una **frecuencia intermedia (IF)** fija, donde el filtrado y la amplificacion son mas faciles de realizar:

$$\boxed{f_{IF} = |f_{RF} - f_{LO}|}$$

Ventajas del superheterodino: [analysis]
- Filtrado en IF es mas selectivo que en RF
- Amplificacion en IF es mas estable y de mayor ganancia
- La frecuencia imagen se rechaza con filtros de preseleccion

→ [[../modulacion-analogica/receptor-superheterodino|Receptor Superheterodino]]

### Unidad 4 — Modulacion de Frecuencia (FM) (1933)

Armstrong invento y demostro la modulacion FM, probando que ofrecia una inmunidad al ruido muy superior a AM. En FM, la frecuencia instantanea de la portadora varia proporcionalmente a la señal moduladora $m(t)$:

$$\boxed{s_{FM}(t) = A_c \cos\left[2\pi f_c t + 2\pi k_f \int_0^t m(\tau) d\tau\right]}$$

#### Metodo Indirecto de Armstrong (NBFM → WBFM)

Armstrong desarrollo un metodo practico para generar FM de banda ancha (WBFM) sin necesidad de un VCO lineal:

1. Generar **FM de banda angosta (NBFM)** mediante un modulador de fase con $m(t)$ integrada
2. **Multiplicar la frecuencia** para aumentar la desviacion
3. **Mezclar** con un oscilador para ajustar la portadora final

[analysis]

→ [[../modulacion-analogica/fm-vs-pm|FM vs PM]]
→ [[../modulacion-analogica/fm-banda-angosta|FM de Banda Angosta]]
→ [[../modulacion-analogica/ancho-banda-carson|Regla de Carson para FM]]

### La Lucha Legal por FM

Armstrong batallo legalmente contra RCA (su antiguo empleador) durante años para proteger su patente de FM. La FCC inicialmente favorecio la TV sobre la radio FM, desplazando la banda de FM de 42-50 MHz a 88-108 MHz, lo que dejo obsoletos los primeros equipos. Armstrong nunca vio el exito comercial masivo de FM; se suicido en 1954. [analysis]

## Ver Tambien

- [[../modulacion-analogica/receptor-superheterodino|Receptor Superheterodino]]
- [[../modulacion-analogica/fm-vs-pm|FM vs PM]]
- [[../modulacion-analogica/fm-banda-angosta|FM de Banda Angosta]]
- [[../modulacion-analogica/ancho-banda-carson|Regla de Carson]]
- [[../modulacion-analogica/modulador-fm|Moduladores y Detectores FM]]
- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]
- [[../conceptos-integradores/aportes-nyquist|Aportes de Nyquist]]
