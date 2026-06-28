# Carta 30: Velocidad de Señalización vs Tasa de Bits

> **Unidad 6**: Modulación Digital

---

## 🎯 Pregunta

Defina velocidad de señalización (baud rate) y tasa de bits (bit rate). ¿Son siempre iguales?

---

## 📝 Respuesta Breve (de la carta original)

**Velocidad de señalización (Rs)**:
- Símbolos transmitidos por segundo
- Unidad: baudios (símbolos/s)
- Relacionada con ancho de banda

**Tasa de bits (Rb)**:
- Bits transmitidos por segundo
- Unidad: bits/s (bps)

**Relación**:
$$R_b = R_s \cdot \log_2(M)$$
donde M = número de símbolos posibles

**NO son iguales** excepto en modulaciones binarias (M=2).

**Ejemplos**:
- BPSK: Rs = Rb (1 bit/símbolo)
- QPSK: Rb = 2Rs (2 bits/símbolo)
- 16-QAM: Rb = 4Rs (4 bits/símbolo)

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La distinción entre velocidad de señalización (baud rate) y tasa de bits (bit rate) es fundamental para entender cómo los sistemas de comunicación digital optimizan el uso del espectro electromagnético. Esta diferencia, aunque sutil, representa uno de los conceptos más importantes en el diseño de sistemas de comunicaciones modernos, permitiendo que tecnologías como 5G, WiFi 6 y fibra óptica alcancen velocidades de datos que serían imposibles si cada símbolo transmitiera solo un bit.

¿Por qué es importante esta distinción? En los primeros días de las comunicaciones digitales, cuando los módems telefónicos dominaban el panorama, era común escuchar términos como "modem de 9600 baudios" usado incorrectamente como sinónimo de "9600 bits por segundo". Esta confusión persistió porque en las modulaciones simples de la época, efectivamente coincidían. Sin embargo, a medida que la demanda de velocidad creció y el espectro disponible se volvió más escaso, los ingenieros desarrollaron técnicas para transmitir múltiples bits en cada símbolo, rompiendo esta equivalencia 1:1.

La historia de esta evolución es fascinante. En 1962, los laboratorios Bell desarrollaron el primer módem comercial (Bell 103) que operaba a 300 baudios y 300 bps usando FSK simple. Para 1990, los módems V.32 alcanzaban 9600 bps pero solo operaban a 2400 baudios, transmitiendo 4 bits por símbolo usando QAM. Esta revolución cuadruplicó la eficiencia espectral sin requerir más ancho de banda, demostrando el poder de separar conceptualmente símbolos de bits.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Símbolo vs Bit**: Un bit es la unidad mínima de información (0 o 1), mientras que un símbolo es un estado físico distinguible de la señal
- **Modulación M-aria**: Sistemas donde la señal puede tomar M estados diferentes
- **Teorema de Nyquist**: Relación entre velocidad de símbolo y ancho de banda mínimo
- **Constelaciones digitales**: Representación visual de los M estados posibles

#### Desarrollo Paso a Paso

**Paso 1: Definición Formal de Velocidad de Señalización**

La velocidad de señalización Rs (baud rate) es el número de cambios de estado de la señal por unidad de tiempo:

$$R_s = \frac{1}{T_s} \text{ baudios}$$

donde Ts es la duración de cada símbolo. Físicamente, representa cuán rápido cambia la señal en el canal. Cada cambio puede representar la transmisión de un nuevo símbolo del alfabeto de M símbolos posibles.

**Paso 2: Definición Formal de Tasa de Bits**

La tasa de bits Rb es la cantidad de información binaria transmitida por unidad de tiempo:

$$R_b = \frac{\text{número de bits transmitidos}}{\text{tiempo total}} \text{ bits/s}$$

Esta es la métrica que realmente importa al usuario final: cuánta información útil se está transmitiendo.

**Paso 3: Relación Fundamental**

