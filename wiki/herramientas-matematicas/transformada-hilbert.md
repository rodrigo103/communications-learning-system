---
tags:
  - wiki/herramientas-matematicas
source_file: explicaciones_anki/unidad_02/carta_08_transformada_hilbert.md
curso: Sistemas de Comunicaciones
unidad: 2
---

# Transformada de Hilbert

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]

## Definicion

La Transformada de Hilbert $\hat{x}(t)$ de una señal $x(t)$ produce un **desfasaje de -90° para todas las frecuencias positivas** [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]:

$$\hat{x}(t) = \mathcal{H}\{x(t)\} = \frac{1}{\pi} \text{P.V.} \int_{-\infty}^{\infty} \frac{x(\tau)}{t-\tau} d\tau$$

P.V. denota el **valor principal de Cauchy** para manejar la singularidad en $\tau = t$.

## Respuesta en Frecuencia

La Transformada de Hilbert es un sistema LTI con funcion de transferencia [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]:

$$\boxed{H(f) = -j \cdot \text{sgn}(f) = \begin{cases} -j & f > 0 \\ 0 & f = 0 \\ +j & f < 0 \end{cases}}$$

Caracteristicas:
- $|H(f)| = 1$ para $f \neq 0$: **conserva la energia/amplitud**
- Fase = $-90°$ para $f > 0$, $+90°$ para $f < 0$
- Elimina la componente DC ($f = 0$)
- Es una convolucion con $\frac{1}{\pi t}$: $\hat{x}(t) = x(t) * \frac{1}{\pi t}$

## Pares Fundamentales

$$\boxed{\mathcal{H}\{A\cos(2\pi f_0 t + \phi)\} = A\sin(2\pi f_0 t + \phi)}$$

$$\boxed{\mathcal{H}\{A\sin(2\pi f_0 t + \phi)\} = -A\cos(2\pi f_0 t + \phi)}$$

| Señal $x(t)$ | Transformada $\hat{x}(t)$ |
|--------------|---------------------------|
| $\cos(\omega t)$ | $\sin(\omega t)$ |
| $\sin(\omega t)$ | $-\cos(\omega t)$ |
| $\delta(t)$ | $1/(\pi t)$ |
| $1/(\pi t)$ | $-\delta(t)$ |

## Señal Analitica

La señal analitica se construye combinando la señal original con su transformada [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]:

$$x_a(t) = x(t) + j\hat{x}(t)$$

Propiedad clave: su espectro solo contiene **frecuencias positivas**:

$$X_a(f) = \begin{cases} 2X(f) & f > 0 \\ X(0) & f = 0 \\ 0 & f < 0 \end{cases}$$

Esto elimina la redundancia de frecuencias negativas en señales reales.

## Aplicaciones en Comunicaciones

### 1. Generacion de SSB (Banda Lateral Unica)

La señal SSB se genera usando la transformada de Hilbert [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]:

$$s_{SSB}(t) = m(t)\cos(2\pi f_c t) \mp \hat{m}(t)\sin(2\pi f_c t)$$

- Signo $(-)$: USB (Upper Sideband)
- Signo $(+)$: LSB (Lower Sideband)

Ver [[../modulacion-analogica/modulacion-ssb]] para detalles.

### 2. Deteccion de Envolvente en AM

Para una señal AM $r(t)$, la envolvente se extrae via:

$$|r_a(t)| = |r(t) + j\hat{r}(t)|$$

### 3. Frecuencia Instantanea en FM

Para una señal FM $s(t)$, la frecuencia instantanea se calcula como:

$$f_i(t) = \frac{1}{2\pi}\frac{d}{dt}\angle s_a(t)$$

## Analogia

La Transformada de Hilbert es como ver una onda desde una posicion rotada 90°. Ambas vistas describen la misma onda pero desde perspectivas ortogonales. La señal analitica combina ambas vistas para una descripcion completa [analysis].

## Puntos Clave

- ✓ NO cambia el contenido de frecuencias, solo las fases [source — [[../../explicaciones_anki/unidad_02/carta_08_transformada_hilbert]]]
- ✓ $|H(f)| = 1$ para $f \neq 0$: conserva energia
- ✓ Solo definida para señales reales
- ✓ La señal analitica elimina frecuencias negativas

## Ver tambien

- [[../herramientas-matematicas/teorema-convolucion]]
- [[../modulacion-analogica/modulacion-ssb]]
- [[../introduccion/modelo-shannon]]
