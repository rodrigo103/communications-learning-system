# Carta 52: CDMA - Acceso Múltiple por División de Código

> **Unidad 10**: Espectro Expandido y OFDM

---

## 🎯 Pregunta

Explique el principio de CDMA (Code Division Multiple Access).

---

## 📝 Respuesta Breve (de la carta original)

**CDMA** permite que múltiples usuarios compartan simultáneamente la misma banda de frecuencia usando códigos ortogonales únicos.

**Principio**:
1. Cada usuario tiene código PN único
2. Transmisor: datos × código → señal expandida
3. Todos transmiten en misma frecuencia simultáneamente
4. Receptor: señal recibida × mismo código → recupera datos
   - Señales con códigos diferentes aparecen como ruido
   - **Correlación**: alta con código correcto, baja con otros

**Requisitos clave**:
- Códigos **ortogonales** o casi-ortogonales (baja correlación cruzada)
- Sincronización precisa
- Control de potencia (problema near-far)

**Ventajas**:
- Capacidad flexible (soft capacity)
- Inmunidad a interferencias
- Handoff suave en celular

**Aplicaciones**: 3G (IS-95, CDMA2000, WCDMA)

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

**¿Por qué es importante CDMA?** CDMA revolucionó las comunicaciones móviles en los años 90 y fue la base de las redes 3G mundiales. A diferencia de FDMA (donde cada usuario tiene su frecuencia) o TDMA (donde cada usuario tiene su intervalo de tiempo), CDMA permite que todos los usuarios transmitan simultáneamente en la misma frecuencia. Esta aparente contradicción se resuelve mediante el uso inteligente de códigos matemáticos.

**¿Dónde se aplica?** CDMA fue fundamental en:
- **Sistemas celulares 3G**: IS-95 (cdmaOne), CDMA2000, WCDMA/UMTS
- **GPS**: todos los satélites transmiten en las mismas frecuencias
- **WiFi 802.11b**: usa CDMA con DSSS
- **Comunicaciones militares**: resistencia a jamming e interceptación

**¿Cuándo lo encontrarás?** En el diseño de sistemas de múltiple acceso donde se requiere:
- Flexibilidad en la asignación de recursos
- Operación en ambientes con alta interferencia
- Privacidad inherente en la capa física
- Soft handoff entre celdas

**Historia:** Desarrollado originalmente por Qualcomm a fines de los 80, basándose en técnicas de espectro expandido militares de la Segunda Guerra Mundial (Hedy Lamarr y George Antheil patentaron una forma primitiva en 1942).

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Espectro expandido (Carta 50)
- Secuencias PN (Pseudo-Noise)
- Correlación y ortogonalidad de señales
- DSSS - Direct Sequence Spread Spectrum (Carta 51)

#### Desarrollo Paso a Paso

**Paso 1: Generación de Códigos Únicos**

Cada usuario recibe un código spreading único, típicamente una secuencia PN (pseudo-aleatoria) o código Walsh. Estos códigos tienen propiedades especiales:
- **Longitud**: N chips (típicamente 64, 128, o 256)
- **Chip rate**: mucho mayor que bit rate (factor de spreading)
- **Autocorrelación alta**: el código correlaciona bien consigo mismo
- **Correlación cruzada baja**: correlaciona mal con otros códigos

**Paso 2: Proceso de Spreading (Transmisor)**

Para transmitir un bit de datos:
1. El bit de datos (±1) se multiplica por el código de spreading
2. Si bit = +1: se transmite el código tal cual
3. Si bit = -1: se transmite el código invertido
4. La señal resultante ocupa mucho más ancho de banda

**Paso 3: Transmisión Simultánea**

Todos los usuarios transmiten en el mismo canal al mismo tiempo:
- Las señales se suman linealmente en el aire
- Cada señal individual parece ruido para los demás
- La potencia de cada usuario se distribuye sobre el ancho de banda expandido

**Paso 4: Proceso de Despreading (Receptor)**

El receptor correlaciona la señal recibida con su código:
1. Multiplica la señal recibida por el código del usuario deseado
2. Integra sobre la duración del bit
3. Las señales con otros códigos promedian a ~0 (ruido)
4. La señal deseada se recupera con ganancia de procesamiento

#### Derivación Matemática

**Modelo de transmisión CDMA:**

Para K usuarios activos, la señal recibida es:

$$r(t) = \sum_{k=1}^{K} A_k d_k(t) c_k(t) \cos(2\pi f_c t + \phi_k) + n(t)$$

Donde:
- $A_k$ = amplitud del usuario k
- $d_k(t)$ = datos del usuario k (±1)
- $c_k(t)$ = código spreading del usuario k
- $\phi_k$ = fase del usuario k
- $n(t)$ = ruido AWGN

**Proceso de correlación para usuario 1:**

$$y_1 = \int_0^{T_b} r(t) c_1(t) \cos(2\pi f_c t) dt$$

Expandiendo:

