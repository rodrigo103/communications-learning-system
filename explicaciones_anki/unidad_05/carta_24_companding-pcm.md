# Carta 24: Companding en PCM - Optimización del Rango Dinámico

> **Unidad 5**: Modulación de Pulsos

---

## 🎯 Pregunta

¿Qué es el companding en PCM y por qué se utiliza?

---

## 📝 Respuesta Breve (de la carta original)

**Companding** = Compresión + Expansión

**Transmisor (compresor)**:
- Comprime el rango dinámico de la señal
- Señales débiles: mayor resolución
- Señales fuertes: menor resolución

**Receptor (expansor)**:
- Operación inversa, restaura rango original

**Por qué se usa**:
1. **SNR uniforme**: mejora SNR de señales débiles sin degradar las fuertes
2. **Rango dinámico efectivo**: mejor aprovechamiento de bits disponibles
3. **Percepción logarítmica**: se adapta a respuesta humana

**Leyes estándar**:
- **μ-law** (USA, Japón): μ = 255
- **A-law** (Europa): A = 87.6

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El **companding** (palabra compuesta de **compressing** y **expanding**) es una técnica fundamental en los sistemas PCM modernos que resuelve uno de los principales desafíos en la digitalización de señales analógicas: cómo mantener una calidad uniforme para señales con un amplio rango dinámico usando un número limitado de bits.

**¿Por qué es importante este concepto?** En sistemas de comunicaciones reales, especialmente en telefonía, las señales de voz tienen un rango dinámico de aproximadamente 40-60 dB. Esto significa que la señal más fuerte puede ser 10,000 veces más intensa que la más débil. Sin companding, necesitaríamos 12-14 bits por muestra para mantener calidad aceptable en todo el rango, lo cual es ineficiente y costoso en términos de ancho de banda.

**¿Dónde se aplica?** El companding es omnipresente en:
- **Telefonía digital**: todos los sistemas telefónicos digitales (PSTN, VoIP)
- **Audio profesional**: grabación y transmisión de audio
- **Comunicaciones satelitales**: optimización del enlace limitado en potencia
- **Telefonía móvil**: codecs de voz en GSM, 3G, 4G, 5G

**Historia relevante:** El companding fue desarrollado en Bell Labs en los años 1960s como parte del desarrollo de PCM para telefonía. Bernard Smith patentó la técnica en 1970, revolucionando la eficiencia de los sistemas telefónicos digitales. Las leyes μ (mu-law) y A-law fueron estandarizadas por ITU-T en la recomendación G.711 en 1972.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **PCM básico** (Carta 23): proceso de digitalización en tres etapas
- **Cuantificación uniforme**: división del rango en niveles equidistantes
- **Relación señal-ruido de cuantificación (SQNR)**: medida de calidad
- **Rango dinámico**: relación entre señal máxima y mínima

#### Desarrollo Paso a Paso

**Paso 1: El Problema con Cuantificación Uniforme**

En cuantificación uniforme con n bits, el paso de cuantificación es:
$$\Delta = \frac{V_{max} - V_{min}}{2^n}$$

El error de cuantificación máximo es $\pm\Delta/2$, constante para todas las amplitudes.

Para señales débiles (amplitud pequeña comparada con $\Delta$):
- SNR de cuantificación es **muy pobre**
- El error relativo es grande
- La señal puede perderse en el ruido de cuantificación

Para señales fuertes (amplitud grande):
- SNR de cuantificación es **buena**
- El error relativo es pequeño
- Se "desperdicia" resolución

**Paso 2: La Solución - Cuantificación No Uniforme**

La idea clave es usar **pasos de cuantificación variables**:
- Pasos pequeños para señales débiles → mejor resolución donde se necesita
- Pasos grandes para señales fuertes → suficiente calidad sin desperdiciar bits

Esto se logra mediante una función de compresión que "deforma" la señal antes de cuantificar uniformemente.

**Paso 3: Implementación del Companding**

El proceso completo es:
1. **Compresión**: $y = C(x)$ donde C es no-lineal
2. **Cuantificación uniforme** de y
3. **Transmisión digital**
4. **Expansión en receptor**: $x' = C^{-1}(y')$

La función de compresión debe ser **monótona creciente** e **invertible**.

#### Derivación Matemática

**Ley μ (mu-law) - Estándar Norteamericano:**

La función de compresión μ-law está definida como:

$$C_\mu(x) = \text{sgn}(x) \cdot \frac{\ln(1 + \mu|x/V_{max}|)}{\ln(1 + \mu)}$$

donde:
- $\mu$ = parámetro de compresión (típicamente 255)
- $V_{max}$ = voltaje máximo de entrada
- sgn(x) = función signo

**Derivación de la mejora en SNR:**

Para señales pequeñas, la pendiente de la curva de compresión es:
$$\frac{dC_\mu}{dx}\bigg|_{x\to 0} \approx \frac{\mu}{V_{max} \ln(1+\mu)}$$

