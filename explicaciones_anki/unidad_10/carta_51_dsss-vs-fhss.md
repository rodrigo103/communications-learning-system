# Carta 51: DSSS vs FHSS - Técnicas de Espectro Expandido

> **Unidad 10**: Espectro Expandido y OFDM

---

## 🎯 Pregunta

Compare las técnicas DSSS (Direct Sequence) y FHSS (Frequency Hopping) de espectro expandido.

---

## 📝 Respuesta Breve (de la carta original)

**DSSS (Direct Sequence Spread Spectrum)**:
- Multiplica datos por secuencia PN de alta velocidad (chip rate >> bit rate)
- Ocupa todo el BW todo el tiempo
- Ganancia de procesamiento: $G_p = BW_{RF}/BW_{info}$
- Mejor para ambientes con ruido continuo
- Ejemplo: GPS, CDMA (IS-95), WiFi 802.11b

**FHSS (Frequency Hopping Spread Spectrum)**:
- Cambia rápidamente la frecuencia de portadora según patrón PN
- Usa una frecuencia a la vez, pero muchas frecuencias en el tiempo
- Dos tipos: Fast hopping (varios hops/bit) y Slow hopping (varios bits/hop)
- Mejor contra interferencia de banda angosta y jamming
- Ejemplo: Bluetooth, 802.11 (original)

**Comparación**:
- DSSS: mejor ganancia de procesamiento, más complejo
- FHSS: implementación más simple, mejor contra jamming pulsado

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

**¿Por qué es importante este concepto?**
DSSS y FHSS representan las dos estrategias fundamentales para implementar spread spectrum, cada una con ventajas únicas que las hacen óptimas para diferentes escenarios. La elección entre DSSS y FHSS determina la arquitectura completa del sistema, desde el transmisor hasta los algoritmos de sincronización. Comprender sus diferencias es crucial para diseñar sistemas robustos: GPS usa DSSS por su excelente correlación, mientras que Bluetooth usa FHSS para coexistir con WiFi en 2.4 GHz.

**¿Dónde se aplica?**
Las aplicaciones reales muestran la complementariedad de ambas técnicas:
- **DSSS**: GPS (todos los satélites en la misma frecuencia), redes celulares CDMA, WiFi 802.11b (11 Mbps), sistemas militares de comunicación segura
- **FHSS**: Bluetooth (adaptative frequency hopping), sistemas militares tácticos, radios HF militares, primeras versiones de WiFi (802.11 legacy)
- **Híbridos**: Algunos sistemas modernos combinan ambas técnicas para máxima robustez

**Historia:**
FHSS fue la primera técnica propuesta (patente de Hedy Lamarr, 1942) para torpedos guiados. DSSS se desarrolló en los 1950s para comunicaciones militares. Durante la Guerra Fría, ambas evolucionaron paralelamente. En los 1990s, la decisión de Qualcomm de usar DSSS para CDMA celular y de Ericsson de usar FHSS para Bluetooth marcó sus aplicaciones comerciales distintivas.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Espectro expandido básico (Carta 50)
- Secuencias pseudoaleatorias (PN sequences)
- Modulación digital (PSK, FSK)
- Sincronización de sistemas
- Teoría de correlación

#### Desarrollo Paso a Paso

**Paso 1: DSSS - Expansión Directa**

En DSSS, la señal de datos se multiplica directamente por un código PN de alta velocidad:

$$s_{DSSS}(t) = d(t) \cdot c(t) \cdot \cos(2\pi f_c t)$$

Donde:
- $d(t)$ = datos binarios (±1) con período $T_b$
- $c(t)$ = código PN (±1) con período $T_c$ (chip)
- $T_c << T_b$ (típicamente $T_b/T_c$ = 10 a 1000)

El espectro resultante tiene ancho de banda:
$$BW_{DSSS} \approx \frac{2}{T_c} = 2R_{chip}$$

**Paso 2: FHSS - Saltos de Frecuencia**

En FHSS, la frecuencia de portadora cambia según un patrón pseudoaleatorio:

