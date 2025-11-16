# Carta 21: Comparación FM vs PM - Ventajas, Desventajas y Aplicaciones

> **Unidad 4**: Modulación Exponencial

---

## 🎯 Pregunta

Compare FM y PM en términos de ventajas, desventajas y aplicaciones.

---

## 📝 Respuesta Breve (de la carta original)

**FM (Frequency Modulation)**:
- Ventajas: excelente rechazo al ruido, amplitud constante
- Desventajas: BW grande, circuitos más complejos
- Aplicaciones: radio broadcast, audio de TV, comunicaciones móviles

**PM (Phase Modulation)**:
- Ventajas: implementación más simple, no requiere integrador/derivador
- Desventajas: sensible a ruido de fase, menos común
- Aplicaciones: modulaciones digitales (PSK), transmisión de datos

**Comparación**:
- Ambas son modulaciones exponenciales (amplitud constante)
- FM más popular para aplicaciones analógicas
- PM base de modulaciones digitales modernas

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La **comparación entre FM y PM** revela una fascinante dualidad en las modulaciones angulares. Aunque matemáticamente relacionadas (una es la derivada/integral de la otra), sus características prácticas las han llevado a dominar diferentes nichos tecnológicos. FM reina en el mundo analógico del audio broadcast, mientras PM es la base fundamental de las comunicaciones digitales modernas.

**¿Por qué es importante este concepto?** Entender las diferencias entre FM y PM es crucial para el diseño de sistemas de comunicación. La elección entre ellas determina la complejidad del hardware, la calidad de transmisión, y la eficiencia espectral del sistema. Cada tecnología de comunicación moderna, desde tu radio FM hasta el 5G de tu smartphone, tomó una decisión consciente entre estas modulaciones o sus derivadas.

**¿Dónde se aplica?** FM domina en radio comercial (88-108 MHz), walkie-talkies, audio de TV analógica, y sintetizadores musicales. PM es fundamental en GPS (BPSK), WiFi (QAM basado en PM), comunicaciones satelitales (QPSK), y toda la familia de modulaciones PSK/QAM digitales. La elección depende de si se transmite información analógica (voz/música) o digital (datos).

**Historia relevante:** Edwin Armstrong patentó FM en 1933, revolucionando la radiodifusión. PM fue desarrollada casi simultáneamente, pero su verdadero potencial no se realizó hasta la era digital. La ironía histórica es que Armstrong inicialmente intentaba crear PM pero "accidentalmente" inventó FM, que resultó ser superior para audio analógico.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Modulación angular básica** (Carta 16): relación matemática FM-PM
- **Índice de modulación** (Carta 17): comportamiento diferente en FM y PM
- **Espectro de señales moduladas**: funciones de Bessel
- **Ruido de fase vs. ruido de frecuencia**: diferentes impactos

#### Desarrollo Paso a Paso

**Paso 1: Relación matemática fundamental**

FM y PM están íntimamente relacionadas:

**FM (Modulación de Frecuencia):**
$$s_{FM}(t) = A_c \cos\left[2\pi f_c t + 2\pi k_f \int_{-\infty}^{t} m(\tau) d\tau\right]$$

La frecuencia instantánea: $f_i(t) = f_c + k_f m(t)$

**PM (Modulación de Fase):**
$$s_{PM}(t) = A_c \cos[2\pi f_c t + k_p m(t)]$$

La fase instantánea: $\phi_i(t) = 2\pi f_c t + k_p m(t)$

**Relación clave:** FM de $m(t)$ = PM de $\int m(t) dt$

**Paso 2: Comportamiento espectral diferente**

Para una señal sinusoidal $m(t) = A_m \cos(2\pi f_m t)$:

**Índice de modulación FM:**
$$\beta_{FM} = \frac{k_f A_m}{f_m} = \frac{\Delta f}{f_m}$$
- Depende inversamente de la frecuencia moduladora

**Índice de modulación PM:**
$$\beta_{PM} = k_p A_m$$
- Independiente de la frecuencia moduladora

Esta diferencia es crucial: FM tiene "memoria" (integración), PM responde instantáneamente.

**Paso 3: Respuesta al ruido**

El ruido afecta diferentemente:

**FM:** Ruido causa desviaciones de frecuencia aleatorias
- Después del discriminador: ruido crece con f²
- Preénfasis/deénfasis muy efectivos

**PM:** Ruido causa fluctuaciones de fase aleatorias
- Impacto uniforme en todas las frecuencias
- Más sensible al jitter y ruido de fase

#### Derivación Matemática

**Análisis comparativo de ancho de banda:**

Para modulación sinusoidal, ambas usan la regla de Carson, pero con índices diferentes:

**FM:**
$$BW_{FM} = 2(f_m + \Delta f) = 2f_m(1 + \beta_{FM})$$

Para señal de audio compleja:
$$\beta_{FM}(f) = \frac{k_f |M(f)|}{f}$$

El índice decrece con frecuencia → FM favorece bajas frecuencias.

