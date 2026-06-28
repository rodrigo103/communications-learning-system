# Carta 40: Parámetros de Comparación de Sistemas de Modulación

> **Unidad 8**: Intercomparación de Sistemas

---

## 🎯 Pregunta

¿Qué parámetros se utilizan para comparar diferentes sistemas de modulación?

---

## 📝 Respuesta Breve (de la carta original)

**Parámetros principales de comparación**:

1. **Eficiencia espectral**: bits/s/Hz
2. **Eficiencia de potencia**: Eb/N0 requerido para cierto BER
3. **Ancho de banda requerido**: vs. tasa de información
4. **SNR de salida**: vs. SNR de entrada
5. **Complejidad**: de implementación
6. **Robustez**: ante ruido, interferencia, desvanecimiento
7. **Inmunidad a no-linealidades**: amplificadores
8. **Sincronización**: requerimientos
9. **Costo**: económico y energético

**Trade-offs clave**:
- Ancho de banda ↔ Potencia (Shannon)
- Complejidad ↔ Desempeño
- Eficiencia espectral ↔ Robustez

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La comparación sistemática de diferentes esquemas de modulación es fundamental en el diseño de sistemas de comunicaciones. En la práctica, no existe una modulación "perfecta" que sea óptima para todas las aplicaciones. En cambio, cada sistema representa un conjunto de compromisos entre múltiples parámetros de desempeño. El ingeniero debe seleccionar la modulación más apropiada basándose en los requisitos específicos del sistema y las restricciones del entorno operativo.

Esta evaluación multidimensional es crítica en aplicaciones modernas como 5G, donde diferentes servicios (video streaming, IoT, comunicaciones de emergencia) requieren diferentes características de desempeño. Por ejemplo, un sistema satelital prioriza la eficiencia de potencia debido a limitaciones energéticas, mientras que una red de fibra óptica puede priorizar la eficiencia espectral dado que la potencia es abundante.

La evolución histórica de los sistemas de comunicación refleja cómo estos parámetros han ganado o perdido importancia según la tecnología disponible. En los años 1920s, la simplicidad del receptor AM era primordial. Hoy, con procesadores digitales baratos, la complejidad es menos restrictiva, permitiendo esquemas sofisticados como OFDM con QAM adaptativo.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Teorema de Shannon-Hartley (capacidad del canal)
- Relación señal-ruido (SNR)
- Probabilidad de error de bit (BER)
- Densidad espectral de potencia
- Sistemas lineales y no lineales

#### Desarrollo Paso a Paso

**Paso 1: Marco de Evaluación Fundamental**

Todo sistema de comunicación debe satisfacer tres requisitos básicos:
1. **Fidelidad**: transmitir información con mínimo error
2. **Eficiencia**: usar recursos (espectro, potencia) óptimamente
3. **Viabilidad**: ser implementable técnica y económicamente

**Paso 2: Parámetros de Desempeño**

Los parámetros de comparación se clasifican en categorías:

**A. Eficiencia de Recursos**
- **Eficiencia Espectral** (η_B):
  $$\eta_B = \frac{R_b}{B} \text{ [bits/s/Hz]}$$
  Mide cuánta información se transmite por unidad de ancho de banda

- **Eficiencia de Potencia** (η_P):
  Caracterizada por el Eb/N0 requerido para alcanzar un BER objetivo
  $$\frac{E_b}{N_0} = \frac{S}{N} \cdot \frac{B}{R_b}$$

**B. Calidad de Transmisión**
- **Probabilidad de Error (BER/SER)**:
  $$BER = Q\left(\sqrt{2\frac{E_b}{N_0}}\right)$$ para BPSK

- **Ganancia de Procesamiento**:
  $$G_p = \frac{SNR_{out}}{SNR_{in}}$$

**Paso 3: Análisis de Trade-offs**

El teorema de Shannon establece el trade-off fundamental:
$$C = B\log_2(1 + SNR)$$

Esto implica que podemos intercambiar ancho de banda por potencia:
- Si duplicamos B, podemos reducir SNR manteniendo C
- Si aumentamos SNR, podemos reducir B manteniendo C

#### Derivación Matemática

**Relación entre Parámetros Fundamentales:**

Partiendo de la capacidad del canal:
$$C = B\log_2(1 + SNR)$$

Para transmisión sin errores: $R_b \leq C$

Expresando en términos de Eb/N0:
$$\frac{R_b}{B} \leq \log_2\left(1 + \frac{E_b}{N_0} \cdot \frac{R_b}{B}\right)$$

