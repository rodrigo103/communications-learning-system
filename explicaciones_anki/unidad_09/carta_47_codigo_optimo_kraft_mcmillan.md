# Carta 47: Códigos Óptimos y el Criterio de Kraft-McMillan

> **Unidad 9**: Teoría de la Información

---

## 🎯 Pregunta

Explique qué es un código óptimo o compacto según el criterio de Kraft-McMillan.

---

## 📝 Respuesta Breve (de la carta original)

Un **código óptimo** (o compacto) minimiza la longitud promedio de palabra código.

**Criterio de Kraft-McMillan** (para código instantáneo):
$$\sum_{i=1}^{n} 2^{-l_i} ≤ 1$$

donde $l_i$ = longitud del código i

**Código óptimo**:
- Satisface desigualdad de Kraft (es instantáneo/únicamente decodificable)
- Longitud promedio $\bar{L}$ satisface: $H ≤ \bar{L} < H + 1$
- Asigna códigos más cortos a símbolos más probables

**Ejemplos**:
- **Huffman coding**: construye código óptimo
- **Shannon-Fano**: aproximación

**Límite**: ningún código puede tener $\bar{L} < H$ (entropía es límite inferior)

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

**¿Por qué es importante este concepto?** Los códigos óptimos son fundamentales en la compresión de datos y la transmisión eficiente de información. En sistemas de comunicaciones modernos, desde la compresión de archivos en tu smartphone hasta la transmisión de video en Netflix, los códigos óptimos permiten reducir drásticamente la cantidad de bits necesarios para representar información, sin pérdida alguna de contenido.

**¿Dónde se aplica?** Los códigos óptimos aparecen en prácticamente todos los sistemas digitales modernos:
- **Compresión de archivos**: ZIP, RAR, 7z utilizan variantes de codificación Huffman
- **Transmisión de video**: H.264, H.265 emplean códigos de longitud variable
- **Comunicaciones móviles**: LTE y 5G optimizan la codificación de señalización
- **Almacenamiento digital**: SSDs y discos duros comprimen datos internamente

**¿Cuándo lo encontrarás?** Este concepto surge en la etapa de codificación de fuente, antes de la transmisión. Es el primer paso para maximizar la eficiencia del sistema de comunicaciones, eliminando redundancia innecesaria antes de aplicar codificación de canal para protección contra errores.

**Historia**: El teorema de Kraft fue publicado por Leon Kraft en 1949 como parte de su tesis de maestría en MIT. McMillan demostró independientemente el mismo resultado en 1956, extendiendo su aplicabilidad. Estos trabajos formalizaron matemáticamente las condiciones para códigos eficientes que Shannon había intuido en 1948.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Entropía de Shannon** (Carta 44): medida de información promedio
- **Teoría de códigos**: representación binaria de símbolos
- **Árbol de decisión binario**: estructura de decodificación

#### Desarrollo Paso a Paso

**Paso 1: Comprensión de la Codificación de Fuente**

Un código de fuente asigna una secuencia binaria (palabra código) a cada símbolo de un alfabeto. Por ejemplo:
- Símbolo A → 00
- Símbolo B → 01
- Símbolo C → 10
- Símbolo D → 110

El objetivo es minimizar la longitud promedio de las palabras código mientras se mantiene la capacidad de decodificación única.

**Paso 2: Propiedad de Código Instantáneo**

Un código es **instantáneo** (o de prefijo) si ninguna palabra código es prefijo de otra. Esto permite decodificación inmediata sin necesidad de ver símbolos futuros. En el ejemplo anterior, el código no es instantáneo porque "1" sería ambiguo.

**Paso 3: Formalización del Criterio de Kraft-McMillan**

Para cualquier código únicamente decodificable con longitudes de palabra $l_1, l_2, ..., l_n$:

$$\sum_{i=1}^{n} 2^{-l_i} \leq 1$$

Esta desigualdad establece una condición necesaria y suficiente para la existencia de un código instantáneo con esas longitudes.

#### Derivación Matemática

**Partiendo del árbol de decisión binario:**

Consideremos un árbol binario completo de profundidad $L_{max}$ = longitud máxima del código.

$$\text{Número total de hojas} = 2^{L_{max}}$$

**Paso de derivación 1:**

Cada palabra código de longitud $l_i$ "bloquea" $2^{L_{max} - l_i}$ hojas potenciales en el árbol (sus descendientes).

$$\text{Hojas bloqueadas por símbolo i} = 2^{L_{max} - l_i}$$

