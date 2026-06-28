# Carta 7: Teorema de Convolución y Sistemas LTI

> **Unidad 2**: Análisis de Señales

---

## 🎯 Pregunta

Explique el Teorema de Convolución en el dominio del tiempo y su importancia en sistemas lineales.

---

## 📝 Respuesta Breve (de la carta original)

El Teorema de Convolución establece que:
$$y(t) = x(t) * h(t) \quad \Leftrightarrow \quad Y(f) = X(f) \cdot H(f)$$

**Importancia**:
- La convolución en el tiempo equivale a multiplicación en frecuencia
- Permite analizar sistemas LTI más fácilmente en el dominio frecuencial
- La respuesta de un sistema es: entrada ⊗ respuesta al impulso
- Fundamental para entender filtrado, modulación y procesamiento de señales

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El Teorema de Convolución es uno de los pilares fundamentales del procesamiento de señales y sistemas de comunicaciones. Este teorema establece una relación elegante y poderosa entre dos operaciones aparentemente diferentes: la convolución en el dominio del tiempo y la multiplicación en el dominio de la frecuencia.

**¿Por qué es importante este concepto?** En sistemas de comunicaciones, constantemente procesamos señales a través de filtros, moduladores, canales de transmisión y otros sistemas. Cada uno de estos elementos modifica la señal de entrada de alguna manera. El teorema de convolución nos proporciona dos formas equivalentes de analizar estos efectos: una en el dominio temporal (convolución) y otra en el dominio frecuencial (multiplicación). Esta dualidad es crucial porque algunos análisis son más simples en un dominio que en el otro.

**¿Dónde se aplica?** Este teorema aparece en prácticamente todos los aspectos de las comunicaciones modernas: el diseño de filtros en receptores WiFi, el análisis del efecto de canales multipaso en comunicaciones celulares, el procesamiento de audio en codecs de voz, la ecualización en módems DSL, y el análisis de distorsión en amplificadores de radiofrecuencia.

**Historia**: El concepto de convolución fue desarrollado de manera independiente por varios matemáticos, pero su aplicación sistemática a sistemas lineales fue formalizada por Norbert Wiener y otros en la primera mitad del siglo XX. La conexión con la transformada de Fourier, estableciendo el teorema de convolución, revolucionó el análisis de sistemas y señales.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Sistemas LTI (Lineales e Invariantes en el Tiempo)**: sistemas cuya salida para una combinación lineal de entradas es la misma combinación lineal de las salidas individuales, y cuyo comportamiento no cambia con el tiempo
- **Transformada de Fourier**: herramienta matemática que descompone una señal en sus componentes frecuenciales
- **Respuesta al impulso h(t)**: salida del sistema cuando la entrada es un impulso δ(t)
- **Integral de convolución**: operación matemática que combina dos funciones

#### Desarrollo Paso a Paso

**Paso 1: La operación de convolución en el tiempo**

La convolución de dos señales x(t) y h(t) se define matemáticamente como:

$$y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau$$

Esta integral puede interpretarse como: "para cada instante t, multiplica x(τ) por una versión reflejada y desplazada de h, luego integra sobre todo τ". Es como deslizar una función sobre la otra, calculando el área bajo el producto en cada posición.

**Paso 2: Transformada de Fourier de la convolución**

Cuando aplicamos la transformada de Fourier a la convolución:

$$\mathcal{F}\{y(t)\} = \mathcal{F}\{x(t) * h(t)\}$$

El resultado fundamental es:

$$Y(f) = X(f) \cdot H(f)$$

Donde Y(f), X(f) y H(f) son las transformadas de Fourier de y(t), x(t) y h(t) respectivamente.

**Paso 3: La operación inversa también es cierta**

Si multiplicamos dos señales en el dominio del tiempo:

$$z(t) = x(t) \cdot h(t)$$

Su transformada de Fourier es:

$$Z(f) = X(f) * H(f)$$

La multiplicación en tiempo corresponde a convolución en frecuencia.

#### Derivación Matemática

**Partiendo de la definición de convolución:**

$$y(t) = \int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau$$

**Aplicando la transformada de Fourier:**

$$Y(f) = \int_{-\infty}^{\infty} y(t) e^{-j2\pi ft} dt$$

$$Y(f) = \int_{-\infty}^{\infty} \left[\int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau\right] e^{-j2\pi ft} dt$$

**Intercambiando el orden de integración (teorema de Fubini):**

$$Y(f) = \int_{-\infty}^{\infty} x(\tau) \left[\int_{-\infty}^{\infty} h(t-\tau) e^{-j2\pi ft} dt\right] d\tau$$

**Haciendo el cambio de variable u = t - τ:**

$$Y(f) = \int_{-\infty}^{\infty} x(\tau) \left[\int_{-\infty}^{\infty} h(u) e^{-j2\pi f(u+\tau)} du\right] d\tau$$

