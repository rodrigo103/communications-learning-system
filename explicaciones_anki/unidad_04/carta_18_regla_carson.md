# Carta 18: La Regla de Carson para Ancho de Banda en FM

> **Unidad 4**: Modulación Exponencial

---

## 🎯 Pregunta

¿Qué establece la Regla de Carson para FM y cuál es su interpretación?

---

## 📝 Respuesta Breve (de la carta original)

La **Regla de Carson** estima el ancho de banda de una señal FM:
$$BW ≈ 2(\Delta f + f_m) = 2f_m(\beta + 1)$$

**Interpretación**:
- Incluye el 98% de la potencia de la señal
- Considera la desviación de frecuencia más el ancho de banda de la moduladora
- Es una aproximación práctica (el espectro FM teóricamente es infinito)
- Útil para diseño de sistemas y asignación de espectro

**Ejemplo**: FM broadcast
- $f_m$ = 15 kHz, $\Delta f$ = 75 kHz
- $BW$ ≈ 2(75 + 15) = 180 kHz
- En práctica se asignan 200 kHz por canal

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

La **Regla de Carson** es una de las herramientas más prácticas en ingeniería de comunicaciones FM. Propuesta por John Renshaw Carson en 1928 en los Laboratorios Bell, resuelve un problema fundamental: aunque el espectro FM es teóricamente infinito (infinitas bandas laterales), necesitamos una estimación práctica del ancho de banda para diseño de sistemas y asignación espectral.

**¿Por qué es importante este concepto?** Sin la Regla de Carson, sería imposible planificar sistemas FM prácticos. Los organismos reguladores (FCC, ITU) la usan para asignar espectro, los ingenieros para diseñar filtros, y los fabricantes para especificar equipos. Es el puente entre la teoría matemática compleja (funciones de Bessel) y la implementación práctica.

**¿Dónde se aplica?** En TODOS los sistemas FM: radiodifusión comercial (88-108 MHz), comunicaciones móviles, enlaces satelitales, telemetría espacial, radioaficionados. Cada vez que se diseña un canal FM o se calcula la separación entre portadoras, la Regla de Carson es la herramienta principal.

**Historia relevante:** Carson desarrolló esta regla empíricamente analizando el espectro de señales FM reales. Descubrió que aunque teóricamente hay infinitas componentes, el 98% de la potencia está contenida en un ancho de banda finito y predecible. Este hallazgo fue crucial para hacer FM comercialmente viable.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Espectro de señales FM (funciones de Bessel)
- Índice de modulación β (Carta 17)
- Concepto de potencia contenida en banda
- Densidad espectral de potencia

#### Desarrollo Paso a Paso

**Paso 1: El problema fundamental**

Una señal FM con modulación sinusoidal tiene espectro:
$$S_{FM}(f) = \sum_{n=-\infty}^{\infty} J_n^2(\beta) \cdot \delta(f - f_c - nf_m)$$

Teóricamente, existen infinitas componentes espectrales en $f_c ± nf_m$ con amplitudes dadas por funciones de Bessel $J_n(\beta)$.

**Problema**: ¿Cuántas componentes debemos considerar en la práctica?

**Paso 2: Análisis de potencia contenida**

La potencia total de la señal FM es:
$$P_{total} = A_c^2/2 = \text{constante (independiente de β)}$$

La potencia en las primeras N bandas laterales es:
$$P_N = \frac{A_c^2}{2}\left[J_0^2(\beta) + 2\sum_{n=1}^{N} J_n^2(\beta)\right]$$

Carson descubrió empíricamente que para contener ≈98% de la potencia:
$$N \approx \beta + 1$$

**Paso 3: Formulación de la Regla de Carson**

El ancho de banda que contiene las componentes significativas es:

Para NBFM (β < 1):
- Componentes significativas: $f_c$, $f_c ± f_m$
- BW ≈ 2$f_m$

Para WBFM (β ≫ 1):
- Componentes significativas hasta: $f_c ± \beta f_m$
- BW ≈ 2β$f_m$ = 2Δf

**Regla unificada**:
$$BW_{Carson} = 2(\Delta f + f_m) = 2f_m(\beta + 1)$$

Esta fórmula funciona para TODO valor de β.

#### Derivación Matemática: Justificación del 98%

**Propiedad de las funciones de Bessel**:

Para argumento grande (β ≫ 1):
$$J_n(\beta) \approx 0 \text{ para } |n| > \beta$$

