---
tags:
  - wiki/espectro-expandido
source_file: explicaciones_anki/unidad_10/carta_51_dsss-vs-fhss.md
curso: Sistemas de Comunicaciones
unidad: 10
---

# DSSS — Direct Sequence Spread Spectrum

> **Last verified:** 2025-11-16 | **Verified by:** source

## Principio

**DSSS** (Direct Sequence Spread Spectrum) expande el espectro multiplicando los datos por una secuencia pseudoaleatoria (PN) de alta velocidad. La senal ocupa un ancho de banda mucho mayor que el de la informacion original. [source]

$$s_{DSSS}(t) = d(t) \cdot c(t) \cdot \cos(2\pi f_c t)$$

Donde:
- $d(t)$: datos binarios ($\pm 1$) con periodo $T_b$ (bit)
- $c(t)$: codigo PN ($\pm 1$) con periodo $T_c$ (chip)
- $T_c \ll T_b$ (tipicamente $T_b/T_c = 10$ a $1000$)

## Parametros Clave

### Ganancia de Procesamiento

$$\boxed{G_p = \frac{BW_{SS}}{BW_{info}} = \frac{R_{chip}}{R_{bit}}}$$

- $BW_{SS} \approx 2 R_{chip}$: ancho de banda del espectro expandido
- $R_{chip}$: tasa de chips del codigo PN (Mchips/s)
- $R_{bit}$: tasa de bits de informacion (kbps)

La ganancia cuantifica la mejora en SNR tras el despreading:

$$\boxed{SNR_{out} = G_p \cdot SNR_{in}}$$

En dB: $SNR_{out,dB} = SNR_{in,dB} + G_{p,dB}$.

### Resistencia a Interferencia

Para interferencia de banda angosta $J$:

$$\frac{S_{out}}{J_{out}} = \frac{S_{in}}{J_{in}} \cdot G_p$$

DSSS es excelente contra ruido continuo e interferencia de banda angosta. La interferencia se "expande" en el receptor, quedando como ruido de fondo atenuado. [analysis]

## Proceso de Spreading y Despreading

### Transmision

1. Bit de datos ($+1$ o $-1$) se multiplica por el codigo PN
2. Si $d_k = +1$: se transmite el codigo PN tal cual
3. Si $d_k = -1$: se transmite el codigo PN invertido
4. El espectro se expande: PSD baja y ancha

### Recepcion

1. Senal recibida se multiplica por el mismo codigo PN sincronizado
2. Correlacion: alta con codigo correcto, baja con otros
3. Integracion sobre la duracion del bit recupera los datos
4. Interferencias se expanden $\to$ ruido de fondo

## Ventajas y Desventajas

**Ventajas de DSSS**: [analysis]
- Mejor ganancia de procesamiento
- Excelente para medicion de tiempo (GPS)
- Resistente a ruido continuo e interferencia de banda angosta
- Permite CDMA con codigos ortogonales

**Desventajas**:
- Mas complejo que FHSS (requiere correladores)
- Vulnerable a interferencia de banda ancha
- Sincronizacion de codigo critica

## Aplicaciones Principales

| Sistema | $R_{chip}$ | $G_p$ | Uso |
|---------|------------|-------|-----|
| GPS C/A | 1.023 Mcps | 43 dB | Todos los satelites comparten frecuencia |
| IS-95 CDMA | 1.2288 Mcps | 21 dB | Celular 2G/3G |
| WiFi 802.11b | 11 Mcps | 10.4 dB | WLAN 11 Mbps |

## DSSS vs FHSS

| Aspecto | DSSS | FHSS |
|---------|------|------|
| Dominio expansion | Codigo (tiempo) | Frecuencia |
| Ocupacion espectral | Banda ancha continua | Pico que salta |
| Contra ruido continuo | Excelente | Bueno |
| Contra jammer parcial | Bueno | Excelente |
| Complejidad | Mayor (correladores) | Menor (sintetizador) |

Ver [[espectro-expandido/fhss]] para la comparacion detallada.

## Errores Comunes

- Confundir chip rate con bit rate: $R_{chip} \gg R_{bit}$
- Creer que DSSS aumenta la capacidad del canal: no aumenta $C$, solo redistribuye recursos (intercambia BW por robustez)
- Asumir que mas spreading siempre es mejor: hay limites practicos (sincronizacion, complejidad)

## Ver tambien

- [[espectro-expandido/cdma]]
- [[espectro-expandido/fhss]]
- [[espectro-expandido/correlacion-senales]]
- [[espectro-expandido/ofdm]]
- [[ruido/ruido-blanco-banda-angosta]]
- [[espectro-expandido/aplicaciones-spread-spectrum]]
