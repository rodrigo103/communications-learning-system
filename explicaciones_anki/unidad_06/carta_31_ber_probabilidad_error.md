# Carta 31: BER - Probabilidad de Error de Bit

> **Unidad 6**: Modulación Digital

---

## 🎯 Pregunta

¿Qué es la probabilidad de error de bit (BER) y de qué factores depende?

---

## 📝 Respuesta Breve (de la carta original)

**BER (Bit Error Rate)** es la probabilidad de que un bit transmitido se reciba erróneamente.

**Definición**:
$$BER = \frac{\text{bits erróneos}}{\text{total de bits transmitidos}}$$

**Depende de**:
1. **SNR o Eb/N0**: relación señal-ruido por bit
2. **Tipo de modulación**: diferentes curvas BER vs Eb/N0
3. **Tipo de detección**: coherente vs no coherente
4. **Características del canal**: desvanecimiento, interferencia
5. **Codificación**: códigos correctores mejoran BER

**Objetivo típico**: BER < 10⁻⁶ (telefonía), < 10⁻⁹ (datos)

**Curvas BER**: herramienta fundamental para comparar modulaciones

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La **Probabilidad de Error de Bit (BER)** es quizás la métrica más fundamental para evaluar la calidad de un sistema de comunicación digital. Representa la fracción de bits que se corrompen durante la transmisión, convirtiéndose en el criterio definitivo para determinar si un sistema cumple con los requisitos de confiabilidad. En el mundo real, donde cada bit puede representar desde un píxel en una videollamada hasta un dígito en una transacción bancaria, entender y controlar el BER es crucial para garantizar que la información llegue correctamente a su destino.

¿Por qué es tan importante el BER? Considera esto: en una transmisión de datos a 1 Gbps con un BER de 10⁻⁶, estadísticamente ocurren 1000 errores por segundo. Para una aplicación crítica como control de tráfico aéreo o equipos médicos, esto sería inaceptable. Por otro lado, para streaming de video donde hay redundancia y corrección de errores, podría ser tolerable. Esta distinción hace que el diseño de sistemas requiera un profundo entendimiento de cómo diferentes factores afectan el BER y cómo optimizarlo para cada aplicación.

La historia del estudio del BER se remonta a los trabajos de Claude Shannon en 1948, quien estableció los límites teóricos de la comunicación confiable en presencia de ruido. Sin embargo, fue el desarrollo de las comunicaciones digitales en los años 1960s-70s lo que convirtió al BER en la métrica estándar de la industria. Los primeros sistemas satelitales y de microondas terrestres establecieron el precedente de usar curvas BER vs Eb/N0 como la herramienta principal para el diseño y evaluación de enlaces de comunicación.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Ruido Gaussiano Blanco Aditivo (AWGN)** - modelo estándar de canal ruidoso
- **Función Q y función error complementaria (erfc)** - para calcular probabilidades
- **Decisión por umbral** - cómo el receptor decide entre símbolos
- **Distancia euclidiana** - separación entre puntos de constelación

#### Desarrollo Paso a Paso

**Paso 1: Modelo de Sistema y Fuente de Errores**

En un sistema de comunicación digital, los errores ocurren principalmente cuando el ruido desplaza la señal recibida más allá del umbral de decisión:

1. Transmisor envía símbolo s₁ o s₂
2. Canal añade ruido gaussiano n(t)
3. Receptor recibe r(t) = s(t) + n(t)
4. Decisor compara con umbral y decide ŝ
5. Error ocurre si ŝ ≠ s transmitido

La probabilidad de error depende de la separación entre símbolos y la potencia del ruido.

**Paso 2: Cálculo de Probabilidad de Error para BPSK**

Para BPSK (caso más simple), con símbolos antipodales ±A:

- Umbral de decisión: 0
- Error ocurre si ruido > A (para símbolo -A) o ruido < -A (para símbolo +A)
- Ruido es gaussiano con varianza σ² = N₀/2

La probabilidad de error de símbolo (que equivale a BER en BPSK) es:

$$P_e = Q\left(\frac{A}{\sigma}\right) = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$

donde Q(x) es la función Q gaussiana.

**Paso 3: Generalización a Otras Modulaciones**

Para modulaciones más complejas:
- **M-PSK**: Los símbolos están en círculo, error depende del ángulo
- **M-QAM**: Los símbolos en grilla, múltiples umbrales de decisión
- **M-FSK**: Ortogonalidad entre frecuencias afecta la probabilidad

Cada modulación tiene su propia expresión de BER, pero todas siguen el patrón general de depender de la distancia entre símbolos y el nivel de ruido.

#### Derivación Matemática

**BER para Modulaciones Comunes en Canal AWGN:**

**BPSK (Binary Phase Shift Keying):**
$$BER_{BPSK} = Q\left(\sqrt{\frac{2E_b}{N_0}}\right) = \frac{1}{2}\text{erfc}\left(\sqrt{\frac{E_b}{N_0}}\right)$$

**QPSK (Quadrature PSK):**
$$BER_{QPSK} \approx Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$
(mismo que BPSK debido a la codificación Gray)

