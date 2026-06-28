# Carta 4: Teorema de Parseval - Conservación de Energía en el Dominio Frecuencial

> **Unidad 2**: Análisis de Señales

---

## 🎯 Pregunta

Enuncie y explique el Teorema de Parseval. ¿Qué interpretación física tiene?

---

## 📝 Respuesta Breve (de la carta original)

El Teorema de Parseval establece que:
$$\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df$$

**Interpretación física**: La energía total de una señal en el dominio del tiempo es igual a la energía total en el dominio de la frecuencia. Esto demuestra que la Transformada de Fourier conserva la energía, y permite calcular la energía de una señal integrando su densidad espectral de energía.

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El **Teorema de Parseval** es uno de los pilares fundamentales del análisis de señales, estableciendo un puente crítico entre las representaciones temporal y frecuencial de una señal. Su importancia radica en que garantiza que no se pierde ni se crea energía cuando transformamos una señal entre dominios, un principio fundamental que tiene profundas implicaciones tanto teóricas como prácticas.

En **sistemas de comunicaciones**, este teorema es esencial porque permite analizar la distribución de energía de las señales en frecuencia, lo que es crucial para el diseño de filtros, la asignación de espectro, y el análisis de interferencias. Por ejemplo, cuando diseñamos un sistema WiFi, necesitamos saber exactamente cuánta energía de nuestra señal cae dentro del canal asignado y cuánta podría interferir con canales adyacentes.

**Históricamente**, el teorema fue desarrollado por Marc-Antoine Parseval des Chênes en 1799, inicialmente en el contexto de series de Fourier. Más tarde, fue generalizado para la transformada de Fourier continua, convirtiéndose en una herramienta fundamental para el análisis de señales no periódicas.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Transformada de Fourier**: Debe conocerse la relación entre x(t) y X(f)
- **Energía de una señal**: Concepto de integral del cuadrado de la amplitud
- **Densidad espectral de energía**: |X(f)|² como distribución de energía en frecuencia

#### Desarrollo Paso a Paso

**Paso 1: Definición de Energía en el Tiempo**

Para una señal x(t), la energía total se define como:
$$E_{tiempo} = \int_{-\infty}^{\infty} |x(t)|^2 dt$$

Esta integral suma la potencia instantánea |x(t)|² sobre todo el tiempo.

**Paso 2: Representación en Frecuencia**

La transformada de Fourier X(f) nos dice cómo está distribuida la señal en frecuencia:
$$X(f) = \int_{-\infty}^{\infty} x(t) e^{-j2\pi ft} dt$$

El término |X(f)|² representa la densidad espectral de energía.

**Paso 3: Establecimiento de la Igualdad**

El teorema establece que:
$$E_{frecuencia} = \int_{-\infty}^{\infty} |X(f)|^2 df = E_{tiempo}$$

#### Derivación Matemática

**Partiendo de la definición de energía en el tiempo:**

$$E = \int_{-\infty}^{\infty} x(t) \cdot x^*(t) dt$$

donde x*(t) es el complejo conjugado de x(t).

**Usando la transformada inversa de Fourier:**

$$x(t) = \int_{-\infty}^{\infty} X(f) e^{j2\pi ft} df$$

**Sustituyendo en la expresión de energía:**

$$E = \int_{-\infty}^{\infty} x(t) \left[\int_{-\infty}^{\infty} X^*(f) e^{-j2\pi ft} df\right] dt$$

**Intercambiando el orden de integración (teorema de Fubini):**

$$E = \int_{-\infty}^{\infty} X^*(f) \left[\int_{-\infty}^{\infty} x(t) e^{-j2\pi ft} dt\right] df$$

**Reconociendo la transformada de Fourier interna:**

$$E = \int_{-\infty}^{\infty} X^*(f) \cdot X(f) df$$

**Resultado final:**
$$\boxed{E = \int_{-\infty}^{\infty} |X(f)|^2 df}$$

**Versión con frecuencia angular** ($\omega = 2\pi f$):
$$E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} |X(\omega)|^2 d\omega$$

**Significado físico de cada término:**
- $|x(t)|^2$: Potencia instantánea en el instante t
- $|X(f)|^2$: Densidad espectral de energía en la frecuencia f
- Las integrales: Suman estas densidades para obtener la energía total

