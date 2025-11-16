# Carta 25: PCM vs Modulación Delta - Paradigmas de Digitalización

> **Unidad 5**: Modulación de Pulsos

---

## 🎯 Pregunta

Compare PCM con Modulación Delta (DM) y Delta Adaptativa (ADM).

---

## 📝 Respuesta Breve (de la carta original)

**PCM**:
- Transmite valor absoluto de cada muestra (n bits)
- Mayor tasa de bits pero mejor calidad
- Complejidad moderada

**Delta Modulation (DM)**:
- Transmite solo 1 bit por muestra (incremento/decremento)
- Tasa de bits muy baja
- Problemas: slope overload, granular noise
- Simple pero calidad limitada

**Adaptive Delta Modulation (ADM)**:
- Paso de cuantificación variable (adaptativo)
- Soluciona problemas de DM estándar
- Mejor balance complejidad/calidad
- Usado en aplicaciones de baja tasa (codecs de voz)

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La comparación entre **PCM** y **Modulación Delta** representa uno de los trade-offs fundamentales en comunicaciones digitales: complejidad y calidad versus simplicidad y eficiencia de ancho de banda. Estos dos enfoques representan filosofías opuestas para digitalizar señales analógicas, cada una con sus ventajas en diferentes escenarios.

**¿Por qué es importante este concepto?** La elección entre PCM y DM (o sus variantes) determina la arquitectura completa del sistema de comunicaciones. PCM domina en aplicaciones de alta calidad (telefonía, audio profesional), mientras que DM y ADM encuentran nichos en sistemas con ancho de banda muy limitado o requisitos de ultra-baja complejidad.

**¿Dónde se aplica?**
- **PCM**: Telefonía digital (PSTN), audio CD, sistemas profesionales
- **DM**: Sistemas militares antiguos, telemetría simple
- **ADM**: Comunicaciones tácticas, codecs de voz de baja tasa, sistemas embebidos
- **CVSD** (variante de ADM): Bluetooth (versión clásica), radios militares

**Historia relevante:** La Modulación Delta fue inventada en 1946 por E.M. Deloraine en los laboratorios ITT de Francia, predatando al PCM práctico. Sin embargo, PCM se volvió dominante con la llegada de circuitos integrados baratos. ADM fue desarrollada en los 1960s para resolver las limitaciones de DM, y CVSD (Continuously Variable Slope Delta modulation) se convirtió en estándar militar NATO en los 1970s.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Muestreo de Nyquist**: frecuencia de muestreo mínima
- **Cuantificación**: conversión de valores continuos a discretos
- **Predicción lineal**: estimar valor futuro basado en historia
- **Correlación temporal**: las muestras adyacentes de señales reales están correlacionadas

#### Desarrollo Paso a Paso

**Paso 1: PCM - Codificación del Valor Absoluto**

PCM codifica cada muestra independientemente:

1. **Muestreo**: $x[n] = x(nT_s)$ donde $f_s \geq 2f_m$
2. **Cuantificación**: $x_q[n] = Q(x[n])$ con $2^n$ niveles
3. **Codificación**: n bits por muestra
4. **Tasa de bits**: $R_{PCM} = n \cdot f_s$ bits/s

Características:
- **Sin memoria**: cada muestra es independiente
- **Error acotado**: $|e_q| \leq \Delta/2$
- **Robusto**: error en un bit afecta solo una muestra

**Paso 2: DM - Codificación de la Diferencia**

DM explota la correlación temporal transmitiendo solo el **cambio**:

1. **Predicción**: $\hat{x}[n] = \hat{x}[n-1] + \delta \cdot b[n-1]$
2. **Comparación**: Si $x[n] > \hat{x}[n]$ entonces $b[n] = +1$, sino $b[n] = -1$
3. **Transmisión**: 1 bit por muestra
4. **Tasa de bits**: $R_{DM} = f_s$ bits/s (¡n veces menor que PCM!)

El receptor reconstruye integrando los bits:
$$\hat{x}[n] = \hat{x}[0] + \delta \sum_{i=1}^{n} b[i]$$