La conexión entre ambas métricas surge del concepto de información por símbolo. Si tenemos M símbolos posibles (todos equiprobables), cada símbolo puede transportar:

$$k = \log_2(M) \text{ bits de información}$$

Por lo tanto, la relación fundamental es:

$$\boxed{R_b = R_s \cdot \log_2(M)}$$

#### Derivación Matemática

**Análisis desde la Teoría de la Información:**

Consideremos un sistema de comunicación digital con alfabeto de M símbolos {s₁, s₂, ..., sₘ}.

**Información por símbolo:**
Si los símbolos son equiprobables con probabilidad p = 1/M, la información de cada símbolo es:

$$I(s_i) = -\log_2(p) = -\log_2(1/M) = \log_2(M) \text{ bits}$$

**Tasa de información:**
Si transmitimos Rs símbolos por segundo, la tasa de información es:

$$R_b = R_s \cdot I(s_i) = R_s \cdot \log_2(M)$$

**Relación con el ancho de banda:**
Por el criterio de Nyquist para transmisión sin ISI:

$$B_{min} = \frac{R_s}{2} \text{ Hz (para pulsos sinc ideales)}$$

En la práctica, con factores de roll-off α:

$$B_{real} = \frac{R_s(1+\alpha)}{2} \text{ Hz}$$

**Eficiencia espectral resultante:**

$$\eta = \frac{R_b}{B} = \frac{R_s \cdot \log_2(M)}{R_s(1+\alpha)/2} = \frac{2\log_2(M)}{1+\alpha} \text{ bits/s/Hz}$$

**Significado físico de cada término:**
- $R_s$: Rapidez de cambios físicos en el canal
- $\log_2(M)$: Bits de información por cambio
- $B$: Ancho de banda ocupado en el espectro
- $\alpha$: Factor de exceso de banda para pulsos realizables

### 🔬 Intuición y Analogías

**Analogía principal:**

Imagina un semáforo que puede cambiar de estado cada 3 segundos (velocidad de señalización = 1/3 cambios por segundo). Si el semáforo tradicional tiene 3 colores (rojo, amarillo, verde), cada cambio transmite log₂(3) ≈ 1.58 bits de información. Pero si inventamos un "súper-semáforo" con 8 colores diferentes, ahora cada cambio transmite log₂(8) = 3 bits, triplicando la información transmitida sin cambiar más rápido. La velocidad de señalización (qué tan rápido cambia) permanece igual, pero la tasa de bits (cuánta información se transmite) se triplica.

**Intuición física:**

En el dominio eléctrico, Rs determina el ancho de banda necesario porque define qué tan rápido debe responder el canal a los cambios. Es como el ancho de una autopista: determina cuántos "vehículos" (símbolos) pueden pasar por segundo. Pero cada vehículo puede ser un auto (1 bit), un autobús (4 bits), o un camión (8 bits). La capacidad de carga total (tasa de bits) depende tanto del flujo de vehículos como de su capacidad individual.

**Visualización:**

Imagina un osciloscopio mostrando una señal digital. La velocidad de señalización determina qué tan rápido ves cambios en la pantalla. Para BPSK, verías la señal saltando entre dos niveles. Para 16-QAM, verías la señal tomando 16 combinaciones diferentes de amplitud y fase, pero los cambios ocurrirían a la misma velocidad. El ojo entrenado puede "leer" más información de cada estado en 16-QAM.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Modem V.34 Clásico

**Situación:** Un módem V.34 de los años 90 operando sobre línea telefónica.

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Velocidad de señalización | 3429 | baudios |
| Constelación | 512-QAM | - |
| Ancho de banda disponible | 3.4 | kHz |
| Tasa objetivo | 33.6 | kbps |

**Solución paso a paso:**

1. **Bits por símbolo con 512-QAM:**
   $$k = \log_2(512) = 9 \text{ bits/símbolo}$$

