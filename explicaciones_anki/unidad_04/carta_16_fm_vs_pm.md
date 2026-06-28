# Carta 16: Diferenciación entre FM y PM desde el punto de vista matemático

> **Unidad 4**: Modulación Exponencial

---

## 🎯 Pregunta

Diferencie entre modulación en frecuencia (FM) y modulación en fase (PM) desde el punto de vista matemático.

---

## 📝 Respuesta Breve (de la carta original)

**FM (Frequency Modulation)**:
$$s_{FM}(t) = A_c\cos[2\pi f_c t + 2\pi k_f \int m(t)dt]$$
- La frecuencia instantánea varía con $m(t)$
- $f_i(t) = f_c + k_f m(t)$

**PM (Phase Modulation)**:
$$s_{PM}(t) = A_c\cos[2\pi f_c t + k_p m(t)]$$
- La fase instantánea varía directamente con $m(t)$

**Relación**: FM de $m(t)$ ≡ PM de $\int m(t)dt$
- FM es derivador respecto a PM
- PM es integrador respecto a FM

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La **modulación angular** o **exponencial** es una familia de técnicas donde la información se codifica modificando el ángulo (fase) de una portadora sinusoidal, manteniendo su amplitud constante. Esta característica fundamental las diferencia de la modulación lineal (AM) y les confiere propiedades únicas de robustez ante el ruido.

**¿Por qué es importante este concepto?** FM y PM son las dos formas principales de modulación angular, fundamentales en sistemas de comunicaciones modernos. Aunque matemáticamente relacionadas, sus aplicaciones prácticas difieren significativamente: FM domina en radiodifusión analógica (radio FM comercial en 88-108 MHz), mientras que PM es la base de modulaciones digitales modernas (PSK, QPSK, QAM).

**¿Dónde se aplica?** FM se encuentra en radio broadcast FM, audio de televisión analógica, comunicaciones satelitales, y sistemas de telemetría. PM aparece en todas las comunicaciones digitales modernas: WiFi, 4G/5G, comunicaciones satelitales digitales, y enlaces de microondas.

**Historia relevante:** Edwin Armstrong inventó FM en 1933 como solución al problema del ruido en AM, revolucionando la radiodifusión. PM fue desarrollada posteriormente, encontrando su nicho principal en comunicaciones digitales donde la fase puede representar símbolos discretos eficientemente.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Señales sinusoidales y su representación fasorial
- Concepto de frecuencia instantánea y fase instantánea
- Derivación e integración de señales
- Relación entre frecuencia y fase: $\omega = d\phi/dt$

#### Desarrollo Paso a Paso

**Paso 1: Señal portadora sin modular**

Comenzamos con una portadora sinusoidal pura:
$$c(t) = A_c\cos(\theta(t)) = A_c\cos(2\pi f_c t + \phi_0)$$

donde el argumento $\theta(t) = 2\pi f_c t + \phi_0$ es el **ángulo instantáneo**.

**Paso 2: Definiciones fundamentales**

Para cualquier señal sinusoidal:
- **Fase instantánea**: $\theta(t) = 2\pi f_c t + \phi(t)$
- **Frecuencia instantánea**: $f_i(t) = \frac{1}{2\pi}\frac{d\theta(t)}{dt} = f_c + \frac{1}{2\pi}\frac{d\phi(t)}{dt}$

La relación fundamental es:
$$\phi(t) = 2\pi\int_{-\infty}^{t} [f_i(\tau) - f_c] d\tau$$

**Paso 3: Modulación en Fase (PM)**

En PM, la fase instantánea varía directamente con la señal moduladora:
$$\phi(t) = k_p m(t)$$

donde $k_p$ es la sensibilidad de fase [radianes/voltio].

La señal PM resulta:
$$s_{PM}(t) = A_c\cos[2\pi f_c t + k_p m(t)]$$

La frecuencia instantánea en PM es:
$$f_i^{PM}(t) = f_c + \frac{k_p}{2\pi}\frac{dm(t)}{dt}$$

**Paso 4: Modulación en Frecuencia (FM)**

En FM, la frecuencia instantánea varía directamente con la señal moduladora:
$$f_i(t) = f_c + k_f m(t)$$

donde $k_f$ es la sensibilidad de frecuencia [Hz/voltio].

Integrando para obtener la fase:
$$\phi(t) = 2\pi k_f \int_{-\infty}^{t} m(\tau) d\tau$$

