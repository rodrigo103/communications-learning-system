# Carta 48: Códigos Detectores y Correctores de Errores

> **Unidad 9**: Teoría de la Información

---

## 🎯 Pregunta

¿Qué son los códigos detectores y correctores de errores? Dé ejemplos.

---

## 📝 Respuesta Breve (de la carta original)

**Códigos de canal** agregan redundancia controlada para detectar/corregir errores de transmisión.

**Códigos Detectores**:
- Detectan errores pero no pueden corregirlos
- Ejemplo simple: **bit de paridad**
- Requieren retransmisión (ARQ)

**Códigos Correctores (FEC)**:
- Detectan Y corrigen errores sin retransmisión
- Requieren más redundancia

**Ejemplos**:

*Códigos de bloque*:
- **Hamming (7,4)**: 4 bits datos, 3 bits paridad, corrige 1 error
- **Reed-Solomon**: muy usado (CD, DVD, QR, espacio)
- **BCH**: flexible, potente

*Códigos convolucionales*:
- **Viterbi decoding**: usado en telefonía móvil
- **Turbo codes**: cerca del límite de Shannon

**Parámetro clave**: distancia de Hamming → capacidad de detección/corrección

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

**¿Por qué es importante este concepto?** Los códigos detectores y correctores de errores son la razón por la cual las comunicaciones digitales modernas funcionan de manera confiable. Sin ellos, cada bit corrupto en una transmisión WiFi causaría pérdida de datos, cada rayón en un CD lo haría inservible, y las comunicaciones espaciales serían imposibles. Estos códigos transforman canales ruidosos e imperfectos en enlaces virtuales casi libres de errores.

**¿Dónde se aplica?** La codificación de canal está omnipresente en el mundo digital:
- **Almacenamiento**: Discos duros, SSDs, CDs, DVDs, Blu-ray utilizan Reed-Solomon
- **Comunicaciones móviles**: 4G/5G emplean Turbo codes y LDPC
- **Internet**: TCP/IP usa checksums, WiFi emplea códigos convolucionales
- **Espacio**: Voyager usó códigos concatenados, Mars rovers usan Turbo codes
- **Códigos QR**: Pueden recuperarse incluso con 30% de daño gracias a Reed-Solomon

**¿Cuándo lo encontrarás?** Los códigos de canal se aplican después de la codificación de fuente pero antes de la modulación. Son la última línea de defensa digital antes de convertir los bits en señales analógicas, y la primera protección al recibir.

**Historia**: Richard Hamming desarrolló los primeros códigos correctores en 1950 mientras trabajaba en Bell Labs, frustrado porque las computadoras se detenían por errores simples. Claude Shannon había demostrado teóricamente en 1948 que era posible la comunicación libre de errores, pero Hamming fue el primero en mostrar cómo hacerlo prácticamente.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Distancia de Hamming**: número de bits diferentes entre dos palabras
- **Espacio de códigos**: conjunto de todas las palabras código válidas
- **Teorema de Shannon (Carta 45)**: establece que es posible comunicación libre de errores

#### Desarrollo Paso a Paso

**Paso 1: El Problema Fundamental**

En cualquier canal real, los bits pueden corromperse por ruido, interferencia, o imperfecciones del medio. Si transmitimos "1011", podríamos recibir "1001" (error en el tercer bit). Sin protección, este error es indetectable e incorregible.

**Paso 2: La Solución - Redundancia Controlada**

La idea clave es agregar bits extra (redundancia) de manera sistemática. No cualquier redundancia sirve; debe seguir reglas matemáticas precisas que permitan:
1. Detectar cuándo ocurrió un error
2. Idealmente, determinar qué bit(s) se corrompieron
3. Corregir los errores automáticamente

**Paso 3: Clasificación de Códigos**

Los códigos se clasifican según su estructura y capacidad:

**Por estructura:**
- **Códigos de bloque**: procesan bloques fijos de k bits → n bits (n > k)
- **Códigos convolucionales**: procesan flujo continuo con memoria

**Por capacidad:**
- **Solo detección**: identifican errores pero requieren retransmisión
- **Corrección directa (FEC)**: corrigen errores sin retransmisión

#### Derivación Matemática

**Capacidad de detección y corrección:**

Para un código con distancia mínima de Hamming $d_{min}$:

**Capacidad de detección:**
$$e_d = d_{min} - 1$$

Un código puede detectar hasta $e_d$ errores porque cualquier patrón de error con ≤ $e_d$ bits no puede transformar una palabra código válida en otra válida.

**Capacidad de corrección:**
$$e_c = \left\lfloor \frac{d_{min} - 1}{2} \right\rfloor$$

