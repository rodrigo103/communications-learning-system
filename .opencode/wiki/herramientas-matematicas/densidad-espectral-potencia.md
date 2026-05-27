---
tags:
  - wiki/herramientas-matematicas
source_file: explicaciones_anki/unidad_02/carta_06_densidad-espectral-potencia.md
curso: Sistemas de Comunicaciones
unidad: 2
---

# Densidad Espectral de Potencia y Teorema de Wiener-Khinchin

> **Last verified:** 2025-11-22 | **Verified by:** [source]

## Definicion

La **densidad espectral de potencia (DEP)** $S_x(f)$ describe como se distribuye la potencia de una señal en el dominio de la frecuencia, con unidades [W/Hz] [source].

## Teorema de Wiener-Khinchin

La DEP y la funcion de autocorrelacion $R_x(\tau)$ forman un **par de transformadas de Fourier** [source]:

$$\boxed{S_x(f) = \mathcal{F}\{R_x(\tau)\} = \int_{-\infty}^{\infty} R_x(\tau) e^{-j2\pi f\tau} d\tau}$$

## Relacion con Autocorrelacion

Para señales deterministicas:

$$R_x(\tau) = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} x(t)x^*(t-\tau) dt$$

Para procesos aleatorios estacionarios:

$$R_x(\tau) = E[X(t)X^*(t-\tau)]$$

## Propiedades Fundamentales

- **Potencia total**: $P = R_x(0) = \int_{-\infty}^{\infty} S_x(f) df$ [source]
- **No negatividad**: $S_x(f) \geq 0$ para todo $f$ (es potencia)
- **Real**: $S_x(f)$ es siempre real (por ser $R_x(\tau)$ hermitiana)
- **Filtro LTI**: si $y(t) = x(t) * h(t)$, entonces $S_y(f) = |H(f)|^2 S_x(f)$

## Definicion a partir de Señal Truncada

Para $x_T(t)$ truncada a $[-T, T]$:

$$S_x(f) = \lim_{T \to \infty} \frac{|X_T(f)|^2}{2T}$$

## Ruido Blanco Gaussiano

El caso mas importante en comunicaciones [source]:

- **DEP**: $N_0 = kT$ [W/Hz] (convencion unilateral, $f > 0$)
- A $T = 290$K: $N_0 = 4.0 \times 10^{-21}$ W/Hz $= -174$ dBm/Hz
- **Autocorrelacion**: $R_n(\tau) = N_0 \delta(\tau)$ (ruido completamente incorrelado)
- **Wiener-Khinchin**: $\mathcal{F}\{N_0\delta(\tau)\} = N_0$ (DEP constante = espectro "blanco")
- **Potencia en banda B**: $P_{ruido} = N_0 \cdot B$

## Ejemplo: Señal Sinusoidal

Para $x(t) = A\cos(2\pi f_0 t + \phi)$:

- Autocorrelacion: $R_x(\tau) = \frac{A^2}{2}\cos(2\pi f_0 \tau)$
- DEP: $S_x(f) = \frac{A^2}{4}[\delta(f - f_0) + \delta(f + f_0)]$
- Toda la potencia concentrada en $\pm f_0$

## Analogia

La DEP es como un **analisis financiero de gastos**: el total mensual es la potencia total, y la DEP muestra como se distribuye: alimentacion (bajas frecuencias), transporte (frecuencias medias), entretenimiento (altas frecuencias). La autocorrelacion analiza patrones: si gastas mucho un dia, ¿es probable gastar mucho al siguiente? [analysis]

## Puntos Clave

- ✓ Dualidad DEP $\leftrightarrow$ autocorrelacion es fundamental [source]
- ✓ DEP plana $\leftrightarrow$ autocorrelacion delta (ruido blanco)
- ✓ Area bajo la DEP = potencia total = $R_x(0)$
- ✓ DEP requiere estacionariedad; para señales no estacionarias usar espectrograma

## Ver tambien

- [[herramientas-matematicas/teorema-parseval]]
- [[herramientas-matematicas/senales-energia-potencia]]
- [[herramientas-matematicas/teorema-convolucion]]
- [[ruido/ruido-blanco-banda-angosta]]
