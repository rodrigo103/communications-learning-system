# Carta 45: Teorema de Shannon-Hartley

> **Unidad 9**: Teoría de la Información

---

## 🎯 Pregunta

Enuncie y explique el Teorema de Shannon-Hartley.

---

## 📝 Respuesta Breve (de la carta original)

El **Teorema de Shannon-Hartley** establece la **capacidad máxima** de un canal con ruido gaussiano blanco:

$$C = B \log_2\left(1 + \frac{S}{N}\right) \text{ bits/s}$$

donde:
- C = capacidad del canal (bits/s)
- B = ancho de banda (Hz)
- S/N = relación señal a ruido (lineal)

**Implicaciones fundamentales**:
1. **Límite teórico**: tasa máxima para comunicación libre de errores
2. **Trade-off BW-SNR**: se puede intercambiar ancho de banda por potencia y viceversa
3. **Inalcanzable en práctica**: pero indica dirección de diseño
4. **Base de comparación**: eficiencia de sistemas reales vs. límite de Shannon

**Conclusión**: fija límite fundamental de lo que es posible en comunicaciones.

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El Teorema de Shannon-Hartley, publicado independientemente por Claude Shannon (1948) y Ralph Hartley (1928), es posiblemente el resultado más importante en teoría de comunicaciones. Este teorema establece el límite fundamental e insuperable de la velocidad a la que podemos transmitir información a través de cualquier canal de comunicación con ruido.

**¿Por qué es importante este concepto?** Antes de Shannon, los ingenieros creían que para transmitir sin errores necesitaban aumentar indefinidamente la potencia o reducir drásticamente la velocidad. Shannon demostró algo revolucionario: existe una velocidad máxima específica (la capacidad) por debajo de la cual podemos transmitir con error arbitrariamente pequeño, y por encima de la cual el error es inevitable, sin importar cuánta potencia usemos.

**¿Dónde se aplica?** El teorema es fundamental en:
- **Diseño de modems**: DSL, cable, fibra óptica
- **Comunicaciones inalámbricas**: WiFi, 4G/5G, satelital
- **Almacenamiento**: discos duros, SSD (canal con ruido)
- **Estándares modernos**: todos buscan acercarse al límite de Shannon

**¿Cuándo lo encontrarás?** En cada decisión de diseño de sistemas: selección de modulación, codificación, asignación de potencia, y evaluación de desempeño. Los sistemas modernos operan a 1-3 dB del límite de Shannon.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Entropía y información mutua (Carta 44)
- Proceso gaussiano y ruido blanco
- Teoría de probabilidad y procesos estocásticos
- Concepto de canal de comunicación

#### Desarrollo Paso a Paso

**Paso 1: Modelo del canal AWGN**

Consideramos el canal de ruido aditivo gaussiano blanco (AWGN):
$$Y = X + N$$

donde:
- X: señal transmitida con potencia S
- N: ruido gaussiano con potencia N
- Y: señal recibida

**Paso 2: Información mutua**

La capacidad es la máxima información mutua entre entrada y salida:
$$C = \max_{p(x)} I(X;Y)$$

Para el canal gaussiano, la distribución óptima de entrada es gaussiana.

**Paso 3: Derivación de la capacidad**

Para entrada gaussiana y canal AWGN:
$$I(X;Y) = H(Y) - H(Y|X) = H(Y) - H(N)$$

donde:
- $H(Y)$: entropía de la salida (gaussiana con potencia S+N)
- $H(N)$: entropía del ruido (gaussiana con potencia N)

#### Derivación Matemática Completa

**Partiendo de la entropía diferencial gaussiana:**

Para una variable gaussiana con varianza $\sigma^2$:
$$h(X) = \frac{1}{2}\log_2(2\pi e \sigma^2)$$

**Aplicando al canal:**

La salida Y es gaussiana con potencia (S+N):
$$h(Y) = \frac{1}{2}\log_2[2\pi e(S+N)]$$

El ruido N es gaussiano con potencia N:
$$h(N) = \frac{1}{2}\log_2(2\pi eN)$$

**Calculando la información mutua:**
$$I(X;Y) = h(Y) - h(N) = \frac{1}{2}\log_2\left(\frac{S+N}{N}\right) = \frac{1}{2}\log_2\left(1 + \frac{S}{N}\right)$$

