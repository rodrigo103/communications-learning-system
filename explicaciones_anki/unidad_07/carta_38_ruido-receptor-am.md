# Carta 38: Efecto del Ruido en Receptor AM - El Fenómeno del Umbral

> **Unidad 7**: Ruido en Sistemas de Comunicaciones

---

## 🎯 Pregunta

Explique el efecto del ruido sobre un receptor AM con detección de envolvente.

---

## 📝 Respuesta Breve (de la carta original)

En **AM con detección de envolvente**, señal + ruido:
$$r(t) = [A_c + m(t) + x(t)]\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)$$

**Casos**:

**Alto SNR** (señal >> ruido):
- Envolvente ≈ $A_c + m(t) + x(t)$
- Componente en fase del ruido interfiere
- SNR salida ≈ SNR entrada (detección lineal)

**Bajo SNR** (señal ≪ ruido):
- **Efecto umbral**: degradación súbita
- Ruido domina, envolvente sigue al ruido
- Pérdida completa de señal debajo del umbral
- Umbral típico: SNR ≈ 10 dB

**Conclusión**: AM requiere SNR mínimo para operación útil.

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El análisis del efecto del ruido en receptores AM es fundamental para entender las limitaciones prácticas de este sistema de modulación. A diferencia de los sistemas digitales que pueden operar con SNR bajas usando codificación, AM con detección de envolvente exhibe un comportamiento no lineal dramático conocido como **efecto umbral**, que limita severamente su uso en ambientes ruidosos.

**¿Por qué es importante este concepto?**
- Explica por qué **AM necesita alta potencia** de transmisión
- Justifica la transición histórica de **AM a FM** para radiodifusión de calidad
- Define los **límites de cobertura** de estaciones AM
- Es fundamental para el **diseño de enlaces** con modulación AM

**¿Dónde se aplica?**
- **Radio AM comercial**: 530-1710 kHz, limitada por ruido nocturno
- **Comunicaciones aeronáuticas**: VHF AM (118-137 MHz) por simplicidad
- **Banda ciudadana (CB)**: 27 MHz AM, alcance limitado por ruido
- **Radioaficionados**: Bandas HF con propagación variable
- **Sistemas de emergencia**: Donde la simplicidad es crítica

**Historia:** El efecto umbral en AM fue una de las motivaciones principales para el desarrollo de FM por Edwin Armstrong en los años 1930s, buscando un sistema más robusto ante el ruido.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Modulación AM convencional
- Ruido de banda angosta (componentes I-Q)
- Detección de envolvente
- Relación señal-ruido (SNR)

#### Desarrollo Paso a Paso

**Paso 1: Modelo de señal AM con ruido**

La señal AM en el receptor, después del filtro IF pero antes del detector:
$$s_{AM}(t) = A_c[1 + m(t)]\cos(2\pi f_c t)$$

donde $m(t)$ es la señal moduladora normalizada (|m(t)| ≤ 1).

**Paso 2: Adición del ruido de banda angosta**

El ruido se suma a la señal:
$$r(t) = s_{AM}(t) + n(t)$$

Expandiendo con componentes I-Q del ruido:
$$r(t) = [A_c(1 + m(t)) + x(t)]\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)$$

**Paso 3: Detección de envolvente**

El detector de envolvente extrae:
$$E(t) = \sqrt{[A_c(1 + m(t)) + x(t)]^2 + y^2(t)}$$

#### Derivación Matemática

**Caso 1: SNR Alta (A_c >> σ_n)**

Cuando la portadora es mucho mayor que el ruido, podemos aproximar:

$$E(t) = A_c\sqrt{\left[1 + m(t) + \frac{x(t)}{A_c}\right]^2 + \left[\frac{y(t)}{A_c}\right]^2}$$

Para $|x(t)|, |y(t)| << A_c$, usando aproximación de Taylor:

$$E(t) \approx A_c\left[1 + m(t) + \frac{x(t)}{A_c}\right]\sqrt{1 + \frac{y^2(t)}{[A_c(1+m(t))+x(t)]^2}}$$

$$E(t) \approx A_c\left[1 + m(t) + \frac{x(t)}{A_c}\right]$$

**Salida del detector (quitando DC):**
$$\boxed{y_D(t) = A_c m(t) + x(t)}$$

**SNR de salida:**
$$SNR_{out} = \frac{A_c^2\overline{m^2(t)}}{\sigma_x^2} = \frac{A_c^2\overline{m^2(t)}}{\sigma_n^2}$$

**Caso 2: SNR Baja (A_c << σ_n)**

El ruido domina completamente:

$$E(t) \approx \sqrt{x^2(t) + y^2(t)} = R_n(t)$$

La envolvente sigue una distribución de Rayleigh del ruido, independiente de la señal:

$$\boxed{y_D(t) \approx R_n(t) - E[R_n]}$$

La señal está completamente perdida - **supresión de la modulación**.

**Caso 3: SNR Intermedia - Efecto Umbral**

