# Carta 28: Diagrama de Constelación en Modulación Digital

> **Unidad 6**: Modulación Digital

---

## 🎯 Pregunta

Explique qué es una constelación en modulación digital y su importancia.

---

## 📝 Respuesta Breve (de la carta original)

Una **constelación** es la representación gráfica de todos los símbolos posibles de una modulación digital en el plano complejo (I-Q).

**Componentes**:
- Eje I (In-phase): componente en fase
- Eje Q (Quadrature): componente en cuadratura
- Cada punto representa un símbolo único

**Importancia**:
1. **Visualización**: permite ver la estructura de la modulación
2. **Distancia entre símbolos**: determina robustez ante ruido
3. **Diseño**: optimización de esquemas de modulación
4. **Diagnóstico**: identificar problemas (ruido, offset, errores IQ)

**Ejemplos**:
- BPSK: 2 puntos en eje I
- QPSK: 4 puntos en esquinas de cuadrado
- QAM: red rectangular de puntos

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El diagrama de constelación es una herramienta fundamental en comunicaciones digitales que proporciona una representación visual intuitiva y matemáticamente precisa de las señales moduladas. Desarrollado en los años 1960s con el advenimiento de las comunicaciones digitales coherentes, se ha convertido en el lenguaje universal para describir, analizar y diagnosticar sistemas de modulación digital.

**¿Por qué es importante este concepto?** El diagrama de constelación es a las comunicaciones digitales lo que el osciloscopio es a la electrónica: una herramienta de visualización esencial. Permite a los ingenieros "ver" la calidad de la señal, diagnosticar problemas y optimizar el diseño del sistema. En sistemas modernos como 5G, los equipos de prueba muestran constelaciones en tiempo real para monitorear la salud del enlace.

**¿Dónde se aplica?** Desde el diseño de moduladores/demoduladores hasta el diagnóstico de campo, las constelaciones aparecen en:
- Analizadores de espectro vectoriales
- Software de simulación (MATLAB, GNU Radio)
- Equipos de prueba de telecomunicaciones
- Monitoreo de calidad en transmisores de TV digital
- Optimización de enlaces satelitales
- Debugging de problemas en WiFi/LTE

**Historia**: La representación I-Q surge naturalmente de la teoría de señales analíticas de Gabor (1946) y la detección coherente. La visualización como "constelación" de puntos se popularizó con el desarrollo de QAM en los 1960s para módems telefónicos de alta velocidad.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Números complejos y plano complejo
- Señales en cuadratura (I/Q)
- Modulación y demodulación coherente
- Espacio de señales y bases ortogonales
- Concepto de símbolo vs bit

#### Desarrollo Paso a Paso

**Paso 1: Representación de señal modulada en banda pasante**

Cualquier señal modulada digitalmente puede expresarse como:
$$s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$

donde:
- $I(t)$ = componente en fase (In-phase)
- $Q(t)$ = componente en cuadratura (Quadrature)
- $f_c$ = frecuencia de la portadora

**Paso 2: Representación compleja equivalente en banda base**

La señal puede representarse como número complejo:
$$\tilde{s}(t) = I(t) + jQ(t) = A(t)e^{j\phi(t)}$$

donde:
- $A(t) = \sqrt{I^2(t) + Q^2(t)}$ = amplitud
- $\phi(t) = \arctan(Q(t)/I(t))$ = fase

**Paso 3: Símbolos digitales como puntos**

Para modulación digital, $I(t)$ y $Q(t)$ toman valores discretos durante cada período de símbolo:
- Cada combinación $(I_k, Q_k)$ define un símbolo $s_k$
- El conjunto de todos los símbolos posibles forma la constelación
- Número de puntos = M (para modulación M-aria)

#### Derivación Matemática de distancias y regiones de decisión

**Distancia euclidiana entre símbolos:**
$$d_{ij} = |s_i - s_j| = \sqrt{(I_i - I_j)^2 + (Q_i - Q_j)^2}$$

**Distancia mínima de la constelación:**
$$d_{min} = \min_{i \neq j} d_{ij}$$

**Energía promedio por símbolo:**
$$E_s = \frac{1}{M}\sum_{k=1}^{M} |s_k|^2 = \frac{1}{M}\sum_{k=1}^{M} (I_k^2 + Q_k^2)$$

**Relación con probabilidad de error (para AWGN):**
$$P_e \approx Q\left(\frac{d_{min}}{2\sigma_n}\right)$$

donde $\sigma_n^2 = N_0/2$ es la varianza del ruido por dimensión.

**Regiones de decisión (Voronoi):**
Para detección óptima (ML), la región de decisión para símbolo $s_i$:
$$R_i = \{r : |r - s_i| < |r - s_j|, \forall j \neq i\}$$

