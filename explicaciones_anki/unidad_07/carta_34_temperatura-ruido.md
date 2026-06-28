# Carta 34: Temperatura de Ruido - Caracterización Térmica del Ruido

> **Unidad 7**: Ruido

---

## 🎯 Pregunta

Explique el concepto de temperatura de ruido de un dispositivo.

---

## 📝 Respuesta Breve (de la carta original)

La **temperatura de ruido** $T_e$ es una forma de caracterizar el ruido que un dispositivo agrega a la señal.

**Definición**: temperatura equivalente de una resistencia que produciría la misma potencia de ruido que el dispositivo.

**Relación con potencia de ruido**:
$$N = kT_e B$$
donde:
- k = constante de Boltzmann (1.38×10⁻²³ J/K)
- B = ancho de banda (Hz)

**Relación con figura de ruido**:
$$T_e = T_0(F - 1)$$
donde $T_0$ = 290 K (temperatura de referencia)

**Ventaja**: útil para sistemas en cascada, componentes criogénicos, antenas

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La **temperatura de ruido** es un concepto brillante que unifica la termodinámica con la teoría de comunicaciones. Permite caracterizar cualquier fuente de ruido, independientemente de su origen físico, como si fuera ruido térmico a una temperatura específica. Esta abstracción simplifica enormemente el análisis de sistemas complejos.

**¿Por qué es importante este concepto?** En sistemas de comunicaciones modernos, especialmente en aplicaciones de alta sensibilidad como radioastronomía, comunicaciones satelitales y radar, la temperatura de ruido determina directamente los límites de detección. Un receptor con menor temperatura de ruido puede detectar señales más débiles, extendiendo el alcance o reduciendo la potencia de transmisión necesaria.

**¿Dónde se aplica?** La temperatura de ruido es crítica en:
- **Estaciones terrenas satelitales**: LNAs con Te < 50 K
- **Radioastronomía**: receptores criogénicos con Te < 10 K
- **Sistemas de radar**: determinando alcance máximo
- **Enlaces de microondas**: calculando márgenes de desvanecimiento
- **Receptores GPS**: sensibilidad de -160 dBW requiere Te muy baja

**Historia**: El concepto emergió del trabajo de John B. Johnson y Harry Nyquist en Bell Labs (1928), quienes descubrieron y explicaron el ruido térmico. Harald Friis extendió el concepto en 1944, desarrollando la temperatura equivalente de ruido como herramienta de diseño para sistemas en cascada.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Ruido térmico (Johnson-Nyquist)**: fluctuaciones por agitación térmica
- **Figura de ruido**: degradación de SNR en un dispositivo
- **Teoría cinética**: relación temperatura-energía
- **Sistemas en cascada**: combinación de múltiples etapas

#### Desarrollo Paso a Paso

**Paso 1: Origen del Ruido Térmico**

Una resistencia a temperatura T genera ruido debido al movimiento térmico aleatorio de electrones:

$$v_n^2 = 4kTRB$$

donde:
- $v_n^2$ = voltaje cuadrático medio de ruido
- R = resistencia (Ω)
- B = ancho de banda (Hz)

La potencia disponible (adaptación de impedancias):
$$N_{térmico} = kTB$$

**Relación entre ambas fórmulas:**

Ambas ecuaciones describen el mismo fenómeno físico (ruido térmico), pero desde perspectivas diferentes:

- **$v_n^2 = 4kTRB$**: Describe la **tensión de ruido** (voltaje RMS al cuadrado) en los terminales de una resistencia R
- **$N_{térmico} = kTB$**: Describe la **potencia disponible** que se puede transferir a una carga adaptada

**Derivación de la conexión:**

Partimos de un circuito equivalente: resistencia R (fuente de ruido) conectada a una carga $R_L$.

1. **Modelo de Thévenin**: La resistencia R genera una fuente de voltaje de ruido $v_n$ con impedancia interna R.

2. **Potencia transferida a la carga**:
   $$P = \frac{v_n^2 \cdot R_L}{(R + R_L)^2}$$

3. **Condición de adaptación** (máxima transferencia de potencia):
   Para $R_L = R$ (carga adaptada):
   $$P_{max} = \frac{v_n^2 \cdot R}{(R + R)^2} = \frac{v_n^2}{4R}$$

4. **Sustituyendo** $v_n^2 = 4kTRB$:
   $$P_{max} = \frac{4kTRB}{4R} = kTB$$