**Considerando el ancho de banda B:**

En tiempo continuo con ancho de banda B Hz, por el teorema del muestreo podemos transmitir 2B muestras/segundo independientes:

$$\boxed{C = B\log_2\left(1 + \frac{S}{N}\right) \text{ bits/s}}$$

**Significado físico de cada término:**
- $B$: Ancho de banda disponible (Hz) - dimensión "espacial" del canal
- $S/N$: Calidad del canal - cuánto destaca la señal sobre el ruido
- $\log_2(1 + S/N)$: Bits por uso del canal (por dimensión)

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina una autopista (canal) con neblina (ruido):
- El ancho de banda B es como el número de carriles
- La SNR es como la visibilidad a través de la neblina
- La capacidad C es el flujo máximo de vehículos sin accidentes
- Más carriles O mejor visibilidad aumentan el flujo
- Pero hay rendimientos decrecientes (logaritmo)

**Intuición física:**
El teorema captura dos recursos fundamentales:
1. **Grados de libertad** (ancho de banda): más dimensiones independientes para transmitir
2. **Distinguibilidad** (SNR): capacidad de diferenciar niveles de señal

**Visualización:**
La función $\log_2(1 + SNR)$ tiene forma característica:
- SNR baja: crecimiento casi lineal (régimen limitado por potencia)
- SNR alta: crecimiento logarítmico lento (régimen limitado por banda)
- Punto de inflexión alrededor de SNR = 1 (0 dB)

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Canal de Voz Telefónica

**Situación:** Línea telefónica tradicional

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Ancho de banda | 3100 | Hz |
| SNR | 30 | dB (1000 lineal) |

**Solución paso a paso:**

1. **Convertir SNR a lineal:**
   $$SNR_{lineal} = 10^{30/10} = 1000$$

2. **Aplicar Shannon-Hartley:**
   $$C = 3100 \times \log_2(1 + 1000)$$
   $$C = 3100 \times 9.97$$

3. **Resultado:**
   $$\boxed{C = 30,900 \text{ bits/s}}$$

**Interpretación:** El límite teórico es ~31 kbps, explicando por qué los modems de 56k necesitaban trucos especiales y nunca alcanzaban velocidad nominal.

---

#### Ejemplo 2: WiFi 802.11ac

**Contexto:** Canal WiFi moderno de 80 MHz con buena señal

**Parámetros reales:**

| Parámetro | Valor | Notas |
|-----------|-------|-------|
| Ancho de banda | 80 MHz | Canal ancho |
| SNR típica | 40 dB | Excelente señal |
| SNR lineal | 10,000 | - |

**Cálculo de capacidad teórica:**
$$C = 80 \times 10^6 \times \log_2(1 + 10000)$$
$$C = 80 \times 10^6 \times 13.29$$
$$C = 1,063 \text{ Mbps}$$

**Realidad práctica:**
- 802.11ac alcanza ~867 Mbps (con 256-QAM, codificación 5/6)
- Eficiencia: 867/1063 = 81.6% del límite de Shannon
- Overhead por: preámbulos, pilotos, guard intervals, CSMA/CA

---

#### Ejemplo 3: Regímenes Límite

**¿Qué pasa cuando...?**

**Caso 1: SNR → ∞ (Régimen limitado por banda)**
$$C \approx B\log_2(SNR) \quad \text{(crecimiento logarítmico)}$$

Duplicar la potencia solo agrega 1 bit/s/Hz adicional.

**Caso 2: SNR → 0 (Régimen limitado por potencia)**
Usando aproximación $\ln(1+x) \approx x$ para x pequeño:
$$C \approx B \cdot \frac{S}{N} \cdot \frac{1}{\ln(2)} = 1.44 \cdot B \cdot \frac{S}{N}$$

La capacidad es proporcional a la potencia.

**Caso 3: Ancho de banda infinito**
$$C_{\infty} = \lim_{B→∞} B\log_2\left(1 + \frac{S}{N_0 B}\right) = \frac{S}{N_0 \ln(2)} = 1.44 \frac{S}{N_0}$$

Existe un límite finito incluso con banda infinita!

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Entropía** (Carta 44): Capacidad maximiza la información mutua
- **Eb/N0 mínimo** (Carta 57): Límite de Shannon -1.59 dB
- **Modulación adaptativa**: Ajusta esquema según SNR disponible
- **Códigos correctores** (Carta 48): Permiten acercarse a C

