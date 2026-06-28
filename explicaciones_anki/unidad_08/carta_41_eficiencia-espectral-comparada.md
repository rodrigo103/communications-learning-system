# Carta 41: Eficiencia Espectral Comparada de Sistemas de Modulación

> **Unidad 8**: Intercomparación de Sistemas

---

## 🎯 Pregunta

Compare la eficiencia espectral de diferentes esquemas de modulación.

---

## 📝 Respuesta Breve (de la carta original)

**Eficiencia espectral** = Rb/BW (bits/s/Hz)

**Analógicas** (referencia):
- AM-DSB: ~1 bit/s/Hz (pobre)
- SSB: ~2 bits/s/Hz (mejor)
- FM: muy pobre (BW grande), pero buena en SNR

**Digitales**:
- **ASK, FSK**: 0.5-1 bit/s/Hz (baja)
- **BPSK**: ~1 bit/s/Hz
- **QPSK**: ~2 bits/s/Hz
- **8-PSK**: ~3 bits/s/Hz
- **16-QAM**: ~4 bits/s/Hz
- **64-QAM**: ~6 bits/s/Hz
- **256-QAM**: ~8 bits/s/Hz

**Tendencia**: QAM de alto orden tiene máxima eficiencia espectral, pero requiere mayor SNR.

**Conclusión**: existe trade-off entre eficiencia espectral y robustez (BER).

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La eficiencia espectral es uno de los parámetros más críticos en el diseño de sistemas de comunicaciones modernos. Con el espectro electromagnético siendo un recurso finito y costoso, maximizar la cantidad de información transmitida por unidad de ancho de banda se ha vuelto esencial. Este concepto es particularmente crucial en sistemas celulares donde el espectro licenciado puede costar miles de millones de dólares, y en aplicaciones satelitales donde el ancho de banda del transpondedor es extremadamente valioso.

En la práctica, la eficiencia espectral determina cuántos usuarios pueden ser servidos simultáneamente en una red celular, cuántos canales de TV pueden transmitirse en un cable coaxial, o cuánta información puede enviarse a través de un enlace de microondas. Por ejemplo, la evolución de 2G GSM (0.33 bits/s/Hz) a 5G (hasta 30 bits/s/Hz en condiciones ideales) ha permitido el explosivo crecimiento del tráfico de datos móviles.

Históricamente, la búsqueda de mayor eficiencia espectral ha impulsado innovaciones fundamentales en comunicaciones. Desde el simple AM de los años 1920s hasta las sofisticadas constelaciones QAM de orden superior usadas en WiFi 6 y 5G, cada generación ha empujado los límites de cuánta información puede empaquetarse en el espectro disponible.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Ancho de banda de señales moduladas
- Velocidad de símbolo vs tasa de bits
- Teorema de Nyquist para señalización
- Constelaciones de señales digitales
- Filtrado de forma de pulso

#### Desarrollo Paso a Paso

**Paso 1: Definición Formal de Eficiencia Espectral**

La eficiencia espectral η se define como:
$$\eta = \frac{R_b}{B} \text{ [bits/s/Hz]}$$

Donde:
- $R_b$ = tasa de bits (bits/s)
- $B$ = ancho de banda ocupado (Hz)

Para modulaciones M-arias:
$$\eta = \frac{R_s \cdot \log_2(M)}{B}$$

Donde $R_s$ es la tasa de símbolos (baudios).

**Paso 2: Límites Teóricos**

El teorema de Nyquist establece que para señalización sin ISI:
$$R_s \leq 2B$$

Por lo tanto, la eficiencia espectral máxima teórica:
$$\eta_{max} = 2\log_2(M) \text{ bits/s/Hz}$$

Esto asume filtrado ideal (pulsos sinc) que es irrealizable. En práctica con filtrado raised-cosine:
$$\eta_{práctica} = \frac{\log_2(M)}{1 + \alpha}$$

Donde α es el factor de roll-off (típicamente 0.2-0.35).

