# Carta 37: Ruido de Banda Angosta - Análisis en Componentes I-Q

> **Unidad 7**: Ruido en Sistemas de Comunicaciones

---

## 🎯 Pregunta

¿Qué es el ruido de banda angosta y cómo se representa matemáticamente?

---

## 📝 Respuesta Breve (de la carta original)

El **ruido de banda angosta** es ruido blanco filtrado a un ancho de banda pequeño centrado en una frecuencia.

**Representación**:
$$n(t) = x(t)\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)$$

donde:
- $x(t)$ = componente en fase (in-phase)
- $y(t)$ = componente en cuadratura
- Ambas son procesos gaussianos, media cero, idéntica varianza

**Representación alternativa** (envolvente-fase):
$$n(t) = R(t)\cos[2\pi f_c t + \phi(t)]$$

donde:
- $R(t)$ = envolvente (distribución de Rayleigh)
- $\phi(t)$ = fase (distribución uniforme)

**Uso**: analizar efectos del ruido en receptores AM, FM, etc.

---

## 📖 Explicación Detallada

### 🔍 Introducción y Contexto

El ruido de banda angosta es un concepto fundamental para entender cómo el ruido afecta a las señales moduladas. Cuando el ruido blanco pasa por los filtros selectivos de un receptor, se convierte en ruido de banda angosta centrado alrededor de la frecuencia de la portadora. Este modelo es esencial para analizar el rendimiento de todos los sistemas de comunicaciones con portadora.

**¿Por qué es importante este concepto?**
- Permite **analizar matemáticamente** el efecto del ruido en señales moduladas
- Es la base para calcular **SNR de salida** en detectores AM y FM
- Explica fenómenos como el **efecto umbral** en demodulación
- Fundamental para entender la **detección coherente vs. envolvente**

**¿Dónde se aplica?**
- **Receptores AM/FM**: análisis de calidad de audio
- **Comunicaciones digitales**: cálculo de probabilidad de error
- **Sistemas de radar**: detección de blancos en ruido
- **Enlaces satelitales**: análisis de degradación por ruido
- **Instrumentación RF**: caracterización de sensibilidad

**Desarrollo histórico:** El análisis del ruido de banda angosta fue desarrollado por S.O. Rice en los laboratorios Bell en la década de 1940, proporcionando las herramientas matemáticas para el diseño moderno de receptores.

### 📐 Fundamentos Teóricos

#### Conceptos Prerequisitos
- Ruido blanco gaussiano
- Filtrado de señales aleatorias
- Representación de señales en cuadratura
- Distribuciones de probabilidad (Gaussiana, Rayleigh, uniforme)

#### Desarrollo Paso a Paso

**Paso 1: Origen del ruido de banda angosta**

Cuando el ruido blanco (espectro plano) pasa por un filtro pasabanda centrado en $f_c$:
- El espectro resultante está limitado a $f_c ± B/2$
- Si $B << f_c$, tenemos ruido de "banda angosta"
- El ruido resultante "parece" una portadora con amplitud y fase aleatorias

**Paso 2: Necesidad de representación especial**

El ruido de banda angosta oscila rápidamente cerca de $f_c$, pero su amplitud y fase varían lentamente. Necesitamos una representación que capture esta estructura.

**Paso 3: Descomposición en cuadratura**

Cualquier señal de banda angosta puede expresarse como la suma de dos componentes ortogonales moduladas en cuadratura.

#### Derivación Matemática

**Partiendo del ruido filtrado:**

Sea $n(t)$ ruido blanco gaussiano filtrado por un filtro pasabanda ideal:

$$H(f) = \begin{cases}
1 & |f - f_c| < B/2 \\
0 & \text{otro caso}
\end{cases}$$

**Representación en componentes I-Q:**

Podemos escribir:
$$n(t) = x(t)\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)$$

donde $x(t)$ e $y(t)$ se obtienen por:

