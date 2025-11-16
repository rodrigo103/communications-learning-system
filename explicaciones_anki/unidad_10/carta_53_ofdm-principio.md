# Carta 53: OFDM - Principio de Funcionamiento

> **Unidad 10**: Espectro Expandido y OFDM

---

## 🎯 Pregunta

¿Qué es OFDM y cuál es su principio de funcionamiento?

---

## 📝 Respuesta Breve (de la carta original)

**OFDM (Orthogonal Frequency Division Multiplexing)** divide el canal en múltiples subportadoras ortogonales de banda angosta.

**Principio**:
1. Flujo de datos serial → paralelo en N subcanales
2. Cada subcanal modula una subportadora (típicamente QAM)
3. Subportadoras son ortogonales: $\Delta f = 1/T_{symbol}$
4. Implementación eficiente: **IFFT** (transmisor) y **FFT** (receptor)

**Características clave**:
- Espectros de subportadoras se solapan, pero son ortogonales
- Cada subportadora transmite a baja tasa → símbolo largo
- **Prefijo cíclico (CP)**: guarda contra multitrayecto

**Ventajas**:
1. **Resistencia a multitrayecto**: ecualización simple
2. **Uso eficiente del espectro**: ortogonalidad
3. **Adaptabilidad**: puede variar modulación por subportadora
4. **Implementación digital eficiente**: FFT/IFFT

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

**¿Por qué es importante OFDM?** OFDM es la tecnología de capa física dominante en las comunicaciones modernas de alta velocidad. Resuelve elegantemente uno de los problemas más difíciles en comunicaciones: transmitir datos a alta velocidad en canales con multitrayecto severo (donde las señales rebotan y llegan por múltiples caminos). En lugar de luchar contra el multitrayecto con ecualizadores complejos, OFDM lo convierte en un problema simple de multiplicación en el dominio de la frecuencia.

**¿Dónde se aplica?** OFDM es ubicuo en sistemas modernos:
- **WiFi**: 802.11a/g/n/ac/ax (WiFi 6)
- **4G LTE y 5G NR**: la base de las redes celulares modernas
- **Televisión Digital**: DVB-T/T2, ATSC 3.0, ISDB-T
- **DSL**: ADSL, VDSL usan DMT (variante de OFDM)
- **PLC**: Power Line Communications
- **Radio Digital**: DAB, DRM, HD Radio

**¿Cuándo lo encontrarás?** OFDM es la elección natural cuando:
- El canal tiene multitrayecto significativo (urbano, indoor)
- Se requieren tasas de datos muy altas
- El espectro debe usarse eficientemente
- Se necesita flexibilidad en la asignación de recursos

**Historia:** Propuesto en 1966 por Chang (Bell Labs), pero no fue práctico hasta los 90s cuando los DSPs se volvieron lo suficientemente potentes para implementar FFTs grandes en tiempo real. Weinstein y Ebert (1971) propusieron usar DFT para la implementación.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Transformada de Fourier y DFT/FFT
- Ortogonalidad de funciones
- Sistemas lineales e invariantes en el tiempo
- Modulación QAM (Carta 29)
- Teorema del muestreo

#### Desarrollo Paso a Paso

**Paso 1: División del Espectro en Subcanales**

En lugar de transmitir datos en serie a alta velocidad (susceptible a ISI), OFDM:
- Divide el ancho de banda total B en N subportadoras
- Cada subportadora tiene ancho de banda Δf = B/N
- Los datos se transmiten en paralelo a velocidad N veces menor

**Paso 2: Ortogonalidad - La Clave de OFDM**

Las subportadoras están espaciadas exactamente por:
$$\Delta f = \frac{1}{T_s}$$

donde $T_s$ es la duración del símbolo OFDM. Esta relación específica garantiza ortogonalidad:

$$\int_0^{T_s} e^{j2\pi f_k t} \cdot e^{-j2\pi f_m t} dt = \begin{cases} T_s & \text{si } k = m \\ 0 & \text{si } k \neq m \end{cases}$$

