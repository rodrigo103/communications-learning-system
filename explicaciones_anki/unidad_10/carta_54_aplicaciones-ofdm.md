# Carta 54: Aplicaciones de OFDM y su Dominio en Comunicaciones Modernas

> **Unidad 10**: Espectro Expandido y OFDM

---

## 🎯 Pregunta

¿Cuáles son las principales aplicaciones de OFDM y por qué es tan popular?

---

## 📝 Respuesta Breve (de la carta original)

**Aplicaciones principales de OFDM**:

1. **WiFi**: 802.11a/g/n/ac/ax
2. **4G LTE / 5G**: downlink usa OFDMA
3. **TV Digital**: DVB-T, ISDB-T, ATSC 3.0
4. **Radio Digital**: DAB, HD Radio
5. **DSL**: ADSL, VDSL (DMT - variante de OFDM)
6. **WiMAX**: 802.16

**Por qué es popular**:
1. **Multitrayecto**: maneja canales difíciles sin ecualizador complejo
2. **Eficiencia espectral**: alta capacidad
3. **Flexibilidad**: adaptive modulation and coding (AMC)
4. **Escalabilidad**: fácil variar BW
5. **Implementación práctica**: DSP eficiente con FFT

**Desventaja principal**: alto PAPR (Peak-to-Average Power Ratio) → requiere amplificadores lineales costosos

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

**¿Por qué OFDM domina las comunicaciones modernas?** OFDM se ha convertido en la tecnología de capa física dominante porque resuelve elegantemente los desafíos fundamentales de las comunicaciones de alta velocidad: multitrayecto severo, uso eficiente del espectro, y flexibilidad para adaptarse a condiciones cambiantes del canal. Su adopción masiva desde WiFi hasta 5G no es casualidad - es el resultado de ventajas técnicas fundamentales que ninguna otra tecnología iguala.

**¿Dónde NO se usa OFDM?** Es igualmente instructivo entender dónde OFDM no es óptimo:
- Enlaces satelitales (problema de PAPR con amplificadores de potencia)
- Comunicaciones submarinas de ultra largo alcance (sensibilidad a offset de frecuencia)
- Sistemas de muy bajo consumo (complejidad de FFT)
- Uplink de LTE usa SC-FDMA (single carrier) por eficiencia de potencia

**Evolución histórica de adopción:**
- 1995: DAB (Digital Audio Broadcasting) en Europa - primera aplicación masiva
- 1999: WiFi 802.11a - llevó OFDM al consumidor
- 2002: DVB-T para TV digital terrestre
- 2009: LTE adoptó OFDMA para 4G
- 2019: 5G NR refinó OFDM con numerologías flexibles

### 📐 Fundamentos Teóricos

#### Por Qué OFDM Resuelve Problemas Fundamentales

**1. Problema del Multitrayecto**

En comunicaciones de alta velocidad, el multitrayecto causa ISI (Inter-Symbol Interference):

**Sin OFDM (single carrier):**
- Símbolo corto: Ts < delay spread → ISI severo
- Requiere ecualizador complejo: complejidad O(L²) donde L = longitud del canal
- A 100 Mbps en ambiente urbano: ecualizador de ~100 taps

**Con OFDM:**
- Símbolo largo: Ts >> delay spread
- Prefijo cíclico absorbe multitrayecto
- Ecualización: simple multiplicación por subportadora O(N)

**2. Flexibilidad y Adaptación**

OFDM permite **granularidad fina** en la asignación de recursos:

$$\text{Capacidad total} = \sum_{k=1}^{N} \log_2\left(1 + \text{SNR}_k\right) \times \Delta f$$

Cada subportadora puede tener:
- Modulación diferente (BPSK a 256-QAM)
- Potencia diferente (water-filling)
- Código diferente (rate matching)

**3. Compatibilidad con MIMO**

OFDM convierte el problema MIMO de banda ancha en N problemas MIMO de banda angosta:

$$\mathbf{Y}_k = \mathbf{H}_k \mathbf{X}_k + \mathbf{N}_k$$

Donde cada $\mathbf{H}_k$ es una matriz constante (flat fading) por subportadora.

#### Matemática de las Aplicaciones

**WiFi 802.11ac (Wave 2):**

Parámetros avanzados:
- FFT: hasta 512 puntos (160 MHz)
- Subportadoras de datos: 468
- Modulación máxima: 256-QAM
- MIMO: hasta 8×8
- MU-MIMO: 4 usuarios simultáneos

Capacidad máxima teórica:
$$R_{max} = 8 \text{ streams} \times 468 \text{ sc} \times 8 \text{ bits} \times \frac{5}{6} \text{ coding} \times \frac{1}{4.0 \mu s} = 6.93 \text{ Gbps}$$

**LTE Advanced (Release 10):**

Agregación de portadoras:
- Hasta 5 portadoras de 20 MHz = 100 MHz total
- 6000 subportadoras activas totales
- MIMO 8×8 en downlink

$$R_{peak} = 6000 \times 15 \text{ kHz} \times 6 \text{ bits} \times 8 \text{ layers} = 4.32 \text{ Gbps}$$

