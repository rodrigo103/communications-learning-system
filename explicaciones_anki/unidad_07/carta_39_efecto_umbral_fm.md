# Carta 39: Efecto Umbral en FM

> **Unidad 7**: Ruido en Sistemas de Comunicaciones

---

## 🎯 Pregunta

¿Qué es el efecto umbral en FM y cómo se manifiesta?

---

## 📝 Respuesta Breve (de la carta original)

El **efecto umbral en FM** es una degradación súbita del desempeño cuando SNR cae por debajo de un valor crítico.

**Manifestación**:
- **Sobre umbral**: FM mejora SNR (intercambio BW por SNR)
  - SNR salida $\propto \beta^2$ (ventaja de FM)
- **Cerca/bajo umbral**: clicks de ruido
  - Saltos de fase de 2π generan pulsos impulsivos
  - Degradación rápida

**Umbral típico**: SNR entrada ≈ 10 dB (depende de β)

**Soluciones**:
- Aumentar potencia transmitida
- Usar PLL (baja umbral ~3 dB)
- Feedback demodulator
- No operar cerca del umbral en diseño

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El efecto umbral es uno de los fenómenos más importantes en sistemas FM y representa una **limitación fundamental** de este tipo de modulación. Aunque FM ofrece excelente desempeño en presencia de ruido cuando la señal es fuerte, su comportamiento cambia drásticamente cuando la relación señal-ruido cae por debajo de cierto punto crítico.

Este fenómeno es crucial para el diseño de sistemas de comunicaciones FM, incluyendo:
- **Radio FM broadcast** (88-108 MHz): Las estaciones deben transmitir con suficiente potencia para que los receptores operen sobre el umbral
- **Comunicaciones satelitales**: El diseño del enlace debe considerar el umbral para garantizar calidad
- **Telemetría espacial**: Misiones espaciales usan técnicas especiales para operar bajo el umbral
- **Comunicaciones móviles FM**: La potencia y ubicación de antenas se diseña para evitar el umbral

Históricamente, el efecto umbral fue uno de los principales desafíos que enfrentó la tecnología FM en sus inicios. Edwin Armstrong, inventor de la FM, tuvo que demostrar que los beneficios de FM justificaban la necesidad de mayor potencia transmitida para operar sobre el umbral.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos

Para entender el efecto umbral necesitas conocer:
- **FM básica** (Carta 16): Cómo funciona la modulación en frecuencia
- **Índice de modulación β** (Carta 17): Relación entre desviación y frecuencia moduladora
- **Ruido de banda angosta** (Carta 37): Representación del ruido en sistemas paso banda
- **SNR**: Relación señal-ruido y su efecto en la calidad

#### Desarrollo Paso a Paso

**Paso 1: Comportamiento Normal de FM (Sobre el Umbral)**

Cuando la señal FM es fuerte comparada con el ruido (SNR alto), el sistema presenta ventajas extraordinarias:

$$\left(\frac{S}{N}\right)_{salida} = 3\beta^2(\beta+1)\left(\frac{S}{N}\right)_{entrada}$$

Esta relación muestra la **ganancia de SNR de FM**: incrementar el índice de modulación β (usando más ancho de banda) mejora el SNR de salida. Este es el famoso "trade-off" de FM: ancho de banda por SNR.

**Ejemplo**: Con β = 5 (FM broadcast típico):
- Factor de mejora: $3 \times 5^2 \times 6 = 450$ (26.5 dB)
- Si SNR entrada = 20 dB → SNR salida ≈ 46.5 dB (¡excelente!)

**Paso 2: ¿Qué Pasa Cuando SNR Disminuye?**

La fórmula anterior es válida solo cuando la **amplitud de la señal es mayor que la amplitud del ruido**. Cuando esto deja de cumplirse, el comportamiento cambia radicalmente.

**Condición normal**: $A_c >> n(t)$
- La fase de la señal compuesta está dominada por la señal FM
- El ruido agrega pequeñas variaciones que se pueden filtrar

**Cerca del umbral**: $A_c \approx n(t)$
- El ruido empieza a tener influencia significativa en la fase resultante
- Aparecen "clicks" de ruido cuando el fasor de ruido cruza el origen