**Paso de derivación 2:**

La suma de todas las hojas bloqueadas no puede exceder el total disponible:

$$\sum_{i=1}^{n} 2^{L_{max} - l_i} \leq 2^{L_{max}}$$

**Resultado final:**

Dividiendo ambos lados por $2^{L_{max}}$:

$$\boxed{\sum_{i=1}^{n} 2^{-l_i} \leq 1}$$

**Significado físico de cada término:**
- $2^{-l_i}$: fracción del espacio de códigos que ocupa el símbolo i
- $\sum 2^{-l_i}$: espacio total ocupado por todos los símbolos
- La desigualdad garantiza que hay "espacio suficiente" en el árbol binario

### 🔬 Intuición y Analogías

**Analogía principal:**

Imagina que tienes una pizza (el espacio total de códigos binarios) que debes dividir entre varios comensales (símbolos). Cada comensal necesita una porción, pero algunos necesitan porciones más grandes (códigos más cortos = mayor porción). El criterio de Kraft-McMillan dice que la suma de todas las porciones no puede exceder una pizza completa.

**Intuición física:**

Los códigos cortos son "caros" en términos de espacio de códigos. Un código de 1 bit ocupa la mitad del espacio total (2^(-1) = 0.5), mientras que un código de 4 bits solo ocupa 1/16 del espacio (2^(-4) = 0.0625). No puedes asignar códigos cortos a todos porque te quedarías sin espacio.

**Visualización:**

Imagina el árbol binario de decodificación. Cada bifurcación representa un bit (izquierda = 0, derecha = 1). Los símbolos se colocan en las hojas. Si colocas un símbolo en un nodo intermedio (código corto), bloqueas todo el subárbol debajo de él.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Verificación del Criterio de Kraft

**Situación:** Verificar si es posible construir un código instantáneo con las siguientes longitudes:

**Datos:**
| Símbolo | Longitud deseada | 2^(-l_i) |
|---------|------------------|----------|
| A | 1 | 0.5 |
| B | 2 | 0.25 |
| C | 3 | 0.125 |
| D | 3 | 0.125 |

**Solución paso a paso:**

1. **Calcular la suma de Kraft:**
   $$K = 2^{-1} + 2^{-2} + 2^{-3} + 2^{-3}$$
   $$K = 0.5 + 0.25 + 0.125 + 0.125$$

2. **Verificar la desigualdad:**
   $$K = 1.0 \leq 1$$

3. **Resultado:**
   $$\boxed{K = 1.0 \text{ - Código posible y óptimo (igualdad)}}$$

**Interpretación:** Como K = 1, el código es posible y no desperdicia ningún bit. Un código concreto sería: A→0, B→10, C→110, D→111.

---

#### Ejemplo 2: Código de Huffman para Texto en Español

**Contexto:** Comprimir un texto en español donde las letras más frecuentes son:

| Letra | Probabilidad | Código Huffman | Longitud |
|-------|--------------|----------------|----------|
| E | 0.14 | 00 | 2 |
| A | 0.12 | 01 | 2 |
| O | 0.09 | 100 | 3 |
| S | 0.08 | 101 | 3 |
| N | 0.07 | 110 | 3 |
| Otros | 0.50 | varios | 4-8 |

**Verificación de Kraft:**
$$K = 2 \times 2^{-2} + 3 \times 2^{-3} + ... \approx 0.99 < 1$$

**Longitud promedio:**
$$\bar{L} = 0.14 \times 2 + 0.12 \times 2 + 0.09 \times 3 + ... \approx 3.8 \text{ bits/letra}$$

**Comparación:** Sin codificación óptima necesitaríamos $\lceil \log_2(27) \rceil = 5$ bits/letra. El ahorro es del 24%.

---

#### Ejemplo 3: Caso Límite - Código Uniforme vs. Óptimo

**¿Qué pasa cuando todos los símbolos son equiprobables?**

Si tenemos 8 símbolos con $p_i = 1/8$ para todo i:

- **Entropía**: $H = -8 \times (1/8) \times \log_2(1/8) = 3$ bits
- **Código uniforme**: todos con longitud 3 → $\bar{L} = 3$ bits
- **Verificación Kraft**: $8 \times 2^{-3} = 1$ ✓

**Conclusión**: Cuando los símbolos son equiprobables, el código uniforme ES óptimo. La optimización solo ayuda cuando hay diferencias en las probabilidades.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Entropía** (Carta 44): Límite inferior teórico para $\bar{L}$
- **Redundancia** (Carta 46): Lo que los códigos óptimos eliminan
- **Teorema de Shannon** (Carta 45): Establece los límites de compresión

