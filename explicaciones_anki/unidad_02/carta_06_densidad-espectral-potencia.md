# Carta 6: Densidad Espectral de Potencia y el Teorema de Wiener-Khinchin

> **Unidad 2**: Análisis de Señales

---

## 🎯 Pregunta

¿Qué es la densidad espectral de potencia y cómo se relaciona con la autocorrelación?

---

## 📝 Respuesta Breve (de la carta original)

La **densidad espectral de potencia (DEP)** $S_x(f)$ describe cómo se distribuye la potencia de una señal en el dominio de la frecuencia.

**Relación con autocorrelación** (Teorema de Wiener-Khinchin):
$$S_x(f) = \mathcal{F}\{R_x(\tau)\}$$

Donde $R_x(\tau)$ es la función de autocorrelación. Esto significa que la DEP y la autocorrelación forman un **par de transformadas de Fourier**.

**Implicación**: características temporales de correlación se traducen en características espectrales de distribución de potencia.

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La **Densidad Espectral de Potencia (DEP)** es una herramienta fundamental para analizar señales aleatorias y determinísticas de potencia en sistemas de comunicaciones. Mientras que la transformada de Fourier tradicional nos dice qué frecuencias están presentes en una señal determinística de energía finita, la DEP nos revela cómo se distribuye la potencia promedio de una señal a lo largo del espectro de frecuencias, siendo especialmente útil para señales que existen indefinidamente en el tiempo.

**¿Por qué es importante en comunicaciones?** En el mundo real, las señales de comunicación son típicamente procesos aleatorios (ruido, señales moduladas con información aleatoria, interferencias). No podemos aplicar directamente la transformada de Fourier a estas señales porque tienen energía infinita. La DEP nos permite caracterizar espectralmente estos procesos de manera significativa. Por ejemplo, cuando diseñamos un receptor WiFi, necesitamos conocer la DEP del ruido térmico para calcular la sensibilidad del sistema.

**¿Dónde se aplica?** La DEP es ubicua en el análisis y diseño de sistemas:
- **Análisis de ruido**: Caracterización del ruido blanco, rosa, flicker
- **Diseño de filtros**: Optimización para maximizar SNR
- **Asignación de espectro**: Máscaras espectrales en WiFi, LTE, satelital
- **Análisis de vibraciones**: Diagnóstico de maquinaria, sismología
- **Procesamiento de audio**: Ecualización, análisis espectral
- **Radar y sonar**: Detección de señales en ruido

**Historia**: El teorema de Wiener-Khinchin fue desarrollado independientemente por Norbert Wiener (1930) y Aleksandr Khinchin (1934), unificando conceptos de análisis espectral con teoría de procesos estocásticos.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Procesos estocásticos estacionarios**: Propiedades estadísticas invariantes en el tiempo
- **Función de autocorrelación**: Medida de similitud de una señal consigo misma desplazada
- **Señales de potencia vs energía**: Distinción fundamental
- **Valor esperado y promedios temporales**: Para procesos ergódicos

#### Desarrollo Paso a Paso

**Paso 1: Limitación de Señales de Potencia**

Para una señal de potencia x(t) (energía infinita, potencia finita), no existe X(f) en el sentido tradicional. Necesitamos un enfoque diferente.

**Paso 2: Definición de Autocorrelación**

Para señales determinísticas:
$$R_x(\tau) = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} x(t)x^*(t-\tau) dt$$

Para procesos aleatorios estacionarios:
$$R_x(\tau) = E[X(t)X^*(t-\tau)]$$

**Paso 3: Conexión con el Espectro**

El teorema de Wiener-Khinchin establece que la DEP es la transformada de Fourier de la autocorrelación:
$$S_x(f) = \int_{-\infty}^{\infty} R_x(\tau) e^{-j2\pi f\tau} d\tau$$

#### Derivación Matemática

**Para una señal x(t) truncada a [-T, T]:**

Definimos la versión truncada:
$$x_T(t) = \begin{cases} x(t) & |t| \leq T \\ 0 & |t| > T \end{cases}$$

**La energía de la señal truncada:**
$$E_T = \int_{-\infty}^{\infty} |x_T(t)|^2 dt = \int_{-\infty}^{\infty} |X_T(f)|^2 df$$

**La potencia promedio en el intervalo:**
$$P = \lim_{T \to \infty} \frac{E_T}{2T} = \lim_{T \to \infty} \frac{1}{2T} \int_{-\infty}^{\infty} |X_T(f)|^2 df$$

**Definiendo la DEP:**
$$S_x(f) = \lim_{T \to \infty} \frac{|X_T(f)|^2}{2T}$$

**Aplicando el teorema de convolución y propiedades de Fourier:**

Se puede demostrar que:
$$S_x(f) = \mathcal{F}\{R_x(\tau)\}$$

**Resultado final (Teorema de Wiener-Khinchin):**
$$\boxed{S_x(f) = \int_{-\infty}^{\infty} R_x(\tau) e^{-j2\pi f\tau} d\tau}$$