Para corregir, necesitamos que la palabra recibida esté más cerca de la palabra correcta que de cualquier otra palabra código.

**Ejemplo - Código de Hamming (7,4):**

Matriz generadora:
$$G = \begin{pmatrix}
1 & 0 & 0 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 0 & 1 & 1 & 0 \\
0 & 0 & 1 & 0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1 & 1 & 1 & 1
\end{pmatrix}$$

Matriz de paridad:
$$H = \begin{pmatrix}
1 & 1 & 0 & 1 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 1 & 0 & 0 & 1
\end{pmatrix}$$

**Síndrome para detección/corrección:**
$$\boxed{s = H \cdot r^T}$$

donde $r$ es la palabra recibida. Si $s = 0$, no hay error. Si $s ≠ 0$, el síndrome indica la posición del error.

### 🔬 Intuición y Analogías

**Analogía principal:**

Imagina enviar un paquete frágil por correo. El código detector es como el número de seguimiento - te dice si llegó correctamente pero no puede reparar daños. El código corrector es como embalar el objeto con espuma protectora y piezas de repuesto - el paquete puede autorrepararse de daños menores.

**Intuición física:**

Los códigos correctores funcionan creando "esferas" de palabras código en el espacio de Hamming. Si una palabra se corrompe ligeramente, todavía cae dentro de la esfera de la palabra original, permitiendo la corrección. Es como tener tolerancias en ingeniería mecánica.

**Visualización:**

En un espacio de 3 bits, tenemos 8 posibles palabras (000 a 111). Si solo usamos 2 como palabras código válidas (000 y 111), tienen distancia 3. Cualquier error simple nos deja más cerca de la palabra original:
- 000 con 1 error → 001, 010, o 100 (todas más cerca de 000)
- 111 con 1 error → 110, 101, o 011 (todas más cerca de 111)

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Bit de Paridad Simple

**Situación:** Transmitir el byte 10110011 con protección básica.

**Datos:**
| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| Datos originales | 10110011 | 8 bits |
| Tipo de paridad | Par | Número par de 1s |
| Bits de 1s | 5 | Impar |

**Solución paso a paso:**

1. **Contar 1s en datos originales:**
   $$\text{Número de 1s} = 5 \text{ (impar)}$$

2. **Calcular bit de paridad:**
   $$\text{Bit de paridad} = 1 \text{ (para hacer el total par)}$$

3. **Palabra transmitida:**
   $$\boxed{101100111 \text{ (9 bits)}}$$

**Detección:** Si se recibe 101100101 (error en bit 7), la paridad es impar → error detectado (pero no sabemos dónde).

---

#### Ejemplo 2: Código de Hamming (7,4) en Acción

**Contexto:** Transmitir 1011 usando Hamming (7,4).

**Codificación:**
| Bit de datos | d1 | d2 | d3 | d4 |
|--------------|----|----|----|----|
| Valor | 1 | 0 | 1 | 1 |

**Cálculo de bits de paridad:**
- p1 = d1 ⊕ d2 ⊕ d4 = 1 ⊕ 0 ⊕ 1 = 0
- p2 = d1 ⊕ d3 ⊕ d4 = 1 ⊕ 1 ⊕ 1 = 1
- p3 = d2 ⊕ d3 ⊕ d4 = 0 ⊕ 1 ⊕ 1 = 0

**Palabra código:** 1011010

**Simulación de error:** Se recibe 1011110 (error en bit 5)
- Síndrome: s = [1, 0, 1] = 5 en binario
- **Corrección:** Flip bit 5 → 1011010 ✓

---

#### Ejemplo 3: Reed-Solomon en un CD de Audio

**Contexto:** Un CD usa Reed-Solomon RS(255,223) con símbolos de 8 bits.

**Parámetros:**
- 223 símbolos de datos
- 32 símbolos de paridad
- Puede corregir hasta 16 símbolos erróneos

**¿Qué pasa cuando hay un rayón?**

Si un rayón daña 2mm del CD:
- A 1.2 m/s de velocidad lineal = 1.67 ms de datos perdidos
- A 44.1 kHz × 16 bits × 2 canales = 2,940 bits afectados
- Equivale a ~368 bytes = 368 símbolos

Sin corrección: pérdida total de audio
Con RS + interleaving: los 368 símbolos se dispersan en múltiples bloques, cada uno con ≤16 errores → **recuperación perfecta**

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Teorema de Shannon** (Carta 45): Establece que existe codificación para R < C
- **BER y Eb/N0** (Carta 31): Los códigos mejoran BER para mismo Eb/N0
- **Modulación digital** (Cartas 27-32): Se combina con FEC para sistemas robustos

