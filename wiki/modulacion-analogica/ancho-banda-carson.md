---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_04/carta_18_regla_carson.md
curso: Sistemas de Comunicaciones
unidad: 4
---

# Regla de Carson para Ancho de Banda en FM

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]]

## Enunciado

La Regla de Carson estima el ancho de banda practico de una señal FM [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]]:

$$\boxed{BW \approx 2(\Delta f + f_m) = 2f_m(\beta + 1)}$$

donde:
- $\Delta f$ = desviacion maxima de frecuencia [Hz]
- $f_m$ = frecuencia maxima de la moduladora [Hz]
- $\beta = \Delta f / f_m$ = indice de modulacion

Esta regla contiene **aproximadamente el 98% de la potencia total** de la señal [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]].

## Justificacion

Aunque el espectro FM teoricamente tiene **infinitas** componentes (funciones de Bessel), Carson determino que:

- NBFM ($\beta < 1$): componentes significativas en $f_c$ y $f_c \pm f_m$
- WBFM ($\beta \gg 1$): componentes significativas hasta $f_c \pm \beta f_m$

Potencia contenida en $|n| \leq \beta + 1$ bandas laterales:

| $\beta$ | Bandas (Carson) | Potencia contenida |
|---------|-----------------|-------------------|
| 0.5 | 2 | 99.0% |
| 1.0 | 2 | 98.4% |
| 2.0 | 3 | 98.2% |
| 5.0 | 6 | 98.0% |
| 10.0 | 11 | 98.1% |

La regla mantiene ~98% consistentemente [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]].

## Casos Limite

### NBFM ($\beta \to 0$):

$$BW \to 2f_m \quad \text{(igual que AM-DSB)}$$

### WBFM ($\beta \to \infty$):

$$BW \to 2\Delta f \quad \text{(dominado por la desviacion)}$$

### Caso General:

La formula $BW = 2(\Delta f + f_m)$ funciona para TODO valor de $\beta$ [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]].

## Aplicacion: FM Broadcast

Para radio FM comercial estandar [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]]:

| Parametro | Valor |
|-----------|-------|
| Frecuencia max. audio ($f_m$) | 15 kHz |
| Desviacion max. ($\Delta f$) | $\pm 75$ kHz |
| Indice ($\beta$) | $75/15 = 5$ |
| BW Carson | $2(75 + 15) = 180$ kHz |
| BW asignado (FCC) | 200 kHz |
| Margen de guarda | 20 kHz |

## Interpretacion del Factor 2

El factor 2 representa las **dos bandas laterales** (superior e inferior) que se extienden simetricamente alrededor de $f_c$ [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]]:

- Banda lateral inferior: $f_c - (\Delta f + f_m)$
- Banda lateral superior: $f_c + (\Delta f + f_m)$
- Total: $2(\Delta f + f_m)$

## Limitaciones

- Carson se derivo para **modulacion sinusoidal (tono unico)** [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]]
- Para señales complejas: usar $f_m$ = frecuencia maxima de la moduladora
- **NO da el 100%** de la potencia (siempre hay energia residual fuera de banda)
- Es una aproximacion, no un resultado exacto

## Formula Alternativa

$$\boxed{BW = 2f_m(\beta + 1) = 2(\Delta f + f_m)}$$

## Puntos Clave

- ✓ Carson es **empirica**, basada en observacion [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]]
- ✓ Contiene ~98% de la potencia [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]]
- ✓ Unifica NBFM y WBFM en una sola formula [source — [[../../explicaciones_anki/unidad_04/carta_18_regla_carson]]]
- ✓ No es exacta: siempre hay potencia residual fuera de banda
- ✓ Para diseño practico: agregar 10-15% de margen

## Ver tambien

- [[../modulacion-analogica/fm-vs-pm]]
- [[../modulacion-analogica/fm-banda-angosta]]
- [[../derivaciones/modulacion-fm-carson]]
- [[../../claude-conversations/2025-11-19_separaci-n-de-canales-fm-y-ancho-de-banda-real|Conversación: separación de canales FM]]