**PM:**
$$BW_{PM} = 2f_m(1 + \beta_{PM})$$

Para señal de audio:
$$\beta_{PM}(f) = k_p |M(f)|$$

El índice es constante → todas las frecuencias contribuyen igualmente.

**Resultado clave:**
$$\boxed{\text{FM es eficiente para audio, PM para datos digitales}}$$

**Significado físico:**
- FM: naturalmente comprime el espectro de audio (menos BW para altas frecuencias)
- PM: preserva fielmente las transiciones rápidas (ideal para pulsos digitales)

### 🔬 Intuición y Analogías

**Analogía principal:**
FM es como un velocímetro que mide qué tan rápido cambias de dirección, mientras PM es como un GPS que marca tu posición angular exacta. Si estás navegando con música suave (cambios graduales), el velocímetro (FM) es más natural. Si necesitas coordenadas precisas en instantes específicos (datos digitales), el GPS (PM) es superior.

**Intuición física:**
Imagina un péndulo. FM controla la velocidad de oscilación - más rápido o más lento según la señal. PM controla la posición angular directa - salta a ángulos específicos. Para movimientos suaves (audio), controlar velocidad es natural. Para posiciones discretas (digital), control directo de ángulo es mejor.

**Visualización:**
En un osciloscopio:
- FM: la señal se "comprime" y "expande" horizontalmente (período variable)
- PM: la señal "salta" en fase manteniendo período constante

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Sistema de radio FM comercial vs. comunicación QPSK satelital

**Situación:** Comparar implementaciones reales de FM y PM.

**FM Broadcast (88-108 MHz):**

| Parámetro | Valor | Razón |
|-----------|-------|--------|
| Modulación | FM estéreo | Calidad de audio superior |
| Desviación | ±75 kHz | Balance calidad/ancho de banda |
| Ancho de banda | 200 kHz | Regla de Carson |
| Preénfasis | 75 μs | Mejora SNR en agudos |
| SNR típico | 60 dB | Alta fidelidad |

**Ventajas en esta aplicación:**
- Audio natural sin distorsión
- Inmunidad a variaciones de amplitud
- Compatibilidad mono/estéreo

**QPSK Satelital (basado en PM):**

| Parámetro | Valor | Razón |
|-----------|-------|--------|
| Modulación | QPSK (4-PM) | 2 bits/símbolo |
| Fases | 0°, 90°, 180°, 270° | Máxima separación |
| Tasa de símbolos | 30 Msym/s | Alta capacidad |
| Eficiencia espectral | ~2 bits/s/Hz | Uso eficiente del espectro |
| BER objetivo | 10⁻⁶ | Comunicación confiable |

**Ventajas en esta aplicación:**
- Transiciones de fase precisas para datos digitales
- Fácil sincronización de reloj
- Compatible con códigos de corrección de errores

---

#### Ejemplo 2: Generación de FM vs PM - Complejidad de implementación

**Contexto:** Diseño de moduladores para cada tipo.

**Modulador FM directo (VCO):**
```
Entrada de audio → Amplificador → VCO → Salida FM
                         ↑
                    Voltaje de control
```

Componentes necesarios:
- VCO (oscilador controlado por voltaje)
- Linealización del VCO
- Estabilización de frecuencia central

Complejidad: Media (el VCO debe ser muy lineal)

**Modulador PM directo (Phase shifter):**
```
Oscilador → Desfasador variable → Salida PM
                    ↑
              Señal moduladora
```

Componentes necesarios:
- Oscilador estable
- Modulador de fase (varactor o línea de retardo)
- Rango limitado de fase (necesita reset)

Complejidad: Baja para rangos pequeños, alta para rangos grandes

**Conversión indirecta:**
- FM desde PM: Integrar la moduladora primero
- PM desde FM: Derivar la moduladora primero

Esto explica por qué algunos transmisores FM usan PM con integrador previo.

---

#### Ejemplo 3: Comportamiento ante diferentes señales

**¿Qué pasa con distintos tipos de contenido?**

**Señal de voz (300-3000 Hz):**

*FM:*
- Desviación típica: ±5 kHz (narrowband)
- Índice β variable: alto en bajas frecuencias
- Resultado: voz clara, natural

*PM:*
- Desviación de fase: ±1 radian
- Necesita ecualización para voz natural
- Usado principalmente en radios digitales con vocoder

**Tono puro de prueba (1 kHz):**

*FM:*
- Desviación constante: ±75 kHz (broadcast)
- Espectro de Bessel bien definido
- β = 75 (banda ancha)

*PM:*
- Desviación de fase: proporcional a amplitud
- Espectro idéntico a FM con β constante
- Más fácil de analizar matemáticamente

**Datos digitales (pulsos rectangulares):**

*FM (FSK):*
- Transiciones suaves entre frecuencias
- Ocupa más ancho de banda
- Robusto pero ineficiente