$$s_{FHSS}(t) = d(t) \cdot \cos(2\pi f_i(t) \cdot t)$$

Donde $f_i(t)$ salta entre M frecuencias disponibles:
$$f_i \in \{f_1, f_2, ..., f_M\}$$

El patrón de saltos está determinado por el código PN.

**Paso 3: Comparación de Procesamiento**

**DSSS - Procesamiento:**
- Receptor multiplica por el mismo código PN sincronizado
- Correlación alta solo con código correcto
- Interferencias se expanden y quedan como ruido de fondo

**FHSS - Procesamiento:**
- Receptor salta sincronizadamente con transmisor
- Interferencia afecta solo cuando coincide en frecuencia y tiempo
- Promediación sobre múltiples saltos reduce efecto de interferencias

#### Derivación Matemática

**Ganancia de Procesamiento en DSSS:**

Para DSSS, la ganancia contra interferencia de banda angosta:

$$G_{p,DSSS} = \frac{BW_{SS}}{BW_{datos}} = \frac{R_{chip}}{R_{bit}}$$

**Después del despread en receptor:**
$$\frac{S}{J}_{out} = \frac{S}{J}_{in} \cdot G_{p,DSSS}$$

**Ganancia de Procesamiento en FHSS:**

Para FHSS con interferencia en k de M frecuencias:

$$G_{p,FHSS} = \frac{M}{k}$$

**Probabilidad de hit (colisión):**
$$P_{hit} = \frac{k}{M}$$

**Comparación de BER:**

Para DSSS con BPSK y ruido gaussiano:
$$BER_{DSSS} = Q\left(\sqrt{2G_p \cdot \frac{E_b}{N_0}}\right)$$

Para FHSS con FSK no coherente:
$$BER_{FHSS} = \frac{P_{hit}}{2}e^{-\frac{E_b}{2N_0}} + \frac{1-P_{hit}}{2}e^{-\frac{E_b}{N_0}}$$

### 🔬 Intuición y Analogías

**Analogía DSSS:**
DSSS es como susurrar un secreto en un estadio lleno mezclándolo con el ruido de la multitud. El mensaje se distribuye en todo el "ruido", pero quien conoce el patrón exacto (código) puede filtrar y reconstruir el susurro original. El mensaje está presente todo el tiempo, pero diluido en todo el espectro.

**Analogía FHSS:**
FHSS es como una conversación donde cambias constantemente de idioma según un patrón acordado. Un espía que escuche en un solo idioma solo captará fragmentos. Solo quien conoce la secuencia de idiomas puede seguir toda la conversación. Cada "salto" usa todo el poder pero en diferente "canal".

**Intuición de la diferencia:**
- DSSS: "Esconde en el ruido" - señal débil pero omnipresente
- FHSS: "Evade al enemigo" - señal fuerte pero móvil

**Visualización espectral:**
- DSSS: banda ancha continua de baja densidad
- FHSS: pico estrecho que salta aleatoriamente

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Diseño de Sistema GPS (DSSS)

**Situación:** Analizar por qué GPS usa DSSS en lugar de FHSS

**Datos del sistema GPS:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Código C/A length | 1023 | chips |
| Chip rate | 1.023 | Mchips/s |
| Período código | 1 | ms |
| Número de satélites | 32 | códigos únicos |

**Análisis DSSS para GPS:**

1. **Correlación cruzada entre códigos:**
   - Códigos Gold con correlación cruzada baja
   - Permite que todos los satélites transmitan en 1575.42 MHz
   $$\rho_{ij} \leq \frac{65}{1023} \approx 0.064$$

2. **Adquisición de señal:**
   - Búsqueda en código (1023 chips) y Doppler
   - Tiempo de correlación: 1 ms

3. **Por qué no FHSS:**
   - Requeriría sincronización de saltos entre satélites
   - Complicaría enormemente la adquisición
   - Perdería capacidad de correlación para medición precisa de tiempo

**Conclusión:** DSSS permite medición precisa de tiempo de vuelo, esencial para posicionamiento.

