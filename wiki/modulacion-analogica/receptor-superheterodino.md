---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_03/carta_12_receptor-superheterodino.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Receptor Superheterodino

> **Last verified:** 2025-11-16 | **Verified by:** [source]

## Principio de Funcionamiento

El receptor superheterodino convierte la señal de RF recibida a una **frecuencia intermedia (FI) fija** mediante un mezclador y oscilador local [source]:

$$\boxed{f_{FI} = |f_{RF} - f_{LO}|}$$

Diagrama de bloques:

```
Antena → Amp RF → Mezclador → Amp FI → Detector → Amp Audio
                    ↑
              Oscilador Local
```

## Por que Superheterodino

Antes del superheterodino, los receptores TRF (Tuned Radio Frequency) tenian problemas graves:
- Selectividad y ganancia variaban con la frecuencia
- Imposible separar estaciones cercanas
- Dificil mantener ancho de banda constante

La solucion: convertir **todas** las señales a una FI fija donde se optimiza el procesamiento [source].

## Etapas del Receptor

1. **Amplificador RF**: preseleccion y amplificacion inicial
2. **Mezclador**: multiplica $s_{RF}(t)$ con $s_{LO}(t)$
3. **Filtro FI**: selecciona la frecuencia diferencia
4. **Amplificador FI**: proporciona la mayor ganancia y selectividad
5. **Detector**: recupera la informacion modulada
6. **Amplificador de audio**: señal demodulada final

## Analisis Matematico del Mezclador

Señal RF: $s_{RF}(t) = A_c[1 + m(t)]\cos(2\pi f_{RF} t)$

Oscilador local: $s_{LO}(t) = A_{LO}\cos(2\pi f_{LO} t)$

Mezclador (multiplicador):

$$s_{mez}(t) = \frac{A_c A_{LO}}{2}[1 + m(t)][\cos(2\pi(f_{RF} + f_{LO})t) + \cos(2\pi(f_{RF} - f_{LO})t)]$$

El filtro FI selecciona la componente diferencia: $f_{FI} = |f_{RF} - f_{LO}|$.

## Problema de Frecuencia Imagen

Existe una frecuencia no deseada que tambien produce la misma FI [source]:

$$f_{imagen} = f_{LO} \pm f_{FI}$$

Para LO por encima ($f_{LO} = f_{RF} + f_{FI}$):

$$f_{imagen} = f_{RF} + 2f_{FI}$$

La frecuencia imagen debe ser **rechazada por el filtro de RF** antes del mezclador.

## Ventajas del Superheterodino

- **Selectividad constante**: filtros FI optimizados para una sola frecuencia [source]
- **Alta ganancia**: amplificacion mas eficiente en FI fija [source]
- **Sintonizacion simple**: solo varia el oscilador local
- **Rechazo de imagen**: con filtrado RF adecuado

## Valores Tipicos de FI

| Sistema | FI Estandar | Ancho de Banda |
|---------|------------|----------------|
| AM Broadcast | 455 kHz | 10 kHz |
| FM Broadcast | 10.7 MHz | 200 kHz |
| TV Analogica | 45.75 MHz (video) | 6 MHz |

## Doble Conversion

Para mejorar rechazo de imagen y selectividad:

```
RF → 1er Mezclador → 1ra FI (10.7 MHz) → 2do Mezclador → 2da FI (455 kHz) → Detector
```

Usado en receptores FM de alta calidad y comunicaciones profesionales [analysis].

## Analogia

El superheterodino es como un sistema de traduccion universal: en lugar de aprender 100 idiomas (receptor TRF), contratas traductores que convierten todo a tu idioma nativo (FI) donde tienes maxima comprension [analysis].

## Puntos Clave

- ✓ Convierte TODAS las señales a una FI fija [source]
- ✓ FI fija permite optimizacion de filtros y amplificadores [source]
- ✓ La frecuencia imagen debe rechazarse en RF [source]
- ✓ Arquitectura dominante en receptores desde 1918 hasta hoy [source]

## Ver tambien

- [[modulacion-analogica/am-vs-dsb-sc]]
- [[modulacion-analogica/modulacion-ssb]]
- [[modulacion-analogica/fm-estereo]]
- [[ruido/factor-ruido-temperatura]]
