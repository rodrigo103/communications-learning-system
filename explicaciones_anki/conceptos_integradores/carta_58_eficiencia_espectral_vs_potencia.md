# Carta 58: Eficiencia Espectral vs Eficiencia de Potencia - El Trade-off Fundamental del Diseño

> **Conceptos Integradores**: Diseño de Sistemas, Optimización de Recursos

---

## 🎯 Pregunta

Explique el concepto de eficiencia espectral y eficiencia de potencia, y el trade-off entre ambas.

---

## 📝 Respuesta Breve (de la carta original)

**Eficiencia Espectral** (η_B):
$$\eta_B = \frac{R_b}{B} \text{ bits/s/Hz}$$
Mide cuánta información se transmite por unidad de ancho de banda.

**Eficiencia de Potencia** (η_P):
Medida por Eb/N0 requerido para cierto BER.
- Menor Eb/N0 → más eficiente en potencia

**Trade-off fundamental**:
- **Alta η_B** (QAM alto orden): requiere alta SNR → baja η_P
  - Ejemplo: 256-QAM: 8 bits/s/Hz, pero requiere Eb/N0 alto
- **Alta η_P** (spread spectrum, codificación): usa más BW → baja η_B
  - Ejemplo: GPS: robusta pero poca capacidad

**Aplicaciones**:
- Satélite (potencia limitada): priorizar η_P
- Fibra óptica (potencia abundante): priorizar η_B
- Sistemas adaptativos (LTE, 5G): varían según condiciones

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El trade-off entre eficiencia espectral y eficiencia de potencia es **la decisión de diseño más fundamental en comunicaciones modernas**. Este balance determina todo, desde la elección de modulación hasta la arquitectura completa del sistema. Es el dilema eterno: ¿queremos transmitir más información en menos espectro, o queremos usar menos energía por bit?

**¿Por qué es importante este concepto?** Porque los recursos en comunicaciones son finitos y costosos. El espectro radioeléctrico es un recurso natural limitado con valor de miles de millones de dólares en subastas. La potencia determina la vida de la batería en dispositivos móviles y el costo operativo en sistemas satelitales. Ningún diseñador puede maximizar ambas eficiencias simultáneamente.

**¿Dónde se aplica?** Este trade-off aparece en cada decisión de diseño:
- **5G**: Usa modulación adaptativa para balancear dinámicamente ambas eficiencias
- **Satélites**: Priorizan eficiencia de potencia debido a paneles solares limitados
- **Cable/Fibra**: Priorizan eficiencia espectral porque la potencia es relativamente barata
- **IoT**: Dispositivos con batería priorizan eficiencia de potencia para durar años

**Historia y evolución**: En los primeros días de la radio (1920s-1960s), el espectro parecía infinito y la preocupación era la potencia. Con la explosión de servicios inalámbricos (1980s-presente), el espectro se volvió el recurso más escaso, llevando a un énfasis en eficiencia espectral. Hoy, con billones de dispositivos IoT, volvemos a preocuparnos por la eficiencia energética.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Modulación digital y constelaciones
- Relación señal-ruido y BER
- Teorema de Shannon
- Eb/N0 y métricas de desempeño
- Codificación de canal

#### Desarrollo Paso a Paso

**Paso 1: Definición Formal de Eficiencia Espectral**

La eficiencia espectral mide cuántos bits de información podemos transmitir por cada Hz de ancho de banda:

$$\eta_B = \frac{R_b}{B} \text{ [bits/s/Hz]}$$

donde:
- $R_b$ = Tasa de bits de información (bits/s)
- $B$ = Ancho de banda ocupado (Hz)

Para modulación M-aria con tasa de símbolos $R_s$:
$$\eta_B = \frac{R_s \log_2(M)}{B}$$

En el caso ideal donde $B = R_s$:
$$\eta_B = \log_2(M)$$

**Paso 2: Definición de Eficiencia de Potencia**

