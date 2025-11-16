# Carta 50: Modulación de Espectro Expandido (Spread Spectrum)

> **Unidad 10**: Espectro Expandido y OFDM

---

## 🎯 Pregunta

¿Qué es la modulación de espectro expandido (Spread Spectrum) y cuáles son sus ventajas principales?

---

## 📝 Respuesta Breve (de la carta original)

**Spread Spectrum** expande deliberadamente el ancho de banda de la señal mucho más allá del mínimo necesario.

**Características**:
- BW transmitida >> BW de información
- Usa secuencia pseudoaleatoria (código)
- Densidad espectral de potencia baja

**Ventajas principales**:
1. **Resistencia a interferencias**: señal parece ruido para no-autorizados
2. **Múltiple acceso** (CDMA): usuarios comparten frecuencia
3. **Inmunidad a jamming**: aplicaciones militares
4. **Privacidad**: difícil interceptar sin conocer código
5. **Resistencia a multitrayecto**: diversidad temporal
6. **Baja probabilidad de detección** (LPD/LPI)

**Costo**: requiere mayor BW y sincronización precisa

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

**¿Por qué es importante este concepto?**
El espectro expandido representa un paradigma revolucionario en comunicaciones que contradice la intuición tradicional de eficiencia espectral. Mientras que los sistemas convencionales buscan minimizar el ancho de banda, spread spectrum deliberadamente lo expande para obtener beneficios únicos. Esta técnica es fundamental en sistemas modernos como GPS, comunicaciones militares seguras, redes celulares 3G, y WiFi, donde la resistencia a interferencias y la capacidad de compartir espectro son críticas.

**¿Dónde se aplica?**
Las aplicaciones del espectro expandido son ubicuas en la vida moderna:
- **GPS**: todos los satélites transmiten en la misma frecuencia usando códigos únicos
- **Comunicaciones militares**: resistentes a jamming y difíciles de detectar
- **Redes celulares CDMA**: IS-95, CDMA2000, WCDMA (3G)
- **WiFi original**: 802.11b usaba DSSS para 11 Mbps
- **Bluetooth**: usa frequency hopping para evitar interferencias
- **Sistemas RFID**: algunos tags activos usan spread spectrum

**Historia:**
El concepto fue patentado en 1942 por la actriz Hedy Lamarr y el compositor George Antheil para sistemas de torpedos guiados resistentes a jamming. Durante la Guerra Fría, se desarrolló extensivamente para comunicaciones militares seguras. En los 1980s-1990s, Qualcomm revolucionó las comunicaciones celulares aplicando CDMA comercialmente.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Teorema de Shannon-Hartley: C = B log₂(1 + SNR)
- Correlación y funciones de autocorrelación
- Secuencias pseudoaleatorias (PN)
- Procesamiento de señales digitales
- Modulaciones digitales básicas (PSK, QAM)

#### Desarrollo Paso a Paso

**Paso 1: Principio Fundamental**
En sistemas convencionales, el ancho de banda de transmisión es aproximadamente igual al ancho de banda de la información:
$$BW_{trans} \approx BW_{info}$$

En spread spectrum, expandimos deliberadamente:
$$BW_{trans} >> BW_{info}$$

El factor de expansión se llama **ganancia de procesamiento**:
$$G_p = \frac{BW_{trans}}{BW_{info}}$$

**Paso 2: Proceso de Expansión**
La expansión se logra multiplicando la señal de información por una secuencia pseudoaleatoria de alta velocidad:

$$s_{SS}(t) = m(t) \cdot c(t) \cdot \cos(2\pi f_c t)$$

Donde:
- $m(t)$ = señal de información (baja velocidad)
- $c(t)$ = código PN (alta velocidad, chip rate >> bit rate)
- $f_c$ = frecuencia de portadora

**Paso 3: Densidad Espectral de Potencia**
La potencia total se mantiene constante pero se distribuye en un ancho de banda mayor:

$$PSD_{SS}(f) = \frac{P_{total}}{BW_{trans}}$$

Esto resulta en una señal que parece ruido y está por debajo del nivel de ruido en muchos casos.

#### Derivación Matemática

**Ganancia de Procesamiento y SNR:**

Partiendo del modelo de sistema con interferencia:

$$r(t) = s_{SS}(t) + n(t) + j(t)$$

Donde $j(t)$ es interferencia de banda angosta.

**En el receptor, después de la decorrelación:**

$$SNR_{out} = SNR_{in} \cdot G_p$$

**Para interferencia de banda angosta:**

$$\frac{S_{out}}{J_{out}} = \frac{S_{in}}{J_{in}} \cdot G_p$$

**Resultado fundamental:**
$$\boxed{G_p = \frac{BW_{SS}}{R_b} = \frac{R_{chip}}{R_{bit}}}$$

