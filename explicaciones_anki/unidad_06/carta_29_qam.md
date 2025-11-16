# Carta 29: QAM - Modulación de Amplitud en Cuadratura

> **Unidad 6**: Modulación Digital

---

## 🎯 Pregunta

¿Qué es QAM y por qué es ampliamente utilizada en comunicaciones modernas?

---

## 📝 Respuesta Breve (de la carta original)

**QAM (Quadrature Amplitude Modulation)** modula independientemente amplitud y fase de dos portadoras en cuadratura.

**Señal QAM**:
$$s(t) = A_I(t)\cos(2\pi f_c t) - A_Q(t)\sin(2\pi f_c t)$$

**Ventajas**:
1. **Alta eficiencia espectral**: M-QAM transmite $\log_2(M)$ bits/símbolo
2. **Flexibilidad**: múltiples configuraciones (16-QAM, 64-QAM, 256-QAM, etc.)
3. **Adaptabilidad**: puede ajustar orden según condiciones del canal

**Desventaja**: sensible a ruido y no-linealidades (amplitud variable)

**Aplicaciones**:
- Cable modems, DSL
- WiFi (802.11), 4G/5G
- TV digital, comunicaciones satelitales

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La **Modulación de Amplitud en Cuadratura (QAM)** representa uno de los pilares fundamentales de las comunicaciones digitales modernas, siendo la técnica de modulación preferida cuando se requiere transmitir datos a alta velocidad en un ancho de banda limitado. QAM es omnipresente en nuestra vida diaria: cada vez que navegas por internet usando WiFi, transmites video en streaming, o realizas una videollamada por celular, QAM está trabajando silenciosamente para hacer posible esa transmisión de información.

¿Por qué es tan importante QAM? En la era de la información digital, donde la demanda de datos crece exponencialmente mientras que el espectro electromagnético disponible permanece fijo, necesitamos técnicas que maximicen la cantidad de información transmitida por cada Hertz de ancho de banda. QAM logra precisamente esto al explotar dos dimensiones ortogonales (amplitud y fase) de manera independiente, efectivamente creando dos canales paralelos en el mismo espacio espectral.

La historia de QAM se remonta a los años 1960s, cuando los ingenieros de telecomunicaciones buscaban maneras más eficientes de transmitir datos digitales sobre líneas telefónicas analógicas. La empresa Bell System fue pionera en su implementación práctica, desarrollando módems que usaban QAM para alcanzar velocidades de datos que parecían imposibles con técnicas anteriores. Desde entonces, QAM ha evolucionado continuamente, con constelaciones cada vez más densas que permiten tasas de datos más altas a medida que mejoran las tecnologías de procesamiento de señales.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Modulación digital básica** (ASK, PSK) - entender cómo se mapean bits a símbolos
- **Señales ortogonales** - comprensión de componentes en fase y cuadratura
- **Espacio de señal y constelaciones** - representación geométrica de modulaciones
- **Transformada de Fourier** - análisis espectral de señales moduladas

#### Desarrollo Paso a Paso

**Paso 1: Principio de Ortogonalidad**

QAM se basa en el principio fundamental de que dos señales sinusoidales desfasadas 90° son ortogonales, lo que significa que no interfieren entre sí cuando se transmiten simultáneamente:

$$\int_{0}^{T} \cos(2\pi f_c t) \cdot \sin(2\pi f_c t) dt = 0$$

Esta ortogonalidad permite transmitir dos flujos de información independientes usando la misma frecuencia portadora, duplicando efectivamente la capacidad del canal sin requerir ancho de banda adicional.

**Paso 2: Construcción de la Señal QAM**

La señal QAM se construye combinando dos portadoras en cuadratura, cada una modulada en amplitud por flujos de datos independientes:

- **Componente en Fase (I)**: $I(t) \cdot \cos(2\pi f_c t)$
- **Componente en Cuadratura (Q)**: $Q(t) \cdot \sin(2\pi f_c t)$

Donde I(t) y Q(t) son las señales de banda base que contienen la información digital. La señal completa es:

$$s_{QAM}(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t)$$

**Paso 3: Mapeo de Bits a Símbolos**

En M-QAM, donde M representa el número de puntos en la constelación, cada símbolo transmite $\log_2(M)$ bits. Por ejemplo:
- 16-QAM: 4 bits por símbolo
- 64-QAM: 6 bits por símbolo
- 256-QAM: 8 bits por símbolo

Los bits se dividen en dos grupos: uno controla la amplitud I y otro la amplitud Q, creando una red rectangular de puntos en el plano complejo.

#### Derivación Matemática

**Representación en Banda Base Compleja:**

Partiendo de la representación temporal, podemos expresar QAM usando notación compleja:

$$s_{QAM}(t) = \text{Re}\{[I(t) + jQ(t)] \cdot e^{j2\pi f_c t}\}$$

Definiendo la envolvente compleja como:
$$\tilde{s}(t) = I(t) + jQ(t) = A(t)e^{j\phi(t)}$$

Donde:
- $A(t) = \sqrt{I^2(t) + Q^2(t)}$ es la amplitud instantánea
- $\phi(t) = \arctan(Q(t)/I(t))$ es la fase instantánea