### 🔬 Intuición y Analogías

**Analogía principal:**

Imagina un campo de tiro con blancos. Cada blanco representa un símbolo posible:
- La posición del blanco = punto ideal en la constelación
- Los disparos = símbolos recibidos con ruido
- La dispersión de los impactos = efecto del ruido
- Blancos muy juntos = más errores cuando hay viento (ruido)
- Blancos separados = menos confusión pero necesitas un campo más grande (más potencia)

**Intuición física:**

El diagrama I-Q es como mirar la señal RF "desde arriba" mientras gira a la frecuencia de la portadora:
- Sin modulación: punto fijo (portadora pura)
- Con modulación: el punto salta entre posiciones definidas
- El ruido hace que el punto "tiemble" alrededor de su posición ideal

**Visualización dinámica:**

En un osciloscopio vectorial:
- Puntos nítidos = buena SNR
- Nubes difusas = mucho ruido
- Puntos desplazados = errores de frecuencia/fase
- Elipses = desbalance I/Q

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Diseño de constelación QPSK

**Situación:** Diseñar una constelación QPSK con energía promedio unitaria

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Número de símbolos (M) | 4 | - |
| Energía promedio | 1 | - |
| Bits por símbolo | 2 | bits |

**Solución paso a paso:**

1. **Distribución simétrica de 4 puntos:**
   Para máxima separación con energía fija, usar esquinas de cuadrado

2. **Cálculo de coordenadas:**
   Si los puntos están en $(\pm a, \pm a)$:
   $$E_s = \frac{1}{4}[4 \cdot (a^2 + a^2)] = 2a^2 = 1$$
   $$a = \frac{1}{\sqrt{2}} \approx 0.707$$

3. **Constelación resultante:**
   - Símbolo 00: $(+0.707, +0.707)$ → "11"
   - Símbolo 01: $(-0.707, +0.707)$ → "01"
   - Símbolo 10: $(+0.707, -0.707)$ → "10"
   - Símbolo 11: $(-0.707, -0.707)$ → "00"

   (Mapeo Gray para minimizar BER)

4. **Distancia mínima:**
   $$d_{min} = 2a = \sqrt{2} \approx 1.414$$

**Interpretación:** La constelación QPSK óptima forma un cuadrado con mapeo Gray

---

#### Ejemplo 2: Análisis de constelación 16-QAM en WiFi 802.11

**Contexto:** WiFi 802.11n/ac usa 16-QAM cuando las condiciones del canal son buenas

Constelación 16-QAM estándar:
- 16 puntos en grilla 4×4
- Coordenadas: $\{-3, -1, +1, +3\} \times \{-3, -1, +1, +3\}$ (normalizado)
- Energía promedio: $E_s = 10$ (con normalización mostrada)
- Distancia mínima: $d_{min} = 2$

**Análisis de robustez:**
Para BER = $10^{-6}$:
- QPSK requiere: $E_b/N_0 \approx 10.5$ dB
- 16-QAM requiere: $E_b/N_0 \approx 14.5$ dB
- Penalidad: 4 dB por duplicar eficiencia espectral

**Decisión adaptativa:**
- SNR > 20 dB: usar 16-QAM (4 bits/símbolo)
- SNR 15-20 dB: usar QPSK (2 bits/símbolo)
- SNR < 15 dB: usar BPSK (1 bit/símbolo)

---

#### Ejemplo 3: Diagnóstico de problemas mediante constelación

**Problema observado:** Constelación 8-PSK distorsionada en transmisor

**Síntomas y diagnósticos:**

1. **Puntos en espiral en lugar de círculo:**
   - Causa: Error de frecuencia entre Tx y Rx
   - Solución: Ajustar PLL o referencia de frecuencia

2. **Puntos formando elipse:**
   - Causa: Desbalance de ganancia I/Q
   - Medición: Relación eje mayor/menor = desbalance
   - Solución: Calibración de ganancias I/Q

3. **Compresión en cuadrantes externos:**
   - Causa: Saturación del amplificador
   - Verificación: Reducir potencia de entrada
   - Solución: Operar en región lineal o usar predistorsión

4. **Offset del centro:**
   - Causa: DC offset en modulador I/Q
   - Medición: Distancia del centroide al origen
   - Solución: Compensación de DC

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **ASK/FSK/PSK** (Carta 27): Casos especiales de constelaciones
- **QAM** (Carta 29): Constelaciones rectangulares densas
- **BER** (Carta 31): Relacionado con distancia mínima
- **Detección coherente** (Carta 32): Necesaria para demodular usando constelación
- **Velocidad de señalización** (Carta 30): Puntos de constelación = símbolos