**Significado físico:**
- $G_p$: mejora en SNR después del despread
- $BW_{SS}$: ancho de banda del spread spectrum
- $R_b$: tasa de bits de información
- $R_{chip}$: tasa de chips del código PN

### 🔬 Intuición y Analogías

**Analogía principal:**
El spread spectrum es como escribir un mensaje secreto distribuyendo cada letra en páginas diferentes de muchos libros en una biblioteca. Solo quien conoce el patrón exacto (el código) puede reconstruir el mensaje. Para todos los demás, las letras parecen ruido aleatorio en los libros.

**Intuición física:**
Imagina que tienes 1 watt de potencia. En comunicación convencional, concentras toda esa potencia en un ancho de banda estrecho (como un láser). En spread spectrum, dispersas esa misma potencia en un espectro muy amplio (como una linterna con difusor). La energía total es la misma, pero la densidad es mucho menor, haciéndola menos detectable y menos susceptible a interferencias puntuales.

**Visualización:**
En el dominio frecuencial, una señal de banda angosta es como un pico alto y estrecho, mientras que spread spectrum es como una meseta baja y amplia. La interferencia que afecta una frecuencia específica daña completamente la señal estrecha, pero apenas afecta a la señal expandida.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Sistema GPS Civil

**Situación:** Calcular la ganancia de procesamiento del GPS L1 C/A

**Datos:**
| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Chip rate | 1.023 | Mchips/s |
| Data rate | 50 | bits/s |
| Frecuencia portadora | 1575.42 | MHz |

**Solución paso a paso:**

1. **Calcular ganancia de procesamiento:**
   $$G_p = \frac{R_{chip}}{R_{bit}} = \frac{1.023 \times 10^6}{50} = 20,460$$

2. **Expresar en dB:**
   $$G_p(dB) = 10\log_{10}(20,460) = 43.1 \text{ dB}$$

3. **Ancho de banda ocupado:**
   $$BW_{SS} \approx 2 \times R_{chip} = 2.046 \text{ MHz}$$

**Interpretación:** El GPS puede funcionar con señales 43 dB por debajo del nivel de ruido térmico gracias a esta enorme ganancia de procesamiento.

---

#### Ejemplo 2: Sistema CDMA IS-95 (Celular 2G/3G)

**Contexto:** Canal de voz en sistema CDMA comercial

**Parámetros del sistema:**
- Chip rate: 1.2288 Mchips/s
- Tasa de voz codificada: 9.6 kbps
- Ancho de banda del canal: 1.25 MHz

**Cálculos:**
1. Ganancia de procesamiento:
   $$G_p = \frac{1.2288 \times 10^6}{9.6 \times 10^3} = 128 = 21 \text{ dB}$$

2. Capacidad del sistema (simplificada):
   $$N_{usuarios} \approx \frac{G_p}{(E_b/N_0)_{req} \cdot \alpha}$$

   Donde α incluye factores de actividad de voz, sectorización, etc.

3. Con valores típicos:
   - $(E_b/N_0)_{req}$ = 6 dB = 4 (lineal)
   - Factor de actividad de voz = 0.4
   - Sectorización (3 sectores) = 2.5

   $$N_{usuarios} \approx \frac{128}{4} \cdot 0.4 \cdot 2.5 = 32 \text{ usuarios/sector}$$

---

#### Ejemplo 3: Resistencia a Jamming

**¿Qué pasa cuando hay interferencia intencional?**

Consideremos un sistema con:
- Potencia de señal: -100 dBm
- Potencia de jammer: -60 dBm (40 dB más fuerte)
- Ganancia de procesamiento: 30 dB

**Análisis:**
- SJR (Signal-to-Jammer Ratio) inicial: -40 dB
- SJR después del despread: -40 + 30 = -10 dB
- Con codificación adicional (3 dB): -7 dB

**Resultado:** El sistema puede operar incluso con jammers 40 dB más potentes que la señal deseada.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Teorema de Shannon** (Carta 45): Spread spectrum intercambia ancho de banda por robustez
- **CDMA** (Carta 52): Aplicación directa de spread spectrum para acceso múltiple
- **Modulaciones digitales** (Cartas 27-32): Base sobre la cual se aplica spreading
- **Ruido blanco** (Carta 33): La señal spread spectrum se asemeja a ruido
- **OFDM** (Carta 53): Técnica complementaria/alternativa para multiacceso

#### Dependencias (lo que necesitas saber primero)
1. Correlación y ortogonalidad → Para entender códigos PN
2. Transformada de Fourier → Para analizar expansión espectral
3. SNR y Eb/N0 → Para cuantificar mejoras