2. **Tasa de bits teórica:**
   $$R_b = 3429 \times 9 = 30,861 \text{ bps}$$

3. **Con codificación Trellis (transmite bits adicionales):**
   El V.34 usa codificación Trellis que permite aproximadamente:
   $$R_b = 3429 \times 9.8 \approx 33,600 \text{ bps}$$

4. **Verificación de ancho de banda:**
   $$B_{necesario} \approx R_s = 3.429 \text{ kHz}$$

   Apenas cabe en los 3.4 kHz disponibles de una línea telefónica.

**Interpretación:** Este ejemplo muestra cómo los módems telefónicos maximizaron la capacidad usando constelaciones enormes (512 puntos) mientras mantenían la velocidad de símbolo dentro del ancho de banda limitado del canal telefónico.

---

#### Ejemplo 2: Comparación Gigabit Ethernet

**Contexto:** Ethernet Gigabit usando diferentes técnicas de modulación.

**1000BASE-T (Cable de cobre Cat5e):**
- Usa 4 pares de cables simultáneamente
- Cada par: 125 Mega baudios
- Modulación: PAM-5 (5 niveles)
- Bits por símbolo: log₂(5) ≈ 2.32 bits
- Pero usa codificación 4D-PAM5 que transmite 2 bits/símbolo efectivos
- Tasa por par: 125 × 2 = 250 Mbps
- Tasa total: 4 × 250 = 1000 Mbps

**1000BASE-X (Fibra óptica):**
- Velocidad de señalización: 1250 Mega baudios
- Modulación: NRZ (binaria)
- Bits por símbolo: 1
- Usa codificación 8B/10B (overhead del 25%)
- Tasa efectiva: 1250 × 1 × 0.8 = 1000 Mbps

La comparación muestra cómo el cobre necesita modulación multinivel para alcanzar la misma tasa que la fibra con modulación binaria, debido a las limitaciones de ancho de banda del medio.

---

#### Ejemplo 3: Evolución de WiFi

**¿Cómo ha evolucionado la relación Rs/Rb en WiFi?**

| Estándar | Modulación Máx | Bits/Símbolo | Rs típica | Rb máxima | Rb/Rs |
|----------|----------------|--------------|-----------|-----------|-------|
| 802.11b | QPSK | 2 | 11 MS/s | 11 Mbps | 1.0 |
| 802.11g | 64-QAM | 6 | 18.5 MS/s | 54 Mbps | 2.9 |
| 802.11n | 64-QAM | 6 | 18.5 MS/s | 65 Mbps | 3.5 |
| 802.11ac | 256-QAM | 8 | 78 MS/s | 433 Mbps | 5.5 |
| 802.11ax | 1024-QAM | 10 | 78 MS/s | 600 Mbps | 7.7 |

Esta evolución muestra cómo WiFi ha aumentado dramáticamente la tasa de bits principalmente aumentando los bits por símbolo (orden de modulación), no solo la velocidad de señalización.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **QAM** (Carta 29): Ejemplo perfecto de cómo M grande separa Rs de Rb
- **BER** (Carta 31): Mayor M (más bits/símbolo) típicamente degrada BER
- **Eficiencia espectral** (Carta 41): Directamente relacionada con log₂(M)
- **Teorema de Nyquist** (Carta 5): Establece relación entre Rs y ancho de banda

#### Dependencias (lo que necesitas saber primero)
1. **Logaritmos en base 2** → Para calcular bits por símbolo
2. **Concepto de símbolo digital** → Estado distinguible de la señal
3. **Modulaciones M-arias** → Sistemas con M > 2 estados

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Diseño de sistemas**: Selección de M para cumplir requisitos de Rb con Rs limitada
2. **Análisis de capacidad**: Cálculo de throughput máximo de un canal
3. **OFDM**: Cada subportadora tiene su propia relación Rs/Rb

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La diferencia conceptual fundamental entre cambios físicos (baudios) e información (bits)
- Cómo calcular una métrica conociendo la otra y el esquema de modulación
- Por qué sistemas modernos prefieren aumentar M en lugar de Rs
- El impacto en el ancho de banda requerido de cada enfoque