#### Dependencias (lo que necesitas saber primero)
1. **Álgebra lineal**: Operaciones con matrices para códigos de bloque
2. **Campos finitos (Galois)**: Base matemática de Reed-Solomon
3. **Teoría de probabilidad**: Para analizar rendimiento

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Sistemas de comunicación modernos**: Todos usan FEC
2. **Almacenamiento confiable**: RAID, sistemas distribuidos
3. **Computación cuántica**: Códigos cuánticos correctores

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La diferencia fundamental entre detección y corrección
- Cómo la distancia de Hamming determina la capacidad del código
- El trade-off entre redundancia y capacidad de corrección
- Por qué los códigos son esenciales para alcanzar la capacidad de Shannon

#### Tipos de problemas típicos
1. **Calcular capacidad de detección/corrección**: Dado $d_{min}$, hallar $e_d$ y $e_c$
   - Estrategia: Aplicar fórmulas $e_d = d_{min} - 1$, $e_c = \lfloor(d_{min} - 1)/2\rfloor$

2. **Codificar/decodificar con Hamming**: Aplicar matrices G y H
   - Estrategia: Multiplicación matricial, interpretación de síndrome

3. **Análisis de rendimiento**: Calcular probabilidad de error residual
   - Estrategia: Usar distribución binomial para probabilidad de > $e_c$ errores

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir tasa del código con eficiencia**
- Por qué ocurre: R = k/n parece eficiencia pero es solo la fracción de bits útiles
- Cómo evitarlo: Eficiencia real incluye ganancia de codificación y mejora en BER
- Ejemplo: Un código con R = 0.5 puede ser muy eficiente si permite usar modulación de alto orden

❌ **Error #2: Pensar que más redundancia siempre es mejor**
- Por qué ocurre: Intuitivamente parece que más protección = mejor
- Cómo evitarlo: Existe un óptimo. Demasiada redundancia reduce la tasa efectiva
- Límite: Shannon dice que existe un código óptimo para cada canal

❌ **Error #3: Ignorar la latencia en códigos convolucionales**
- Distinción importante: Códigos de bloque procesan inmediatamente, convolucionales tienen memoria
- Impacto: En aplicaciones de tiempo real, la latencia puede ser crítica

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Detección: e_d = d_min - 1
Corrección: e_c = ⌊(d_min - 1)/2⌋
Tasa del código: R = k/n
Límite de Singleton: d_min ≤ n - k + 1
```

#### Conceptos Fundamentales
- ✓ **Distancia mínima es clave**: Determina toda la capacidad del código
- ✓ **Trade-off fundamental**: Tasa vs. capacidad de corrección
- ✓ **FEC vs. ARQ**: Forward Error Correction vs. Automatic Repeat Request
- ✓ **Límite de Shannon alcanzable**: Turbo y LDPC se acercan al límite teórico

#### Reglas Mnemotécnicas
- 🧠 **"DCC"**: Distancia determina Capacidad de Corrección
- 🧠 **Hamming (7,4)**: "7 total, 4 datos, 3 paridad, 1 error corregible"

#### Valores Típicos (para referencias rápidas)
| Sistema | Código | Capacidad | Overhead |
|---------|--------|-----------|----------|
| WiFi 802.11 | Convolucional | BER 10^-5 → 10^-10 | 50-75% |
| 4G LTE | Turbo | Cerca de Shannon | Variable |
| DVD | Reed-Solomon | Corrige ráfagas | 13% |
| QR Code | RS + estructura | Hasta 30% daño | 7-30% |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**: Lin & Costello "Error Control Coding" - La biblia del tema
- **Papers**: Berrou et al. (1993) sobre Turbo codes - Revolucionario
- **Simulación**: GNU Radio tiene bloques FEC para experimentar

#### Temas Relacionados para Explorar
1. **Códigos LDPC**: Low-Density Parity Check - Usados en 5G
2. **Códigos polares**: Los más recientes, probadamente óptimos
3. **Códigos fuente**: LT codes, Raptor codes para erasure channels

#### Preguntas para Reflexionar
- ¿Por qué los Turbo codes fueron tan revolucionarios cuando aparecieron en 1993?
- ¿Cómo se puede demostrar que un código alcanza la capacidad del canal?
- ¿Qué tipo de código sería óptimo para comunicaciones con Marte?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 50 minutos
**Prerequisitos críticos**: Álgebra lineal, probabilidad, teoría de Shannon
**Tags**: `#codigos-canal` `#FEC` `#hamming` `#reed-solomon` `#correccion-errores`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*