La eficiencia de potencia no tiene una única definición, pero se caracteriza por:

1. **Eb/N0 requerido para cierto BER**:
   - Menor Eb/N0 → Mayor eficiencia de potencia

2. **Distancia al límite de Shannon**:
   $$\text{Gap to Shannon} = (E_b/N_0)_{\text{actual}} - (E_b/N_0)_{\text{Shannon}}$$

3. **Potencia transmitida por bit útil**:
   $$\eta_P = \frac{\text{Bits de información transmitidos}}{\text{Energía total consumida}}$$

**Paso 3: El Trade-off Fundamental**

El teorema de Shannon establece el límite:
$$C = B \log_2(1 + \text{SNR})$$

Reordenando para eficiencia espectral máxima:
$$\eta_{B,max} = \log_2(1 + \text{SNR})$$

Y para el Eb/N0 mínimo requerido:
$$\left(\frac{E_b}{N_0}\right)_{min} = \frac{2^{\eta_B} - 1}{\eta_B}$$

#### Derivación Matemática del Trade-off

**Partiendo de la capacidad de Shannon:**

Para un sistema operando a capacidad con eficiencia espectral $\eta_B = C/B$:

$$\eta_B = \log_2(1 + \text{SNR})$$

Como SNR = $(E_b/N_0) \cdot \eta_B$ (de la carta anterior):

$$\eta_B = \log_2\left(1 + \frac{E_b}{N_0} \cdot \eta_B\right)$$

Despejando Eb/N0:
$$\frac{E_b}{N_0} = \frac{2^{\eta_B} - 1}{\eta_B}$$

**Análisis de los extremos:**

1. **Límite de baja eficiencia espectral** ($\eta_B \to 0$):
   $$\lim_{\eta_B \to 0} \frac{E_b}{N_0} = \ln(2) = -1.59 \text{ dB}$$

2. **Límite de alta eficiencia espectral** ($\eta_B \to \infty$):
   $$\lim_{\eta_B \to \infty} \frac{E_b}{N_0} = \lim_{\eta_B \to \infty} \frac{2^{\eta_B}}{\eta_B} = \infty$$

**Resultado clave:**
$$\boxed{\text{Alta } \eta_B \Leftrightarrow \text{Alto } E_b/N_0 \text{ requerido} \Leftrightarrow \text{Baja } \eta_P}$$

### 🔬 Intuición y Analogías

**Analogía principal: El Dilema del Empaque**

Imagina que debes enviar paquetes:
- **Eficiencia espectral** = ¿Cuántos objetos caben en cada caja?
- **Eficiencia de potencia** = ¿Cuán fácil es desempacar sin errores?

Si empacas muy denso (alta η_B):
- ✓ Necesitas menos cajas (menos ancho de banda)
- ✗ Es más difícil desempacar sin confundirse (requiere más SNR)

Si empacas con mucho espacio (baja η_B):
- ✓ Fácil identificar cada objeto (bajo Eb/N0 requerido)
- ✗ Necesitas muchas cajas (más ancho de banda)

**Intuición física del trade-off:**

En el espacio de señales (constelación):
- **Alta η_B**: Muchos puntos apretados → fácil confundirlos con ruido
- **Baja η_B**: Pocos puntos separados → difícil confundirlos

Es como escribir en una hoja de papel:
- Letra pequeña y apretada: más información por página pero más difícil de leer
- Letra grande y espaciada: menos información pero más legible

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Comparación de Esquemas de Modulación

**Situación:** Diseñar enlace con BER objetivo = 10⁻⁶

**Comparación de opciones:**

