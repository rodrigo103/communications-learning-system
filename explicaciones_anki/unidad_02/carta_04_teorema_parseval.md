# Carta 4: Teorema de Parseval

## Pregunta
Enuncie y explique el Teorema de Parseval. ¿Qué interpretación física tiene?

## Respuesta Breve
El Teorema de Parseval establece que:
$$\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df$$

**Interpretación física**: La energía total de una señal en el dominio del tiempo es igual a la energía total en el dominio de la frecuencia. Esto demuestra que la Transformada de Fourier conserva la energía, y permite calcular la energía de una señal integrando su densidad espectral de energía.

## Explicación Detallada

### Introducción
El Teorema de Parseval, también conocido como Teorema de Plancherel o Identidad de Rayleigh en diferentes contextos, es uno de los resultados más importantes en el análisis de señales. Establece un puente fundamental entre los dominios del tiempo y la frecuencia, demostrando que la transformada de Fourier preserva la energía. Este teorema es esencial para entender cómo se distribuye la energía de una señal en el espectro de frecuencias y tiene aplicaciones directas en diseño de filtros, análisis de potencia y sistemas de comunicaciones.

### Desarrollo Conceptual

#### 1. Enunciado Matemático Completo

**Para señales de energía (no periódicas)**:
$$E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df$$

donde:
- $x(t)$ = señal en el tiempo
- $X(f)$ = Transformada de Fourier de $x(t)$
- $E$ = energía total de la señal

**Versión con frecuencia angular** ($\omega = 2\pi f$):
$$E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} |X(\omega)|^2 d\omega$$

**Para señales de potencia (periódicas)**:
$$P = \frac{1}{T}\int_0^T |x(t)|^2 dt = \sum_{n=-\infty}^{\infty} |c_n|^2$$

donde $c_n$ son los coeficientes de la Serie de Fourier.

#### 2. Demostración Conceptual

**Partiendo de la Transformada de Fourier**:
$$X(f) = \int_{-\infty}^{\infty} x(t)e^{-j2\pi ft} dt$$

**Transformada inversa**:
$$x(t) = \int_{-\infty}^{\infty} X(f)e^{j2\pi ft} df$$

**Energía en el tiempo**:
$$E = \int_{-\infty}^{\infty} x(t) \cdot x^*(t) dt$$

Sustituyendo $x^*(t)$ con su transformada inversa:
$$E = \int_{-\infty}^{\infty} x(t) \left[\int_{-\infty}^{\infty} X^*(f)e^{-j2\pi ft} df\right] dt$$

Intercambiando el orden de integración (Fubini):
$$E = \int_{-\infty}^{\infty} X^*(f) \left[\int_{-\infty}^{\infty} x(t)e^{-j2\pi ft} dt\right] df$$

La integral interna es precisamente $X(f)$:
$$E = \int_{-\infty}^{\infty} X^*(f) \cdot X(f) df = \int_{-\infty}^{\infty} |X(f)|^2 df$$

**Q.E.D.**

#### 3. Interpretación Física

**Densidad Espectral de Energía**:
Definimos $\mathcal{E}(f) = |X(f)|^2$ como la **densidad espectral de energía**.

Parseval nos dice:
$$E_{total} = \int_{-\infty}^{\infty} \mathcal{E}(f) df$$

**Significado**:
- $\mathcal{E}(f)df$ = energía contenida en el intervalo de frecuencia $[f, f+df]$
- La energía se "distribuye" a lo largo del espectro
- Podemos calcular energía en cualquier banda integrando en ese rango

**Energía en una banda específica** $[f_1, f_2]$:
$$E_{banda} = \int_{f_1}^{f_2} |X(f)|^2 df$$

#### 4. Aplicaciones del Teorema

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

**c) Ancho de banda equivalente**

Definimos el ancho de banda equivalente de ruido:
$$B_n = \frac{\int_0^{\infty} |H(f)|^2 df}{|H(f_{max})|^2}$$

**d) Relación señal-ruido**

Si señal y ruido son independientes:
$$SNR = \frac{E_{señal}}{E_{ruido}} = \frac{\int |X(f)|^2 df}{\int |N(f)|^2 df}$$

### Ejemplos Prácticos

#### Ejemplo 1: Pulso Rectangular

**Señal en el tiempo**:
$$x(t) = \begin{cases} A & |t| \leq T/2 \\ 0 & |t| > T/2 \end{cases}$$

**Energía en el tiempo** (directo):
$$E_t = \int_{-T/2}^{T/2} A^2 dt = A^2 T$$