**Paso 3: Implementación con FFT**

La genialidad de OFDM es que la modulación/demodulación de todas las subportadoras se puede hacer con una sola FFT:

- **Transmisor**: IFFT convierte símbolos complejos en muestras temporales
- **Receptor**: FFT convierte muestras temporales en símbolos complejos

Esto reduce la complejidad de O(N²) a O(N log N).

#### Derivación Matemática

**Señal OFDM en tiempo continuo:**

La señal transmitida para un símbolo OFDM es:

$$s(t) = \sum_{k=0}^{N-1} X_k e^{j2\pi f_k t} \quad \text{para } 0 \leq t \leq T_s$$

donde:
- $X_k$ = símbolo complejo de datos en subportadora k
- $f_k = f_0 + k\Delta f$ = frecuencia de subportadora k
- $N$ = número de subportadoras

**Relación con IDFT:**

Si muestreamos a tasa $f_s = N\Delta f$:

$$s[n] = s(nT_s/N) = \sum_{k=0}^{N-1} X_k e^{j2\pi kn/N}$$

Esto es exactamente la IDFT de los símbolos $\{X_k\}$:

$$\boxed{s[n] = \text{IDFT}\{X_k\} = \text{IFFT}\{X_k\}}$$

**Proceso en el receptor:**

El receptor calcula:

$$Y_k = \frac{1}{N}\sum_{n=0}^{N-1} r[n] e^{-j2\pi kn/N} = \text{DFT}\{r[n]\}$$

**Canal con multitrayecto:**

Si el canal tiene respuesta $h(t)$ con transformada $H(f)$:

$$Y_k = H(f_k) \cdot X_k + N_k$$

**Resultado clave:** ¡El multitrayecto se convierte en una simple multiplicación por subportadora!

$$\boxed{X̂_k = \frac{Y_k}{H(f_k)}}$$

### 🔬 Intuición y Analogías

**Analogía principal: El coro de cantantes**

Imagina un coro donde cada cantante (subportadora) canta una nota diferente:
- **Sin OFDM**: un solo cantante intenta cantar todas las notas rápidamente (serial)
- **Con OFDM**: muchos cantantes, cada uno canta su nota lentamente (paralelo)
- **Ortogonalidad**: las notas están perfectamente espaciadas en frecuencia para no interferir
- **FFT**: el director que coordina a todos los cantantes eficientemente

**Intuición física del multitrayecto:**

Piensa en el eco en una catedral:
- **Transmisión serial rápida**: el eco de una palabra interfiere con la siguiente
- **OFDM**: cada "palabra" (símbolo) es tan larga que el eco muere antes de la siguiente
- **Subportadoras**: como hablar en muchos tonos simultáneamente, cada tono viaja independiente

**Visualización espectral:**

Los espectros de las subportadoras se ven como funciones sinc que se solapan:
```
     |  /\    /\    /\    /\
Amp  | /  \  /  \  /  \  /  \
     |/    \/    \/    \/    \
     |____________________
          f1  f2  f3  f4   Frecuencia
```
- Los picos de una coinciden con los ceros de las otras → ortogonalidad
- A pesar del solapamiento, no hay interferencia

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Sistema OFDM Simple de 4 Subportadoras

**Situación:** Transmitir 8 bits usando OFDM con 4 subportadoras y QPSK

**Datos:**
| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Bits a transmitir | [1,0,1,1,0,1,0,0] | - |
| N (subportadoras) | 4 | - |
| Modulación | QPSK | 2 bits/símbolo |
| BW total | 1 MHz | - |
| Duración símbolo | 4 μs | - |

**Solución paso a paso:**

1. **Mapeo a símbolos QPSK:**
   - Bits [1,0] → X₀ = 1+j (45°)
   - Bits [1,1] → X₁ = -1+j (135°)
   - Bits [0,1] → X₂ = -1-j (225°)
   - Bits [0,0] → X₃ = 1-j (315°)