#### Aplicaciones del Teorema

**a) Cálculo de energía en el dominio de frecuencia**

A veces es más fácil calcular energía en frecuencia que en tiempo.

**Ejemplo**: Señal $x(t) = e^{-at}u(t)$ con $a > 0$

Transformada de Fourier:
$$X(f) = \frac{1}{a + j2\pi f}$$

Magnitud:
$$|X(f)|^2 = \frac{1}{a^2 + (2\pi f)^2}$$

Energía (usando Parseval):
$$E = \int_{-\infty}^{\infty} \frac{1}{a^2 + (2\pi f)^2} df = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{1}{(a/2\pi)^2 + f^2} df = \frac{1}{2a}$$

Verificación en el tiempo:
$$E = \int_0^{\infty} e^{-2at} dt = \left[-\frac{e^{-2at}}{2a}\right]_0^{\infty} = \frac{1}{2a}$$ ✓

**b) Diseño de filtros**

Queremos que un filtro preserve cierta fracción de energía:
$$\eta = \frac{\int_{-\infty}^{\infty} |X(f)|^2 |H(f)|^2 df}{\int_{-\infty}^{\infty} |X(f)|^2 df}$$

donde $H(f)$ es la respuesta en frecuencia del filtro.

**c) Ancho de banda equivalente de ruido**

Definimos el ancho de banda equivalente de ruido:
$$B_n = \frac{\int_0^{\infty} |H(f)|^2 df}{|H(f_{max})|^2}$$

**d) Relación señal-ruido via Parseval**

Si señal y ruido son independientes:
$$SNR = \frac{E_{señal}}{E_{ruido}} = \frac{\int |X(f)|^2 df}{\int |N(f)|^2 df}$$

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina el teorema de Parseval como un **principio de conservación financiera**: Si tienes $1000 en billetes de diferentes denominaciones, no importa si los cuentas como billetes individuales o los agrupas por denominación - el total siempre será $1000. Similarmente, la energía de una señal es la misma ya sea que la midamos instante por instante en el tiempo o frecuencia por frecuencia.

**Intuición física:**
La transformada de Fourier es como un **prisma óptico** que descompone la luz blanca en sus colores componentes. El teorema de Parseval nos asegura que la energía total de la luz blanca es igual a la suma de las energías de todos los colores individuales - no se pierde energía en la descomposición.

**Visualización:**
Imagina dos gráficas:
1. **Dominio del tiempo**: Área bajo la curva de |x(t)|²
2. **Dominio de frecuencia**: Área bajo la curva de |X(f)|²

El teorema dice que estas dos áreas son exactamente iguales.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Pulso Rectangular

**Situación:** Analizar la energía de un pulso rectangular de amplitud A y duración T.

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Amplitud (A) | 5 | V |
| Duración (T) | 2 | ms |

**Solución paso a paso:**

1. **Energía en el dominio del tiempo:**
   $$E_{tiempo} = \int_{-T/2}^{T/2} A^2 dt = A^2 \cdot T = 25 \cdot 0.002 = 0.05 \text{ J}$$

2. **Transformada de Fourier del pulso:**
   $$X(f) = AT \cdot \text{sinc}(fT) = 0.01 \cdot \text{sinc}(0.002f)$$

3. **Verificación por Parseval:**
   $$E_{frecuencia} = \int_{-\infty}^{\infty} |AT \cdot \text{sinc}(fT)|^2 df = A^2T = 0.05 \text{ J}$$

**Interpretación:** La energía es la misma en ambos dominios, confirmando el teorema.

---

#### Ejemplo 2: Señal de Radio AM

**Contexto:** Estación de radio AM transmitiendo en 1 MHz con modulación de voz.

Una señal AM con índice de modulación m=0.5 y portadora de 100W:

- **Energía en tiempo**: Integración de la envolvente modulada al cuadrado
- **Energía en frecuencia**: Suma de energías en:
  - Portadora: 100W
  - Banda lateral superior: 12.5W
  - Banda lateral inferior: 12.5W
  - Total: 125W

