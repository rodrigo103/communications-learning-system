# Carta 19: Discriminador de Frecuencia para Demodular FM

> **Unidad 4**: Modulación Exponencial

---

## 🎯 Pregunta

Explique el funcionamiento del discriminador de frecuencia para demodular FM.

---

## 📝 Respuesta Breve (de la carta original)

El **discriminador de frecuencia** convierte variaciones de frecuencia en variaciones de amplitud para recuperar la moduladora.

**Principio**:
1. Circuito resonante con respuesta lineal en rango de $f_c ± \Delta f$
2. Convierte desviaciones de frecuencia en cambios de amplitud
3. Detector de envolvente extrae la señal moduladora

**Tipos principales**:
- **Discriminador Foster-Seeley**: usa transformador sintonizado
- **Detector de relación (ratio detector)**: más estable ante variaciones de amplitud
- **PLL (Phase-Locked Loop)**: moderno, más lineal y preciso

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El **discriminador de frecuencia** es el corazón de cualquier receptor FM, encargado de la tarea crítica de convertir las variaciones de frecuencia de la señal modulada de vuelta a la señal de audio original. Esta función es fundamental en todos los sistemas FM, desde tu radio del automóvil hasta los sistemas de comunicación de emergencia.

**¿Por qué es importante este concepto?** Sin un discriminador eficiente, sería imposible disfrutar de la alta fidelidad que caracteriza a la radio FM comercial. Es el componente que hace posible la demodulación FM, permitiendo extraer música y voz con calidad superior a la que ofrece AM. En la cadena de recepción FM, el discriminador es tan crítico como el modulador en el transmisor.

**¿Dónde se aplica?** Los discriminadores de frecuencia están presentes en cada receptor FM del planeta: radios de automóviles (sintonizando las estaciones de 88-108 MHz), teléfonos inalámbricos antiguos, walkie-talkies, receptores de TV analógica (para el audio), sistemas de telemetría, y enlaces de microondas. Incluso en sistemas modernos digitales, variantes del concepto se utilizan en FSK y GMSK.

**Historia relevante:** El discriminador Foster-Seeley fue desarrollado por Dudley E. Foster y Stuart William Seeley en 1936 en los laboratorios RCA. Su invención fue crucial para hacer práctica la recepción FM de alta calidad, complementando el trabajo pionero de Edwin Armstrong en modulación FM.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- **Modulación FM básica** (Carta 16): comprensión de cómo la información se codifica en variaciones de frecuencia
- **Circuitos resonantes LC**: comportamiento de impedancia vs. frecuencia
- **Detección de envolvente**: extracción de la amplitud de una señal modulada
- **Respuesta en frecuencia de filtros**: características de fase y amplitud

#### Desarrollo Paso a Paso

**Paso 1: El problema fundamental de la demodulación FM**

En FM, la información está codificada en las variaciones de frecuencia instantánea:
$$f_i(t) = f_c + k_f m(t)$$

El receptor recibe:
$$s_{FM}(t) = A_c \cos\left[2\pi f_c t + 2\pi k_f \int m(t) dt\right]$$

El desafío es recuperar $m(t)$ a partir de las variaciones de frecuencia. Como los detectores convencionales responden a amplitud, necesitamos convertir las variaciones de frecuencia en variaciones de amplitud proporcionales.

**Paso 2: Principio de conversión F-A (Frecuencia a Amplitud)**

La idea clave es usar un circuito cuya respuesta en amplitud varíe linealmente con la frecuencia en el rango de operación. Si pasamos la señal FM por un circuito con función de transferencia:

$$H(f) = K(f - f_0)$$

para frecuencias cercanas a $f_c$, entonces:
- Cuando $f = f_c$: salida nominal
- Cuando $f = f_c + \Delta f$: salida aumenta proporcionalmente
- Cuando $f = f_c - \Delta f$: salida disminuye proporcionalmente

**Paso 3: Implementación práctica con circuitos resonantes**

Un circuito LC paralelo tiene una respuesta en frecuencia que, en las "faldas" de su curva de resonancia, es aproximadamente lineal:

$$|Z(f)| \approx Z_0 \left[1 + 2Q\frac{f - f_r}{f_r}\right]$$

donde $Q$ es el factor de calidad y $f_r$ es la frecuencia de resonancia.

#### Derivación Matemática

**Análisis del discriminador ideal:**

Partiendo de la señal FM de entrada:
$$v_{in}(t) = A_c \cos[\phi(t)]$$
donde $\phi(t) = 2\pi f_c t + 2\pi k_f \int m(t) dt$

La frecuencia instantánea es:
$$f_i(t) = \frac{1}{2\pi}\frac{d\phi(t)}{dt} = f_c + k_f m(t)$$

**Respuesta del discriminador:**

