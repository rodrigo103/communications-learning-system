# Modulación BPSK sobre FM en telemetría espacial

**Fecha:** 2025-11-20

**Rodrigo** (2025-11-20 20:05:48):

Como funciona la modulación de datos digitales?
Por ejemplo, sistema BPSK sobre FM (telemetría espacial)

---

**Claude** (2025-11-20 20:06:23):

# Modulación Digital: BPSK sobre FM en Telemetría Espacial

Este es un ejemplo perfecto de **modulación en cascada** que ilustra cómo la ingeniería práctica requiere múltiples etapas para resolver diferentes problemas.

## La Arquitectura de Dos Etapas

**Nivel 1: BPSK (Binary Phase Shift Keying)**
- Los datos digitales (bits) modulan la **fase** de una subportadora de frecuencia fija
- Bit "0" → fase 0°
- Bit "1" → fase 180°

**Nivel 2: FM**
- La señal BPSK resultante modula la **frecuencia** de la portadora RF principal

Matemáticamente:
```
Datos → [BPSK] → s_BPSK(t) → [FM] → s_RF(t)

s_BPSK(t) = A·cos(2πf_sub·t ± π)  [subportadora modulada]
s_RF(t) = A_c·cos(2πf_c·t + k_f∫s_BPSK(τ)dτ)  [señal final]
```

## ¿Por Qué Esta Arquitectura "Redundante"?

Aquí está la clave: **cada etapa resuelve un problema diferente**.

### BPSK: Robustez frente a ruido
- Máxima separación entre símbolos (180° de diferencia)
- Detección coherente = mejor performance en bajo SNR
- Solo 2 estados = decisión binaria simple

### FM: Transmisión por el canal espacial
1. **Amplificación eficiente**: Los transmisores espaciales usan amplificadores **no lineales** (Clase C) para máxima eficiencia energética → FM mantiene envolvente constante
2. **Captura del canal**: El efecto de captura de FM rechaza señales interferentes más débiles
3. **Inmunidad a variaciones de amplitud**: Fading atmosférico, efectos ionosféricos
4. **Simplicidad de detección**: Los receptores FM son más simples que receptores coherentes directos

## El Concepto de Subportadora

La subportadora (típicamente 1-10 MHz) actúa como **banda base analógica** para el transmisor FM:

```
Bits → Subportadora BPSK → "Señal analógica" → Transmisor FM → Canal
```

Esto permite usar **hardware FM estándar** (que fue diseñado para audio/analógico) para transmitir datos digitales.

## Análisis Espectral

El espectro final tiene una estructura compleja:

**Ancho de banda BPSK**: ~2·R_b (donde R_b = bit rate)

**Ancho de banda FM**: Regla de Carson
```
B_FM ≈ 2(Δf + f_sub·m)
```
donde:
- Δf = desviación de frecuencia 
- m = índice de modulación BPSK
- f_sub = frecuencia de subportadora

## Ejemplo Práctico: Voyager

Las sondas Voyager usan precisamente este esquema:
- Subportadora BPSK a varios MHz
- Transmisión FM en banda S (2.3 GHz) o banda X (8.4 GHz)
- Potencia de transmisión: solo 23 watts
- Distancia: miles de millones de kilómetros

La razón histórica: aprovechar la **infraestructura existente** de receptores FM desarrollados para comunicaciones analógicas, añadiendo solo un demodulador BPSK después del discriminador FM.

## Comparación con Alternativas

**¿Por qué no BPSK directo sobre la portadora RF?**
- Requeriría detección coherente a GHz → circuitos complejos, inestabilidad de fase
- Los amplificadores de potencia espaciales son más eficientes con envolvente constante

**¿Por qué no FSK directo?**
- BPSK tiene mejor performance que FSK binario para el mismo SNR (~3 dB de ventaja)
- La estructura de dos etapas permite optimizar cada etapa independientemente

## Ventaja de Performance

La ganancia total del sistema combina:
1. **Ganancia de BPSK**: Detección coherente, máxima distancia entre símbolos
2. **Ganancia de FM**: Mejora de SNR proporcional a β² (índice de modulación)
3. **Ganancia de procesamiento**: La banda ancha FM se "colapsa" en el demodulador

¿Querés que profundicemos en algún aspecto particular? Por ejemplo:
- El análisis matemático detallado del SNR en cascada
- La implementación práctica de los demoduladores
- Cómo se relaciona esto con el spread spectrum que viste en la Unidad 10

> [!note]- Thinking
> El usuario Rodrigo me pregunta sobre cómo funciona la modulación de datos digitales, específicamente el caso de BPSK sobre FM en telemetría espacial. Esto es un tema interesante que combina dos niveles de modulación.
> 
> Dado su perfil, Rodrigo busca entender los fundamentos, las derivaciones matemáticas y las conexiones entre teoría y práctica. No quiere solo una descripción superficial, sino entender el "por qué" de las decisiones de ingeniería.
> 
> Voy a explicar:
> 1. La modulación digital básica (BPSK)
> 2. Por qué se usa una modulación sobre otra (BPSK sobre FM)
> 3. El concepto de subportadora
> 4. Las ventajas prácticas de este esquema en telemetría espacial
> 
> Me voy a enfocar en la comprensión conceptual primero, luego en las matemáticas, y finalmente en las razones prácticas/históricas que justifican este diseño aparentemente redundante.

---

**Rodrigo** (2025-12-04 03:51:23):

Que es la detección coherente a GHz?

---

**Claude** (2025-12-04 03:52:05):

# Detección Coherente a GHz: El Problema Fundamental