La señal FM resulta:
$$s_{FM}(t) = A_c\cos\left[2\pi f_c t + 2\pi k_f \int_{-\infty}^{t} m(\tau) d\tau\right]$$

#### Derivación Matemática de la Relación FM-PM

**Partiendo del principio fundamental:**

Para cualquier modulación angular:
$$s(t) = A_c\cos[\theta(t)]$$

**En PM:**
$$\theta_{PM}(t) = 2\pi f_c t + k_p m(t)$$

**En FM:**
$$\theta_{FM}(t) = 2\pi f_c t + 2\pi k_f \int m(t)dt$$

**Relación clave:**

Si aplicamos PM a la integral de $m(t)$:
$$\theta_{PM}^* = 2\pi f_c t + k_p \int m(t)dt$$

Comparando con FM, vemos que:
$$\text{FM}[m(t)] \equiv \text{PM}\left[\int m(t)dt\right]$$

Similarmente:
$$\text{PM}[m(t)] \equiv \text{FM}\left[\frac{dm(t)}{dt}\right]$$

### 🔬 Intuición y Analogías

**Analogía del automóvil:**

Imagina conducir un automóvil donde:
- **FM es como controlar directamente el velocímetro**: La señal moduladora $m(t)$ controla qué tan rápido vas (frecuencia). La distancia recorrida (fase) es la integral de la velocidad.
- **PM es como controlar directamente el odómetro**: La señal moduladora $m(t)$ controla tu posición (fase). La velocidad (frecuencia) es la derivada de la posición.

**Intuición física:**

FM responde a cambios lentos de la moduladora mejor que PM porque integra la señal. PM responde mejor a cambios rápidos porque la frecuencia instantánea depende de la derivada de la moduladora.

**Visualización:**

Para una moduladora sinusoidal $m(t) = A_m\cos(2\pi f_m t)$:
- En FM: la frecuencia oscila sinusoidalmente alrededor de $f_c$
- En PM: la fase oscila sinusoidalmente, pero la frecuencia oscila como $-A_m\sin(2\pi f_m t)$ (desfasada 90°)

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Modulación con Tono Simple

**Situación:** Modular una portadora de 100 MHz con un tono de 1 kHz

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| $f_c$ | 100 | MHz |
| $f_m$ | 1 | kHz |
| $A_m$ | 1 | V |
| $k_f$ | 75 | kHz/V |
| $k_p$ | π/2 | rad/V |

**Solución paso a paso:**

1. **Señal moduladora:**
   $$m(t) = \cos(2\pi \cdot 10^3 t)$$

2. **Para FM:**
   $$s_{FM}(t) = A_c\cos\left[2\pi \cdot 10^8 t + \frac{75 \cdot 10^3}{10^3}\sin(2\pi \cdot 10^3 t)\right]$$
   $$s_{FM}(t) = A_c\cos[2\pi \cdot 10^8 t + 75\sin(2\pi \cdot 10^3 t)]$$

   Índice de modulación: $\beta_{FM} = 75$

3. **Para PM:**
   $$s_{PM}(t) = A_c\cos[2\pi \cdot 10^8 t + \frac{\pi}{2}\cos(2\pi \cdot 10^3 t)]$$

   Índice de modulación: $\beta_{PM} = \pi/2 \approx 1.57$

**Interpretación:** FM produce una desviación de frecuencia constante (75 kHz) independiente de $f_m$. PM produce una desviación de fase constante (π/2 rad) pero la desviación de frecuencia aumenta con $f_m$.

---

#### Ejemplo 2: Radio FM Broadcast

**Contexto:** Estación FM comercial transmitiendo audio estéreo

En radio FM comercial (88-108 MHz):
- Desviación máxima: ±75 kHz
- Audio: 50 Hz - 15 kHz
- Preénfasis aplicado: +6 dB/octava desde 2.1 kHz

Para un programa musical típico:
- Frecuencias bajas (bajo, bombo): producen gran desviación pero lenta
- Frecuencias altas (platillos, armónicos): producen menor desviación pero rápida
- El preénfasis compensa la menor desviación en altas frecuencias

---

#### Ejemplo 3: Comportamiento en Casos Límite

**¿Qué pasa cuando la moduladora es un escalón?**

Señal escalón: $m(t) = u(t)$ (función escalón unitario)

**En PM:**
- Fase salta instantáneamente de 0 a $k_p$
- Frecuencia tiene un impulso $\delta(t)$ (teóricamente infinito)
- Prácticamente irrealizable sin distorsión