2. **Vector de entrada a IFFT:**
   $$X = [1+j, -1+j, -1-j, 1-j]$$

3. **Cálculo IFFT (4 puntos):**
   $$s[n] = \frac{1}{4}\sum_{k=0}^{3} X_k e^{j2\pi kn/4}$$

   Resultados:
   - s[0] = 0.0 + 0.0j
   - s[1] = 0.5 - 0.5j
   - s[2] = 0.0 + 1.0j
   - s[3] = 0.5 + 0.5j

4. **Transmisión:**
   Estas 4 muestras complejas se transmiten en 4 μs

**Interpretación:** Los 8 bits se transmiten en paralelo, cada subportadora lleva 2 bits a velocidad reducida.

---

#### Ejemplo 2: WiFi 802.11a/g

**Contexto:** Estándar WiFi usando OFDM

**Especificaciones 802.11a:**
| Parámetro | Valor | Significado |
|-----------|-------|-------------|
| Subportadoras totales | 64 | Tamaño FFT |
| Subportadoras de datos | 48 | Llevan información |
| Subportadoras piloto | 4 | Para estimación de canal |
| Subportadoras nulas | 12 | Guarda bandas y DC |
| Espaciado subportadora | 312.5 kHz | Δf |
| Duración símbolo útil | 3.2 μs | 1/Δf |
| Prefijo cíclico | 0.8 μs | 25% overhead |
| Duración total símbolo | 4.0 μs | Útil + CP |
| BW ocupado | 16.6 MHz | 52 × 312.5 kHz |
| BW canal | 20 MHz | Asignado |

**Cálculo de tasa máxima (64-QAM, rate 3/4):**

$$R_{max} = \frac{48 \text{ subportadoras} \times 6 \text{ bits/símbolo} \times 3/4}{4.0 \text{ μs}} = 54 \text{ Mbps}$$

---

#### Ejemplo 3: Efecto del Multitrayecto

**¿Qué pasa con y sin prefijo cíclico?**

**Escenario:**
- Canal con dos trayectos: directo y reflejado con retardo de 200 ns
- Atenuación del reflejo: -6 dB (factor 0.5)
- Sistema OFDM con Ts = 3.2 μs

**Sin prefijo cíclico:**
- El retardo causa ISI entre símbolos OFDM consecutivos
- También causa ICI (inter-carrier interference)
- Ortogonalidad destruida → BER alto

**Con CP de 0.8 μs (> 200 ns):**
1. CP absorbe el retardo
2. Después de remover CP, solo queda efecto multiplicativo
3. Canal en frecuencia: $H(f) = 1 + 0.5e^{-j2\pi f \times 200ns}$
4. Ecualización: simple división por H(f) en cada subportadora
5. BER se mantiene bajo

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **QAM** (Carta 29): modulación típica por subportadora
- **Teorema del Muestreo** (Carta 5): base para dimensionar FFT
- **Prefijo Cíclico** (Carta 55): componente esencial de OFDM
- **CDMA** (Carta 52): tecnología competidora en 3G

#### Dependencias (lo que necesitas saber primero)
1. FFT/DFT → implementación práctica de OFDM
2. Ortogonalidad de señales → por qué funciona sin interferencia
3. Respuesta en frecuencia → cómo el canal afecta cada subportadora

#### Aplicaciones Posteriores (dónde usarás esto)
1. **OFDMA**: extensión multiusuario en LTE/5G
2. **MIMO-OFDM**: combinación con múltiples antenas
3. **SC-FDMA**: variante usada en uplink de LTE
4. **Diseño de sistemas 5G/6G**: base de la capa física

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- Por qué la ortogonalidad requiere Δf = 1/Ts exactamente
- Cómo la FFT implementa eficientemente OFDM
- Por qué OFDM simplifica la ecualización
- El rol crítico del prefijo cíclico

