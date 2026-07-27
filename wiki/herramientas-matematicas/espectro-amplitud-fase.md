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

## Producto Temporal y Traslacion Espectral

Multiplicar en el tiempo equivale a trasladar en frecuencia. Esta es la operacion fundamental detras de toda modulacion. La forma exponencial del seno y el coseno es la via mas limpia para entenderla.

### Formas Exponenciales (Euler)

$$\boxed{\cos(2\pi f_c t) = \frac{e^{+j2\pi f_c t} + e^{-j2\pi f_c t}}{2}}$$

$$\boxed{\sin(2\pi f_c t) = \frac{e^{+j2\pi f_c t} - e^{-j2\pi f_c t}}{2j}}$$

Ambas son sumas de dos exponenciales complejas. Una exponencial compleja pura $e^{+j2\pi f_c t}$ tiene un solo impulso en frecuencia, no dos:

| Tiempo | Frecuencia |
|--------|-----------|
| $1$ | $\delta(f)$ |
| $\cos(2\pi f_c t)$ | $\frac{1}{2}[\delta(f-f_c) + \delta(f+f_c)]$ |
| $\sin(2\pi f_c t)$ | $\frac{j}{2}[\delta(f+f_c) - \delta(f-f_c)]$ |
| $e^{+j2\pi f_c t}$ | $\delta(f - f_c)$ |
| $e^{-j2\pi f_c t}$ | $\delta(f + f_c)$ |

### La Propiedad Fundamental

Multiplicar cualquier señal por una exponencial compleja **corre** su espectro sin deformarlo:

$$\boxed{m(t) \cdot e^{+j2\pi f_c t} \;\xleftrightarrow{\mathcal{F}}\; M(f - f_c)}$$

$$\boxed{m(t) \cdot e^{-j2\pi f_c t} \;\xleftrightarrow{\mathcal{F}}\; M(f + f_c)}$$

Es una **traslacion pura**: el espectro $M(f)$ entero se desplaza a la posicion de la exponencial.

### Producto por Coseno

Aplicando Euler a la portadora coseno y usando la propiedad de traslacion:

$$m(t) \cdot \cos(2\pi f_c t) = m(t) \cdot \frac{e^{+j2\pi f_c t} + e^{-j2\pi f_c t}}{2}$$

$$m(t) \cdot e^{+j2\pi f_c t} \;\xleftrightarrow{\mathcal{F}}\; M(f - f_c)$$
$$m(t) \cdot e^{-j2\pi f_c t} \;\xleftrightarrow{\mathcal{F}}\; M(f + f_c)$$

Juntando ambos terminos (por linealidad de Fourier):

$$\boxed{m(t) \cdot \cos(2\pi f_c t) \;\xleftrightarrow{\mathcal{F}}\; \frac{1}{2}[M(f - f_c) + M(f + f_c)]}$$

El espectro $M(f)$ se **copia** en $+f_c$ y $-f_c$, cada copia reducida a la mitad de amplitud. Es una fotocopia exacta, sin distorsion. [analysis]

Cuando $m(t)$ es un solo tono ($\cos$ a frecuencia $f_m$), esto se reduce a la identidad trigonometrica $\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$, pero el principio es general y vale para **cualquier** $m(t)$.

### Producto por Seno

$$m(t) \cdot \sin(2\pi f_c t) = m(t) \cdot \frac{e^{+j2\pi f_c t} - e^{-j2\pi f_c t}}{2j}$$

Aplicando traslacion:

$$\boxed{m(t) \cdot \sin(2\pi f_c t) \;\xleftrightarrow{\mathcal{F}}\; \frac{1}{2j}[M(f - f_c) - M(f + f_c)]}$$

El signo menos en el segundo termino y el factor $1/j = e^{-j\pi/2}$ explican los desfasajes de $\pm 90^\circ$ del espectro de fase.

### Por Que No Hace Falta Convolucionar

Convolucionar con impulsos es trivial:

$$\delta(f - f_c) * M(f) = M(f - f_c)$$

Multiplicar por portadora en el tiempo → trasladar el espectro sumando $f_c$. Sin cuentas largas, sin integrales de convolucion. [analysis]

### El Rol de las Exponenciales en la Modulacion

Toda la teoria de modulacion descansa en estos dos hechos: [analysis]

1. La exponencial compleja $e^{j2\pi f_c t}$ corre el espectro a **una sola banda** ($+f_c$)
2. El coseno y el seno son la suma/resta de dos exponenciales → producen **dos bandas laterales** ($\pm f_c$)

Esto explica por que:
- **DSB/AM** usa coseno → dos bandas simetricas
- **SSB** suprime una exponencial (filtrando una banda lateral)
- **QAM/I-Q** usa coseno Y seno simultaneamente → dos canales ortogonales en la misma frecuencia
- **Receptor superheterodino** baja de RF a IF con la misma propiedad al reves

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
