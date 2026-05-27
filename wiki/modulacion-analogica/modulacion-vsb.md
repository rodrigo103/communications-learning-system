---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Modulacion VSB (Banda Lateral Vestigial)

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]

## Definicion

VSB (Vestigial Sideband) es un compromiso entre DSB y SSB: transmite **una banda lateral completa** y un **vestigio** (porcion) de la otra banda lateral [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]. Su ancho de banda:

$$\boxed{BW_{VSB} = f_m + f_v}$$

donde $f_v$ es la frecuencia del vestigio, tipicamente $f_v \approx (0.1\text{--}0.25)f_m$.

## Por que VSB

Para señales con contenido DC significativo (ej: video) [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]:
- **DSB**: demasiado ancho de banda ($2f_m$) 
- **SSB**: no puede transmitir DC ni frecuencias muy bajas (requiere filtros irrealizables)
- **VSB**: transmite todo el espectro usando solo $25\text{--}30\%$ mas BW que SSB

## Condicion de Simetria Vestigial

Para recuperacion perfecta, el filtro VSB debe satisfacer [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]:

$$\boxed{H_{VSB}(f_c + f) + H_{VSB}(f_c - f) = 1 \quad \text{para } |f| < f_v}$$

Esta condicion asegura que las contribuciones de ambas bandas se sumen correctamente en la demodulacion. El vestigio "rellena" lo que falta de la banda suprimida [analysis].

## Generacion

1. Generar DSB-SC: $s_{DSB}(t) = m(t)\cos(\omega_c t)$
2. Aplicar filtro VSB con respuesta de roll-off alrededor de $f_c$

El filtro VSB tiene roll-off tipico de $0.5\text{--}1.5$ MHz en TV analogica.

## Demodulacion

Multiplicando por $2\cos(\omega_c t)$ y filtrando paso-bajo [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]:

$$m_{recuperada}(t) = m(t) \cdot [H_{VSB}(f_c + f) + H_{VSB}(f_c - f)] = m(t)$$

Por la condicion de simetria, la recuperacion es **perfecta**.

## Aplicacion Principal: Television

### TV Analogica NTSC

| Parametro | Valor |
|-----------|-------|
| Portadora de video | 83.25 MHz (canal 6) |
| Ancho de banda video | 4.2 MHz |
| Vestigio inferior | 1.25 MHz |
| Ancho de banda total | 5.45 MHz |
| Eficiencia espectral | $4.2/5.45 = 77\%$ |

Comparacion: DSB requeriria $8.4$ MHz (54% mas) [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]].

### TV Digital ATSC (8-VSB)

Usa modulacion 8-VSB (8 niveles) con VSB para transmision terrestre en canales de 6 MHz [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]].

## Analogia

VSB es como empacar inteligentemente para un viaje: no puedes llevar todo (DSB), pero tampoco solo lo minimo (SSB pierde cosas esenciales). VSB lleva un conjunto completo y solo los elementos esenciales del otro — perfecto balance [analysis].

## Puntos Clave

- ✓ VSB preserva DC: critico para video y datos [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]
- ✓ Condicion de simetria vestigial: clave para demodulacion sin distorsion [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]
- ✓ Compromiso optimo entre eficiencia espectral y complejidad [source — [[../../explicaciones_anki/unidad_03/carta_15_banda_lateral_vestigial]]]
- ✓ Roll-off tipico: $f_v/f_m = 0.1\text{--}0.25$

## Ver tambien

- [[../modulacion-analogica/modulacion-ssb]]
- [[../modulacion-analogica/am-vs-dsb-sc]]
- [[../introduccion/espectro-electromagnetico]]