**Paso 3: Análisis por Tipo de Modulación**

**Modulaciones Analógicas:**
- **AM-DSB**: BW = 2fm, transporta ~fm de información → η ≈ 0.5-1 bits/s/Hz
- **SSB**: BW = fm, mejor eficiencia → η ≈ 1-2 bits/s/Hz
- **FM**: BW = 2(Δf + fm), muy ineficiente espectralmente → η < 0.5 bits/s/Hz

**Modulaciones Digitales Básicas:**
- **ASK/OOK binario**: 1 bit/símbolo, η ≈ 0.5-1 bits/s/Hz
- **FSK binario**: Separación de frecuencias reduce eficiencia, η ≈ 0.4-0.8 bits/s/Hz
- **BPSK**: 1 bit/símbolo, η ≈ 0.8-1 bits/s/Hz con filtrado práctico

**Modulaciones M-arias:**
- **M-PSK**: log₂(M) bits/símbolo, misma BW que BPSK
- **M-QAM**: log₂(M) bits/símbolo, constelación rectangular eficiente

#### Derivación Matemática

**Cálculo de Eficiencia para M-QAM:**

Para M-QAM con filtrado raised-cosine:

$$B = \frac{R_s(1 + \alpha)}{2}$$ (para transmisión banda base equivalente)

La tasa de bits:
$$R_b = R_s \cdot \log_2(M)$$

Por lo tanto:
$$\eta = \frac{R_b}{B} = \frac{R_s \cdot \log_2(M)}{R_s(1 + \alpha)/2} = \frac{2\log_2(M)}{1 + \alpha}$$

Con α = 0.25 (típico):
$$\boxed{\eta_{M-QAM} = \frac{2\log_2(M)}{1.25} = 1.6\log_2(M) \text{ bits/s/Hz}}$$

**Ejemplos numéricos:**
- 16-QAM: η = 1.6 × 4 = 6.4 bits/s/Hz
- 64-QAM: η = 1.6 × 6 = 9.6 bits/s/Hz
- 256-QAM: η = 1.6 × 8 = 12.8 bits/s/Hz

### 🔬 Intuición y Analogías

**Analogía Principal: El Empaquetado de Información**

Imagine el espectro como una autopista y los bits como vehículos. La eficiencia espectral es como la densidad de tráfico: cuántos vehículos (bits) pueden viajar por unidad de ancho de carretera (Hz) por unidad de tiempo (segundo).

- **Modulaciones simples (BPSK)**: Como motocicletas, un vehículo por carril
- **QPSK**: Como autos, transportan más pasajeros en el mismo espacio
- **QAM alto orden**: Como buses, máxima capacidad pero requieren condiciones ideales
- **FSK**: Como camiones con carga ancha, ocupan múltiples carriles

**Intuición Física:**

La eficiencia espectral refleja qué tan "apretados" podemos empaquetar los símbolos tanto en tiempo como en frecuencia sin que interfieran entre sí. Es un balance entre:
- **Separación temporal**: Qué tan rápido enviamos símbolos
- **Separación espectral**: Cuánto espectro ocupa cada símbolo
- **Separación en constelación**: Qué tan cerca están los puntos de la constelación

**Visualización:**

En un diagrama tiempo-frecuencia:
- **Eje horizontal**: Tiempo (duración del símbolo)
- **Eje vertical**: Frecuencia (ancho de banda)
- **Área del rectángulo**: Recurso tiempo-frecuencia usado
- **Eficiencia**: Bits transportados por unidad de área

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Cálculo de Eficiencia Espectral en Sistema WiFi 802.11ac

**Situación:** Canal WiFi de 80 MHz usando diferentes modulaciones según condiciones

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Ancho de canal | 80 | MHz |
| Subportadoras de datos | 234 | - |
| Duración símbolo OFDM | 3.6 | μs |
| Intervalo de guarda | 0.4 | μs |

