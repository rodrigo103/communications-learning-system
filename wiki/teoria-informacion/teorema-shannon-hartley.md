---
tags:
  - wiki/teoria-informacion
source_file: explicaciones_anki/unidad_09/carta_45_teorema-shannon-hartley.md
curso: Sistemas de Comunicaciones
unidad: 9
---

# Teorema de Shannon-Hartley

> **Last verified:** 2025-11-16 | **Verified by:** source

## Enunciado

El **Teorema de Shannon-Hartley** establece la **capacidad maxima** de un canal de comunicacion con ruido gaussiano blanco aditivo (AWGN): [source]

$$\boxed{C = B \log_2\left(1 + \frac{S}{N}\right) \quad \text{[bits/s]}}$$

Puntos clave:
- $B$: ancho de banda (Hz) — dimension "espacial" del canal
- $S/N$: relacion senal a ruido (lineal) — calidad del canal
- $\log_2(1 + S/N)$: bits por uso del canal (por dimension)

## Implicaciones Fundamentales

1. **Limite teorico estricto**: tasa maxima a la cual es posible comunicacion libre de errores. Ningun esquema puede superar $C$. [source]
2. **Trade-off BW-SNR**: se puede intercambiar ancho de banda por potencia y viceversa, pero con rendimientos diferentes.
3. **Inalcanzable en la practica**: la demostracion asume codigos de longitud infinita (latencia infinita). Los sistemas reales operan 1–3 dB por debajo.
4. **Base de comparacion**: eficiencia de sistemas reales vs. limite de Shannon como benchmark universal.

## Derivacion para Canal AWGN

Considerando el canal $Y = X + N$ donde $N \sim \mathcal{N}(0, \sigma^2 = N)$:

1. La entropia diferencial gaussiana: $h(X) = \frac{1}{2}\log_2(2\pi e \sigma^2)$
2. Salida: $h(Y) = \frac{1}{2}\log_2[2\pi e (S+N)]$
3. Ruido: $h(N) = \frac{1}{2}\log_2(2\pi e N)$
4. Informacion mutua:

$$I(X;Y) = h(Y) - h(N) = \frac{1}{2}\log_2\left(1 + \frac{S}{N}\right)$$

5. Por el teorema del muestreo, en tiempo continuo con $B$ Hz se obtienen $2B$ muestras independientes/s:

$$\boxed{C = B \log_2\left(1 + \frac{S}{N}\right)}$$

## Regimenes de Operacion

### SNR alto (regimen limitado por banda)

$$C \approx B \log_2(SNR) \quad \text{— crecimiento logaritmico}$$

Duplicar la potencia solo agrega $\sim 1$ bit/s/Hz adicional. Rendimientos decrecientes.

### SNR bajo (regimen limitado por potencia)

$$\boxed{C \approx 1.44 \cdot B \cdot \frac{S}{N}}$$

La capacidad es proporcional a la potencia. Eficiente intercambiar BW por SNR.

### Punto de transicion

En $SNR \approx 1$ (0 dB) ocurre el cambio entre regimen logaritmico y lineal. [analysis]

## Ejemplo: Canal de Voz Telefonica

- $B = 3100$ Hz, $SNR = 30$ dB ($= 1000$ lineal)
- $C = 3100 \times \log_2(1001) \approx 3100 \times 9.97 = 30,900$ bits/s

Interpretacion: el limite teorico es $\sim 31$ kbps, explicando por que los modems superiores a 56k requerian tecnicas especiales. [analysis]

## Relacion con $E_b/N_0$

En terminos de energia por bit ($E_b$) y densidad espectral de ruido ($N_0$):

$$\frac{E_b}{N_0} = \frac{2^{\eta} - 1}{\eta}, \quad \eta = \frac{C}{B}$$

Limite cuando $\eta \to 0$ (banda infinita):

$$\boxed{\left(\frac{E_b}{N_0}\right)_{min} = \ln(2) \approx -1.59 \text{ dB}}$$

Este es el limite absoluto: ningun sistema, sin importar cuanto ancho de banda use, puede operar con $E_b/N_0 < -1.59$ dB. [source]

## Errores Comunes

- Usar SNR en dB directamente en la formula: convertir siempre a lineal
- Confundir capacidad con velocidad real alcanzable
- Pensar que mas potencia siempre ayuda proporcionalmente (recordar el logaritmo)

## Ver tambien

- [[teoria-informacion/capacidad-canal-shannon]]
- [[teoria-informacion/entropia-fuente]]
- [[teoria-informacion/sistema-ideal-comunicaciones]]
- [[conceptos-integradores/comparacion-global-modulaciones]]
- [[conceptos-integradores/compromisos-diseno]]
- [[ruido/intercomparacion-sistemas]]