**Significado físico de cada término:**
- $S_x(f)$: Potencia por unidad de frecuencia [W/Hz]
- $R_x(\tau)$: Correlación temporal de la señal
- $R_x(0)$: Potencia total de la señal
- La integral de $S_x(f)$: Potencia total

### 🔬 Intuición y Analogías

**Analogía principal:**
La DEP es como un **análisis financiero de gastos mensuales**. Mientras que el total mensual (potencia total) te dice cuánto gastas, la DEP te dice cómo se distribuye ese gasto: cuánto en alimentación (bajas frecuencias), transporte (frecuencias medias), entretenimiento (altas frecuencias). La autocorrelación sería como analizar patrones de gasto: si gastas mucho un día, ¿es probable que gastes mucho al día siguiente?

**Intuición física:**
Imagina la DEP como un **ecualizador gráfico** en un sistema de audio:
- Cada barra representa cuánta potencia hay en esa banda de frecuencia
- La altura total de todas las barras suma la potencia total
- Un ruido blanco tendría todas las barras a la misma altura
- Una señal tonal pura tendría solo una barra muy alta

**Visualización:**
- **Dominio del tiempo**: R(τ) muestra qué tan "predecible" es la señal
  - R(0) = máximo (perfecta correlación consigo misma)
  - R(τ grande) → 0 para señales aleatorias
- **Dominio frecuencial**: S(f) muestra distribución de potencia
  - Área bajo S(f) = potencia total = R(0)

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Ruido Blanco Gaussiano

**Situación:** Analizar el ruido térmico en un resistor de 50Ω a temperatura ambiente.

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Resistencia | 50 | Ω |
| Temperatura | 290 | K |
| Ancho de banda | 1 | MHz |
| Constante de Boltzmann | 1.38×10⁻²³ | J/K |

**Solución paso a paso:**

1. **Densidad espectral de potencia disponible del ruido térmico:**

   **Convención unilateral** (solo frecuencias positivas, más simple):
   $$N_0 = kT = 1.38×10^{-23} \times 290$$
   $$N_0 = 4.0×10^{-21} \text{ W/Hz} = -174 \text{ dBm/Hz}$$

   **Nota**: La potencia disponible es independiente de R (vale para carga adaptada).

2. **Función de autocorrelación (ruido blanco, convención unilateral):**
   $$R_n(\tau) = N_0\delta(\tau) = kT\delta(\tau)$$

   Esto indica correlación cero para $\tau \neq 0$ (ruido completamente aleatorio).

3. **Verificación Wiener-Khinchin:**
   $$S_n(f) = \mathcal{F}\{N_0\delta(\tau)\} = N_0 = 4.0×10^{-21} \text{ W/Hz}$$

   La DEP es constante para todas las frecuencias (espectro "blanco").

4. **Potencia total en el ancho de banda (B = 1 MHz):**
   $$P_{ruido} = \int_{0}^{B} S_n(f) df = N_0 \times B$$
   $$P_{ruido} = 4.0×10^{-21} \times 10^6 = 4.0×10^{-15} \text{ W} = -114 \text{ dBm}$$

**Nota histórica**: El voltaje de ruido se expresa como $\overline{v_n^2} = 4kTRB$ (con factor 4), pero la **potencia disponible** es $P = kTB$ (sin factor 4). Ver Unidad 7 para detalles.

**Interpretación:** El ruido blanco tiene DEP constante (plana) y autocorrelación delta, indicando completa aleatoriedad temporal.

---

#### Ejemplo 2: Señal Modulada BPSK

**Contexto:** Sistema de comunicación digital transmitiendo datos aleatorios con BPSK a 1 Mbps.

**Análisis de la DEP:**

Para BPSK con datos aleatorios equiprobables:

1. **Autocorrelación de la señal modulada:**
   $$R_s(\tau) = \frac{A^2}{2}R_b(\tau)\cos(2\pi f_c \tau)$$

   donde $R_b(\tau)$ es la autocorrelación de los bits (triangular).

2. **DEP aplicando Wiener-Khinchin:**
   $$S_s(f) = \frac{A^2T_b}{4}[\text{sinc}^2((f-f_c)T_b) + \text{sinc}^2((f+f_c)T_b)]$$

3. **Ancho de banda al primer nulo:**
   $$BW = 2R_b = 2 \text{ MHz}$$

La DEP muestra lóbulos principales centrados en ±f_c con forma sinc².

---

#### Ejemplo 3: Análisis de Interferencia Periódica

**¿Qué pasa con interferencia de 60 Hz de la red eléctrica?**

**Señal interferente:** x(t) = A cos(2π×60t + φ)

1. **Autocorrelación:**
   $$R_x(\tau) = \frac{A^2}{2}\cos(2\pi \times 60 \tau)$$

   Nota: No depende de la fase φ

2. **DEP:**
   $$S_x(f) = \frac{A^2}{4}[\delta(f-60) + \delta(f+60)]$$

3. **Interpretación:**
   - Toda la potencia concentrada en ±60 Hz
   - Filtro notch en 60 Hz eliminaría completamente la interferencia
   - La fase aleatoria no afecta la DEP

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados
- **Teorema de Parseval** (Carta 4): Caso especial para señales de energía
- **Ruido** (Unidad 7): DEP caracteriza completamente ruido gaussiano
- **Filtrado óptimo**: Maximizar SNR usando conocimiento de DEP
- **Teorema de Convolución** (Carta 7): Salida de filtro: $S_y(f) = |H(f)|^2 S_x(f)$