Definiendo eficiencia espectral normalizada $\rho = R_b/C$:
$$\frac{E_b}{N_0} = \frac{2^{\rho \cdot R_b/B} - 1}{\rho \cdot R_b/B}$$

**Límite de Shannon** cuando $\rho \to 1$:
$$\boxed{\left(\frac{E_b}{N_0}\right)_{min} = \ln(2) = 0.693 \text{ o } -1.59 \text{ dB}}$$

### 🔬 Intuición y Analogías

**Analogía Principal: El Triángulo de Compromisos**

Imagine un triángulo con vértices representando:
- **Velocidad** (tasa de datos)
- **Alcance** (robustez/potencia)
- **Economía** (simplicidad/costo)

Como un triángulo de hierro en gestión de proyectos, solo puede optimizar dos vértices a expensas del tercero. Un sistema de alta velocidad y largo alcance será costoso. Un sistema económico de largo alcance tendrá baja velocidad. Un sistema rápido y económico tendrá alcance limitado.

**Intuición Física:**

El espacio de diseño de modulaciones es como un paisaje multidimensional donde:
- Cada esquema de modulación ocupa una región
- Los límites físicos (Shannon) forman fronteras infranqueables
- La tecnología disponible determina qué regiones son accesibles
- La aplicación determina la región óptima

**Visualización:**

Imagine un gráfico 3D con ejes:
- X: Eficiencia espectral (bits/s/Hz)
- Y: Eficiencia de potencia (Eb/N0 para BER=10^-6)
- Z: Complejidad computacional

Cada modulación forma un punto en este espacio. La frontera de Shannon forma una superficie límite que ningún sistema puede superar.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Comparación AM vs FM para Radio Broadcasting

**Situación:** Evaluar AM y FM para transmisión de audio con calidad aceptable

**Datos:**

| Parámetro | AM | FM | Unidades |
|-----------|-----|-----|----------|
| Ancho de banda | 10 | 200 | kHz |
| SNR salida requerida | 40 | 40 | dB |
| Potencia típica | 50 | 10 | kW |
| Complejidad receptor | Baja | Media | - |

**Análisis comparativo:**

1. **Eficiencia espectral:**
   - AM: Alta (10 kHz para audio de 5 kHz)
   - FM: Baja (200 kHz para audio de 15 kHz)

2. **Eficiencia de potencia:**
   - AM: Baja (requiere 50 kW)
   - FM: Alta (solo 10 kW para mejor calidad)

3. **Trade-off aplicado:**
   FM intercambia ancho de banda por potencia y robustez

**Interpretación:** FM domina en calidad y eficiencia de potencia, pero AM permite más estaciones en el espectro disponible.

---

#### Ejemplo 2: Selección de Modulación para Enlace Satelital

**Contexto:** Diseñar enlace descendente de satélite geoestacionario a 12 GHz

**Restricciones del sistema:**
- Potencia limitada: Panel solar de 2 kW
- Ancho de banda disponible: 36 MHz
- BER objetivo: 10^-9
- Servicio: TV digital HD

**Evaluación de opciones:**

| Modulación | η_B [bits/s/Hz] | Eb/N0 req. [dB] | Potencia TX [W] | Viable |
|------------|-----------------|-----------------|-----------------|--------|
| BPSK | 0.8 | 10.5 | 150 | ✓ |
| QPSK | 1.6 | 10.5 | 150 | ✓ |
| 8-PSK | 2.4 | 14.0 | 380 | ✓ |
| 16-QAM | 3.2 | 14.5 | 450 | ✓ |
| 64-QAM | 4.8 | 18.5 | 1800 | Marginal |

**Selección:** QPSK o 16-QAM según condiciones atmosféricas

---

#### Ejemplo 3: Análisis de Sistema Adaptativo (LTE)

**¿Qué pasa cuando las condiciones del canal varían?**

LTE usa modulación adaptativa que cambia según SNR:

- **SNR > 25 dB**: 256-QAM (8 bits/símbolo)
  - Máxima eficiencia espectral
  - Usuarios cerca de la estación base

- **SNR 15-25 dB**: 64-QAM (6 bits/símbolo)
  - Balance eficiencia/robustez
  - Distancia media

- **SNR 10-15 dB**: 16-QAM (4 bits/símbolo)
  - Prioriza confiabilidad
  - Usuarios en borde de celda