**Interpretación física:**

- El factor **4** en $v_n^2 = 4kTRB$ refleja que el voltaje se mide en **circuito abierto** (toda la resistencia)
- Al conectar una carga adaptada, solo **1/4** de la potencia potencial se transfiere efectivamente
- El resultado $N_{térmico} = kTB$ es **independiente de R**: la potencia disponible depende solo de T y B, no de la resistencia específica
- Esta independencia de R es fundamental: permite definir la potencia de ruido térmico de forma universal

**Caso práctico - Cálculo numérico:**

Para T = 290 K, B = 1 MHz, R = 50 Ω:

| Magnitud | Valor | Unidades |
|----------|-------|----------|
| $v_n^2$ | $4 \times 1.38 \times 10^{-23} \times 290 \times 50 \times 10^6$ | V² |
| $v_n$ | 0.896 | μV |
| $P_{disponible}$ | $1.38 \times 10^{-23} \times 290 \times 10^6$ | W |
| $N_{térmico}$ | 4.0 × 10⁻¹⁵ | W |
| $N_{térmico}$ | -114 | dBm |

**Verificación**: $P = v_n^2/(4R) = (0.896 \times 10^{-6})^2/(4 \times 50) = 4.0 \times 10^{-15}$ W ✓

**Paso 2: Concepto de Temperatura Equivalente**

Cualquier dispositivo que agregue ruido puede caracterizarse por una temperatura equivalente $T_e$ tal que:
- Un resistor a temperatura $T_e$ produciría el mismo ruido
- El ruido total a la salida es como si la entrada estuviera a temperatura $T_0 + T_e$

**Paso 3: Temperatura de Sistema**

Para un sistema completo:
$$T_{sys} = T_{antena} + T_{receptor}$$

donde:
- $T_{antena}$ incluye ruido cósmico, atmosférico y de lóbulos laterales
- $T_{receptor}$ es la temperatura equivalente del receptor completo

#### Derivación Matemática

**Partiendo de la definición de figura de ruido:**

La figura de ruido F relaciona SNR de entrada y salida:
$$F = \frac{(S/N)_{in}}{(S/N)_{out}}$$

**Para un amplificador con ganancia G:**

Señal de salida: $S_{out} = GS_{in}$

Ruido de salida: $N_{out} = GN_{in} + N_{agregado}$

donde $N_{agregado}$ es el ruido propio del dispositivo.

**Expresando el ruido agregado como temperatura:**

$$N_{agregado} = GkT_eB$$

**Sustituyendo en la definición de F:**

$$F = \frac{S_{in}/N_{in}}{GS_{in}/(GN_{in} + GkT_eB)}$$

$$F = \frac{GN_{in} + GkT_eB}{GN_{in}} = 1 + \frac{T_e}{T_0}$$

**Resultado final:**
$$\boxed{T_e = T_0(F - 1)}$$

**Significado de cada término:**
- $T_e$: temperatura de ruido del dispositivo
- $T_0$: temperatura de referencia (290 K estándar)
- $F$: figura de ruido (adimensional, F ≥ 1)

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina la temperatura de ruido como el "calor electrónico" de un dispositivo. Así como un objeto caliente irradia energía térmica, un dispositivo con temperatura de ruido irradia "energía de ruido". Mientras más "caliente" electrónicamente, más ruido genera.

**Intuición física:**
Cuando enfriamos un amplificador criogénicamente:
1. Los electrones se mueven menos → menos ruido térmico interno
2. Semiconductores más eficientes → menos ruido shot
3. Resistencias parásitas contribuyen menos → menor Te total

**Visualización:**
- Dispositivo ideal (sin ruido): Te = 0 K (cero absoluto electrónico)
- Dispositivo a temperatura ambiente: Te ≈ T ambiente
- Dispositivo ruidoso: Te >> T ambiente (electrónicamente "caliente")

### 💡 Ejemplos Prácticos

#### Ejemplo 1: LNA para Estación Terrena Satelital

**Situación:** Diseño de receptor para comunicación con satélite geoestacionario en banda Ku (12 GHz).

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Figura de ruido LNA | 0.8 | dB |
| Temperatura antena | 50 | K |
| Ancho de banda | 36 | MHz |
| Ganancia LNA | 60 | dB |

**Solución paso a paso:**

1. **Convertir figura de ruido a lineal:**
   $$F = 10^{0.8/10} = 1.20$$