### 🔬 Intuición y Analogías

**Analogía principal: El sistema de autopistas urbano**

Imagina el espectro como una autopista:

**Single carrier (tradicional)** = Una autopista de un solo carril muy ancho:
- Si hay un accidente (interferencia), todo el tráfico se detiene
- Difícil de gestionar a alta velocidad
- Un solo vehículo grande y rápido

**OFDM** = Múltiples carriles paralelos:
- Si un carril tiene problemas, los otros siguen funcionando
- Cada carril puede tener límite de velocidad diferente
- Gestión independiente por carril
- El prefijo cíclico es como el espacio de seguridad entre vehículos

**Intuición del éxito comercial:**

OFDM es como LEGO™ para comunicaciones:
- **Bloques básicos** (subportadoras) que se pueden combinar flexiblemente
- **Escalable**: usa más o menos bloques según necesites
- **Adaptable**: cambia la configuración sin cambiar la arquitectura
- **Estándar**: los mismos bloques funcionan en diferentes sistemas

### 💡 Ejemplos Prácticos

#### Ejemplo 1: WiFi 6 (802.11ax) - Última Generación

**Situación:** Análisis de mejoras en WiFi 6 vs WiFi 5

**Especificaciones comparativas:**

| Parámetro | WiFi 5 (802.11ac) | WiFi 6 (802.11ax) | Mejora |
|-----------|------------------|-------------------|---------|
| Subportadoras (20 MHz) | 64 | 256 | 4× |
| Espaciado Δf | 312.5 kHz | 78.125 kHz | 1/4 |
| Duración símbolo | 3.2 μs | 12.8 μs | 4× |
| Modulación máxima | 256-QAM | 1024-QAM | +25% bits |
| OFDMA multiusuario | No | Sí | Nuevo |
| Eficiencia espectral | ~7.5 bps/Hz | ~9.6 bps/Hz | +28% |

**Cálculo de mejora en latencia con OFDMA:**

Sin OFDMA (WiFi 5):
- Usuario debe esperar su turno completo
- Latencia promedio = N × tiempo_trama / 2

Con OFDMA (WiFi 6):
- Múltiples usuarios transmiten simultáneamente
- Latencia = tiempo_trama / usuarios_paralelos

Mejora típica: 75% reducción en latencia para IoT

---

#### Ejemplo 2: LTE vs 5G NR - Evolución de OFDM

**Contexto:** Cómo 5G mejoró OFDM para nuevos casos de uso

**Numerologías flexibles en 5G:**

| μ | Δf (kHz) | Ts (μs) | CP (μs) | Caso de uso |
|---|----------|---------|---------|--------------|
| 0 | 15 | 66.7 | 4.7 | Cobertura amplia |
| 1 | 30 | 33.3 | 2.3 | Estándar |
| 2 | 60 | 16.7 | 1.2 | URLLC (baja latencia) |
| 3 | 120 | 8.3 | 0.59 | mmWave |
| 4 | 240 | 4.2 | 0.29 | mmWave indoor |

**Ventaja de numerología flexible:**
- Adapta OFDM a diferentes escenarios
- Trade-off latencia vs cobertura
- Coexistencia de servicios (eMBB, URLLC, mMTC)

**Ejemplo de slot 5G con mixed numerology:**
```
Frecuencia
    ↑
    |[-- eMBB: μ=1, video streaming --]
    |[URLLC μ=2][URLLC μ=2]  <- Baja latencia
    |[-- mMTC: μ=0, sensores IoT -----]
    |________________________________> Tiempo
```

---

#### Ejemplo 3: DVB-T2 para TV Digital

**Aplicación:** Broadcast de TV terrestre con OFDM

**Parámetros DVB-T2 (modo 32K):**

| Parámetro | Valor | Propósito |
|-----------|-------|-----------|
| Tamaño FFT | 32768 | Ultra alta resolución |
| Portadoras útiles | 27841 | Máxima capacidad |
| Duración útil | 3.584 ms | Símbolos muy largos |
| CP opciones | 1/128 a 19/128 | Flexible según terreno |
| Pilotos | ~8% | Estimación de canal |
| Modulación | QPSK a 256-QAM | Adaptable a SNR |
| FEC | LDPC + BCH | Cerca de Shannon |

**Cálculo de cobertura (Single Frequency Network):**

Con CP = 532 μs (19/256):
- Distancia máxima entre transmisores = c × TCP = 3×10⁸ × 532×10⁻⁶ = 159 km
- Permite SFN (Single Frequency Network) nacional
- Todos los transmisores en misma frecuencia

**Ventaja sobre analógico:**
- 6-8 canales HD en espectro de 1 canal analógico
- Recepción móvil posible
- Servicios interactivos (HbbTV)

### 🔗 Conexiones con Otros Conceptos

#### Evolución y Competencia Tecnológica
- **CDMA → OFDM**: 3G usó CDMA, 4G cambió a OFDM (mejor para datos)
- **SC-FDMA**: Variante single-carrier para uplink LTE (mejor PAPR)
- **FBMC**: Filter Bank Multi-Carrier - posible sucesor de OFDM
- **OTFS**: Orthogonal Time Frequency Space - para alta movilidad

