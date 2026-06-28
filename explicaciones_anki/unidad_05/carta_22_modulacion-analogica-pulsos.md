# Carta 22: Modulación Analógica de Pulsos: PAM, PWM y PPM

> **Unidad 5**: Modulación de Pulsos

---

## 🎯 Pregunta

Explique los tipos de modulación analógica de pulsos: PAM, PWM y PPM.

---

## 📝 Respuesta Breve (de la carta original)

**PAM (Pulse Amplitude Modulation)**:
- Amplitud del pulso varía según $m(t)$
- Más simple, base de PCM
- Susceptible a ruido

**PWM (Pulse Width Modulation)**:
- Ancho del pulso varía según $m(t)$
- Amplitud constante (mayor inmunidad al ruido)
- Usado en control de potencia

**PPM (Pulse Position Modulation)**:
- Posición temporal del pulso varía según $m(t)$
- Mayor inmunidad al ruido que PWM
- Requiere sincronización precisa
- Mejor eficiencia energética

Todas permiten multiplexación por división de tiempo (TDM).

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La modulación analógica de pulsos representa el puente histórico y tecnológico entre los sistemas puramente analógicos y los digitales modernos. Estos esquemas surgieron en la década de 1940 como una forma de aprovechar las ventajas del muestreo temporal sin necesitar la complejidad completa de la digitalización.

**¿Por qué es importante este concepto?** En sistemas de comunicaciones modernos, aunque estos tipos de modulación raramente se usan en su forma pura para transmisión, forman la base conceptual de sistemas más complejos. PAM es el primer paso en PCM (Pulse Code Modulation), el estándar para telefonía digital. PWM domina en control de potencia para motores, LEDs, y conversión DC-DC. PPM encuentra uso en telemetría y control remoto.

**¿Dónde se aplica?** Encontrarás PAM en el proceso interno de conversión analógico-digital (ADC), PWM en inversores solares y controladores de motores de vehículos eléctricos, y PPM en algunos sistemas de control remoto de radiocontrol y en comunicaciones ópticas de corto alcance.

**Historia relevante:** Alec Reeves patentó PCM en 1937, pero su implementación práctica requería primero dominar PAM. Durante la Segunda Guerra Mundial, sistemas PAM-TDM secretos permitieron múltiples conversaciones telefónicas encriptadas en un solo canal de radio, precediendo la era digital.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Teorema del Muestreo de Nyquist-Shannon (Carta 5)
- Multiplexación por División de Tiempo (TDM)
- Conceptos básicos de pulsos y trenes de pulsos
- Ancho de banda y eficiencia espectral

#### Desarrollo Paso a Paso

**Paso 1: Fundamento Común - El Tren de Pulsos**

Todos estos esquemas comienzan con un tren de pulsos periódicos con período $T_s$ (período de muestreo):

$$p(t) = \sum_{n=-\infty}^{\infty} \Pi\left(\frac{t - nT_s}{\tau}\right)$$

donde $\Pi(t/\tau)$ es un pulso rectangular de ancho $\tau$ y $T_s = 1/f_s$ con $f_s \geq 2f_m$ (Nyquist).

**Paso 2: PAM - Modulación en Amplitud**

En PAM, la amplitud de cada pulso es proporcional al valor instantáneo de la señal moduladora:

$$s_{PAM}(t) = \sum_{n=-\infty}^{\infty} m(nT_s) \cdot \Pi\left(\frac{t - nT_s}{\tau}\right)$$

La señal PAM natural preserva la forma de $m(t)$ dentro de cada pulso:
$$s_{PAM-natural}(t) = m(t) \cdot p(t)$$

PAM instantánea (sample-and-hold) mantiene amplitud constante durante el pulso:
$$s_{PAM-flat}(t) = \sum_{n=-\infty}^{\infty} m(nT_s) \cdot \Pi\left(\frac{t - nT_s}{\tau}\right)$$

**Paso 3: PWM - Modulación en Ancho de Pulso**

En PWM, el ancho del pulso varía proporcionalmente a $m(t)$ mientras la amplitud permanece constante:

$$\tau(t) = \tau_0[1 + k_{PWM} \cdot m(t)]$$

donde $\tau_0$ es el ancho nominal y $k_{PWM}$ es el índice de modulación PWM.

La señal PWM se puede expresar como:
$$s_{PWM}(t) = A \sum_{n=-\infty}^{\infty} \Pi\left(\frac{t - nT_s}{\tau(nT_s)}\right)$$