**En FM:**
- Frecuencia salta de $f_c$ a $f_c + k_f$
- Fase cambia linealmente con pendiente $2\pi k_f$
- Más realizable en la práctica

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Índice de modulación** (Carta 17): Define comportamiento espectral
- **Regla de Carson** (Carta 18): Estima ancho de banda para ambas
- **Discriminador de frecuencia** (Carta 19): Demodula FM pero complica PM
- **Modulación digital PSK** (Carta 27): PM es base de PSK/QPSK

#### Dependencias (lo que necesitas saber primero)
1. Transformada de Fourier → Para entender espectro
2. Derivación e integración → Relación fundamental FM-PM
3. Concepto de fase y frecuencia instantánea → Base conceptual

#### Aplicaciones Posteriores (dónde usarás esto)
1. **NBFM vs WBFM**: El índice determina el régimen de operación
2. **Modulaciones digitales**: PM evoluciona a BPSK, QPSK, QAM
3. **Sistemas adaptativos**: Selección FM vs PM según canal

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La relación derivada/integral entre FM y PM NO es casualidad, es fundamental
- Para la misma moduladora, FM y PM producen espectros diferentes
- FM es preferible para señales con contenido de baja frecuencia
- PM es preferible para señales digitales (símbolos discretos)

#### Tipos de problemas típicos
1. **Conversión FM↔PM**: Dado un modulador, diseñar el otro
   - Estrategia: Agregar integrador o derivador según el caso

2. **Cálculo de desviaciones**: Hallar Δf y Δφ para moduladora dada
   - Estrategia: Aplicar definiciones directamente

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir las constantes $k_f$ y $k_p$**
- Por qué ocurre: Ambas relacionan moduladora con desviación
- Cómo evitarlo: Recordar unidades: $k_f$ [Hz/V], $k_p$ [rad/V]
- Ejemplo de error: Usar $k_f$ en fórmula de PM o viceversa

❌ **Error #2: Olvidar el factor 2π en las conversiones**
- Por qué ocurre: Mezclar frecuencia angular y frecuencia en Hz
- Cómo evitarlo: Siempre verificar dimensiones
- Distinción importante: $\omega = 2\pi f$

❌ **Error #3: Pensar que FM y PM son independientes**
- Por qué ocurre: Se presentan como técnicas separadas
- Realidad: Son dos caras de la misma moneda (modulación angular)
- Cómo evitarlo: Recordar relación integral/derivada

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
FM: s(t) = A_c cos[2πf_c t + 2πk_f ∫m(t)dt]
PM: s(t) = A_c cos[2πf_c t + k_p m(t)]
Relación: FM[m(t)] = PM[∫m(t)dt]
```

#### Conceptos Fundamentales
- ✓ **FM modula frecuencia**: La desviación de frecuencia es proporcional a m(t)
- ✓ **PM modula fase**: La desviación de fase es proporcional a m(t)
- ✓ **Relación integral**: FM integra mientras PM deriva (relativamente)

#### Reglas Mnemotécnicas
- 🧠 **"FM Frecuenta, PM Fasea"**: FM controla frecuencia, PM controla fase
- 🧠 **"FM Integra, PM Deriva"**: Para convertir, FM necesita integrador

#### Valores Típicos (para referencias rápidas)

| Parámetro | FM Broadcast | PM Digital |
|-----------|--------------|------------|
| Desviación típica | ±75 kHz | ±π/4 a ±π rad |
| Índice β | 5 (típico) | < 1 (usual) |
| Aplicación | Audio análogo | Datos digitales |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Haykin Cap. 4.1-4.3, Carlson Cap. 5
- **Material del curso**: Apuntes sobre modulación angular
- **Simulaciones**: GNU Radio para experimentar con FM/PM

#### Temas Relacionados para Explorar
1. Funciones de Bessel y espectro FM
2. FM estéreo y multiplexación
3. Modulaciones CPM (Continuous Phase Modulation)

#### Preguntas para Reflexionar
- ¿Por qué FM es más popular que PM en radiodifusión analógica?
- ¿Qué pasaría si moduláramos en frecuencia y fase simultáneamente?
- ¿Cómo afecta el ruido diferentemente a FM y PM?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 25 minutos
**Prerequisitos críticos**: Señales sinusoidales, derivación/integración, fase y frecuencia
**Tags**: `#modulacion-angular` `#FM` `#PM` `#relacion-integral-derivada`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*