En la región de transición ($A_c \approx \sigma_n$):
- La envolvente sigue una **distribución de Rice**
- Aparecen "clicks" de ruido cuando $R_n(t)$ momentáneamente excede $A_c$
- Degradación rápida y no lineal del rendimiento

### 🔬 Intuición y Analogías

**Analogía del faro en la niebla:**

Imagina un faro (portadora AM) enviando destellos de información (modulación) a través de niebla densa (ruido):

- **Niebla ligera** (SNR alta): Los destellos son claramente visibles, la niebla solo los atenúa ligeramente
- **Niebla densa** (SNR baja): No puedes ver el faro en absoluto, solo ves fluctuaciones aleatorias de la niebla
- **Niebla intermedia** (umbral): A veces ves el faro, a veces se pierde completamente - muy confuso

**Intuición física del umbral:**

El detector de envolvente "sigue" al vector más fuerte:
- Si portadora > ruido: sigue a la señal (con algo de perturbación)
- Si ruido > portadora: sigue al ruido (señal perdida)
- En el umbral: "batalla" entre señal y ruido, causando distorsión severa

**Visualización vectorial:**

```
SNR Alta:          SNR Baja:
    ↑                 ↗↖↙
    │Ac               ↘n↗
    │                 ↙↖
────┼──→           ───┼───→
    │x                │
Señal domina     Ruido domina
```

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Análisis Cuantitativo de Radio AM Comercial

**Situación:** Estación AM transmitiendo música en 1000 kHz

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Potencia portadora recibida | -60 | dBm |
| Índice de modulación | 0.8 | - |
| Ancho de banda audio | 5 | kHz |
| Densidad de ruido | -174 | dBm/Hz |
| Ancho de banda IF | 10 | kHz |

**Análisis paso a paso:**

1. **Calcular potencia de ruido:**
   $$N = -174 + 10\log(10000) = -174 + 40 = -134 \text{ dBm}$$

2. **SNR de entrada (portadora a ruido):**
   $$SNR_{in} = -60 - (-134) = 74 \text{ dB}$$

3. **Potencia de señal moduladora:**
   $$P_m = P_c \cdot \frac{m^2}{2} = -60 + 10\log(0.32) = -65 \text{ dBm}$$

4. **SNR de salida (audio):**
   Para detección de envolvente con m = 0.8:
   $$SNR_{out} = SNR_{in} \cdot \frac{m^2}{2+m^2} = 74 + 10\log\left(\frac{0.64}{2.64}\right)$$
   $$SNR_{out} = 74 - 6.2 = 67.8 \text{ dB}$$

**Interpretación:** Excelente calidad de audio, muy por encima del umbral (~10 dB).

---

#### Ejemplo 2: Determinación del Alcance Máximo con Efecto Umbral

**Contexto:** Transmisor AM de 1 kW para comunicaciones de emergencia

**Parámetros del sistema:**
- Frecuencia: 3.5 MHz (banda de 80m)
- Potencia transmitida: 1 kW (60 dBm)
- Ganancia antena TX: 0 dBi
- Ganancia antena RX: 0 dBi
- Umbral SNR requerido: 15 dB (para inteligibilidad)
- Índice de modulación: 1.0 (100%)
- BW audio: 3 kHz

**Cálculo de alcance:**

1. **Potencia de ruido en receptor:**
   $$N = kTB = -174 + 10\log(6000) = -136.2 \text{ dBm}$$

2. **Potencia mínima de portadora (15 dB sobre ruido):**
   $$P_{c,min} = -136.2 + 15 = -121.2 \text{ dBm}$$

3. **Pérdidas de propagación máximas:**
   $$L_{max} = P_{TX} - P_{c,min} = 60 - (-121.2) = 181.2 \text{ dB}$$

4. **Distancia máxima (propagación en espacio libre):**
   $$L = 32.45 + 20\log(f_{MHz}) + 20\log(d_{km})$$
   $$181.2 = 32.45 + 20\log(3.5) + 20\log(d)$$
   $$20\log(d) = 137.9$$
   $$d = 7,900 \text{ km}$$

**Realidad con propagación por onda de superficie:**
- Día: ~200 km (pérdidas adicionales del suelo)
- Noche: ~2000 km (propagación ionosférica)

---

#### Ejemplo 3: Comparación de Rendimiento cerca del Umbral

**¿Qué pasa cuando operamos cerca del umbral?**

**Escenario:** Receptor móvil acercándose al límite de cobertura

| Distancia | SNR (dB) | Calidad de Audio | Fenómenos Observados |
|-----------|----------|------------------|----------------------|
| Cerca | 30 | Excelente | Audio limpio, sin distorsión |
| Media | 20 | Buena | Ligero ruido de fondo |
| Límite | 15 | Aceptable | Ruido notable, pero inteligible |
| **Umbral** | **10** | **Marginal** | **Aparecen "clicks" de ruido** |
| Bajo umbral | 5 | Inutilizable | Modulación suprimida, solo ruido |
| Muy bajo | 0 | Perdida | Señal completamente en el ruido |

**Demostración matemática del umbral:**