$$x(t) = 2 \cdot \text{LPF}[n(t) \cos(2\pi f_c t)]$$
$$y(t) = 2 \cdot \text{LPF}[n(t) \sin(2\pi f_c t)]$$

**Propiedades estadísticas:**

Para ruido gaussiano de banda angosta:
1. $x(t)$ e $y(t)$ son procesos gaussianos
2. $E[x(t)] = E[y(t)] = 0$ (media cero)
3. $\sigma_x^2 = \sigma_y^2 = \sigma_n^2$ (misma varianza que $n(t)$)
4. $x(t)$ e $y(t)$ son independientes en cada instante $t$

**Representación polar:**

Definiendo:
$$R(t) = \sqrt{x^2(t) + y^2(t)}$$
$$\phi(t) = \arctan\left(\frac{y(t)}{x(t)}\right)$$

Entonces:
$$n(t) = R(t)\cos[2\pi f_c t + \phi(t)]$$

**Distribuciones resultantes:**

$$\boxed{p_R(r) = \frac{r}{\sigma^2}\exp\left(-\frac{r^2}{2\sigma^2}\right), \quad r \geq 0}$$ (Rayleigh)

$$\boxed{p_\phi(\phi) = \frac{1}{2\pi}, \quad 0 \leq \phi < 2\pi}$$ (Uniforme)

### 🔬 Intuición y Analogías

**Analogía de las olas del mar:**

Imagina observar las olas del océano desde un muelle:
- Las olas tienen una frecuencia dominante (como $f_c$)
- La altura de las olas varía aleatoriamente (como $R(t)$)
- El momento exacto en que llega cada cresta es aleatorio (como $\phi(t)$)
- Si miras por un tiempo, la altura sigue una distribución de Rayleigh

**Intuición física:**

El ruido de banda angosta es como una portadora "ruidosa":
- Oscila cerca de una frecuencia central
- Su amplitud fluctúa aleatoriamente (envolvente de Rayleigh)
- Su fase es completamente aleatoria (uniforme)
- Las fluctuaciones son lentas comparadas con la frecuencia de la portadora

**Visualización en el dominio del tiempo:**

```
Señal pura:    ━━━━━━━━━━━━━━━━━━━━━
               Amplitud constante

Ruido B.A.:    ∿∿∿⁓⁓≈≈∿∿∿⁓⁓⁓≈≈∿∿∿
               Envolvente variable
```

### 💡 Ejemplos Prácticos

#### Ejemplo 1: Análisis de Ruido en Receptor AM

**Situación:** Receptor AM sintonizado a 1 MHz con filtro IF de 10 kHz de ancho de banda

**Datos:**

| Parámetro | Valor | Unidades |
|-----------|-------|----------|
| Frecuencia central | 1.0 | MHz |
| Ancho de banda | 10 | kHz |
| Potencia de ruido | -100 | dBm |
| Impedancia | 50 | Ω |

**Análisis del ruido:**

1. **Calcular σ del ruido:**
   $$P_n = -100 \text{ dBm} = 10^{-13} \text{ W}$$
   $$\sigma^2 = \frac{P_n \cdot R}{2} = \frac{10^{-13} \times 50}{2} = 2.5 \times 10^{-12}$$
   $$\sigma = 1.58 \times 10^{-6} \text{ V}$$

2. **Componentes I-Q:**
   - $\sigma_x = \sigma_y = 1.58 \mu V$
   - Ancho de banda de $x(t)$ e $y(t)$: 5 kHz cada uno

3. **Distribución de la envolvente:**
   - Valor más probable: $R_{mp} = \sigma = 1.58 \mu V$
   - Valor medio: $E[R] = \sigma\sqrt{\pi/2} = 1.98 \mu V$
   - Probabilidad de $R > 3\sigma$:
   $$P(R > 3\sigma) = \exp(-9/2) = 0.011$$ (1.1%)

**Interpretación:** El ruido aparece como una portadora de 1 MHz con envolvente fluctuante de ~2 μV típicamente.

---

#### Ejemplo 2: Comparación Ruido Banda Angosta vs. Banda Ancha

