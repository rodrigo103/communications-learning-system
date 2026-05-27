---
tags:
  - wiki/derivaciones
  - wiki/teoria-informacion
source_file: outputs/derivations/Shannon_Hartley_comprehensive_20251116.md
curso: Sistemas de Comunicaciones
unidad: 9
---

# Derivación del Teorema de Shannon-Hartley

> **Last verified:** 2025-11-16 | **Verified by:** source

## Enunciado

El teorema de Shannon-Hartley establece la capacidad máxima de un canal con ruido gaussiano blanco aditivo (AWGN):

$$\boxed{C = B \log_2(1 + \text{SNR}) \text{ bits/s}}$$

Equivalentemente:

$$\boxed{C = B \log_2\left(1 + \frac{P}{N_0 B}\right) \text{ bits/s}}$$

donde $C$ es la capacidad del canal, $B$ el ancho de banda, $P$ la potencia promedio de señal, y $N_0$ la densidad espectral de ruido [source].

## Modelo del canal

Canal AWGN: $Y(t) = X(t) + N(t)$, donde:
- $X(t)$: señal transmitida con potencia promedio $P$
- $N(t)$: ruido gaussiano blanco con DEP $N_0/2$
- $Y(t)$: señal recibida

## Derivación paso a paso

### Paso 1: Muestreo de Nyquist

Una señal limitada en banda a $B$ Hz se representa con $2B$ muestras/segundo [source]:

$$X(t) = \sum_n X[n] \cdot \text{sinc}(2Bt - n)$$

Esto permite analizar el canal continuo como $2B$ canales discretos paralelos por segundo.

### Paso 2: Capacidad como información mutua máxima

$$C = 2B \cdot \max_{f_X(x)} I(X;Y) \text{ bits/s}$$

### Paso 3: Información mutua para canal AWGN

$$I(X;Y) = h(Y) - h(Y|X) = h(Y) - h(N)$$

donde $h(\cdot)$ es la entropía diferencial [source].

### Paso 4: Entropía del ruido gaussiano

Para $N \sim \mathcal{N}(0, \sigma_N^2)$:

$$h(N) = \frac{1}{2}\log_2(2\pi e \sigma_N^2)$$

### Paso 5: Maximización de entropía

Teorema: entre todas las distribuciones con varianza fija, la gaussiana maximiza la entropía diferencial [source].

Con $E[Y^2] = P + \sigma_N^2$ y restricción de potencia, $h(Y)$ se maximiza cuando $X$ es gaussiana: $X \sim \mathcal{N}(0, P)$.

Entonces $Y \sim \mathcal{N}(0, P + \sigma_N^2)$ y:

$$\begin{aligned}
I(X;Y) &= \frac{1}{2}\log_2(2\pi e(P + \sigma_N^2)) - \frac{1}{2}\log_2(2\pi e \sigma_N^2) \\
&= \frac{1}{2}\log_2\left(1 + \frac{P}{\sigma_N^2}\right)
\end{aligned}$$

### Paso 6: Relacionar con parámetros físicos

$\sigma_N^2 = N_0 B$ (potencia de ruido en ancho de banda $B$), $\text{SNR} = P/(N_0 B)$:

$$C = 2B \cdot \frac{1}{2}\log_2(1 + \text{SNR}) = B\log_2(1 + \text{SNR})$$

## Casos límite

### SNR bajo (régimen limitado por potencia)
$$C \approx 1.44 B \cdot \text{SNR}$$
Capacidad lineal con SNR [analysis].

### SNR alto (régimen limitado por banda)
$$C \approx B \log_2(\text{SNR})$$
Crecimiento logarítmico con potencia.

### $B \to \infty$ (ancho de banda infinito)
$$\lim_{B\to\infty} C = \frac{P}{N_0 \ln 2} \approx 1.44 \frac{P}{N_0}$$

Capacidad finita incluso con ancho de banda infinito [source].

### $B \to 0$ (ancho de banda nulo)
$$\lim_{B\to 0} C = \frac{P}{N_0 \ln 2}$$

## Implicaciones fundamentales

1. **Existencia de códigos:** Para $R < C$, existe un código que permite transmisión con error arbitrariamente pequeño [source]
2. **Trade-off BW-potencia:** Se puede intercambiar ancho de banda por potencia
3. **Límite de Shannon:** $E_b/N_0 \geq \ln(2) \approx -1.59$ dB es el mínimo absoluto
4. **Gaussianidad óptima:** La distribución gaussiana de entrada alcanza la capacidad

## Códigos que se aproximan

- **Turbo codes** (1993): a ~0.5 dB del límite
- **LDPC**: usados en 5G, WiFi 6
- **Polar codes**: demostrados como capacity-achieving

## Ver también

- [[teoria-informacion/teorema-shannon-hartley]]
- [[teoria-informacion/capacidad-canal-shannon]]
- [[ruido/intercomparacion-sistemas]]
- [[teoria-informacion/entropia]]
- [[teoria-informacion/codificacion-canal]]
- [[conceptos-integradores/trade-off-bw-potencia]]
