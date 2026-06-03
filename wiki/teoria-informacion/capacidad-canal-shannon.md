---
tags:
  - wiki/teoria-informacion
source_file: explicaciones_anki/unidad_09/carta_45_teorema-shannon-hartley.md
curso: Sistemas de Comunicaciones
unidad: 9
---

# Capacidad del Canal de Shannon

> **Last verified:** 2025-11-16 | **Verified by:** source

## Definicion

La **capacidad del canal** $C$ es la maxima tasa de transmision a la cual es posible comunicacion libre de errores. Establecida por el teorema de codificacion de canal de Shannon, es un limite fundamental e insuperable en teoria de comunicaciones. [source — [[../../explicaciones_anki/unidad_09/carta_45_teorema-shannon-hartley]]]

$$\boxed{C = \max_{p(x)} I(X;Y) \quad \text{[bits/s]}}$$

donde $I(X;Y)$ es la informacion mutua entre entrada $X$ y salida $Y$, y la maximizacion es sobre todas las distribuciones de entrada.

## Teorema de Codificacion de Canal de Shannon

Shannon demostro que para un canal con capacidad $C$: [source — [[../../explicaciones_anki/unidad_09/carta_45_teorema-shannon-hartley]]]

- Para cualquier tasa $R < C$, existe un codigo que permite transmitir con probabilidad de error $P_e \to 0$ (arbitrariamente pequena).
- Para cualquier tasa $R > C$, la probabilidad de error esta inevitablemente acotada lejos de cero.

**Implicacion revolucionaria**: Antes de Shannon, se creia que para transmitir sin errores habia que aumentar indefinidamente la potencia o reducir drasticamente la velocidad. Shannon demostro que existe una velocidad especifica (la capacidad) por debajo de la cual se puede lograr error arbitrariamente pequeno. [analysis]

## Canal AWGN y el Teorema de Shannon-Hartley

Para el canal de ruido aditivo gaussiano blanco (AWGN), con ancho de banda $B$ y relacion senal a ruido $S/N$:

$$\boxed{C = B \log_2\left(1 + \frac{S}{N}\right) \quad \text{[bits/s]}}$$

Donde: [source — [[../../explicaciones_anki/unidad_09/carta_45_teorema-shannon-hartley]]]
- $B$: ancho de banda disponible (Hz)
- $S/N$: relacion senal a ruido (lineal, no en dB)
- $C$: capacidad maxima sin errores

### Derivacion

Para entrada gaussiana en canal AWGN, la informacion mutua es maxima:

$$I(X;Y) = h(Y) - h(N) = \frac{1}{2}\log_2\left(1 + \frac{S}{N}\right)$$

donde $h(Y)$ y $h(N)$ son entropias diferenciales. Con $2B$ muestras independientes por segundo (teorema del muestreo), se obtiene: $C = B\log_2(1 + S/N)$.

## Trade-off Ancho de Banda — SNR

La formula de Shannon revela dos recursos intercambiables:

### Regimen limitado por banda ($S/N \gg 1$)

$$C \approx B \log_2(S/N) \quad \text{[crecimiento logaritmico]}$$

Duplicar la potencia solo agrega $\sim 1$ bit/s/Hz adicional. El ancho de banda es el recurso mas valioso.

### Regimen limitado por potencia ($S/N \ll 1$)

$$\boxed{C \approx \frac{1.44 \cdot B \cdot S}{N}}$$

La capacidad es proporcional a la potencia. Duplicar $B$ o $S/N$ duplica $C$.

### Banda infinita ($B \to \infty$)

Existe un limite finito incluso con banda infinita: [analysis]

$$\boxed{C_{\infty} = \frac{S}{N_0 \ln 2} = 1.44 \frac{S}{N_0}}$$

## Valores Tipicos de Capacidad

| Sistema | BW | SNR | $C$ (teorica) | Real | Eficiencia |
|---------|-----|-----|--------------|------|-----------|
| DSL | 1.1 MHz | 40 dB | 44 Mbps | 24 Mbps | 55% |
| LTE | 20 MHz | 20 dB | 133 Mbps | 100 Mbps | 75% |
| WiFi 6 | 160 MHz | 35 dB | 1.8 Gbps | 1.2 Gbps | 67% |

Los sistemas modernos (con Turbo codes, LDPC) operan a 1–3 dB del limite de Shannon. [analysis]

## Errores Comunes

- Usar SNR en dB directamente en la formula: siempre convertir a lineal ($SNR_{lineal} = 10^{SNR_{dB}/10}$)
- Confundir capacidad con velocidad real: sistemas reales tienen overhead y operan por debajo de $C$
- Creer que mas potencia siempre ayuda proporcionalmente: a alta SNR, rendimientos decrecientes por el logaritmo

## Ver tambien

- [[../teoria-informacion/teorema-shannon-hartley]]
- [[../teoria-informacion/entropia-fuente]]
- [[../ruido/relacion-snr]]
- [[../teoria-informacion/sistema-ideal-comunicaciones]]
- [[../conceptos-integradores/comparacion-global-modulaciones]]
- [[../conceptos-integradores/compromisos-diseno]]
- [[../../claude-conversations/2025-11-05_shannon-capacity-and-signal-to-noise-ratio|Conversación: capacidad de Shannon y SNR]]