| Modulación | η_B (bits/s/Hz) | Eb/N0 req. (dB) | Distancia entre símbolos | Aplicación típica |
|------------|-----------------|-----------------|--------------------------|-------------------|
| BPSK | 1 | 10.5 | 2√Eb | Enlaces robustos |
| QPSK | 2 | 10.5 | √(2Eb) | Balance |
| 16-QAM | 4 | 14.5 | √(Eb/2.5) | Cable/fibra |
| 64-QAM | 6 | 18.5 | √(Eb/10.5) | WiFi cercano |
| 256-QAM | 8 | 23 | √(Eb/42.5) | Cable DOCSIS |

**Análisis del trade-off:**
- BPSK → 256-QAM: η_B aumenta 8×
- Costo: Eb/N0 aumenta 12.5 dB (factor 18×)
- **Conclusión**: Ganar 1 bit/s/Hz adicional cuesta cada vez más potencia

---

#### Ejemplo 2: Diseño de Sistema Satelital vs Terrestre

**Escenario A: Satélite GEO**
- Potencia solar limitada: 100W
- Espectro disponible: 500 MHz
- Distancia: 36,000 km

**Decisión de diseño:**
```
Prioridad: Eficiencia de Potencia
Solución: QPSK con FEC fuerte
- η_B = 1.5 bits/s/Hz (con codificación)
- Eb/N0 efectivo = 3 dB
- Capacidad total = 750 Mbps
```

**Escenario B: Enlace de fibra metropolitano**
- Potencia disponible: Sin restricción práctica
- Espectro óptico: Limitado a banda C (4 THz)
- Distancia: 100 km

**Decisión de diseño:**
```
Prioridad: Eficiencia Espectral
Solución: 256-QAM con DSP avanzado
- η_B = 8 bits/s/Hz
- Eb/N0 requerido = 25 dB (aceptable con amplificadores)
- Capacidad total = 32 Tbps
```

---

#### Ejemplo 3: Sistema Adaptativo 5G

**Contexto:** Estación base 5G sirviendo usuarios a diferentes distancias

**Estrategia de modulación y codificación adaptativa (AMC):**

| Distancia | SNR disponible | Esquema seleccionado | η_B | Eb/N0 usado | Throughput |
|-----------|---------------|---------------------|-----|-------------|------------|
| 0-100m | 30 dB | 256-QAM 5/6 | 6.67 | 20 dB | 667 Mbps |
| 100-500m | 20 dB | 64-QAM 3/4 | 4.5 | 15 dB | 450 Mbps |
| 500-1km | 15 dB | 16-QAM 2/3 | 2.67 | 12 dB | 267 Mbps |
| 1-2km | 10 dB | QPSK 1/2 | 1 | 8 dB | 100 Mbps |
| >2km | 5 dB | QPSK 1/3 | 0.67 | 4 dB | 67 Mbps |

**Observación clave:** El sistema automáticamente balancea η_B vs η_P según las condiciones del canal.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados del Curso
- **Teorema de Shannon** (Carta 45): Define el límite teórico del trade-off
- **Constelaciones** (Carta 28): Visualizan el trade-off en el plano I-Q
- **Codificación** (Carta 48): Mejora η_P a costa de η_B
- **OFDM** (Carta 53): Permite ajustar el trade-off por subportadora
- **Spread Spectrum** (Carta 50): Ejemplo extremo de baja η_B, alta η_P

#### El Trade-off en Diferentes Dominios

1. **Dominio de Frecuencia**:
   - Alta η_B: Espectro compacto, lóbulos laterales mínimos
   - Baja η_B: Espectro expandido, robustez a interferencia

2. **Dominio del Tiempo**:
   - Alta η_B: Símbolos cortos, sensible a ISI
   - Baja η_B: Símbolos largos, robusto a multitrayecto

3. **Dominio del Código**:
   - Códigos de alta tasa: Buena η_B, peor η_P
   - Códigos de baja tasa: Mala η_B, mejor η_P

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- No existe un esquema óptimo universal: depende de los recursos disponibles
- El trade-off es fundamental, no tecnológico (Shannon lo impone)
- Capacidad de elegir el punto de operación correcto para cada aplicación
- Comprensión de por qué diferentes sistemas hacen diferentes elecciones