#### Dependencias
1. Teoría de información básica → necesaria para entender información mutua
2. Procesos aleatorios → para caracterizar señal y ruido
3. Teoría de muestreo → relaciona tiempo continuo con discreto

#### Aplicaciones Posteriores
1. **Diseño de códigos**: Turbo codes, LDPC se acercan al límite
2. **MIMO**: Extiende Shannon a múltiples antenas
3. **5G/6G**: Opera cerca del límite en cada subportadora

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- Shannon NO dice CÓMO alcanzar la capacidad, solo que EXISTE
- El teorema asume codificación de longitud infinita (no práctica)
- Trade-off fundamental: puedes intercambiar BW por SNR
- La capacidad es un límite superior estricto e infranqueable

#### Tipos de problemas típicos
1. **Cálculo directo**: Dados B y SNR, calcular C
2. **Diseño inverso**: Dada C objetivo, encontrar B o SNR necesarios
3. **Comparación**: Eficiencia de sistema real vs. límite de Shannon
4. **Análisis de trade-offs**: Costo de duplicar capacidad

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Usar SNR en dB directamente en la fórmula**
- Por qué ocurre: Olvido de conversión
- Cómo evitarlo: SIEMPRE convertir dB a lineal primero
- Ejemplo: 20 dB = 100 (no 20) en la fórmula

❌ **Error #2: Confundir capacidad con velocidad real**
- Por qué ocurre: Shannon da límite teórico
- Cómo evitarlo: Sistemas reales tienen overhead y operan debajo de C
- Realidad: Buenos sistemas alcanzan 50-90% de Shannon

❌ **Error #3: Creer que más potencia siempre ayuda proporcionalmente**
- Por qué ocurre: Intuición lineal
- Cómo evitarlo: Recordar el logaritmo - rendimientos decrecientes
- A alta SNR: Duplicar potencia solo agrega ~1 bit/s/Hz

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Capacidad: C = B log₂(1 + S/N) bits/s
Límite de potencia: C ≈ 1.44 × B × (S/N) cuando SNR << 1
Límite de banda: C ≈ B × log₂(SNR) cuando SNR >> 1
Banda infinita: C∞ = S/(N₀ ln 2) = 1.44 S/N₀
```

#### Conceptos Fundamentales
- ✓ **Límite fundamental**: No hay esquema que supere C
- ✓ **Trade-off BW-Power**: Recursos intercambiables pero con rendimientos diferentes
- ✓ **Alcanzable**: Existe codificación que se acerca arbitrariamente a C

#### Reglas Mnemotécnicas
- 🧠 **"BLoS"**: Bandwidth, Log, Signal-to-noise
- 🧠 **Factor 1.44**: Aparece en régimen de baja SNR (1/ln(2))
- 🧠 **0 dB = transición**: Cambio entre régimen lineal y logarítmico

#### Valores Típicos

| Sistema | BW | SNR | Capacidad | Real | Eficiencia |
|---------|-----|-----|-----------|------|------------|
| DSL | 1.1 MHz | 40 dB | 44 Mbps | 24 Mbps | 55% |
| LTE | 20 MHz | 20 dB | 133 Mbps | 100 Mbps | 75% |
| WiFi 6 | 160 MHz | 35 dB | 1.8 Gbps | 1.2 Gbps | 67% |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Paper original**: Shannon, "Communication in the Presence of Noise" (1949)
- **Libro de texto**: Proakis & Salehi, Cap. 7 "Channel Capacity and Coding"
- **Implementación**: Simulaciones en MATLAB/Python de curvas de capacidad

#### Temas Relacionados para Explorar
1. Capacidad de canales con desvanecimiento
2. MIMO y capacidad de múltiples antenas
3. Capacidad con información de estado del canal (CSI)
4. Teoría de tasa-distorsión

#### Preguntas para Reflexionar
- ¿Por qué el logaritmo aparece naturalmente en la capacidad?
- ¿Qué pasaría si el ruido no fuera gaussiano?
- ¿Cómo cambiaría todo si pudiéramos usar retroalimentación?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 60 minutos
**Prerequisitos críticos**: Entropía, procesos gaussianos, teoría de información
**Tags**: `#shannon` `#capacidad-canal` `#limite-fundamental` `#awgn`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*