**Contexto:** Sistema de comunicaciones con dos configuraciones de filtrado

**Configuración A - Banda Angosta:**
- $f_c = 100$ MHz
- $B = 1$ MHz
- $B/f_c = 0.01$ (1%)

**Configuración B - Banda Ancha:**
- $f_c = 100$ MHz
- $B = 20$ MHz
- $B/f_c = 0.20$ (20%)

**Análisis comparativo:**

| Propiedad | Banda Angosta (A) | Banda Ancha (B) |
|-----------|-------------------|-----------------|
| Validez aproximación I-Q | Excelente | Marginal |
| Fluctuación envolvente | Lenta (~1 MHz) | Rápida (~20 MHz) |
| Distribución envolvente | Rayleigh precisa | Rayleigh aproximada |
| Correlación temporal | Alta (τ ~ 1 μs) | Baja (τ ~ 50 ns) |
| Análisis matemático | Simple | Complejo |

**Espectro de las componentes:**
- **Banda angosta:** $x(t)$, $y(t)$ tienen espectro de 0 a 0.5 MHz
- **Banda ancha:** $x(t)$, $y(t)$ tienen espectro de 0 a 10 MHz

---

#### Ejemplo 3: Efecto en Detección de Señales

**¿Cómo afecta el ruido de banda angosta a una señal AM?**

**Señal AM + Ruido:**
$$r(t) = [A_c + m(t) + x(t)]\cos(2\pi f_c t) - y(t)\sin(2\pi f_c t)$$

**Envolvente detectada:**
$$R(t) = \sqrt{[A_c + m(t) + x(t)]^2 + y^2(t)}$$

**Casos límite:**

1. **SNR alta** ($A_c >> \sigma$):
   $$R(t) \approx A_c + m(t) + x(t)$$
   - Solo la componente en fase del ruido afecta
   - Ruido aditivo simple

2. **SNR baja** ($A_c << \sigma$):
   $$R(t) \approx \sqrt{x^2(t) + y^2(t)} = R_n(t)$$
   - Señal perdida en el ruido
   - Envolvente sigue distribución de Rayleigh

3. **SNR intermedia** ($A_c \approx \sigma$):
   - Distribución de Rice
   - Transición no lineal
   - Aparece efecto umbral

### 🔗 Conexiones con Otros Conceptos

#### Conceptos Relacionados (del mismo curso)
- **Efecto del ruido en AM** (Carta 38): Usa este modelo para análisis
- **Efecto umbral en FM** (Carta 39): También basado en ruido de banda angosta
- **Detección coherente**: Explota conocimiento de componentes I-Q
- **Ruido blanco** (Carta 33): Fuente original antes del filtrado

#### Dependencias (lo que necesitas saber primero)
1. Procesos aleatorios gaussianos
2. Filtrado de señales aleatorias
3. Modulación en cuadratura
4. Transformada de Hilbert (para obtener componentes)

#### Aplicaciones Posteriores (dónde usarás esto)
1. **Análisis de BER**: En sistemas digitales con ruido
2. **Diseño de detectores**: Óptimos para diferentes SNR
3. **Simulación de sistemas**: Modelado preciso del ruido

### 🎓 Perspectiva de Examen

#### Lo que el profesor busca que entiendas
- La diferencia entre representación I-Q y envolvente-fase
- Por qué la envolvente sigue distribución de Rayleigh
- Que las componentes I-Q son gaussianas independientes
- La condición de banda angosta: $B << f_c$
- Cómo se obtienen las componentes mediante demodulación

#### Tipos de problemas típicos
1. **Calcular estadísticas**: Dada potencia de ruido, hallar σ de componentes
   - Estrategia: $\sigma_x = \sigma_y = \sigma_n$

2. **Distribuciones**: Probabilidades de envolvente o fase
   - Estrategia: Usar Rayleigh para R, uniforme para φ

3. **Efecto en modulaciones**: SNR de salida con ruido de banda angosta
   - Estrategia: Separar análisis para componentes I y Q

