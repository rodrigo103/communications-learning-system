# Carta 26: TDM en Sistemas PCM - Multiplexación Temporal Digital

> **Unidad 5**: Modulación de Pulsos

---

## 🎯 Pregunta

¿Qué es TDM (Time Division Multiplexing) y cómo se implementa en sistemas PCM?

---

## 📝 Respuesta Breve (de la carta original)

**TDM** permite transmitir múltiples señales por un canal compartiendo el tiempo.

**Implementación en PCM**:
1. Cada canal se muestrea secuencialmente (muestreo entrelazado)
2. Muestras se cuantifican y codifican
3. Se forma una **trama** con:
   - Bits de cada canal
   - Bits de sincronización (frame alignment)
   - Posible señalización

**Ejemplo**: Sistema T1 (USA)
- 24 canales de voz
- 8 bits/muestra, 8000 muestras/s por canal
- Tasa: 1.544 Mbps (incluye overhead)

**Ventajas**: eficiente, flexible, regeneración digital
**Jerarquías**: E1, T1, PDH, SDH

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

**Time Division Multiplexing (TDM)** en sistemas PCM representa uno de los mayores avances en telecomunicaciones del siglo XX, permitiendo que múltiples conversaciones telefónicas compartan un mismo medio de transmisión. Esta tecnología transformó las redes telefónicas mundiales de analógicas a digitales, multiplicando la capacidad y mejorando la calidad.

**¿Por qué es importante este concepto?** TDM-PCM es la base de toda la infraestructura telefónica digital mundial. Desde los años 1960s hasta hoy, billones de llamadas han sido transportadas usando estos principios. Aunque VoIP está reemplazando la telefonía tradicional, TDM sigue siendo fundamental en backbones de telecomunicaciones, y sus principios se aplican en 4G/5G, fibra óptica y sistemas satelitales.

**¿Dónde se aplica?**
- **Telefonía digital**: Toda la red PSTN (Public Switched Telephone Network)
- **Enlaces troncales**: Conexiones entre centrales telefónicas
- **Acceso celular**: Backhaul de estaciones base
- **Sistemas empresariales**: PBX digitales, enlaces E1/T1
- **Transmisión de datos**: Frame relay, ATM (histórico)
- **Fibra óptica**: SDH/SONET para transporte de alta capacidad

**Historia relevante:** El sistema T1 fue desarrollado por Bell Labs en 1962 para conectar oficinas centrales telefónicas en Chicago. Fue el primer sistema de transmisión digital comercial, revolucionando las telecomunicaciones. Europa desarrolló el estándar E1 poco después con 32 canales. Estos sistemas evolucionaron a las jerarquías PDH (Plesiochronous Digital Hierarchy) y luego SDH/SONET en los 1980s.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **PCM básico**: digitalización de señales analógicas
- **Teorema del muestreo**: sincronización de muestras
- **Sincronización**: alineación temporal entre transmisor y receptor
- **Multiplexación**: compartir recursos entre múltiples usuarios

#### Desarrollo Paso a Paso

**Paso 1: Principio Fundamental de TDM**

TDM divide el tiempo en **ranuras temporales** (time slots) recurrentes:

- Cada canal tiene asignada una ranura específica
- Las ranuras se repiten cíclicamente formando **tramas** (frames)
- Período de trama = 1/frecuencia de muestreo = 125 μs (para voz a 8 kHz)

Matemáticamente:
$$T_{frame} = \frac{1}{f_s} = \frac{1}{8000} = 125 \text{ μs}$$

**Paso 2: Proceso de Multiplexación PCM-TDM**

Para N canales de voz:

1. **Muestreo secuencial**:
   - Canal 1 → muestra → codifica (n bits)
   - Canal 2 → muestra → codifica (n bits)
   - ...
   - Canal N → muestra → codifica (n bits)

2. **Formación de trama**:
   $$\text{Trama} = [Sync][Ch1][Ch2]...[ChN][Señalización]$$

3. **Tasa de bits agregada**:
   $$R_{total} = N \cdot n \cdot f_s + R_{overhead}$$

**Paso 3: Sincronización - El Desafío Crítico**

La sincronización es vital para TDM:

- **Sincronización de bit**: identificar límites de bits
- **Sincronización de byte**: identificar bytes dentro de ranura
- **Sincronización de trama**: identificar inicio de trama
- **Sincronización de multitrama**: para señalización

Se logra mediante:
- **Patrones de sincronización**: secuencias únicas en la trama
- **Bits de alineación de trama** (Frame Alignment Word - FAW)
- **Verificación continua**: pérdida y recuperación de sincronismo

**Paso 4: Jerarquías Digitales**

Los sistemas TDM se organizan en jerarquías:

**PDH (Plesiochronous Digital Hierarchy):**
- Nivel 1: E1 (2.048 Mbps) o T1 (1.544 Mbps)
- Nivel 2: E2 (8.448 Mbps) o T2 (6.312 Mbps)
- Nivel 3: E3 (34.368 Mbps) o T3 (44.736 Mbps)
- Cada nivel multiplexa 4 del nivel inferior (típicamente)

**SDH/SONET (Synchronous):**
- STM-1 (155.52 Mbps)
- STM-4 (622.08 Mbps)
- STM-16 (2.5 Gbps)
- Multiplexación más eficiente y flexible

#### Derivación Matemática

**Sistema T1 Norteamericano:**

Parámetros:
- 24 canales de voz
- 8 bits/muestra (7 datos + 1 señalización cada 6 tramas)
- 8000 tramas/segundo
- 1 bit de sincronización por trama

Cálculo de tasa:
$$R_{T1} = 24 \text{ canales} \times 8 \text{ bits} \times 8000 \text{ Hz} + 1 \text{ bit} \times 8000 \text{ Hz}$$
$$R_{T1} = 1,536,000 + 8,000 = 1,544,000 \text{ bps} = 1.544 \text{ Mbps}$$

**Sistema E1 Europeo:**

Parámetros:
- 32 ranuras de tiempo (time slots)
- 30 canales de voz + 1 sincronización + 1 señalización
- 8 bits/ranura
- 8000 tramas/segundo

Cálculo:
$$R_{E1} = 32 \text{ ranuras} \times 8 \text{ bits} \times 8000 \text{ Hz}$$
$$R_{E1} = 256 \times 8000 = 2,048,000 \text{ bps} = 2.048 \text{ Mbps}$$

**Eficiencia espectral:**

Para E1 en cable coaxial con codificación HDB3:
$$\eta = \frac{30 \text{ canales} \times 64 \text{ kbps}}{BW_{coax}} = \frac{1.92 \text{ Mbps}}{1.5 \text{ MHz}} \approx 1.28 \text{ bits/s/Hz}$$

### 🔬 Intuición y Analogías

**Analogía principal:**
TDM es como un **carrusel o tren de tiempo compartido**. Imagina un tren circular con 24 vagones (T1) que pasa por cada estación (canal) cada 125 μs:
- Cada estación puede subir exactamente un paquete (8 bits) a su vagón asignado
- El tren completa una vuelta en 125 μs
- En el destino, cada estación recoge su paquete del vagón correspondiente
- La sincronización asegura que todos sepan qué vagón les corresponde

**Intuición física:**
TDM es como **proyectar múltiples películas con un solo proyector** usando un disco giratorio con sectores. Cada sector proyecta un fotograma de una película diferente, pero gira tan rápido que cada pantalla ve su película completa sin interrupción.

**Visualización:**
Imagina el flujo de bits como una autopista donde cada carril (ranura temporal) está reservado para un usuario específico. Los carriles se asignan cíclicamente, y todos viajan a la misma velocidad. La sincronización es como las líneas que separan los carriles - críticas para mantener el orden.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Diseño de Enlace E1 para Oficina

**Situación:** Conectar oficina remota con 25 líneas telefónicas a central.

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Líneas telefónicas | 25 | canales |
| Calidad requerida | G.711 | 64 kbps/canal |
| Distancia | 5 | km |
| Medio | Cable coaxial | - |

**Solución paso a paso:**

1. **Capacidad de E1:**
   - 30 canales útiles de voz
   - 25 canales necesarios < 30 disponibles ✓

2. **Estructura de trama E1:**
   ```
   TS0: Sincronización y alarmas
   TS1-15: Canales 1-15 (voz)
   TS16: Señalización (CAS o CCS)
   TS17-31: Canales 16-30 (voz)
   ```
   Usaremos TS1-TS25 para las 25 líneas