Esto significa que las señales débiles se amplifican por este factor antes de cuantificar, mejorando su SNR efectivo.

**Ley A - Estándar Europeo:**

$$C_A(x) = \begin{cases}
\text{sgn}(x) \cdot \frac{A|x/V_{max}|}{1 + \ln(A)} & \text{si } |x| \leq \frac{V_{max}}{A} \\
\text{sgn}(x) \cdot \frac{1 + \ln(A|x/V_{max}|)}{1 + \ln(A)} & \text{si } |x| > \frac{V_{max}}{A}
\end{cases}$$

donde A = 87.6 típicamente.

**Mejora en rango dinámico:**

Con companding, el rango dinámico efectivo aumenta aproximadamente:
$$\Delta_{DR} \approx 20\log_{10}(\mu) \text{ dB}$$

Para μ = 255: mejora ≈ 48 dB

### 🔬 Intuición y Analogías

**Analogía principal:**
El companding es como un **sistema de iluminación automático con sensor** en fotografía. Cuando fotografías una escena con mucho contraste (sol brillante y sombras oscuras):
- Sin companding: como una cámara con exposición fija - las sombras quedan negras o las luces se queman
- Con companding: como HDR (High Dynamic Range) - ajusta la sensibilidad según el brillo local, capturando detalles en toda la escena

**Intuición física:**
El oído humano naturalmente realiza una forma de companding - percibimos sonidos en escala logarítmica. Una conversación susurrada y un grito tienen niveles muy diferentes, pero ambos son igualmente inteligibles. El companding digital imita esta característica perceptual.

**Visualización:**
Imagina una regla con marcas uniformes (cuantificación uniforme) vs. una regla logarítmica (con companding). En la regla logarítmica, hay más divisiones cerca del cero (mejor resolución para valores pequeños) y divisiones más espaciadas para valores grandes.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Comparación de SNR con y sin Companding

**Situación:** Digitalizar una señal de voz con rango dinámico de 40 dB usando PCM de 8 bits.

**Datos:**
| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Bits por muestra | 8 | bits |
| Rango dinámico de voz | 40 | dB |
| μ-law parameter | 255 | - |

**Solución paso a paso:**

1. **Sin companding (cuantificación uniforme):**
   $$SNR_{uniforme} = 6.02n + 1.76 = 6.02(8) + 1.76 = 49.92 \text{ dB}$$

   Pero esto es solo para señales cerca del máximo. Para señales a -40 dB:
   $$SNR_{débil} = 49.92 - 40 = 9.92 \text{ dB}$$ (inaceptable para voz)

2. **Con μ-law companding:**
   La mejora para señales débiles es aproximadamente:
   $$G_{companding} \approx 20\log_{10}(255) = 48.1 \text{ dB}$$

   SNR para señales débiles:
   $$SNR_{débil,comp} \approx 30-35 \text{ dB}$$ (calidad telefónica aceptable)

3. **Resultado:**
   $$\boxed{\text{Mejora de } \approx 20-25 \text{ dB para señales débiles}}$$

**Interpretación:** El companding permite calidad telefónica aceptable en todo el rango dinámico con solo 8 bits/muestra.

---

#### Ejemplo 2: Sistema Telefónico Digital T1 (Aplicación Real)

**Contexto:** Canal de voz en sistema T1 norteamericano usando μ-law PCM.

**Especificaciones del sistema:**
- Frecuencia de muestreo: 8000 Hz (Nyquist para voz 0-4 kHz)
- Bits por muestra: 8 bits (con μ-law)
- Tasa de bits por canal: 64 kbps
- μ = 255 (estándar ITU-T G.711)

**Proceso de una palabra hablada "Hola" (nivel medio -20 dBm):**

1. **Señal analógica de entrada:** -20 dBm (10 mW en 600Ω)
2. **Después de compresión μ-law:** señal mapeada al 60% del rango
3. **Cuantificación:** asignada al nivel 153 de 256 posibles
4. **Código binario transmitido:** 10011001
5. **En receptor:** expansión restaura nivel original -20 dBm

**Comparación con susurro (-40 dBm):**
- Sin companding: usaría solo 6 niveles de 256 (SNR pobre)
- Con companding: usa ~40 niveles (SNR aceptable)

---

#### Ejemplo 3: Análisis de Casos Límite

**¿Qué pasa cuando...?**

**Caso 1: μ → 0 (sin compresión)**
$$\lim_{\mu \to 0} C_\mu(x) = x$$
El sistema degenera a PCM uniforme, perdiendo los beneficios del companding.

**Caso 2: μ → ∞ (compresión máxima)**
$$\lim_{\mu \to \infty} C_\mu(x) = \text{sgn}(x)$$
Compresión extrema, convierte el sistema en un comparador de 1 bit.