Si el discriminador tiene pendiente $K_d$ (V/Hz):
$$v_{out}(t) = K_d[f_i(t) - f_c] = K_d k_f m(t)$$

**Función de transferencia completa:**
$$\boxed{v_{out}(t) = K_{dem} \cdot m(t)}$$

donde $K_{dem} = K_d k_f$ es la constante de demodulación total.

**Significado físico de cada término:**
- $K_d$ [V/Hz]: sensibilidad del discriminador, determina cuántos voltios de salida por Hz de desviación
- $k_f$ [Hz/V]: sensibilidad del modulador original
- $K_{dem}$ [adimensional]: ganancia total del proceso demodulación

### 🔬 Intuición y Analogías

**Analogía principal:**
Imagina un tobogán con pendiente variable. La señal FM es como una pelota rodando por este tobogán. La altura representa la amplitud de salida, y la posición horizontal representa la frecuencia. Cuando la pelota se mueve hacia frecuencias más altas (derecha), sube por la pendiente y la amplitud aumenta. Cuando va hacia frecuencias más bajas (izquierda), baja y la amplitud disminuye. La pendiente del tobogán es la característica de conversión F-A del discriminador.

**Intuición física:**
El discriminador es esencialmente un "medidor de velocidad" para las oscilaciones. Así como un velocímetro de automóvil convierte la rapidez de rotación de las ruedas en una lectura de aguja (velocidad → posición angular), el discriminador convierte la "velocidad" de oscilación (frecuencia) en un voltaje de salida.

**Visualización:**
Imagina la curva de respuesta del discriminador como una rampa en el dominio de la frecuencia. La señal FM "camina" horizontalmente por esta rampa, y su posición vertical (amplitud de salida) sigue las variaciones de frecuencia.

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Radio FM comercial con discriminador Foster-Seeley

**Situación:** Diseñar un discriminador para un receptor de FM broadcast.

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Frecuencia central | 100 | MHz |
| Desviación máxima | ±75 | kHz |
| Frecuencia de audio máxima | 15 | kHz |
| Sensibilidad deseada | 10 | mV/kHz |

**Solución paso a paso:**

1. **Ancho de banda del discriminador:**
   $$BW_{disc} = 2\Delta f_{max} = 2 \times 75 = 150 \text{ kHz}$$

2. **Factor Q del transformador:**
   $$Q = \frac{f_c}{BW} = \frac{100 \times 10^6}{150 \times 10^3} = 667$$

3. **Voltaje de salida máximo:**
   $$V_{out,max} = K_d \times \Delta f_{max} = 10 \times 75 = 750 \text{ mV}$$

4. **Resultado:**
   $$\boxed{V_{out} = 750 \text{ mV pico para modulación 100\%}}$$

**Interpretación:** El discriminador produce ±750 mV de salida para la máxima desviación de frecuencia, perfectamente adecuado para alimentar las etapas de audio del receptor.

---

#### Ejemplo 2: Sistema PLL moderno para FM

**Contexto:** Receptor FM digital usando PLL como discriminador en un chip de radio SDR.

Un PLL (Phase-Locked Loop) actúa como discriminador de frecuencia cuando su voltaje de control del VCO se usa como salida demodulada.

**Parámetros típicos:**
- Frecuencia de referencia: 10.7 MHz (FI estándar)
- Rango de captura: ±100 kHz
- Ganancia del VCO: $K_{VCO} = 50$ kHz/V
- Voltaje de control: 0-3.3V

**Análisis:**
La salida del filtro del PLL es directamente proporcional a la desviación de frecuencia:
$$V_{control} = \frac{\Delta f}{K_{VCO}} = \frac{75 \text{ kHz}}{50 \text{ kHz/V}} = 1.5 \text{ V}$$

El PLL mantiene linealidad excelente en todo el rango, con distorsión típica < 0.1%.

---

#### Ejemplo 3: Detector de relación vs. Foster-Seeley

**¿Qué pasa cuando hay variaciones de amplitud indeseadas?**

**Foster-Seeley estándar:**
- Si la amplitud de entrada varía 20%, la salida demodulada también varía
- Requiere limitador previo para funcionar correctamente
- THD típica: 1-2% sin limitador

**Detector de relación (ratio detector):**
- Automáticamente rechaza variaciones de amplitud
- Usa capacitor grande para estabilizar la amplitud total
- No requiere limitador (ventaja en receptores económicos)
- THD típica: 0.5-1% incluso con AM residual

**Caso especial - Multitrayecto:**
Cuando hay reflexiones (ghosting):
- Foster-Seeley: distorsión severa por las variaciones de amplitud
- Ratio detector: mantiene calidad aceptable
- PLL: mejor desempeño, puede "seguir" la señal dominante

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Modulación FM** (Carta 16): El discriminador realiza la operación inversa del modulador FM
- **Índice de modulación β** (Carta 17): Determina el rango de frecuencias que el discriminador debe manejar
- **Preénfasis/Deénfasis** (Carta 20): El discriminador precede a la red de deénfasis en la cadena
- **Receptor superheterodino** (Carta 12): El discriminador opera sobre la señal en FI (10.7 MHz típicamente)