#### Dependencias
1. **Procesos aleatorios** → Base estadística para señales reales
2. **Transformada de Fourier** → Herramienta matemática fundamental
3. **Autocorrelación** → Dual de la DEP en tiempo

#### Aplicaciones Posteriores
1. **Diseño de receptores**: Filtro adaptado basado en DEP de señal y ruido
2. **Capacidad de canal**: Shannon usa DEP del ruido
3. **Análisis de modulaciones**: Calcular ocupación espectral
4. **Estimación espectral**: Métodos como periodograma, Welch

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La dualidad DEP ↔ autocorrelación es fundamental
- La DEP tiene unidades de potencia/frecuencia [W/Hz]
- Para ruido blanco: DEP plana, autocorrelación delta
- El área bajo la DEP es la potencia total

#### Tipos de problemas típicos
1. **Calcular DEP desde autocorrelación**: Dado R(τ), encontrar S(f)
   - Estrategia: Aplicar transformada de Fourier directamente

2. **Potencia en una banda**: Integrar S(f) entre f₁ y f₂
   - Estrategia: ∫_{f₁}^{f₂} S(f) df

3. **Salida de un filtro**: Dado S_x(f) y H(f), encontrar S_y(f)
   - Estrategia: S_y(f) = |H(f)|² S_x(f)

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir DEP con |X(f)|²**
- Por qué ocurre: Similitud superficial con Parseval
- Cómo evitarlo: DEP es para señales de potencia, |X(f)|² para energía
- Diferencia clave: DEP tiene unidades W/Hz, no J/Hz

❌ **Error #2: Olvidar que S(f) es siempre real y no negativa**
- Por qué ocurre: R(τ) es hermitiana → S(f) real
- Cómo evitarlo: Verificar que resultado sea ≥ 0 para todo f

❌ **Error #3: Aplicar DEP a señales no estacionarias**
- Distinción importante: DEP asume estacionariedad
- Solución: Usar espectrograma o wavelets para no estacionarias

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Wiener-Khinchin: S_x(f) = F{R_x(τ)}
Potencia total: P = R_x(0) = ∫S_x(f)df
Filtro LTI: S_y(f) = |H(f)|²S_x(f)
Ruido blanco: S_n(f) = N₀ = kT (convención unilateral, f > 0)
               S_n(f) = N₀/2 = kT/2 (convención bilateral, ±f)
```

#### Conceptos Fundamentales
- ✓ **Dualidad**: DEP y autocorrelación son transformadas de Fourier
- ✓ **Potencia total**: Área bajo DEP = R(0) = potencia promedio
- ✓ **No negatividad**: S(f) ≥ 0 siempre (es potencia)
- ✓ **Estacionariedad**: Requisito para que DEP tenga sentido

#### Reglas Mnemotécnicas
- 🧠 **"WK = TF"**: Wiener-Khinchin = Transformada de Fourier
- 🧠 **"Plano → Delta"**: DEP plana ↔ autocorrelación delta (ruido blanco)
- 🧠 **"Área = Potencia"**: Integral de S(f) = potencia total

#### Valores Típicos

| Señal | DEP característica | Aplicación |
|-------|-------------------|------------|
| Ruido térmico | N₀ = kT = -174 dBm/Hz @ 290K (unilateral) | Todos los receptores |
| Ruido 1/f | K/f | Dispositivos semiconductores |
| OFDM | Rectangular en banda | WiFi, LTE |
| Spread spectrum | Plana en banda ancha | GPS, CDMA |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**:
  - Papoulis "Probability, Random Variables, and Stochastic Processes" Cap. 10
  - Kay "Modern Spectral Estimation" para métodos avanzados
- **Software**:
  - MATLAB: pwelch() para estimación de DEP
  - Python: scipy.signal.welch(), matplotlib.pyplot.psd()
- **Instrumentos**:
  - Analizador de espectro para medición directa de DEP

#### Temas Relacionados para Explorar
1. **Estimación espectral**: Periodograma, Welch, Bartlett
2. **Métodos paramétricos**: AR, MA, ARMA
3. **Espectro cruzado**: Para señales correlacionadas
4. **Coherencia espectral**: Medida de correlación vs frecuencia

#### Preguntas para Reflexionar
- ¿Por qué la fase no aparece en la DEP?
- ¿Cómo afecta el windowing a la estimación de DEP?
- ¿Qué información se pierde al usar solo DEP sin fase?
- ¿Cómo se extiende el concepto a procesos no estacionarios?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 35 minutos
**Prerequisitos críticos**: Procesos aleatorios, autocorrelación, transformada de Fourier
**Tags**: `#DEP` `#wiener-khinchin` `#autocorrelacion` `#espectro` `#potencia`

---

*Generado el: 2024-11-16*
*Última revisión: 2025-11-22 - Corregido ejemplo de ruido térmico (N₀=kT, no 4kTR)*