---
tags:
  - wiki/ruido
source_file: explicaciones_anki/unidad_07/carta_33_ruido-blanco.md
curso: Sistemas de Comunicaciones
unidad: 7
---

# Fuentes de Ruido en Comunicaciones

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_07/carta_33_ruido-blanco]]]

## Clasificación de Fuentes de Ruido

El ruido está presente en todo sistema de comunicaciones real y determina los límites fundamentales de lo que se puede comunicar. [source — [[../../explicaciones_anki/unidad_07/carta_33_ruido-blanco]]]

### Ruido Térmico (Johnson-Nyquist)

Originado por la agitación térmica de electrones en conductores. Es la fuente de ruido más fundamental:

$$\boxed{N = kTB}$$

donde:
- $k = 1.38 \times 10^{-23}$ J/K (constante de Boltzmann)
- $T$ = temperatura absoluta en Kelvin
- $B$ = ancho de banda en Hz

A temperatura ambiente (290 K): $N_0 = kT = -174$ dBm/Hz. [source — [[../../explicaciones_anki/unidad_07/carta_33_ruido-blanco]]]

### Ruido Shot (Schottky)

Fluctuaciones por el flujo discreto de portadores de carga a través de una barrera de potencial. Significativo en dispositivos semiconductores y fotodetectores.

### Ruido Flicker (1/f)

Predominante en bajas frecuencias, con densidad espectral proporcional a $1/f$. Importante en osciladores y mezcladores.

### Ruido Atmosférico

Generado por descargas eléctricas atmosféricas (rayos). Significativo en bandas VLF, LF y MF.

### Ruido Artificial (Man-Made)

Generado por actividad humana: motores, líneas de potencia, ignición de vehículos, equipos electrónicos. Predominante en entornos urbanos.

## Características del Ruido Blanco

El modelo de ruido blanco gaussiano (AWGN) es el más usado por: [analysis]
1. Aproxima bien el ruido térmico en el ancho de banda del sistema
2. Es matemáticamente tratable (muestras independientes)
3. Es un modelo conservador pero realista (peor caso razonable)

**Propiedad clave:** muestras en instantes diferentes son completamente incorrelacionadas, la autocorrelación es una delta:

$$R_n(\tau) = N_0 \delta(\tau)$$

## Nota sobre Convenciones

| Convención | DEP | Potencia | Uso |
|-----------|-----|----------|-----|
| Unilateral (moderna) | $N_0 = kT$ | $N = kTB$ | Este curso |
| Bilateral (antigua) | $S_n(f) = kT/2$ | $N = kTB$ | Textos históricos |

La potencia disponible es la misma en ambas: $N = kTB$. [source — [[../../explicaciones_anki/unidad_07/carta_33_ruido-blanco]]]

## Ver también

- [[../ruido/ruido-blanco-banda-angosta]] — Ruido blanco filtrado: modelo de banda angosta
- [[../ruido/factor-ruido-temperatura]] — Temperatura equivalente de ruido
- [[../ruido/relacion-snr]] — Relación señal-ruido como métrica de calidad
- [[aclaracion-densidad-espectral-ruido]] — Densidad espectral de ruido (aclaración)