$$Y(f) = \int_{-\infty}^{\infty} x(\tau) e^{-j2\pi f\tau} \left[\int_{-\infty}^{\infty} h(u) e^{-j2\pi fu} du\right] d\tau$$

**Reconociendo las transformadas de Fourier:**

$$\boxed{Y(f) = X(f) \cdot H(f)}$$

**Significado físico de cada término:**
- $Y(f)$: espectro de la señal de salida del sistema
- $X(f)$: espectro de la señal de entrada
- $H(f)$: función de transferencia del sistema (respuesta en frecuencia)

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina el proceso de convolución como aplicar un "filtro fotográfico" a una imagen. En el dominio del tiempo (la imagen original), aplicar el filtro requiere un proceso complejo pixel por pixel (convolución). Pero si transformamos la imagen al dominio de frecuencias (como descomponerla en patrones de diferentes tamaños), aplicar el filtro es tan simple como ajustar la intensidad de cada patrón (multiplicación). El teorema de convolución nos dice que ambos procesos dan exactamente el mismo resultado.

**Intuición física:**
Cuando una señal pasa por un sistema físico (como un cable, un amplificador, o el aire), cada componente frecuencial de la señal es afectada de manera independiente. Algunas frecuencias pueden ser atenuadas, otras amplificadas, y todas pueden sufrir diferentes retrasos. La función de transferencia H(f) captura exactamente cómo cada frecuencia es modificada. La multiplicación X(f)·H(f) representa este proceso de modificación frecuencia por frecuencia.

**Visualización:**
Piensa en el espectro de una señal como un ecualizador gráfico de audio con infinitas bandas. La función de transferencia H(f) actúa como los controles deslizantes de cada banda: sube o baja la intensidad de cada frecuencia. El resultado Y(f) es simplemente el espectro de entrada con cada banda ajustada según H(f).

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Filtro Pasa-Bajos RC Simple

**Situación:** Un circuito RC actúa como filtro pasa-bajos con frecuencia de corte fc = 1 kHz. Queremos analizar su efecto sobre una señal cuadrada de 500 Hz.

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| R | 159.15 | Ω |
| C | 1 | μF |
| fc | 1000 | Hz |
| f_señal | 500 | Hz |

**Solución paso a paso:**

1. **Función de transferencia del filtro RC:**
   $$H(f) = \frac{1}{1 + j2\pi fRC} = \frac{1}{1 + jf/f_c}$$

2. **Espectro de la señal cuadrada (primeros armónicos):**
   - Fundamental (500 Hz): amplitud = 4/π
   - 3er armónico (1500 Hz): amplitud = 4/(3π)
   - 5to armónico (2500 Hz): amplitud = 4/(5π)

3. **Aplicación del teorema de convolución:**
   - Y(500 Hz) = X(500 Hz) × H(500 Hz) = (4/π) × 0.894∠-26.6°
   - Y(1500 Hz) = X(1500 Hz) × H(1500 Hz) = (4/3π) × 0.555∠-56.3°
   - Y(2500 Hz) = X(2500 Hz) × H(2500 Hz) = (4/5π) × 0.371∠-68.2°

**Interpretación:** El filtro atenúa progresivamente los armónicos superiores, convirtiendo la señal cuadrada en una forma más sinusoidal. Esto demuestra cómo la multiplicación en frecuencia (simple) equivale a la convolución en tiempo (compleja).

---

#### Ejemplo 2: Canal de Comunicación con Multitrayecto

**Contexto:** Una señal WiFi en 2.4 GHz experimenta reflexión en las paredes, creando un canal con dos caminos: directo y reflejado.

**Modelo del canal:**
- Camino directo: h₁(t) = δ(t) (sin atenuación)
- Camino reflejado: h₂(t) = 0.5δ(t - 50ns) (atenuado al 50%, retrasado 50 ns)

**Respuesta al impulso total:**
$$h(t) = \delta(t) + 0.5\delta(t - 50ns)$$

**Función de transferencia (aplicando Fourier):**
$$H(f) = 1 + 0.5e^{-j2\pi f \cdot 50ns}$$

**Efecto sobre una subportadora OFDM:**
Para f = 2.4 GHz + 10 MHz (una subportadora):
$$|H(f)| = |1 + 0.5e^{-j\pi}| = |1 - 0.5| = 0.5$$

**Resultado:** Esta frecuencia específica sufre desvanecimiento profundo (atenuación del 50%) debido a la interferencia destructiva entre los dos caminos.

---

#### Ejemplo 3: Convolución para Matched Filtering

**¿Qué pasa cuando convolucionamos una señal con su versión invertida en tiempo?**

Para detección óptima en presencia de ruido:
- Señal transmitida: s(t) = pulso rectangular de duración T
- Filtro adaptado: h(t) = s(T - t) (versión reflejada)

**Salida:**
$$y(t) = s(t) * h(t)$$