#### Aplicaciones Posteriores (dónde usarás esto)
1. **CDMA**: Acceso múltiple en redes celulares
2. **Ultra-wideband (UWB)**: Llevando spread spectrum al extremo
3. **Cognitive Radio**: Compartir espectro dinámicamente
4. **IoT y LoRa**: Comunicaciones de largo alcance y baja potencia

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La diferencia fundamental entre eficiencia espectral y robustez
- Cómo la correlación permite recuperar señales bajo el ruido
- Por qué spread spectrum es resistente a interferencias de banda angosta
- La relación entre ganancia de procesamiento y mejora en SNR
- Aplicaciones prácticas donde spread spectrum es la mejor solución

#### Tipos de problemas típicos
1. **Cálculo de ganancia de procesamiento**: Dados chip rate y bit rate
   - Estrategia: $G_p = R_{chip}/R_{bit}$, convertir a dB

2. **Análisis de resistencia a jamming**: Calcular SJR antes y después
   - Estrategia: Sumar $G_p$ (en dB) al SJR inicial

3. **Diseño de sistema**: Determinar chip rate necesario para cierta robustez
   - Estrategia: Trabajar desde requisitos de $G_p$ hacia atrás

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir chip rate con bit rate**
- Por qué ocurre: Ambos se miden en "por segundo"
- Cómo evitarlo: Chip rate SIEMPRE >> bit rate en spread spectrum
- Ejemplo: GPS tiene 1.023 Mchips/s pero solo 50 bits/s de datos

❌ **Error #2: Pensar que spread spectrum aumenta la capacidad del canal**
- Por qué ocurre: Confusión con el teorema de Shannon
- Cómo evitarlo: SS no aumenta C, solo redistribuye recursos
- Distinción: Intercambia eficiencia espectral por robustez

❌ **Error #3: Asumir que más spreading siempre es mejor**
- Por qué ocurre: Si algo de spreading es bueno, más debe ser mejor
- Realidad: Hay límites prácticos (sincronización, complejidad, delay)
- Balance: Optimizar $G_p$ según requisitos del sistema

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Ganancia de procesamiento: Gp = BWss/Rb = Rchip/Rbit
Mejora en SJR: SJRout = SJRin + Gp (en dB)
Capacidad CDMA: N ≈ Gp/(Eb/N0)req
```

#### Conceptos Fundamentales
- ✓ **Expansión deliberada**: BW transmitido >> BW información (contraintuitivo pero poderoso)
- ✓ **Ganancia de procesamiento**: Cuantifica la mejora en robustez
- ✓ **Códigos ortogonales**: Permiten múltiples usuarios simultáneos
- ✓ **Trade-off fundamental**: Eficiencia espectral vs. robustez/seguridad

#### Reglas Mnemotécnicas
- 🧠 **"SPREAD"**: Security, Privacy, Resistance, Energy (baja densidad), Access (múltiple), Detection (difícil)
- 🧠 **GPS = 43 dB**: Recordar que GPS tiene ~43 dB de ganancia de procesamiento

#### Valores Típicos (para referencias rápidas)
| Sistema | Chip Rate | Gp (dB) | Aplicación |
|---------|-----------|---------|------------|
| GPS C/A | 1.023 Mchips/s | 43 | Navegación civil |
| CDMA IS-95 | 1.2288 Mchips/s | 21 | Celular 2G/3G |
| WiFi 802.11b | 11 Mchips/s | 10.4 | WLAN 11 Mbps |
| Bluetooth | 1 MHz hops | Variable | PAN |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**:
  - Simon, Omura et al., "Spread Spectrum Communications Handbook"
  - Peterson & Ziemer, "Introduction to Spread Spectrum Communications"
  - Proakis & Salehi, Cap. 13: "Spread Spectrum Signals"
- **Papers clásicos**:
  - Scholtz (1982): "The Origins of Spread-Spectrum Communications"
- **Simulaciones**:
  - MATLAB Communications Toolbox: ejemplos de DSSS y FHSS
  - GNU Radio: implementaciones de spread spectrum

#### Temas Relacionados para Explorar
1. Secuencias PN: m-sequences, Gold codes, Walsh codes
2. Sincronización y adquisición en spread spectrum
3. Near-far problem en CDMA
4. Ultra-wideband (UWB) como caso extremo
5. Spread spectrum en comunicaciones ópticas

#### Preguntas para Reflexionar
- ¿Por qué GPS funciona con señales 20 dB bajo el ruido?
- ¿Cómo puede Bluetooth evitar interferir con WiFi compartiendo la banda de 2.4 GHz?
- ¿Cuál es el límite teórico de usuarios en un sistema CDMA perfecto?
- ¿Por qué los sistemas modernos (4G/5G) prefieren OFDMA sobre CDMA?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 45 minutos
**Prerequisitos críticos**: Teoría de señales, correlación, secuencias PN
**Tags**: `#spread-spectrum` `#CDMA` `#GPS` `#ganancia-procesamiento` `#robustez`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*