#### Tipos de problemas típicos
1. **Diseño de sistema OFDM**: Dados requisitos, calcular N, Δf, CP
   - Estrategia: comenzar con delay spread para CP, luego coherence BW

2. **Cálculo de capacidad**: Determinar throughput con modulación adaptativa
   - Estrategia: sumar capacidades por subportadora según SNR

3. **Análisis de ortogonalidad**: Demostrar ortogonalidad matemáticamente
   - Estrategia: integral de producto de exponenciales complejas

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Pensar que las subportadoras no se solapan**
- Por qué ocurre: diagramas simplificados muestran canales separados
- Realidad: los espectros se solapan completamente
- Clave: la ortogonalidad permite solapamiento sin interferencia

❌ **Error #2: Ignorar la pérdida por prefijo cíclico**
- Por qué ocurre: se olvida que CP no lleva datos
- Impacto: eficiencia = Ts/(Ts+Tcp) < 1
- Ejemplo: CP de 25% reduce throughput en 20%

❌ **Error #3: Confundir OFDM con FDM clásico**
- FDM: necesita bandas de guarda entre canales
- OFDM: no necesita bandas de guarda (ortogonalidad)
- Diferencia: OFDM es ~50% más eficiente espectralmente

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Espaciado subportadoras: Δf = 1/Ts
Número subportadoras: N = BW/Δf
Duración CP: Tcp > τmax (delay spread)
Eficiencia: η = Ts/(Ts + Tcp)
Tasa datos: R = N × log₂(M) × r × η / (Ts + Tcp)
```

#### Conceptos Fundamentales
- ✓ **Ortogonalidad**: la magia que permite solapamiento sin interferencia
- ✓ **FFT = OFDM**: implementación eficiente es clave de su éxito
- ✓ **Paralelo vence serie**: muchos canales lentos mejor que uno rápido
- ✓ **Multitrayecto simplificado**: de convolución a multiplicación

#### Reglas Mnemotécnicas
- 🧠 **OFDM = "Ortogonalidad Facilita División Multiportadora"**
- 🧠 **FFT**: "Fast Fourier Transforms → Fast OFDM"
- 🧠 **CP**: "Cyclic Prefix = Cura Para multitrayecto"

#### Valores Típicos (para referencias rápidas)
| Sistema | Subportadoras | Δf | CP |
|---------|---------------|-----|-----|
| WiFi 802.11a/g | 64 (48 datos) | 312.5 kHz | 0.8 μs |
| WiFi 802.11ac | 256 (234 datos) | 78.125 kHz | 0.8 μs |
| LTE (20 MHz) | 2048 (1200 datos) | 15 kHz | 4.7 μs |
| 5G NR | Hasta 4096 | 15/30/60 kHz | Variable |
| DVB-T | 2048/8192 | Variable | 1/4, 1/8, 1/16, 1/32 |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libro clásico**: Bahai & Saltzberg "Multi-Carrier Digital Communications"
- **Paper fundamental**: Weinstein & Ebert 1971 (DFT for OFDM)
- **Estándares**: IEEE 802.11, 3GPP Release 8 (LTE)
- **Simulación**: GNU Radio tiene excelentes bloques OFDM

#### Temas Relacionados para Explorar
1. OFDMA - extensión multiusuario de OFDM
2. PAPR (Peak-to-Average Power Ratio) - principal problema de OFDM
3. Estimación de canal con pilotos en OFDM
4. MIMO-OFDM - combinación poderosa

#### Preguntas para Reflexionar
- ¿Por qué OFDM no se usó antes si la teoría existía desde 1966?
- ¿Cómo afecta el efecto Doppler a la ortogonalidad en OFDM?
- ¿Qué ventajas mantiene single-carrier sobre OFDM?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 40 minutos
**Prerequisitos críticos**: FFT, ortogonalidad, sistemas LTI
**Tags**: `#ofdm` `#fft` `#multicarrier` `#wifi` `#lte` `#5g`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*