#### Dependencias (lo que necesitas saber primero)
1. **Teoría de probabilidad** → Para entender distribuciones de símbolos
2. **Sistemas binarios** → Base de la codificación digital
3. **Árboles de decisión** → Estructura de decodificación

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Codificación de canal**: Después de comprimir, se protege contra errores
2. **Multiplexación estadística**: Asignación dinámica de recursos
3. **Compresión con pérdida**: Extensión a cuantización óptima

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La diferencia entre código instantáneo y únicamente decodificable
- Por qué la suma de Kraft no puede exceder 1 (interpretación del espacio de códigos)
- La relación entre entropía y longitud promedio mínima
- Cómo construir un código dado un conjunto de longitudes que satisfacen Kraft

#### Tipos de problemas típicos
1. **Verificación de Kraft**: Dadas las longitudes, ¿es posible el código?
   - Estrategia: Calcular $\sum 2^{-l_i}$ y verificar ≤ 1

2. **Construcción de código óptimo**: Dadas las probabilidades, hallar el código
   - Estrategia: Aplicar algoritmo de Huffman

3. **Cálculo de eficiencia**: Comparar $\bar{L}$ con entropía H
   - Estrategia: Eficiencia = H/$\bar{L}$ × 100%

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir Kraft con optimalidad**
- Por qué ocurre: Satisfacer Kraft no garantiza que el código sea óptimo
- Cómo evitarlo: Kraft es condición necesaria pero no suficiente para optimalidad
- Ejemplo: {2, 2, 2, 2} satisface Kraft para 4 símbolos, pero puede no ser óptimo si las probabilidades son muy diferentes

❌ **Error #2: Olvidar que Kraft aplica a códigos únicamente decodificables**
- Por qué ocurre: Se piensa que solo aplica a códigos instantáneos
- Cómo evitarlo: McMillan demostró que aplica a TODOS los códigos únicamente decodificables

❌ **Error #3: Intentar violar el límite de entropía**
- Distinción importante: Ningún código sin pérdida puede tener $\bar{L} < H$
- Shannon demostró que H es el límite fundamental

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Desigualdad de Kraft-McMillan: ∑ 2^(-l_i) ≤ 1
Límite de Shannon: H ≤ L̄ < H + 1
Eficiencia del código: η = H/L̄
```

#### Conceptos Fundamentales
- ✓ **Kraft = Existencia**: Si satisface Kraft, existe un código instantáneo con esas longitudes
- ✓ **Óptimo = Mínima longitud promedio**: Minimiza $\bar{L} = \sum p_i l_i$
- ✓ **Huffman siempre óptimo**: Algoritmo garantizado para códigos de prefijo óptimos

#### Reglas Mnemotécnicas
- 🧠 **"KILO"**: Kraft Indica Longitudes Óptimas (posibles)
- 🧠 **Suma ≤ 1**: "No puedes gastar más espacio del que tienes"

#### Valores Típicos (para referencias rápidas)
| Aplicación | Compresión típica | Método |
|------------|-------------------|---------|
| Texto inglés | 60-70% | Huffman adaptativo |
| Imágenes (sin pérdida) | 40-60% | PNG (Huffman + filtros) |
| Audio (sin pérdida) | 50-70% | FLAC (códigos de Rice) |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Cover & Thomas "Elements of Information Theory" Cap. 5
- **Papers originales**: Kraft (1949), McMillan (1956)
- **Implementaciones**: Estudiar código fuente de zlib (implementación de Huffman)

#### Temas Relacionados para Explorar
1. **Códigos aritméticos**: Superan la barrera del bit entero
2. **Codificación adaptativa**: Ajuste dinámico a estadísticas cambiantes
3. **Compresión universal**: Lempel-Ziv y sus variantes

#### Preguntas para Reflexionar
- ¿Por qué exactamente la igualdad en Kraft (K = 1) indica uso óptimo del espacio?
- ¿Cómo se extiende Kraft-McMillan a alfabetos no binarios (D-arios)?
- ¿Qué pasa con la codificación cuando la fuente tiene memoria (correlación)?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 45 minutos
**Prerequisitos críticos**: Entropía, probabilidad, árboles binarios
**Tags**: `#teoria-informacion` `#codificacion-fuente` `#kraft-mcmillan` `#huffman` `#compresion`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*