**Bajo el umbral**: $A_c < n(t)$
- El ruido domina completamente
- La fase salta aleatoriamente 2π (clicks constantes)
- El discriminador de frecuencia detecta estos saltos como pulsosimpulsivos
- **Colapso total** del desempeño

**Paso 3: Análisis Matemático del Umbral**

Cuando la señal FM más ruido se representa como fasor:

$$s(t) + n(t) = A_c\cos(2\pi f_c t + \phi_m(t)) + n_i(t)\cos(2\pi f_c t) - n_q(t)\sin(2\pi f_c t)$$

La fase resultante es:

$$\phi_{total}(t) = \phi_m(t) + \tan^{-1}\left(\frac{-n_q(t)}{A_c + n_i(t)}\right)$$

**Sobre el umbral** ($A_c >> n$):
$$\phi_{total}(t) \approx \phi_m(t) - \frac{n_q(t)}{A_c}$$
- Aproximación lineal válida
- Ruido de cuadratura se suma a la fase
- El discriminador detecta principalmente la modulación

**Bajo el umbral** ($A_c < n$):
- La función $\tan^{-1}$ no se puede linealizar
- Cuando el denominador $A_c + n_i(t)$ cruza cero, la fase salta ±π
- Estos saltos generan pulsos impulsivos en la salida del discriminador

**Paso 4: Ubicación del Umbral**

El umbral ocurre típicamente cuando:

$$\left(\frac{S}{N}\right)_{entrada} \approx 10 \text{ dB}$$

Este valor depende de:
- **Índice de modulación β**: Mayor β → umbral ligeramente más alto
- **Tipo de demodulador**: PLL tiene umbral ~3 dB más bajo que discriminador
- **Ancho de banda del filtro**: Afecta la potencia de ruido

#### Derivación de la Tasa de Clicks

La tasa de clicks (saltos de fase 2π) se puede derivar de la teoría de cruces por cero del ruido de Rice:

$$\lambda_{clicks} = \frac{BW}{\pi}\exp\left(-\frac{A_c^2}{2\sigma_n^2}\right) = \frac{BW}{\pi}\exp(-SNR)$$

donde:
- $BW$ = ancho de banda del filtro
- $A_c$ = amplitud de portadora
- $\sigma_n^2$ = potencia de ruido

**Interpretación**:
- Sobre el umbral (SNR alto): $\lambda_{clicks} \approx 0$ (exponencial es muy pequeña)
- En el umbral (SNR ≈ 1): Los clicks empiezan a ser frecuentes
- Bajo el umbral (SNR < 1): $\lambda_{clicks}$ aumenta exponencialmente

### 🔬 Intuición y Analogías

**Analogía principal: El Surfista y las Olas**

Imagina un surfista (la señal FM) montando una ola (la portadora). Pequeñas perturbaciones del agua (ruido bajo) solo hacen que el surfista se tambalee un poco, pero mantiene su dirección.

- **Sobre el umbral**: El surfista es hábil y pesado, las pequeñas olas no lo afectan mucho
- **En el umbral**: Las olas se vuelven tan grandes que ocasionalmente tumban al surfista
- **Bajo el umbral**: Las olas son tan grandes que el surfista es lanzado constantemente en todas direcciones

Cada vez que el surfista cae y gira 360°, es como un "click" de fase en FM: un evento discontinuo que crea un pulso impulsivo de ruido.

**Intuición física del efecto:**

El discriminador de FM detecta cambios de frecuencia, es decir, **la derivada de la fase**:

$$f_i(t) = f_c + \frac{1}{2\pi}\frac{d\phi(t)}{dt}$$

Un salto súbito de fase de 2π produce una **función delta** en la derivada:

$$\frac{d}{dt}[2\pi u(t)] = 2\pi\delta(t)$$

donde $u(t)$ es el escalón unitario.

Esto se escucha como un **"click"** o "pop" intenso. Bajo el umbral, estos clicks ocurren frecuentemente y dominan la salida, destruyendo completamente la señal deseada.

**Visualización mental:**

Imagina un diagrama fasorial:
- **Sobre umbral**: Fasor de señal grande, ruido agrega pequeñas variaciones angulares
- **Umbral**: Fasor de señal y ruido comparables, ocasionalmente el ruido "envuelve" el origen
- **Bajo umbral**: Fasor de ruido grande, señal apenas perturba, fase gira aleatoriamente

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Radio FM Broadcast (99.5 MHz)

