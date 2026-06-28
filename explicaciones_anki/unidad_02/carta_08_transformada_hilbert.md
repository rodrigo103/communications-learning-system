# Carta 8: Transformada de Hilbert y Señales Analíticas

> **Unidad 2**: Análisis de Señales

---

## 🎯 Pregunta

¿Qué es la Transformada de Hilbert y cuál es su aplicación en comunicaciones?

---

## 📝 Respuesta Breve (de la carta original)

La Transformada de Hilbert $\hat{x}(t)$ de una señal $x(t)$ produce un **desfasaje de -90° para todas las frecuencias**.

**Aplicaciones principales**:
1. **Señal analítica**: $x_a(t) = x(t) + j\hat{x}(t)$ permite representar señales reales como complejas
2. **Modulación BLU**: permite generar banda lateral única matemáticamente
3. **Demodulación**: facilita la detección de envolvente y fase
4. **Análisis de modulaciones**: separación de componentes en fase y cuadratura

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La Transformada de Hilbert es una herramienta matemática fundamental que permite crear una versión "en cuadratura" de cualquier señal real. Esta transformación es esencial en comunicaciones modernas porque proporciona una forma elegante de representar y procesar señales moduladas, facilitando operaciones que serían complejas o imposibles trabajando solo con señales reales.

**¿Por qué es importante este concepto?** En sistemas de comunicaciones, constantemente necesitamos extraer información de amplitud y fase de señales moduladas. La Transformada de Hilbert nos permite construir una representación compleja (señal analítica) a partir de una señal real, lo que simplifica enormemente el análisis de envolvente, fase instantánea, y frecuencia instantánea. Sin esta herramienta, operaciones como la generación de banda lateral única (SSB) o la demodulación coherente serían mucho más complicadas.

**¿Dónde se aplica?** La Transformada de Hilbert aparece en numerosas aplicaciones prácticas: generación de señales SSB en transmisores de radio HF, procesamiento de señales de radar para detección Doppler, análisis de señales biomédicas (ECG, EEG), demodulación de señales AM y FM en receptores SDR (Software Defined Radio), y en el procesamiento de señales de sonar y ultrasonido.

**Historia**: David Hilbert introdujo esta transformación en 1905 como parte de su trabajo en análisis matemático. Sin embargo, su aplicación a comunicaciones fue desarrollada décadas después, especialmente con el trabajo de Dennis Gabor en 1946 sobre señales analíticas. La importancia práctica creció con el desarrollo de la radio de banda lateral única y posteriormente con el procesamiento digital de señales.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Transformada de Fourier**: descomposición de señales en componentes frecuenciales
- **Números complejos**: representación y operaciones con señales complejas
- **Fase y amplitud**: componentes de una señal sinusoidal
- **Sistemas LTI**: la Transformada de Hilbert es un sistema lineal e invariante

#### Desarrollo Paso a Paso

**Paso 1: Definición matemática básica**

La Transformada de Hilbert de una señal x(t) se define como:

$$\hat{x}(t) = \mathcal{H}\{x(t)\} = \frac{1}{\pi} \text{P.V.} \int_{-\infty}^{\infty} \frac{x(\tau)}{t-\tau} d\tau$$

Donde P.V. denota el valor principal de Cauchy (para manejar la singularidad en τ = t).

Esta integral puede interpretarse como una convolución:
$$\hat{x}(t) = x(t) * \frac{1}{\pi t}$$

**Paso 2: Respuesta en frecuencia del transformador de Hilbert**

En el dominio de la frecuencia, la Transformada de Hilbert tiene una función de transferencia particularmente simple:

$$H(f) = -j \cdot \text{sgn}(f) = \begin{cases}
-j & \text{para } f > 0 \\
0 & \text{para } f = 0 \\
+j & \text{para } f < 0
\end{cases}$$

Esto significa que:
- Frecuencias positivas: desfasaje de -90° (multiplicación por -j)
- Frecuencias negativas: desfasaje de +90° (multiplicación por +j)
- DC (f = 0): se elimina completamente

**Paso 3: Construcción de la señal analítica**

La señal analítica se construye combinando la señal original con su Transformada de Hilbert:

$$x_a(t) = x(t) + j\hat{x}(t)$$

Esta señal compleja tiene la propiedad especial de que su espectro solo contiene frecuencias positivas:

$$X_a(f) = \begin{cases}
2X(f) & \text{para } f > 0 \\
X(0) & \text{para } f = 0 \\
0 & \text{para } f < 0
\end{cases}$$

#### Derivación Matemática

**Partiendo de una señal coseno simple:**

$$x(t) = A\cos(2\pi f_0 t + \phi)$$

**Aplicando la Transformada de Hilbert:**

Sabemos que H(f) = -j·sgn(f), entonces para nuestra señal coseno:

$$X(f) = \frac{A}{2}[\delta(f-f_0)e^{j\phi} + \delta(f+f_0)e^{-j\phi}]$$

**Aplicando H(f):**

$$\hat{X}(f) = H(f) \cdot X(f) = -j \cdot \frac{A}{2}\delta(f-f_0)e^{j\phi} + j \cdot \frac{A}{2}\delta(f+f_0)e^{-j\phi}$$

**Transformada inversa:**

$$\hat{x}(t) = A\sin(2\pi f_0 t + \phi)$$

**Resultado fundamental:**
$$\boxed{\mathcal{H}\{A\cos(2\pi f_0 t + \phi)\} = A\sin(2\pi f_0 t + \phi)}$$

**Significado físico:**
- La Transformada de Hilbert convierte cosenos en senos
- Mantiene la amplitud constante
- Produce exactamente 90° de desfasaje para cualquier frecuencia

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina que tienes una onda en la superficie del agua vista desde un costado (señal real). La Transformada de Hilbert es como ver la misma onda pero desde una posición rotada 90° alrededor del eje de propagación. Ambas vistas describen la misma onda, pero desde perspectivas ortogonales. Combinar ambas vistas (señal analítica) te da una descripción completa del movimiento circular que realiza cada partícula de agua.

**Intuición física:**
Cuando una señal real pasa por el transformador de Hilbert, cada componente sinusoidal se convierte en su versión "en cuadratura" (90° desfasada). Es como si cada frecuencia pasara por un desfasador perfecto de -90°. Esto es notable porque el desfasaje es independiente de la frecuencia (excepto el signo para frecuencias negativas).

**Visualización:**
En el plano complejo, si la señal original x(t) representa la proyección sobre el eje real de un fasor rotante, entonces la Transformada de Hilbert $\hat{x}(t)$ representa la proyección sobre el eje imaginario del mismo fasor. La señal analítica x_a(t) = x(t) + j$\hat{x}(t)$ es el fasor completo rotando.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Generación de Señal SSB-USB

**Situación:** Queremos transmitir una señal de voz m(t) = cos(2π·1000t) + 0.5cos(2π·3000t) usando modulación de banda lateral superior (USB) con portadora en 100 kHz.

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| f_c | 100,000 | Hz |
| f_m1 | 1,000 | Hz |
| f_m2 | 3,000 | Hz |
| A_m1 | 1.0 | - |
| A_m2 | 0.5 | - |

**Solución paso a paso:**

1. **Calcular la Transformada de Hilbert de m(t):**
   $$\hat{m}(t) = \sin(2\pi \cdot 1000t) + 0.5\sin(2\pi \cdot 3000t)$$

2. **Generar la señal SSB-USB:**
   $$s_{USB}(t) = m(t)\cos(2\pi f_c t) - \hat{m}(t)\sin(2\pi f_c t)$$

3. **Expandiendo:**
   $$s_{USB}(t) = \cos(2\pi \cdot 101,000t) + 0.5\cos(2\pi \cdot 103,000t)$$

**Interpretación:** La señal resultante solo contiene las frecuencias laterales superiores (101 kHz y 103 kHz). Las frecuencias laterales inferiores (99 kHz y 97 kHz) han sido completamente suprimidas gracias a la Transformada de Hilbert.

---

#### Ejemplo 2: Detección de Envolvente Compleja en AM

**Contexto:** Una señal AM con modulación del 80% y portadora en 1 MHz necesita ser demodulada. La señal moduladora es un tono de 1 kHz.

**Señal AM recibida:**
$$r(t) = [1 + 0.8\cos(2\pi \cdot 1000t)]\cos(2\pi \cdot 10^6 t)$$

**Proceso usando Transformada de Hilbert:**

1. **Calcular $\hat{r}(t)$:**
   $$\hat{r}(t) = [1 + 0.8\cos(2\pi \cdot 1000t)]\sin(2\pi \cdot 10^6 t)$$

2. **Formar la señal analítica:**
   $$r_a(t) = r(t) + j\hat{r}(t) = [1 + 0.8\cos(2\pi \cdot 1000t)]e^{j2\pi \cdot 10^6 t}$$

3. **Extraer la envolvente:**
   $$|r_a(t)| = |1 + 0.8\cos(2\pi \cdot 1000t)|$$

**Resultado:** La envolvente compleja nos da directamente la información moduladora, sin necesidad de filtrado adicional.

---

#### Ejemplo 3: Análisis de Frecuencia Instantánea en FM

**¿Qué pasa cuando aplicamos la Transformada de Hilbert a una señal FM?**

**Señal FM:**
$$s(t) = A\cos\left(2\pi f_c t + 2\pi k_f \int m(\tau)d\tau\right)$$

