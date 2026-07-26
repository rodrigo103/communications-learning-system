---
tags:
  - wiki/herramientas-matematicas
curso: Sistemas de Comunicaciones
---

# Espectro de Amplitud y Fase

> **Last verified:** 2026-07-19 | **Verified by:** analysis

Toda transformada de Fourier $X(f)$ es un numero complejo. Para graficarla se separa en dos representaciones independientes:

$$\boxed{X(f) = |X(f)| \cdot e^{j\phi(f)}}$$

- **Espectro de amplitud**: $|X(f)|$ — magnitud vs frecuencia
- **Espectro de fase**: $\phi(f) = \arctan\left(\frac{\text{Im}\{X(f)\}}{\text{Re}\{X(f)\}}\right)$ — angulo vs frecuencia

A continuacion se desarrolla el ejemplo concreto del seno y el coseno para entender como se calculan ambas representaciones.

---

## Transformada del Coseno

$$\boxed{\mathcal{F}\{\cos(2\pi f_0 t)\} = \frac{1}{2}[\delta(f - f_0) + \delta(f + f_0)]}$$

### Espectro de Amplitud

Para calcular la magnitud se usa $|X(f)| = \sqrt{a^2 + b^2}$, donde $X(f) = a + jb$:

**En $f = +f_0$:**

$$X(+f_0) = \frac{1}{2} = \frac{1}{2} + j0$$

- $a = 1/2$, $b = 0$
- $|X(+f_0)| = \sqrt{(1/2)^2 + 0^2} = \boxed{1/2}$

**En $f = -f_0$:**

$$X(-f_0) = \frac{1}{2} = \frac{1}{2} + j0$$

- $a = 1/2$, $b = 0$
- $|X(-f_0)| = \sqrt{(1/2)^2 + 0^2} = \boxed{1/2}$

Dos impulsos de magnitud $1/2$ en $\pm f_0$:

```
          |X(f)|
           |
      1/2  ●           ●  1/2
           |           |
      -----+-----------+----- f
          -f₀          +f₀
```

### Espectro de Fase

Para cada frecuencia se escribe $X(f)$ en la forma $a + jb$ y se calcula $\phi = \arctan(b/a)$:

**En $f = +f_0$:**

$$X(+f_0) = \frac{1}{2} = \frac{1}{2} + j0$$

- $a = 1/2$, $b = 0$
- $b = 0, a > 0$ → $\boxed{\phi = 0^\circ}$

**En $f = -f_0$:**

$$X(-f_0) = \frac{1}{2} = \frac{1}{2} + j0$$

- $a = 1/2$, $b = 0$
- $b = 0, a > 0$ → $\boxed{\phi = 0^\circ}$

Ambos terminos son reales puros y positivos: la energia esta concentrada en el eje real, sin componente imaginaria.

```
          φ(f)
           |
       0°  ●-----------●  0°
           |
      -----+-----------+----- f
          -f₀          +f₀
```

---

## Transformada del Seno

$$\boxed{\mathcal{F}\{\sin(2\pi f_0 t)\} = \frac{j}{2}[\delta(f + f_0) - \delta(f - f_0)]}$$

Expandiendo la expresion:

$$X(f) = \frac{j}{2}\delta(f + f_0) - \frac{j}{2}\delta(f - f_0)$$

### Espectro de Amplitud

Para calcular la magnitud se usa $|X(f)| = \sqrt{a^2 + b^2}$, donde $X(f) = a + jb$:

**En $f = +f_0$:**

$$X(+f_0) = -\frac{j}{2} = 0 - j\frac{1}{2}$$

- $a = 0$, $b = -1/2$
- $|X(+f_0)| = \sqrt{0^2 + (-1/2)^2} = \boxed{1/2}$

**En $f = -f_0$:**

$$X(-f_0) = +\frac{j}{2} = 0 + j\frac{1}{2}$$

- $a = 0$, $b = +1/2$
- $|X(-f_0)| = \sqrt{0^2 + (1/2)^2} = \boxed{1/2}$

Resultado: dos impulsos de magnitud $1/2$ en $\pm f_0$, identico al coseno:

```
          |X(f)|
           |
      1/2  ●           ●  1/2
           |           |
      -----+-----------+----- f
          -f₀          +f₀
```

### Espectro de Fase

Para cada frecuencia se escribe $X(f)$ en la forma $a + jb$ y se calcula $\phi = \arctan(b/a)$:

**En $f = +f_0$:**

$$X(+f_0) = -\frac{j}{2} = 0 - j\frac{1}{2}$$

- $a = 0$, $b = -1/2$
- $b < 0$ con $a = 0$ → $\boxed{\phi = -90^\circ = -\pi/2}$

**En $f = -f_0$:**

$$X(-f_0) = +\frac{j}{2} = 0 + j\frac{1}{2}$$

- $a = 0$, $b = +1/2$
- $b > 0$ con $a = 0$ → $\boxed{\phi = +90^\circ = +\pi/2}$

```
          φ(f)
           |
     +90°  ●
           |
      -----+-----------+----- f
          -f₀          +f₀
           |           ●  -90°
```

### Metodo Alternativo con Euler

Recordando que $j = e^{j\pi/2}$ y $-j = e^{-j\pi/2}$:

$$X(f) = \frac{1}{2}\left[e^{j\pi/2}\delta(f + f_0) + e^{-j\pi/2}\delta(f - f_0)\right]$$

Lectura directa: la fase en $-f_0$ es $+\pi/2$ y en $+f_0$ es $-\pi/2$.

---

## Comparacion Lado a Lado

| | Coseno | Seno |
|--|--------|------|
| **Señal** | Par: $\cos(-x) = \cos x$ | Impar: $\sin(-x) = -\sin x$ |
| **Transformada** | Real pura | Imaginaria pura |
| **Amplitud en $\pm f_0$** | $1/2$ | $1/2$ |
| **Fase en $+f_0$** | $0^\circ$ | $-90^\circ$ |
| **Fase en $-f_0$** | $0^\circ$ | $+90^\circ$ |

```
  Amplitud (ambas iguales)       Fase coseno      Fase seno
        |                           |                |
    1/2 ●        ● 1/2          0°  ●------● 0°   +90° ●
        |        |                  |                |
   -----+--------+-----        -----+--------+    -----+--------+-----
       -f₀      +f₀              -f₀      +f₀      -f₀ ●      +f₀
                                                             -90°
```

---

## Por Que la Diferencia

La diferencia de fase entre seno y coseno refleja una propiedad general de Fourier:

- **Funcion par** $x(-t) = x(t)$ → $X(f)$ es **real pura** → fase = $0^\circ$ o $180^\circ$
- **Funcion impar** $x(-t) = -x(t)$ → $X(f)$ es **imaginaria pura** → fase = $\pm 90^\circ$

El seno esta $90^\circ$ desfasado respecto al coseno en el tiempo. Ese desfasaje temporal se traduce en fases opuestas en $\pm f_0$ en el dominio frecuencial. La informacion es la misma; cambia como se representa. [analysis]

---

## Ver Tambien

- [[../herramientas-matematicas/transformada-fourier|Transformada de Fourier]]
- [[../herramientas-matematicas/serie-fourier|Serie de Fourier]]
- [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]]
- [[../herramientas-matematicas/teorema-convolucion|Teorema de Convolucion]]
- [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]]
- [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]