La potencia contenida en $|n| ≤ \beta + 1$ es:
$$\frac{P_{contenida}}{P_{total}} = J_0^2(\beta) + 2\sum_{n=1}^{\lfloor\beta+1\rfloor} J_n^2(\beta)$$

**Verificación numérica**:

| β | Bandas (Carson) | Potencia contenida |
|---|-----------------|-------------------|
| 0.5 | 2 | 99.0% |
| 1.0 | 2 | 98.4% |
| 2.0 | 3 | 98.2% |
| 5.0 | 6 | 98.0% |
| 10.0 | 11 | 98.1% |

La regla mantiene ~98% consistentemente.

### 🔬 Intuición y Analogías

**Analogía de la campana de Gauss:**

Imagina el espectro FM como una distribución donde la energía se concentra cerca del centro y decae hacia los extremos:
- El "ancho" de esta distribución es proporcional a la desviación de frecuencia Δf
- Pero siempre necesitas al menos el ancho de la información original (fm)
- Carson suma ambos: lo que "esparce" la modulación (Δf) + lo mínimo necesario (fm)

**Intuición física del factor 2:**

El factor 2 en la fórmula representa las dos bandas laterales (superior e inferior). La señal se extiende simétricamente alrededor de fc:
- Banda lateral inferior: fc - (Δf + fm)
- Banda lateral superior: fc + (Δf + fm)
- Total: 2(Δf + fm)

**Visualización práctica:**

Piensa en FM como "vibración" de la frecuencia:
- La frecuencia oscila entre fc - Δf y fc + Δf
- Pero cada oscilación genera sus propias bandas laterales de ancho fm
- El ancho total combina ambos efectos

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Diseño de Canal para Radio FM Comercial

**Situación:** Calcular requisitos espectrales para estación FM estéreo

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Audio máximo | 15 | kHz |
| Desviación estándar | 75 | kHz |
| Portadora | 99.5 | MHz |

**Solución paso a paso:**

1. **Índice de modulación:**
   $$\beta = \frac{75 \text{ kHz}}{15 \text{ kHz}} = 5$$

2. **Aplicando Regla de Carson:**
   $$BW = 2(75 + 15) = 180 \text{ kHz}$$

3. **Consideraciones prácticas:**
   - BW teórico: 180 kHz
   - Asignación FCC: 200 kHz
   - Margen de guarda: 20 kHz (10%)

4. **Rango de frecuencias ocupado:**
   - Límite inferior: 99.5 - 0.09 = 99.41 MHz
   - Límite superior: 99.5 + 0.09 = 99.59 MHz

**Interpretación:** Los 200 kHz asignados proporcionan margen para tolerancias del transmisor y deriva de frecuencia.

---

#### Ejemplo 2: Comparación con Cálculo Exacto usando Bessel

**Contexto:** Verificar precisión de Carson para diferentes valores de β

**Sistema con fm = 1 kHz, variando Δf:**

| Δf (kHz) | β | BW Carson | Componentes >1% | BW real (99%) | Error |
|----------|---|-----------|-----------------|---------------|-------|
| 0.5 | 0.5 | 3 kHz | 3 | 3 kHz | 0% |
| 1 | 1 | 4 kHz | 4 | 4 kHz | 0% |
| 5 | 5 | 12 kHz | 8 | 16 kHz | -25% |
| 10 | 10 | 22 kHz | 13 | 26 kHz | -15% |

**Observación:** Carson es conservador (subestima) para β grande, pero el error es aceptable para diseño.

---

#### Ejemplo 3: Aplicación en Comunicaciones Satelitales

**¿Qué pasa con modulación de datos digitales?**

**Sistema BPSK sobre FM (telemetría espacial):**
- Datos: 10 kbps (rectangular)
- Componente fundamental: 5 kHz
- Desviación pico: ±20 kHz

**Análisis con Carson:**

1. **Para componente fundamental (5 kHz):**
   $$\beta_1 = 20/5 = 4$$
   $$BW_1 = 2(20 + 5) = 50 \text{ kHz}$$

2. **Considerando armónicos (3×5 = 15 kHz):**
   $$\beta_3 = 20/15 = 1.33$$
   $$BW_3 = 2(20 + 15) = 70 \text{ kHz}$$

3. **BW total recomendado:**
   70 kHz para incluir tercer armónico

