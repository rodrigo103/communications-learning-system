---
tags:
  - wiki/derivaciones
  - wiki/herramientas-matematicas
source_file: outputs/derivations/parsevals_theorem_comprehensive.md
curso: Sistemas de Comunicaciones
unidad: 2
---

# Derivación del Teorema de Parseval

> **Last verified:** 2025-11-15 | **Verified by:** source

## Enunciado del teorema

Para una señal $x(t)$ con transformada de Fourier $X(f)$:

$$\boxed{\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df}$$

Alternativamente con frecuencia angular $\omega = 2\pi f$:

$$\int_{-\infty}^{\infty} |x(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} |X(\omega)|^2 d\omega$$

**Interpretación física:** La energía total de una señal es la misma calculada en el dominio del tiempo o en el dominio de la frecuencia. La transformada de Fourier conserva la energía [source].

## Derivación paso a paso

### Paso 1: Expresar la energía

$$E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} x(t) x^*(t) dt$$

### Paso 2: Sustituir $x^*(t)$ por la transformada inversa

$$x^*(t) = \int_{-\infty}^{\infty} X^*(f) e^{-j2\pi ft} df$$

### Paso 3: Intercambiar orden de integración

$$E = \int_{-\infty}^{\infty} X^*(f) \left[ \int_{-\infty}^{\infty} x(t) e^{-j2\pi ft} dt \right] df$$

### Paso 4: Reconocer la transformada de Fourier

El término entre corchetes es exactamente $X(f)$:

$$E = \int_{-\infty}^{\infty} X^*(f) X(f) df = \int_{-\infty}^{\infty} |X(f)|^2 df$$

Con esto queda demostrado: la energía se conserva [analysis].

### Forma generalizada (Plancherel)

$$\int_{-\infty}^{\infty} x(t) y^*(t) dt = \int_{-\infty}^{\infty} X(f) Y^*(f) df$$

## Formas del teorema

### Series de Fourier (señales periódicas)

$$\frac{1}{T_0}\int_0^{T_0} |x(t)|^2 dt = \sum_{n=-\infty}^{\infty} |c_n|^2$$

### Tiempo discreto (DTFT)

$$\sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega$$

### DFT (N puntos)

$$\sum_{n=0}^{N-1} |x[n]|^2 = \frac{1}{N}\sum_{k=0}^{N-1} |X[k]|^2$$

## Densidad espectral de energía

$|X(f)|^2$ se denomina **densidad espectral de energía (ESD)**. Representa la distribución de energía por unidad de frecuencia. $|X(f)|^2 df$ es la energía contenida en la banda $[f, f+df]$ [source].

## Aplicaciones en comunicaciones

1. **Cálculo de SNR:** La energía de señal puede calcularse en el dominio más conveniente
2. **Diseño de filtros:** El filtro adaptado maximiza SNR aprovechando Parseval
3. **Ancho de banda:** Encontrar $B$ tal que $\int_{-B}^{B} |X(f)|^2 df = 0.95 \cdot E_{total}$
4. **Densidad espectral de potencia:** Teorema de Wiener-Khinchin: $S_x(f) = \mathcal{F}\{R_x(\tau)\}$
5. **Análisis de modulación:** La energía de una señal modulada puede calcularse más fácilmente en frecuencia [analysis]

### Ejemplo: filtro adaptado

Para señal $s(t)$ en ruido blanco con DEP $N_0/2$:

$$\text{SNR}_{max} = \frac{2E_s}{N_0}$$

donde $E_s$ se calcula con Parseval en tiempo o frecuencia.

## Conexión con principio de incertidumbre

Parseval está relacionado con la desigualdad de incertidumbre tiempo-frecuencia:

$$\Delta t \cdot \Delta f \geq \frac{1}{4\pi}$$

Ambos resultados derivan de propiedades fundamentales de la transformada de Fourier [analysis].

## Ver también

- [[herramientas-matematicas/teorema-parseval]]
- [[herramientas-matematicas/densidad-espectral-potencia]]
- [[herramientas-matematicas/senales-energia-potencia]]
- [[herramientas-matematicas/serie-fourier]]
- [[herramientas-matematicas/transformada-fourier]]
- [[herramientas-matematicas/teorema-wiener-khinchin]]