**Paso 4: PPM - Modulación en Posición**

En PPM, la posición temporal del pulso dentro de su ventana temporal varía con $m(t)$:

$$\Delta t(n) = k_{PPM} \cdot m(nT_s)$$

donde $\Delta t(n)$ es el desplazamiento desde la posición nominal.

La señal PPM:
$$s_{PPM}(t) = A \sum_{n=-\infty}^{\infty} \Pi\left(\frac{t - nT_s - \Delta t(n)}{\tau}\right)$$

#### Análisis Espectral Comparativo

**PAM**: El espectro contiene la señal original más réplicas en múltiplos de $f_s$:
$$S_{PAM}(f) = \frac{\tau}{T_s} M(f) \cdot \text{sinc}(\pi f \tau) + \text{componentes en } kf_s$$

**PWM/PPM**: Espectros más complejos con componentes armónicas significativas que requieren mayor ancho de banda pero ofrecen amplitud constante.

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina tres formas de transmitir la temperatura del agua en una serie de señales de humo:

- **PAM**: Cambias el tamaño de la bocanada de humo - más grande = más caliente
- **PWM**: Mantienes el tamaño igual pero cambias cuánto tiempo dura cada señal
- **PPM**: Todas las señales son iguales pero cambias cuándo aparecen respecto a un reloj de referencia

**Intuición física:**
PAM es intuitiva pero vulnerable - cualquier atenuación afecta directamente la información. PWM y PPM codifican información en el dominio temporal, más robusto ante cambios de amplitud. Es como la diferencia entre transmitir información por el volumen de tu voz (PAM) versus el ritmo de tus palabras (PWM) o los silencios entre ellas (PPM).

**Visualización:**
Imagina un osciloscopio mostrando tres señales con la misma información:
- PAM: pulsos de altura variable en intervalos regulares
- PWM: pulsos de misma altura pero anchos variables
- PPM: pulsos idénticos pero en diferentes posiciones temporales

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Sistema PAM para Voz

**Situación:** Diseñar un sistema PAM para transmitir voz telefónica

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Frecuencia máxima voz | 3.4 | kHz |
| Frecuencia de muestreo | 8 | kHz |
| Ciclo de trabajo | 10 | % |

**Solución paso a paso:**

1. **Período de muestreo:**
   $$T_s = \frac{1}{f_s} = \frac{1}{8000} = 125 \text{ μs}$$

2. **Ancho del pulso PAM:**
   $$\tau = 0.1 \times T_s = 12.5 \text{ μs}$$

3. **Ancho de banda mínimo (primer nulo):**
   $$BW_{min} = \frac{1}{\tau} = \frac{1}{12.5 \times 10^{-6}} = 80 \text{ kHz}$$

**Interpretación:** Aunque la señal original ocupa solo 3.4 kHz, el sistema PAM requiere al menos 80 kHz de ancho de banda debido a los pulsos estrechos.

---

#### Ejemplo 2: Control PWM de LED

**Contexto:** Sistema de iluminación LED regulable usando PWM a 1 kHz

Para controlar el brillo percibido de un LED desde 0% hasta 100%:

- Frecuencia PWM: 1 kHz (período = 1 ms)
- Brillo 25%: pulso activo 0.25 ms, inactivo 0.75 ms
- Brillo 75%: pulso activo 0.75 ms, inactivo 0.25 ms

La frecuencia de 1 kHz es suficientemente alta para que el ojo humano no perciba parpadeo (límite ~100 Hz), integrando la potencia promedio:

$$P_{promedio} = P_{max} \times \text{Ciclo de trabajo}$$

---

#### Ejemplo 3: Sistema PPM de Telemetría

**¿Qué pasa cuando...?**

Si tenemos un sistema PPM con:
- Período de frame: 20 ms
- Desplazamiento máximo: ±5 ms
- Pulso de ancho: 0.5 ms

**Casos límite:**
- Si $m(t) = +1$: pulso aparece 5 ms después de la referencia
- Si $m(t) = 0$: pulso en posición nominal (10 ms)
- Si $m(t) = -1$: pulso aparece 5 ms antes (a los 5 ms)