**Paso 3: Los Problemas Fundamentales de DM**

**Slope Overload** (sobrecarga de pendiente):
- Ocurre cuando: $|\frac{dx}{dt}| > \delta \cdot f_s$
- La señal cambia más rápido de lo que DM puede seguir
- El codificador "persigue" la señal sin alcanzarla

**Granular Noise** (ruido granular):
- Ocurre en regiones planas de la señal
- El codificador oscila ±δ alrededor del valor real
- Genera patrón de ruido característico

**Paso 4: ADM - La Solución Adaptativa**

ADM varía el paso δ según la señal:

$$\delta[n] = \begin{cases}
\delta[n-1] \cdot K & \text{si } b[n] = b[n-1] \text{ (misma dirección)} \\
\delta[n-1] / K & \text{si } b[n] \neq b[n-1] \text{ (cambio dirección)}
\end{cases}$$

donde K > 1 (típicamente 1.5)

Esto permite:
- Pasos grandes para pendientes pronunciadas (evita slope overload)
- Pasos pequeños en regiones planas (reduce granular noise)

#### Derivación Matemática

**Análisis de SNR para DM:**

Para una señal senoidal $x(t) = A\sin(2\pi f_m t)$:

Máxima pendiente:
$$\left|\frac{dx}{dt}\right|_{max} = 2\pi f_m A$$

Condición para evitar slope overload:
$$\delta f_s \geq 2\pi f_m A$$

Por lo tanto:
$$\delta \geq \frac{2\pi f_m A}{f_s}$$

**SNR de DM (sin slope overload):**
$$SNR_{DM} = \frac{3f_s^3}{8\pi^2 f_m^2 f_M}$$

donde $f_M$ es la frecuencia máxima del espectro de la señal.

**Comparación con PCM:**

Para PCM con n bits:
$$SNR_{PCM} = 6.02n + 1.76 \text{ dB}$$

Para igualar la tasa de bits: $n \cdot f_{s,PCM} = f_{s,DM}$

Si $f_{s,DM} = 8f_{s,PCM}$ (oversampling típico), entonces n = 8 bits PCM equivalen a DM simple en tasa, pero PCM tiene SNR ≈ 50 dB vs DM ≈ 20-30 dB.

**Mejora con ADM:**

ADM puede mejorar SNR en 10-15 dB sobre DM simple:
$$SNR_{ADM} \approx SNR_{DM} + 10\log_{10}(G_{adapt})$$

donde $G_{adapt}$ es la ganancia adaptativa (típicamente 3-5).

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina describir la trayectoria de un avión a un controlador:

- **PCM**: "Estoy en coordenadas (x, y, z)" - información completa cada vez
- **DM**: "Sube, sube, baja, izquierda..." - solo direcciones relativas
- **ADM**: "Sube poco, sube MUCHO, baja poco..." - direcciones con magnitud variable

**Intuición física:**
DM es como un **sistema de control bang-bang** (termostato simple):
- Solo puede decir "más calor" o "menos calor"
- Oscila alrededor del punto deseado
- Simple pero con ondulación inherente

PCM es como un **termostato digital preciso**:
- Lee y transmite la temperatura exacta
- Control preciso pero más complejo
- No hay oscilación inherente

**Visualización:**
Piensa en DM como subir una escalera con pasos fijos (puedes quedarte corto o pasarte), mientras ADM es como tener una escalera telescópica que ajusta la altura del peldaño según necesites.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Digitalización de Señal de Voz

**Situación:** Digitalizar voz telefónica (300-3400 Hz) comparando PCM vs DM vs ADM.

**Datos:**
| Parámetro | PCM | DM | ADM |
|-----------|-----|----|----|
| Frecuencia de muestreo | 8 kHz | 64 kHz | 32 kHz |
| Bits por muestra | 8 | 1 | 1 |
| Tasa de bits | 64 kbps | 64 kbps | 32 kbps |

**Análisis comparativo:**