2. **Calcular temperatura de ruido del LNA:**
   $$T_e = T_0(F - 1) = 290 \times (1.20 - 1)$$
   $$T_e = 58 \text{ K}$$

3. **Temperatura total del sistema:**
   $$T_{sys} = T_{antena} + T_{LNA} = 50 + 58 = 108 \text{ K}$$

4. **Potencia de ruido del sistema:**
   $$N = kT_{sys}B = 1.38 \times 10^{-23} \times 108 \times 36 \times 10^6$$
   $$\boxed{N = 5.36 \times 10^{-14} \text{ W} = -102.7 \text{ dBm}}$$

**Interpretación:** La temperatura de ruido del LNA (58 K) es comparable a la temperatura de la antena (50 K), por lo que ambas contribuyen significativamente al ruido total.

---

#### Ejemplo 2: Receptor Criogénico para Radioastronomía

**Contexto:** Radiotelescopio operando a 1.4 GHz (línea de hidrógeno) con LNA enfriado a 20 K físicos.

**Parámetros del sistema:**
- Temperatura física LNA: 20 K
- Figura de ruido a 20 K: 0.1 dB (F = 1.023)
- Temperatura antena (mirando al espacio): 3 K (radiación cósmica de fondo)
- Segunda etapa (300 K): F₂ = 2 dB, G₁ = 30 dB

**Análisis:**

1. **Te del LNA criogénico:**
   $$T_{e1} = 290 \times (1.023 - 1) = 6.7 \text{ K}$$

2. **Te de la segunda etapa referida a la entrada:**
   $$T_{e2,ref} = \frac{T_{e2}}{G_1} = \frac{290 \times (10^{0.2} - 1)}{1000} = 0.17 \text{ K}$$

3. **Temperatura total del receptor:**
   $$T_{rx} = T_{e1} + T_{e2,ref} = 6.7 + 0.17 = 6.87 \text{ K}$$

4. **Temperatura del sistema completo:**
   $$T_{sys} = T_{ant} + T_{rx} = 3 + 6.87 = 9.87 \text{ K}$$

**Comparación con sistema no criogénico:**
- Sin enfriamiento (Te ≈ 100 K): Tsys ≈ 103 K
- Con enfriamiento: Tsys ≈ 10 K
- **Mejora: 10 dB en sensibilidad**

---

#### Ejemplo 3: Análisis de Cascada - Receptor GPS

**¿Qué pasa cuando conectamos múltiples etapas?**

**Sistema GPS típico:**
```
Antena → Cable → LNA → Mezclador → IF Amp
Ta=100K   L=2dB   F=2dB  F=8dB     F=6dB
         (0.63)   G=20dB  G=0dB     G=30dB
```

**Cálculo de temperatura equivalente total:**

1. **Cable (atenuador pasivo a 290K):**
   $$T_{cable} = 290 \times (1/0.63 - 1) = 170 \text{ K}$$

2. **LNA:**
   $$T_{LNA} = 290 \times (10^{0.2} - 1) = 169 \text{ K}$$

3. **Aplicando Friis para temperaturas:**
   $$T_{total} = T_a + T_{cable} + \frac{T_{LNA}}{0.63} + \frac{T_{mix}}{0.63 \times 100} + ...$$

4. **Resultado:**
   $$T_{total} = 100 + 170 + 268 + 22 + 0.7 ≈ 561 \text{ K}$$

**Lección clave:** El cable antes del LNA domina la temperatura del sistema. Por eso los LNAs se montan directamente en la antena.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Ruido blanco** (Carta 33): Te caracteriza la densidad espectral N₀
- **Figura de ruido** (Carta 35): Relación directa Te = T₀(F-1)
- **Fórmula de Friis** (Carta 36): Se puede expresar en términos de temperaturas
- **Link budget**: Tsys determina la sensibilidad del receptor
- **Teorema de Shannon**: C = B·log₂(1 + S/(kTsysB))

#### Dependencias (lo que necesitas saber primero)
1. **Ruido térmico** → Origen físico del concepto
2. **Ganancia y atenuación** → Para análisis de cascada
3. **Decibeles** → Conversiones frecuentes dB ↔ lineal

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Diseño de receptores de alta sensibilidad**: Minimizar Tsys
2. **Cálculo de alcance en radar**: Ecuación de radar usa Te
3. **Enlaces satelitales**: G/T (ganancia sobre temperatura) es métrica clave
4. **Radioastronomía**: Detectar señales cósmicas débiles

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La equivalencia entre figura de ruido y temperatura de ruido
- Por qué la temperatura de ruido es aditiva en cascada (con ponderación por ganancia)
- Cómo la temperatura física afecta la temperatura de ruido
- La importancia de minimizar Te en las primeras etapas