#### Dependencias (lo que necesitas saber primero)
1. Respuesta en frecuencia de circuitos RLC → Para entender la conversión F-A
2. Detección de envolvente → Para extraer la señal después de la conversión
3. Teoría de realimentación → Para comprender el funcionamiento del PLL

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Demodulación FSK**: Versión digital del mismo principio
2. **Síntesis de frecuencia**: PLLs como discriminadores y sintetizadores
3. **Medición de frecuencia**: Discriminadores como frecuencímetros analógicos

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La conversión frecuencia-amplitud es la clave de la demodulación FM
- Diferentes implementaciones (Foster-Seeley, ratio, PLL) tienen distintos trade-offs
- La linealidad del discriminador determina la distorsión de la señal demodulada
- La importancia del limitador en algunos diseños pero no en otros

#### Tipos de problemas típicos
1. **Cálculo de sensibilidad**: Dado un discriminador con cierta pendiente, calcular voltaje de salida
   - Estrategia: Aplicar directamente $V_{out} = K_d \times \Delta f$

2. **Diseño de parámetros**: Especificar Q del circuito resonante para cubrir el rango de desviación
   - Estrategia: Relacionar ancho de banda con factor Q y frecuencia central

3. **Análisis de distorsión**: Evaluar no-linealidades en la característica del discriminador
   - Estrategia: Expansión en serie de Taylor, calcular armónicos

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir discriminador de frecuencia con detector de fase**
- Por qué ocurre: Ambos están relacionados (frecuencia es derivada de fase)
- Cómo evitarlo: Recordar que discriminador responde a $df/dt$, no a fase absoluta
- Ejemplo de error: Usar detector de fase directamente para FM (funcionaría para PM)

❌ **Error #2: Ignorar el rango lineal del discriminador**
- Por qué ocurre: Asumir respuesta lineal infinita
- Cómo evitarlo: Verificar que $\Delta f_{max}$ esté dentro del rango lineal
- Consecuencia: Distorsión severa si se excede el rango

❌ **Error #3: Olvidar el limitador en Foster-Seeley**
- Por qué ocurre: No considerar variaciones de amplitud de entrada
- Cómo evitarlo: Siempre incluir etapa limitadora antes del discriminador
- Excepción: Ratio detector no lo necesita (diseño auto-limitante)

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Salida del discriminador: v_out = K_d × Δf
Sensibilidad total: K_dem = K_d × k_f
Rango lineal necesario: ±Δf_max
```

#### Conceptos Fundamentales
- ✓ **Conversión F-A**: El discriminador convierte frecuencia en amplitud linealmente
- ✓ **Tres tipos principales**: Foster-Seeley (simple), Ratio (inmune a AM), PLL (preciso)
- ✓ **Linealidad crítica**: Determina la fidelidad de la demodulación

#### Reglas Mnemotécnicas
- 🧠 **"FART"**: Frecuencia → Amplitud → Rectificación → Tono (audio)
- 🧠 **Foster necesita Limitador, Ratio Rechaza AM, PLL es Preciso**

#### Valores Típicos (para referencias rápidas)

| Parámetro | Valor Típico | Aplicación |
|-----------|--------------|------------|
| FI estándar FM | 10.7 MHz | Receptores comerciales |
| Sensibilidad típica | 5-20 mV/kHz | Discriminadores prácticos |
| Q del circuito | 100-1000 | Según ancho de banda |
| THD con buen diseño | < 0.5% | Alta fidelidad |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - "Communication Systems" de Haykin, Cap. 4.7-4.8 (análisis detallado de discriminadores)
  - "Radio-Frequency Electronics" de Hagen (implementaciones prácticas)
- **Datasheets**: MC3361 (receptor FM completo con discriminador de cuadratura)
- **Simulaciones**: LTspice con modelos de transformadores para Foster-Seeley

#### Temas Relacionados para Explorar
1. Discriminadores de cuadratura (otra topología importante)
2. Demodulación digital I/Q moderna
3. Discriminadores en sistemas de radar FM-CW

#### Preguntas para Reflexionar
- ¿Por qué el PLL es superior en ambientes de señal débil?
- ¿Cómo afecta la no-linealidad del discriminador al espectro de audio?
- ¿Podría usarse un discriminador AM modificado para demodular FM?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 45 minutos
**Prerequisitos críticos**: Modulación FM, circuitos resonantes, detección de envolvente
**Tags**: `#FM` `#demodulacion` `#discriminador` `#receptor` `#Foster-Seeley` `#PLL`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*