#### Tipos de problemas típicos
1. **Conversión Rs ↔ Rb**: Dado uno, calcular el otro para modulación específica
   - Estrategia: Identificar M, calcular log₂(M), aplicar fórmula

2. **Diseño de sistema**: Alcanzar Rb objetivo con restricción de ancho de banda
   - Estrategia: BW limita Rs máxima, calcular M necesario

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Asumir que baudios = bits/s**
- Por qué ocurre: Terminología histórica confusa, especialmente en módems antiguos
- Cómo evitarlo: Siempre verificar el esquema de modulación
- Ejemplo: "Módem de 56k" no opera a 56,000 baudios

❌ **Error #2: Olvidar el overhead de codificación**
- Por qué ocurre: Las fórmulas dan tasa bruta, no neta
- Cómo evitarlo: Considerar FEC, codificación de línea, headers
- Ejemplo: Ethernet 8B/10B reduce tasa efectiva en 20%

❌ **Error #3: Confundir velocidad de chip con velocidad de símbolo**
- Distinción importante: En spread spectrum, chip rate >> symbol rate
- Ejemplo: GPS transmite 1.023 Mchips/s pero solo 50 símbolos/s

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Relación fundamental: Rb = Rs × log₂(M)
Eficiencia espectral: η = Rb/BW = log₂(M) (ideal)
Ancho de banda Nyquist: BW = Rs/2 (mínimo teórico)
Ancho de banda real: BW = Rs(1+α)/2
```

#### Conceptos Fundamentales
- ✓ **Bauds ≠ Bits/s**: Solo iguales cuando M=2 (modulación binaria)
- ✓ **Trade-off fundamental**: Aumentar M aumenta Rb sin aumentar Rs (ni BW)
- ✓ **Límite práctico**: Mayor M requiere mejor SNR para mantener BER aceptable
- ✓ **Velocidad de símbolo**: Determina ancho de banda necesario

#### Reglas Mnemotécnicas
- 🧠 **"Bits = Baudios × Binario-logaritmo"**: Rb = Rs × log₂(M)
- 🧠 **"QPSK duplica, 16-QAM cuadruplica"**: Relación directa con BPSK

#### Valores Típicos (para referencias rápidas)

| Modulación | M | Bits/Símbolo | Rb/Rs |
|------------|---|--------------|-------|
| BPSK | 2 | 1 | 1 |
| QPSK | 4 | 2 | 2 |
| 8-PSK | 8 | 3 | 3 |
| 16-QAM | 16 | 4 | 4 |
| 64-QAM | 64 | 6 | 6 |
| 256-QAM | 256 | 8 | 8 |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Sklar Cap. 3 "Bandpass Modulation and Demodulation"
- **Material del curso**: Laboratorio de medición de velocidad de símbolo con osciloscopio
- **Simulaciones**: GNU Radio - visualización de símbolos vs bits en tiempo real

#### Temas Relacionados para Explorar
1. Codificación de línea y su efecto en la velocidad de señalización
2. Técnicas de pulse shaping y su impacto en el ancho de banda
3. Velocidades de símbolo fraccionales en sistemas modernos

#### Preguntas para Reflexionar
- ¿Por qué los sistemas ópticos pueden usar velocidades de símbolo mucho mayores que los inalámbricos?
- ¿Cuál sería el límite práctico de M considerando ruido y complejidad del receptor?
- ¿Cómo afecta la velocidad de símbolo al consumo de potencia del transceptor?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 35 minutos
**Prerequisitos críticos**: Modulación digital básica, logaritmos, concepto de símbolo
**Tags**: `#velocidad-simbolo` `#tasa-bits` `#baudios` `#eficiencia-espectral`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*