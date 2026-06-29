# Carta 23: PCM (Pulse Code Modulation) y sus Etapas Principales

> **Unidad 5**: Modulación de Pulsos

---

## 🎯 Pregunta

Describa el proceso de PCM (Pulse Code Modulation) y sus etapas principales.

---

## 📝 Respuesta Breve (de la carta original)

**PCM** digitaliza señales analógicas en tres etapas:

**1. Muestreo**:
- Frecuencia: $f_s ≥ 2f_m$ (Nyquist)
- Genera PAM natural

**2. Cuantificación**:
- Divide rango en $L = 2^n$ niveles
- Error de cuantificación: $e_q ≤ \Delta/2$ donde $\Delta$ = paso de cuantificación
- SNR cuantificación: $SNR_q ≈ 6n + 1.76$ dB (n = bits)

**3. Codificación**:
- Asigna código binario de n bits a cada nivel
- Transmite secuencia de bits

**Ventajas**: inmunidad al ruido, regeneración, procesamiento digital
**Desventaja**: mayor ancho de banda

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

PCM (Pulse Code Modulation) representa uno de los inventos más transformadores en la historia de las comunicaciones, convirtiendo el mundo analógico en digital. Patentado por Alec Reeves en 1937, PCM no fue práctica hasta la invención del transistor, pero ahora es la base de toda comunicación digital moderna.

**¿Por qué es importante este concepto?** PCM es el fundamento de la era digital. Cada llamada telefónica, cada canción en Spotify, cada video en YouTube, comenzó como una señal analógica convertida a digital mediante PCM o sus derivados. Es el puente entre el mundo físico analógico y el procesamiento digital que domina la tecnología moderna.

**¿Dónde se aplica?** PCM está en todas partes: telefonía digital (G.711), audio CD (44.1 kHz, 16 bits), grabación de estudio (hasta 192 kHz, 24 bits), conversión analógico-digital en smartphones, sistemas de comunicación satelital, y como base para compresión de audio/video (MP3, AAC, H.264).

**Historia relevante:** Durante la Segunda Guerra Mundial, el sistema SIGSALY usó PCM para encriptar comunicaciones entre Churchill y Roosevelt. Bell System implementó el primer sistema PCM comercial (T1) en 1962, revolucionando la telefonía. El CD, lanzado en 1982, popularizó PCM para consumidores, estableciendo 44.1 kHz como frecuencia icónica.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Teorema del Muestreo de Nyquist-Shannon (fundamental)
- Conversión analógico-digital (ADC)
- Sistemas numéricos binarios
- Análisis de ruido y SNR
- PAM como etapa previa (Carta 22)

#### Desarrollo Paso a Paso

**Paso 1: Muestreo - Capturando el Tiempo**

El muestreo convierte la señal continua $x(t)$ en una secuencia discreta $x(nT_s)$:

$$x_s(t) = x(t) \cdot \sum_{n=-\infty}^{\infty} \delta(t - nT_s) = \sum_{n=-\infty}^{\infty} x(nT_s) \delta(t - nT_s)$$

La frecuencia de muestreo debe satisfacer Nyquist:
$$f_s \geq 2f_{max}$$

En el dominio frecuencial:
$$X_s(f) = f_s \sum_{k=-\infty}^{\infty} X(f - kf_s)$$

Esto muestra que el espectro se replica cada $f_s$ Hz. Si $f_s < 2f_{max}$, las réplicas se solapan (aliasing).

**Paso 2: Cuantificación - Discretizando la Amplitud**

La cuantificación mapea infinitos valores posibles a L niveles finitos:

Para cuantificación uniforme con rango $[-V_{max}, +V_{max}]$:

$$\Delta = \frac{2V_{max}}{L} = \frac{2V_{max}}{2^n}$$

El valor cuantificado $x_q$ para una entrada $x$:
$$x_q = \Delta \cdot \text{round}\left(\frac{x}{\Delta}\right)$$

El error de cuantificación:
$$e_q = x - x_q$$

con $-\Delta/2 \leq e_q \leq \Delta/2$

**Paso 3: Análisis del Ruido de Cuantificación**

Modelando el error como ruido uniforme:

Potencia del error:
$$\sigma_q^2 = \int_{-\Delta/2}^{\Delta/2} e^2 \cdot \frac{1}{\Delta} de = \frac{\Delta^2}{12}$$