**Situación**: Estación de radio FM transmitiendo con parámetros típicos

**Datos del sistema**:

| Parámetro | Valor |
|-----------|-------|
| Potencia ERP | 50 kW |
| Frecuencia portadora | 99.5 MHz |
| Desviación máxima | 75 kHz |
| Frecuencia moduladora máx | 15 kHz |
| Índice de modulación β | 75/15 = 5 |
| Ancho de banda (Carson) | 2(75+15) = 180 kHz |

**Cálculo del umbral**:

A una distancia donde la señal recibida tiene SNR = 10 dB en el ancho de banda de FM:

**Sobre el umbral** (SNR entrada = 20 dB):
$$SNR_{salida} = 3\beta^2(\beta+1) \cdot SNR_{entrada}$$
$$= 3 \times 25 \times 6 \times 100 = 45,000 = 46.5 \text{ dB}$$

**En el umbral** (SNR entrada = 10 dB):
- La fórmula empieza a no ser válida
- Aparecen clicks ocasionales
- La calidad de audio se degrada notablemente

**Bajo el umbral** (SNR entrada = 5 dB):
- Clicks constantes
- Audio ininteligible
- Es mejor apagar el receptor

**Conclusión práctica**: La estación debe asegurar que en toda su área de cobertura el SNR > 12-13 dB para operación confiable, dejando margen sobre el umbral.

---

#### Ejemplo 2: Enlace de Telemetría Espacial

**Contexto**: Sonda espacial transmitiendo datos científicos a la Tierra

**Datos**:

| Parámetro | Valor |
|-----------|-------|
| Distancia | 1 millón de km |
| Potencia transmitida | 10 W |
| Frecuencia | 2.3 GHz (banda S) |
| Ancho de banda FM | 100 kHz |
| Temperatura de ruido receptor | 50 K (LNA criogénico) |

**Problema**: A gran distancia, la señal recibida es extremadamente débil

**Cálculo simplificado**:

Pérdida de espacio libre:
$$L_{fs} = 20\log_{10}\left(\frac{4\pi d}{\lambda}\right)$$
$$= 20\log_{10}\left(\frac{4\pi \times 10^9}{0.13}\right) \approx 200 \text{ dB}$$

Si SNR resultante está cerca del umbral:
- **Solución 1**: Aumentar potencia (limitado por paneles solares)
- **Solución 2**: Usar demodulador PLL (baja umbral 3 dB)
- **Solución 3**: Reducir β (menor calidad pero umbral más bajo)
- **Solución 4**: Usar modulación PSK digital en lugar de FM analógica

**Decisión histórica**: Voyager, Pioneer usaban FM para video pero PSK para telemetría crítica

---

#### Ejemplo 3: Comparación Demodulador Convencional vs PLL

**Experimento**: Medir BER o calidad vs SNR de entrada

**Demodulador discriminador convencional**:

| SNR entrada (dB) | Calidad de salida |
|------------------|-------------------|
| 20 dB | Excelente (SNR salida ~47 dB) |
| 15 dB | Muy buena (SNR salida ~42 dB) |
| 12 dB | Buena (SNR salida ~38 dB) |
| **10 dB** | **Umbral: comienzan clicks** |
| 8 dB | Mala (clicks frecuentes) |
| 5 dB | Inutilizable |

**Demodulador PLL** (Phase-Locked Loop):

| SNR entrada (dB) | Calidad de salida |
|------------------|-------------------|
| 20 dB | Excelente |
| 15 dB | Excelente |
| 10 dB | Muy buena |
| **7 dB** | **Umbral: comienzan clicks** |
| 5 dB | Mala |
| 2 dB | Inutilizable |

**Ventaja del PLL**: Reduce el umbral en aproximadamente **3 dB**, lo que se traduce en:
- Mayor alcance (√2 ≈ 1.4x distancia)
- Menor potencia requerida (mitad)
- Mayor confiabilidad en condiciones marginales

**Por qué el PLL es mejor**: El lazo realimentado "ayuda" a seguir la fase incluso con ruido moderado, extendiendo la región lineal.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)

