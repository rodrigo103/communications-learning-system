---
tags:
  - wiki/espectro-expandido
source_file: explicaciones_anki/unidad_10/carta_52_cdma.md
curso: Sistemas de Comunicaciones
unidad: 10
---

# CDMA — Acceso Multiple por Division de Codigo

> **Last verified:** 2025-11-16 | **Verified by:** source

## Principio

**CDMA** (Code Division Multiple Access) permite que multiples usuarios compartan simultaneamente la misma banda de frecuencia usando codigos de espectro expandido ortogonales. Revoluciono las comunicaciones moviles en los anos 90 y fue la base de las redes 3G. [source — [[../../explicaciones_anki/unidad_10/carta_52_cdma]]]

A diferencia de FDMA (cada usuario en su frecuencia) o TDMA (cada usuario en su intervalo de tiempo), CDMA permite que **todos los usuarios transmitan simultaneamente en la misma frecuencia**, separados unicamente por codigos matematicos.

## Funcionamiento

### Transmision

1. Cada usuario recibe un **codigo PN** (pseudoaleatorio) unico (Walsh, Gold)
2. Los datos del usuario ($\pm 1$) se multiplican por el codigo de spreading
3. La senal expandida ocupa todo el ancho de banda disponible
4. Todos los usuarios transmiten en el mismo canal simultaneamente

Senal transmitida del usuario $k$:

$$s_k(t) = A_k \cdot d_k(t) \cdot c_k(t) \cdot \cos(2\pi f_c t + \phi_k)$$

### Recepcion (Despreading)

La senal recibida es la suma de $K$ usuarios mas ruido:

$$r(t) = \sum_{k=1}^{K} A_k d_k(t) c_k(t) \cos(2\pi f_c t + \phi_k) + n(t)$$

El receptor del usuario 1 correlaciona con su codigo:

$$y_1 = \int_0^{T_b} r(t) \cdot c_1(t) \cdot \cos(2\pi f_c t) \, dt$$

Resultado:

$$\boxed{y_1 = \frac{A_1 T_b}{2} d_1 + \text{MAI} + \text{ruido}}$$

Donde MAI (Multiple Access Interference) es la interferencia residual de otros usuarios. Si los codigos son perfectamente ortogonales: MAI = 0.

## Ganancia de Procesamiento

$$\boxed{G_p = \frac{W}{R} = \frac{R_{chip}}{R_{bit}}}$$

- $W$: ancho de banda del spreading
- $R$: tasa de bits de informacion
- Tipicamente: $G_p = 128$ (21 dB) en IS-95, hasta 43 dB en GPS

La mejora en SNR despues del despreading: $SNR_{out} = G_p \cdot SNR_{in}$.

## Control de Potencia y Problema Near-Far

El **problema near-far** es critico en CDMA: un usuario cercano a la estacion base puede "ahogar" a usuarios lejanos si no se controla la potencia transmitida. Una diferencia de 40 dB (factor de 10,000) entre usuarios colapsaria el sistema. [analysis]

Solucion: **control de potencia estricto**:
- Lazo abierto: ajuste inicial basado en potencia recibida
- Lazo cerrado: comandos rapidos de $\pm 1$ dB (800 Hz en IS-95)
- Rango dinamico: $\sim 80$ dB
- Objetivo: todos los usuarios llegan con potencia similar ($\pm 1$ dB)

## Codigos Ortogonales

Los codigos deben tener: [source — [[../../explicaciones_anki/unidad_10/carta_52_cdma]]]
- **Autocorrelacion alta**: correlaciona bien consigo mismo
- **Correlacion cruzada baja**: correlaciona mal con otros codigos

Tipos:
- **Walsh**: ortogonales si estan sincronizados (usados en downlink)
- **Gold**: baja correlacion cruzada, usados en GPS
- **PN largos** ($2^{42} - 1$): spreading adicional, privacidad

## Capacidad del Sistema

$$K_{max} \approx \frac{W/R}{(E_b/N_0)_{req}} \cdot \frac{1}{1+f} \cdot \alpha \cdot \beta$$

Donde: [analysis]
- $W/R$: ganancia de procesamiento
- $(E_b/N_0)_{req}$: requisito de calidad
- $f$: factor de reuso (interferencia de otras celdas)
- $\alpha$: factor de actividad de voz
- $\beta$: ganancia por sectorizacion

Capacidad **flexible** (soft capacity): mas usuarios degradan gradualmente la calidad (no hay limite duro).

## Aplicaciones

| Sistema | Chip rate | $G_p$ | Descripcion |
|---------|-----------|-------|-------------|
| GPS C/A | 1.023 Mcps | 43 dB | Navegacion |
| IS-95 | 1.2288 Mcps | 21 dB | 2G/3G celular |
| WCDMA | 3.84 Mcps | Variable | 3G global |

## Errores Comunes

- **Confundir CDMA con DSSS**: DSSS es el mecanismo de capa fisica, CDMA agrega gestion de multiples usuarios
- **Asumir ortogonalidad perfecta**: multitrayecto y asincronia destruyen ortogonalidad, generando MAI
- **Ignorar el problema near-far**: sin control de potencia CDMA no funciona

## Ver tambien

- [[../espectro-expandido/dsss]]
- [[../espectro-expandido/fhss]]
- [[../espectro-expandido/correlacion-senales]]
- [[../espectro-expandido/aplicaciones-spread-spectrum]]
- [[../espectro-expandido/ofdm]]
