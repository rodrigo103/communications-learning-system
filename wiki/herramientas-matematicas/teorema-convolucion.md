---
tags:
  - wiki/herramientas-matematicas
source_file: explicaciones_anki/unidad_02/carta_07_teorema_convolucion.md
curso: Sistemas de Comunicaciones
unidad: 2
---

# Teorema de Convolucion

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Enunciado

El Teorema de Convolucion establece una dualidad fundamental entre los dominios del tiempo y la frecuencia [source]:

$$\boxed{y(t) = x(t) * h(t) \quad \Leftrightarrow \quad Y(f) = X(f) \cdot H(f)}$$

La **convolucion en el tiempo equivale a multiplicacion en frecuencia**, y viceversa:

$$x(t) \cdot h(t) \quad \Leftrightarrow \quad X(f) * H(f)$$

## Definicion de Convolucion

$$y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau$$

## Derivacion

Partiendo de la definicion y aplicando la transformada de Fourier:

$$Y(f) = \int_{-\infty}^{\infty} x(\tau) \left[\int_{-\infty}^{\infty} h(u) e^{-j2\pi f(u+\tau)} du\right] d\tau$$

Intercambiando integracion (Fubini) y haciendo cambio de variable $u = t - \tau$:

$$Y(f) = \int_{-\infty}^{\infty} x(\tau) e^{-j2\pi f\tau} d\tau \cdot \int_{-\infty}^{\infty} h(u) e^{-j2\pi fu} du = X(f) \cdot H(f)$$

## Significado en Sistemas LTI

- $Y(f)$: espectro de la señal de salida
- $X(f)$: espectro de la señal de entrada
- $H(f)$: **funcion de transferencia** = respuesta en frecuencia del sistema [source]
- $h(t)$: **respuesta al impulso** (inversa de Fourier de $H(f)$)

Un sistema LTI queda completamente caracterizado por $h(t)$ o $H(f)$ [source].

## Importancia Practica

La multiplicacion en frecuencia es computacionalmente mas simple que la convolucion en tiempo. Esto permite:
- Analizar filtros en el dominio frecuencial donde $H(f)$ actua como "ecualizador" que amplifica o atenua cada frecuencia [analysis]
- Implementar filtrado eficiente via FFT: multiplicar en frecuencia en lugar de convolucionar en tiempo
- Analizar efectos de canales con multitrayecto en comunicaciones

## Ejemplo: Filtro RC Pasa-Bajos

Para $H(f) = \frac{1}{1 + jf/f_c}$:

| Armonico | Frecuencia | $|H(f)|$ | Efecto |
|----------|------------|---------|--------|
| Fundamental | 500 Hz | 0.894 | Leve atenuacion |
| 3er armonico | 1500 Hz | 0.555 | Atenuacion moderada |
| 5to armonico | 2500 Hz | 0.371 | Atenuacion significativa |

El filtro convierte progresivamente una señal cuadrada en sinusoidal atenuando armonicos superiores [analysis].

## Aplicacion: Canal con Multitrayecto

Para $h(t) = \delta(t) + 0.5\delta(t - 50\text{ns})$:

$$H(f) = 1 + 0.5e^{-j2\pi f \cdot 50\text{ns}}$$

Algunas frecuencias sufren interferencia destructiva ($|H(f)| \approx 0.5$), otras constructiva ($|H(f)| \approx 1.5$), produciendo **desvanecimiento selectivo en frecuencia** [source].

## Puntos Clave

- ✓ Convolucion en tiempo = Multiplicacion en frecuencia [source]
- ✓ La multiplicacion en frecuencia es mas simple que la convolucion
- ✓ El teorema SOLO aplica para sistemas LTI [source]
- ✓ $h(t)$ y $H(f)$ caracterizan completamente un sistema LTI

## Ver tambien

- [[herramientas-matematicas/teorema-parseval]]
- [[herramientas-matematicas/transformada-hilbert]]
- [[herramientas-matematicas/densidad-espectral-potencia]]
- [[modulacion-analogica/receptor-superheterodino]]