- **Carta 16 - FM vs PM**: Ambas modulaciones exponenciales sufren efecto umbral similar
- **Carta 17 - Índice de modulación**: Mayor β mejora SNR sobre el umbral pero puede elevar ligeramente el umbral mismo
- **Carta 18 - Regla de Carson**: El ancho de banda afecta el SNR de entrada y por tanto la proximidad al umbral
- **Carta 20 - Preénfasis/Deénfasis**: Mejora SNR sobre el umbral pero no cambia la ubicación del umbral
- **Carta 37 - Ruido de banda angosta**: Base teórica para analizar el efecto del ruido en FM
- **Carta 38 - Umbral en AM**: AM también tiene umbral pero menos dramático que FM
- **Carta 45 - Shannon-Hartley**: El colapso bajo el umbral representa operar fuera del régimen donde se puede lograr capacidad del canal

#### Dependencias (lo que necesitas saber primero)

1. **Modulación FM básica**: Entender cómo la información se codifica en frecuencia
2. **Representación fasorial**: Ver señal + ruido como suma vectorial
3. **Discriminador de frecuencia**: Cómo se recupera la información de frecuencia
4. **SNR**: Concepto y medición

#### Aplicaciones Posteriores (dónde usarás esto)

1. **Diseño de enlaces FM**: Calcular presupuesto para operar sobre umbral
2. **Selección de modulación**: Decidir FM vs AM vs digital según SNR disponible
3. **Sistemas de comunicaciones espaciales**: Crucial para misiones de larga distancia
4. **Comparación con sistemas digitales**: Entender por qué digital no tiene umbral tan marcado

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas

1. **Comportamiento no-lineal**: FM no es lineal en todo el rango de SNR
2. **Trade-off fundamental**: Sobre el umbral FM es excelente, bajo el umbral es inútil
3. **Causa física**: Los clicks vienen de saltos de fase cuando ruido domina
4. **Implicación práctica**: Diseño debe garantizar operación sobre el umbral
5. **Comparación AM-FM**: FM mejor en SNR alto, AM más robusto en SNR bajo

#### Tipos de problemas típicos

1. **Calcular ubicación del umbral** para un sistema dado
   - Estrategia: Identificar dónde SNR ≈ 10 dB, considerar β y tipo de demodulador

2. **Diseñar margen sobre el umbral** en un enlace
   - Estrategia: Calcular worst-case SNR, asegurar > 12-13 dB

3. **Comparar desempeño** sobre y bajo umbral
   - Estrategia: Usar fórmula de ganancia FM sobre umbral, describir colapso bajo umbral

4. **Explicar por qué digital reemplazó a FM** en muchas aplicaciones
   - Estrategia: Mencionar umbral súbito de FM vs degradación gradual de digital

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Pensar que la fórmula de ganancia FM es siempre válida**
- **Por qué ocurre**: La ecuación $SNR_{out} = 3\beta^2(\beta+1) \cdot SNR_{in}$ aparece en todos los textos
- **Realidad**: Solo es válida sobre el umbral (típicamente SNR > 10 dB)
- **Cómo evitarlo**: Siempre verificar que estás en la región lineal antes de aplicar fórmulas

❌ **Error #2: Confundir el umbral de FM con el umbral de detección de AM**
- **Diferencia clave**:
  - FM: Colapso súbito y dramático debido a saltos de fase
  - AM con detector de envolvente: Degradación gradual, el ruido simplemente se suma
- **El umbral de FM es mucho más pronunciado**

❌ **Error #3: Pensar que aumentar β siempre mejora el desempeño**
- **Por qué ocurre**: Sobre el umbral, mayor β da mejor SNR
- **Trampa**: Mayor β también requiere mayor ancho de banda, lo que aumenta la potencia de ruido
- **Resultado**: Puede acercar al umbral si la potencia de señal no es suficiente
- **Balance**: Existe un β óptimo según las condiciones del enlace

❌ **Error #4: Olvidar que el umbral depende del demodulador**
- **Discriminador convencional**: Umbral ≈ 10 dB
- **PLL**: Umbral ≈ 7 dB
- **Demodulador con realimentación**: Umbral ≈ 4-5 dB
- **En examen**: Especificar qué tipo de demodulador se está considerando

❌ **Error #5: No considerar el umbral en el diseño**
- **Consecuencia**: Sistema funciona bien en laboratorio (alta señal) pero falla en campo (señal variable)
- **Diseño correcto**: Calcular worst-case SNR y asegurar margen de 2-3 dB sobre el umbral