**Transformada de Fourier**:
$$X(f) = AT \text{sinc}(\pi fT) = AT \frac{\sin(\pi fT)}{\pi fT}$$

**Energía en frecuencia** (Parseval):
$$E_f = \int_{-\infty}^{\infty} |AT \text{sinc}(\pi fT)|^2 df = A^2T^2 \int_{-\infty}^{\infty} \text{sinc}^2(\pi fT) df$$

Usando la integral conocida:
$$\int_{-\infty}^{\infty} \text{sinc}^2(x) dx = 1$$

Con cambio de variable $x = \pi fT$, $dx = \pi T df$:
$$E_f = A^2T^2 \cdot \frac{1}{\pi T} \cdot \pi = A^2T$$ ✓

**Verificación**: $E_t = E_f$ como predice Parseval.

#### Ejemplo 2: Señal Sinusoidal Modulada por Exponencial

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

Calcular $|X(f)|^2$ e integrar sería laborioso, pero conceptualmente más claro.

#### Ejemplo 3: Ancho de Banda del 99% de Energía

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

### Relación con Otros Conceptos

**Prerequisites**:
- Transformada de Fourier y sus propiedades
- Concepto de señales de energía vs. potencia
- Integración compleja (para demostraciones rigurosas)

**Conexiones directas**:
- **Densidad espectral de potencia** (PSD): versión para señales de potencia
- **Teorema de Wiener-Khinchin**: relaciona autocorrelación con PSD
- **Teorema del Muestreo**: ancho de banda determina tasa mínima
- **Filtrado óptimo**: diseño de filtros adaptados (matched filter)

**Aplicaciones en comunicaciones**:
- **Análisis de ancho de banda**: cuánto espectro ocupa una señal
- **Eficiencia energética**: distribución de potencia TX
- **Diseño de filtros**: preservar energía en banda útil
- **Detección óptima**: maximizar SNR en recepción

### Puntos Clave para Recordar

1. **Conservación de energía**: TF no cambia la energía total
2. **Dos dominios, una energía**: $E_{tiempo} = E_{frecuencia}$
3. **Densidad espectral**: $|X(f)|^2$ indica distribución de energía
4. **Herramienta práctica**: a veces más fácil calcular en frecuencia
5. **Base del filtrado**: entender cómo filtros afectan energía

**Fórmulas clave**:
- Parseval: $\int |x(t)|^2 dt = \int |X(f)|^2 df$
- Densidad espectral: $\mathcal{E}(f) = |X(f)|^2$
- Energía en banda: $E_{[f_1,f_2]} = \int_{f_1}^{f_2} |X(f)|^2 df$

**Regla mnemotécnica**:
> "La energía no se crea ni destruye, solo se transforma... en frecuencia"

### Errores Comunes

1. **Olvidar el factor $1/(2\pi)$ en versión con $\omega$**: Importante distinguir $f$ vs. $\omega$
2. **Confundir con señales de potencia**: Parseval para energía es diferente que para potencia
3. **Signos incorrectos**: $|X(f)|^2 = X(f) \cdot X^*(f)$, no $X(f)^2$
4. **Límites de integración**: $-\infty$ a $+\infty$, no solo frecuencias positivas (excepto si se especifica)
5. **Olvidar que energía es positiva**: $|x(t)|^2$, no $x(t)^2$ (si $x$ es compleja)
6. **Aplicar a señales de potencia infinita**: Teorema es para señales de energía finita

### Referencias y Profundización

**Conceptos relacionados**:
- **Transformada de Fourier**: base matemática
- **Teorema de convolución**: dual en frecuencia
- **Teorema de modulación**: traslación espectral preserva energía
- **Lema de Schwarz**: desigualdad relacionada

**Extensiones**:
- **Teorema de Parseval generalizado**: producto de dos señales
  $$\int x(t)y^*(t) dt = \int X(f)Y^*(f) df$$
- **Versión discreta** (DFT):
  $$\sum_{n=0}^{N-1} |x[n]|^2 = \frac{1}{N}\sum_{k=0}^{N-1} |X[k]|^2$$
- **Series de Fourier**: versión para señales periódicas

**Aplicaciones avanzadas**:
- Análisis de wavelets (energía en tiempo-frecuencia)
- Teoría de información (capacidad del canal)
- Procesamiento de imágenes (energía espectral 2D)
- Mecánica cuántica (función de onda)

**Temas para profundizar**:
- Espacios de Hilbert (marco matemático riguroso)
- Teoría de operadores lineales
- Análisis funcional
- Teoría de la medida (Fubini, intercambio de integrales)