**Cálculo para diferentes MCS (Modulation Coding Schemes):**

1. **MCS 0 (BPSK, rate 1/2):**
   $$R_b = \frac{234 \times 1 \times 0.5}{4\mu s} = 29.25 \text{ Mbps}$$
   $$\eta = \frac{29.25}{80} = 0.366 \text{ bits/s/Hz}$$

2. **MCS 7 (64-QAM, rate 5/6):**
   $$R_b = \frac{234 \times 6 \times 5/6}{4\mu s} = 292.5 \text{ Mbps}$$
   $$\eta = \frac{292.5}{80} = 3.66 \text{ bits/s/Hz}$$

3. **MCS 9 (256-QAM, rate 5/6):**
   $$R_b = \frac{234 \times 8 \times 5/6}{4\mu s} = 390 \text{ Mbps}$$
   $$\eta = \frac{390}{80} = 4.875 \text{ bits/s/Hz}$$

**Interpretación:** WiFi adapta la eficiencia según SNR, priorizando robustez en malas condiciones.

---

#### Ejemplo 2: Comparación de Eficiencia en Evolución Celular

**Contexto:** Evolución de eficiencia espectral en redes móviles

**Análisis histórico:**

| Generación | Tecnología | Modulación típica | η promedio [bits/s/Hz/celda] | η pico [bits/s/Hz] |
|------------|------------|------------------|------------------------------|-------------------|
| 2G | GSM | GMSK | 0.33 | 0.33 |
| 3G | WCDMA | QPSK/16-QAM | 0.7 | 2 |
| 4G | LTE | QPSK a 64-QAM | 1.6 | 5 |
| 4G+ | LTE-Advanced | hasta 256-QAM | 2.4 | 8 |
| 5G | NR | hasta 1024-QAM | 3.5 | 30 |

**Factores de mejora:**
- Modulaciones de orden superior
- MIMO (múltiples antenas)
- Mejor codificación de canal
- Coordinación entre celdas
- Carrier aggregation

---

#### Ejemplo 3: Trade-off Eficiencia vs SNR Requerido

**¿Qué pasa cuando aumentamos el orden de modulación?**

Análisis del costo en SNR para mantener BER = 10^-6:

| Modulación | η teórica [bits/s/Hz] | SNR requerido [dB] | Incremento SNR | Aplicación típica |
|------------|------------------------|-------------------|----------------|-------------------|
| BPSK | 1 | 10.5 | - | Telemetría espacial |
| QPSK | 2 | 10.5 | 0 dB | DVB-S, GPS |
| 8-PSK | 3 | 14.0 | +3.5 dB | EDGE |
| 16-QAM | 4 | 17.4 | +6.9 dB | LTE urbano |
| 64-QAM | 6 | 23.5 | +13 dB | Cable, WiFi cerca AP |
| 256-QAM | 8 | 29.8 | +19.3 dB | Cable DOCSIS 3.1 |
| 1024-QAM | 10 | 36.1 | +25.6 dB | Microondas línea vista |

**Observación clave:** Cada duplicación de eficiencia espectral requiere aproximadamente 6 dB adicionales de SNR.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Teorema de Shannon** (Carta 45): Define el límite superior de eficiencia
- **Constelaciones digitales** (Carta 28): Base para modulaciones M-arias
- **Ancho de banda de Carson** (Carta 18): Para calcular eficiencia en FM
- **OFDM** (Carta 53): Maximiza eficiencia mediante subportadoras ortogonales

#### Dependencias (lo que necesitas saber primero)
1. Relación símbolo-bit en modulaciones M-arias
2. Concepto de ancho de banda de señales moduladas
3. Teorema de Nyquist para señalización sin ISI

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Diseño de sistemas**: Selección de modulación según espectro disponible
2. **Planificación de redes**: Cálculo de capacidad y cobertura
3. **Análisis económico**: Costo por bit transmitido

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La eficiencia espectral no es gratis: mayor eficiencia requiere mayor SNR
- Existe un límite teórico (Shannon) que ningún sistema puede superar
- La eficiencia práctica es menor que la teórica debido a filtrado y overhead
- Diferentes aplicaciones requieren diferentes balances eficiencia-robustez