### ✅ Puntos Clave para Recordar

#### Conceptos Fundamentales

- ✓ **Umbral ≈ 10 dB SNR entrada**: Por debajo, FM colapsa súbitamente
- ✓ **Causa: saltos de fase 2π**: Cuando ruido domina, la fase gira aleatoriamente
- ✓ **Clicks de ruido**: Saltos de fase suenan como pulsos impulsivos
- ✓ **PLL reduce umbral ~3 dB**: Técnica común para mejorar desempeño
- ✓ **Sobre umbral FM es superior, bajo umbral es inferior a AM**: Trade-off clave

#### Fórmulas Esenciales

**Ganancia FM (solo sobre umbral)**:
$$SNR_{salida} = 3\beta^2(\beta+1) \cdot SNR_{entrada}$$

**Tasa de clicks (aproximada)**:
$$\lambda_{clicks} \approx \frac{BW}{\pi}\exp(-SNR)$$

**Umbral típico**:
$$SNR_{umbral} \approx 10 \text{ dB (discriminador)}, \quad 7 \text{ dB (PLL)}$$

#### Reglas Mnemotécnicas

- 🧠 **"10 dB es la frontera"**: Por debajo de 10 dB, FM empieza a colapsar
- 🧠 **"Clicks = Saltos de fase"**: Cada click es un cruce 2π
- 🧠 **"PLL = -3 dB de regalo"**: PLL baja el umbral 3 dB
- 🧠 **"Sobre el cielo, bajo el infierno"**: Sobre umbral = excelente, bajo = terrible

#### Valores Típicos

| Sistema | SNR Típico Operación | Margen sobre Umbral |
|---------|---------------------|---------------------|
| FM broadcast (99.5 MHz) | 20-40 dB | 10-30 dB (muy seguro) |
| FM móvil | 12-25 dB | 2-15 dB (marginal a bueno) |
| Telemetría espacial | 8-15 dB | -2 a 5 dB (usa PLL!) |
| FM analógica TV (obsoleta) | 15-30 dB | 5-20 dB |

### 📚 Para Profundizar

#### Recursos Recomendados

- **Haykin & Moher**: "Communication Systems" (5ta Ed.), Sección 4.8 - Threshold Effect in FM
- **Taub & Schilling**: "Principles of Communication Systems", Capítulo sobre FM noise analysis
- **Carlson**: "Communication Systems" (5th Ed.), Sección 7.4 - Threshold and Clicks
- **Paper clásico**: Rice, S.O. (1944-1945) "Mathematical Analysis of Random Noise", Bell System Technical Journal (base teórica de cruces por cero)

#### Simulaciones Útiles

- **GNU Radio**: Implementar FM demodulator y observar el umbral agregando ruido
- **MATLAB/Simulink**: Communications Toolbox tiene ejemplos de FM threshold
- **Python con scipy.signal**: Simular discriminador y ver clicks

#### Temas Relacionados para Explorar

1. **Demoduladores avanzados**: Feedback demodulators, FMFB (FM Feedback)
2. **Comparación con sistemas digitales**: PSK, FSK no tienen umbral tan marcado
3. **Threshold extension techniques**: Métodos para operar bajo el umbral clásico
4. **Análisis de Rice**: Distribución de envolvente y fase de señal + ruido gaussiano

#### Preguntas para Reflexionar

- ¿Por qué el umbral de FM es súbito mientras que AM degrada gradualmente?
- ¿Existe un índice de modulación β óptimo considerando el umbral?
- ¿Cómo afecta el desvanecimiento del canal al cruce del umbral?
- ¿Por qué las comunicaciones espaciales modernas usan digital en lugar de FM a pesar del mayor ancho de banda de FM?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 - concepto avanzado con análisis no-lineal)
**Tiempo de estudio sugerido**: 45-60 minutos
**Prerequisitos críticos**: FM básica, representación de ruido, fasores
**Tags**: `#FM` `#ruido` `#umbral` `#no-lineal` `#clicks` `#PLL` `#demodulacion`

---

*Generado para el curso de Sistemas de Comunicaciones - UTN*
*Carta 39 de 60 del Mazo de Anki*