#### Tipos de problemas típicos
1. **Selección de modulación**: Dados requisitos de BER y recursos, elegir esquema óptimo
2. **Análisis de trade-off**: Calcular η_B y Eb/N0 para diferentes opciones
3. **Diseño de sistema**: Justificar elección basada en restricciones
4. **Comparación**: Evaluar diferentes sistemas en términos de ambas eficiencias

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Pensar que existe un "mejor" punto de operación**
- Por qué ocurre: Buscar una solución única
- Realidad: El óptimo depende completamente de las restricciones
- Ejemplo: BPSK es "mejor" para satélite, 256-QAM es "mejor" para cable

❌ **Error #2: Ignorar el impacto de la codificación**
- Por qué ocurre: Considerar solo la modulación
- Realidad: FEC cambia significativamente el trade-off
- Solución: Siempre considerar tasa de código efectiva

❌ **Error #3: Comparar eficiencias de sistemas en diferentes condiciones**
- Confusión: Comparar η_B de WiFi con satélite
- Problema: Operan en puntos muy diferentes del trade-off
- Correcto: Comparar sistemas con restricciones similares

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Eficiencia espectral: η_B = Rb/B = log₂(M) (ideal)
Relación de Shannon: Eb/N0_min = (2^η_B - 1)/η_B
Límite η_B → 0: Eb/N0 → ln(2) = -1.59 dB
Con codificación: η_B_efectiva = η_B_mod × R_código
```

#### Conceptos Fundamentales
- ✓ **Trade-off inevitable**: No se puede maximizar ambas eficiencias
- ✓ **Recurso escaso manda**: Optimizar según qué es más limitado
- ✓ **Adaptación es clave**: Sistemas modernos ajustan dinámicamente
- ✓ **Codificación media**: Permite moverse en la curva del trade-off

#### Tabla de Aplicaciones y Prioridades
| Aplicación | Recurso Limitado | Prioridad | Solución Típica |
|------------|------------------|-----------|-----------------|
| Espacio profundo | Potencia extrema | η_P máxima | BPSK + códigos potentes |
| Satélite broadcast | Potencia | η_P > η_B | QPSK/8PSK + FEC |
| Celular (borde celda) | Potencia | η_P | QPSK con spreading |
| Celular (centro) | Espectro | η_B | 256-QAM |
| WiFi | Variable | Adaptativa | BPSK a 1024-QAM |
| Fibra óptica | Espectro | η_B máxima | QAM alto orden |
| IoT sensores | Batería | η_P extrema | LoRa, NB-IoT |
| TV Cable | Espectro | η_B | 256/1024-QAM |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Análisis fundamental**: Biglieri et al. "Digital Transmission over Fading Channels"
- **Diseño práctico**: Goldsmith "Wireless Communications" Cap. 6
- **Codificación y trade-off**: Lin & Costello "Error Control Coding" Cap. 1

#### Temas Avanzados Relacionados
1. Región de capacidad en sistemas multi-usuario
2. Trade-off con múltiples antenas (MIMO)
3. Eficiencia energética total (incluyendo circuitos)
4. Optimización cross-layer del trade-off

#### Preguntas para Reflexionar
- ¿Cómo cambiaría el diseño de WiFi si el espectro fuera gratis pero la batería costara $1000/Wh?
- ¿Por qué los sistemas ópticos pueden usar modulación tan densa mientras que los satelitales no?
- Si pudieras diseñar un nuevo espectro solo para IoT, ¿qué trade-off elegirías?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4 estrellas - Concepto de diseño crucial)
**Tiempo de estudio sugerido**: 40 minutos
**Prerequisitos críticos**: Modulación digital, Shannon, Eb/N0, codificación
**Tags**: `#eficiencia` `#trade-off` `#diseño` `#optimizacion` `#recursos`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*