Para señal senoidal de amplitud completa:
$$\text{Potencia señal} = \frac{V_{max}^2}{2}$$

SNR de cuantificación:
$$SNR_q = 10\log_{10}\left(\frac{V_{max}^2/2}{\Delta^2/12}\right)$$

Sustituyendo $\Delta = 2V_{max}/2^n$:
$$SNR_q = 10\log_{10}\left(\frac{3 \cdot 2^{2n}}{2}\right) = 6.02n + 1.76 \text{ dB}$$

**La famosa regla de 6 dB/bit**

**Paso 4: Codificación - Asignación Binaria**

Cada nivel cuantificado recibe un código único de n bits:

Para codificación natural binaria:
- Nivel 0 → 000...000
- Nivel 1 → 000...001
- ...
- Nivel L-1 → 111...111

Tasa de bits resultante:
$$R_b = n \cdot f_s \text{ bits/s}$$

Para telefonía: n=8 bits, fs=8 kHz → 64 kbps por canal

#### Derivación del Ancho de Banda PCM

Para transmisión en banda base con pulsos rectangulares:

$$BW_{PCM} \approx \frac{R_b}{2} = \frac{n \cdot f_s}{2}$$

Comparado con señal analógica original de ancho de banda $f_m$:

$$\frac{BW_{PCM}}{BW_{analog}} = \frac{n \cdot f_s}{2f_m} \geq n$$

PCM intercambia ancho de banda por inmunidad al ruido.

### 🔬 Intuición y Analogías

**Analogía principal:**
PCM es como convertir una rampa suave en una escalera:
- **Muestreo**: Decidir dónde poner los escalones horizontalmente (cada cuánto)
- **Cuantificación**: Decidir la altura de cada escalón (cuántos niveles)
- **Codificación**: Numerar cada escalón para poder reconstruirlo

Entre más escalones (mayor fs) y más niveles de altura (más bits), mejor aproximación a la rampa original.

**Intuición física:**
Imagina fotografiar una onda en el mar:
- Si tomas fotos muy seguidas (alta fs), capturas todos los cambios
- Si tu cámara tiene muchos niveles de gris (muchos bits), capturas todos los matices
- Si numerás cada foto, puedes reconstruir el movimiento después

**Visualización del error de cuantificación:**
El error es como el "pixelado" en una imagen: visible cuando hay pocos niveles (pocos bits), imperceptible con suficientes niveles. En audio, pocos bits suenan "granulosos" o "arenosos".

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Sistema PCM para Música

**Situación:** Diseñar PCM para calidad CD de audio

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Frecuencia máxima audible | 20 | kHz |
| Rango dinámico deseado | 96 | dB |
| Canales | 2 | estéreo |

**Solución paso a paso:**

1. **Frecuencia de muestreo (Nyquist):**
   $$f_s = 2.2 \times f_{max} = 2.2 \times 20 = 44 \text{ kHz}$$
   (Se usa 44.1 kHz en CD por razones históricas de video)

2. **Bits necesarios para 96 dB SNR:**
   $$SNR = 6.02n + 1.76 = 96$$
   $$n = \frac{96 - 1.76}{6.02} = 15.68 \approx 16 \text{ bits}$$

3. **Tasa de bits total:**
   $$R_b = 2 \times 16 \times 44100 = 1,411,200 \text{ bps} = 1.411 \text{ Mbps}$$

4. **Capacidad de un CD (74 minutos):**
   $$\text{Datos} = 1.411 \times 10^6 \times 74 \times 60 = 626 \text{ MB}$$

**Interpretación:** El estándar CD usa exactamente estos parámetros, demostrando que PCM permite calidad transparente para el oído humano.

---

#### Ejemplo 2: Telefonía Digital G.711

**Contexto:** Sistema PCM estándar para voz en telefonía

El estándar G.711 usa:
- Frecuencia de muestreo: 8 kHz (voz hasta 3.4 kHz)
- Cuantificación: 8 bits con companding (μ-law o A-law)
- Tasa de bits: 64 kbps por canal

