---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
unidad: 2-3
---

# David Hilbert y sus Aportes a los Sistemas de Comunicaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

David Hilbert (1862–1943) fue un matematico aleman, uno de los mas influyentes del siglo XX. Aunque su fama principal viene de los fundamentos de la geometria y los 23 problemas de Hilbert, en comunicaciones su nombre esta asociado a la **transformada de Hilbert**, una herramienta esencial para el procesamiento de señales pasabanda.

## Transformada de Hilbert

La transformada de Hilbert $\hat{x}(t)$ de una señal $x(t)$ aplica un desfasaje de $-90^\circ$ a cada componente frecuencial positiva (y $+90^\circ$ a las negativas), sin alterar la amplitud:

$$\boxed{\hat{x}(t) = \mathcal{H}\{x(t)\} = \frac{1}{\pi} \int_{-\infty}^{\infty} \frac{x(\tau)}{t - \tau} d\tau}$$

En el dominio de la frecuencia:

$$\boxed{\hat{X}(f) = -j \cdot \text{sgn}(f) \cdot X(f)}$$

Donde $\text{sgn}(f) = +1$ para $f > 0$, $-1$ para $f < 0$. Esto es un **filtro pasa-todo con fase $-90^\circ$**. [analysis]

### Propiedades Clave

| Propiedad | Expresion |
|-----------|-----------|
| **Transformada del coseno** | $\mathcal{H}\{\cos(\omega t)\} = \sin(\omega t)$ |
| **Transformada del seno** | $\mathcal{H}\{\sin(\omega t)\} = -\cos(\omega t)$ |
| **Doble transformada** | $\mathcal{H}\{\mathcal{H}\{x(t)\}\} = -x(t)$ |
| **Señal + su Hilbert** | Ortogonales: $\int x(t) \hat{x}(t) dt = 0$ |
| **Bedrosian** | $\mathcal{H}\{a(t)\cos(\phi(t))\} = a(t)\sin(\phi(t))$ si espectros no solapan |

[analysis]

## Mapa de Aportes al Curso

### Unidad 2 — Señal Analitica

La señal analitica $x_a(t)$ se construye combinando la señal original con su transformada de Hilbert como parte imaginaria:

$$\boxed{x_a(t) = x(t) + j \hat{x}(t)}$$

**Para que sirve:** [analysis]
- Representa una señal real como una señal compleja de banda unilateral (solo frecuencias positivas)
- Permite definir **envolvente** y **fase instantanea** de cualquier señal pasabanda:

$$\boxed{a(t) = |x_a(t)| = \sqrt{x^2(t) + \hat{x}^2(t)}}$$

$$\boxed{\phi(t) = \angle x_a(t) = \arctan\left(\frac{\hat{x}(t)}{x(t)}\right)}$$

Esto es esencial para demodular señales AM y FM, analizar distorsion, y diseñar receptores I/Q.

→ [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]

### Unidad 3 — Generacion de SSB (Metodo de Fase / Weaver)

La BLU (SSB) puede generarse sin filtros fisicos usando la transformada de Hilbert. El **metodo de fase** (o de Weaver en su version digital):

$$\boxed{s_{SSB}(t) = m(t) \cos(2\pi f_c t) \mp \hat{m}(t) \sin(2\pi f_c t)}$$

Donde $\mp$ selecciona USB ($-$) o LSB ($+$). [analysis]

Este metodo es ideal para implementaciones digitales (SDR) donde el filtro de Hilbert se aproxima con un filtro FIR. [analysis]

→ [[../modulacion-analogica/modulacion-ssb|Modulacion SSB (BLU)]]

### Unidad 4 — Representacion de FM/PM

La envolvente y fase instantanea permiten analizar señales de FM y PM sin necesidad de demodular:

$$\boxed{s(t) = A_c \cos[2\pi f_c t + \phi(t)]}$$

Donde $\phi(t)$ contiene la informacion modulada y se extrae via $x_a(t)$. [analysis]

→ [[../modulacion-analogica/fm-vs-pm|FM vs PM]]

### Unidad 7 — Ruido Pasabanda

El ruido de banda angosta se modela usando la transformada de Hilbert:

$$\boxed{n(t) = n_I(t) \cos(2\pi f_c t) - n_Q(t) \sin(2\pi f_c t)}$$

Donde $n_I$ y $n_Q$ son componentes en fase y cuadratura, relacionadas via Hilbert en la representacion de envolvente compleja. Esto es fundamental para calcular SNR en receptores coherentes. [analysis]

→ [[../ruido/ruido-banda-angosta|Ruido de Banda Angosta]]

## Ver Tambien

- [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]
- [[../herramientas-matematicas/senales-energia-potencia|Señales de Energia y Potencia]]
- [[../modulacion-analogica/modulacion-ssb|Modulacion SSB]]
- [[../modulacion-analogica/fm-vs-pm|FM vs PM]]
- [[../ruido/ruido-banda-angosta|Ruido de Banda Angosta]]
- [[../conceptos-integradores/aportes-fourier|Aportes de Fourier]]
- [[../conceptos-integradores/aportes-parseval|Aportes de Parseval]]
- [[../conceptos-integradores/pioneros-comunicaciones|Pioneros de las Comunicaciones]]
