---
tags:
  - wiki/teoria-informacion
source_file: explicaciones_anki/unidad_09/carta_47_codigo_optimo_kraft_mcmillan.md
curso: Sistemas de Comunicaciones
unidad: 9
---

# Codigos Compactos y el Criterio de Kraft-McMillan

> **Last verified:** 2025-11-16 | **Verified by:** source

## Definicion

Un **codigo optimo** (o compacto) minimiza la longitud promedio de palabra codigo $\bar{L}$ para una fuente con distribucion de probabilidad conocida. Es la herramienta fundamental para la codificacion de fuente (compresion sin perdida). [source — [[../../explicaciones_anki/unidad_09/carta_47_codigo_optimo_kraft_mcmillan]]]

$$\bar{L} = \sum_{i=1}^{n} p_i \cdot l_i$$

donde $p_i$ es la probabilidad del simbolo $i$ y $l_i$ la longitud de su palabra codigo.

## Criterio de Kraft-McMillan

Para cualquier codigo **unicamente decodificable** (y en particular para codigos instantaneos o de prefijo), las longitudes $l_i$ deben satisfacer: [source — [[../../explicaciones_anki/unidad_09/carta_47_codigo_optimo_kraft_mcmillan]]]

$$\boxed{\sum_{i=1}^{n} 2^{-l_i} \leq 1}$$

### Significado

- Cada palabra codigo de longitud $l_i$ "ocupa" una fraccion $2^{-l_i}$ del espacio total de codigos
- La desigualdad garantiza que existe "espacio suficiente" en el arbol binario para todos los simbolos
- La igualdad ($\sum 2^{-l_i} = 1$) indica un codigo **completo** (sin desperdicio de espacio) [analysis]

### Interpretacion via Arbol Binario

En un arbol de profundidad $L_{max}$, cada palabra codigo bloquea $2^{L_{max} - l_i}$ hojas. La suma de hojas bloqueadas no puede exceder $2^{L_{max}}$, de donde:

$$\sum_i 2^{L_{max} - l_i} \leq 2^{L_{max}} \Rightarrow \sum_i 2^{-l_i} \leq 1$$

## Limite de Shannon para Codigos de Fuente

El teorema de codificacion de fuente establece que la longitud promedio de cualquier codigo sin perdida satisface: [source — [[../../explicaciones_anki/unidad_09/carta_47_codigo_optimo_kraft_mcmillan]]]

$$\boxed{H \leq \bar{L} < H + 1}$$

- **Limite inferior**: $\bar{L} \geq H$ — no se puede comprimir por debajo de la entropia
- **Limite superior**: $\bar{L} < H + 1$ — siempre existe un codigo dentro de 1 bit del optimo

La **eficiencia del codigo** es: $\eta = H / \bar{L} \leq 1$.

## Codigo de Huffman

Algoritmo que construye el codigo de prefijo optimo: [analysis]

1. Ordenar simbolos por probabilidad decreciente
2. Combinar los dos simbolos menos probables en un nuevo nodo (suma de probabilidades)
3. Repetir hasta obtener un solo arbol
4. Asignar 0 y 1 a las ramas; leer codigos desde la raiz

Propiedades:
- Siempre produce un codigo optimo para codigos de prefijo
- Asigna codigos mas cortos a simbolos mas probables
- Cuando todos los simbolos son equiprobables, el codigo uniforme es optimo

## Ejemplo Numerico

Para 4 simbolos con longitudes $\{l_1=1, l_2=2, l_3=3, l_4=3\}$:

$$\sum 2^{-l_i} = 2^{-1} + 2^{-2} + 2^{-3} + 2^{-3} = 0.5 + 0.25 + 0.125 + 0.125 = 1.0$$

$K = 1.0 \leq 1 \Rightarrow$ codigo posible y completo. Un codigo concreto: $A \to 0$, $B \to 10$, $C \to 110$, $D \to 111$.

## Relacion con Compresion

| Aplicacion | Compresion tipica | Metodo |
|-----------|-------------------|--------|
| Texto ingles | 60-70% | Huffman adaptativo |
| Imagenes (sin perdida) | 40-60% | PNG (Huffman + filtros) |
| Audio (sin perdida) | 50-70% | FLAC (codigos de Rice) |

## Errores Comunes

- **Confundir Kraft con optimalidad**: Kraft es condicion necesaria pero no suficiente para optimalidad. Un codigo puede satisfacer Kraft pero no ser optimo.
- **Olvidar que el limite $H$ es teorico**: $H$ puede no ser entero; las longitudes de codigo deben ser enteras.
- **Ignorar fuentes con memoria**: la entropia real es menor que la calculada sin considerar dependencias.

## Ver tambien

- [[../teoria-informacion/entropia-fuente]]
- [[../teoria-informacion/codigos-deteccion-error]]
- [[../teoria-informacion/teorema-shannon-hartley]]
- [[../teoria-informacion/capacidad-canal-shannon]]