> [!note]- 📡 Companding (μ-law / A-law): ¿qué es?
> **Companding** = **Comp**ressing + **Exp**anding. Es cuantificación **no uniforme** que mejora la SNR para señales débiles sin aumentar el número de bits.
>
> **Problema:** En cuantificación uniforme con 8 bits, las señales débiles sufren error relativo muy grande (SNR ≈ 9.9 dB en voz con 40 dB de rango). Las fuertes "desperdician" resolución.
>
> **Solución:** Pasos de cuantificación **variables**:
> - **Pequeños** donde la señal es débil → alta resolución
> - **Grandes** donde la señal es fuerte → resolución suficiente
>
> **Dos leyes (G.711):**
> - **μ-law** ($\mu = 255$): Norteamérica y Japón
>   $$C_\mu(x) = \text{sgn}(x) \cdot \frac{\ln(1 + \mu|x/V_{max}|)}{\ln(1 + \mu)}$$
> - **A-law** ($A = 87.6$): Europa y resto del mundo (función lineal + logarítmica)
>
> **Proceso:** comprimir en TX → cuantificar uniforme → expandir en RX ($C^{-1}$). Mejora el rango dinámico en ≈ $20\log_{10}(\mu) \approx 48$ dB **sin aumentar bits**. ⚠️ μ-law y A-law **no son compatibles** entre sí.

Para una central telefónica con 30 canales (E1 europeo):

**Trama PCM:**
- 30 canales de voz + 2 canales de señalización
- 32 × 8 bits × 8000 Hz = 2.048 Mbps

> [!note]- 📡 Canales de señalización E1: ¿para qué sirven?
> Los 2 slots no-voz de la trama E1 son:
> - **TS0**: sincronización de trama (*Frame Alignment Word*). Sin él, el receptor no sabe dónde empieza cada trama y los 30 canales se mezclan.
> - **TS16**: señalización por canal asociado (CAS). Transporta la info de control de los 30 canales rotando en una *multitrama* de 16 tramas.
>
> **Qué viaja en la señalización:**
> - **Supervisión:** off-hook (descolgó), on-hook (colgó), contestó
> - **Direccionamiento:** dígitos marcados (DTMF o decádicos)
> - **Tasación:** pulsos de billing
> - **Alarmas:** pérdida de señal, falla de equipo
>
> Equivalente digital del "tono de llamada" y "tono de ocupado": sin señalización, los canales transmitirían voz pero no podrían establecer ni terminar llamadas.

**Estructura temporal:**
- Período de trama: 125 μs (1/8000 Hz)
- 32 time slots de 3.9 μs cada uno
- Cada slot transporta 8 bits de un canal

> [!note]- 📡 Ancho de banda del sistema PCM (E1): ¿cuánto ocupa?
> $$BW_{PCM} \approx \frac{R_b}{2} = \frac{n \cdot f_s}{2} \quad \text{(banda base, pulsos NRZ)}$$
>
> **E1 completo (2.048 Mbps):**
> $$BW_{E1} \approx \frac{2.048 \times 10^6}{2} = 1.024 \text{ MHz}$$
>
> **Un solo canal de voz (64 kbps):**
> $$BW_{canal} \approx \frac{64 \times 10^3}{2} = 32 \text{ kHz}$$
>
> **Trade-off fundamental:** la voz original ocupa ~3.4 kHz. PCM requiere ~32 kHz por canal, casi **10× más**. Se sacrifica ancho de banda a cambio de inmunidad al ruido y capacidad de regeneración digital.
>
> En la práctica, con codificación HDB3 (usada en E1), el espectro se moldea para eliminar la DC y el primer nulo espectral cae en $R_b$ (NRZ) o menos (pulsos conformados).

---

#### Ejemplo 3: Análisis del Error de Cuantificación

**¿Qué pasa cuando la señal es débil?**

Para señal senoidal a -20 dB del fondo de escala:

**Con 8 bits (256 niveles):**
- SNR máximo: 6.02(8) + 1.76 = 49.92 dB
- SNR con señal débil: 49.92 - 20 = 29.92 dB
- Calidad: aceptable pero con ruido audible

**Con 16 bits (65536 niveles):**
- SNR máximo: 6.02(16) + 1.76 = 98.08 dB
- SNR con señal débil: 98.08 - 20 = 78.08 dB
- Calidad: excelente, ruido imperceptible

**Conclusión:** Más bits mejoran especialmente las señales débiles, por eso audio profesional usa 24 bits.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **PAM** (Carta 22): Primera etapa del proceso PCM
- **Companding** (Carta 24): Mejora SNR para señales débiles
- **Delta Modulation** (Carta 25): Alternativa a PCM
- **TDM** (Carta 26): Multiplexación de canales PCM
- **Teorema de Shannon** (Carta 45): Límites teóricos de digitalización