#### Tipos de problemas típicos
1. **Conversión F ↔ Te**: Dado uno, calcular el otro
   - Estrategia: Usar Te = T₀(F - 1) con T₀ = 290 K

2. **Sistema en cascada**: Calcular Tsys de múltiples etapas
   - Estrategia: Aplicar fórmula de Friis en términos de temperatura

3. **Comparación criogénico vs. ambiente**: Evaluar mejora en sensibilidad
   - Estrategia: Comparar Tsys y calcular mejora en dB

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir temperatura física con temperatura de ruido**
- Por qué ocurre: Ambas se miden en Kelvin
- Cómo evitarlo: Recordar que Te es una medida de ruido, no de calor
- Ejemplo: Un amplificador a 300 K físicos puede tener Te = 100 K

❌ **Error #2: Sumar temperaturas sin considerar ganancia en cascada**
- Por qué ocurre: Olvidar que etapas posteriores contribuyen menos
- Cómo evitarlo: Siempre dividir por ganancia acumulada previa

❌ **Error #3: Usar T₀ incorrecto en conversiones**
- Distinción importante:
  - Estándar IEEE: T₀ = 290 K
  - Algunas referencias usan 300 K
  - Criogenia a veces usa temperatura física real

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Te = T₀(F - 1)                [Conversión F → Te, T₀=290K]
F = 1 + Te/T₀                  [Conversión Te → F]
Tsys = Tant + Trx              [Temperatura total del sistema]
N = k·Tsys·B                   [Potencia de ruido total]
```

#### Conceptos Fundamentales
- ✓ **Te caracteriza todo el ruido**: No solo térmico, también shot, flicker, etc.
- ✓ **Aditiva con ponderación**: En cascada, dividir por ganancia previa
- ✓ **Independiente del ancho de banda**: Te es propiedad del dispositivo
- ✓ **Límite físico**: Te ≥ 0 K (no puede ser negativa)

#### Reglas Mnemotécnicas
- 🧠 **"TeF-1"**: Te = T₀(F-1), donde T₀ = 290 K
- 🧠 **"Primero importa más"**: Primera etapa domina Tsys

#### Valores Típicos (para referencias rápidas)

| Dispositivo | Te Típica | Figura de Ruido | Aplicación |
|-------------|-----------|-----------------|------------|
| LNA criogénico | 5-20 K | 0.1-0.3 dB | Radioastronomía |
| LNA HEMT @ 300K | 35-70 K | 0.5-0.9 dB | Satélites |
| LNA estándar | 170-300 K | 2-3 dB | Comunicaciones |
| Mezclador | 1500-3000 K | 8-12 dB | Conversión RF-IF |
| Cable coaxial | (L-1)×290 K | L (pérdida) | Conexiones |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - Pozar, "Microwave Engineering", Cap. 10
  - Kraus, "Radio Astronomy", Cap. 7 (aplicaciones criogénicas)
- **Application notes**:
  - Agilent: "Noise Figure Measurement Accuracy"
  - Mini-Circuits: "Understanding Noise Figure"
- **Software**:
  - AppCAD: Calculadora de cascada de ruido
  - ADS/AWR: Simulación de ruido en sistemas

#### Temas Relacionados para Explorar
1. **Medición de temperatura de ruido**: Método Y-factor
2. **Temperatura de antena**: Contribuciones terrestres y cósmicas
3. **Amplificadores paramétricos**: Te < temperatura física
4. **Ruido cuántico**: Límite fundamental Te ≥ hf/k

#### Preguntas para Reflexionar
- ¿Por qué no podemos alcanzar Te = 0 K incluso a temperatura física cero?
- ¿Cómo afecta la frecuencia de operación a la temperatura de ruido mínima alcanzable?
- ¿Por qué los radioastrónomos enfrían sus receptores pero no las antenas?
- ¿Existe algún dispositivo con "temperatura de ruido negativa"? (Hint: masers)

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 35 minutos
**Prerequisitos críticos**: Ruido térmico, figura de ruido, sistemas en cascada
**Tags**: `#temperatura-ruido` `#Te` `#criogenia` `#receptores` `#sensibilidad`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*