**Transformada de Hilbert:**
$$\hat{s}(t) = A\sin\left(2\pi f_c t + 2\pi k_f \int m(\tau)d\tau\right)$$

**Señal analítica:**
$$s_a(t) = Ae^{j(2\pi f_c t + 2\pi k_f \int m(\tau)d\tau)}$$

**Frecuencia instantánea:**
$$f_i(t) = \frac{1}{2\pi}\frac{d\phi(t)}{dt} = f_c + k_f m(t)$$

La Transformada de Hilbert permite extraer directamente la frecuencia instantánea, fundamental para demodulación FM.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Teorema de Convolución** (Carta 7): La Transformada de Hilbert es una convolución con 1/(πt)
- **Modulación SSB** (Carta 11): Usa directamente la Transformada de Hilbert para suprimir una banda lateral
- **Señales de energía vs potencia** (Carta 9): La Transformada de Hilbert preserva la energía/potencia

#### Dependencias (lo que necesitas saber primero)
1. Transformada de Fourier → Para entender la respuesta en frecuencia H(f) = -j·sgn(f)
2. Números complejos → Para trabajar con señales analíticas
3. Convolución → La Transformada de Hilbert es una convolución especial

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Modulación SSB/VSB**: Generación eficiente de banda lateral única
2. **Demodulación coherente**: Extracción de componentes I/Q
3. **Procesamiento de radar**: Detección de blancos móviles vía procesamiento Doppler

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La Transformada de Hilbert NO cambia el contenido de frecuencias, solo las fases
- La señal analítica elimina redundancia de frecuencias negativas
- Es una herramienta de análisis, no siempre se implementa físicamente
- La relación cos → sin es el caso más simple pero fundamental

#### Tipos de problemas típicos
1. **Cálculo directo**: Hallar la Transformada de Hilbert de señales simples
   - Estrategia: Memorizar pares básicos (cos→sin, sin→-cos)

2. **Aplicación a modulación**: Generar señales SSB o analizar AM/FM
   - Estrategia: Usar la señal analítica para simplificar cálculos

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Pensar que la Transformada de Hilbert amplifica o atenúa**
- Por qué ocurre: El desfasaje puede parecer una modificación de amplitud
- Cómo evitarlo: Recordar que |H(f)| = 1 para todo f ≠ 0
- La energía se conserva completamente

❌ **Error #2: Aplicar la transformada a señales complejas**
- Por qué ocurre: Confusión con la definición
- Cómo evitarlo: La Transformada de Hilbert solo se define para señales reales

❌ **Error #3: Olvidar el cambio de signo para senos**
- Distinción importante: H{cos(ωt)} = sin(ωt), pero H{sin(ωt)} = -cos(ωt)

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Transformada de Hilbert: H(f) = -j·sgn(f)
Señal analítica: x_a(t) = x(t) + j·ĥ(t)
Par fundamental: H{cos(ωt)} = sin(ωt)
SSB-USB: s(t) = m(t)cos(ωct) - m̂(t)sin(ωct)
```

#### Conceptos Fundamentales
- ✓ **Desfasaje universal**: -90° para todas las frecuencias positivas
- ✓ **Preservación de energía**: La transformada no cambia la potencia
- ✓ **Eliminación de redundancia**: La señal analítica no tiene frecuencias negativas

#### Reglas Mnemotécnicas
- 🧠 **"Hilbert Hace Senos"**: Cosenos se convierten en senos
- 🧠 **"Analítica = Real + j·Hilbert"**: Construcción de señal analítica

#### Valores Típicos (para referencias rápidas)

| Señal x(t) | Transformada de Hilbert ĥ(t) |
|------------|-------------------------------|
| cos(ωt) | sin(ωt) |
| sin(ωt) | -cos(ωt) |
| δ(t) | 1/(πt) |
| 1/(πt) | -δ(t) |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Carlson "Communication Systems" Cap. 6 (SSB generation)
- **Material del curso**: Laboratorio de generación SSB con MATLAB
- **Simulaciones**: Python scipy.signal.hilbert(), GNU Radio Hilbert block

#### Temas Relacionados para Explorar
1. Transformada de Hilbert discreta y su implementación FIR
2. Relaciones de Kramers-Kronig en sistemas causales
3. Aplicaciones en procesamiento de imágenes (detección de bordes)

#### Preguntas para Reflexionar
- ¿Por qué la Transformada de Hilbert de una constante es cero?
- ¿Cómo se relaciona la causalidad con la Transformada de Hilbert?
- ¿Qué ventajas tiene trabajar con señales analíticas en lugar de señales reales?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 50 minutos
**Prerequisitos críticos**: Transformada de Fourier, Números complejos, Convolución
**Tags**: `#hilbert` `#señal-analitica` `#ssb` `#cuadratura`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*