#### Dependencias (lo que necesitas saber primero)
1. Teorema de Nyquist → Define fs mínima
2. Conversión A/D básica → Comprensión del proceso
3. Sistemas binarios → Para entender codificación

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Codecs de audio**: MP3, AAC parten de PCM
2. **Video digital**: Cada frame es PCM 2D
3. **Comunicaciones digitales**: Base para modulaciones QAM, PSK
4. **DSP**: Todo procesamiento digital comienza con PCM

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La relación exacta entre fs, n bits, y calidad (SNR)
- Por qué 6.02 dB/bit es fundamental
- Cómo calcular tasas de bits y anchos de banda
- Trade-offs entre parámetros del sistema

#### Tipos de problemas típicos
1. **Diseño de sistema PCM**: Dados requisitos de calidad, determinar fs y n
   - Estrategia: Aplicar Nyquist para fs, regla 6 dB para bits

2. **Análisis de error**: Calcular SNR para diferentes tipos de señales
   - Estrategia: Considerar potencia de señal vs. ruido de cuantificación

3. **Comparación de sistemas**: PCM vs. otros esquemas de modulación
   - Estrategia: Evaluar tasa de bits, SNR, complejidad

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir frecuencia de muestreo con tasa de bits**
- Por qué ocurre: Ambas tienen unidades de "por segundo"
- Cómo evitarlo: fs es muestras/s, Rb = n × fs es bits/s
- Ejemplo: CD tiene fs=44.1 kHz pero Rb=1.411 Mbps

❌ **Error #2: Aplicar la regla 6 dB/bit a señales no sinusoidales**
- Por qué ocurre: La fórmula asume señal senoidal a fondo de escala
- Cómo evitarlo: Ajustar por factor de cresta de la señal real

❌ **Error #3: Ignorar el aliasing al elegir fs**
- Distinción importante: fs > 2fm no es suficiente si no hay filtro anti-aliasing

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Nyquist: fs ≥ 2fm
Niveles: L = 2^n
Paso: Δ = 2Vmax/2^n
SNR: SNRq = 6.02n + 1.76 dB
Tasa bits: Rb = n·fs
BW PCM: BW ≈ n·fs/2
```

#### Conceptos Fundamentales
- ✓ **Muestreo**: Discretización temporal según Nyquist
- ✓ **Cuantificación**: Discretización de amplitud, introduce error
- ✓ **6 dB/bit**: Cada bit adicional duplica niveles, mejora SNR 6 dB
- ✓ **Trade-off**: Ancho de banda vs. calidad (SNR)

#### Reglas Mnemotécnicas
- 🧠 **"MQC"**: Muestreo → Quantización → Codificación
- 🧠 **"6 para SNR"**: 6 dB por bit para recordar la mejora

#### Valores Típicos (para referencias rápidas)

| Parámetro | Valor Típico | Aplicación |
|-----------|--------------|------------|
| Voz telefonía | 8 kHz, 8 bits | G.711 (64 kbps) |
| CD Audio | 44.1 kHz, 16 bits | Red Book standard |
| DVD Audio | 48-192 kHz, 24 bits | Alta fidelidad |
| Bluetooth audio | 16 kHz, 16 bits | Headsets |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros**: Haykin Cap. 4.4-4.6, Proakis Digital Communications Cap. 6
- **Papers**: A. Reeves original PCM patent (1937)
- **Software**: Audacity para experimentar con muestreo/cuantificación
- **Hardware**: ADC chips datasheets (TI, Analog Devices)

#### Temas Relacionados para Explorar
1. DPCM y ADPCM (predicción adaptativa)
2. Sigma-Delta ADCs (oversampling)
3. Dithering (ruido añadido para mejorar cuantificación)
4. Non-uniform quantization (companding)

#### Preguntas para Reflexionar
- ¿Por qué el CD usa 44.1 kHz y no 40 kHz exactos?
- ¿Cómo afecta el jitter en el reloj de muestreo a la calidad?
- ¿Es posible recuperar información perdida por cuantificación?
- ¿Por qué algunos audiófilos prefieren vinilo (analógico) sobre CD (PCM)?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 35 minutos
**Prerequisitos críticos**: Teorema de Nyquist, PAM, conversión A/D
**Tags**: `#PCM` `#digitalizacion` `#muestreo` `#cuantificacion` `#6dB-bit`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*