En frecuencia:
$$Y(f) = S(f) \cdot S^*(f) = |S(f)|^2$$

**Resultado:** La salida tiene máxima energía en t = T, maximizando la SNR en el instante de decisión. Este es el principio del matched filter, fundamental en receptores digitales.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Teorema del Muestreo** (Carta 5): El muestreo puede verse como multiplicación por tren de impulsos, que en frecuencia se convierte en convolución con otro tren de impulsos
- **Densidad Espectral de Potencia** (Carta 6): La DEP de la salida de un sistema LTI es |H(f)|²·Sx(f)
- **Transformada de Hilbert** (Carta 8): Es un caso especial de sistema LTI con H(f) = -j·sgn(f)

#### Dependencias (lo que necesitas saber primero)
1. Transformada de Fourier → Necesaria para entender el dominio frecuencial
2. Sistemas LTI → Base conceptual para aplicar el teorema
3. Integral de convolución → Operación matemática fundamental

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Modulación AM/FM**: El proceso de modulación es una multiplicación en tiempo, que se convierte en convolución en frecuencia
2. **Diseño de filtros**: Especificar H(f) deseado y obtener h(t) vía transformada inversa
3. **Ecualización**: Compensar distorsión del canal diseñando un filtro con H_eq(f) = 1/H_canal(f)

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La dualidad tiempo-frecuencia no es coincidencia, es una propiedad fundamental
- Saber cuándo es más conveniente trabajar en tiempo vs. frecuencia
- La capacidad de pasar fluidamente entre dominios según conveniencia
- Entender que H(f) caracteriza completamente un sistema LTI

#### Tipos de problemas típicos
1. **Análisis de filtros**: Dado h(t) o H(f), encontrar la salida para una entrada específica
   - Estrategia: Si la entrada tiene pocas componentes frecuenciales, usar dominio de frecuencia

2. **Diseño de sistemas**: Especificar H(f) para lograr cierto procesamiento
   - Estrategia: Trabajar en frecuencia para el diseño, luego obtener h(t) si se necesita implementación temporal

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir convolución con correlación**
- Por qué ocurre: Ambas involucran integrales similares
- Cómo evitarlo: Recordar que convolución usa h(t-τ) (reflexión), correlación usa h(t+τ)
- Ejemplo de error: En matched filtering, el filtro es h(t) = s(-t), no s(t)

❌ **Error #2: Olvidar que la convolución es conmutativa**
- Por qué ocurre: La integral parece asimétrica
- Cómo evitarlo: x(t)*h(t) = h(t)*x(t), siempre verdadero

❌ **Error #3: Aplicar el teorema cuando el sistema no es LTI**
- Distinción importante: El teorema SOLO aplica para sistemas lineales e invariantes en el tiempo

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Convolución temporal: y(t) = x(t) * h(t) = ∫x(τ)h(t-τ)dτ
Multiplicación frecuencial: Y(f) = X(f) · H(f)
Dualidad: x(t)·h(t) ↔ X(f)*H(f)
```

#### Conceptos Fundamentales
- ✓ **Equivalencia fundamental**: Convolución en tiempo = Multiplicación en frecuencia
- ✓ **Simplificación computacional**: Multiplicar es más simple que convolucionar
- ✓ **Caracterización completa**: H(f) o h(t) definen completamente un sistema LTI

#### Reglas Mnemotécnicas
- 🧠 **"ConvT = MultF"**: Convolución en Tiempo = Multiplicación en Frecuencia
- 🧠 **"FFT para filtrar"**: Para filtros largos, es más eficiente usar FFT → multiplicar → IFFT

#### Valores Típicos (para referencias rápidas)

| Sistema | h(t) típico | H(f) típico |
|---------|------------|-------------|
| Filtro RC | exponencial decayente | 1/(1+jf/fc) |
| Canal ideal | δ(t) | 1 |
| Retardo puro | δ(t-τ) | e^(-j2πfτ) |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Oppenheim & Willsky "Señales y Sistemas" Cap. 3
- **Material del curso**: Práctica de laboratorio sobre filtrado digital
- **Simulaciones**: MATLAB función conv(), Python scipy.signal.convolve

#### Temas Relacionados para Explorar
1. Convolución circular y su relación con DFT
2. Algoritmos rápidos de convolución (overlap-add, overlap-save)
3. Deconvolución y problemas inversos

#### Preguntas para Reflexionar
- ¿Por qué la convolución con δ(t) devuelve la misma señal?
- ¿Qué pasa si H(f) = 0 para alguna frecuencia? ¿Es invertible el sistema?
- ¿Cómo se relaciona el ancho de h(t) con el ancho de banda de H(f)?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 45 minutos
**Prerequisitos críticos**: Transformada de Fourier, Sistemas LTI
**Tags**: `#convolucion` `#sistemas-lti` `#fourier` `#filtrado`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*