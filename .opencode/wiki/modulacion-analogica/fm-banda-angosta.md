---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_04/carta_17_indice_modulacion_fm.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# FM de Banda Angosta (NBFM) vs Banda Ancha (WBFM)

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Indice de Modulacion

El indice de modulacion $\beta$ en FM se define como [source]:

$$\boxed{\beta = \frac{\Delta f}{f_m} = \frac{k_f A_m}{f_m}}$$

donde $\Delta f = k_f A_m$ es la desviacion pico de frecuencia.

## FM de Banda Angosta (NBFM): $\beta < 0.5$

### Aproximacion

Para $\beta \ll 1$, usando aproximaciones de funciones de Bessel de argumento pequeño [source]:
- $J_0(\beta) \approx 1$
- $J_1(\beta) \approx \beta/2$
- $J_n(\beta) \approx 0$ para $n \geq 2$

### Señal NBFM

$$\boxed{s_{NBFM}(t) \approx A_c\cos(2\pi f_c t) - \frac{A_c\beta}{2}\cos[2\pi(f_c - f_m)t] + \frac{A_c\beta}{2}\cos[2\pi(f_c + f_m)t]}$$

### Caracteristicas

| Propiedad | Valor |
|-----------|-------|
| Ancho de banda | $BW \approx 2f_m$ |
| Componentes espectrales | Portadora + 1 par de bandas laterales |
| Similitud | Similar a AM pero con bandas laterales en cuadratura |
| Aplicacion tipica | Walkie-talkies, radio movil |

## FM de Banda Ancha (WBFM): $\beta > 1$

### Espectro Completo

Usando funciones de Bessel [source]:

$$s_{FM}(t) = A_c\sum_{n=-\infty}^{\infty} J_n(\beta)\cos[2\pi(f_c + nf_m)t]$$

### Comportamiento de Bessel para $\beta$ grande:
- Multiples $J_n(\beta)$ son significativas
- Numero de bandas laterales significativas $\approx \beta + 1$
- Amplitudes oscilan; la portadora ($J_0$) puede incluso anularse

### Caracteristicas

| Propiedad | Valor |
|-----------|-------|
| Ancho de banda | $BW \approx 2(\Delta f + f_m) = 2f_m(\beta + 1)$ |
| Componentes espectrales | Multiples ($\approx \beta+1$ pares) |
| Mejora de SNR | $SNR_{out} = 3\beta^2 \cdot SNR_{in}$ |
| Aplicacion tipica | FM broadcast, TV audio |

## Comparacion NBFM vs WBFM

| Parametro | NBFM | WBFM |
|-----------|------|------|
| Indice $\beta$ | $< 0.5$ | $> 1$ |
| Ancho de banda | $\approx 2f_m$ | $\approx 2f_m(\beta + 1)$ |
| Complejidad | Baja | Alta |
| Inmunidad al ruido | Similar a AM | Muy superior |
| Uso tipico | Comunicaciones de voz | Broadcast de alta fidelidad |

## Ejemplo Numerico

Sistema FM con $\Delta f = 15$ kHz, $f_m = 3$ kHz:

$$\beta = \frac{15}{3} = 5 \quad \Rightarrow \quad \text{WBFM}$$

$$BW = 2(15 + 3) = 36 \text{ kHz}$$

Numero de bandas laterales significativas $\approx 5 + 1 = 6$ pares.

## Trade-off Fundamental

$$\boxed{\text{Mayor } \beta \Rightarrow \text{ Mejor SNR pero Mayor BW}}$$

La mejora en SNR es proporcional a $\beta^2$ [source]: WBFM intercambia ancho de banda por calidad de señal.

## Zona de Transicion

Para $0.5 < \beta < 1$: transicion gradual entre NBFM y WBFM. La aproximacion NBFM pierde validez pero el espectro aun no muestra muchas componentes significativas [analysis].

## Puntos Clave

- ✓ $\beta$ determina completamente el comportamiento espectral [source]
- ✓ NBFM: espectro similar a AM ($\approx 3$ componentes) [source]
- ✓ WBFM: multiples componentes, espectro "peine de frecuencias" [source]
- ✓ El espectro FM teorico es infinito; practico es finito

## Ver tambien

- [[modulacion-analogica/fm-vs-pm]]
- [[modulacion-analogica/ancho-banda-carson]]
- [[derivaciones/modulacion-fm-banda-angosta]]