Excelente pregunta que va al corazón de por qué la arquitectura en cascada tiene sentido.

## ¿Qué es Detección Coherente?

**Matemáticamente**, para demodular BPSK necesitás:

```
s(t) = A·cos(2πf_c·t + θ_datos)  [señal recibida]

Demodulador coherente:
s(t) × 2·cos(2πf_c·t + θ_ref) → [Filtro PB] → Decisión

Si θ_ref = θ_portadora → detección óptima
Si θ_ref ≠ θ_portadora → pérdida de SNR (factor cos(Δθ))
```

**Requerimientos**:
1. **Oscilador local** sincronizado con la portadora recibida
2. **Mezclador** que multiplique señal × referencia
3. **Recuperación de portadora**: circuito PLL que "enganche" la fase

## El Problema a GHz (2-8 GHz en espacial)

### 1. **Estabilidad de Fase del Oscilador**

A 2.3 GHz (banda S de Voyager):
- Si tu oscilador tiene inestabilidad de 1 ppm (parte por millón)
- Error de frecuencia: 2.3 GHz × 10⁻⁶ = **2.3 kHz**

Para un símbolo de duración T_s = 1 ms (bit rate bajo en espacio):
- Rotación de fase: 2π × 2.3 kHz × 0.001 s = **14.5 radianes** ≈ 2.3 vueltas completas
- Resultado: **pérdida total de sincronismo**

**En contraste**, con subportadora a 1 MHz:
- Mismo 1 ppm → 1 Hz de error
- Rotación en 1 ms: 2π × 1 Hz × 0.001 s = **0.006 radianes** ≈ 0.36°
- **Completamente manejable**

### 2. **Ruido de Fase**

Los osciladores tienen **ruido de fase** L(f) que aumenta con la frecuencia:

```
Jitter de fase ≈ √(∫ L(f)df)
```

A GHz, el ruido de fase es mucho mayor que a MHz, causando:
- Fluctuaciones aleatorias de fase
- Degradación del SNR efectivo
- Dificultad para mantener "enganche" del PLL

### 3. **Efecto Doppler en Comunicaciones Espaciales**

Para una nave a velocidad v:
```
Δf = (v/c)·f_c
```

Voyager alejándose a 17 km/s:
- A 2.3 GHz: Δf = (17000/3×10⁸) × 2.3×10⁹ = **130 kHz**
- A 1 MHz (subportadora): Δf = 57 Hz

El PLL debe "seguir" esta deriva de frecuencia. A GHz es muchísimo más difícil mantener enganche coherente.

### 4. **Complejidad del Hardware**

**Recuperación de portadora a GHz requiere**:
- VCO (oscilador controlado por tensión) estable a GHz → difícil, caro, consume potencia
- PLL con ancho de banda adecuado → conflicto entre velocidad de adquisición y ruido
- Componentes RF de muy bajo ruido de fase

**A MHz** (después de bajar con FM):
- Osciladores de cristal ultra-estables
- PLLs digitales implementables en FPGA
- Tecnología madura y confiable

## La Solución Práctica: Arquitectura Superheterodina

Por eso las comunicaciones espaciales usan:

```
[Antena] → [Mezclador] → [IF FM] → [Discriminador FM] → [Subportadora BPSK] → [Demodulador coherente]
         ↗                                                                    ↗
    [LO estable]                                              [Recuperador de portadora simple]
       GHz                                                              MHz
```

**Primera bajada** (GHz → IF):
- Solo necesitás un LO estable (no sincronizado con datos)
- FM tolera derivas de frecuencia

**Segunda etapa** (MHz):
- Detección coherente en frecuencias manejables
- Circuitos digitales pueden hacer todo el procesamiento

## Analogía Conceptual

Es como intentar enhebrar una aguja:
- **A GHz**: La aguja vibra 2,300,000,000 veces por segundo, y necesitás que tu hilo vibre **exactamente** en fase
- **A MHz**: La aguja vibra solo 1,000,000 veces por segundo, mucho más controlable

## Por Qué Funciona la Cascada

```
Datos → [BPSK @ MHz] → [FM @ GHz] → Canal espacial

Receptor:
Canal → [Discriminador FM] → [Señal @ MHz] → [BPSK coherente] → Datos
```

**La magia**: El discriminador FM es **no coherente**, solo detecta cambios de frecuencia. No necesita referencia de fase a GHz. Entrega la subportadora donde **ahora sí** podés hacer detección coherente cómodamente.

## Nota Histórica

Este es un patrón recurrente en ingeniería: cuando algo es difícil a alta frecuencia, **bajá a frecuencia intermedia** donde tu tecnología es más madura. Es el mismo principio del receptor superheterodino que estudiaste en la Unidad 3 (modulación lineal).

¿Querés que veamos cómo se implementa prácticamente un recuperador de portadora (Costas loop, squaring loop) para la subportadora BPSK?

> [!note]- Thinking
> Rodrigo está preguntando sobre "detección coherente a GHz" - esto es una pregunta fundamental sobre por qué es difícil hacer detección coherente directamente en frecuencias de RF de GHz (como las usadas en comunicaciones espaciales).
> 
> Déjame explicar esto de manera rigurosa, conectando con sus conocimientos previos de modulación digital y receptores superheterodinos.
> 
> La detección coherente requiere:
> 1. Una referencia de fase sincronizada con la portadora recibida
> 2. Mezcladores (multiplicadores) que funcionen a la frecuencia de la portadora
> 3. Estabilidad de fase durante el tiempo de símbolo
> 
> A GHz esto se vuelve extremadamente difícil por razones prácticas de hardware.

---