3. **Tasa de bits:**
   $$R = 32 \times 8 \times 8000 = 2.048 \text{ Mbps}$$

4. **Tiempo por canal:**
   $$t_{slot} = \frac{125 \mu s}{32} = 3.906 \text{ μs}$$

**Resultado:**
$$\boxed{\text{Un enlace E1 es suficiente con 5 canales de reserva}}$$

---

#### Ejemplo 2: Sistema T1 en Empresa Real

**Contexto:** Call center usando T1 para conectar PBX a PSTN.

**Configuración típica T1 (Super Frame - SF):**

```
Estructura de Super Frame (12 tramas):
- Tramas 1-12: 193 bits cada una
- Total: 2316 bits en 1.5 ms

Trama individual (193 bits):
[F][Canal 1: 8 bits][Canal 2: 8 bits]...[Canal 24: 8 bits]

F = bit de framing (patrón: 100011011100 en 12 tramas)
```

**Procesamiento de llamada entrante:**

1. **Llegada de llamada** (Canal 5):
   - Tiempo hasta ranura 5: 4 × 8 bits × 0.648 μs = 20.7 μs

2. **Digitalización de "Hello":**
   - Muestreo: 8000 Hz
   - Cuantificación: μ-law, 8 bits
   - Código típico: 11011010 (nivel +0.6V)

3. **Transmisión en trama n:**
   - Posición en trama: bits 41-48
   - Tiempo absoluto: (n × 125 μs) + 26.8 μs

4. **Señalización (robbed bit):**
   - Tramas 6 y 12: bit 8 usado para señalización
   - Estado on-hook/off-hook transmitido

---

#### Ejemplo 3: Análisis de Sincronización y Errores

**Caso: Pérdida y recuperación de sincronización en E1**

**Escenario de pérdida:**
1. **Errores de bit acumulados**: BER > 10⁻³
2. **Pérdida de patrón FAW** (Frame Alignment Word)
3. **Alarma**: "Loss of Frame" (LOF)

**Proceso de recuperación:**

1. **Búsqueda de FAW** (0011011 en TS0):
   ```
   Estado 1: Buscar patrón bit a bit
   Estado 2: Encontrado - verificar en siguiente trama
   Estado 3: Confirmado - verificar N tramas consecutivas
   Estado 4: Sincronizado - operación normal
   ```

2. **Tiempo de recuperación:**
   - Mejor caso: 2 tramas (250 μs)
   - Caso típico: 5-10 tramas (0.625-1.25 ms)
   - Peor caso: 50 tramas (6.25 ms)

3. **Impacto en servicio:**
   - Audio: click o silencio breve
   - Datos: retransmisión de paquetes
   - Señalización: posible caída de llamada

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **PCM** (Carta 23): TDM multiplexa canales PCM individuales
- **Companding** (Carta 24): Cada canal TDM puede usar μ-law/A-law
- **Modulación Delta** (Carta 25): TDM también puede multiplexar canales DM/ADM
- **Teoría de colas**: Análisis de tráfico en sistemas TDM
- **OFDM** (Unidad 10): Multiplexación en frecuencia vs tiempo

#### Dependencias (lo que necesitas saber primero)
1. **Digitalización PCM** → Qué se está multiplexando
2. **Sincronización de sistemas** → Crítico para demultiplexar
3. **Codificación de línea** → HDB3, AMI para transmisión

#### Aplicaciones Posteriores (dónde usarás esto)
1. **VoIP/SIP trunking**: Migración de TDM a paquetes
2. **Redes ópticas**: WDM + TDM para máxima capacidad
3. **5G fronthaul**: eCPRI usa principios TDM
4. **Sistemas satelitales**: TDM + FDM para acceso múltiple

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- **Cálculo de tasas**: Derivar tasa total desde parámetros básicos
- **Estructura de trama**: Entender organización temporal
- **Sincronización crítica**: Por qué es vital y cómo se logra
- **Comparación T1/E1**: Diferencias históricas y técnicas
- **Jerarquías digitales**: Cómo se escalan los sistemas

#### Tipos de problemas típicos
1. **Diseño de sistema**: Calcular número de E1/T1 necesarios para N canales
   - Estrategia: Considerar overhead y canales útiles