---

#### Ejemplo 2: Coexistencia Bluetooth/WiFi (FHSS)

**Contexto:** Bluetooth usa FHSS adaptativo para coexistir con WiFi en 2.4 GHz

**Parámetros Bluetooth:**
- Banda ISM: 2.400 - 2.485 GHz
- Canales: 79 canales de 1 MHz
- Saltos por segundo: 1600 (clásico)
- Duración slot: 625 μs

**Análisis de coexistencia:**

1. **Sin WiFi presente:**
   - Usa los 79 canales uniformemente
   - Probabilidad de colisión con interferencia aleatoria:
   $$P_{col} = \frac{1}{79} = 0.0127$$

2. **Con WiFi 802.11b/g (canal 6, 22 MHz):**
   - WiFi ocupa canales Bluetooth 24-45 (22 canales)
   - Adaptive Frequency Hopping (AFH) detecta y evita
   - Canales buenos: 79 - 22 = 57
   $$P_{col,AFH} = 0$$ (idealmente)

3. **Ventaja de FHSS:**
   - Puede adaptar dinámicamente el conjunto de saltos
   - DSSS no podría evitar interferencia WiFi fija

---

#### Ejemplo 3: Comparación en Ambiente Jamming

**Escenario:** Sistema militar con jammer parcial

**Condiciones:**

| Parámetro | DSSS | FHSS |
|-----------|------|------|
| Ancho de banda total | 100 MHz | 100 MHz |
| Tasa de datos | 100 kbps | 100 kbps |
| Potencia señal | -100 dBm | -100 dBm |
| Potencia jammer | -60 dBm | -60 dBm |
| BW jammer | 10 MHz | 10 MHz |

**Análisis DSSS:**
1. Ganancia de procesamiento:
   $$G_p = \frac{100 \text{ MHz}}{100 \text{ kHz}} = 1000 = 30 \text{ dB}$$

2. Jammer afecta toda la transmisión pero atenuado:
   $$SJR_{out} = -40 + 30 = -10 \text{ dB}$$

**Análisis FHSS:**
1. Número de canales: 100 (1 MHz cada uno)
2. Canales afectados por jammer: 10
3. Probabilidad de hit: 10/100 = 0.1
4. Desempeño:
   - 90% del tiempo: sin interferencia (BER ≈ 10⁻⁶)
   - 10% del tiempo: con jamming (BER ≈ 0.5)
   - BER promedio: 0.9 × 10⁻⁶ + 0.1 × 0.5 ≈ 0.05

**Conclusión:** FHSS mejor contra jammer de banda parcial, DSSS mejor contra ruido uniforme.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Spread Spectrum básico** (Carta 50): Fundamento de ambas técnicas
- **CDMA** (Carta 52): Usa principalmente DSSS
- **Correlación y ortogonalidad**: Clave en DSSS para separar usuarios
- **Sincronización**: Crítica en ambas, pero diferente complejidad
- **Teorema de Shannon**: Ambas intercambian BW por robustez

#### Dependencias (lo que necesitas saber primero)
1. Secuencias PN y sus propiedades de correlación
2. Espectro de señales moduladas digitalmente
3. Efectos del ruido y la interferencia

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Sistemas híbridos DS/FH**: Máxima robustez militar
2. **Cognitive radio**: FHSS dinámico evitando usuarios primarios
3. **5G y más allá**: Combinaciones con OFDM
4. **IoT de largo alcance**: LoRa usa una variante de spread spectrum

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- Las diferencias fundamentales en cómo cada técnica expande el espectro
- Cuándo es preferible una técnica sobre la otra
- Cómo calcular ganancia de procesamiento en cada caso
- El impacto de diferentes tipos de interferencia en cada técnica
- Complejidad de implementación y sincronización

#### Tipos de problemas típicos
1. **Comparar desempeño con interferencia específica**
   - Estrategia: Calcular SIR o BER para cada técnica