**M-QAM Rectangular (aproximación para M grande):**
$$BER_{M-QAM} \approx \frac{2(\sqrt{M}-1)}{\sqrt{M}\log_2(M)} Q\left(\sqrt{\frac{3\log_2(M)E_b}{(M-1)N_0}}\right)$$

**FSK Ortogonal Coherente:**
$$BER_{FSK} = Q\left(\sqrt{\frac{E_b}{N_0}}\right)$$
(3 dB peor que BPSK)

**Relación General con SNR:**
$$BER = f(E_b/N_0, \text{modulación}, \text{detección})$$

donde:
$$\frac{E_b}{N_0} = \frac{SNR \cdot BW}{R_b}$$

**Significado físico:**
- $E_b$: Energía promedio por bit transmitido
- $N_0$: Densidad espectral de potencia del ruido
- $Q(x)$: Probabilidad de que variable gaussiana exceda x desviaciones estándar

### 🔬 Intuición y Analogías

**Analogía principal:**

Imagina que estás lanzando dardos a dos blancos separados, donde cada blanco representa un bit (0 o 1). El BER es como la probabilidad de que tu dardo caiga más cerca del blanco equivocado. El "viento" (ruido) desvía tu dardo de manera aleatoria. Cuanto más separados estén los blancos (mayor potencia de señal) y menos viento haya (menor ruido), menor será la probabilidad de error. Si los blancos están muy juntos o hay mucho viento, frecuentemente acertarás al blanco equivocado.

**Intuición física:**

En el receptor, la decisión es como establecer una frontera invisible entre regiones del espacio de señal. El ruido hace que el punto recibido "baile" alrededor de su posición ideal. Si este baile aleatorio cruza la frontera hacia el territorio de otro símbolo, ocurre un error. El BER mide qué fracción del tiempo el ruido es suficientemente fuerte para empujar la señal al lado equivocado de la frontera.

**Visualización:**

Imagina la constelación de señal como islas en un mar. Cada símbolo transmitido es como enviar un barco a una isla específica, pero las corrientes (ruido) pueden desviar el barco. El BER es la probabilidad de que el barco termine en la isla equivocada. Islas más grandes y separadas (mejor diseño de constelación) reducen esta probabilidad.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Enlace WiFi Doméstico con 64-QAM

**Situación:** Router WiFi transmitiendo a laptop en sala con 64-QAM.

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Potencia transmitida | 20 | dBm |
| Pérdidas de propagación | 60 | dB |
| Ruido térmico | -90 | dBm |
| Ancho de banda | 20 | MHz |
| Tasa de bits | 120 | Mbps |

**Solución paso a paso:**

1. **SNR en el receptor:**
   $$SNR = P_{tx} - L + (-N) = 20 - 60 - (-90) = 50 \text{ dB}$$

2. **Conversión a Eb/N0:**
   $$\frac{E_b}{N_0} = SNR - 10\log_{10}\left(\frac{R_b}{BW}\right)$$
   $$= 50 - 10\log_{10}(6) = 50 - 7.78 = 42.22 \text{ dB}$$

3. **BER para 64-QAM (usando aproximación):**
   Para Eb/N0 = 42.22 dB (≈ 16,700 lineal):
   $$BER \approx 4Q\left(\sqrt{\frac{3 \times 6 \times 16700}{63}}\right) \approx 10^{-12}$$

4. **Interpretación:**
   $$\boxed{BER \approx 10^{-12}}$$

**Interpretación:** Este BER extremadamente bajo indica transmisión prácticamente libre de errores. En condiciones reales, el BER sería mayor debido a interferencia, desvanecimiento y no-linealidades no consideradas.

---

#### Ejemplo 2: Enlace Satelital con QPSK

**Contexto:** Comunicación satelital para TV con requisito de BER < 10⁻⁷.

Un satélite geoestacionario transmite señal de TV usando QPSK. Las pérdidas de espacio libre a 36,000 km son aproximadamente 200 dB. Con una antena parabólica de 1.2m de diámetro (ganancia ~40 dB) y LNB con figura de ruido de 0.7 dB:

**Cálculo de Eb/N0 requerido:**
Para QPSK con BER = 10⁻⁷:
$$E_b/N_0 = 11.3 \text{ dB (de tablas)}$$

**Link budget necesario:**
- EIRP del satélite: 53 dBW
- Pérdidas de espacio: -200 dB
- Ganancia antena Rx: +40 dB
- Pérdidas adicionales: -2 dB
- Potencia recibida: -109 dBW

Con temperatura de ruido del sistema de 75K:
$$N_0 = kT = 1.38 \times 10^{-23} \times 75 = -198.8 \text{ dBW/Hz}$$

El margen de enlace confirma que se cumple el requisito de BER.

---

#### Ejemplo 3: Impacto de la Codificación en BER

**¿Cómo mejora un código corrector el BER?**

Consideremos un sistema con:
- BER sin codificar: 10⁻³
- Código Hamming (7,4): corrige 1 error en 7 bits

**Sin codificación:**
Probabilidad de recibir correctamente 7 bits:
$$P_{correcto} = (1-10^{-3})^7 \approx 0.993$$

