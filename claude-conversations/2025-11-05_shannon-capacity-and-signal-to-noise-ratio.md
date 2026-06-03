# Shannon capacity and signal-to-noise ratio

**Fecha:** 2025-11-05

**Rodrigo** (2025-11-05 04:49:09):

Cual es la ecuación de la capacidad ara transmitir información que la relaciona con al relación señal-ruido

---

**Claude** (2025-11-05 04:49:29):

La ecuación que buscas es la **fórmula de Shannon-Hartley** (también conocida como teorema de Shannon o expresión de Hartley-Shannon, como se menciona en tu programa), que relaciona la capacidad de un canal para transmitir información con la relación señal-ruido:

## **C = B · log₂(1 + S/N)**

Donde:
- **C** = Capacidad del canal (en bits por segundo)
- **B** = Ancho de banda del canal (en Hz)
- **S/N** = Relación señal a ruido (relación de potencias, adimensional)

### Variaciones de la ecuación:

1. **Con logaritmo natural:**
   C = B · ln(1 + S/N) / ln(2)

2. **Con SNR en decibeles:**
   Si tienes SNR(dB) = 10·log₁₀(S/N), primero debes convertir:
   - S/N = 10^(SNR(dB)/10)
   - Luego aplicar: C = B · log₂(1 + 10^(SNR(dB)/10))

### Conceptos importantes:

- Esta ecuación establece el **límite teórico máximo** de la tasa de información que puede transmitirse sin errores a través de un canal con ruido gaussiano blanco
- Muestra el **intercambio fundamental** entre ancho de banda y relación señal-ruido: puedes compensar un menor ancho de banda con mayor S/N y viceversa
- Es la base del "sistema ideal de comunicaciones" mencionado en la Unidad 9 de tu programa

Esta ecuación es fundamental para el análisis comparativo de sistemas de modulación que estudias en la Unidad 8 y para entender los límites teóricos de cualquier sistema de comunicaciones.

> [!note]- Thinking
> El usuario está preguntando sobre la ecuación de capacidad de canal que relaciona la capacidad de transmisión de información con la relación señal-ruido. Basándome en el programa de la materia, puedo ver que esto se cubre en la Unidad 9 sobre Teoría de la Información, donde se menciona específicamente:
> 
> "Canal de comunicación. Capacidad del canal con ruido. Ancho de banda e intercambio con la relación S/R. Capacidad máxima. Expresión de Hartley-Shannon."
> 
> Esta es claramente la fórmula de Shannon-Hartley o teorema de Shannon para la capacidad del canal, que es una ecuación fundamental en teoría de la información.

---

**Rodrigo** (2025-11-05 04:51:53):

Cómo se deduce dicha ecuación?

---

**Claude** (2025-11-05 04:52:23):

## Deducción de la Ecuación de Shannon-Hartley

La deducción combina conceptos de **teoría de la información** con el **teorema del muestreo** y análisis de **ruido gaussiano**. Te presento el desarrollo paso a paso:

### 1. **Punto de partida: Teorema del Muestreo**
Por el teorema de Nyquist, una señal limitada en banda B puede representarse completamente mediante **2B muestras por segundo**.

En un tiempo T, tenemos:
- Número de muestras = 2BT

### 2. **Análisis de la señal con ruido**
En el canal tenemos:
- **Señal transmitida**: potencia S
- **Ruido gaussiano blanco**: potencia N
- **Señal recibida**: y(t) = s(t) + n(t)

La potencia total recibida es: **P = S + N**

### 3. **Niveles distinguibles**
Con ruido gaussiano, el número de niveles de amplitud distinguibles es aproximadamente:

**M ≈ √(1 + S/N)**

Esto surge porque:
- La señal total tiene rango ≈ √(S+N)
- El ruido limita la resolución a ≈ √N
- Niveles distinguibles = √(S+N)/√N = √(1 + S/N)

### 4. **Información por muestra**
La información máxima por muestra (en bits) es:

**I = log₂(M²) = log₂(1 + S/N)**

El cuadrado aparece porque consideramos la potencia (amplitud²).

### 5. **Capacidad del canal**
La capacidad es la información total por unidad de tiempo:

**C = (información/muestra) × (muestras/segundo)**

**C = log₂(1 + S/N) × 2B**

Sin embargo, Shannon demostró rigurosamente que el factor 2 se simplifica al considerar la distribución óptima de la señal, resultando en:

## **C = B · log₂(1 + S/N)**

### Deducción más rigurosa (Shannon):

Shannon utilizó conceptos de **información mutua** I(X;Y) entre entrada X y salida Y:

1. **Canal gaussiano**: Y = X + N
   - X: señal de entrada con potencia S
   - N: ruido gaussiano con potencia N

2. **Entropía diferencial**:
   - h(Y) = ½log₂(2πe(S+N))
   - h(N) = ½log₂(2πeN)

3. **Información mutua**:
   - I(X;Y) = h(Y) - h(Y|X) = h(Y) - h(N)
   - I(X;Y) = ½log₂(2πe(S+N)) - ½log₂(2πeN)
   - I(X;Y) = ½log₂((S+N)/N) = ½log₂(1 + S/N)

4. **Considerando el ancho de banda**:
   Por el teorema del muestreo, en un canal de ancho de banda B, podemos transmitir 2B símbolos independientes por segundo, cada uno llevando ½log₂(1 + S/N) bits.

5. **Capacidad final**:
   C = 2B × ½log₂(1 + S/N) = **B · log₂(1 + S/N)**

### Puntos clave de la deducción:

- **Supuesto fundamental**: El ruido es **gaussiano blanco aditivo** (AWGN)
- La señal óptima también tiene **distribución gaussiana**
- La ecuación representa el **límite teórico** - ningún sistema real puede superarlo
- Para S/N >> 1: C ≈ B·log₂(S/N)
- Para S/N << 1: C ≈ B·(S/N)/ln(2)

Esta ecuación es fundamental porque establece el límite absoluto de la eficiencia espectral (bits/s/Hz) que cualquier sistema de comunicaciones puede alcanzar.

> [!note]- Thinking
> El usuario quiere saber cómo se deduce la ecuación de Shannon-Hartley. Esta es una deducción importante en teoría de la información que involucra conceptos de entropía, información mutua y el teorema del muestreo. Voy a presentar una deducción paso a paso que sea clara y comprensible.

---