1. **PCM (8 bits, 8 kHz):**
   - SNR teórico: $6.02(8) + 1.76 = 49.92$ dB
   - Calidad: Excelente para voz
   - Complejidad: Moderada (ADC de 8 bits)

2. **DM (1 bit, 64 kHz):**
   - Oversampling: 64/8 = 8 veces
   - SNR típico: 25-30 dB
   - Problemas: Slope overload en consonantes explosivas (p, t, k)
   - Calidad: Marginal para voz

3. **ADM (1 bit, 32 kHz):**
   - Oversampling: 4 veces
   - SNR típico: 30-35 dB
   - Tasa reducida: 32 kbps (mitad que PCM)
   - Calidad: Aceptable para comunicaciones tácticas

**Resultado:**
$$\boxed{\text{PCM: mejor calidad, DM: más simple, ADM: mejor compromiso}}$$

---

#### Ejemplo 2: Sistema Bluetooth Clásico con CVSD

**Contexto:** Bluetooth v1.2 usa CVSD (Continuously Variable Slope Delta) para audio.

**Especificaciones CVSD en Bluetooth:**
- Tasa de muestreo: 64 kHz
- Tasa de bits: 64 kbps
- Adaptación: basada en patrón de últimos 3-4 bits
- Algoritmo silábico: constante de tiempo ~5 ms

**Procesamiento de palabra "Hello":**

1. **Sílaba "He" (transición suave):**
   - Bits típicos: 01010101... (alternando)
   - Paso δ se reduce gradualmente
   - Buena reconstrucción

2. **Transición "ll" (cambio rápido):**
   - Bits: 11111... (misma dirección)
   - Paso δ aumenta rápidamente
   - Evita slope overload

3. **Vocal "o" (estado estable):**
   - Bits: 01100110... (patrón mixto)
   - Paso δ se estabiliza
   - Mínimo ruido granular

**Ventaja sobre PCM:** Degradación gradual con errores de bit (robusto para wireless).

---

#### Ejemplo 3: Análisis de Casos Extremos

**Caso 1: Señal DC (constante)**
- **PCM**: Perfecto, transmite valor exacto
- **DM**: Oscila ±δ alrededor del valor (granular noise puro)
- **ADM**: δ se reduce al mínimo, minimiza oscilación

**Caso 2: Escalón unitario**
- **PCM**: Captura perfectamente en una muestra
- **DM**: Rampa de subida, tiempo = A/δ muestras
- **ADM**: Acelera subida aumentando δ progresivamente

**Caso 3: Señal de alta frecuencia (cerca de fs/2)**
- **PCM**: Funciona bien si fs > 2fm (Nyquist)
- **DM**: Falla completamente (slope overload constante)
- **ADM**: Intenta compensar pero calidad pobre

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Companding** (Carta 24): ADM es análogo a companding dinámico
- **TDM** (Carta 26): DM permite más canales en mismo ancho de banda
- **Predicción lineal**: Base teórica de DM y codecs modernos
- **Teoría de tasa-distorsión**: Trade-off fundamental bits vs calidad

#### Dependencias (lo que necesitas saber primero)
1. **Proceso PCM básico** → Para entender la alternativa
2. **Correlación temporal de señales** → Por qué DM puede funcionar
3. **Realimentación y sistemas de control** → Comportamiento del lazo DM

#### Aplicaciones Posteriores (dónde usarás esto)
1. **DPCM y ADPCM**: Extensiones más sofisticadas del concepto
2. **Codecs de voz modernos**: Usan predicción similar a DM
3. **Compresión de video**: Codificación diferencial entre frames
4. **Sigma-Delta ADCs**: DM en conversores modernos de alta resolución

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- **Trade-offs fundamentales**: Simplicidad vs calidad vs tasa de bits
- **Condiciones de falla**: Cuándo ocurre slope overload y granular noise
- **Aplicabilidad**: Cuándo elegir cada técnica
- **Cálculos básicos**: SNR aproximado, condición de no-overload

