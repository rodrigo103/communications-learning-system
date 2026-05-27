---
tags:
  - wiki/modulacion-analogica
source_file: explicaciones_anki/unidad_03/carta_13_indice_modulacion_am.md
curso: Sistemas de Comunicaciones
unidad: 3
---

# Indice de Modulacion en AM

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_03/carta_13_indice_modulacion_am]]]

## Definicion

El indice de modulacion $m$ cuantifica la profundidad de la modulacion en AM [source — [[../../explicaciones_anki/unidad_03/carta_13_indice_modulacion_am]]]:

$$\boxed{m = \frac{A_m}{A_c} = \frac{A_{max} - A_{min}}{A_{max} + A_{min}}}$$

donde:
- $A_m$ = amplitud de la señal moduladora
- $A_c$ = amplitud de la portadora
- $A_{max}$, $A_{min}$ = valores extremos de la envolvente

## Señal AM y Envolvente

La señal AM se expresa:

$$s_{AM}(t) = A_c[1 + m\cos(\omega_m t)]\cos(\omega_c t)$$

La envolvente varia entre:
- Maximo: $A_c(1 + m)$
- Minimo: $A_c(1 - m)$

Para evitar inversion de fase: $A_c(1 - m) \geq 0 \Rightarrow m \leq 1$ [source — [[../../explicaciones_anki/unidad_03/carta_13_indice_modulacion_am]]].

## Regimenes de Modulacion

| Regimen | $m$ | Caracteristica |
|---------|-----|----------------|
| Submodulacion | $m < 1$ | Transmision normal, envolvente nunca toca cero |
| Modulacion 100% | $m = 1$ | Maxima eficiencia sin distorsion |
| Sobremodulacion | $m > 1$ | **Distorsion severa**, inversion de envolvente |

## Eficiencia de Potencia

La eficiencia depende del indice de modulacion [source — [[../../explicaciones_anki/unidad_03/carta_13_indice_modulacion_am]]]:

$$\boxed{\eta = \frac{m^2}{2 + m^2}}$$

La potencia total transmitida:

$$P_{total} = P_c\left(1 + \frac{m^2}{2}\right)$$

donde $P_c = A_c^2/2$ es la potencia de portadora.

| $m$ | $\eta$ | Interpretacion |
|-----|--------|----------------|
| 0 | 0% | Solo portadora, sin informacion |
| 0.3 | 4.3% | Radio AM tipica en musica |
| 0.5 | 11.1% | Modulacion moderada |
| 0.85 | 26.5% | Picos en radio AM |
| 1.0 | 33.3% | Maximo teorico sin distorsion |

## Analisis Espectral y de Potencia

La señal AM contiene tres componentes:

| Componente | Frecuencia | Amplitud | Potencia |
|-----------|------------|----------|----------|
| Portadora | $f_c$ | $A_c$ | $P_c = A_c^2/2$ |
| Banda lateral inf. | $f_c - f_m$ | $mA_c/2$ | $m^2P_c/4$ |
| Banda lateral sup. | $f_c + f_m$ | $mA_c/2$ | $m^2P_c/4$ |

Potencia total de bandas laterales (informacion): $P_{SB} = m^2P_c/2$

## Ejemplo: Radio AM Comercial

Estacion en 1000 kHz, $P_{total} = 50$ kW, $m_{promedio} = 0.3$:

- Portadora: $P_c = 50/(1 + 0.09/2) = 47.85$ kW
- Eficiencia: $\eta = 0.09/2.09 = 4.3\%$
- Potencia en informacion: $2.15$ kW
- El **95.7%** de la potencia se desperdicia en portadora

Por esto las estaciones usan compresion de audio para mantener $m$ alto [analysis].

## Analogia

El indice de modulacion es como el volumen de tu voz en una conversacion ruidosa: muy suave ($m$ pequeño) → mensaje se pierde; gritar ($m > 1$) → voz se distorsiona. Existe un punto optimo ($m$ cercano a 1) [analysis].

## Puntos Clave

- ✓ $m$ debe ser $\leq 1$ para evitar distorsion [source — [[../../explicaciones_anki/unidad_03/carta_13_indice_modulacion_am]]]
- ✓ Eficiencia maxima teorica: $33.33\%$ (con $m = 1$) [source — [[../../explicaciones_anki/unidad_03/carta_13_indice_modulacion_am]]]
- ✓ $m > 1$ causa distorsion **catastrofica**, no gradual [source — [[../../explicaciones_anki/unidad_03/carta_13_indice_modulacion_am]]]
- ✓ $m = 0.99$ → señal limpia; $m = 1.01$ → señal destruida

## Ver tambien

- [[../modulacion-analogica/am-vs-dsb-sc]]
- [[../derivaciones/modulacion-am]]
- [[../ruido/efecto-umbral]]