#### Dependencias (lo que necesitas saber primero)
1. Representación fasorial de señales → Base matemática
2. Teoría de detección → Regiones de decisión óptimas
3. Procesos aleatorios → Efecto del ruido en constelación

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Codificación TCM**: Diseño conjunto de código y constelación
2. **MIMO**: Múltiples constelaciones simultáneas
3. **Modulación adaptativa**: Selección dinámica de constelación según canal
4. **Predistorsión digital**: Compensación usando constelación inversa

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- Relación entre distancia y probabilidad de error
- Cómo el ruido afecta la constelación (nubes gaussianas)
- Trade-off entre densidad de puntos y robustez
- Cálculo de energía promedio y distancia mínima
- Mapeo Gray y su importancia

#### Tipos de problemas típicos
1. **Diseño**: Dada M y energía, encontrar coordenadas óptimas
2. **Análisis**: Calcular $d_{min}$ y $P_e$ para constelación dada
3. **Comparación**: Evaluar trade-offs entre diferentes constelaciones
4. **Diagnóstico**: Identificar problemas desde forma de constelación

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir constelación de potencia con amplitud**
- Por qué ocurre: Los ejes I/Q representan amplitud, no potencia
- Cómo evitarlo: Potencia = $I^2 + Q^2$, no $I + Q$
- Ejemplo: Punto en (1,1) tiene potencia 2, no 1

❌ **Error #2: Ignorar el mapeo de bits a símbolos**
- Por qué ocurre: Enfocarse solo en geometría
- Cómo evitarlo: Mapeo Gray minimiza BER
- Impacto: Mal mapeo puede duplicar BER

❌ **Error #3: Asumir que más puntos siempre es mejor**
- Por qué ocurre: Mayor eficiencia espectral es atractiva
- Cómo evitarlo: Considerar SNR disponible
- Realidad: Constelación densa requiere mayor SNR

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Distancia euclidiana: d = √[(I₁-I₂)² + (Q₁-Q₂)²]
Energía promedio: Es = (1/M)Σ(Ii² + Qi²)
Bits por símbolo: log₂(M)
Pe aproximada: Q(dmin/2σn)
```

#### Conceptos Fundamentales
- ✓ **Distancia mínima determina robustez**: Mayor dmin → menor Pe
- ✓ **Simetría maximiza eficiencia**: Constelaciones regulares son óptimas
- ✓ **Mapeo Gray es crítico**: Minimiza errores de bits
- ✓ **Trade-off fundamental**: Densidad vs robustez

#### Reglas Mnemotécnicas
- 🧠 **"I Quit"**: I=In-phase (horizontal), Q=Quadrature (vertical)
- 🧠 **"Distance Decides"**: Distancia mínima determina desempeño
- 🧠 **"Gray Saves the Day"**: Mapeo Gray para símbolos adyacentes

#### Valores Típicos (para referencias rápidas)

| Modulación | M | Forma | dmin (norm) | Eb/N0 @ 10^-6 |
|------------|---|-------|-------------|---------------|
| BPSK | 2 | Línea | 2 | 10.5 dB |
| QPSK | 4 | Cuadrado | √2 | 10.5 dB |
| 8-PSK | 8 | Octágono | 0.765 | 14 dB |
| 16-QAM | 16 | Grilla 4×4 | 0.632 | 14.5 dB |
| 64-QAM | 64 | Grilla 8×8 | 0.308 | 18.5 dB |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**: "Digital Communications" - Proakis & Salehi, Cap. 4
- **Software**: GNU Radio Companion - bloques de constelación
- **Herramientas online**: "Constellation Simulator" - dspillustrations.com
- **Videos**: "I/Q Data Explained" - Keysight Technologies

#### Temas Relacionados para Explorar
1. Constelaciones no uniformes (APSK)
2. Constelaciones multidimensionales
3. Shaping de constelación para canales no lineales
4. Constelaciones probabilísticas (probabilistic shaping)

#### Preguntas para Reflexionar
- ¿Por qué las constelaciones circulares (PSK) son mejores para canales no lineales?
- ¿Cómo diseñarías una constelación óptima para un canal con ruido no gaussiano?
- ¿Qué ventajas tendría una constelación en 3D o más dimensiones?
- ¿Cómo afecta el desvanecimiento selectivo a diferentes puntos de la constelación?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 30 minutos
**Prerequisitos críticos**: Números complejos, señales I/Q, teoría de detección
**Tags**: `#constelacion` `#IQ` `#modulacion-digital` `#visualizacion` `#diagnostico`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*