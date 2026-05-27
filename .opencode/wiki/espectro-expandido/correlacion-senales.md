---
tags:
  - wiki/espectro-expandido
source_file: explicaciones_anki/unidad_10/carta_50_spread-spectrum.md
curso: Sistemas de Comunicaciones
unidad: 10
---

# Correlacion de Senales en Spread Spectrum y CDMA

> **Last verified:** 2025-11-16 | **Verified by:** source

## Funcion de Correlacion

En sistemas de espectro expandido, la correlacion es la operacion fundamental que permite recuperar senales debiles inmersas en ruido e interferencia. [analysis]

### Autocorrelacion

La autocorrelacion de un codigo PN $c(t)$ con periodo $T$:

$$R_{cc}(\tau) = \frac{1}{T} \int_0^T c(t) \cdot c(t + \tau) \, dt$$

Propiedades deseables: [source]
- **Pico estrecho en $\tau = 0$**: permite sincronizacion precisa
- **Valores bajos para $\tau \neq 0$**: evita falsas detecciones

Para un codigo PN ideal de longitud $L$ chips:

$$R_{cc}(\tau) = \begin{cases} 1 & \tau = 0 \\ -1/L & \tau \neq 0 \end{cases}$$

### Correlacion Cruzada

Entre dos codigos diferentes $c_i(t)$ y $c_j(t)$:

$$R_{c_i c_j}(\tau) = \frac{1}{T} \int_0^T c_i(t) \cdot c_j(t + \tau) \, dt$$

Para CDMA, la **correlacion cruzada debe ser minima**: $|R_{c_i c_j}| \ll 1$. Esto garantiza que la senal de un usuario aparezca como ruido para los demas. [analysis]

## Ortogonalidad en CDMA

Dos secuencias son **ortogonales** si su correlacion cruzada en $\tau = 0$ es nula:

$$\int_0^T c_i(t) \cdot c_j(t) \, dt = 0 \quad \text{para } i \neq j$$

### Codigos Walsh

Los codigos Walsh son ortogonales si estan perfectamente sincronizados. Se generan recursivamente con la matriz de Hadamard:

$$H_{2N} = \begin{pmatrix} H_N & H_N \\ H_N & -H_N \end{pmatrix}, \quad H_1 = [1]$$

Ejemplo con 4 chips: [analysis]
- $W_1 = [+1, +1, +1, +1]$
- $W_2 = [+1, -1, +1, -1]$
- $W_3 = [+1, +1, -1, -1]$
- $W_4 = [+1, -1, -1, +1]$

Producto interno $W_1 \cdot W_3 = 1+1-1-1 = 0 \Rightarrow$ ortogonales.

**Limitacion**: la ortogonalidad se destruye con multitrayecto y asincronia entre usuarios. Por eso en uplink de CDMA se usan codigos PN largos con baja correlacion cruzada en vez de Walsh. [analysis]

### Codigos Gold

Generados por suma modulo-2 de dos secuencias-$m$. Proporcionan:
- Baja correlacion cruzada: $|\rho_{ij}| \leq 65/1023 \approx 0.064$ para GPS
- Gran cantidad de codigos unicos
- Usados en GPS: 32 satelites con codigos Gold distintos

## Procesamiento de Correlacion en el Receptor

El receptor DSSS/CDMA realiza:

1. **Multiplicacion**: $r(t) \times c_{local}(t)$ — alinea el codigo local con el deseado
2. **Integracion**: $\int_0^{T_b} (\dots) \, dt$ — acumula energia del bit
3. **Decision**: compara con umbral para decidir el bit transmitido

La ganancia de procesamiento surge porque:
- Senal deseada: se correlaciona coherentemente $\to$ crece linealmente con $T_b$
- Ruido e interferencia: no se correlacionan $\to$ crecen como $\sqrt{T_b}$ (promedio cero)

$$\boxed{SNR_{out} = G_p \cdot SNR_{in} = \frac{T_b}{T_c} \cdot SNR_{in}}$$

## Densidad Espectral de Potencia (PSD)

Una senal spread spectrum tiene PSD:

$$PSD_{SS}(f) = \frac{P_{total}}{BW_{SS}}$$

Caracteristicas: [analysis]
- **Baja densidad**: potencia total constante distribuida en banda ancha
- **Forma de $\text{sinc}^2$**: ensanchada por el chip rate
- **Debajo del ruido termico**: en GPS la senal esta $\sim 20$ dB por debajo del piso de ruido

La baja PSD proporciona:
- Baja probabilidad de deteccion (LPD — Low Probability of Detection)
- Baja probabilidad de interceptacion (LPI)
- Resistencia a jamming

## Ejemplo: Recuperacion en GPS

GPS transmite con $R_{chip} = 1.023$ Mchips/s y $R_{bit} = 50$ bps:

$$G_p = 1.023 \times 10^6 / 50 = 20,\!460 \approx 43 \text{ dB}$$

La correlacion sobre $T_b = 20$ ms acumula energia de 20,460 chips, amplificando la senal 43 dB sobre el ruido de fondo. Esto permite que GPS funcione con senales mucho mas debiles que el ruido termico. [analysis]

## Errores Comunes

- **Asumir ortogonalidad en condiciones reales**: multitrayecto y desplazamiento Doppler destruyen la ortogonalidad perfecta
- **Confundir correlacion con convolucion**: ambas usan integral de producto, pero con signos diferentes
- **Ignorar requisitos de sincronizacion**: la correlacion solo funciona con codigos alineados

## Ver tambien

- [[espectro-expandido/cdma]]
- [[espectro-expandido/dsss]]
- [[espectro-expandido/fhss]]
- [[herramientas-matematicas/densidad-espectral-potencia]]
- [[ruido/ruido-blanco-banda-angosta]]