**Con Hamming (7,4):**
El código puede corregir 1 error. Falla solo si hay 2 o más errores:
$$P_{error\_decodificado} \approx \binom{7}{2}(10^{-3})^2(0.999)^5 \approx 2.1 \times 10^{-5}$$

**Mejora efectiva:**
$$\frac{BER_{sin\_codigo}}{BER_{con\_codigo}} = \frac{10^{-3}}{2.1 \times 10^{-5}} \approx 48$$

La codificación mejora el BER en casi 2 órdenes de magnitud, al costo de reducir la tasa efectiva en 4/7 ≈ 0.57.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Eb/N0** (Carta 57): Métrica normalizada relacionada directamente con BER
- **Constelaciones** (Carta 28): Distancia entre puntos determina BER
- **Detección coherente** (Carta 32): Afecta significativamente el BER
- **Códigos correctores** (Carta 48): Reducen BER efectivo del sistema

#### Dependencias (lo que necesitas saber primero)
1. **Probabilidad y estadística** → Distribuciones gaussianas, función Q
2. **Teoría de decisión** → Regiones de decisión óptimas
3. **Ruido AWGN** → Modelo de canal básico

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Diseño de enlaces**: Determinar potencia necesaria para BER objetivo
2. **Selección de modulación**: Trade-off entre eficiencia espectral y BER
3. **Sistemas adaptativos**: Ajustar modulación según BER medido

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La relación exponencial entre Eb/N0 y BER (pequeños cambios en SNR → grandes cambios en BER)
- Por qué diferentes modulaciones tienen diferentes curvas BER
- Cómo usar curvas BER para diseñar sistemas
- El impacto de la detección coherente vs no coherente

#### Tipos de problemas típicos
1. **Cálculo de BER**: Dado Eb/N0 y modulación, encontrar BER
   - Estrategia: Usar fórmula apropiada o tabla/gráfica

2. **Diseño de enlace**: Encontrar potencia para lograr BER objetivo
   - Estrategia: Trabajar hacia atrás desde BER requerido

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir BER con SER (Symbol Error Rate)**
- Por qué ocurre: En M-arias, un error de símbolo puede ser 1 o más bits
- Cómo evitarlo: Con Gray coding: BER ≈ SER/log₂(M)
- Ejemplo: En 16-QAM, SER = 4×BER aproximadamente

❌ **Error #2: Usar fórmula de canal AWGN en canal con desvanecimiento**
- Por qué ocurre: Las fórmulas estándar asumen canal AWGN ideal
- Cómo evitarlo: Canales reales requieren modelos de Rayleigh, Rician, etc.

❌ **Error #3: Ignorar el piso de error (error floor)**
- Distinción importante: ISI y no-linealidades crean BER mínimo irreducible
- No mejora indefinidamente con más potencia

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
BER definición: BER = bits_erróneos / bits_totales
BPSK/QPSK: BER = Q(√(2Eb/N0))
Relación SNR: Eb/N0 = SNR × BW/Rb
Función Q: Q(x) ≈ (1/√(2π)) × exp(-x²/2) / x  (para x grande)
```

#### Conceptos Fundamentales
- ✓ **BER exponencial**: Decrece exponencialmente con Eb/N0
- ✓ **Waterfall region**: Zona de cambio rápido en curvas BER
- ✓ **Error floor**: BER mínimo por imperfecciones del sistema
- ✓ **Trade-off**: Mayor eficiencia espectral → peor BER para mismo Eb/N0

#### Reglas Mnemotécnicas
- 🧠 **"3 dB duplica"**: 3 dB más de Eb/N0 mejora BER en ~10x para región waterfall
- 🧠 **"10⁻⁶ para voz, 10⁻⁹ para datos"**: Requisitos típicos de BER

#### Valores Típicos (para referencias rápidas)

| Aplicación | BER Objetivo | Eb/N0 típico (QPSK) |
|------------|--------------|---------------------|
| Voz digital | 10⁻³ - 10⁻⁴ | 4-6 dB |
| Video streaming | 10⁻⁶ | 10.5 dB |
| Datos críticos | 10⁻⁹ - 10⁻¹² | 13-15 dB |
| Fibra óptica | 10⁻¹⁵ | >15 dB + FEC |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Proakis Cap. 5 "Optimum Receivers for AWGN Channels"
- **Material del curso**: Simulación Monte Carlo de BER en MATLAB
- **Herramientas**: Bertool de MATLAB para análisis de BER

#### Temas Relacionados para Explorar
1. Canales con desvanecimiento y su impacto en BER
2. Técnicas de diversidad para mejorar BER
3. Turbo códigos y LDPC para acercarse al límite de Shannon

#### Preguntas para Reflexionar
- ¿Por qué el BER no puede ser exactamente cero en un sistema real?
- ¿Cómo cambiaría el análisis de BER en un canal con memoria?
- ¿Qué relación existe entre el BER y la capacidad del canal de Shannon?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 40 minutos
**Prerequisitos críticos**: Probabilidad, ruido AWGN, modulaciones digitales
**Tags**: `#ber` `#probabilidad-error` `#calidad-enlace` `#metricas-digitales`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*