*PM (PSK):*
- Transiciones instantáneas de fase
- Ancho de banda mínimo
- Eficiente espectralmente

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Modulación exponencial básica** (Carta 16): Fundamento matemático FM-PM
- **QAM** (Carta 29): Evolución de PM para mayor eficiencia
- **OFDM** (Carta 53): Usa subportadoras moduladas en fase/amplitud
- **Spread Spectrum** (Carta 50): Puede usar FM (FH) o PM (DS)

#### Dependencias (lo que necesitas saber primero)
1. Análisis de Fourier → Para entender espectros FM/PM
2. Funciones de Bessel → Para calcular componentes espectrales
3. Ruido en sistemas → Para comparar desempeño

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Modulaciones híbridas**: GMSK (combina ventajas de ambas)
2. **Software Defined Radio**: Implementación flexible FM/PM
3. **5G NR**: Modulaciones basadas en PM (π/2-BPSK, QAM)
4. **Síntesis de audio**: FM synthesis vs PM synthesis

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- FM y PM son matemáticamente duales (derivada/integral)
- FM es superior para audio analógico por su respuesta al ruido
- PM es base de modulaciones digitales por sus transiciones precisas
- La elección depende de la aplicación, no hay una "mejor" universal

#### Tipos de problemas típicos
1. **Conversión FM↔PM**: Dado un modulador, generar el otro tipo
   - Estrategia: Agregar integrador o derivador según el caso

2. **Análisis espectral comparativo**: Calcular BW para misma señal
   - Estrategia: Considerar cómo varía β con frecuencia

3. **Selección de modulación**: Elegir FM o PM para aplicación dada
   - Estrategia: Evaluar tipo de información, ancho de banda, complejidad

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Asumir que FM y PM son intercambiables**
- Por qué ocurre: Son matemáticamente relacionadas
- Cómo evitarlo: Recordar que sus características prácticas difieren mucho
- Ejemplo: FM broadcast no funcionaría bien con PM directa

❌ **Error #2: Ignorar el comportamiento del índice de modulación**
- Por qué ocurre: No considerar dependencia de frecuencia
- Cómo evitarlo: β_FM ∝ 1/f_m, β_PM = constante
- Impacto: Ancho de banda muy diferente para señales complejas

❌ **Error #3: Confundir PM analógica con PSK digital**
- Por qué ocurre: PSK es "phase shift keying" - parece PM
- Cómo evitarlo: PSK usa fases discretas, PM es continua
- Clarificación: PSK es aplicación digital de principios PM

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
FM: f_i(t) = f_c + k_f·m(t)
PM: φ_i(t) = 2πf_c·t + k_p·m(t)
Relación: FM[m(t)] = PM[∫m(t)dt]
β_FM = Δf/f_m, β_PM = k_p·A_m
```

#### Conceptos Fundamentales
- ✓ **Dualidad matemática**: FM y PM relacionadas por integración/derivación
- ✓ **FM para audio**: Natural para señales analógicas continuas
- ✓ **PM para datos**: Ideal para símbolos digitales discretos

#### Reglas Mnemotécnicas
- 🧠 **"FM-Fluido, PM-Preciso"**: FM fluye continuamente, PM posiciona precisamente
- 🧠 **"Audio→FM, Digital→PM"**: Regla práctica de selección
- 🧠 **"FM∫, PM'"**: FM integra, PM deriva (respecto a la otra)

#### Valores Típicos (para referencias rápidas)
| Aplicación | Tipo | Parámetros Típicos |
|------------|------|-------------------|
| Radio broadcast | FM | ±75 kHz desviación |
| Radio móvil | FM | ±5 kHz (narrowband) |
| GPS | BPSK (PM) | 2 fases, 1.023 Mchips/s |
| WiFi | QAM (basado en PM) | Hasta 1024-QAM |
| TV satelital | QPSK (PM) | 4 fases, 30 Msym/s |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - "Angle Modulation" de Panter - tratamiento matemático riguroso
  - "Digital Communications" de Proakis - enfoque en PM/PSK digital
  - "FM Stereo Technology" - aplicaciones prácticas de FM
- **Papers históricos**: Armstrong (1936) - "A Method of Reducing Disturbances in Radio Signaling by a System of Frequency Modulation"
- **Simulaciones**: MATLAB/Simulink - comparación visual FM vs PM

#### Temas Relacionados para Explorar
1. GMSK - Híbrido usado en GSM
2. CPM (Continuous Phase Modulation) - generalización
3. Síntesis FM en música electrónica (Yamaha DX7)
4. Optical PM en comunicaciones de fibra

#### Preguntas para Reflexionar
- ¿Por qué no existe "AM digital" exitosa pero sí PM digital (PSK)?
- ¿Podría diseñarse un sistema que aproveche ventajas de ambas?
- ¿Cómo afecta el multitrayecto diferentemente a FM vs PM?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 60 minutos
**Prerequisitos críticos**: Modulación angular, análisis espectral, sistemas digitales básicos
**Tags**: `#FM` `#PM` `#comparacion` `#modulacion-angular` `#digital` `#analogico`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*