$$y_1 = A_1 d_1 \int_0^{T_b} c_1^2(t) \cos^2(2\pi f_c t) dt + \sum_{k=2}^{K} A_k d_k \int_0^{T_b} c_k(t)c_1(t) \cos^2(2\pi f_c t) dt + n'$$

**Resultado después de la correlación:**

$$\boxed{y_1 = \frac{A_1 T_b}{2} d_1 + \text{interferencia} + \text{ruido}}$$

**Significado físico:**
- Primer término: señal deseada amplificada por $T_b/2$
- Segundo término: interferencia de otros usuarios (MAI - Multiple Access Interference)
- Tercer término: ruido térmico

La clave es que si los códigos son ortogonales: $\int c_k(t)c_1(t)dt = 0$ para $k \neq 1$

### 🔬 Intuición y Analogías

**Analogía principal: La fiesta de cóctel**

Imagina una fiesta donde muchas personas hablan simultáneamente:
- **Sin CDMA**: todos hablan el mismo idioma → cacofonía incomprensible
- **Con CDMA**: cada pareja habla un idioma diferente → puedes enfocarte en tu idioma y filtrar los demás como ruido de fondo

Los "idiomas" son los códigos spreading - tu cerebro (receptor) correlaciona con el idioma conocido y rechaza los demás.

**Intuición física:**

CDMA es como pintar con colores que solo son visibles con filtros específicos:
1. Cada usuario "pinta" su información con un "color" único (código)
2. Todos pintan en el mismo lienzo (frecuencia) al mismo tiempo
3. Con el filtro correcto (correlación), solo ves un color
4. Los otros colores aparecen como un fondo grisáceo uniforme

**Visualización:**

Imagina el espectro de frecuencia como una autopista:
- FDMA: cada carro tiene su propio carril
- TDMA: los carros toman turnos para usar toda la autopista
- CDMA: todos los carros usan toda la autopista simultáneamente, pero cada uno tiene un "patrón de manejo" único que permite identificarlo

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Sistema CDMA Simple con 2 Usuarios

**Situación:** Dos usuarios transmitiendo bits simultáneamente

**Datos:**
| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| Código usuario 1 | [+1, +1, -1, -1] | Secuencia Walsh |
| Código usuario 2 | [+1, -1, +1, -1] | Ortogonal a usuario 1 |
| Bit usuario 1 | +1 | Dato a transmitir |
| Bit usuario 2 | -1 | Dato a transmitir |

**Solución paso a paso:**

1. **Señales transmitidas:**
   - Usuario 1: (+1) × [+1, +1, -1, -1] = [+1, +1, -1, -1]
   - Usuario 2: (-1) × [+1, -1, +1, -1] = [-1, +1, -1, +1]

2. **Señal combinada en el canal:**
   $$s_{total} = [+1, +1, -1, -1] + [-1, +1, -1, +1] = [0, +2, -2, 0]$$

3. **Recuperación usuario 1 (correlación):**
   $$y_1 = [0, +2, -2, 0] \cdot [+1, +1, -1, -1] = 0 + 2 + 2 + 0 = +4$$

   Decisión: +4 > 0 → bit = +1 ✓

**Interpretación:** A pesar de la interferencia, cada usuario puede recuperar su información mediante correlación con su código único.

---

#### Ejemplo 2: Sistema IS-95 Real

**Contexto:** Red celular CDMA comercial (Verizon, Sprint en USA)

**Especificaciones IS-95:**
| Parámetro | Valor | Significado |
|-----------|-------|-------------|
| Chip rate | 1.2288 Mcps | Velocidad de código |
| Bit rate voz | 9.6 kbps | Velocidad de datos |
| Processing gain | 128 (21 dB) | Factor de spreading |
| Códigos Walsh | 64 códigos | Ortogonales en downlink |
| Códigos PN largos | 2^42 - 1 | Para spreading adicional |
| Control de potencia | 800 Hz | Actualización rápida |

**Cálculo de capacidad (simplificado):**

$$K_{max} \approx \frac{W/R}{E_b/N_0} \cdot \frac{1}{(1+f)} \cdot \alpha \cdot \beta$$

Donde:
- W/R = 128 (processing gain)
- Eb/N0 = 7 dB = 5 (requerido)
- f = 0.6 (factor de reuso de frecuencia)
- α = 0.35 (factor de actividad de voz)
- β = 0.85 (sectorización)

$$K_{max} \approx \frac{128}{5} \cdot \frac{1}{1.6} \cdot 0.35 \cdot 0.85 \approx 4.75 \text{ usuarios/sector/portadora}$$

---

#### Ejemplo 3: Problema Near-Far

**¿Qué pasa cuando un usuario está mucho más cerca de la estación base?**

**Escenario:**
- Usuario A: 100m de la base, pérdida = 70 dB
- Usuario B: 2 km de la base, pérdida = 110 dB
- Diferencia: 40 dB = factor de 10,000 en potencia