**Ventaja clave:** La información está en el timing, no en la amplitud. Un pulso atenuado al 50% sigue transmitiendo la misma información si su posición es detectada correctamente.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **PCM** (Carta 23): PAM es el primer paso antes de cuantificación
- **TDM** (Carta 26): Todos estos esquemas permiten multiplexación temporal
- **Teorema de Muestreo** (Carta 5): Fundamento teórico para todos
- **Modulaciones digitales** (Unidad 6): Evolución natural de estos conceptos

#### Dependencias (lo que necesitas saber primero)
1. Muestreo y teorema de Nyquist → Determina la tasa de pulsos
2. Análisis de Fourier → Para entender espectros de pulsos
3. Sistemas lineales → Para análisis de reconstrucción

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Conversión A/D**: PAM es etapa intermedia en todo ADC
2. **Electrónica de potencia**: PWM domina en inversores y fuentes switching
3. **Comunicaciones digitales**: Base conceptual para ASK, FSK, PSK

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La diferencia fundamental entre modular amplitud vs. tiempo
- Por qué PWM/PPM son más robustas al ruido que PAM
- Cómo calcular anchos de banda requeridos para cada tipo
- La relación entre ciclo de trabajo y eficiencia espectral

#### Tipos de problemas típicos
1. **Diseño de sistema PAM-TDM**: Dados N canales, calcular tasas y anchos de banda
   - Estrategia: Aplicar Nyquist, considerar guard time entre pulsos

2. **Comparación de inmunidad al ruido**: Analizar BER para cada tipo
   - Estrategia: Considerar qué parámetro lleva la información

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir PAM natural con PAM flat-top**
- Por qué ocurre: Ambas se llaman PAM pero tienen espectros diferentes
- Cómo evitarlo: PAM natural mantiene forma de m(t), flat-top es rectangular
- Ejemplo: PAM flat-top introduce distorsión de apertura que requiere ecualización

❌ **Error #2: Asumir que PWM no requiere más ancho de banda**
- Por qué ocurre: La amplitud es constante, pero los flancos variables generan armónicos
- Cómo evitarlo: Recordar que PWM genera espectro complejo con múltiples armónicos

❌ **Error #3: Ignorar requisitos de sincronización en PPM**
- Distinción importante: PPM requiere sincronización mucho más precisa que PAM o PWM

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
PAM: s(t) = Σ m(nTs)·p(t-nTs)
PWM: τ(t) = τ₀[1 + k·m(t)]
PPM: Δt = k·m(nTs)
Ancho de banda pulsos: BW ≈ 1/τ
```

#### Conceptos Fundamentales
- ✓ **PAM**: Simple pero vulnerable al ruido, base de PCM
- ✓ **PWM**: Robusta, ideal para control de potencia
- ✓ **PPM**: Máxima robustez, máxima complejidad de sincronización
- ✓ **Trade-off universal**: Simplicidad vs. Robustez vs. Ancho de banda

#### Reglas Mnemotécnicas
- 🧠 **A-W-P**: Amplitud-Width-Position (orden de complejidad creciente)
- 🧠 **Robustez**: PAM < PWM < PPM (información temporal > amplitud)

#### Valores Típicos (para referencias rápidas)

| Parámetro | Valor Típico | Aplicación |
|-----------|--------------|------------|
| fs telefonía | 8 kHz | PAM en PCM |
| PWM motores | 1-20 kHz | Control industrial |
| PWM audio | >40 kHz | Amplificadores Clase D |
| PPM RC | 50 Hz (20ms) | Radiocontrol |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**: Haykin Cap. 4.1-4.3, Lathi Cap. 6.1
- **Simulaciones**: GNU Radio Companion - bloques PAM/PWM
- **Hardware**: Arduino para experimentar con PWM real

#### Temas Relacionados para Explorar
1. Modulación delta y sus variantes
2. Sigma-delta modulation (evolución moderna de PWM)
3. Clase D amplifiers (aplicación de PWM en audio)

#### Preguntas para Reflexionar
- ¿Por qué PWM domina en electrónica de potencia pero no en comunicaciones?
- ¿Cómo afecta el jitter (variación temporal) a cada tipo de modulación?
- ¿Podría diseñarse un sistema híbrido PAM-PWM? ¿Qué ventajas tendría?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 25 minutos
**Prerequisitos críticos**: Teorema de muestreo, análisis de Fourier
**Tags**: `#modulacion-pulsos` `#PAM` `#PWM` `#PPM` `#TDM`

---

*Generado el: 2024-11-16*
*Última revisión: 2024-11-16*