Para SNR = 10 dB (factor 10):
- $A_c/\sigma_n = \sqrt{10} = 3.16$
- Probabilidad de que $R_n > A_c$:
  $$P(R_n > A_c) = \exp\left(-\frac{A_c^2}{2\sigma_n^2}\right) = \exp(-5) = 0.0067$$

Esto significa ~0.7% del tiempo el ruido "gana", causando clicks audibles.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Ruido de banda angosta** (Carta 37): Modelo base para el análisis
- **Efecto umbral en FM** (Carta 39): Comparación con otro sistema
- **Índice de modulación**: Afecta directamente la SNR de salida
- **Detector síncrono**: Alternativa sin efecto umbral

#### Dependencias (lo que necesitas saber primero)
1. Detección de envolvente no lineal
2. Distribuciones de Rayleigh y Rice
3. Componentes I-Q del ruido
4. Concepto de SNR en banda base

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Diseño de enlaces AM**: Cálculo de coberturas
2. **Comparación AM vs FM**: Justificación de FM para broadcast
3. **Sistemas de respaldo**: Donde AM es suficiente

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- El efecto umbral es **no lineal** y súbito
- Solo la componente **en fase** del ruido afecta en SNR alta
- Por debajo del umbral hay **supresión de modulación**
- El umbral típico está en **10 dB de SNR**
- AM DSB-SC con detección síncrona **no tiene** efecto umbral

#### Tipos de problemas típicos
1. **Cálculo de SNR de salida**: Dado SNR entrada y m, hallar SNR audio
   - Estrategia: $SNR_{out} = SNR_{in} \times m^2/(2+m^2)$ para envolvente

2. **Determinación del umbral**: Calcular SNR mínima para operación
   - Estrategia: Típicamente 10-12 dB, depende del criterio

3. **Comparación de detectores**: Envolvente vs síncrono con ruido
   - Estrategia: Síncrono no tiene umbral pero es más complejo

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Asumir que todo el ruido afecta igual**
- Por qué ocurre: Simplificación excesiva
- Cómo evitarlo: En SNR alta, solo x(t) importa, no y(t)
- Recordar: Detección de envolvente es no lineal

❌ **Error #2: Confundir SNR de portadora con SNR de audio**
- Por qué ocurre: Diferentes definiciones de SNR
- Cómo evitarlo: SNR_audio < SNR_portadora por factor m²/(2+m²)
- Verificación: SNR_out siempre menor que SNR_in

❌ **Error #3: Ignorar el efecto umbral en diseño**
- Por qué ocurre: Análisis solo para SNR alta
- Cómo evitarlo: Siempre verificar operación sobre umbral
- Consecuencia: Sistema inútil si cae bajo umbral

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
SNR_out = SNR_in × m²/(2+m²)           [Detección envolvente]
Umbral ≈ 10 dB SNR                     [Valor típico]
y(t) = Ac·m(t) + x(t)                  [Salida en SNR alta]
P(clicks) = exp(-SNR/2)                [Probabilidad de umbral]
```

#### Conceptos Fundamentales
- ✓ **Efecto umbral**: Degradación súbita en SNR ≈ 10 dB
- ✓ **Solo fase importa**: En SNR alta, solo x(t) afecta
- ✓ **Supresión total**: Bajo umbral, señal perdida
- ✓ **No linealidad**: Causa del comportamiento umbral

#### Reglas Mnemotécnicas
- 🧠 **"10 dB to Breathe"**: Necesitas 10 dB SNR mínimo para AM
- 🧠 **"Phase matters Most"**: En SNR alta, fase del ruido domina
- 🧠 **"Below threshold = Below useful"**: No hay recuperación gradual

#### Comparación de Detectores AM

| Detector | Umbral | Complejidad | SNR out/in | Uso típico |
|----------|--------|-------------|------------|------------|
| Envolvente | 10 dB | Muy simple | < 1 | Broadcast |
| Síncrono | No tiene | Complejo | ≈ 1 | Profesional |
| Cuadrado | 13 dB | Simple | < 1 | Histórico |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - Carlson, "Communication Systems", Cap. 9.3
  - Haykin, "Communication Systems", Cap. 3.8
  - Couch, "Digital and Analog Communication", Cap. 7
- **Material del curso**: Laboratorio de detección AM con ruido
- **Simulaciones**: GNU Radio para experimentar con umbrales

#### Temas Relacionados para Explorar
1. Detección síncrona y su inmunidad al umbral
2. Distribución de Rice en la región de transición
3. AM estéreo y su susceptibilidad al ruido
4. Técnicas de reducción de ruido en AM

#### Preguntas para Reflexionar
- ¿Por qué la aviación sigue usando AM a pesar del umbral?
- ¿Cómo afecta el desvanecimiento selectivo al efecto umbral?
- ¿Se puede diseñar un detector que mitigue el efecto umbral?
- ¿Qué pasa con SSB-SC en lugar de AM convencional?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 30 minutos
**Prerequisitos críticos**: Detección AM, ruido banda angosta, SNR
**Tags**: `#AM` `#ruido` `#efecto-umbral` `#deteccion-envolvente` `#SNR`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*