El teorema garantiza que ambos cálculos darán el mismo resultado.

---

#### Ejemplo 3: Casos Límite

**¿Qué pasa cuando...?**

- **Señal impulso δ(t)**:
  - Tiempo: Energía infinita (integral de δ²(t))
  - Frecuencia: |F{δ(t)}|² = 1 para toda f → energía infinita
  - Parseval se mantiene: ∞ = ∞

- **Señal sinusoidal pura**:
  - Tiempo: Energía infinita (duración infinita)
  - Frecuencia: Delta en ±f₀ → energía infinita
  - Consistencia mantenida

#### Ejemplo 4: Señal Sinusoidal Modulada por Exponencial

**Señal**:
$$x(t) = e^{-at}\cos(2\pi f_0 t)u(t), \quad a > 0$$

**Método 1 - Tiempo** (difícil):
$$E_t = \int_0^{\infty} e^{-2at}\cos^2(2\pi f_0 t) dt$$

Usando $\cos^2(\theta) = (1 + \cos(2\theta))/2$:
$$E_t = \frac{1}{2}\int_0^{\infty} e^{-2at}dt + \frac{1}{2}\int_0^{\infty} e^{-2at}\cos(4\pi f_0 t) dt$$

Primera integral: $\frac{1}{4a}$

Segunda integral (más compleja): $\frac{a}{2(a^2 + 4\pi^2f_0^2)}$

$$E_t = \frac{1}{4a} + \frac{a}{4(a^2 + 4\pi^2f_0^2)}$$

**Método 2 - Frecuencia** (más sistemático):

Usando propiedades de la transformada:
$$x(t) = e^{-at}u(t) \cdot \cos(2\pi f_0 t)$$

$$X(f) = \frac{1}{2}\left[\frac{1}{a + j2\pi(f-f_0)} + \frac{1}{a + j2\pi(f+f_0)}\right]$$

Calcular $|X(f)|^2$ e integrar sería laborioso, pero conceptualmente más claro y ambos métodos producen el mismo resultado.

#### Ejemplo 5: Ancho de Banda del 99% de Energía

**Problema**: Determinar el ancho de banda que contiene el 99% de la energía de un pulso rectangular.

**Señal**: Pulso rectangular de amplitud $A$ y duración $T$
$$|X(f)|^2 = A^2T^2 \text{sinc}^2(\pi fT)$$

**Energía total**:
$$E_{total} = A^2T$$

**Queremos** $B$ tal que:
$$\int_{-B}^{B} A^2T^2 \text{sinc}^2(\pi fT) df = 0.99 \cdot A^2T$$

Simplificando:
$$\int_{-B}^{B} \text{sinc}^2(\pi fT) df = \frac{0.99}{T}$$

Por simetría:
$$2\int_0^{B} \text{sinc}^2(\pi fT) df = \frac{0.99}{T}$$

Cambio de variable $u = \pi fT$:
$$\frac{2}{\pi T}\int_0^{\pi BT} \text{sinc}^2(u) du = \frac{0.99}{T}$$

$$\int_0^{\pi BT} \text{sinc}^2(u) du = 0.99 \cdot \frac{\pi}{2}$$

Sabiendo que $\int_0^{\infty} \text{sinc}^2(u) du = \pi/2$:

Resolviendo numéricamente: $\pi BT \approx 2.5\pi$

$$B \approx \frac{2.5}{T}$$

**Interpretación**: Necesitamos aproximadamente 2.5 veces el inverso de la duración del pulso para capturar el 99% de la energía.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados
- **Teorema de Convolución** (Carta 7): Parseval es caso especial cuando convolución es con conjugado
- **Densidad Espectral de Potencia** (Carta 6): DEP usa Parseval para señales de potencia
- **Teorema del Muestreo** (Carta 5): Parseval ayuda a entender aliasing energético

#### Dependencias
1. **Transformada de Fourier** → Necesaria para establecer la relación
2. **Concepto de energía** → Base para entender qué se conserva

#### Aplicaciones Posteriores
1. **Diseño de filtros**: Calcular energía perdida/transmitida
2. **Análisis de modulación**: Distribución de energía en bandas laterales
3. **Compresión de señales**: Concentrar energía en pocas frecuencias

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La energía es invariante bajo la transformada de Fourier
- Puedes calcular energía en el dominio más conveniente
- La densidad espectral de energía tiene significado físico real