#### Tipos de problemas típicos
1. **Diseño de sistema**: Elegir fs y δ para DM dada una señal
   - Estrategia: Usar condición de máxima pendiente

2. **Comparación cuantitativa**: Calcular SNR para PCM vs DM con misma tasa
   - Estrategia: Igualar tasas de bits, comparar SNR

3. **Análisis de señales específicas**: Predecir comportamiento de DM/ADM
   - Estrategia: Identificar regiones problemáticas (pendientes altas, zonas planas)

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Pensar que DM siempre usa menos bits que PCM**
- Por qué ocurre: DM usa 1 bit/muestra pero requiere mayor fs
- Cómo evitarlo: Comparar tasa de bits total, no bits/muestra
- Ejemplo: DM a 64 kHz = PCM de 8 bits a 8 kHz

❌ **Error #2: Ignorar el oversampling necesario en DM**
- Por qué ocurre: No considerar requisito de seguir pendientes
- Cómo evitarlo: DM típicamente necesita fs = 4-8 veces mayor que PCM
- Factor clave: Oversampling es esencial para DM funcional

❌ **Error #3: Confundir ADM con ADPCM**
- Por qué ocurre: Nombres similares, ambos "adaptativos"
- Distinción: ADM adapta paso δ, ADPCM adapta predictor y cuantificador
- ADM es 1 bit/muestra, ADPCM típicamente 2-4 bits/muestra

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Condición no-overload DM: δ·fs ≥ max|dx/dt|
SNR PCM: 6.02n + 1.76 dB
Tasa PCM: R = n·fs
Tasa DM: R = fs (siempre)
Oversampling típico DM: 4-8x
```

#### Conceptos Fundamentales
- ✓ **PCM**: Calidad superior, complejidad moderada, estándar industrial
- ✓ **DM**: Ultra-simple, calidad limitada, requiere oversampling
- ✓ **ADM**: Compromiso inteligente, adapta a características locales
- ✓ **Trade-off clave**: Simplicidad ↔ Calidad ↔ Tasa de bits

#### Reglas Mnemotécnicas
- 🧠 **"PCM Preciso, DM Diferencial, ADM Adaptable"**: Características clave
- 🧠 **"SONG"**: Slope Overload, Noise Granular - problemas de DM
- 🧠 **"1 bit maravilla, 8x problema"**: DM usa 1 bit pero necesita 8x oversampling

#### Valores Típicos (para referencias rápidas)
| Parámetro | PCM | DM | ADM |
|-----------|-----|----|----|
| Bits/muestra | 8-16 | 1 | 1 |
| Oversampling | 1x | 4-8x | 2-4x |
| SNR típico voz | 50 dB | 25 dB | 35 dB |
| Complejidad | Media | Muy baja | Baja |
| Aplicación típica | Telefonía | Telemetría | Tactical radio |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**:
  - Jayant & Noll, "Digital Coding of Waveforms" - Biblia de DM/ADM
  - Haykin, "Communication Systems", Cap. 6.7-6.8
- **Papers históricos**:
  - Abate (1967) "Linear and Adaptive Delta Modulation"
- **Simulaciones**: GNU Radio tiene bloques CVSD para experimentar

#### Temas Relacionados para Explorar
1. **Sigma-Delta modulation**: DM de alta resolución para audio
2. **DPCM/ADPCM**: Evolución natural de DM
3. **Continuously Variable Slope Delta (CVSD)**: Estándar militar
4. **Linear Predictive Coding (LPC)**: Generalización de predicción

#### Preguntas para Reflexionar
- ¿Por qué DM no se usa en sistemas modernos de alta calidad?
- ¿Podría diseñarse un ADM "inteligente" con ML?
- ¿Cómo afecta el ruido del canal a DM vs PCM?
- ¿Existe un punto óptimo de oversampling para DM?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 30 minutos
**Prerequisitos críticos**: PCM, muestreo, cuantificación, sistemas realimentados
**Tags**: `#delta-modulation` `#pcm` `#adm` `#cvsd` `#codificacion-diferencial`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*