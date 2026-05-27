---
tags:
  - wiki/informacion
source_file: explicaciones_anki/unidad_09/carta_46_redundancia-compresion.md
curso: Sistemas de Comunicaciones
unidad: 9
---

# Redundancia y Compresion

> **Last verified:** 2025-11-16 | **Verified by:** [source — [[../../explicaciones_anki/unidad_09/carta_46_redundancia-compresion]]]

La redundancia es la diferencia entre la entropia real de una fuente y su maxima entropia posible. Cuantifica que tan ineficientemente esta representada la informacion y, equivalentemente, cuanto se puede comprimir.

## Definicion de redundancia

$$\boxed{\text{Redundancia} = 1 - \frac{H}{H_{\max}} = 1 - \frac{H}{\log_2(n)}}$$

donde $H$ es la entropia de la fuente y $H_{\max} = \log_2(n)$ es la maxima entropia posible (cuando todos los $n$ simbolos son equiprobables). [source — [[../../explicaciones_anki/unidad_09/carta_46_redundancia-compresion]]]

## Eficiencia de fuente

$$\boxed{\eta = \frac{H}{H_{\max}}}$$

Una fuente con $\eta = 1$ es perfectamente eficiente (sin redundancia). Fuentes con memoria o simbolos no equiprobables tienen $\eta < 1$.

## Limite de compresion sin perdida (Shannon)

El teorema de codificacion de fuente establece que la longitud media minima de un codigo sin perdida es:

$$\boxed{L_{\min} = H}$$

Ningun codigo sin perdida puede tener una longitud media menor que la entropia de la fuente. El factor de compresion maximo es:

$$\text{Compresion maxima} = \frac{H_{\max}}{H}$$

[source — [[../../explicaciones_anki/unidad_09/carta_46_redundancia-compresion]]]

## Redundancia como predictibilidad

La redundancia no es solo repeticion literal: es **predictibilidad estadistica**. Una fuente con memoria (Markov) tiene mas redundancia que una fuente sin memoria porque los simbolos futuros son parcialmente predecibles a partir de los pasados.

Ejemplo: los lenguajes naturales tienen ~50% de redundancia ("y cn lers ls letrs"). [analysis]

## Compromiso compresion vs robustez

| Prioridad | Estrategia |
|---|---|
| **Eficiencia** | Eliminar redundancia → maxima compresion |
| **Robustez** | Agregar redundancia controlada → correccion de errores |

La redundancia removida en compresion de fuente **no es la misma** que la redundancia agregada en codificacion de canal. La primera es ineficiencia estadistica; la segunda es proteccion contra errores. [analysis]

## Tipos de redundancia en distintos medios

| Medio | Redundancia tipica | Fuente |
|---|---|---|
| Texto | Patrones repetitivos, frecuencia de letras | Codigo Morse, Huffman |
| Audio | Enmascaramiento perceptual (no oimos todo) | MP3, AAC |
| Video | Correlacion temporal/espacial entre frames | H.264, H.265 |
| Imagenes | Pixeles vecinos correlacionados | JPEG, PNG |

## Compresion sin perdida vs con perdida

- **Lossless (sin perdida):** $L \geq H$ — Huffman, Lempel-Ziv, codigos aritmeticos. Aprovechan redundancia estadistica.
- **Lossy (con perdida):** $L < H$ — descartan informacion perceptual o numericamente irrelevante. Explotan limitaciones del sistema sensorial humano.

## Ejemplo: Codigo de Huffman

Dada una fuente con simbolos $\{A, B, C, D\}$ y probabilidades $\{0.5, 0.25, 0.125, 0.125\}$:
- $H = 1.75$ bits/simbolo
- Codigo compacto (Huffman): A=0, B=10, C=110, D=111
- Longitud media: $L = 0.5(1) + 0.25(2) + 0.125(3) + 0.125(3) = 1.75 = H$

Se alcanza el limite teorico porque las probabilidades son potencias de 2. [analysis]

## Ver también

- [[../teoria-informacion/entropia-fuente]] — Entropia de fuente
- [[../teoria-informacion/entropia]] — Entropia
- [[../teoria-informacion/codigo-compacto]] — Codigo compacto
- [[../teoria-informacion/teorema-shannon-hartley]] — Shannon-Hartley
- [[../teoria-informacion/codificacion-canal]] — Codificacion de canal