**Caso 3: Señal exactamente en V_max/A (frontera en A-law)**
En este punto, la ley A cambia de comportamiento lineal a logarítmico, asegurando continuidad pero con cambio en la pendiente de la curva de compresión.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **PCM básico** (Carta 23): El companding es una mejora directa del PCM estándar
- **Modulación Delta Adaptativa** (Carta 25): Usa un concepto similar de paso variable
- **TDM** (Carta 26): Los sistemas TDM telefónicos usan companding en cada canal
- **Teoría de la Información** (Unidad 9): Companding es una forma de codificación fuente

#### Dependencias (lo que necesitas saber primero)
1. **Cuantificación y error de cuantificación** → Para entender qué problema resuelve
2. **SNR y rango dinámico** → Para medir la mejora
3. **Proceso PCM completo** → Dónde encaja el companding

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Codecs de voz modernos**: G.711 es base para VoIP
2. **Audio digital**: Conceptos similares en compresión MP3, AAC
3. **Procesamiento de imágenes**: HDR usa principios análogos

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- **No es memorizar las fórmulas** de μ-law o A-law exactas
- **Sí entender el principio**: cuantificación no uniforme mejora SNR para señales débiles
- **Saber calcular** la mejora aproximada en dB
- **Reconocer aplicaciones** donde el companding es crítico

#### Tipos de problemas típicos
1. **Comparación cuantitativa**: Calcular SNR con/sin companding para diferentes niveles de señal
   - Estrategia: Usar fórmula de mejora aproximada

2. **Diseño de sistema**: Elegir entre μ-law y A-law para una aplicación
   - Estrategia: Considerar compatibilidad regional y requisitos específicos

3. **Análisis de rango dinámico**: Determinar si se necesita companding
   - Estrategia: Comparar rango dinámico de señal con capacidad del cuantificador

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir companding con compresión de datos**
- Por qué ocurre: Ambos "comprimen" pero son conceptos diferentes
- Cómo evitarlo: Companding no reduce bits, redistribuye resolución
- Ejemplo de error: "El companding reduce la tasa de bits" - FALSO

❌ **Error #2: Pensar que μ-law y A-law son intercambiables**
- Por qué ocurre: Ambas hacen companding
- Cómo evitarlo: Son incompatibles, causan distorsión si se mezclan
- Distinción: μ-law (América/Japón) vs A-law (Europa/resto del mundo)

❌ **Error #3: Olvidar la expansión en el receptor**
- Por qué ocurre: Focus excesivo en la compresión
- Cómo evitarlo: Recordar que es un proceso de dos pasos complementarios
- Sin expansión correcta: distorsión severa de la señal

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Mejora aproximada: ΔDR ≈ 20log₁₀(μ) dB
SNR con companding uniforme para todo el rango
μ-law: μ = 255 (estándar norteamericano)
A-law: A = 87.6 (estándar europeo)
```

#### Conceptos Fundamentales
- ✓ **Principio básico**: "Más resolución donde más se necesita"
- ✓ **Beneficio clave**: SNR uniforme en todo el rango dinámico
- ✓ **Implementación**: Compresión → Cuantificación uniforme → Expansión
- ✓ **Compatibilidad**: μ-law y A-law NO son compatibles entre sí

#### Reglas Mnemotécnicas
- 🧠 **"COMPress AND EXPand = COMPAND"**: Recordar ambas operaciones
- 🧠 **"μSA, A-Europe"**: μ-law en USA, A-law en Europa
- 🧠 **"255 y 87.6"**: Valores estándar de μ y A

#### Valores Típicos (para referencias rápidas)
| Parámetro | Valor Típico | Aplicación |
|-----------|--------------|------------|
| μ | 255 | Telefonía G.711 μ-law |
| A | 87.6 | Telefonía G.711 A-law |
| Mejora DR (μ=255) | ~48 dB | Rango dinámico adicional |
| Bits típicos con companding | 8 | Calidad telefónica |
| Bits sin companding equivalente | 12-14 | Para mismo rango dinámico |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - Haykin, "Communication Systems", Cap. 6.4-6.5
  - Proakis & Salehi, "Digital Communications", Sección sobre PCM no uniforme
- **Estándares**: ITU-T G.711 (especificación completa de μ-law y A-law)
- **Simulaciones**: MATLAB tiene funciones `compand` y `quantiz` para experimentar

#### Temas Relacionados para Explorar
1. **Companding instantáneo vs. silábico**: Diferentes escalas temporales
2. **Cuantificación vectorial**: Extensión multidimensional
3. **Codecs perceptuales modernos**: MP3, AAC usan principios similares

#### Preguntas para Reflexionar
- ¿Por qué se eligió μ=255 y no 256 (potencia de 2)?
- ¿Cómo afectaría usar companding en señales que no son de voz?
- ¿Se podría diseñar una ley de companding óptima para música vs. voz?
- ¿Qué pasaría si se aplica doble companding por error?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 25 minutos
**Prerequisitos críticos**: PCM básico, cuantificación, SNR
**Tags**: `#pcm` `#companding` `#cuantificacion` `#telefonia` `#g711`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*