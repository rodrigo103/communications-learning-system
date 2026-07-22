---
tags:
  - wiki/conceptos-integradores
curso: Sistemas de Comunicaciones
unidad: 2
---

# Joseph Fourier y sus Aportes a los Sistemas de Comunicaciones

> **Last verified:** 2026-06-10 | **Verified by:** analysis

Jean-Baptiste Joseph Fourier (1768–1830) fue un matematico y fisico frances cuyo trabajo sobre la descomposicion de funciones periodicas en series trigonometricas se convirtio en la **herramienta matematica fundamental** de las comunicaciones modernas. Todas las tecnicas de modulacion, filtrado y analisis espectral del curso dependen de sus ideas.

## La Transformada de Fourier

Toda señal $x(t)$ puede representarse como una superposicion de exponenciales complejas:

$$\boxed{X(f) = \int_{-\infty}^{\infty} x(t) e^{-j2\pi ft} dt}$$

$$\boxed{x(t) = \int_{-\infty}^{\infty} X(f) e^{j2\pi ft} df}$$

### ¿Por que es el pilar de TODO el curso?

El analisis en frecuencia permite: [analysis]
- Entender el **espectro** de cada modulacion (AM, DSB, SSB, FM, QAM, OFDM)
- Diseñar **filtros** que seleccionen bandas de frecuencia
- Calcular **ancho de banda** y verificar cumplimiento de regulaciones
- Analizar los efectos del **ruido** sobre señales moduladas

## Serie de Fourier (señales periodicas)

Para $x(t)$ periodica con periodo $T_0$:

$$\boxed{x(t) = \sum_{n=-\infty}^{\infty} c_n e^{j2\pi n f_0 t}}$$

Donde $f_0 = 1/T_0$ y los coeficientes $c_n$ representan el espectro discreto de la señal.

Esto es esencial para entender: señales de reloj digital, trenes de pulsos en PAM/PCM, y cualquier señal periodica en comunicaciones.

## Propiedades Fundamentales

| Propiedad       | Tiempo                 | Frecuencia      |        |           |     |        |
| --------------- | ---------------------- | --------------- | ------ | --------- | --- | ------ |
| **Linealidad**  | $a x_1 + b x_2$        | $a X_1 + b X_2$ |        |           |     |        |
| **Convolucion** | $x_1 * x_2$            | $X_1 \cdot X_2$ |        |           |     |        |
| **Modulacion**  | $x(t) e^{j2\pi f_c t}$ | $X(f - f_c)$    |        |           |     |        |
| **Escalado**    | $x(at)$                | $\frac{1}{      | a      | } X(f/a)$ |     |        |
| **Parseval**    | $\int                  | x               | ^2 dt$ | $\int     | X   | ^2 df$ |

La propiedad de **modulacion** (traslacion en frecuencia) es la que hace posible toda modulacion analogica y digital: multiplicar por una portadora desplaza el espectro de la señal a la frecuencia deseada. [analysis]

## De Fourier a la Ingenieria Moderna

Sin la transformada de Fourier no existirian: [analysis]
- Ecualizadores y filtros
- Analizadores de espectro
- OFDM (basado enteramente en FFT/IFFT)
- Compresion de audio/video (JPEG, MP3 — via DCT, una variante de Fourier)
- Software Defined Radio (SDR)

→ [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]]
→ [[../herramientas-matematicas/teorema-convolucion|Teorema de Convolucion]]
→ [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]]

## Ver Tambien

- [[../herramientas-matematicas/teorema-parseval|Teorema de Parseval]]
- [[../herramientas-matematicas/teorema-convolucion|Teorema de Convolucion]]
- [[../herramientas-matematicas/densidad-espectral-potencia|Densidad Espectral de Potencia]]
- [[../herramientas-matematicas/transformada-hilbert|Transformada de Hilbert]]
- [[../conceptos-integradores/aportes-shannon|Aportes de Shannon]]
- [[../conceptos-integradores/aportes-nyquist|Aportes de Nyquist]]