- **SNR < 10 dB**: QPSK (2 bits/símbolo)
  - Máxima robustez
  - Condiciones adversas

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Teorema de Shannon** (Carta 45): Define límites teóricos de comparación
- **BER y Eb/N0** (Carta 31, 57): Métricas fundamentales de calidad
- **Eficiencia espectral** (Carta 41): Parámetro clave de comparación
- **Ganancia de procesamiento** (Carta 42): Métrica para sistemas de pulsos

#### Dependencias (lo que necesitas saber primero)
1. Fundamentos de modulación → Para entender qué se está comparando
2. Análisis de ruido → Para evaluar robustez
3. Teoría de información → Para entender límites fundamentales

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Diseño de enlaces**: Selección de esquema óptimo
2. **Análisis de sistemas**: Evaluación de alternativas
3. **Evolución tecnológica**: Entender por qué ciertos sistemas prevalecen

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- No existe modulación universalmente óptima
- Los trade-offs son fundamentales, no accidentales
- La selección depende de requisitos y restricciones específicas
- Los límites de Shannon son infranqueables

#### Tipos de problemas típicos
1. **Comparación cuantitativa**: Dados dos sistemas, evaluar eficiencias
   - Estrategia: Calcular η_B y Eb/N0, graficar en espacio de trade-offs

2. **Selección de sistema**: Dadas restricciones, elegir modulación
   - Estrategia: Identificar parámetro crítico, filtrar opciones

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Comparar sistemas con diferentes BER**
- Por qué ocurre: Olvidar normalizar a mismo criterio de calidad
- Cómo evitarlo: Siempre especificar BER objetivo antes de comparar
- Ejemplo: BPSK a BER=10^-3 vs QAM a BER=10^-6 no es comparación justa

❌ **Error #2: Ignorar complejidad de implementación**
- Por qué ocurre: Enfocarse solo en desempeño teórico
- Cómo evitarlo: Considerar viabilidad técnica y económica
- Distinción: Un sistema 3 dB mejor pero 10× más complejo puede no ser práctico

❌ **Error #3: Optimizar un solo parámetro**
- Por qué ocurre: Visión unidimensional del problema
- Cómo evitarlo: Evaluar todos los parámetros relevantes
- Ejemplo: Máxima eficiencia espectral puede requerir SNR impráctico

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Eficiencia espectral: η_B = R_b/B [bits/s/Hz]
Relación Eb/N0 y SNR: Eb/N0 = SNR × B/R_b
Límite de Shannon: C = B×log₂(1 + SNR)
Trade-off fundamental: Mayor η_B requiere mayor Eb/N0
```

#### Conceptos Fundamentales
- ✓ **Multi-criterio**: La comparación debe considerar múltiples dimensiones
- ✓ **Trade-offs inevitables**: No se puede optimizar todo simultáneamente
- ✓ **Contexto determina óptimo**: La mejor modulación depende de la aplicación

#### Reglas Mnemotécnicas
- 🧠 **RESPECT**: Robustez, Eficiencia, Simplicidad, Potencia, Espectro, Costo, Tiempo
- 🧠 **"No free lunch"**: Toda mejora en un parámetro tiene un costo en otro

#### Valores Típicos (para referencias rápidas)

| Sistema | η_B [bits/s/Hz] | Eb/N0 @ BER=10^-6 [dB] | Aplicación |
|---------|-----------------|-------------------------|------------|
| BPSK | 1 | 10.5 | Satélites, espacio profundo |
| QPSK | 2 | 10.5 | DVB-S, telemetría |
| 16-QAM | 4 | 14.5 | Cable modems, WiFi |
| 64-QAM | 6 | 18.8 | LTE, cable digital |
| 256-QAM | 8 | 24.4 | Cable DOCSIS 3.1, WiFi 6 |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Proakis & Salehi Cap. 8 "Performance Analysis"
- **Papers**: "Comparison of Modulation Methods" - IEEE Communications Surveys
- **Simulaciones**: MATLAB Communications Toolbox - bertool para curvas BER

#### Temas Relacionados para Explorar
1. Modulación adaptativa y esquemas híbridos
2. Teoría de detección y estimación
3. Capacity-approaching codes (LDPC, Turbo)

#### Preguntas para Reflexionar
- ¿Por qué sistemas antiguos (AM) sobreviven si hay alternativas superiores?
- ¿Cómo cambiarán estos parámetros con computación cuántica?
- ¿Es posible un sistema que se adapte dinámicamente a todos los parámetros?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 25 minutos
**Prerequisitos críticos**: Modulaciones básicas, teoría de información, análisis de ruido
**Tags**: `#comparacion-sistemas` `#trade-offs` `#eficiencia` `#diseño-sistemas`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*