**Eficiencia Espectral:**

Para M-QAM con velocidad de símbolo $R_s$, la tasa de bits es:

$$R_b = R_s \cdot \log_2(M) \text{ bits/s}$$

El ancho de banda mínimo requerido (Nyquist):

$$B_{min} = R_s \text{ Hz}$$

Por lo tanto, la eficiencia espectral es:

$$\boxed{\eta = \frac{R_b}{B} = \log_2(M) \text{ bits/s/Hz}}$$

**Significado físico de cada término:**
- $R_s$: número de cambios de símbolo por segundo (bauds)
- $M$: tamaño de la constelación (número de puntos)
- $\eta$: bits transmitidos por cada Hz de ancho de banda

### 🔬 Intuición y Analogías

**Analogía principal:**

Imagina QAM como un sistema de comunicación en una plaza donde dos personas (canales I y Q) pueden hablar simultáneamente sin interferirse. Una persona mira hacia el norte (componente I) y otra hacia el este (componente Q). Cada persona puede variar el volumen de su voz (amplitud) para transmitir diferentes mensajes. Como están orientadas perpendicularmente, un receptor con dos oídos direccionales puede escuchar y decodificar ambos mensajes independientemente. El número de niveles de volumen diferentes que cada persona puede usar determina cuánta información puede transmitir.

**Intuición física:**

QAM explota el hecho de que una onda electromagnética tiene tanto magnitud como dirección. Es como lanzar flechas a un blanco: no solo importa qué tan lejos del centro caiga la flecha (amplitud), sino también en qué dirección desde el centro (fase). Cada punto específico en el blanco representa un símbolo único que codifica múltiples bits.

**Visualización:**

La constelación QAM se visualiza mejor como una cuadrícula de puntos en un plano cartesiano. Para 16-QAM, imagina un tablero de ajedrez 4x4 donde cada casilla representa una combinación única de 4 bits. La distancia desde el origen determina la potencia de transmisión para ese símbolo, mientras que el ángulo determina la fase de la portadora.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Transmisión WiFi 802.11ac con 64-QAM

**Situación:** Un router WiFi transmitiendo video HD usando 64-QAM en un canal de 20 MHz.

**Datos:**
| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Modulación | 64-QAM | - |
| Ancho de banda del canal | 20 | MHz |
| Velocidad de símbolo | 18.52 | Msímbolos/s |
| Tasa de código | 3/4 | - |

**Solución paso a paso:**

1. **Bits por símbolo sin codificación:**
   $$b = \log_2(64) = 6 \text{ bits/símbolo}$$

2. **Tasa de bits sin codificación:**
   $$R_{raw} = 18.52 \times 6 = 111.12 \text{ Mbps}$$

3. **Tasa de bits efectiva con codificación:**
   $$R_{efectiva} = 111.12 \times \frac{3}{4} = 83.34 \text{ Mbps}$$

4. **Eficiencia espectral:**
   $$\boxed{\eta = \frac{83.34}{20} = 4.17 \text{ bits/s/Hz}}$$

**Interpretación:** Este sistema puede transmitir video 4K comprimido (que requiere típicamente 25-50 Mbps) con margen suficiente para otras aplicaciones simultáneas.

---

#### Ejemplo 2: Cable Modem DOCSIS 3.1 con 4096-QAM

**Contexto:** Un cable modem moderno operando en condiciones ideales con 4096-QAM.

En los sistemas de cable más avanzados, cuando la relación señal-ruido es excepcionalmente alta (>40 dB), se puede usar 4096-QAM. Esto transmite 12 bits por símbolo, alcanzando eficiencias espectrales de hasta 10 bits/s/Hz después de la codificación de canal. Un solo portadora de 6 MHz puede entonces transportar:

$$R_b = 6 \text{ MHz} \times 10 \text{ bits/s/Hz} = 60 \text{ Mbps}$$

Los módems DOCSIS 3.1 pueden vincular múltiples portadoras, alcanzando velocidades agregadas superiores a 1 Gbps en downstream. Sin embargo, 4096-QAM requiere condiciones casi perfectas del canal y raramente se usa en la práctica, donde 256-QAM o 1024-QAM son más comunes.

---

#### Ejemplo 3: Adaptación Dinámica en LTE

**¿Qué pasa cuando las condiciones del canal varían?**

Los sistemas LTE implementan Adaptive Modulation and Coding (AMC), ajustando dinámicamente el orden de QAM según la calidad del enlace:

- **SNR > 25 dB**: Usa 256-QAM (8 bits/símbolo) - máxima capacidad
- **SNR 15-25 dB**: Usa 64-QAM (6 bits/símbolo) - balance capacidad/robustez
- **SNR 10-15 dB**: Usa 16-QAM (4 bits/símbolo) - mayor robustez
- **SNR 5-10 dB**: Usa QPSK (2 bits/símbolo) - máxima robustez
- **SNR < 5 dB**: Posible pérdida de conexión