**Sin control de potencia:**
- Usuario A llegaría 10,000 veces más fuerte
- Bloquearía completamente a usuario B
- Sistema colapsaría

**Con control de potencia (IS-95):**
- Lazo abierto: ajuste inicial basado en potencia recibida
- Lazo cerrado: comandos de ±1 dB a 800 Hz
- Rango dinámico: 80 dB
- Todos los usuarios llegan con potencia similar (±1 dB)

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Espectro Expandido** (Carta 50): CDMA es una aplicación de DSSS para múltiple acceso
- **DSSS** (Carta 51): base técnica de CDMA
- **OFDM** (Carta 53): tecnología competidora/complementaria en 4G/5G
- **Teoría de la Información** (Carta 45): capacidad multiusuario y límites de Shannon

#### Dependencias (lo que necesitas saber primero)
1. Correlación y productos internos → base matemática de la detección
2. Secuencias PN → generación de códigos spreading
3. Modulación digital básica → lo que se transmite antes del spreading

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Redes 3G**: entender WCDMA/CDMA2000
2. **GPS**: todos los satélites usan CDMA
3. **5G**: aunque usa OFDM, conceptos CDMA aparecen en NOMA
4. **IoT**: algunas tecnologías usan CDMA para bajo consumo

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La diferencia fundamental entre CDMA, FDMA y TDMA
- Por qué la ortogonalidad de códigos es crítica
- El rol del control de potencia en CDMA
- Cómo calcular la capacidad de un sistema CDMA

#### Tipos de problemas típicos
1. **Demostración de ortogonalidad**: Dados códigos Walsh, verificar ortogonalidad
   - Estrategia: calcular producto interno, debe ser 0

2. **Cálculo de capacidad**: Estimar usuarios soportados dado processing gain
   - Estrategia: usar fórmula de capacidad con factores de corrección

3. **Análisis near-far**: Calcular requerimientos de control de potencia
   - Estrategia: determinar rango dinámico necesario

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir CDMA con simple DSSS**
- Por qué ocurre: CDMA usa DSSS, pero agrega múltiple acceso
- Cómo evitarlo: DSSS es para un usuario, CDMA para múltiples
- Distinción: CDMA requiere gestión de códigos y potencia

❌ **Error #2: Asumir ortogonalidad perfecta en práctica**
- Por qué ocurre: teoría asume códigos perfectamente ortogonales
- Realidad: multitrayecto y asincronía destruyen ortogonalidad
- Solución: por eso existe MAI (interferencia de acceso múltiple)

❌ **Error #3: Ignorar el problema near-far**
- Por qué ocurre: no es obvio en el análisis teórico
- Impacto: sin control de potencia, CDMA no funciona
- Clave: control de potencia es tan importante como los códigos

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Processing Gain: Gp = W/R = Tchip/Tbit
Capacidad CDMA: K ≈ (W/R)/(Eb/N0) × factores_corrección
SNR después de despreading: SNRout = Gp × SNRin
```

#### Conceptos Fundamentales
- ✓ **Principio básico**: "Todos hablan a la vez, pero en diferentes idiomas"
- ✓ **Ortogonalidad**: la clave para separar usuarios
- ✓ **Control de potencia**: crítico para combatir near-far
- ✓ **Soft capacity**: no hay límite duro de usuarios

#### Reglas Mnemotécnicas
- 🧠 **CDMA = "Códigos Distinguen Múltiples Accesos"**
- 🧠 **Near-Far**: "El más Cercano Ahoga al más Lejano"
- 🧠 **MAI**: "Multiple Access Interference" - el ruido es de otros usuarios

#### Valores Típicos (para referencias rápidas)
| Parámetro | Valor Típico | Sistema |
|-----------|--------------|----------|
| Chip rate | 1.23 Mcps | IS-95 |
| Chip rate | 3.84 Mcps | WCDMA |
| Processing gain | 128-256 | Celular |
| Control potencia | 800-1500 Hz | Actualización |
| Códigos Walsh | 64-256 | Downlink |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**: Viterbi "CDMA: Principles of Spread Spectrum Communication"
- **Papers**: artículo original de Qualcomm sobre IS-95
- **Estándares**: 3GPP especificaciones de WCDMA
- **Simulaciones**: GNU Radio tiene bloques CDMA

#### Temas Relacionados para Explorar
1. Receptores Rake para combatir multitrayecto en CDMA
2. Soft handoff y diversidad de macrodiversidad
3. Turbo códigos en CDMA2000
4. Evolución de CDMA a OFDMA en 4G

#### Preguntas para Reflexionar
- ¿Por qué LTE abandonó CDMA en favor de OFDMA?
- ¿Cómo maneja CDMA la sincronización inicial sin canal dedicado?
- ¿Qué ventajas mantiene CDMA sobre OFDM en ciertos escenarios?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 35 minutos
**Prerequisitos críticos**: Espectro expandido, DSSS, correlación
**Tags**: `#cdma` `#multiple-access` `#3g` `#spreading` `#walsh-codes`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*