### ⚠️ Errores Comunes y Trampas

❌ **Error #1: Confundir varianza de componentes con varianza total**
- Por qué ocurre: La potencia se divide entre I y Q
- Cómo evitarlo: $\sigma_x^2 + \sigma_y^2 = \sigma_n^2$ (no $2\sigma_n^2$)
- Verificación: La potencia total se conserva

❌ **Error #2: Asumir que R(t) es gaussiana**
- Por qué ocurre: x(t) e y(t) son gaussianas
- Cómo evitarlo: R es Rayleigh (módulo de dos gaussianas)
- Recordar: Solo las componentes son gaussianas, no la envolvente

❌ **Error #3: Aplicar modelo a banda ancha**
- Por qué ocurre: Generalización incorrecta
- Cómo evitarlo: Verificar $B/f_c < 0.1$ aproximadamente
- Consecuencia: Modelo I-Q no es válido para banda ancha

### ✅ Puntos Clave para Recordar

#### Fórmulas Esenciales
```
n(t) = x(t)cos(ωct) - y(t)sin(ωct)     [Representación I-Q]
n(t) = R(t)cos(ωct + φ(t))             [Representación polar]
σx² = σy² = σn²                         [Varianzas iguales]
pR(r) = (r/σ²)exp(-r²/2σ²)             [Distribución Rayleigh]
```

#### Conceptos Fundamentales
- ✓ **Banda angosta**: B << fc (típicamente B/fc < 0.1)
- ✓ **Componentes I-Q**: Gaussianas, independientes, misma varianza
- ✓ **Envolvente**: Distribución de Rayleigh
- ✓ **Fase**: Distribución uniforme en [0, 2π]

#### Reglas Mnemotécnicas
- 🧠 **"IQ-GI"**: I-Q son Gaussianas Independientes
- 🧠 **"RAF"**: Rayleigh-Amplitude, Flat-phase (uniforme)
- 🧠 **"Narrow needs Nice"**: Banda angosta necesita B << fc

#### Valores y Relaciones Típicas

| Parámetro | Valor/Relación |
|-----------|----------------|
| Condición banda angosta | B/fc < 0.1 |
| Media de Rayleigh | E[R] = σ√(π/2) ≈ 1.25σ |
| Moda de Rayleigh | Rmp = σ |
| Varianza de Rayleigh | Var[R] = σ²(2-π/2) |
| P(R > 3σ) | ≈ 1.1% |

### 📚 Para Profundizar

#### Recursos Recomendados
- **Libros de texto**:
  - Carlson, "Communication Systems", Cap. 8
  - Haykin, "Communication Systems", Cap. 9
  - Papoulis, "Probability, Random Variables", Cap. 10
- **Paper clásico**: S.O. Rice, "Mathematical Analysis of Random Noise", BSTJ, 1944
- **Simulaciones**: MATLAB Communications Toolbox para visualización

#### Temas Relacionados para Explorar
1. Distribución de Rice (señal + ruido)
2. Procesos de banda angosta no gaussianos
3. Ruido cicloestacionario en comunicaciones
4. Expansión de Edgeworth para no-gaussianidad

#### Preguntas para Reflexionar
- ¿Qué pasa cuando el filtro no es simétrico respecto a fc?
- ¿Cómo cambia el análisis para ruido no blanco?
- ¿Por qué la fase es uniforme incluso si el filtro no es ideal?
- ¿Cómo se extiende a señales complejas en banda base?

---

## 🏷️ Metadatos de la Carta

**Dificultad**: ⭐⭐⭐⭐ (4/5 estrellas)
**Tiempo de estudio sugerido**: 25 minutos
**Prerequisitos críticos**: Procesos aleatorios, filtrado, modulación I-Q
**Tags**: `#ruido-banda-angosta` `#componentes-IQ` `#rayleigh` `#deteccion` `#receptor`

---

*Generado el: 2025-11-16*
*Última revisión: 2025-11-16*