Esta adaptación ocurre en tiempo real, ajustándose cada pocos milisegundos según las mediciones de calidad del canal reportadas por el dispositivo móvil.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **PSK** (Carta 27): QAM es una generalización de PSK que también varía la amplitud
- **Constelaciones** (Carta 28): QAM define constelaciones rectangulares en el plano I-Q
- **BER** (Carta 31): El desempeño de QAM se evalúa mediante curvas BER vs Eb/N0
- **Detección coherente** (Carta 32): QAM requiere detección coherente para demodulación

#### Dependencias (lo que necesitas saber primero)
1. **Señales ortogonales** → Entender por qué cos y sin no interfieren
2. **Mapeo de bits Gray** → Minimizar errores de bit en símbolos adyacentes
3. **Ruido AWGN** → Cómo afecta a la constelación QAM

#### Aplicaciones Posteriores (dónde usarás esto)
1. **OFDM**: Cada subportadora típicamente usa QAM
2. **MIMO**: Múltiples flujos QAM paralelos
3. **Diseño de sistemas**: Selección de orden QAM según requisitos

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La relación directa entre orden de QAM y eficiencia espectral
- El trade-off fundamental entre capacidad y robustez al aumentar M
- Cómo calcular tasas de bits y anchos de banda para diferentes órdenes
- Por qué QAM requiere mejor SNR que modulaciones más simples

#### Tipos de problemas típicos
1. **Cálculo de eficiencia espectral**: Dado M y el ancho de banda, calcular la tasa máxima
   - Estrategia: Aplicar $\eta = \log_2(M)$ y multiplicar por BW

2. **Diseño de enlace**: Seleccionar orden de QAM para cumplir requisitos de tasa y BER
   - Estrategia: Usar curvas BER vs Eb/N0 para diferentes M-QAM

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir símbolos con bits**
- Por qué ocurre: No recordar que cada símbolo QAM transmite múltiples bits
- Cómo evitarlo: Siempre calcular $\log_2(M)$ para obtener bits/símbolo
- Ejemplo de error: Asumir que 16-QAM transmite 16 bits (correcto: 4 bits)

❌ **Error #2: Ignorar el factor de roll-off en el ancho de banda**
- Por qué ocurre: Usar solo el ancho de banda de Nyquist teórico
- Cómo evitarlo: Considerar factor de roll-off α: $BW_{real} = R_s(1+\alpha)$

❌ **Error #3: Asumir que mayor M siempre es mejor**
- Distinción importante: Mayor M aumenta capacidad pero reduce robustez
- Requiere SNR más alta para mantener mismo BER

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Señal QAM: s(t) = I(t)cos(2πfct) - Q(t)sin(2πfct)
Eficiencia espectral: η = log₂(M) bits/s/Hz
Tasa de bits: Rb = Rs × log₂(M)
Potencia promedio: P = (2/3)(M-1)d² para M-QAM cuadrada
```

#### Conceptos Fundamentales
- ✓ **Ortogonalidad I-Q**: Permite dos canales independientes sin interferencia
- ✓ **Trade-off M**: Mayor M → mayor capacidad pero menor robustez
- ✓ **Constelación rectangular**: Puntos uniformemente espaciados en grilla
- ✓ **Detección coherente obligatoria**: Necesita recuperación de portadora precisa

#### Reglas Mnemotécnicas
- 🧠 **"QAM = Quantity And More"**: Más puntos, más bits, más SNR necesaria
- 🧠 **Potencias de 2**: M siempre es 2^n donde n es par para QAM cuadrada

#### Valores Típicos (para referencias rápidas)
| Sistema | Orden QAM Típico | Eficiencia | SNR mínima |
|---------|------------------|------------|------------|
| ADSL | 16-256 QAM | 4-8 bits/s/Hz | 15-25 dB |
| Cable TV | 64-256 QAM | 6-8 bits/s/Hz | 20-30 dB |
| WiFi 6 | 1024 QAM | 10 bits/s/Hz | >35 dB |
| 5G | hasta 256 QAM | 8 bits/s/Hz | >25 dB |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Proakis & Salehi Cap. 4.3-4.5 (análisis detallado de M-QAM)
- **Material del curso**: Prácticas de laboratorio con GNU Radio para visualizar constelaciones
- **Simulaciones**: MATLAB Communications Toolbox - qammod/qamdemod

#### Temas Relacionados para Explorar
1. Codificación Gray para minimizar BER
2. Ecualización adaptativa para combatir ISI en QAM
3. Peak-to-Average Power Ratio (PAPR) en sistemas multiportadora con QAM

#### Preguntas para Reflexionar
- ¿Por qué QAM rectangular es más común que QAM circular pese a ser menos eficiente en potencia?
- ¿Cómo afectaría un error de fase de 5° en la recuperación de portadora a 256-QAM vs QPSK?
- ¿Por qué los sistemas ópticos pueden usar órdenes de QAM mucho mayores que los inalámbricos?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 45 minutos
**Prerequisitos críticos**: PSK, constelaciones, detección coherente
**Tags**: `#modulacion-digital` `#qam` `#eficiencia-espectral` `#comunicaciones-modernas`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*