#### Tipos de problemas típicos
1. **Verificación del teorema**: Dado x(t), calcular energía en ambos dominios
   - Estrategia: Elegir el dominio donde la integral sea más simple

2. **Cálculo de energía en banda**: ¿Cuánta energía hay entre f₁ y f₂?
   - Estrategia: Usar |X(f)|² e integrar solo en la banda de interés

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Olvidar el módulo al cuadrado**
- Por qué ocurre: Confusión con la transformada directa
- Cómo evitarlo: Siempre |X(f)|², no X(f)
- Ejemplo: Para señal compleja, |X(f)|² ≠ X²(f)

❌ **Error #2: Confundir energía con potencia**
- Por qué ocurre: Señales periódicas tienen energía infinita
- Cómo evitarlo: Parseval clásico es para señales de energía finita

❌ **Error #3: Unidades incorrectas**
- Distinción importante: [V²·s] en tiempo, [V²·s] en frecuencia (Hz⁻¹ se cancela)

❌ **Error #4: Olvidar el factor $1/(2\pi)$ en versión con $\omega$**
- Importante distinguir entre usar $f$ vs $\omega$
- La fórmula cambia según la variable de integración
- Siempre verificar: $\int |X(f)|^2 df$ vs $\frac{1}{2\pi}\int |X(\omega)|^2 d\omega$

❌ **Error #5: Límites de integración incorrectos**
- La integral es de $-\infty$ a $+\infty$ para ambos dominios
- No confundir con integración solo en frecuencias positivas
- Si la señal es par, puede integrarse en positivos y multiplicar por 2

❌ **Error #6: Aplicar a señales de potencia infinita**
- El teorema clásico es para señales de energía finita
- Para señales de potencia se usa la versión periódica
- La versión de potencia usa $\frac{1}{T}\int_0^T |x(t)|^2 dt = \sum |c_n|^2$

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Parseval (energía): ∫|x(t)|² dt = ∫|X(f)|² df
Parseval (potencia): (1/T)∫|x(t)|² dt = Σ|Xₙ|²  (para periódicas)
```

#### Conceptos Fundamentales
- ✓ **Conservación**: La transformada de Fourier conserva energía
- ✓ **Dualidad**: Puedes elegir el dominio más conveniente para calcular
- ✓ **Distribución**: |X(f)|² muestra cómo se distribuye la energía en frecuencia

#### Reglas Mnemotécnicas
- 🧠 **"TIEMPO = FRECUENCIA"**: Las energías son iguales
- 🧠 **"Módulo al cuadrado"**: Siempre |·|² en ambos lados

#### Valores Típicos

| Señal | Energía | Aplicación |
|-------|---------|------------|
| Bit digital (1V, 1μs) | 1 μJ | Comunicaciones digitales |
| Pulso radar (1kW, 1μs) | 1 mJ | Sistemas radar |
| Símbolo OFDM | Variable | WiFi, LTE |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**: Oppenheim & Willsky Cap. 4, Proakis & Manolakis Cap. 3
- **Simulaciones**: MATLAB fft() para verificar numéricamente
- **Experimentos**: Analizador de espectro para ver distribución real

#### Temas Relacionados para Explorar
1. Teorema de Parseval generalizado (producto interno): $\int x(t)y^*(t) dt = \int X(f)Y^*(f) df$
2. Versión discreta (DFT): $\sum |x[n]|^2 = \frac{1}{N}\sum |X[k]|^2$
3. Relación con teorema de Plancherel
4. Extensiones: wavelets, mecánica cuántica, espacios de Hilbert

#### Preguntas para Reflexionar
- ¿Por qué la conservación de energía es fundamental en comunicaciones?
- ¿Cómo afecta el filtrado a la distribución de energía?
- ¿Qué pasa con Parseval en señales muestreadas?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 25 minutos
**Prerequisitos críticos**: Transformada de Fourier, concepto de energía
**Tags**: `#parseval` `#energia` `#fourier` `#conservacion` `#espectro`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*