#### Tecnologías Complementarias
1. **MIMO + OFDM**: multiplicación de capacidad
2. **Beamforming + OFDM**: direccionalidad por subportadora
3. **Carrier Aggregation**: múltiples bandas OFDM
4. **CoMP**: Coordinated MultiPoint con OFDM

#### Métricas de Rendimiento
1. **Eficiencia espectral**: bits/s/Hz alcanzables
2. **PAPR**: ratio pico a promedio de potencia
3. **Complejidad**: operaciones por símbolo
4. **Flexibilidad**: adaptación a diferentes canales

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- Por qué cada aplicación eligió OFDM sobre alternativas
- Trade-offs específicos de cada estándar
- Cómo los parámetros OFDM se adaptan al caso de uso
- Limitaciones de OFDM y dónde no es óptimo

#### Tipos de problemas típicos
1. **Diseño de sistema**: Elegir parámetros OFDM para aplicación específica
   - Estrategia: comenzar con delay spread y coherence time del canal

2. **Comparación de estándares**: Analizar por qué WiFi y LTE usan parámetros diferentes
   - Estrategia: considerar ambiente (indoor vs outdoor) y movilidad

3. **Cálculo de capacidad**: Throughput máximo en escenario dado
   - Estrategia: considerar overhead (CP, pilotos) y limitaciones prácticas

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Asumir que OFDM es siempre la mejor opción**
- Por qué ocurre: su popularidad hace pensar que es universal
- Realidad: PAPR lo hace inadecuado para transmisores de potencia limitada
- Ejemplo: uplink celular usa SC-FDMA, no OFDM puro

❌ **Error #2: Ignorar overhead en cálculos de capacidad**
- Por qué ocurre: fórmulas teóricas no incluyen overhead
- Realidad: CP, pilotos, preámbulos reducen throughput 20-30%
- Siempre incluir: eficiencia = datos/(datos + overhead)

❌ **Error #3: Confundir OFDM con OFDMA**
- OFDM: técnica de modulación (single user)
- OFDMA: técnica de acceso múltiple (multiuser)
- Diferencia: OFDMA asigna subconjuntos de subportadoras a diferentes usuarios

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Throughput WiFi: R = Nsc × bits/symbol × code_rate / Tsymbol
Throughput LTE: R = PRB × 12 × 14 × bits × code_rate / 1ms
Eficiencia DVB-T2: η = (útiles/total) × (1 - CP_ratio) × code_rate
PAPR (dB): 10 log₁₀(N) donde N = número de subportadoras
```

#### Conceptos Fundamentales
- ✓ **Ubicuidad justificada**: OFDM domina porque resuelve multitrayecto eficientemente
- ✓ **Flexibilidad es clave**: adaptación por subportadora es única
- ✓ **PAPR es el precio**: eficiencia espectral vs eficiencia de potencia
- ✓ **FFT lo hace práctico**: sin FFT, OFDM sería imposible

#### Reglas Mnemotécnicas
- 🧠 **WiFi**: "Wireless Fidelity usa OFDM Inteligentemente"
- 🧠 **LTE**: "Long Term Evolution = OFDM Adaptation"
- 🧠 **DVB**: "Digital Video Broadcasting = OFDM para TV"

#### Tabla Resumen de Aplicaciones
| Sistema | Band | FFT Size | Δf | Uso Principal |
|---------|------|----------|-----|--------------|
| WiFi 6 | 2.4/5/6 GHz | 256-2048 | 78.125 kHz | WLAN |
| LTE | 700 MHz-3.5 GHz | 128-2048 | 15 kHz | Celular |
| 5G NR | 450 MHz-52 GHz | 128-4096 | 15-240 kHz | Todo |
| DVB-T2 | VHF/UHF | 1K-32K | Variable | TV |
| DAB | VHF Band III | 256-2048 | 1-8 kHz | Radio |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Estándares**: IEEE 802.11ax-2021, 3GPP TS 38.211 (5G NR)
- **Libros**: Andrews "Fundamentals of WiMAX" - excelente en OFDMA
- **White papers**: Qualcomm y Huawei sobre evolución de OFDM
- **Cursos online**: "Wireless Communications" de Goldsmith

#### Temas Avanzados
1. **OFDM Indexing**: usar índices de subportadoras para datos
2. **Sparse OFDM**: no usar todas las subportadoras
3. **Filtered OFDM**: reducir emisiones fuera de banda
4. **Full-duplex OFDM**: transmitir y recibir simultáneamente

#### Preguntas para Reflexionar
- ¿Por qué el uplink celular evita OFDM puro?
- ¿Cómo afectará 6G a la evolución de OFDM?
- ¿Puede OFDM manejar canales doblemente selectivos (tiempo y frecuencia)?
- ¿Qué tecnología podría reemplazar a OFDM en el futuro?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 35 minutos
**Prerequisitos críticos**: OFDM básico (Carta 53), modulación digital
**Tags**: `#ofdm-applications` `#wifi` `#lte` `#5g` `#dvb` `#standards`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*