#### Tipos de problemas típicos
1. **Cálculo directo**: Dada modulación y BW, calcular tasa máxima
   - Estrategia: Aplicar η = log₂(M)/(1+α) y multiplicar por BW

2. **Comparación de sistemas**: Evaluar mejora al cambiar modulación
   - Estrategia: Calcular ratio de eficiencias y costo en SNR

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir eficiencia teórica con práctica**
- Por qué ocurre: Ignorar efectos de filtrado y roll-off
- Cómo evitarlo: Incluir factor (1+α) en cálculos reales
- Ejemplo: 16-QAM no da 4 bits/s/Hz en práctica, sino ~3.2 con α=0.25

❌ **Error #2: Ignorar overhead de protocolo**
- Por qué ocurre: Considerar solo la capa física
- Cómo evitarlo: Distinguir entre eficiencia de modulación y throughput neto
- Ejemplo: WiFi 802.11ac puede tener η=5 bits/s/Hz pero throughput real ~3.5

❌ **Error #3: Asumir eficiencia constante en todo el área de cobertura**
- Por qué ocurre: No considerar variación de SNR con distancia
- Cómo evitarlo: Usar eficiencia promedio ponderada por área
- Distinción: Centro de celda puede usar 256-QAM, borde solo QPSK

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Eficiencia espectral: η = R_b/B [bits/s/Hz]
M-QAM teórica: η = log₂(M) [bits/s/Hz]
M-QAM práctica: η = log₂(M)/(1+α) [bits/s/Hz]
Límite de Shannon: η_max = log₂(1 + SNR) [bits/s/Hz]
```

#### Conceptos Fundamentales
- ✓ **Jerarquía clara**: QAM > PSK > FSK en eficiencia espectral
- ✓ **Trade-off fundamental**: Mayor eficiencia requiere mayor SNR
- ✓ **Límite de Shannon**: Barrera infranqueable para cualquier sistema

#### Reglas Mnemotécnicas
- 🧠 **"Bits por Hertz"**: La eficiencia es literalmente bits/s dividido por Hz
- 🧠 **"Duplicar cuesta 6"**: Duplicar eficiencia requiere ~6 dB más de SNR

#### Valores Típicos (para referencias rápidas)

| Aplicación | Modulación común | η típica [bits/s/Hz] | SNR típico [dB] |
|------------|------------------|---------------------|-----------------|
| Satélite | QPSK | 1.5 | 5-10 |
| TV Digital | 64-QAM | 5 | 20-25 |
| WiFi cercano | 1024-QAM | 8-10 | >35 |
| 5G mmWave | 256-QAM | 6-8 | 25-30 |
| Fibra óptica | 64-QAM | 6 | >30 |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**: Goldsmith "Wireless Communications" Cap. 4 - Adaptive Modulation
- **Papers**: "Spectral Efficiency Limits and Modulation Order Selection" - IEEE Comm. Magazine
- **Herramientas**: GNU Radio para experimentar con diferentes modulaciones

#### Temas Relacionados para Explorar
1. Técnicas de modulación multidimensional
2. Shaping de constelación para acercarse a Shannon
3. Eficiencia espectral con MIMO masivo

#### Preguntas para Reflexionar
- ¿Por qué no usamos siempre la modulación de mayor orden disponible?
- ¿Cómo afecta la movilidad a la eficiencia espectral alcanzable?
- ¿Será posible alcanzar el límite de Shannon en sistemas prácticos?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 30 minutos
**Prerequisitos críticos**: Modulaciones digitales, teorema de Nyquist, constelaciones
**Tags**: `#eficiencia-espectral` `#modulacion-maria` `#qam` `#trade-offs`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*