2. **Diseñar sistema para requisitos dados**
   - Estrategia: Evaluar tipo de interferencia esperada y elegir técnica

3. **Calcular recursos necesarios (chips, frecuencias)**
   - Estrategia: Desde Gp requerida, determinar parámetros

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Pensar que FHSS siempre evita interferencias**
- Por qué ocurre: Simplificación excesiva del concepto
- Realidad: Solo efectivo si interferencia es parcial en frecuencia
- Ejemplo: Jammer de banda ancha afecta todos los saltos

❌ **Error #2: Asumir que DSSS es siempre más complejo**
- Por qué ocurre: DSSS requiere correladores complejos
- Realidad: FHSS requiere sintetizadores ágiles y sincronización precisa
- Balance: Depende de la tecnología disponible y requisitos

❌ **Error #3: Confundir slow-FH con fast-FH**
- Distinción clave:
  - Slow-FH: múltiples bits por hop (más simple)
  - Fast-FH: múltiples hops por bit (más robusto)
- Impacto: Muy diferente comportamiento ante errores de ráfaga

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
DSSS: Gp = Rchip/Rbit = BWss/BWdata
FHSS: Gp ≈ Número de frecuencias disponibles
DSSS con jammer: SJRout = SJRin + Gp (dB)
FHSS con jammer parcial: Phit = BWjammer/BWtotal
```

#### Conceptos Fundamentales
- ✓ **DSSS**: Expansión en dominio temporal/código - todo el BW, todo el tiempo
- ✓ **FHSS**: Expansión en dominio frecuencial - una frecuencia a la vez
- ✓ **Trade-offs**: DSSS mejor Gp y correlación; FHSS mejor contra jamming parcial
- ✓ **Sincronización**: Ambas la requieren, pero de diferente naturaleza

#### Reglas Mnemotécnicas
- 🧠 **DSSS = "Dilute"**: Diluye la señal en todo el espectro
- 🧠 **FHSS = "Flee"**: Huye de interferencias saltando
- 🧠 **GPS-DSSS, Bluetooth-FHSS**: Recordar aplicaciones típicas

#### Valores Típicos (para referencias rápidas)

| Sistema | Técnica | Gp típica | Característica clave |
|---------|---------|-----------|---------------------|
| GPS | DSSS | 43 dB | Correlación precisa |
| CDMA IS-95 | DSSS | 21 dB | Multiusuario |
| Bluetooth | FHSS | 18 dB | 79 canales AFH |
| WiFi 802.11b | DSSS | 10 dB | 11 Mbps |
| Militar | Híbrido | >40 dB | Máxima robustez |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**:
  - Torrieri, "Principles of Spread-Spectrum Communication Systems"
  - Simon et al., "Spread Spectrum Communications Handbook"
  - Sklar, "Digital Communications", Cap. 12
- **Papers**:
  - Pickholtz et al. (1982): "Theory of Spread-Spectrum Communications—A Tutorial"
- **Estándares**:
  - Bluetooth Core Specification (adaptive frequency hopping)
  - IS-95 CDMA standard (DSSS implementation)

#### Temas Relacionados para Explorar
1. Híbridos DS/FH para máxima robustez
2. Time Hopping Spread Spectrum (THSS)
3. Chirp Spread Spectrum (CSS) usado en LoRa
4. Sincronización y adquisición en DSSS vs FHSS
5. Ultra-wideband como caso extremo de DSSS

#### Preguntas para Reflexionar
- ¿Por qué los sistemas militares modernos combinan DSSS y FHSS?
- ¿Cómo afecta el efecto Doppler a DSSS vs FHSS?
- ¿Qué técnica sería mejor para comunicación submarina?
- ¿Cómo implementarías un sistema resistente a todo tipo de jamming?
- ¿Por qué 5G no usa spread spectrum como tecnología principal?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 40 minutos
**Prerequisitos críticos**: Spread spectrum básico, secuencias PN, sincronización
**Tags**: `#DSSS` `#FHSS` `#spread-spectrum` `#GPS` `#Bluetooth` `#comparación`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*