**Verificación práctica:** Mediciones reales muestran 95% de potencia en 65 kHz, validando Carson.

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Índice de modulación** (Carta 17): β es entrada clave para Carson
- **NBFM vs WBFM** (Carta 17): Carson unifica ambos casos
- **Comparación FM vs AM** (Carta 41): Carson cuantifica penalty de BW
- **Ruido en FM** (Carta 39): BW de Carson define BW de ruido

#### Dependencias (lo que necesitas saber primero)
1. Concepto de ancho de banda → Para entender qué estima Carson
2. Desviación de frecuencia → Parámetro clave Δf
3. Espectro de líneas → FM produce espectro discreto

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Planificación de frecuencias**: Separación entre canales
2. **Diseño de filtros**: BW de filtro IF en receptores
3. **Link budget**: Cálculo de densidad espectral de potencia

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- Carson NO es exacta, es una aproximación práctica del 98%
- La fórmula funciona para TODO β (NBFM y WBFM)
- El factor 2 representa las DOS bandas laterales
- Para β→0, Carson→2fm (como AM)
- Para β→∞, Carson→2Δf (dominado por desviación)

#### Tipos de problemas típicos
1. **Cálculo directo**: Dado β y fm, hallar BW
   - Estrategia: Aplicar fórmula directamente

2. **Diseño inverso**: Dado BW disponible, hallar Δf máximo
   - Estrategia: Despejar Δf de la ecuación de Carson

3. **Comparación de sistemas**: FM vs otros, usando Carson para FM
   - Estrategia: Calcular eficiencia espectral relativa

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Olvidar el factor 2**
- Por qué ocurre: Pensar solo en desviación unilateral
- Cómo evitarlo: Recordar que FM tiene DOS bandas laterales
- Ejemplo: BW ≠ Δf + fm, es 2(Δf + fm)

❌ **Error #2: Confundir 98% con 100%**
- Por qué ocurre: Pensar que Carson da BW total
- Realidad: Siempre hay potencia residual fuera
- Implicación: Necesitas márgenes adicionales en diseño

❌ **Error #3: Aplicar Carson a modulación no sinusoidal sin cuidado**
- Por qué ocurre: Carson se deriva para tono único
- Para señales complejas: Usar fm = frecuencia máxima de la moduladora
- Mejor práctica: Verificar con simulación para moduladoras complejas

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
Regla de Carson: BW = 2(Δf + fm) = 2fm(β + 1)
Casos límite:
  β → 0: BW → 2fm (como AM)
  β → ∞: BW → 2Δf (dominado por desviación)
Potencia contenida: ~98%
```

#### Conceptos Fundamentales
- ✓ **Carson es empírica**: Basada en observación, no derivación rigurosa
- ✓ **98% es suficiente**: El 2% restante es despreciable en la práctica
- ✓ **Unifica NBFM y WBFM**: Una fórmula para todos los casos

#### Reglas Mnemotécnicas
- 🧠 **"Carson = 2 × (Desviación + Moduladora)"**: Fácil de recordar
- 🧠 **"98 no 100"**: Carson da 98%, no 100% de potencia
- 🧠 **"Beta más uno, multiplicado por dos fm"**: Forma alternativa

#### Valores Típicos (para referencias rápidas)

| Sistema | Δf | fm | BW Carson | BW Asignado |
|---------|----|----|-----------|-------------|
| FM Broadcast | 75 kHz | 15 kHz | 180 kHz | 200 kHz |
| TV Audio | 25 kHz | 15 kHz | 80 kHz | 100 kHz |
| Narrow FM | 5 kHz | 3 kHz | 16 kHz | 25 kHz |
| Satelital | 10 kHz | 4 kHz | 28 kHz | 36 kHz |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Paper original**: J.R. Carson, "Notes on the Theory of Modulation" (1922)
- **Libros**: Carlson Cap. 5.3, Haykin Cap. 4.7
- **Simulaciones**: GNU Radio para verificar Carson experimentalmente

#### Temas Relacionados para Explorar
1. Reglas alternativas (99% de potencia, criterio de -40 dB)
2. Carson para FM estéreo con subportadoras
3. Ancho de banda en modulación digital FSK

#### Preguntas para Reflexionar
- ¿Por qué 98% y no 95% o 99%?
- ¿Cómo cambiaría Carson para modulación exponencial generalizada?
- ¿Es Carson óptima para asignación espectral moderna?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐ (3/5 estrellas)
**Tiempo de estudio sugerido**: 20 minutos
**Prerequisitos críticos**: Índice de modulación, espectro FM, concepto de ancho de banda
**Tags**: `#FM` `#regla-carson` `#ancho-banda` `#diseño-espectral`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*