2. **Análisis de trama**: Identificar posición temporal de canal específico
   - Estrategia: Usar estructura de trama y timing

3. **Cálculo de eficiencia**: Comparar capacidad útil vs total
   - Estrategia: Separar payload de overhead

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Olvidar el overhead de sincronización**
- Por qué ocurre: Focus solo en canales de voz
- Cómo evitarlo: T1 = 193 bits/trama (no 192), E1 = 32 slots (no 30)
- Impacto: Cálculo erróneo de capacidad

❌ **Error #2: Confundir T1 y E1**
- Por qué ocurre: Ambos son "primarios" pero incompatibles
- Diferencias clave:
  - T1: 1.544 Mbps, 24 canales, μ-law
  - E1: 2.048 Mbps, 30 canales, A-law
- No son interoperables directamente

❌ **Error #3: Asumir sincronización perfecta**
- Por qué ocurre: Simplificación excesiva
- Realidad: Necesita reloj maestro, distribución, recuperación
- Problema del "clock slip": pérdida de bits por desincronización

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Tasa TDM = N × bits/muestra × fs + overhead
T1: 24 × 8 × 8000 + 8000 = 1.544 Mbps
E1: 32 × 8 × 8000 = 2.048 Mbps
Tiempo de trama = 1/fs = 125 μs (telefonía)
Tiempo por canal = Ttrama/N
```

#### Conceptos Fundamentales
- ✓ **TDM = Time Sharing**: Cada canal tiene su momento exclusivo
- ✓ **Sincronización es crítica**: Sin ella, el sistema colapsa
- ✓ **Overhead inevitable**: 3-10% típico para sync + señalización
- ✓ **Jerarquías multiplexan**: Cada nivel agrupa varios del inferior
- ✓ **125 μs es universal**: Período de trama para voz (8 kHz)

#### Reglas Mnemotécnicas
- 🧠 **"TE unos dos"**: T1 ≈ 1.5 Mbps, E1 ≈ 2 Mbps
- 🧠 **"24 americanos, 30 europeos"**: Canales en T1 vs E1
- 🧠 **"8-8-8"**: 8 bits, 8000 Hz, 8 kHz = fundamentos PCM-TDM
- 🧠 **"PETS"**: PDH→E1→T1→SDH (evolución histórica)

#### Valores Típicos (para referencias rápidas)

| Sistema | Tasa (Mbps) | Canales voz | Región | Codificación línea |
|---------|-------------|-------------|---------|-------------------|
| T1 | 1.544 | 24 | Americas/Japan | AMI, B8ZS |
| E1 | 2.048 | 30 | Europe/World | HDB3 |
| T3 | 44.736 | 672 | Americas | B3ZS |
| E3 | 34.368 | 480 | Europe | HDB3 |
| STM-1 | 155.52 | 1890 | Global | NRZ |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**:
  - Freeman, "Telecommunication System Engineering" - Biblia de TDM
  - ITU-T G.704: Especificación completa de estructuras de trama
- **Estándares clave**:
  - G.703: Características físicas/eléctricas
  - G.704: Estructuras de trama
  - G.706: Procedimientos de alineación
- **Simuladores**: GNS3 con routers Cisco para configurar E1/T1

#### Temas Relacionados para Explorar
1. **Statistical TDM**: Asignación dinámica vs fija
2. **ATM (Asynchronous Transfer Mode)**: Evolución de TDM
3. **MPLS-TP**: TDM sobre redes de paquetes
4. **Circuit Emulation**: TDM sobre Ethernet (CESoP, SAToP)
5. **Time-Sensitive Networking**: TDM moderno para Ethernet industrial

#### Preguntas para Reflexionar
- ¿Por qué 8000 Hz se volvió universal para telefonía?
- ¿Cómo compite TDM con multiplexación estadística de paquetes?
- ¿Por qué T1/E1 siguen usándose cuando hay tecnologías más modernas?
- ¿Podría diseñarse TDM adaptativo que ajuste slots dinámicamente?
- ¿Cómo afecta la latencia de propagación a sistemas TDM satelitales?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 35 minutos
**Prerequisitos críticos**: PCM, sincronización, multiplexación
**Tags**: `#tdm` `#t1` `#e1` `#multiplexacion` `#telefonia-digital` `#pdh`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*